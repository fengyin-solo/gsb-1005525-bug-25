"""各业务模块 service 的共同基类。

筛选 → 数总数 → 分页切片只允许按 app.pagination 里的一套算法执行；
导出与列表共用同一个筛选函数，保证“导出条数 == 列表总数”。
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

from app.pagination import PageData, paginate
from app.store import store


class BaseModuleService:
    module: str = ""
    required_fields: list[str] = []
    status_order: list[str] = []
    action_rules: dict[str, str] = {}
    negative_actions: list[str] = []
    list_fields: list[str] = []
    # 模糊检索关键字时匹配的字段（各模块覆盖为自己的编号/名称字段）。
    keyword_fields: list[str] = []
    label: str = ""

    # ---- 筛选：列表与导出唯一共用的口径 ----
    def filtered_rows(
        self,
        *,
        keyword: str | None = None,
        status: str | None = None,
        filters: dict[str, str] | None = None,
    ) -> list[dict[str, Any]]:
        rows = store.rows(self.module)
        if keyword:
            kw = keyword.strip()
            if kw:
                rows = [
                    row for row in rows
                    if any(kw in str(row.get(field, "")) for field in self.keyword_fields)
                ]
        if status:
            rows = [row for row in rows if row.get("status") == status]
        for field, value in (filters or {}).items():
            value = (value or "").strip()
            if not value:
                continue
            rows = [row for row in rows if value in str(row.get(field, ""))]
        # 登记时间从早到晚、同时间按 id，保证列表与导出顺序稳定一致。
        return sorted(rows, key=lambda row: (str(row.get("created_at", "")), int(row.get("id", 0))))

    def list_entries(self, query: Any) -> PageData:
        """列表：先按当前条件取全量，再交统一分页口径数总数、切片、校正页码。"""
        matched = self.filtered_rows(
            keyword=query.keyword, status=query.status, filters=query.filters
        )
        return paginate(matched, page=query.page, size=query.size, client_total=query.total)

    def export_entries(self, query: Any) -> dict[str, Any]:
        """导出：按当前条件取全量（不分页），条数即列表总数，结果落库。

        导出没有页码语义，page/size 只随请求体透传、不参与截断；唯一需要提示的是
        请求携带的缓存总数与当前条件实算总数冲突，此时与列表一样以接口总数为准。
        """
        filters = {"keyword": query.keyword, "status": query.status, "filters": query.filters}
        matched = self.filtered_rows(
            keyword=query.keyword, status=query.status, filters=query.filters
        )
        total = len(matched)
        notice = ""
        if query.total is not None and int(query.total) != total:
            notice = (
                f"请求携带的总数 {query.total} 与当前条件下的实际总数 {total} 不一致，"
                f"导出条数以接口口径的 {total} 为准"
            )
        record = store.save_export(module=self.module, items=matched, filters=filters)
        return {
            "module": self.module,
            "total": total,
            "items": matched,
            "export_id": record["id"],
            "created_at": record["created_at"],
            "notice": notice,
        }

    # ---- 单条与登记/动作：沿用各模块原有业务规则 ----
    def get_entry(self, entry_id: int) -> dict[str, Any] | None:
        return store.find(self.module, entry_id)

    def create_entry(self, values: dict[str, Any]) -> tuple[dict[str, Any] | None, list[str]]:
        missing = [field for field in self.required_fields if not str(values.get(field) or "").strip()]
        if missing:
            return None, missing
        rows = store.rows(self.module)
        entry = {"id": max((int(row.get("id", 0)) for row in rows), default=0) + 1}
        entry.update({field: values.get(field) for field in self.required_fields})
        entry["status"] = self.status_order[0]
        entry["pending"] = True
        entry["abnormal"] = False
        entry["created_at"] = datetime.now().replace(microsecond=0).isoformat()
        rows.append(entry)
        return entry, []

    def run_action(self, entry_id: int, action: str) -> tuple[dict[str, Any] | None, str]:
        entry = store.find(self.module, entry_id)
        if entry is None:
            return None, f"{self.label} {entry_id} 不存在或已归档"
        if action not in self.action_rules:
            return None, f"动作「{action}」不属于{self.label}可执行范围"
        target = self.action_rules[action]
        if target not in self.status_order:
            return None, f"目标状态「{target}」不在允许的状态序列里"
        entry["status"] = target
        entry["pending"] = target != self.status_order[-1]
        entry["abnormal"] = action in self.negative_actions
        return entry, f"{self.label}已{action}"

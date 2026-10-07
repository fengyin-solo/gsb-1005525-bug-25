"""业务服务基类：列表、导出、登记、状态流转的通用实现。

各模块服务只声明自己的常量（模块名、字段、状态序列、动作规则），
筛选与分页口径全部走 app.listing 这一套，不再每个模块各写一遍。
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, ClassVar

from app.listing import PageData, apply_filters, paginate, sort_rows
from app.store import store


class BaseService:
    MODULE: ClassVar[str]  # 数据表名
    ENTRY_LABEL: ClassVar[str]  # 单条记录的称谓，用于提示语
    SCOPE_LABEL: ClassVar[str]  # 模块的称谓，用于动作范围提示
    KEYWORD_FIELD: ClassVar[str]  # 关键字检索命中的字段
    REQUIRED_FIELDS: ClassVar[list[str]]
    STATUS_ORDER: ClassVar[list[str]]
    ACTION_RULES: ClassVar[dict[str, str]]
    NEGATIVE_ACTIONS: ClassVar[list[str]] = []

    def _filtered_rows(
        self,
        *,
        keyword: str | None = None,
        status: str | None = None,
        order: str = "desc",
    ) -> list[dict[str, Any]]:
        """筛选 + 排序：列表和导出共用这一段，保证两边是同一份数据。"""
        rows = apply_filters(
            store.rows(self.MODULE),
            keyword=keyword,
            keyword_field=self.KEYWORD_FIELD,
            status=status,
        )
        return sort_rows(rows, order)

    def list_entries(
        self,
        *,
        keyword: str | None = None,
        status: str | None = None,
        page: int = 1,
        size: int = 20,
        order: str = "desc",
    ) -> PageData:
        rows = self._filtered_rows(keyword=keyword, status=status, order=order)
        return paginate(rows, page=page, size=size)

    def export_entries(
        self,
        *,
        keyword: str | None = None,
        status: str | None = None,
        order: str = "desc",
    ) -> tuple[list[dict[str, Any]], int]:
        """导出按当前条件取全量：与列表走同一段筛选，条数天然同一份口径。"""
        rows = self._filtered_rows(keyword=keyword, status=status, order=order)
        return rows, len(rows)

    def get_entry(self, entry_id: int) -> dict[str, Any] | None:
        return store.find(self.MODULE, entry_id)

    def create_entry(self, values: dict[str, Any]) -> tuple[dict[str, Any] | None, list[str]]:
        missing = [field for field in self.REQUIRED_FIELDS if not str(values.get(field) or "").strip()]
        if missing:
            return None, missing
        rows = store.rows(self.MODULE)
        entry = {"id": max((int(row.get("id", 0)) for row in rows), default=0) + 1}
        entry.update({field: values.get(field) for field in self.REQUIRED_FIELDS})
        entry["status"] = self.STATUS_ORDER[0]
        entry["pending"] = True
        entry["abnormal"] = False
        entry["created_at"] = datetime.now().isoformat(timespec="seconds")
        rows.append(entry)
        return entry, []

    def run_action(self, entry_id: int, action: str) -> tuple[dict[str, Any] | None, str]:
        entry = store.find(self.MODULE, entry_id)
        if entry is None:
            return None, f"{self.ENTRY_LABEL} {entry_id} 不存在或已归档"
        if action not in self.ACTION_RULES:
            return None, f"动作「{action}」不属于{self.SCOPE_LABEL}可执行范围"
        target = self.ACTION_RULES[action]
        if target not in self.STATUS_ORDER:
            return None, f"目标状态「{target}」不在允许的状态序列里"
        entry["status"] = target
        entry["pending"] = target != self.STATUS_ORDER[-1]
        entry["abnormal"] = action in self.NEGATIVE_ACTIONS
        return entry, f"{self.ENTRY_LABEL}已{action}"

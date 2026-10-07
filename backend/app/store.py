"""内存数据仓库：给每个业务模块准备一份可筛选、可流转的示例数据。

真实项目里这里会换成数据库访问层；当前实现只依赖标准库，保证克隆下来就能起。

存量数据没有登记时间：载入种子数据时按登记先后（各模块内 id 顺序）回填
created_at，保证按登记时间排序、分页的口径对老数据同样成立。
"""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from app.seed import SEED_ROWS

# 存量数据回填登记时间的基准：从该时刻起按 id 顺序逐条往后推一小时。
BACKFILL_BASE = datetime(2026, 9, 1, 8, 0, 0)


def _backfill_created_at(rows: list[dict[str, Any]]) -> None:
    """给缺登记时间的存量记录回填 created_at（按 id 顺序，稳定可复现）。"""
    for row in rows:
        if row.get("created_at"):
            continue
        moment = BACKFILL_BASE + timedelta(hours=max(int(row.get("id", 1)) - 1, 0))
        row["created_at"] = moment.isoformat(timespec="seconds")


class Store:
    def __init__(self) -> None:
        self._tables: dict[str, list[dict[str, Any]]] = {
            name: [dict(row) for row in rows] for name, rows in SEED_ROWS.items()
        }
        for rows in self._tables.values():
            _backfill_created_at(rows)
        # 导出落库的记录：独立于业务表，不进模块清单与概览统计。
        self._export_records: list[dict[str, Any]] = []

    def module_names(self) -> list[str]:
        return sorted(self._tables)

    def rows(self, module: str) -> list[dict[str, Any]]:
        return self._tables.setdefault(module, [])

    def find(self, module: str, entry_id: int) -> dict[str, Any] | None:
        for row in self.rows(module):
            if int(row.get("id", 0)) == entry_id:
                return row
        return None

    def record_export(
        self,
        *,
        module: str,
        filters: dict[str, Any],
        items: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """导出结果落库：留下谁都能核对的快照（条件、条数、明细、时间）。"""
        record = {
            "id": len(self._export_records) + 1,
            "module": module,
            "filters": filters,
            "total": len(items),
            "items": [dict(row) for row in items],
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
        self._export_records.append(record)
        return record

    def export_records(self) -> list[dict[str, Any]]:
        return list(self._export_records)

    def overview(self) -> dict[str, object]:
        modules: list[dict[str, object]] = []
        for name in self.module_names():
            rows = self.rows(name)
            modules.append({
                "name": name,
                "created": len(rows),
                "pending": sum(1 for row in rows if row.get("pending")),
                "abnormal": sum(1 for row in rows if row.get("abnormal")),
            })
        cards = [
            {"label": "业务模块", "value": len(modules)},
            {"label": "今日新增", "value": sum(int(item["created"]) for item in modules)},
            {"label": "待处理", "value": sum(int(item["pending"]) for item in modules)},
            {"label": "异常量", "value": sum(int(item["abnormal"]) for item in modules)},
        ]
        return {"cards": cards, "modules": modules}


store = Store()

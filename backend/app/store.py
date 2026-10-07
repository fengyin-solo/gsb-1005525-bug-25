"""内存数据仓库：给每个业务模块准备一份可筛选、可流转的示例数据。

真实项目里这里会换成数据库访问层；当前实现只依赖标准库，保证克隆下来就能起。
两类数据存在这里：
- 业务模块表：存量行在装载时统一按业务日期回填 created_at（登记时间）；
- 导出记录表：每次全量导出都落一份快照，导出条数与列表总数必须来自同一份口径。
"""
from __future__ import annotations

import re
from typing import Any

from app.seed import SEED_ROWS

# 用来识别业务行里的“日期”字段，回填登记时间时按字段名优先级取第一个命中的。
_DATE_FIELD_HINTS = ("登记", "注册", "时间", "日期", "月份", "有效期", "起止", "投运")
_DATE_VALUE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def _row_created_at(row: dict[str, Any], fallback_day: int) -> str:
    """存量数据没有登记时间：按行内登记/业务日期回填，都没有时落到统一的基准时间。"""
    for hint in _DATE_FIELD_HINTS:
        for key, value in row.items():
            if hint in str(key) and isinstance(value, str) and _DATE_VALUE_RE.match(value.strip()):
                return value.strip()
    return f"2026-08-31T00:{fallback_day:02d}:00"


class Store:
    def __init__(self) -> None:
        self._tables: dict[str, list[dict[str, Any]]] = {}
        for name, rows in SEED_ROWS.items():
            table = [dict(row) for row in rows]
            for index, row in enumerate(table):
                row.setdefault("created_at", _row_created_at(row, index + 1))
            self._tables[name] = table
        # 导出记录表：只存库内，不混进业务模块列表与概览统计。
        self._tables["_export_records"] = []

    def module_names(self) -> list[str]:
        return sorted(name for name in self._tables if not name.startswith("_"))

    def rows(self, module: str) -> list[dict[str, Any]]:
        return self._tables.setdefault(module, [])

    def find(self, module: str, entry_id: int) -> dict[str, Any] | None:
        for row in self.rows(module):
            if int(row.get("id", 0)) == entry_id:
                return row
        return None

    def save_export(
        self,
        *,
        module: str,
        items: list[dict[str, Any]],
        filters: dict[str, Any],
    ) -> dict[str, Any]:
        """导出结果落库：快照存的是当前筛选条件下的全量匹配数据。"""
        records = self.rows("_export_records")
        record = {
            "id": max((int(row.get("id", 0)) for row in records), default=0) + 1,
            "module": module,
            "total": len(items),
            "filters": dict(filters),
            "items": [dict(item) for item in items],
            "created_at": _now(),
        }
        records.append(record)
        return record

    def export_records(self) -> list[dict[str, Any]]:
        return list(reversed(self.rows("_export_records")))

    def find_export(self, export_id: int) -> dict[str, Any] | None:
        for row in self.rows("_export_records"):
            if int(row.get("id", 0)) == export_id:
                return row
        return None

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


def _now() -> str:
    from datetime import datetime

    return datetime.now().replace(microsecond=0).isoformat()


store = Store()

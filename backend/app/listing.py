"""列表分页与筛选的统一口径。

所有业务模块的列表接口、导出接口都只走这里的一套算法：
筛选（编号关键字 + 状态）→ 排序（登记时间）→ 分页（先数总数，再校验页码）。

页码、每页条数与总数冲突时，以这里算出的总数为准统一判定：
非法页码回到第一页，并在 notice 里写明原因，由接口返回给前端展示。
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Any

from app.config import settings

ORDER_FIELD = "created_at"  # 登记时间：排序与回填的统一依据
ORDER_CHOICES = ("asc", "desc")


@dataclass
class PageData:
    """一次列表查询的最终结果：页码、每页条数、总数以这份为准。"""

    items: list[dict[str, Any]]
    total: int
    page: int
    size: int
    notice: str | None = None


def apply_filters(
    rows: list[dict[str, Any]],
    *,
    keyword: str | None,
    keyword_field: str,
    status: str | None,
) -> list[dict[str, Any]]:
    """筛选口径：编号关键字模糊匹配 + 状态精确匹配，列表与导出共用。"""
    keyword = (keyword or "").strip()
    if keyword:
        rows = [row for row in rows if keyword in str(row.get(keyword_field, ""))]
    if status:
        rows = [row for row in rows if row.get("status") == status]
    return rows


def sort_rows(rows: list[dict[str, Any]], order: str = "desc") -> list[dict[str, Any]]:
    """翻页顺序：按登记时间排序，id 兜底，保证翻页期间顺序稳定不跳动。"""
    reverse = order != "asc"
    return sorted(
        rows,
        key=lambda row: (str(row.get(ORDER_FIELD) or ""), int(row.get("id", 0))),
        reverse=reverse,
    )


def paginate(rows: list[dict[str, Any]], *, page: int, size: int) -> PageData:
    """分页口径：先数总数，再据此校验页码与每页条数，最后只切一次片。

    非法输入不报错、不静默：回到安全值并在 notice 里写明原因。
    """
    notices: list[str] = []
    if size < 1:
        notices.append(f"每页条数 {size} 非法，已按默认 {settings.page_size_default} 条返回")
        size = settings.page_size_default
    elif size > settings.page_size_max:
        notices.append(f"每页条数 {size} 超过上限 {settings.page_size_max}，已按上限返回")
        size = settings.page_size_max

    total = len(rows)
    max_page = max(1, ceil(total / size))
    if page < 1:
        notices.append(f"页码 {page} 小于 1，已回到第一页")
        page = 1
    elif page > max_page:
        notices.append(f"页码 {page} 超出范围（共 {total} 条、{max_page} 页），已回到第一页")
        page = 1

    start = (page - 1) * size
    return PageData(
        items=rows[start:start + size],
        total=total,
        page=page,
        size=size,
        notice="；".join(notices) or None,
    )

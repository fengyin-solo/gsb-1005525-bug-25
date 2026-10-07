"""统一分页口径。

所有模块的列表接口都只允许走这一套算法，顺序固定为：
1. 按筛选条件取全量匹配行（筛选口径与导出共用，禁止先切片再数总数）；
2. 对这批行只数一次总数 total，分页判定一律以该 total 为准；
3. 依据 total 与每页条数切片，非法页码回到第一页，并在 notice 里写明原因。

调用方（各模块 service）只负责第 1 步的筛选，分页与页码校正全部收口在这里，
避免每个模块各写一遍、最后一页条数对不上。
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from app.config import settings


@dataclass(frozen=True)
class PageData:
    """一次分页的全部结果：切片数据、权威总数、生效页码/每页条数、校正说明。"""

    items: list[dict[str, Any]]
    total: int
    page: int
    size: int
    notice: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "items": self.items,
            "total": self.total,
            "page": self.page,
            "size": self.size,
            "notice": self.notice,
        }


def paginate(
    matched: Sequence[dict[str, Any]],
    *,
    page: int,
    size: int,
    client_total: int | None = None,
) -> PageData:
    """按唯一一套口径分页。

    参数说明：
    - matched：已按当前筛选条件过滤好的全量行，总数以 len(matched) 为唯一权威值；
    - page/size：请求体里带来的页码与每页条数，非法时在这里统一校正；
    - client_total：请求体可能捎带的前端缓存总数；与权威总数冲突时以本函数数出的
      total 为准，并在 notice 里说明。
    """
    notices: list[str] = []

    # 每页条数非法（0、负数或超过上限）时回落到默认值，而不是任由切片越界。
    if size < 1:
        notices.append(f"每页条数 {size} 非法（必须为正整数），已按默认 {settings.page_size_default} 条/页处理")
        size = settings.page_size_default
    elif size > settings.page_size_max:
        notices.append(
            f"每页条数 {size} 超过上限 {settings.page_size_max}，已按上限 {settings.page_size_max} 条/页处理"
        )
        size = settings.page_size_max

    # 总数只在这里数一次，后续页码判定与切片全部使用这一个值。
    total = len(matched)
    if client_total is not None and int(client_total) != total:
        notices.append(
            f"请求携带的总数 {client_total} 与当前条件下的实际总数 {total} 不一致，总数以接口返回的 {total} 为准"
        )

    if page < 1:
        notices.append(f"页码 {page} 非法（页码从 1 开始），已回到第一页")
        page = 1

    # 页码超出最后一页（例如筛选后结果变少、停留在旧页码）时回到第一页，
    # 保证“翻到最后一页时每页条数对不上”的情况不会再出现。
    if total == 0:
        if page != 1:
            notices.append("当前条件下没有匹配数据，已回到第一页")
        page = 1
    else:
        last_page = (total - 1) // size + 1
        if page > last_page:
            notices.append(f"页码 {page} 超出最后一页（共 {last_page} 页），已回到第一页")
            page = 1

    start = (page - 1) * size
    return PageData(
        items=list(matched[start:start + size]),
        total=total,
        page=page,
        size=size,
        notice="；".join(notices),
    )

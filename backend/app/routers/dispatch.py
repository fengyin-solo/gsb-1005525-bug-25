"""调度指令接口：维护调度指令单，覆盖确认执行、完成回复、驳回指令等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.dispatch import DispatchService

router = build_router(
    service=DispatchService(),
    prefix="/api/dispatch",
    tag="调度指令",
    keyword_desc="按指令编号检索",
    status_desc="待执行、执行中、已完成、已驳回",
)

"""巡视检查接口：维护巡视记录，覆盖开始巡视、提交记录、归档记录等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.patrol import PatrolService

router = build_router(
    service=PatrolService(),
    prefix="/api/patrol",
    tag="巡视检查",
    keyword_desc="按记录编号检索",
    status_desc="待巡视、巡视中、已记录、已归档",
)

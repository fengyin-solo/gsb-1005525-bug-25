"""检修计划接口：维护检修计划，覆盖提交审批、开始执行、确认完工等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.maintenance import MaintenanceService

router = build_router(
    service=MaintenanceService(),
    prefix="/api/maintenance",
    tag="检修计划",
    keyword_desc="按计划编号检索",
    status_desc="待审批、已批复、执行中、已完工",
)

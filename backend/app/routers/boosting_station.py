"""升压站监视接口：维护升压站，覆盖恢复正常、检查保护、安排检修等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.boosting_station import BoostingStationService

router = build_router(
    service=BoostingStationService(),
    prefix="/api/boosting_station",
    tag="升压站监视",
    keyword_desc="按升压站编号检索",
    status_desc="正常运行、非全相运行、保护动作、待检修",
)

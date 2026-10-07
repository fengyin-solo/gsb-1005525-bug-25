"""逆变器监视接口：维护逆变器，覆盖恢复运行、降容保护、安排检修等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.inverter import InverterService

router = build_router(
    service=InverterService(),
    prefix="/api/inverter",
    tag="逆变器监视",
    keyword_desc="按逆变器编号检索",
    status_desc="正常运行、降容运行、高温报警、待检修",
)

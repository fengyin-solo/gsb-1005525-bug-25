"""告警事件接口：维护告警事件，覆盖确认告警、开始处理、消除告警等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.alarm import AlarmService

router = build_router(
    service=AlarmService(),
    prefix="/api/alarm",
    tag="告警事件",
    keyword_desc="按告警编号检索",
    status_desc="未确认、已确认、处理中、已消除",
)

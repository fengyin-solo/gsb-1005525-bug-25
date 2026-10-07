"""环境监测站接口：维护环境监测站，覆盖恢复正常、标记异常、停用站点等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.environment import EnvironmentService

router = build_router(
    service=EnvironmentService(),
    prefix="/api/environment",
    tag="环境监测站",
    keyword_desc="按站点编号检索",
    status_desc="数据正常、数据异常、传感器故障、已停用",
)

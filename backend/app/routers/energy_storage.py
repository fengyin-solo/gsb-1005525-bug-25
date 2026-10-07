"""储能电池组接口：维护储能电池组，覆盖启动充电、启动放电、切换到待机等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.energy_storage import EnergyStorageService

router = build_router(
    service=EnergyStorageService(),
    prefix="/api/energy_storage",
    tag="储能电池组",
    keyword_desc="按电池组编号检索",
    status_desc="充电中、放电中、待机、故障停机",
)

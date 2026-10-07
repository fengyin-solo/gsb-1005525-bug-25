"""光伏阵列接口：维护光伏阵列，覆盖恢复全功率、降功率运行、申请停机等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.pv_array import PvArrayService

router = build_router(
    service=PvArrayService(),
    prefix="/api/pv_array",
    tag="光伏阵列",
    keyword_desc="按阵列编号检索",
    status_desc="运行中、限功率、计划停机、故障停机",
)

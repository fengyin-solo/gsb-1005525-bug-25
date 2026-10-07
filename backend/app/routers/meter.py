"""关口计量接口：维护关口表计，覆盖确认正常、标记异常、停用表计等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.meter import MeterService

router = build_router(
    service=MeterService(),
    prefix="/api/meter",
    tag="关口计量",
    keyword_desc="按表计编号检索",
    status_desc="通讯正常、数据异常、通讯中断、已停用",
)

"""汇流箱检测接口：维护汇流箱，覆盖恢复正常、标记异常、停用设备等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.combiner_box import CombinerBoxService

router = build_router(
    service=CombinerBoxService(),
    prefix="/api/combiner_box",
    tag="汇流箱检测",
    keyword_desc="按汇流箱编号检索",
    status_desc="运行正常、熔断器异常、通讯中断、已停用",
)

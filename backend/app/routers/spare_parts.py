"""备品备件接口：维护备件物料，覆盖入库登记、领用出库、标记废弃等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.spare_parts import SparePartsService

router = build_router(
    service=SparePartsService(),
    prefix="/api/spare_parts",
    tag="备品备件",
    keyword_desc="按备件编号检索",
    status_desc="存量充足、低于安全量、已用尽、已废弃",
)

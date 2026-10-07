"""运维合同接口：维护运维合同，覆盖确认签订、开始履行、终止合同等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.contract import ContractService

router = build_router(
    service=ContractService(),
    prefix="/api/contract",
    tag="运维合同",
    keyword_desc="按合同编号检索",
    status_desc="草稿中、已签订、履行中、已到期、已终止",
)

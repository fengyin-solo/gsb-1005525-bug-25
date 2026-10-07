"""安全措施接口：维护安全措施票，覆盖签发措施、开始执行、解除措施等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.safety import SafetyService

router = build_router(
    service=SafetyService(),
    prefix="/api/safety",
    tag="安全措施",
    keyword_desc="按措施编号检索",
    status_desc="待签发、已签发、执行中、已解除",
)

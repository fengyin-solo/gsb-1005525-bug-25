"""变压器监视接口：维护变压器，覆盖恢复正常、降负荷运行、安排检修等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.transformer import TransformerService

router = build_router(
    service=TransformerService(),
    prefix="/api/transformer",
    tag="变压器监视",
    keyword_desc="按变压器编号检索",
    status_desc="正常运行、过负荷、油温异常、待检修",
)

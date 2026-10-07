"""缺陷管理接口：维护设备缺陷，覆盖分派处理、提交验收、关闭缺陷等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.defect import DefectService

router = build_router(
    service=DefectService(),
    prefix="/api/defect",
    tag="缺陷管理",
    keyword_desc="按缺陷编号检索",
    status_desc="待分派、处理中、已验收、已关闭",
)

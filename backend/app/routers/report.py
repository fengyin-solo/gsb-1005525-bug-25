"""运行月报接口：维护运行月报，覆盖填写月报、提交审核、发布月报等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.report import ReportService

router = build_router(
    service=ReportService(),
    prefix="/api/report",
    tag="运行月报",
    keyword_desc="按月报编号检索",
    status_desc="待填写、已填写、已审核、已发布",
)

"""组件清洗接口：维护清洗任务，覆盖排期确认、开始作业、验收完成等动作。

列表分页、筛选与导出的实现统一收在 app.routers.base.build_router。
"""
from __future__ import annotations

from app.routers.base import build_router
from app.services.cleaning import CleaningService

router = build_router(
    service=CleaningService(),
    prefix="/api/cleaning",
    tag="组件清洗",
    keyword_desc="按任务编号检索",
    status_desc="待排期、已排期、作业中、已完成",
)

"""运行月报接口：列表、导出、登记与动作全部走统一路由工厂，分页口径只有一套。"""
from __future__ import annotations

from app.routers._factory import build_module_router
from app.services.report import ReportService

service = ReportService()
router = build_module_router(service, tag="运行月报")

"""储能电池组接口：列表、导出、登记与动作全部走统一路由工厂，分页口径只有一套。"""
from __future__ import annotations

from app.routers._factory import build_module_router
from app.services.energy_storage import EnergyStorageService

service = EnergyStorageService()
router = build_module_router(service, tag="储能电池组")

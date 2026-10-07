"""模块路由工厂：所有业务模块的列表/导出/登记/动作接口结构完全一致，统一在这里生成。

口径约定：
- 列表 POST /list：请求体携带 page/size/total 与筛选条件，总数与页码校正只走
  app.pagination 这一套算法，冲突时以接口返回的 total 为准；
- 导出 POST /export：请求体与列表同一份筛选条件，导出条数即列表 total，结果落库；
- 登记 POST /entries、动作 POST /{id}/actions、明细 GET /{id} 沿用原语义。
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas import ActionResult, EntryPayload, ExportResult, ListQuery, PageResult
from app.services.base import BaseModuleService


def build_module_router(service: BaseModuleService, *, tag: str) -> APIRouter:
    router = APIRouter(prefix=f"/api/{service.module}", tags=[tag])

    @router.post("/list", response_model=PageResult[dict])
    def list_entries(query: ListQuery) -> PageResult[dict]:
        """按当前筛选条件取数；页码/每页条数/总数的判定全部走统一分页口径。"""
        result = service.list_entries(query)
        return PageResult(**result.as_dict())

    @router.post("/export", response_model=ExportResult)
    def export_entries(query: ListQuery) -> ExportResult:
        """按当前筛选条件导出全量；导出条数与列表总数同源，导出结果落库留痕。"""
        return ExportResult(**service.export_entries(query))

    @router.get("/{entry_id}", response_model=dict)
    def get_entry(entry_id: int) -> dict:
        """读取单条明细；不存在时给出可读的错误说明。"""
        entry = service.get_entry(entry_id)
        if entry is None:
            raise HTTPException(status_code=404, detail=f"{service.label} {entry_id} 不存在或已归档")
        return entry

    @router.post("/entries", response_model=ActionResult)
    def create_entry(payload: EntryPayload) -> ActionResult:
        """登记一条记录，缺字段时说明原因而不是静默丢弃。"""
        entry, missing = service.create_entry(payload.values)
        if missing:
            return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
        return ActionResult(ok=True, message=f"{service.label}已登记", entry=entry)

    @router.post("/{entry_id}/actions", response_model=ActionResult)
    def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
        """对单条记录执行状态流转动作；不允许的动作会被拦下并说明原因。"""
        action = str(payload.values.get("action") or "").strip()
        entry, message = service.run_action(entry_id, action)
        if entry is None:
            return ActionResult(ok=False, message=message)
        return ActionResult(ok=True, message=message, entry=entry)

    return router

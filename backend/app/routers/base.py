"""列表/导出接口的统一装配。

18 个业务模块的接口结构完全一样，分页、筛选、导出落库只在这里写一遍；
各模块路由文件只剩一句 build_router(...) 和自己的文案。

注意路由顺序：/export 必须注册在 /{entry_id} 之前，否则 "export" 会被
当成 entry_id 解析，导出接口直接 422。
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, ExportResult, PageResult
from app.services.base import BaseService
from app.store import store

ORDER_DESC = "登记时间排序：desc 最新在前（默认），asc 最早在前"


def build_router(
    *,
    service: BaseService,
    prefix: str,
    tag: str,
    keyword_desc: str,
    status_desc: str,
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[tag])
    label = service.ENTRY_LABEL

    @router.get("", response_model=PageResult[dict])
    def list_entries(
        keyword: str | None = Query(default=None, description=keyword_desc),
        status: str | None = Query(default=None, description=status_desc),
        page: int = 1,
        size: int = 20,
        order: str = Query(default="desc", description=ORDER_DESC),
    ) -> PageResult[dict]:
        """按统一口径返回一页数据；非法页码回到第一页并在 notice 写明原因。"""
        data = service.list_entries(keyword=keyword, status=status, page=page, size=size, order=order)
        return PageResult(
            items=data.items,
            total=data.total,
            page=data.page,
            size=data.size,
            notice=data.notice,
        )

    @router.get("/export", response_model=ExportResult)
    def export_entries(
        keyword: str | None = Query(default=None, description=keyword_desc),
        status: str | None = Query(default=None, description=status_desc),
        order: str = Query(default="desc", description=ORDER_DESC),
    ) -> ExportResult:
        """按当前筛选条件取全量：与列表同一段筛选，条数同一份口径，结果落库。"""
        items, total = service.export_entries(keyword=keyword, status=status, order=order)
        record = store.record_export(
            module=service.MODULE,
            filters={"keyword": keyword, "status": status, "order": order},
            items=items,
        )
        return ExportResult(
            module=service.MODULE,
            total=total,
            items=items,
            record={
                "id": record["id"],
                "module": record["module"],
                "filters": record["filters"],
                "total": record["total"],
                "created_at": record["created_at"],
            },
        )

    @router.get("/{entry_id}", response_model=dict)
    def get_entry(entry_id: int) -> dict:
        """读取单条明细；不存在时给出可读的错误说明。"""
        entry = service.get_entry(entry_id)
        if entry is None:
            raise HTTPException(status_code=404, detail=f"{label} {entry_id} 不存在或已归档")
        return entry

    @router.post("", response_model=ActionResult)
    def create_entry(payload: EntryPayload) -> ActionResult:
        """登记一条记录，缺字段时说明原因而不是静默丢弃。"""
        entry, missing = service.create_entry(payload.values)
        if missing:
            return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
        return ActionResult(ok=True, message=f"{label}已登记", entry=entry)

    @router.post("/{entry_id}/actions", response_model=ActionResult)
    def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
        """对单条记录执行状态流转；不允许的动作会被拦下并说明原因。"""
        action = str(payload.values.get("action") or "").strip()
        entry, message = service.run_action(entry_id, action)
        if entry is None:
            return ActionResult(ok=False, message=message)
        return ActionResult(ok=True, message=message, entry=entry)

    return router

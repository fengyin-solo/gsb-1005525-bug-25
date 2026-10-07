"""导出记录接口：每次模块导出都会落库，这里分页查看并可取单条快照核对。"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.pagination import paginate
from app.schemas import ExportListQuery, PageResult
from app.store import store

router = APIRouter(prefix="/api/export_records", tags=["导出记录"])


@router.post("/list", response_model=PageResult[dict])
def list_export_records(query: ExportListQuery) -> PageResult[dict]:
    """分页查看导出记录；同样只走统一分页口径。"""
    rows = store.export_records()
    if query.module:
        rows = [row for row in rows if row.get("module") == query.module]
    result = paginate(rows, page=query.page, size=query.size)
    # 列表不带 items 快照明细，避免整包数据随列表返回。
    items = [
        {"id": row["id"], "module": row["module"], "total": row["total"],
         "filters": row["filters"], "created_at": row["created_at"]}
        for row in result.items
    ]
    return PageResult(items=items, total=result.total, page=result.page,
                      size=result.size, notice=result.notice)


@router.get("/{export_id}", response_model=dict)
def get_export_record(export_id: int) -> dict:
    """读取一次导出的完整快照（含全量条目），用于和列表口径对账。"""
    record = store.find_export(export_id)
    if record is None:
        raise HTTPException(status_code=404, detail=f"导出记录 {export_id} 不存在")
    return record

"""备品备件业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明备品备件自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class SparePartsService(BaseService):
    MODULE = "spare_parts"
    ENTRY_LABEL = "备件物料"
    SCOPE_LABEL = "备品备件"
    KEYWORD_FIELD = "备件编号"
    REQUIRED_FIELDS = ['备件编号', '备件名称', '规格型号']
    STATUS_ORDER = ['存量充足', '低于安全量', '已用尽', '已废弃']
    ACTION_RULES = {'入库登记': '存量充足', '领用出库': '低于安全量', '标记废弃': '已废弃'}
    NEGATIVE_ACTIONS = []

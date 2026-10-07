"""巡视检查业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明巡视检查自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class PatrolService(BaseService):
    MODULE = "patrol"
    ENTRY_LABEL = "巡视记录"
    SCOPE_LABEL = "巡视检查"
    KEYWORD_FIELD = "记录编号"
    REQUIRED_FIELDS = ['记录编号', '巡视区域', '巡视日期']
    STATUS_ORDER = ['待巡视', '巡视中', '已记录', '已归档']
    ACTION_RULES = {'开始巡视': '巡视中', '提交记录': '已记录', '归档记录': '已归档'}
    NEGATIVE_ACTIONS = []

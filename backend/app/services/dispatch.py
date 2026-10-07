"""调度指令业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明调度指令自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class DispatchService(BaseService):
    MODULE = "dispatch"
    ENTRY_LABEL = "调度指令单"
    SCOPE_LABEL = "调度指令"
    KEYWORD_FIELD = "指令编号"
    REQUIRED_FIELDS = ['指令编号', '下发单位', '指令类型']
    STATUS_ORDER = ['待执行', '执行中', '已完成', '已驳回']
    ACTION_RULES = {'确认执行': '执行中', '完成回复': '已完成', '驳回指令': '已驳回'}
    NEGATIVE_ACTIONS = ['驳回指令']

"""调度指令单业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "dispatch"
REQUIRED_FIELDS = ['指令编号', '下发单位', '指令类型']
STATUS_ORDER = ['待执行', '执行中', '已完成', '已驳回']
ACTION_RULES = {'确认执行': '执行中', '完成回复': '已完成', '驳回指令': '已驳回'}
NEGATIVE_ACTIONS = ['驳回指令']
LIST_FIELDS = ['指令编号', '下发单位', '指令类型', '下发时间', '执行时限', '执行人', '执行结果', '指令状态']
KEYWORD_FIELDS = ['指令编号']
LABEL = "调度指令单"


class DispatchService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

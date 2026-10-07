"""告警事件业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "alarm"
REQUIRED_FIELDS = ['告警编号', '告警来源', '告警类型']
STATUS_ORDER = ['未确认', '已确认', '处理中', '已消除']
ACTION_RULES = {'确认告警': '已确认', '开始处理': '处理中', '消除告警': '已消除'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['告警编号', '告警来源', '告警类型', '触发时间', '告警阈值', '当前值', '确认人', '告警状态']
KEYWORD_FIELDS = ['告警编号']
LABEL = "告警事件"


class AlarmService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

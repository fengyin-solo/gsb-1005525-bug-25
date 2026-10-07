"""告警事件业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明告警事件自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class AlarmService(BaseService):
    MODULE = "alarm"
    ENTRY_LABEL = "告警事件"
    SCOPE_LABEL = "告警事件"
    KEYWORD_FIELD = "告警编号"
    REQUIRED_FIELDS = ['告警编号', '告警来源', '告警类型']
    STATUS_ORDER = ['未确认', '已确认', '处理中', '已消除']
    ACTION_RULES = {'确认告警': '已确认', '开始处理': '处理中', '消除告警': '已消除'}
    NEGATIVE_ACTIONS = []

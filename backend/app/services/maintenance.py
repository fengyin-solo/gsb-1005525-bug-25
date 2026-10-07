"""检修计划业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明检修计划自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class MaintenanceService(BaseService):
    MODULE = "maintenance"
    ENTRY_LABEL = "检修计划"
    SCOPE_LABEL = "检修计划"
    KEYWORD_FIELD = "计划编号"
    REQUIRED_FIELDS = ['计划编号', '检修设备', '检修类别']
    STATUS_ORDER = ['待审批', '已批复', '执行中', '已完工']
    ACTION_RULES = {'提交审批': '已批复', '开始执行': '执行中', '确认完工': '已完工'}
    NEGATIVE_ACTIONS = []

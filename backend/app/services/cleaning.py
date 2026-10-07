"""组件清洗业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明组件清洗自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class CleaningService(BaseService):
    MODULE = "cleaning"
    ENTRY_LABEL = "清洗任务"
    SCOPE_LABEL = "组件清洗"
    KEYWORD_FIELD = "任务编号"
    REQUIRED_FIELDS = ['任务编号', '清洗区域', '清洗方式']
    STATUS_ORDER = ['待排期', '已排期', '作业中', '已完成']
    ACTION_RULES = {'排期确认': '已排期', '开始作业': '作业中', '验收完成': '已完成'}
    NEGATIVE_ACTIONS = []

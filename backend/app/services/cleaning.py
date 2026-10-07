"""清洗任务业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "cleaning"
REQUIRED_FIELDS = ['任务编号', '清洗区域', '清洗方式']
STATUS_ORDER = ['待排期', '已排期', '作业中', '已完成']
ACTION_RULES = {'排期确认': '已排期', '开始作业': '作业中', '验收完成': '已完成'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['任务编号', '清洗区域', '清洗方式', '计划日期', '作业人员', '用水吨数', '清洗后PR值', '清洗状态']
KEYWORD_FIELDS = ['任务编号']
LABEL = "清洗任务"


class CleaningService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

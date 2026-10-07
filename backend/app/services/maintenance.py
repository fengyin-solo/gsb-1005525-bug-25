"""检修计划业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "maintenance"
REQUIRED_FIELDS = ['计划编号', '检修设备', '检修类别']
STATUS_ORDER = ['待审批', '已批复', '执行中', '已完工']
ACTION_RULES = {'提交审批': '已批复', '开始执行': '执行中', '确认完工': '已完工'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['计划编号', '检修设备', '检修类别', '计划开始', '计划结束', '责任人', '安全措施', '计划状态']
KEYWORD_FIELDS = ['计划编号']
LABEL = "检修计划"


class MaintenanceService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

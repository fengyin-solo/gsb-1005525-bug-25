"""巡视记录业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "patrol"
REQUIRED_FIELDS = ['记录编号', '巡视区域', '巡视日期']
STATUS_ORDER = ['待巡视', '巡视中', '已记录', '已归档']
ACTION_RULES = {'开始巡视': '巡视中', '提交记录': '已记录', '归档记录': '已归档'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['记录编号', '巡视区域', '巡视日期', '巡视人员', '发现缺陷数', '红外测温结果', '接线端子温度', '巡视状态']
KEYWORD_FIELDS = ['记录编号']
LABEL = "巡视记录"


class PatrolService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

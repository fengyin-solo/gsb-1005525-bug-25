"""设备缺陷业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "defect"
REQUIRED_FIELDS = ['缺陷编号', '发现日期', '缺陷设备']
STATUS_ORDER = ['待分派', '处理中', '已验收', '已关闭']
ACTION_RULES = {'分派处理': '处理中', '提交验收': '已验收', '关闭缺陷': '已关闭'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['缺陷编号', '发现日期', '缺陷设备', '缺陷类别', '严重等级', '处理方案', '整改时限', '缺陷状态']
KEYWORD_FIELDS = ['缺陷编号']
LABEL = "设备缺陷"


class DefectService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

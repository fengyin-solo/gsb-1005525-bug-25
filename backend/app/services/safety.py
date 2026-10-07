"""安全措施票业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "safety"
REQUIRED_FIELDS = ['措施编号', '措施类型', '涉及设备']
STATUS_ORDER = ['待签发', '已签发', '执行中', '已解除']
ACTION_RULES = {'签发措施': '已签发', '开始执行': '执行中', '解除措施': '已解除'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['措施编号', '措施类型', '涉及设备', '签发人', '执行人', '监护人', '有效期至', '措施状态']
KEYWORD_FIELDS = ['措施编号']
LABEL = "安全措施票"


class SafetyService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

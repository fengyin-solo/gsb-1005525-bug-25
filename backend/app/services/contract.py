"""运维合同业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "contract"
REQUIRED_FIELDS = ['合同编号', '合同名称', '签约甲方']
STATUS_ORDER = ['草稿中', '已签订', '履行中', '已到期', '已终止']
ACTION_RULES = {'确认签订': '已签订', '开始履行': '履行中', '终止合同': '已终止'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['合同编号', '合同名称', '签约甲方', '签约乙方', '合同金额', '起止日期', '续签条款', '合同状态']
KEYWORD_FIELDS = ['合同编号', '合同名称']
LABEL = "运维合同"


class ContractService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

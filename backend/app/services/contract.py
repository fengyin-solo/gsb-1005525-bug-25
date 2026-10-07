"""运维合同业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明运维合同自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class ContractService(BaseService):
    MODULE = "contract"
    ENTRY_LABEL = "运维合同"
    SCOPE_LABEL = "运维合同"
    KEYWORD_FIELD = "合同编号"
    REQUIRED_FIELDS = ['合同编号', '合同名称', '签约甲方']
    STATUS_ORDER = ['草稿中', '已签订', '履行中', '已到期', '已终止']
    ACTION_RULES = {'确认签订': '已签订', '开始履行': '履行中', '终止合同': '已终止'}
    NEGATIVE_ACTIONS = []

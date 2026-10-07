"""安全措施业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明安全措施自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class SafetyService(BaseService):
    MODULE = "safety"
    ENTRY_LABEL = "安全措施票"
    SCOPE_LABEL = "安全措施"
    KEYWORD_FIELD = "措施编号"
    REQUIRED_FIELDS = ['措施编号', '措施类型', '涉及设备']
    STATUS_ORDER = ['待签发', '已签发', '执行中', '已解除']
    ACTION_RULES = {'签发措施': '已签发', '开始执行': '执行中', '解除措施': '已解除'}
    NEGATIVE_ACTIONS = []

"""缺陷管理业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明缺陷管理自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class DefectService(BaseService):
    MODULE = "defect"
    ENTRY_LABEL = "设备缺陷"
    SCOPE_LABEL = "缺陷管理"
    KEYWORD_FIELD = "缺陷编号"
    REQUIRED_FIELDS = ['缺陷编号', '发现日期', '缺陷设备']
    STATUS_ORDER = ['待分派', '处理中', '已验收', '已关闭']
    ACTION_RULES = {'分派处理': '处理中', '提交验收': '已验收', '关闭缺陷': '已关闭'}
    NEGATIVE_ACTIONS = []

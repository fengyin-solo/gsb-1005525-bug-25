"""关口计量业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明关口计量自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class MeterService(BaseService):
    MODULE = "meter"
    ENTRY_LABEL = "关口表计"
    SCOPE_LABEL = "关口计量"
    KEYWORD_FIELD = "表计编号"
    REQUIRED_FIELDS = ['表计编号', '计量点名称', '表计精度']
    STATUS_ORDER = ['通讯正常', '数据异常', '通讯中断', '已停用']
    ACTION_RULES = {'确认正常': '通讯正常', '标记异常': '数据异常', '停用表计': '已停用'}
    NEGATIVE_ACTIONS = ['停用表计']

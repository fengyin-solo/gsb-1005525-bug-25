"""变压器监视业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明变压器监视自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class TransformerService(BaseService):
    MODULE = "transformer"
    ENTRY_LABEL = "变压器"
    SCOPE_LABEL = "变压器监视"
    KEYWORD_FIELD = "变压器编号"
    REQUIRED_FIELDS = ['变压器编号', '电压等级', '额定容量']
    STATUS_ORDER = ['正常运行', '过负荷', '油温异常', '待检修']
    ACTION_RULES = {'恢复正常': '正常运行', '降负荷运行': '过负荷', '安排检修': '待检修'}
    NEGATIVE_ACTIONS = []

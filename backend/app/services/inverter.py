"""逆变器监视业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明逆变器监视自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class InverterService(BaseService):
    MODULE = "inverter"
    ENTRY_LABEL = "逆变器"
    SCOPE_LABEL = "逆变器监视"
    KEYWORD_FIELD = "逆变器编号"
    REQUIRED_FIELDS = ['逆变器编号', '品牌型号', '额定功率']
    STATUS_ORDER = ['正常运行', '降容运行', '高温报警', '待检修']
    ACTION_RULES = {'恢复运行': '正常运行', '降容保护': '降容运行', '安排检修': '待检修'}
    NEGATIVE_ACTIONS = []

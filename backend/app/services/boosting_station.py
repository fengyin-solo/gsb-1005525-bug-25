"""升压站监视业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明升压站监视自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class BoostingStationService(BaseService):
    MODULE = "boosting_station"
    ENTRY_LABEL = "升压站"
    SCOPE_LABEL = "升压站监视"
    KEYWORD_FIELD = "升压站编号"
    REQUIRED_FIELDS = ['升压站编号', '进线电压', '出线电压']
    STATUS_ORDER = ['正常运行', '非全相运行', '保护动作', '待检修']
    ACTION_RULES = {'恢复正常': '正常运行', '检查保护': '非全相运行', '安排检修': '待检修'}
    NEGATIVE_ACTIONS = []

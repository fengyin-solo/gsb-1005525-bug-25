"""储能电池组业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明储能电池组自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class EnergyStorageService(BaseService):
    MODULE = "energy_storage"
    ENTRY_LABEL = "储能电池组"
    SCOPE_LABEL = "储能电池组"
    KEYWORD_FIELD = "电池组编号"
    REQUIRED_FIELDS = ['电池组编号', '电池类型', '额定容量']
    STATUS_ORDER = ['充电中', '放电中', '待机', '故障停机']
    ACTION_RULES = {'启动充电': '充电中', '启动放电': '放电中', '切换到待机': '待机'}
    NEGATIVE_ACTIONS = []

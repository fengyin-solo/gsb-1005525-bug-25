"""光伏阵列业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明光伏阵列自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class PvArrayService(BaseService):
    MODULE = "pv_array"
    ENTRY_LABEL = "光伏阵列"
    SCOPE_LABEL = "光伏阵列"
    KEYWORD_FIELD = "阵列编号"
    REQUIRED_FIELDS = ['阵列编号', '所属片区', '组件型号']
    STATUS_ORDER = ['运行中', '限功率', '计划停机', '故障停机']
    ACTION_RULES = {'恢复全功率': '运行中', '降功率运行': '限功率', '申请停机': '计划停机'}
    NEGATIVE_ACTIONS = []

"""光伏阵列业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "pv_array"
REQUIRED_FIELDS = ['阵列编号', '所属片区', '组件型号']
STATUS_ORDER = ['运行中', '限功率', '计划停机', '故障停机']
ACTION_RULES = {'恢复全功率': '运行中', '降功率运行': '限功率', '申请停机': '计划停机'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['阵列编号', '所属片区', '组件型号', '单块功率', '串联片数', '总装机容量', '投运日期', '阵列状态']
KEYWORD_FIELDS = ['阵列编号']
LABEL = "光伏阵列"


class PvArrayService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

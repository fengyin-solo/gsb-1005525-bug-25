"""关口表计业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "meter"
REQUIRED_FIELDS = ['表计编号', '计量点名称', '表计精度']
STATUS_ORDER = ['通讯正常', '数据异常', '通讯中断', '已停用']
ACTION_RULES = {'确认正常': '通讯正常', '标记异常': '数据异常', '停用表计': '已停用'}
NEGATIVE_ACTIONS = ['停用表计']
LIST_FIELDS = ['表计编号', '计量点名称', '表计精度', '正向有功电量', '反向有功电量', '上月示数', '本月示数', '通讯状态']
KEYWORD_FIELDS = ['表计编号', '计量点名称']
LABEL = "关口表计"


class MeterService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

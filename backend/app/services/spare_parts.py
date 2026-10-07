"""备件业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "spare_parts"
REQUIRED_FIELDS = ['备件编号', '备件名称', '规格型号']
STATUS_ORDER = ['存量充足', '低于安全量', '已用尽', '已废弃']
ACTION_RULES = {'入库登记': '存量充足', '领用出库': '低于安全量', '标记废弃': '已废弃'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['备件编号', '备件名称', '规格型号', '适用设备', '安全存量', '当前存量', '存放位置', '备件状态']
KEYWORD_FIELDS = ['备件编号', '备件名称']
LABEL = "备件"


class SparePartsService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

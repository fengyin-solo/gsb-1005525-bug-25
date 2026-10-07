"""升压站业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "boosting_station"
REQUIRED_FIELDS = ['升压站编号', '进线电压', '出线电压']
STATUS_ORDER = ['正常运行', '非全相运行', '保护动作', '待检修']
ACTION_RULES = {'恢复正常': '正常运行', '检查保护': '非全相运行', '安排检修': '待检修'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['升压站编号', '进线电压', '出线电压', '主变容量', '母线状态', '断路器状态', '无功补偿', '运行状态']
KEYWORD_FIELDS = ['升压站编号']
LABEL = "升压站"


class BoostingStationService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

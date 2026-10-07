"""逆变器业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "inverter"
REQUIRED_FIELDS = ['逆变器编号', '品牌型号', '额定功率']
STATUS_ORDER = ['正常运行', '降容运行', '高温报警', '待检修']
ACTION_RULES = {'恢复运行': '正常运行', '降容保护': '降容运行', '安排检修': '待检修'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['逆变器编号', '品牌型号', '额定功率', '输入电压范围', '所属阵列', '运行温度', '日均发电量', '运行状态']
KEYWORD_FIELDS = ['逆变器编号']
LABEL = "逆变器"


class InverterService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

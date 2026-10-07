"""变压器业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "transformer"
REQUIRED_FIELDS = ['变压器编号', '电压等级', '额定容量']
STATUS_ORDER = ['正常运行', '过负荷', '油温异常', '待检修']
ACTION_RULES = {'恢复正常': '正常运行', '降负荷运行': '过负荷', '安排检修': '待检修'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['变压器编号', '电压等级', '额定容量', '油温上限', '绕组温度', '油位状态', '瓦斯保护状态', '运行状态']
KEYWORD_FIELDS = ['变压器编号']
LABEL = "变压器"


class TransformerService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

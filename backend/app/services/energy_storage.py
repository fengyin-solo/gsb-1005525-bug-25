"""储能电池组业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "energy_storage"
REQUIRED_FIELDS = ['电池组编号', '电池类型', '额定容量']
STATUS_ORDER = ['充电中', '放电中', '待机', '故障停机']
ACTION_RULES = {'启动充电': '充电中', '启动放电': '放电中', '切换到待机': '待机'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['电池组编号', '电池类型', '额定容量', 'SOC上限', '充放电循环', '电池温度', '内阻变化率', '运行状态']
KEYWORD_FIELDS = ['电池组编号']
LABEL = "储能电池组"


class EnergyStorageService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

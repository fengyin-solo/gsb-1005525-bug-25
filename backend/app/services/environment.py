"""环境监测站业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "environment"
REQUIRED_FIELDS = ['站点编号', '安装位置', '辐照度']
STATUS_ORDER = ['数据正常', '数据异常', '传感器故障', '已停用']
ACTION_RULES = {'恢复正常': '数据正常', '标记异常': '数据异常', '停用站点': '已停用'}
NEGATIVE_ACTIONS = ['停用站点']
LIST_FIELDS = ['站点编号', '安装位置', '辐照度', '环境温度', '风速', '风向', '积灰比', '通讯状态']
KEYWORD_FIELDS = ['站点编号', '安装位置']
LABEL = "环境监测站"


class EnvironmentService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

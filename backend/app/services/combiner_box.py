"""汇流箱业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "combiner_box"
REQUIRED_FIELDS = ['汇流箱编号', '所属阵列', '输入路数']
STATUS_ORDER = ['运行正常', '熔断器异常', '通讯中断', '已停用']
ACTION_RULES = {'恢复正常': '运行正常', '标记异常': '熔断器异常', '停用设备': '已停用'}
NEGATIVE_ACTIONS = ['停用设备']
LIST_FIELDS = ['汇流箱编号', '所属阵列', '输入路数', '熔断器状态', '防雷模块状态', '通讯状态', '箱体温度', '运行状态']
KEYWORD_FIELDS = ['汇流箱编号']
LABEL = "汇流箱"


class CombinerBoxService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

"""运行月报业务规则：状态流转与字段校验沿用本模块定义，筛选/分页/导出口径统一走基类。"""
from __future__ import annotations

from app.services.base import BaseModuleService

MODULE = "report"
REQUIRED_FIELDS = ['月报编号', '统计月份', '发电量']
STATUS_ORDER = ['待填写', '已填写', '已审核', '已发布']
ACTION_RULES = {'填写月报': '已填写', '提交审核': '已审核', '发布月报': '已发布'}
NEGATIVE_ACTIONS = []
LIST_FIELDS = ['月报编号', '统计月份', '发电量', '等效利用小时', '综合效率PR', '设备可利用率', '故障停机时间', '月报状态']
KEYWORD_FIELDS = ['月报编号']
LABEL = "运行月报"


class ReportService(BaseModuleService):
    module = MODULE
    required_fields = REQUIRED_FIELDS
    status_order = STATUS_ORDER
    action_rules = ACTION_RULES
    negative_actions = NEGATIVE_ACTIONS
    list_fields = LIST_FIELDS
    keyword_fields = KEYWORD_FIELDS
    label = LABEL

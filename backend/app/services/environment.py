"""环境监测站业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明环境监测站自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class EnvironmentService(BaseService):
    MODULE = "environment"
    ENTRY_LABEL = "环境监测站"
    SCOPE_LABEL = "环境监测站"
    KEYWORD_FIELD = "站点编号"
    REQUIRED_FIELDS = ['站点编号', '安装位置', '辐照度']
    STATUS_ORDER = ['数据正常', '数据异常', '传感器故障', '已停用']
    ACTION_RULES = {'恢复正常': '数据正常', '标记异常': '数据异常', '停用站点': '已停用'}
    NEGATIVE_ACTIONS = ['停用站点']

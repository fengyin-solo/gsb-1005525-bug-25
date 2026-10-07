"""汇流箱检测业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明汇流箱检测自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class CombinerBoxService(BaseService):
    MODULE = "combiner_box"
    ENTRY_LABEL = "汇流箱"
    SCOPE_LABEL = "汇流箱检测"
    KEYWORD_FIELD = "汇流箱编号"
    REQUIRED_FIELDS = ['汇流箱编号', '所属阵列', '输入路数']
    STATUS_ORDER = ['运行正常', '熔断器异常', '通讯中断', '已停用']
    ACTION_RULES = {'恢复正常': '运行正常', '标记异常': '熔断器异常', '停用设备': '已停用'}
    NEGATIVE_ACTIONS = ['停用设备']

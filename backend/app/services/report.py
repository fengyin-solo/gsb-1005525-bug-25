"""运行月报业务规则：状态流转、字段校验与筛选口径都收在这里。

分页、筛选、排序的通用实现见 app.services.base.BaseService 与 app.listing，
这里只声明运行月报自己的常量。
"""
from __future__ import annotations

from app.services.base import BaseService


class ReportService(BaseService):
    MODULE = "report"
    ENTRY_LABEL = "运行月报"
    SCOPE_LABEL = "运行月报"
    KEYWORD_FIELD = "月报编号"
    REQUIRED_FIELDS = ['月报编号', '统计月份', '发电量']
    STATUS_ORDER = ['待填写', '已填写', '已审核', '已发布']
    ACTION_RULES = {'填写月报': '已填写', '提交审核': '已审核', '发布月报': '已发布'}
    NEGATIVE_ACTIONS = []

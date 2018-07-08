# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 20:18
# @Author  : LeonHardt
# @File    : evalerror.py

"""
evalerror : 模型训练使用的损失函数，与评分方式对应

"""
import math
from sklearn.metrics import mean_squared_log_error


def evalerror(preds, dtrain):       # written by myself
    labels = dtrain.get_label()
    return 'error', math.sqrt(mean_squared_log_error(preds,labels))


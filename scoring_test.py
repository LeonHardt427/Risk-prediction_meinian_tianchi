# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 13:42
# @Author  : LeonHardt
# @File    : scoring_test.py

import os
import pandas as pd
from math import log1p, pow
# 计算误差损失（评估分数）


def calc_logloss(true_df, pred_df):
    new = 3
    loss_sum = 0
    rows = true_df.shape[0]
    for c in true_df.columns:
        # 预测结果必须要>0,否则log函数会报错，导致最终提交结果没有分数
        print(c)
        true_df[c] = true_df[c].apply(lambda x: log1p(x))
        pred_df[c] = pred_df[c].apply(lambda x: log1p(x))
        true_df[c+new] = pred_df[c]-true_df[c]
        true_df[c+new] = true_df[c+new].apply(lambda x: pow(x, 2))
        loss_item = (true_df[c+new].sum())/rows
        loss_sum += loss_item
        print('%s的loss：%f' % (c, loss_item))
    loss_sum = loss_sum/5
    print('总的loss：', loss_sum)


if __name__ == '__main__':
    path = os.getcwd() + '/updata/'
    print(path)
    true = pd.read_csv(path+'updata_1.csv', index_col=0, delimiter=',', header=None)
    pred = pd.read_csv(path+'updata_3.csv', index_col=0, delimiter=',', header=None)
    calc_logloss(true, pred)
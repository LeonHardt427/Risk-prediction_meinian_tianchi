# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 21:39
# @Author  : LeonHardt
# @File    : feature_selection2.py

import os
import pandas as pd

path = os.getcwd() + "data_std/"

df1 = pd.read_csv(path+"data_std1.csv", delimiter=',', index_col=0, encoding="gbk")
df2 = pd.read_csv(path+"data_std2.csv", delimiter=',', index_col=0, encoding="gbk")
# part 1 539-妇科  102-脂肪肝
col1 = ['2403', '2403', '2405', '2420', '1321', '1322', '1325', '1326', '2406', '1319', '1320', '539', '102']

df1_1 = df1.loc[:, ]
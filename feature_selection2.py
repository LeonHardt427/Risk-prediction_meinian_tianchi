# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 21:39
# @Author  : LeonHardt
# @File    : feature_selection2.py

import os
import pandas as pd

path = os.getcwd() + "/data_std/"

df1 = pd.read_csv(path+"data_std1.csv", delimiter=',', index_col=0, encoding="gbk")
df2 = pd.read_csv(path+"data_std2.csv", delimiter=',', index_col=0, encoding="gbk")
# part 1 539-妇科  102-脂肪肝
# col1 = ['2403', '2403', '2405', '2420', '1321', '1322', '1325', '1326', '2406', '1319', '1320', '539', '102']
col1 = ['2403', '2403', '2405', '2420', '1321', '1322', '1325', '1326', '2406', '1319', '1320']
col2 = ['31', '312', '313', '314', '32', '320', '38', '3193', '1850', '10004', '190', '191', '2333', '2372', '10002',
        '10003', '1814', '1815', '183', '1845', '192', '193', '2174', '100006']
df1_1 = df1.loc[:, col1]
df2_2 = df2.loc[:, col2]

df_whole = df1_1.join(df2_2)

df_whole.to_csv(path+'data_whole_std1.csv', sep=',')


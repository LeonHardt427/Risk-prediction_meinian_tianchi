# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 20:15
# @Author  : LeonHardt
# @File    : feature_selection3.py

# 对于tidy数据使用，预处理然后提取特征

import os
import pandas as pd
import numpy as np

path = os.getcwd() + '/data_std/'

df_tidy1 = pd.read_csv(path+'data_tidy1.csv', delimiter=',', encoding='gbk', index_col=0)
df_tidy2 = pd.read_csv(path+'data_tidy2.csv', delimiter=',', encoding='gbk', index_col=0)

col_drop1 = []
col_drop2 = []

df_tidy1.fillna(0.0)
df_tidy2.fillna(0.0)
df_nan1 = (df_tidy1 == 0)
df_nan2 = (df_tidy2 == 0)

useless = ["未见异常", "正常", "未查",]
for num, col in enumerate(df_tidy1.columns):
    print(num)
    temp = np.sum(df_nan1.loc[:, col], axis=0)
    if (temp/57298) > 0.2 :
        col_drop1.append(col)
    for ind in df_tidy1.index:
        if df_tidy1.loc[ind, col] in useless:
            col_drop1.append(col)
            break

for nu, col in enumerate(df_tidy2.columns):
    print(nu)
    temp = np.sum(df_nan2.loc[:, col], axis=0)
    if (temp/57298) > 0.2 :
        col_drop2.append(col)
    for ind in df_tidy2.index:
        if df_tidy2.loc[ind, col] in useless:
            col_drop2.append(col)
            break

print(col_drop1)
print(col_drop2)


df_tidy1 = df_tidy1.drop(col_drop1, axis=1, inplace=True)
df_tidy2 = df_tidy2.drop(col_drop2, axis=1, inplace=True)

df_tidy1.to_csv(path+'data_std1_drop08.csv', delimiter=',')
df_tidy2.to_csv(path+'data_std2_drop08.csv', delimiter=',')
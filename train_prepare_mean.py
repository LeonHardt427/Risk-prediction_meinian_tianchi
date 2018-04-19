# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 9:22
# @Author  : LeonHardt
# @File    : train_prepare_mean.py


import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd() + '/data_use/'

df_train = pd.read_csv(path + 'train_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_test = pd.read_csv(path + 'test_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_y_trains = pd.read_csv(os.getcwd() + '/data_orginal/meinian_round1_train_20180408.csv', delimiter=',',
                          encoding='gbk', index_col=0)
# NaN -> 0.0
df_train = df_train.fillna(0.0)
df_test = df_test.fillna(0.0)

save_path = os.getcwd() + '/data_app/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

# ---------------------------------------------------------------
# x_train_ str to float:

for i, indexs in enumerate(df_train.index):
    print(i)
    for cols in df_train.columns:
        try:
            df_train.loc[indexs, cols] = float(df_train.loc[indexs, cols])
        except ValueError:
            df_train.loc[indexs, cols] = 0

# --------------------
# x_train mean data
for mean_num, cols in enumerate(df_train.columns):
    temp = df_train.loc[:, cols].mean()
    for ind in df_train.index:
        if df_train.loc[ind, cols] == 0:
            df_train.loc[ind, cols] = temp

x_train = df_train.loc[:, :].values
np.savetxt(save_path + 'x_train_mean.txt', x_train, delimiter=',')

# ----------------------------------------------------------------------------------------
# y_train_ str to float:

for i, indexs in enumerate(df_y_trains.index):
    print(i)
    for cols in df_y_trains.columns:
        try:
            df_y_trains.loc[indexs, cols] = float(df_y_trains.loc[indexs, cols])
        except ValueError:
            df_y_trains.loc[indexs, cols] = 0

y_train = df_y_trains.loc[:, :].values
np.savetxt(save_path + 'y_train_mean.txt', y_train, delimiter=',')

# -----------------------------------------------------------------------------------------
# x_test_ str to float:

for i, indexs in enumerate(df_test.index):
    print(i)
    for cols in df_test.columns:
        try:
            df_test.loc[indexs, cols] = float(df_test.loc[indexs, cols])
        except ValueError:
            df_test.loc[indexs, cols] = 0.0
# --------------------
# x_test mean data
for mean_nu, cols in enumerate(df_test.columns):
    temp = df_test.loc[:, cols].mean()
    for ind in df_test.index:
        if df_test.loc[ind, cols] == 0:
            df_test.loc[ind, cols] = temp

x_test = df_test.loc[:, :].values
np.savetxt(save_path + 'x_test_mean.txt', x_test, delimiter=',')

# print(x_train)
# print(y_train)
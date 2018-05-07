# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 16:50
# @Author  : LeonHardt
# @File    : train_prepare_error.py.py

import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd() + '/data_use/'
train_save = os.getcwd() + '/train_watch/'

# df_train = pd.read_csv(path + 'train_use_nan_change3.csv', delimiter=',', encoding='gbk', index_col=0)
df_test = pd.read_csv(path + 'test_use_nan_change3_b.csv', delimiter=',', encoding='gbk', index_col=0)

df_y_trains = pd.read_csv(os.getcwd() + '/data_orginal/meinian_round1_train_20180408.csv', delimiter=',',
                          encoding='gbk', index_col=0)

# error
# df_error = pd.read_csv(os.getcwd() + '/data_orginal/error_train3.csv', delimiter=',', encoding="gbk", header=None)
# error = []
# for ind in df_error.index:
#     error.append(df_error.iloc[ind, 0])
# print(error)

save_path = os.getcwd() + '/data_app/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

# ---------------------------------------------------------------
# x_train_ str to float:

# df_train.drop(error, axis=0, inplace=True)
#
# for i, indexs in enumerate(df_train.index):
#     print(i)
#     for cols in df_train.columns:
#         try:
#             df_train.loc[indexs, cols] = float(df_train.loc[indexs, cols])
#         except ValueError:
#             df_train.loc[indexs, cols] = np.nan
#
#
# df_train.to_csv(train_save + 'tain_feature_nan_change4.csv', sep=',')
# x_train = df_train.loc[:, :].values
# np.savetxt(save_path + 'x_train_nan_change4.txt', x_train, delimiter=',')

# ----------------------------------------------------------------------------------------
# y_train_ str to float:

# df_y_trains.drop(error, axis=0, inplace=True)
#
# for i, indexs in enumerate(df_y_trains.index):
#     print(i)
#     for cols in df_y_trains.columns:
#         try:
#             df_y_trains.loc[indexs, cols] = float(df_y_trains.loc[indexs, cols])
#         except ValueError:
#             df_y_trains.loc[indexs, cols] = np.nan
#
# df_y_trains.to_csv(train_save + 'tain_label_nan_change4.csv', sep=',')
# y_train = df_y_trains.loc[:, :].values
# np.savetxt(save_path + 'y_train_nan_change4.txt', y_train, delimiter=',')

# -----------------------------------------------------------------------------------------
# x_test_ str to float:

for i, indexs in enumerate(df_test.index):
    print(i)
    for cols in df_test.columns:
        try:
            df_test.loc[indexs, cols] = float(df_test.loc[indexs, cols])
        except ValueError:
            df_test.loc[indexs, cols] = np.nan

df_test.to_csv(train_save + 'x_test_label_nan_change4_b.csv', sep=',')
x_test = df_test.loc[:, :].values
np.savetxt(save_path + 'x_test_nan_change4_b.txt', x_test, delimiter=',')

# print(x_train)
# print(y_train)


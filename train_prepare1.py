# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 15:51
# @Author  : LeonHardt
# @File    : train_prepare1.py



import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd()+'/data_use/'

df_train = pd.read_csv(path+'train_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_test = pd.read_csv(path+'test_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_y_trains = pd.read_csv(os.getcwd()+'/data_orginal/meinian_round1_train_20180408.csv', delimiter=',',
                          encoding='gbk', index_col=0)
# NaN -> 0.0
df_train = df_train.fillna(0.0)
df_test = df_test.fillna(0.0)
df_error = pd.read_csv(os.getcwd() + '/data_orginal/error_train.csv', delimiter=',', encoding="gbk")
error = []

for ind in df_error.index:
    error.append(df_error.iloc[ind, 0])

print(error)
print(type(error))
# print(type(error))
# print(error.shape)
# error = error.reshape(-1, 1)
# print(error)

save_path = os.getcwd() + '/data_app/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

# ---------------------------------------------------------------
# x_train_ str to float:

df_train.drop(error, axis=0, inplace=True)
for i, indexs in enumerate(df_train.index):
    print(i)
    for cols in df_train.columns:
        try:
            df_train.loc[indexs, cols] = float(df_train.loc[indexs, cols])
        except ValueError:
            df_train.loc[indexs, cols] = 0

x_train = df_train.loc[:, :].values

np.savetxt(save_path+'x_train_mean1.txt', x_train, delimiter=',')


# ----------------------------------------------------------------------------------------
# y_train_ str to float:

df_y_trains.drop(error, axis=0, inplace=True)
for i, indexs in enumerate(df_y_trains.index):
    print(i)
    for cols in df_y_trains.columns:
        try:
            df_y_trains.loc[indexs, cols] = float(df_y_trains.loc[indexs, cols])
        except ValueError:
            df_y_trains.loc[indexs, cols] = 0

y_train = df_y_trains.loc[:, :].values

np.savetxt(save_path+'y_train_mean1.txt', y_train, delimiter=',')

# -----------------------------------------------------------------------------------------
# x_test_ str to float:

for i, indexs in enumerate(df_test.index):
    # print(i)
    for cols in df_test.columns:
        try:
            df_test.loc[indexs, cols] = float(df_test.loc[indexs, cols])
        except ValueError:
            df_test.loc[indexs, cols] = 0.0


x_test = df_test.loc[:, :].values
np.savetxt(save_path+'x_test_mean1.txt', x_test, delimiter=',')

# print(x_train)
# print(y_train)
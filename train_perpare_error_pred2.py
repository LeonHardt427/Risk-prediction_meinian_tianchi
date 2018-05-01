# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 9:46
# @Author  : LeonHardt
# @File    : train_perpare_error_pred2.py


import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd() + '/data_use/'
train_save = os.getcwd() + '/train_watch/'

df_train_pred2 = pd.read_csv(path + 'train_use_nan_change.csv', delimiter=',', encoding='gbk', index_col=0)

df_y_trains_pred2 = pd.read_csv(os.getcwd() + '/data_orginal/meinian_round1_train_20180408.csv', delimiter=',',
                          encoding='gbk', index_col=0)

# error
df_error = pd.read_csv(os.getcwd() + '/data_orginal/error_train3.csv', delimiter=',', encoding="gbk", header=None)
df_error_2 = pd.read_csv(os.getcwd() + '/data_orginal/error_predict2.csv', delimiter=',', encoding="gbk", header=None)
error = []
for ind in df_error.index:
    error.append(df_error.iloc[ind, 0])
for ind in df_error_2.index:
    error.append(df_error_2.iloc[ind, 0])
print(error)

save_path = os.getcwd() + '/data_app/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

# ---------------------------------------------------------------
# x_train_ str to float:

df_train_pred2.drop(error, axis=0, inplace=True)

for i, indexs in enumerate(df_train_pred2.index):
    print(i)
    for cols in df_train_pred2.columns:
        try:
            df_train_pred2.loc[indexs, cols] = float(df_train_pred2.loc[indexs, cols])
        except ValueError:
            df_train_pred2.loc[indexs, cols] = np.nan


df_train_pred2.to_csv(train_save + 'tain_feature_nan_error3_change_pred23.csv', sep=',')
x_train = df_train_pred2.loc[:, :].values
np.savetxt(save_path + 'x_train_nan_error3_change_pred23.txt', x_train, delimiter=',')

# ----------------------------------------------------------------------------------------
# y_train_ str to float:

df_y_trains_pred2.drop(error, axis=0, inplace=True)

for i, indexs in enumerate(df_y_trains_pred2.index):
    print(i)
    for cols in df_y_trains_pred2.columns:
        try:
            df_y_trains_pred2.loc[indexs, cols] = float(df_y_trains_pred2.loc[indexs, cols])
        except ValueError:
            df_y_trains_pred2.loc[indexs, cols] = np.nan

df_y_trains_pred2.loc[:, :] .to_csv(train_save + 'tain_label_nan_error3_change_pred23.csv', sep=',')
y_train = df_y_trains_pred2.loc[:, :].values
np.savetxt(save_path + 'y_train_nan_error3_change_pred23.txt', y_train, delimiter=',')

# print(x_train)
print(y_train)


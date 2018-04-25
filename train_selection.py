# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 18:42
# @Author  : LeonHardt
# @File    : train_selection.py


import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd()+'/data_use/'

df_train = pd.read_csv(path+'train_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_test = pd.read_csv(path+'test_use.csv', delimiter=',', encoding='gbk', index_col=0)
df_y_trains = pd.read_csv(os.getcwd()+'/data_orginal/meinian_round1_train_20180408.csv', delimiter=',',
                          encoding='gbk', index_col=0)

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
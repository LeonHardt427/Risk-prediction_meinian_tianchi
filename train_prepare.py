# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 10:32
# @Author  : LeonHardt
# @File    : train_prepare.py

import os
import pandas as pd

path = os.getcwd() + '/data_std/'
file = path + 'data_whole_std1.csv'
file_usedata = os.getcwd() + '/data_use/'
if os.path.exists(file_usedata) is False:
    os.makedirs(file_usedata)

train_path = os.getcwd() + '/data_orginal/meinian_round1_train_20180408.csv'
test_path = os.getcwd() + '/data_orginal/[new] meinian_round1_test_a_20180409.csv'
train_id = []
test_id = []

df_train = pd.read_csv(train_path, delimiter=',', encoding='gbk', index_col=0)
df_test = pd.read_csv(test_path, delimiter=',', encoding='gbk', index_col=0)
for vid in df_train.index:
    train_id.append(vid)
for vid in df_test.index:
    test_id.append(vid)

df_whole = pd.read_csv(file, delimiter=',', encoding='gbk', index_col=0)
df_train_use = df_whole.loc[train_id, :]
df_test_use = df_whole.loc[test_id, :]

df_train_use.to_csv(file_usedata+'train_use.csv', sep=',')
df_test_use.to_csv(file_usedata+'test_use.csv', sep=',')
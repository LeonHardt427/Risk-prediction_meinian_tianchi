# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 10:54
# @Author  : LeonHardt
# @File    : watch_train.py

import os
import numpy as np
import pandas as pd

path = os.getcwd() + '/train_watch'

df_error = pd.read_csv(os.getcwd() + '/data_orginal/error_train1.csv', delimiter=',', encoding="gbk")
error = []
for ind in df_error.index:
    error.append(df_error.iloc[ind, 0])

df_x_train = pd.read_csv(path+'/tain_feature_nan_change4.csv', delimiter=',', encoding="gbk", index_col=0)
df_y_train = pd.read_csv(path+'/tain_label_nan_change4.csv', delimiter=',', encoding="gbk", index_col=0)

df_x_train.drop(error, axis=0, inplace=True)
df_y_train.drop(error, axis=0, inplace=True)

x_train = df_x_train.loc[:, :].values
y_train = df_y_train.loc[:, :].values

save_path = os.getcwd()+'/data_app/'
np.savetxt(save_path+'x_train_change4_error1.txt', x_train, delimiter=',')
np.savetxt(save_path+'y_train_change4_error1.txt', y_train, delimiter=',')
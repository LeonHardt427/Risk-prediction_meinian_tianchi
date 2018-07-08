# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:42
# @Author  : LeonHardt
# @File    : train_drop_error_part.py

import os
import numpy as np
import pandas as pd

path = os.getcwd() + '/train_watch'
i = 4
df_error = pd.read_csv(os.getcwd() + '/error/error' + str(i) + '.csv', delimiter=',', encoding="gbk", header=None)  #
error = []
for ind in df_error.index:
    error.append(df_error.iloc[ind, 0])

df_x_train = pd.read_csv(path+'/tain_feature_nan_change4.csv', delimiter=',', encoding="gbk", index_col=0)
df_y_train = pd.read_csv(path+'/tain_label_nan_change4.csv', delimiter=',', encoding="gbk", index_col=0)

df_x_train.drop(error, axis=0, inplace=True)
df_y_train.drop(error, axis=0, inplace=True)

x_train = df_x_train.iloc[:, :].values
y_train = df_y_train.iloc[:, i].values   #

save_path = os.getcwd()+'/data_part'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

df_train = df_x_train.iloc[:, :]
df_train.to_csv(save_path + '/train'+str(i)+'_error.csv', sep=',')  #
df_label = df_y_train.iloc[:, i]   #
df_label.to_csv(save_path + '/label'+str(i)+'_error.csv', sep=',')  #

np.savetxt(save_path+'/x_train'+str(i)+'_change4_error.txt', x_train, delimiter=',')  #
np.savetxt(save_path+'/y_train'+str(i)+'_change4_error.txt', y_train, delimiter=',')  #

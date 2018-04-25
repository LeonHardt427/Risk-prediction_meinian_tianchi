# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 18:20
# @Author  : LeonHardt
# @File    : false_sample_train.py

import os
import numpy as np
import pandas as pd

path = os.getcwd()+"/train_watch/"
save_path = os.getcwd()+"/data_app/"
df_train = pd.read_csv(path + 'tain_feature_nan_error3.csv', delimiter=',', encoding='gbk', index_col=0)
df_label= pd.read_csv(path + 'tain_label_nan_error3.csv', delimiter=',', encoding='gbk', index_col=0)

# error
df_error = pd.read_csv(os.getcwd() + '/data_orginal/error_train_prepredict.csv', delimiter=',', encoding="gbk",
                       header=None)
error = []
for ind in df_error.index:
    error.append(df_error.iloc[ind, 0])
print(error)
df_train.drop(error, axis=0, inplace=True)
df_label.drop(error, axis=0, inplace=True)

x_train = df_train.loc[:, :].values
y_label = df_label.loc[:, :].values

np.savetxt(save_path + 'x_train_mean_nan_error3.txt', x_train, delimiter=',')
np.savetxt(save_path + 'y_train_mean_nan_error3.txt', y_label, delimiter=',')
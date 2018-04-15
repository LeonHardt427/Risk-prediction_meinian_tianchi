# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 16:56
# @Author  : LeonHardt
# @File    : result_prepare.py

import os
import numpy as np
import pandas as pd

file = os.getcwd() + '/predict/prediction.txt'
save_file = os.getcwd() + '/updata/'
if os.path.exists(save_file) is False:
    os.makedirs(save_file)
prediction = np.loadtxt(file, delimiter=',', dtype=float)
print(prediction.shape)

df_test = pd.read_csv(os.getcwd()+'/data_orginal/[new] meinian_round1_test_a_20180409.csv',
                      delimiter=',', encoding='gbk', index_col=0)
for i, index in enumerate(df_test.index):
    df_test.loc[index, :] = prediction[i, :]

print(df_test)
df_test.to_csv(save_file+'updata_1.csv', sep=',', header=None)

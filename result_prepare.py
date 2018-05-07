# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 16:56
# @Author  : LeonHardt
# @File    : result_prepare.py

import os
import numpy as np
import pandas as pd

file = os.getcwd() + '/predict/b/prediction_gbm_part_change4_error_b2.txt'
save_file = os.getcwd() + '/updata/b/'
if os.path.exists(save_file) is False:
    os.makedirs(save_file)
prediction = np.loadtxt(file, delimiter=',', dtype=float)
print(prediction.shape)

df_test = pd.read_csv(os.getcwd()+'/data_orginal/meinian_round1_test_b_20180505.csv',
                      delimiter=',', encoding='gbk', index_col=0)
for i, index in enumerate(df_test.index):
    df_test.loc[index, :] = prediction[i, :]

# for index in df_test.index:
#     if df_test.loc[index, "舒张压"] > 140 or df_test.loc[index, "舒张压"] < 39:
#         df_test.loc[index, "舒张压"] = 60
print(df_test)
df_test.to_csv(save_file+'updata_gbm_nan_change4_error3_b2.csv', sep=',', header=None)

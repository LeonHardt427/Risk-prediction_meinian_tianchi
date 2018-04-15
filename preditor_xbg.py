# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 11:15
# @Author  : LeonHardt
# @File    : preditor_xbg.py

import os
import numpy as np
import pandas as pd

import xgboost as xgb

path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train.txt', delimiter=',', dtype='float')
x_test = np.loadtxt(path+'x_test.txt', delimiter=',', dtype='float')

# xlf = xgb.XGBRegressor(max_depth=10, learning_rate=0.1, silent=True, objective='reg:gamma',
#                       nthread=-1, gamma=0, min_child_weight=1, max_delta_step=0, subsample=0.85, colsample_bytree=0.7,
#                        colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=1440, missing=None)

xlf = xgb.XGBRegressor(max_depth=10, learning_rate=0.1, n_estimators=160, silent=True, objective='reg:linear')
# print(y_train.shape)

xlf.fit(x_train, y_train[:, 0])
pred1 = xlf.predict(x_test)
prediction = pred1

xlf.fit(x_train, y_train[:, 1])
pred2 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred2))

xlf.fit(x_train, y_train[:, 2])
pred3 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred3))

xlf.fit(x_train, y_train[:, 3])
pred4 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred4))

xlf.fit(x_train, y_train[:, 4])
pred5 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred5))

prediction = prediction.T
np.savetxt(save_path+'prediction.txt', prediction, fmt='%.3e',  delimiter=',')
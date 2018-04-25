# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 11:15
# @Author  : LeonHardt
# @File    : preditor_xbg.py

import os
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scoring_test import evalerror

import xgboost as xgb

path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train_mean_nan_error3.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train_mean_nan_error3.txt', delimiter=',', dtype='float')
x_test = np.loadtxt(path+'x_test_mean_nan_error3.txt', delimiter=',', dtype='float')

# xlf = xgb.XGBRegressor(max_depth=10, learning_rate=0.1, silent=True, objective='reg:gamma',
#                       nthread=-1, gamma=0, min_child_weight=1, max_delta_step=0, subsample=0.85, colsample_bytree=0.7,
#                        colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=1440, missing=None)

# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

xlf = xgb.XGBRegressor(max_depth=6, learning_rate=0.1, n_estimators=60, subsample=1, silent=False, eta=0.2,
                       objective='reg:linear')
# print(y_train.shape)

xlf.fit(x_train, y_train[:, 0], eval_metric=evalerror)
pred1 = xlf.predict(x_test)
prediction = pred1

xlf.fit(x_train, y_train[:, 1], eval_metric=evalerror)
pred2 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred2))


xlf.fit(x_train, y_train[:, 2], eval_metric=evalerror)
pred3 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred3))


xlf.fit(x_train, y_train[:, 3], eval_metric=evalerror)
pred4 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred4))


xlf.fit(x_train, y_train[:, 4], eval_metric=evalerror)
pred5 = xlf.predict(x_test)
prediction = np.vstack((prediction, pred5))

prediction = prediction.T
np.savetxt(save_path+'prediction_nan_error33.txt', prediction, fmt='%.3e',  delimiter=',')
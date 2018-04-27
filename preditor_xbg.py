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

xlf0 = xgb.XGBRegressor(max_depth=4, learning_rate=0.1, n_estimators=160, subsample=0.8, silent=False,  gamma=0.2,
                       objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=0, reg_lambda=1)
xlf0.fit(x_train, y_train[:, 0], eval_metric=evalerror)
pred1 = xlf0.predict(x_test)
prediction = pred1

xlf1 = xgb.XGBRegressor(max_depth=4, learning_rate=0.1, n_estimators=170, subsample=1, gamma=0.7, silent=False,
                       objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=3, reg_lambda=1)
xlf1.fit(x_train, y_train[:, 1], eval_metric=evalerror)
pred2 = xlf1.predict(x_test)
prediction = np.vstack((prediction, pred2))

xlf2 = xgb.XGBRegressor(max_depth=6, learning_rate=0.075, n_estimators=50, subsample=0.8, silent=False, gamma=0.4,
                       objective='reg:linear', min_child_weight=4, colsample_bytree=0.7, reg_alpha=0, reg_lambda=1)
xlf2.fit(x_train, y_train[:, 2], eval_metric=evalerror)
pred3 = xlf2.predict(x_test)
prediction = np.vstack((prediction, pred3))

xlf3 = xgb.XGBRegressor(max_depth=10, learning_rate=0.025, n_estimators=230, subsample=0.7, silent=False, gamma=0.1,
                       objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=0, reg_lambda=1)
xlf3.fit(x_train, y_train[:, 3], eval_metric=evalerror)
pred4 = xlf3.predict(x_test)
prediction = np.vstack((prediction, pred4))

xlf4 = xgb.XGBRegressor(max_depth=8, learning_rate=0.05, n_estimators=210, subsample=0.7, silent=False, gamma=0.1,
                       objective='reg:linear', min_child_weight=3, colsample_bytree=1, reg_alpha=2, reg_lambda=3)
xlf4.fit(x_train, y_train[:, 4], eval_metric=evalerror)
pred5 = xlf4.predict(x_test)
prediction = np.vstack((prediction, pred5))

prediction = prediction.T
np.savetxt(save_path+'prediction_nan_error35.txt', prediction, fmt='%.3e',  delimiter=',')
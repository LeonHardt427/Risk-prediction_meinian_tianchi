# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 9:25
# @Author  : LeonHardt
# @File    : paramter_xgb_2.py


import os
import numpy as np
import pandas

import xgboost as xbg

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from scoring_test import evalerror

path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train_mean_nan_error3.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train_mean_nan_error3.txt', delimiter=',', dtype='float')
for i in range(5):
    y_train_num = y_train[:, i]

    params_grid = {
        'max_depth': range(6, 15, 2),
        'n_estimators': range(10, 301, 50),
        'learning_rate': [0.0005, 0.001, 0.01, 0.1, 0.5, 0.8, 1]
    }
    params_fixed = {
        'objective': 'reg:linear',
        'silent': True
    }
    bst_grid = GridSearchCV(
        estimator=xbg.XGBRegressor(**params_fixed, random_state=1),
        param_grid=params_grid,
        cv=5,
        scoring='neg_mean_squared_log_error'
    )

    bst_grid.fit(x_train, y_train_num)
    print("time is ")
    print(i)
    print("Best score: %0.3f" % bst_grid.best_score_)

    print("the best parameter is :")
    print(bst_grid.best_params_.items())

# y_train_num = y_train[:, 2]
#
# params_grid = {
#     'max_depth': range(6, 15, 2),
#     'n_estimators': range(10, 300, 50),
#     'learning_rate': [0.0005, 0.001, 0.01, 0.1, 0.5, 0.8, 1]
# }
# params_fixed = {
#     'objective': 'reg:linear',
#     'silent': True
# }
# bst_grid = GridSearchCV(
#     estimator=xbg.XGBRegressor(**params_fixed, random_state=1),
#     param_grid=params_grid,
#     cv=5,
#     scoring='neg_mean_squared_log_error'
# )
#
# bst_grid.fit(x_train, y_train_num)
#
# print("the best parameter is :")
# print(bst_grid.best_params_.items())
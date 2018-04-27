# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 19:36
# @Author  : LeonHardt
# @File    : parameter_lbgm.py

import os
import numpy as np
import pandas
import lightgbm as lgb

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from scoring_test import evalerror
if __name__=='__main__':
    path = os.getcwd() + '/data_app/'
    save_path = os.getcwd() + '/predict/'
    if os.path.exists(save_path) is False:
        os.makedirs(save_path)

    x_train = np.loadtxt(path+'x_train_mean_nan_error3.txt', delimiter=',', dtype='float')
    y_train = np.loadtxt(path+'y_train_mean_nan_error3.txt', delimiter=',', dtype='float')
    for i in [4]:
        y_train_num = y_train[:, i]

        params_grid = {
            # 'n_estimators': range(10, 170, 10),
            #  'num_leaves': range(45, 70, 2)
            'learning_rate': [0.005,  0.01, 0.05, 0.1, 0.2],
            # 'gamma': [0.3, 0.4, 0.5, 0.6, 0.7],
            # 'subsample': [0.7, 0.8, 1],
            # "min_child_weight": [1, 2, 3, 4, 5]
            # 'colsample_bytree': [0.7, 0.8, 0.9, 1]
            # 'reg_alpha': [0, 0.05, 0.1, 1, 2, 3],
            # 'reg_lambda': [0, 0.05, 0.1, 1, 2, 3]
        }
        params_fixed = {
            'objective': 'regression',
            'n_estimators': 150,
            'max_depth': -1,
            'num_leaves': 51,
            'learning_rate': 0.05,
            'min_child_weight': 1,
            'colsample_bytree': 0.7,
            'reg_alpha': 2,
            'reg_lambda': 3

        }
        bst_grid = GridSearchCV(
            estimator=lgb.LGBMRegressor(**params_fixed, random_state=1),
            param_grid=params_grid,
            cv=5,
            scoring='neg_mean_squared_log_error',
            n_jobs=-1,

            )

        bst_grid.fit(x_train, y_train_num)
        print("time is ")
        print(i)
        print("Best score: %0.3f" % bst_grid.best_score_)

        print("the best parameter is :")
        print(bst_grid.best_params_.items())

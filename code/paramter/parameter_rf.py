# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 21:55
# @Author  : LeonHardt
# @File    : parameter_rf.py

import os
import numpy as np
import pandas
import lightgbm as lgb

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestRegressor
from scoring_test import evalerror
if __name__=='__main__':
    path = os.getcwd() + '/data_app/'
    save_path = os.getcwd() + '/predict/'
    if os.path.exists(save_path) is False:
        os.makedirs(save_path)

    x_train_2 = np.loadtxt(path + 'x_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')
    y_train_2 = np.loadtxt(path + 'y_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')


    imp2 = Imputer(missing_values='NaN', strategy='median', axis=1)
    imp2.fit(x_train_2)
    x_train_pred2 = imp2.transform(x_train_2)

    for i in [1]:
        y_train_num = y_train_2

        params_grid = {
            'n_estimators': range(50, 1000, 200),
            #  'num_leaves': range(67, 100, 2)
            # 'learning_rate': [0.005,  0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1, 0.2, 0.3],
            # 'gamma': [0.3, 0.4, 0.5, 0.6, 0.7],
            # 'subsample': [0.7, 0.8, 1],
            # "min_child_weight": [1, 2, 3, 4, 5],
            # 'colsample_bytree': [0.7, 0.8, 0.9, 1]
            # 'reg_alpha': [0, 0.05, 0.1, 1, 2, 3],
            # 'reg_lambda': [0, 0.05, 0.1, 1, 2, 3]
        }
        params_fixed = {
            # 'objective': 'regression',
            # 'n_estimators': 239,
            # 'max_depth': -1,
            # 'num_leaves': 85,
            # # 'learning_rate': 0.03,
            # 'min_child_weight': 1,
            # 'colsample_bytree': 0.7,
            # 'reg_alpha': 2,
            # 'reg_lambda': 3

        }
        bst_grid = GridSearchCV(
            estimator=RandomForestRegressor(**params_fixed, random_state=1),
            param_grid=params_grid,
            cv=5,
            scoring='neg_mean_squared_log_error',
            n_jobs=-1,

            )

        bst_grid.fit(x_train_pred2, y_train_num)
        print("time is ")
        print(i)
        print("Best score: %0.3f" % bst_grid.best_score_)

        print("the best parameter is :")
        print(bst_grid.best_params_.items())


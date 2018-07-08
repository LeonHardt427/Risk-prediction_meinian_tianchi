# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 18:40
# @Author  : LeonHardt
# @File    : part_parameter_lgb.py


import os
import numpy as np
import pandas
import lightgbm as lgb

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from scoring_test import evalerror
if __name__ == '__main__':
    path = os.getcwd() + '/data_part/'
    i = 4
    x_train = np.loadtxt(path+'x_train'+str(i)+'_change4_error.txt', delimiter=',', dtype='float')
    y_train = np.loadtxt(path+'y_train'+str(i)+'_change4_error.txt', delimiter=',', dtype='float')
    params_grid = {
        # 'n_estimators': range(400, 440, 3),
         'num_leaves': range(64, 85, 3)
        # 'learning_rate': [0.005,  0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1, 0.2, 0.3],
        # 'gamma': [0.3, 0.4, 0.5, 0.6, 0.7],
        # 'subsample': [0.7, 0.8, 1],
        # "min_child_weight": [1, 2, 3, 4, 5],
        # 'colsample_bytree': [0.7, 0.8, 0.9, 1]
        # 'reg_alpha': [0, 0.05, 0.1, 1, 2, 3],
        # 'reg_lambda': [0, 0.05, 0.1, 1, 2, 3]
    }
    params_fixed = {
        'objective': 'regression',
        'n_estimators': 406,
        'max_depth': -1,
        'num_leaves': 79,
        'learning_rate': 0.05,
        'min_child_weight': 1,
        'colsample_bytree': 0.7,
        'reg_alpha': 1,
        'reg_lambda': 1

    }
    bst_grid = GridSearchCV(
        estimator=lgb.LGBMRegressor(**params_fixed, random_state=1),
        param_grid=params_grid,
        cv=5,
        scoring='neg_mean_squared_log_error',
        n_jobs=-1,

        )

    bst_grid.fit(x_train, y_train)
    print("time is ")
    print(i)
    print("Best score: %0.3f" % bst_grid.best_score_)

    print("the best parameter is :")
    print(bst_grid.best_params_.items())

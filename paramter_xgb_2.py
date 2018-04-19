# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 9:25
# @Author  : LeonHardt
# @File    : paramter_xgb_2.py


import os
import numpy as np
import pandas

import xgboost as xbg

from sklearn.model_selection import GridSearchCV, StratifiedKFold

path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train.txt', delimiter=',', dtype='float')
y_train_num = y_train[:, 4]

params_grid = {
    'max_depth': range(6, 13, 2),
    'n_estimators': range(10, 211, 40),
    'learning_rate': np.linspace(1e-16, 1, 8)
}
params_fixed = {
    'objective': 'reg:linear',
    'silent': True
}
bst_grid = GridSearchCV(
    estimator=xbg.XGBRegressor(**params_fixed, random_state=1),
    param_grid=params_grid,
    cv=5,
    scoring='neg_mean_squared_error'
)

bst_grid.fit(x_train, y_train_num)

print("the bset parameter 1 is :")
print(bst_grid.best_params_.items())
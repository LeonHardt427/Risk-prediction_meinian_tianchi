# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 18:49
# @Author  : LeonHardt
# @File    : predictor_lbgm.py

import os
import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from scoring_test import evalerror

# load or create your dataset
print('Load data...')
path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train_nan_error3_change3.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train_nan_error3_change3.txt', delimiter=',', dtype='float')
x_test = np.loadtxt(path+'x_test_nan_error3_change3.txt', delimiter=',', dtype='float')


print('Start training...')
# train
gbm0 = lgb.LGBMRegressor(objective='regression', num_leaves=57, learning_rate=0.05, n_estimators=195,
                         min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
gbm0.fit(x_train, y_train[:, 0], eval_metric=evalerror)
pred0 = gbm0.predict(x_test)
prediction = pred0

gbm1 = lgb.LGBMRegressor(objective='regression', num_leaves=45, learning_rate=0.05, n_estimators=156,
                         min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
gbm1.fit(x_train, y_train[:, 1], eval_metric=evalerror)
pred1 = gbm1.predict(x_test)
prediction = np.vstack((prediction, pred1))

gbm2 = lgb.LGBMRegressor(objective='regression', num_leaves=57, learning_rate=0.05, n_estimators=183,
                         min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
gbm2.fit(x_train, y_train[:, 2], eval_metric=evalerror)
pred2 = gbm2.predict(x_test)
prediction = np.vstack((prediction, pred2))

gbm3 = lgb.LGBMRegressor(objective='regression', num_leaves=59, learning_rate=0.05, n_estimators=515,
                         min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
gbm3.fit(x_train, y_train[:, 3], eval_metric=evalerror)
pred3 = gbm3.predict(x_test)
prediction = np.vstack((prediction, pred3))

gbm4 = lgb.LGBMRegressor(objective='regression', num_leaves=73, learning_rate=0.04, n_estimators=305,
                         min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
gbm4.fit(x_train, y_train[:, 4], eval_metric=evalerror)
pred4 = gbm4.predict(x_test)
prediction = np.vstack((prediction, pred4))

prediction = prediction.T
np.savetxt(save_path+'prediction_gbm_nan_change3_error31.txt', prediction, fmt='%.3e',  delimiter=',')


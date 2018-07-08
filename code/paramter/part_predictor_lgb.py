# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 20:32
# @Author  : LeonHardt
# @File    : part_predictor_lgb.py

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import KFold
import lightgbm as lgb
import xgboost as xgb
from scoring_test import calc_logloss, evalerror, single_logloss
from sklearn.preprocessing import Imputer, Normalizer
from sklearn.ensemble import RandomForestRegressor,ExtraTreesRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# load or create your dataset
summary = []
prediction = []
x_test = np.loadtxt(os.getcwd()+'/data_app/x_test_nan_change4_b.txt', delimiter=',', dtype='float')
for num in range(5):
    print('The {} prediction...'.format(num))
    path = os.getcwd() + '/data_part/'
    x_train = np.loadtxt(path+'x_train'+str(num)+'_change4_error.txt', delimiter=',', dtype='float')
    y_train = np.loadtxt(path+'y_train'+str(num)+'_change4_error.txt', delimiter=',', dtype='float')
    score = []
    if num == 0:
        gbm0 = lgb.LGBMRegressor(objective='regression', num_leaves=55, learning_rate=0.05,
                                 # n_estimators=220,
                                 n_estimators=500,
                                 min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
        gbm0.fit(x_train, y_train, eval_metric=evalerror)
        pred0 = gbm0.predict(x_test)
        prediction = pred0
    elif num == 1:
        gbm1 = lgb.LGBMRegressor(objective='regression', num_leaves=55, learning_rate=0.05,
                                 # n_estimators=176,
                                 n_estimators=500,
                                 min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
        gbm1.fit(x_train, y_train, eval_metric=evalerror)
        pred1 = gbm1.predict(x_test)
        prediction = np.vstack((prediction, pred1))
    elif num == 2:
        gbm2 = lgb.LGBMRegressor(objective='regression', num_leaves=85, learning_rate=0.05,
                                 # n_estimators=186,
                                 n_estimators=500,
                                 min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
        gbm2.fit(x_train, y_train, eval_metric=evalerror)
        pred2 = gbm2.predict(x_test)
        prediction = np.vstack((prediction, pred2))
    elif num == 3:
        gbm3 = lgb.LGBMRegressor(objective='regression', num_leaves=76, learning_rate=0.05,
                                 # n_estimators=421,
                                 n_estimators=500,
                                 min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
        gbm3.fit(x_train, y_train, eval_metric=evalerror)
        pred3 = gbm3.predict(x_test)
        prediction = np.vstack((prediction, pred3))
    elif num == 4:
        gbm4 = lgb.LGBMRegressor(objective='regression', num_leaves=79, learning_rate=0.05,
                                 # n_estimators=406,
                                 n_estimators=500,
                                 min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
        gbm4.fit(x_train, y_train, eval_metric=evalerror)
        pred4 = gbm4.predict(x_test)
        prediction = np.vstack((prediction, pred4))

save_path = os.getcwd() + '/predict/b/'
prediction = prediction.T
np.savetxt(save_path+'prediction_gbm_part_change4_error_b2.txt', prediction, fmt='%.3f',  delimiter=',')
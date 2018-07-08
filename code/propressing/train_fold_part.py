# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:38
# @Author  : LeonHardt
# @File    : train_fold_part.py

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

for num in range(5):
    print('The {} test...'.format(num))
    path = os.getcwd() + '/data_part/'
    x_train = np.loadtxt(path+'x_train'+str(num)+'_change4_error.txt', delimiter=',', dtype='float')
    y_train = np.loadtxt(path+'y_train'+str(num)+'_change4_error.txt', delimiter=',', dtype='float')

    #
    # imp2 = Imputer(missing_values='NaN', strategy='median', axis=1)
    # imp2.fit(x_train_2)
    # x_train_pred2 = imp2.transform(x_train_2)怒目而视
    # # x_test1_pred2 = imp2.transform(x_test)

    # nor1 = Normalizer()
    # x_train1 = nor1.fit_transform(x_train1)

    # nor2 = Normalizer())
    print('Testing data...')
    fold = KFold(n_splits=5, shuffle=True, random_state=1)
    prediction = []
    score = []
    for i, (train_index, test_index) in enumerate(fold.split(x_train, y_train)):
        # print("{} is start".format(i))

        data_train, data_test = x_train[train_index, :], x_train[test_index, :]
        label_train, label_test = y_train[train_index], y_train[test_index]

    # ----------------------------------- lgb
        if num == 0:
            gbm0 = lgb.LGBMRegressor(objective='regression', num_leaves=55, learning_rate=0.05,
                                     n_estimators=143,
                                     min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
            gbm0.fit(data_train, label_train, eval_metric=evalerror)
            pred0 = gbm0.predict(data_test)
            prediction = pred0
        elif num == 1:
            gbm1 = lgb.LGBMRegressor(objective='regression', num_leaves=55, learning_rate=0.05,
                                     n_estimators=208,
                                     min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
            gbm1.fit(data_train, label_train, eval_metric=evalerror)
            pred1 = gbm1.predict(data_test)
            prediction = pred1
        elif num == 2:
            gbm2 = lgb.LGBMRegressor(objective='regression', num_leaves=85, learning_rate=0.05,
                                     n_estimators=213,
                                     min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
            gbm2.fit(data_train, label_train, eval_metric=evalerror)
            pred2 = gbm2.predict(data_test)
            prediction = pred2
        elif num == 3:
            gbm3 = lgb.LGBMRegressor(objective='regression', num_leaves=61, learning_rate=0.05,
                                     n_estimators=384,
                                     min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
            gbm3.fit(data_train, label_train, eval_metric=evalerror)
            pred3 = gbm3.predict(data_test)
            prediction = pred3
        elif num == 4:
            gbm4 = lgb.LGBMRegressor(objective='regression', num_leaves=58, learning_rate=0.05,
                                     n_estimators=412,
                                     min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
            gbm4.fit(data_train, label_train, eval_metric=evalerror)
            pred4 = gbm4.predict(data_test)
            prediction = pred4
        else:
            print("No files")
    # # ----------------------------------- xgb
    #     xlf0 = xgb.XGBRegressor(max_depth=4, learning_rate=0.1, n_estimators=160, subsample=0.8, silent=True, gamma=0.2,
    #                             objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=0, reg_lambda=1)
    #     xlf0.fit(data_train, label_train[:, 0], eval_metric=evalerror)
    #     pred1 = xlf0.predict(data_test)
    #     prediction = pred1
    #
    #     xlf1 = xgb.XGBRegressor(max_depth=4, learning_rate=0.1, n_estimators=170, subsample=1, gamma=0.7, silent=True,
    #                             objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=3, reg_lambda=1)
    #     xlf1.fit(data_train, label_train[:, 1], eval_metric=evalerror)
    #     pred2 = xlf1.predict(data_test)
    #     prediction = np.vstack((prediction, pred2))
    #
    #     xlf2 = xgb.XGBRegressor(max_depth=6, learning_rate=0.075, n_estimators=50, subsample=0.8, silent=True, gamma=0.4,
    #                             objective='reg:linear', min_child_weight=4, colsample_bytree=0.7, reg_alpha=0, reg_lambda=1)
    #     xlf2.fit(data_train, label_train[:, 2], eval_metric=evalerror)
    #     pred3 = xlf2.predict(data_test)
    #     prediction = np.vstack((prediction, pred3))
    #
    #     xlf3 = xgb.XGBRegressor(max_depth=10, learning_rate=0.025, n_estimators=230, subsample=0.7, silent=True, gamma=0.1,
    #                             objective='reg:linear', min_child_weight=1, colsample_bytree=1, reg_alpha=0, reg_lambda=1)
    #     xlf3.fit(data_train, label_train[:, 3], eval_metric=evalerror)
    #     pred4 = xlf3.predict(data_test)
    #     prediction = np.vstack((prediction, pred4))
    #
    #     xlf4 = xgb.XGBRegressor(max_depth=8, learning_rate=0.05, n_estimators=210, subsample=0.7, silent=True, gamma=0.1,
    #                             objective='reg:linear', min_child_weight=3, colsample_bytree=1, reg_alpha=2, reg_lambda=3)
    #     xlf4.fit(data_train, label_train[:, 4], eval_metric=evalerror)
    #     pred5 = xlf4.predict(data_test)
    #     prediction = np.vstack((prediction, pred5))

        df_test = pd.DataFrame(data=label_test)
        df_pred = pd.DataFrame(data=prediction)

        temp = single_logloss(df_test, df_pred)
        score.append(temp)
    summ = np.mean(score)
    print(" The {0} loss is {1}".format(num, summ))
    summary.append(summ)
print("summaty: {}".format(summary))
mean_loss = np.mean(summary)
print("The whole loss is {}".format(mean_loss))



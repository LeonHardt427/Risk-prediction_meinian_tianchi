# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 17:42
# @Author  : LeonHardt
# @File    : train_scoring.py

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import KFold
import lightgbm as lgb
import xgboost as xgb
from scoring_test import calc_logloss, evalerror
from sklearn.preprocessing import Imputer, Normalizer
from sklearn.ensemble import RandomForestRegressor,ExtraTreesRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# load or create your dataset
print('Load data...')
path = os.getcwd() + '/data_app/'
x_train = np.loadtxt(path+'x_train_nan_error3_change.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train_nan_error3_change.txt', delimiter=',', dtype='float')

x_train_2 = np.loadtxt(path+'x_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')
y_train_2 = np.loadtxt(path+'y_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')



# imp1 = Imputer(missing_values='NaN', strategy='median', axis=1)
# imp1.fit(x_train)
# x_train1 = imp1.transform(x_train)
# # x_test1 = imp1.transform(x_test)
#
# imp2 = Imputer(missing_values='NaN', strategy='median', axis=1)
# imp2.fit(x_train_2)
# x_train_pred2 = imp2.transform(x_train_2)
# # x_test1_pred2 = imp2.transform(x_test)

# nor1 = Normalizer()
# x_train1 = nor1.fit_transform(x_train1)

# nor2 = Normalizer())

fold = KFold(n_splits=5, shuffle=True, random_state=1)
prediction = []
score = []
for i, (train_index, test_index) in enumerate(fold.split(x_train, y_train)):
    print("{} is start".format(i))
    # data_train, data_test = x_train1[train_index, :], x_train1[test_index, :]
    # label_train, label_test = y_train[train_index], y_train[test_index]

    data_train, data_test = x_train[train_index, :], x_train[test_index, :]
    label_train, label_test = y_train[train_index], y_train[test_index]

    # data_train, data_test = x_train_2[train_index, :], x_train_2[test_index, :]
    # label_train, label_test = y_train_2[train_index], y_train_2[test_index]


# ----------------------------------- lgb
    gbm0 = lgb.LGBMRegressor(objective='regression', boosting_type="gbdt", num_leaves=57, learning_rate=0.05,
                             n_estimators=195, min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    gbm0.fit(data_train, label_train[:, 0])
    pred0 = gbm0.predict(data_test)
    prediction = pred0

    gbm1 = lgb.LGBMRegressor(objective='regression', boosting_type='gbdt', num_leaves=45, learning_rate=0.05,
                             n_estimators=156,
                             min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    gbm1.fit(data_train, label_train[:, 1])
    pred1 = gbm1.predict(data_test)
    prediction = np.vstack((prediction, pred1))

    gbm2 = lgb.LGBMRegressor(objective='regression', boosting_type='gbdt', num_leaves=57, learning_rate=0.05,
                             n_estimators=183,
                             min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    gbm2.fit(data_train, label_train[:, 2])
    pred2 = gbm2.predict(data_test)
    prediction = np.vstack((prediction, pred2))

    gbm3 = lgb.LGBMRegressor(objective='regression', boosting_type='gbdt', num_leaves=59, learning_rate=0.05,
                             n_estimators=515,
                             min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    gbm3.fit(data_train, label_train[:, 3])
    pred3 = gbm3.predict(data_test)
    prediction = np.vstack((prediction, pred3))

    gbm4 = lgb.LGBMRegressor(objective='regression', boosting_type='gbdt', num_leaves=73, learning_rate=0.04,
                             n_estimators=305,
                             min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    gbm4.fit(data_train, label_train[:, 4])
    pred4 = gbm4.predict(data_test)
    prediction = np.vstack((prediction, pred4))
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


    # gbm2 = lgb.LGBMRegressor(objective='regression', num_leaves=85, learning_rate=0.03, n_estimators=239,
    #                          min_child_weight=1, colsample_bytree=0.7, reg_lambda=3, reg_alpha=2)
    # # xlf2 = xgb.XGBRegressor(max_depth=6, learning_rate=0.075, n_estimators=50, subsample=0.8, silent=True, gamma=0.4,
    #                         objective='reg:linear', min_child_weight=4, colsample_bytree=0.7, reg_alpha=0, reg_lambda=1)
    # xlf2.fit(data_train, label_train, eval_metric=evalerror)
    # ext = ExtraTreesRegressor(n_estimators=100)
    # gbm2.fit(data_train, label_train)
    # pred2 = gbm2.predict(data_test)
    # prediction = pred2

    # rf0 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # rf0.fit(data_train, label_train[:, 0])
    # pred0 = rf0.predict(data_test)
    # prediction = pred0
    #
    # rf1 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # rf1.fit(data_train, label_train[:, 0])
    # pred1 = rf1.predict(data_test)
    # prediction = np.vstack((prediction, pred1))
    #
    # rf1 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # rf1.fit(data_train, label_train[:, 0])
    # pred1 = rf1.predict(data_test)
    # prediction = np.vstack((prediction, pred1))
    # # rf2 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # # rf2.fit(x_train_pred2, y_train_2)  # train 2
    # # pred2 = rf2.predict(x_test1)
    # # prediction = np.vstack((prediction, pred2))
    #
    # rf3 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # rf3.fit(data_train, label_train[:, 0])
    # pred3 = rf3.predict(data_test)
    # prediction = np.vstack((prediction, pred3))
    #
    # rf4 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
    # rf4.fit(data_train, label_train[:, 0])
    # pred4 = rf4.predict(data_test)
    # prediction = np.vstack((prediction, pred4))
    #
    prediction = prediction.T
# clean predictiuon
    df_test = pd.DataFrame(data=label_test)
    df_pred = pd.DataFrame(data=prediction)

    temp = calc_logloss(df_test, df_pred)
    score.append(temp)

print(np.mean(score))




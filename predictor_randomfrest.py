# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 16:47
# @Author  : LeonHardt
# @File    : predictor_randomfrest.py

import os
import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from scoring_test import evalerror
from sklearn.preprocessing import Imputer

# load or create your dataset
print('Load data...')
path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train_nan_error3_change.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train_nan_error3_change.txt', delimiter=',', dtype='float')
x_test = np.loadtxt(path+'x_test_nan_error3_change.txt', delimiter=',', dtype='float')

x_train_2 = np.loadtxt(path+'x_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')
y_train_2 = np.loadtxt(path+'y_train_nan_error3_change_pred21.txt', delimiter=',', dtype='float')

imp1 = Imputer(missing_values='NaN', strategy='median', axis=1)
imp1.fit(x_train)
x_train1 = imp1.transform(x_train)
x_test1 = imp1.transform(x_test)

imp2 = Imputer(missing_values='NaN', strategy='median', axis=1)
imp2.fit(x_train_2)
x_train_pred2 = imp2.transform(x_train_2)
x_test1_pred2 = imp2.transform(x_test)

print('Start training...')
# train
rf0 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
rf0.fit(x_train1, y_train[:, 0])
pred0 = rf0.predict(x_test1)
prediction = pred0

rf1 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
rf1.fit(x_train1, y_train[:, 1])
pred1 = rf1.predict(x_test1_pred2)
prediction = np.vstack((prediction, pred1))

rf2 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
rf2.fit(x_train_pred2, y_train_2)   # train 2
pred2 = rf2.predict(x_test1)
prediction = np.vstack((prediction, pred2))

rf3 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
rf3.fit(x_train1, y_train[:, 3])
pred3 = rf3.predict(x_test1)
prediction = np.vstack((prediction, pred3))

rf4 = RandomForestRegressor(n_estimators=400, n_jobs=-1)
rf4.fit(x_train1, y_train[:, 4])
pred4 = rf4.predict(x_test1)
prediction = np.vstack((prediction, pred4))

prediction = prediction.T
np.savetxt(save_path+'prediction_rf_medium_change_error3_pred21.txt', prediction, fmt='%.3e',  delimiter=',')

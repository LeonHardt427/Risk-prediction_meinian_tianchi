# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 12:37
# @Author  : LeonHardt
# @File    : predictor_svm.py

import os
import numpy as np
import pandas as pd

from sklearn.svm import SVR

path = os.getcwd() + '/data_app/'
save_path = os.getcwd() + '/predict/'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

x_train = np.loadtxt(path+'x_train.txt', delimiter=',', dtype='float')
y_train = np.loadtxt(path+'y_train.txt', delimiter=',', dtype='float')
x_test = np.loadtxt(path+'x_test.txt', delimiter=',', dtype='float')

# xlf = xgb.XGBRegressor(max_depth=10, learning_rate=0.1, silent=True, objective='reg:gamma',
#                       nthread=-1, gamma=0, min_child_weight=1, max_delta_step=0, subsample=0.85, colsample_bytree=0.7,
#                        colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=1440, missing=None)

predicor = SVR(kernel='rbf', C=400, gamma=0.1)
# print(y_train.shape)

predicor.fit(x_train, y_train[:, 0])
pred1 = predicor.predict(x_test)
prediction = pred1

predicor.fit(x_train, y_train[:, 1])
pred2 = predicor.predict(x_test)
prediction = np.vstack((prediction, pred2))

predicor.fit(x_train, y_train[:, 2])
pred3 = predicor.predict(x_test)
prediction = np.vstack((prediction, pred3))

predicor.fit(x_train, y_train[:, 3])
pred4 = predicor.predict(x_test)
prediction = np.vstack((prediction, pred4))

predicor.fit(x_train, y_train[:, 4])
pred5 = predicor.predict(x_test)
prediction = np.vstack((prediction, pred5))

prediction = prediction.T
np.savetxt(save_path+'prediction_svm1.txt', prediction, fmt='%.3e',  delimiter=',')

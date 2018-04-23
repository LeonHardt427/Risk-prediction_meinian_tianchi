# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 15:38
# @Author  : LeonHardt
# @File    : feature_selection4.py

import os
import pandas as pd
# 手动选择特征作为基本特征并将数据粘连

path = os.getcwd() + "/data_std/"

df1 = pd.read_csv(path+"data_tidy1.csv", delimiter=',', index_col=0, encoding="gbk")
df2 = pd.read_csv(path+"data_tidy2.csv", delimiter=',', index_col=0, encoding="gbk")
# part 1 539-妇科  102-脂肪肝
# col1 = ['2403', '2403', '2405', '2420', '1321', '1322', '1325', '1326', '2406', '1319', '1320', '539', '0102']
col1 = ['2403', '2404', '2405', '2420', '3601', '0102', '0539', '0121', 'A705', '4001', '0409', '0424', '1321',
        '1322', '2406']
col2 = ['100005', '100007', '31', '314', '315', '316', '317', '319', '32', '320', '33', '34', '37', '38', '39', '1840',
        '3193', '3399', '1850', '10004', '190', '191', '2333', '2372', '10003', '1115', '1117',
        '1814', '1815', '183', '1845', '192', '193', '2174', '100006']
df1_1 = df1.loc[:, col1]
print(df1_1)
df2_2 = df2.loc[:, col2]

df1_1 = df1_1.fillna(0.0)
df2_2 = df2_2.fillna(0.0)

# ----------------------deal df1-------------------------------------------
# col = 3601
for ind in df1_1.index:
    temp = str(df1_1.loc[ind, '3601'])
    if "严重" in temp:
        df1_1.loc[ind, '3601'] = 1
    elif "中度" in temp:
        df1_1.loc[ind, '3601'] = 0.7
    else:
        if "减少" in temp or "降低" in temp :
            df1_1.loc[ind, '3601'] = 0.3
        else:
            df1_1.loc[ind, '3601'] = 0.0

# col = 102
for ind in df1_1.index:
    temp = str(df1_1.loc[ind, '0102'])
    print(temp)
    if "脂肪" in temp:
        if "重" in temp:
            df1_1.loc[ind, '0102'] = 1
        elif "中" in temp:
            df1_1.loc[ind, '0102'] = 0.7
        elif "轻" in temp:
            df1_1.loc[ind, '0102'] = 0.3
        else:
            df1_1.loc[ind, '0102'] = 0.0
    else:
            df1_1.loc[ind, '0102'] = 0.0


# col = 539
for ind in df1_1.index:
    temp = df1_1.loc[ind, '0539']
    print(temp)
    if temp != 0:
        df1_1.loc[ind, '0539'] = 1

# col = 121
for ind in df1_1.index:
    temp = df1_1.loc[ind, '0121']
    if temp == 0:
        pass
    else:
        df1_1.loc[ind, '0539'] = 1

# col = A705
for ind in df1_1.index:
    temp = df1_1.loc[ind, 'A705']
    if "脂肪" in str(temp):
        df1_1.loc[ind, 'A705'] = 1
    else:
        df1_1.loc[ind, 'A705'] = 0

# col = 4001
for ind in df1_1.index:
    temp = df1_1.loc[ind, '4001']
    if "重度" in str(temp):
        df1_1.loc[ind, '4001'] = 1
    elif "中度" in str(temp):
        df1_1.loc[ind, '4001'] = 0.7
    elif "轻度" in str(temp):
        df1_1.loc[ind, '4001'] = 0.3
    else:
        df1_1.loc[ind, '4001'] = 0.0

# col = 409
for ind in df1_1.index:
    temp = df1_1.loc[ind, '0409']
    if "血压" in str(temp):
        df1_1.loc[ind, '0409'] = 1
    elif "糖尿病" in str(temp):
        df1_1.loc[ind, '0409'] = 2
    elif "脂肪肝" in str(temp):
        df1_1.loc[ind, '0409'] = 3
    else:
        df1_1.loc[ind, '0409'] = 0.0

# col = 424
for ind in df1_1.index:
    temp = df1_1.loc[ind, '0424']
    if "过缓" in str(temp):
        df1_1.loc[ind, '0424'] = 50
    elif "次" in str(temp):
        df1_1.loc[ind, '0424'] = 70
    else:
        df1_1.loc[ind, '0424'] = 0.0

for ind in df1_1.index:
    for cols in ['1321', '1322']:
        if df1_1.loc[ind, cols] == "未查":
            df1_1.loc[ind, cols] = 0

df1_1.drop(["0121"], axis=1, inplace=True)

# ------------------------------deal df2-------------------------------------------
# col = 3399
for ind in df2_2.index:
    temp = df2_2.loc[ind, '3399']
    if "淡黄色" in str(temp):
        temp = df2_2.loc[ind, '3399'] = 1
    else:
        temp = df2_2.loc[ind, '3399'] = 0


df_whole = df1_1.join(df2_2)

df_whole.to_csv(path+'data_whole_new.csv', sep=',')



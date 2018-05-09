# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 9:05
# @Author  : LeonHardt
# @File    : propressing.py

import os
import numpy as np
import pandas as pd

path = os.getcwd() + '/data_orginal/'
data1 = pd.read_table(path+'meinian_round1_data_part1_20180408.txt', encoding='UTF8', delimiter='$')
print(data1)
vid1 = []
table_id1 = []
for index in data1.index:
    temp_vid = data1.loc[index, 'vid']
    temp_table = data1.loc[index, 'table_id']
    if temp_vid in vid1 is False:
        vid1.append(temp_vid)
    if temp_table in table_id1 is False:
        table_id1.append(temp_table)
data_sheet1 = pd.DataFrame(index=vid1, columns=table_id1)
for index in data1.index:
    ind = data1.loc[index, 'vid']
    col = data1.loc[index, 'table_id']
    value = data1.loc[index, 'field_results']
    data_sheet1.loc[ind, col] = value
data_sheet1.to_csv('test1.csv', sep=',')


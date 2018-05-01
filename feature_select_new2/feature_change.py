# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 11:12
# @Author  : LeonHardt
# @File    : feature_change.py


import os
import pandas as pd
path = os.getcwd() + "/"

df1 = pd.read_csv("data_whole_new3_test.csv", delimiter=',', index_col=0, encoding="gbk")

# col = 3601
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3601']):
        pass
    else:
        temp = str(df1.loc[ind, '3601'])
        if "严重" in temp:
            df1.loc[ind, '3601'] = 4
        elif "中度" in temp:
            df1.loc[ind, '3601'] = 3
        else:
            if "减少" in temp or "降低" in temp:
                df1.loc[ind, '3601'] = 2
            else:
                df1.loc[ind, '3601'] = 1

# col = 0102
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0102']):
        pass
    else:
        temp = str(df1.loc[ind, '0102'])
        value = 0
        print(temp)
        if "脂肪" in temp:
            if "重" in temp:
                value = 4
            elif "中" in temp:
                value = 3
            elif "轻" in temp:
                value = 2
            else:
                value = 1
        else:
            value = 0.0
        if "多发" in temp:
            value += 0.5
        df1.loc[ind, '0102'] = value

# col = 0113
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0113']):
        pass
    else:
        temp = str(df1.loc[ind, '0113'])
        value = 0
        print(temp)
        if "弥漫性" in temp:
            value = 5
        if "欠清晰" in temp:
            value += 2
        if "粗" in temp:
           value += 0.5
        if "多发" in temp:
            value += 0.5
        if "斑点状" in temp:
            value += 1
        if "回声区" in temp:
            value += 1
        df1.loc[ind, '0113'] = value

# col = 0114
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0114']):
        pass
    else:
        temp = df1.loc[ind, '0114']
        value = 0
        print(temp)
        if "毛糙" in temp:
            value = 4
        if "强回声" in temp:
            value += 1
        df1.loc[ind, '0114'] = value

# col = 0115
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0115']):
        pass
    else:
        temp = df1.loc[ind, '0115']
        value = 0
        print(temp)
        if "不清晰" in temp:
            value = 4
        if "增强" in temp:
            value += 1
        df1.loc[ind, '0115'] = value

# col = 0116
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0116']):
        pass
    else:
        temp = df1.loc[ind, '0116']
        value = 0
        print(temp)
        if "不清晰" in temp:
            value = 4
        if "增强" in temp:
            value += 1
        df1.loc[ind, '0116'] = value

# col = 0117
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0117']):
        pass
    else:
        temp = df1.loc[ind, '0117']
        value = 0
        print(temp)
        if "强回声" in temp:
            value = 4
        if "无回声" in temp:
            value += 1
        if "欠均匀" in temp:
            value += 1
        df1.loc[ind, '0117'] = value

# col = 0118
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0118']):
        pass
    else:
        temp = df1.loc[ind, '0118']
        value = 0
        print(temp)
        if "强回声" in temp:
            value = 4
        if "无回声" in temp:
            value += 1
        if "欠均匀" in temp:
            value += 1
        df1.loc[ind, '0118'] = value

# col = 0201 0202 0203
for ind in df1.index:
    for col in ['0201', '0202', '0203', '0501']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未见" in temp:
                value += 1
            else:
                value += 10
            df1.loc[ind, col] = value

# col = 0503
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0503']):
        pass
    else:
        temp = df1.loc[ind, '0503']
        value = 0
        print(temp)
        if "分泌物多" in temp:
            value = 8
        if "分泌物中" in temp:
            value = 5
        if "分泌物少" in temp:
            value = 3
        if "浓性" in temp:
            value += 1
        if "充血" in temp:
            value += 1
        if "黄色" in temp:
            value += 0.5

        df1.loc[ind, '0503'] = value

# col = 0509
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0509']):
        pass
    else:
        temp = df1.loc[ind, '0509']
        value = 0
        print(temp)
        if "充血" in temp:
            value = 8
        if "肥大" in temp:
            value = 5
        if "轻糜" in temp:
            value += 1
        if "中糜" in temp:
            value += 1.5
        if "囊" in temp:
            value += 0.5
        df1.loc[ind, '0509'] = value

# col = 0516
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0516']):
        pass
    else:
        temp = df1.loc[ind, '0516']
        value = 0
        print(temp)
        if "前位" in temp:
            value = 8
        if "后位" in temp:
            value = 5
        if "平位" in temp:
            value = 3
        if "增大" in temp:
            value += 1
        if "硬" in temp:
            value += 0.5
        df1.loc[ind, '0516'] = value
# col = 0537
for ind in df1.index:
    for col in ['0537', '0541']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未见" in temp:
                value += 1
            else:
                value += 10
            df1.loc[ind, col] = value

# col = 0539
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0539']):
        pass
    else:
        temp = df1.loc[ind, '0539']
        value = 0
        print(temp)
        if "分泌物" in temp:
            value += 1
        if "肥大" in temp:
            value += 2
        if "充血" in temp:
            value += 3
        if "炎" in temp:
            value += 0.5

        df1.loc[ind, '0539'] = value

# col = 2302
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2302']):
        pass
    else:
        temp = df1.loc[ind, '2302']
        value = 0
        print(temp)
        if "亚健康" in temp:
            value = 3

        df1.loc[ind, '2302'] = value

# col = 1316
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '1316']):
        pass
    else:
        temp = df1.loc[ind, '1316']
        value = 0
        print(temp)
        if "正常" in temp or "未见" in temp :
           pass
        else:
            if "I" in temp:
                value += 5
            if "II" in temp:
                value += 10
        df1.loc[ind, '1316'] = value

# col = 0101
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0101']):
        pass
    else:
        temp = df1.loc[ind, '0101']
        value = 0
        print(temp)
        if "低回声" in temp or "回声区" in temp:
            value += 1

        df1.loc[ind, '0101'] = value

# col = 0119
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0119']):
        pass
    else:
        temp = df1.loc[ind, '0119']
        value = 0
        print(temp)
        if "欠佳" in temp:
            value = 2

        df1.loc[ind, '0119'] = value

# col = 0121
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0121']):
        pass
    else:
        temp = df1.loc[ind, '0121']
        value = 0
        print(temp)
        if "低回声" in temp or "回声区" in temp:
            value += 1

        df1.loc[ind, '0121'] = value


# col = 0122
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0122']):
        pass
    else:
        temp = df1.loc[ind, '0122']
        value = 0
        print(temp)
        if "回声团" in temp or "回声区" in temp:
            value += 1

        df1.loc[ind, '0122'] = value

# col = 0123
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0123']):
        pass
    else:
        temp = df1.loc[ind, '0123']
        value = 0
        print(temp)
        if "回声团" in temp or "回声区" in temp:
            value += 1

        df1.loc[ind, '0123'] = value

# col = A705
for ind in df1.index:
    if pd.isnull(df1.loc[ind, 'A705']):
        pass
    else:
        temp = df1.loc[ind, 'A705']
        value = 0
        print(temp)
        if "衰减" in temp:
            value += 5

        df1.loc[ind, 'A705'] = value

# col = 0901
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0901']):
        pass
    else:
        temp = df1.loc[ind, '0901']
        value = 0
        print(temp)
        if "未见" in temp:
            value += 0
        else:
            value += 3

        df1.loc[ind, '0901'] = value

# col = 0911
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0911']):
        pass
    else:
        temp = df1.loc[ind, '0911']
        value = 0
        print(temp)
        if "肿大" in temp:
            value += 2

        df1.loc[ind, '0911'] = value

# col = 0912
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0912']):
        pass
    else:
        temp = df1.loc[ind, '0912']
        value = 0
        print(temp)
        if "无肿大" in temp or "未见" in temp:
            pass
        else:
            value += 2

        df1.loc[ind, '0912'] = value

# col = 0929
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0929']):
        pass
    else:
        temp = df1.loc[ind, '0929']
        value = 0
        print(temp)
        if "不全" in temp:
            value = 3
        if "增生" in temp:
            value = 6

        df1.loc[ind, '0929'] = value

# col = 0972
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0972']):
        pass
    else:
        temp = df1.loc[ind, '0972']
        value = 0
        print(temp)
        if "未" in temp or "弃" in temp:
            value += 0
        if "痔" in temp:
            value += 10
        df1.loc[ind, '0972'] = value

# col = A201
for ind in df1.index:
    if pd.isnull(df1.loc[ind, 'A201']):
        pass
    else:
        temp = df1.loc[ind, 'A201']
        value = 0
        print(temp)
        if "胸廓对称" in temp:
            value += 0
        else:
            value += 5
        df1.loc[ind, 'A201'] = value

# col = A202
for ind in df1.index:
    if pd.isnull(df1.loc[ind, 'A202']):
        pass
    else:
        temp = df1.loc[ind, 'A202']
        value = 0
        print(temp)
        if "陈旧" in temp:
            value = 5
        if "灶" in temp:
            value += 1

        df1.loc[ind, 'A202'] = value

# col = 1102
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '1102']):
        pass
    else:
        temp = df1.loc[ind, '1102']
        value = 0
        print(temp)
        if "增生" in temp:
            value += 1
        df1.loc[ind, '1102'] = value

# col = 0208
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0208']):
        pass
    else:
        temp = df1.loc[ind, '0208']
        value = 0
        print(temp)
        if "正常" in temp or "未见" in temp:
            pass
        else:
            value += 1

        df1.loc[ind, '0208'] = value

# col = '206','207', '208', '209', '210', '213'
for ind in df1.index:
    for col in ['0206', '0207', '0209', '0210', '0213']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            try:
                if "正常" in temp or "未见" in temp:
                    pass
                else:
                    value += 1
            except TypeError:
                value = temp

            df1.loc[ind, col] = value

# col = '0215'
for ind in df1.index:
    for col in ['0215']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "充血" in temp:
                value += 15
            if '炎' in temp:
                value += 10
            if '增' in temp:
                value += 5
            df1.loc[ind, col] = value

# col = '0216',  '0218','0219','0220', '0221'
for ind in df1.index:
    for col in ['0216', '0218', '0219','0220', '0221']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未见" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value

# col = 0210
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0210']):
        pass
    else:
        temp = df1.loc[ind, '0210']
        value = 0
        print(temp)
        try:
            if "正常" in temp or "未见" in temp:
                pass
            else:
                value += 1
        except TypeError:
            value = temp
        df1.loc[ind, '0210'] = value


# col = 0217
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0217']):
        pass
    else:
        temp = df1.loc[ind, '0217']
        value = 0
        print(temp)
        try:
            if "正常" in temp or "未见" in temp:
                pass
            else:
                value += 1
            if "肿" in temp:
                value += 5
        except TypeError:
            value =temp
        df1.loc[ind, '0217'] = value

# col = 0222
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0222']):
        pass
    else:
        temp = df1.loc[ind, '0222']
        value = 0
        print(temp)
        if "充血" in temp:
            value += 5
        if "炎" in temp:
            value += 5
        if "正常" in temp or "未见" in temp:
            pass
        else:
            value += 5
        df1.loc[ind, '0222'] = value

# col = 4001
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '4001']):
        pass
    else:
        temp = df1.loc[ind, '4001']
        value = 0
        print(temp)
        if "轻度" in temp:
            value = 3
        if "中度" in temp:
            value = 5
        if "重度" in temp:
            value = 8
        df1.loc[ind, '4001'] = value

# col = 1001
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '1001']):
        pass
    else:
        temp = df1.loc[ind, '1001']
        value = 0
        print(temp)
        if "过缓" in temp or "不齐" in temp or "偏" in temp:
            value += 3
        df1.loc[ind, '1001'] = value

# col = 0403
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0403']):
        pass
    else:
        temp = df1.loc[ind, '0403']
        value = 0
        print(temp)
        if "不大" in temp:
            value += 5

        if "正常" in temp or "未见" in temp:
            pass
        else:
            value += 3
        df1.loc[ind, '0403'] = value
# col = '0405', '0406', '0407','0413','0414', '0420', '0423'
for ind in df1.index:
    for col in ['0405', '0406', '0407','0413', '0414', '0420', '0423']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value
# col = 0409
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0409']):
        pass
    else:
        temp = df1.loc[ind, '0409']
        value = 0
        print(temp)
        if "血压" in temp:
            value += 9
        if "糖尿" in temp:
            value += 3
        if "脂肪" in temp:
            value += 5
        df1.loc[ind, '0409'] = value

# col = 0421
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0421']):
        pass
    else:
        temp = df1.loc[ind, '0421']
        value = 0
        print(temp)
        if "不齐" in temp:
            value += 3

        df1.loc[ind, '0421'] = value

# col = 0424
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0424']):
        pass
    else:
        temp = df1.loc[ind, '0424']
        value = 0
        print(temp)
        if "次" in temp:
            if "70" in temp:
                value = 70
            else:
                value = 80

        df1.loc[ind, '0424'] = value

# col = 0425
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0425']):
        pass
    else:
        temp = df1.loc[ind, '0425']
        value = 0
        print(temp)
        if "正常" in temp:
            value += 1

        df1.loc[ind, '0425'] = value
# col = '0426', '0431', '0433'
for ind in df1.index:
    for col in ['0426', '0431', '0433']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value

# col = 0434
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0434']):
        pass
    else:
        temp = df1.loc[ind, '0434']
        value = 0
        print(temp)
        if "血压" in temp:
            value += 9
        if "糖尿" in temp:
            value += 3
        if "脂肪" in temp:
            value += 5
        if "心" in temp:
            value += 1
        df1.loc[ind, '0434'] = value

# col = '1313', '1314', '1315'
for ind in df1.index:
    for col in ['1313', '1314', '1315']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value

# col = 1402
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '1402']):
        pass
    else:
        temp = df1.loc[ind, '1402']
        value = 0
        print(temp)
        if "硬" in temp:
            value += 15
        if "低" in temp:
            value += 10
        if "慢" in temp:
            value += 5
        df1.loc[ind, '1402'] = value

# col = 0120
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0120']):
        pass
    else:
        temp = df1.loc[ind, '0120']
        value = 0
        print(temp)
        if "强回声" in temp:
            value += 5
        if "低" in temp:
            value += 1

        df1.loc[ind, '0120'] = value
# col = '0981', '0982'
for ind in df1.index:
    for col in ['0981', '0982']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未" in temp or "自述" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value

# col = 0984
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '0984']):
        pass
    else:
        temp = df1.loc[ind, '0984']
        value = 0
        print(temp)
        if "增" in temp:
            value += 5

        df1.loc[ind, '0984'] = value
# col = '0429', '0430', '0432', '0437'
for ind in df1.index:
    for col in ['0429', '0430', '0432', '0435', '0437']:
        if pd.isnull(df1.loc[ind, col]):
            pass
        else:
            temp = df1.loc[ind, col]
            value = 0
            print(temp)
            if "正常" in temp or "未" in temp or "自述" in temp:
                pass
            else:
                value += 5
            df1.loc[ind, col] = value

# col = 100010
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '100010']):
        pass
    else:
        temp = df1.loc[ind, '100010']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1
        df1.loc[ind, '0100010'] = value

# col = 3190
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3190']):
        pass
    else:
        temp = df1.loc[ind, '3190']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1
        df1.loc[ind, '3190'] = value

# col = 3191
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3191']):
        pass
    else:
        temp = df1.loc[ind, '3191']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1

        df1.loc[ind, '3191'] = value

# col = 3192
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3192']):
        pass
    else:
        temp = df1.loc[ind, '3192']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1

        df1.loc[ind, '3192'] = value
# col = 3195
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3195']):
        pass
    else:
        temp = df1.loc[ind, '3195']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1

        df1.loc[ind, '3195'] = value

# col = 3196
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3196']):
        pass
    else:
        temp = df1.loc[ind, '3196']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1

        df1.loc[ind, '3196'] = value

# col = 3197
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3197']):
        pass
    else:
        temp = df1.loc[ind, '3197']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1
        df1.loc[ind, '3197'] = value

# col = 3430
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3430']):
        pass
    else:
        temp = df1.loc[ind, '3430']
        value = 0
        print(temp)
        if "+" in temp:
            value += 5
            if "++" in temp:
                value += 5
            if "+++" in temp:
                value += 5
            if "++++" in temp:
                value += 5
            if "+-" in temp:
                value = 3
        else:
            value += 1

        df1.loc[ind, '3430'] = value
# col = 3399
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3399']):
        pass
    else:
        temp = df1.loc[ind, '3399']
        value = 0
        print(temp)
        if "淡" in temp:
            value += 5
        else:
            value += 1

        df1.loc[ind, '3399'] = value

# col = 30007
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '30007']):
        pass
    else:
        temp = df1.loc[ind, '30007']
        value = 0
        print(temp)
        if "I" in temp:
            value += 5
            if "II" in temp:
                value += 5
            if "III" in temp:
                value += 5
            if "IV" in temp:
                value += 15
        else:
            if "中度" in temp:
                value += 3
            else:
                value = 1

        df1.loc[ind, '30007'] = value

# col = 3485
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3485']):
        pass
    else:
        temp = df1.loc[ind, '3485']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '3485'] = value
# col = 3486
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '3486']):
        pass
    else:
        temp = df1.loc[ind, '3486']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '3486'] = value

# col = 300062
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '300062']):
        pass
    else:
        temp = df1.loc[ind, '300062']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass

        if "+-" in temp:
            value = 9
        df1.loc[ind, '300062'] = value

# col = 2235
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2235']):
        pass
    else:
        temp = df1.loc[ind, '2235']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2235'] = value

# col = 2228
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2228']):
        pass
    else:
        temp = df1.loc[ind, '2228']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2228'] = value

# col = 2229
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2229']):
        pass
    else:
        temp = df1.loc[ind, '2229']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2229'] = value

# col = 2230
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2230']):
        pass
    else:
        temp = df1.loc[ind, '2230']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2230'] = value

# col = 2231
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2231']):
        pass
    else:
        temp = df1.loc[ind, '2231']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2231'] = value

# col = 2233
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '2233']):
        pass
    else:
        temp = df1.loc[ind, '2233']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '2233'] = value
# col = 300018
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '300018']):
        pass
    else:
        temp = df1.loc[ind, '300018']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '300018'] = value

# col = 21A235
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '21A235']):
        pass
    else:
        temp = df1.loc[ind, '21A235']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '21A235'] = value
# col = 21A236
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '21A236']):
        pass
    else:
        temp = df1.loc[ind, '21A236']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '21A236'] = value
# col = 21A237
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '21A237']):
        pass
    else:
        temp = df1.loc[ind, '21A237']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '21A237'] = value
# col = 21A238
for ind in df1.index:
    if pd.isnull(df1.loc[ind, '21A238']):
        pass
    else:
        temp = df1.loc[ind, '21A238']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, '21A238'] = value
# col = I49012
for ind in df1.index:
    if pd.isnull(df1.loc[ind, 'I49012']):
        pass
    else:
        temp = df1.loc[ind, 'I49012']
        value = 0
        print(temp)
        if "阴性" in temp:
            value += 1
        elif "未见" in temp:
            value += 3
        elif "查" in temp:
            value += 6
        elif "+" in temp or "阳性" in temp:
            value += 15
        else:
            pass
        if "+-" in temp:
            value = 9
        df1.loc[ind, 'I49012'] = value


df1.to_csv('data_feature_change3_test.csv', sep=',')
# 美年健康AI大赛—双高疾病风险预测总结
===
author: LeonHardt427
date:2018-06-25
比赛链接：https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100150.711.7.54592784WpUREj&raceId=231654
_____________________
## 1、 比赛成绩（初赛）
队伍名：中药世家 
成绩： *0.0291* 
排名： *60/3152*  
 __________________
## 2、赛题个人思路
赛题通过对样本病历数据的分析，搭建模型进行收缩压、舒张压、甘油三酯、高密度脂蛋白胆固醇和低密度脂蛋白胆固醇这五种指标的预测。

其实赛题的思路还是蛮清晰的，即用已有数据库进行目标数值的预测，属于5个回归类问题。但是真的拿到数据一看，是真的乱。。。将所有的个人病历进行汇总，以所有病人的id为index，以及所有出现过的体检项目编号为column， 制作总体的训练样本，可以清楚地观察到训练样本的全貌以及需要解决的问题。首先，病历的数据字符型与数值型型数据混合。其次，因为每个人检查项目的差异，导致建立的总表缺失数据很多。再之，因为体检医生不一以及中文的博大精深，导致体验病历某些指标的表达没有统一的格式，加大了处理的难度。最后也是因为没有给出具体的体检项目名称，只是用编号代替，所以有许多项目很难知道奇具体含义，无法从医学角度进行病历分析。

初赛开始初期，为了不浪费每一次测评机会，我首先使用的是纯数值的体检结果做为特征训练。训练过程中删除了缺失值超过80%的特征，使用平均数，-1等方法对缺失值进行了填充，同时测试用不同的机器学习方法进行建模。最后发现在不使用缺失值填充的情况下（我个人在此题中倾向于不进行缺失值填充，因为我感觉没体检该项目说明正常），使用lightGBM进行建模，取得了当时条件下最好的效果，得分在0.033左右。在测试了许多次无法提高成绩之后，我再次对训练数据进行仔细的分析，这时发现在官方给的训练样本标签值有很多明显不符合常理的数据，比如收缩压高达900的天外来客。之前都是对特征筛选比较多，完全没想到训练集的标签值会出问题，因此我意识到到对一些异常样本的剔除也十分有必要。我针对五种不同的预测目标，逐一排查异常数据，将过大的数据删除，将边缘化的连续标签进行离散化处理，最终得到了在预测每一个项目的时候的错误数据的训练集病人编号（该过程是手动处理的，每次机器因为内存小崩溃都是一把辛酸泪）。我在训练模型时，针对不同的项目将有问的病人去除，进行预测。这下效果比之前又好了一些，能到0.031左右。在我又一次陷入无法提高成绩的时候，我明白还是逃不掉要对样本进行文本分析处理的任务了。我再次对训练样本进行分析，从中提取出了缺失值较少的文本特征，排除了一些与预测项目无关（例如牙齿检查情况）以及信息含量极少（全部都是无异常）的特征，然后对样本进行了数值化的处理，处理的思想还是对关键字的提取，通过观察得到特征中出现此处比较多的词语，通过检测词语出现情况进行数值变换以及权重增加，最终将有用的文本信息转化成了数值信息。特征词的提取完全是靠自己的观察得到的。最后，通过加入了转化好的特征进行预测，最终达到了该次比赛自己最好的成绩。
_______________________
## 3、Code整理
最后比赛将代码提交到了天池比赛组织方进行测试，在我的github存放在final_code 文件加下。其余文件为比赛做零散的各种测试文件，包括特征处理文件等，不做具体描述。下面对final_code进行解释： 
#### （1）prject结构说明
**project**
|--README.md
|--version.txt
|--data
|--code
&emsp;|-- main.py *(主程序）*
&emsp;|-- evalerror.py *（用于模型训练的损失函数文件）*
&emsp;|-- error0.csv *（训练第0列数据（收缩压）模型时需去除的病人编号标签）*
&emsp;|-- error1.csv *（训练第1列数据（舒张压）模型时需去除的病人编号标签）*
&emsp;|-- error2.csv *（训练第2列数据（血清甘油三酯）模型时需去除的病人编号标签）*
&emsp;|-- error3.csv *（训练第3列数据（血清高密度脂蛋白）模型时需去除的病人编号标签）*
&emsp;|-- error4.csv *（训练第4列数据（血清低密度脂蛋白）模型时需去除的病人编号标签）*
|--submit
&emsp;|-- submit_Ymd_HMS.csv *（提交结果文件）*

#### （2）Main函数逻辑（注释分割与main函数中分割对应）
|----------preprocessing----------
"""
将项目给予的源数据转化成为DataFrame，index为病人的id，columns为检测项目编号，对于空缺的数据使用NaN填充。
将part1的全部以及part2的前625列拼成一个DataFrame，作为预测的原始数据df_whole_new。
"""
|----------feature to  Integer----------
"""
将原始数据逐列进行转换，利用关键词将文字信息转化为可以用于分析的数值信息，直接在df_whole_new上进行变化。
"""
|----------train/test sets  prepare----------
"""
根据所给训练集与测试集的vid将病人特征从df_whole_new中提取出来，然后将数值型的数据进行保留，将无法识别的文字信息删除，用NaN填充。最后得到全为数值型的训练特征集df_train_use，训练标签集df_y_trains，以及测试特征集df_test_use。
针对测试集分析，发现有许多异常数据，对其进行手动的筛选。因为一共有5种标签需要预测，因此针对每一种标签，统计出需要排除的病人vid，保存在了error0--error4共5个文件中。将分别将训练特征集以及训练标签集中对应的异常病人数据剔除，最后得到5组训练特征标签数据集（train0，label0）、...、（train4，label4）
"""
|----------prediction(ligtbgm)----------
利用之前得到的五组训练预测数据集，分别对对应的五个标签进行预测。选用lightbgm作为预测方法。得到预测结果prediction。
|----------submit prepare----------
将prediction整合成为系统要求的csv格式，进行保存上传。
#### （3）重要说明
1、输入为官方解压后的文件
2、程序运行根目录为 "project/code/"
2、error0-error4这五个文件是手动从异常数据中筛选出来的，都是病人vid，保存在code文件中。
________
## 4、比赛总结与感想
这是我第一次做类似的算法比赛，虽然在实验室做了很多机器学习的东西，但是这次真正体会到真实数据与实验室自己科研数据的差异性，也再一次体会到特征才是预测结果最本质的根基。不过也是通过这次比赛，大大提升了自己对数据分析的喜爱。同时这次比赛中基本是自己一个人solo，我也遇到了不少问题，在自己非常困惑的时候得到了麻婆豆腐大佬（大佬主页：https://tianchi.aliyun.com/science/scientistDetail.htm?spm=5176.8366600.0.0.1f0f311flGyuy0&userId=1095279138174 ）的无私指点，也确实体会到了这个圈子大家互相帮助的良好氛围，自己也很想在将来为这个环境的建设尽一份自己的力。

参加比赛还是以学习为主，做多了科研理所当然的觉得数据就是上帝摆放在自己面前的干净数据， 做实际的东西才知道现实处理的样本就像是下水道里掏出来的一样。希望自己能进一步提高水平，才能做得更好。
import jieba
import math
import re,string
import os

def matchText(adr1, adr2):
    #读取txt文件
    try:
        f1 = open(adr1,'r')
        f2 = open(adr2,'r')
        t1 = f1.read()
        t2 = f2.read()
    finally:
        if f1:
            f1.close()
        if f2:
            f2.close()
    #去除标点符号
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“”：’；、。，？》《{}\n \t'
    t1 = re.sub(r"[%s]+" %punc, "",t1)
    t2 = re.sub(r"[%s]+" %punc, "",t2)

    #使用 jieba 分词
    s1_cut = [i for i in jieba.cut(t1, cut_all=True) if i != '']
    s2_cut = [i for i in jieba.cut(t2, cut_all=True) if i != '']

    word_set = set(s1_cut).union(set(s2_cut))

    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1

    s1_cut_code = [word_dict[word] for word in s1_cut]
    s1_cut_code = [0]*len(word_dict)

    for word in s1_cut:
        s1_cut_code[word_dict[word]]+=1

    s2_cut_code = [word_dict[word] for word in s2_cut]

    s2_cut_code = [0]*len(word_dict)
    for word in s2_cut:
        s2_cut_code[word_dict[word]]+=1

    #计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
        sq1 += pow(s1_cut_code[i], 2)
        sq2 += pow(s2_cut_code[i], 2)

    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    
    #输出结果
    print('\n结果：',result)
    path1=os.path.realpath(adr1)
    print('论文原文的绝对路径：')
    print(path1)
    print('抄袭版论文的绝对路径：')
    path2=os.path.realpath(adr2)
    print(path2)
    print('答案文件的绝对路径：')  
    f3 = open('doc/result.txt','a')
    f3.write(str(result))
    f3.write('\n')
    f3.close()
    path3=os.path.realpath('doc/result.txt')
    print(path3)
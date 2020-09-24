from algorithm import matchText
import cProfile
matchText('doc/orig.txt','doc/orig_0.8_add.txt')
matchText('doc/orig.txt','doc/orig_0.8_del.txt')
matchText('doc/orig.txt','doc/orig_0.8_dis_1.txt')
matchText('doc/orig.txt','doc/orig_0.8_dis_10.txt')
matchText('doc/orig.txt','doc/orig_0.8_dis_15.txt')
cProfile.run("matchText('doc/orig.txt','doc/orig_0.8_add.txt')")
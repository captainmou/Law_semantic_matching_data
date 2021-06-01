import pandas as pd
import os
import re
import random
import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

path='./focus_group'
dir_list = os.listdir(path)
focus_list=dir_list
# print('focus_list:',focus_list)

focus_len=[]
for i in focus_list:
    with open(path+'/'+i,'r') as f:
        fi=f.readlines()
        focus_len.append(len(fi))
        # print(i,len(fi))
        f.close()
# print('focus_len:',focus_len)

def gen(focus_len,dir_list,data_in_path,data_out_path='example',n=3):
    rand_num_ran=[sum(focus_len[i:]) for i in range(len(focus_len))]
    rand_num_ran.append(0)
    # print(rand_num_ran)

    with open(data_out_path, 'w', encoding='utf-8') as out:
        while n:
            r1=random.randint(0,rand_num_ran[0]-1)
            r2=random.randint(0,rand_num_ran[0]-1)
            f1=1
            f2=1
            for i in range(len(rand_num_ran)-1):
                # print(rand_num_ran[i],rand_num_ran[i+1],i)
                if rand_num_ran[i]>r1>=rand_num_ran[i+1] and f1:
                    r1=i
                    f1=0
                if rand_num_ran[i]>r2>=rand_num_ran[i+1] and f2:
                    r2=i
                    f2=0
            # print(r1,r2)
            if r1==r2:
                continue
            l1 = focus_len[r1]
            l2 = focus_len[r2]
            # print(l1,l2)
            s={}
            with open(os.path.join(data_in_path,dir_list[r1])) as f1:
                f1=f1.readlines()
                with open(os.path.join(data_in_path, dir_list[r2])) as f2:
                    f2=f2.readlines()
                    r3 = random.randint(0, l1 - 1)
                    r4 = random.randint(0, l1 - 1)
                    r5 = random.randint(0, l2 - 1)
                    # print(r3,r4,r5)
                    s['Q']=f1[r3][:512]
                    s['D1']=f1[r4][:512]
                    s['D2']=f2[r5][:512]
                    # s['Q']=f1[r3][-512:]
                    # s['D1']=f1[r4][-512:]
                    # s['D2']=f2[r5][-512:]

                    print('focus1:'+ dir_list[r1])
                    print(s['Q'])
                    print(s['D1'])
                    print('focus2:'+ dir_list[r2])
                    print(s['D2'])
                    print('\n')
                    json_str = json.dumps(s, ensure_ascii=False)
                    out.write(json_str + '\n')
                    n-=1
                    # print(n)
gen(focus_len,dir_list,path)

# -*- coding: UTF-8 -*-

# Filename : math exercise.py
# author by : （Vivian)
# 说明：出小学数学题
import random
print('-----小学四则运算基础题-----')

filename = "小学四则运算基础题.txt"
f = open(filename, 'w')  # write 方式第一次写一行
text2write = "---开始出题目---\n"
f.write(text2write)

filename = "小学四则运算基础题.txt"
# 向文件追加内容
f = open(filename, 'a') # append 方式读文件

count=0
for row in range(1,21):
    line1 = ""
    for col in range(1,6):
        count=count+1
        a = random.randint(0,99)
        b = random.randint(0,99)
        op = random.randint(1,4)
        if op==1:
            line1 =line1+"%d+%d=\t"%(a,b)
            # print(line1)
        if op==2:
            line1 =line1+"%d-%d=\t"%(a,b)
            # print(line1)
        if op==3:
            line1 =line1+"%d*%d=\t"%(a,b)
            # print(line1)
        if op==4:
            line1 =line1+"%d/%d=\t"%(a,b)
            # print(line1)
        # print("现在打印第{0}行,第{1}列,第{2}题\t\t\t".format(row,col,count))
#print('结束 总共出了100题')

    # print(line1)
    text2write = line1 +'\n'
    f.write(text2write)
    # print(\n)

text2write = "----总共出了{0}道四则运算题 ----\n".format(count)
f.write(text2write)

f.close()

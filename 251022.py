'''
shshi
shiifj
jdkvnii
'''
import random
print(int(random.random()*9000+1000))
num = 10
for i in range(0,num)
    if i <=5:
        print("%d"%i);

a = 0
print("a")

import random
num = int(random.randint(1,100))
count = 0
while num <= 95:
    print(num)
    count = count + 1
    print("数据个数：%d"%count)
    num = int(random.randint(1,100))

print(num)


for i in range(10,99,2):
    if i%3 == 0:
        print("能整除3的是%d"%i)
    else:
        print("不能整除3的是%d"%i)


import random
print("请输入数字：")
limit=float(input())
num=float(random.random())
count=0
while num>limit:
    print(num)
    num=float(random.random())
    count=count+1

print(num)
print("一共打了%d个数"%count)

# 猜固定数字游戏
import random
answer=17
count=0
a=int(random.randint(1,100))
while a<17 or a>17:
    count=count+1
    print("猜的是：%d,再试试"%a)
    a=int(random.randint(1,100))

print("恭喜你！猜对了")
print("一共猜了%d次"%count)

# 猜随机数字游戏
import random
count=1
a=int(random.randint(1,10))
b=int(input("从1-10中猜一个数字： "))
while a!=b:
    count = count + 1
    print("答案是：%d,再试试" % a)
    a = int(random.randint(1, 10))
    b=int(input("从1-10中猜一个数字： "))

print("恭喜你！猜对了")
print("一共猜了%d次"%count)

# 电脑自猜数字游戏
import random
count=1
r=int(input("请输入范围： "))
a=random.randint(1,r)
b=random.randint(1,r)
while a!=b:
    count = count + 1
    print("答案是：%d,再试试" % a)
    a = random.randint(1, r)
    b=random.randint(1, r)

print("恭喜你！猜对了，答案是：%d"%a)
print("一共猜了%d次"%count)


####
n=3
for n in range(5):
    print(n)

####
count=0
str="ahsdhinsduu17235444ncjjnnbuhhfjdj"
for i in str:
    if i=="j":
        count=count+1
print("count=%d"%count)
print(len(str))


str="ahsdhinsduu17235444ncjjnnbuhhfjdj"
for i in str:
    if  i=="j":
        break
    print(i)

print("end")

def plus(a,b):
    c=a+b
    print(c)
    return c

import math
a=round(math.pi*6,8)
print(a)

str="ahsd hi,ns duu 17,2354 44n c,jjn,n buhh f:jdj"
a=str.split()
b=len(a)
print(b)
print(a)

def plus(*mm):
    n=0
    for i in mm:
        n=n+i
        print(n)
    return n

def mul(*mm):
    result=1
    for i in mm:
        result=i*result
    return result

import numpy as np
list=np.array[[1,2,3,4,5,6,7,8,9],
      [11,12,13,14,15,16,17,18,19],
      [21,22,23,24,25,26,27,18,29],
      [31,32,33,34,35,36,37,38,39]]
print(list[0,3])


import pandas as pd



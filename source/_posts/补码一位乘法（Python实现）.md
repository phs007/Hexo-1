---
title: 补码一位乘法（Python实现）
date:
comments: 
description: 基于Python语言实现的补码一位乘法算法
tags:
	- 代码
	- 理论
	- Python
category:
	- 计算机
	- 理论
	- 计算机组成原理
---

``` python
# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:Complement_one_multiplication.py
@time:2018/9/29 17:06
"""


def tostring(list):
    str = ''
    for i in range(len(list)):
        str = str + '{n}'.format(n=list[i])
    return str


def fan(n):
    if n == 1:
        return 0
    else:
        return 1


def zhen2yuan(zhen):
    yuan = []
    flag = False
    for i in range(len(zhen)):
        if i == 0:
            if zhen[i] == '-':
                yuan.append(1)
            else:
                yuan.append(0)
        else:
            if zhen[i] == '.':
                flag = True
            if flag:
                if zhen[i] == '0':
                    yuan.append(0)
                elif zhen[i] == '1':
                    yuan.append(1)
    return yuan


def yuan2bu(yuan):
    if yuan[0] == 0:
        return yuan
    bu = []
    flag = 0
    for i in range(1, len(yuan)):
        if yuan[len(yuan) - i] == 1:
            flag = len(yuan) - i
            break

    bu.append(yuan[0])

    count = 0
    for i in range(1, len(yuan)):
        if i < flag:
            bu.append(fan(yuan[i]))
        else:
            bu.append(yuan[i])
        if yuan[i] == 0:
            count += 1

    if count == len(yuan) - 1:
        bu[0] = 0

    return bu


def bianbu(bu):
    bianbu = []
    flag = 0
    for i in range(1, len(bu)):
        if bu[len(bu) - i] == 1:
            flag = len(bu) - i
            break

    for i in range(len(bu)):
        if i < flag:
            bianbu.append(fan(bu[i]))
        else:
            bianbu.append(bu[i])

    return bianbu


def twofu(input):
    twofu = []
    twofu.append(input[0])
    twofu.append(input[0])
    for i in range(1, len(input)):
        twofu.append(input[i])

    return twofu


def twofuadd(A, B):
    for i in range(len(A)):
        A[i] += B[i]

    for i in range(len(A)):
        if i != len(A) - 1:
            A[len(A) - i - 2] += (int)(A[len(A) - i - 1] / 2)
        A[len(A) - i - 1] = (int)(A[len(A) - i - 1] % 2)
    return A


"""
-0.1101
-0.1011
"""
if __name__ == '__main__':

    # 数据输入
    # X = input()
    # Y = input()
    X = '-0.1101'
    Y = '0.1011'

    # 前期准备
    A = [0, 0, 0, 0, 0, 0]  # 累加器

    Xyuan = zhen2yuan(X)  # X源码
    Yyuan = zhen2yuan(Y)  # Y源码

    Xbu = yuan2bu(Xyuan)  # X补
    Ybu = yuan2bu(Yyuan)  # Y补

    B = twofu(Xbu)  # 双符号位X补
    fanB = twofu(bianbu(Xbu))  # 双符号位-X补
    C = Ybu  # Y补

    # 计算开始
    print("步数       条件      操作        A        C          Cn+1")
    for step in range(len(C)):

        if step == 0:
            C.append(0)
            print("         CnCn+1              {A}    {C}         {Cnp1}".format(A=tostring(A), C=tostring(C[:-1]),
                                                                                  Cnp1=C[-1]))
        else:
            t = []
            t.append(A[len(A) - 1])
            for i in range(len(C) - 1):
                t.append(C[i])
            C = t

            for i in range(3):
                A[len(A) - i - 1] = A[len(A) - i - 2]
            A[2] = A[1]
            print('                     ->      {A}    {C}         {Cnp1}'.format(A=tostring(A), C=tostring(C[:-1]),
                                                                                  Cnp1=C[-1]))

        caozuo = ''
        beicheng = [0, 0, 0, 0, 0, 0]
        if C[-1] - C[-2] == 0:
            caozuo = ' 0'
        elif C[-1] - C[-2] == 1:
            caozuo = '+B'
            beicheng = B
        else:
            caozuo = '-B'
            beicheng = fanB

        print('第{step}步      {pr1}{pr2}        {caozuo}     +{beicheng}'.format(step=step + 1, pr1=C[-2], pr2=C[-1],
                                                                                caozuo=caozuo,
                                                                                beicheng=tostring(beicheng)))
        print('                          ----------')

        A = twofuadd(A, beicheng)

        if step == len(C) - 2:
            print('                             {A}    {C}'.format(A=tostring(A), C=tostring(C[:-1])))
        else:
            print("                             {A}".format(A=tostring(A)))

    for i in range(len(C) - 2):
        A.append(C[i])

    print('[XY]补=', tostring(A[1:]))

```

---

## 运行结果：
```
步数       条件      操作        A        C          Cn+1
         CnCn+1              000000    01011         0
第1步      10        -B     +001101
                          ----------
                             001101
                     ->      000110    10101         1
第2步      11         0     +000000
                          ----------
                             000110
                     ->      000011    01010         1
第3步      01        +B     +110011
                          ----------
                             110110
                     ->      111011    00101         0
第4步      10        -B     +001101
                          ----------
                             001000
                     ->      000100    00010         1
第5步      01        +B     +110011
                          ----------
                             110111    00010
[XY]补= 101110001
```

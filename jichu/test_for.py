#! /usr/bin/env python
# coding: utf8
#
# alist = [];
# for i in range(1,11):
#     if(i%2 ==0):
#         alist.append(i*i)
#
# print(alist)
# #列表推导式
# blist = [i*i for i in range(1,11) if(i%2)==0]
#
# print(blist)
#
# #字典推导式
# abb = ['a','b']
# aaa = {i:0 for i in abb}


def fun():
    list = []
    strs = [108, 1873]
    # 去除字符串两边的字符
    # s = strs.strip("'[]'")
    # print s
    # # 以逗号拆分字符串，并逐一添加到list中
    # a = int(s.split(',')[0])
    # b = int(s.split(',')[1])
    # list.append(a)

    for i in strs:
        print(i)


def fun1():
    try:
       a=12/0
       print(a)
    except Exception as e:
       print(".....")
    # print("!!!!!!!!/\",a)

def fun3():
    dict = {"name":"zhangkejin", "age":23}
    print(dict["name"])
    print "zhangkejin"



def fun2():
    a = 0b10
    print("a:%s"%a)

if __name__ == '__main__':
    fun3()
    fun2()
    fun1()
    print("asdf")

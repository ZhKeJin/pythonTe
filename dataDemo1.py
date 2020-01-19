#定义数据类型
bandwidth = 100
ratio = 8
x = 'asdf'
y = "asfasdf"
print(type(y))
print(bandwidth/8)

#序列
shenxiao = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
print(shenxiao[0])
print(shenxiao[0:4])

#
year = 2020
print(year%12)
print(shenxiao[year%12])

print("...............")


#元组的定义
string = "asdfasdfadsf"
list1 = ['asdf',3,'asdf',"a"]
name = ("asfdf","asdf","asdf","asdf")
data = ((1,22),(2,33),(4,44))
(moth,day) = (2,32)
dataday = filter(lambda x : x <=(moth,day), data)

mlen = len(list(dataday))%12

print(name[mlen])
print(string[3])
print(list1[2])
print(name[2])


#条件
x = "asdfuu"
if x=='asdfuu' :
    print(x)

#循环
shenxiao  = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
for i in shenxiao:
    print(i)

for i in range(1999,2001):
    print("%s 年的生肖是 %s" %(i,shenxiao[i%12]))

x =5
while x > 0 :
    print(x)
    temp = x-1
    x = temp


#字典
dict = {}
print(dict)
dict1 = {1:'qqq','x':"asdfadf"}
print(dict1)




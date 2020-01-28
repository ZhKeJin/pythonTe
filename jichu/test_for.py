#从1 至  10 计算偶数的和

alist = [];
for i in range(1,11):
    if(i%2 ==0):
        alist.append(i*i)

print(alist)
#列表推导式
blist = [i*i for i in range(1,11) if(i%2)==0]

print(blist)

#字典推导式
abb = ['a','b']
aaa = {i:0 for i in abb}


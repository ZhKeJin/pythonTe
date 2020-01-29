#求水花仙数

#1000之内 的三位数
j=1
i=100

while i<1000:
    a = i//100
    b = (i-a*100)//10
    c = i%10

    if a*a*a + b*b*b + c*c*c == i:
        print(i)
    i+=1
shenxiaos = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

xinzuos = ("白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座",
           "天蝎座","射手座","摩羯座","水瓶座","双鱼座")
riqi = ((1,22),(2,22),(3,22),(4,22),(5,22),(6,22),(7,22),
        (8,22),(9,22),(10,22),(11,22),(12,22))

shenxiao = {}
for i in shenxiaos:
    shenxiao[i] = 0

xinzuo = {}
for i in xinzuos:
    xinzuo[i] = 0


while True:
    year = int(input("year:"))
    moth = int(input("moth:"))
    day = int(input("day:"))
    n=0

    while riqi[n]<(moth,day):
      if moth == 12 and day > 22:
         break;
      n+=1

    print(xinzuos[n])
    print("%s 年的生肖是：%s" %(year,shenxiaos[year%12]))

    xinzuo[xinzuos[n]]+=1
    shenxiao[shenxiaos[year%12]]+=1

    for eachshenxiao in shenxiao.keys():
        print("生肖 %s 有%s 个"%(eachshenxiao,shenxiao[eachshenxiao]))




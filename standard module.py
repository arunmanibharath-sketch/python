# import math
# print(math.sqrt(169))
# print(math.factorial(4))
#
# ceil_value=math.ceil(9.1)#nearest high value
# print(ceil_value)
#
# floor_value=math.floor(9.9)#nearest down value
# print(math.floor)
#
# gcd_value=math.gcd(24,36)#to find gcd value
# print(gcd_value)
#
# print(math.lcm(12,24))# find the lcm

# import statistics
#
# data=[10,20,30,40,50]
# print(statistics.mean(data))#add all num
# print(statistics.median(data))
# # data=[10,20,30,40,50,40,30]
# print(statistics.mode(data))
# data1=[10,20,30,40,]
# print(statistics.median_high(data1))
# print(statistics.median_low(data1))
#
#
# # date&time
# import datetime
# print(datetime.datetime.now())
# dob= datetime.datetime(2005,11,1,5,26,40)
# print(dob)
# birth = datetime.date(2005,11,10)
#
#
# x=datetime.datetime.now()
# print(x.strftime("%B-%D-%y"))
#
# x=datetime.datetime.now()
# print(x.strftime("%A-%B-%D-%y"))
#
#
# import datetime
# now=datetime.datetime.now()
# sample_date=datetime.datetime(2026,2,12,2,12,43)
#
# future_date=sample_date+datetime.timedelta(days=10)
# future_date=now+datetime.timedelta(minutes=10)
# future_date=now+datetime.timedelta(hours=10)
# future_date=now+datetime.timedelta(weeks=2)
# print(future_date)
#
#
# import random
# ran_integer=random.randint(1,8)
# print(ran_integer)
#
# ran_float=random.random()
# print(ran_float)
#
# ran_float=random.uniform(1.4,2.4)
# #
# fruits=["apple","banana","cherry","date"]#pick a random things
# print(random.choice(fruits))
# print(random.sample(fruits,4))
#
# cards=["ace","king","queen","jack","10"]#shuffle methood is shuffle the data's
# random.shuffle(cards)
# print(cards)
#
# random_range=


# # assignment
# import math
# print(math.sqrt(144))
#
# down= math.floor(7.9)
# print(down)
#
# up=math.ceil(7.1)
# print(up)
#
#
# fact=math.factorial(6)
# print(fact)
#
# gcd_value=math.gcd(36,60)
# print(gcd_value)
#
#
# import statistics
#
# x=[10, 20, 30, 40, 50]
# print(statistics.mean(x))
#
# y=[1, 2, 3, 4, 5, 6]
# print(statistics.median(y))
#
# data=[2, 4, 4, 6, 8, 8, 8, 10]
# print(statistics.mode(data))
#
# data1= [10, 20, 30, 40]
# print(statistics.median_high(data1))
#
#
# data2=[10, 20, 30, 40]
# print(statistics.median_low(data2))
#
#
# import datetime
#
# today=datetime.date.today()
# print(today)
#
# time=datetime.datetime.now().time()
# print(time)
#
# ind=datetime.date(1947,8,15)
# print(ind)
#
# time=datetime.time(9,30)
# print(time)
#
# x=datetime.datetime.now()
# print(x.strftime ("%d-%m-%y"))
#
#
# import datetime
#
# now=datetime.datetime.now()
# fut_date=now+datetime.timedelta(days=100)
# print(fut_date)
#
#
# import datetime
#
# sub_date=now-datetime.timedelta(days=7)
# print(sub_date)
#
#
# import datetime
#
# date1= datetime.date(2024,1,1)
# date2= datetime.date(2026,10,6)
#
# dif=date2-date1
# print(dif.days)
#
# import datetime
#
# current_date = datetime.date.today().year
# print(current_date)
#
# import datetime
# date=datetime.date(2000,1,1)
# print(date)
#
# import random
#
# ran_int=random.randint(1,50)
# print(ran_int)
#
# import random
# ran_float=random.random()
# print(ran_float)
#
# ran=random.uniform(10,20)
# print(ran)
#
# col=["red", "blue", "green"]
# print(random.choice(col))
#
# num=[1,2,3,4,5,6,7,8,9,10]
# ran=(random.sample(num,3))
# print(ran)
#
# num=[1,2,3,4,5]
# random.shuffle(num)
# print(num)
#
# ran=random.randrange(2,20,2)
# print(ran)
#
# ran1=random.randrange(1,7)
# print(ran1)
#
# import random
#
# toss=random.choice(["HEADS","TAILS"])
# print(toss)
#
#
# num=range(1,100)
# ran=(random.sample(num,5))
# print(ran)

# import random
# import time
# otp=random.randint(100000,900000)
#
# print("OTP SEND:",otp)
#
# start_time=time.time()
# user_otp=int(input("ENTER THE OTP:"))
# if time.time()-start_time >5:
#     print("OTP expired")
# elif user_otp == otp:
#     print("OTP verified. access granted")
# else:
#     print("wrong OTP")

#
# x=int(input("enter the number"))
# if x  %2==0:
#     print("even number")
# else:
#     print("odd number")

# a=2
# b=40
# c=15
# if a>b and a>c:
#     print("a is greatest")
# elif b>c:
#     print("b is greatest")
# else:
#     print("c is greatest")

# x=int(input("enter the number"))
# if x<0:
#     print("negative")
# elif x>0:
#     print("positive")
# else:
#     print("zero")
#4


# y=int(input("enter the num"))
# if y %2==0:
#     print("even num")
# else:
#     print("odd num")


# for num in range(1,21):
#     count=0
#     for i in range(1,num+1):
#         if num% i==0:
#             count = count +1
#
#     if count ==2:
#         print(num)


# a=25
# b=40
# c=15
# if a>b and a>c:
#     print("a is greatest")
# elif b>c:
#     print("b is greatest")
# else:
#     print("c is the greatest")

# total=0
# for i in range(1,21):
#     total=total+i
# print(total)
#
# x= [10, 25, 7, 40, 18]
#
# largest=max(x)
# print(largest)



# import os
# os.getcwd() get current working directory
# print(os.getcwd())

import os
os.listdir()
print(os.listdir)

# import os
# os.rename("file1.py","file_1.py"),


# import os
# os.remove("file name") #remove thee any file does mention the file name

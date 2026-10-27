# # def add (a,b):
# #     return a+b
# # print(add(10,20))
#
#
# class employee:
#     def __init__(self,name):
#         self.name =name
#
#     def login(self):
#         return f"{self.name} has logged in."
#
#     def view_task(self):
#         return f"{self.name} can view assigned task."
#
# class team_member(employee):
#     def submit_task(self):
#         return f"{self.name} has submitted the task."
#
# class manager(employee):
#     def assign_task(self):
#         return f"{self.name} has assigned the task."
#
# arun= team_member("Arun")
# mani= manager("Mani")
#
# print(arun.login())
# print(arun.submit_task())
# print(mani.login())
# print(mani.assign_task())


# import random
# import time
# otp= random.randint(100000,999999)
# print("your otp is",otp)
#
# start_time=time.time()
# user_otp=int(input("enter otp:"))
#
# if time.time()- start_time > 30:
#     print("otp expired")
# elif user_otp == otp:
#     print("otp  verified")
# else:
#     print("invalid otp")

# import datetime
#
# now=datetime.datetime.now()
#
# print("current date:",now.date())
# print("current time:",now.strftime("%H:%M:%S"))
# print("date and time:",now.strftime("%d-%m-%Y %H:%M:%S"))
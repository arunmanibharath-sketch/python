# def welcome(name ):
#     print(name)
# welcome("arun")

# def sum(a,b):
#     return(a+b)
# print(sum(10,20))
#
# def multi(a,b):
#     return(a*b)
# print(multi(5,4))
#
# sign=input("enter your signal :").lower ()
# def example(sign):
#     if sign  == "red" or sign== "RED":
#         print("stop")
#     elif sign == "yellow" or sign=="YELLOW":
#         print("wait")
#     elif sign == "green" or sign== "GREEN":
#         print("go")
#     else:
#         print("invalid signal")
# example(sign)
#
# signal=input("enter your signal:").lower()
# def sign(signal):
#     if signal == "red" :
#         print("stop")
#     elif signal =="yellow" :
#         print("wait")
#     elif signal =="green" :
#         print("go")
#     else:
#         print("invalid signal")
# sign(signal)

# # 05/10/26
#
# def add_sum(x=3,y=6):
#     return x+y
# print(add_sum(4,6))#10
# print(add_sum(4))#10
# print(add_sum())#9

# variable lenth args

# def add_nums(*x):
#     print(sum(x))
# add_nums(1,2,3,4,5,6,7)
# add_nums(1,2,3,4,)


# def count_num(*x):
#     print(len(x))
#     print(min(x))
#     print(max(x))
# count_num(1,2,3,4,5,5,10)

# def count_num(**x):
#      print(x)
# count_num(a=1,b=2,c=3,d=4,e=5,)
#
# def count_num(**x):
#     print(len(x.items))
# count_num(a=1,b=2,c=3,d=4,e=5,)
#
#
# a=6
# b=7




# x=30
# print(bin(x))
#
#
# y=[1,2,3,4]
# print(sum(y))
# print(sum([1,2,3,4],5))

# assignment-11
#
# def employee_details(emp_name="ARUN",emp_role="DATA ANALYTICS",emp_salary=40000):
#     print("EMPLOYEE NAME:",emp_name)
#     print("EMPLOYEE ROLE:",emp_role)
#     print("EMPLOYEE SALARY:",emp_salary)
# employee_details()

#
# def total_num(*numbers):
#     total=sum(numbers)
#     return total
# print (total_num(10,20,30,40))
#
# def profile(**details):
#     for key,values in details.items():
#         print(key,":",values)
# profile(name="ARUN",age=21,course="DA",city="chennai")

#
# find_min=lambda a,b :min(a,b)
# print(find_min(8,6))
#
# cube=lambda x: x**3
# print(cube(3))
#
# num=lambda x:x%5==0
# print(num(30))
#
# rev=lambda x: x[::-1]
# print(rev("python"))
# try:
#     num=int(input("enter num:"))
#     den=int(input("enter den"))
#     result=num/den
# except ZeroDivisionError:
#     print("denominator cant be zero")
# except ValueError:
#     print("only integers allowed")
# else:
#     print(result)
# finally:
#  print("completed")
# /

# try:
#     dict1={
#         "name":"arun",
#         "age":21
#     }
#     print(dict1["name"])
# except KeyError:
#     print("key not found")
# finally:
#     print("completed")

# try:
#     x=open("file3.py")
# except FileNotFoundError:
#     print("print File not found")
# else:
#     print("file found")
# finally:
#     print("completed")

# try:
#     x=["a","b","c"]
#     print(x[2])
# except IndexError:
#     print("Index not found")
# else:
#     print("Index found")
# finally:
#     print("completed")


# x=int(input("enter ur age:"))
#
# if x<18:
#     raise ValueError("age cannot below 18")



# WHILE TRUE MOST IMPORTANT
# try:
#     a=int(input())
#     b=int(input())
#     c=a/b
# except:
#     print("error")
# else:
#     print(c)
#     break
# finally:
#     print("completed")


# assignment-15
# try:
#     num=int(input("enter ur num"))
#     dig=int(input("enter ur dig"))
#     result=num/dig
# except ZeroDivisionError:
#     print("denominators cant be zero")
# else:
#     print("Result:",result)
# finally:
#     print("completed")


# try:
#     x=int(input("enter the num:"))
#
# except ValueError:
#     print("invalid input")
# finally:
#     print("completed")

#
# try:
#     x=int("abc")
#     print(x)
# except ValueError:
#     print("invalid conversion")


# this_list=[10,20,30,40,50]
#
# try:
#     index=int(input("enter ur index:"))
#     print(this_list[index])
# except IndexError:
#     print("index out of  range")

# student={
#     "name":"Arun",
#     "age":21,
#     "city":"nagapattinam"
# }
# try:
#     key=input("entr the key")
#     print(student[key])
# except KeyError:
#     print("key not found")

# try:
#     file=open("student.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("file  not found")


# try:
#     a=10
#     b="hello"
#     print(a+b)
#
# except TypeError:
#         print("cannot add int and string")

# try:
#     age = int(input("Enter your age: "))
#
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#
#     print("Age:", age)
#
# except ValueError as e:
# #     print("Invalid age:", e)
#
#
#
# try:
#     a = int(input("Enter num: "))
#     b = int(input("Enter den: "))
#     result = a / b
#
# except ValueError:
#     print("Please enter valid integers")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#
# else:
#     print("Result:", result)

# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("Valid number:", num)
#         break
#
#     except ValueError:
#         print("Invalid input. Please enter an integer.")


# 16/10/2026

# class mobile:
#     brand = "samsung"
#     color ="cherry wine red"
#     price =234565
#     def display_details(self):
#         print(f"brand:{self.brand},"
#               f"color:{self.color},price:{self.price}")
# obj1 =mobile()
# obj1. display_details()



# class employee:
#     name = "arun"
#     role ="DA"
#     salary =23456
#     def display_details(self):
#         print(f"name:{self.name},"
#               f"role:{self.role},"
#               f"salary:{self.salary}")
# obj1 =employee
# obj1.display_details()

class employee:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    def display_details(self):
        print(f"name:{self.name},"
              f"role:{self.role},"
              f"salary:{self.salary}")
obj1 = employee("arun","DA",23454)
obj1.display_details()
obj2 = employee("b","ds",23456)
obj2.display_details()
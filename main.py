#
# x=int(input("enter x"))
# if x >0:
#     print ("positive")
# if x<0:
#     print("negative")
#     if x==0:
#      print("zero")
# check_num=int(input("enter num"))
# print(check_num % 2==0)
# if check_num%2  !=0:
#     print("odd")
# #
#
#

# nested condition

# marks= int(input ("enter your marks"))
# if marks <100 and marks >95:
#      print(" A grade")
# elif  marks <=95 and marks >85:
#     print("B grade")
# elif  marks <85 and marks >75:
#     print(" C grade")
# elif   marks <65 and marks >55:
#     print(" D grade")
# else:
#     print( " you have failed  ")





# age=int(input("enter your age"))
# if age> 0:
#     if age >18:
#         print("eligible for vote ")
#     else:
#         print(" not eligible to vote ")
# else:
#     print("pls enter  an age above 0 ")
#

#
# password =int( input( "enter your password"))
#
# if password == 5250:
#  print(" login successfully")
# else:
#          print("wrong password")


#
#
#
#
# degree=int(input("Enter degree : "))
# if degree >30:
#     print("weather is hot")
# if degree <=30:
#    print ("weather is cool")

# marks = int(input("enter marks"))
# if marks >=40:
#     print ("pass")
# else:
#     print("fail")


# num =int(input("enter the number"))
# if num % 5==0:
#       print("divided by 5 ")
# else:
#       print("not divided by 5")
#
# A =int(input("enter the number"))
# B =int(input("enter the number"))
# C =int(input("enter the number"))
#
# if  A>B and A>C :
#     print("A is the largest ")
# elif  B>C:
#     print("B is the largest ")
# else:
#     print("C is the largest")


# A=(input("enter the colour"))
#
# if A== "red":
#     print("stop")
# elif A== "yellow":
#     print("wait")
# elif A=="green":
#     print("go")
# else:
#     print("invalid signal")

#
# card=(input("card inserted or not"))
# pin =int(input("enter the pin " ))
# if card== "inserted":
#     if pin==5250:
#         print("transaction allowed")
#     else:
#         print("Transaction not Allowed")
# else:
#     print("Transaction not Allowed")
#
# username =input("enter your username")
# password =int(input("enter your password " ))
# if username== "arun":
#     if password==5250:
#         print("login successfully")
#     else:
#         print("incorrect password")
# else:
#      print("invalid username")





# age=int(input("enter the age" ))
# if age<=13:
#     print("child")
# elif age>13 and age<=19:
#     print("teenager")
# elif age>20 and age<59:
#     print("adult")
# else:
#     print("senior citizen")


# LOOPS CONCEPT 26/09/26

# x="ARUNMANI"
# for i in x:
#      print(i)
#     # print(i,end="")
#
#
# for i in range(5,51,5):
#     print (i)
#
# for i in range(2,21,2):
#     print(i)
# else:
#     # print()#newline/ next line
#     print("loop completed")
#     print("/n finished")#newline/ next line

#
# for i in range (2,21,2):
#     if i==10:
#         break
#     print(i)
# else:
#     print("loop completed")
#2,4,6,8
#
# for i in range(2,21,2):
#     print(i)
#     if i==10:
#         break
#o/p=2,4,6,8,10

# for i in range(2,21,2):
#     print(i)
#     if i==10:
#       break
# else:
#      print("completed")#not run because in else statement
# print("loop breaks")

#
# for i in range(2,21,2):
#     if i==10:
#      continue
#     print(i)
# else:
#     print("loop completed")
#
# for i in range(11):
#     if i ==6:
#         continue
#     print(i)
# else:
#     print("loop completed")

#nested for loop
# for i in range(5):
#     for j in range(4):
#         print(i,j)
#
# for i in range(5):
#     for j in range(4):
#         print(f"i={i},j={j}")

# for i in range(5):
#     for j in range(4):
#         if i==2:
#             break
#         print(i,j)
#
# for i in range(5):
#     for j in range(4):
#          if i == 2:
#           continue
#          print(i,j)


# for i in range(1,11):
#     print(i)
# #
# for i in range(2,21):
#     if i==15:
#        break
#     print(i)
#
# for i in range(10,21):
#     if i ==15:
#         continue
#     print(i)
#
# for i in range(1,6):
#     print(i)
# else:
#     print("loop completed")


# 23/09/26 for i in loop
#
# for i in range(4):
#     if i==2:
#         break
#     for j in range(3):
#         print(i,j)
#
# for i in range(4):
#     if i==(2):
#         continue
#     for j in range(2):
#         print(i,j)

# for i in range(4):
#     for j in range(2):
#         if i == (2):
#             break
#     print(i, j)

# i=0
# while i<5:
#     print(i)
#     i+=1

# i=1
# while i<=15:
#     if i ==11:
#         break
#     print(i)
#     i+=2
# else:
#     print("loop completed.")
#
# print("this is outside the loop.")

# i=2
# while i<=10:
#     print(i)
#     i+=2
#
# i=2
# while i<=10:
#     if i==6:
#         i+=2
#         continue
#     print(i)
#     i+=2
# else:
#     print("loop completed.")

# i=4
# while i<=28:
#     if i==20:
#       i+=4
#       continue
#     print(i)
#
#     i+=4
# else:
#     print("loop completed")

# i=0
# while  i<=3:
#     j=0
#     while j<2:
#         print(i,j)
#         j+=1
#     i+=1
#
# i=0
# while  i<=3:
#     if i ==1:
#         break
#     j=0
#     while j<2:
#         print(i,j)
#         j+=1
#     i+=1

# i=0
# while i < 3:
#     j = 0
#     while j < 3 :
#         if j == 1:
#            j += 1
#            continue
#         print(i,j)
#         j += 1
#     i += 1

# i=10
# while i >= 1:
#     print(i)
#     i-=1

# i=1
# while i <=50:
#     if i% 5 == 0:
#        print(i)
#     i+=1
# i=1
# while i<=20:
#     if i==10:
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=20:
#     if i==16:
#      break
#     print(i)
#     i+=1
#
# for i in range(0,4):
#     for j in range(0,4):
#         if j == 3:
#          # j+=1
#           break
#         print(i,j)


# 24/05/26

# a="arunmani"
# print(a)
# print(len(a))

# concatenation
#
# a= "arun"
# b=("mani")
# print(a+" "+b)


# a=("arun ")
# y=(a*5)
# print(y)
#
# indexing
# x="apple"
# print(x[-2])



# x="apple"
# print(x[-4:-2])

# for reverse
# x="apple"
# print(x[::-1])

# x="INTERNATIONAL"
# print(x[-3:])
# print(x[-4:-1])
# print(x[-7:-2])
# print(x[::-1])
# print(x[-3])
# print(x[-3:][::-1])
# print(x[-8:][::-1])
#
# a="INTERNATIONAL"
# print(a.lower())

# a="arunmani rajendran"
# print(a.upper())

#
# a="INTERNATIONAL"
# print(a.replace('N','$'))
#
# y="a b c"
# print(y.split())
#
# y="a,b,c"
# print(y.split(","))

#
# a="123456789"
# print(a.isalnum())
#
# b="arunmani"
# print(b.isalnum())

# a="ARUN"
# print(a.isalpha())
#
# b="arun!"
# print(b.isalpha())

#
# a="12345"
# print(a.isdigit())

# a="12345wer"
# print(a.isdigit())
#
# a="123 45"
# print(a.isdigit())

# b="arun!"
# print(b.islower())
#
# b="ARUN!"
# print(b.isupper())

# 25/09/26


# x="  "
# print(x.isspace())

# a='arun'
# b="mani"
# c='''python'''
# print(a,b,c)
#
# a="good"
# b="morning"
# print(a+" "+b)


#
# a="I LOVE PYTHON. "
# b=(a*3 )
# print(b)
#
# x="DYNAMIC LANGUAGE"
# print(x[0])
# print(x[2])
# print(x[15])


# a="PROGRAMMING"
# print(a[3:7])
#
# x="HELLO"
# print(x[::-1])

# x="STRING FUNCTIONS"
# print(len(x))
#
# a="Python3"
# print(a.isalnum())

# x="Python!"
# print(x.isalpha())


# a="1234"
# print(a.isdigit())
# b="12.34"
# print(b.isdigit())

# x="Hello World"
# print(x.lower())
# print(x.upper())

# x="     python    "
# print(x.strip())
#
# a="java is fun"
# print(a.replace('java','python'))
#
# y="apple banana cherry"
# print(y.split())

#
# x="welcome to python"
# print(x.istitle())x= ["a","r","u","n","m","a","n","i"]
# # print(x)
# # print(len(x))
# # print(type(x))
# # print(x[1])
# # print(x[1:3])
# # print("e"in x)
# print(x.swapcase())

# 28/9/26
# sample list

#
#
#
# thislist=["apple","banana",""]
#
#
#
#
# thislist=["car","bike","bus"]
# thislist[1]="two wheeler"
# print(thislist)
#
# thislist=["apple","banana","cherry","orange","kiwi","mango"]

# thislist[1:3]=["blackcurrant","watermelon"]
# print(thislist)
#
# thislist=["apple","banana","cherry"]
#
# thislist[1:2]=["blackcurrant","watermelon"]
# print(thislist)
#
# thislist=["apple","banana","cherry"]
# thislist[1:3]=["watermelon"]
# print(thislist)

#
# thislist=["apple","banana","cherry"]
# thislist.insert(2,"watermelon")
# thislist.insert(1,"melon")
# print(thislist)
#
# x=["apple","banana","cherry"]
# x.append("guava")
# print(x)
# x.extend(["orange","grapes"])
# print(x)


# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist=["apple","banana","cherry"]
# thislist.pop()
# # thislist.pop(1)
# print(thislist)


# thislist=["apple","banana","cherry"]
# del thislist[0]
# # del thislist[1:3]
# print(thislist)

# x=["a","b","c","d","e","f","g"]
# x.remove("f")
# print(x)
#
# x=["a","b","c","d","e","f","g"]
# x.pop(1)
# print(x)


# x=["a","b","c","d","e","f","g"]
# del x[2:3]
# print(x)

# thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)
#
# thislist=["apple","banana","cherry"]
# [print(x) for x in thislist ]
#
# upp_fn=[x.upper() for x in  thislist]
# print(upp_fn)

# thislist=["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)
#
# thislist=["orange","mango","kiwi","pineapple","banana"]
# thislist.sort(reverse=True)
# print(thislist)
#
# thislist=[100,50,30,40,82]
# thislist.sort()
# print(thislist)
#
#
#
# thislist=[100,50,30,40,82]
# thislist.sort(reverse=True)
# print(thislist)



# thislist=[100,50,30,40,82]
# thislist.sort(reverse=True)
# print(thislist)


# thislist=[100,50,30,40,82]
# # thislist.sort()
# print(thislist)


#assingnment


# thislist=["apple","banana","jack fruit","grapes","orange"]
# print(thislist)

# x= ["pen", "pencil", "eraser", "sharpener"]
# print(x[0])
# print(x[3])

# x=["red", "green", "blue", "yellow"]
# print(x[-1])
#
# fruits=["mango","banana","apple"]
# if "apple" in fruits:
#     print("apple is in the list")
# else:
#     print("apple exists")

#
# fruits=["apple","banana","cherry"]
# fruits[1]="grapes"
# print(fruits)
#
# thislist= ["dog", "cat", "rabbit", "parrot"]
# thislist[1]="cow"
# thislist[2]="goat"
# print(thislist)
#
#
# thislist=["apple", "banana", "cherry"]
# thislist.insert(1,"pineapple")
# print(thislist)
#
# fruits= ["apple", "banana"]
# fruits.extend(["mango","orange"])
# print(fruits)
# #
# veg= ["potato", "carrot", "onion"]
# veg.remove("carrot")
# print(veg)
#
# thislist=["apple", "banana", "cherry", "mango"]
# thislist.pop(1)
# print(thislist)
# thislist.clear()
# print(thislist)

# thislist=["java", "python", "c++"]
# for x in thislist:
#     print(x)
#
# thislist= ["rose", "lotus", "lily"]
# i=0
# while i <len(thislist):
#     print(thislist[i])
#     i+=1
#

# thislist= [45, 12, 89, 33, 5]
# thislist.sort()
# print(thislist)
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x= [x for x in numbers if x %2==0]
# print(x)

# num=[1,2,3,4,5]
# num.clear()
# print(num)

# 29/09/26
#tuples
#
# sample_tuple=("a","b","c","d")
# print(sample_tuple)
# print(type(sample_tuple))
#
# tuple_1=("a")
# print(tuple_1)
# print(type(tuple_1))#class str
#
# tuple_1=("a",)
# print(tuple_1)
# print(type(tuple_1))#class tuple

#
# tuple_1=("a","b","c")
# print(tuple_1)
# print(type(tuple_1))
# print(len(tuple_1))#3
# print(tuple_1[1:3])#b,c
# print("c"in tuple_1)

#
# x=("a","b","c")
# print(x)
# y=list(x)
# print(y)
# y[1]="x"
# print(y)
# x=tuple(y)
# print(x)

# list tuple

# tuple_1=("x","y","z")
# tuple_2=list(tuple_1)
# tuple_2.insert (2,["a","b"])
# print(tuple_2)
# tuple_2.append("c")
# tuple_2.pop(3)
# tuple_1=tuple(tuple_2)
# print(tuple_1)


# x=("a","b","c","d")
# fruits1 = ("apple", "banana", "cherry")
#
# fruits2 = ("mango","grapes")
#
# total = fruits2 + fruits1
#
# print(total)
#
# fruits = ("a","b","c")
#
# mytuple = fruits * 2
#
# print(mytuple)
#
#
# thistuple = (1,2,3,4,5,5,5,6,7,8)
#
# x = thistuple.count(5)
#
# print(x)

# # set
# set1={"a","b","c","d"}
# print(set1)
# print(len(set1))
# print(type(set1))
# set1.add("e")
# set1.update("f","g")
# print(set1)


# set1={"a","b","c","d"}
# # set1.remove("a")
# # set1.discard("b")
# # set1.pop()
# # set1.clear()
# del set1
# print (set1)

# #
# x=("chennai","madurai","coimbatore","nagapattinam","tiruchirappalli")
# print(x)
# print(type(x))
#
# tuple_1=("red", "blue", "green", "yellow")
# print(tuple_1[2])
#
# flower=("rose", "lotus", "lily")
# print(flower[-1])
# print(type(flower))
#
# num= (10, 20, 30, 40, 50, 60)
# print(num[2:5])
# print(type(num))

# fruits= ("mango", "banana", "apple")
# if "apple" in  fruits:
#     print("yes apple in fruits list")
# else:
#     print("no existence")

#
# tuple_1=(100, 200, 300, 400)
# print(len(tuple_1))

#
# x=("python",)
# print(type(x))
#
# y= [1, 2, 3, 4]
# x=tuple(y)
# print(x)
#
# tuple_1= ("car", "bike", "bus")
# y=list(tuple_1)
# y[1]="train"
# tuple_1=tuple(y)
# print(tuple_1)

# x=(1,2,3)
# y=(4,5,6)
# z=x+y
# print(z)

# x=(10,20)
# print(x*3)
#
# y= ("pen", "pencil", "eraser")
# (pen,pencil,eraser)=y
# print(pen)
# print(pencil)
# print(eraser)


# pet=("dog", "cat", "cow")
# for cat in pet:
#      print(cat)

# tuple_1 =(1, 5, 7, 5, 9, 5, 11)
# x=tuple_1.count(5)
# print(x)


# colour=("red", "blue", "green", "yellow")
# x=colour.index("blue")
# print(x)

# 30/09/26
# set operators

#example

# set1={'a','b','c'}
# set2={'c','d','e'}
# print(set1|set2)
# print(set1.union(set2))
# print(set1&set2)
# print(set1.intersection(set2))
# print(set1-set2)
# print(set1.difference(set2))
# print(set1^set2)
# print(set1.symmetric_difference(set2))

# dict1={"name":"arun",
#        "age":22,
#        "place":"ngpt"}
# print(dict1)
#
# dict2={
#     "name":"arun",
#     "subject":["maths","science","english"],
#     "score":[78,88,35]
# }
# print(dict2)
# print(dict2["name"])
# print(dict2["score"][1])
# print(dict2.get("name"))
# print(dict2.get("score")[1:3])
# print(dict2["score"][1:3])
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())
# dict2["name"]="mani"
# print(dict2)
# dict2["score"][2]=50
# print(dict2)
# dict2["result"]= "pass"
# print(dict2)
# dict2.update({
#     "key1": "value1",
#     "key2": "value2"
# })
# print(dict2)
#
# dict2.pop("key1")
# print(dict2)#specific item
# dict2.popitem()#last item
# del dict2["result"]#clears all data
# dict2.clear()#clear all data
# del dict2#delete entire dictionary

#nested dictionary
# x={
#     "name":"arun",
#     "marks":{
#         "maths":55,
#         "science":60,
#         "english":76
#     }
# }
# print(x)
# print(x["marks"]["science"])


# assig09

# student={
#     "name":"john",
#     "age":20,
#     "course":"Python"
# }
# print(student)

#
# car={
#     "brand":"Ford",
#     "model":"Fiesta",
#     "year":2010
# }
# print(car["model"])



# fruits={
#     "name":"apple",
#     "colour":"red",
#     "price":120
# }
# print(fruits.get("colour"))


# bike={
#     "brand":"yamaha",
#     "model":"R15",
#     "year":2010
# }
# bike["year"]=2024
# print(bike)


# city={
#     "name":"paris",
#     "country":"France",
# }
# city["colour"]="blue"
# print(city)


# person={
#     "name":"Alice",
#     "age":25,
#     "job":"Engineer"
# }
# del person["age"]
# print(person)


# animal = {"type": "Dog", "breed": "Labrador", "age": 5}
# print(animal.keys())

#
# country = {"name": "India", "capital": "New Delhi", "currency": "Rupee"}
# for values in country.values():
#  print(values)

#
# employee = {"id": 101, "name": "Rahul", "dept": "Sales"}
# emp_copy=employee.copy()
# print(emp_copy)



# students={
#     "student1":{
#         "name":"arun",
#         "age":22,
#     },
#     "student2":{
#         "name":"mani",
#         "age":21,
#     }
# }
# print(students)

# deg=int(input("enter the deg"))
# if deg>30:
#     print("negative")
# else:
#     print("positive")


# a=int(input("enter the num"))
# b=int(input("enter the num"))
# c=int(input("enter the num"))
# if a>b and a>c:
#     print("a is the largest")
# elif b>c:
# #     print("b is the largest")
# # else:
# #     print("c is he largest")
#
# num=int(input("enter the num"))
# if num %2!=0:
#         print("odd")
# else:
#     print("even")

# num=int(input("enter the num"))
# if num<2:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             print("not prime")
#             break
#     else:
#         print("prime")



# 01/10/26

# def find_diff(a,b):
#     print(a-b)
# find_diff(10,6)
# find_diff(5,2)
#
#
# def full_name(fname,lname):
#     print(f"my firstname is {fname}"
#            f"and my lastname is {lname}")
# full_name("arun","mani")
#
#
# def find_sum(a,b):
#     return a+b
# print(find_sum(1,3))

# def find_square(x):
#     return x*x
#     return x ** 2# for squares
#     return x**3#forn cubes
# print(find_square(4))
#
# def personal_det(name,age):
#     return f"hi am {name} and i am {22} years old..."
# print(personal_det("arun",22))

#
#
# def student_det(name,course):
#     print(f" name:{name},course:{course}")
# student_det(course="DA",name="ARUN")

# assignment-10
#
# def find_sum(a,b):
#     total_sum=a+b
#     return total_sum
# sum_1=find_sum(10,20)
# print(sum_1)
#
# def find_square(a):
#     return a*a
# print(find_square(5))

# def find_greater(a,b,c):
#     if a>b and a>c :
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(find_greater(15,20,18))

# def travel(source,destination,distance):
#   print("source:",source)
#   print("destination:",destination)
#   print("distance:",distance)
#
# travel("chennai","nagapattinam",350)

#
# def student_enrollment(name,age,phone_num,course):
#     print("name:",name)
#     print("age:",age)
#     print("phone_num:",phone_num)
#     print("course:",course)
# student_enrollment(
#     name="arun",
#     age=22,
#     phone_num=9600762177,
#     course="Data Analytics"
# )
#
# def find_sum(a,b):
#     return a+b
# print(find_sum(10,20))
#
# def find_odd_even(num):
#     if num %2== 0:
#         print("even number")
#     else:
#         print("odd number")
# find_odd_even(7)
#
# def find_square(a):
#     return a*a
# print(find_square(5))
#
# def find_weather(deg):
#     if deg >30:
#         print("negative")
#     elif deg < 30:
#         print("positive")
#     else:
#         print("zero")
# find_weather(33)
#
#
# def find_max(a,b,c):
#     if a>b:
#         print("A is greater")
#     elif b>c:
#         print("B is greater")
#     else:
#         print("c is greater")
# find_max(10,20,30)

#
# def find_student_details(name,age,course,mark):
#     print("name:",name)
#     print("age:",age)
#     print("course:",course)
#     print("mark:",mark)
# find_student_details (
#     name="arun",
#     age=22,
#     course="Data analytics",
#     mark=78
# )
#
# def tour(source,destination,distance):
#     print("source:",source)
#     print("destination:",destination)
#     print("distance:",distance)
#
# tour("chennai","ooty",440)

# def mul(num):
#     for  i in  range(1,11):
#          print(num,"x",i,"=",num**  i)
#
# mul(6)
# mul(7)



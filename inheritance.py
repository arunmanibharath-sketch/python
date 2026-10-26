# class parent:
#     def method1(self):
#         print("method1")
# class child:
#     def method2(self):
#         print("method2")
# obj1 =parent()
# obj1.method1()
#
# obj2 =child()
# obj2.method2()
# obj2.method1()

# multiple
# class parent1:
#     def method1(self):
#         print("method1")
# class parent2:
#     def method2(self):
#         print("method2")
# class child(parent1,parent2):
#     def method3(self):
#         print("method3")
# obj=child()
# obj.method1()
# obj.method2()
# obj.method3()

# multilevel
# class grandparent:
#     def method1(self):
#         print("method1")
# class parent(grandparent):
#     def method2(self):
#         print("method2")
# class child(parent):
#     def method3(self):
#         print("method3")
# obj1 = child()
# obj1.method1()
# obj1.method2()

# hierarchild
# class parent:
#     def method1(self):
#         print("method1")
# class child1(parent):
#     def method2(self):
#         print("method2")
# class child2(parent):
#     def method3(self):
#         print("method3")
# obj1 = child1()
# obj1.method1()
# obj1.method2()
# obj2 =child2()
# obj2.method1()


# class vehicle:
#     def method1(self):
#         print("This is a vehicle")
# class car(vehicle):
#     def car_method2(self):
#         print("this is a car")
# obj=car()
# obj.method1()
# obj.car_method2()
#
# class father :
#     def father(self):
#         print("This is the father.")
# class mother:
#     def mother(self):
#         print("This is the mother.")
# class child(father,mother):
#     def child(self):
#         print("This is the child.")
# obj=child()
# obj.father()
# obj.mother()
# obj.child()

# class person:
#     def get_name(self):
#         print("My name is Arun")
# class employee(person):
#     def get_employee_id(self):
#         print("Employee ID:101")
# class manager(employee):
#     def get_department(self):
#         print("Department: DA")
# obj=manager()
# obj.get_name()
# obj.get_employee_id()
# obj.get_department()

# class animal:
#     def animal_sound(self):
#         print("Animals makes sounds.")
# class dog(animal):
#     def bark(self):
#         print("Dog barks.")
# class cat(animal):
#     def meow(self):
#         print("cat meows.")
#
# obj1= dog()
# obj1.animal_sound()
# obj1.bark()
#
# obj2= cat()
# obj2.animal_sound()
# obj2.meow()

# class device:
#     def power_on(self):
#         print("Device powered on")
# class phone(device):
#     def make_call(self):
#         print("Making a call")
# class tablet(device):
#     def browse_web(self):
#         print("Browsing the web")
# class smart:
#     def connect_to_wifi(self):
#         print("connect to WIFI")
# class smartphone(phone,smart):
#     pass
# obj1= smartphone()
# obj1.power_on()
# obj1.make_call()
# obj1.connect_to_wifi()


# #
# class person:
#     def __init__(self,name):
#         self.name=name
#
#     def person_info(self):
#         print("name:",self.name)
#
# class student(person):
#     def __init__(self,name,roll_no):
#         super().__init__(name)
#         self.roll_no=roll_no
#
#     def student_info(self):
#         print("Roll number:",self.roll_no)
#
# class sports:
#     def __init__(self,sport):
#        self.sport = sport
#
#     def sport_info(self):
#         print("sport:",self.sport)
#
# class student_athlete(student,sports):
#     def __init__(self,name,roll_no,sport):
#         student.__init__(self,name,roll_no)
#         sports.__init__(self,sport)
#
# s=student_athlete("Arun
# mani",18,"cricket")
#
# s.person_info()
# s.student_info()
# s.sport_info()
#
# class vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#
#     def vehicle_info(self):
#         print("brand:",self.brand)
#
# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#
#
#     def car_info(self):
#         print("Model:",self.model)
#
# class electric:
#     def __init__(self,battery):
#         self.battery=battery
#
#     def battery_info(self):
#         print("Battery Capacity:",self.battery)
#
# class electric_car(car,electric):
#     def __init__(self,brand,model,battery):
#         car.__init__(self,brand,model)
#         electric.__init__(self,battery)
#
# car=electric_car("TATA","Nexon EV","40.5 kWh")
#
# car.vehicle_info()
# car.car_info()
# car.battery_info()


#
# class A:
#     def find_sum (self,a,b):
#         print(a+b)

# class A:
#     def method1(self):
#         print("method1")
# class B(A):
#     def method2(self):
#         super().method1()
#         print("method2")
# obj2=B()
# obj2.method1()

# class animal:
#     def speak(self):
#         print("Animal makes a sound")
# class dog:
#     def speak(self):
#         print("dog barks")
# animal_obj=animal()
# dog_obj=dog()
#
# animal_obj.speak()
# dog_obj.speak()
#
# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __add__(x,y):
#         print(x,y)
# p1=product("tv",50000)
# p2=product("phone",75000)
# p1+p2


# class prouct:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __add__(a,b):
#         return product(a.name+"+"+b.name,a.price+b.price)
#     def __str__(self):
#         return f"product :{self.name},price:{self.price}"
# x=product("a",1000)
# y=product("b",2000)
# z=product("c",3000)
# total =x+y+z


# duck typing




# class duck:
#     def sound(self):
#         print("quack...")
# class cat:
#     def sound(self):
#         print("meow...")
# class dog:
#     def sound(self):
#         print("bow...")
# def animal_sound(obj):
#     obj.sound()
# x=duck()
# y=cat()
# z=dog()
# animal_sound(x)
# animal_sound(y)
# animal_sound(z)


# @abstract method

#
# from abc import ABC, abstractmethod
# class  vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("vehicle class")
# class car(vehicle):
#     def start(self):
#         print("car start with key")
# class bike(vehicle):
#     def start(self):
#         print("bike start with button")
# c =car()
# b =bike()
# c.start()
# b.start()

# encapsulaion method
#
# class BankAccount:
#     def __init__(self):
#         self.balance =0
#     def deposit(self,amount):
#         self.balance +=amount
#     def get_balance(self):
#         return self.balance
# acc =BankAccount()
# acc.deposit(3000)
# print(acc.get_balance())


# assignment 16

# class greeter:
#     def greet(self,*names):
#         if len(names)==1:
#             print("Hello",names[0])
#         elif len(names)==2:
#             print("Hello",names[0],"and",names[1])
#         elif len(names)==3:
#             print("Hello",names[0],",",names[1],"and",names[2])
#         else:
#             print("please enter 1,2 or 3 names.")
# g= greeter()
#
# g.greet("arun")
# g.greet("arun","mani")
# g.greet("arun","mani","raja")


#
# class shape:
#     def draw(self):
#         print("drawing a shape")
# class circle(shape):
#     def draw(self):
#         print("drawing a circle")
#         super().draw()
# class coloredcircle(circle):
#     def draw(self):
#         print("drawing a colored circle")
#         super().draw()
#         shape().draw()
#
# obj= coloredcircle()
# obj.draw()


# from fractions import Fraction as F
#
# class Fraction:
#     def __init__(self,numerator,denominator):
#         self.value=F(numerator,denominator)
#     def __sub__(self,other):
#         result=self.value -other.value
#         return result
#     def display(self):
#         print(self.value)
#
# f1 =Fraction(1,2)
# f2 =Fraction(1,3)
# result=f1-f2
# print(result)

#
# class employee:
#     def __init__(self,name,salary):
#         self.name= name
#         self.salary=salary
#
#     def __gt__(self,other):
#         return self.salary>other.salary
#
# e1 =employee("arun",30000)
# e2 =employee("mani",25000)
#
# if e1>e2:
#     print(e1.name,"Has higher salary")
# else:
#     print(e2.name,"Has higher or equal salary")

# duck typing
#
# class creditcard:
#     def process_payment(self):
#         print("payment processed used credit card")
#
# class paypal:
#     def process_payment(self):
#         print("payment processed used paypal")
#
# class Bitcoin:
#     def process_payment(self):
#
#         print("payment processed used Bitcoin")
#
# def process_order(payment_method):
#     payment_method.process_payment()
#
# p1=creditcard()
# p2=paypal()
# p3=Bitcoin()
#
# process_order(p1)
# process_order(p2)
# process_order(p3)


 # task 01
# class student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("course:",self.course)
#
# s1=student("Arunmani",21,"BBA")
#
# s1.display()

# task 02
#
# class employee:
#     def __init__(self,emp_id,emp_name,salary):
#         self.emp_id=emp_id
#         self.emp_name=emp_name
#         self.salary=salary
#
#     def display(self):
#         print("employee id:",self.emp_id)
#         print("employee name:",self.emp_name)
#         print("salary:",self.salary)
#         print("___________________")
#
# e1=employee(18,"arun",35000)
# e2=employee(35,"mani",30000)
#
# e1.display()
# e2.display()

# task 03
#
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount >0:
#             self.__balance += amount
#             print("deposited:",amount)
#         else:
#             print("invalid deposit amount")
#
#     def withdraw(self,amount):
#         if 0< amount <=self.__balance:
#             self.__balance-= amount
#             print("withdrawn",amount)
#         else:
#             print("insufficient balance ")
#     def show_balance(self):
#         print("current balance:",self.__balance)
#
# acc= BankAccount(5000)
#
# acc.show_balance()
# acc.deposit(2000)
# acc.withdraw(3000)
# acc.show_balance()

# task 04

# class person:
#     def __init__(self,name):
#         self.name=name
#
#     def show_name(self):
#         print("name:",self.name)
#
#
# class teacher(person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject=subject
#
#     def show_subject(self):
#         print("subject:",self.subject)
#
# t=teacher("anushya","python")
#
# t.show_name()
# t.show_subject()

# task 05

# class animal:
#     def sound(self):
#         print("animal makes sound")
#
# class dog(animal):
#     def sound(self):
#         print("dog: barks")
#
# class cat(animal):
#     def sound(self):
#         print("cat: meow")
#
# d= dog()
# c= cat()
#
# d.sound()
# c.sound()


# task 06

# class bird:
#     def fly(self):
#         print("bird is flying")
#
# class airplane:
#     def fly(self):
#         print("airplane is flying")
#
# def start_flying(obj):
#     obj.fly()
#
# b = bird()
# a = airplane()
#
# start_flying(b)
# start_flying(a)

# task 07

# from abc import ABC ,abstractmethod
#
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#
#     def area(self):
#         return self.length * self.breadth
#
# r=rectangle(10,5)
#
# print("area rectangle:",r.area())
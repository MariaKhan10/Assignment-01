# Python Reserved Keywords:

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield




from typing import Any
import math as m
import asyncio


#------------------------------------------------------------------------------------------------------------
# 1- False

have_money : bool = False
print(have_money)
print(int(False))

#------------------------------------------------------------------------------------------------------------
# 2- None 
info : Any = None
print(info)



#------------------------------------------------------------------------------------------------------------
# 3- True 
has_money : bool = True
print(has_money)
print(int(True))



#------------------------------------------------------------------------------------------------------------
# 4- and
name : str = "John"
age : int = 19

if len(name) > 0 and age > 18:
    print("User is eligible to signup")



#------------------------------------------------------------------------------------------------------------
# 5- as
x = m.ceil(134.765)
print(x)


#------------------------------------------------------------------------------------------------------------
# 6- assert
def divide(a,b):
    assert b != 0 
    return a/b


print(divide(10,5))
# print(divide(8,0))   // it will give error


#------------------------------------------------------------------------------------------------------------
# 7- async
async def hello():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

asyncio.run(hello()) 



#------------------------------------------------------------------------------------------------------------
# 8- await

async def greet():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

async def main():
    print("Start") 
    await greet()
    print("End")  

asyncio.run(main())     


# // output


# Start
# Hello,
# (2 second pause)
# World!
# End


#------------------------------------------------------------------------------------------------------------
# 9- break

for i in range(1,7):
    if i == 3:
        print(i,"Loop breaks")
        break

    print(i)


#------------------------------------------------------------------------------------------------------------
# 10- class 


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


    def show_details(self):
        print(f"Brand : {self.brand} , Model : {self.model}" )    


my_car = Car("Toyata","Corolla")     
my_car.show_details()  





#------------------------------------------------------------------------------------------------------------
# 11- continue

for i in range(1,7):
    if i == 4:
        print("Skipping")
        continue
    print(i) 



#------------------------------------------------------------------------------------------------------------
# 12- def


def greet1(name):
    print(f"Hello {name} Welcome to Python !")

greet1("Maria")    



#------------------------------------------------------------------------------------------------------------
# 13- del

a = 10
print(a)
del a

fruits : list = ["apple","banana","cherry"]
print(fruits)

del(fruits[1])
print(fruits)


#------------------------------------------------------------------------------------------------------------

# 14,15,16  - if-elif-else
 
marks = 95

if marks >= 90:
    print("Grade A")

elif marks < 90 and marks >=80:
    print("Grade B")
elif marks < 80 and marks >=70:
    print("Grade c")    
else:
    print("Grade D")


#------------------------------------------------------------------------------------------------------------
# 17,18,19  try-except-finally

try:
   num =  int(input("Enter a number : "))
   result = 10/num
   print("Result", result)
except ZeroDivisionError:
   print("Error: Cannot divide by zero!")

finally:
    print("Execution completed")   



#------------------------------------------------------------------------------------------------------------
# 20  for

fruits = ["Banana","Cherry","Mango"]    
for fruit in fruits:
    print(fruit)


for i in range(1,10):
    print(i)




#------------------------------------------------------------------------------------------------------------
# 21  from

from math import sqrt

print("sqrt",sqrt(25))



#------------------------------------------------------------------------------------------------------------
#22  global

x = 10 # global variable

def my_function():
    global x
    x = x + 2
    print("Inside function",x)

my_function()   
print("Outside function", x) # global variable is updated



#------------------------------------------------------------------------------------------------------------
#23  import

from typing import Any
import math as m
import asyncio



#------------------------------------------------------------------------------------------------------------
# 24  in

fruits = ["banana","mango","apple"]
if "banana" in fruits:
    print("Banana is in the list")



words = "Python"
for word in words:
    print(word)    



#------------------------------------------------------------------------------------------------------------
# 25   is

x = 100
y = 100

print(x is y)  # True (Same memory location for small integers)


e = [1,2,3]
f = [1,2,3]


print(e == f)   # True  (Values are same)
print(e is f)   # False (Different memory locations)



#------------------------------------------------------------------------------------------------------------
# 26 lambda

add = lambda x,y: x + y
print(add(2,4))   # output 6


# difference b/w normal and lambda(one liner function)

def square(number):
    return number * number

sqr_func = lambda number : number * number

result = square(4)
print(result)    # Output: 16
print(sqr_func(4))   # Output: 16





#------------------------------------------------------------------------------------------------------------
# 27  not

x = True
y = False

print(not x)   # False
print(not y)   # True


password = ""
if not password:
    print("Passwoed cant be empty")
    


age = 18
if not age < 18 :
    print("You are an adult")   



#------------------------------------------------------------------------------------------------------------
# 28    or

age = 20
has_permission = True

if age >= 18 or has_permission:
    print("Access Granted")

else:
    print("Access Denied")



#------------------------------------------------------------------------------------------------------------
# 29     pass

x = 10
if x > 12:
    pass    # No error, even if block is empty


def myfunc():
    pass


for i in range(1,6):
    pass



#------------------------------------------------------------------------------------------------------------
#30  raise

# x = -5
# if x < 0:
#     raise ValueError("Negative values are not allowed!")



#------------------------------------------------------------------------------------------------------------
# 31  return

def addition(a,b):
    return a + b

result = addition(5,7)
print(result)



#------------------------------------------------------------------------------------------------------------
# 32  while

i = 1
while i <= 10:
    print(i)

    i += 1   


j = 1
while j < 5:
    if j == 3:
        break
    print(j)

    j += 1    




#------------------------------------------------------------------------------------------------------------
# 33  with

# with open("filename.txt", "r") as file:
#     content = file.read()
#     print(content) 



#------------------------------------------------------------------------------------------------------------
# 34  yield

def my_generator():
    yield 1    
    yield 2    
    yield 3    

gen = my_generator()   

print(next(gen))
print(next(gen))
print(next(gen))



#------------------------------------------------------------------------------------------------------------
# 35   non local

def outer():
    x = 10  # Parent function ka variable

    def inner():
        x = 20  # Yeh new local variable ban raha hai, parent ka x change nahi hoga
        print("Inner:", x)  

    inner()
    print("Outer:", x)  # Parent function ka x waise ka waise rahega

outer()



# With nonlocal (Parent Variable Modify Hota Hai)
def outer2():
    x = 10  

    def inner():
        nonlocal x  # Ab yeh parent function ka x modify karega
        x = 20  
        print("Inner:", x)  

    inner()
    print("Outer2:", x)  # Ab parent function ka x bhi change ho gaya

outer2()

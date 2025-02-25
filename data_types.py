#=-------------------------------------------------------------------------------------------------------#

#                                              Python Data Types  

#=-------------------------------------------------------------------------------------------------------#

# 1- Numeric

# - int
# - float
# - complex


x = 10  # Integer type
print(type(x))  # Output: <class 'int'>

y = 3.14  # Floating-point number
print(type(y))  # Output: <class 'float'>


z = 2 + 3j  # Complex number (real + imaginary part)
print(type(z))  # Output: <class 'complex'>


#=-------------------------------------------------------------------------------------------------------#

# 2- Dictionary

info = {"name":"john", "age" : 20, "city": "New York"}
print(info)
print(type(info))
print(info["city"])
info["gender"] = "Male"   # adding new key:value
print(info)   # updated

#=-------------------------------------------------------------------------------------------------------#


# 3- Boolean

x = True
y = False

print(type(x))
print(type(y))


#=-------------------------------------------------------------------------------------------------------#


# 4- Set

my_set = {1,2,3,4,5}
print(type(my_set))

my_set1 = {1,2,2,3,4,5,5,5,6,6,7,7,8,9,10}
print(my_set1)  # remove duplicates automatically

my_set1.add(99)
print(my_set1)  # add 

my_set1.remove(99)
print(my_set1)  # remove


first_set = {1,2,3,4,5}
second_set = {4,5,6,7,8}

print(first_set | second_set)  # Union             1,2,3,4,5,6,7,8
print(first_set & second_set)  # intersection       4,5


#=-------------------------------------------------------------------------------------------------------#

# 5- Sequence Type

# - string
# - tuple
# - list



# - string  (Immutable Text Data)

text = "Hello Maria"
print(text[2])    # positive index
print(text[-3])   # negative index
print(text[1:4])  # slicing



# - tuple (Immutable Ordered Collection)

my_tuple = (1,2,3,"a","banana",True)
print(my_tuple[1])     # 2
print(my_tuple[-3])    # a

new_tuple = my_tuple + (10,"Cherry")
print(new_tuple)


# - list  (Mutable Ordered Collection)

my_list = ["Apple","Banana",10,20,False]
print(my_list[2])            # 10
print(my_list[-1])           # False
my_list[2] = "Cherry"        # can be changed
print(my_list)

my_list.append("Strawberry")    # add
my_list.remove("Banana")        # remove

print(my_list)

#=-------------------------------------------------------------------------------------------------------#
'''
def anonymous(y):
    print(id(y))
    x = 8
    print(id(x))
    print('x is', x)


a = 10
print(id(a))
anonymous(a)
print('a is', a)
'''

# whenever we call a function passing a value, they'll share the same id(address)
'''
def anonymous(y):
    print(id(y))
    x = 8
    print(id(x))
    print('x is', x)


a = 10
print(id(a))
anonymous(a)
print('a is', a)
'''

'''
def anonymous(gst):
    print(id(gst))
    gst[0] = 0
    print(gst)
    print(id(gst))
list  = [2, 4, 6, 8, 10 ]
anonymous(list)
print(id(list))
'''
'''
# Formal arguments
def add(x, y):
    c = x + y
    print(c)
# Actual arguments(Positional, Keyword, Default, Variable length)
add(10, 20)    
'''
'''
def person(name, age):
    print(name)
    print(age)
# positional arguments
person('sudhamsh', 27)    
'''
'''
def person(name, age):
    print(name)
    print(age - 5)
# keyword arguments
person(age = 27, name = 'sudhamsh')    
'''


'''
def person(name, age = 27):
    print(name)
    print(age - 5)
# Default arguments
person(name = 'sudhamsh')
person(name = 'sudhamsh', age = 30)
'''

'''
def sum(*b):
def sum(a, *b):
    # c = a
    # c = 0
    for i in b: 
        c = c + i
    print(c)           
    # print(a)
    # print(b)
# variable length argument
sum(2, 3, 4, 5, 6, 7, 8, 9, 10)
'''
'''
def person(name, **kwargs):
    print(name)
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)   

# Keyword variable length arguments
person('sudhamsh', age = 27, city = 'bangalore')
'''

'''
a = 10
def something():
    # global a
    a = 15
    print('inside the function', a)
something()
print('outside', a)
'''
'''
a = 10
def something():
    print('inside the function', a)
something()
print('outside', a)
'''



'''
a = 10
def something():
    global a
    a = 15
    print('inside the function', a)
something()
print('outside', a)
'''


# a = [1,2,3,4,5,6,7,8,9,10]
# def something(x):    
#     even = 0
#     odd = 0
#     for each_value in a:
#         # print(each_value)
#         if each_value % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd    
# eww, oops = something(a)
# print(eww)
# print(oops)


import os
import time
import platform
if platform.system() == 'Linux':
    os.system('ls-lrt')
else:
    print('Not supported')

print(dir(platform))
print(dir(os))
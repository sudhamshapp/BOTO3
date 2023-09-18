import operator
'''
a = 2.0
b = 2
c = 'sudhamsh'
print(type(a))
print(type(b))
print(type(c))
'''

'''
a = 2
b = '6'
c = int(b)
print(a + int(b)) # we need to parse the string into integer, to get the desired output, we need to transform it
print(a + c)

a = 'sudhamsh'
b = 'mars'
print(a + ' ' +b)
'''


'''
= is assignment operator
== is comparison operator
'''

# strip is the built-in function that removes the leading and trailing whitespaces
'''
a = 'sudhamsh '
b = a.strip()
print(b)
print(a == b)
'''

'''
a = "Hello World"
b = a.split()
print(b)
'''

# split converts the string into a list 
'''
a = 'sudhamsh '
b = a.split()
print(b)
'''


'''
a = 'sudhamsh '
b = list(a.strip())
'''
'''
a = ['sudhamsh', 2.0, 5]
print(type(a))

b = ['mars', 'saturn', 'jupiter']
b.pop()
print(b)
'''

'''
c = ['sudhamsh']
c.append('mars')
print(c)
'''

'''
# Immutable behaviour
a = 'Hello'
b = a
print(a)
print(b)
a = 'sudhamsh'
print(a)
print(b)
'''

# Mutable behaviour
'''
a = ['sudhamsh']
b = a
a.append('mars')
print(a)
print(b)
'''

'''
# a = [1, 2, 3, 4, 5]
# print(a[0:2])

# a = [1, 2, 3, 4, 5]
# (a[0]) = 'sudhamsh'
# print(a)

# empties the list
# a = [1, 2, 3, 4, 5]
# a.clear()
# print(a)


# insert method inserts the desired value at a specific index
# a = [1, 2, 3, 4, 5]
# a.insert(0, 'sudhamsh')
# print(a)

# a = {1: 'sudhamsh', 2: 'mars'}
# a.keys()
# a.items()
# print(a)
'''

# a = { 1: 'sudhamsh', 2: 'mars', 'eve': 'ganesh chathurthi'}
# print(type(a))
# print(a['eve'])

# a = { 1: 'sudhamsh', 2: 'mars', 'eve': 'ganesh chathurthi'}
# a[1] = 'sudhamsh mars'
# print(a)

# a = [1,2,3,4,5, 'sudhamsh', {'name': 'sudhamsh', 'age': 'mars'}]
# print(a[6]['name'])


# a = {'Marks': [1,2,3,4,5], 'Name': 'sudhamsh'}
# print(a['Marks'][0])

# b = """ this is a 
# multiline 
# string."""
# print(b)

# a = {'Name': 'sudhamsh', 'age': 'mars'}
# a.popitem()
# print(a)

# sum  = 0
# a = [1,2,3,4,5,6,7,8,9,10]
# for each_value in a:
#     sum = sum + each_value
#     print(sum)
# print(sum)        


# a = { 1: 'sudhamsh', 2: 'mars', 'eve': 'ganesh chathurthi'}
# print(a.keys())
# print(a.values())
# print(a.items())

a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]
def sumof(var1):
    sudhamsh = 0
    for each_value in var1:
        sudhamsh = sudhamsh + each_value
    return sudhamsh
sum_of_values_ofa = sumof(a)
sum_of_values_ofb = sumof(b)
print(sum_of_values_ofa)
print(sum_of_values_ofb)    
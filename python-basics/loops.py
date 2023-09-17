# count = 1
# for x in "banana":
#     print('-------------')
#     print(count, x)
#     count += 1


# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)

# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# for x in range(10):
#     print(x)

# for x in range(2, 10):
#     print(x)

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# list1 = ['red', 'green', 'blue']
# list2 = ['apple', 'banana', 'cherry']
# for x in list1:
    # for y in list2:
    # print(x)


'''
list1 = ['red', 'green', 'blue']
list2 = ['apple', 'banana', 'cherry']
list3 = ['orange', 'pear', 'peach']
for x in list1:
    for y in list2:
        print(x,y)
'''


# ==============================================lists=============================================


'''
list1 = ['red', 'green', 'blue']
list2 = ['apple', 'banana', 'cherry']
list3 = ['orange', 'pear', 'peach']
for x in list1:
    for y in list2:
        for z in list3:
            print(x,y,z)
'''

# mylist = ["apple", "banana", "cherry"]
# print(mylist[1])

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist[0:3])
# print(thislist[0][3])

'''
thislist = ["apple", "banana", "cherry", "date", "elderberry"]

# Access a range of items (from index 1 to 3, inclusive of 1 but exclusive of 3)
subset = thislist[1:3]
print(subset)  # Output: ['banana', 'cherry']

# Access all items from a starting index to the end
subset_from_start = thislist[2:]
print(subset_from_start)  # Output: ['cherry', 'date', 'elderberry']

# Access all items up to a specific index (exclusive)
subset_up_to_end = thislist[:3]
print(subset_up_to_end)  # Output: ['apple', 'banana', 'cherry']

# Access all items with a specific step (here, every 2nd item)
subset_with_step = thislist[::2]
print(subset_with_step)  # Output: ['apple', 'cherry', 'elderberry']

# Access items in reverse order
reverse_list = thislist[::-1]
print(reverse_list)  # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple']

'''

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# To add an item to the end of the list, use the append() method:
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# To append elements from another list to the current list, use the extend() method.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurance:

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# The pop() method removes the specified index.
'''
thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
thislist.pop()
print(thislist)
'''


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# a = [1, 2, 3]
# b = []
# for each_item in a:
#     b.append(each_item)
# print(b)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# print(type(y))
# x = tuple(y)
# print(type(x))
# print(x)


# x = ("apple", "banana", "cherry")
# try:
#     x[0] = 'sudhamsh'
# except TypeError:
#     print('TypeError')
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for i in ((thistuple)):
#   print(i)


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict['brand'])
print(thisdict.get('brand'))
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict.keys())
print(thisdict.values())
'''
# x= {'Name': 'Sudhamsh'}
# y= {'Name': 'Mars'}

# for each_item in x.items():
#   print(each_item)


'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])
'''
# my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
# stuff = my_dict.items()
# print(stuff)
# Using a for loop to iterate over key-value pairs
# for key, value in my_dict.items():
#     print(f'Key: {key}, Value: {value}')

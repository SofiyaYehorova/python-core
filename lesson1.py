# comment

"""
comment
comment
comment
"""

'''
comment
comment
comment
'''

# print('hello world')
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep='*', end='end\n')

# i = 3
# f = 1.3
# b = True  # False
# s = "text"  # 'text'
# n = None

# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))


# a = b = c = 20
# print(a, b, c)

# fs = str(f)
# print(type(fs))
# print(fs)

# a = 5
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)
# print(round(a / b))  # заокруглює до найближчого парного числа
# print(3 % 2)

# name = input('Enter your name: ')
#
# print(name)

# a = 2
# b = 3

# print('a<b', a < b)
# print('a<=b', a <= b)
# print('a>b', a > b)
# print('a>=b', a >= b)
# print('a==b', a == b) # print('a==b' is a==b)
# print('a!=b', a != b) # print('a==b' is not a==b)

# res = isinstance(a, int)
# res = isinstance(a, str)
#
# print(res)


# check = False
# 
# if not check:
#     print('Ok')


# num = int(input('Enter number: '))
#
# res = 'yes' if num > 5 else 'no'
#
# print(res)

# ----------------------------------------------------------------------------------------------------------------

# list

# l = [1, 2, 3, 4, 'hello', True]
# print(l[0])
# print(l[-1])
# l[4] = 'world'
# print(l)
# print(len(l))
# l2 = l
# print(l2)

# l2 = l.copy()
# l2[1] = 555
# print(l2)
# print(l)

# l = [1, 2, 3, 4, 'hello', True]
# l2 = [2, 6, 8, 3, 4]
# l3=['a', 'b','g', 'f']
# l.append(55)
# l.insert(1, 'hi')

# pop = l.pop()
# print(pop)

# l.remove(3)

# l.extend(l2)
# l+=l2

# print(l.index(2))
# print(l.reverse())
# l.clear()
# print(l.count('hello'))
# l.sort()
# print(l)

# l = [1, 2, 3, 4, 'hello', True]
# l_new = l[0:4]  # [:4]
# l_new1 = l[:4:2]
# l_new2 = l[::-1]
# print(l_new)
# print(l_new1)
# print(l_new2)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# tuple

# my_tuple = (1, 2, 4, 3, 4, 5)
# print(my_tuple[1])
# my_tuple.count(4)
# print(my_tuple.index(2))

# ******************************************************************************************************************

# dict

# dict1 = {
#     'name': 'Max',
#     'age': 20
# }

# print(dict1)
# print(dict1['age'])

# get = dict1.get('name')
# print(get)
#
# print(dict1.items())
# print(list(dict1.items())[0])

# print(dict1.keys())

# pop = dict1.pop('name')
# print(pop)
# print

# popitem = dict1.popitem()
# print(popitem)
# print(dict1)

# dict1 = {
#     'name': 'Max',
#     'age': 20
# }
#
# dict2 = {
#     'house': 45
# }
# dict1.setdefault('age3', 55)
# print(dict1)

# dict1.update(dict2) # dict1 |=dict2
# print(dict1)

# print(dict1.values())

# ============================================================================================================
# set

# set1 = {1, 2, 3, 2, 5}
# set1 = set()
# print(type(set1))
# set1.add(6)
# set1.add(4)
# set1.add(3)
# set1.add(1)
# print(set1)

# set_1 = {1, 2, 3, 4}
# set_2 = {5, 6, 4, 2}
# print(set_1.issuperset(set_2))
# print(set_1.issubset(set_2))
# print(set_1.isdisjoint(set_2))
# print(set_1.intersection(set_2))
# difference = set_1.symmetric_difference(set_2)
# print(list(difference))
# set_1.remove(2)
# set_1.discard(5466)
# print(set_1)
# pop = set_1.pop()
# print(pop)

# =========================================================================================================

# string
# string = "name = 'Vasyl \"'"
# print(string)
#
# st = '*'*50
# print(st)

# name = 'Max'
# age = 20
# weight = 82.3

# string = 'Hello my name is Max, I`m 20 years old, my weight 82.3 kg'
# string = 'Hello my name is ' + name + ', I`m ' + str(age) + ' years old, my weight ' + str(weight) + 'kg'
# string = 'Hello my name is %s, I`m %i years old, my weight %f kg' %(name, age, weight)
# string = 'Hello my name is {}, I`m {} years old, my weight {} kg'.format(name, age, weight)
# string = 'Hello my name is {name}, I`m {age} years old, my weight {weight} kg'.format(name=name, age=age, weight=weight)
# string = f'Hello my name is {name}, I`m {age} years old, my weight {weight} kg'
#
# print(string)

# print(string.index('llo'))
# print(string.count('k'))

# print(string.capitalize())
# print(string.upper())
# print(string.lower())

# str = 'hello world'
# print(str.islower())
# print(str.isupper())
# print(str.title())
# print('Hello World'.swapcase())
# print('asd'.isalpha())
# print('1234'.isalpha())

# print('1234'.isdigit()) #True
# print('1234'.isnumeric()) #True
# print('123s4'.isalnum()) #True
# print('1 23s4'.isalnum()) #False

# print('hello'.startswith('h')) #True
# print('hello'.endswith('h')) #False

# print(['     ssvjs         '.strip()])
# print(['     ssvjs         '.lstrip()])
# print(['     ssvjs         '.rstrip()])
# print(['abaaa     ssvjs         ghghg'.strip('a')])

# print('hello world'.split())
# print('hello-world'.split('-'))

# print('hello is true'.partition('is'))  #return tuple

# l = ['1', '2', '3']
# print(''.join(l))
#
# l = ['1', '2', '3']
# print('-'.join(l))

# print('       '.isspace())

# print('hello world'.replace('l', 'L'))

# print('hello world'[:5])

# print(min(3, 5, 7, 1, -8))
# print(max([4, 7, 9, 0]))
# print(sum([3, 7, 8, 12]))
# l = sorted([2, 7, 9, 0, -13])
# l2 = sorted([4, 7, 89, 12], reverse=True)
# print(l, l2)
# print(pow(3, 5)) #3**5

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# functions


# def func():
#     print('hello')
# func()

# def func(a, b, c):
#     print(a, b, c)
# func(2, 3, 4)

# def func(a, b, c=15):
#     print(a, b, c)
# func(5, 2)

# def func(a, b, c=15, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
# func(5, 2, 555, 8, 9, 10, 154, name='Max', age=20)

# l = [1, 2, 6, 7]
# user = {
#     'name':'Max',
#     'age':20
# }
#
# def func(a, b, c, d, name, age):
#     print(a, b, c, d)
#     print(name, age)
# func(*l, **user)


# ---------------------------------------------------------------------------------------------------------
# cycles

# while

# i = 5
#
# while i > 0:
#     i -= 1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('finish')

# for in

# users = ['Olga', 'Anna', 'Masha']

# for user in users:
#     print(user)

# for i in range(50):
#     print(i)

# for i in range(2, 60, 4):
#     print(i)

# for i, user in enumerate(users): #user and index
#     print(i, user)

# user = {
#     'name': 'Max',
#     'age': 20,
#     'house': 48
# }
#
# for k, v in user.items():
#     print(k)
#     print(v)

# l = [i for i in range(10)]
# print(l)

# l = [1, 2, 3, 4, 5]

# res = [i for i in l if i % 2 == 0]
# res = [i**2 for i in l]
# res = [str(i ** 2) for i in l]
# res = [str(i ** 3) for i in l if i % 2 == 1]
# print(res)

# super_list = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 0]
# ]

# res = [i for j in super_list for i in j]

# res = []
# for j in super_list:
#     for i in j:
#         res.append(i)
#
# print(res)


# dict1 = {'NaMe': 'Olga', 'aGe': 20}
#
# dict2 = {k.lower(): v for k, v in dict1.items()}
# print(dict2)

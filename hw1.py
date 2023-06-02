# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
#
# is_digit = [num for num in st if num.isdigit()]
# print(is_digit)
# join = ', '.join(is_digit)
# print(join)

# print((', '.join(num for num in st if num.isdigit())))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# ch = [ch if ch.isdigit() else ' ' for ch in st]
# print(ch)
# join_ch = ''.join(ch)
# print(join_ch)
# split = ', '.join(join_ch.split())
# print(split)

# print(', '.join(''.join([ch if ch.isdigit() else ' ' for ch in st]).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
#
# print([let.upper() for let in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i ** 2 for i in range(50) if i % 2])


# function
#
# - створити функцію яка виводить ліст

# list = [1, 2, 3, 4]

# def show_list(arr):
#     print(arr)
# show_list(list)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_n(a, b, c):
#     max_num = max(a, b, c)
#     print(max_num)
#     return max_num
# max_n(5, 8, 10)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_max(*args):
#     print(max(args))
#     return min(args)
# min_max(15, 17, 8, 3)

# - створити функцію яка повертає найбільше число з ліста

# def max_of_list(arr):
#     return max(arr)

# - створити функцію яка повертає найменьше число з ліста

# def min_of_list(arr):
#     return min(arr)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_of_list(arr):
#     return sum(arr)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_of_list(arr):
#     return sum(arr)/len(arr)

# ################################################################################################
# 1)Дан list:

list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - знайти мін число

# print(min(list1))


def min_of_list(arr):
    return min(arr)

#   - видалити усі дублікати

def del_dupl():
    copy_list = list1.copy()
    print(list(set(copy_list)))
del_dupl()

#   - замінити кожне 4-те значення на 'X'

# count = 3
# while (count < len(list1)):
#     list1[count] = 'X'
#     count += 4
# print(list1)


def to_x():
    list_copy = list1.copy()
    # print(['X' if not (i + 1) % 4 else item for i, item in enumerate(list_copy)])
    for i in range(3, len(list_copy), 4):
        list_copy[i] = "X"
    print(list_copy)

to_x()

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

# length = int(input("Enter the size of the square: "))


# for i in range(length):
#     for j in range(length):
#         if(i == 0 or i == length - 1 or j == 0 or j == length - 1):
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#     print()


def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
square(10)

# 3) вывести табличку множення за допомогою цикла while

# for row in range(0, 10):
#     for col in range(0, 10):
#         num = row * col
#         if num < 10:
#             empty = "  "
#         else:
#             if num < 100:
#                 empty = " "
#         if col == 0:
#             if row == 0:
#                 print("    ", end='')
#             else:
#                 print("  ", row, end='')
#         elif row == 0:
#             print("  ", col, end='')
#         else:
#             print(empty, num, end='')
#     print()


def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            print(' ' if res // 10 else '  ', end='')
            print(res, end='')
            # print(f'{res:4}', end='')
            j += 1
        print()
        i += 1

multi_table()

# 4) переробити це завдання під меню

while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*"')
    print('5) вивести табличку множення за допомогою цикла while')
    print('9) вихід')

    choise = input('Зробіть свій вибір: ')

    if choise == '1':
        print(min_of_list(list1))
    elif choise == '2':
        del_dupl()
    elif choise == '3':
        to_x()
    elif choise == '4':
        square(5)
    elif choise == '5':
        multi_table()
    elif choise == '9':
        break


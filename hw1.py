# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі



# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# print(greeting.upper().split(','))
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#


# function
#
# - створити функцію яка виводить ліст
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]

#   - знайти мін число

#   - видалити усі дублікати

#   - замінити кожне 4-те значення на 'X'

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

# length = int(input("Enter the size of the square: "))
#
# for i in range(length):
#     for j in range(length):
#         if(i == 0 or i == length - 1 or j == 0 or j == length - 1):
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#     print()

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

# 4) переробити це завдання під меню
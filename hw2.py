# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append('{}) {}'.format(len(todo_list) + 1, todo))
#
#     def get_all():
#         nonlocal todo_list
#         return todo_list
#
#     return get_all, add_todo
#
#
# get_todo, add_todo = notebook()
# add_todo('To do something')
# add_todo('Learn something new')
# add_todo('Watch something new')
# add_todo('Cook something new')
# add_todo('Go to gym')
#
# print(*get_todo(), sep='\n')



# 2) протипізувати перше завдання


# from typing import Callable
#
# def notebook() -> tuple[
#     Callable[[], list[str]],
#     Callable[[str], None]
# ]:
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append('{}) {}'.format(len(todo_list) + 1, todo))
#
#     def get_all() -> list[str, ...]:
#         nonlocal todo_list
#         return todo_list
#
#     return get_all, add_todo
#
#
# get_todo, add_todo = notebook()
# add_todo('To do something')
# add_todo('Learn something new')
# add_todo('Watch something new')
# add_todo('Cook something new')
# add_todo('Go to gym')
# print(*get_todo(), sep='\n')

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'





# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та
# буде виводити це значення після виконання функцій



# def decor(func):
#     counter = 0
#
#     def increment():
#         nonlocal counter
#         counter += 1
#         print('count: {}'.format(counter))
#         func()
#         print('-' * 15)
#
#     return increment
#
#
# @decor
# def checking():
#     print('Checking your order')
#
#
# @decor
# def cancel():
#     print('Cancel your order')
#
#
# checking()
# checking()
# checking()
#
# cancel()
# cancel()
#
# checking()
# cancel()

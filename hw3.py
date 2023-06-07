# Створити клас Rectangle:
# -він має приймати дві сторони x, y

# -описати поведінку на арифметични методи:

# + сумма площин двох екземплярів класу

# - різниця площин двох екземплярів класу

# == площин на рівність

# != площин на не рівність

# >, < меньше більше при виклику метода len()

# підраховувати сумму сторін

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.area = x * y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eg__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(5, 9)
# rectangle2 = Rectangle(6, 12)
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1 > rectangle2)
# print(len(rectangle1))
# print(len(rectangle2))

# ###############################################################################

# створити клас Human(name, age)

# створити два класи Prince i Cinderella, які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги, у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати
# список попелюшок, та шукати ту саму в класі попелюшки має бути count який буде зберігати кількість створених екземплярів класу також має бути
# метод класу який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#         Cinderella.__count += 1
#
#     def __str__(self):
#         return f'name:{self.name}, age: {self.age}, shoe size: {self.shoe_size}'
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_found):
#         super().__init__(name, age)
#         self.shoe_found = shoe_found
#
#     def find_cinderella(self, cinderellas: list[Cinderella, ...]):
#         for cinderella in cinderellas:
#             if cinderella.shoe_size == self.shoe_found:
#                 print(cinderella)
#                 break
#
#
# list_of_cinderellas: list[Cinderella, ...] = [
#     Cinderella('Sofiya', 38, 37),
#     Cinderella('Olga', 38, 38),
#     Cinderella('Liliya', 38, 39),
#     Cinderella('Anna', 38, 35),
#     Cinderella('Tanya', 38, 36),
#     Cinderella('Svitlana', 38, 40)
# ]
#
# prince = Prince('Oleksandr', 42, 38)
#
# prince.find_cinderella(list_of_cinderellas)

# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

# 3) Створити клас Main в якому буде:

# - змінна класу printable_list, яка буде зберігати книжки та журнали

# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine
# iнакше  ігрнорувати додавання

# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу

# - метод show_all_books, який буде виводити всі книги викликаючи метод print абстрактного класу

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки класів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass
    
    
class Book(Printable):
    def __init__(self, name):
        self.name = name
        
    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    __printable_list = []

    def add(self):
        if isinstance(self, Magazine):
            Main.__printable_list.append(self)
        elif isinstance(self, Book):
            Main.__printable_list.append(self)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Vogue'))
Main.add(Magazine('Elle'))
Main.add(Magazine("Harper's bazaar"))
Main.add(Magazine('Cosmopoliten'))

Main.add(Book('Marry Poppins'))
Main.add(Book('A Christmas Carol'))
Main.add(Book('The Canterbury Tales'))

Main.show_all_magazines()
print('*/' * 20)
Main.show_all_books()




        
        

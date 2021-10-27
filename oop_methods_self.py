# у сущностей есть данные и действия
# действия - методы
# данные - поля (атрибуты)


if __name__ == '__main__':
    pass


class Person:
    pass


p1 = Person()
p1.name = "John"
p1.surname = "Savage"
p1.age = 22

# printf - появился в 3-й версии позволяет использовать код внутри строки
print(f"{p1.name} {p1.surname} {p1.age}")


class Person2:
    # в self находится объект на котором вызвывается этот метод
    def print_info(self):
        print(f"{self.name} {self.surname} {self.age}")


p2 = Person2()
p2.name = "Alex"
p2.surname = "Surname"
p2.age = 20

p2.print_info()
# питон переводит это в такой код
Person2.print_info(p2)

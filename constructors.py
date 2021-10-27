class Person:
    # Атрибуты класса создаются внутри самого класса
    some_num = 123

    def __init__(self, name, surname, year_of_birth):
        # Атрибуты объекта
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def print_info(self):
        print(f"name: {self.name} \nsurname: {self.surname} \nyear of birth: {self.year_of_birth}")


if __name__ == '__main__':
    p1 = Person("Elon", "Musk", "1971")
    p1.print_info()

    p1.new_attribute = "text"
    print(p1.new_attribute)
    p1.print_info()

    print(Person.some_num)
    Person.some_num = 456
    print(Person.some_num)
    print(p1.some_num)

    # мы не можем менять значение атрибута класса через объект
    p1.some_num = 55  # создает новый атрибук объекта который перекроет аттрибут класса
    print(p1.some_num)
    print(Person.some_num)


    class Circle:
        # константы пишутся с вобльшой буквы
        PI = 3.14

        def __init__(self, radius):
            self.radius = radius

        def get_perimeter(self):
            return self.radius * 2 * self.PI

        def get_area(self):
            return Circle.PI * self.radius ** 2


    c = Circle(3)
    print(c.get_perimeter())
    print(c.get_area())

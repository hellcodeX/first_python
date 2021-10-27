# наследование - отношение is-a
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")

    def say_hello(self):
        print(f"{self.name} says hello!")


class Student(Person):
    pass


class Teacher(Person):
    # без вызова super() переопределенный конструктор не будет создавать поля базового класса
    # можно и Person.__init__(self, name, age) написать но так делать не стоит.
    # super() позволяет обратится к объекту родительского класса или просто к родительскому классу
    def __init__(self, name, age, teachId):
        super().__init__(name, age)
        self.teachId = teachId
        print("teacher created")

    def teach(self):
        print(f"{self.name} teaches")


if __name__ == '__main__':
    p1 = Person("Tom", 15)
    p1.say_hello()

    s1 = Student("Alex", 18)
    t1 = Teacher("John", 45, 22)

    s1.say_hello()
    t1.say_hello()
    t1.teach()

class Animal:
    def say(self):
        print("Animal is saying")


class Cat(Animal):
    def say(self):
        print("Meow")


class Dog(Animal):
    def say(self):
        print("Ghaf")


if __name__ == '__main__':
    def some_func(animals):
        print("some animals")
        for animal in animals:
            animal.say()


    list_of_animals = [Cat(), Dog()]
    some_func(list_of_animals)

# пример недостатка динамической типизации - хоть и не наследуется можно вызвать some_func()
    class TestClass:
        def say(self):
            print("say from test class")

    some_func([TestClass(), TestClass()])


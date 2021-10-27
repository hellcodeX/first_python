# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = 5
print(a)
print("a")

b = 10
print(b)

# Все переменные в python - указатель (не коробки которые содержат сообщение).
# b и c указывают на однин и тот же участок памяти
b = 7
# старое значение b 10 было очищено
c = 7
print(a)

# мы можем всегда поменять тип данных на который ссылается переменная
c = "my message"
print(c)

x = 1
y = 2

# swap vars
temp = x
x = y
y = temp

print(x)
print(y)

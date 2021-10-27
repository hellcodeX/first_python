if __name__ == '__main__':
    a = ["hey", "hello", "goodbye"]
    total_sum = 0
    for word in a:
        print(word)
        total_sum += len(word)
        print(total_sum)

    print(range(1, 5))
    # для корректного отображение диапазона нужно передать его в метод лист
    print(list(range(1, 5)))

    for i in range(1, 5):
        print(i)

    print("################")

    for j in range(1, 20):
        if j % 3 == 0 or j % 5 == 0:
            print(j)

    print("###  while")
    list11 = list(range(1, 5))
    print(list11)

    index = 0
    while index < 5:
        print(list11[index])
        if index == 2:
            break
        index += 1

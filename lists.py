if __name__ == '__main__':
    my_list = [1, 2, 3]
    print(my_list)
    my_list.append(5)
    print(my_list)

    my_list.append([9, 8])
    print(my_list)

    my_list.pop()
    print(my_list)

    print("Index is 2: " + str(my_list[2]))
    print("Index is -1: " + str(my_list[-1]))

    the_list = [2, 5, 6]
    the_list[0] = 10
    print(the_list)

    list2 = [1, 2]
    # свап с кратким синтаксисом
    list2[0], list2[1] = list2[1], list2[0]
    print(list2)
    # такое присвоение возможно
    a, b = 1, 2
    print(a)
    print(b)

    # while True: infinity loop
    #   print()

    for i in range(len("word")):  # from 0 to string len
        print(i)

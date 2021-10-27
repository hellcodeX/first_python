if __name__ == '__main__':
    a = range(5)

    b = []
    for num in a:
        b.append(num * 2)

    print(b)

    # аналогичное с помощю генераторов списка
    c = [num * 2 for num in a]
    print(c)

    range1 = [num * 3 for num in range(1, 6)]
    print(range1)

    a = [1, 10, 12, 4, 3, 20, 55]
    a_filtered = []
    for num in a:
        if num < 10:
            a_filtered.append(num)

    print(a_filtered)

    # аналогичное с помощю генераторов списка

    b_filtered = [num for num in a if num < 10]
    print(b_filtered)
    print([num ** 2 for num in b_filtered if num <= 3])

    words = ["hello", "hey", "goodbye", "guitar", "piano"]

    print([word.capitalize() for word in words if len(word) < 6])

    print([num * 2 for num in range(10, 1, -1) if num % 2 == 0])  # range третим аргументом принимает шаг

    print([word + "." for word in words if len(word) > 5])

if __name__ == '__main__':
    # key : value
    # pass - затыка для отсутствующего кода

    # 2 равнозначных способа создания словаря
    d = {}
    d2 = dict()

    d3 = {"alex": 25, "petr": 37}
    print(len(d3))
    print(d3)
    d3["kate"] = 18
    print(d3)

    print(d3["petr"])
    # print(d3["tom"])  # ошибка такого ключа нету в словаре

    print(d3["kate"])
    d3["kate"] = 24

    print(d3)

    for key, value in d3.items():
        print("key: " + key + "|value: " + str(value))

    ex1 = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
    ex_dict = {}
    last_key = None

    for element in ex1:
        if type(element) == str:
            ex_dict[element] = []
            last_key = element
        else:
            ex_dict[last_key].append(element)

    print(ex_dict)

    ex_text = "Какойто текст непонятно о чем непонятно зачем и для чего тоже неясно"
    words = ex_text.split()
    print(len(words))

    words_count = 1
    for c in ex_text:
        if c == " ":
            words_count += 1
    print(words_count)

    if "зачем" in ex_text:
        print("слово \"зачем\" существет")

    dtest = {"hi": 10, "fck": 5}
    if "fck" in dtest:
        print("fck!")

    # задача на количество повторений в слова в строке
    ex2_text = "привет мир мир питон язык программирования язык очень крут"
    # 1-й способ
    mydict2 = {}
    for word in ex2_text.split():
        if word in mydict2:
            mydict2[word] += 1
        else:
            mydict2[word] = 1  # так как слово встретилось
    print(mydict2)

    # 2-й способ
    mydict3 = {}
    for word in ex2_text.split():
        mydict3[word] = mydict3.get(word, 0) + 1  # второй аргумент - значение которое будет возвращено
        # в случает отсутсвия ключи
    print(mydict3)

# в множетсве не может быть дубликатов а ткаже елементы не упорядочены
# в множетсве используется хеш-таблица поетому поиск елемента осуществляется очень быстро
# в листе алгоритму для нахождения необходимо пройтись по каждому елементу
# в множестве мы не можем обращается к елементам по их индексу

if __name__ == '__main__':
    a = set()
    print(a)

    b = set([1, 10, 5, "hello"])
    print(b)

    c = {1, 10, "hello"} # самый распостраненный способ создания множества
    print(c)

    # однако мы не можем создать с помощью этого синтаксиса пустое множество
    aa = {} # это словарь
    print(type(aa))

    print("##################")

    a = set()
    a.add(2)
    a.add(2)
    a.add(2)
    a.add("hello")
    a.add("hello")
    a.add(10)
    print(a)

    for el in a:
        print(el)

    mylist = [1, 2, 2, 5, "hello", "hello"]

    # как убрать дубликаты
    # print(set([mylist])) - unhashable type 'list' error | [] - лишние
    print(set(mylist))
    my_set = set()
    for el in mylist:
        my_set.add(el)

    print(my_set)

    # обратно из множества в лист
    print(list(my_set))

    print(5 in mylist)
    print("hello" in my_set)
    print("3" in my_set)

    print("NOT:")
    print(3 not in mylist)

    # сумма уникальных елементов в списке
    mylist_ex = [1, 1, 2, 5, 10, 10, 10]

    # способ 1
    my_set_ex = set(mylist_ex)
    print(my_set_ex)
    total = 0
    for el in set(mylist_ex):
        total += el

    print(total)

    # способ 2
    print(sum(set(mylist_ex)))

    def is_set_contains_all_that_list_have(p_set, p_list):
        if len(set(p_list)) == len(p_list):
            return True
        else:
            return False

    the_set = {1, 3, 4, "word"}
    the_list = ["word", 1, 4, 3, 3]
    print(is_set_contains_all_that_list_have(the_set, the_list))

    def is_list_contains_elements_that_have_set(p_set, p_list):
        print(p_set)
        print(set(p_list))
        for e in set(p_list):
            if e not in p_set:
                return False
        return True

    print(is_list_contains_elements_that_have_set({2, 5, "word"}, [5, "oh"]))

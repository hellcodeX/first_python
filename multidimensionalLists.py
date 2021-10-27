def print_matrix(arr2d):
    for cell in arr2d:
        print(cell)


if __name__ == '__main__':
    aa = [1, 2, [1, 2]]
    print(aa[2][1])

    matrix = [[1, 2, 3],
              [3, 4, 5],
              [6, 7, 8]]

    print("method1")
    for cell in matrix:
        for e in cell:
            print(str(e), end=' ')  # позволяет избежань символав новой строки
        print()

    print("method2")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')  # позволяет избежань символав новой строки
        print()

    print('a', 'b', 'c', sep='SP')  # установка разделителся между аргументами в принте

    print_matrix(matrix)

    print("create 2d array func")


    def create_2d_arr(m, n):
        array2d = []
        for cell in range(m):
            row = []
            for e in range(n):
                row.append(0)
            array2d.append(row)
        return array2d


    print_matrix(create_2d_arr(5, 5))

    test_cell = [1, 2, 3, 4, 5]

    def swap_in_cell(array1d):
        middle = int(len(array1d) / 2) # len(array1d // 2) делит на 2 целочисленно
        print(middle)
        for i in range(middle + 1):
            array1d[i], array1d[len(array1d) - i - 1] = array1d[len(array1d) - i - 1], array1d[i]

    swap_in_cell(test_cell)
    print(test_cell)

    matrix11 = [[1, 2, 3, 4],
              [3, 4, 5, 6],
              [6, 7, 8, 9]]

    for cell in matrix11:
        swap_in_cell(cell)

    print_matrix(matrix11)

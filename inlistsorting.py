def flat_list(array):
    b =[]
    def my_func(array):
        for a in array:
            if type(a) == type(array):
                my_func(a)
            else:
                b.append(a)

    my_func(array)
    print(b)
    return b

if __name__ == '__main__':
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
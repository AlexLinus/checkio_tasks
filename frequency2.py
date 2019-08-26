#checkio https://py.checkio.org/mission/sort-array-by-element-frequency/solve/
# Вариант сработал!
from collections import Counter


def frequency_sort(items):
    # your code here
    my_count = Counter()
    for item in items:
        my_count[item] +=1
    common_list = list(my_count.most_common())
    filtered_list = []
    for item in common_list:
        for i in range(0, item[1]):
            filtered_list.append(item[0])
    return filtered_list

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

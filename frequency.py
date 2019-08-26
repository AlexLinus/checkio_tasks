from collections import Counter


def frequency_sort(items):
    # your code here
    counts = dict(Counter(items))
    print(counts)
    filtered_list = []
    counts = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))
    print('Сейчас будет  counts = dict(sorted(counts.items(), key=lambda item: (item[1], item[0])))')
    print(counts)
    for item in counts.keys():
        count = 0
        while count < counts[item]:
            filtered_list.append(item)
            count += 1
    print('Перед сортировкой')
    print(filtered_list)
    return filtered_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print("Example2:")
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob', 'alex'])) == ['bob', 'bob', 'bob', 'carl', 'alex', 'alex']
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

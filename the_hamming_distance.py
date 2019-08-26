#https://py.checkio.org/ru/mission/hamming-distance2/
#Find Hamming Distance

def checkio(n, m):
    new_digit = "{0:b}".format(n)
    new_digit2 = "{0:b}".format(m)
    difference = abs(len(new_digit) - len(new_digit2))
    start_len = None
    hamming_distance = 0

    if len(new_digit2) > len(new_digit):
        start_len = len(new_digit2)
        new_digit = '0' * difference + new_digit
    else:
        start_len = len(new_digit)
        new_digit2 = '0' * difference + new_digit2

    for i in range(start_len):
        if new_digit2[i] != new_digit[i]:
            hamming_distance += 1

    return hamming_distance


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
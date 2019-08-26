def checkio(numbers_array):
    def sravni(num):
        return abs(num)
    new_array = sorted(numbers_array, key=sravni)
    print(new_array)
    return numbers_array

#These "asserts" using only for self-checking and not necessary for auto-testing
#if __name__ == '__main__':
#    print('Example:')
#    print(list(checkio((-20, -5, 10, 15))))

#    def check_it(array):
#        if not isinstance(array, (list, tuple)):
#            raise TypeError("The result should be a list or tuple.")
 #       return list(array)

checkio((-20, -5, 15, 10))
    #assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    #assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
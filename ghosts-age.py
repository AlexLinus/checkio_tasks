#Задачка с числами Фибоначчи
#https://py.checkio.org/ru/mission/ghosts-age/
#Числа фибоначи это то число, если сумма двух предыдущих чисел равна ему.
def checkio(opacity):
    age = 0
    newborn = 10000
    fib1 = 0
    fib2 = 1
    while newborn != opacity:
        age += 1
        if age == fib1 + fib2:
            newborn -= age
            fib1, fib2 = fib2, age
        else:
            newborn +=1
    return age

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
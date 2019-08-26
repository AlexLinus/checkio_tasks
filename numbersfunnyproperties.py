
def dig_pow(n, p):
    print('Сейчас будет строка и ее длина:{}. Длина: {}'.format(str(n), len(str(n))))
    raise_to_power = [i for i in range(p, p + len(str(n)))]
    print(raise_to_power)
    digit_list = [int(digit) for digit in str(n)]
    print(list(zip(digit_list,raise_to_power)))
    final_list = [a**b for a,b in zip(digit_list,raise_to_power)]
    final_calculate = sum(final_list)
    if round(final_calculate)%n == 0:
        return round(sum(final_list)/n)
    else:
        return -1

print(dig_pow(89, 1)) #1)
print(dig_pow(92, 1))#-1)
print(dig_pow(46288, 3)) #51)
def correct_phone(number):
   number_string = str(number)
   if len(number_string) == 10 and number_string.isdigit():
        return 'Номер телефона: ({}) {}-{}-{}'.format(number_string[0:3], number_string[4:6], number_string[7:8], number_string[9:10])
   else:
       return 'Номер телефона некорректен. Слишком много или мало цифр: {}'.format(number)

result = correct_phone(1234567891)
print(result)
result = correct_phone(1314556831)
print(result)
result = correct_phone(7315541123)
print(result)
result = correct_phone(7315556411221)
print(result)
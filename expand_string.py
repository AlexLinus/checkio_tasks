def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(12)) #, '10 + 2');
print(expanded_form(42))#, '40 + 2');
print(expanded_form(432))#, '40 + 2');
print(expanded_form(4251532))#, '40 + 2');
#print(expanded_form(70304))#, '70000 + 300 + 4');

my_list = ['Alex', 'Denis', 'Tima', 'Evgen']
print(enumerate(my_list))


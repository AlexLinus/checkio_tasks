#https://py.checkio.org/ru/mission/ip-network-route-summarization/

#print(int('17216120', base=2))
#print(format(172, '08b'))
#a = int('0000000000', base=2)
#https://github.com/narimiran/checkio/blob/master/ip-network-route-summarization.py

def checkio(data):
    #replace this for solution
    splitted_list = [i.split('.') for i in data]
    binar_list = []
    for item in splitted_list:
        #print(item)
        temp_list = []
        for i in item:
            temp_list.append(format(int(i), '08b'))
        binar_list.append(temp_list)
    full_binnar_list = [''.join(i) for i in binar_list]
    print(full_binnar_list)
    correct = ''
    tumblr = True

    for i in range(len(full_binnar_list[0])):
        if tumblr:
            first_chars = []
            print(first_chars)
            for item in full_binnar_list:
                first_chars.append(item[i])
            if len(list(set(first_chars))) == 1:
                print('СРАБОТАЛО!')
                correct += list(set(first_chars))[0]
                print(correct)
            else:
                print('Сработал FALSE')
                tumblr = False
    print('Сейчас будет совпадающая часть: {}'.format(correct))
    print('172 - {}, 16 - {}, 3 - {}'.format(correct[0:8], correct[8:16], correct[16:]))
    third_part = correct[16:]
    if len(third_part) <8:
        third_part += '0'*(8-len(third_part))
    new_adress = '{}.{}.{}.0/{}'.format(int(correct[0:8],2), int(correct[8:16],2), int(third_part, 2), len(correct))
    print(new_adress)
    return new_adress

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    #assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"

#Какой то список может быть длинеее, какой то короче.
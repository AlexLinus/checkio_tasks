def checkio(array):
    count = 0
    sum = 0
    for i in array:
        if count % 2 == 0:
            print(i)
            sum +=i
            count +=1
            print(sum)
        else:
            print('Сработал Else')
            count += 1
            continue
        print(sum)
        print('Сейчас будет count')
        print(count)
    return sum*array[-1]

print(checkio([0, 1, 2, 3, 4, 5]))
checkio([0, 1, 2, 3, 4, 5])# == 30, "(0+2+4)*5=30"
checkio([1, 3, 5])# == 30, "(1+5)*5=30"
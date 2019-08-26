#Restricted Sum
#https://py.checkio.org/ru/mission/restricted-sum/

#Запрет
#sum
#import
#for
#while
#reduce

def checkio(data):
    new_int = 0
    if data:
        new_int += data.pop() + checkio(data)
    return new_int


print(checkio([1, 2, 3]))
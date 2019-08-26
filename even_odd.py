def iq_test(numbers):
    my_list = [int(item)%2 for item in numbers.split(" ")]
    position = 0
    if my_list.count(0) > my_list.count(1):
        position = my_list.index(1)+1
    else:
        position = my_list.index(0)+1
    print(position)
    return position

iq_test("2 4 7 8 10")#3
iq_test("1 2 2") #1
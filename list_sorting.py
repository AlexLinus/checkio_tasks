def move_zeros(array):
    old_list = array[:]
    list = array
    print(list)
    zero = [0 for item in range(0, array.count(0))]
    filtered_list = []
    move_index = 0
    #Он короче когда удаляет элемент, список смещается и он перескакивает
    for index, item in enumerate(old_list):
        try:
            if int(item) == 0 and not (item is False):
                array.pop(index - move_index)
                move_index +=1
        except:
            continue

    return list.extend(zero)
    #your code here

filtered_list = move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
correct_test_list = ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]

if filtered_list == correct_test_list:
    print("ПРАВИЛЬНО!")
else:
    print("ОШИБКА!")




#print('Количество 0 в массиве: {}'.format(array.count(0)))
#print('Изначально array')
#print(array)
#list = [item for item in array if item != 0]
#list.extend([0 for item in range(0, array.count(0))])
#print('После фильтрации')
#print(list)
#print('Количество 0 в отфильтрованном списке: {}'.format(list.count(0)))
#new_list = [0 for item in range(0, array.count(0))]
#print(new_list)
#return list
#your code here

#['a', 0, 0, 'b', None, 'c', 'd', 0, 1, False, 5, 'hello']
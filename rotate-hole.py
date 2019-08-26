#https://py.checkio.org/ru/mission/rotate-hole/
# Rotate Hole
def rotate(state, pipe_numbers):
    step = 0
    steps = []
    new_state = state
    for i in range(0, len(state)):
        correct_list = []
        for pipe in pipe_numbers:
            if new_state[pipe] == 1:
                correct_list.append('True')
            else:
                correct_list.append('False')
        if len(set(correct_list)) == 1 and list(set(correct_list))[0] == 'True':
            steps.append(step)
            step +=1
        else:
            step += 1
        new_state.insert(0,new_state.pop())
    return steps

#ПОСМОТРЕТЬ ЕЩЕ РАЗ РАЗОБРАТЬСЯ С ALL
#Можно еще решить следующим способом
def rotate2(state, pipe_numbers):
    rotate_list = []                                #future result
    for i in range(len(state)):                     #rotate count
        new_state = state[-i:] + state[:-i]         #rotate
        #all() Проверяет, все ли указанные элементы принимают значение «истина».
        if all(new_state[n] for n in pipe_numbers): #checking by index (numbers in pipe_numbers as index of new_state)
            rotate_list.append(i)                   #if all - append to result list
    return rotate_list

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

def find_it(resultat):
    unique = list(set(resultat))
    print(unique)
    result_list = [i for i in unique if resultat.count(i)%2 != 0]
    return result_list[0]

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) #Результат должен быть 5
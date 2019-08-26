#Create Intervals
#Из множества(set) целых чисел(int) вам нужно создать список(list) замкнутых интервалов в виде кортежей(tuple) таких, чтобы интервалы охватывали все значения, найденные в множестве.

#https://py.checkio.org/ru/mission/create-intervals/
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    new_data = sorted(data)
    intervals = []
    for i in range(len(new_data)):
        if i == 0 or new_data[i] - new_data[i-1] != 1:
            intervals.append((new_data[i], new_data[i]))
        else:
            intervals[len(intervals)-1] = (intervals[len(intervals)-1][0],new_data[i])
            #Здесь мы каждый раз перезаписываем то есть (1,1), потом (1,2), потом, (1,3). И когда есть разрыв, то добавляется (1,3)(6,6) и пошли операции уже со вторым списком, то есть (6,7),(6,8) и т.д.
    return intervals

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 4, 5, 3, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    #assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"

#count-consecutive-summers
#https://py.checkio.org/ru/mission/count-consecutive-summers/
# DONE!

def count_consecutive_summers(num):
    # your code here
    list_range = [i for i in range(1, num+1)]
    count_ways = 0
    def ways_count(input_list, num):
        total_sum = 0
        ways = 0
        if input_list[0] == num and len(input_list) == 1:
            ways +=1
        else:
            for i in input_list:
                if total_sum != num or total_sum < num:
                    total_sum +=i
                elif total_sum == num:
                    ways += 1
                    break
                else:
                    break
        return ways

    while list_range:
        count_ways += ways_count(list_range, num)
        list_range.pop(0)

    return count_ways


if __name__ == '__main__':
    print("Example:")
    #print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    assert count_consecutive_summers(15) == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")

def find_uniq(arr):
    return [i for i in arr if arr.count(i) == 1][0]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))


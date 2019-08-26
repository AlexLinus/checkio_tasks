def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    new_tupple = [elements[0], elements[2], elements[-2]]
    print(new_tupple)
    return [elements[0], elements[2], elements[-2]]

print(easy_unpack((1, 1, 1, 1)))
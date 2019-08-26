def second_index(text, symbol):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    final_index = None
    position = None
    count = 0
    for i in text:
        if i == symbol:
            if position != None:
                final_index = count
                break
            else:
                position = count
        count +=1
    print(final_index)
    return final_index


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    #assert second_index("find the river", "e") == 12, "Second"
    #assert second_index("hi", " ") is None, "Third"
    #assert second_index("hi mayor", " ") is None, "Fourth"
    #assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    #print('You are awesome! All tests are done! Go Check it!')

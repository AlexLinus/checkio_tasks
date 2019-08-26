from collections import Counter
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    maximum_lenght = 0
    current_letter_lenght = 1
    last_letter = None

    for letter in line:
        if last_letter == letter:
            last_letter = letter
            current_letter_lenght +=1
            if maximum_lenght < current_letter_lenght:
                maximum_lenght = current_letter_lenght
            #print(last_letter)
        elif last_letter != letter:
            last_letter = letter
            current_letter_lenght = 1
            if maximum_lenght < current_letter_lenght:
                maximum_lenght = current_letter_lenght
            #print(last_letter)

    print(maximum_lenght)
    return maximum_lenght

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

# Разбить через counter на буквы. вырезать подстроки по этим буквам, добавить их в словарь подстрока - значение длины.

   #new_line = dict(Counter(line))
    #print(new_line)
    #cutted_lines = {}
    #for key in new_line.keys():
    #    first_position = line.find(key)
    #    last_position = line.rfind(key)
    #    cuted_line = line[first_position:last_position+1]
    #    cutted_lines[cuted_line] = len(cuted_line)
    #print(cutted_lines)
import re
import operator
def checkio(sample_text):
    lower_text = sample_text.lower()
    line = re.sub('[\.\?\s\!\d]', '', lower_text)
    print(line)
    total = {}
    print(type(5124))
    for letter in line:
        if letter not in total:
            total[letter] = line.count(letter)
    maximum = max(sorted(total.items()), key=lambda k: k[1])
    print(maximum)
    popular_key = maximum[0]
    # replace this for solution
    print(total)
    print(popular_key)
    return popular_key


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
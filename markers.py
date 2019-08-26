def between_markers(text, begin, end):
    """
        returns substring between two given markers
    """
    # your code here
    return text[text.index(begin)+1:text.index(end)]


print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    #assert between_markers('What is >apple<', '>', '<') == "apple"
    #assert between_markers('What is [apple]', '[', ']') == "apple"
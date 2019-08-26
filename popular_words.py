def popular_words(text, words): #text: str, words: list
    list_text = text.lower().split()
    result = {}
    for word in words:
        result[word] = list_text.count(word)

    print(result)
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
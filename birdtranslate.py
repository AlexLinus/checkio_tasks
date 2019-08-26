import re


def translate(phrase):
    if re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase):
        vowels = list('aeiouy')
        consonants = list('bcdfghjklmnpqrstvwxyz')
        current_index = 0
        filtered_sentence = ''
        while current_index < len(phrase):
            #if current_index >len(phrase):
            #    print('Сработало Break')
            #    break
            if phrase[current_index] in vowels:
                filtered_sentence += phrase[current_index]
                current_index += 3
            elif phrase[current_index] in consonants:
                filtered_sentence += phrase[current_index]
                current_index += 2
            else:
                filtered_sentence += " "
                current_index += 1
        return filtered_sentence
    return None


if __name__ == '__main__':
    print("Example:")
    print(translate("hleeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

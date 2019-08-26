def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    new_phrases = " ".join(phrases)
    new_phrases = new_phrases.replace('right', 'left')

    #for i in phrases:
    #    if 'right' in i:
    #        print('right')
    return "left"


if __name__ == '__main__':
    print('Example:')
    #print(left_join(("left", "right", "left", "stop")))
    left_join(("bright aright", "ok"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    #assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
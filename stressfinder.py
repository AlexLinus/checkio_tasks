def is_stressful(subj):
    """
        recoognise stressful subject
    """
    subj.replace('-', '')
    subj.replace('.', '')
    subj = subj.lower()
    words = ['help', 'urgent', 'asap']
    result = False
    if subj.count(
            '!') >= 3 or subj.isupper() or 'help' in subj.lower() or 'asap' in subj.lower() or 'urgent' in subj.lower():
        result = True
    else:
        index = 0
        promej_result = []
        for word in words:
            for i in word:
                try:
                    find_index = subj.index(i)
                    if find_index >= index:
                        index = find_index
                        promej_result.append(True)
                    else:
                        promej_result = []
                        index = 0
                        break
                except:
                    promej_result = []
                    index = 0
                    break
            if promej_result.count(True) == len(word):
                result = True
                break
            else:
                continue
    print(result)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

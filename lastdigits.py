def increment_string(strng):
    string_len = len(strng)
    try:
        if int(strng[-1]) != 9:
            strng = strng[:-1] + str(int(strng[-1]) + 1)
        print(strng)
        if int(strng[-1]) == 9:
            try:
            except:
                
    except:
        strng = strng + '1'
    return strng
increment_string('foo1')
increment_string('foo')
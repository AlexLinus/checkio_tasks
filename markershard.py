#Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
#Начальный и конечный маркеры всегда разные
#Если нет начального маркера, то началом считать начало строки
#Если нет конечного маркера, то концом считать конец строки
#Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
#Если конечный маркер стоит перед начальным, то вернуть пустую строку
#Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
#Output: Строка.
#Предусловия: не может быть более одного маркера одного типа

def between_markers(text, begin, end):
    """
        returns substring between two given markers
    """
    # your code here
    try:
        first = text.index(begin) + (len(begin))
    except:
        first = 0
    try:
        last = text.index(end)
    except:
        last = -1

    if last == -1:
        print(text[first:])
    else:
        print(text[first:last])
    return True


print('Example:')
print(between_markers('What is >apple<', '>', '<'))

# These "asserts" are used for self-checking and not for testing
between_markers('What is >apple<', '>', '<')
between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>")
between_markers('No[/b] hi', '[b]', '[/b]')
between_markers('No [b]hi', '[b]', '[/b]')
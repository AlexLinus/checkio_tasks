def namelist(names):
    names_list = [i['name'] for i in names]
    print(names_list)
    final = ""
    if len(names_list) == 0:
        return ''
    if len(names_list) > 2:
        last_items = []
        last_items.append(names_list[-2])
        last_items.append(names_list[-1])
        print('Сейчас будет last_items')
        print(last_items)
        print('Конец last_items')
        begin_items = names_list[0:int(len(names_list))-2]
        print('Сейчас будет begin_items')
        print(begin_items)
        print('Конец begin-items')
        final = final + ", ".join(begin_items) + ", " + " & ".join(last_items)
    if len(names_list) == 2:
        final = final + " & ".join(names_list)
    else:
        final = final + names_list[0]
    return final
    #your code here

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
#namelist([])
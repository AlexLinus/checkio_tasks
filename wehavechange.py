def tickets(people):
    ticket_cost = 25
    my_bancknotes = [25 for item in range(0, people.count(25))]
    result = []
    print("Сейчас будет изначальный people")
    print(people)
    for human in people:
        if human == 25:
            continue
        elif human == 50:
            if 25 in my_bancknotes:
                my_bancknotes.append(50)
                my_bancknotes.remove(25)
                result.append("YES")
            else:
                result.append("NO")
        elif human == 100:
            if my_bancknotes.count(50) >= 1 and my_bancknotes.count(25) >= 1:
                print("Сработало!")
                my_bancknotes.remove(50)
                my_bancknotes.remove(25)
                my_bancknotes.append(100)
                result.append("YES")
            elif my_bancknotes.count(25) >= 3:
                for i in range(0, 3):
                    my_bancknotes.remove(25)
                my_bancknotes.append(100)
                result.append("YES")
            else:
                result.append("NO")

    print("Сейчас будет result")
    print(result)
    print("Сейчас будет my_basnknotes")
    print(my_bancknotes)
    if "NO" in result and len(result) >= 1:
        return "NO"
    else:
        return "YES"

print(tickets([25, 25, 50]))#YES
print(tickets([25, 100]))#NO

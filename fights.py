class Warrior:
    health = 50
    power = 5
    is_alive = True

class Knight(Warrior):
    power = 7

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_2.health != 0 and unit_1.health != 0:
            unit_2.health = unit_2.health - unit_1.power
        if unit_2.health != 0 and unit_1.health != 0:
            unit_1.health = unit_1.health - unit_2.power
        print('Сработало!')
        if unit_1.health <= 0:
            unit_1.is_alive = False
        elif unit_2.health <= 0:
            unit_2.is_alive = False
    if unit_1.is_alive and not unit_2.is_alive:
        print('Победил 1')
        return True
    else:
        print('Победил 2')
        return False

chuck = Warrior()
bruce = Warrior()
fight(chuck, bruce)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

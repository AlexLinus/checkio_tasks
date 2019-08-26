#https://py.checkio.org/ru/mission/speechmodule/
#Speech Module
# 0 < number < 1000

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = ''
    def under_100(number):
        result = ''
        if 0 < number < 10:
            result += FIRST_TEN[number-1]
        elif 10 <= number < 20:
            result += SECOND_TEN[int(str(number)[1])]
        elif 20 <= number < 100:
            result += OTHER_TENS[int(str(number)[0])-2]
            if int(str(number)[1]) == 0:
                pass
            else:
                result += ' ' + FIRST_TEN[int(str(number)[1])-1]
        return result
    if number < 100:
        result = under_100(number)

    else:
        result += f'{FIRST_TEN[int(str(number)[0])-1]} {HUNDRED} {under_100(int(str(number)[1:3]))}'
    return result.rstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(4) == 'four', "1st example"
    #assert checkio(133) == 'one hundred thirty three', "2nd example"
    #assert checkio(12) == 'twelve', "3rd example"
    #assert checkio(14) == 'fourteen', "4rd example"
    #assert checkio(15) == 'fifteen', "4rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(51) == 'fifty one', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
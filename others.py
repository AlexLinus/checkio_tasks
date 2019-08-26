
#def digital_root(n):
#    numbers = [int(digit) for digit in str(n)]
#    answer = sum(numbers)
#    print(answer)
#    if answer > 9:
#        answer = digital_root(answer)
#        print('сработал if')
#    return answer


#rint(digital_root(16))
#print(digital_root(456))

#def find_short(s):
#    # your code here
#    max_lenght_word = min([len(word) for word in s.split(" ")])
#
#    return max_lenght_word  # l: shortest word length
#print(find_short("bitcoin take over the world maybe who knows perhaps"))
#print(find_short("turns out random test cases are easier than writing out basic ones"))
#print(find_short("lets talk about javascript the best language"))
#print(find_short("i want to travel the world writing code one day"))
#print(find_short("Lets all go on holiday somewhere very cold"))

def maskify(cc):
    if len(cc) > 4:
        cc = cc.replace(cc[0:len(cc)-4], '#'*(len(cc)-4))
        print(cc)
    return cc
cc = '123456789'
r = maskify(cc)

{'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}

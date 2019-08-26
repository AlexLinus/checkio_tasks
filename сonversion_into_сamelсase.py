#https://py.checkio.org/ru/mission/conversion-into-camelcase/
#Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated without any intervening characters.

def to_camel_case(name):
    return ''.join([i.capitalize() for i in name.split('_')])

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
def is_valid_IP(strng):
    strng.replace(" ", "")
    ip_list = strng.split(".")
    try:
        correct_list = []
        for item in ip_list:
            copied_item = item[:]
            if 0 < int(item) <= 255 and copied_item[0] != "0" and copied_item[:1] != "00":
                correct_list.append('TRUE')
        if correct_list.count('TRUE') == 4:
            print('TRUE')
            return True
        else:
            print('FALSE')
            return False
    except:
        return False

is_valid_IP('12.255.56.1')
is_valid_IP('1.2.3.4')
is_valid_IP('0.0.0.0')
#is_valid_IP('')
#is_valid_IP('abc.def.ghi.jkl')
#is_valid_IP('123.456.789.0')
#is_valid_IP('12.34.56')
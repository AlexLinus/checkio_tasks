#Конвертер секунд в человеческий формат времени
def make_readable(seconds):
    #Более короткий вариант решения, рабочий
    #h= seconds/60**2
    #m= (seconds%60**2)/60
    #s= (seconds%60**2%60)
    #return "%02d:%02d:%02d" % (h, m, s)
    final_time = ''
    def test_lenght(digit):
        if len(str(digit)) <2:
            return '0{}'.format(digit)
        elif len(str(digit)) == 2:
            return '{}'.format(digit)

    if seconds < 60:
        if seconds <10:
            final_time = "00:00:0{}".format(seconds)
        else:
            final_time = "00:00:{}".format(seconds)
    elif 60 <= seconds < 3600:
        minutes = seconds//60
        seconds_new = seconds%60
        final_time = '00:{}:{}'.format(test_lenght(minutes),test_lenght(seconds_new))

    elif 3600 <= seconds < 360000:
        hours = seconds//3600
        minutes = (seconds%3600)//60
        seconds_new = ((seconds%3600)%60)%60
        final_time = '{}:{}:{}'.format(test_lenght(hours),test_lenght(minutes), test_lenght(seconds_new))
    return final_time

print(make_readable(0)) #===> 00:00:00
print(make_readable(5)) #===> 00:00:05
print(make_readable(60)) #===> 00:01:00
print(make_readable(86399)) #==> 23:59:59
print(make_readable(359999)) #===> 99:59:59
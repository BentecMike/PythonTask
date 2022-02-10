# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным

from random import randrange
a = randrange(1, 8)
list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
if 1 < a < 6:
    print('будний день')
    if a == 1:
        print('сегодня {}'.format(list[0]))
    elif a == 2:
        print('сегодня {}'.format(list[1]))
    elif a == 3:
        print('сегодня {}'.format(list[2]))
    elif a == 4:
        print('сегодня {}'.format(list[3]))
    else:
        print('сегодня {}'.format(list[4]))
elif 5 < a < 8:
    print('выходной день')
    if a == 6:
        print('сегодня {}'.format(list[5]))
    else:
        print('сегодня {}'.format(list[6]))
    
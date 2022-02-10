# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным

from random import randrange
a = randrange(1, 8)
list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
if a == 1:
    print('сегодня {}'.format(list[0]))
elif a == 2:
    print('сегодня {}'.format(list[1]))
elif a == 3:
    print('сегодня {}'.format(list[2]))
elif a == 4:
    print('сегодня {}'.format(list[3]))
elif a == 5:
    print('сегодня {}'.format(list[4]))
elif a == 6:
    print('сегодня {}'.format(list[5]))
else:
    print('сегодня {}'.format(list[6]))
    
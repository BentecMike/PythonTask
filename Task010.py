# 10. Найти расстояние между двумя точками пространства

from random import randrange
x1 = randrange(-10, 10)
y1 = randrange(-10, 10)
z1 = randrange(-10, 10)
print('A = ({}, {}, {})'.format(x1,y1,z1))

x2 = randrange(-10, 10)
y2 = randrange(-10, 10)
z2 = randrange(-10, 10)
print('B = ({}, {}, {})'.format(x2,y2,z2))

from math import sqrt
AB = pow((x2 - x1),2)*0.5 + pow((y2-y1),2)*0.5 + pow((z2-z1), 2)*0.5
print(AB)
# AB1 = (pow((x2 - x1),2) + pow((y2-y1),2) + pow((z2-z1), 2))
# print(sqrt(AB1))

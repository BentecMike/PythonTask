# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

x = int(input('x = '))
y = int(input('y = '))
if x == 0 and y == 0:
    print('x,y = ({};{}) - точка начала координат'.format(x,y))
elif x >= 0:
    if y>= 0:
        print('x,y = ({};{}) - I четверть плоскости'.format(x,y))
    else:
        print('x,y = ({};{}) - IV четверть плоскости'.format(x,y))
else:
    if y >= 0:
        print('x,y = ({};{}) - II четверть плоскости'.format(x,y))
    else:
        print('x,y = ({};{}) - III четверть плоскости'.format(x,y))
  
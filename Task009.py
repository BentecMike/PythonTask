# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

a = int(input('введите номер плоскости = '))
list = ['x,y > 0', 'x < 0, y > 0', 'x,y < 0', 'x > 0, y < 0']
if 0 < a < 5:
      print(list[a - 1])    
else:
    print('введите номер четверти в диапазоне [1-4]')
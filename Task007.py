# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

from operator import truediv
x = True
y = True
z = True
def Method(x, y, z):
    a = x and y and z
    #print(a)
    a = not a
    #print(a)
    b = not x 
    #print('b {}'.format(b))
    c = not y 
    #print('c {}'.format(c))
    d = not z
    #print('d {}'.format(d))
    f = b or c or d
    #print('f {}'.format(f))
    print('a = f {} == {}'.format(a, f))
#not(x and y and z) == (not x or not y or not z)   
Method(False, False, False)
Method(True, False, False)
Method(False, True, False)
Method(False, False, True)
Method(True, True, False)
Method(False, True, True)
Method(True, False, True)
Method(True, True, True)

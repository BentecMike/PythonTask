# 1. По двум заданным числам проверять является ли первое квадратом второго

# a = int(input('введите 1 число: '))
# b = int(input('введите 2 число: '))
# if a == b**2:
#     print('{}, является квадратом, {}'.format(a, b))
# else:
#     print('{}, НЕявляется квадратом, {}'.format(a, b))




# 3. По заданному номеру дня недели вывести его название

# from random import randrange
# a = randrange(1, 8)
# list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# if a == 1:
#     print('сегодня {}'.format(list[0]))
# elif a == 2:
#     print('сегодня {}'.format(list[1]))
# elif a == 3:
#     print('сегодня {}'.format(list[2]))
# elif a == 4:
#     print('сегодня {}'.format(list[3]))
# elif a == 5:
#     print('сегодня {}'.format(list[4]))
# elif a == 6:
#     print('сегодня {}'.format(list[5]))
# else:
#     print('сегодня {}'.format(list[6]))
    



# 5. Написать программу вычисления значения функции y = f(a)
## y = a^3 * 2 + 15

# from random import randrange
# a = randrange(1, 10)
# b = pow(a,3) * 2 + 15
# print('{} = ({} ^ 3) * 2 + 15'.format(b, a))




# 7. Показать числа от -N до N

# n = int(input('введите N: '))
# for i in range(-n, n+1):
#     print(i)




# 9. Показать последнюю цифру трёхзначного числа

# a = int(input('Введите трехзначное число: '))
# a1 = round(a % 1000/100)
# if a1 != 0:
#     print('{}'.format(a1))
# else:
#     print('нет третьей цифры')     
 



# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# from random import randrange
# a = randrange(10, 100)
# b = a % 100//10 
# c = a % 10
# if b > c:
#     print('{} > {}'.format(b,c))
# else:
#     print('{1} > {0}'.format(b,c))
# print('{}, {}, {}'.format(a, b, c))




# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

# a = int(input('Введите число: '))
# b = 5
# if a % b == 0:
#     print('{} кратно {}'.format(a,b))
# else:
#     print('{} некратно {}'.format(a,b))




# 15. Дано число. Проверить кратно ли оно 7 и 23

# from random import randrange
# a = randrange(10, 1000)               #161
# b = 7
# c = 23
# if a % b == 0 and a % c == 0:
#     print('{} кратно {} и {}'.format(a,b,c))
# else:
#      print('{} некратно {} и {}'.format(a,b,c))




# 17. По двум заданным числам проверять является ли одно квадратом другого
          
# a = int(input('введите 1 число: '))
# b = int(input('введите 2 число: '))
# if a == b**2:
#     print('{}, if является квадратом, {}'.format(a, b))
# elif b == a**2:
#     print('{}, elif является квадратом, {}'.format(b, a))
# else:
#     print('{}, {} НЕявляются квадратом'.format(a, b))




# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# for x in range(0,2):
#     for y in range(0,2):
#         print(not(x or y) == (not(x) and not(y)))


#         if not(x or y) == (not(x) and not(y)):
#             print(f'При Х = {x} Y = {y} истинно')
#         else:
#             print(f'При Х = {x} Y = {y} ложно')




# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# x = int(input('x = '))
# y = int(input('y = '))
# if x > 0 and y > 0:
#     print('x,y = ({};{}) - I четверть плоскости'.format(x,y))
# elif x < 0 and y > 0:
#     print('x,y = ({};{}) - II четверть плоскости'.format(x,y))
# elif x < 0 and y < 0:
#     print('x,y = ({};{}) - III четверть плоскости'.format(x,y))
# else:
#     print('x,y = ({};{}) - IV четверть плоскости'.format(x,y))




# 20. Задать номер четверти, показать диапазоны для возможных координат

# a = int(input('введите номер плоскости = '))
# list = ['x,y > 0', 'x < 0, y > 0', 'x,y < 0', 'x > 0, y < 0']
# if 0 < a < 5:
#       print(list[a - 1])    
# else:
#     print('введите номер четверти в диапазоне [1-4]')




# 21. Программа проверяет пятизначное число на палиндромом.

# a = int(input('введите число: '))
# n = str(a)
# if 9999 < a < 100000:
#     if n[0] == n[4] and n[1] == n[3]:
#         print('{} Palindrom'.format(a))
#     else:
#         print('{} NOT Palindrom'.format(a))
# else:
#     print('Try again! ')

# n = input()                                    ## решение с интернета
# n = int(n)
# copy_n=n
# result = 0

# while(n!=0):
#     digit = n%10
#     result = result*10 + digit
#     n=int(n/10)

# print("Result is: ", result)
# if(result==copy_n):
#     print("Palindrome!")
# else:
#     print("Not a Palindrome!")



    
# 22. Найти расстояние между точками в пространстве 2D/3D (AB = √(xb - xa)2 + (yb - ya)2) //(AB = √(xb - xa)2 + (yb - ya)2 + (zb - za)2)

# from random import randrange
# x1 = randrange(-10, 10)
# y1 = randrange(-10, 10)
# z1 = randrange(-10, 10)
# print('A = ({}, {}, {})'.format(x1,y1,z1))

# x2 = randrange(-10, 10)
# y2 = randrange(-10, 10)
# z2 = randrange(-10, 10)
# print('B = ({}, {}, {})'.format(x2,y2,z2))

# from math import sqrt
# AB = pow((x2 - x1) + (y2-y1) + (z2-z1), 2)
# print(sqrt(AB))




# 23. Показать таблицу квадратов чисел от 1 до N

# n = int(input('Enter N: '))
# list = range(1, n+1)
# for i in list: 
#     print('N = {} - N^2 = {}'.format(list[i], list[i]**2))




# 24. Найти кубы чисел от 1 до N

# n = int(input('Enter N: '))
# list = range(1, n+1)
# for i in list: 
#     print('N = {} - N^3 = {}'.format(list[i], list[i]**3))




# 25. Найти сумму чисел от 1 до А

# a = int(input('Enter A: '))
# lits = list(range(1, a+1))
# print(type(lits))
# sum = 0
# for i in lits: 
#     sum += i
#     print('Sum = {} + {} = {}'.format(i, sum, sum))




# 26. Возведите число А в натуральную степень B используя цикл

# a = int(input('Enter A: '))
# b = int(input('Enter ^b: '))
# res = 1
# for i in range(b):
#     res *=a
# # i, res = 1, 1
# # while i <= b:
# #     res *= a
# #     i+=1
# print('{}^{} = {}'.format(a, b, res))




# 27. Определить количество цифр в числе

#print('количество цифр в числе = {}'.format(len(str(input('введите число: ')))))




# 28. Подсчитать сумму цифр в числе

# a = int(input('enter A: '))
# sum = 0
# while a !=0:
#     sum = sum + a % 10
#     a = a // 10 
# print(sum)


# a = input('a = ')
# res = 0
# for i in range(len(a)):
#     res = res + int(a[i])
# print(res)




# 29. Написать программу вычисления произведения чисел от 1 до N

# a = int(input('Enter A: '))
# lits = list(range(1, a+1))
# print(type(lits))
# sum = 1
# for i in lits: 
#     sum *= i
#     print('multi = {} * {} = {}'.format(i, sum, sum))




# 30. Показать кубы чисел, заканчивающихся на четную цифру

# n = int(input('Enter N: '))
# list = range(1,n+1)
# for i in list: 
#     mul = list[i]**3
#     #if mul % 2 == 0:
#     print('N = {} - N^3 = {}'.format(list[i], list[i]**3))




# 31. Задать массив из 8 элементов и вывести их на экран

# lis = range(8)
# lit = list(lis) 
# print(lit)




# 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

# lis = [0, 1] * 4
# print(lis)




# 33. Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

# from random import randint
# from math import fabs
# n=12
# a=[randint(-9,10) for i in range(n)]
# print(a)
# sum, sum1 = 0, 0
# for i in a:
#     #print(i)
#     if i >= 0:
#         sum += i
# else: 
#     sum1 = abs(i + sum1)
# print(sum, sum1)




# 34. Написать программу замену элементов массива на противоположные

# from random import randint
# a=[randint(-12,12) for i in range(10)]
# print(a)
# for i in a:
#     print(i*-1, end = " ")

# lis = range(8)
# lit = list(lis)
# for i in lit:
#     print(i*-1)
# print(lit)




# 35. Определить, присутствует ли в заданном массиве, некоторое число

# from random import randint

# k = int(input('Enter k: '))
# a=[randint(1,12) for i in range(10)]
# print(a)
# print(k in a)




# 36. Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

# from random import randint

# a = [randint(100, 1000) for i in range(15)]
# print(a)
# sum, sum1 = 0, 0
# for i in a:
#     if i % 2 == 0:
#         sum = sum + 1
#     else:
#         sum1 = sum1 + 1
# print(f'четных = {sum}, нечетных = {sum1}')




# 37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

# from random import randint

# a = [randint(1, 150) for i in range(123)]
# print(a)
# sum = 0
# for i in a:
#     if 10 < i < 100:
#         sum = sum + 1
# print(sum)




# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции

# from random import randint

# a = [randint(1, 5) for i in range(10)]
# print(a)
# sum = 0
# for i in a[1:: 2]:  
#     sum = i + sum
# print(sum)




# 39. Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint

# a = [randint(1, 5) for i in range(12)]
# print(a)
# k = 0
# for i in a:
#     if k < len(a)//2:
#         c1 = i * a[len(a) - k - 1] 
#         print(f'{i} * {a[len(a) - k - 1]} = {c1}')
#     k = k + 1
        
        


# 40. В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

# from random import randint

# a = [randint(1, 200) for i in range(12)]
# print(a)
# print(f' min = {min(a)}, max = {max(a)}; delta = {max(a) - min(a)}')




# ## Почувствуй себя лидом
# 41. Выяснить являются ли три числа сторонами треугольника
# 42. Определить сколько чисел больше 0 введено с клавиатуры
# 43. Написать программу преобразования десятичного числа в двоичное
# 44. Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы
# 45. Показать числа Фибоначчи
# 46. Написать программу масштабирования фигуры
# 47. Написать программу копирования массива
##Вывести квадрат числа

#a = int(input('введите число: '))
#print('Квадрат числа {} - это {}'.format(a, a**2))


##Даны два числа. Показать большее и меньшее число
#a = int(input('введите число: '))
#b = int(input('введите число: '))
#
#if a > b:
#    print('Максимальное число - ', a)
#    print('Минимальное число - ', b)
#else:
#    print('Минимальное число - ', b)
#    print('Максимальное число - ', a)

## Найти максимальное из трех чисел

# list = []
# for i in range(3):
#     a = int(input())
#     list.append(a)
# print(max(list))

#a = 2
#b = 4
#c = 6
#max = a

#if b > max:
#    max = b
#if c > max:
#    max = c
#print(max)

## Выяснить является ли число чётным
#a = int(input('Введите число: '))

#if a % 2 == 0:
#    print(a, 'четное число')
#else:
#    print(a, 'нечетное число')


## Показать четные числа от 1 до N
# list = range(1, 10)
# for i in list:
#    if list[i] % 2 == 0:
#        print(list[i])


## Показать вторую цифру трёхзначного числа
# a = int(input('Введите трехзначное число: '))
# print(a % 100 // 10)
# print(f"Вторая цифра этого числа: {input('Введите трехзначное число: ')[1]}")


## Удалить вторую цифру трёхзначного числа
# a = int(input('Введите трехзначное число: '))
# a1 = round(a % 1000/100)
# a3 = round(a % 10, 1)
# print('{}{}'.format(a1,a3))

# num = int(input('Введите трехзначное число '))
# res = num % 10 + 10 * (num // 100)
# print(res)


##Найти третью цифру числа или сообщить, что её нет
a = int(input('Введите трехзначное число: '))
a1 = round(a % 10)
if a > 99 and a < 1000:
    print('{}'.format(a1))
elif a > 999:
    print('{} это не трехзначное число'.format(a))
else:
    print('нет третьей цифры')     
 



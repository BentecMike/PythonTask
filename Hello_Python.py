## print('Hello world!!')


# типы данных и переменные
# int, float, value

#value = None
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#value = 12334
#print(type(value))

#s = 'qwerty'
#print(s)                # вывод строки 
#s = 'qwe "rty'
#print(s)  
#s = 'qwe \nrty'
#print(s)  

#print(a, '-' , b,'-',  s)
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}')
#print('{2} - {1} - {0}'.format(a, b, s))

#f = True
#print(f)

#list = [1, 2, 5]
#print(list)

#list = ['1' , '2' , '5']
#print(list)

#list = ['1' , 2 , True, 5]
#print(list)

## ввод и вывод данных 

#print('введите а')
#a = int(input())                 # если без int тогда получим сложение строк   
#print('введите b')
#b = float(input())
#print(a, '+', b, '=', a+b)

# Сокращенные операции

#a = 1.3
#b = 3                   # round(a * b, 3) - округляет числа до 3
#c = round(a * b, 3)       # // деление в целых числах, ** возведение в степень
#print(c)

#a = 3
#a = a + 5      # a +=5
#print(a)

## логические операции

#a = 1 > 4 and 2 > 3
#print(a)

#a = 'qwe'
#b = 'qwe'
#print(a==b)

#a = [1,23]
#b = [1,2]
#print(a==b)

#a = 1 < 3 < 5
#print(a)

#func = 1
#T = 4
#x = 123

#print(func<T>(x))


#f = 1 > 2 or 4 < 6
#f = [1, 2, 3, 4]
#print(f)
#print(2 in f)
#print(not 2 in f)

#is_odd = f[0] % 2 == 0      ## = not f[0] % 2
#print(is_odd)

#a = int(input('a ='))
#b = int(input('b ='))
#if a > b:
#    print(a)
#else:
#    print(b)

##while
#orig = 23
#inver = 0
#while orig !=0:
#    inver = inver * 10 + (orig % 10)
#    orig //= 10
#    print(orig)
#else:
#    print('Пожалуй')
#    print('хватит ')
#print(inver)

## for  for i in enumeration

# for i in 1,2,3,4:
#    print(i**2)

#list = [1, 3, 5, 2, 7]
#for i in list:
#    print(i**2)

#r = range(10)
#for i in range(5): ### range (1, 5)    ### range(1, 10, 2)
#    print(i)

#for i in 'qwe - rty':
#    print(i)

#text = 'съешь еще этих мягких французских булок'
#print(len(text))       ##39
#print('еще' in text)       ##true
#print(text.isdigit())      ##False
#print(text.islower())       ##True
#print(text.replace('еще', 'ЕЩЕ'))

#for c in text:
#    print(c)

#print(text[0])     #c
#print(text[1])     #ъ
#print(text[len(text)-1])     #k
#print(text[-5])     #б
#print(text[:])     #print text
#print(text[2:5])     #ешь
#print(text[0:len(text):6])     #cеикакл
#print(text[::6])     #cеикакл


##lists

#numbers = [1,2,3,4,5]
#print(numbers)
#ran = range(1,6)
#print(type(ran))
#numbers = list(ran)
#print(type(numbers))

#print(numbers)
#numbers[0] = 10
#print(f'{len(numbers)} len')
#print(numbers)
#for i in numbers:
#    i*=2
#    print(i)
#print(numbers)

#colors = ['red', 'green', 'blue']

#for e in colors:
#    print(e) ##red gren blue

#for e in colors:
#    print(e*2)     ##redred greengreen blueblue

#colors.append('gray')
#print(colors == ['red', 'green', 'blue', 'gray'])
#colors.remove('red') ##del colors[0]
#print(colors)



# functions deffunction_name(x):

# def f(x):
#    if x == 1:
#        return 'Целое'
#    elif x == 2.3:
#        return 23
#    else:
#        return

#arg = 2
#print(f(arg))
#print(type(f(arg)))






# Lection002

# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# data.writelines(colors)   # разделителей не будет
# data.writelines('\nLine 2\n')   # разделителей не буде
# data.writelines('LINE 33\n')   # разделителей не буде
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# другой способ дописывать в файл
# with open('file.txt', 'a') as data:
#     data.write('line 123\n')
#     data.write('line 00022\n')


# вызов функции из файла
# import Hello_Python as h
# print(h.f(1))

# функции
# def new_string(symbol, count):
#     return symbol*count

# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))     # typeError missing 1 required....

# def new_string(symbol, count = 3):
#     return symbol*count

# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))     # !!!
# print(new_string(4))       # 12


# передача неограниченных аргументов
# def const(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(const('a', 's', 'd', 'w'))    # asdw
# print(const('a', '1', 'd', '3'))    # a1d3
# print(const(1, 2, 3, 5))            # TypeError

# def const(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res
# print(const(1, 2, 3, 5))            # 11


# рекурсия
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
#     print(list)


# кортежи константы
# e = ()
# print(type(e))       # tuple

# e = (1,)
# print(type(e))       # tuple

# e = (28, 9, 1990)
# print(type(e))       # tuple

# colors = ['red', 'green', 'blue3']
# print(colors)         # ['red', 'green', 'blue3']

# e = tuple(colors)
# print(e)                 # ['red', 'green', 'blue3']

a = (3, 4, 5, 41)
print(a)
print(a[-2])



# словари -  неупорядоченные коллекции 
# произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '*',
#         'left': '7',
#         'down': '6'
#     }
# # print(dictionary) # {'up': '*', 'left': '7', 'down': '6'}
# # print(dictionary['left'])    # 7 

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)



# множества (type set)
# colors = {'red', 'green'}
# print(colors)



# Lection003


# def f(x):
#     x**2

# g = f
# print(type(g))
# print(g(1))
# print(f(1))


# def f(x):
#     return x**2

# g = f
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def calc1(x):
#     return x+10

# # print(calc1(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)








# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y+1

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     return(op(a,b))

# calc(sum, 4, 5)
# calc(lambda x, y: x+y+1, 4, 5)





# list = []

# for i in range(1, 101):
#     if i%2 == 0:
#         list.append(i)
# print(list)

# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1,21) if i%2 ==  0]
# print(list)


# мой вариант
# list = [1,2,3,5,8,15,23,38]
# def f(x):
#     return x**2

# list1 = [(i,f(i)) for i in list if i%2 == 0]
# print(list1)

# вариант Сергея
# path = '/Users/mikhail.silonov/Desktop/Geekbrains/python/doc.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[:space_pos+1]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)


# вариант с лекции
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)







# li = [x for x in range(1,20)]

# li = list(map(lambda x: x + 10, li))
# print(li)


# data = list(map(int,(input().split())))
# print(data)

# data = list(map(int,'1 2 3'.split()))
# for e in data:
#     print(e)

# print('---')
# for e in data:
#     print(e)


# вариант с лекции после изучения функции map

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# изучение функции filter
# data = [ x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

# вариант с лекции после изучения функции map

# data = '1 2 3 5 8 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# функция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [ 4, 5, 9, 14, 7]
# salary = [111,222,333]

# data = list(zip(users, ids, salary))
# print(data)

# функция enumerate

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [ 4, 5, 9, 14, 7]
# salary = [111,222,333]

# data = list(enumerate(users))
# print(data)
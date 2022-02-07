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

#for i in 1,2,3,4:
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



##functions deffunction_name(x):

#def f(x):
#    if x == 1:
#        return 'Целое'
#   elif x == 2.3:
#        return 23
#    else:
#        return

#arg = 2
#print(f(arg))
#print(type(f(arg)))

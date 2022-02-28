# 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

n = int(input('enter n: '))
a = []
sum = 0
for i in range(1, n+1): 
    z = a.append((1+1*i)*i)
    sum += (1+1*i)*i
print(f'{a}, sum = {sum}')

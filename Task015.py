# Написать программу получающую набор произведений чисел от 1 до N.
#     Пример: пусть N = 4, тогда
#     [ 1, 2, 6, 24 ]

n = int(input('Enter n: '))
a = [1]

z = 1
for i in range(n):
    mul = a.append(a[i] * z)
    z += 1

del a[0]
 
print(a)

# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('enter N: '))
a = [1]
for i in range(n - 1): 
    z = a.append(a[i] * (-3))
print(a)   

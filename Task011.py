# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# мой вариант

n = int(input('enter N: '))
a = [1]
for i in range(n - 1): 
    z = a.append(a[i] * (-3))
print(a)   

# вариант с семинара 
def create_list(n):
    lst = []
    spam = 1
    for i in range(n):
        lst.append(spam)
        spam *= -3
    return lst

print(create_list(6))
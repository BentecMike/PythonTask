# 14. Подсчитать сумму цифр в вещественном числе.

a = input('Enter a: ')
a = a.replace(".", "")
a = a.replace(",", "")
sum = 0
for i in range(len(a)):
    sum = int(a[i]) + sum
print(f'sum = {sum}')

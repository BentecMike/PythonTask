# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

a = int(input('enter a: '))

if a % 30 == 0: # or a % 5 != 0 and a % 10 != 0 or a % 15 != 0:
    print('{} кратно 30'.format(a))
elif a % 5 == 0 and a % 10 == 0 or a % 15 == 0:
    print('{} кратно 5 и 10 или 15'.format(a))
else:
    print('{} некратно 5 и 10 или 15 или 30'.format(a))


# Реализовать алгоритм перемешивания списка
from random import randint

list1 = [x for x in range(1,8)] 
print(list1)

for i in range(len(list1)):
    list1[i], list1[randint(1, len(list1)-1)] = list1[randint(1, len(list1)-1)], list1[i]    

print(list1)
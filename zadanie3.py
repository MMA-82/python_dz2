#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
import random
list = []
l = int(input('Введите длину списка: '))
for i in range(l):
    list.append(random.randint(0, 100))
print(list)

for i in range(l):
    mix = random.randint(0, l-1)
    temp = list[i]
    list[i] = list[mix]
    list[mix] = temp
print('Перемешанный список:')
print(list)
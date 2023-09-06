# # Перейти к содержимому
# # Словари (Dict) / Методы словарей
# # Если есть возможность, то напишите двумя вариантами, обычный
# # и с генератором словаря
# # 1) Есть два словаря, объедините их:
print('-' * 10, 'Задача № 1', '-' * 10)
from pprint import pprint
dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
dict4 = {a: b for a, b in dict1.items()}
dict4.update(dict2)
pprint(dict4)
#
# # 2) Напишите сценарий Python для создания и печати словаря,
# содержащего число (от 1 до n включительно)
# (где n — введенное пользователем число) в форме (x, x * x).
print('-' * 10, 'Задача № 2', '-' * 10)
num = input('Введите число: ')
if num.isdigit():
    num = int(num)
    dict_num = {a: a**2 for a in range(1, num + 1)}
    print(dict_num)
# #
# # 3) Напишите код для суммирования всех значений словаря
##и вывод среднего арифметического значения.
print('-' * 10, 'Задача № 3', '-' * 10)
num1 = input('Введите число: ')
if num1.isdigit():
    num1 = int(num1)
    val_sum = 0
    dict_num1 = {}
    #dict_num1 = {a: a for a in range(num1)}
    for a in range(num1 + 1):
        dict_num1[a] = a
        val_sum += a
    evr = val_sum / num1
    print(dict_num1)
    print(f'Сумма всех значений: {val_sum}')
    print(f'Среднее арифметическое: {evr}')
# #
# # 4) Напишите код для объединения двух списков в словарь ключ: значение. СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)
# #
# #
# # 5) Есть словарь координат городов:
# #
# # cities = {
# # 'Moscow': (550, 370),
# # 'London': (510, 510),
# # 'Paris': (480, 480),
# # }
# # Составьте словарь расстояний между городами по формуле:
# #
# #
# # например расстояние между Лондоном и Парижем:
# #
# #
# # Используйте часть кода:
# #
# # distances = {}
# # moscow = cities['Moscow']
# # london = cities['London']
# # paris = cities['Paris']
#

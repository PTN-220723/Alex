# # # # Списки (List) / Методы списков
# # # # 1) Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # # # Выведите в отдельный список числа, которые меньше или равны 5
# # # # и числа, которые больше 5.
# # # #------------------------------ Задание № 1 ---------------------------
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# smol = []
# big = []
# for i in a:
#     if i <= 5:
#         smol.append(i)
#     else:
#         big.append(i)
# print(('-' * 10), ' Задание № 1', ('-' * 10))
# print(f'Список чисел меньше или равных 5 {smol}')
# print(f'Список чисел больше 5 {big}')
#
# # # 2) Вы принимаете от пользователя его имя, фамилию, возраст.
# # # Сохраните их в соответствующие переменные.
# # # Сохраните полученные значения в список.
#
# print(('-' * 10), ' Задание № 2', ('-' * 10))
# first_name = input('Введите Ваше имя: ')
# last_name = input('Введите Вашу фамилию: ')
# age = int(input('Введите Ваш возраст: '))
# user = []
# user.append(first_name)
# user.append(last_name)
# user.append(age)
# print(f'Список данных пользователя: {user}')
# # #
# # #
# # # # 3) Напишите программу, которая принимает от пользователя секвенцию чисел,
# # # # разделенных запятой и пробелом.
# # # # После чего запишите каждое число в список.
# #
# print(('-' * 10), ' Задание № 3', ('-' * 10))
# str_numbers = input('Введите секвенцию чисел разделенных запятой и пробелом: ')
# list_numbers = str_numbers.split(', ')
# list_numbs = []
# for num in list_numbers:
#     if num.isdigit():
#         list_numbs.append(num)
# print('Список чисел: ', list_numbs)
#
# # #
# # # #
# # # # 4) Напишите программу, которая принимает пример со СЛОЖЕНИЕМ у пользователя
# # # # и затем выдает результат. (решите с помощью генератора списка)
# print(('-' * 10), ' Задание № 4', ('-' * 10))
# str = input('Введите пример со сложением: ')
# list_numbs = str.split(' + ')
# #list_digits = []
# sum = 0
# # for num in list_numbs:
# #     if num.isdigit():
# #         list_digits.append(int(num))
# list_digits = [int(num) for num in list_numbs if num.isdigit()]
# #list_digits = [list_digits.append(int(num)) for num in list_numbs if num.isdigit()]
#
# for i in list_digits:
#     sum += i
# print(list_digits)
# print(sum)
#
# # # 5) Напишите программу, которая будет принимать три имени в качестве входных данных
# # # от пользователя в одном input() вызове функции.
# print(('-' * 10), ' Задание № 5', ('-' * 10))
# name_str = input('Введите три имени разделенных между собой пробелом: ')
# name_list = name_str.split(' ')
# if len(name_list) == 3:
#     nm_list = [i for i in name_list]
#     for i in range(3):
#         if i == 0:
#             print(f'Первое имя: {nm_list[i]}')
#         elif i == 1:
#             print(f'Второе имя: {nm_list[i]}')
#         elif i == 2:
#             print(f'Третье имя: {nm_list[i]}')
# else:
#     print('Неверное количество имен')
#
# #
# # # 6) Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7].
# # # напишите программу, которая превращает каждый элемент списка в его квадрат.
# print(('-' * 10), ' Задание № 6', ('-' * 10))
# numbers = [1, 2, 3, 4, 5, 6, 7]
# sqw = [num ** 2 for num in numbers]
# print(numbers)
# print(sqw)
#
# # # 7) Создайте список из любимых вами блюд.
# # #
# # # Создайте список из любимых блюд вашего друга, скопировав свой список.
# # # Убедитесь что два списка разные, добавив по одному разному блюду в каждый список.
# # # Выведите два списка.
# print(('-' * 10), ' Задание № 7', ('-' * 10))
# my_food = ['плов', 'шурпа', 'борщ']
# friends_food = my_food.copy()
# my_food.append('мороженое')
# print(f'Список моих любимых блюд: {my_food}')
# friends_food.append('самса')
# print(f'Cписок любимых блюд друга: {friends_food}')
#
# # # 8) Создайте переменную user_num, которая будет принимать от пользователя число.
# # # Создайте числовой список от 1 до значения из переменной user_num
# # # (значение из переменной включительно). Выведите сам список и сумму его чисел.
# print(('-' * 10), ' Задание № 8', ('-' * 10))
# user_num = input('Введите число: ')
# if user_num.isdigit():
#     user_num = int(user_num)
#     user_list = []
#     sum1 = 0
#     for i in range(user_num):
#         user_list.append(i + 1)
#         sum1 += i + 1
#     print(f'Список чисел в диапазоне от 1 до {user_num}: {user_list}')
#     print(f'Сумма чисел списка равна: {sum1}')
# #
# # # 9) Создайте два числовых списка от 1 до 100.
# # Первый будет состоять только из четных чисел, а второй из нечётных.
# # Выведите сам список и сумму его чисел.
# print(('-' * 10), ' Задание № 9', ('-' * 10))
# even_list = []
# odd_list = []
# even_sum = 0
# odd_sum = 0
# for i in range(100):
#     if i % 2 == 0:
#         even_list.append(i)
#         even_sum += i
#     elif i % 2 != 0:
#         odd_list.append(i)
#         odd_sum  += i
# print(f'Список четных чисел: {even_list}')
# print(f'Сумма четных чисел: {even_sum}')
# print(f'Список нечетных чисел: {odd_list}')
# print(f'Сумма нечетных чисел: {odd_sum}')
#
# # #
# # # 10) Напишите программу, которая выводит все четные числа из списка
# # в исходном порядке, и останавливается когда число равно 815.
# # # numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
# print(('-' * 10), ' Задание № 10', ('-' * 10))
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
#
# #numbers1 = [numbers1.append(i) for i in numbers if i % 2 == 0 and i != 815]
# numbers1 = []
# for i in numbers:
#     if i % 2 == 0:
#         numbers1.append(i)
#     elif i == 815:
#         break
# print(numbers1)
# # # 11) Подсчитайте общее количество цифр в числе.
# # #
# # # Например, число 75869 , поэтому на выходе должно быть 5 .
# print(('-' * 10), ' Задание № 11', ('-' * 10))
# num = 75869
# num = str(num)
# print(num)
# print(f'Количество цифр в числе {num} равно {len(num)}')
# while True:
#     user_num = input('Введите положительное число: ')
#     if user_num.isdigit():
#         print(f'Количество цифр в числе {user_num} равно {len(user_num)}')
#     elif not user_num or user_num == 'exit':
#         break

# # #
# # # 12) ** Напишите программу для отображения всех простых чисел в диапазоне (Учтите что пользователь может ввести отрицательное число)
# # #
# # # (Для справки: Простое число — это число, которое нельзя получить путем умножения других целых чисел. Простое число — это натуральное число больше 1, которое не является произведением двух меньших натуральных чисел.
# # #
# # # Например:
# # # — 6 не является простым числом, потому что его можно получить как 2 × 3 = 6
# # # — 37 — простое число, потому что никакие другие целые числа не умножаются вместе, чтобы получить его.)
# # #
# # #
# # # Учтите что пользователь может ввести отрицательное число
# # #
# # #
# # # 13) *** Обработать строку ospf_route и вывести информацию на стандартный поток вывода как на картинке ниже:
# # #
# # # ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
# # #
# # # для практики возьмите список маршрутов со своего роутера и попробуйте преобразить вывод всех таблиц маршрутов
# # #
# # # 14) *** Получите список VLANов со строки:
# # #
# # # config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# # #

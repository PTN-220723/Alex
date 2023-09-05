# products = ['bread', 'milk', 'banana']
# print(products)
# while True:
#     user_text = input('Введите команду: ')  # add monkey или delete monkey
#
#     if len(user_text.split()) == 2:
#         #command = user_text.split()[0]
#         #value = user_text.split()[1]
#         command, value = user_text.split()
#         #print(command)
#         #print(value)
#         if command == 'add':
#             if value in products:
#                 print(f'Продукт {value} уже есть в списке {products}')
#             else:
#                 products.append(value)
#                 print(f'Добавил {value} в список {products}')
#         elif command == 'delete':
#             if value in products:
#                 products.remove(value)
#                 print(f'Удалили {value} из списка {products}')
#             else:
#                 print(f'Продукта {value} и так нет в списке {products}')
#     elif len(user_text.split()) == 1 and user_text.split()[0] == 'exit':
#         break
#     elif not user_text:
#         print('Неверная команда. Читайте документацию.')
#     else:
#         print('Вы ввели неверное значение!')

# tuple1 = ('1, 5, 7', '12, 15', '17', '32')
# print(tuple1)
# tuple2 = sorted(tuple1)
# print(tuple2)

# action = ['like', 'dislike']
# all_action = dict.fromkeys(action, 0)
# print(all_action)

# string = 'Micros'
# list_string = list(string)
# print(list_string)
# dict_string = dict.fromkeys(list_string, 100)
# print(dict_string)
# dict_string1 = {a : 10 for a in string}
# print(dict_string1)
#print(dict.keys(list_string, 11))

# lst = [12, 5, 7, 12, 9, 12]
# cnt = lst.count(12)
# print(cnt)
# for i in range(cnt):
#     lst.remove(12)
# print(lst)

print(('-' * 10), ' Задание № 4', ('-' * 10))
str = input('Введите пример со сложением: ')
list_numbs = str.split(' + ')
# list_digits = []
sum1 = 0
# for num in list_numbs:
#     if num.isdigit():
#        list_digits.append(int(num))
list_digits = [int(num) for num in list_numbs if num.isdigit()]
#list_digits = [list_digits.append(int(num)) for num in list_numbs if num.isdigit()]

for i in list_digits:
    sum1 += i
print(list_digits)
print(sum1)
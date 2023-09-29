# files = open('files/byron.txt', 'r', encoding='UTF-8')
# print(files.closed)
# print(files.read())
# rd = files.read()
# print(rd)
# files.close()
# print(files.closed)
# #####################################
#
# files = open('files/byron.txt', 'r', encoding='UTF-8')
# context = files.read().split()
# print(type(context))
# # for line in context:
# #     if line == 'quickly':
# #         print('Yess!!!')
# if 'quickly' in context:
#     print('Ok')
# print(context)
# print(len(context))
# for line in context:
#     print(line)
# files.close()
##################################
# files = open('files/byron.txt', 'r', encoding='UTF-8')
# context = files.read()  # без split()
# print(type(context))
# print(len(context))
#
# for line in context:
#     print(line)         # вывод познаково
# files.close()
#####################################################
# files = open('files/byron.txt', 'r', encoding='UTF-8')
# for lines in files:
#     #    print(lines)            # вывод построчно str
#     print(lines.rstrip())  # вывод построчно с удалением пробелов справа
# #    print(lines.split())    # вывод построчно списком
# files.close()
######################################################
############# Запись в файл ##############
# file = open('test.txt', mode='w')       # w перезаписывает файл
# file.write('1111111\n')
# file.close()
#
# file = open('test.txt', mode='a')       # a добавляет в файл (если файл не существует, то создает его)
# file.write('2222222\n')
# file.close()
#
# file = open('test.txt', mode='a')
# file.write('3333333\n')
# file.close()
###################
# file = open('test2,txt', 'w', encoding='UTF-8')
# for i in range(100):
#     file.write(f'Проход №{i}. Привет!\n')
# file.close()
########## Копирование файла #################
# file_read = open('files/pushkin.txt', mode='r', encoding='UTF-8')
# file_write = open('pushkin-copy.txt', mode='w', encoding='UTF-8')
#
# context = file_read.read()
# file_write.write(context)
#
# file_write.close()
# file_read.close()

# with open('files/pushkin.txt', mode='r', encoding='UTF-8') as f1:
#     with open('pushkin-copy2.txt', mode='w', encoding='UTF-8') as f2:
#         context = f1.read()
#         f2.write(context)

# with open('files/pushkin.txt', encoding='UTF-8') as f1, open('pushkin-copy3.txt', mode='w', encoding='UTF-8') as f2:
#     context = f1.read()
#     f2.write(context)

#################################
# with open('files/romeo.txt') as file:    # mode='r' при чтении стоит по умолчанию.
#                                         # поэтому указывать 'r' не обязательно. encoding='UTF-8' тоже не обязателен
#                                         # потому что текст на латинице.
#     context = file.read()
#     print(context)
#     print(file.closed)                  # при конструкции with open(...) as f закрывать файл не нужно.
#                                         # Он автоматически закрывается программой.
#
# print(file.closed)
###########################
# try:
#     with open('files/romeo.txt') as file:
#         context = file.read()
#         print(context)
#         print(file.closed)
#         raise OSError
# except:
#     print('ERROR')
#
# print(file.closed)

#################################
# with open('files/nature.jpg', mode='rb') as jpg:
#     context = jpg.read()
#     for i in range(1, 11):
#         new_file = open(f'files/nature_copy{1}.jpg', mode='wb')
#         new_file.write(context)
#         new_file.close()
#######################################
### Функции
##################################
# def my_divmod(a, b):
#     return (a // b, a % b)
#
#
# my_number = my_divmod(10, 3)
# print(my_number)
###########################
# def max_number(num1, num2):
#     print(f'Глобальные переменные {a} и {b}')
#     print(f'Локальные переменные {num1} и {num2}')
#     if num1 > num2:
#         return num1
#     elif num2 > num1:
#         return num2
#     else:
#         return 'Числа равны'
#     print('Конец функции')          # После return ничего не распечатывается
#
# a = 12
# b = 33
# result = max_number(a, b)
# print(result)
###################################
# def my_calc(a, b, action):
#     if action == '+':
#         return a + b
#     elif action == '-':
#         return a - b
#     elif action == '*':
#         return a * b
#     elif action == '/':
#         return a / b
#
#
# result1 = my_calc(50, 60, '+')
# result2 = my_calc(50, 60, '-')
# result3 = my_calc(50, 60, '*')
# result4 = my_calc(50, 60, '/')
# print(result1)
# print(result2)
# print(result3)
# print(result4)
#######################################
# def my_calc(a, b, action='+', verbose=False):   #  verbose=... это параметр с ключем
#     if verbose:
#         return f'{a} + {b} = {a + b}'
#     else:
#         if action == '+':
#             return a + b
# result1 = my_calc(50, 60, verbose=True)         #  verbose=... это аргумент с ключем - ключевой аргумент
# print(result1)
#############################################
##### Очень хорошая проверка типа входной переменной ###############
# def check_param(age):
#     if isinstance(age, str) and age.isdigit():
#         return int(age)
#     elif isinstance(age, int):
#         return age
#     else:
#         print('Вы введли не числовое значение, значение по умолчанию 18 лет')
#         return 18
#
#
# def my_age(age=10):
#     age = check_param(age)
#     if 0 < age <= 18:
#         print('Вам нужно учиться')
#     elif 18 < age <= 50:
#         print('Вам нужно работать')
#     elif 50 < age <= 59:
#         print('Вам скоро на пенсию')
#     elif 60 < age <= 110:
#         print('Вы пенсионер')
#     else:
#         print('Вы сказочник')
#
#
# my_age(-5)
##############################
list1 = [1, 2, 3, 4, 5, 6]
def from_int_to_str(list1):
    return [str(i) for i in list1]


list2 = from_int_to_str(list1)
print(list1)
print(list2)



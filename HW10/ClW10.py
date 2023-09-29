# def calculator(a, b, /, *, action='+', verbose=True):  # * указывает, что последующие
#     # параметры обязательно передавать с ключем (ключевые параметры)
#     # / указывает, что параметры, находящиеся слева от знака, должны передаваться
#     # только позиционными аргументами.
#     """
#     Простой калькулятор
#    принимает int:param a:
#    принимает int:param b:
#     принимает + - / * :param action:
#     True False :param verbose:
#     Возвращает result :return:
#     """
#     if action == '+':
#         if verbose:
#             return f'{a} + {b} = {a+b}'
#         else:
#             return a + b
#
#
# # x = 5
# # y = 10
# a = calculator(5, 10, action='+', verbose=True)
# print(a)
# print(calculator.__doc__)
####### args kwargs ############
# def pitzza(dough, cheese, meat, *args, **kwargs):   # args - (необязательное) неограниченное количество
#     # позиционных аргументов
#     # kwargs - необязательное неограниченное кол-во ключевых аргументов
#     # * - указатель на то, что будет позиционный-е аргумент-ты
#     # ** - указатель на то, что последуют ключевые аргументы
#     """Функция, через которую можно заказать пицу"""
#     print(f'Приготовили пицу из теста {dough}, с  сыром {cheese} и мясом {meat})')
#     if args:
#         print(f'Дополнительные аргументы: {args}')
#     elif kwargs:
#         print(f'Дополнительные услуги: {kwargs}')
#
#
# pitzza('слоеное', 'пармезан', 'курица')
# pitzza('слоеное', 'пармезан', 'курица', 'анчоусы', 'помидорки чери', 'докторская колбаса')
# pitzza('слоеное', 'пармезан', 'курица', payment='Click', delivery=True)
#########################################################################
############# Анотация типов в функции #################
# def upper_to_lower(word: str) -> str:
#     """
#     Функция принимает текст и возвращает его в нижнем регисте
#    str :param word:
#    str :return:
#     """
#     return word.lower()
#
#
# print(upper_to_lower('PYTHON'))
###################################
# def str_to_int_for_iterable(var: list) -> list:
#     list1 = []
#     for i in var:
#         list1.append(int(i))
#     return list1
#
#
# list1 = ['10', '20', '30']
# list2 = str_to_int_for_iterable(list1)
# print(list1)
# print(list2)
######################3
# def str_to_int_for_iterable(var: list) -> list:
#     """Короткая версия"""
#     return [int(i) for i in var]
#
#
# list1 = ['10', '20', '30']
# list2 = str_to_int_for_iterable(list1)
#
# print(list1)
# print(list2)
# print(str_to_int_for_iterable.__annotations__)
# print(str_to_int_for_iterable.__doc__)
#########################3
######### zip() ################
# team_name = ['management', 'sales', 'hr', 'production', 'admins']
# vlan_number = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
# dict1 = {}
# for i in range(len(team_name)):
#     dict1[team_name[i]] = vlan_number[i]
#
# print(dict1)
#####
# team_name = ['management', 'sales', 'hr', 'production', 'admins']
# vlan_number = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
# dict1 = zip(team_name, vlan_number) # соединяет 2 списка в словарь, выводит только ключи имеющие значение (пары).
#                                     # При наличии лишний ключей или значений
#                                     # игнорирует их и ошибки не выдает.
# print(dict1)                    # Выводит как объект
# dict2 = dict(zip(team_name, vlan_number))
# print(dict2)                    # Выводит как список
# dict3 = zip(team_name, vlan_number)
# print(dict(dict3))              # Выводит как объект
#########################################################
#### map() ######################
### вариант 1 с циклом for
# list1 = ['1', '2', '3']
# list2 = []
# for i in list1:
#     list2.append(int(i))
#
# print(list2)
### Вариант 2 с генератором списка
# list1 = ['1', '2', '3']
# list2 = [int(i) for i in list1]
# print(list2)
### вариант 3 с помощью map()
## map(Что сделать, с кем это сделать) предположительно:
## map берет первый элемент из итерируемого объекта, запускает его
# в указанную функцию (что сделать с...) и, затем, выдает его далее...
# list1 = ['1', '2', '3']
# list2 = map(int, list1)
# print(list2)            # выдает объект
# list3 = list(map(int, list1))
# print(list3)            # выдает список
#################

# def add_one(var: str) -> str:
#     print(var)
#     return str(int(var) + 1)


# list1 = ['1', '2', '3']
# list2 = list(map(add_one, list1))   # map(Что сделать, с кем это сделать) предположительно:
# ## map берет первый элемент из итерируемого объекта - list1, запускает его
# # в указанную функцию add_one - получает обработанный элемент (что сделать с...)
# # и, затем, выдает его далее, а именно помещает его в список (внутри map есть append)  list2...
# print(list2)
##########################################
# def mult(number: int) -> int:
#     if number % 2 == 0:
#         return number * 3
#     else:
#         return number * 5
#
#
# list1 = [i for i in range(10)]
# print(list1)
# list2 = list(map(mult, list1))
# print(list2)
####################################3
# def mult(number: int) -> int:
#     return number ** 2
#
#
# list1 = [i for i in range(10)]
# print(list1)
# list2 = list(map(mult, list1))
# print(list2)
########################################
### filter() ###
### filter(как отфильтровать, и что отфильтровать)
# # filter(Выдает True False включает или не включает, в итерируемый объект)
# def if_chet(var: int) -> bool:
#     return var % 2 == 0      # а если без "== 0", то выдаст нечетные числа
#
#
# list1 = [i for i in range(10)]
# list2 = list(filter(if_chet, list1))
# print(list2)
# #########################################
# def undo_musor(var: int | str) -> bool:
#     return type(var) == str
#
#
# musor = ['linux', 12, 'python', 22, 'micros', 777]
# list_str = list(filter(undo_musor, musor))  # Помещает в итерируемый объект все, что True
# print(list_str)
####################
###lambda() анонимная функция ###
### lambda param1, param2: instruction
### lambda args: expression
# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(3, 5))
##################
# result = lambda a, b: a + b
# print(result(3, 5))
#############################
# def apply_func(elements: list, func) -> None:
#     for a in elements:
#         print(func(a))
#
#
#
# # my_func = lambda x: x * x
# # apply_func([1, 2, 3, 4], my_func)
# #                                           #
#                                             # оба варианта идентичны
# apply_func([1, 2, 3, 4], lambda x: x * x)   #
################################################
# def double(x):
#     return x * x
#
#
# numbers1 = [i + 1 for i in range(6)]
# numbers2 = list(map(double, numbers1))
# print(numbers1)
# print(numbers2)
##### Предыдущий пример только с lambda функцией
# numbers1 = [i + 1 for i in range(6)]
# numbers2 = list(map(lambda x: x * x, numbers1))
# print(numbers1)
# print(numbers2)
####################################################
# my_list = [18, -3, 5, 0, -1, 12]
# new_list = list(filter(lambda num: num > 0, my_list))
# print(new_list)
#################
# def mult(number):
#     if number % 2 == 0:
#         return number * 3
#     else:
#         return number * 5
#
#
# list1 = [i for i in range(10)]
# list2 = list(map(mult, list1))
# print(list1)
# print(list2)
#
# list3 = list(map(lambda num: num * 3 if num % 2 == 0 else num * 5, list1))
# list4 = list(map(lambda num: num * 5 if num % 2 else num * 3, list1))
# print(list3)
# print(list4)
###########################################
def undo_musor(item):
    return type(item) == str


musor = ['linux', 12, 'python', 22, 'micros', 777]

no_musor1 = list(filter(undo_musor, musor))

no_musor2 = list(filter(lambda var: type(var) == str, musor))

print(no_musor1)
print(no_musor2)

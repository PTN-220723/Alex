"""
list      [ object1, object2, object3 ]
tuple     ( object1, object2, object3 )
"""
## list
list0 = []  # Литерал
list0.append(20)
list0.append('micros')
list0.append(3.14)
list0.append([1, 2, 3])
print(list0)

cnt = 1
for i in list0:
    print(f'Студент номер {cnt} - {i}')
    cnt += 1

list1 = ['яблоко', 'банан', 'огурец']
print(list1[0])
print(list1[1])
print(list1[2])

string = '10,20,30,40,50'
list2 = string.split(',')
print(list2)

string = '10 20 30 40 50'
list2 = string.split(' ')
print(list2)

string = '10 20 30 40 50'
list2 = string.split()
print(list2)


string = '10:20:30:40:50'
list2 = string.split(':')
print(list2)

ip_a = '''
192.168.8.1
192.168.8.125
192.168.8.137
192.168.8.180
192.168.8.255
224.0.0.22
224.0.0.251
239.255.102.18
239.255.255.250
255.255.255.255
'''
list_ip = ip_a.split()

for ip in list_ip:
    print(f'ping {ip} -c 1')


nums = input('Введите числа через ", " : ')
list_nums = nums.split(', ')
print(list_nums)
sum_number = 0
for num in list_nums:
    sum_number += int(num)

print(sum_number)


list1 = ['яблоко', 'банан', 'огурец', 20, 40, 'гастраном', 'asd', 'linux']
print(list1[0])
print(list1[2])
print(list1[-1])

'''
            0         1        2      3   4        5         6        7
list1 = ['яблоко', 'банан', 'огурец', 20, 40, 'гастраном', 'asd', 'linux']
           -8        -7        -6     -5   -4     -3         -2      -1
'''
print(list1[-8])
print(list1[0])



list1 = ['яблоко', 'банан', 'огурец', 20, 40, 'гастраном', 'asd', 'linux']
print(list1[1:5])
print(list1[1:5:2])
print(list1[:5])
print(list1[5:])
print(list1[::-1])

list5 = [[1, 2, 3, 4, 5], ['один', 'два', 'три', 'четыре', 'пять']]
print(list5[0])
print(list5[1][-2])

list6 = list5[1]
print(list6[-2])


list1 = [20, 50, 10, 1, 2, 100, 4]
# for i in range(len(list1)):
#     print(list1[i])
for i in list1:
    print(i)


### Методы
list1 = [20, 50, 10, 1, 2, 100, 4]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list1 = [20, 50, 10, 1, 2, 100, 4]
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
print(list1)
print(list2)
print(list3)

'''
list1 = [20, 50, 10, 1, 2, 100, 4]
list1.sort()
sorted(list1)
'''
list1 = [20, 50, 10, 1, 2, 100, 4]
print(max(list1))
print(min(list1))
print(sum(list1))



list1 = [20, 50, 10, 1, 2, 100, 10,4]
cnt = list1.count(10)
print(cnt)
list1.append(50)
print(list1)
list1.insert(0, 44)
print(list1)
list1.insert(2, ['10', 'qwew'])
print(list1)

list1 = [222, 11, 22, 3333]
list2 = ['qwe', 'AD', 'SSS', 1111]
list1.extend(list2)
list1.extend(['a', 'b', 'c'])
print(list1)


list1 = [222, 11, 22, 3333]
list2 = ['qwe', 'AD', 'SSS', 1111]
list3 = list1 + list2
print(list3)

list1 = [222, 11, 22, 3333]
elem = list1.pop(10)
print(list1)
print(f'remove {elem}')

list1 = [222, 11, 22, 3333, 22]
list1.remove(22)
print(list1)


list1 = [222, 11, 22, 3333, 22]
cnt = list1.count(22)
for _ in range(cnt):
    list1.remove(22)

print(list1)

list1 = [222, 11, 22, 3333, 22]
i = list1.index(22)
print(i)


list1 = [222, 11, 22, 3333, 22]
list2 = list1
list1.append(1111111)
print(list1)
print(list2)

list1 = [222, 11, 22, 3333, 22]
list2 = list1
print(id(list1))
print(id(list2))


list1 = [222, 11, 22, 3333, 22]
list2 = list1.copy()
print(id(list1))
print(id(list2))
list1.append(55555555)
print(list1)
print(list2)


print(id(list1))
list1.clear()
print(id(list1))
print(list1)


string = '10,20,30,40,50'
list2 = string.split(',')
print(list2)

string2 = '->'.join(list2)
print(string2)


##### Генераторы списка

# -----------Пример 1

kv = []
for i in range(10):
    kv.append(i ** 2)

print(kv)

## сокращенный вариант ГЕНЕРАТОР СПИСКА (List Comprehension)
kv2 = [i ** 2 for i in range(10)]
print(kv2)


# -----------Пример 2

hello = []
for i in range(16):
    hello.append(f'hello {i}')

print(hello)

## сокращенный вариант ГЕНЕРАТОР СПИСКА (List Comprehension)
hello2 = [f'hello {i}' for i in range(16)]
print(hello2)

## -----------Пример 3
#  Создать 2 списка чисел от 0 до 100 один четные другой - нечетные

sp1 = []
sp2 = []
for i in range(100):
    if i % 2 == 0:
        sp1.append(i)
    elif i % 2 != 0:
        sp2.append(i)

print(sp1)
print(sp2)

## С помощью генератора:
sp1 = [i for i in range(0, 100, 2)]
sp2 = [i for i in range(1, 100, 2)]
print(sp1)
print(sp2)

## -----------Пример 4
trash = ['toy', 1, 2, 'hello', 'monkey', 3]
# Рассортировать этот список на 2 по типу данных

int_list = []
str_list = []
for element in trash:
    if type(element) is int:
        int_list.append(element)
    elif type(element) is str:
        str_list.append(element)

print(int_list)
print(str_list)


## С помощью генератора:
int_list2 = [element for element in trash if type(element) is int]
srt_list2 = [element for element in trash if type(element) is str]
print(int_list2)
print(srt_list2)


### добавить и удалить объект списка
products = ['bread', 'milk', 'banana']
while True:
    user_text = input('Введите команду: ')  #  # add monkey  или  delete monkey
    if len(user_text.split()) == 2:
        # command = user_text.split()[0]
        # value = user_text.split()[1]
        command, value = user_text.split()
        if command == 'add':
            if value in products:
                print(f'Продукт {value} уже есть в списке {products}')
            else:
                products.append(value)
                print(f'Добавили {value} в список {products}')
        elif command == 'delete':
            if value in products:
                products.remove(value)
                print(f'Удалили {value} из списка {products}')
            else:
                print(f'Продукта {value} и так нет в списке {products}')

    elif len(user_text.split()) == 1 and user_text.split()[0] == 'exit':
        break
    elif not user_text:
        print('Не верная команда. Читайте документацию')
    else:
        print('Вы ввели не верное значение. Нужно ввести 2 слова')


###### Кортежи (Tuple)
tuple1 = ('aaa', 'bbb', 'cccc', '1111')
tuple2 = tuple(sorted(tuple1))
print(tuple1)
print(tuple2)
print(tuple1[0])

tuple1 = ('aaa', 'bbb', 'cccc', '1111')
temp = list(tuple1)
temp.append(66666)
tuple1 = tuple(temp)
print(tuple1)

tuple1 = (11111,)
print(type(tuple1))

tuple1 = ()
print(type(tuple1))
#1)
while True:
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')

    try:
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
    finally:
        if not num1 or not num2:
            break
        else:
            print(f'Первое значение: {num1}')
            print(f'Второе значение: {num2}')
            print(f'Результат: {num1 + num2}')

#2)
list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
num1 = []
str1 = []
for i in list1:
    test = 0
    try:
        test += i
    except:
        str1.append(i)
    else:
        num1.append(i)
print(list1)
print(str1)
print(num1)

#3)
list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
num1 = []
str1 = []
for i in list1:
    test = 0
    try:
        test += i
    except:
        str1.append(i)
        print(f'В список чисел добавлен элемент {i} : {str1}')
    else:
        num1.append(i)
        print(f'В список строк добавлен элемент {i} : {num1}')
print(list1)
print(f'Строки {str1}')
print(f'Числа {num1}')

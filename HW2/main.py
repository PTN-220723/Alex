# Александр
# # Урок № 2 Задание № 2
# 1) Составить три формы присвоение следующего вида x, y, z = y, z, x (придумать способ применения )
# а)
x, y, z = 11, 22, 33
print(x, y, z)

temp = x
x = y
y = z
z = temp
print(x, y, z, '\n')

# b)
x, y, z = 11, 22, 33
print(x, y, z)

tmp1 = x
tmp2 = y
tmp3 = z

x = tmp2
y = tmp3
z = tmp1
print(x, y, z, '\n')

# c)
x, y, z = 11, 22, 33
print(x, y, z)

x, y, z = y, z, x
print(x, y, z, '\n')

# # Урок № 2 Задание № 2
# # 2) Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:

num1 = '3.14'
num2 = '4'
num1 = float(num1)
num2 = int(num2)

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} ** {num2} = {num1 ** num2}\n')


# Урок № 2 Задание № 3
#3) Воспользуйтесь различными методами строк

str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '

str1 = str1.strip(' <-').lower()
print(str1)
str2 = str2.strip(' .\n').upper()
print(str2)
str3 = str3.strip(' (-:+').title()
print(str3,'\n')

# Урок № 2 Задание № 4
#4) Обработайте каждую переменную и получите результат как на картинке:

string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'

string1 = string1[::-1]
print(string1)
string2 = string2.split(' ')
print(string2[1] + ' ' + string2[3])
string3 = string3[::2]
print(string3, '\n')

# Урок № 2 Задание № 5
# 5) С помощью метода строк Замените слово show на display и создайте другую переменную

show = 'show ip interface brief'
display = show.replace('show', 'display')
print(display, '\n')

# Урок № 2 Задание № 6
# 6) ** В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу,
# которая определяет номер купе, в котором находится место с заданным номером
# (нумерация мест сквозная, начинается с 1).
# Сам решить не смог. Подсмотрел в телеграмме в Вашем посте...

num = input('Введите номер места, а я отвечу в каком купе оно находится: ')
kupe = (int(num) - 1) // 4 + 1
print(f'Место под номером {num} находится в(во) {kupe} купе.')

# Урок № 2 Задание № 7
#7) Подсчитайте общее количество цифр в числе.
# Например, число 75869 , поэтому на выходе должно быть 5

num = 75869
print(len(str(num)))

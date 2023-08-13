# if/elif/else
# 1) Дано целое число. Если оно является положительным то прибавить к нему 20,
# в противном случае вычесть из него 5. Вывести полученное число
num = int(input('Введите число: '))

# if num >= 0:
#     print(num + 20)
# else:
#     print(num - 5)

print(num + 20) if num >= 0 else print(num - 5)

# 2) Дано два числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2.
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
summ = num1 + num2

# if summ % 5 == 0:
#    print(summ + 1)
# else:
#    print(summ - 2)

print(summ + 1) if summ % 5 == 0 else print(summ - 2)

#3) Ввести 2 числа. Если их произведение отрицательно, умножить его на 8 и вывести на экран,
# в противном случае увеличить его в 1,5 раза и вывести на экран.
nm1 = int(input('Введите первое число: '))
nm2 = int(input('Введите второе число: '))
mult = nm1 * nm2

# if mult < 0:
#     print(mult * 8)
# else:
#     print(mult * 1.5)

print(mult * 8) if mult < 0 else print(mult * 1.5)
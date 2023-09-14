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


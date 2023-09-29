def factorial(num: int) ->int:
    fct = 1
    for i in range(num):
        fct *= i + 1
    return fct


number = int(input('Введите число: '))
f = factorial(number)
print(f)


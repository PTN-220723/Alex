def max_num(num1: int, num2: int, num3: int) -> int:
    if num2 < num1 > num3:
        return num1
    elif num1 < num2 >num3:
        return num2
    elif num1 < num3 > num2:
        return num3

result = max_num(33, 25, 102)
print(result)



def nums_mult(lst: list) -> int:
    """
    Функция принимает список и перемножает члены списка.
    Выдает результат в int формате.
    берет аргумент list1 :param lst:
    возвращает переменную mult в типе int:return:
    """
    mult = 1
    for i in lst:
        mult *= i
    return mult


list1 = [8, 2, 3, -1, 7]
res = nums_mult(list1)
print(res)
print(nums_mult.__doc__)

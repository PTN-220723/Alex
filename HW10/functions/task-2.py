
def sum_of_items(lst: list) -> int:
    """
    function resives the list1, проходит по списку и суммирует значения списка.
    принимает аргумент list1:param list1:
    возвращает  сумму элементов списка int:return: int
    """
    sum_items = 0
    for i in lst:
        sum_items += i

    return sum_items


list1 = [8, 2, 3, 0, 7]
print(sum_of_items(list1))
print(sum_of_items.__doc__)


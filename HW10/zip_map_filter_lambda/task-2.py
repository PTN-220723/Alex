def more_than_75(var: list) -> list:
    #return var > 75
    list_75 = []
    for score in var:
        if score > 75:
            list_75.append(score)

    return list_75


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
list1 = more_than_75(scores)
print(list1)
list2 = list(filter(lambda score: score > 75, scores))
print(list2)
# list3 = list(filter(more_than_75, scores))
# print(list3)
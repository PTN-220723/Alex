def names_title(var: list) -> list:
    title_names = []
    for name in var:
        title_names.append(name.title())
    return title_names


names = ['alfred', 'tabitha', 'william', 'arla']
list_names = names_title(names)
print(list_names)

list_names1 = list(map(lambda name: name.title(), names))
print(list_names1)

list_names2 = list(map(names_title, names))         # с map() что-то не получается...
print(list_names2)
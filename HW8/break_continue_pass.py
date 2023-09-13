# # continue
list1 = [i for i in range(100)]
for i in list1:
    if i % 5 == 0:
        continue
    else:
        print(i)

# # break
while True:
    name = input('Введите имя: ')
    if not name:
        break
    else:
        print(name)

## pass
list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
list3 = []
str1 = ''
cnt = len(list1)
for i in range(len(list1)):
    if i > 0:
        list2.append(' ')
    for j in range(len(list1[i])):
        if list1[i][j] == 'i':
            pass
        else:
            list2.append(list1[i][j])

str1 = str1.join(list2)
list3 = str1.split(' ')

print(list1)
print(list3)

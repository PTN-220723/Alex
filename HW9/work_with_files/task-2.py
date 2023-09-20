file = open('../files/romeo.txt')
words_list, words_set, words_list1 = [], {}, []

for line in file:
    line1 = line.split()
    for word in line1:
        words_list.append(word)
        words_set = set(words_list)
        words_list1 = sorted(words_set)
print(words_list1)

file.close()

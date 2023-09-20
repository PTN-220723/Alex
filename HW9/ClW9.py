# files = open('files/byron.txt', 'r', encoding='UTF-8')
# print(files.closed)
# print(files.read())
# rd = files.read()
# print(rd)
# files.close()
# print(files.closed)
# #####################################
#
# files = open('files/byron.txt', 'r', encoding='UTF-8')
# context = files.read().split()
# print(type(context))
# # for line in context:
# #     if line == 'quickly':
# #         print('Yess!!!')
# if 'quickly' in context:
#     print('Ok')
# print(context)
# print(len(context))
# for line in context:
#     print(line)
# files.close()
##################################
# files = open('files/byron.txt', 'r', encoding='UTF-8')
# context = files.read()  # без split()
# print(type(context))
# print(len(context))
#
# for line in context:
#     print(line)         # вывод познаково
# files.close()
#####################################################
files = open('files/byron.txt', 'r', encoding='UTF-8')
for lines in files:
    #    print(lines)            # вывод построчно str
    print(lines.rstrip())  # вывод построчно с удалением пробелов справа
#    print(lines.split())    # вывод построчно списком
files.close()
######################################################
############# Запись в файл ##############
# file = open('test.txt', mode='w')       # w перезаписывает файл
# file.write('1111111\n')
# file.close()
#
# file = open('test.txt', mode='a')       # a добавляет в файл (если файл не существует, то создает его)
# file.write('2222222\n')
# file.close()
#
# file = open('test.txt', mode='a')
# file.write('3333333\n')
# file.close()
###################
# file = open('test2,txt', 'w', encoding='UTF-8')
# for i in range(100):
#     file.write(f'Проход №{i}. Привет!\n')
# file.close()
########## Копирование файла #################
# file_read = open('files/pushkin.txt', mode='r', encoding='UTF-8')
# file_write = open('pushkin-copy.txt', mode='w', encoding='UTF-8')
#
# context = file_read.read()
# file_write.write(context)
#
# file_write.close()
# file_read.close()

# with open('files/pushkin.txt', mode='r', encoding='UTF-8') as f1:
#     with open('pushkin-copy2.txt', mode='w', encoding='UTF-8') as f2:
#         context = f1.read()
#         f2.write(context)

# with open('files/pushkin.txt', encoding='UTF-8') as f1, open('pushkin-copy3.txt', mode='w', encoding='UTF-8') as f2:
#     context = f1.read()
#     f2.write(context)

#################################
# with open('files/romeo.txt') as file:    # mode='r' при чтении стоит по умолчанию.
#                                         # поэтому указывать 'r' не обязательно. encoding='UTF-8' тоже не обязателен
#                                         # потому что текст на латинице.
#     context = file.read()
#     print(context)
#     print(file.closed)                  # при конструкции with open(...) as f закрывать файл не нужно.
#                                         # Он автоматически закрывается программой.
#
# print(file.closed)
###########################
# try:
#     with open('files/romeo.txt') as file:
#         context = file.read()
#         print(context)
#         print(file.closed)
#         raise OSError
# except:
#     print('ERROR')
#
# print(file.closed)

#################################
# with open('files/nature.jpg', mode='rb') as jpg:
#     context = jpg.read()
#     for i in range(1, 11):
#         new_file = open(f'files/nature_copy{1}.jpg', mode='wb')
#         new_file.write(context)
#         new_file.close()



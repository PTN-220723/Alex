# num1 = 2
# num2 = 0
# try:
#     result = num1 / num2
#     print(result)
# except Exception as e:
#     print(e)
#     print(e.__class__)
#     print(e.__class__.__name__)
#     print('На ноль делить нельзя')
##########################################
# while True:
#     num = input('Введите номер ошибки: ')
#     try:
#         num = int(num)
#         if num == 1
#             print(name)  # NameError
#         elif num == 2:
#             list1 = [1, 2, 3]
#             print(list1[6])  # IndexError
#         elif num == 3:
#             print(10/0)  # ZeroDivisionError1
#     except Exception as e:
#         if e.__class__ is NameError:
#             print('NameError')
#         elif e.__class__ is IndexError:
#             print('IndexError')
#         elif e.__class__ is ZeroDivisionError:
#             print('ZeroDivisionError')

while True:
    num = input('Введите номер ошибки: ')
    try:
        num = int(num)
        if num == 1:
            print(name)  # NameError
        elif num == 2:
            list1 = [1, 2, 3]
            print(list1[6])  # IndexError
        elif num == 3:
            print(10/0)  # ZeroDivisionError1
        elif num == 4:
            raise OSError('ошибка OSError')
    except NameError as e:
        print(e)
        print('NameError new')
    except IndexError:
        print('IndexError new')
    except ZeroDivisionError:
        print('ZeroDivisionError new')
    except Exception as e:
        print(e)
        print('что то пошло не так!!!')
    else:
        print('Ошибок нет')
    finally:
        print('Выполню в любом случае')


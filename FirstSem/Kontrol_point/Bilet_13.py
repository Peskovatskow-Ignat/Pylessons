"""
13 Билет
"""


def sorting_check(list_1):
    if list_1 == []:
        return True
    else:
        if list_1 == sorted(list_1):
            return True
        else:
            return False


list_1 = []
print("Завершить программу - Enter")
data = (input("Введите число которое хотите увидеть в списке по порядку, который вы хотите видеть в списке - "))
if data != "":
    list_1.append(int(data))
    while True:
        data = input("Введите число которое хотите увидеть в списке по порядку, который вы хотите видеть в списке - ")
        if data == "":
            break
        else:
            list_1.append(int(data))


print(list_1)
print(sorted(list_1))


print(sorting_check(list_1))



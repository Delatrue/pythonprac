import random

# Урок 3. Списки и словари
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

lenList = int(input())
list = [random.randint(0, 10) for i in range(lenList)]
print(*list)
findX = int(input())
print(f"-> {list.count(findX)}")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


# lenList = int(input())
# list = [random.randint(0, 10) for i in range(lenList)]
# print(*list)
# list.sort()
# findX = int(input())
# if findX in list:  # Если элемент в спике
#     findXindex = list.index(findX)  # находим его индекс
#     if findXindex > 0 and findXindex < lenList - 1:
#         prevElem = list[findXindex] - list[findXindex - 1]
#         nextElem = (
#             list[findXindex + 1] - list[findXindex]
#         )  # и сравниваем элементы предыдущий и следующий
#         if prevElem < nextElem:  # выводим элемент с меньшей разницей
#             print(list[findXindex - 1])
#         else:
#             print(list[findXindex + 1])
#     else:
#         print(list[findXindex - 1])
# else:  # Если элемент не в списке
#     list.append(findX)
#     list.sort()  # добавляем его в список, снова сортируем (ну и наверное лучше обернуть поиск в функцию, т.к получается дублирование кода)
#     findXindex = list.index(findX)
#     if findXindex > 0 and findXindex < lenList:
#         prevElem = list[findXindex] - list[findXindex - 1]
#         nextElem = list[findXindex + 1] - list[findXindex]
#         if prevElem <= nextElem:
#             print(list[findXindex - 1])
#         else:
#             print(list[findXindex + 1])
#     elif findXindex == 0:
#         print(list[findXindex + 1])
#     elif findXindex == lenList:
#         print(list[findXindex - 1])
# ------------------------------------------------------
# ваш вариант решения сохраню здесь :)
# ------------------------------------------------------
# from random import randint

# n = int(input())
# list_nums = [randint(1, 50) for _ in range(n)]
# print(list_nums)
# b = int(input())
# m = min(list_nums, key=lambda x: abs(x - b))
# print(m)
# #-------------------------------------------------------


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# dictAll = {
#     "AEIOULNSTRАВЕИНОРСТ": 1,
#     "DGДКЛМПУ": 2,
#     "BCMPБГЁЬЯ": 3,
#     "FHVWYЙЫ": 4,
#     "KЖЗХЦЧ": 5,
#     "JXШЭЮ": 8,
#     "QZФЩЪ": 10,
# }
# word = input()
# print(sum([i[1] for i in dictAll.items() for j in word.upper() if j in i[0]]))

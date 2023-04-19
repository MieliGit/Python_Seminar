# №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# from random import randint
# s = input('введите количество элементов в массиве и диапазон от и до через пробел: ').split()

# d = {}

# for el in s:
#     d[el] = 0

# sout = []
# for el in s:
#     if d[el] == 0:
#         sout.append(el)
#         d[el] += 1
#     else:
#         sout.append(f'{el}_{d[el]}')
#         d[el] += 1
# print(*sout)

text = input('Введите строку: ').split()

count = {}

for letter in text:
    if letter not in count:
        print(f'{letter}', end=' ')
    else:
        print(f'{letter}_{count[letter]}', end=" ")

    count[letter] = count.get(letter, 0) + 1

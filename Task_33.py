# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1
import random

n = int(input("Введите колличество оценок: "))

list_1 = []

for i in range(1, n + 1):

    list_1.append(random.randint(1, 5))

print(list_1)
maxx = max(list_1)
minn = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == maxx:
        list_1[i] = minn

print(list_1)



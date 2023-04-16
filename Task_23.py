# №23. Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.


import random

n = int(input("Введите колличество чисел в списке: "))
count = 0

list_1 = [random.randint(-10, 10) for i in range (n)]
print(list_1)

# i = 0
# while i < len(list_1):
#     if list_1[i] > list_1[i-1]:
#         count += 1
#     i += 1
# print(count)

for i in range(len(list_1)):
       if list_1[i] > list_1[i-1]:
        count += 1
        i += 1
    #    else:i += 1

print(count)
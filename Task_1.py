# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной
#  инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math # Для применений формул math

n = int(input("Введите сколько километров машина проезжает за день: ")) 
m = int(input("Введите сколько киллометров нужно проехать: "))

# print((m + n - 1) // speed)
print(math.ceil(m / n))  #Позволяет округлить в большую сторону 

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

def sem_divisors(n):
    div_sum = 1
    for i in range(2, n):
        if n % i == 0:
            div_sum += i

    return div_sum


def find_amicable(k):

    div_sum_dict = {}
    for n in range(1, k + 1):
        s_n = sem_divisors(n)
        if s_n in div_sum_dict and div_sum_dict[s_n] == n and n != s_n:
            print(n, s_n)
        div_sum_dict[n] = s_n



find_amicable(100000)
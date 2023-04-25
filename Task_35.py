# Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes


def check(x):
    for i in range(2, n):

        if n%i == 0:
            return 'No'
    return 'Yes'

n = int(input("Введите число: "))
print(check(n))
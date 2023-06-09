#Задача 26: возвести число А в степень В с помощью рекурсии
# def rekursAB(a, b):
#     if b == 0:
#         return 1
#     return a * rekursAB(a, b-1)

# a = int(input("Введите число "))
# b = int(input("Введите степень числа "))
# print(rekursAB(a, b))

# Задача 28: найти сумму 2-х неотрицательных чисел используя рекурсию

def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(recSum(a, b))
#Задача 16: Сколькораз встречается число "а" в заданом списке

n = int(input("Введите количество чисел в списке: "))
lst = []
for i in range(n):
    num = int(input("Введите число: "))
    lst.append(num)
    print(lst)

a = int(input("Введите нужное вам число: "))
count = 0
for i in lst:
    if a == i:
        count += 1
        print(count)
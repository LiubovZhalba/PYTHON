#Задача 1 семинара 6: Вывести элементы первого массива, которых нет во втором
# def num_in(list_1, list_2):
#     result = []
#     for num in list_1:
#         if num not in list_2:
#             result.append(num)
#     return result

# list_1 = [5,1 ,3, 4, 5 ,12]
# list_2 = [4, 3, 6, 8,23, 67]

# Задача 47 из Семинара 7
# print(num_in(list_1, list_2))
# Задача 41 на подсчет количества элементов
# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(transormed_values == values)

#Святослав Миловидов
#list_old = [2, 4, 7, 12]

# Вариант 1
#          что сделать              где взять          *при каком условии
#list_new = [(0 if num < 5 else num) for num in list_old if num > 5]

# Вариант 2
# for num in list_old:
#     list_new.append(0 if num < 5 else num)

# Вариант 3
# list_new = list(map(lambda num: 0 if num < 5 else num, list_old))

#print(list_new)

#Задача про планеты Вариант 1:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#print(*find_farthest_orbit(orbits))
res = 0
maxim = 0
for i in range(len(orbits)):
    if orbits[i][0] != orbits[i][1]:
        res = orbits[i][0] * orbits[i][1]
        if res > maxim:
            maxim = res
            max_i = (orbits[i][0], orbits[i][1])
    print(maxim)
print (max_i)

#Задача про планеты Вариант 2 (упрощенный)
def find_farthest_orbit(orbits):
    s = [(dbl[0] * dbl[1] if dbl[0] != dbl[1] else 0) for dbl in orbits]
    # print(s)
    # print(max(s))
    # print(s.index(max(s)))
    return orbits[s.index(max(s))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit(orbits)
print(*find_farthest_orbit(orbits))

 


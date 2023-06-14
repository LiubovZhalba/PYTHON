# Задача: определить есть ли ритм в песне Вини-Пуха 
#"пара-ра-рам рам-пам-папам па-ра-па-дам" - есть; "па-па ра" - нет

# def poems(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum += 1
#         list_1.append(sum)
#     return len(list_1) == list_1.count(list_1[0])

# text = input("Введите фразу: ")
# if poems(text):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)








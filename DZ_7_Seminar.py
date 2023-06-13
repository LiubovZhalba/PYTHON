# Задача: определить есть ли ритм в песне Вини-Пуха 
#"пара-ра-рам рам-пам-папам па-ра-па-дам" - есть; "па-па ра" - нет

def poems(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum += 1
        list_1.append(sum)
    return len(list_1) == list_1.count(list_1[0])

text = input("Введите фразу: ")
if poems(text):
    print('Парам пам-пам')
else:
    print('Пам парам')











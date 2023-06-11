def ritm(str):
    str = str_1
    list_1 = []
    for word in str:
        sum_word = 0
        for i in word:
            if i in "аеёиоуыэюя":
                sum_word += 1
            list_1.append(sum_word)
        return len(list_1) == list_1.count(list_1[0])
    
str_1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"
if ritm(str_1):
    print("Парам-пам-пам")
else:
    print("Пам парам")



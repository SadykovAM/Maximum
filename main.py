
# #Подсчет одинаковых символов (При вводе 3х символов 9 итерации. Оченьтрудоемко 2**2)
# s='aab'
# for sym in s:
#     count = 0
#     for sub_sim in s:
#         if sub_sim == sym:
#             count += 1
#     print(sym, count)




##Оптимизация используя SET(выбирает уникальные символы, При вводе 3х символов 6 итерации. N*количество уникальных значений)
##При условии всех уникальных символов смысла нет.
s='aaba'
for sym in set(s):
    count = 0
    for sub_sim in s:
        if sub_sim == sym:
            count += 1
    print(sym, count)



# #Перебор в один цикл всего три итерации
# s='aaba'
# syms_counter = {}
# for sym in s:
#     syms_counter[sym] = syms_counter.get(sym, 0) + 1
# print(syms_counter)
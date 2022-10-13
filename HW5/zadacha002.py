# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

random_lst = [
    1, 382, 1, 8, 9,
    83, 91, 2, 3, 2,
    4, 5, 3, 4, 2, 1
    ]

origin_lst = []

[origin_lst.append(num) for num in random_lst if random_lst.count(num) == 1]
print(origin_lst)


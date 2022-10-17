# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.

from itertools import count


numbr_lst = [1, 2, 3, 5, 1, 5, 3, 10] 
povtory = []
unic_el = []

unic_el = list(filter(lambda x :  numbr_lst.count(x)== 1, numbr_lst))

povtory = list(set(filter(lambda x :  numbr_lst.count(x) > 1 , numbr_lst)))


print(unic_el)
print(povtory)
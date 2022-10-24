import random

some_lst = []

for i in range(0, 15):
    some_lst.append(random.randint(1,10))
print(some_lst)

original_lst = []

[ original_lst.append(i) for i in some_lst if some_lst.count(i) < 2 ]

print(original_lst) 
some_list = [
            2, 3, 5,
            7, 9, 3
            ]

sum_of_element = 0

for i in range(0, len(some_list)):
    if i % 2 != 0 :
        sum_of_element += some_list[i]

print(sum_of_element)


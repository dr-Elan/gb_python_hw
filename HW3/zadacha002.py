some_list = [
    2, 3, 4,
    5, 6, 7
]

sum_of_multiply = 1
for i in range(0, int(len(some_list)/2)):
    multiply = some_list[i]*some_list[-i]
    sum_of_multiply *= multiply
    i += 1 

print(sum_of_multiply)



nmbr = int(input('Введеите некоторое число N: '))
list_of_sqrs = [1]
for i in range(1, nmbr):
    list_of_sqrs.append((i+1)*list_of_sqrs[i-1])
print(list_of_sqrs)
nmbr = input("Введите некоторое число: ")
sum_of_digits = 0
for i in range(0, len(nmbr)):
    if nmbr[i] != ',':
        sum_of_digits += int(nmbr[i])
print(sum_of_digits)

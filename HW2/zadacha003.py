nmbr = int(input('Ввеедите число N: '))
list_of_succesion = []
for i in range(1, nmbr+1):
    list_of_succesion.append((1 + 1/i)**(i))
print("Последовательность: ", list_of_succesion)
print("Сумма элементов последовательности: ", sum(list_of_succesion))

# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

some_nm = int(input('Введите натуральное число: N = '))
output = some_nm
factor = []
sqr_smn = int(some_nm ** 0.5) + 2
for j in range(2, sqr_smn):
    while some_nm % j == 0:
        factor.append(j)
        some_nm /= j
if some_nm != 1:
    factor.append(int(some_nm))
print(f'Список простых множителей числа {output}: {factor}')


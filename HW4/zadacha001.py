# Вычислить число c заданной точностью d

d = input('Введите необходимую точность для числа d: ')

irrational = float(input('Ввведите число, которое необходимо округлить: '))

tochnost = len(d.split('.')[1]) 
irr_round = round(irrational, tochnost )
print(f"округлённое значение числа равно: {irr_round}")
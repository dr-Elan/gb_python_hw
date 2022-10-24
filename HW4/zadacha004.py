import random
k = int(input('Введите степень полинома: '))
lst_of_coeef = []

lst_of_coeef = [ random.randint(0, 100)  for i in range(0, k) ]
print(lst_of_coeef)
terms = []
for ratio in lst_of_coeef:
    if k == 0:
        ratio = ratio
    elif ratio == 1:
        ratio = ''
    
    if k == 1:
        power = 'x'
    elif k == 0:
        power= ''
    else:
        power = f'x^{k}'
    k -= 1


    terms.append(f'{ratio}{power}')

polynom = ' + '.join(terms) + ' = 0'
print(polynom)
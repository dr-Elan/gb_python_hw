# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

import re
some_string ="1+20-2*2/3+1/2*3-3"

digit_lst = re.split('\-|\+', some_string)  # ['1', '20', '2*2/3', '1/2*3', '3'] --- так будет выглядить лист для данного пример

lst_of_= [] # здесь будут храниться знаки, которые будут выполняться вторым действием
for c in some_string:
    try:
        digitn = int(c)
    except:
        if c == '+':
            lst_of_.append('+')
        elif c == '-':
            lst_of_.append('-')
multi_dived = [] # этот массив заполним числами, которые необходимо будет складывать или вычитать
for item in digit_lst:
    try:
        multi_dived.append(int(item)) # очевинод, если элемент нельзя сделать int,то он будет содержать элемент умножнеия или деления
    except:
        mlt_dv = float() # в это переменную мы запишем результат перемножнеия и деления
        if ('*' in item) or ('/' in item): # это условие может быть и лишнее, но всё же я её решил не убирать 
            mlt_dv = int(item[0])
            for i in range(1, len(item)):
                if item[i] == '*':
                    mlt_dv = mlt_dv * int(item[i+1])
                elif item[i] == '/':
                    mlt_dv = mlt_dv / int(item[i+1])
            multi_dived.append(mlt_dv)
total = multi_dived[0]
for item in range(0, len(lst_of_)):
    if (lst_of_[item] == '-'):
        total -= multi_dived[item+1]
    elif (lst_of_[item] == '+'):
        total += multi_dived[item+1]
print(total)

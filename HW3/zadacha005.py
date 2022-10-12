number = int(input('Введеите номер: '))

sm_lst = [0,1]

for i in range(1, number+1):
    sm_lst.append(sm_lst[i-1]+ sm_lst[i])
sm_lst.insert(0, 1)
sm_lst.insert(0, -1)
for j in range(0, number ):
    sm_lst.insert(0, sm_lst[1] - sm_lst[0])
print(sm_lst)
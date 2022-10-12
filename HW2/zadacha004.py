import random
nmbr = int(input("Ввеедите число N: "))
sm_list = []
for i in range(0, nmbr):
    sm_list.append(random.randrange(-nmbr, nmbr))
print(sm_list)

file1 = open("file.txt", "r")
list_of_file = []
while True:
    line = file1.readline()
    if not line:
        break
    list_of_file.append(line.strip())
file1.close
multiplication = 1
for i in range(0, nmbr):
    if i in list_of_file:
        multiplication *= sm_list[i]

print(multiplication)

random.shuffle(sm_list)
number = int(input("Введите некоторое число: "))
bool_number = str()

while number > 0 :
    bool_number = str(number%2) + bool_number
    number = number // 2
print(bool_number)

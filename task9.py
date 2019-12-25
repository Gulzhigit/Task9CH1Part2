num_ = int(input("Введите число: "))
factorial = 1
for i in range(1, num_+1):
    factorial *= i
print("Факториал числа", num_, "равен", factorial)
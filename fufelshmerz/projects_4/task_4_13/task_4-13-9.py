array = [5, 3, 8, 4, 2, 7, 1]
s = 0
for x in array:
    if x % 2 != 0:
        s = s + x

print("Сумма всех нечетных элементов массива:", s)
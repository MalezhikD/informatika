array = [5, 3, 8, 4, 2, 7, 1]
s = 0
for i in range(len(array)):
    if i % 2 != 0:
        s = s + array[i]

print("Сумма элементов с нечетными индексами:", s)
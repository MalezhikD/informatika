array = [5, 3, 8, 4, 2, 7, 1]
s = 0
count = 0
for i in range(len(array)):
    if i % 2 == 0:
        s = s + array[i]
        count = count + 1
average = s / count

print("Среднее арифметическое чётных:", average)
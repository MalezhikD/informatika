n = int(input("Число N: "))
s = 0
i = 1
while i <= n:
    s = s + i * i
    i = i + 1

print("Квадраты первых N чисел:", s)
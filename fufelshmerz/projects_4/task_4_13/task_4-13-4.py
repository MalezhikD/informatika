n = int(input("Введите число N: "))
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1

print("Сумма первых N натуральных чисел:", s)
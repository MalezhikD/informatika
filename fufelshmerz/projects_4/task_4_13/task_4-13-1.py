a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
d = float(input("Четвертое число: "))
min_value = a

if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d

print("Минимальное число:", min_value)
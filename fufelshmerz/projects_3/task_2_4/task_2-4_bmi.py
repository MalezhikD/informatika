weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)

print(f"--Отсчет о состоянии здоровья-- \nРост:\t {height}\nВес:\t{weight}\nИндекс массы тела:{bmi:.2f}")
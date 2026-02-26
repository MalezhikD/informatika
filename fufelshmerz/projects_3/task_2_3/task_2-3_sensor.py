name = input("Введите имя оператора: ")
sensor = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as sensor: 
    sensor.write(f"Оператор: {name}\tЗначение: {sensor}")
    
print("Данные успешно сохранены в sensor_log.txt")
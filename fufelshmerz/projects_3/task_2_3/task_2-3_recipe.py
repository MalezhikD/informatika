name = input("Введите название питательной среды: ")
сoncentration = input("Введите концентрацию агара (%): ")
temp = input("Введите температуру стерилизации (°C): ")

with open('recipe.txt', 'w', encoding='utf-8') as file:
    
    file.write(f"{name}\n")
    file.write("=" * len(name) + "\n\n")  
    
    file.write("Параметры среды:\n")
    file.write(f"Концентрация агара: {сoncentration}%\n")
    file.write(f"Температура стерилизации: {temp}°C\n")

print("\nФайл 'recipe.txt' успешно сформирован!")
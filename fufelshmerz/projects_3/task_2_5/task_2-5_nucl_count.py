print("=== Анализ последовательности ДНК ===")

dna = input("Введите последовательность ДНК: ").upper()
count_A = dna.count("A")
count_T = dna.count("T")
count_C = dna.count("C")
count_G = dna.count("G")

print("Подсчет нуклеотидов:")
print(f"Количетво аденина: {count_A}")
print(f"Количетво тимина: {count_T}")
print(f"Количетво цитозина: {count_C}")
print(f"Количетво гуанина: {count_G}")

count = count_G + count_A + count_C + count_T
print(f"\nОбщая длина: {count} нуклеотидов")

calculating_percentages1 = (count_A/count) * 100
calculating_percentages2 = (count_C/count) * 100
calculating_percentages3 = (count_G/count) * 100
calculating_percentages4 = (count_T/count) * 100

print(f"\nПроцентное содержание аденина: {calculating_percentages1}%")
print(f"\nПроцентное содержание тимина: {calculating_percentages4}%")
print(f"\nПроцентное содержание цитозина: {calculating_percentages2}%")
print(f"\nПроцентное содержание гуанина: {calculating_percentages3}%")
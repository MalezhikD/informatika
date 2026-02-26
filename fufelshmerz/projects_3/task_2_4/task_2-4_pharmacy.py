manufactured_capsules = int(input("Введите общее количество произведенных капсул(шт): "))
quantity_per_package = int(input("Введите количество капсул в одной упаковке(шт): "))

full = (manufactured_capsules // quantity_per_package)
remain = (manufactured_capsules % quantity_per_package)

print(f"--- Отчет фасовочного цеха ---\nПолных упаковок:\t{full}\nОстаток капсул:\t        {remain}\n==============================")
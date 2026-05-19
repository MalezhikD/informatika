import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_medians.txt'

try:
    df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')
except Exception as e:
    print(f"Ошибка чтения файла: {e}")
    exit()

numeric_cols = [col for col in df.select_dtypes(include='number').columns if col != 'boar_id']

if not numeric_cols:
    print(" В файле не найдено числовых столбцов для расчёта.")
    exit()

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("МЕДИАННЫЕ ЗНАЧЕНИЯ ПО ПАРАМЕТРАМ\n\n")
    for col in numeric_cols:
        median_val = df[col].median()
        f.write(f"{col}: {median_val:.2f}\n")
    f.write(f"\n Всего параметров: {len(numeric_cols)}\n")

print("\n Содержимое выходного файла:")
print("-" * 40)
with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
    print(f.read())

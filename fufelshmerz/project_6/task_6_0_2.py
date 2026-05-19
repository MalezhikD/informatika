import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_averages.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

numeric_cols = df.select_dtypes(include='number').columns

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("СРЕДНИЕ ЗНАЧЕНИЯ ПО ПАРАМЕТРАМ\n\n")

    for col in numeric_cols:
        mean_val = df[col].mean()
        f.write(f"{col}: {mean_val:.2f}\n")

    f.write(f"\n Всего записей: {len(df)}\n")
    f.write(f" Обработано столбцов: {len(numeric_cols)}\n")

print("-" * 40)
with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
    print(f.read())

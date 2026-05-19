import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_modes.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("МОДАЛЬНЫЕ ЗНАЧЕНИЯ ПО ВСЕМ СТОЛБЦАМ\n\n")
    for col in df.columns:
        mode_val = df[col].mode().iloc[0]

        if isinstance(mode_val, float):
            f.write(f"{col}: {mode_val:.1f}\n")
        else:
            f.write(f"{col}: {mode_val}\n")

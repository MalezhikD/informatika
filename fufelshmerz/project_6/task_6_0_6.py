import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_iqr_length.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("Межквартильный размах (IQR) для длины тела \n\n")

    for gender in ['Male', 'Female']:
        subset = df[df['gender'] == gender]['length_cm']

        q1 = subset.quantile(0.25)
        q3 = subset.quantile(0.75)
        iqr = q3 - q1

        f.write(f"{gender}:\n")
        f.write(f"  Q1 (25%): {q1:.1f} cm\n")
        f.write(f"  Q3 (75%): {q3:.1f} cm\n")
        f.write(f"  IQR: {iqr:.1f} cm\n")
        f.write(f"   N={len(subset)} записей\n\n")

with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
    print("\n" + f.read())

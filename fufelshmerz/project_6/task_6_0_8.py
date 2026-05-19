import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_cv_tusk.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("Коэффициент вариации (CV) для длины клыков \n\n")

    for gender in ['Male', 'Female']:
        tusks = df[df['gender'] == gender]['tusk_length_cm'].dropna()

        mean = tusks.mean()
        std = tusks.std()
        cv = (std / mean * 100) if mean != 0 else 0.0

        f.write(f"{gender}:\n")
        f.write(f"  Mean: {mean:.2f} cm\n")
        f.write(f"  Std Dev: {std:.2f} cm\n")
        f.write(f"  CV: {cv:.2f} %\n")
        f.write(f"   N={len(tusks)} записей\n\n")

with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
    print("\n" + f.read())

import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_stats.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

numeric_cols = [col for col in df.select_dtypes(include='number').columns if col != 'boar_id']

def get_unit(col):
    if '_kg' in col: return ' kg'
    if '_cm' in col: return ' cm'
    if '_years' in col: return ' years'
    if '_ha' in col: return ' ha'
    if '_score' in col: return ' pts'
    return ''

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("ДИСПЕРСИЯ, СТАНДАРТНОЕ ОТКЛОНЕНИЕ, КОЭФФИЦИЕНТ ВАРИАЦИИ \n\n")

    for col in numeric_cols:
        mean = df[col].mean()
        variance = df[col].var()
        std = df[col].std()
        cv = (std / mean * 100) if mean != 0 else 0.0

        header = col.replace('_', ' ').title()
        unit = get_unit(col)

        f.write(f"{header}:\n")
        f.write(f"  Variance: {variance:.2f}{unit}²\n")
        f.write(f"  Std Dev: {std:.2f}{unit}\n")
        f.write(f"  CV: {cv:.2f} %\n")
        f.write("\n")

with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
    print("\n" + f.read())

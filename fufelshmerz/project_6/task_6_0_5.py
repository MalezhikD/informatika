import pandas as pd

INPUT_FILE = '/home/chuvak01/wild_boars_2.csv'
OUTPUT_FILE = '/home/chuvak01/wild_boars_percentiles.txt'

df = pd.read_csv(INPUT_FILE, sep=';', decimal=',', encoding='utf-8-sig')

numeric_cols = [col for col in df.select_dtypes(include='number').columns if col != 'boar_id']

percentiles = [
    (0.25, "Percentile 25 (Q1)"),
    (0.50, "Median 50 (Q2)"),
    (0.75, "Percentile 75 (Q3)"),
    (0.90, "Percentile 90"),
    (0.95, "Percentile 95"),
    (1.00, "Max")
]

def get_unit(col_name):
    if '_kg' in col_name: return ' kg'
    if '_cm' in col_name: return ' cm'
    if '_years' in col_name: return ' years'
    if '_ha' in col_name: return ' ha'
    if '_score' in col_name: return ' pts'
    return ''

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for col in numeric_cols:
        header = col.replace('_', ' ').title()
        f.write(f"{header}:\n")

        for q, label in percentiles:
            val = df[col].quantile(q)
            unit = get_unit(col)
            f.write(f"{label}:\t{val:.1f}{unit}\n")

        f.write("\n")

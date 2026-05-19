import pandas as pd

FILE_NAME = '/home/chuvak01/wild_boars_2.csv'
TUSK_COL = 'tusk_length_cm'
WEIGHT_COL = 'weight_kg'
GENDER_COL = 'gender'

try:
    df = pd.read_csv(FILE_NAME, sep=';', decimal=',', encoding='utf-8-sig', on_bad_lines='warn')
except Exception as e:
    print(f" Ошибка загрузки: {e}")
    exit()

print(f"\n Длина клыков ")

tusk_min = df[TUSK_COL].min()
tusk_max = df[TUSK_COL].max()
print(f"\n Самые короткие клыки: {tusk_min:.2f} см")
print(f" Самые длинные клыки:  {tusk_max:.2f} см\n")

avg_weight_all = df[WEIGHT_COL].mean()
print(f" Средняя масса всех кабанчиков: {avg_weight_all:.2f} кг\n")

avg_by_gender = df.groupby(GENDER_COL)[WEIGHT_COL].mean()
MALE_KEY = 'Male'

if MALE_KEY in avg_by_gender.index:
    print(f" Средняя масса самцов: {avg_by_gender[MALE_KEY]:.2f} кг")
else:
    print(f" Ключ '{MALE_KEY}' не найден. Доступные значения: {df[GENDER_COL].unique()}")

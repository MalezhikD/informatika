donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови пациента(реципиента) (I, II, III, IV): ").strip().upper()

control = ["I", "II", "III", "IV"]

if donor not in control and recipient not in control:
    print("Группы крови пациента и донора введены некорректно. Попробуйте снова.")
elif donor not in control:
    print("Группа крови донора введена некорректно. Попробуйте снова.")
elif recipient not in control:
    print("Группа крови пациента введена некорректно. Попробуйте снова.")

elif donor == recipient or donor == "I":
    print("Группы крови сходятся (или у донора I группа крови). Переливание возможно!")
else:
    print("Группы крови донора и пациента не совместимы. Переливание невозможно!")





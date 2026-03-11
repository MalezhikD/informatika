name = input('Введите ФИО исследователя: ')
date = input('Введите дату: ')
expname = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')

with open ('C:\\Users\\vinde\\OneDrive\\Рабочий стол\\journal.txt', 'w', encoding="utf-8") as journal:
    journal.write("+----------------------------------------------+\n")
    journal.write("|        Электронный лабораторный журнал       |\n")
    journal.write("+----------------------------------------------+\n")
    journal.write(f"| ФИО исследователя : {name}\n")
    journal.write(f"| Дата : {date}\n")
    journal.write(f"| Эксперимент : {expname}\n")
    journal.write("+----------------------------------------------+\n")
    journal.write(f"| Вывод: {conclusion}\n")
    journal.write("+----------------------------------------------+\n")


print("Файл 'journal.txt' создан!")

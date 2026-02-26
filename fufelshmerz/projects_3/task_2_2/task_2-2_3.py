import random

words_list = ["Исправен" , "Неисправен"]
random_word = random.choice(words_list)

device_name = "Микроскоп"
inventory_number = 5437856158
condition = random_word 
quantity = 17

print(f"Название прибора:\t{device_name}\nИнвентарный номер:\t{inventory_number}\nСостояние:\t        {condition}\nКоличество:\t        {quantity}")
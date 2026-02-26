name = "Олег"
group = "4731204/50003"
score = 180
print(f"Студен {name} из группы {group} получил {score} баллов")

f = open("result.txt", "w", encoding="utf-8")
print("Результаты работы", file=f)
f.close()
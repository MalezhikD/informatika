reagent = input()
quantity = input()

f = open("inventory.txt", "w", encoding="utf-8")
print(f"Реактив {reagent} поступил на склад в количестве {quantity} шт.", file=f)
f.close()
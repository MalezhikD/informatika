#!/bin/bash

echo "=== СОЗДАНИЕ ФАЙЛОВ ==="

for ((i=1; i<=10; i++)); do
    filename="test${i}.txt"
    touch "$filename"
    echo "Создан файл: $filename"
done

echo ""
echo "Список созданных файлов:"
ls -la test*.txt 2>/dev/null || echo "Файлы не найдены"

echo ""
echo "=== УДАЛЕНИЕ ФАЙЛОВ В ОБРАТНОМ ПОРЯДКЕ ==="

counter=10
while [ $counter -ge 1 ]; do
    filename="test${counter}.txt"

    if [ -f "$filename" ]; then
        rm "$filename"
        echo "Удален файл: $filename"
    else
        echo "Файл не найден: $filename"
    fi
    ((counter--))
done

echo ""
echo "Проверка оставшихся файлов:"
ls -la test*.txt 2>/dev/null || echo "Все файлы удалены. Файлов test*.txt не найдено."

echo ""
echo "Скрипт завершен."

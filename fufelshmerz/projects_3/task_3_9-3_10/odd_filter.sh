#!/bin/bash

echo "Нечетные числа от 1 до 20 (до встречи числа 15):"

for ((i=1; i<=20; i++)); do

    if [ $i -eq 15 ]; then
        echo "Достигнуто число 15. Остановка."
        break
    fi

    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi

    echo $i
done

echo "Скрипт завершен."

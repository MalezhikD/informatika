#!/bin/bash

echo "Сумма всех оценок:"
SUM=$(awk '{sum += $2} END {print sum}' students.txt)
echo "   Сумма = $SUM"

echo "Средняя оценка:"
AVG=$(awk '{sum += $2; count++} END {printf "%.2f", sum/count}' students.txt)
echo "   Средняя = $AVG"

echo "Максимальная оценка:"
MAX=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "   Максимальная = $MAX"
#!/bin/bash

echo "Студенты с оценкой выше 80:"
echo "──────────────"
awk '$2 > 80 {print $0}' students.txt
echo "──────────────"
echo ""

echo "Студенты с оценкой ниже 70:"
echo "──────────────"
awk '$2 < 70 {print $0}' students.txt
echo "──────────────"
echo ""

echo "Первая строка файла"
echo "──────────────"
head -n 1 students.txt
echo "──────────────"

#!/bin/bash

echo "Имена студентов:"
echo "─────────────"
awk '{print $1}' students.txt
echo "─────────────"
echo ""

echo "Оценки студентов:"
echo "────────────"
awk '{print $2}' students.txt
echo "────────────"
echo ""

echo "Номер строки и имя:"
echo "────────────"
awk '{print "Строка " NR ": " $1}' students.txt
echo "────────────"
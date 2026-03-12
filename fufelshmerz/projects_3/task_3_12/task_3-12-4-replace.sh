#!/bin/bash

echo "Замена пробелов на табуляцию в файле sequences.txt"

echo "Исходное содержимое файла:"
echo "-------------------------"
cat sequences.txt
echo "-------------------------"

sed -i 's/ /\t/g' sequences.txt

echo "Новое содержимое файла:"
echo "-------------------------"
cat sequences.txt
echo "-------------------------"
echo "Завершено!"

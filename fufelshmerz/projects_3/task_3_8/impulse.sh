#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Ошибка: Неверное количество аргументов"
    echo "Использование: $0 <имя_гена> <уровень_экспрессии>"
    exit 1
fi

gene_name="$1"
expression_level="$2"

if ! [[ "$expression_level" =~ ^-?[0-9]+$ ]]; then
    echo "Ошибка: Уровень экспрессии должен быть целым числом"
    exit 1
fi

echo "Экспрессия гена $gene_name составляет $expression_level единиц"

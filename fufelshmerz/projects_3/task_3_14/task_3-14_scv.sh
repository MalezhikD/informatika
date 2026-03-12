#!/bin/bash

echo " Названия товаров "
cut -d',' -f2 data.csv

echo -e "\n Товары дороже 20 "
awk -F',' '$3 > 20' data.csv

echo -e "\n Общая стоимость "
awk -F',' '{sum += $3} END {print sum}' data.csv

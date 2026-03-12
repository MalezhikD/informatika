#!/bin/bash

echo "Замена пути к базе данных в файле settings.php"

sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php

echo "Замена выполнена!"

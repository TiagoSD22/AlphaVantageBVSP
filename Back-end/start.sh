#!/bin/bash
while ! nc -z database 5432; 
do 
    echo 'Banco de dados ainda não está pronto, esperando container database..';
    sleep 2; 
done;
echo 'Container database pronto para receber conexões, iniciando aplicação';

python3.7 application.py
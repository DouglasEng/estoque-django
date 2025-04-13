#!/usr/bin/env bash

# Aplica migrações do banco de dados (SQLite no seu caso)
python manage.py migrate

# Coleta arquivos estáticos (CSS, JS, imagens...)
python manage.py collectstatic --noinput

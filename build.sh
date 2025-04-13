#!/usr/bin/env bash
# build.sh

# Instala as dependências
pip install -r requirements.txt

# Aplica as migrações
python manage.py migrate

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

#!/usr/bin/env bash

echo "🔧 Instalando dependências..."
pip install -r requirements.txt

echo "🎯 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

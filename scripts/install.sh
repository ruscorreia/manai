#!/bin/bash

set -e

echo "🚀 Instalando Manai..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale antes de continuar."
    exit 1
fi

# Criar ambiente virtual
VENV_DIR="/tmp/manai_install"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# Baixar repositório
cd "$VENV_DIR"
git clone https://github.com/ruscorreia/manai.git 
cd manai

# Instalar dependências
pip install --no-cache-dir -r requirements.txt

# Instalar pacote
pip install .

# Limpar
deactivate
rm -rf "$VENV_DIR"

echo "✅ Manai instalado com sucesso!"
echo ""

echo "📌 Adicione-as permanentemente ao ~/.bashrc ou ~/.zshrc"
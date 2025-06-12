#!/bin/bash

# Script de instalação para o Manai v2.0
# Integração com Azure Function

SCRIPT_NAME="manai"
INSTALL_DIR="/usr/local/bin"
SCRIPT_FILE="manai_updated.py"

echo "A instalar o comando $SCRIPT_NAME v2.0..."

# Verificar se o ficheiro existe
if [ ! -f "./$SCRIPT_FILE" ]; then
    echo "Erro: Ficheiro $SCRIPT_FILE não encontrado!"
    echo "Certifique-se de que está no directório correcto."
    exit 1
fi

# Verificar se o Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "Erro: Python 3 não está instalado!"
    echo "Instale o Python 3 antes de continuar."
    exit 1
fi

# Verificar se a biblioteca requests está instalada
if ! python3 -c "import requests" &> /dev/null; then
    echo "A instalar a biblioteca requests..."
    pip3 install requests
    if [ $? -ne 0 ]; then
        echo "Erro: Falha ao instalar a biblioteca requests!"
        echo "Execute manualmente: pip3 install requests"
        exit 1
    fi
fi

# Copiar o script para o directório de instalação
sudo cp "./$SCRIPT_FILE" "$INSTALL_DIR/$SCRIPT_NAME"

# Tornar executável
sudo chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

# Verificar se a instalação foi bem-sucedida
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    echo "Instalação concluída com sucesso!"
    echo ""
    echo "O comando '$SCRIPT_NAME' está agora disponível."
    echo ""
    echo "PRÓXIMOS PASSOS:"
    echo "1. Teste o comando:"
    echo "   $SCRIPT_NAME 'como listar ficheiros?'"
    echo ""
    echo "Para mais informações, execute: $SCRIPT_NAME --config"
else
    echo "Erro: Falha na instalação!"
    exit 1
fi


#!/bin/bash

# Script de desinstalação para o Manai v2.0

SCRIPT_NAME="manai"
INSTALL_DIR="/usr/local/bin"

echo "A desinstalar o comando $SCRIPT_NAME..."

# Verificar se o comando está instalado
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    # Remover o comando
    sudo rm "$INSTALL_DIR/$SCRIPT_NAME"
    
    if [ $? -eq 0 ]; then
        echo "Comando $SCRIPT_NAME removido com sucesso!"
        
        # Remover ficheiro de sessão se existir
        SESSION_FILE="$HOME/.manai_session"
        if [ -f "$SESSION_FILE" ]; then
            rm "$SESSION_FILE"
            echo "Ficheiro de sessão removido."
        fi
        
        echo ""
        echo "NOTA: As variáveis de ambiente não foram removidas."
        echo "Se desejar, pode remover manualmente:"
        echo "- MANAI_AZURE_FUNCTION_URL"
        echo "- MANAI_FUNCTION_KEY"
        
    else
        echo "Erro: Falha ao remover o comando!"
        exit 1
    fi
else
    echo "O comando $SCRIPT_NAME não está instalado."
fi


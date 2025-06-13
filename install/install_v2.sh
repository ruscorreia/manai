#!/bin/bash

# Script de instalação para o Manai v2.0
# Integração com Azure Function

SCRIPT_NAME="manai"
INSTALL_DIR="$HOME/.local/bin"
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
    pip3 install --user requests
    if [ $? -ne 0 ]; then
        echo "Erro: Falha ao instalar a biblioteca requests!"
        echo "Execute manualmente: pip3 install --user requests"
        exit 1
    fi
fi

# Criar o diretório de instalação se não existir
mkdir -p "$INSTALL_DIR"

# Copiar o script para o diretório de instalação
cp "./$SCRIPT_FILE" "$INSTALL_DIR/$SCRIPT_NAME"

# Tornar executável
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

# Função para adicionar ao PATH no bashrc ou zshrc
add_path_to_shellrc() {
    local shell_rc="$1"
    local export_line="export PATH=\"$INSTALL_DIR:\$PATH\""
    if [ -f "$shell_rc" ]; then
        if grep -Fxq "$export_line" "$shell_rc"; then
            echo "O diretório $INSTALL_DIR já está no PATH em $shell_rc"
        else
            echo "" >> "$shell_rc"
            echo "# Adicionado pelo instalador do Manai v2.0" >> "$shell_rc"
            echo "$export_line" >> "$shell_rc"
            echo "Adicionado $INSTALL_DIR ao PATH no arquivo $shell_rc"
        fi
    else
        echo "Arquivo $shell_rc não encontrado, criando e adicionando PATH..."
        echo "# Adicionado pelo instalador do Manai v2.0" > "$shell_rc"
        echo "$export_line" >> "$shell_rc"
        echo "Criado $shell_rc e adicionado PATH."
    fi
}

# Detectar shell do usuário e adicionar PATH
USER_SHELL=$(basename "$SHELL")

case "$USER_SHELL" in
    bash)
        add_path_to_shellrc "$HOME/.bashrc"
        ;;
    zsh)
        add_path_to_shellrc "$HOME/.zshrc"
        ;;
    *)
        echo "Shell $USER_SHELL não suportada para configuração automática do PATH."
        echo "Adicione manualmente a linha:"
        echo "  export PATH=\"$INSTALL_DIR:\$PATH\""
        ;;
esac

# Verificar se a instalação foi bem-sucedida
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    echo ""
    echo "Instalação concluída com sucesso!"
    echo ""
    echo "O comando '$SCRIPT_NAME' está agora disponível no diretório:"
    echo "  $INSTALL_DIR"
    echo ""
    echo "Para aplicar as alterações do PATH, reinicie o terminal ou execute:"
    echo "  source ~/.bashrc    # para bash"
    echo "  ou"
    echo "  source ~/.zshrc     # para zsh"
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


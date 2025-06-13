#!/bin/bash

SCRIPT_NAME="manai"
INSTALL_DIR="$HOME/.local/bin"
EXPORT_LINE="export PATH=\"$INSTALL_DIR:\$PATH\""

echo "A desinstalar o comando $SCRIPT_NAME..."

# Remover o arquivo do comando
if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    rm "$INSTALL_DIR/$SCRIPT_NAME"
    echo "Removido $INSTALL_DIR/$SCRIPT_NAME"
else
    echo "Arquivo $INSTALL_DIR/$SCRIPT_NAME não encontrado."
fi

# Função para remover a linha do PATH do arquivo shellrc
remove_path_from_shellrc() {
    local shell_rc="$1"
    if [ -f "$shell_rc" ]; then
        if grep -Fxq "$EXPORT_LINE" "$shell_rc"; then
            # Criar um arquivo temporário sem a linha de exportação
            grep -v -F "$EXPORT_LINE" "$shell_rc" > "${shell_rc}.tmp" && mv "${shell_rc}.tmp" "$shell_rc"
            echo "Removido $EXPORT_LINE do $shell_rc"
        else
            echo "Linha $EXPORT_LINE não encontrada em $shell_rc"
        fi
    else
        echo "Arquivo $shell_rc não encontrado."
    fi
}

# Detectar shell do usuário e remover PATH
USER_SHELL=$(basename "$SHELL")

case "$USER_SHELL" in
    bash)
        remove_path_from_shellrc "$HOME/.bashrc"
        ;;
    zsh)
        remove_path_from_shellrc "$HOME/.zshrc"
        ;;
    *)
        echo "Shell $USER_SHELL não suportada para remoção automática do PATH."
        echo "Remova manualmente a linha:"
        echo "  $EXPORT_LINE"
        ;;
esac

echo ""
echo "Desinstalação concluída."
echo "Para aplicar as alterações, reinicie o terminal ou execute:"
echo "  source ~/.bashrc    # para bash"
echo "  ou"
echo "  source ~/.zshrc     # para zsh"

#!/bin/bash
# Desk Organizer Mac - Script de Compilação do Aplicativo macOS (.app)
# Desenvolvido por: Daniel Júnior Barbosa da Silva (DL MIDIA) & Antigravity AI

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

APP_NAME="Organizar Mesa.app"
DEST_PATH="$HOME/Desktop/$APP_NAME"

echo "Compilando aplicativo AppleScript..."
osacompile -o "$DEST_PATH" "$DIR/main.scpt"

echo "Copiando scripts de organização para o pacote..."
mkdir -p "$DEST_PATH/Contents/Resources"
cp "$DIR/organizar_mesa.py" "$DEST_PATH/Contents/Resources/"
cp "$DIR/organizar_downloads.py" "$DEST_PATH/Contents/Resources/"
cp "$DIR/organizar_tudo.py" "$DEST_PATH/Contents/Resources/"

echo "✓ $APP_NAME gerado com sucesso em: $DEST_PATH"

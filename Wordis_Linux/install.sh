#1/bin/bash

caminho_relativo_app=$(find . -name "Wordis")
caminho_relativo_icon=$(find . -name "WordisIco.ico")
caminho_app=$(readlink -f $caminho_relativo_app)
caminho_icon=$(readlink -f $caminho_relativo_icon)

echo "[Desktop Entry]
Name=Wordis
Type=Application
Terminal=true
Exec=$caminho_app
Icon=$caminho_icon
Categories=Games" > Wordis.desktop

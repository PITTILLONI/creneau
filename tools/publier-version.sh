#!/bin/sh
# Donne un nouveau numéro de version à la page et à version.json, pour que les
# pages déjà ouvertes (et l'app sur l'écran d'accueil) se rechargent toutes seules.
# Usage : sh tools/publier-version.sh   (puis commit + push)
set -e
cd "$(dirname "$0")/.."
v=$(date +%Y%m%d-%H%M%S)
sed -i '' -E "s/const APP_VERSION = '[^']*';/const APP_VERSION = '$v';/" index.html
printf '{ "version": "%s" }\n' "$v" > version.json
echo "version $v"

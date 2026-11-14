#!/bin/sh
# Copie le corps HTML d'un mail dans le presse-papiers macOS (type HTML), pour le coller dans Gmail.
python3 - "$1" <<'P'
import sys,subprocess
s=open(sys.argv[1]).read()
b=s[s.index('>',s.index('<body'))+1:s.rindex('</body>')]
h=b.encode('utf-8').hex()
subprocess.run(['osascript','-e',f'set the clipboard to «data HTML{h}»'],check=True)
P

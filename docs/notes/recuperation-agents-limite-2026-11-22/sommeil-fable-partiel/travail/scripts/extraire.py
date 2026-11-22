# usage: python3 -I extraire.py PDF SORTIE_TXT
# Extrait le texte page par page (pdftotext -layout désactivé), avec un marqueur de page "=== PAGE n / N ===".
import subprocess, sys, re
pdf, out = sys.argv[1], sys.argv[2]
info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
m = re.search(r'Pages:\s+(\d+)', info)
n = int(m.group(1))
with open(out, 'w', encoding='utf-8') as f:
    for p in range(1, n + 1):
        t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), pdf, '-'], capture_output=True, text=True).stdout
        f.write(f'\n=== PAGE {p} / {n} ===\n')
        f.write(t)
print(out, n, 'pages')

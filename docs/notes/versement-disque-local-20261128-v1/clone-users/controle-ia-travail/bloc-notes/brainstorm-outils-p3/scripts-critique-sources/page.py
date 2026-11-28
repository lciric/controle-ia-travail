# page.py TXT N [N2] : imprime la page N (ou N..N2) du texte extrait
import sys
pages = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\f')
a = int(sys.argv[2]); b = int(sys.argv[3]) if len(sys.argv) > 3 else a
for i in range(a, b+1):
    print(f"===== page {i} / {len(pages)-1 if pages[-1].strip()=='' else len(pages)}")
    print(pages[i-1])

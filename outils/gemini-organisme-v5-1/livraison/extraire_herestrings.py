r"""Reconstitue les fichiers écrits par un script PowerShell de la forme
   Write-Utf8NoBomLf "$org\chemin" @'
   ...contenu...
   '@
sans exécuter le script. Écrit chaque fichier sous la racine donnée, en UTF-8 sans BOM, fins de ligne LF.
Usage : python -I extraire_herestrings.py SCRIPT RACINE_SORTIE"""
import pathlib, re, sys

script, racine = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
texte = script.read_text(encoding="utf-8")
lignes = texte.split("\n")
motif = re.compile(r'^Write-Utf8NoBomLf "\$org\\(?P<chemin>[^"]+)" @\'$')
i, n, ecrits = 0, len(lignes), []
while i < n:
    m = motif.match(lignes[i].rstrip("\r"))
    if not m:
        i += 1
        continue
    chemin = m.group("chemin").replace("\\", "/")
    j = i + 1
    corps = []
    while j < n and lignes[j].rstrip("\r") != "'@":
        corps.append(lignes[j].rstrip("\r"))
        j += 1
    if j >= n:
        sys.exit(f"here-string non fermée pour {chemin} (ligne {i+1})")
    contenu = "\n".join(corps)
    # PowerShell : le here-string @'...'@ n'inclut ni la fin de ligne après @' ni celle avant '@ ; le script ajoute
    # son contenu tel quel (Replace CRLF->LF). Le fichier écrit n'a donc pas de fin de ligne finale, sauf si le corps
    # se termine par une ligne vide.
    cible = racine / chemin
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(contenu, encoding="utf-8", newline="\n")
    ecrits.append((chemin, len(contenu.encode("utf-8")), i + 1, j + 1))
    i = j + 1
for chemin, octets, debut, fin in ecrits:
    print(f"{chemin}\t{octets} octets\tlignes {debut}-{fin}")
print(f"{len(ecrits)} fichiers écrits sous {racine}")

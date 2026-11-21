"""Essai des essais du correctif de la pagination de l'arbre du corpus (R5) : chaque garde de `corpus_pagine_v1` est défaite
tour à tour dans une copie jetable du paquet (hors du dépôt, rien n'est écrit sous `src/`), et le fichier d'essais
`tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py` doit tomber sur chaque copie défaite.

Emploi (depuis la racine du dépôt) :
    python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/essai-des-essais-corpus-pagine-v1.py
Sortie : une ligne par défaite (« tombe » attendu partout), puis le compte ; code de retour 1 si une défaite passe inaperçue.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[5]
MODULE = "controle_ia/lentilles_sondes_bbis/corpus_pagine_v1.py"
ESSAIS = RACINE / "tests" / "test_lentilles_sondes_bbis_corpus_pagine_v1.py"
DELAI_S = 120
DEFAITES = {
    "sans la borne du nombre de pages": ("        if lues >= int(borne):", "        if False:"),
    "borne décalée d'une page": ("        if lues >= int(borne):", "        if lues > int(borne):"),
    "lien hors de l'arbre du jeu demandé suivi": (
        "        if suivant is not None and not dans_l_arbre_du_jeu(suivant, depot):", "        if False:"),
    "garde du lien réduite à l'hôte": ('startswith(f"{mo.HOTE_HF}/api/datasets/{depot}/tree/")', 'startswith(f"{mo.HOTE_HF}/")'),
    "repli silencieux sur la première page": (
        '    raise Arret("transport sans lecture de page (ni méthode `page`, ni transport réel) : ',
        '    return transport.octets(url), None\n    raise Arret("transport sans lecture de page (ni méthode `page`, ni transport réel) : '),
    "pages non suivies (le défaut d'origine)": ("        url = suivant\n", "        url = None\n"),
    "texte de l'exception dans le message": ('({type(e).__name__})") from None\n        return contenu',
                                             '({e})") from None\n        return contenu'),
    "toute relation prise pour « next »": ('"next" in relation.group(1).lower().split()', "relation.group(1)"),
    "plus grand chemin au lieu du plus petit": ("            return fichiers[0]", "            return fichiers[-1]"),
    "toute extension comptée comme donnée": (' and str(e.get("path", "")).endswith(mo.EXTENSIONS_DONNEES))', ")"),
    "autre phrase quand aucun fichier": ("aucun fichier de données dans l'arbre : arrêt ; nœud", "aucun fichier : arrêt ; nœud"),
    "en-tête Link ignoré par le transport réel": ('lien_suivant(r.headers.get("Link"), url)', "None"),
}


def jouer(src: Path) -> bool:
    # `pyproject.toml` met `src` en tête des chemins d'import : la copie jetable le remplace, pour que ce soit elle qui soit lue
    # une défaite qui fait tourner les essais sans fin (la borne retirée) est vue : le délai passé compte comme une chute
    try:
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                            "-o", f"pythonpath={src} {RACINE / 'tests'}", str(ESSAIS)], cwd=RACINE, timeout=DELAI_S,
                           capture_output=True, text=True, env=os.environ | {"PYTHONPATH": str(src), "PYTHONDONTWRITEBYTECODE": "1"})
    except subprocess.TimeoutExpired:
        return False
    return r.returncode == 0


origine = (RACINE / "src" / MODULE).read_text(encoding="utf-8")
inapercues = []
with tempfile.TemporaryDirectory() as tmp:
    src = Path(tmp) / "src"
    shutil.copytree(RACINE / "src" / "controle_ia", src / "controle_ia", ignore=shutil.ignore_patterns("__pycache__"))
    print("copie saine :", "passe" if jouer(src) else "TOMBE (inattendu)")
    for nom, (avant, apres) in DEFAITES.items():
        assert origine.count(avant) == 1, (nom, origine.count(avant))
        (src / MODULE).write_text(origine.replace(avant, apres), encoding="utf-8")
        passe = jouer(src)
        print(f"{nom} :", "PASSE (défaite inaperçue)" if passe else "tombe")
        if passe:
            inapercues.append(nom)
print(f"{len(DEFAITES)} défaites, {len(DEFAITES) - len(inapercues)} vues par les essais, {len(inapercues)} inaperçues")
sys.exit(1 if inapercues else 0)

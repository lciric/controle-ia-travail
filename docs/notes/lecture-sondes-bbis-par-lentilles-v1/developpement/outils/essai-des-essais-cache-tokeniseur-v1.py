"""Essai des essais du correctif du tokeniseur (R5) : chaque garde de `cache_tokeniseur_v2` est défaite tour à tour dans une
copie jetable du paquet (hors du dépôt, rien n'est écrit sous `src/`), et les essais du module dans
`tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py` doivent tomber sur chaque copie défaite.

Les essais du lanceur (montage entier, fiche du code, fabrique, lignes) sont laissés de côté ici : la fiche du code des jouets
porte les empreintes du paquet du dépôt, si bien qu'ils tomberaient sur toute copie modifiée, sans rien prouver.

Emploi (depuis la racine du dépôt) :
    python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/essai-des-essais-cache-tokeniseur-v1.py
Sortie : une ligne par défaite (« tombe » attendu partout), puis le compte ; code de retour 1 si une défaite passe inaperçue.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[5]
MODULE = "controle_ia/lentilles_sondes_bbis/cache_tokeniseur_v2.py"
ESSAIS = RACINE / "tests" / "test_lentilles_sondes_bbis_cache_tokeniseur_v2.py"
HORS_LANCEUR = "not lanceur and not montage and not fiche_du_code and not modules_de and not outil and not lignes_de"
DELAI_S = 600
DEFAITES = {
    "aucun marqueur écrit (le défaut d'origine)": ("    for nom in absents:\n        with open(", "    for nom in ():\n        with open("),
    "un marqueur de moins dans la liste": ('ABSENTS_CONNUS = ("tokenizer.model", "added_tokens.json", "chat_template.jinja")',
                                           'ABSENTS_CONNUS = ("tokenizer.model", "added_tokens.json")'),
    "témoin de la lecture de l'arbre retiré": ('    manquants = sorted(n for n in poses if racine.get(n) != "file")', "    manquants = []"),
    "témoin qui accepte un dossier": ('if racine.get(n) != "file")', "if n not in racine)"),
    "présence à la racine non regardée": ("    presents = sorted(n for n in absents if n in racine)", "    presents = []"),
    "présence regardée pour les fichiers seulement": ("    presents = sorted(n for n in absents if n in racine)",
                                                      '    presents = sorted(n for n in absents if racine.get(n) == "file")'),
    "sans la borne de l'arbre": ("    if len(arbre) >= BORNE_ARBRE:", "    if False:"),
    "borne de l'arbre décalée": ("    if len(arbre) >= BORNE_ARBRE:", "    if len(arbre) > BORNE_ARBRE:"),
    "entrée en double acceptée": ('        if e["path"] in racine:', "        if False:"),
    "forme de l'arbre non contrôlée": ("    if not isinstance(arbre, list) or not all(", "    if False and not all("),
    "arbre lu sans la clé": ("transport.octets(mo.url_arbre(depot, revision), cle)", "transport.octets(mo.url_arbre(depot, revision), None)"),
    "arbre récursif au lieu de la racine": ("transport.octets(mo.url_arbre(depot, revision), cle)",
                                            "transport.octets(mo.url_arbre(depot, revision, recursif=True), cle)"),
    "refus de l'arbre laissé sans arrêt nommé": ("    except mo.RefusReseau as e:\n        raise Arret(f\"arbre des fichiers du modèle refusé",
                                                 "    except ZeroDivisionError as e:\n        raise Arret(f\"arbre des fichiers du modèle refusé"),
    "identifiant de contenu non relu": ("        if len(contenu) != int(taille) or mo.identifiant_git(contenu) != identifiant:",
                                        "        if len(contenu) != int(taille):"),
    "taille non relue": ("        if len(contenu) != int(taille) or mo.identifiant_git(contenu) != identifiant:",
                         "        if mo.identifiant_git(contenu) != identifiant:"),
    "branche principale non relue": ("    if designe != revision:", "    if False:"),
    "branche lue à un saut de ligne près": ('ref.read_text(encoding="utf-8") if', 'ref.read_text(encoding="utf-8").strip() if'),
    "autre branche ou autre instantané accepté": (
        "    if [p.name for p in _entrees(base / \"refs\")] != [BRANCHE] or [p.name for p in _entrees(base / \"snapshots\")] != [revision]:",
        "    if False:"),
    "fichier de plus accepté dans l'instantané": ("    if sorted(p.name for p in poses) != sorted(attendus) or ",
                                                  "    if not set(attendus) <= {p.name for p in poses} or "),
    "lien accepté dans l'instantané": ("or any(p.is_symlink() or not p.is_file() for p in poses)", "or any(not p.is_file() for p in poses)"),
    "marqueur de plus accepté": ("            or sorted(p.name for p in marqueurs) != sorted(absents)):",
                                 "            or not set(absents) <= {p.name for p in marqueurs}):"),
    "marqueur manquant accepté": ("            or sorted(p.name for p in marqueurs) != sorted(absents)):",
                                  "            or not {p.name for p in marqueurs} <= set(absents)):"),
    "marqueurs d'une autre révision acceptés": ("    if ([p.name for p in _entrees(dossier)] != ([revision] if absents else [])\n            or ",
                                                "    if (False\n            or "),
    "marqueur non vide accepté": (" or p.stat().st_size != 0:", ":"),
    "marqueur qui n'est pas un fichier accepté": ("        if p.is_symlink() or not p.is_file() or p.stat().st_size != 0:",
                                                  "        if not p.is_symlink() and p.is_file() and p.stat().st_size != 0:"),
    "cache déjà présent réécrit": ("    if base.exists() or base.is_symlink():", "    if False:"),
    "noms non contrôlés": ("        if not isinstance(nom, str) or not _NOM_SIMPLE.fullmatch(nom):", "        if False:"),
    "nom avec un dossier accepté": ('_NOM_SIMPLE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")', '_NOM_SIMPLE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")'),
    "nom à la fois posé et marqué accepté": ("    if communs:", "    if False:"),
    "doublon de nom accepté": ("    if len(set(absents)) != len(absents) or len(set(fichiers)) != len(fichiers):", "    if False:"),
    "attendus sans rapport avec les fichiers acceptés": ("    if sorted(attendus) != sorted(fichiers):", "    if False:"),
    "écriture avant la vérification de l'arbre": (
        "    racine = racine_du_depot(transport, cle, depot, revision)\n    exiger_absents(racine, fichiers, absents)\n"
        "    mo.poser_cache_tokeniseur(hf_home, fichiers, depot, revision)\n",
        "    mo.poser_cache_tokeniseur(hf_home, fichiers, depot, revision)\n"
        "    racine = racine_du_depot(transport, cle, depot, revision)\n    exiger_absents(racine, fichiers, absents)\n"),
}


def jouer(src: Path) -> bool:
    # `pyproject.toml` met `src` en tête des chemins d'import : la copie jetable le remplace, pour que ce soit elle qui soit lue
    try:
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", HORS_LANCEUR,
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
    print("copie saine :", "passe" if jouer(src) else "TOMBE (inattendu)", flush=True)
    for nom, (avant, apres) in DEFAITES.items():
        assert origine.count(avant) == 1, (nom, origine.count(avant))
        (src / MODULE).write_text(origine.replace(avant, apres), encoding="utf-8")
        passe = jouer(src)
        print(f"{nom} :", "PASSE (défaite inaperçue)" if passe else "tombe", flush=True)
        if passe:
            inapercues.append(nom)
print(f"{len(DEFAITES)} défaites, {len(DEFAITES) - len(inapercues)} vues par les essais, {len(inapercues)} inaperçues")
sys.exit(1 if inapercues else 0)

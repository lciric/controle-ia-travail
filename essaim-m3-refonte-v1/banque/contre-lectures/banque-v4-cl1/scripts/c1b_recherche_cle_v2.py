"""Contre-lecture banque v4 — c1b (v2 : dossiers de dépendances et objets git exclus) : où la clé v4 apparaît-elle sur disque ? — v1.
Lit la clé dans son fichier ; cherche ses écritures décimale et hexadécimale (minuscules, majuscules, 32 chiffres) dans
tous les fichiers des racines données, hors dossiers `donnees`, `runs`, `diag`, hors fichiers `P3-consignes-v1.md` et
`textes-actions-*`, hors dossier de sortie de cette contre-lecture. N'imprime que des chemins et des comptes.
Usage : python3 -I -B c1b_recherche_cle_v1.py FICHIER_CLE RACINE...
"""
import json, os, pathlib, sys

cle = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
e = int(cle["entropie_seed_sequence"])
motifs = {m.encode("ascii") for m in (str(e), format(e, "x"), format(e, "X"), format(e, "032x"), format(e, "032X"))}
EXCLUS_D = {"donnees", "runs", "diag", "proc", "sys", "dev", ".git", ".venv", "venv", "node_modules", "site-packages", ".cache", ".cargo", ".rustup", ".npm", ".gradle", ".bun", ".nix-defexpr", ".nix-profile"}
MOI = "/var/tmp/contre-lecture-banque-v4-v1"
LIMITE = 50 * 1024 * 1024
trouves, n_lus, n_grands, n_illisibles = [], 0, 0, 0
for racine in sys.argv[2:]:
    for d, sous, fichiers in os.walk(racine, followlinks=False):
        if d.startswith(MOI):
            sous[:] = []; continue
        sous[:] = [s for s in sous if s not in EXCLUS_D and not os.path.join(d, s).startswith(MOI)]
        for f in fichiers:
            if f == "P3-consignes-v1.md" or f.startswith("textes-actions-"):
                continue
            p = os.path.join(d, f)
            try:
                if os.path.islink(p) or not os.path.isfile(p):
                    continue
                if os.path.getsize(p) > LIMITE:
                    n_grands += 1; continue
                with open(p, "rb") as fh:
                    contenu = fh.read()
                n_lus += 1
                if any(m in contenu for m in motifs):
                    trouves.append(p)
            except OSError:
                n_illisibles += 1
print(json.dumps({"racines": sys.argv[2:], "fichiers_lus": n_lus, "fichiers_plus_de_50_Mo_non_lus": n_grands,
                  "illisibles": n_illisibles, "fichiers_contenant_la_cle": sorted(set(trouves))}, ensure_ascii=False, indent=1))

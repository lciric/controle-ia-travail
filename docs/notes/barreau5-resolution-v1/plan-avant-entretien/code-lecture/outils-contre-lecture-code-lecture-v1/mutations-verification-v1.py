"""Mutations du contre-lecteur à la vérification des corrections du code de lecture du barreau 5 (20 novembre 2026) : les
huit mutations de la contre-lecture (C1 à C8), rejouées telles quelles sur le code corrigé, et six neuves (N1 à N6) sur les
corrections et sur l'amorce.

Même procédé que `mutations-contre-lecture-v1.py` : une copie de travail sous le bloc-notes ; chaque « avant » doit paraître
exactement une fois ; attrapée si pytest rend le code 1 ; témoins sans mutation exigés verts ; fichier remis à l'identique.

Usage : python -B mutations-verification-v1.py COPIE BASETEMP
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
P = "src/controle_ia/barreau5_familles/"
L, S, R, A = f"{P}lecture_v1.py", f"{P}sondes_v1.py", f"{P}relecture_v1.py", "scripts/amorce_b5f_lecture_v1.sh"
EL, ES, ER, EA = ("tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py",
                  "tests/test_barreau5_familles_relecture_v1.py", "tests/test_amorce_b5f_lecture_v1.py")
A_COPIER = ["src", "tests/conftest.py", EL, ES, ER, EA, "tests/test_lancer_b5f_lecture_v1.py",
            "scripts/lancer_b5f_lecture_v1.sh", A, "prereg/T0.6-organismes-config-7b-v1.json",
            "prereg/T0.6-organismes-config-7b-v1.json.sha256", "pyproject.toml", "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    ("C1", L, "probabilité rapportée de « séparé » prise sur la somme des rangs positifs",
     "float(probabilite_au_plus(K, w_moins))", "float(probabilite_au_plus(K, w_plus))", [EL]),
    ("C2", L, "issue E sans que la séparation apprise soit établie",
     'if sep is not None and sep["etablie"] and E3["K"] > 0 and all(', 'if sep is not None and E3["K"] > 0 and all(', [EL]),
    ("C3", L, "issue E sans valeur absolue",
     'all(abs(v) < SEUIL_EMPREINTE * sep["delta_app"]', 'all(v < SEUIL_EMPREINTE * sep["delta_app"]', [EL]),
    ("C4", L, "garde d'ouverture : épreuve à vérité plantée non exigée avant les scores",
     'for a in ("ENGAGEMENT-B5F", "EPREUVE-B5F", "GO-LECTURE-B5F", "CODE-LECTURE-B5F"):',
     'for a in ("ENGAGEMENT-B5F", "GO-LECTURE-B5F", "CODE-LECTURE-B5F"):', [EL]),
    ("C5", L, "garde d'ouverture : table reçue non comparée à OUVERTURE-B5F",
     '_exiger(en.empreinte_table(table) == reg["ouverture"]["table"],', "_exiger(True,", [EL]),
    ("C6", L, "E2b : rapport des poussées inversé", "c = math.sqrt(rj / rs)", "c = math.sqrt(rs / rj)", [EL]),
    ("C7", L, "M1 et M3 : tâches en réunion au lieu de l'intersection",
     "communes = set.intersection(*jouees)", "communes = set.union(*jouees)", [EL]),
    ("C8", S, "la sonde d'un pli note les actions de l'autre pli",
     "series = noter(appris[(d.nom, k)], d, lecteur, cles, plis[k])",
     "series = noter(appris[(d.nom, k)], d, lecteur, cles, plis[1 - k])", [ES]),
    ("N1", L, "correction M-3 : le contenu d'un compagnon de l'arbre de lecture n'est plus vérifié",
     "        verifier(arbre / vise)", "        pass", [EL]),
    ("N2", L, "correction M-1 : sous « non interprétable », les descriptifs gardent les notations des sondes",
     'descriptifs(ch if lu else {**ch, "notations": {}}, fam', "descriptifs(ch, fam", [EL]),
    ("N3", R, "entrées : métadonnées admises dans un fichier d'adaptateur (« seuls tenseurs »)",
     'if not isinstance(entete, dict) or "__metadata__" in entete:', "if not isinstance(entete, dict):", [ER]),
    ("N4", R, "entrées : noms opaques non contigus admis",
     'if sorted(tenus) != [f"X-{k:02d}" for k in range(1, len(tenus) + 1)]:', "if False:", [ER]),
    ("N5", A, "amorce : témoin du versement final écrit sans les activations gardées versées",
     'if [ -f "$MARCHE_FINIE" ] && [ -s "$SORTIES_PROUVEES" ] && [ -f "$ACTIVATIONS_VERSEES" ]; then',
     'if [ -f "$MARCHE_FINIE" ] && [ -s "$SORTIES_PROUVEES" ]; then', [EA]),
    ("N6", A, "amorce : les entrées de lecture admises quand un fichier n'est pas ajouté par leur commit",
     '[ "$tous" = "$ajoutes" ] && [ -z "$autres" ] ||', "true ||", [EA]),
]


def copier(copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def jouer(copie: Path, base: Path, nom: str, essais) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *essais], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1][:200] if lignes else "",
            "premier_echec": echec[0][:220] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {}, "mutations": []}
    for nom, essais in {"EL": [EL], "ES": [ES], "ER": [ER], "EA": [EA]}.items():
        bilan["temoins"][nom] = jouer(copie, base, f"temoin-{nom}", essais)
        print(f"témoin {nom} : code {bilan['temoins'][nom]['code']} ({bilan['temoins'][nom]['fin']})", file=sys.stderr,
              flush=True)
    if any(t["code"] != 0 for t in bilan["temoins"].values()):
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        raise SystemExit("un témoin sans mutation échoue : aucun compte de mutations")
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        n = origine.count(avant)
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if n != 1:
            x.update({"etat": "introuvable", "occurrences": n})
            bilan["mutations"].append(x)
            print(f"{mid} introuvable ({n})", file=sys.stderr, flush=True)
            continue
        cible = copie / fichier
        cible.write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid, essais)
        finally:
            cible.write_text(origine, encoding="utf-8")
        etat = "attrapée" if r["code"] == 1 else ("MANQUÉE" if r["code"] == 0 else f"erreur de l'outil (code {r['code']})")
        x.update({"etat": etat, **r})
        bilan["mutations"].append(x)
        print(f"{mid} {etat} ({r['duree_s']} s) {r['premier_echec'] or ''}", file=sys.stderr, flush=True)
    joues = [m for m in bilan["mutations"] if m["etat"] in ("attrapée", "MANQUÉE")]
    bilan["compte"] = {"jouees": len(joues), "attrapees": sum(m["etat"] == "attrapée" for m in joues),
                       "manquees": [m["id"] for m in joues if m["etat"] == "MANQUÉE"],
                       "autres": [m["id"] for m in bilan["mutations"] if m["etat"] not in ("attrapée", "MANQUÉE")]}
    print(json.dumps(bilan["compte"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

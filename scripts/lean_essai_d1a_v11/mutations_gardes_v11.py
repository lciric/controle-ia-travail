"""Mutations des gardes neuves de l'essai Lean D-1a, v11 (exécuteur v7, épreuve v7, attendus v6, pilote v11), sur des copies.

Méthode des lanceurs précédents (`scripts/lean_essai_d1a_v10/mutations_harnais_v10.py`), allégée aux gardes neuves : une
copie neuve par mutation (`src/`, les essais v7 et v11 et `conftest.py`, les artefacts, les scripts v10 et v11) ; remplacement
exact présent une seule fois (sinon arrêt avant tout) ; **import tracé** vers la copie ; `pytest` lancé sur la copie, sans
`PYTHONPATH` hérité. Une mutation est tuée si les essais échouent. Témoin d'abord : la copie sans mutation doit passer.
Les essais avec chaîne (sondes v2 et v3 compilées dans le bac à sable) sont joués si `LEAN_ESSAI_D1A_CHAINE` est posée.

Usage : python -I -B mutations_gardes_v11.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_executeur_v7.py", "tests/test_lean_essai_epreuve_v7.py", "tests/test_lean_essai_pilote_v11.py"]
A_COPIER = ["src", "tests/conftest.py", *ESSAIS, "scripts/lean_essai_d1a_v4/artefacts_r5_v4", "scripts/lean_essai_d1a_v10",
            "scripts/lean_essai_d1a_v11"]
LE = "src/controle_ia/lean_essai/"
X7, E7 = LE + "executeur_bac_v7.py", LE + "epreuve_isolement_v7.py"
A6 = "scripts/lean_essai_d1a_v4/artefacts_r5_v4/attendus-v6.json"
P11 = "scripts/lean_essai_d1a_v11/piloter_poste_v11.sh"
DELAI_S = 900

MUTATIONS = [
    # exécuteur v7 : classement du temps de processeur (pas 4)
    ("x701", "seuil strict : limite atteinte exactement non classée", X7,
     '        return "délai" if cpu >= cpu_max_s else None', '        return "délai" if cpu > cpu_max_s else None'),
    ("x702", "jamais « délai » hors timeout", X7,
     '        return "délai" if cpu >= cpu_max_s else None', '        return None'),
    ("x703", "retour au code de sortie : 137 vaut « délai »", X7,
     '        return "délai" if cpu >= cpu_max_s else None', '        return "délai" if res.get("code") == 137 else None'),
    ("x704", "retour à la fin du processus : « XCPU » vaut « délai »", X7,
     '        return "délai" if cpu >= cpu_max_s else None',
     '        return "délai" if "XCPU" in (res.get("fin") or "") else None'),
    ("x705", "temps de processeur absent : repli silencieux", X7,
     '            raise ErreurBac(f"résultat {resultat!r} sans temps de processeur rapporté par systemd : classement impossible")',
     '            return None'),
    ("x706", "réussite classée par le temps de processeur", X7,
     '    if resultat == "success":\n        return None\n    if resultat == "timeout":',
     '    if False:\n        return None\n    if resultat == "timeout":'),
    ("x707", "limite de la configuration ignorée (5 s fixes)", X7,
     "incident_c = classer_execution(compil, self.cfg.cpu_max_s)", "incident_c = classer_execution(compil, 5)"),
    ("x714", "limite de la configuration ignorée au noyau (5 s fixes)", X7,
     "incident_v = classer_execution(verif, self.cfg.cpu_max_s)", "incident_v = classer_execution(verif, 5)"),
    ("x715", "limite de la configuration ignorée en Python (5 s fixes)", X7,
     "incident = classer_execution(r, self.cfg.cpu_max_s)", "incident = classer_execution(r, 5)"),
    # exécuteur v7 : pic de mémoire (pas 5)
    ("x708", "pic : dernier relevé au lieu du plus haut", X7,
     "pic, echantillons = (v if pic is None else max(pic, v)), echantillons + 1",
     "pic, echantillons = v, echantillons + 1"),
    ("x709", "pic lu dans une autre tranche", X7, 'TRANCHE = "system.slice"', 'TRANCHE = "user.slice"'),
    ("x710", "aucun échantillonnage pendant l'attente", X7, "        while p.poll() is None:", "        while False:"),
    ("x711", "« Memory peak » de systemd relu", X7,
     '        elif "Service runtime:" in ligne:',
     '        elif "Memory peak:" in ligne:\n            res["memoire_pic"] = ligne.split(":", 1)[1].strip()\n'
     '        elif "Service runtime:" in ligne:'),
    ("x712", "sortie d'erreur de la compilation non lue", X7,
     '"erreurs_compilation": _lire(d_sorties / "compilation.err")', '"erreurs_compilation": _lire(d_sorties / "absent.err")'),
    ("x713", "pic retiré des clés publiques", X7,
     '"cpu_s", "memoire_pic_echantillonne_octets",\n', '"cpu_s",\n'),
    # épreuve v7 (pas 3 et 5)
    ("e701", "cas sain toujours vivant", E7,
     "    return all(vues.get(nom) == attendu for nom, attendu in cas[\"tentatives\"].items())", "    return True"),
    ("e702", "genre mort jamais déclaré", E7, "        if sains.get(g) is False:", "        if False:"),
    ("e703", "épreuve morte rapportée « non conforme »", E7,
     'statut = "épreuve morte" if morts else', 'statut = "non conforme" if morts else'),
    ("e704", "ECHEC sans valeur de preuve admis", E7,
     "for m in cas.get(\"echecs_invalides\", []) if m in details.get(nom, \"\")]",
     "for m in cas.get(\"echecs_invalides\", []) if False]"),
    ("e705", "détail des tentatives non capturé", E7,
     "RE_TENTATIVE = re.compile(r'ISOLEMENT (\\S+) (ECHEC|REUSSI)((?:(?!\\\\n)[^\\n\"])*)')",
     "RE_TENTATIVE = re.compile(r'ISOLEMENT (\\S+) (ECHEC|REUSSI)()')"),
    ("e706", "sortie de compilation non bornée", E7,
     '"sortie_compilation_extrait": so[:EXTRAIT_SONDE]', '"sortie_compilation_extrait": so'),
    ("e707", "sonde muette jamais marquée", E7, '"sonde_muette": not RE_TENTATIVE.search(so)}', '"sonde_muette": False}'),
    ("e708", "sortie de compilation absente du JSON de l'isolement", E7,
     '        _noter(rendus, sorties, "isolement Lean", cas, res, juger_tentatives(cas, res["sortie_compilation"]),\n'
     '               extrait_sonde(res))',
     '        _noter(rendus, sorties, "isolement Lean", cas, res, juger_tentatives(cas, res["sortie_compilation"]))'),
    ("e709", "groupe des limites Lean non joué", E7,
     'attendus.get("limites_lean", [])', 'attendus.get("limites_lean_absent", [])'),
    ("e710", "limite Lean : incident non jugé", E7,
     "    if res.get(\"incident_bac\") != cas[\"incident_attendu\"]:\n        ecarts.append(f\"incident du bac {res.get('incident_bac')!r}, {cas['incident_attendu']!r} attendu\")\n    if cas.get(\"compilation_code_non_nul\")",
     "    if cas.get(\"compilation_code_non_nul\")"),
    ("e711", "code de sortie de l'épreuve morte confondu (1)", E7, "        return 3\n", "        return 1\n"),
    ("e712", "cas sain Python non relevé", E7, '            sains["Python"] = sain_vivant(cas, res["stdout"])',
     '            pass'),
    ("e713", "épreuve toujours sur les attendus v5", E7, 'ATTENDUS = "attendus-v6.json"', 'ATTENDUS = "attendus-v5.json"'),
    # attendus v6 et pilote v11
    ("a701", "limite Lean attendue sans incident", A6,
     '"incident_attendu": "mémoire",\n   "compilation_code_non_nul"', '"incident_attendu": null,\n   "compilation_code_non_nul"'),
    ("a702", "cas 137 attendu « délai »", A6,
     '"SORTIE 137"\n   ],\n   "incident_attendu": null', '"SORTIE 137"\n   ],\n   "incident_attendu": "délai"'),
    ("p701", "pilote : épreuve v6 copiée", P11, '"$PAQ/epreuve_isolement_v7.py"', '"$PAQ/epreuve_isolement_v6.py"'),
]


def copier(racine: Path, copie: Path) -> None:
    for rel in A_COPIER:
        s, d = racine / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def environnement(copie: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "HCLOUD_TOKEN", "VAST_API_KEY")}
    env["PYTHONPATH"] = str(copie / "src")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def tracer_import(copie: Path) -> str:
    p = subprocess.run([sys.executable, "-B", "-c", "import controle_ia.lean_essai.executeur_bac_v7 as X; print(X.__file__)"],
                       capture_output=True, text=True, env=environnement(copie), cwd=copie, timeout=60)
    chemin = p.stdout.strip()
    if not chemin.startswith(str(copie)):
        raise SystemExit(f"import non tracé vers la copie : {chemin!r} {p.stderr[-300:]}")
    return chemin


def lancer_essais(copie: Path) -> tuple[int, str]:
    try:
        p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--rootdir",
                            str(copie), *[str(copie / e) for e in ESSAIS]],
                           capture_output=True, text=True, env=environnement(copie), cwd=copie, timeout=DELAI_S)
    except subprocess.TimeoutExpired:
        return -9, "délai"
    lignes = [l for l in p.stdout.splitlines() if l.strip()]
    return p.returncode, (lignes[-1] if lignes else p.stderr[-200:])


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 2:
        raise SystemExit("usage : RACINE TRAVAIL")
    racine, travail = Path(argv[0]).resolve(), Path(argv[1]).resolve()
    ids = [m[0] for m in MUTATIONS]
    if len(ids) != len(set(ids)):
        raise SystemExit("identifiants de mutation en double")
    for ident, _d, fichier, ancien, _n in MUTATIONS:
        n = (racine / fichier).read_text(encoding="utf-8").count(ancien)
        if n != 1:
            raise SystemExit(f"{ident} inapplicable : {n} occurrence(s) dans {fichier}")
    if travail.exists():
        raise SystemExit(f"{travail} existe déjà : dossier de travail neuf exigé")
    travail.mkdir(parents=True)
    temoin = travail / "temoin"
    copier(racine, temoin)
    tracer_import(temoin)
    code, ligne = lancer_essais(temoin)
    resultats = [{"id": "témoin", "defaut": "aucune mutation", "code": code, "fin": ligne, "tuee": None}]
    if code != 0:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        raise SystemExit("la copie témoin ne passe pas : mutations sans objet")
    shutil.rmtree(temoin)
    for ident, defaut, fichier, ancien, nouveau in MUTATIONS:
        copie = travail / ident
        copier(racine, copie)
        cible = copie / fichier
        cible.write_text(cible.read_text(encoding="utf-8").replace(ancien, nouveau), encoding="utf-8")
        tracer_import(copie)
        code, ligne = lancer_essais(copie)
        resultats.append({"id": ident, "defaut": defaut, "fichier": fichier, "code": code, "fin": ligne,
                          "tuee": code != 0, "par_delai": code == -9})
        shutil.rmtree(copie)
    survivantes = [r["id"] for r in resultats if r["tuee"] is False]
    print(json.dumps({"version": "mutations_gardes_v11", "chaine": bool(os.environ.get("LEAN_ESSAI_D1A_CHAINE")),
                      "mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "detail": resultats}, ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())

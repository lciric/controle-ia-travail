"""Mutations du harnais Lean v4 sur des copies (CLC3-11 de la contre-lecture courte de la v3 `b6ca886d…`, R-2307).

Même méthode que la v3 : copie neuve par mutation, remplacement exact présent une seule fois (sinon arrêt), **import tracé**
vers la copie, `pytest -o pythonpath=<copie>/src <copie>/tests` sans `PYTHONPATH` hérité, délai de 180 s. Au moins une mutation
par correction v4 (CLC3-01 à CLC3-04, CLC3-06 à CLC3-10), et une par survivante de CLC3-11, k12 en tête (k01, k02, k03, k04,
k05, k07, k11, k12, k13, k14, k15, k16).

Usage : python -I -B mutations_harnais_v4.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_gardes_v4.py", "tests/test_lean_essai_executeur_v4.py",
          "tests/test_lean_essai_minuterie_v4.py"]
G, X, E, M, M3, H4, H3 = ("gardes_lean_v4", "executeur_bac_v4", "epreuve_isolement_v4", "minuterie_v4", "minuterie_v3",
                          "hetzner_v4", "hetzner_v3")

MUTATIONS = [
    ("k12", "CLC3-11 k12 : imbrication", G, "                        profondeur, j = profondeur + 1, j + 2",
     "                        profondeur, j = profondeur, j + 2"),
    ("c01", "CLC3-01 : documentation", G, 'profondeur, j = 1, i + (3 if source.startswith(("/--", "/-!"), i) else 2)',
     "profondeur, j = 1, i + 2"),
    ("c02a", "CLC3-02 : troncature", G,
     'if a.get("tronque") is not False or "⋯" in str(a.get("enonce", "")) or "⋯" in str(a.get("enonce_explicite", "")):',
     'if a.get("tronque") is True:'),
    ("c02b", "CLC3-02 : métavariables", G, 'if a.get("metavariables") is not False:', "if False:"),
    ("c02c", "CLC3-02 : messages", G, 'if a.get("messages_elaboration") != 0:', "if False:"),
    ("c03", "CLC3-03 : imports exacts", G, "if v[\"imports\"] and sorted(modules or []) != sorted(IMPORTS_EXACTS):", "if False:"),
    ("c06a", "CLC3-06 : énoncé final", G, "            if nom == ENONCE:", "            if False:"),
    ("c06b", "CLC3-06 : liste rapportée", G, "if not isinstance(citees, list):", "if False:"),
    ("c06c", "CLC3-06 : hors ASCII", G, "        if hors_ascii:", "        if False:"),
    ("k07", "CLC3-11 k07", G, 'if not RE_NONCE.match(nonce or ""):', "if False:"),
    ("k14", "CLC3-11 k14", G, "anomalies.append(f\"constante {o.get('nom')!r} rapportée deux fois\")", "pass"),
    ("k15", "CLC3-11 k15", G, "if permis and len(rejeux) != 1:", "if permis and len(rejeux) < 1:"),
    ("c04a", "CLC3-04 : rejeu exposé", G, '"rejeu_present": len(rejeux) == 1,', '"rejeu_present": True,'),
    ("c04b", "CLC3-04 : G-L1 et G-L7", E, 'if not v["gardes"][g]["ok"] and g not in cas.get("echecs", []):', "if False:"),
    ("c04c", "CLC3-04 : ligne de rejeu", E, 'if not v.get("rejeu_present"):', "if False:"),
    ("c04d", "CLC3-04 : constante nommée", E, 'elif cas.get("constante_fautive", "\\0") not in str(v.get("rejeu_erreur", "")):', "elif False:"),
    ("c04e", "CLC3-04 : sans G-L3+", E, 'for passage, supplementaires in (("avec G-L3+", True), ("sans G-L3+", False)):',
     'for passage, supplementaires in (("avec G-L3+", True),):'),
    ("c05a", "note 3 : lstat", X, "if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:", "if False:"),
    ("c05b", "CLC3-05 : borne de l'olean", X, "if st.st_size > OLEAN_MAX:", "if False:"),
    ("k05", "CLC3-11 k05", X, 'if r["code"] != 0 or r.get("resultat") != "success":', 'if r["code"] != 0:'),
    ("c07a", "CLC3-07 a : nom", M, "    trouves = sorted(set(par_etiquettes) | set(par_nom))", "    trouves = sorted(set(par_etiquettes))"),
    ("c07b", "CLC3-07 a, note 4", M, "    autres = [(i, n) for i, n in trouves if n != NOM_MACHINE]", "    autres = []"),
    ("c07c", "CLC3-07 b : setsid", M, "start_new_session=True", "start_new_session=False"),
    ("c07d", "CLC3-07 b : PID", M, 'fichier_pid.write_text(f"{p.pid} {identifiant} {jeton}\\n", encoding="utf-8")',
     'fichier_pid.write_text(f"0 {identifiant} {jeton}\\n", encoding="utf-8")'),
    ("c07e", "CLC3-07 b : contrôle du PID", M, "    vivante = all(a in arguments for a in attendu)", "    vivante = True"),
    ("c07f", "CLC3-07 c : marge", M, "    tache = echeance - timedelta(hours=MARGE_TACHE_H)", "    tache = echeance"),
    ("c07g", "CLC3-07 d : fichier", M, '    chemin.write_text(json.dumps(entree, ensure_ascii=False, indent=1, default=str) + "\\n", encoding="utf-8")\n',
     ""),
    ("c07h", "CLC3-07 d : jeton neuf", M, '    if chemin.exists():\n        raise GardeArret(f"{chemin} existe déjà',
     '    if False:\n        raise GardeArret(f"{chemin} existe déjà'),
    ("c08a", "CLC3-08 : fenêtre", M, "        if ecoule >= fenetre_s:", "        if True:"),
    ("c08b", "CLC3-08 : rien trouvé", M, '    if not detruits:\n        raise GardeArret(f"rien trouvé',
     '    if False:\n        raise GardeArret(f"rien trouvé'),
    ("c08c", "note 5 : aucune création", M, 'if e.get("destruction_confirmee") or e.get("aucune_creation"):',
     'if e.get("destruction_confirmee"):'),
    ("c08d", "note 5 : refus net", H4, "        if 400 <= statut < 500:", "        if False:"),
    ("c09", "CLC3-09", M, "    except OSError as e:\n        try:\n            sys.stderr.write(f\"journal en échec",
     "    except ZeroDivisionError as e:\n        try:\n            sys.stderr.write(f\"journal en échec"),
    ("c10a", "CLC3-10 / k16 : taux", M, "    return max(TAUX_USD_EUR_RETENU, declare or 0.0)", "    return declare or TAUX_USD_EUR_RETENU"),
    ("c10b", "CLC3-10 : taux non positif", M, "    if declare is not None and declare <= 0:", "    if False:"),
    ("c10c", "CLC3-10 : type (création)", M, "    if type_serveur not in TYPES_PERMIS:\n        raise GardeArret(f\"type",
     "    if False:\n        raise GardeArret(f\"type"),
    ("c10d", "CLC3-10 : type (client)", H4, "        if type_serveur not in TYPES_PERMIS:", "        if False:"),
    ("c10e", "CLC3-07 a : pas", H4, "selecteur = urllib.parse.quote(f\"essai={ETIQUETTES['essai']},pas={pas}\", safe=\"\")",
     "selecteur = urllib.parse.quote(f\"essai={ETIQUETTES['essai']}\", safe=\"\")"),
    ("k01", "CLC3-11 k01", M, "    depuis = min(intention, cree_a)", "    depuis = cree_a"),
    ("k02", "CLC3-11 k02", M, "for i, n in trouves]", "for i, n in trouves[:1]]"),
    ("k03", "CLC3-11 k03", M3, 'if g["echeance"] is not None and not (g["accorde"] <= aujourdhui <= g["echeance"]):', "if False:"),
    ("k11", "CLC3-11 k11", M, "    if declare is not None and declare < registre:", "    if False:"),
    ("k13a", "CLC3-11 k13", M, '            if echeance > ECHEANCES_H[a.pas]:\n                raise GardeArret("échéance plus longue',
     '            if False:\n                raise GardeArret("échéance plus longue'),
    ("k13b", "veiller --depuis", M, "            if depuis > cree_a:", "            if False:"),
    ("k13c", "veiller --depuis lu", M, "            depuis = cree_a if a.depuis is None else datetime.fromisoformat(a.depuis)",
     "            depuis = cree_a"),
    ("k04", "CLC3-11 k04", H3, "    if not appliques:", "    if False:"),
]

def copier(racine: Path, dest: Path) -> None:
    (dest / "src" / "controle_ia").mkdir(parents=True)
    for f in ("__init__.py", "gardes.py"):
        shutil.copy2(racine / "src" / "controle_ia" / f, dest / "src" / "controle_ia" / f)
    shutil.copytree(racine / "src" / "controle_ia" / "lean_essai", dest / "src" / "controle_ia" / "lean_essai",
                    ignore=shutil.ignore_patterns("__pycache__"))
    (dest / "tests").mkdir()
    for f in ["tests/conftest.py"] + ESSAIS:
        shutil.copy2(racine / f, dest / f)
    shutil.copy2(racine / "pyproject.toml", dest / "pyproject.toml")
    shutil.copytree(racine / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4",
                    dest / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4")


def env_propre() -> dict:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def tracer_import(copie: Path, module: str) -> str:
    code = ("import sys; sys.path[:0] = [sys.argv[1] + '/src', sys.argv[1] + '/tests']; "
            f"import controle_ia.lean_essai.{module} as m; print(m.__file__)")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(copie)], capture_output=True, text=True,
                       env=env_propre(), cwd=copie)
    chemin = p.stdout.strip()
    if p.returncode != 0 or not chemin.startswith(str(copie)):
        raise SystemExit(f"import non tracé vers la copie : {chemin!r} {p.stderr[-300:]}")
    return chemin


def lancer_essais(copie: Path) -> tuple[int, str]:
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-c", str(copie / "pyproject.toml"),
           "--rootdir", str(copie), "-o", f"pythonpath={copie / 'src'} {copie / 'tests'}"] + [str(copie / e) for e in ESSAIS]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=env_propre(), cwd=copie, timeout=180)
    except subprocess.TimeoutExpired:
        return -9, "délai dépassé (boucle sans fin) : enfant arrêté par son PID"
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    return p.returncode, (lignes[-1] if lignes else p.stderr[-200:])


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    racine, travail = Path(argv[0]).resolve(), Path(argv[1]).resolve()
    travail.mkdir(parents=True, exist_ok=True)
    temoin = travail / "temoin"
    shutil.rmtree(temoin, ignore_errors=True)
    copier(racine, temoin)
    tracer_import(temoin, G)
    code, ligne = lancer_essais(temoin)
    resultats = [{"id": "témoin", "defaut": "aucune mutation", "code": code, "fin": ligne, "tuee": None}]
    if code != 0:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        raise SystemExit("la copie témoin ne passe pas : mutations sans objet")
    for ident, defaut, module, ancien, nouveau in MUTATIONS:
        copie = travail / ident
        shutil.rmtree(copie, ignore_errors=True)
        copier(racine, copie)
        fichier = copie / "src" / "controle_ia" / "lean_essai" / f"{module}.py"
        texte = fichier.read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            raise SystemExit(f"{ident} inapplicable : {texte.count(ancien)} occurrence(s) dans {module}.py")
        fichier.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        trace = tracer_import(copie, module)
        code, ligne = lancer_essais(copie)
        resultats.append({"id": ident, "defaut": defaut, "module": module, "import": trace.replace(str(travail), "<travail>"),
                          "code": code, "fin": ligne, "tuee": code != 0})
        shutil.rmtree(copie)
    shutil.rmtree(temoin)
    survivantes = [r["id"] for r in resultats if r["tuee"] is False]
    print(json.dumps({"mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "detail": resultats}, ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())

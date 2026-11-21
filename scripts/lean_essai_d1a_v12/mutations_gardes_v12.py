"""Mutations des gardes de l'essai Lean D-1a, v12 (exécuteur v8, épreuve v8, attendus v7, pilote v12), sur des copies.

Copie de `scripts/lean_essai_d1a_v11/mutations_gardes_v11.py` (inchangé, R12) ; changements : essais v8 et pilote v12 ;
mutations de la v11 portées sur les v8 (x701 à x715 ; e701 à e713 sauf e710, sans objet : le juge du cas Lean de mémoire est
réécrit) ; neuves : x801 à x810 (marge du « délai », B2, incidents à part, tranche), e801 à e822 (B1, signal d'un chemin de
cgroupe faux, mémoire de la machine entière, témoin sain obligatoire), a801, p801. Même méthode. Les variables X7, E7, A6 et P11 gardent leur nom et
désignent les v8, les attendus v7 et le pilote v12.

Usage : python -I -B mutations_gardes_v12.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.

Texte de la v11 :
Mutations des gardes neuves de l'essai Lean D-1a, v11 (exécuteur v7, épreuve v7, attendus v6, pilote v11), sur des copies.

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

ESSAIS = ["tests/test_lean_essai_executeur_v8.py", "tests/test_lean_essai_epreuve_v8.py", "tests/test_lean_essai_pilote_v12.py"]
A_COPIER = ["src", "tests/conftest.py", *ESSAIS, "scripts/lean_essai_d1a_v4/artefacts_r5_v4", "scripts/lean_essai_d1a_v10",
            "scripts/lean_essai_d1a_v11", "scripts/lean_essai_d1a_v12"]
LE = "src/controle_ia/lean_essai/"
X7, E7 = LE + "executeur_bac_v8.py", LE + "epreuve_isolement_v8.py"
A6 = "scripts/lean_essai_d1a_v4/artefacts_r5_v4/attendus-v7.json"
P11 = "scripts/lean_essai_d1a_v12/piloter_poste_v12.sh"
DELAI_S = 900

MUTATIONS = [
    # --- portées de la v11 : exécuteur, classement du temps de processeur
    ("x701", "seuil strict : limite moins la tolérance non classée", X7,
     '        return "délai" if cpu >= cpu_max_s - TOLERANCE_CPU_S else None',
     '        return "délai" if cpu > cpu_max_s - TOLERANCE_CPU_S else None'),
    ("x702", "jamais « délai » hors timeout", X7,
     '        return "délai" if cpu >= cpu_max_s - TOLERANCE_CPU_S else None', '        return None'),
    ("x703", "retour au code de sortie : 137 vaut « délai »", X7,
     '        return "délai" if cpu >= cpu_max_s - TOLERANCE_CPU_S else None',
     '        return "délai" if res.get("code") == 137 else None'),
    ("x704", "retour à la fin du processus : « XCPU » vaut « délai »", X7,
     '        return "délai" if cpu >= cpu_max_s - TOLERANCE_CPU_S else None',
     '        return "délai" if "XCPU" in (res.get("fin") or "") else None'),
    ("x705", "temps de processeur absent : repli silencieux", X7,
     '            raise ErreurBac(f"résultat {resultat!r} sans temps de processeur rapporté par systemd : classement impossible")',
     '            return None'),
    ("x706", "réussite classée par le temps de processeur", X7,
     '    if resultat == "success":\n        return None\n    if resultat == "timeout":',
     '    if False:\n        return None\n    if resultat == "timeout":'),
    ("x707", "limite de la configuration ignorée à la compilation (5 s fixes)", X7,
     "incident_c = classer_execution(compil, self.cfg.cpu_max_s)", "incident_c = classer_execution(compil, 5)"),
    ("x714", "limite de la configuration ignorée au noyau (5 s fixes)", X7,
     "incident_v = classer_execution(verif, self.cfg.cpu_max_s)", "incident_v = classer_execution(verif, 5)"),
    ("x715", "limite de la configuration ignorée en Python (5 s fixes)", X7,
     "incident = classer_execution(r, self.cfg.cpu_max_s)", "incident = classer_execution(r, 5)"),
    # --- portées de la v11 : exécuteur, pic de mémoire
    ("x708", "pic : dernier relevé au lieu du plus haut", X7,
     "pic, echantillons = (v if pic is None else max(pic, v)), echantillons + 1",
     "pic, echantillons = v, echantillons + 1"),
    ("x709", "tranche par défaut changée", X7, 'TRANCHE = "system.slice"   # tranche par défaut',
     'TRANCHE = "user.slice"   # tranche par défaut'),
    ("x710", "aucun échantillonnage pendant l'attente", X7, "        while p.poll() is None:", "        while False:"),
    ("x711", "« Memory peak » de systemd relu", X7,
     '        elif "Service runtime:" in ligne:',
     '        elif "Memory peak:" in ligne:\n            res["memoire_pic"] = ligne.split(":", 1)[1].strip()\n'
     '        elif "Service runtime:" in ligne:'),
    ("x712", "sortie d'erreur de la compilation non lue", X7,
     '"erreurs_compilation": _lire(d_sorties / "compilation.err")', '"erreurs_compilation": _lire(d_sorties / "absent.err")'),
    ("x713", "pic retiré des clés publiques", X7,
     '"cpu_s", "memoire_pic_echantillonne_octets",\n', '"cpu_s",\n'),
    # --- neuves : exécuteur v8
    ("x801", "marge du « délai » retirée", X7,
     '        return "délai" if cpu >= cpu_max_s - TOLERANCE_CPU_S else None',
     '        return "délai" if cpu >= cpu_max_s else None'),
    ("x802", "marge du « délai » portée à 1 s", X7, "TOLERANCE_CPU_S = 0.05", "TOLERANCE_CPU_S = 1.0"),
    ("x803", "B2 défait : « fichier absent » seul attrapé", X7,
     "    except (OSError, ValueError):\n        return None", "    except (FileNotFoundError, ProcessLookupError):\n        return None"),
    ("x804", "B2 à moitié : contenu illisible non attrapé", X7,
     "    except (OSError, ValueError):\n        return None", "    except OSError:\n        return None"),
    ("x805", "B2 à moitié : « No such device » non attrapé", X7,
     "    except (OSError, ValueError):\n        return None", "    except (FileNotFoundError, ValueError):\n        return None"),
    ("x806", "incident de la compilation confondu avec celui du bac", X7,
     '"incident_compilation": incident_c,', '"incident_compilation": incident_c or incident_v,'),
    ("x807", "tranche de la configuration ignorée dans la commande", X7, 'f"--slice={c.tranche}"', 'f"--slice={TRANCHE}"'),
    ("x808", "tranche de la configuration ignorée dans le chemin du cgroupe", X7,
     "self.cfg.racine_cgroup / self.cfg.tranche /", "self.cfg.racine_cgroup / TRANCHE /"),
    ("x809", "nom de tranche non contrôlé", X7, "        if not RE_TRANCHE.match(cfg.tranche):", "        if False:"),
    ("x810", "tranche à tiret admise", X7, 'RE_TRANCHE = re.compile(r"^[A-Za-z0-9_]{1,64}\\.slice$")',
     'RE_TRANCHE = re.compile(r"^[A-Za-z0-9_-]{1,64}\\.slice$")'),
    # --- portées de la v11 : épreuve
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
    ("e711", "code de sortie de l'épreuve morte confondu (1)", E7, "        return 3\n", "        return 1\n"),
    ("e712", "cas sain Python non relevé", E7, '            sains["Python"] = sain_vivant(cas, res["stdout"])',
     '            pass'),
    ("e713", "épreuve sur les attendus v6", E7, 'ATTENDUS = "attendus-v7.json"', 'ATTENDUS = "attendus-v6.json"'),
    # --- neuves : épreuve v8, B1
    ("e801", "B1 défait : retour à l'incident du bac", E7,
     '    if compil.get("resultat") != cas["resultat_compilation_attendu"]:\n'
     '        ecarts.append(f"compilation : résultat systemd {compil.get(\'resultat\')!r}, "\n'
     '                      f"{cas[\'resultat_compilation_attendu\']!r} attendu")\n'
     '    if res.get("incident_compilation") != cas["incident_compilation_attendu"]:\n'
     '        ecarts.append(f"compilation : incident {res.get(\'incident_compilation\')!r}, "\n'
     '                      f"{cas[\'incident_compilation_attendu\']!r} attendu")\n',
     '    if res.get("incident_bac") != cas["incident_compilation_attendu"]:\n'
     '        ecarts.append(f"incident du bac {res.get(\'incident_bac\')!r}")\n'),
    ("e802", "B1 : résultat systemd de la compilation non jugé", E7,
     '    if compil.get("resultat") != cas["resultat_compilation_attendu"]:', '    if False:'),
    ("e803", "B1 : classement lu sur l'incident du bac", E7,
     '    if res.get("incident_compilation") != cas["incident_compilation_attendu"]:',
     '    if res.get("incident_bac") != cas["incident_compilation_attendu"]:'),
    ("e804", "incident de compilation attendu non admis par _noter", E7,
     '(cas.get("incident_attendu") or cas.get("incident_compilation_attendu"))', 'cas.get("incident_attendu")'),
    # --- neuves : signal d'un chemin de cgroupe faux
    ("e805", "signal : durée minimale ignorée", E7,
     '        if (t.get("duree_service_s") or 0) >= DUREE_MIN_RELEVE_S and n == 0:', '        if n == 0:'),
    ("e806", "signal : pics rapportés malgré un chemin faux", E7,
     '"pics_rapportes_octets": {} if sans else pics}', '"pics_rapportes_octets": pics}'),
    ("e807", "signal : pic rapporté sur moins de trois relevés", E7,
     'if n >= ECHANTILLONS_MIN else None', 'if n >= 1 else None'),
    ("e808", "signal : chemin jamais déclaré faux", E7, "            sans.append(nom)", "            pass"),
    ("e820", "bloc mémoire absent de la sortie de l'épreuve", E7,
     '"conforme": conforme, "memoire": memoire}', '"conforme": conforme}'),
    # --- neuves : mémoire de la machine entière
    ("e809", "recoupement par /proc/meminfo retiré", E7,
     "        if baisse > pic + TOLERANCE_RECOUPEMENT_OCTETS:", "        if False:"),
    ("e810", "estimation prudente sans le pic de la tranche", E7,
     "        prudente = avant - max(baisse, pic)", "        prudente = avant - baisse"),
    ("e811", "seuil du pic de la tranche relâché", E7, "SEUIL_PIC_TRANCHE = 0.5", "SEUIL_PIC_TRANCHE = 0.6"),
    ("e812", "pic de la tranche admis sur moins de trois relevés", E7,
     '    if pic is None or m.get("pic_tranche_echantillons", 0) < ECHANTILLONS_MIN:', '    if pic is None:'),
    ("e813", "chemin faux ignoré par le compte du parallèle", E7,
     '    if signal.get("chemin_cgroupe_faux"):', '    if False:'),
    ("e814", "incident d'un passage parallèle ignoré", E7, '        if p.get("incident_bac"):', '        if False:'),
    ("e815", "passages parallèles hors de la tranche réservée", E7,
     "    bac_p = X.Bac(replace(cfg, tranche=tranche))", "    bac_p = X.Bac(cfg)"),
    ("e816", "relevé de la machine sur une autre tranche", E7,
     '    with ReleveMachine(cfg.racine_cgroup / tranche / "memory.peak", meminfo) as releve:',
     '    with ReleveMachine(cfg.racine_cgroup / "system.slice" / "memory.peak", meminfo) as releve:'),
    ("e817", "mémoire disponible : plus haut au lieu du plus bas", E7,
     "(dispo if self.dispo_min is None else min(self.dispo_min, dispo))",
     "(dispo if self.dispo_min is None else max(self.dispo_min, dispo))"),
    ("e818", "pic de la tranche : dernier relevé au lieu du plus haut", E7,
     "self.pic, self.n_pic = (v if self.pic is None else max(self.pic, v)), self.n_pic + 1",
     "self.pic, self.n_pic = v, self.n_pic + 1"),
    ("e819", "/proc/meminfo lu sans le facteur des kB", E7,
     '(1024 if morceaux[1:2] == ["kB"] else 1)', '1'),
    ("e821", "témoin sain non exigé", E7, "        if not any(c.get(\"sain\") for c in attendus[groupe]):",
     "        if False:"),
    ("e822", "incident de la compilation absent du JSON du cas Lean de mémoire", E7,
     'dict(extrait_sonde(res), incident_compilation=res.get("incident_compilation"),',
     'dict(extrait_sonde(res), incident_compilation=None,'),
    # --- attendus v7 et pilote v12
    ("a801", "cas Lean de mémoire attendu en « exit-code »", A6,
     '"resultat_compilation_attendu": "oom-kill"', '"resultat_compilation_attendu": "exit-code"'),
    ("p801", "pilote : épreuve v7 copiée", P11, '"$PAQ/epreuve_isolement_v8.py"', '"$PAQ/epreuve_isolement_v7.py"'),
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
    p = subprocess.run([sys.executable, "-B", "-c", "import controle_ia.lean_essai.executeur_bac_v8 as X; print(X.__file__)"],
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
    print(json.dumps({"version": "mutations_gardes_v12", "chaine": bool(os.environ.get("LEAN_ESSAI_D1A_CHAINE")),
                      "mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "detail": resultats}, ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())

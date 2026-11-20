#!/usr/bin/env python3
"""Contrôle du registre propre candidat avant de commettre la ligne de relance (barreau 5, additif 1, section 5).

La ligne `GO-RELANCE-FORMATION-B5F` ne se réécrit pas et ne se double pas : le fichier du registre candidat (registre de
la branche principale, plus la ligne telle qu'elle sera commise) est lu ici TEL QUEL, par les deux codes qui le liront :
- `formation_v1.lire_code_et_accord` du code des relances (arbre au commit d116bf78…) ;
- `lecture_v1.relance_du_registre` du code de lecture figé à `CODE-LECTURE-B5F` (arbre au commit c76e7916…).
Chaque lecture se fait dans un sous-processus à part, avec son propre PYTHONPATH (le `src` de son arbre) ; le
sous-processus prouve qu'il a chargé le module de son arbre, et l'empreinte des fichiers lus est comparée à celle
attendue. Ce programme ne lit rien d'autre, n'écrit rien, n'appelle ni le loueur ni le réseau.

Usage : python controler_registre_candidat_v1.py REGISTRE_CANDIDAT ARBRE_CODE_DES_RELANCES ARBRE_CODE_DE_LECTURE_FIGE
Sortie : « registre candidat ACCEPTÉ » et code 0 ; sinon « registre candidat REFUSÉ : <raison> » et code 1.

Exigé : instances [1, 2, 3, 4, 5, 7] des deux côtés ; accord GO-2026-11-19-86 ; commit du code des relances
d116bf78bb2084b2d4f406535a6c6f0a23179efe ; le commit des premières marches et l'entropie sont lus et rendus."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

INSTANCES = [1, 2, 3, 4, 5, 7]
ACCORD = "GO-2026-11-19-86"
CODE_DES_RELANCES = "d116bf78bb2084b2d4f406535a6c6f0a23179efe"
PAQUET = "src/controle_ia/barreau5_familles"
# empreintes des fichiers lus : formation_v1.py au commit d116bf78… ; lecture_v1.py au commit de CODE-LECTURE-B5F (celle
# que citent les lignes CODE-LECTURE-B5F et EPREUVE-B5F) ; engagement_v1.py, le même fichier des deux côtés
SHA_FORMATION = "1f3e67c31ae17a0c77259ac8067f635ffd94df6d497c595e2cbf50f73b647d3b"
SHA_LECTURE = "ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f"
SHA_ENGAGEMENT = "565d4e51eccd82562f3f00e7bd020beba525ac09b782905151a38e72ca536396"
DELAI_S = 300

# code joué dans chaque sous-processus : lit le fichier candidat tel quel, rend un objet JSON sur la dernière ligne
LIRE_PAR_LES_RELANCES = r"""
import json, sys
from pathlib import Path
from controle_ia.barreau5_familles import formation_v1 as m
lu = m.lire_code_et_accord(Path(sys.argv[1]))
print(json.dumps({"module": m.__file__, "relance": lu["relance"], "commit": lu["commit"], "entropie": str(lu["entropie"]),
                  "go_id": lu["go_id"]}))
"""
LIRE_PAR_LA_LECTURE = r"""
import json, sys
from pathlib import Path
from controle_ia.barreau5_familles import lecture_v1 as m
print(json.dumps({"module": m.__file__, "relance": m.relance_du_registre(Path(sys.argv[1]).read_text(encoding="utf-8"))}))
"""


class Refus(Exception):
    pass


def _sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def _exiger_fichier(arbre: Path, nom: str, attendu: str, quoi: str) -> None:
    f = arbre / PAQUET / nom
    if not f.is_file():
        raise Refus(f"{quoi} : {f} absent (l'arbre donné n'est pas le bon)")
    if _sha(f) != attendu:
        raise Refus(f"{quoi} : {nom} a l'empreinte {_sha(f)[:16]}…, {attendu[:16]}… attendue (l'arbre n'est pas au bon commit)")


def _lire(arbre: Path, code: str, registre: Path, quoi: str) -> dict:
    """Joue `code` dans un sous-processus isolé : PYTHONPATH = le `src` de l'arbre, et lui seul ; répertoire courant
    neutre ; aucun fichier de cache écrit."""
    env = {"PYTHONPATH": str(arbre / "src"), "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1",
           "PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C.UTF-8", "PYTHONIOENCODING": "utf-8"}
    try:
        p = subprocess.run([sys.executable, "-B", "-c", code, str(registre)], capture_output=True, text=True, env=env,
                           cwd="/", timeout=DELAI_S)
    except subprocess.TimeoutExpired:
        raise Refus(f"{quoi} : lecture sans réponse après {DELAI_S} s") from None
    if p.returncode != 0:
        derniere = (p.stderr.strip().splitlines() or ["aucun message"])[-1]
        raise Refus(f"{quoi} : le registre est refusé : {derniere}")
    try:
        rendu = json.loads(p.stdout.strip().splitlines()[-1])
    except (IndexError, ValueError):
        raise Refus(f"{quoi} : sortie illisible") from None
    module = Path(rendu["module"]).resolve()
    if (arbre / "src").resolve() not in module.parents:
        raise Refus(f"{quoi} : module chargé hors de l'arbre donné ({module})")
    return rendu


def controler(registre: Path, relances: Path, lecture: Path) -> dict:
    if not registre.is_file():
        raise Refus(f"registre candidat {registre} absent")
    for arbre, quoi in ((relances, "arbre du code des relances"), (lecture, "arbre du code de lecture figé")):
        if not (arbre / "src").is_dir():
            raise Refus(f"{quoi} : {arbre}/src absent")
    if relances.resolve() == lecture.resolve():
        raise Refus("les deux arbres sont le même : deux codes distincts attendus")
    _exiger_fichier(relances, "formation_v1.py", SHA_FORMATION, "code des relances")
    _exiger_fichier(relances, "engagement_v1.py", SHA_ENGAGEMENT, "code des relances")
    _exiger_fichier(lecture, "lecture_v1.py", SHA_LECTURE, "code de lecture figé")
    _exiger_fichier(lecture, "engagement_v1.py", SHA_ENGAGEMENT, "code de lecture figé")
    avant = _sha(registre)
    f = _lire(relances, LIRE_PAR_LES_RELANCES, registre, "code des relances (formation_v1.lire_code_et_accord)")
    r = f["relance"]
    if r is None:
        raise Refus("code des relances : aucune ligne GO-RELANCE-FORMATION-B5F dans le registre candidat")
    if r["instances"] != INSTANCES:
        raise Refus(f"code des relances : instances {r['instances']}, {INSTANCES} attendues")
    if r["go_id"] != ACCORD or f["go_id"] != ACCORD:
        raise Refus(f"code des relances : accord {r['go_id']} (formation : {f['go_id']}), {ACCORD} attendu")
    if r["commit"] != CODE_DES_RELANCES:
        raise Refus(f"code des relances : commit du code des relances {r['commit']}, {CODE_DES_RELANCES} attendu")
    if f["commit"] == r["commit"] or len(f["commit"]) != 40 or not f["entropie"].isdigit() or int(f["entropie"]) <= 0:
        raise Refus("code des relances : commit des premières marches ou entropie illisibles")
    lu = _lire(lecture, LIRE_PAR_LA_LECTURE, registre, "code de lecture figé (lecture_v1.relance_du_registre)")
    if lu["relance"] != INSTANCES:
        raise Refus(f"code de lecture figé : relance {lu['relance']}, {INSTANCES} attendues")
    if _sha(registre) != avant:
        raise Refus("le registre candidat a changé pendant le contrôle")
    return {"registre_sha256": avant, "instances": r["instances"], "accord": r["go_id"], "code_des_relances": r["commit"],
            "code_des_premieres_marches": f["commit"], "entropie": f["entropie"], "instances_lues_par_la_lecture": lu["relance"]}


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage : controler_registre_candidat_v1.py REGISTRE_CANDIDAT ARBRE_CODE_DES_RELANCES "
              "ARBRE_CODE_DE_LECTURE_FIGE", file=sys.stderr)
        print("registre candidat REFUSÉ : trois arguments attendus")
        return 1
    try:
        vu = controler(*(Path(a) for a in argv))
    except Refus as e:
        print(f"registre candidat REFUSÉ : {e}")
        return 1
    except Exception as e:                                   # aucune acceptation sur une erreur imprévue
        print(f"registre candidat REFUSÉ : erreur imprévue du contrôle ({type(e).__name__} : {e})")
        return 1
    print(f"registre candidat lu tel quel : sha256 {vu['registre_sha256']}")
    print(f"code des relances : instances {vu['instances']} ; accord {vu['accord']} ; code des relances commit "
          f"{vu['code_des_relances']}")
    print(f"code des premières marches (CODE-FORMATION-B5F) : commit {vu['code_des_premieres_marches']} ; entropie "
          f"{vu['entropie']}")
    print(f"code de lecture figé : instances {vu['instances_lues_par_la_lecture']}")
    print("registre candidat ACCEPTÉ")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Essai de raccord du programme de lecture et de la fabrique des mondes (barreau 5) — v1.

Mandat `mandat-essai-raccord-v1.md` (`46390c9a…`). Ce n'est pas l'épreuve à vérité plantée : un petit nombre de mondes,
sous une entropie tirée pour cet essai seul ; aucune règle du point 11 n'est jugée, aucun taux n'est calculé, aucune
vérité n'est engagée. Aucune donnée.

Pour chaque monde, dans cet ordre, chaque pièce par sa ligne de commande (rien du programme de lecture n'est importé) :
1. la fabrique (`epreuve_verite_plantee_v1 monde`) écrit le monde sous `<tmp>/mondes/<monde>` ;
2. le programme de lecture (`lecture_v1 monde`, sans `--racine`, comme le disent son en-tête et la section 5 de la
   contre-lecture de la fabrique) ; code de sortie, sortie d'erreur, résultat s'il existe ;
3. le comparateur de la seconde programmation (`seconde_programmation_v3 comparer CODE [RESULTAT] [--refus-attendu]`),
   `--refus-attendu` pour les seuls mondes dont l'identifiant est un cas de refus de V7 (rien n'est lu des vérités) ;
4. le traducteur (`traducteur_verite_plantee_v1 … --accord`), qui ajoute une ligne aux rendus.
Puis un fichier de vérités réduit aux seuls mondes de l'essai (mêmes champs que `ecrire_verites`, fonctions `planter` et
`verite` de la fabrique ; il n'est ni engagé ni lu par cet outil au-delà de son empreinte), et le juge sur ces rendus.
Enfin, du juge, le contrôle de forme de chaque rendu (`erreurs_rendu`) et, pour les cas de refus de V7, le fragment de
motif qu'il attend (`v7_refus`, confronté au seul cas tiré de l'identifiant).

Usage : `PYTHONPATH=src .venv/bin/python -B <ce fichier> --entropie N --tmp /dev/shm/b5f-raccord-v1 --resume <json>`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
PY = str(DEPOT / ".venv" / "bin" / "python")
LECTURE = DEPOT / "src" / "controle_ia" / "barreau5_familles" / "lecture_v1.py"
LECTURE_SHA256 = "ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f"

sys.path.insert(0, str(DEPOT / "src"))
from controle_ia.barreau5_familles import epreuve_verite_plantee_v1 as fab  # noqa: E402
from controle_ia.barreau5_familles import juge_verite_plantee_v1 as juge  # noqa: E402

# Un monde sain de chacune des classes V0 à V12 (hors V7) ; les neuf mondes de V7 (les six refus plantés des quatre
# premiers cas, et les trois mondes sains des cas 5 et 6) ; deux mondes où les coûts d'une tâche sont illisibles chez un
# seul membre (VC2, VC3 : addendum 1, point 2).
MONDES = (["V0-0000", "V1-0000", "V2-0000", "V3-0000", "V4-0000", "V5-0000", "V6-0000"]
          + [f"V7-{i:04d}" for i in range(len(fab.CAS_V7))]
          + ["V8-0000", "V9-0000", "V10-0000", "V11-0000", "V12-0000", "VC2-0000", "VC3-0000"])


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cas_de(monde: str):
    g, i = fab.analyser(monde)
    return fab.CAS_V7[i][0] if g == "V7" else None


def lancer(args, sortie_std: Path, sortie_err: Path) -> int:
    env = dict(os.environ, PYTHONPATH=str(DEPOT / "src"), PYTHONDONTWRITEBYTECODE="1")
    with open(sortie_std, "xb") as o, open(sortie_err, "xb") as e:
        return subprocess.run([PY, "-B", *args], cwd=str(DEPOT), env=env, stdout=o, stderr=e).returncode


def derniere_ligne(p: Path) -> str:
    lignes = [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    return lignes[-1] if lignes else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entropie", type=int, required=True)
    ap.add_argument("--tmp", required=True)
    ap.add_argument("--resume", required=True)
    a = ap.parse_args()
    tmp = Path(a.tmp)
    if sha(LECTURE) != LECTURE_SHA256:
        print("programme de lecture d'une autre empreinte que celle du mandat : arrêt", file=sys.stderr)
        return 4
    tmp.mkdir(parents=True)
    params_f = tmp / "parametres.json"
    # seul paramètre réglé : l'empreinte du programme joué (contre-lecture de la fabrique, section 9, point 3)
    params_f.write_text(json.dumps({"empreinte_lecture": LECTURE_SHA256}), encoding="utf-8")
    params = fab.Parametres.depuis_fichier(params_f)
    rendus_f = tmp / "rendus.jsonl"
    rendus_f.touch()
    lignes = []
    for m in MONDES:
        cas = cas_de(m)
        artefact = cas in fab.REFUS_V7
        d = tmp / "mondes" / m
        j = tmp / "journaux" / m
        j.mkdir(parents=True)
        ligne = {"monde": m, "cas_V7": cas, "artefact": artefact}
        ligne["fabrique_code"] = lancer(["-m", "controle_ia.barreau5_familles.epreuve_verite_plantee_v1", "monde",
                                         "--entropie", str(a.entropie), "--monde", m, "--dossier", str(d),
                                         "--parametres", str(params_f)], j / "fabrique.out", j / "fabrique.err")
        if ligne["fabrique_code"] != 0:
            ligne["fabrique_erreur"] = derniere_ligne(j / "fabrique.err")
            lignes.append(ligne)
            continue
        sortie = tmp / "lectures" / m
        code = lancer(["-m", "controle_ia.barreau5_familles.lecture_v1", "monde", "--registre", str(d / "registre.txt"),
                       "--arbre", str(d / "arbre"), "--table", str(d / "etiquettes.json"), "--couts",
                       str(d / "couts.json"), "--formation", str(d / "formation-resume.json"), "--sortie", str(sortie)],
                      j / "lecture.out", j / "lecture.err")
        res = sortie / "resultat-lecture-b5f.json"
        ligne["lecture_code"] = code
        ligne["resultat_ecrit"] = res.exists()
        ligne["lecture_derniere_ligne_erreur"] = derniere_ligne(j / "lecture.err")
        if res.exists():
            r = json.loads(res.read_text(encoding="utf-8"))
            g = r.get("g_issue") or {}
            ligne["issue_ecrite"] = {"code": g.get("code"), "niveau": g.get("niveau"), "motifs": g.get("motifs")}
            ligne["resultat_sha256"] = sha(res)
        comp = ["-m", "controle_ia.barreau5_familles.seconde_programmation_v3", "comparer", str(code)]
        if res.exists():
            comp.append(str(res))
        if artefact:
            comp.append("--refus-attendu")
        ligne["comparateur_code"] = lancer(comp, j / "accord.json", j / "accord.err")
        try:
            acc = json.loads((j / "accord.json").read_text(encoding="utf-8"))
            ligne["accord"] = {"verdict": acc["verdict"], "arret_par_une_garde": acc["arret_par_une_garde"],
                               "champs_manquants": acc["champs_manquants"], "desaccords": acc["desaccords"]}
        except (ValueError, KeyError) as e:
            ligne["accord"] = {"illisible": str(e)}
        trad = ["-m", "controle_ia.barreau5_familles.traducteur_verite_plantee_v1", "--monde", m, "--code", str(code),
                "--stderr", str(j / "lecture.err"), "--accord", str(j / "accord.json"), "--rendus", str(rendus_f)]
        if res.exists():
            trad += ["--resultat", str(res)]
        ligne["traducteur_code"] = lancer(trad, j / "traducteur.out", j / "traducteur.err")
        if ligne["traducteur_code"] != 0:
            ligne["traducteur_erreur"] = derniere_ligne(j / "traducteur.err")
        lignes.append(ligne)

    # vérités réduites aux mondes de l'essai (mêmes champs que `ecrire_verites`), pour que le juge lise ces seuls mondes
    doc = {"format": fab.FORMAT_VERITES, "entropie": a.entropie, "cle": fab.CLE_EPREUVE,
           "fabrique": {"module": "controle_ia.barreau5_familles.epreuve_verite_plantee_v1",
                        "sha256": sha(Path(fab.__file__))},
           "parametres": params.en_dict(), "reduit_a_l_essai_de_raccord": True,
           "nombres": {g: fab.nombre(g) for g in fab.GROUPES}, "cas_V7": [list(c) for c in fab.CAS_V7],
           "mondes": [fab.verite(fab.planter(a.entropie, m, params)) for m in MONDES]}
    ver_f = tmp / "verites-essai-raccord.json"
    ver_f.write_bytes(json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    ver_sha = sha(ver_f)
    verdict_f = tmp / "verdict-juge.json"
    juge_code = lancer(["-m", "controle_ia.barreau5_familles.juge_verite_plantee_v1", "--verites", str(ver_f),
                        "--empreinte", ver_sha, "--rendus", str(rendus_f), "--sortie", str(verdict_f)],
                       tmp / "juge.out", tmp / "juge.err")
    rendus = juge.lire_rendus(rendus_f)
    for ligne in lignes:
        r = rendus.get(ligne["monde"])
        ligne["rendu_present"] = r is not None
        if r is None:
            continue
        ligne["juge_erreurs_de_forme"] = juge.erreurs_rendu(r)
        ligne["rendu_refus"] = r.get("refus")
        ligne["rendu_motif_refus"] = r.get("motif_refus")
        ligne["rendu_seconde_programmation"] = r.get("seconde_programmation")
        if ligne["artefact"]:
            ligne["juge_fragment_attendu"] = juge.FRAGMENTS_REFUS_V7.get(ligne["cas_V7"])
            ligne["juge_v7_refus_au_bon_motif"] = juge.v7_refus(r, {"motif_refus": ligne["cas_V7"]})
    resume = {"entropie": a.entropie, "lecture_sha256": LECTURE_SHA256, "parametres": {"empreinte_lecture": LECTURE_SHA256},
              "mondes": lignes, "verites_reduites_sha256": ver_sha, "juge_code": juge_code,
              "juge_sortie": (tmp / "juge.out").read_text(encoding="utf-8"),
              "juge_erreur": (tmp / "juge.err").read_text(encoding="utf-8")}
    if verdict_f.exists():
        v = json.loads(verdict_f.read_text(encoding="utf-8"))
        resume["juge_regles"] = v["regles"]
        resume["juge_V7_motifs_de_refus"] = v["descriptifs"].get("V7_motifs_de_refus")
    with open(a.resume, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(resume, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"mondes": len(lignes), "juge_code": juge_code}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

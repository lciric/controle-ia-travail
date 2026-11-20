"""Joueur de l'épreuve à vérité plantée du programme de lecture (barreau 5), passage par lots — v1.

Mandats : `mandats-epreuve-verite-plantee-v1.md` (`2dce334d…`), rôle 2, et son complément 1 par lots (`9ea1c75a…`),
section 3. Rien n'est lu sous `<base>/verites/` ni dans `<base>/journaux/` (journal du tireur).

Pour chaque lot k, dans l'ordre :
- attendre `<base>/temoins/lot-k.pret`, puis vérifier l'inventaire du lot contre les fichiers ;
- pour chaque monde du lot, comme l'essai de raccord (`outils-essai-raccord-v1/essai_raccord_v1.py`) : le programme de
  lecture figé (`lecture_v1 monde`, sans `--racine`), le comparateur de la seconde programmation v3 (`--refus-attendu`
  pour les seuls mondes dont l'identifiant est un des quatre premiers cas de V7, d'après la table `CAS_V7` de la
  fabrique ; rien n'est lu des vérités), puis le traducteur avec `--accord` ;
- les rendus sous `<base>/rendus/lot-k/` ; puis le témoin `<base>/temoins/lot-k.joue`.
À la fin : l'inventaire général des rendus et son empreinte. Aucun taux, aucune règle jugée.

Usage : `PYTHONPATH=src .venv/bin/python -B <ce fichier> --base /dev/shm/b5f-epreuve-v1 --journal <fichier>`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
PY = str(DEPOT / ".venv" / "bin" / "python")
LECTURE = DEPOT / "src" / "controle_ia" / "barreau5_familles" / "lecture_v1.py"
LECTURE_SHA256 = "ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f"

sys.path.insert(0, str(DEPOT / "src"))
from controle_ia.barreau5_familles import epreuve_verite_plantee_v1 as fab  # noqa: E402

JOURNAL = None
VERROU = threading.Lock()


def journal(msg: str) -> None:
    ligne = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
    with VERROU, open(JOURNAL, "a", encoding="utf-8") as fh:
        fh.write(ligne + "\n")


def sha_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def cas_de(monde: str):
    g, i = fab.analyser(monde)
    return fab.CAS_V7[i][0] if g == "V7" else None


def lancer(args, sortie_std: Path, sortie_err: Path) -> int:
    env = dict(os.environ, PYTHONPATH=str(DEPOT / "src"), PYTHONDONTWRITEBYTECODE="1")
    with open(sortie_std, "xb") as o, open(sortie_err, "xb") as e:
        return subprocess.run([PY, "-B", *args], cwd=str(DEPOT), env=env, stdout=o, stderr=e).returncode


def derniere_ligne(p: Path) -> str:
    lignes = [x for x in p.read_text(encoding="utf-8", errors="replace").splitlines() if x.strip()]
    return lignes[-1] if lignes else ""


class Arret(Exception):
    pass


# ------------------------------------------------------------------------------------------ inventaire d'un lot

TEMOIN_PRET = re.compile(r"^lot (\d+) ; (\d+) mondes ; inventaire sha256 ([0-9a-f]{64})\s*$")


def lire_inventaire_lot(base: Path, k: int) -> list[str]:
    """Rend la liste ordonnée des mondes du lot k, après vérification de l'inventaire contre les fichiers.

    Témoin `<base>/temoins/lot-k.pret` : « lot k ; N mondes ; inventaire sha256 <64> ». Inventaire
    `<base>/inventaires/inventaire-lot-k.txt` : une ligne « <sha256>  <monde>/<chemin> » par fichier, chemins relatifs
    à `<base>/mondes/lot-k/`. Vérifié : empreinte de l'inventaire égale à celle du témoin ; chaque fichier présent et de
    l'empreinte inscrite ; aucun fichier du lot hors de l'inventaire ; nombre de mondes égal à celui du témoin ;
    chaque monde a les fichiers que lit le programme."""
    texte = (base / "temoins" / f"lot-{k}.pret").read_text(encoding="utf-8")
    t = TEMOIN_PRET.match(texte.strip())
    if not t or int(t.group(1)) != k:
        raise Arret(f"lot {k} : témoin prêt illisible : {texte!r}")
    n_annonce, sha_annonce = int(t.group(2)), t.group(3)
    inv_f = base / "inventaires" / f"inventaire-lot-{k}.txt"
    inv_octets = inv_f.read_bytes()
    if sha_octets(inv_octets) != sha_annonce:
        raise Arret(f"lot {k} : inventaire d'empreinte {sha_octets(inv_octets)} ≠ témoin {sha_annonce}")
    dossier = base / "mondes" / f"lot-{k}"
    inscrits = {}
    mondes = []
    for i, ligne in enumerate(inv_octets.decode("utf-8").splitlines()):
        if not ligne.strip():
            continue
        if len(ligne) < 67 or ligne[64:66] != "  " or not re.fullmatch(r"[0-9a-f]{64}", ligne[:64]):
            raise Arret(f"lot {k} : ligne {i + 1} de l'inventaire illisible")
        chemin = ligne[66:]
        if chemin in inscrits or chemin.startswith("/") or ".." in Path(chemin).parts:
            raise Arret(f"lot {k} : chemin d'inventaire refusé ou en double : {chemin}")
        inscrits[chemin] = ligne[:64]
        m = Path(chemin).parts[0]
        if not mondes or mondes[-1] != m:
            if m in mondes:
                raise Arret(f"lot {k} : monde {m} non contigu dans l'inventaire")
            mondes.append(m)
    presents = {str(p.relative_to(dossier)) for p in dossier.rglob("*") if p.is_file() or p.is_symlink()}
    if presents != set(inscrits):
        manque = sorted(set(inscrits) - presents)[:3]
        hors = sorted(presents - set(inscrits))[:3]
        raise Arret(f"lot {k} : fichiers ≠ inventaire (absents {manque} ; hors inventaire {hors})")
    for chemin, s in inscrits.items():
        p = dossier / chemin
        if p.is_symlink() or sha(p) != s:
            raise Arret(f"lot {k} : {chemin} : empreinte différente de l'inventaire (ou lien)")
    if len(mondes) != n_annonce:
        raise Arret(f"lot {k} : {len(mondes)} mondes à l'inventaire ≠ {n_annonce} au témoin")
    for m in mondes:
        fab.analyser(m)
        for f in ("registre.txt", "etiquettes.json", "couts.json", "formation-resume.json"):
            if f"{m}/{f}" not in inscrits:
                raise Arret(f"lot {k} : {m} sans {f}")
    return mondes


# ------------------------------------------------------------------------------------------ un monde

def jouer_monde(dossier_monde: Path, sortie_lot: Path, monde: str) -> dict:
    cas = cas_de(monde)
    artefact = cas in fab.REFUS_V7
    j = sortie_lot / "mondes" / monde
    j.mkdir(parents=True)
    ligne = {"monde": monde, "cas_V7": cas, "refus_attendu_passe": artefact}
    sortie = j / "lecture"
    t0 = time.monotonic()
    d = dossier_monde
    code = lancer(["-m", "controle_ia.barreau5_familles.lecture_v1", "monde", "--registre", str(d / "registre.txt"),
                   "--arbre", str(d / "arbre"), "--table", str(d / "etiquettes.json"), "--couts",
                   str(d / "couts.json"), "--formation", str(d / "formation-resume.json"), "--sortie", str(sortie)],
                  j / "lecture.out", j / "lecture.err")
    ligne["duree_lecture_s"] = round(time.monotonic() - t0, 2)
    res = sortie / "resultat-lecture-b5f.json"
    ligne["lecture_code"] = code
    ligne["resultat_ecrit"] = res.exists()
    ligne["plantage"] = code not in (0, 2)
    ligne["lecture_derniere_ligne_erreur"] = derniere_ligne(j / "lecture.err")
    if res.exists():
        ligne["resultat_sha256"] = sha(res)
    comp = ["-m", "controle_ia.barreau5_familles.seconde_programmation_v3", "comparer", str(code)]
    if res.exists():
        comp.append(str(res))
    if artefact:
        comp.append("--refus-attendu")
    ligne["comparateur_code"] = lancer(comp, j / "accord.json", j / "accord.err")
    rendu_f = j / "rendu.jsonl"
    rendu_f.touch()
    trad = ["-m", "controle_ia.barreau5_familles.traducteur_verite_plantee_v1", "--monde", monde, "--code", str(code),
            "--stderr", str(j / "lecture.err"), "--accord", str(j / "accord.json"), "--rendus", str(rendu_f)]
    if res.exists():
        trad += ["--resultat", str(res)]
    ligne["traducteur_code"] = lancer(trad, j / "traducteur.out", j / "traducteur.err")
    if ligne["traducteur_code"] != 0:
        ligne["traducteur_erreur"] = derniere_ligne(j / "traducteur.err")
    ligne["rendu_lignes"] = len([x for x in rendu_f.read_text(encoding="utf-8").splitlines() if x.strip()])
    journal(f"monde {monde} : lecture {code} ({ligne['duree_lecture_s']} s) ; comparateur {ligne['comparateur_code']} ; "
            f"traducteur {ligne['traducteur_code']}")
    return ligne


# ------------------------------------------------------------------------------------------ inventaires des rendus

def inventaire_dossier(racine: Path, exclure: set[Path]) -> list[dict]:
    fichiers = []
    for p in sorted(racine.rglob("*")):
        if p.is_file() and p not in exclure:
            fichiers.append({"chemin": str(p.relative_to(racine)), "octets": p.stat().st_size, "sha256": sha(p)})
    return fichiers


def ecrire_scelle(p: Path, octets: bytes) -> str:
    with open(p, "xb") as fh:
        fh.write(octets)
    s = sha_octets(octets)
    with open(p.with_name(p.name + ".sha256"), "x", encoding="utf-8") as fh:
        fh.write(f"{s}  {p.name}\n")
    return s


def jouer_lot(base: Path, k: int, travailleurs: int, joues: set[str]) -> dict:
    mondes = lire_inventaire_lot(base, k)
    for m in mondes:
        if m in joues:
            raise Arret(f"lot {k} : monde {m} déjà joué dans un lot précédent")
    sortie_lot = base / "rendus" / f"lot-{k}"
    sortie_lot.mkdir(parents=True)
    dossier_lot = base / "mondes" / f"lot-{k}"
    journal(f"lot {k} : {len(mondes)} mondes, inventaire vérifié ; début du jeu")
    with ThreadPoolExecutor(max_workers=travailleurs) as ex:
        lignes = list(ex.map(lambda m: jouer_monde(dossier_lot / m, sortie_lot, m), mondes))
    # rendus du lot, dans l'ordre de l'inventaire
    rendus = b"".join((sortie_lot / "mondes" / m / "rendu.jsonl").read_bytes() for m in mondes)
    with open(sortie_lot / "rendus.jsonl", "xb") as fh:
        fh.write(rendus)
    with open(sortie_lot / "lignes.jsonl", "x", encoding="utf-8") as fh:
        for ligne in lignes:
            fh.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    plantages = sum(1 for x in lignes if x["plantage"])
    codes = {}
    for x in lignes:
        codes[str(x["lecture_code"])] = codes.get(str(x["lecture_code"]), 0) + 1
    trad_pannes = sum(1 for x in lignes if x["traducteur_code"] != 0)
    inv = {"format": "b5f-epreuve-inventaire-rendus-lot-v1", "lot": k, "mondes": len(mondes),
           "codes_de_sortie_lecture": codes, "plantages": plantages, "traducteur_non_zero": trad_pannes,
           "fichiers": inventaire_dossier(sortie_lot, set())}
    s = ecrire_scelle(sortie_lot / f"inventaire-rendus-lot-{k}.json",
                      json.dumps(inv, ensure_ascii=False, indent=1).encode("utf-8"))
    for m in mondes:
        joues.add(m)
    temoin = base / "temoins" / f"lot-{k}.joue"
    with open(temoin, "x", encoding="utf-8") as fh:
        fh.write(json.dumps({"lot": k, "mondes": len(mondes), "inventaire_rendus_lot_sha256": s,
                             "ecrit": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, ensure_ascii=False) + "\n")
    journal(f"lot {k} joué : {len(mondes)} mondes ; codes {codes} ; plantages {plantages} ; "
            f"traducteur non nul {trad_pannes} ; inventaire du lot {s} ; témoin écrit")
    return {"lot": k, "mondes": len(mondes), "plantages": plantages, "codes": codes, "traducteur_non_zero": trad_pannes,
            "inventaire_rendus_lot_sha256": s}


def main() -> int:
    global JOURNAL
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--journal", required=True)
    ap.add_argument("--travailleurs", type=int, default=2)
    ap.add_argument("--attente-max-s", type=int, default=4 * 3600)
    a = ap.parse_args()
    JOURNAL = a.journal
    base = Path(a.base)
    if sha(LECTURE) != LECTURE_SHA256:
        journal("programme de lecture d'une autre empreinte que celle du mandat : arrêt")
        return 4
    attendus = set(fab.liste_mondes())
    journal(f"début ; programme de lecture {LECTURE_SHA256} ; {len(attendus)} mondes attendus ; "
            f"{a.travailleurs} travailleurs")
    (base / "rendus").mkdir(exist_ok=False)
    joues: set[str] = set()
    bilans = []
    k = 0
    try:
        while joues != attendus:
            pret = base / "temoins" / f"lot-{k}.pret"
            t0 = time.monotonic()
            while not pret.exists():
                if time.monotonic() - t0 > a.attente_max_s:
                    raise Arret(f"lot {k} : témoin prêt absent après {a.attente_max_s} s")
                time.sleep(15)
            bilans.append(jouer_lot(base, k, a.travailleurs, joues))
            inconnus = joues - attendus
            if inconnus:
                raise Arret(f"mondes hors de la liste de la fabrique : {sorted(inconnus)[:5]}")
            k += 1
    except Arret as e:
        journal(f"ARRÊT : {e}")
        return 5
    except Exception as e:  # aucun repli silencieux : toute panne du joueur l'arrête et s'écrit
        journal(f"ARRÊT (panne du joueur) : {type(e).__name__} : {e}")
        return 6
    rendus_racine = base / "rendus"
    tous = b"".join((rendus_racine / f"lot-{b['lot']}" / "rendus.jsonl").read_bytes() for b in bilans)
    s_tous = ecrire_scelle(rendus_racine / "rendus-epreuve-v1.jsonl", tous)
    inv_f = rendus_racine / "inventaire-general-rendus-epreuve-v1.json"
    inv = {"format": "b5f-epreuve-inventaire-general-rendus-v1", "lecture_sha256": LECTURE_SHA256,
           "mondes_joues": len(joues), "plantages": sum(b["plantages"] for b in bilans),
           "lots": bilans, "rendus_concatenes_sha256": s_tous,
           "fichiers": inventaire_dossier(rendus_racine, {inv_f, inv_f.with_name(inv_f.name + ".sha256")})}
    s = ecrire_scelle(inv_f, json.dumps(inv, ensure_ascii=False, indent=1).encode("utf-8"))
    journal(f"FIN : {len(joues)} mondes joués ; plantages {inv['plantages']} ; inventaire général {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

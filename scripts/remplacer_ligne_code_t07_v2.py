#!/usr/bin/env python3
"""Remplacement, une seule fois, de la ligne `CODE-T07` du registre des scellements — v2 (fichier neuf, R12 ; la v1,
`scripts/remplacer_ligne_code_t07_v1.py`, `a89e2226…`, reste telle quelle).

**v2 = v1 + m-6 de la contre-lecture des pièces de relance** (`relance-v2-preparation-v1/contre-lecture-relance-v2-v1.md`,
`703195e5…`) : la trace est **écrite et scellée avant** le remplacement ; si elle ne peut pas s'écrire, refus et **rien n'est
remplacé** ; si le remplacement échoue après elle, la trace et son compagnon sont retirés et le registre reste tel quel (refus) ;
une relecture différente après le remplacement est un refus « nœud » (la trace reste : elle dit l'état attendu). Tout le reste
(contrôles (1) à (6), format, commandes) est celui de la v1.

Décision : R-2604 (1) (mot de Lazar « go recos », option (a)) : la ligne `CODE-T07` de `registres/scellements-v1.md` est
**remplacée une seule fois**, par un script éprouvé qui vérifie l'ancienne ligne à l'octet ; l'ancienne ligne est recopiée dans
l'addendum de T0.7 ; écart déclaré à la règle « lignes ajoutées, jamais réécrites » du registre. Raison (R-2601, R-2602) : le code
épinglé exige **exactement une** ligne `CODE-T07` (`registre_v1.lire_registre_detail`) et `code_t07_v1 verifier` lit la première
(`lecture_v2.lire_lignes_actuelles`) : ajouter une ligne ne suffit pas.

Deux commandes (PYTHONPATH=src, depuis la racine du dépôt) :

    construire --racine R --chemin P [--date AAAA-MM-JJTHH:MM:SSZ]
        imprime la nouvelle ligne, construite par `registre_v1.ecrire_ligne` (clé `CODE-T07`, date donnée ou `date -u`, chemin P,
        empreinte du fichier R/P après vérification de son compagnon `.sha256`) ; n'écrit rien.

    remplacer --racine R --registre REG --ancienne 'LIGNE' --nouvelle 'LIGNE' --trace T [--a-blanc]
        refuse (code 2, motif sur la sortie d'erreur, **rien d'écrit**) si l'un de ces contrôles échoue :
          (1) registre lisible en UTF-8 strict, lignes séparées par « \\n » seulement (aucun autre séparateur que lirait
              `str.splitlines`, aucun retour chariot) ;
          (2) **exactement une** ligne du registre dont la première cellule est `CODE-T07` (découpage de `registre_v1`) ;
          (3) cette ligne **égale à l'octet** à l'ancienne attendue (premier octet différent cité) ;
          (4) nouvelle ligne **bien formée** : égale à `ecrire_ligne(*ses quatre cellules)`, clé `CODE-T07`, chemin relatif au
              motif que le script de l'instance recopie (`[A-Za-z0-9._/-]+`, sans « .. »), autre que celui de l'ancienne
              (R12), fichier cité scellé (compagnon égal, empreinte égale à celle de la ligne, `sceau_conforme`) et de la forme
              d'un fichier `CODE-T07` (`code_t07_v1.lire_fichier_code`), date au format, strictement postérieure à celle de
              l'ancienne et non future ; différente de l'ancienne ;
          (5) aucune ligne `OUVERTURE-T07` au journal des ouvertures du registre (`<REG>.ouvertures.md`) : la ligne `CODE-T07`
              doit précéder strictement la première ouverture (`code_t07_v1.controler_code`) ;
          (6) fichier de trace T absent, son compagnon absent, son dossier présent ; fichier temporaire absent.
        Sinon : contrôle, avant toute écriture, que les octets hors de la ligne sont identiques et que la copie ne porte qu'une
        ligne `CODE-T07`, égale à la nouvelle ; écrit la copie dans un fichier temporaire du même dossier ; **écrit la trace
        (création exclusive) et la scelle** (`controle_ia.scellement.sceller`) : ancienne et nouvelle lignes, heure `date -u`,
        empreintes du registre avant et après (attendue), position et longueurs de la ligne, empreinte de ce script ; **puis**
        remplace en place (`os.replace` ; mode du fichier gardé) et relit. `--a-blanc` : tous les contrôles, rien d'écrit.

Ce script n'a jamais été exécuté sur le vrai registre par son auteur : essais sur des copies,
`docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1/essais-outil/test_remplacer_ligne_code_t07_v2.py`.
Code de sortie : 0 fait (ou à blanc conforme), 2 refus.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from controle_ia.scellement import sceller
from controle_ia.t07 import code_t07_v1 as ct
from controle_ia.t07 import registre_v1 as rg

CLE = rg.CODE_T07
CHEMIN_RECOPIABLE = re.compile(r"[A-Za-z0-9._/-]+")        # motif de l'awk du script de l'instance (v4, l. 182) : sinon non recopié
SUFFIXE_TMP = ".remplacement-code-t07-v2.tmp"


class RefusRemplacement(rg.RefusRegistre):
    """Refus du remplacement : rien n'est écrit (code 2)."""


def cellules(ligne: str) -> list[str]:
    """Découpage de `registre_v1.lire_registre_detail` (même règle)."""
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def heure_date_u() -> str:
    r = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True)
    h = r.stdout.strip()
    if not rg.DATE.fullmatch(h):
        raise RefusRemplacement(f"date -u : sortie {h!r} hors format")
    return h


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _premier_octet_different(a: bytes, b: bytes) -> int:
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return min(len(a), len(b))


def construire(racine: Path, chemin: str, date: str | None = None) -> str:
    """Nouvelle ligne `CODE-T07` au format exact (`ecrire_ligne`), empreinte du fichier cité (compagnon vérifié)."""
    date = date or heure_date_u()
    sha = rg.sceau_conforme(Path(racine) / chemin)
    return rg.ecrire_ligne(CLE, date, chemin, sha)


def controler_nouvelle(racine: Path, nouvelle: str, ancienne: str, maintenant: int) -> dict:
    if "\n" in nouvelle or "\r" in nouvelle:
        raise RefusRemplacement("nouvelle ligne : saut de ligne ou retour chariot dedans")
    c = cellules(nouvelle)
    if len(c) != 4:
        raise RefusRemplacement(f"nouvelle ligne : {len(c)} cellule(s), 4 attendues")
    cle, date, chemin, sha = c
    if cle != CLE:
        raise RefusRemplacement(f"nouvelle ligne : clé {cle!r}, {CLE} attendue")
    try:
        forme = rg.ecrire_ligne(cle, date, chemin, sha)
    except rg.RefusRegistre as e:
        raise RefusRemplacement(f"nouvelle ligne mal formée : {e}") from None
    if forme != nouvelle:
        raise RefusRemplacement(f"nouvelle ligne : n'est pas au format exact de ecrire_ligne (attendu {forme!r})")
    if not CHEMIN_RECOPIABLE.fullmatch(chemin) or chemin.startswith("/") or ".." in Path(chemin).parts or ".." in chemin:
        raise RefusRemplacement(f"nouvelle ligne : chemin {chemin!r} (relatif, [A-Za-z0-9._/-]+, sans « .. » attendu)")
    ca = cellules(ancienne)
    if len(ca) == 4 and ca[2] == chemin:
        raise RefusRemplacement(f"nouvelle ligne : même chemin que l'ancienne ({chemin}) : R12, une nouvelle version prend un nouveau nom")
    try:
        instant = rg.instant_utc(date)
        rg.sceau_conforme(Path(racine) / chemin, sha)
        fichier = ct.lire_fichier_code(Path(racine) / chemin)
    except rg.RefusRegistre as e:
        raise RefusRemplacement(f"nouvelle ligne : {e}") from None
    if len(ca) == 4 and rg.DATE.fullmatch(ca[1]):
        if not instant > rg.instant_utc(ca[1]):
            raise RefusRemplacement(f"nouvelle ligne datée {date}, pas strictement postérieure à l'ancienne ({ca[1]})")
    if instant > int(maintenant):
        raise RefusRemplacement(f"nouvelle ligne datée {date}, dans le futur (maintenant {rg.date_utc(maintenant)})")
    if nouvelle == ancienne:
        raise RefusRemplacement("nouvelle ligne égale à l'ancienne : rien à remplacer")
    return {"date": date, "chemin": chemin, "sha256": sha, "commit_cite": fichier["commit"], "fichiers_cites": len(fichier["fichiers"])}


def preparer(racine: Path, registre: Path, ancienne: str, nouvelle: str, trace: Path, maintenant: int | None = None) -> dict:
    """Tous les contrôles (1) à (6) ; rend les octets avant et après et le rapport. N'écrit rien."""
    racine, registre, trace = Path(racine), Path(registre), Path(trace)
    maintenant = int(time.time()) if maintenant is None else int(maintenant)
    if "\n" in ancienne or "\r" in ancienne:
        raise RefusRemplacement("ancienne ligne : saut de ligne ou retour chariot dedans")
    if not registre.is_file():
        raise RefusRemplacement(f"registre {registre} absent")
    for p in (trace, Path(str(trace) + ".sha256")):
        if p.exists():
            raise RefusRemplacement(f"fichier de trace {p} déjà présent : jamais réécrit (R12)")
    if not trace.parent.is_dir():
        raise RefusRemplacement(f"dossier de la trace {trace.parent} absent")
    if trace.resolve() == registre.resolve():
        raise RefusRemplacement("la trace ne peut pas être le registre")
    tmp = Path(str(registre) + SUFFIXE_TMP)
    if tmp.exists():
        raise RefusRemplacement(f"fichier temporaire {tmp} déjà présent")
    avant = registre.read_bytes()
    try:
        texte = avant.decode("utf-8")
    except UnicodeDecodeError as e:
        raise RefusRemplacement(f"registre : UTF-8 illisible ({e.reason}, octet {e.start})") from None
    if "\r" in texte:
        raise RefusRemplacement("registre : retour chariot présent (forme inattendue)")
    lignes = texte.split("\n")
    corps = lignes[:-1] if texte.endswith("\n") else lignes
    if texte and texte.splitlines() != corps:
        raise RefusRemplacement("registre : séparateur de lignes autre que « \\n » (str.splitlines le découperait autrement)")
    indices = [i for i, l in enumerate(lignes) if cellules(l) and cellules(l)[0] == CLE]
    if len(indices) != 1:
        raise RefusRemplacement(f"registre : {len(indices)} ligne(s) {CLE}, exactement une attendue")
    i = indices[0]
    if lignes[i].encode("utf-8") != ancienne.encode("utf-8"):
        k = _premier_octet_different(lignes[i].encode("utf-8"), ancienne.encode("utf-8"))
        raise RefusRemplacement(f"registre : la ligne {CLE} diffère de l'ancienne attendue (premier octet différent : {k} ; "
                                f"longueurs {len(lignes[i].encode('utf-8'))} et {len(ancienne.encode('utf-8'))})")
    journal = Path(str(registre) + ".ouvertures.md")
    if journal.is_file():
        for l in journal.read_text(encoding="utf-8").splitlines():
            c = cellules(l)
            if c and c[0] == "OUVERTURE-T07":
                raise RefusRemplacement(f"journal {journal} : une ligne OUVERTURE-T07 y est déjà : la ligne {CLE} doit précéder "
                                        "strictement la première ouverture ; aucun remplacement après une ouverture")
    rapport = controler_nouvelle(racine, nouvelle, ancienne, maintenant)
    debut = len("\n".join(lignes[:i]).encode("utf-8")) + (1 if i > 0 else 0)
    fin = debut + len(ancienne.encode("utf-8"))
    apres = avant[:debut] + nouvelle.encode("utf-8") + avant[fin:]
    # contrôles de la copie avant toute écriture : seuls les octets de la ligne changent ; une seule ligne CODE-T07, la nouvelle
    if avant[debut:fin] != ancienne.encode("utf-8") or apres[:debut] != avant[:debut] or apres[debut + len(nouvelle.encode("utf-8")):] != avant[fin:]:
        raise RefusRemplacement("contrôle interne : octets hors de la ligne changés (rien d'écrit)")
    lignes_apres = apres.decode("utf-8").split("\n")
    n_apres = [l for l in lignes_apres if cellules(l) and cellules(l)[0] == CLE]
    autres_avant = [l for j, l in enumerate(lignes) if j != i]
    autres_apres = [l for j, l in enumerate(lignes_apres) if j != i]
    if n_apres != [nouvelle] or autres_avant != autres_apres or len(lignes_apres) != len(lignes):
        raise RefusRemplacement("contrôle interne : copie remplacée non conforme (rien d'écrit)")
    rapport.update({"registre": str(registre), "ligne_numero": i + 1, "octet_debut": debut,
                    "octets_ancienne": len(ancienne.encode("utf-8")), "octets_nouvelle": len(nouvelle.encode("utf-8")),
                    "sha256_avant": sha256_octets(avant), "sha256_apres": sha256_octets(apres)})
    return {"avant": avant, "apres": apres, "rapport": rapport, "tmp": tmp}


def texte_trace(r: dict, ancienne: str, nouvelle: str, heure: str, outil_sha: str) -> str:
    return (
        "# Trace du remplacement de la ligne CODE-T07 du registre des scellements — v1\n\n"
        "Trace écrite et scellée **avant** le remplacement (outil v2) ; le remplacement est attesté par l'empreinte du registre "
        "après, ci-dessous, que l'outil a relue après l'écriture.\n\n"
        f"- **Heure (UTC, `date -u`)** : {heure}\n"
        f"- **Décision** : R-2604 (1), option (a) : remplacement unique, ancienne ligne vérifiée à l'octet ; écart déclaré à la règle "
        "« lignes ajoutées, jamais réécrites » (addendum de T0.7, cache du modèle de P3).\n"
        f"- **Registre** : `{r['registre']}` ; ligne n° {r['ligne_numero']} (octet {r['octet_debut']}, {r['octets_ancienne']} octets "
        f"avant, {r['octets_nouvelle']} après) ; aucun autre octet changé (contrôlé avant et après l'écriture).\n"
        f"- **Empreinte du registre avant** : `{r['sha256_avant']}`\n"
        f"- **Empreinte du registre après** : `{r['sha256_apres']}`\n"
        f"- **Fichier cité par la nouvelle ligne** : `{r['chemin']}` (`{r['sha256']}`, compagnon conforme) ; champ `commit` "
        f"`{r['commit_cite']}` ; {r['fichiers_cites']} fichiers.\n"
        f"- **Outil** : `scripts/remplacer_ligne_code_t07_v2.py` (`{outil_sha}`).\n\n"
        "## Ancienne ligne (à l'octet)\n\n```\n" + ancienne + "\n```\n\n"
        "## Nouvelle ligne (à l'octet)\n\n```\n" + nouvelle + "\n```\n")


def remplacer(racine: Path, registre: Path, ancienne: str, nouvelle: str, trace: Path, a_blanc: bool = False,
              maintenant: int | None = None, heure=heure_date_u) -> dict:
    p = preparer(racine, registre, ancienne, nouvelle, trace, maintenant)
    r = p["rapport"]
    if a_blanc:
        r["a_blanc"] = True
        return r
    registre, trace, tmp = Path(registre), Path(trace), p["tmp"]
    if sha256_octets(registre.read_bytes()) != r["sha256_avant"]:
        raise RefusRemplacement("registre changé pendant les contrôles : rien d'écrit")
    compagnon = Path(str(trace) + ".sha256")
    with open(tmp, "xb") as f:
        f.write(p["apres"])
        f.flush()
        os.fsync(f.fileno())
    shutil.copymode(registre, tmp)
    # m-6 : la trace d'abord ; si elle ne peut pas s'écrire, rien n'est remplacé
    try:
        h = heure()
        outil = sha256_octets(Path(__file__).read_bytes())
        with open(trace, "x", encoding="utf-8") as f:
            f.write(texte_trace(r, ancienne, nouvelle, h, outil))
        trace_sha = sceller(trace)
    except Exception as e:                              # noqa: BLE001 — toute faute de la trace refuse le remplacement
        for x in (compagnon, trace, tmp):               # absents au départ (contrôle (6)) : présents, ils viennent de cet appel
            if x.exists():
                x.unlink()
        raise RefusRemplacement(f"trace impossible ({type(e).__name__} : {e}) : rien n'est remplacé") from None
    try:
        os.replace(tmp, registre)
    except OSError as e:
        for x in (compagnon, trace, tmp):
            if x.exists():
                x.unlink()
        raise RefusRemplacement(f"remplacement impossible ({type(e).__name__} : {e}) : trace retirée, registre inchangé") from None
    if registre.read_bytes() != p["apres"]:
        raise RefusRemplacement(f"relecture : le registre ne porte pas les octets attendus ({r['sha256_apres'][:12]}…) : nœud "
                                f"(trace {trace} gardée : elle dit l'état attendu)")
    r.update({"heure": h, "trace": str(trace), "trace_sha256": trace_sha, "outil_sha256": outil})
    return r


def main(argv: list[str]) -> int:
    a = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    s = a.add_subparsers(dest="commande", required=True)
    c = s.add_parser("construire")
    c.add_argument("--racine", required=True)
    c.add_argument("--chemin", required=True)
    c.add_argument("--date")
    r = s.add_parser("remplacer")
    r.add_argument("--racine", required=True)
    r.add_argument("--registre", required=True)
    r.add_argument("--ancienne", required=True)
    r.add_argument("--nouvelle", required=True)
    r.add_argument("--trace", required=True)
    r.add_argument("--a-blanc", action="store_true")
    x = a.parse_args(argv)
    try:
        if x.commande == "construire":
            print(construire(Path(x.racine), x.chemin, x.date))
            return 0
        rap = remplacer(Path(x.racine), Path(x.registre), x.ancienne, x.nouvelle, Path(x.trace), a_blanc=x.a_blanc)
    except rg.RefusRegistre as e:          # RefusRemplacement comprise
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    if rap.get("a_blanc"):
        print(f"À BLANC, conforme : ligne n° {rap['ligne_numero']} ; registre {rap['sha256_avant']} → {rap['sha256_apres']} ; rien d'écrit")
    else:
        print(f"REMPLACÉE : ligne n° {rap['ligne_numero']} ; registre {rap['sha256_avant']} → {rap['sha256_apres']} ; "
              f"heure {rap['heure']} ; trace {rap['trace']} ({rap['trace_sha256']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

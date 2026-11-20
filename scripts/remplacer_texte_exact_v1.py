#!/usr/bin/env python3
"""Remplacement de textes exacts dans une copie d'un fichier — v1 (bibliothèque standard seulement).

Outil écrit d'avance pour les agents du compte (GO-2026-11-19-84 : jamais de code en ligne passé à un interpréteur) :
on l'appelle par son chemin, les textes à remplacer sont dans un fichier JSON.

Usage (depuis n'importe quel dossier) :

    python3 -B scripts/remplacer_texte_exact_v1.py --cible FICHIER --remplacements R.json --sortie NOUVEAU [--sur-place-interdit]

  - `--cible` : fichier lu, jamais modifié.
  - `--remplacements` : fichier JSON, UTF-8, une liste non vide d'objets `{"ancien": "...", "neuf": "..."}` (ces deux clés
    exactement, valeurs chaînes, aucune clé en double).
  - `--sortie` : fichier neuf (R12) ; écrit avec, à côté, `<sortie>.sha256` (format `sha256sum`), le journal
    `<sortie>.journal-remplacements-v1.json` et son compagnon `<sortie>.journal-remplacements-v1.json.sha256`.
  - `--sur-place-interdit` : toujours vrai, que l'option soit passée ou non ; aucune option n'écrit sur place.

Règles (toute violation = refus, code 2, motif sur la sortie d'erreur, **aucun fichier écrit**) :
  (1) cible et JSON lisibles, fichiers ordinaires, UTF-8 strict ; JSON bien formé, de la forme ci-dessus ; « ancien » non vide,
      différent de « neuf », sans substitut isolé (« \\ud800 ») ;
  (2) chaque texte ancien figure **exactement une fois** dans la cible, occurrences chevauchantes comptées (« aa » figure deux
      fois dans « aaa ») ;
  (3) les zones des textes anciens ne se chevauchent pas (deux zones contiguës sont permises) ;
  (4) les remplacements s'appliquent **simultanément**, aux positions trouvées dans la cible d'origine (un texte neuf n'est
      jamais relu par un autre remplacement) ;
  (5) après application, chaque texte neuf non vide figure dans la sortie exactement k fois de plus que dans la cible, k étant
      le nombre de remplacements qui portent ce texte neuf (k = 1 dans le cas ordinaire : « une fois de plus qu'avant, ou
      exactement une fois s'il n'y était pas ») ; un texte neuf vide (suppression) n'a pas ce contrôle, la règle (6) le couvre ;
  (6) contrôle interne avant écriture : longueur de la sortie égale à celle de la cible plus la somme des écarts, octets hors
      des zones identiques à l'octet (fins de ligne, marque d'ordre des octets, fin de fichier comprises), sortie en UTF-8
      strict ;
  (7) sortie, compagnon, journal et compagnon du journal **absents** (même un lien symbolique), dossier de la sortie présent ;
      chaque fichier est créé en mode exclusif ; si une écriture ou la relecture échoue, les fichiers créés par cet appel sont
      retirés et l'outil refuse.

Avertissement non bloquant (sortie d'erreur et journal) : un texte neuf apporte un style de fin de ligne (« \\r\\n » ou « \\n »
seul) absent de la cible.

Codes de sortie : 0 fait ; 2 refus (et usage invalide, par argparse) ; tout autre code non nul = faute inattendue (trace).
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import sys
from pathlib import Path

NOM_OUTIL = "remplacer_texte_exact_v1"
SUFFIXE_SHA = ".sha256"
SUFFIXE_JOURNAL = ".journal-remplacements-v1.json"
CODE_REFUS = 2
CLES = {"ancien", "neuf"}


class Refus(Exception):
    """Refus : aucun fichier n'est écrit (ou ceux que cet appel a créés sont retirés)."""


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def apercu(b: bytes, n: int = 60) -> str:
    t = b.decode("utf-8", errors="replace")
    return repr(t if len(t) <= n else t[:n] + "…")


def lire_octets(chemin: Path, role: str) -> bytes:
    if not os.path.lexists(chemin):
        raise Refus(f"{role} {chemin} : absent")
    if not chemin.is_file():
        raise Refus(f"{role} {chemin} : pas un fichier ordinaire")
    try:
        return chemin.read_bytes()
    except OSError as e:
        raise Refus(f"{role} {chemin} : illisible ({type(e).__name__} : {e})") from None


def decoder_utf8(b: bytes, role: str) -> str:
    try:
        return b.decode("utf-8", errors="strict")
    except UnicodeDecodeError as e:
        raise Refus(f"{role} : UTF-8 illisible ({e.reason}, octet {e.start})") from None


def _objet_sans_doublon(paires: list) -> dict:
    d: dict = {}
    for k, v in paires:
        if k in d:
            raise Refus(f"fichier de remplacements : clé {k!r} en double dans un même objet")
        d[k] = v
    return d


def _constante_refusee(nom: str):
    raise Refus(f"fichier de remplacements : constante JSON non standard {nom}")


def lire_remplacements(octets: bytes) -> list[dict]:
    """Liste de {rang, ancien, neuf} en octets UTF-8 ; refus sur toute forme inattendue."""
    texte = decoder_utf8(octets, "fichier de remplacements")
    try:
        donnees = json.loads(texte, object_pairs_hook=_objet_sans_doublon, parse_constant=_constante_refusee)
    except json.JSONDecodeError as e:
        raise Refus(f"fichier de remplacements : JSON illisible ({e.msg}, ligne {e.lineno}, colonne {e.colno})") from None
    if not isinstance(donnees, list):
        raise Refus(f"fichier de remplacements : une liste est attendue, pas {type(donnees).__name__}")
    if not donnees:
        raise Refus("fichier de remplacements : liste vide, rien à remplacer")
    res = []
    for rang, r in enumerate(donnees, 1):
        if not isinstance(r, dict):
            raise Refus(f"remplacement n° {rang} : un objet est attendu, pas {type(r).__name__}")
        if set(r) != CLES:
            raise Refus(f"remplacement n° {rang} : clés {sorted(r)} ; exactement {sorted(CLES)} attendues")
        a, n = r["ancien"], r["neuf"]
        if not isinstance(a, str) or not isinstance(n, str):
            raise Refus(f"remplacement n° {rang} : « ancien » et « neuf » doivent être des chaînes")
        if a == "":
            raise Refus(f"remplacement n° {rang} : texte ancien vide")
        if a == n:
            raise Refus(f"remplacement n° {rang} : texte neuf égal à l'ancien, rien à remplacer")
        try:
            ab, nb = a.encode("utf-8"), n.encode("utf-8")
        except UnicodeEncodeError as e:
            raise Refus(f"remplacement n° {rang} : caractère non encodable en UTF-8 (substitut isolé ?) : {e.reason}") from None
        res.append({"rang": rang, "ancien": ab, "neuf": nb})
    return res


def positions(meule: bytes, aiguille: bytes) -> list[int]:
    """Toutes les positions de départ de `aiguille` dans `meule`, occurrences chevauchantes comprises."""
    if not aiguille:
        raise ValueError("aiguille vide")
    res = []
    i = meule.find(aiguille)
    while i != -1:
        res.append(i)
        i = meule.find(aiguille, i + 1)
    return res


def numero_ligne(b: bytes, pos: int) -> int:
    return b.count(b"\n", 0, pos) + 1


def styles_fin_de_ligne(b: bytes) -> set[str]:
    s = set()
    if b"\r\n" in b:
        s.add("\\r\\n")
    if b.count(b"\n") > b.count(b"\r\n"):
        s.add("\\n seul")
    return s


def preparer(cible: bytes, remplacements: list[dict]) -> dict:
    """Contrôles (2) à (6) ; rend les octets de la sortie et le détail. N'écrit rien.

    Recherche à l'octet : en UTF-8 valide, une occurrence d'un texte UTF-8 valide commence et finit toujours sur une limite de
    caractère ; compter à l'octet revient donc à compter sur le texte.
    """
    decoder_utf8(cible, "cible")
    zones = []
    for r in remplacements:
        pos = positions(cible, r["ancien"])
        if len(pos) != 1:
            lignes = ", ".join(str(numero_ligne(cible, p)) for p in pos[:5]) + (" …" if len(pos) > 5 else "")
            ou = f" (lignes {lignes})" if pos else ""
            raise Refus(f"remplacement n° {r['rang']} : texte ancien {apercu(r['ancien'])} trouvé {len(pos)} fois dans la cible"
                        f"{ou}, exactement une attendue")
        zones.append((pos[0], pos[0] + len(r["ancien"]), r))
    zones.sort(key=lambda z: (z[0], z[1]))
    for (d1, f1, r1), (d2, f2, r2) in zip(zones, zones[1:]):
        if d2 < f1:
            raise Refus(f"remplacements n° {r1['rang']} et n° {r2['rang']} : zones qui se chevauchent "
                        f"(octets {d1}–{f1} et {d2}–{f2}, ligne {numero_ligne(cible, d2)})")
    morceaux, curseur = [], 0
    for d, f, r in zones:
        morceaux.append(cible[curseur:d])
        morceaux.append(r["neuf"])
        curseur = f
    morceaux.append(cible[curseur:])
    sortie = b"".join(morceaux)

    # (6) contrôle interne, indépendant de l'assemblage
    attendu = len(cible) + sum(len(r["neuf"]) - len(r["ancien"]) for _, _, r in zones)
    if len(sortie) != attendu:
        raise Refus(f"contrôle interne : longueur de la sortie {len(sortie)}, {attendu} attendue")
    decalage, fin_prec = 0, 0
    for d, f, r in zones:
        if sortie[fin_prec + decalage:d + decalage] != cible[fin_prec:d]:
            raise Refus(f"contrôle interne : octets hors zone changés avant l'octet {d} de la cible")
        if sortie[d + decalage:d + decalage + len(r["neuf"])] != r["neuf"]:
            raise Refus(f"contrôle interne : texte neuf n° {r['rang']} absent à sa place")
        decalage += len(r["neuf"]) - (f - d)
        fin_prec = f
    if sortie[fin_prec + decalage:] != cible[fin_prec:]:
        raise Refus("contrôle interne : octets changés après la dernière zone")
    decoder_utf8(sortie, "sortie (contrôle interne)")

    # (5) chaque texte neuf : k occurrences de plus qu'avant
    multiplicite: dict[bytes, int] = {}
    for _, _, r in zones:
        multiplicite[r["neuf"]] = multiplicite.get(r["neuf"], 0) + 1
    comptes = {}
    for neuf, k in multiplicite.items():
        if not neuf:
            continue
        avant, apres = len(positions(cible, neuf)), len(positions(sortie, neuf))
        comptes[neuf] = (avant, apres)
        if apres != avant + k:
            rangs = [r["rang"] for _, _, r in zones if r["neuf"] == neuf]
            raise Refus(f"remplacement(s) n° {rangs} : texte neuf {apercu(neuf)} présent {avant} fois avant et {apres} fois "
                        f"après, {avant + k} attendues (le texte ancien le contient-il, ou une jonction le recrée-t-elle ?)")

    avertissements = []
    styles_cible = styles_fin_de_ligne(cible)
    for _, _, r in zones:
        nouveaux = styles_fin_de_ligne(r["neuf"]) - styles_cible
        if nouveaux and styles_cible:
            avertissements.append(f"remplacement n° {r['rang']} : fin(s) de ligne {sorted(nouveaux)} absente(s) de la cible "
                                  f"(style de la cible : {sorted(styles_cible)})")
    detail = []
    for d, f, r in sorted(zones, key=lambda z: z[2]["rang"]):
        avant, apres = comptes.get(r["neuf"], (None, None))
        detail.append({"rang": r["rang"], "octet_debut_cible": d, "ligne_cible": numero_ligne(cible, d),
                       "octets_ancien": len(r["ancien"]), "octets_neuf": len(r["neuf"]),
                       "sha256_ancien": sha256_octets(r["ancien"]), "sha256_neuf": sha256_octets(r["neuf"]),
                       "occurrences_neuf_avant": avant, "occurrences_neuf_apres": apres})
    return {"sortie": sortie, "detail": detail, "avertissements": avertissements}


def chemins_ecrits(sortie: Path) -> dict[str, Path]:
    s = str(sortie)
    return {"sortie": Path(s), "compagnon": Path(s + SUFFIXE_SHA), "journal": Path(s + SUFFIXE_JOURNAL),
            "compagnon_journal": Path(s + SUFFIXE_JOURNAL + SUFFIXE_SHA)}


def controler_sorties(sortie: Path, cible: Path, json_r: Path) -> dict[str, Path]:
    ch = chemins_ecrits(sortie)
    for role, p in ch.items():
        if os.path.lexists(p):
            raise Refus(f"{role} {p} : existe déjà ; jamais réécrit (R12), choisir un nouveau nom")
    if not sortie.parent.is_dir():
        raise Refus(f"dossier de la sortie {sortie.parent} : absent")
    for p in ch.values():
        for autre, role in ((cible, "la cible"), (json_r, "le fichier de remplacements")):
            if p.resolve() == autre.resolve():
                raise Refus(f"{p} désigne {role} : écriture sur place interdite")
    return ch


def ecrire(ch: dict[str, Path], contenus: dict[str, bytes]) -> None:
    crees: list[Path] = []
    try:
        for cle in ("sortie", "compagnon", "journal", "compagnon_journal"):
            with open(ch[cle], "xb") as f:
                crees.append(ch[cle])
                f.write(contenus[cle])
                f.flush()
                os.fsync(f.fileno())
        for cle in ("sortie", "compagnon", "journal", "compagnon_journal"):
            if ch[cle].read_bytes() != contenus[cle]:
                raise Refus(f"relecture : {ch[cle]} ne porte pas les octets écrits")
    except (OSError, Refus) as e:
        restes = []
        for p in reversed(crees):
            try:
                p.unlink()
            except OSError:
                restes.append(str(p))
        msg = f"écriture impossible ({type(e).__name__} : {e}) ; fichiers créés par cet appel retirés"
        if restes:
            msg += f" SAUF {restes} (à retirer à la main)"
        raise Refus(msg) from None


def executer(cible: Path, json_r: Path, sortie: Path, sur_place_interdit: bool = True) -> dict:
    if sur_place_interdit is not True:
        raise Refus("l'écriture sur place est toujours interdite")
    octets_cible = lire_octets(cible, "cible")
    octets_json = lire_octets(json_r, "fichier de remplacements")
    remplacements = lire_remplacements(octets_json)
    ch = controler_sorties(sortie, cible, json_r)
    p = preparer(octets_cible, remplacements)
    sha_sortie = sha256_octets(p["sortie"])
    try:
        sha_outil = sha256_octets(Path(__file__).read_bytes())
    except OSError:
        sha_outil = None
    journal = {
        "outil": NOM_OUTIL, "outil_sha256": sha_outil,
        "heure_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cible": str(cible), "cible_sha256": sha256_octets(octets_cible), "cible_octets": len(octets_cible),
        "remplacements": str(json_r), "remplacements_sha256": sha256_octets(octets_json),
        "sortie": str(sortie), "sortie_sha256": sha_sortie, "sortie_octets": len(p["sortie"]),
        "nombre_remplacements": len(remplacements), "detail": p["detail"], "avertissements": p["avertissements"],
    }
    octets_journal = (json.dumps(journal, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    contenus = {
        "sortie": p["sortie"],
        "compagnon": f"{sha_sortie}  {ch['sortie'].name}\n".encode("utf-8"),
        "journal": octets_journal,
        "compagnon_journal": f"{sha256_octets(octets_journal)}  {ch['journal'].name}\n".encode("utf-8"),
    }
    ecrire(ch, contenus)
    return {"journal": journal, "chemins": {k: str(v) for k, v in ch.items()}}


def main(argv: list[str] | None = None) -> int:
    a = argparse.ArgumentParser(prog="remplacer_texte_exact_v1.py", description=__doc__.split("\n\n")[0],
                                allow_abbrev=False)
    a.add_argument("--cible", required=True, help="fichier lu, jamais modifié")
    a.add_argument("--remplacements", required=True, help='JSON : [{"ancien": "...", "neuf": "..."}, ...]')
    a.add_argument("--sortie", required=True, help="fichier neuf ; refus s'il existe")
    a.add_argument("--sur-place-interdit", action="store_const", const=True, default=True,
                   help="toujours vrai ; aucune option n'écrit sur place")
    x = a.parse_args(argv)
    try:
        r = executer(Path(x.cible), Path(x.remplacements), Path(x.sortie), x.sur_place_interdit)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        print("Sortie non écrite.", file=sys.stderr)
        return CODE_REFUS
    j = r["journal"]
    for av in j["avertissements"]:
        print(f"AVERTISSEMENT : {av}", file=sys.stderr)
    print(f"FAIT : {j['nombre_remplacements']} remplacement(s) ; cible {j['cible_sha256']} → sortie {r['chemins']['sortie']} "
          f"({j['sortie_sha256']}) ; journal {r['chemins']['journal']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

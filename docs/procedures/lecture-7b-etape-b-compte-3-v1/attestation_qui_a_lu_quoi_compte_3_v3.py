"""Attestation « qui a lu quoi » pour la session hôte du compte 3, v3 (phase C ; la v2 reste, R12, pour la phase A).

Ce que la v3 ajoute : `--admettre-hote CELLULE`. Après la phase A, la mère inscrit l'hôte lui-même dans la liste (hôte du verdict
de la table A) ; R-2711 (2) veut la même session pour la phase C. Une ligne qui nomme l'identifiant **entier** de l'hôte est alors
admise si, et seulement si, sa cellule « exclu de » est exactement la cellule donnée (exclusions de l'hôte écrites par la commande
de la phase A, section 1, qui ne nomment pas l'étape B de T0.7) ; toute autre mention de l'hôte, ou son préfixe seul, arrête.

Écrit le 2026-11-14 par le préparateur (modèle A). Bibliothèque standard seule ; lit la seule liste scellée ; n'écrit rien.

Ce que la v2 change : l'exclusion se juge **par identifiant de session**, non par compte. Règle, dans l'ordre :
  1. la liste est scellée : empreinte égale à l'attendue et à son compagnon ;
  2. l'identifiant entier de la session hôte n'apparaît nulle part, ni ses douze premiers caractères après `session_`
     (identifiant tronqué) ;
  3. le tableau porte un en-tête avec les cellules « session », « compte » et « exclu de » (casse libre) ;
  4. une ligne qui nomme le compte 3 (colonne « session » ou « compte ») est admise si elle porte « aucune exclusion déclarée »,
     ou si sa colonne « session » donne l'identifiant d'**une autre** session (par exemple celle du lot du brief du compte 3) :
     l'exclusion est alors celle de cette session, pas de l'hôte ; une ligne du compte 3 **sans identifiant de session** et avec
     une exclusion arrête : on ne peut pas la distinguer de l'hôte, la mère donne l'identifiant dans la liste.

    python3 -I -B attestation_qui_a_lu_quoi_compte_3_v3.py LISTE EMPREINTE_ATTENDUE SESSION [--admettre-hote CELLULE]

Codes : 0 conforme ; 2 arrêt (motif imprimé) ; 1 erreur d'appel.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

COMPTE_3 = re.compile(r"compte[\s  _-]*3(?![0-9])", re.IGNORECASE)
SESSION = re.compile(r"session_[0-9A-Za-z]{10,}")
SANS_EXCLUSION = "aucune exclusion déclarée"


def _norme(c: str) -> str:
    return c.strip().strip("`*_ ").strip().lower()


def attester(liste: Path, attendu: str, session: str, cellule_hote: str | None = None) -> str:
    liste = Path(liste)
    if not SESSION.fullmatch(session):
        raise ValueError(f"session {session!r} hors de la forme session_…")
    donnees = liste.read_bytes()
    h = hashlib.sha256(donnees).hexdigest()
    comp = Path(str(liste) + ".sha256")
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0] if comp.is_file() else ""
    if h != attendu or h != lu:
        raise SystemExit(f"ARRÊT : liste {liste} : empreinte {h[:12]}… (attendue {attendu[:12]}…, compagnon {lu[:12] or 'absent'}…)")
    texte = donnees.decode("utf-8")
    prefixe = session[len("session_"):][:12]
    lignes_hote = [l for l in texte.splitlines() if session in l]
    if lignes_hote and cellule_hote is None:
        raise SystemExit(f"ARRÊT : la session {session} figure dans la liste : la mère tranche")
    if prefixe in "\n".join(l for l in texte.splitlines() if session not in l):
        raise SystemExit(f"ARRÊT : les douze premiers caractères de la session ({prefixe}) figurent dans la liste (identifiant tronqué ?) : la mère tranche")
    lignes = [l for l in texte.splitlines() if l.lstrip().startswith("|")]
    entete = None
    for l in lignes:
        c = [_norme(x) for x in l.strip().strip("|").split("|")]
        if "session" in c and "compte" in c and "exclu de" in c:
            entete = c
            break
    if entete is None:
        raise SystemExit("ARRÊT : en-tête du tableau sans les cellules « session », « compte » et « exclu de »")
    i_s, i_c, i_e = entete.index("session"), entete.index("compte"), entete.index("exclu de")
    hote_admis = 0
    for l in lignes_hote:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) != len(entete) or session not in c[i_s] or _norme(c[i_e]) != _norme(cellule_hote or ""):
            raise SystemExit(f"ARRÊT : ligne qui nomme la session hôte hors de la forme admise (identifiant dans la colonne « session », "
                             f"« exclu de » égal à la cellule donnée) : la mère tranche")
        hote_admis += 1
    sans, autres = 0, []
    for l in lignes:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) != len(entete) or [_norme(x) for x in c] == entete or all(set(x) <= set("-: ") for x in c):
            continue
        if not (COMPTE_3.search(c[i_c]) or COMPTE_3.search(c[i_s])):
            continue
        if _norme(c[i_e]) == SANS_EXCLUSION:
            sans += 1
            continue
        ids = SESSION.findall(c[i_s])
        if session in ids:
            continue                      # ligne de l'hôte, admise plus haut
        if ids:
            autres.append(f"« {c[0]} » ({', '.join(ids)})")
            continue
        raise SystemExit(f"ARRÊT : ligne « {c[0]} » : le compte 3, sans identifiant de session, y porte « {c[i_e]} » : on ne peut pas la "
                         "distinguer de l'hôte ; la mère donne l'identifiant dans la liste")
    return (f"ATTESTATION : CONFORME — session {session} : aucune mention hors des lignes admises, préfixe compris ({liste.name}, {h[:12]}…) ; lignes du compte 3 : "
            f"{sans} sans exclusion, {len(autres)} d'une autre session identifiée{(' : ' + '; '.join(autres)) if autres else ''} ; "
            f"lignes de l'hôte admises : {hote_admis}")


if __name__ == "__main__":
    args = sys.argv[1:]
    cellule = None
    if len(args) == 5 and args[3] == "--admettre-hote":
        cellule, args = args[4], args[:3]
    if len(args) != 3:
        print(__doc__)
        sys.exit(1)
    try:
        print(attester(Path(args[0]), args[1], args[2], cellule))
    except SystemExit as e:
        print(e)
        sys.exit(2)
    except (OSError, ValueError, UnicodeDecodeError) as e:
        print(f"ERREUR D'APPEL : {type(e).__name__} : {e}")
        sys.exit(1)

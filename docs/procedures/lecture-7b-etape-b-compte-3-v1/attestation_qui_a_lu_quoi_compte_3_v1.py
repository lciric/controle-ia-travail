"""Attestation « qui a lu quoi » pour la session hôte du compte 3 (lecture de 7b et étape B de T0.7), v1.

Écrit le 2026-11-14 par le préparateur neuf (modèle A) ; appelé par `commande-compte-3-v1.md`, bloc 2. Bibliothèque standard
seule ; lit la seule liste scellée ; n'écrit rien.

Règle (adaptée de `controle_a_blanc_compte_2_v1.py`, fonction `attester`, parce que la liste v1 nomme déjà le compte 3 sans
exclusion, ligne 17 du tableau) :
  1. la liste est scellée : empreinte égale à l'attendue et à son compagnon ;
  2. l'identifiant de la session hôte n'apparaît **nulle part** dans le fichier ;
  3. le tableau porte un en-tête avec les cellules « session », « compte » et « exclu de » (casse libre) ;
  4. toute ligne du tableau qui nomme le compte 3 (colonne « session » ou « compte ») porte, en « exclu de », exactement
     « aucune exclusion déclarée » ; sinon arrêt : la mère tranche.

    python3 -I -B attestation_qui_a_lu_quoi_compte_3_v1.py LISTE EMPREINTE_ATTENDUE SESSION

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


def attester(liste: Path, attendu: str, session: str) -> str:
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
    if session in texte:
        raise SystemExit(f"ARRÊT : la session {session} figure dans la liste : la mère tranche")
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
    n3 = 0
    for l in lignes:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) != len(entete) or [_norme(x) for x in c] == entete or all(set(x) <= set("-: ") for x in c):
            continue
        if COMPTE_3.search(c[i_c]) or COMPTE_3.search(c[i_s]):
            n3 += 1
            if _norme(c[i_e]) != SANS_EXCLUSION:
                raise SystemExit(f"ARRÊT : ligne « {c[0]} » de la liste : le compte 3 y porte « {c[i_e]} » en « exclu de » : la mère tranche")
    return (f"ATTESTATION : CONFORME — session {session} absente de la liste {liste.name} ({h[:12]}…) ; {n3} ligne(s) nomment le "
            f"compte 3, toutes « {SANS_EXCLUSION} »")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    try:
        print(attester(Path(sys.argv[1]), sys.argv[2], sys.argv[3]))
    except SystemExit as e:
        print(e)
        sys.exit(2)
    except (OSError, ValueError, UnicodeDecodeError) as e:
        print(f"ERREUR D'APPEL : {type(e).__name__} : {e}")
        sys.exit(1)

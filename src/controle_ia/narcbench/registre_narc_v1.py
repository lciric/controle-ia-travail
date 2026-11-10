"""Garde d'ouverture du registre des scellements pour NARCBench, v1 (brouillon 4, « Lignes de registre » ; contre-lecture 3, m2).

Format et contrôles de forme : ceux de `t07/registre_v1.py` (sur `main`), réutilisés (`DATE`, `SHA`, `CLE`, `sceau_conforme`,
`extrait_est_une_ligne_de`, `instant_utc`, `date_utc`) ; la règle de classement des clés de T0.7 (`classer_cle_inconnue`) est
propre à T0.7 et n'est **pas** reprise. Règle de ce module, **à écrire dans le brouillon 5** (le brouillon 4 ne la fixe pas) :
une clé exigée absente, en double ou mal formée refuse ; une clé permise absente n'est pas rendue ; une clé de bonne forme ni
exigée ni permise est **ignorée et comptée** si elle ne porte pas la marque `NARC`, **refusée** si elle la porte.

Clés : étape A et bras externe exigent `SCELLEMENT-NARC-8B`, `GO-NARC-8B` ; étape B exige en plus `SCORES-NARC-8B`,
`SONDES-NARC-8B`, `EXTERNE-NARC` ; permises : `SONDES-T07`, `SCELLEMENT-CONCEPTS-T07`. Refus : `RefusRegistre` (code 2 en
ligne de commande), rien d'écrit. La ligne `GO-NARC-8B` cite un extrait scellé qui doit être une ligne de `registres/go.md`.
"""
from __future__ import annotations

from pathlib import Path

from ..t07.registre_v1 import (CLE, DATE, SHA, RefusRegistre, date_utc, extrait_est_une_ligne_de, instant_utc,
                               sceau_conforme)

SCELLEMENT, GO, SCORES, SONDES, EXTERNE = ("SCELLEMENT-NARC-8B", "GO-NARC-8B", "SCORES-NARC-8B", "SONDES-NARC-8B",
                                           "EXTERNE-NARC")
EXIGEES = {"A": (SCELLEMENT, GO), "externe": (SCELLEMENT, GO), "B": (SCELLEMENT, GO, SCORES, SONDES, EXTERNE)}
PERMISES = ("SONDES-T07", "SCELLEMENT-CONCEPTS-T07")
MARQUE = "NARC"
FICHIER_GO = "registres/go.md"


def lire(registre: Path, etape: str) -> tuple[dict, list]:
    if etape not in EXIGEES:
        raise RefusRegistre(f"étape {etape!r} inconnue")
    registre = Path(registre)
    if not registre.is_file():
        raise RefusRegistre(f"registre {registre} absent")
    exigees = EXIGEES[etape]
    trouvees = {k: [] for k in exigees + PERMISES}
    fautes, ignorees = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if not c or not c[0]:
            continue
        if c[0] in trouvees:
            trouvees[c[0]].append(c)
        elif len(c) == 4 and DATE.fullmatch(c[1]) and CLE.fullmatch(c[0]):
            if MARQUE in c[0].split("-")[1:]:
                fautes.append(f"registre : ligne {c[0]} de NARCBench ni exigée ni permise à l'étape {etape}")
            else:
                ignorees.append(c[0])
    sortie = {}
    for k, lignes in trouvees.items():
        if not lignes and k in PERMISES:
            continue
        if len(lignes) != 1:
            fautes.append(f"registre : {len(lignes)} ligne(s) {k}, exactement une attendue")
            continue
        c = lignes[0]
        if len(c) != 4 or not DATE.fullmatch(c[1]) or not SHA.fullmatch(c[3]) or not c[2] or c[2].startswith("/") \
                or ".." in Path(c[2]).parts:
            fautes.append(f"registre : ligne {k} mal formée")
            continue
        sortie[k] = (instant_utc(c[1]), c[1], c[2], c[3])
    if fautes:
        raise RefusRegistre(" ; ".join(fautes))
    return sortie, ignorees


def garde_ouverture(registre: Path, racine: Path, etape: str, instant: int) -> dict:
    """Toutes les lignes lues : strictement antérieures à `instant`, fichier cité scellé et égal ; `GO-NARC-8B` : extrait égal
    à une ligne de `registres/go.md`. Tous les refus relevés avant d'être rendus."""
    lignes, ignorees = lire(registre, etape)
    racine, fautes, sortie = Path(racine), [], {}
    for k, (t, date, chemin, sha) in lignes.items():
        try:
            if not t < int(instant):
                raise RefusRegistre(f"ligne {k} datée {date}, pas strictement antérieure à l'ouverture ({date_utc(instant)})")
            sceau_conforme(racine / chemin, sha)
            e = {"date": date, "chemin": chemin, "sha256": sha}
            if k == GO:
                e["ligne_go"] = extrait_est_une_ligne_de(racine / chemin, racine / FICHIER_GO)
            sortie[k] = e
        except RefusRegistre as err:
            fautes.append(str(err))
    if fautes:
        raise RefusRegistre(" ; ".join(fautes))
    return {"etape": etape, "lignes": sortie, "ignorees": ignorees, "instant": date_utc(instant)}


__all__ = ["lire", "garde_ouverture", "EXIGEES", "PERMISES", "SCELLEMENT", "GO", "SCORES", "SONDES", "EXTERNE"]

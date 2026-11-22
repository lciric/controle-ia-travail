"""Pièce 10 — lien avec l'épreuve 11 : table à cinq cas (spécification, section 8).

Le devin sur la lecture est le contrôle de manipulation des deux bras ; le canal est
ouvert à dose λ (part d'épisodes où un verdict revient).

| Bras   | Devin     | Courbe de rétablissement           | Lecture |
| Fermé  | au hasard | monte                              | conforme à l'attendu (non réfuté à l'étage joué ; rien n'est établi) |
| Ouvert | rejette   | reste au niveau des fausses alertes| sain |
| Ouvert | rejette   | monte                              | le banc ne mesure rien (test de mort de N-076) |
| Ouvert | au hasard | —                                  | bras non ouvert ou devin aveugle : épreuve refusée |
| Fermé  | rejette   | —                                  | le harnais fuit : réparer avant de lire la courbe |

Une combinaison hors de la table (bras fermé, devin au hasard, courbe qui ne monte
pas) n'est pas lue : refus, sans repli (point laissé ouvert au rapport).
"""
from __future__ import annotations

from typing import Sequence

import numpy as np

from . import RefusDevin

FERME, OUVERT = "ferme", "ouvert"
MONTE, RESTE = "monte", "reste_au_niveau_des_fausses_alertes"

CONFORME = "conforme à l'attendu (non réfuté à l'étage joué ; rien n'est établi)"
SAIN = "sain"
BANC_NUL = "le banc ne mesure rien (test de mort de N-076)"
EPREUVE_REFUSEE = "bras non ouvert ou devin aveugle : épreuve refusée"
HARNAIS_FUIT = "le harnais fuit : réparer avant de lire la courbe"

CAS_ACCEPTES = (CONFORME, SAIN)
CAS_REFUSES = (BANC_NUL, EPREUVE_REFUSEE, HARNAIS_FUIT)


def lire(bras: str, devin_rejette: bool, courbe: str | None) -> str:
    """Rend la lecture de la table. `courbe` est ignorée (« — ») quand la table ne la lit pas."""
    if bras not in (FERME, OUVERT):
        raise RefusDevin(f"bras {bras!r} inconnu")
    if bras == FERME and devin_rejette:
        return HARNAIS_FUIT
    if bras == OUVERT and not devin_rejette:
        return EPREUVE_REFUSEE
    if courbe not in (MONTE, RESTE):
        raise RefusDevin(f"courbe {courbe!r} : « {MONTE} » ou « {RESTE} » exigée pour ce cas")
    if bras == FERME:
        if courbe == MONTE:
            return CONFORME
        raise RefusDevin("bras fermé, devin au hasard, courbe qui ne monte pas : cas hors de la table, non lu")
    return SAIN if courbe == RESTE else BANC_NUL


def exiger_lecture_acceptee(bras: str, devin_rejette: bool, courbe: str | None) -> str:
    """Les deux premiers cas passent ; les trois autres lèvent un refus."""
    l = lire(bras, devin_rejette, courbe)
    if l in CAS_REFUSES:
        raise RefusDevin(f"épreuve 11 : {l}")
    return l


DOSES_ATTENDUES = (0.0, 0.1, 0.3, 1.0)


def verifier_attendu_monde_plante(doses: Sequence[float], statistiques: Sequence[float],
                                  retablissement: Sequence[float] | None = None) -> dict:
    """Attendu sur monde planté : la statistique du devin croît avec λ et le rétablissement
    décroît. Écart : refus. Le rétablissement n'est vérifié que s'il est fourni (la courbe
    de l'épreuve 11 n'est pas écrite ici)."""
    d = np.asarray(doses, dtype=float)
    s = np.asarray(statistiques, dtype=float)
    if d.size < 2 or d.size != s.size or np.any(np.diff(d) <= 0):
        raise RefusDevin("doses vides, non strictement croissantes ou de longueur différente")
    if np.any(np.diff(s) <= 0):
        raise RefusDevin(f"statistique du devin non croissante avec λ : {s.tolist()}")
    r = {"doses": d.tolist(), "statistiques": s.tolist(), "retablissement": "non fourni (non vérifié)"}
    if retablissement is not None:
        rt = np.asarray(retablissement, dtype=float)
        if rt.size != d.size or np.any(np.diff(rt) >= 0):
            raise RefusDevin(f"rétablissement non décroissant avec λ : {rt.tolist()}")
        r["retablissement"] = rt.tolist()
    return r

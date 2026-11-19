"""Garde de priorité de l'étape B bis sur la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale) — v2.

v2 = v1 (`garde_priorite_bbis_v1.py`, `75b5db7e…`) corrigée selon la vérification de la différence v6→v7
(`correctifs-b-beta/verification-difference-commande-b-beta-v6-v7.md`, mineurs 1 à 3) : (1) la machine des lentilles absente d'une seule
liste ne termine plus la garde — il faut `ABSENCES_MAX` listes consécutives lues sans erreur **et** une lecture de l'instance qui la dit
absente ; jusque-là la garde continue (crédit lu, destruction sous le seuil) et l'étape B bis n'est jamais déclarée finie sur une liste
qui ne montre pas la machine ; (2) preuve d'absence après destruction avec `non_vide` ; (3) toute exception d'un tour vaut un tour
illisible → destruction (sens sévère) ; une écriture de journal en échec ne change pas le code de sortie.

Posée par la mère (2026-11-18, après le mot de Lazar « pas la peine on a la recharge automatique », R-3319, qui lève la condition de
crédit de la commande) : **tant que l'étape B bis tourne** (son instance, lue par son identifiant seulement dans la liste des
instances), le crédit du loueur est relu au moins toutes les 15 minutes ; **sous 12 USD, la machine des lentilles est détruite par
son identifiant**, puis son absence est prouvée. La recharge automatique (5 USD sous 5 USD) arrive trop tard pour l'étape B bis, qui
se détruit d'elle-même sous 8 USD.

Côté commande (le conteneur de la session), jamais sur la machine louée. Aucun repli silencieux (R5) :
- liste des instances illisible : l'étape B bis est **supposée en marche** (sens sévère) ;
- crédit illisible : relu jusqu'à `essais_credit` fois à `pause_credit` s d'écart ; toujours illisible → **destruction** (sens sévère :
  la priorité de l'étape B bis ne se vérifie plus) ;
- l'étape B bis absente d'une liste lue sans erreur, qui contient la machine des lentilles (témoin) → la garde a fini son office ;
- la machine des lentilles absente d'une liste lue sans erreur → rien à garder ;
- destruction non suivie d'une absence prouvée → état `destruction_non_prouvee`, code 4, message.
Chaque tour est journalisé (une ligne JSON) ; le crédit seul est lu de `show user` (aucun autre champ imprimé).

Usage : `python -m controle_ia.neuron_lens.garde_priorite_bbis_v1 --instance <ID> --bbis 61276240 --journal <fichier>`
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from controle_ia.neuron_lens import suivi_vast_v6 as sv
from controle_ia.neuron_lens.garde_depense_v4 import detruire_verifie

SEUIL_USD = 12.0
PERIODE_S = 600.0  # 10 minutes, sous les 15 exigées
PERIODE_MAX_S = 900.0


def lire_credit(appel=sv._vast):
    """Crédit (float) ou None si illisible. Ne rend que le crédit."""
    code, out, err = appel("show", "user", "--raw")
    d, e = sv._lire_json(code, out, err)
    if e or not isinstance(d, dict):
        return None
    try:
        c = float(d.get("credit"))
    except (TypeError, ValueError):
        return None
    return c if math.isfinite(c) else None


def bbis_en_marche(liste, id_bbis: int, id_lentilles: int) -> tuple[bool, str]:
    """(en_marche, motif). Liste illisible → supposée en marche. Absente → seulement si la liste contient le témoin."""
    if isinstance(liste, dict):
        return True, f"liste illisible ({liste.get('erreur')}) : étape B bis supposée en marche"
    ids = {str(x.get("id")) for x in liste}
    if str(int(id_bbis)) in ids:
        return True, "étape B bis présente"
    if str(int(id_lentilles)) not in ids:
        return True, "étape B bis absente mais témoin (machine des lentilles) absent aussi : liste non probante, supposée en marche"
    return False, "étape B bis absente d'une liste lue sans erreur qui contient la machine des lentilles"


ABSENCES_MAX = 3


def tour(id_lentilles: int, id_bbis: int, *, appel=sv._vast, seuil: float = SEUIL_USD, essais_credit: int = 3,
         pause_credit: float = 60.0, dormir=time.sleep, absences: int = 0) -> dict:
    """Un tour de garde. Rend un état : `continuer`, `bbis_finie`, `lentilles_absentes`, `detruire` (avec motif et crédit), et le
    compte `absences` de listes consécutives lues sans erreur où la machine des lentilles manque."""
    liste = sv.instances(appel)
    if isinstance(liste, dict):
        absences = 0
    elif str(int(id_lentilles)) in {str(x.get("id")) for x in liste}:
        absences = 0
    else:
        absences += 1
        if absences >= ABSENCES_MAX and sv.instance(id_lentilles, appel).get("absente"):
            return {"etat": "lentilles_absentes", "absences": absences}
    marche, motif = bbis_en_marche(liste, id_bbis, id_lentilles)
    if not marche:
        return {"etat": "bbis_finie", "motif": motif, "absences": absences}
    credit = None
    for i in range(essais_credit):
        credit = lire_credit(appel)
        if credit is not None:
            break
        if i + 1 < essais_credit:
            dormir(pause_credit)
    if credit is None:
        return {"etat": "detruire", "motif": f"crédit illisible {essais_credit} fois ({motif})", "credit": None, "absences": absences}
    if credit < seuil:
        return {"etat": "detruire", "motif": f"crédit {credit:.2f} < {seuil} USD ({motif})", "credit": credit, "absences": absences}
    return {"etat": "continuer", "motif": motif, "credit": credit, "absences": absences}


def detruire_et_prouver(id_lentilles: int, appel=sv._vast, dormir=time.sleep) -> tuple[bool, str]:
    def detruire(i):
        code, out, err = appel("destroy", "instance", str(int(i)), "-y")
        if code != 0:
            raise RuntimeError(f"code {code}")

    def lire(i):
        r = sv.instance(i, appel)
        if r.get("absente"):
            return None
        if "erreur" in r:
            raise RuntimeError(r["erreur"])
        return r.get("dph_total")

    detruire_verifie(id_lentilles, detruire, lire, dormir=dormir)
    return sv.absente(id_lentilles, appel, non_vide=True)


def surveiller(id_lentilles: int, id_bbis: int, *, appel=sv._vast, rapporter=print, dormir=time.sleep,
               periode: float = PERIODE_S, seuil: float = SEUIL_USD, tours_max=None) -> dict:
    if not (0 < periode <= PERIODE_MAX_S):
        raise ValueError(f"période {periode} s hors de ]0, {PERIODE_MAX_S}]")
    n, absences = 0, 0
    while True:
        try:
            r = tour(id_lentilles, id_bbis, appel=appel, seuil=seuil, dormir=dormir, absences=absences)
            absences = r.get("absences", 0)
        except Exception as e:  # noqa: BLE001 — tour illisible : sens sévère
            r = {"etat": "detruire", "motif": f"tour en exception ({type(e).__name__}) : sens sévère", "credit": None}
        if r["etat"] == "detruire":
            try:
                ok, preuve = detruire_et_prouver(id_lentilles, appel, dormir)
            except Exception as e:  # noqa: BLE001
                ok, preuve = False, f"destruction en exception ({type(e).__name__})"
            r = r | {"etat": "detruite" if ok else "destruction_non_prouvee", "preuve": preuve, "id": id_lentilles}
            rapporter(r)
            return r
        rapporter(r)
        if r["etat"] != "continuer":
            return r
        n += 1
        if tours_max is not None and n >= tours_max:
            return r
        dormir(periode)


def main(argv=None):
    p = argparse.ArgumentParser(description="Garde de priorité de l'étape B bis (crédit < seuil → destruction des lentilles)")
    p.add_argument("--instance", type=int, required=True, help="identifiant de la machine des lentilles")
    p.add_argument("--bbis", type=int, required=True, help="identifiant de l'instance de l'étape B bis")
    p.add_argument("--journal", type=Path, required=True)
    p.add_argument("--seuil", type=float, default=SEUIL_USD)
    p.add_argument("--periode", type=float, default=PERIODE_S)
    p.add_argument("--fichier-pid", type=Path)
    a = p.parse_args(argv)
    if a.fichier_pid:
        import os
        a.fichier_pid.write_text(f"{os.getpid()}\n", encoding="utf-8")

    def rapporter(r):
        r = r | {"heure": datetime.now(timezone.utc).isoformat(timespec="seconds"), "instance": a.instance, "bbis": a.bbis}
        ligne = json.dumps(r, ensure_ascii=False)
        try:
            with open(a.journal, "a", encoding="utf-8") as f:
                f.write(ligne + "\n")
        except OSError as e:  # le journal en échec ne change ni la décision ni le code de sortie
            ligne += f" [journal en échec : {type(e).__name__}]"
        print(ligne, flush=True)

    r = surveiller(a.instance, a.bbis, rapporter=rapporter, periode=a.periode, seuil=a.seuil)
    sys.exit({"detruite": 3, "destruction_non_prouvee": 4}.get(r["etat"], 0))


if __name__ == "__main__":
    main()

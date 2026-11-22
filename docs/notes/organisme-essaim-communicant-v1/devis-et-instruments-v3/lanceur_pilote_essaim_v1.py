#!/usr/bin/env python3
"""Lanceur du pilote P-std de l'essaim — v1. Il ne contient AUCUN client de fournisseur : la couche d'appel est un objet
injecté (`client.appeler(appel, texte, max_tokens)` → {"usage": {"entree", "sortie"}, "texte", "fin"}), un faux client local
pour les épreuves. Toute exécution sans client injecté est refusée (code 20) : ce fichier ne peut rien dépenser.

Chaque appel passe obligatoirement par `garde_pilote_essaim_v1.Garde` : `avant` (sortie demandée, octets d'entrée,
messages, relances, réserve de dépense, plan) puis `apres` (usage rendu, cumul) ou `echec`. Une garde franchie
(`ArretCourse`) arrête la course : une ligne `{"evenement": "arret", "code", "garde", "detail"}` est écrite au journal et le
code est rendu. Une erreur inattendue du client (autre que `ErreurFournisseur`) arrête aussi la course (code 17). Aucun repli,
aucune poursuite après un arrêt.

Journal : JSON par ligne, ouvert en création exclusive (jamais écrasé), une ligne par appel, par échec, par arrêt, et une ligne
de fin. Prix : ceux de `calcul_devis_essaim_v3.tarifs()` (pièces du dépôt lues à leur empreinte), espèce « kimi » par défaut.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import garde_pilote_essaim_v1 as GP  # noqa: E402

CODE_ERREUR_INATTENDUE = 17
CODE_SANS_CLIENT = 20


class ErreurFournisseur(Exception):
    """Erreur rendue par la couche d'appel (délai, surcharge) : l'appel peut être relancé, dans la limite des 10 %."""


def _maintenant():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


class Journal:
    def __init__(self, chemin):
        self.f = open(chemin, "x", encoding="utf-8")

    def ecrire(self, **ligne):
        self.f.write(json.dumps(dict(t=_maintenant(), **ligne), ensure_ascii=False, sort_keys=True) + "\n")
        self.f.flush()

    def fermer(self):
        self.f.close()


def courir(plan, client, fournisseur_entree, chemin_journal, prix, plafond_depense=None, relancer=True, max_tokens_par_role=None):
    """Rend (code, garde). Code 0 : plan entier joué sans garde franchie."""
    if client is None:
        j = Journal(chemin_journal)
        j.ecrire(evenement="arret", code=CODE_SANS_CLIENT, garde="client", detail="aucun client injecté : refus")
        j.fermer()
        return CODE_SANS_CLIENT, None
    garde = GP.Garde(plan, prix, plafond_depense)
    mt = dict(GP.PLAFOND_SORTIE, **(max_tokens_par_role or {}))
    j = Journal(chemin_journal)
    j.ecrire(evenement="debut", appels_du_plan=len(garde.plan), relances_max=garde.relances_max,
             plafond_depense_usd=garde.plafond_depense, borne=garde.borne, prix=list(prix),
             plafonds={"sortie": GP.PLAFOND_SORTIE, "entree_jetons": GP.PLAFOND_ENTREE_JETONS, "entree_octets": GP.PLAFOND_ENTREE_OCTETS,
                       "messages_par_monde": GP.MESSAGES_PAR_MONDE})
    try:
        for appel in plan:
            texte = fournisseur_entree(appel)
            while True:
                reserve = garde.avant(appel, texte, mt[appel["role"]])
                try:
                    rep = client.appeler(appel, texte, mt[appel["role"]])
                except ErreurFournisseur as ex:
                    garde.echec(appel)
                    j.ecrire(evenement="echec", id=appel["id"], reserve_usd=round(reserve, 6), depense_usd=round(garde.depense, 6),
                             motif=str(ex)[:200])
                    if relancer:
                        continue
                    garde.abandon()
                    break
                c = garde.apres(appel, rep.get("usage") if isinstance(rep, dict) else None)
                j.ecrire(evenement="appel", id=appel["id"], role=appel["role"], octets=len(texte.encode("utf-8")),
                         usage=rep["usage"], fin=rep.get("fin"), cout_usd=round(c, 6), reserve_usd=round(reserve, 6),
                         depense_usd=round(garde.depense, 6), relances=garde.relances)
                break
    except GP.ArretCourse as ex:
        j.ecrire(evenement="arret", code=ex.code, garde=ex.garde, detail=ex.detail, depense_usd=round(garde.depense, 6),
                 appels_joues=garde.prochain, relances=garde.relances)
        j.fermer()
        return ex.code, garde
    except Exception as ex:  # noqa: BLE001  (aucun repli : toute erreur inattendue arrête la course)
        j.ecrire(evenement="arret", code=CODE_ERREUR_INATTENDUE, garde="erreur inattendue", detail=f"{type(ex).__name__}: {ex}"[:300],
                 depense_usd=round(garde.depense, 6), appels_joues=garde.prochain)
        j.fermer()
        return CODE_ERREUR_INATTENDUE, garde
    if not garde.termine():
        j.ecrire(evenement="arret", code=15, garde="plan", detail="plan non terminé", depense_usd=round(garde.depense, 6))
        j.fermer()
        return 15, garde
    j.ecrire(evenement="fin", code=0, depense_usd=round(garde.depense, 6), appels_joues=garde.prochain, relances=garde.relances,
             plafond_depense_usd=garde.plafond_depense)
    j.fermer()
    return 0, garde


def main(argv):
    """Exécution directe : refusée. Aucun client réel n'existe dans ce fichier ; seules les épreuves injectent un faux client."""
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : lanceur_pilote_essaim_v1.py JOURNAL.jsonl (neuf) — refuse toujours : aucun client réel", file=sys.stderr)
        return 2
    code, _ = courir(GP.plan_pstd(), None, None, argv[1], (0.0, 0.0))
    print(f"arrêt {code} : aucun client injecté", file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))

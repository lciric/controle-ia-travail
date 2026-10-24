# -*- coding: utf-8 -*-
"""Adaptateur v2 : le client d'appel de `m3_commun` branché sur `noyau_client`, fourni par le noyau dans le bac à
sable. Aucune clé ni aucun réseau dans l'organisme : chaque appel passe par le noyau, qui journalise, impose ses
plafonds et refuse toute bascule de modèle.

Correspondance des statuts du noyau vers ceux de `m3_commun` v2 (un statut par cas, rien n'est fondu) :
OK → ok ; VIDE, TRONQUE → vide ; REFUS → refus ; MODELE_NON_CONFORME → modele_non_conforme ;
ECHEC_API, ANOMALIE et tout statut inconnu → echec_api ; PLAFOND → exception `BudgetDepasse`.

Le noyau ne transmet pas de température. La température tirée pour une caste est consignée dans le journal de
l'organisme (`temperature_tiree`), avec `temperature_transmise` faux : c'est un écart déclaré à la conception du
moteur, qui en faisait le trait distinctif des castes.
"""
from __future__ import annotations

import time
from dataclasses import asdict

import noyau_client as nc

import m3_commun as m3

CORRESPONDANCE = {"OK": "ok", "VIDE": "vide", "TRONQUE": "vide", "REFUS": "refus",
                  "MODELE_NON_CONFORME": "modele_non_conforme", "ECHEC_API": "echec_api", "ANOMALIE": "echec_api"}


def especes_disponibles() -> list:
    try:
        return [m3.normaliser_lignee(e) for e in nc.especes()]
    except Exception:  # le noyau ne répond pas : aucune espèce, l'organisme s'arrête proprement
        return []


class ClientNoyau:
    """Même interface que `m3_commun.Client.appeler`, sans réseau propre."""

    def __init__(self, config: m3.Config, journal: m3.Journal, budget: m3.Budget):
        self.config, self.journal, self.budget = config, journal, budget

    def appeler(self, lignee: str, invite: str, temperature=None, etiquette: str = "",
                outil_recherche: bool = False) -> m3.Reponse:
        lignee = m3.normaliser_lignee(lignee)
        self.budget.reserver_appel()
        debut = time.time()
        r = nc.appeler(lignee, invite, max_tokens=self.config.max_tokens_par_appel, role=str(etiquette)[:40])
        statut_noyau = str(r.get("statut", "ANOMALIE"))
        if statut_noyau == "PLAFOND":
            self.journal.ecrire({"etiquette": etiquette, "lignee": lignee, "statut": "plafond_noyau",
                                 "echec": r.get("echec"), "heure_utc": m3.heure_utc()})
            raise m3.BudgetDepasse(f"plafond du noyau : {r.get('echec')}")
        statut = CORRESPONDANCE.get(statut_noyau, "echec_api")
        texte = (r.get("texte") or "") if statut == "ok" else ""
        if statut == "ok" and len(texte.strip()) < m3.SEUIL_TEXTE_VIDE:
            statut = "vide"
        usage = r.get("usage") or {}
        rep = m3.Reponse(ok=(statut == "ok"), statut=statut, lignee=lignee,
                         modele_demande=m3.LIGNEES[lignee]["modele"], modele_servi=r.get("modele_servi"),
                         texte=texte, raison_arret=r.get("fin"), http=None, erreur=r.get("echec"),
                         jetons_entree=usage.get("entree", usage.get("input_tokens")),
                         jetons_sortie=usage.get("sortie", usage.get("output_tokens")),
                         duree_s=round(time.time() - debut, 3), etiquette=etiquette,
                         empreinte_invite=m3.empreinte(invite), empreinte_texte=m3.empreinte(texte), tentatives=1,
                         heure_utc=m3.heure_utc(), a_blanc=False, temperature_envoyee=None)
        enregistrement = asdict(rep)
        enregistrement.update({"statut_noyau": statut_noyau, "temperature_tiree": temperature,
                               "temperature_transmise": False, "cout_usd": r.get("cout_usd"),
                               "identifiant_noyau": r.get("identifiant")})
        self.journal.ecrire(enregistrement)
        self.budget.ajouter_jetons(rep.jetons_entree, rep.jetons_sortie)
        return rep

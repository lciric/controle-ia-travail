"""Adaptateur : le client d'appel de `m3_commun` (essaim de Gemini, version déboguée par la lignée « session-depot »)
branché sur `noyau_client` du bac à sable. Aucune clé, aucun réseau dans l'organisme : chaque appel passe par le
noyau, qui journalise, impose les plafonds et refuse toute bascule de modèle.

Correspondance des statuts du noyau vers ceux de `m3_commun` : OK → ok ; VIDE, TRONQUE, REFUS → vide (la raison
d'arrêt garde « refusal » pour que `evaluer_reponse` compte le refus d'interface) ; ECHEC_API, MODELE_NON_CONFORME,
PLAFOND → echec_api (un plafond du noyau lève `BudgetDepasse`, comme le budget local)."""
import time

import noyau_client as nc

import m3_commun as m3

CORRESPONDANCE = {"OK": "ok", "VIDE": "vide", "TRONQUE": "vide", "REFUS": "vide", "ANOMALIE": "echec_api",
                  "ECHEC_API": "echec_api", "MODELE_NON_CONFORME": "echec_api", "PLAFOND": "echec_api"}


class ClientNoyau:
    """Même interface que `m3_commun.Client.appeler`, sans réseau propre."""

    def __init__(self, config: m3.Config, journal: m3.Journal, budget: m3.Budget):
        self.config, self.journal, self.budget = config, journal, budget

    def appeler(self, lignee: str, invite: str, temperature=None, etiquette: str = "", outil_recherche: bool = False) -> m3.Reponse:
        lignee = m3.normaliser_lignee(lignee)
        self.budget.reserver_appel()
        debut = time.time()
        r = nc.appeler(lignee, invite, max_tokens=self.config.max_tokens_par_appel, role=str(etiquette)[:40])
        statut_noyau = str(r.get("statut", "ANOMALIE"))
        if statut_noyau == "PLAFOND":
            raise m3.BudgetDepasse(f"plafond du noyau : {r.get('echec')}")
        statut = CORRESPONDANCE.get(statut_noyau, "echec_api")
        texte = r.get("texte", "") if statut == "ok" else ""
        usage = r.get("usage") or {}
        rep = m3.Reponse(ok=(statut == "ok"), statut=statut, lignee=lignee, modele_demande=m3.LIGNEES[lignee]["modele"],
                         modele_servi=r.get("modele_servi"), texte=texte, raison_arret=r.get("fin"),
                         http=None, erreur=r.get("echec"), jetons_entree=usage.get("entree"), jetons_sortie=usage.get("sortie"),
                         duree_s=round(time.time() - debut, 3), etiquette=etiquette, empreinte_invite=m3.empreinte(invite),
                         empreinte_texte=m3.empreinte(texte), tentatives=1, heure_utc=m3.heure_utc(), a_blanc=False,
                         temperature_envoyee=None)
        self.journal.ecrire(m3.asdict(rep))
        self.budget.ajouter_jetons(rep.jetons_entree, rep.jetons_sortie)
        return rep

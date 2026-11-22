#!/usr/bin/env python3
"""Faux fournisseur local (transport injecté dans `AdaptateurChatCompletions`) qui tient SA PROPRE FACTURE, pour les
épreuves du lanceur v2 et le rejeu des attaques A1 à A10 de la contre-lecture de la v3. Aucun réseau.

Réglages : entrée facturée (par défaut ⌈octets / 3,3⌉), sortie (fonction ou valeur), relances internes cachées (facturées,
invisibles), réflexion facturée hors de `completion_tokens`, panne après facturation, usage négatif ou absent, modèle servi
différent, tentatives rendues, erreurs de fournisseur (sans facturation, ou facturées au plafond)."""
import math

import adaptateur_fournisseur_v1 as A


class FauxFournisseur:
    def __init__(self, prix, modele="kimi-gele", sortie=None, entree=None, relances_internes=0, relances_declarees=None,
                 reflexion_hors=0, reflexion_detail_hors=0, panne_apres_facture_au=None, usage_negatif_au=None, usage_absent_au=None,
                 modele_servi=None, tentatives=None, erreurs_aux=(), erreur_facturee=False, rng=None):
        self.prix, self.modele = prix, modele
        self.relances_internes = relances_internes if relances_declarees is None else relances_declarees
        self._relances_reelles = relances_internes
        self.repli_modele = None
        self.sortie, self.entree, self.rng = sortie, entree, rng
        self.reflexion_hors, self.reflexion_detail_hors = reflexion_hors, reflexion_detail_hors
        self.panne_au, self.neg_au, self.absent_au = panne_apres_facture_au, usage_negatif_au, usage_absent_au
        self.modele_servi, self.tentatives = modele_servi, tentatives
        self.erreurs_aux, self.erreur_facturee = set(erreurs_aux), erreur_facturee
        self.k = 0             # tentatives reçues
        self.facture = 0.0
        self.requetes = 0

    def _facturer(self, e, s):
        self.facture += (e * self.prix[0] + s * self.prix[1]) / 1e6

    def envoyer(self, requete):
        k = self.k
        self.k += 1
        self.requetes += 1 + self._relances_reelles
        texte = requete["messages"][0]["content"]
        mt = requete["max_tokens"]
        e = self.entree(k, texte) if callable(self.entree) else (self.entree if self.entree is not None else math.ceil(len(texte.encode()) / 3.3))
        if k in self.erreurs_aux:
            if self.erreur_facturee:
                self._facturer(e, mt)
            raise A.ErreurFournisseur(f"délai dépassé (faux fournisseur, tentative {k})")
        if callable(self.sortie):
            s = self.sortie(k, mt)
        elif self.sortie is not None:
            s = self.sortie
        else:
            s = int(self.rng.integers(3000, 12801)) if mt > 2000 else int(self.rng.integers(200, 401))
            s = min(s, mt)
        # facture : la tentative visible, les relances internes cachées, la réflexion hors compte
        for _ in range(1 + self._relances_reelles):
            self._facturer(e, s + self.reflexion_hors + self.reflexion_detail_hors)
        if self.panne_au is not None and k == self.panne_au:
            raise KeyError("choices")  # réponse facturée, mal lue
        usage = {"prompt_tokens": e, "completion_tokens": s}
        if self.reflexion_hors:
            usage["reasoning_tokens"] = self.reflexion_hors
        if self.reflexion_detail_hors:
            usage["completion_tokens_details"] = {"reasoning_tokens": s + self.reflexion_detail_hors}
        if self.neg_au is not None and k == self.neg_au:
            usage["completion_tokens"] = -24000
        if self.absent_au is not None and k == self.absent_au:
            usage = None
        rep = {"model": self.modele_servi or requete["model"], "usage": usage,
               "choices": [{"message": {"content": ""}, "finish_reason": "stop"}]}
        if self.tentatives is not None:
            rep["tentatives"] = self.tentatives
        return rep

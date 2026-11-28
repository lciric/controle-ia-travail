"""Essai (vérification VCB3) : rangées rendues par le témoin jouet, avec la graine (code tel quel) et sans elle
(`torch.manual_seed` neutralisé le temps de l'appel, comme sous RQ-17), depuis plusieurs états du générateur global.
Aucun fichier du clone n'est écrit. Usage : PYTHONPATH=<clone>/src:<clone>/tests python -B essai_sans_graine.py"""
import pytest
import torch

import test_plan_b_requalifier as t
from controle_ia.environnements import requalifier_juges as rq

with pytest.MonkeyPatch.context() as mp:
    t.h4_courte(mp)
    m = t._modele_temoin()
    vrai = torch.manual_seed

    def appel(sans_graine: bool, etat: int):
        vrai(etat)
        if sans_graine:
            torch.manual_seed = lambda s: None
        try:
            a = rq.appel_temoin(m, t.FMT, t.DEMANDES_COURTES[:2], 12, t.C_TEMOIN)
        finally:
            torch.manual_seed = vrai
        return [(r["jetons_generes"], r["tronquee"]) for r in a["rangees"]]

    for sans in (False, True):
        vus = [appel(sans, e) for e in range(40)]
        distincts = sorted({tuple(v) for v in vus})
        print("sans graine" if sans else "avec la graine 12", ": 40 états globaux,", len(distincts),
              "résultat(s) distinct(s) :", distincts[:6], "; part de [(6, True), (6, True)] :",
              sum(v == [(6, True), (6, True)] for v in vus), "/ 40")

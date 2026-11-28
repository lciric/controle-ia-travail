"""Essai (hors du clone) : jetons générés par le témoin jouet selon la graine, et appels de torch.manual_seed."""
import pytest
import torch
import test_plan_b_requalifier as T
from controle_ia.environnements import requalifier_juges as rq

mp = pytest.MonkeyPatch()
T.h4_courte(mp)
m = T._modele_temoin()
print("vocabulaire", len(T.TOK), "fins", sorted(T.FMT.fins))
journal, jetons = [], []
vrai_seed, vrai_gen = torch.manual_seed, m.generate
def seed(s):
    journal.append(("graine", s)); return vrai_seed(s)
def gen(*a, **k):
    journal.append(("generate",)); out = vrai_gen(*a, **k); jetons.append(out[:, k["input_ids"].shape[1]:].tolist()); return out
mp.setattr(torch, "manual_seed", seed)
mp.setattr(m, "generate", gen)
for etat, g in ((1, 12), (2, 12), (3, 13), (4, 14), (5, 15)):
    vrai_seed(etat)
    a = rq.appel_temoin(m, T.FMT, T.DEMANDES_COURTES[:2], g, T.C_TEMOIN)
    print(g, jetons[-1], [(r["jetons_generes"], r["tronquee"]) for r in a["rangees"]])
print(journal)

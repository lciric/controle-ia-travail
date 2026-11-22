"""N3b : deux courses entrelacées sur le même registre, de façon déterministe (la course B démarre pendant l'appel 5 de A).
Usage : python -B attaque_concurrence_v4_cl_v1.py DOSSIER_V4 DOSSIER_NEUF"""
import json, os, sys
V4, D = sys.argv[1:3]; sys.path.insert(0, V4)
import numpy as np
import adaptateur_fournisseur_v1 as A, faux_fournisseur_v1 as F, garde_pilote_essaim_v2 as GP, lanceur_pilote_essaim_v2 as L, registre_depense_v1 as RG
os.makedirs(D); P = GP.plan_pstd(); PRIX = GP.PRIX_GELES; BORNE = GP.borne_pire(P, PRIX)["pire_usd"]
ENT = lambda a: "x" * GP.PLAFOND_ENTREE_OCTETS[a["role"]]
pe = lambda k, t: GP.PLAFOND_ENTREE_JETONS["proposeur"] if len(t) > 20000 else GP.PLAFOND_ENTREE_JETONS["message"]
class H(F.FauxFournisseur):
    def envoyer(self, r):
        rep = super().envoyer(r); rep.setdefault("tentatives", 1); return rep
reg = os.path.join(D, "registre"); L.creer_registre(reg)
tB = H(PRIX, entree=pe, sortie=lambda k, mt: mt); resB = {}
class DeclencheB(H):
    def envoyer(self, r):
        if self.k == 5 and not resB:
            resB["code"], g = L.courir(P, A.AdaptateurChatCompletions(tB, "kimi-gele"), ENT, os.path.join(D, "jB.jsonl"), reg)
            resB["dep"] = g.depense if g else None
        return super().envoyer(r)
tA = DeclencheB(PRIX, entree=pe, sortie=lambda k, mt: mt)
cA, gA = L.courir(P, A.AdaptateurChatCompletions(tA, "kimi-gele"), ENT, os.path.join(D, "jA.jsonl"), reg)
try: RG.Registre(reg, L.parametres(BORNE)); rel = "relu sans refus"
except RG.RegistreRefuse as ex: rel = f"refus {ex.code} : {ex.detail}"
r = {"codes": [cA, resB.get("code")], "depense_comptee_A": gA.depense if gA else None, "depense_comptee_B": resB.get("dep"),
     "facture_totale": tA.facture + tB.facture, "borne": BORNE, "relecture_apres": rel}
print(json.dumps(r, ensure_ascii=False)); json.dump(r, open(os.path.join(D, "resultat.json"), "x"), ensure_ascii=False)

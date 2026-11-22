"""Attaques du contre-lecteur contre le lanceur v2, le registre et l'adaptateur (v4). Faux fournisseur local, aucun réseau.
Usage : python -B attaques_lanceur_v4_cl_v1.py DOSSIER_V4 DOSSIER_NEUF SORTIE.json"""
import json, os, sys, time, multiprocessing as mp
V4, D, OUT = sys.argv[1:4]
sys.path.insert(0, V4)
import numpy as np
import adaptateur_fournisseur_v1 as A, faux_fournisseur_v1 as F, garde_pilote_essaim_v2 as GP
import lanceur_pilote_essaim_v2 as L, registre_depense_v1 as RG
os.makedirs(D)
P, PRIX = GP.plan_pstd(), GP.PRIX_GELES
BORNE = GP.borne_pire(P, PRIX)["pire_usd"]
ENT = lambda a: "x" * GP.PLAFOND_ENTREE_OCTETS[a["role"]]
def plaf_e(k, t): return GP.PLAFOND_ENTREE_JETONS["proposeur"] if len(t) > 20000 else GP.PLAFOND_ENTREE_JETONS["message"]
def plaf_s(k, mt): return mt
class Honnete(F.FauxFournisseur):  # rend ses vraies tentatives (forme de l'auteur)
    def envoyer(self, r):
        rep = super().envoyer(r); rep.setdefault("tentatives", 1 + self._relances_reelles); return rep
class Menteur(F.FauxFournisseur):  # relances cachées ET « tentatives = 1 » (forme réelle de A3 : un kit client mal réglé)
    def envoyer(self, r):
        rep = super().envoyer(r); rep["tentatives"] = 1; return rep
class ReflexionMuette(Honnete):  # réflexion facturée, absente de l'usage rendu (forme réelle de A4)
    def envoyer(self, r):
        rep = super().envoyer(r)
        if rep.get("usage"): rep["usage"].pop("reasoning_tokens", None); rep["usage"].pop("completion_tokens_details", None)
        return rep
def ff(cls=Honnete, **kw): return cls(PRIX, entree=plaf_e, sortie=plaf_s, rng=np.random.default_rng(0), **kw)
res = []
def note(nom, codes, compte, facture, commentaire):
    r = {"attaque": nom, "codes": codes, "depense_comptee": round(compte, 4), "facture": round(facture, 4), "borne": BORNE,
         "facture_au_dela_de_la_borne": facture > BORNE + 1e-9, "sous_compte": facture > compte + 1e-9, "commentaire": commentaire}
    res.append(r); print(json.dumps(r, ensure_ascii=False), flush=True)
def run(nom, t, reg, creer=True, ad=None, **kw):
    if creer: L.creer_registre(reg)
    code, g = L.courir(P, ad or A.AdaptateurChatCompletions(t, "kimi-gele"), ENT, os.path.join(D, f"j-{nom}-{time.time_ns()}.jsonl"), reg, **kw)
    return code, (g.depense if g else 0.0)
# V3a : A3 sous sa forme réelle (transport menteur)
t = ff(Menteur, relances_internes=2, relances_declarees=0); c, dep = run("V3a", t, os.path.join(D, "r-V3a"))
note("V3a A3 réel : relances cachées, tentatives=1 déclarée", [c], dep, t.facture, "la garde ne voit que ce que le transport déclare")
# V4a : A4 sous sa forme réelle (réflexion muette)
t = ff(ReflexionMuette, reflexion_hors=8000); c, dep = run("V4a", t, os.path.join(D, "r-V4a"))
note("V4a A4 réel : réflexion facturée, non rendue", [c], dep, t.facture, "invisible sans H2 vérifiée")
# N1 : registre neuf créé ailleurs
t = ff(); c1, d1 = run("N1a", t, os.path.join(D, "r-N1a")); c2, d2 = run("N1b", t, os.path.join(D, "autre", "r-N1b") if os.makedirs(os.path.join(D, "autre")) is None else "")
note("N1 registre neuf à un autre chemin après une course close", [c1, c2], d1 + d2, t.facture, "aucun verrou global ni chemin unique imposé")
# N2 : réécriture du registre et de son sceau (troncature à la ligne de création, chaîne et sceau refaits)
t = ff(); reg = os.path.join(D, "r-N2"); c1, d1 = run("N2a", t, reg)
premiere = open(reg, encoding="utf-8").readline()
open(reg, "w", encoding="utf-8").write(premiere); RG._sceller(reg)
c2, d2 = run("N2b", t, reg, creer=False)
note("N2 registre tronqué à la création puis re-scellé", [c1, c2], d1 + d2, t.facture, "sceau sans secret : réécrivable par quiconque écrit le fichier")
# N3 : deux processus en même temps sur le même registre
reg = os.path.join(D, "r-N3"); L.creer_registre(reg)
def enfant(i, q):
    class Lent(Honnete):
        def envoyer(self, r):
            time.sleep(0.002); return super().envoyer(r)
    t = Lent(PRIX, entree=plaf_e, sortie=plaf_s, rng=np.random.default_rng(i))
    try:
        code, g = L.courir(P, A.AdaptateurChatCompletions(t, "kimi-gele"), ENT, os.path.join(D, f"j-N3-{i}.jsonl"), reg)
        q.put((i, code, g.depense if g else 0.0, t.facture))
    except Exception as ex:
        q.put((i, f"{type(ex).__name__}", 0.0, t.facture))
q = mp.Queue(); ps = [mp.Process(target=enfant, args=(i, q)) for i in (1, 2)]
[p.start() for p in ps]; out = [q.get() for _ in ps]; [p.join() for p in ps]
try:
    RG.Registre(reg, L.parametres(BORNE)); apres = "registre relu sans refus"
except RG.RegistreRefuse as ex:
    apres = f"relecture : refus {ex.code}"
note("N3 deux processus simultanés sur le même registre", [o[1] for o in out], sum(o[2] for o in out), sum(o[3] for o in out),
     f"aucun verrou ; le registre n'est relu qu'à l'ouverture ; après coup : {apres}")
# N4 : registre créé directement par RG.creer avec un plafond de 1e6
reg = os.path.join(D, "r-N4"); RG.creer(reg, L.parametres(10 ** 6))
t = ff()
try:
    c, dep = run("N4", t, reg, creer=False)
except Exception as ex:
    c, dep = f"{type(ex).__name__}", 0.0
note("N4 registre forgé par RG.creer avec plafond 1e6", [c], dep, t.facture, "le plafond du registre est-il comparé à la borne ?")
# N5 : sous-classe de l'adaptateur qui envoie trois fois
class Adapt3(A.AdaptateurChatCompletions):
    def appeler(self, appel, texte, mt):
        for _ in range(2): self.transport.envoyer({"model": self.modele, "messages": [{"role": "user", "content": texte}], "max_tokens": mt})
        return super().appeler(appel, texte, mt)
t = ff(); c, dep = run("N5", t, os.path.join(D, "r-N5"), ad=Adapt3(t, "kimi-gele"))
note("N5 sous-classe de l'adaptateur qui envoie trois fois", [c], dep, t.facture, "isinstance accepte toute sous-classe")
json.dump(res, open(OUT, "x"), ensure_ascii=False, indent=1)

"""Attaques du contre-lecteur contre le registre v2 et le lanceur v3 (v5). Faux fournisseur local, aucun réseau ; chemins du
bloc-notes seulement (jamais ceux du pilote). Usage : python -B attaques_v5_cl_v1.py DOSSIER_V5 DOSSIER_NEUF SORTIE.json"""
import json, os, sys, time, shutil, multiprocessing as mp
V5, D, OUT = sys.argv[1:4]; sys.path.insert(0, V5)
import numpy as np
import adaptateur_fournisseur_v1 as A, faux_fournisseur_v1 as F, garde_pilote_essaim_v2 as GP
import lanceur_pilote_essaim_v3 as L, registre_depense_v2 as RG
os.makedirs(D); P = GP.plan_pstd(); PRIX = GP.PRIX_GELES; BORNE = L.borne()
ENT = lambda a: "x" * GP.PLAFOND_ENTREE_OCTETS[a["role"]]
pe = lambda k, t: GP.PLAFOND_ENTREE_JETONS["proposeur"] if len(t) > 20000 else GP.PLAFOND_ENTREE_JETONS["message"]
class H(F.FauxFournisseur):
    def envoyer(self, r):
        rep = super().envoyer(r); rep.setdefault("tentatives", 1 + self._relances_reelles); return rep
def ch(nom, etat=None):
    e = etat or os.path.join(D, f"etat-{nom}")
    return RG.Chemins(os.path.join(D, f"registre-{nom}.jsonl"), os.path.join(e, "ancre.json"), os.path.join(e, "cle"))
def t(): return H(PRIX, entree=pe, sortie=lambda k, mt: mt, rng=np.random.default_rng(0))
import hashlib
def admis(tr):
    m = sys.modules[type(tr).__module__]
    return {(type(tr).__module__, type(tr).__qualname__): hashlib.sha256(open(m.__file__, "rb").read()).hexdigest()}
def courir(c, tr, ad=None):
    code, g = L._courir(P, ad or A.AdaptateurChatCompletions(tr, "kimi-gele"), ENT, os.path.join(D, f"j-{time.time_ns()}.jsonl"), c, admis(tr))
    return code
res = []
def note(nom, codes, facture, comm):
    r = {"attaque": nom, "codes": codes, "facture": round(facture, 4), "borne": BORNE, "au_dela": facture > BORNE + 1e-9, "commentaire": comm}
    res.append(r); print(json.dumps(r, ensure_ascii=False), flush=True)
def resceller(c, octets):  # forge avec la clé lisible
    cle = open(c.cle, "rb").read(); mac, n = RG._sceau(cle, octets)
    open(c.sceau, "w").write(json.dumps({"hmac": mac, "lignes": n}) + "\n"); open(c.ancre, "w").write(json.dumps(RG._ancre(octets, mac, n)) + "\n")
# rejeu de mes attaques v4 sous v5
tr = t(); c1 = ch("N1a"); L.creer_registre(c1); a = courir(c1, tr); c2 = ch("N1b"); L.creer_registre(c2); b = courir(c2, tr)
note("N1 registre neuf ailleurs, via _courir (fonction de module, chemins libres)", [a, b], tr.facture, "le chemin dur ne vaut que pour courir_pilote")
tr = t(); c = ch("N2"); L.creer_registre(c); a = courir(c, tr)
premiere = open(c.registre, "rb").readline(); open(c.registre, "wb").write(premiere); RG_s = None
try: b = courir(c, tr)
except Exception as ex: b = type(ex).__name__
note("N2 tronqué sans re-sceller", [a, b], tr.facture, "refus attendu")
resceller(c, premiere)
try: b2 = courir(c, tr)
except Exception as ex: b2 = type(ex).__name__
note("K1 tronqué et re-scellé AVEC la clé (lisible par le même utilisateur) et l'ancre réécrite", [a, b, b2], tr.facture, "clé et ancre dans l'espace du même utilisateur")
# K2 : tout supprimer (registre, sceau, ancre), clé gardée, recréer
tr = t(); c = ch("K2"); L.creer_registre(c); a = courir(c, tr)
for p in (c.registre, c.sceau, c.ancre): os.remove(p)
L.creer_registre(c); b = courir(c, tr)
note("K2 registre, sceau et ancre supprimés puis recréés au même chemin", [a, b], tr.facture, "creer n'exige que l'absence des trois")
# K2b : ancre seule supprimée, ou recréée à partir d'une autre
tr = t(); c = ch("K2b"); L.creer_registre(c); os.remove(c.ancre)
try: x = courir(c, tr)
except Exception as ex: x = type(ex).__name__
note("K2b ancre seule supprimée", [x], tr.facture, "refus attendu")
# K3 : conteneur neuf — dossier d'état perdu, registre présent (poussé) ou absent (non poussé)
tr = t(); c = ch("K3"); L.creer_registre(c); a = courir(c, tr); shutil.rmtree(os.path.dirname(c.ancre))
try: x = courir(c, tr)
except Exception as ex: x = type(ex).__name__
os.remove(c.registre); os.remove(c.sceau); L.creer_registre(c); y = courir(c, tr)
note("K3 conteneur neuf : état perdu ; registre gardé, puis registre non poussé", [a, x, y], tr.facture, "sans registre durable hors du conteneur, budget neuf")
# K4 : mort entre l'ajout de la ligne et le sceau
tr = t(); c = ch("K4"); L.creer_registre(c)
orig = RG._ecrire_atomique; compte = {"n": 0}
def casse(chemin, texte):
    compte["n"] += 1
    if compte["n"] == 40: raise KeyboardInterrupt("mort entre l'ajout et le sceau")
    return orig(chemin, texte)
RG._ecrire_atomique = casse
try: a = courir(c, tr)
except KeyboardInterrupt: a = "processus tué"
RG._ecrire_atomique = orig
try: b = courir(c, tr)
except Exception as ex: b = type(ex).__name__
note("K4 mort entre l'ajout et le sceau, puis reprise", [a, b], tr.facture, "échec sûr mais course bloquée")
# N3 : deux processus
c = ch("N3"); L.creer_registre(c)
def enfant(i, q):
    class Lent(H):
        def envoyer(self, r): time.sleep(0.001); return super().envoyer(r)
    tr = Lent(PRIX, entree=pe, sortie=lambda k, mt: mt, rng=np.random.default_rng(i))
    try: q.put((L._courir(P, A.AdaptateurChatCompletions(tr, "kimi-gele"), ENT, os.path.join(D, f"j-N3-{i}.jsonl"), c, admis(tr))[0], tr.facture))
    except Exception as ex: q.put((type(ex).__name__, tr.facture))
q = mp.Queue(); ps = [mp.Process(target=enfant, args=(i, q)) for i in (1, 2)]
ps[0].start(); time.sleep(1.0); ps[1].start(); o = [q.get(), q.get()]; [p.join() for p in ps]
note("N3 deux processus", [x[0] for x in o], sum(x[1] for x in o), "verrou")
# N3b : entrelacement dans le même processus
c = ch("N3b"); L.creer_registre(c); trB = t(); rB = {}
class Declenche(H):
    def envoyer(self, r):
        if self.k == 5 and not rB:
            try: rB["c"] = L._courir(P, A.AdaptateurChatCompletions(trB, "kimi-gele"), ENT, os.path.join(D, "jB.jsonl"), c, admis(trB))[0]
            except Exception as ex: rB["c"] = type(ex).__name__
        return super().envoyer(r)
trA = Declenche(PRIX, entree=pe, sortie=lambda k, mt: mt, rng=np.random.default_rng(0)); a = courir(c, trA)
note("N3b courses entrelacées", [a, rB.get("c")], trA.facture + trB.facture, "verrou")
# N4 : plafond forgé
c = ch("N4"); os.makedirs(os.path.dirname(c.ancre)); RG.creer(c, L.parametres(10 ** 6)); tr = t()
try: x = courir(c, tr)
except Exception as ex: x = type(ex).__name__
note("N4 registre forgé à 1e6", [x], tr.facture, "")
# N5 : sous-classe ; N7 : méthode de la classe admise remplacée à l'exécution (relances cachées)
class A3(A.AdaptateurChatCompletions): pass
tr = t(); c = ch("N5"); L.creer_registre(c)
try: x = courir(c, tr, A3(tr, "kimi-gele"))
except Exception as ex: x = type(ex).__name__
note("N5 sous-classe de l'adaptateur", [x], tr.facture, "")
tr = t(); c = ch("N7"); L.creer_registre(c)
orig_app = A.AdaptateurChatCompletions.appeler
def appeler3(self, appel, texte, mt):
    for _ in range(2): self.transport.envoyer({"model": self.modele, "messages": [{"role": "user", "content": texte}], "max_tokens": mt})
    return orig_app(self, appel, texte, mt)
A.AdaptateurChatCompletions.appeler = appeler3
try: x = courir(c, tr)
finally: A.AdaptateurChatCompletions.appeler = orig_app
note("N7 méthode `appeler` de la classe admise remplacée en mémoire (fichier inchangé)", [x], tr.facture, "empreinte du fichier, pas du code chargé")
json.dump(res, open(OUT, "x"), ensure_ascii=False, indent=1)

#!/usr/bin/env python3
"""Artefacts d'attaque du contre-lecteur contre le lanceur et la garde du pilote P-std (faux client local, aucun réseau).
Usage : python -B attaques_lanceur_cl_v1.py DOSSIER_PIECES_V3 DOSSIER_JOURNAUX_NEUF SORTIE.json"""
import json, math, os, sys
ICI = sys.argv[1]; JD = sys.argv[2]; OUT = sys.argv[3]
sys.path.insert(0, ICI)
import garde_pilote_essaim_v1 as GP
import lanceur_pilote_essaim_v1 as L
import epreuves_gardes_pilote_v1 as E
os.makedirs(JD, exist_ok=False)
PRIX, _ = E.prix_kimi()
P = GP.plan_pstd()
BORNE = GP.borne_pire(P, PRIX)["pire_usd"]
res = []
def j(n): return os.path.join(JD, f"{n}.jsonl")
def note(nom, code, depense_garde, depense_reelle, commentaire, plafond=None):
    r = {"attaque": nom, "code": code, "depense_vue_par_la_garde": round(depense_garde, 4),
         "depense_reelle_du_faux_fournisseur": round(depense_reelle, 4), "borne_annoncee": BORNE,
         "borne_franchie": depense_reelle > BORNE + 1e-9 or depense_garde > BORNE + 1e-9, "plafond_de_la_course": plafond, "depense_au_dela_du_plafond_de_la_course": (plafond is not None and depense_garde > plafond + 1e-9), "commentaire": commentaire}
    res.append(r); print(json.dumps(r, ensure_ascii=False))

class Facturant(E.FauxClient):
    """Faux fournisseur qui tient sa propre facture (ce que la garde ne voit pas)."""
    def __init__(self, cache_retries=0, reflexion_hors=0, **kw):
        super().__init__(usage=kw.pop("usage", E.au_plafond), **kw); self.facture = 0.0
        self.cache_retries = cache_retries; self.reflexion_hors = reflexion_hors
    def appeler(self, appel, texte, max_tokens):
        rep = super().appeler(appel, texte, max_tokens)
        u = rep["usage"]
        # tentatives internes du kit client (max_retries) : facturées, invisibles ; jetons de réflexion rendus à part
        self.facture += (1 + self.cache_retries) * GP.cout(u["entree"], u["sortie"] + self.reflexion_hors, PRIX)
        return rep

ENT = E.entree_taille(E.ENTREE_AU_PLAFOND)

# A1 : plafond de dépense passé par l'appelant, sans contrôle contre la borne ; plan doublé accepté
P2 = P + [dict(a, id=a["id"] + "-bis") for a in P if a["role"] == "proposeur"]
c = Facturant(); code, g = L.courir(P2, c, ENT, j("A1"), PRIX, plafond_depense=10**6)
note("A1 plan doublé et plafond 1e6 acceptés par courir", code, g.depense, c.facture,
     "courir ne vérifie ni plan == plan_pstd() ni plafond <= borne(plan_pstd, prix Kimi)")

# A2 : cumul remis à zéro par une seconde invocation après un arrêt
c = Facturant(); code1, g1 = L.courir(P, c, ENT, j("A2a"), PRIX)
code2, g2 = L.courir(P, c, ENT, j("A2b"), PRIX)
note("A2 deux invocations successives (relance de course après arrêt ou fin)", (code1, code2), g1.depense + g2.depense, c.facture,
     "aucun registre de dépense persistant entre invocations : la borne vaut par appel de courir, pas par pilote")

# A3 : relances internes du kit client (ex. max_retries=2), facturées mais invisibles
c = Facturant(cache_retries=2); code, g = L.courir(P, c, ENT, j("A3"), PRIX)
note("A3 relances internes cachées dans le client (2 par appel)", code, g.depense, c.facture,
     "H1 violée sans signal : la garde ne compte que les relances qu'elle voit")

# A4 : jetons de réflexion facturés hors du champ « sortie » rendu par l'adaptateur
c = Facturant(reflexion_hors=8000); code, g = L.courir(P, c, ENT, j("A4"), PRIX)
note("A4 réflexion (8 000 jetons) facturée hors de usage.sortie", code, g.depense, c.facture,
     "H2 contrôlée seulement si l'adaptateur range la réflexion dans « sortie » : invérifiable par la garde")

# A5 : exception inattendue APRÈS facturation : l'appel n'est pas compté
class ApresFacture(Facturant):
    def appeler(self, appel, texte, max_tokens):
        rep = super().appeler(appel, texte, max_tokens)
        if self.k == 30: raise KeyError("choices")   # réponse facturée mais mal lue
        return rep
c = ApresFacture(); code, g = L.courir(P, c, ENT, j("A5"), PRIX)
lig = [json.loads(x) for x in open(j("A5"))][-1]
note("A5 erreur inattendue après facturation (code 17)", code, lig["depense_usd"], c.facture,
     "l'appel en cours n'est pas compté à sa réserve au code 17 : dépense journalisée sous-estimée d'un appel")

# A6 : prix nuls (ou faux) passés à courir : garde de dépense vide
c = Facturant(); code, g = L.courir(P, c, ENT, j("A6"), (0.0, 0.0))
note("A6 prix (0, 0) acceptés", code, g.depense, c.facture, "prix non vérifiés contre tarifs() à l'empreinte")

# A7 : sortie négative : coût négatif ramené à 0, appel compté 0 au lieu de sa réserve
c = Facturant(usage=E.modifie_au(3, "sortie", -24000, base=E.au_plafond)); code, g = L.courir(P, c, ENT, j("A7"), PRIX)
note("A7 usage à sortie négative", code, g.depense, c.facture, "arrêt 16 correct mais l'appel anormal n'est pas compté à sa réserve")

# A8 : entrée réelle bien plus grosse que le texte (adaptateur qui ajoute l'historique) près du plafond : dépassement
class GrosseEntree(Facturant):
    def appeler(self, appel, texte, max_tokens):
        rep = super().appeler(appel, texte, max_tokens)
        if self.k == 743: rep["usage"]["entree"] = 256000; self.facture += GP.cout(256000 - 23200, 0, PRIX)
        return rep
c = GrosseEntree(); code, g = L.courir(P, c, ENT, j("A8"), PRIX, plafond_depense=176.6)
note("A8 dernier appel rendu à 256 000 jetons d'entrée (fenêtre), cumul près du plafond (176,6)", code, g.depense, c.facture,
     "garde après coup : un appel hors H3 franchit le plafond de la course avant l'arrêt ; son excès n'est borné que par la fenêtre de contexte", plafond=176.6)

# A9 : relance d'un message sous un rôle de proposeur (même identifiant) par l'API Garde
g = GP.Garde(P, PRIX); msg = next(a for a in P if a["role"] == "message")
for a in P[:P.index(msg)]:
    g.avant(a, "x", 10); g.apres(a, {"entree": 1, "sortie": 1})
g.avant(msg, "x", 2000); g.echec(msg)
try:
    g.avant(dict(msg, role="proposeur"), "x" * 60000, 24000); code = 0
except GP.ArretCourse as ex: code = ex.code
note("A9 relance d'un message déguisé en proposeur (24 000 jetons, 60 000 octets)", code, g.depense, 0.0,
     "la relance ne compare que l'identifiant, pas l'entrée du plan : plafonds du mauvais rôle acceptés")

# A10 : abandons sans limite (relancer=False) : échecs non comptés comme relances
c = Facturant(echecs=range(0, 10**6)); code, g = L.courir(P, c, ENT, j("A10"), PRIX, relancer=False)
note("A10 tous les appels échouent, relancer=False", code, g.depense, c.facture,
     f"échecs abandonnés hors du compte des relances ; arrêt seulement par la dépense ; relances={g.relances}")
json.dump(res, open(OUT, "x"), ensure_ascii=False, indent=1, sort_keys=True)

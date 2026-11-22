#!/usr/bin/env python3
"""Épreuves (R5) du lanceur v2, de la garde v2, du registre et du gabarit d'adaptateur, sur le faux fournisseur qui tient sa
propre facture. Chaque garde : un cas sain et au moins un artefact qui doit la déclencher. Rejoue aussi, sous leur forme v4,
les attaques A1 à A10 de la contre-lecture de la v3 (`devis-et-instruments-v3/contre-lecture-v1/outils/attaques_lanceur_cl_v1.py`).
Critère de chaque cas : code attendu ; ligne d'arrêt au journal ; dépense comptée ≥ facture du faux fournisseur (la garde ne
sous-compte jamais), sauf cas déclaré « limite » ; dépense comptée ≤ plafond, sauf cas déclaré « limite ».
Aucun appel, aucun réseau. Graines : SeedSequence(20261125).spawn(16) (R9).
Usage : python -I -B epreuves_lanceur_pilote_v2.py SORTIE.json DOSSIER_NEUF"""
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import adaptateur_fournisseur_v1 as A  # noqa: E402
import faux_fournisseur_v1 as F  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import lanceur_pilote_essaim_v2 as L  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402

RACINE_GRAINES = 20261125
P = GP.plan_pstd()
PRIX = GP.PRIX_GELES
BORNE = GP.borne_pire(P, PRIX)["pire_usd"]
ENTREE_ATTENDUE = {"proposeur": int((9000 + 3200) * 3.3), "message": int(3000 * 3.3)}
ENTREE_AU_PLAFOND = dict(GP.PLAFOND_ENTREE_OCTETS)
SS = np.random.SeedSequence(RACINE_GRAINES).spawn(16)


def entree(octets):
    return lambda appel: "x" * octets[appel["role"]]


def au_plafond_entree(k, texte):
    return GP.PLAFOND_ENTREE_JETONS["proposeur"] if len(texte) > 20000 else GP.PLAFOND_ENTREE_JETONS["message"]


def au_plafond_sortie(k, mt):
    return mt


class TransportAvecTentatives(F.FauxFournisseur):
    """Le transport réel doit rendre le nombre d'envois HTTP faits (« tentatives ») ; le faux le rend aussi."""

    def envoyer(self, requete):
        rep = F.FauxFournisseur.envoyer(self, requete)
        rep.setdefault("tentatives", 1 + self._relances_reelles)
        return rep


def ff(i=0, **kw):
    kw.setdefault("rng", np.random.default_rng(SS[i]))
    return TransportAvecTentatives(PRIX, **kw)


def adapt(t):
    return A.AdaptateurChatCompletions(t, "kimi-gele")


def courir_cas(d, nom, transport, ent, plafond_registre=None, creer=True, invocations=1, **kw):
    reg = os.path.join(d, f"registre-{nom}.jsonl")
    if creer:
        L.creer_registre(reg, plafond_registre)
    codes, g = [], None
    for i in range(invocations):
        ad = transport if not isinstance(transport, F.FauxFournisseur) else adapt(transport)
        try:
            code, g2 = L.courir(P, ad, ent, os.path.join(d, f"journal-{nom}-{i}.jsonl"), reg, **kw)
            g = g2 or g  # une invocation refusée avant la garde ne remet pas la dépense déjà comptée à zéro
        except KeyboardInterrupt:
            code = "processus tué"
        codes.append(code)
    return codes, g, reg


def resultat(nom, garde_visee, codes, attendu, g, transport, d, limite=None, plafond=None):
    facture = getattr(transport, "facture", 0.0) if transport is not None else 0.0
    dep = g.depense if g is not None else 0.0
    plaf = g.plafond_depense if g is not None else plafond
    sous_compte = facture > dep + 1e-9
    au_dela = plaf is not None and dep > plaf + 1e-9
    tenu = codes == attendu and (limite is not None or (not sous_compte and not au_dela))
    return {"cas": nom, "garde": garde_visee, "codes_attendus": attendu, "codes_rendus": codes, "depense_comptee_usd": round(dep, 6),
            "facture_du_faux_fournisseur_usd": round(facture, 6), "plafond_usd": plaf, "sous_compte": sous_compte,
            "au_dela_du_plafond": au_dela, "limite_declaree": limite, "tenu": tenu}


def jouer(d):
    os.makedirs(d)
    R = []

    def cas(nom, garde, attendu, transport, ent=entree(ENTREE_ATTENDUE), limite=None, **kw):
        codes, g, reg = courir_cas(d, nom, transport, ent, **kw)
        R.append(resultat(nom, garde, codes, attendu, g, transport, d, limite))
        return reg

    # --- sains ---
    cas("sain : P-std entier, faux fournisseur réaliste", "toutes", [0], ff(0))
    cas("sain : tout au plafond de jetons", "sortie, entrée, dépense", [0], ff(1, entree=au_plafond_entree, sortie=au_plafond_sortie), ent=entree(ENTREE_AU_PLAFOND))
    cas("sain : 74 échecs relancés", "échecs", [0], ff(2, erreurs_aux=range(0, 148, 2)))
    cas("sain : pire extrême (plafonds, 74 échecs facturés au plafond)", "dépense", [0],
        ff(3, entree=au_plafond_entree, sortie=au_plafond_sortie, erreurs_aux=range(0, 148, 2), erreur_facturee=True), ent=entree(ENTREE_AU_PLAFOND))

    class Tueur(TransportAvecTentatives):
        def envoyer(self, requete):
            rep = TransportAvecTentatives.envoyer(self, requete)
            if self.k == 101 and not getattr(self, "tue", False):
                self.tue = True
                raise KeyboardInterrupt("processus tué après facturation")
            return rep
    cas("sain : processus tué pendant l'appel 101 puis reprise (réserve en suspens comptée)", "registre persistant", ["processus tué", 0],
        Tueur(PRIX, rng=np.random.default_rng(SS[4])), invocations=2)
    # --- A1, A6 : configuration ---
    P2 = P + [dict(a, id=a["id"] + "-bis") for a in P if a["role"] == "proposeur"]
    t = ff(5)
    reg = os.path.join(d, "registre-A1.jsonl")
    L.creer_registre(reg)
    code, g = L.courir(P2, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-A1.jsonl"), reg, plafond_depense=10 ** 6)
    R.append(resultat("A1 plan doublé et plafond 1e6", "plan", [code], [15], g, t, d))
    code, g = L.courir(P, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-A1b.jsonl"), reg, plafond_depense=10 ** 6)
    R.append(resultat("A1b bon plan, plafond 1e6", "configuration", [code], [24], g, t, d))
    code, g = L.courir(P, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-A6.jsonl"), reg, prix=(0.0, 0.0))
    R.append(resultat("A6 prix (0, 0)", "configuration", [code], [24], g, t, d))
    try:
        L.creer_registre(os.path.join(d, "registre-plafond-haut.jsonl"), BORNE + 1)
        R.append({"cas": "registre créé au-dessus de la borne", "tenu": False})
    except GP.ArretCourse as ex:
        R.append({"cas": "registre créé au-dessus de la borne", "garde": "configuration", "codes_attendus": [24], "codes_rendus": [ex.code], "tenu": ex.code == 24})
    # --- A2 et registre ---
    t = ff(6)
    cas("A2 seconde invocation après une fin", "course close", [0, 23], t, invocations=2)
    t = ff(7)
    cas("registre absent", "registre", [21], t, creer=False)
    t = ff(8)
    reg = cas("registre altéré : ligne du milieu modifiée, sceau laissé", "registre", [23], t)  # la course finit : fin écrite (close)
    lignes = open(reg, encoding="utf-8").read().splitlines()
    k = next(i for i, l in enumerate(lignes) if '"evenement": "regle"' in l and i > 2)
    assert '"cout_usd": ' in lignes[k]
    lignes[k] = lignes[k].replace('"cout_usd": ', '"cout_usd": 0.0, "x": ', 1)
    open(reg, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    code, g = L.courir(P, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-altere.jsonl"), reg)
    R[-1].update(codes_rendus=[code], codes_attendus=[22], tenu=code == 22)
    # registre altéré puis RE-SCELLÉ : la chaîne doit le voir (ligne du milieu)
    reg2 = os.path.join(d, "registre-rescelle.jsonl")
    L.creer_registre(reg2)

    class Tueur2(TransportAvecTentatives):
        def envoyer(self, requete):
            if self.k == 30 and not getattr(self, "tue", False):
                self.tue = True
                raise KeyboardInterrupt
            return TransportAvecTentatives.envoyer(self, requete)
    t = Tueur2(PRIX, rng=np.random.default_rng(SS[9]))
    try:
        L.courir(P, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-rescelle-0.jsonl"), reg2)
    except KeyboardInterrupt:
        pass
    lignes = open(reg2, encoding="utf-8").read().splitlines()
    k = next(i for i, l in enumerate(lignes) if '"evenement": "regle"' in l and i > 2)
    assert '"cout_usd": ' in lignes[k] and k < len(lignes) - 2
    lignes[k] = lignes[k].replace('"cout_usd": ', '"cout_usd": 0.0, "x": ', 1)
    open(reg2, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    RG._sceller(reg2)
    code, g = L.courir(P, adapt(t), entree(ENTREE_ATTENDUE), os.path.join(d, "journal-rescelle-1.jsonl"), reg2)
    R.append({"cas": "registre altéré puis re-scellé (ligne du milieu)", "garde": "registre", "codes_attendus": [22], "codes_rendus": [code], "tenu": code == 22})
    # --- A3 : relances internes ---
    t = ff(10, relances_internes=2)
    try:
        adapt(t)
        R.append({"cas": "A3 relances internes déclarées (2)", "tenu": False})
    except A.ConfigurationRefusee:
        R.append({"cas": "A3 relances internes déclarées (2) : adaptateur refusé à la construction", "garde": "configuration",
                  "codes_attendus": ["refus"], "codes_rendus": ["refus"], "tenu": True, "facture_du_faux_fournisseur_usd": t.facture})
    cas("A3b relances internes cachées (déclarées 0), tentatives rendues 3", "facturation hors borne", [16], ff(11, relances_internes=2, relances_declarees=0))

    class SansTentatives(F.FauxFournisseur):
        pass
    cas("A3c transport qui ne rend pas ses tentatives", "facturation hors borne", [16], SansTentatives(PRIX, rng=np.random.default_rng(SS[12])))
    # --- A4 : réflexion ---
    cas("A4 réflexion (8 000) facturée hors de completion_tokens", "sortie", [10], ff(13, entree=au_plafond_entree, sortie=au_plafond_sortie, reflexion_hors=8000), ent=entree(ENTREE_AU_PLAFOND))
    cas("A4b réflexion du détail au-delà de completion_tokens", "sortie", [10], ff(13, sortie=lambda k, mt: 9000, reflexion_detail_hors=8000))
    cas("A4c réflexion hors compte sous le plafond, au-delà du max_tokens envoyé", "facturation hors borne", [16],
        ff(13, sortie=lambda k, mt: 15000, reflexion_hors=1001), max_tokens_par_role={"proposeur": 16000})
    # --- A5, A7 : exceptions et usages anormaux ---
    cas("A5 panne après facturation (appel 30)", "erreur après envoi", [17], ff(14, panne_apres_facture_au=30))
    cas("A7 sortie négative (appel 3)", "facturation hors borne", [16], ff(14, usage_negatif_au=3))
    cas("A7b usage absent (appel 7)", "facturation hors borne", [16], ff(14, usage_absent_au=7))
    cas("modèle servi différent (repli)", "facturation hors borne", [16], ff(14, modele_servi="autre-modele"))
    # --- A8 : entrée hors H3 ---
    cas("A8 entrée rendue 256 000 jetons au dernier appel, plafond 176,6", "entrée", [11],
        ff(15, entree=lambda k, tx: 256000 if k == 743 else au_plafond_entree(k, tx), sortie=au_plafond_sortie), ent=entree(ENTREE_AU_PLAFOND),
        plafond_registre=176.6, limite="un appel hors H3 n'est borné que par la fenêtre du modèle : la limite chez le fournisseur couvre ce cas")
    # --- A10 : abandons ---
    cas("A10 tous les appels échouent, relancer=False", "échecs", [13], ff(0, erreurs_aux=range(0, 10 ** 6)), relancer=False)
    # --- gardes de la v1, sous la v2 ---
    cas("max_tokens 24 001 demandé", "sortie", [10], ff(1), max_tokens_par_role={"proposeur": 24001})
    cas("entrée de 64 961 octets", "entrée", [11], ff(1), ent=entree({"proposeur": GP.PLAFOND_ENTREE_OCTETS["proposeur"] + 1, "message": 9900}))
    cas("sortie rendue 24 001", "sortie", [10], ff(1, sortie=lambda k, mt: 24001 if k == 100 else min(6000, mt)))
    cas("entrée rendue 5 000 pour 1 000 octets (H3)", "facturation hors borne", [16], ff(1, entree=lambda k, tx: 5000 if k == 3 else 300),
        ent=entree({"proposeur": 1000, "message": 1000}))
    cas("75 échecs relancés", "échecs", [13], ff(2, erreurs_aux=range(0, 150, 2)))
    cas("plafond du registre abaissé à 50 USD", "dépense", [14], ff(0), plafond_registre=50.0)
    codes, g, _ = courir_cas(d, "sans-adaptateur", None, entree(ENTREE_ATTENDUE))
    R.append(resultat("aucun adaptateur", "client", codes, [20], g, None, d))
    t = ff(0)
    reg = os.path.join(d, "registre-client-nu.jsonl")
    L.creer_registre(reg)
    code, g = L.courir(P, t, entree(ENTREE_ATTENDUE), os.path.join(d, "journal-client-nu.jsonl"), reg)
    R.append(resultat("couche d'appel nue (sans adaptateur vérifié)", "configuration", [code], [24], g, t, d))
    # --- garde directe : plan, messages, relance déguisée (A9) ---
    def direct(nom, garde, attendu, f):
        try:
            f()
            code = 0
        except GP.ArretCourse as ex:
            code = ex.code
        R.append({"cas": nom, "garde": garde, "codes_attendus": [attendu], "codes_rendus": [code], "tenu": code == attendu})
    g = GP.Garde(P, PRIX, BORNE)
    msg = next(a for a in P if a["role"] == "message")
    for a in P[:P.index(msg)]:
        g.avant(a, "x", 10)
        g.apres(a, {"entree": 1, "sortie": 1})
    g.avant(msg, "x", 2000)
    g.echec(msg)
    direct("A9 relance d'un message déguisé en proposeur", "plan", 15, lambda: g.avant(dict(msg, role="proposeur"), "x" * 60000, 24000))
    direct("sain : relance identique du message", "plan", 0, lambda: g.avant(msg, "x", 2000))
    plan13 = list(P)
    i = max(k for k, a in enumerate(plan13) if a["monde"] == 0 and a["role"] == "message")
    plan13.insert(i + 1, {"id": "w00-a-g3-message-99", "monde": 0, "bras": "a", "generation": 3, "role": "message"})

    def treize():
        g2 = GP.Garde(plan13, PRIX, 10 ** 6)
        for a in plan13:
            g2.avant(a, "x", 10)
            g2.apres(a, {"entree": 1, "sortie": 1})
    direct("13e message d'un monde (plan fautif, garde directe)", "messages", 12, treize)
    direct("appel hors plan", "plan", 15, lambda: GP.Garde(P, PRIX, BORNE).avant(P[5], "x", 10))
    # adaptateur seul, cas sain : réflexion comprise dans completion_tokens
    t = TransportAvecTentatives(PRIX, sortie=5000, rng=np.random.default_rng(SS[0]))
    rep = adapt(t).appeler(P[0], "x" * 330, 24000)
    R.append({"cas": "sain : adaptateur, usage rendu (entrée 100, sortie 5 000)", "garde": "adaptateur", "codes_attendus": [{"entree": 100, "sortie": 5000}],
              "codes_rendus": [rep["usage"]], "tenu": rep["usage"] == {"entree": 100, "sortie": 5000}})
    try:
        adapt(A.TransportNonCable()).appeler(P[0], "x", 10)
        R.append({"cas": "transport non câblé", "tenu": False})
    except A.ConfigurationRefusee:
        R.append({"cas": "transport non câblé : refus à l'envoi", "garde": "adaptateur", "codes_attendus": ["refus"], "codes_rendus": ["refus"], "tenu": True})
    return R


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[1]) or os.path.exists(argv[2]):
        print("usage : epreuves_lanceur_pilote_v2.py SORTIE.json DOSSIER (neufs)", file=sys.stderr)
        return 2
    R = jouer(argv[2])
    out = {"version": "epreuves-lanceur-pilote-v2", "graines": f"SeedSequence({RACINE_GRAINES}).spawn(16)", "numpy": np.__version__,
           "prix_geles": list(PRIX), "prix_de_la_table": list(L.prix_de_la_table()), "plan_sha256": GP.PLAN_SHA256,
           "borne_pire_pstd": GP.borne_pire(P, PRIX), "cas": R, "tenus": sum(bool(r.get("tenu")) for r in R), "total": len(R)}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    for r in R:
        print("TENU  " if r.get("tenu") else "CASSÉ ", r.get("codes_attendus"), r.get("codes_rendus"), r["cas"],
              r.get("depense_comptee_usd", ""), r.get("facture_du_faux_fournisseur_usd", ""))
    print(json.dumps(out["borne_pire_pstd"], ensure_ascii=False))
    return 0 if all(r.get("tenu") for r in R) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

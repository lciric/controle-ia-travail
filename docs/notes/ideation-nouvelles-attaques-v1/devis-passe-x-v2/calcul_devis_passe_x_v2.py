#!/usr/bin/env python3
"""Devis de la passe X rallongée (dix-sept questions), course « nouvelles attaques » — v2.

Remplace calcul_devis_passe_x_v1.py (archivé sans changement). Processeur seul : aucun appel
de modèle, aucun réseau, aucune clé lue. Usage : python -I calcul_devis_passe_x_v2.py SORTIE.json
Montants en Decimal ; un coût s'arrondit au centime supérieur, une part ou une marge au centime inférieur.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR

M = "/home/user/main-lecture"
DOSSIER = M + "/docs/notes/demandes-fable-api-2026-11-22-v1/"
# Ordre de la liste fermée de GO-2026-11-22-46 (go.md l. 733) : les sept servies, le lot, les huit jamais servies.
PIECES = [
    "question-neutre-modes-attaque-servie-v1.md",
    "question-neutre-modes-attaque-ajout-organisme-v1.md",
    "question-neutre-billet-drapeau-servie-v2.md",
    "question-neutre-coeurs-algorithmiques-servie-v2.md",
    "question-neutre-etau-equipe-rouge-servie-v3.md",
    "question-neutre-questions-concurrents-servie-v1.md",
    "question-neutre-theoreme-negatif-servie-v2.md",
    "question-neutre-tirage-au-hasard-servie-v1.md",
    "question-neutre-lot-quarantaine-servie-v1.md",
    "question-neutre-generale-v2.md",
    "question-neutre-papier-a-v2.md",
    "question-neutre-papier-b-v2.md",
    "question-neutre-papier-c-v2.md",
    "question-neutre-revendications-v2.md",
    "question-neutre-taches-sabotage-v2.md",
    "question-neutre-these-boite-blanche-v2.md",
    "question-neutre-etau-v2.md",
]
EMPREINTES_ADDITIF = {  # additif v2 l. 23-24
    "question-neutre-modes-attaque-servie-v1.md": "02ad3d76ae90648f2fbb8498bc109d4a51a9dddd8b965e03326013e9ee08c9b8",
    "question-neutre-modes-attaque-ajout-organisme-v1.md": "8c54752fef44683a7f25e079e22344589e3306130a69eb166333f870a8761669",
}
# Séparateur proposé, déclaré à l'enveloppe (K-2 (5)), hors des corps : une ligne par pièce.
SEPARATEUR = "[Pièce {k} sur 17]"

ENVELOPPE_OCTETS = 512
SPJ_ATTENDU, SPJ_HAUT = D(3), D(2)
PIRE_SCELLE = D("6.05")            # DV l. 63, l. 119 ; AV l. 129 (P4), l. 143 (P15)
PLAFOND_GO_46 = D(200)             # go.md l. 733
TEXTE_VISE = 32000
TEXTE_MIN_GOOGLE = 16000           # AV l. 111 (G-6)
P_OUT = 96000
# Sorties maximales par famille (paramètre) : None = à relever. AN l. 7-8 et l. 10 (interface synchrone).
SORTIE_MAX = {"opus46": 128000, "sonnet46": 128000, "google": None, "openai": None, "claude_course": None, "kimi": None}
FRACTION = {"attendu": D("0.4"), "haut": D("0.8"), "pire": D(1)}

T = {
    "google": {"attendu": (D(2), D(10)), "haut": (D(4), D(20)), "pire": (D("8.3"), D("41.5"))},
    "openai": {k: (D(10), D(50)) for k in FRACTION},
    "claude_course": {k: (D(10), D(50)) for k in FRACTION},
    "kimi": {k: (D(2), D(10)) for k in FRACTION},
    "opus46": {k: (D(5), D(25)) for k in FRACTION},
    "sonnet46": {k: (D(3), D(15)) for k in FRACTION},
}
SOURCES_TARIFS = {
    "google": "RQ l. 25, l. 26, l. 28 (cités, non vérifiés)",
    "openai": "RQ l. 29 (repris par citation)",
    "claude_course": "RQ l. 31 (plus haut tarif Claude cité ; identité des espèces 3 et 4 hors des pièces lues)",
    "kimi": "TK l. 10-11 (vérifié sur page gardée)",
    "opus46": "AN l. 7 (page officielle gardée, lue le 2026-11-22T11:53Z)",
    "sonnet46": "AN l. 8 (page officielle gardée, lue le 2026-11-22T11:53Z)",
}
CLE_LUC = "Luc (R-4852, sous GO-2026-11-22-46)"
PROPOSEURS = [
    ("espece_1", "google", "deuxième relais (Google)", ["google"]),
    ("espece_2", "openai", "troisième relais (OpenAI)", ["openai"]),
    ("espece_3", "claude_course", CLE_LUC, ["claude_course", "opus46", "sonnet46"]),
    ("espece_4", "claude_course", CLE_LUC, ["claude_course", "opus46", "sonnet46"]),
    ("espece_5", "google", "deuxième relais (Google)", ["google"]),
    ("ajout_kimi", "kimi", "KIMI_API_KEY (par son nom)", ["kimi"]),
    ("ajout_opus46", "opus46", CLE_LUC, ["opus46", "opus46", "sonnet46"]),
    ("ajout_sonnet46", "sonnet46", CLE_LUC, ["sonnet46", "opus46", "sonnet46"]),
]
SAUT = {"ajout_opus46": ["opus46", "sonnet46"], "ajout_sonnet46": ["sonnet46"]}

# Luc (B2)
LUC_RESTE_DECLARE = D("153")        # PL l. 39-41 (R-4647, « environ 153 »)
LUC_PART_FIXEE = D("125.63")        # CV l. 115
LUC_PART_RELEVABLE = D("136.04")    # AV l. 162 ; GO-42 (go.md l. 729)
LUC_HAUT_ROLES = D("124.35")        # CV l. 115-116
FABLE_SUR_LUC = {                   # GO-2026-11-22-45, go.md l. 732
    "demande 27 (GO-40)": D(8), "relance 22, 23, 24 (GO-43)": D(17), "mathématiques (GO-43)": D(50),
    "banc à vérité plantée (devis 4ac3a214…)": D(24), "chantiers du 21 (GO-29, GO-40)": D(18),
}
FABLE_NON_CHIFFREES = "demandes 28, 29, 30 (GO-42) : plafond non écrit à go.md l. 732"


def cu(x):
    return str(x.quantize(D("0.01"), rounding=ROUND_CEILING))


def fl(x):
    return str(x.quantize(D("0.01"), rounding=ROUND_FLOOR))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def corps(t):
    lignes = t.split("\n")
    titre = lignes[0] if lignes and lignes[0].startswith("#") else None
    if titre is not None:
        lignes = lignes[1:]
    return "\n".join(lignes).strip("\n"), titre


def lire():
    rap, corps_l = [], []
    for k, nom in enumerate(PIECES, 1):
        b = open(DOSSIER + nom, "rb").read()
        t = b.decode("utf-8")
        cp, titre = corps(t)
        corps_l.append(cp)
        rap.append({"rang": k, "piece": nom, "sha256": sha(b), "octets_fichier": len(b), "signes_fichier": len(t),
                    "titre_retire": titre, "titre_nomme_un_modele": bool(titre and re.search(r"Fable|Opus|Neon|Kimi|Claude", titre)),
                    "signes_corps": len(cp), "octets_corps": len(cp.encode()),
                    "quarantaine_corps": len(re.findall("quarantaine", cp, re.I)),
                    "lignes_numerotees_corps": re.findall(r"(?m)^(\d+)\.", cp)})
    return rap, corps_l


def fusion(corps_l, separateurs):
    if not separateurs:
        return "\n\n".join(corps_l) + "\n"
    return "\n\n".join(SEPARATEUR.format(k=k) + "\n\n" + c for k, c in enumerate(corps_l, 1)) + "\n"


def jin(texte):
    s, b = len(texte) + ENVELOPPE_OCTETS, len(texte.encode()) + ENVELOPPE_OCTETS
    return {"attendu": int((D(s) / SPJ_ATTENDU).to_integral_value(ROUND_CEILING)),
            "haut": int((D(s) / SPJ_HAUT).to_integral_value(ROUND_CEILING)), "pire": b}


def cout(fam, cas, ji, jo):
    pi, po = T[fam][cas]
    return (D(ji) * pi + D(jo) * po) / D(10**6)


def devis(j, plafonds=None, lecture="litterale", props=PROPOSEURS, requetes=1, pire_google=None):
    plafonds = plafonds or {}
    lignes, cles = [], {}
    tot = dict.fromkeys(("attendu", "haut", "pire_calcule", "pire_de_lettre"), D(0))
    for nom, fam, cle, chaine in props:
        if lecture == "saut" and nom in SAUT:
            chaine = SAUT[nom]
        cap = lambda f: plafonds.get(f, P_OUT)
        att = cout(fam, "attendu", j["attendu"], int(cap(fam) * FRACTION["attendu"])) * requetes
        h_ch = chaine[:2] if fam in ("claude_course", "opus46") else chaine[:1]
        haut = sum(cout(f, "haut", j["haut"], int(cap(f) * FRACTION["haut"])) for f in h_ch) * requetes
        pires = [cout(f, "pire", j["pire"], cap(f)) for f in chaine]
        if pire_google is not None and fam == "google":
            pires = [D(pire_google)]
        lettre = [max(PIRE_SCELLE, x) for x in pires]
        p, pl = sum(pires) * requetes, sum(lettre) * requetes
        lignes.append({"proposeur": nom, "cle": cle, "chaine": chaine, "tentatives_au_pire": len(chaine) * requetes,
                       "pire_par_tentative_calcule_usd": [cu(x) for x in pires],
                       "attendu_usd": cu(att), "haut_usd": cu(haut), "pire_calcule_usd": cu(p), "pire_de_lettre_usd": cu(pl)})
        for k, v in zip(tot, (att, haut, p, pl)):
            tot[k] += v
        c = cle.split(" (")[0]
        cles.setdefault(c, dict.fromkeys(("attendu", "pire_calcule", "pire_de_lettre"), D(0)))
        cles[c]["attendu"] += att
        cles[c]["pire_calcule"] += p
        cles[c]["pire_de_lettre"] += pl
    return {"lecture_des_chaines": lecture, "requetes_par_proposeur": requetes,
            "plafonds_de_sortie": {f: plafonds.get(f, P_OUT) for f in T},
            "par_proposeur": lignes, "tentatives_au_pire": sum(x["tentatives_au_pire"] for x in lignes),
            "totaux_usd": {k: cu(v) for k, v in tot.items()},
            "par_cle_usd": {c: {k: cu(v) for k, v in d.items()} for c, d in cles.items()},
            "marge_sous_200_usd": fl(PLAFOND_GO_46 - tot["pire_de_lettre"]),
            "_pl": tot["pire_de_lettre"], "_cles_pl": sum(d["pire_de_lettre"] for d in cles.values())}


def nettoie(d):
    return {k: v for k, v in d.items() if not k.startswith("_")}


def luc(dv):
    px = {k: D(v) for k, v in dv["par_cle_usd"]["Luc"].items()}
    fable = sum(FABLE_SUR_LUC.values())
    out = {"fable_sur_luc_au_moins_usd": cu(fable), "fable_detail_usd": {k: cu(v) for k, v in FABLE_SUR_LUC.items()},
           "fable_non_chiffrees": FABLE_NON_CHIFFREES, "reste_declare_usd": cu(LUC_RESTE_DECLARE),
           "passe_x_sur_luc_usd": {k: cu(v) for k, v in px.items()}}
    # Lecture scellée : part = reste − pire des lots non clos (R-4289, CV l. 111) ; nœud sous 124,35 (CV l. 116).
    sc = {}
    for nom, lots in (("fable_seule", fable), ("fable_et_passe_x_avant_course_pire_de_lettre", fable + px["pire_de_lettre"]),
                      ("fable_et_passe_x_avant_course_pire_calcule", fable + px["pire_calcule"])):
        part = LUC_RESTE_DECLARE - lots
        sc[nom] = {"lots_non_clos_usd": cu(lots), "part_r_4289_usd": fl(part),
                   "sous_le_haut_124_35_noeud_L_2": part < LUC_HAUT_ROLES,
                   "manque_sous_le_haut_usd": cu(max(D(0), LUC_HAUT_ROLES - part)),
                   "arret_11_reste_moins_part_fixee_usd": fl(part - LUC_PART_FIXEE) if part >= LUC_PART_FIXEE else "-" + cu(LUC_PART_FIXEE - part)}
    out["lecture_scellee_sans_compte_payant"] = sc
    # Lecture « compte payant à recharge automatique » (comme R-4303 pour OpenAI) : le reste ne borne plus ;
    # l'engagement au pire se paie au-delà du reste déclaré par la recharge.
    cp = {}
    for part_nom, part in (("part_125_63", LUC_PART_FIXEE), ("part_136_04", LUC_PART_RELEVABLE)):
        eng = part + fable + px["pire_de_lettre"]
        cp[part_nom] = {"engagement_au_pire_usd": cu(eng), "au_dela_du_reste_declare_usd": cu(max(D(0), eng - LUC_RESTE_DECLARE)),
                        "sans_passe_x_au_dela_usd": cu(max(D(0), part + fable - LUC_RESTE_DECLARE))}
    out["lecture_compte_payant"] = cp
    out["reste_apres_course_si_part_136_04_consommee_usd"] = fl(LUC_RESTE_DECLARE - LUC_PART_RELEVABLE)
    out["reste_apres_course_au_cas_haut_usd"] = fl(LUC_RESTE_DECLARE - LUC_HAUT_ROLES)
    return out


def main(sortie):
    rap, corps_l = lire()
    f_sans, f_avec = fusion(corps_l, False), fusion(corps_l, True)
    j_sans, j_avec = jin(f_sans), jin(f_avec)
    rec = devis(j_avec)
    saut = devis(j_avec, lecture="saut")
    # borne : plus grand plafond tel qu'une tentative à 10/50 reste ≤ 6,05
    borne = int((PIRE_SCELLE - D(j_avec["pire"]) * 10 / D(10**6)) * D(10**6) / 50)
    google_max_hyp = [65536, 96000, 128000]
    g_rows = [{"sortie_max_hypothese": m, "plafond_effectif": min(P_OUT, m),
               "reflexion_au_plus": min(P_OUT, m) - TEXTE_VISE,
               "texte_garanti_ge_16000": min(P_OUT, m) - (min(P_OUT, m) - TEXTE_VISE) >= TEXTE_MIN_GOOGLE} for m in google_max_hyp]
    fixe_hors_google = D(14) * PIRE_SCELLE
    out = {
        "piece_fusionnee_avec_separateurs_recommandee": {"sha256": sha(f_avec.encode()), "signes": len(f_avec), "octets": len(f_avec.encode()),
                                                         "separateur": SEPARATEUR, "entree_jetons": j_avec},
        "piece_fusionnee_sans_separateurs_v1": {"sha256": sha(f_sans.encode()), "signes": len(f_sans), "octets": len(f_sans.encode()), "entree_jetons": j_sans},
        "pieces": rap,
        "titres_retires": sum(1 for r in rap if r["titre_retire"]),
        "titres_retires_qui_ne_nomment_aucun_modele": [r["piece"] for r in rap if r["titre_retire"] and not r["titre_nomme_un_modele"]],
        "listes_numerotees": {r["rang"]: r["lignes_numerotees_corps"] for r in rap if r["lignes_numerotees_corps"]},
        "plafond_de_sortie": {"propose_jetons": P_OUT, "texte_vise": TEXTE_VISE, "borne_sous_6_05_a_10_50": borne,
                              "google_selon_sortie_maximale_hypothetique": g_rows,
                              "sorties_maximales": {f: (m if m is not None else "à relever") for f, m in SORTIE_MAX.items()}},
        "tarifs_sources": SOURCES_TARIFS,
        "devis_recommande": nettoie(rec),
        "devis_lecture_saut": nettoie(saut),
        "p_x_fonction_du_pire_google": {"formule": "P_X = 14 × 6,05 + 2 × max(6,05 ; [PIRE-G-PROPOSEUR-X])",
                                        "fixe_hors_google_usd": cu(fixe_hors_google),
                                        "pire_google_maximal_sous_200_usd": fl((PLAFOND_GO_46 - fixe_hors_google) / 2),
                                        "exemples": {g: nettoie(devis(j_avec, pire_google=D(g)))["totaux_usd"]["pire_de_lettre"] for g in ("6.05", "8", "12")}},
        "options": {k: nettoie(v) for k, v in {
            "sortie_64000": devis(j_avec, plafonds=dict.fromkeys(T, 64000)),
            "sortie_128000": devis(j_avec, plafonds=dict.fromkeys(T, 128000)),
            "sans_les_deux_ajouts_claude": devis(j_avec, props=PROPOSEURS[:6]),
            "cinq_especes_seules": devis(j_avec, props=PROPOSEURS[:5]),
            "deux_requetes_de_64000": devis(jin(f_avec[: len(f_avec) // 2]), plafonds=dict.fromkeys(T, 64000), requetes=2),
        }.items()},
        "luc": luc(nettoie(rec)),
    }
    # Contrôles calculés (aucun écrit en dur, aucun vrai par construction)
    shas = [r["sha256"] for r in rap]
    pires_96 = [D(x) for p in rec["par_proposeur"] for x in p["pire_par_tentative_calcule_usd"]]
    at_borne = cout("claude_course", "pire", j_avec["pire"], borne)
    at_borne1 = cout("claude_course", "pire", j_avec["pire"], borne + 1)
    controles = {
        "1_empreintes_QN_QA_egales_a_l_additif": all(rap[i]["sha256"] == EMPREINTES_ADDITIF[PIECES[i]] for i in (0, 1)),
        "2_dix_sept_pieces_d_empreintes_distinctes": len(set(shas)) == 17,
        "3_longueur_fusion_sans_separateurs_recomptee": len(f_sans) == sum(len(c) for c in corps_l) + 2 * 16 + 1,
        "4_chaque_corps_est_sous_chaine_de_la_fusion": all(c in f_avec for c in corps_l),
        "5_aucun_corps_ne_porte_quarantaine": all(r["quarantaine_corps"] == 0 for r in rap),
        "6_chaque_tentative_calculee_sous_6_05_a_96000": all(x <= PIRE_SCELLE for x in pires_96),
        "7_borne_exacte_116k": at_borne <= PIRE_SCELLE < at_borne1,
        "8_somme_par_cle_egale_total": rec["_cles_pl"] == rec["_pl"],
        "9_plafond_sous_chaque_sortie_maximale_connue": all(P_OUT <= m for m in SORTIE_MAX.values() if m is not None),
    }
    out["controles"] = controles
    out["nombre_de_controles"] = len(controles)
    assert all(controles.values()), controles
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])

#!/usr/bin/env python3
"""Devis de la passe X rallongée (dix-sept questions), course « nouvelles attaques » — v3.

Remplace calcul_devis_passe_x_v2.py (727fde9f77f06779…, archivé sans changement). Copie de la v2,
sauf :
- le bloc `luc`, recalculé en centimes entiers avec la part de la course à 260,00 (GO-2026-11-22-49) ;
- trois entrées neuves sur Luc : lignes à part (6), attaquant informé de GO-50 (12), réserve de l'étage 2 (88,36) ;
- trois contrôles neufs : corps de la fusion contre le fichier source moins sa ligne de titre ;
  bloc `luc` contre la sortie de l'additif 2, v2 ; entrées de Luc contre les entrées de l'additif 2, v2 ;
- une épreuve sur artefacts (R5) : chaque contrôle est rejoué sur une entrée altérée et doit tomber.
Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue.
Usage : python3 -B calcul_devis_passe_x_v3.py SORTIE.json
Montants du devis en Decimal ; un coût s'arrondit au centime supérieur, une part ou une marge au centime inférieur.
Montants du bloc `luc` en centimes entiers.
"""
import copy
import hashlib
import json
import re
import sys
from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR

M = "/home/user/main-lecture"
DOSSIER = M + "/docs/notes/demandes-fable-api-2026-11-22-v1/"
# Sortie du programme de l'additif 2, v2 (non scellé), lue par son chemin exact pour le contrôle 11 et le 12.
FICHIER_7 = ("/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/"
             "additif-2-complement-luc-payant-v2/calcul-additif-2-luc-v2.json")
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

# Luc (B2), lecture de la v2 : gardée pour mémoire seulement (lecture sans compte payant, écartée par GO-48).
LUC_RESTE_DECLARE = D("153")        # PL l. 39-41 (R-4647, « environ 153 »)
LUC_PART_FIXEE = D("125.63")        # CV l. 115 (caduque depuis GO-49)
LUC_HAUT_ROLES = D("124.35")        # CV l. 115-116 (aiguilleur et espèce 4)
FABLE_SUR_LUC = {                   # GO-2026-11-22-45, go.md l. 732
    "demande 27 (GO-40)": D(8), "relance 22, 23, 24 (GO-43)": D(17), "mathématiques (GO-43)": D(50),
    "banc à vérité plantée (devis 4ac3a214…)": D(24), "chantiers du 21 (GO-29, GO-40)": D(18),
}
FABLE_NON_CHIFFREES = "demandes 28, 29, 30 (GO-42) : plafond non écrit à go.md l. 732"

# Luc, v3 : entrées en centimes entiers, chacune avec sa source.
ENTREES_LUC_V3 = {
    "reste_declare": (15300, "« environ 153 restants », R-4647, PL l. 39-41 ; non relevé"),
    "part_course_go49": (26000, "GO-2026-11-22-49, go.md l. 736 : part de Luc pour la course portée à 260 USD au plus"),
    "lignes_a_part": (600, "additif 2, v2, § 5 et § 8.4 ; complément v3, § 3 (5 + 1 USD) ; clé à trancher (point n° 2)"),
    "attaquant_informe_go50": (1200, "GO-2026-11-22-50, go.md l. 737 : additif 3, sur la clé Luc, environ 12 USD"),
    "reserve_etage_2": (8836, "additif 2, v2, § 2 et § 8.4 ; complément v3, § 3 (R-4293) ; au plus"),
}
# Correspondance entre les entrées de ce programme et celles du fichier 7 (contrôle 12).
CORRESPONDANCE_FICHIER_7 = {
    "reste_declare": "reste_luc_declare", "part_course_go49": "part_luc_go49",
    "lignes_a_part": "plafond_lignes_a_part", "attaquant_informe_go50": "attaquant_informe_go50",
    "reserve_etage_2": "reserve_etage_2", "fable_go45_au_moins": "fable_go45_au_moins",
    "sous_part_passe_x": "sous_part_passe_x_luc",
}


def cu(x):
    return str(x.quantize(D("0.01"), rounding=ROUND_CEILING))


def fl(x):
    return str(x.quantize(D("0.01"), rounding=ROUND_FLOOR))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def centimes(x):
    """Decimal ou nombre JSON en centimes entiers ; refuse un nombre qui n'est pas au centime."""
    c = D(str(x)) * 100
    if c != c.to_integral_value():
        raise ValueError("montant hors du centime : %r" % (x,))
    return int(c)


def usd(c):
    s = "-" if c < 0 else ""
    c = abs(c)
    return "%s%d.%02d" % (s, c // 100, c % 100)


def corps(t):
    lignes = t.split("\n")
    titre = lignes[0] if lignes and lignes[0].startswith("#") else None
    if titre is not None:
        lignes = lignes[1:]
    return "\n".join(lignes).strip("\n"), titre


def lire():
    rap, corps_l, bruts = [], [], []
    for k, nom in enumerate(PIECES, 1):
        b = open(DOSSIER + nom, "rb").read()
        bruts.append(b)
        t = b.decode("utf-8")
        cp, titre = corps(t)
        corps_l.append(cp)
        rap.append({"rang": k, "piece": nom, "sha256": sha(b), "octets_fichier": len(b), "signes_fichier": len(t),
                    "titre_retire": titre, "titre_nomme_un_modele": bool(titre and re.search(r"Fable|Opus|Neon|Kimi|Claude", titre)),
                    "signes_corps": len(cp), "octets_corps": len(cp.encode()),
                    "quarantaine_corps": len(re.findall("quarantaine", cp, re.I)),
                    "lignes_numerotees_corps": re.findall(r"(?m)^(\d+)\.", cp)})
    return rap, corps_l, bruts


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


def entrees_luc(dv):
    """Entrées de Luc en centimes : celles de ENTREES_LUC_V3, plus Fable (GO-45) et la sous-part de passe X (calculée)."""
    e = {k: v for k, (v, _) in ENTREES_LUC_V3.items()}
    e["fable_go45_au_moins"] = centimes(sum(FABLE_SUR_LUC.values()))
    e["sous_part_passe_x"] = centimes(D(dv["par_cle_usd"]["Luc"]["pire_de_lettre"]))
    return e


def engagement(e):
    """Engagement de Luc au pire, en centimes, par étages."""
    base = e["part_course_go49"] + e["fable_go45_au_moins"] + e["sous_part_passe_x"]
    avec_lignes = base + e["lignes_a_part"] + e["attaquant_informe_go50"]
    avec_etage_2 = avec_lignes + e["reserve_etage_2"]
    r = e["reste_declare"]
    return {"engagement_au_pire": base, "au_dela_du_reste_declare": base - r,
            "hors_passe_x_au_dela_du_reste": base - e["sous_part_passe_x"] - r,
            "avec_lignes_a_part_et_go50": avec_lignes, "avec_lignes_a_part_et_go50_au_dela": avec_lignes - r,
            "avec_reserve_etage_2": avec_etage_2, "avec_reserve_etage_2_au_dela": avec_etage_2 - r}


def luc(dv):
    e = entrees_luc(dv)
    g = engagement(e)
    fable = sum(FABLE_SUR_LUC.values())
    px = {k: D(v) for k, v in dv["par_cle_usd"]["Luc"].items()}
    out = {
        "entrees": {k: {"usd": usd(v), "source": ENTREES_LUC_V3[k][1] if k in ENTREES_LUC_V3 else
                        ("GO-2026-11-22-45, go.md l. 732 (somme des plafonds écrits)" if k == "fable_go45_au_moins"
                         else "calculée : devis recommandé, clé Luc, pire de lettre")} for k, v in e.items()},
        "fable_sur_luc_au_moins_usd": cu(fable), "fable_detail_usd": {k: cu(v) for k, v in FABLE_SUR_LUC.items()},
        "fable_non_chiffrees": FABLE_NON_CHIFFREES,
        "passe_x_sur_luc_usd": {k: cu(v) for k, v in px.items()},
        "lecture_compte_payant_part_260": {k + "_usd": usd(v) for k, v in g.items()},
        "note": "compte payant à recharge (GO-2026-11-22-48) ; part de la course fixée à 260 (GO-2026-11-22-49) ; "
                "demandes 28 à 30 non chiffrées ; lignes à part : clé à trancher",
    }
    # Pour mémoire seulement : la lecture sans compte payant de la v2 (R-4289), écartée par GO-48, caduque par GO-49.
    sc = {}
    for nom, lots in (("fable_seule", fable), ("fable_et_passe_x_avant_course_pire_de_lettre", fable + px["pire_de_lettre"]),
                      ("fable_et_passe_x_avant_course_pire_calcule", fable + px["pire_calcule"])):
        part = LUC_RESTE_DECLARE - lots
        sc[nom] = {"lots_non_clos_usd": cu(lots), "part_r_4289_usd": fl(part),
                   "manque_sous_le_haut_usd": cu(max(D(0), LUC_HAUT_ROLES - part)),
                   "arret_11_reste_moins_part_fixee_usd": fl(part - LUC_PART_FIXEE) if part >= LUC_PART_FIXEE else "-" + cu(LUC_PART_FIXEE - part)}
    out["pour_memoire_lecture_sans_compte_payant_ecartee"] = sc
    return out, e, g


def segments_fusion(f_avec, n):
    """Découpe la fusion sur ses séparateurs ; rend le corps de chaque pièce, tel qu'il est dans la fusion."""
    segs = []
    for k in range(1, n + 1):
        tete = SEPARATEUR.format(k=k) + "\n\n"
        i = f_avec.find(tete)
        if i < 0:
            return None
        debut = i + len(tete)
        if k < n:
            fin = f_avec.find("\n\n" + SEPARATEUR.format(k=k + 1) + "\n\n", debut)
        else:
            fin = len(f_avec) - 1 if f_avec.endswith("\n") else -1
        if fin < 0:
            return None
        segs.append(f_avec[debut:fin])
    return segs


def source_moins_titre(b):
    """Fichier source, à l'octet, moins sa ligne de titre (si elle commence par « # ») et ses lignes vides de bord."""
    if b.startswith(b"#"):
        b = b.split(b"\n", 1)[1] if b"\n" in b else b""
    return b.strip(b"\n")


def lire_fichier_7(chemin=FICHIER_7):
    b = open(chemin, "rb").read()
    return json.loads(b.decode("utf-8")), sha(b)


# --- Contrôles : chacun est une fonction d'un dossier d'entrées, pour être rejoué sur artefact (R5). ---

def c1(x):
    return all(x["rap"][i]["sha256"] == EMPREINTES_ADDITIF[PIECES[i]] for i in (0, 1))


def c2(x):
    return len(set(r["sha256"] for r in x["rap"])) == 17


def c3(x):
    return len(x["f_sans"]) == sum(len(c) for c in x["corps_l"]) + 2 * 16 + 1


def c4(x):
    return all(c in x["f_avec"] for c in x["corps_l"])


def c5(x):
    return all(len(re.findall("quarantaine", c, re.I)) == 0 for c in x["corps_l"])


def c6(x):
    return all(v <= PIRE_SCELLE for v in x["pires_96"])


def c7(x):
    a = cout("claude_course", "pire", x["j_avec"]["pire"], x["borne"])
    b = cout("claude_course", "pire", x["j_avec"]["pire"], x["borne"] + 1)
    return a <= PIRE_SCELLE < b


def c8(x):
    return x["cles_pl"] == x["pl"]


def c9(x):
    return all(P_OUT <= m for m in x["sortie_max"].values() if m is not None)


def c10(x):
    segs = segments_fusion(x["f_avec"], len(x["bruts"]))
    if segs is None or len(segs) != 17:
        return False
    return all(s.encode("utf-8") == source_moins_titre(b) for s, b in zip(segs, x["bruts"]))


def c11(x):
    f7 = x["f7"]["engagement_luc_au_pire"]
    ent = x["f7"]["entrees"]
    g = x["g"]
    t, a = centimes(f7["total_usd"]), centimes(f7["au_dela_du_reste_declare_usd"])
    lig = centimes(ent["plafond_lignes_a_part"]["usd"]) + centimes(ent["attaquant_informe_go50"]["usd"])
    sp = centimes(ent["sous_part_passe_x_luc"]["usd"])
    return (g["avec_lignes_a_part_et_go50"] == t and g["avec_lignes_a_part_et_go50_au_dela"] == a
            and g["avec_reserve_etage_2"] == centimes(f7["total_avec_reserve_etage_2_usd"])
            and g["avec_reserve_etage_2_au_dela"] == centimes(f7["au_dela_du_reste_avec_etage_2_usd"])
            # 449,60 et 296,60 ne sont pas écrits au fichier 7 : ils s'en déduisent en retirant lignes à part et GO-50.
            and g["engagement_au_pire"] == t - lig and g["au_dela_du_reste_declare"] == a - lig
            # 224,00 s'en déduit en retirant encore la sous-part de la passe X.
            and g["hors_passe_x_au_dela_du_reste"] == a - lig - sp)


def c12(x):
    ent = x["f7"]["entrees"]
    return all(x["e"][k] == centimes(ent[v]["usd"]) for k, v in CORRESPONDANCE_FICHIER_7.items())


CONTROLES = [
    ("1_empreintes_QN_QA_egales_a_l_additif", c1),
    ("2_dix_sept_pieces_d_empreintes_distinctes", c2),
    ("3_longueur_fusion_sans_separateurs_recomptee", c3),
    ("4_chaque_corps_est_sous_chaine_de_la_fusion", c4),
    ("5_aucun_corps_ne_porte_quarantaine", c5),
    ("6_chaque_tentative_calculee_sous_6_05_a_96000", c6),
    ("7_borne_exacte_116k", c7),
    ("8_somme_par_cle_egale_total", c8),
    ("9_plafond_sous_chaque_sortie_maximale_connue", c9),
    ("10_chaque_corps_de_la_fusion_egal_au_fichier_source_moins_son_titre", c10),
    ("11_engagement_de_luc_egal_au_fichier_7", c11),
    ("12_entrees_de_luc_egales_a_celles_du_fichier_7", c12),
]


def _alt_octet(b):
    """Change un octet au milieu du corps d'un fichier source."""
    i = len(b) // 2
    return b[:i] + (b"Z" if b[i:i + 1] != b"Z" else b"Y") + b[i + 1:]


ARTEFACTS = {
    "1_empreintes_QN_QA_egales_a_l_additif":
        ("empreinte de la pièce 1 changée au premier chiffre", lambda x: x["rap"][0].__setitem__(
            "sha256", ("f" if x["rap"][0]["sha256"][0] != "f" else "e") + x["rap"][0]["sha256"][1:])),
    "2_dix_sept_pieces_d_empreintes_distinctes":
        ("pièce 2 portant l'empreinte de la pièce 1", lambda x: x["rap"][1].__setitem__("sha256", x["rap"][0]["sha256"])),
    "3_longueur_fusion_sans_separateurs_recomptee":
        ("un signe ajouté à la fusion sans séparateurs", lambda x: x.__setitem__("f_sans", x["f_sans"] + "x")),
    "4_chaque_corps_est_sous_chaine_de_la_fusion":
        ("un signe ajouté au corps 1 hors de la fusion", lambda x: x["corps_l"].__setitem__(0, x["corps_l"][0] + "§")),
    "5_aucun_corps_ne_porte_quarantaine":
        ("le mot ajouté au corps 4", lambda x: x["corps_l"].__setitem__(3, x["corps_l"][3] + " quarantaine")),
    "6_chaque_tentative_calculee_sous_6_05_a_96000":
        ("une tentative à 6,06", lambda x: x["pires_96"].append(D("6.06"))),
    "7_borne_exacte_116k":
        ("borne augmentée d'un jeton", lambda x: x.__setitem__("borne", x["borne"] + 1)),
    "8_somme_par_cle_egale_total":
        ("somme par clé augmentée d'un centime", lambda x: x.__setitem__("cles_pl", x["cles_pl"] + D("0.01"))),
    "9_plafond_sous_chaque_sortie_maximale_connue":
        ("sortie maximale de Google posée à 64 000", lambda x: x["sortie_max"].__setitem__("google", 64000)),
    "10_chaque_corps_de_la_fusion_egal_au_fichier_source_moins_son_titre":
        ("un octet changé au milieu du fichier source de la pièce 5", lambda x: x["bruts"].__setitem__(4, _alt_octet(x["bruts"][4]))),
    "11_engagement_de_luc_egal_au_fichier_7":
        ("total du fichier 7 augmenté d'un centime", lambda x: x["f7"]["engagement_luc_au_pire"].__setitem__(
            "total_usd", float(D(str(x["f7"]["engagement_luc_au_pire"]["total_usd"])) + D("0.01")))),
    "12_entrees_de_luc_egales_a_celles_du_fichier_7":
        ("part de Luc du fichier 7 posée à 259", lambda x: x["f7"]["entrees"]["part_luc_go49"].__setitem__("usd", 259.0)),
}


def main(sortie):
    rap, corps_l, bruts = lire()
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
    f7, sha_f7 = lire_fichier_7()
    bloc_luc, e_luc, g_luc = luc(nettoie(rec))
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
        "luc": bloc_luc,
        "fichier_7": {"chemin": FICHIER_7, "sha256": sha_f7, "statut": "sortie de l'additif 2, v2, non scellé"},
    }
    # Contrôles calculés. Les 3, 4 et 8 relisent la recette du programme (vrais par construction, gardés) ;
    # le 10 compare chaque corps au fichier source, à l'octet.
    dossier = {"rap": rap, "corps_l": corps_l, "bruts": bruts, "f_sans": f_sans, "f_avec": f_avec, "j_avec": j_avec,
               "borne": borne, "pires_96": [D(v) for p in rec["par_proposeur"] for v in p["pire_par_tentative_calcule_usd"]],
               "pl": rec["_pl"], "cles_pl": rec["_cles_pl"], "sortie_max": dict(SORTIE_MAX),
               "f7": f7, "e": e_luc, "g": g_luc}
    controles = {nom: f(dossier) for nom, f in CONTROLES}
    # Épreuve sur artefacts (R5) : chaque contrôle, rejoué sur une copie altérée, doit tomber.
    epreuve = {}
    for nom, f in CONTROLES:
        quoi, alterer = ARTEFACTS[nom]
        x = copy.deepcopy(dossier)
        alterer(x)
        try:
            tombe = not f(x)
        except (KeyError, ValueError, IndexError):
            tombe = True
        epreuve[nom] = {"alteration": quoi, "tombe": tombe}
    out["controles"] = controles
    out["nombre_de_controles"] = len(controles)
    out["tous_les_controles_tenus"] = all(controles.values())
    out["epreuve_artefacts"] = epreuve
    out["tous_les_artefacts_tombent"] = all(v["tombe"] for v in epreuve.values())
    assert all(controles.values()), controles
    assert out["tous_les_artefacts_tombent"], epreuve
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])

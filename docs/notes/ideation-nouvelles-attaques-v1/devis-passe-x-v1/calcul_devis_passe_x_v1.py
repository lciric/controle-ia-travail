#!/usr/bin/env python3
"""Devis de la passe X rallongée (dix-sept questions), course « nouvelles attaques » — v1.

Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue.
Usage : python -I calcul_devis_passe_x_v1.py SORTIE.json
Tout montant est calculé en Decimal ; arrondi au centime supérieur pour un coût.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal as D, ROUND_CEILING

M = "/home/user/main-lecture"
DOSSIER = M + "/docs/notes/demandes-fable-api-2026-11-22-v1/"
# Ordre : QN, QA (X-3, l. 186 de l'additif), puis l'ordre du mandat (la liste de Lazar reste à nommer).
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
EMPREINTES_ATTENDUES = {  # additif v2, table des pièces (QN, QA)
    "question-neutre-modes-attaque-servie-v1.md": "02ad3d76ae90648f2fbb8498bc109d4a51a9dddd8b965e03326013e9ee08c9b8",
    "question-neutre-modes-attaque-ajout-organisme-v1.md": "8c54752fef44683a7f25e079e22344589e3306130a69eb166333f870a8761669",
}

ENVELOPPE_OCTETS = 512          # borne de l'enveloppe (K-2 (5)), valeur du rédacteur, à geler
SYNTHESE_OCTETS = 32260         # devis v11 l. 72 (S12) ; variante seulement
PARTIE_SERVIE_OCTETS = 3205     # devis v11 l. 97 ; variante seulement
SIGNES_PAR_JETON_ATTENDU = D(3)  # proposition l. 34 (« 3 à 3,5 »), bas de la fourchette
SIGNES_PAR_JETON_HAUT = D(2)     # plus prudent que 2,5 octets par jeton (devis v11 l. 211)
# pire : un jeton par octet (devis v11 l. 210)
PIRE_SCELLE_PAR_TENTATIVE = D("6.05")  # devis v11 l. 63 (S3), l. 119 ; P15 de l'additif
PLAFOND_DIRECTEUR = D(200)             # GO-2026-11-22-46, selon le mandat (absent de la copie de go.md lue)
LIGNE_GO_43 = D(55)                    # go.md l. 730
SORTIE_MAX_CLAUDE_46 = 128000          # mandat (référence de l'outil de l'API, non relue)
TEXTE_MIN_GOOGLE = 16000               # additif v2 l. 111 (G-6)
TEXTE_VISE = 32000                     # texte visible visé pour 17 questions (note, § 2)
FRACTION = {"attendu": D("0.4"), "haut": D("0.8"), "pire": D(1)}

# Tarifs (USD par million, entrée / sortie) par cas.
T = {
    "google": {"attendu": (D(2), D(10)), "haut": (D(4), D(20)), "pire": (D("8.3"), D("41.5")),
               "source": "rapport qualité-prix l. 25 (Argon 2/10 jusqu'au 30 nov., 4/20 ensuite), l. 26 et l. 28 (borne Argon et Carbon 8,3/41,5) ; cités, non vérifiés"},
    "openai": {c: (D(10), D(50)) for c in FRACTION} | {"source": "rapport qualité-prix l. 29 (Astra 10/50, repris par citation)"},
    "claude_course": {c: (D(10), D(50)) for c in FRACTION} | {"source": "rapport qualité-prix l. 31 (plus haut tarif Claude cité, 10/50) ; identité des espèces 3 et 4 hors des pièces lues"},
    "kimi": {c: (D(2), D(10)) for c in FRACTION} | {"source": "lecture-tarif-et-limite-kimi-v1.md l. 10-11 (vérifié sur page gardée)"},
    "opus46": {c: (D(5), D(25)) for c in FRACTION} | {"source": "mandat : référence de l'outil de l'API, NON relue sur page officielle ; même repère au recalcul-part-luc-153-v2.json l. 92-103"},
    "sonnet46": {c: (D(3), D(15)) for c in FRACTION} | {"source": "mandat : référence de l'outil de l'API, NON relue sur page officielle ; recalcul-part-luc-153-v2.json l. 96-107"},
}

# Proposeurs : (nom, famille de tarif, clé payeuse, chaîne littérale GO-35, chaîne « modèle déjà tenté sauté »)
PROPOSEURS = [
    ("espece_1", "google", "deuxième relais (Google)", ["google"], ["google"]),
    ("espece_2", "openai", "troisième relais (OpenAI)", ["openai"], ["openai"]),
    ("espece_3", "claude_course", "Luc (GO-2026-11-22-45)", ["claude_course", "opus46", "sonnet46"], ["claude_course", "opus46", "sonnet46"]),
    ("espece_4", "claude_course", "Luc", ["claude_course", "opus46", "sonnet46"], ["claude_course", "opus46", "sonnet46"]),
    ("espece_5", "google", "deuxième relais (Google)", ["google"], ["google"]),
    ("ajout_kimi", "kimi", "KIMI_API_KEY (par son nom)", ["kimi"], ["kimi"]),
    ("ajout_opus46", "opus46", "Luc", ["opus46", "opus46", "sonnet46"], ["opus46", "sonnet46"]),
    ("ajout_sonnet46", "sonnet46", "Luc", ["sonnet46", "opus46", "sonnet46"], ["sonnet46"]),
]


def c(x):
    return str(x.quantize(D("0.01"), rounding=ROUND_CEILING))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def corps(texte):
    lignes = texte.split("\n")
    if lignes and lignes[0].startswith("#"):
        lignes = lignes[1:]
    return "\n".join(lignes).strip("\n")


def piece_fusionnee():
    rapports, corps_liste = [], []
    for nom in PIECES:
        b = open(DOSSIER + nom, "rb").read()
        t = b.decode("utf-8")
        cp = corps(t)
        corps_liste.append(cp)
        rapports.append({
            "piece": nom, "sha256": sha(b), "octets_fichier": len(b), "signes_fichier": len(t),
            "titre_retire": t.startswith("#"), "signes_corps": len(cp), "octets_corps": len(cp.encode()),
            "points_d_interrogation_corps": cp.count("?"),
            "occurrences_quarantaine_corps": len(re.findall(r"quarantaine", cp, re.I)),
            "occurrences_quarantaine_fichier": len(re.findall(r"quarantaine", t, re.I)),
        })
    for nom, e in EMPREINTES_ATTENDUES.items():
        r = next(x for x in rapports if x["piece"] == nom)
        assert r["sha256"] == e, nom
    texte = "\n\n".join(corps_liste) + "\n"
    return texte, rapports


def jetons_entree(texte, extra_octets=0):
    b = len(texte.encode()) + ENVELOPPE_OCTETS + extra_octets
    s = len(texte) + ENVELOPPE_OCTETS + extra_octets
    return {"attendu": int((D(s) / SIGNES_PAR_JETON_ATTENDU).to_integral_value(ROUND_CEILING)),
            "haut": int((D(s) / SIGNES_PAR_JETON_HAUT).to_integral_value(ROUND_CEILING)),
            "pire": b}


def cout(fam, cas, jin, jout):
    pin, pout = T[fam][cas]
    return (D(jin) * pin + D(jout) * pout) / D(10**6)


def devis(p_out, jin, lecture="litterale", proposeurs=PROPOSEURS, requetes=1, lettre=True):
    lignes, cles = [], {}
    tot = {"attendu": D(0), "haut": D(0), "pire_calcule": D(0), "pire_de_lettre": D(0)}
    for nom, fam, cle, ch_lit, ch_saut in proposeurs:
        chaine = ch_lit if lecture == "litterale" else ch_saut
        out = {k: int(D(p_out) * f) for k, f in FRACTION.items()}
        att = cout(fam, "attendu", jin["attendu"], out["attendu"]) * requetes
        haut_ch = chaine[:2] if len(chaine) > 1 and fam in ("claude_course", "opus46") else chaine[:1]
        haut = sum(cout(f, "haut", jin["haut"], out["haut"]) for f in haut_ch) * requetes
        pires = [cout(f, "pire", jin["pire"], out["pire"]) for f in chaine]
        pire = sum(pires) * requetes
        pl = sum(max(PIRE_SCELLE_PAR_TENTATIVE, x) if lettre else x for x in pires) * requetes
        lignes.append({"proposeur": nom, "tarif": fam, "cle": cle, "tentatives_au_pire": len(chaine) * requetes,
                       "chaine": chaine, "pire_par_tentative_calcule_usd": [c(x) for x in pires],
                       "attendu_usd": c(att), "haut_usd": c(haut), "pire_calcule_usd": c(pire), "pire_de_lettre_usd": c(pl)})
        for k, v in (("attendu", att), ("haut", haut), ("pire_calcule", pire), ("pire_de_lettre", pl)):
            tot[k] += v
        cles.setdefault(cle.split(" (")[0], D(0))
        cles[cle.split(" (")[0]] += pl
    return {"plafond_de_sortie_jetons": p_out, "lecture_des_chaines": lecture, "requetes_par_proposeur": requetes,
            "par_proposeur": lignes, "totaux_usd": {k: c(v) for k, v in tot.items()},
            "tentatives_au_pire": sum(x["tentatives_au_pire"] for x in lignes),
            "pire_de_lettre_par_cle_usd": {k: c(v) for k, v in cles.items()},
            "marge_sous_200_au_pire_de_lettre_usd": c(PLAFOND_DIRECTEUR - tot["pire_de_lettre"]),
            "tient_sous_200": tot["pire_de_lettre"] <= PLAFOND_DIRECTEUR,
            "tient_sous_55_GO_43": tot["pire_de_lettre"] <= LIGNE_GO_43}


def main(sortie):
    texte, rapports = piece_fusionnee()
    jin = jetons_entree(texte)
    jin_var = jetons_entree(texte, SYNTHESE_OCTETS + PARTIE_SERVIE_OCTETS)
    # plus grand plafond de sortie qui garde chaque tentative sous 6,05 au plus haut tarif cité (50 par million)
    p_max_605 = int(((PIRE_SCELLE_PAR_TENTATIVE - D(jin["pire"]) * D(10) / D(10**6)) * D(10**6) / D(50)))
    P_OUT = 96000
    out = {
        "piece_fusionnee": {
            "sha256": sha(texte.encode()), "signes": len(texte), "octets": len(texte.encode()),
            "lignes": texte.count("\n"), "points_d_interrogation": texte.count("?"),
            "occurrences_quarantaine": len(re.findall(r"quarantaine", texte, re.I)),
            "somme_signes_fichiers": sum(r["signes_fichier"] for r in rapports),
            "somme_octets_fichiers": sum(r["octets_fichier"] for r in rapports),
            "regle": "corps sans titre « # », une ligne vide entre chaque pièce, une fin de ligne finale (X-3)",
        },
        "pieces": rapports,
        "entree_par_requete_jetons": {"enveloppe_octets_borne": ENVELOPPE_OCTETS, **jin,
                                      "regles": "attendu 3 signes par jeton ; haut 2 signes par jeton ; pire 1 jeton par octet"},
        "entree_variante_avec_synthese_et_partie_servie_jetons": jin_var,
        "plafond_de_sortie": {
            "propose_jetons": P_OUT, "texte_vise_jetons": TEXTE_VISE,
            "budget_de_reflexion_google_au_plus": P_OUT - TEXTE_VISE,
            "regle_google_tenue": P_OUT >= (P_OUT - TEXTE_VISE) + TEXTE_MIN_GOOGLE,
            "sous_sortie_max_claude_4_6": P_OUT <= SORTIE_MAX_CLAUDE_46,
            "plus_grand_plafond_sous_6_05_au_tarif_50": p_max_605,
            "sortie_max_a_relever": ["espèces 1 et 5 (Google)", "espèce 2 (OpenAI)", "espèces 3 et 4", "Kimi"],
        },
        "tarifs_sources": {k: v["source"] for k, v in T.items()},
        "devis_recommande": devis(P_OUT, jin, "litterale"),
        "devis_recommande_lecture_saut": devis(P_OUT, jin, "saut"),
        "options": {
            "sortie_64000_litterale": devis(64000, jin, "litterale"),
            "sortie_128000_litterale": devis(128000, jin, "litterale"),
            "sortie_96000_sans_les_deux_ajouts_claude": devis(P_OUT, jin, "litterale", PROPOSEURS[:6]),
            "sortie_96000_cinq_especes_seules": devis(P_OUT, jin, "litterale", PROPOSEURS[:5]),
            "deux_requetes_de_64000": devis(64000, jetons_entree(texte[: len(texte) // 2]), "litterale", requetes=2),
            "sortie_96000_variante_entree_avec_synthese": devis(P_OUT, jin_var, "litterale"),
        },
    }
    out["controles"] = {
        "QN_QA_empreintes_egales_additif": True,
        "pire_calcule_par_tentative_sous_6_05_a_96000": all(
            D(x) <= PIRE_SCELLE_PAR_TENTATIVE for p in out["devis_recommande"]["par_proposeur"] for x in p["pire_par_tentative_calcule_usd"]),
        "dix_sept_pieces": len(rapports) == 17,
        "cinq_especes_egal_54_45_de_X_10": out["options"]["sortie_96000_cinq_especes_seules"]["totaux_usd"]["pire_de_lettre"] == "54.45",
        "quarantaine_absent_du_corps_fusionne": out["piece_fusionnee"]["occurrences_quarantaine"] == 0,
    }
    assert all(out["controles"].values()), out["controles"]
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])

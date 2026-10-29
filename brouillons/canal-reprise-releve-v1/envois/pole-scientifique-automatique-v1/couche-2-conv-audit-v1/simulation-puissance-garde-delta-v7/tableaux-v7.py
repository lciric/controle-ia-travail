"""Tableaux du rapport v7, lus dans les sorties des passages (aucun chiffre recopié à la main). Écrit `tableaux-v7.md` (tableaux en
markdown, avec la source de chaque tableau) et `tableaux-v7-sortie.json` (mêmes nombres, non arrondis). Les valeurs de la v6 citées
(n80, T2) sont lues dans les sorties du dossier v6, dont l'empreinte est écrite.

Usage : python3 -I -B tableaux-v7.py DOSSIER_V7 DOSSIER_V6 SORTIE.md SORTIE.json
"""

import hashlib
import json
import os
import sys

DOSSIER, DOSSIER_V6, SORTIE_MD, SORTIE_JSON = sys.argv[1:5]
PREFIXE = "simulation-puissance-garde-delta-v7-sortie-"
PREFIXE_V6 = "simulation-puissance-garde-delta-v6-sortie-"
PAIRES = ((10, 10), (10, 5), (10, 3), (5, 5), (5, 3), (5, 10))
BIAIS = ("0.0", "0.0125")
REPS = 2000


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def charger(dossier, prefixe, nom):
    chemin = os.path.join(dossier, prefixe + nom + ".json")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f), sha(chemin)


S, EMPREINTES = {}, {}
for nom in ("logit-0", "logit-0.5", "logit-1.0", "beta-0.5", "beta-1.0", "n80-beta-1.0", "rejeu-v6-principale", "rejeu-v6-dispersion-1.0-independante"):
    S[nom], EMPREINTES[nom] = charger(DOSSIER, PREFIXE, nom)
V6, EMPREINTES_V6 = {}, {}
for nom in ("principale", "n80-dispersion-0.5", "n80-dispersion-1.0"):
    V6[nom], EMPREINTES_V6[nom] = charger(DOSSIER_V6, PREFIXE_V6, nom)
SUFFIXE = {"logit-0": "", "logit-0.5": "_effetB0.5", "logit-1.0": "_effetB1.0", "beta-0.5": "_effetB0.5_beta", "beta-1.0": "_effetB1.0_beta",
           "n80-beta-1.0": "_effetB1.0_beta"}
SCENARIOS = [("logit-0", "nulle (σ = 0, les deux échelles)"), ("logit-0.5", "logit σ = 0,5"), ("logit-1.0", "logit σ = 1,0"),
             ("beta-0.5", "bêta (κ de σ = 0,5)"), ("beta-1.0", "bêta (κ de σ = 1,0)")]
sortie_json = {"empreintes_sorties_v7": EMPREINTES, "empreintes_sorties_v6_citees": EMPREINTES_V6}
md = []


def cle(K, Ks, biais, suffixe, n=288):
    return f"binomiale_Kh{K}_Ks{Ks}_taux0.01{suffixe}|delta=0.05|n={n}|n_garde={n}|biais={biais}|k=8"


def cellule(passage, K, Ks, biais):
    return S[passage]["cellules"][cle(K, Ks, biais, SUFFIXE[passage])]


def f2(x):
    return f"{x:.2f}".replace(".", ",")


def f3(x):
    return f"{x:.3f}".replace(".", ",")


def f4(x):
    return f"{x:.4f}".replace(".", ",")


def bi(b):
    return "0" if b == "0.0" else "0,0125"


def ligne(*c):
    return "| " + " | ".join(str(x) for x in c) + " |"


def tableau(titre, source, entetes, lignes, note=None):
    md.append(f"#### {titre}\n")
    md.append(f"Source : {source}\n")
    md.append(ligne(*entetes))
    md.append(ligne(*["---"] * len(entetes)))
    md.extend(ligne(*l) for l in lignes)
    if note:
        md.append("\n" + note)
    md.append("")


# --- T1 : tableau principal, 288 unités : fiche, minimum des 8 gardes, minimum des 8 contrastes, par scénario × (K_h, K_s) × biais
t1 = {}
lignes = []
for passage, nom in SCENARIOS:
    for K, Ks in PAIRES:
        for b in BIAIS:
            c = cellule(passage, K, Ks, b)
            fiche = c["ebh_A"]["retenues_fiches_du_sujet"]
            gardes, contrastes, garde1 = c["40.0"]["k_gardes"]["part"], c["40.0"]["k_contrastes"]["part"], c["40.0"]["garde_seule"]["part"]
            t1[f"{passage}|K_h={K}|K_s={Ks}|biais={b}"] = {"fiche_retenue_ebh_A": fiche, "min_8_gardes_atteint_40": gardes,
                                                          "min_8_contrastes_atteint_40": contrastes, "une_garde_atteint_40": garde1,
                                                          "fiche_atteint_40_sans_ebh": c["40.0"]["fiche_entiere"]["part"]}
            lignes.append([nom, f"{K}", f"{Ks}", bi(b), f3(fiche), f3(gardes), f3(contrastes), f3(garde1)])
tableau("T1. Puissance à 288 unités aux paramètres décidés (k = 8, τ = 0,01, δ = 0,05, α_c = 0,05, lecture (A) m = 2, seuil 40) : fiche, gardes, contrastes",
        "`-sortie-logit-0.json`, `-sortie-logit-0.5.json`, `-sortie-logit-1.0.json`, `-sortie-beta-0.5.json`, `-sortie-beta-1.0.json` ; fiche : `ebh_A.retenues_fiches_du_sujet` "
        "(fiche du mode 1 retenue par l'e-BH, m = 2, arrêt à 40) ; gardes et contrastes : bloc `40.0`, `k_gardes.part` et `k_contrastes.part` (le minimum des 8 "
        f"atteint 40) ; `garde_seule.part` : une garde ; {REPS} répétitions, erreur type ≤ 0,011",
        ["dispersion", "K_h", "K_s", "biais", "fiche", "minimum des 8 gardes", "minimum des 8 contrastes", "1 garde"], lignes,
        "σ = 0 : aucune dispersion, les deux échelles coïncident (une seule ligne). Logit : écart-type σ de l'effet d'unité en logit, espérance tenue, indépendant entre "
        "comparateurs (v6). Bêta : f_B ~ Bêta(τκ, (1 − τ)κ), r_B ~ Bêta(r_Bκ, (1 − r_B)κ), κ telle que l'écart-type de r_B égale celui de la v6 au σ indiqué (T3) ; "
        "honnêtes et sabotés tirés à part. (5, 10) : K_s > K_h, hors de la demande, donné en plus.")
sortie_json["T1_principal_288"] = t1

# --- T1bis : résumé par K_s : fiche, minimum sur K_h ∈ {10, 5} et biais
t1b = {}
lignes = []
for passage, nom in SCENARIOS:
    l = [nom]
    for Ks in (10, 5, 3):
        vals = [cellule(passage, K, Ks, b)["ebh_A"]["retenues_fiches_du_sujet"] for K in (10, 5) for b in BIAIS]
        g = [cellule(passage, K, Ks, b)["40.0"]["k_gardes"]["part"] for K in (10, 5) for b in BIAIS]
        t1b[f"{passage}|K_s={Ks}"] = {"fiche_min": min(vals), "fiche_max": max(vals), "min_8_gardes_min": min(g)}
        l.append(f"{f3(min(vals))} – {f3(max(vals))}")
    lignes.append(l)
tableau("T1bis. Résumé de T1 : fiche retenue, étendue (minimum – maximum) sur K_h ∈ {10, 5} et biais ∈ {0 ; 0,0125}, par K_s",
        "T1", ["dispersion", "K_s = 10", "K_s = 5", "K_s = 3"], lignes,
        "La fiche dépend de K_s (contrastes) et presque pas de K_h (gardes) : lire T1.")
sortie_json["T1bis_resume_par_K_s"] = t1b

# --- T2 : n80 bêta σ = 1,0 contre la v6 (nulle, logit 0,5, logit 1,0)
t2 = {}
lignes = []
for (src, nom, suffixe, dossier_nom) in (("v6", "nulle", "", "principale"), ("v6", "logit σ = 0,5", "_effetB0.5", "n80-dispersion-0.5"),
                                         ("v6", "logit σ = 1,0", "_effetB1.0", "n80-dispersion-1.0"), ("v7", "bêta (κ de σ = 1,0)", "_effetB1.0_beta", "n80-beta-1.0")):
    s = V6[dossier_nom] if src == "v6" else S[dossier_nom]
    for K in (10, 5):
        n80 = s["lois"][f"binomiale_Kh{K}_Ks{K}_taux0.01{suffixe}"]["n_pour_puissance_0_8_k_gardes"]
        for b in BIAIS:
            l = [nom, src, f"{K}", bi(b)]
            for seuil in ("40.0", "160.0"):
                r = n80[f"delta=0.05|seuil={seuil}|biais={b}|k=8"]
                t2[f"{nom}|{src}|K={K}|biais={b}|seuil={seuil}"] = r
                l.append(str(r["n_approx"]) if r["n_approx"] is not None else f"> {r['au_dela_de']}")
            lignes.append(l)
tableau("T2. n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8 (comparateurs seuls, sans fiche), K_s = K_h",
        f"v7 : `-sortie-n80-beta-1.0.json` ({EMPREINTES['n80-beta-1.0'][:8]}…) ; v6 (lues, non recalculées) : `{PREFIXE_V6}principale.json` ({EMPREINTES_V6['principale'][:8]}…), "
        f"`{PREFIXE_V6}n80-dispersion-0.5.json` ({EMPREINTES_V6['n80-dispersion-0.5'][:8]}…), `{PREFIXE_V6}n80-dispersion-1.0.json` ({EMPREINTES_V6['n80-dispersion-1.0'][:8]}…) ; "
        "`lois.*.n_pour_puissance_0_8_k_gardes` ; dichotomie, 2 000 répétitions, incertitude de graine jusqu'à ≈ 6 %",
        ["dispersion", "source", "K_h = K_s", "biais", "seuil 40", "seuil 160"], lignes,
        "La garde est tirée avec le sujet A commun aux 8 comparateurs ; la dispersion est celle des comparateurs B_j.")
sortie_json["T2_n80"] = t2

# --- T3 : correspondance logit → bêta : écarts-types théoriques (décomposition écrite par le script) et tirés (moments), 288 unités, biais 0
t3 = {}
lignes = []
for passage, nom in SCENARIOS[1:]:
    for K, Ks in ((10, 10), (5, 3)):
        c = cellule(passage, K, Ks, "0.0")
        m = c["moments_tires"]
        dec = S[passage]["lois"][f"binomiale_Kh{K}_Ks{Ks}_taux0.01{SUFFIXE[passage]}"]["decomposition_effet_unite"]["biais=0.0"]
        dh, ds = dec["comparateurs_honnetes_fB"], dec["comparateurs_sabotes_rB"]
        kappa = dh.get("kappa_concentration")
        t3[f"{passage}|K_h={K}|K_s={Ks}"] = {"moments_tires": m, "decomposition_fB": dh, "decomposition_rB": ds}
        lignes.append([nom, f"{K}", f"{Ks}", f"{kappa:.3f}".replace(".", ",") if kappa else "—", f4(dh["correlation_intra_unite"]), f4(ds["correlation_intra_unite"]),
                       f3(m["E_fB"]), f3(m["E_rB"]), f4(dh["ecart_type_ajoute_sur_p"]), f4(m["ecart_type_pB_honnetes"]),
                       f4(ds["ecart_type_ajoute_sur_p"]), f4(m["ecart_type_pB_sabotes"])])
tableau("T3. Correspondance logit → bêta : κ, corrélation intra-unité et écarts-types de p_B, attendus (décomposition écrite par le script) et tirés (288 unités, biais 0)",
        "`lois.*.decomposition_effet_unite` et `cellules.*.moments_tires` des sorties de dispersion",
        ["dispersion", "K_h", "K_s", "κ", "ρ intra-unité f_B", "ρ intra-unité r_B", "E[f_B] tiré", "E[r_B] tiré", "écart-type p_B honnêtes attendu", "tiré",
         "écart-type p_B sabotés attendu", "tiré"], lignes,
        "E[f_B] visé 0,010, E[r_B] visé 0,400. Logit : la corrélation intra-unité diffère des deux côtés (le logit charge r_B) ; bêta : κ commune, même corrélation "
        "intra-unité des deux côtés, écart-type de r_B égal à celui du logit au même σ, écart-type de f_B 3 à 4 fois plus grand.")
sortie_json["T3_correspondance"] = t3

# --- T4 : artefacts (R5) sur la garde seule, toutes les cellules de tous les passages
t4 = {}
lignes = []
for nom, s in S.items():
    pf, pt = 0.0, 0.0
    for et, c in s["cellules"].items():
        for seuil, bloc in c.items():
            if isinstance(bloc, dict) and "frontiere_part" in bloc:
                pf = max(pf, bloc["frontiere_part"] / bloc["frontiere_borne_ville"])
                pt = max(pt, bloc["tricheur_part"])
    t4[nom] = {"frontiere_sur_borne_de_Ville_max": pf, "tricheur_max": pt, "cellules": len(s["cellules"])}
    lignes.append([f"`{nom}`", len(s["cellules"]), f2(pf), f3(pt)])
tableau("T4. Artefacts de la garde (R5), toutes cellules de tous les passages", "tous les passages, blocs `frontiere_part`, `frontiere_borne_ville`, `tricheur_part`",
        ["passage", "cellules", "frontière / borne de Ville (max)", "tricheur (max)"], lignes,
        "Frontière E[g] = δ : doit rester sous la borne de Ville 1/seuil (rapport ≤ 1) ; tricheur E[g] = 2δ : doit rester ≈ 0.")
sortie_json["T4_artefacts"] = t4

# --- T5 : passages : durée, commit au lancement, état du script (manifeste de chaque passage contre sa sortie, GD5-03)
t5 = {}
lignes = []
for nom in S:
    with open(os.path.join(DOSSIER, "manifeste-" + PREFIXE + nom + ".json"), encoding="utf-8") as f:
        man = json.load(f)
    sortie = S[nom]
    mm = man["script"]
    t5[nom] = {"repetitions": sortie["reglages"]["repetitions"], "duree_s": man["duree_s"], "commit_manifeste": mm["commit"],
               "commit_sortie": sortie["commit"], "etat_manifeste": mm["etat_du_script"], "etat_sortie": sortie["etat_du_script"],
               "memes": mm["commit"] == sortie["commit"] and mm["etat_du_script"] == sortie["etat_du_script"],
               "python": sortie["environnement"]["python"], "numpy": sortie["environnement"]["numpy"], "sortie_sha256": EMPREINTES[nom]}
    lignes.append([f"`{nom}`", sortie["reglages"]["repetitions"], str(man["duree_s"]).replace(".", ","), f"`{(mm['commit'] or 'absent')[:12]}`",
                   "non suivi (??)" if mm["etat_du_script"].startswith("??") else mm["etat_du_script"][:30], "oui" if t5[nom]["memes"] else "NON",
                   f"`{EMPREINTES[nom][:8]}…`"])
tableau("T5. Passages : répétitions, durée, commit au lancement, état du script (lus dans le manifeste de chaque passage), empreinte de la sortie",
        "`manifeste-simulation-puissance-garde-delta-v7-sortie-*.json`, comparés aux champs `commit` et `etat_du_script` de chaque sortie",
        ["passage", "répétitions", "durée (s)", "commit au lancement", "état du script", "sortie = manifeste", "sortie"], lignes)
sortie_json["T5_passages"] = t5

with open(SORTIE_MD, "x", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
with open(SORTIE_JSON, "x", encoding="utf-8") as f:
    json.dump(sortie_json, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("tableaux écrits :", SORTIE_MD, SORTIE_JSON)

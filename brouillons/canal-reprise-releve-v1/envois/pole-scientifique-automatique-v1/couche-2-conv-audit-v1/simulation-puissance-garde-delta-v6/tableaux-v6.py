"""Tableaux du rapport v6, lus dans les sorties des passages (aucun chiffre recopié à la main). Écrit `tableaux-v6.md` (tableaux
en markdown, avec la source de chaque tableau) et `tableaux-v6-sortie.json` (mêmes nombres, non arrondis).

Usage : python3 -I -B tableaux-v6.py DOSSIER_DES_SORTIES SORTIE.md SORTIE.json
"""

import json
import math
import os
import sys

DOSSIER, SORTIE_MD, SORTIE_JSON = sys.argv[1:4]
PREFIXE = "simulation-puissance-garde-delta-v6-sortie-"
KS = (10, 5, 3)
BIAIS = ("0.0", "0.0125")
TAILLES = (160, 288, 300, 400)
REPS = 2000


def charger(nom):
    with open(os.path.join(DOSSIER, PREFIXE + nom + ".json"), encoding="utf-8") as f:
        return json.load(f)


S = {nom: charger(nom) for nom in ("principale", "dispersion-0.5-independante", "dispersion-1.0-independante",
                                   "dispersion-0.5-rho-0.17", "dispersion-1.0-rho-0.17", "alpha-0.025", "effet-A-1.0",
                                   "n80-dispersion-0.5", "n80-dispersion-1.0")}
# loi de chaque passage : suffixe du nom de la loi
SUFFIXE = {"principale": "", "dispersion-0.5-independante": "_effetB0.5", "dispersion-1.0-independante": "_effetB1.0",
           "dispersion-0.5-rho-0.17": "_effetB0.5_corrB0.17", "dispersion-1.0-rho-0.17": "_effetB1.0_corrB0.17",
           "alpha-0.025": "", "effet-A-1.0": "_effetA1.0", "n80-dispersion-0.5": "_effetB0.5", "n80-dispersion-1.0": "_effetB1.0"}
DISPERSIONS = [("principale", "nulle"), ("dispersion-0.5-independante", "0,5"), ("dispersion-1.0-independante", "1,0"),
               ("dispersion-0.5-rho-0.17", "0,5 ; ρ 0,17"), ("dispersion-1.0-rho-0.17", "1,0 ; ρ 0,17")]
sortie_json = {}
md = []


def cle(K, n, biais, suffixe, lien_coupe=False):
    return f"binomiale_Kh{K}_Ks{K}_taux0.01{suffixe}{'_lien_coupe' if lien_coupe else ''}|delta=0.05|n={n}|n_garde={n}|biais={biais}|k=8"


def cellule(passage, K, n, biais, lien_coupe=False):
    return S[passage]["cellules"][cle(K, n, biais, SUFFIXE[passage], lien_coupe)]


def f2(x):
    return f"{x:.2f}".replace(".", ",")


def f3(x):
    return f"{x:.3f}".replace(".", ",")


def bi(b):
    return "0" if b == "0.0" else "0,0125"


def ligne(*c):
    return "| " + " | ".join(str(x) for x in c) + " |"


def tableau(titre, source, entetes, lignes, note=None):
    md.append(f"### {titre}\n")
    md.append(f"Source : {source}\n")
    md.append(ligne(*entetes))
    md.append(ligne(*["---"] * len(entetes)))
    md.extend(ligne(*l) for l in lignes)
    if note:
        md.append("\n" + note)
    md.append("")


# --- T1 : le chiffre principal, 288 unités
t1 = {}
lignes = []
for K in KS:
    for b in BIAIS:
        l = [f"{K}", bi(b)]
        for passage, nom in DISPERSIONS:
            v = cellule(passage, K, 288, b)["ebh_A"]["retenues_fiches_du_sujet"]
            t1[f"K={K}|biais={b}|{passage}"] = v
            l.append(f3(v))
        lignes.append(l)
tableau("T1. Puissance de la fiche à 288 unités aux paramètres décidés (k = 8, τ = 0,01, δ = 0,05, α_c = 0,05)",
        "`-sortie-principale.json` (dispersion nulle) et `-sortie-dispersion-*.json` ; champ `ebh_A.retenues_fiches_du_sujet` : part des "
        f"suites où la fiche du mode 1 est retenue par l'e-BH (m = 2, arrêt à 40) ; {REPS} répétitions, erreur type ≤ 0,011",
        ["K_h", "biais", "dispersion nulle", "σ = 0,5 indép.", "σ = 1,0 indép.", "σ = 0,5 ; ρ = 0,17", "σ = 1,0 ; ρ = 0,17"], lignes,
        "σ : écart-type, en logit, de l'effet d'unité de chaque comparateur (espérance tenue) ; indép. : effets indépendants entre comparateurs ; "
        "ρ = 0,17 : corrélation des effets entre comparateurs d'une même unité.")
sortie_json["T1_fiche_288"] = t1

# --- T2 : toutes les tailles
t2 = {}
lignes = []
for passage, nom in DISPERSIONS:
    for K in KS:
        for b in BIAIS:
            l = [nom, f"{K}", bi(b)]
            for n in TAILLES:
                v = cellule(passage, K, n, b)["ebh_A"]["retenues_fiches_du_sujet"]
                t2[f"{passage}|K={K}|biais={b}|n={n}"] = v
                l.append(f2(v))
            lignes.append(l)
tableau("T2. Fiche retenue par l'e-BH (A) selon la taille", "mêmes sorties que T1, `ebh_A.retenues_fiches_du_sujet`",
        ["dispersion", "K_h", "biais"] + [f"{n} unités" for n in TAILLES], lignes)
sortie_json["T2_fiche_toutes_tailles"] = t2

# --- T3 : atteinte du seuil 40 (sans la lecture de la valeur finale) et deux modes
t3 = {}
lignes = []
for passage, nom in DISPERSIONS:
    for K in KS:
        for b in BIAIS:
            c = cellule(passage, K, 288, b)
            e = c["ebh_A"]
            t3[f"{passage}|K={K}|biais={b}"] = {"premiere_atteinte_40": e["premiere_atteinte_fiches_du_sujet"],
                                               "retenue_mode_1": e["retenues_fiches_du_sujet"], "retenues_les_deux_modes": e["retenues_toutes_vraies"]}
            lignes.append([nom, f"{K}", bi(b), f2(e["premiere_atteinte_fiches_du_sujet"]), f2(e["retenues_fiches_du_sujet"]),
                           f2(e["retenues_toutes_vraies"]), f2(c["40.0"]["fiche_entiere"]["part"]), f2(c["160.0"]["fiche_entiere"]["part"])])
tableau("T3. À 288 unités : atteinte, retenue du mode 1, retenue des deux modes", "mêmes sorties, `ebh_A` et `40.0`, `160.0` (`fiche_entiere`)",
        ["dispersion", "K_h", "biais", "atteint 40 (mode 1)", "retenue (mode 1)", "retenue (les 2 modes)", "fiche atteint 40", "fiche atteint 160"], lignes,
        "« atteint 40 (mode 1) » : première atteinte de m/α_c = 40 par la fiche du mode 1 ; « fiche atteint 40/160 » : première atteinte du seuil "
        "par le minimum des 8 gardes et des 8 contrastes, sans e-BH (seuil de référence 160 = m = 8).")
sortie_json["T3_atteinte_retenue_288"] = t3

# --- T4 : quel composant limite (288)
t4 = {}
lignes = []
for passage, nom in DISPERSIONS:
    for K in KS:
        for b in BIAIS:
            c = cellule(passage, K, 288, b)["40.0"]
            t4[f"{passage}|K={K}|biais={b}"] = {"garde_seule": c["garde_seule"]["part"], "k_gardes": c["k_gardes"]["part"],
                                               "k_contrastes": c["k_contrastes"]["part"], "fiche_entiere": c["fiche_entiere"]["part"]}
            lignes.append([nom, f"{K}", bi(b), f2(c["garde_seule"]["part"]), f2(c["k_gardes"]["part"]), f2(c["k_contrastes"]["part"]),
                           f2(c["fiche_entiere"]["part"])])
tableau("T4. À 288 unités, seuil 40 : composants de la fiche (première atteinte)", "mêmes sorties, bloc `40.0`",
        ["dispersion", "K_h", "biais", "1 garde", "minimum des 8 gardes", "minimum des 8 contrastes", "fiche entière"], lignes)
sortie_json["T4_composants_288"] = t4

# --- T5 : α_c = 0,025
t5 = {}
lignes = []
for K in KS:
    for b in BIAIS:
        l = [f"{K}", bi(b)]
        for n in TAILLES:
            a = cellule("principale", K, n, b)["ebh_A"]["retenues_fiches_du_sujet"]
            c = cellule("alpha-0.025", K, n, b)["ebh_A"]["retenues_fiches_du_sujet"]
            t5[f"K={K}|biais={b}|n={n}"] = {"alpha_0.05": a, "alpha_0.025": c}
            l.append(f"{f2(a)} · {f2(c)}")
        lignes.append(l)
tableau("T5. α_c = 0,05 · α_c = 0,025 (fiche du mode 1 retenue)", "`-sortie-principale.json` · `-sortie-alpha-0.025.json`, `ebh_A.retenues_fiches_du_sujet` ; "
        "mêmes tirages (mêmes étiquettes de cellule), seuils 40 et 80", ["K_h", "biais"] + [f"{n} unités" for n in TAILLES], lignes,
        "Avec α_c = 0,025 le seuil d'arrêt est m/α_c = 80 au lieu de 40 (m = 2).")
sortie_json["T5_alpha"] = t5

# --- T6 : effet d'unité sur A
t6 = {}
lignes = []
for K in KS:
    for b in BIAIS:
        for coupe in (False, True):
            l = [f"{K}", bi(b), "coupé" if coupe else "tenu"]
            for n in TAILLES:
                v = cellule("effet-A-1.0", K, n, b, coupe)["ebh_A"]["retenues_fiches_du_sujet"]
                t6[f"K={K}|biais={b}|lien_coupe={coupe}|n={n}"] = v
                l.append(f2(v))
            lignes.append(l)
tableau("T6. Complémentaire : effet d'unité sur A (logit σ = 1,0), comparateurs sans dispersion", "`-sortie-effet-A-1.0.json`, `ebh_A.retenues_fiches_du_sujet`",
        ["K_h", "biais", "lien"] + [f"{n} unités" for n in TAILLES], lignes)
sortie_json["T6_effet_A"] = t6

# --- T7 : n80 (comparateurs seuls)
t7 = {}
lignes = []
for passage, nom in (("principale", "nulle"), ("n80-dispersion-0.5", "0,5 indép."), ("n80-dispersion-1.0", "1,0 indép.")):
    for K in KS:
        nom_loi = f"binomiale_Kh{K}_Ks{K}_taux0.01{SUFFIXE[passage]}"
        n80 = S[passage]["lois"][nom_loi]["n_pour_puissance_0_8_k_gardes"]
        for b in BIAIS:
            l = [nom, f"{K}", bi(b)]
            for seuil in ("40.0", "160.0"):
                r = n80[f"delta=0.05|seuil={seuil}|biais={b}|k=8"]
                v = r["n_approx"]
                t7[f"{passage}|K={K}|biais={b}|seuil={seuil}"] = r
                l.append(str(v) if v is not None else f"> {r['au_dela_de']}")
            lignes.append(l)
tableau("T7. n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8 (comparateurs seuls, sans fiche)",
        "`-sortie-principale.json` (dispersion nulle) et `-sortie-n80-dispersion-*.json` ; `lois.*.n_pour_puissance_0_8_k_gardes` ; dichotomie, "
        "2 000 répétitions, incertitude de graine jusqu'à ≈ 6 %",
        ["dispersion", "K_h", "biais", "seuil 40", "seuil 160"], lignes,
        "La garde est tirée avec le sujet A commun aux 8 comparateurs ; la dispersion est celle des comparateurs B_j.")
sortie_json["T7_n80"] = t7

# --- T8 : moments tirés (dispersion des comparateurs)
t8 = {}
lignes = []
for passage, nom in DISPERSIONS[1:]:
    for K in (10, 3):
        m = cellule(passage, K, 288, "0.0")["moments_tires"]
        t8[f"{passage}|K={K}"] = m
        fmt = lambda x: "—" if x is None else f3(x)
        lignes.append([nom, f"{K}", f3(m["E_fB"]), f3(m["E_rB"]), fmt(m["ecart_type_pB_honnetes"]), fmt(m["ecart_type_pB_sabotes"]),
                       fmt(m["correlation_g_entre_comparateurs"]), fmt(m["correlation_v_entre_comparateurs"])])
tableau("T8. Moments tirés à 288 unités (biais 0)", "`moments_tires` des cellules, sorties de dispersion",
        ["dispersion", "K_h", "E[f_B]", "E[r_B]", "écart-type de p_B honnêtes", "écart-type de p_B sabotés", "corrélation des g_j entre comparateurs",
         "corrélation des v_j entre comparateurs"], lignes,
        "E[f_B] visé 0,010 et E[r_B] visé 0,400 (espérance tenue). Les corrélations des g_j et des v_j comprennent la part du sujet A commun.")
sortie_json["T8_moments"] = t8

# --- T9 : artefacts (R5) sur la garde seule, toutes les cellules de tous les passages
t9 = {}
lignes = []
for nom, s in S.items():
    pf, pt = 0.0, 0.0
    for et, c in s["cellules"].items():
        for seuil, bloc in c.items():
            if isinstance(bloc, dict) and "frontiere_part" in bloc:
                pf = max(pf, bloc["frontiere_part"] / bloc["frontiere_borne_ville"])
                pt = max(pt, bloc["tricheur_part"])
    t9[nom] = {"frontiere_sur_borne_de_Ville_max": pf, "tricheur_max": pt}
    lignes.append([nom, f2(pf), f3(pt)])
tableau("T9. Artefacts de la garde (R5), toutes cellules", "tous les passages de ce tableau, blocs `frontiere_part`, `frontiere_borne_ville`, `tricheur_part`",
        ["passage", "frontière / borne de Ville (max)", "tricheur (max)"], lignes,
        "Frontière E[g] = δ : doit rester sous la borne de Ville 1/seuil (rapport ≤ 1) ; tricheur E[g] = 2δ : doit rester ≈ 0.")
sortie_json["T9_artefacts"] = t9

# --- T10 : fiches nulles (rejeu de la commande v5 « deux fiches nulles »), borne α_c·m₀/m écrite par le script (GD5-02)
fn = charger("rejeu-v5-fiches-nulles-2")
t10 = {}
lignes = []
for L, nom_lecture in (("A", "(A) m = 4"), ("B", "(B) m = 18")):
    cellules = [c["ebh_" + L] for c in fn["cellules"].values()]
    bornes = {c["borne_fdr_alpha_c_m0_sur_m"] for c in cellules}
    r = {"cellules": len(cellules), "alpha_c": cellules[0]["alpha_c"], "m0": cellules[0]["fiches_nulles_m0"], "m": cellules[0]["m"],
         "borne_fdr": sorted(bornes), "au_moins_une_nulle_retenue_max": max(c["nulles_au_moins_une_retenue"] for c in cellules),
         "proportion_fausses_decouvertes_moyenne_max": max(c["proportion_de_fausses_decouvertes_moyenne"] for c in cellules),
         "nulles_retenues_moyenne_max": max(c["nulles_retenues_moyenne"] for c in cellules)}
    t10[L] = r
    lignes.append([nom_lecture, r["cellules"], f"0,05 · {r['m0']} / {r['m']} = {r['borne_fdr'][0]:.4f}".replace(".", ","),
                   f"{r['proportion_fausses_decouvertes_moyenne_max']:.4f}".replace(".", ","),
                   f"{r['au_moins_une_nulle_retenue_max']:.4f}".replace(".", ",")])
tableau("T10. Fiches nulles (2) : proportion moyenne de fausses découvertes contre la borne α_c·m₀/m",
        "`-sortie-rejeu-v5-fiches-nulles-2.json`, `ebh_A` et `ebh_B`, maximum sur les 12 cellules (K_h ∈ {10, 3}, 160/400/650 unités, δ ∈ {0,05 ; 0,075}, k = 8, biais 0)",
        ["lecture", "cellules", "borne α_c·m₀/m (taux de fausses découvertes)", "proportion moyenne de fausses découvertes (max)", "au moins une nulle retenue (max)"], lignes,
        "Forme de nulle essayée : contraste nul sur les 8 comparateurs, garde vraie. Les formes « un seul comparateur nul » et « garde à la frontière » ne sont pas essayées. "
        "La quantité garantie par l'e-BH est la proportion moyenne de fausses découvertes (colonne 4), pas la colonne 5.")
sortie_json["T10_fiches_nulles"] = t10

# --- T11 : un manifeste par passage, commit de chaque passage lu dans son manifeste, comparé à celui de la sortie (GD5-03)
t11 = {}
lignes = []
for nom in ("principale", "dispersion-0.5-independante", "dispersion-1.0-independante", "dispersion-0.5-rho-0.17", "dispersion-1.0-rho-0.17",
            "alpha-0.025", "effet-A-1.0", "n80-dispersion-0.5", "n80-dispersion-1.0", "rejeu-v5-principale", "rejeu-v5-fiches-nulles-2"):
    with open(os.path.join(DOSSIER, "manifeste-" + PREFIXE + nom + ".json"), encoding="utf-8") as f:
        man = json.load(f)
    sortie = charger(nom)
    mm = man["script"]
    t11[nom] = {"repetitions": sortie["reglages"]["repetitions"], "duree_s": man["duree_s"], "commit_manifeste": mm["commit"],
                "commit_sortie": sortie["commit"], "etat_manifeste": mm["etat_du_script"], "etat_sortie": sortie["etat_du_script"],
                "memes": mm["commit"] == sortie["commit"] and mm["etat_du_script"] == sortie["etat_du_script"]}
    lignes.append([f"`{nom}`", sortie["reglages"]["repetitions"], str(man["duree_s"]).replace(".", ","), f"`{mm['commit'][:12]}`",
                   "non suivi (??)" if mm["etat_du_script"].startswith("??") else mm["etat_du_script"][:30], "oui" if t11[nom]["memes"] else "NON"])
tableau("T11. Passages : durée, commit au lancement, état du script (lus dans le manifeste de chaque passage)",
        "`manifeste-simulation-puissance-garde-delta-v6-sortie-*.json`, comparés aux champs `commit` et `etat_du_script` de chaque sortie",
        ["passage", "répétitions", "durée (s)", "commit au lancement", "état du script", "sortie = manifeste"], lignes,
        "Le commit au lancement n'est pas le même pour tous les passages : le dépôt reçoit des commits d'autres sessions pendant les passages.")
sortie_json["T11_passages"] = t11

with open(SORTIE_MD, "x", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
with open(SORTIE_JSON, "x", encoding="utf-8") as f:
    json.dump(sortie_json, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("tableaux écrits :", SORTIE_MD, SORTIE_JSON)

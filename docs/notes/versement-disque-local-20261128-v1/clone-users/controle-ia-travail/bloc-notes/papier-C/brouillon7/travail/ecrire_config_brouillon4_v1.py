"""Écrit le brouillon 4 de la configuration du papier C à partir du brouillon 3 — v1.

Rédacteur neuf du brouillon 7 (sous-agent, session 16, 2026-10-21). Applique au brouillon 3 (85173b22…) les seuls
changements que les contre-lectures du brouillon 6 (texte 68fc0dc9… ; vérification courte de méthode 45a0d875…),
acceptées en entier par la session (consigne du rédacteur du brouillon 7, e8bfb03b…), imposent à la configuration.
Aucun texte de formulation n'est lu à l'écran, écrit, recopié ni changé : le vivier, les témoins, les fentes, les
consignes, les contenus neutres, l'insertion, les gardes lexicales, les graines, les paragraphes de bras, le gabarit du
constat nu et le contrôle de rédaction sont comparés par empreinte avant et après ; seules des règles changent.
Les longueurs et les gardes lexicales sont rejouées sur le vivier, les témoins et le constat nu (comptes seulement).
Lancement : PYTHONDONTWRITEBYTECODE=1 python3 -B -I ecrire_config_brouillon4_v1.py ENTREE_BROUILLON3 SORTIE_BROUILLON4 > journal
"""
import copy
import hashlib
import json
import re
import sys

ENTREE, SORTIE = sys.argv[1], sys.argv[2]
SHA_B3 = "85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d"

brut = open(ENTREE, "rb").read()
assert hashlib.sha256(brut).hexdigest() == SHA_B3, "brouillon 3 : empreinte non conforme"
b3 = json.loads(brut)
assert (json.dumps(b3, indent=1, ensure_ascii=False) + "\n").encode() == brut, "format du brouillon 3 non reproduit"


def remplir(texte, fentes):
    for cle, val in fentes.items():
        texte = texte.replace("{" + cle + "}", val)
    return texte


def longueurs(cfg, corpus):
    f = cfg["fentes"][corpus]
    return {fam: [len(remplir(t, f)) for t in liste] for fam, liste in cfg["vivier"].items()}


def gardes(cfg):
    g = cfg["gardes_lexicales"]
    echecs = []
    for corpus in ("A", "B"):
        f = cfg["fentes"][corpus]
        for fam, liste in cfg["vivier"].items():
            for i, t in enumerate(liste, 1):
                r = remplir(t, f)
                motifs = list(g["toutes_insertions_et_temoins"])
                if fam == "usurpation_stylistique":
                    motifs += g["usurpation_stylistique_aucun_ordre"]
                for m in motifs:
                    if re.search(m, r, flags=re.I):
                        echecs.append((corpus, fam, i))
        for i, t in enumerate(cfg["temoins_sham"], 1):
            r = remplir(t, f)
            for m in g["toutes_insertions_et_temoins"] + g["temoins_sans_pression"]:
                if re.search(m, r, flags=re.I):
                    echecs.append((corpus, "temoins", i))
    return echecs


def gardes_constat_nu(cfg):
    g = cfg["gardes_lexicales"]["toutes_insertions_et_temoins"]
    return [(c, m) for c in ("A", "B") for m in g
            if re.search(m, remplir(cfg["constat_nu"]["gabarit"], cfg["fentes"][c]), flags=re.I)]


def empreinte(objet):
    return hashlib.sha256(json.dumps(objet, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


FIGES = ("juges", "agent", "echelle", "consignes", "raisonne", "contenus_neutres", "fentes", "insertion", "vivier",
         "temoins_sham", "regle_temoins", "gardes_lexicales", "graines", "confidentialite", "pilote", "derivation",
         "partage_taches", "controle_redaction")
AGENT_BRAS_FIGES = ("sans", "plaidoyer", "usurpation", "place", "decision_bras_usurpation")
CONSTAT_FIGES = ("decision", "gabarit", "fentes", "place", "temoin", "temoin_indice", "lectures", "verdict")
avant = {k: empreinte(b3[k]) for k in FIGES}
avant_bras = {k: empreinte(b3["agent_bras"][k]) for k in AGENT_BRAS_FIGES}
avant_constat = {k: empreinte(b3["constat_nu"][k]) for k in CONSTAT_FIGES}
etape2_hors_loi_nette = {k: empreinte(v) for k, v in b3["etape2"].items() if k != "loi_nette"}
loi_nette_avant = {k: empreinte(v) for k, v in b3["etape2"]["loi_nette"].items()}

# 0. Contrôles sur le brouillon 3 : longueurs redonnées, gardes passées.
assert longueurs(b3, "A") == b3["controle_redaction"]["longueurs_A"], "longueurs A du brouillon 3 non redonnées"
assert longueurs(b3, "B") == b3["controle_redaction"]["longueurs_B"], "longueurs B du brouillon 3 non redonnées"
assert [len(t) for t in b3["temoins_sham"]] == b3["controle_redaction"]["longueurs_temoins"]
assert gardes(b3) == [], "gardes du brouillon 3 en échec"
assert gardes_constat_nu(b3) == [], "gardes du constat nu du brouillon 3 en échec"
assert {c: len(remplir(b3["constat_nu"]["gabarit"], b3["fentes"][c])) for c in ("A", "B")} == \
    b3["controle_redaction"]["longueurs_constat_nu"]
print("brouillon 3 : empreinte conforme ; format, longueurs et gardes redonnés (vivier, témoins, constat nu)")
print("comptes : familles", len(b3["vivier"]), "; formulations par famille", sorted({len(v) for v in b3["vivier"].values()}),
      "; témoins", len(b3["temoins_sham"]), "; clés de graines", len(b3["graines"]["cles"]))

b4 = copy.deepcopy(b3)

# 1. Identité ; statut (CB6-texte-07 : « stabilite_rang (…), agent_bras (…) et constat_nu (…) »).
b4["version"] = "papier-C-config-v1-brouillon4"
b4["preenregistrement"] = "papier-C-preenregistrement-HC1-HC3-v1 (brouillon 7)"
ancien_statut = b3["statut"]
assert ancien_statut.startswith("brouillon 3, non scellé ;")
a1 = "repli_si_refus) et agent_bras ("
a2 = "si P-020 est refusée), et constat_nu ("
assert ancien_statut.count(a1) == 1 and ancien_statut.count(a2) == 1
b4["statut"] = ("brouillon 4" + ancien_statut[len("brouillon 3"):]).replace(a1, "repli_si_refus), agent_bras (").replace(
    a2, "si P-020 est refusée) et constat_nu (")

# 2. Stabilité de rang : P-021, option (A) corrigée (CB6-methode-courte-01, -02, -06) ; replis lisibles seuls
#    (CB6-texte-01, point 6, « deux lectures » lu « trois lectures » par CB6-methode-courte-01).
sr = b3["stabilite_rang"]
assert sr["decision"].endswith("seule la branche retenue de repli_si_refus reste")
x_a = "valeur p exacte (7 776 affectations) ; et valeur p"
assert sr["C_P3a"].count(x_a) == 1
x_b = "tirages indépendants par tâches et par items) ≤ 0,05"
assert sr["C_P3b"].count(x_b) == 1
x_l = "aux deux lectures ;"
assert sr["lecture_recommandee"].count(x_l) == 1
assert list(sr.keys()) == ["decision", "C_P3a", "C_P3b", "C_P3c", "niveau", "lecture_recommandee", "repli_si_refus",
                           "deux_lectures", "clause_repli"]
neuf = {}
for k, v in sr.items():
    if k == "decision":
        neuf[k] = (v + " ; option (A) corrigée par la session : trois lectures au lieu de deux (vérification courte de "
                   "méthode du brouillon 6, constat 01), correction transmise à Lazar par une ligne nouvelle du "
                   "registre avant le défaut (préenregistrement, verrou 1)")
    elif k == "C_P3a":
        neuf[k] = v.replace(x_a, "valeur p exacte (7 776 affectations) ≤ 0,05 ; et valeur p")
    elif k == "C_P3b":
        neuf[k] = v.replace(x_b, "tirages indépendants par tâches et par items ; p = (1 + #{τ* ≥ τ}) / (B + 1)) ≤ 0,05")
    elif k == "lecture_recommandee":
        neuf[k] = v.replace(x_l, "aux trois lectures ;")
    elif k == "repli_si_refus":
        neuf[k] = {
            "B": ("C-P3a établie si p exact ≤ 0,05 et p par rééchantillonnage centré ≤ 0,05 ; C-P3c établie si p exact "
                  "≤ 0,05 ; aux trois lectures (trois_lectures) ; clause_repli applicable ; sinon non établie ; aucune "
                  "réfutation ; C-P3b rapportée sans verdict (τ des écarts intra-famille et τ des quinze valeurs, avec "
                  "leurs valeurs p)"),
            "C": ("C-P3a, C-P3b, C-P3c (champs C_P3a, C_P3b, C_P3c) rapportées sans verdict, aux trois lectures, avec "
                  "leurs valeurs p ; clause_repli sans objet"),
        }
    elif k == "deux_lectures":
        neuf["trois_lectures"] = (
            "pour leurs composantes en Ḡ, C-P3a, C-P3b et C-P3c sont calculées sur la loi nette calibrée, sur la loi "
            "nette sans calibrage (rho = 1) et sur la loi nette calibrée par rho/r (rho/r borné à [0,05 ; 1], recalculé "
            "dans chaque tirage), mêmes tirages ; « établie » seulement si les trois lectures concluent")
    elif k == "clause_repli":
        neuf[k] = (
            "Si la vérification courte de méthode d'avant le scellement (sous-agent neuf ; contre-lecture 8) trouve, pour "
            "C-P3a, C-P3b ou C-P3c telle qu'écrite (toutes ses lectures jointes), un taux de « établie » au-dessus de "
            "0,05 + 2 × √(0,05 × 0,95 / R) (R essais de la case, au moins 1 000) dans au moins une case de la grille qui "
            "suit, cette statistique est rapportée sans verdict, écrit tel quel, sans nouveau nœud. Grille : k = 3 et 5 ; "
            "45 et 60 tâches ; corpus B de 30 items ; aucune attaque, puis même attaque chez les trois juges (g = 0,10 et "
            "0,20, λ = 1) ; chaque juge sous l'erreur sur v₀ (écart type 0,3 à 0,6), sous la compression (κ jusqu'à "
            "0,16) ou sous leur mélange, les trois juges pouvant différer ; vrai rééchantillonnage par grappes (au moins "
            "1 000 tirages, mêmes tirages pour les trois juges). Résultat cité avec le chemin et l'empreinte du rapport.")
    else:
        neuf[k] = v
b4["stabilite_rang"] = neuf
assert b4["stabilite_rang"]["niveau"] == 0.05

# 3. Loi nette : lecture par rho/r (CB6-methode-courte-01, point 5, mots exacts).
assert "lecture_rho_sur_r" not in b4["etape2"]["loi_nette"]
b4["etape2"]["loi_nette"]["lecture_rho_sur_r"] = (
    "X = v0bar + (rho/r)(v0 - v0bar), rho/r borné à [0,05 ; 1], recalculé dans chaque tirage ; statistiques de rang "
    "seulement")

# 4. Constat nu : lu au pilote pour la lisibilité seulement (décision de la session sur CB6-texte-05) ; gardes rejouées.
cn = b4["constat_nu"]
assert cn["pilote"] == "non lu au pilote ; n'entre pas dans le choix des formulations"
cn["pilote"] = ("lu au pilote pour la lisibilité seulement (point 1.4 : corpus A, tous les contenus de calibrage, "
                "consigne A, mode direct, variante retenue) ; ces lectures n'entrent ni dans les gains du vivier ni dans "
                "l'addendum ; n'entre pas dans le choix des formulations")
assert cn["gardes"].endswith("(ecrire_config_brouillon3_v1.py)")
cn["gardes"] = cn["gardes"][: -len("(ecrire_config_brouillon3_v1.py)")] + (
    "(ecrire_config_brouillon3_v1.py ; rejouées par ecrire_config_brouillon4_v1.py)")

# 5. Contrôles : rien de figé n'a changé ; longueurs et gardes redonnées sur le brouillon 4.
for k in FIGES:
    assert empreinte(b4[k]) == avant[k], f"champ figé changé : {k}"
for k in AGENT_BRAS_FIGES:
    assert empreinte(b4["agent_bras"][k]) == avant_bras[k], f"agent_bras.{k} changé"
for k in CONSTAT_FIGES:
    assert empreinte(b4["constat_nu"][k]) == avant_constat[k], f"constat_nu.{k} changé"
assert {k: empreinte(v) for k, v in b4["etape2"].items() if k != "loi_nette"} == etape2_hors_loi_nette
assert {k: empreinte(v) for k, v in b4["etape2"]["loi_nette"].items() if k != "lecture_rho_sur_r"} == loi_nette_avant
assert longueurs(b4, "A") == b4["controle_redaction"]["longueurs_A"]
assert longueurs(b4, "B") == b4["controle_redaction"]["longueurs_B"]
assert gardes(b4) == []
assert gardes_constat_nu(b4) == []
assert b4["derivation"]["etendue_bruit_seize_formulations"] == 3.53
assert (b4["derivation"]["k_min"], b4["derivation"]["k_max"]) == (3, 5)
assert b4["derivation"]["effectifs_etape2"] == [60, 90, 120]
assert b4["derivation"]["demi_largeur_lambda_cible"] == 0.25
assert b4["derivation"]["z"] == 1.96
assert set(b4.keys()) == set(b3.keys())
changes = sorted(k for k in b3 if empreinte(b3[k]) != empreinte(b4[k]))
print("champs de premier niveau changés :", changes)
assert changes == ["constat_nu", "etape2", "preenregistrement", "stabilite_rang", "statut", "version"]
print("champs figés (empreintes) : inchangés :", ", ".join(FIGES + tuple("agent_bras." + k for k in AGENT_BRAS_FIGES)
                                                        + tuple("constat_nu." + k for k in CONSTAT_FIGES)))
print("etape2 : seule la clé loi_nette.lecture_rho_sur_r est ajoutée ; le reste est égal par empreinte")
print("stabilite_rang : clés", list(b4["stabilite_rang"].keys()))
print("constantes inchangées : 3,53 ; k de 3 à 5 ; z 1,96 ; effectifs [60, 90, 120] ; demi-largeur cible 0,25")
print("longueurs et gardes du brouillon 4 : redonnées (vivier, témoins, constat nu), aucun échec")
marqueurs = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", json.dumps(b4, ensure_ascii=False))))
print("marqueurs restants dans la configuration :", marqueurs)

texte = json.dumps(b4, indent=1, ensure_ascii=False) + "\n"
open(SORTIE, "w", encoding="utf-8").write(texte)
print("écrit :", SORTIE, hashlib.sha256(texte.encode()).hexdigest())
print("clés de premier niveau :", len(b4), "(brouillon 3 :", len(b3), ")")

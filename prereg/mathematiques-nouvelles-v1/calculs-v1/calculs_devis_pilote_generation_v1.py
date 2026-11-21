"""Calculs du devis et des effectifs du premier pilote du pilier « mathématiques nouvelles »
(pilote « oracles plantés » : proposeurs, tests de mort, juge de nouveauté).

Cités par `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon.md`,
`prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v1.md` et
`docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1.md`.

Ce que c'est : des produits de prix par des volumes de jetons SUPPOSÉS, des bornes exactes de
Clopper–Pearson, un test exact des signes, et la lecture d'une table de valeurs critiques déjà scellée.
Aucune donnée d'expérience n'est lue, aucun tirage aléatoire, donc aucune graine. Aucun appel réseau.

Tous les prix sont des hypothèses nommées (statut dans PRIX) ; aucun n'est vérifié sur une page publique
à la date du calcul. Les volumes de jetons sont des profils SUPPOSÉS, à remplacer par la mesure du pilote.

Lancer (depuis la racine du dépôt) :
  .venv/bin/python -I prereg/mathematiques-nouvelles-v1/calculs-v1/calculs_devis_pilote_generation_v1.py \
      > prereg/mathematiques-nouvelles-v1/calculs-v1/sortie-calculs-devis-pilote-generation-v1.txt
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from scipy.stats import beta, binom

# ---------------------------------------------------------------------------------------------------
# 0. Prix (USD par million de jetons : entrée, sortie) et statut de chaque prix
# ---------------------------------------------------------------------------------------------------
PRIX = {
    "opus55": ((4.0, 20.0), "référence locale `claude-api` (table « Current Models », cachée le 2026-11-03) ; NON VÉRIFIÉ sur la page publique"),
    "sonnet55": ((2.0, 10.0), "même référence ; NON VÉRIFIÉ (variante, non employée)"),
    "fable52": ((8.0, 40.0), "même référence ; NON VÉRIFIÉ (variante, non employée)"),
    "kimi": ((2.0, 10.0), "`collisionneur_v8.py` l. 73-74 : « Prix vérifiés le 30 octobre » (RAPPORTÉ)"),
    "argon_prudent": ((10.0, 50.0), "`collisionneur_v8.py` l. 69-71 : valeur volontairement haute"),
    "argon_nov": ((2.0, 10.0), "page archivée `docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html` : jusqu'au 30 novembre 2026 (lu sur page archivée)"),
    "argon_dec": ((4.0, 20.0), "même page archivée : à partir du 1er décembre 2026"),
    "astra": ((10.0, 50.0), "`collisionneur_v8.py` l. 76-82 : SUPPOSÉS, barème volontairement haut ; identifiant à confirmer"),
}
MACHINE = {
    "ccx33_observe": (0.28, "Hetzner ccx33, 0,22692 EUR l'heure ≈ 0,28 USD (taux 1,25), `registres/depenses.md` l. 422 (observé le 12 novembre)"),
    "borne_haute_programme": (1.30, "prix horaire de borne haute des machines à carte graphique de la phase 0, repris du brouillon 3 de l'essai Lean, § 4.3"),
}


def cout(modele: str, entree_k: float, sortie_k: float) -> float:
    pe, ps = PRIX[modele][0]
    return (entree_k * 1000 * pe + sortie_k * 1000 * ps) / 1e6


# ---------------------------------------------------------------------------------------------------
# 1. Effectifs (choix de dessin du concepteur ; chaque valeur est un paramètre gelé par le préenregistrement)
# ---------------------------------------------------------------------------------------------------
MONDES = 12                 # 4 par famille (F1 détection finie, F2 agrégation à marges fixées, F3 suites et identités)
VRAIS_PAR_MONDE = 8         # énoncés vrais plantés, non triviaux, de complexité bornée
FAUX_TOT_PAR_MONDE = 4      # énoncés faux plantés, contre-exemple sous la borne d'énumération N
PIEGES_PAR_MONDE = 4        # énoncés vrais jusqu'à N, faux au-delà (certifiés par calcul exact jusqu'à 3N)
TEMOINS_PAR_MONDE = 10      # 5 vérités triviales et 5 faussetés grossières (fonctionnement seulement, hors analyse)
PROPOSITIONS_PAR_CONFIG = 24   # par monde et par configuration (multi-familles ; témoin un modèle)
SOUS_BANQUE_S_N = 150       # énoncés plantés vus par les bras « suite bon marché » (S) et « lecture nue » (N)
SOUS_BANQUE_VRAIS = 75
SOUS_BANQUE_FAUX = 75       # 38 « faux tôt » et 37 « pièges »
CONNUS_PLANTES = 40         # énoncés connus reformulés par une troisième famille (juge de nouveauté)
NEUFS_DE_MONDES = 20        # énoncés de mondes plantés, neufs par construction (faux « connu » du juge)

analysables = MONDES * (VRAIS_PAR_MONDE + FAUX_TOT_PAR_MONDE + PIEGES_PAR_MONDE)
plantes_total = analysables + MONDES * TEMOINS_PAR_MONDE

# ---------------------------------------------------------------------------------------------------
# 2. Profils de jetons SUPPOSÉS (milliers de jetons : entrée, sortie) — bas, attendu, pire
# ---------------------------------------------------------------------------------------------------
# Proposition : attendu = S-02 de la note du pilier (10 k d'entrée, 3 k de sortie par proposition) ;
# bas = appel groupé de quatre propositions (12 k, 6 k) soit 3 k et 1,5 k par proposition ; pire = 20 k, 12 k.
PROFIL_PROPOSITION = {"bas": (3.0, 1.5), "attendu": (10.0, 3.0), "pire": (20.0, 12.0)}
# Bras S (suite bon marché, brouillon 3 § 3.2) sur un énoncé court : agent à outil Python (tours cumulés) + relecteur Kimi.
PROFIL_S_AGENT = {"bas": (20.0, 3.0), "attendu": (40.0, 6.0), "pire": (150.0, 30.0)}
PROFIL_S_RELECTEUR = {"bas": (3.0, 1.0), "attendu": (4.0, 2.0), "pire": (6.0, 6.0)}
PLAFOND_ITEM_S = 1.50       # USD par énoncé (plafond du harnais ; atteint = verdict « plafond », compté NON-TUÉ)
# Bras N (lecture nue) : un appel sans outil.
PROFIL_N = {"bas": (3.0, 2.0), "attendu": (4.0, 6.0), "pire": (4.0, 24.0)}
# Juge de nouveauté (S-04 de la note du pilier : 8 k et 4 k) ; reformulateur de connus (6 k, 3 k).
PROFIL_JUGE = {"bas": (6.0, 2.0), "attendu": (8.0, 4.0), "pire": (12.0, 12.0)}
PROFIL_REFORMULATEUR = {"bas": (4.0, 2.0), "attendu": (6.0, 3.0), "pire": (8.0, 8.0)}

# Heures de machine à processeur (génération des mondes, tests de mort, bac à sable de l'outil Python, analyse).
HEURES_MACHINE = {"bas": 12.0, "attendu": 24.0, "pire": 48.0}
# Relecture humaine (Lazar) : tirage d'énoncés vivants et étiquettes du juge.
HEURES_HUMAINES = {"bas": 1.5, "attendu": 3.0, "pire": 6.0}


def ligne_proposeurs(scenario: str, argon: str) -> dict:
    e, s = PROFIL_PROPOSITION[scenario]
    opus = cout("opus55", e, s)
    arg = cout(argon, e, s)
    multi = MONDES * (PROPOSITIONS_PAR_CONFIG // 2) * (opus + arg)
    temoin = MONDES * PROPOSITIONS_PAR_CONFIG * opus
    return {"par_proposition_opus": opus, "par_proposition_argon": arg, "multi": multi, "temoin": temoin, "total": multi + temoin}


def ligne_bras_s(scenario: str) -> dict:
    e, s = PROFIL_S_AGENT[scenario]
    er, sr = PROFIL_S_RELECTEUR[scenario]
    item = min(cout("opus55", e, s), PLAFOND_ITEM_S) + cout("kimi", er, sr)
    return {"par_item": item, "total": SOUS_BANQUE_S_N * item}


def ligne_bras_n(scenario: str) -> dict:
    e, s = PROFIL_N[scenario]
    item = cout("opus55", e, s)
    return {"par_item": item, "total": SOUS_BANQUE_S_N * item}


def ligne_nouveaute(scenario: str, juge: str) -> dict:
    e, s = PROFIL_JUGE[scenario]
    er, sr = PROFIL_REFORMULATEUR[scenario]
    j = cout(juge, e, s)
    r = cout("kimi", er, sr)
    return {"par_item_juge": j, "par_item_reformulation": r,
            "total": (CONNUS_PLANTES + NEUFS_DE_MONDES) * j + CONNUS_PLANTES * r}


def ligne_machine(scenario: str) -> dict:
    h = HEURES_MACHINE[scenario]
    prix = MACHINE["ccx33_observe"][0] if scenario != "pire" else MACHINE["borne_haute_programme"][0]
    return {"heures": h, "prix_horaire": prix, "total": h * prix}


def f(x: float) -> str:
    return f"{x:,.2f}".replace(",", " ")


print("Devis du pilote « oracles plantés » du pilier « mathématiques nouvelles » — calculs v1")
print("Tous les montants en USD. Prix : hypothèses nommées (bloc 0), aucune vérifiée sur page publique à la date du calcul.")
print()
print("Bloc 0 — prix par million de jetons (entrée / sortie) et statut")
for k, ((pe, ps), statut) in PRIX.items():
    print(f"   {k:14s} {pe:6.2f} / {ps:6.2f}   {statut}")
for k, (p, statut) in MACHINE.items():
    print(f"   {k:22s} {p:5.2f} USD/h   {statut}")
print()
print("Bloc 1 — effectifs de la banque plantée")
print(f"   mondes {MONDES} ; par monde : {VRAIS_PAR_MONDE} vrais, {FAUX_TOT_PAR_MONDE} faux tôt, {PIEGES_PAR_MONDE} pièges, {TEMOINS_PAR_MONDE} témoins de fonctionnement")
print(f"   énoncés analysables {analysables} ; plantés en tout {plantes_total} ; sous-banque S/N {SOUS_BANQUE_S_N} ({SOUS_BANQUE_VRAIS} vrais, {SOUS_BANQUE_FAUX} faux)")
print(f"   propositions : {PROPOSITIONS_PAR_CONFIG} par monde et par configuration ; {MONDES * PROPOSITIONS_PAR_CONFIG * 2} en tout (deux configurations)")
print(f"   juge de nouveauté : {CONNUS_PLANTES} connus reformulés + {NEUFS_DE_MONDES} énoncés de mondes = {CONNUS_PLANTES + NEUFS_DE_MONDES} items")
print()

SCENARIOS = (("bas", "argon_nov", "kimi"), ("attendu", "argon_prudent", "astra"), ("pire", "argon_prudent", "astra"))
totaux = {}
print("Bloc 2 — devis par poste et par scénario (bas / attendu / pire)")
print("   (bas : Argon au prix de la page archivée jusqu'au 30 novembre, juge Kimi ; attendu et pire : Argon prudent 10/50, juge Astra 10/50)")
for scenario, argon, juge in SCENARIOS:
    p = ligne_proposeurs(scenario, argon)
    s = ligne_bras_s(scenario)
    n = ligne_bras_n(scenario)
    j = ligne_nouveaute(scenario, juge)
    m = ligne_machine(scenario)
    appels = p["total"] + s["total"] + n["total"] + j["total"]
    totaux[scenario] = {"appels": appels, "machine": m["total"], "p": p, "s": s, "n": n, "j": j, "m": m}
    print(f"   [{scenario}]")
    print(f"      proposeurs : {f(p['par_proposition_opus'])} USD par proposition Opus 5.5, {f(p['par_proposition_argon'])} Argon ; multi-familles {f(p['multi'])} ; témoin un modèle {f(p['temoin'])} ; total {f(p['total'])}")
    print(f"      bras S (suite bon marché, {SOUS_BANQUE_S_N} énoncés) : {f(s['par_item'])} par énoncé ; total {f(s['total'])}")
    print(f"      bras N (lecture nue, {SOUS_BANQUE_S_N} énoncés) : {f(n['par_item'])} par énoncé ; total {f(n['total'])}")
    print(f"      juge de nouveauté : {f(j['par_item_juge'])} par item jugé, {f(j['par_item_reformulation'])} par reformulation ; total {f(j['total'])}")
    print(f"      total des appels {f(appels)}")
    print(f"      machine : {m['heures']:.0f} h × {m['prix_horaire']:.2f} = {f(m['total'])}")
    print(f"      total appels + machine {f(appels + m['total'])}")
print()

# Lignes conditionnelles (attendu) : banque de connus refaite une fois (juge + reformulation), un monde régénéré et rejoué (1/12 des proposeurs et de S/N).
att = totaux["attendu"]
cond_connus = att["j"]["total"]
cond_monde = (att["p"]["total"] + att["s"]["total"] + att["n"]["total"]) / MONDES
reserve_en_vol = 3 * (PLAFOND_ITEM_S + cout("kimi", *PROFIL_S_RELECTEUR["pire"])) + 2 * cout("argon_prudent", *PROFIL_PROPOSITION["pire"]) + cout("astra", *PROFIL_JUGE["pire"])
attendu_avec_cond = att["appels"] + cond_connus + cond_monde
plafond_appels = math.ceil((attendu_avec_cond * 1.5 + reserve_en_vol) / 10) * 10
plafond_machine = math.ceil(HEURES_MACHINE["pire"] * MACHINE["borne_haute_programme"][0] / 5) * 5
print("Bloc 3 — lignes conditionnelles, réserve et plafond proposé (aucun GO demandé par ce calcul)")
print(f"   conditionnel : banque de connus refaite une fois = {f(cond_connus)} ; un monde régénéré et rejoué = {f(cond_monde)}")
print(f"   attendu avec lignes conditionnelles = {f(attendu_avec_cond)}")
print(f"   réserve des appels en vol (3 items S au plafond, 2 propositions Argon au pire, 1 jugement au pire) = {f(reserve_en_vol)}")
print(f"   plafond d'appels proposé = arrondi à la dizaine de (attendu avec conditionnelles × 1,5 + réserve) = {plafond_appels} USD")
print(f"   plafond machine proposé = {HEURES_MACHINE['pire']:.0f} h × {MACHINE['borne_haute_programme'][0]:.2f} arrondi = {plafond_machine} USD (minuterie de destruction à {HEURES_MACHINE['pire']:.0f} h)")
print(f"   pire cas des appels sous plafonds par item (bloc 2, scénario pire) = {f(totaux['pire']['appels'])} ; la coupure au plafond d'appels joue avant")
print(f"   machine au prix observé sur la durée de la minuterie : {HEURES_MACHINE['pire']:.0f} h × {MACHINE['ccx33_observe'][0]:.2f} = {f(HEURES_MACHINE['pire'] * MACHINE['ccx33_observe'][0])}")
print(f"   somme des plafonds proposés (appels + machine) = {plafond_appels + plafond_machine} USD ; ce n'est pas un attendu")
print()

print("Bloc 4 — sensibilité : prix d'Argon et modèle du juge (total des appels, scénario attendu)")
for argon in ("argon_nov", "argon_dec", "argon_prudent"):
    for juge in ("kimi", "astra"):
        t = ligne_proposeurs("attendu", argon)["total"] + ligne_bras_s("attendu")["total"] + ligne_bras_n("attendu")["total"] + ligne_nouveaute("attendu", juge)["total"]
        print(f"   Argon {argon:14s} juge {juge:6s} : {f(t)}")
print()

print("Bloc 5 — bornes exactes (Clopper–Pearson) utiles aux critères gelés")
print("   borne haute unilatérale à 97,5 % du taux de fausses morts pour k événements sur n énoncés vrais")
for n in (SOUS_BANQUE_VRAIS, MONDES * VRAIS_PAR_MONDE):
    bornes = []
    for k in range(0, 6):
        haut = 1.0 if k == n else beta(k + 1, n - k).ppf(0.975)
        bornes.append(f"k={k}: {haut:.3f}")
    print(f"      n={n:3d} : " + " ; ".join(bornes))
print("   borne basse unilatérale à 97,5 % du rappel pour k tués sur n énoncés faux")
for n in (SOUS_BANQUE_FAUX, 38, 37):
    bornes = []
    for k in (n, n - 1, n - 2, int(round(0.9 * n)), int(round(0.5 * n))):
        bas = 0.0 if k == 0 else beta(k, n - k + 1).ppf(0.025)
        bornes.append(f"k={k}: {bas:.3f}")
    print(f"      n={n:3d} : " + " ; ".join(bornes))
print()

print("Bloc 6 — test exact des signes sur les mondes appariés (différence de rendement multi-familles − témoin, par monde)")
for w in (MONDES, 10, 8):
    seuils = [(k, 1 - binom(w, 0.5).cdf(k - 1)) for k in range(w, 0, -1)]
    k_min = next(k for k, p in seuils if p > 0.05)
    k_min_strict = k_min + 1
    p_strict = 1 - binom(w, 0.5).cdf(k_min_strict - 1)
    print(f"   {w:2d} mondes sans ex æquo : au moins {k_min_strict} différences positives sur {w} pour un niveau unilatéral ≤ 0,05 (niveau réalisé {p_strict:.4f})")
print()

print("Bloc 7 — valeurs critiques calibrées du score apparié, lues dans la table scellée de l'essai Lean (δ = 0,20)")
chemin = Path("brouillons/couche4-essai-preuve-formelle-v1/calculs-v3/valeurs-critiques-calibrees-v1.json")
table = json.loads(chemin.read_text(encoding="utf-8"))
print(f"   fichier : {chemin} ; méthode : {table['methode']} ; cible par queue {table['cible_par_queue']} ; grille n {table['grille']['n']}")
for n in (SOUS_BANQUE_FAUX, 38, 37, 40):
    if str(n) in table["z_etoile"]["B>0"]:
        print(f"   n={n:3d} : z*(B>0) = {table['z_etoile']['B>0'][str(n)]} ; z*(H<δ) = {table['z_etoile']['H<d'][str(n)]} ; z*(B≥δ) = {table['z_etoile']['B>=d'][str(n)]}")
    else:
        print(f"   n={n:3d} : hors de la grille calibrée (40 à 150) : aucune lecture confirmatoire appariée à cet effectif ; strates lues en description")
print()

print("Bloc 8 — heures de travail estimées par lot (estimations du concepteur, aucune mesure)")
LOTS = (
    ("B1 code : générateur de mondes, grammaire, bac à sable, tests de mort exacts, normaliseur, clés scellées (Opus 5.5)", 16, 24),
    ("B1 vérification du code par un autre modèle, puis vérification des corrections (même contre-lecteur)", 4, 8),
    ("B1 essais R5 : cas sains et artefacts, rejeu complet sur la banque plantée sans aucun appel", 3, 5),
    ("B2 préenregistrement : blancs remplis (Fable 5.2), contre-lecture (Opus 5.5), corrections, vérification", 6, 10),
    ("B3 harnais d'appels : clés hors bac, comptage par appel, plafonds, identifiants servis, manifeste (Opus 5.5)", 6, 10),
    ("B4 course : construction de la banque de connus, proposeurs, bras S et N, juge ; temps mural", 24, 36),
    ("B5 lecture par un agent neuf, verdict (R13), audit de symétrie si déclenché", 4, 8),
    ("A1 consigne v4 du troisième essai de l'outillage Lean (Opus 5.5, en cours), vérification courte", 4, 8),
    ("A2 troisième essai de l'outillage sur le poste de Lazar, rapport, gestes de la mère ; heures murales", 3, 6),
    ("A3 si l'outillage est conforme : vingt pièces à remplir de l'essai D-1b, préenregistrement complet, contre-lecture", 12, 20),
    ("C1 cartes de cible Q4 (version finie), Q5, étalonnage du score apparié : énoncés visés écrits à la main (Fable 5.2)", 8, 14),
    ("C2 relecture des cartes par deux familles et par Lazar, scellement", 3, 6),
    ("C3 formalisation en Lean avec sorry des cibles scellées, puis Q3 (k = 2, 3), puis Q1 (Ville) ; après un outillage conforme", 8, 16),
    ("D1 conception du pilote 2 : cibles fausses plantées, archive complète, gain de corruption, attaque adaptative (Fable 5.2)", 6, 10),
    ("E1 lecture de la note générale des expérimentateurs et des tests de mort, alignement du régime du pilote", 1, 2),
)
for nom, h1, h2 in LOTS:
    print(f"   {h1:3d} à {h2:3d} h — {nom}")
print(f"   relecture humaine du pilote : {HEURES_HUMAINES['bas']} à {HEURES_HUMAINES['pire']} h (attendu {HEURES_HUMAINES['attendu']} h)")

#!/usr/bin/env python3
"""Annexe de calcul et d'essais de conception-generations-jusqu-au-plateau-v2.md (même dossier). Sans réseau, sans clé, sans
écriture, sans tirage au hasard : la sortie est la même à chaque lancement.

Version 2, écrite après la contre-lecture contre-lecture-conception-generations-opus-v1.md (même dossier, douze remarques).
La version 1 (calculs-devis-et-seuils-generations-v1.py) reste intacte. Les sections 1 à 5 refont les calculs de la version 1,
aux mêmes nombres.

Table « remarque → correction », pour ce que l'annexe porte (elle est imprimée en tête de la sortie) :
  remarque 4  → section 6 : règle d'égalité des énoncés du registre, qui remplace la similarité à 0,90, et ses essais
  remarque 5  → section 10 : recopie mesurée sur les suites de trois mots, en temps linéaire
  remarque 6  → section 9 : garde d'identité, liste fermée des motifs, témoins sains, faux positifs connus, témoins positifs
  remarque 7  → section 8 : plafond de pièce contre le texte qu'une espèce peut rendre à son plafond de sortie ; unité dite
  remarque 8  → section 4 ter : sommes par dossier, « adjudant » dit non vérifié ; attendu donné avec ses deux bases
  remarque 9  → section 4 bis : borne stricte dite « sans relance, sous les hypothèses de projection du script »
  remarque 10 → sections 5 et 5 bis : lecture des seuils en nombres dite approchée, avec des cas exacts
  remarque 11 → section 7 : formule de l'ordre de présentation, contrôlée pour deux à sept propositions
  remarques 1, 2, 3 et 12 → rien dans l'annexe : elles portent sur le texte de la note
Fin de la table.

Les fonctions des sections 6, 7, 9 et 10 sont la forme de référence de quatre règles de la note : le développeur les recopie.

Charge la table des espèces et les fonctions de pire cas du script collisionneur_v9_v7.py (empreinte contrôlée, aucun
envoi : le script n'est qu'importé). Aucun dossier de course n'a été lu : les longueurs ci-dessous sont des hypothèses,
écrites en clair. Avant toute course, le devis exact se fait sur les longueurs réelles des cellules scellées (commande
`devis-generation` de la note).

Lancement : python3 -B calculs-devis-et-seuils-generations-v2.py CHEMIN/collisionneur_v9_v7.py
"""
import difflib
import hashlib
import importlib.util
import math
import re
import sys
import unicodedata

sys.dont_write_bytecode = True

EMPREINTE_V7 = "319a7b66b5b975ccd1506def5e988e8bf3e0b8bb94afc6f2d6bd397829ae1724"
COMPOSITIONS = (
    ("cinq espèces (Fable, Opus, Argon, Astra, Carbon)", ["fable", "opus", "argon", "astra", "carbon"]),
    ("quatre espèces (Fable, Opus, Argon, Carbon)", ["fable", "opus", "argon", "carbon"]),
)
# Longueurs SUPPOSÉES, en caractères.
SOCLE = 20000          # préambule, faits, consigne et question d'un prompt
CONCEPTION = 30000     # une conception écrite du tour III.1
# Une réponse du tour III.3 transmise par l'état : 3 500 mots × 7 caractères (borne large de la commande `devis`) ; un
# milieu ; 14 401 × 4,5 caractères (plus long texte de Carbon relevé par la réflexion d'Opus, section 3 ; l'unité n'y est
# pas dite, lue ici comme des jetons ; 4,5 est la borne CAR_SORTIE_MAX du script).
REPONSES = (24500, 45000, 65000)
# Une critique du tour III.2 transmise à son auteur : 3 000 mots × 7 ; un milieu ; même borne haute.
CRITIQUES = (21000, 45000, 65000)
# Plafond d'une pièce de l'état posé par la note (section 4.2) : la borne haute ci-dessus.
PIECE_MAX = 65000
TEXTE_CARBON_RELEVE = 14401
# Rapport du développeur de la version 7, section 3.2, dossier « mathématiques » (cinq espèces, dix cellules à envoyer).
RAPPORT_V7 = {"tour2": 9.50, "tour3": 18.95, "avec_relances": 60.81}
# Seuils du plateau proposés par la note (section 5) ; ils ne valent qu'une fois gelés par Lazar.
SEUIL_RENOUVELLEMENT = 0.25
SEUIL_RENOUVELLEMENT_LIGNEE = 0.50
SEUIL_NEUVES = 0.15
# Dossiers du tableau de la réflexion d'Opus (section 1) : nombre de lignées déduit du compte de cellules (trois tours par
# espèce : 15 cellules, cinq lignées ; 12 cellules, quatre). La composition de « adjudant » n'est pas dite par la source.
DOSSIERS_CINQ = ("percée", "dérive v2", "antériorité", "mathématiques")
DOSSIERS_QUATRE = ("but", "fusionnée")
DOSSIER_NON_VERIFIE = "adjudant"
# Réflexion d'Opus, sections 1 et 3 : la seule génération finie relevée, comptée sous l'ancienne table (Argon à 10 et 50
# USD par million), et son coût réel estimé par la même source.
GENERATION_FINIE_COMPTEE = 14.81
GENERATION_FINIE_REELLE = 10.9


def charger(chemin):
    """Importe le script de la version 7 après contrôle de son empreinte ; rien n'est exécuté hors des définitions."""
    with open(chemin, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != EMPREINTE_V7:
        sys.exit(f"empreinte du script inattendue : {h} (attendue {EMPREINTE_V7}) ; rien n'est calculé")
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v7", chemin)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["collisionneur_v9_v7"] = mod
    spec.loader.exec_module(mod)
    return mod


def pire(mod, m, caracteres, plafond):
    """Pire cas d'un envoi, à la manière de `devis-reprise` : entrée projetée à RATIO_PROJECTION_ENTREE caractères par
    jeton, plus la tolérance de la garde ; plafond de sortie et provision au prix de sortie."""
    garde = mod.garde_entree(math.ceil(caracteres / mod.RATIO_PROJECTION_ENTREE))
    return mod.cout_pire_garde(m, garde, plafond)


def calculer(mod, nom, especes):
    mod.fixer_composition(especes, nom_cle_anthropic="CLE_FACTICE")
    lettres, modeles = mod.LETTRES, mod.MODELES
    n = len(lettres)
    print(f"\n=== {nom} ===")
    print("1. Pire cas de sortie d'une cellule, USD (plafond + provision, au prix de sortie)")
    sortie = relance = 0.0
    for l in lettres:
        m = modeles[l]
        s = (m["max"] + m["provision"]) / 1e6 * m["prix"][1]
        r = (m["max_relance"] + m["provision"]) / 1e6 * m["prix"][1]
        sortie, relance = sortie + s, relance + r
        print(f"   {l} {m['espece']:7s} plafond {m['max']:6d}, relance {m['max_relance']:6d}, provision "
              f"{m['provision']:6d}, prix {m['prix'][0]:g} / {m['prix'][1]:g} : {s:.3f} (relance {r:.3f})")
    print(f"   par tour : {sortie:.3f} sans relance ; relances en plus : {relance:.3f}")

    autres = {l: [x for x in lettres if x != l] for l in lettres}
    borne_critique = {l: modeles[l]["max"] * mod.CAR_SORTIE_MAX[modeles[l]["fournisseur"]] for l in lettres}
    car2 = {l: SOCLE + sum(CONCEPTION + mod.SURCOUT_BLOC for _ in autres[l]) for l in lettres}
    car3 = {l: SOCLE + CONCEPTION + mod.SURCOUT_BLOC + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l])
            for l in lettres}
    t2 = sum(pire(mod, modeles[l], car2[l], modeles[l]["max"]) for l in lettres)
    t3 = sum(pire(mod, modeles[l], car3[l], modeles[l]["max"]) for l in lettres)
    r23 = sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) + pire(mod, modeles[l], c[l], modeles[l]["max_relance"])
              for c in (car2, car3) for l in lettres)
    print(f"2. Tours III.2 et III.3, toutes cellules à envoyer, longueurs supposées (socle {SOCLE}, conception "
          f"{CONCEPTION} caractères)")
    print(f"   tour III.2 {t2:.2f} + tour III.3 {t3:.2f} = {t2 + t3:.2f} USD sans relance ; {r23:.2f} avec relances")
    if n == 5:
        print(f"   rapport de la version 7 (mathématiques) : {RAPPORT_V7['tour2']:.2f} + {RAPPORT_V7['tour3']:.2f} = "
              f"{RAPPORT_V7['tour2'] + RAPPORT_V7['tour3']:.2f} sans relance ; {RAPPORT_V7['avec_relances']:.2f} avec "
              f"relances ; écart du recalcul : {100 * ((t2 + t3) / (RAPPORT_V7['tour2'] + RAPPORT_V7['tour3']) - 1):+.1f} % "
              f"et {100 * (r23 / RAPPORT_V7['avec_relances'] - 1):+.1f} %")

    base1 = sum(pire(mod, modeles[l], SOCLE, modeles[l]["max"]) for l in lettres)
    base1_rel = sum(pire(mod, modeles[l], SOCLE, modeles[l]["max_relance"]) for l in lettres)
    print(f"3. Tour III.1 sans état (comme à la génération 1) : {base1:.2f} USD sans relance ; relances en plus : "
          f"{base1_rel:.2f}")
    etats, critiques = [], []
    for longueur in REPONSES:
        avec = sum(pire(mod, modeles[l], SOCLE + n * (longueur + mod.SURCOUT_BLOC), modeles[l]["max"]) for l in lettres)
        jetons = math.ceil((SOCLE + n * (longueur + mod.SURCOUT_BLOC)) / mod.RATIO_PROJECTION_ENTREE)
        etats.append(avec - base1)
        print(f"   état de {n} réponses de {longueur} caractères : + {avec - base1:.2f} USD d'entrée au tour III.1 "
              f"({jetons} jetons d'entrée projetés par prompt)")
    for longueur in CRITIQUES:
        plus = sum(pire(mod, modeles[l], car2[l] + longueur + mod.SURCOUT_BLOC, modeles[l]["max"])
                   - pire(mod, modeles[l], car2[l], modeles[l]["max"]) for l in lettres)
        critiques.append(plus)
        print(f"   critique précédente de {longueur} caractères rendue à son auteur : + {plus:.2f} USD d'entrée au "
              f"tour III.2")

    print("4. Total au pire d'une génération à partir de la deuxième, USD")
    suite, suite_rel = (t2 + t3, r23)
    source = "recalcul"
    if n == 5:
        suite, suite_rel = RAPPORT_V7["tour2"] + RAPPORT_V7["tour3"], RAPPORT_V7["avec_relances"]
        source = "rapport de la version 7"
    totaux = {}
    for etiquette, e, c in (("bas", etats[0], critiques[0]), ("milieu", etats[1], critiques[1]),
                            ("haut", etats[2], critiques[2])):
        sans = base1 + e + suite + c
        avec = (base1 + e) + (base1_rel + e) + suite_rel + 2 * c
        totaux[etiquette] = sans
        print(f"   longueurs {etiquette:6s} : {sans:.2f} sans relance ; {avec:.2f} si chaque cellule était relancée "
              f"(tours III.2 et III.3 : {source})")
    print(f"   rappel, sans état ni critique rendue (une génération 1) : {base1 + suite:.2f} sans relance ; "
          f"{base1 + base1_rel + suite_rel:.2f} avec relances")

    # Borne stricte avant tout envoi : rien de la génération n'est écrit ; toute conception et toute critique est bornée
    # par le plafond de sortie de son auteur (comme `devis-reprise` borne une critique non écrite) ; chaque pièce de
    # l'état est au plafond de pièce de la note (section 4.2).
    s1 = {l: SOCLE + n * (PIECE_MAX + mod.SURCOUT_BLOC) for l in lettres}
    s2 = {l: SOCLE + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l]) + PIECE_MAX + mod.SURCOUT_BLOC
          for l in lettres}
    s3 = {l: SOCLE + borne_critique[l] + mod.SURCOUT_BLOC + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l])
          for l in lettres}
    stricts = [sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) for l in lettres) for c in (s1, s2, s3)]
    strict_rel = sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) + pire(mod, modeles[l], c[l], modeles[l]["max_relance"])
                     for c in (s1, s2, s3) for l in lettres)
    plus_long = max(math.ceil(c[l] / mod.RATIO_PROJECTION_ENTREE) for c in (s1, s2, s3) for l in lettres)
    print(f"4 bis. Borne stricte avant tout envoi, SANS RELANCE, sous les hypothèses de projection du script "
          f"({mod.RATIO_PROJECTION_ENTREE:g} caractères par jeton d'entrée, caractères par jeton de sortie au plus ceux de "
          f"CAR_SORTIE_MAX : deux constantes SUPPOSÉES) ; tout texte de la génération au plafond de sortie de son auteur, "
          f"pièce d'état à {PIECE_MAX} caractères")
    print(f"   tour III.1 {stricts[0]:.2f} + tour III.2 {stricts[1]:.2f} + tour III.3 {stricts[2]:.2f} = "
          f"{sum(stricts):.2f} USD sans relance ; avec relances, la même borne monte à {strict_rel:.2f} ; plus long prompt "
          f"projeté : {plus_long} jetons d'entrée")
    return {"n": n, "bas": totaux["bas"], "haut": totaux["haut"], "etats": etats, "critiques": critiques,
            "strict": sum(stricts), "strict_relances": strict_rel}


def par_dossier(resultats):
    """4 ter : sommes par dossier et pour plusieurs dossiers ; attendu d'une génération de plus, bases dites."""
    cinq = next(r for r in resultats if r["n"] == 5)
    quatre = next(r for r in resultats if r["n"] == 4)
    print("\n4 ter. Par dossier, jusqu'au plateau, à la manière du rapport, sans relance (USD)")
    for nom, r in (("cinq espèces", cinq), ("quatre espèces", quatre)):
        print(f"   {nom} : une génération de plus {r['bas']:.2f} à {r['haut']:.2f} ; deux générations de plus "
              f"{2 * r['bas']:.2f} à {2 * r['haut']:.2f}")
    n5, n4 = len(DOSSIERS_CINQ), len(DOSSIERS_QUATRE)
    print(f"   composition dite par la source (réflexion d'Opus, section 7) : {', '.join(DOSSIERS_CINQ)} ({n5} dossiers à "
          f"cinq espèces, 15 cellules chacun) ; {', '.join(DOSSIERS_QUATRE)} ({n4} dossiers à quatre espèces, 12 cellules "
          f"chacun) ; « {DOSSIER_NON_VERIFIE} » : 15 cellules, donc cinq lignées, composition NON DITE par la source "
          f"(non vérifié)")
    for nom, k5, k4 in ((f"les {n5 + n4} dossiers dont la composition est dite", n5, n4),
                        (f"les {n5 + n4 + 1} dossiers, « {DOSSIER_NON_VERIFIE} » compté par hypothèse comme les {n5} autres "
                         f"dossiers à quinze cellules", n5 + 1, n4)):
        bas = 2 * (k5 * cinq["bas"] + k4 * quatre["bas"])
        haut = 2 * (k5 * cinq["haut"] + k4 * quatre["haut"])
        print(f"   {nom}, si tous vont à trois générations : {bas:.0f} à {haut:.0f}")
    plus_bas = cinq["etats"][0] + cinq["critiques"][0]
    plus_haut = cinq["etats"][2] + cinq["critiques"][2]
    print("   attendu d'une génération de plus à cinq espèces, estimation non mesurée, DEUX BASES QUI NE SE COMPARENT PAS :")
    print(f"   - surcoût d'entrée de l'état, au pire, sous la table de la version 7 (Argon à 4 et 20 USD par million) : "
          f"{plus_bas:.2f} à {plus_haut:.2f}")
    print(f"   - ajouté aux {GENERATION_FINIE_COMPTEE:.2f} comptés sous l'ancienne table (Argon à 10 et 50) : "
          f"{GENERATION_FINIE_COMPTEE + plus_bas:.2f} à {GENERATION_FINIE_COMPTEE + plus_haut:.2f} ; somme de deux tables, "
          f"ordre de grandeur haut seulement")
    print(f"   - ajouté aux {GENERATION_FINIE_REELLE:.1f} réels estimés par la réflexion d'Opus (prix de novembre) : "
          f"{GENERATION_FINIE_REELLE + plus_bas:.1f} à {GENERATION_FINIE_REELLE + plus_haut:.1f} ; un coût réel plus un pire "
          f"cas compté, ordre de grandeur seulement")


def seuils(n_lignees):
    print(f"\n5. Lecture des seuils en nombres d'entrées, {n_lignees} lignées (lecture APPROCHÉE : exacte seulement si "
          f"aucune entrée n'est neuve ni retirée ; voir les cas exacts plus bas)")
    for par_lignee in (3, 4, 5, 6, 8):
        total = n_lignees * par_lignee
        print(f"   {par_lignee} entrées par lignée ({total} en tout) : plateau si au plus "
              f"{math.floor(SEUIL_RENOUVELLEMENT * total + 1e-9)} entrées touchées sur le cycle, au plus "
              f"{math.floor(SEUIL_RENOUVELLEMENT_LIGNEE * par_lignee + 1e-9)} dans une même lignée, au plus "
              f"{math.floor(SEUIL_NEUVES * total + 1e-9)} entrées neuves, premier choix tenu dans "
              f"{n_lignees - 1} lignées au moins")


def cas_exacts():
    """Remarque 10 : le renouvellement a pour dénominateur tenues + modifiées + neuves + retirées ; la part d'entrées
    neuves a pour dénominateur les entrées actives à l'arrivée (tenues + modifiées + neuves)."""
    print("\n5 bis. Cas exacts, 25 entrées actives au départ, toutes lignées réunies")
    for nom, modifiees, neuves, retirees in (("six modifiées, rien d'autre", 6, 0, 0),
                                             ("sept modifiées, rien d'autre", 7, 0, 0),
                                             ("trois remplacées (trois retirées, trois neuves)", 0, 3, 3),
                                             ("quatre remplacées (quatre retirées, quatre neuves)", 0, 4, 4),
                                             ("quatre modifiées et trois neuves, aucune retirée", 4, 3, 0)):
        tenues = 25 - modifiees - retirees
        touchees = modifiees + neuves + retirees
        renouvellement = 1 - tenues / (tenues + touchees)
        part_neuves = neuves / (tenues + modifiees + neuves)
        c1 = "tient" if renouvellement <= SEUIL_RENOUVELLEMENT + 1e-9 else "tombe"
        c3 = "tient" if part_neuves <= SEUIL_NEUVES + 1e-9 else "tombe"
        print(f"   {nom} : {touchees} entrées touchées sur {tenues + touchees}, renouvellement {renouvellement:.3f} "
              f"(condition 1 {c1}) ; part d'entrées neuves {neuves}/{tenues + modifiees + neuves} = {part_neuves:.3f} "
              f"(condition 3 {c3})")


# ---------- 6. Règle d'égalité des énoncés (note, section 5.1) ----------

# Tirets et signe moins, tous ramenés au signe « - » (après la forme NFKC, il reste ceux-ci).
TIRETS = dict.fromkeys(map(ord, "\u2010\u2012\u2013\u2014\u2015\u2212"), "-")
# Ponctuation retirée (remplacée par une espace) : liste FERMÉE. N'y figurent ni les signes de comparaison, ni les
# opérateurs, ni « % », ni « / », ni « | » : ils portent un sens. Le tiret y figure : il n'est gardé que devant un nombre.
# L'astérisque et le tiret bas y figurent : ils ne sont gardés qu'entre deux lettres ou chiffres (« a*b », « H_A »).
PONCTUATION = dict.fromkeys(map(ord, ".,;:!?'\"\u2019\u2018\u02bc\u201c\u201d\u201e\u00ab\u00bb\u2039\u203a()[]{}*_`\u00b7\u2022-"),
                            " ")


def normaliser_enonce(texte):
    """Forme comparée d'un énoncé. Dans l'ordre :
    1. forme Unicode NFKC, casse repliée, forme NFKC de nouveau ;
    2. caractères de commande et de mise en forme retirés ; toute espace, saut de ligne compris, devient une espace ;
    3. barres obliques inverses retirées ;
    4. tirets et signe moins ramenés à « - » ;
    5. mis à l'abri : le point ou la virgule entre deux chiffres (séparateur décimal, écrit « , ») ; le tiret devant un
       nombre (signe, collé au nombre) ; l'astérisque et le tiret bas entre deux lettres ou chiffres ;
    6. chaque caractère de la liste fermée PONCTUATION remplacé par une espace ;
    7. caractères mis à l'abri rendus ;
    8. espaces réduites à une seule, bords retirés.
    Deux énoncés sont ÉGAUX si leurs formes comparées sont égales au caractère près. Rien d'autre n'est toléré : un mot, un
    nombre, une négation, un signe ou un sens de comparaison changé donne deux formes différentes."""
    t = unicodedata.normalize("NFKC", unicodedata.normalize("NFKC", texte).casefold())
    t = "".join(" " if c.isspace() else c for c in t if c.isspace() or unicodedata.category(c) not in ("Cc", "Cf"))
    t = t.replace("\\", "")
    t = t.translate(TIRETS)
    t = re.sub(r"(?<=\d)[.,](?=\d)", "\x00", t)
    t = re.sub(r"-\s*(?=\d)", "\x01", t)
    t = re.sub(r"(?<=[^\W_])\*(?=[^\W_])", "\x02", t)
    t = re.sub(r"(?<=[^\W_])_(?=[^\W_])", "\x03", t)
    t = t.translate(PONCTUATION)
    t = t.replace("\x00", ",").replace("\x01", "-").replace("\x02", "*").replace("\x03", "_")
    return " ".join(t.split())


def enonces_egaux(a, b):
    return normaliser_enonce(a) == normaliser_enonce(b)


def similarite_v1(a, b):
    """La règle de la version 1, pour comparaison : similarité sur des textes en forme NFKC, casse repliée, espaces
    réduites (`difflib.SequenceMatcher`, sans `autojunk`) ; « tenue » dès 0,90."""
    na, nb = (" ".join(unicodedata.normalize("NFKC", x).casefold().split()) for x in (a, b))
    return difflib.SequenceMatcher(None, na, nb, autojunk=False).ratio()


ENONCE = ("H_A : la sonde linéaire lue à la couche 12 sépare les épisodes sabotés des honnêtes mieux que la base "
          "« mots et coût » ; H_B : elle ne fait pas mieux. Mesure : aire sous la courbe sur 200 paires appariées, "
          "seuil de 0,05.")
ESSAIS_ENONCES = (
    # (nom, autre énoncé, égal attendu)
    ("le même, recopié", ENONCE, True),
    ("point final retiré, casse changée, espaces doublées",
     ENONCE[:-1].replace("Mesure", "MESURE").replace(" sur ", "  sur "), True),
    ("guillemets droits, deux-points sans espace, gras de Markdown",
     ENONCE.replace("« mots et coût »", "\"mots et coût\"").replace("H_A :", "**H_A**:").replace("H_B :", "**H_B**:"),
     True),
    ("point décimal au lieu de la virgule", ENONCE.replace("0,05", "0.05"), True),
    ("seuil changé de 0,05 à 0,01 (essai du contre-lecteur)", ENONCE.replace("0,05", "0,01"), False),
    ("« ne fait pas mieux » devenu « fait mieux » (essai du contre-lecteur)",
     ENONCE.replace("elle ne fait pas mieux", "elle fait mieux"), False),
    ("200 paires devenues 20 (essai du contre-lecteur)", ENONCE.replace("200 paires", "20 paires"), False),
    ("virgule décimale retirée : 0,05 devenu 005", ENONCE.replace("0,05", "005"), False),
    ("couche 12 devenue couche 1,2", ENONCE.replace("couche 12", "couche 1,2"), False),
    ("« mieux que » devenu « moins bien que »", ENONCE.replace("mieux que la base", "moins bien que la base"), False),
)
ESSAIS_SIGNES = (
    ("signe retiré : \u22120,5 et 0,5", "écart de \u22120,5 au plus", "écart de 0,5 au plus", False),
    ("signe moins typographique et tiret : \u22120,5 et -0,5", "écart de \u22120,5 au plus", "écart de -0,5 au plus", True),
    ("sens de la comparaison : p < 0,05 et p > 0,05", "rejet si p < 0,05", "rejet si p > 0,05", False),
    ("inégalité large ou stricte : ≥ 0,8 et > 0,8", "aire ≥ 0,8", "aire > 0,8", False),
    ("pourcentage retiré : 5 % et 5", "au plus 5 % de fausses alertes", "au plus 5 de fausses alertes", False),
    ("apostrophe typographique ou droite, espace insécable", "l\u2019aire sous la courbe\u00a0: 0,8",
     "l'aire sous la courbe : 0,8", True),
    ("trait d'union retiré : non-nul et non nul", "effet non-nul", "effet non nul", True),
    ("négation retirée : sans contrôle et avec contrôle", "sans contrôle négatif", "avec contrôle négatif", False),
    ("gras de Markdown autour d'un mot", "seuil **strict** de 0,05", "seuil strict de 0,05", True),
    ("tiret bas protégé par une barre oblique inverse", "H\\_A contre H\\_B", "H_A contre H_B", True),
    ("produit retiré : a*b et a b", "gain a*b", "gain a b", False),
    ("indice changé : H_A et H_B", "on garde H_A", "on garde H_B", False),
    ("même nombre écrit autrement : 1 000 et 1000 (la règle penche vers le mouvement)", "sur 1 000 paires",
     "sur 1000 paires", False),
    ("espace devant le signe % : 5 % et 5% (la règle penche vers le mouvement)", "au plus 5 % d'alertes",
     "au plus 5% d'alertes", False),
)


def egalite_des_enonces():
    print("\n6. Règle d'égalité des énoncés du registre (remplace la similarité à 0,90 de la version 1)")
    mots = sum(1 for x in ENONCE.split() if any(c.isalnum() for c in x))
    print(f"   énoncé de départ ({mots} mots) : {ENONCE}")
    print(f"   forme comparée : {normaliser_enonce(ENONCE)}")
    echecs = 0
    for nom, autre, attendu in ESSAIS_ENONCES:
        egal = enonces_egaux(ENONCE, autre)
        echecs += egal != attendu
        print(f"   {nom} : {'ÉGAL' if egal else 'DIFFÉRENT'} (attendu {'égal' if attendu else 'différent'}) ; similarité de "
              f"la version 1 : {similarite_v1(ENONCE, autre):.3f}")
    for nom, a, b, attendu in ESSAIS_SIGNES:
        egal = enonces_egaux(a, b)
        echecs += egal != attendu
        print(f"   {nom} : {'ÉGAL' if egal else 'DIFFÉRENT'} (attendu {'égal' if attendu else 'différent'}) ; similarité de "
              f"la version 1 : {similarite_v1(a, b):.3f}")
    print(f"   {len(ESSAIS_ENONCES) + len(ESSAIS_SIGNES)} essais ; contraires à l'attendu : {echecs}")
    return echecs


# ---------- 7. Ordre de présentation (note, section 3.3, point 3) ----------

def rang_parmi_les_autres(i, j, g, n):
    """Rang (de 1 à n − 1) de la pièce de la proposition j parmi les pièces des AUTRES que lit la proposition i, à la
    génération g (g ≥ 2), pour n propositions rangées dans l'ordre des lettres (i et j comptés de 0 à n − 1, j ≠ i). La
    pièce de la proposition i elle-même est toujours servie avant, hors de ce rang."""
    d = (j - i) % n
    s = (g - 2) % (n - 1)
    return ((d - 1 - s) % (n - 1)) + 1


def ordre_de_presentation():
    print("\n7. Ordre de présentation : rang = ((d − 1 − s) modulo (N − 1)) + 1, avec d = (j − i) modulo N et "
          "s = (g − 2) modulo (N − 1)")
    echecs = 0
    for n in range(2, 8):
        attendu = set(range(1, n))
        for g in range(2, n + 3):
            for i in range(n):  # chaque lecteur voit chaque autre pièce à un rang différent
                echecs += {rang_parmi_les_autres(i, j, g, n) for j in range(n) if j != i} != attendu
            for j in range(n):  # chaque pièce occupe chaque rang une fois parmi ses lecteurs
                echecs += {rang_parmi_les_autres(i, j, g, n) for i in range(n) if i != j} != attendu
        for i in range(n):      # sur N − 1 générations de suite, un lecteur voit une même pièce à chaque rang une fois
            for j in range(n):
                if i != j:
                    echecs += {rang_parmi_les_autres(i, j, g, n) for g in range(2, n + 1)} != attendu
    print(f"   contrôle pour N de 2 à 7 et les générations 2 à N + 2 : chaque lecteur voit chaque autre pièce à un rang "
          f"différent ; chaque pièce occupe chaque rang une fois parmi ses lecteurs ; sur N − 1 générations de suite, un "
          f"même lecteur voit une même pièce à chaque rang une fois ; écarts : {echecs}")
    lettres = "ABCDE"
    for g in (2, 3, 4):
        lignes = []
        for i, l in enumerate(lettres):
            autres = sorted((x for x in range(5) if x != i), key=lambda j: rang_parmi_les_autres(i, j, g, 5))
            lignes.append(f"{l} lit {l} puis {' '.join(lettres[j] for j in autres)}")
        print(f"   cinq propositions, génération {g} : " + " ; ".join(lignes))
    print(f"   deux propositions : rang {rang_parmi_les_autres(0, 1, 2, 2)} à la génération 2, "
          f"{rang_parmi_les_autres(0, 1, 3, 2)} à la génération 3 (décalage nul)")
    return echecs


# ---------- 8. Plafond de pièce et texte au plafond de sortie (note, section 4.2) ----------

def plafond_de_piece(mod):
    print(f"\n8. Plafond de pièce ({PIECE_MAX} caractères) contre le texte qu'une espèce peut rendre à son plafond")
    borne = TEXTE_CARBON_RELEVE * mod.CAR_SORTIE_MAX["gemini"]
    print(f"   origine de la borne : plus long texte de Carbon relevé, {TEXTE_CARBON_RELEVE} (unité non dite dans la "
          f"source, lue comme des jetons) × {mod.CAR_SORTIE_MAX['gemini']:g} caractères par jeton = {borne:g} caractères")
    for espece in ("fable", "opus", "argon", "astra", "carbon"):
        m = mod.CATALOGUE[espece]
        jetons = m["max"] - m["provision"]
        car = jetons * mod.CAR_SORTIE_MAX[m["fournisseur"]]
        print(f"   {espece:7s} : plafond {m['max']} − provision {m['provision']} = {jetons} jetons de texte, soit "
              f"{car:g} caractères à {mod.CAR_SORTIE_MAX[m['fournisseur']]:g} par jeton : "
              f"{'au-delà du' if car > PIECE_MAX else 'sous le'} plafond de pièce")
    print(f"   3 500 mots à 7 caractères : 24 500 caractères ; le plafond de pièce vaut {PIECE_MAX / 24500:.2f} fois cette "
          f"longueur")


# ---------- Marqueur de fin et bloc de registre (communs aux sections 9 et 10) ----------

MARQUEUR_FIN = "FIN-DE-CELLULE"  # la constante MARQUEUR du script, contrôlée au lancement
DEBUT_REGISTRE, FIN_REGISTRE = "DEBUT-REGISTRE", "FIN-REGISTRE"


def bornes_du_registre(lignes):
    """Indices des deux lignes de bornes du bloc de registre, s'il y en a un seul et bien formé ; sinon None."""
    debuts = [k for k, l in enumerate(lignes) if l.strip() == DEBUT_REGISTRE]
    fins = [k for k, l in enumerate(lignes) if l.strip() == FIN_REGISTRE]
    if len(debuts) == 1 and len(fins) == 1 and debuts[0] < fins[0]:
        return debuts[0], fins[0]
    return None


def sans_registre(texte):
    """Retire le bloc de registre, lignes de bornes comprises, s'il y en a un seul et bien formé ; sinon rend le texte."""
    lignes = texte.split("\n")
    bornes = bornes_du_registre(lignes)
    return texte if bornes is None else "\n".join(lignes[:bornes[0]] + lignes[bornes[1] + 1:])


# ---------- 9. Garde d'identité : liste fermée des motifs (note, section 3.3, point 2) ----------

SANS_CASSE = re.IGNORECASE
# Désignations de modèle ou de fournisseur du catalogue, sans ambiguïté, cherchées partout dans la pièce, sans casse.
DESIGNATIONS = tuple((nom, re.compile(m, SANS_CASSE)) for nom, m in (
    ("famille Claude", r"\bclaude(?:[ -](?:fable|opus|sonnet|haiku)\b|[ -]?\d|-[a-z0-9])"),
    ("Fable ou Opus suivi d'un numéro", r"\b(?:fable|opus)[ -]\d"),
    ("famille Gemini", r"\bgemini(?:[ -](?:argon|carbon|neon|pro|flash|ultra|nano)\b|[ -]?\d|-[a-z0-9])"),
    ("famille GPT", r"\bgpt(?:[ -]?\d|-[a-z0-9])|\bchatgpt\b"),
    ("famille Kimi", r"\bkimi(?:[ -]k?\d|-[a-z0-9])"),
    ("fournisseurs", r"\b(?:anthropic|openai|deepmind|moonshot ai)\b"),
))
# Noms nus : ils ne comptent qu'après une formule d'auto-désignation, dans la même phrase, ou sur une ligne de bord courte.
NOMS_NUS = re.compile(r"\b(?:claude|gemini|gpt|chatgpt|kimi|anthropic|openai|google|deepmind|moonshot)\b", SANS_CASSE)
NOMS_NUS_CASSE_EXACTE = re.compile(r"\b(?:Fable|Opus|Argon|Carbon|Neon|Astra)\b")  # mots ordinaires en minuscules
# Formules d'auto-désignation, toutes à la première personne, sans casse.
FORMULES = tuple(re.compile(m, SANS_CASSE) for m in (
    r"\bje suis\b",
    r"\ben tant qu(?:e\b|['\u2019])",
    r"\bj['\u2019]ai été (?:développée?|entraînée?|conçue?|créée?)\b",
    r"\b(?:mon|ma|mes) (?:fournisseur|concepteurs?|créateurs?|développeurs?|éditeur|entreprise)\b",
    r"\bi am\b|\bi['\u2019]m\b",
    r"\bas an? (?:ai|llm|assistant|language model|large language model)\b",
    r"\b(?:as|moi,?) (?=(?:claude|gemini|chatgpt|gpt|kimi)\b)",
))
FENETRE = 80  # caractères lus après la formule, sans passer la fin de la phrase
FIN_DE_PHRASE = re.compile(r"[.!?](?:\s|$)|\n")
# Signature : une ligne de bord courte (première ou dernière ligne non vide de la pièce, ligne du marqueur de fin et bloc
# de registre mis à part) qui contient un nom du catalogue.
LIGNE_DE_BORD_COURTE = 60  # caractères, bords retirés


def lignes_de_bord(piece):
    """Première et dernière lignes non vides de la pièce, hors la ligne du marqueur de fin et hors le bloc de registre :
    liste de (position du premier caractère de la ligne, ligne)."""
    lignes = piece.split("\n")
    bornes = bornes_du_registre(lignes)
    position, pleines = 0, []
    for k, l in enumerate(lignes):
        dans_le_registre = bornes is not None and bornes[0] <= k <= bornes[1]
        if l.strip() and l.strip() != MARQUEUR_FIN and not dans_le_registre:
            pleines.append((position, l))
        position += len(l) + 1
    return pleines[:1] + pleines[-1:] if len(pleines) > 1 else pleines


def garde_identite(piece, faits_et_question):
    """Renvoie (refus, signalements) : deux listes de (catégorie, position du premier caractère), jamais le texte trouvé.
    Refus : auto-désignation, c'est-à-dire une formule à la première personne suivie d'un nom du catalogue dans la même
    phrase, ou une signature (ligne de bord courte qui contient un nom du catalogue). Signalement, qui ne bloque rien :
    désignation du catalogue absente des faits et de la question, hors des passages déjà refusés."""
    refus, pris = [], []
    motifs = (NOMS_NUS, NOMS_NUS_CASSE_EXACTE, *(m for _, m in DESIGNATIONS))
    for formule in FORMULES:
        for f in formule.finditer(piece):
            suite = piece[f.end():f.end() + FENETRE]
            fin = FIN_DE_PHRASE.search(suite)
            suite = suite[:fin.start()] if fin else suite
            if any(m.search(suite) for m in motifs):
                refus.append(("auto-désignation", f.start()))
                pris.append((f.start(), f.end() + len(suite)))
    for position, ligne in lignes_de_bord(piece):
        if len(ligne.strip()) <= LIGNE_DE_BORD_COURTE and any(m.search(ligne) for m in motifs):
            refus.append(("auto-désignation (signature)", position))
            pris.append((position, position + len(ligne)))
    reference = faits_et_question.casefold()
    signalements = []
    for _, motif in DESIGNATIONS:
        for m in motif.finditer(piece):
            if any(a <= m.start() < b for a, b in pris):
                continue
            if m.group(0).casefold() not in reference:
                signalements.append(("désignation hors des faits et de la question", m.start()))
    return sorted(set(refus), key=lambda x: x[1]), sorted(set(signalements), key=lambda x: x[1])


FAITS_TEMOIN = "FAITS. La sonde est apprise sur un modèle ouvert de huit milliards de paramètres. QUESTION. Que mesurer ?"
PIECE_OBJETS = ("Le moniteur de confiance pourrait être GPT-4o, et l'agent non fiable Claude 3.5 Sonnet, pris comme objets "
                "d'étude.")
TEMOINS_IDENTITE = (
    # (nom, pièce, nombre de refus attendu, nombre de signalements attendu)
    ("sain : « fable », « opus », « argon », « carbone » en mots ordinaires, un prénom, un modèle hors catalogue comme objet",
     "Cette hypothèse reste une fable tant qu'aucun contrôle négatif ne la borne ; l'opus cité est une référence à "
     "vérifier. La sonde lit un modèle ouvert, Llama 3.1 8B, pris comme objet d'étude. Claude Shannon a posé la mesure "
     "de l'information. Le carbone et l'argon n'ont rien à voir ici. Je suis d'accord avec la critique sur ce point.\n"
     "FIN-DE-CELLULE\n", 0, 0),
    ("sain : « je suis » suivi de « fable » en minuscules", "Je suis la fable du corbeau jusqu'au bout.", 0, 0),
    ("sain : les formules, sans aucun nom du catalogue",
     "Je suis prudent. En tant que proposition, je maintiens ce point. J'ai été conçu pour répondre à la question. "
     "Mon fournisseur n'est pas un fait du dossier. I am not sure. As an assistant, I stay careful. Moi, je maintiens.",
     0, 0),
    ("sain, signalé : deux modèles du catalogue nommés comme objets d'étude, absents des faits", PIECE_OBJETS, 0, 2),
    ("sain, signalé : une liste de modèles au milieu du texte n'est pas une signature",
     "Lecteurs possibles :\n- Claude Opus 5.5\n- GPT-6.2\nLa suite discute ce choix.\nFIN-DE-CELLULE\n", 0, 3),
    ("sain, signalé : une ligne de bord longue qui nomme un modèle comme objet",
     "La mesure tient.\nClaude Opus 5.5 pourrait servir de lecteur hors des familles des moniteurs.\n", 0, 2),
    ("faux positif connu, refusé, à admettre par l'arbitre : « en tant que » suivi d'un rôle, puis un modèle nommé comme objet",
     "La mesure tient, et le choix du lecteur compte.\nEn tant que lecteur, Claude Opus 5.5 serait hors des familles des "
     "moniteurs, ce qui reste à établir par une mesure.\nLa suite discute ce choix sans le trancher ici.\n", 1, 0),
    ("faux positif connu, refusé, à admettre par l'arbitre : dernière ligne courte qui nomme un modèle comme objet",
     "La synthèse tient en une page et ne tranche pas le reste.\nÀ faire d'abord : sonder GPT-4o.\nFIN-DE-CELLULE\n", 1, 0),
    ("positif : « je suis » et un nom nu", "Je suis Claude, et je réponds à la question posée par l'arbitre.", 1, 0),
    ("positif : « je suis » et un surnom à la casse exacte", "Je suis Fable, et je réponds à la question posée par l'arbitre.",
     1, 0),
    ("positif : « je suis », le fournisseur après une virgule",
     "Je suis un grand modèle de langage, entraîné par Google, et je réponds à la question.", 1, 0),
    ("positif : « en tant que » et un fournisseur",
     "En tant que modèle de langage entraîné par Google, je ne peux pas l'affirmer.", 1, 0),
    ("positif : « en tant qu' » avec apostrophe typographique",
     "En tant qu\u2019IA conçue par Anthropic, je m'abstiens de trancher ce point de méthode.", 1, 0),
    ("positif : « j'ai été entraîné par »", "J'ai été entraîné par Anthropic ; cela ne change rien à la méthode.", 1, 0),
    ("positif : « mon fournisseur »", "Mon fournisseur, Moonshot, ne publie pas ce chiffre dans sa documentation.", 1, 0),
    ("positif : formule en anglais", "As an AI developed by OpenAI, I cannot verify this claim from the given facts.", 1, 0),
    ("positif : « I am »", "I am Kimi, and I cannot say more than the facts allow on this point.", 1, 0),
    ("positif : « I'm »", "I'm Gemini 4, so I cannot say more than the facts allow on this point.", 1, 0),
    ("positif : « as » suivi aussitôt du nom", "As Claude, I should note the limits of this design before going on.", 1, 0),
    ("positif : « moi » suivi aussitôt du nom", "Moi, Gemini, je maintiens ce point contre les trois critiques reçues.", 1, 0),
    ("positif : signature en dernière ligne, avant le marqueur de fin",
     "La mesure tient, et la synthèse ne dit rien de plus que les faits.\n\u2014 Claude Fable 5.2\nFIN-DE-CELLULE\n", 1, 0),
    ("positif : identifiant seul en dernière ligne, avant le registre et le marqueur",
     "Fin de la réponse, sans autre remarque de méthode à ce stade.\ngemini-4-carbon\nDEBUT-REGISTRE\n"
     "1 | A-01 | NEUVE | propre | énoncé factice\nFIN-REGISTRE\nFIN-DE-CELLULE\n", 1, 0),
    ("positif : désignation en première ligne, en titre",
     "# Claude Opus 5.5\n\nLa mesure tient, et la synthèse ne dit rien de plus que les faits du dossier.\n", 1, 0),
    ("positif : nom nu en gras en dernière ligne",
     "La mesure tient, et la synthèse ne dit rien de plus que les faits du dossier.\n**Gemini**\n", 1, 0),
    ("positif : surnom à la casse exacte en dernière ligne",
     "La mesure tient, et la synthèse ne dit rien de plus que les faits du dossier.\nSigné : Astra\n", 1, 0),
    ("positif : dernière ligne courte qui dit l'auteur",
     "La mesure tient, et la synthèse ne dit rien de plus que les faits du dossier.\nRéponse rédigée par Gemini.\n", 1, 0),
)
# Pour chaque motif de désignation, dans l'ordre de DESIGNATIONS : des témoins positifs, puis des témoins sains.
TEMOINS_DESIGNATIONS = (
    (("Claude Haiku", "claude-opus-5-5", "Claude 3.5", "Claude Fable 5.2"), ("Claude Shannon", "Jean-Claude", "Claude")),
    (("Fable 5.2", "opus-5-5", "Opus 5"), ("une fable", "l'opus cité", "opus magnum")),
    (("Gemini 4 Carbon", "gemini-4-argon", "Gemini Pro"), ("le programme Gemini", "Gemini")),
    (("GPT-6.2", "gpt-6.2-astra", "GPT 4", "ChatGPT"), ("un modèle de type GPT", "un script")),
    (("Kimi K3.1", "kimi-k3.1-pro"), ("Kimi", "un kimono")),
    (("Anthropic", "OpenAI", "DeepMind", "Moonshot AI"), ("le principe anthropique", "Moonshot", "Google")),
)


def identite():
    print("\n9. Garde d'identité : liste fermée des motifs, témoins (refus et signalements par catégorie et position)")
    echecs = 0
    for (nom, motif), (positifs, sains) in zip(DESIGNATIONS, TEMOINS_DESIGNATIONS):
        manques = [x for x in positifs if not motif.search(x)]
        faux = [x for x in sains if any(m.search(x) for _, m in DESIGNATIONS)]
        echecs += len(manques) + len(faux)
        print(f"   désignation « {nom} » : {len(positifs)} témoins positifs, {len(manques)} manqué(s) ; {len(sains)} témoins "
              f"sains, {len(faux)} pris à tort par un motif de désignation")
    for nom, piece, n_refus, n_signalements in TEMOINS_IDENTITE:
        refus, signalements = garde_identite(piece, FAITS_TEMOIN)
        bon = len(refus) == n_refus and len(signalements) == n_signalements
        echecs += not bon
        print(f"   {nom} : {len(refus)} refus {[p for _, p in refus]}, {len(signalements)} signalement(s) "
              f"{[p for _, p in signalements]} ; attendu {n_refus} et {n_signalements} : {'conforme' if bon else 'ÉCART'}")
    refus, signalements = garde_identite(PIECE_OBJETS, FAITS_TEMOIN + " Le moniteur est GPT-4o ; l'agent est Claude 3.5 "
                                                                      "Sonnet.")
    bon = not refus and not signalements
    echecs += not bon
    print(f"   les deux mêmes objets d'étude, cette fois nommés par les faits : {len(refus)} refus, {len(signalements)} "
          f"signalement ; attendu 0 et 0 : {'conforme' if bon else 'ÉCART'}")
    sortes = (("sain :", "saines sans refus ni signalement"), ("sain, signalé :", "saines avec signalements"),
              ("faux positif connu", "faux positifs connus"), ("positif :", "positives"))
    comptes = ", ".join(f"{sum(1 for t in TEMOINS_IDENTITE if t[0].startswith(prefixe))} {nom}" for prefixe, nom in sortes)
    print(f"   pièces témoins : {len(TEMOINS_IDENTITE)}, soit {comptes} ; mots témoins des désignations : "
          f"{sum(len(p) for p, _ in TEMOINS_DESIGNATIONS)} positifs, {sum(len(x) for _, x in TEMOINS_DESIGNATIONS)} sains")
    print(f"   témoins contraires à l'attendu : {echecs}")
    return echecs


# ---------- 10. Recopie : suites de trois mots, temps linéaire (note, section 5.4) ----------

SEUIL_RECOPIE = 0.90


def suites_de_trois_mots(texte):
    mots = normaliser_enonce(texte).split(" ")
    return {tuple(mots[k:k + 3]) for k in range(len(mots) - 2)}


def similarite_de_recopie(a, b):
    """Similarité de Jaccard entre les ensembles de suites de trois mots de deux textes, registres retirés."""
    sa, sb = suites_de_trois_mots(sans_registre(a)), suites_de_trois_mots(sans_registre(b))
    return len(sa & sb) / len(sa | sb) if sa | sb else 1.0


def texte_fabrique(n_mots):
    """Texte fabriqué sans tirage : suite arithmétique sur un vocabulaire de 5 003 mots factices de six lettres."""
    return " ".join(f"m{(k * 7919 + (k // 13) * 104729 + k * k) % 5003:05d}" for k in range(n_mots))


def recopie():
    print(f"\n10. Recopie : similarité de Jaccard sur les suites de trois mots, registres retirés ; « recopie » dès "
          f"{SEUIL_RECOPIE:.2f}")
    base = texte_fabrique(9285)
    print(f"   texte fabriqué : {len(base.split())} mots, {len(base)} caractères (juste sous le plafond de pièce)")
    registre = "\n".join([DEBUT_REGISTRE] + [f"{k} | A-{k:02d} | TENUE | propre | énoncé factice numéro {k}"
                                             for k in range(1, 9)] + [FIN_REGISTRE])
    copie = similarite_de_recopie(base, base + "\n" + registre)
    print(f"   copie exacte, un registre de huit lignes ajouté à la copie : {copie:.3f}")
    echecs = int(copie != 1.0)
    for pas in (200, 100, 67, 60, 50, 33, 20):
        mots = base.split()
        change = [f"x{k:05d}" if k % pas == pas // 2 else m for k, m in enumerate(mots)]
        part = sum(1 for a, b in zip(mots, change) if a != b) / len(mots)
        s = similarite_de_recopie(base, " ".join(change))
        attendu = (1 - 3 * part) / (1 + 3 * part)
        echecs += abs(s - attendu) > 0.01
        print(f"   un mot changé sur {pas} ({100 * part:.2f} % des mots) : {s:.3f} "
              f"({'recopie' if s >= SEUIL_RECOPIE else 'pas une recopie'}) ; attendu par le calcul (1 − 3p)/(1 + 3p) : "
              f"{attendu:.3f}")
    print(f"   écarts de plus de 0,01 à l'attendu : {echecs}")
    return echecs


def table_des_corrections():
    """La table « remarque → correction » de l'en-tête de ce fichier, telle quelle."""
    lignes = __doc__.split("\n")
    debut = next(k for k, l in enumerate(lignes) if l.startswith("Table « remarque → correction »"))
    fin = next(k for k, l in enumerate(lignes) if l.startswith("Fin de la table"))
    return "\n".join(lignes[debut:fin])


def principal(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    mod = charger(argv[1])
    if mod.MARQUEUR != MARQUEUR_FIN:
        sys.exit(f"marqueur de fin inattendu dans le script : {mod.MARQUEUR!r} ; rien n'est calculé")
    print("Annexe de calcul et d'essais, version 2, de conception-generations-jusqu-au-plateau-v2.md")
    print(table_des_corrections())
    print()
    print(f"Script chargé : {mod.VERSION}, sha256 {EMPREINTE_V7}")
    print(f"Constantes lues dans le script : {mod.RATIO_PROJECTION_ENTREE:g} caractères par jeton d'entrée projeté, "
          f"tolérance de la garde {mod.TOLERANCE_COMPTE}, caractères par jeton de sortie au plus {mod.CAR_SORTIE_MAX}, "
          f"{mod.SURCOUT_BLOC} caractères de balises par pièce")
    resultats = [calculer(mod, nom, especes) for nom, especes in COMPOSITIONS]
    par_dossier(resultats)
    for n in sorted({r["n"] for r in resultats}, reverse=True):
        seuils(n)
    cas_exacts()
    echecs = egalite_des_enonces() + ordre_de_presentation()
    plafond_de_piece(mod)
    echecs += identite() + recopie()
    print(f"\nContrôles des sections 6, 7, 9 et 10 contraires à l'attendu : {echecs}")
    if echecs:
        sys.exit(2)


if __name__ == "__main__":
    principal(sys.argv)

#!/usr/bin/env python3
"""Calculs de l'avis v2 sur le modèle de l'expérimentateur d'épreuve (nœud N4).

Aucun tirage, aucune graine : produits, sommes et bornes exactes ; bibliothèque standard seule.
Chaque fichier lu est d'abord comparé à son empreinte attendue ; une empreinte différente arrête le programme
(aucun repli). Blocs :
  [0] auto-essai des deux gardes du programme, sur un cas sain et sur un artefact ;
  [A] table de coût de l'avis v1, refaite ;
  [B] tables de coût de Carbon et d'Astra, refaites ;
  [C] bornes de l'erratum 1 de la note de conception, pour douze témoins et pour cent six greffons ;
  [D] borne binomiale exacte citée par Astra, et ce qu'il faudrait de témoins pour des bornes plus basses ;
  [E] garde 9 : les lignes 692 à 695 du fichier empreinté, exécutées sur des cas sains et des artefacts ;
  [F] divisions de contrôle sur le relevé du lecteur témoin et sur la sortie du lot d'Astra.

Emploi (depuis la racine du dépôt) :
  python3 calculs-avis-trois-voix-v2.py [--enonce CHEMIN_DE_L_ENONCE_NEUTRE]
L'énoncé neutre n'est pas sur la branche de travail : sans lui, le contrôle de taille du bloc [F] est dit « non fait ».
"""
import argparse
import hashlib
import json
import math
import sys
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction

TOUR_FERME = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/tour_ferme_v64.py"
EMPREINTE_TOUR_FERME = "35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da"
SORTIE_ASTRA = "docs/notes/experimentateurs-et-tests-de-mort-v1/avis-n4-astra-v1/astra62-n4-lot-output_file_id.jsonl"
EMPREINTE_SORTIE_ASTRA = "e679f72835fd7926a4a1dc959a5a07e2283d15ef697ebd443ce58013f00ae073"
EMPREINTE_ENONCE = "cf566995ee4c06cfa06d2c8ab5326ac4750d66617d81c21f2be51ca07f40e2ba"

# Prix par million de jetons (entrée, sortie), tels que l'énoncé neutre les donne (cf566995…, l. 28 à 33).
# Rapportés : aucune source de prix n'a été vérifiée pour cet avis.
PRIX = {
    "Sonnet 5.5": (2, 10),
    "Opus 5.5": (4, 20),
    "Carbon": (4, 20),
    "Fable 5.2": (8, 40),
    "Astra, Argon": (10, 50),
}

EGAL = "égal à l'arrondi"
DIFFERENT = "DIFFÉRENT"


class EmpreinteDifferente(Exception):
    """Le fichier lu n'a pas l'empreinte attendue."""


def lire_empreinte(chemin, attendue):
    """Rend les octets du fichier ; lève `EmpreinteDifferente` si l'empreinte n'est pas celle attendue."""
    with open(chemin, "rb") as f:
        octets = f.read()
    calculee = hashlib.sha256(octets).hexdigest()
    if calculee != attendue:
        raise EmpreinteDifferente(f"empreinte de {chemin} = {calculee}, attendue {attendue}")
    return octets


def usd(x, decimales=2):
    """Écrit une fraction exacte, arrondie au plus proche (demi vers le haut), avec la virgule décimale."""
    q = Decimal(1).scaleb(-decimales)
    d = (Decimal(x.numerator) / Decimal(x.denominator)).quantize(q, rounding=ROUND_HALF_UP)
    return str(d).replace(".", ",")


def cout(prix, jetons_entree, jetons_sortie):
    """Coût exact, en dollars, d'un appel : prix par million de jetons."""
    return Fraction(prix[0] * jetons_entree + prix[1] * jetons_sortie, 1_000_000)


def arrondi_egal(x, imprime):
    """Vrai si la fraction x, arrondie au nombre de décimales de la valeur imprimée, lui est égale."""
    decimales = len(imprime.split(",")[1]) if "," in imprime else 0
    return usd(x, decimales) == imprime


def bloc_0():
    print("[0] Auto-essai des deux gardes du programme (cas sain, puis artefact)")
    sain = arrondi_egal(Fraction(4452, 1000), "4,5")
    artefact = arrondi_egal(Fraction(4452, 1000), "4,6")
    print(f"    comparaison à l'arrondi : 4,452 contre « 4,5 » : {'égal' if sain else 'différent'} (attendu : égal) ;"
          f" 4,452 contre « 4,6 » : {'égal' if artefact else 'différent'} (attendu : différent)")
    lire_empreinte(TOUR_FERME, EMPREINTE_TOUR_FERME)
    try:
        lire_empreinte(TOUR_FERME, "0" * 64)
        arret = False
    except EmpreinteDifferente:
        arret = True
    print(f"    empreinte : fichier à l'empreinte attendue : lu ; même fichier, empreinte attendue fausse :"
          f" {'arrêt' if arret else 'lu'} (attendu : arrêt)")
    if not (sain and not artefact and arret):
        sys.exit("ARRÊT : une garde du programme ne se comporte pas comme attendu")
    print("    bilan du bloc [0] : les deux gardes distinguent le cas sain de l'artefact")
    print()


def bloc_a():
    print("[A] Table de coût de l'avis v1 (18a3883d…, l. 36 à 44), refaite")
    print("    scénarios de la v1 (« supposés ») : court = 6 000 jetons d'entrée et 3 000 de sortie ;")
    print("    long = 150 000 d'entrée et 40 000 de sortie ; par greffon, pour 12 témoins, pour 106 greffons")
    imprimes = {  # valeurs imprimées par la v1 : (par greffon, 12 témoins, 106 greffons), court puis long
        "Sonnet 5.5": (("0,04", "0,5", "4,5"), ("0,70", "8,4", "74")),
        "Opus 5.5": (("0,08", "1,0", "8,9"), ("1,40", "16,8", "148")),
        "Carbon": (("0,08", "1,0", "8,9"), ("1,40", "16,8", "148")),
        "Fable 5.2": (("0,17", "2,0", "17,8"), ("2,80", "33,6", "297")),
        "Astra, Argon": (("0,21", "2,5", "22"), ("3,50", "42", "371")),
    }
    tout_egal = True
    for nom, prix in PRIX.items():
        for etiquette, (entree, sortie), imp in (("court", (6_000, 3_000), imprimes[nom][0]),
                                                 ("long", (150_000, 40_000), imprimes[nom][1])):
            c = cout(prix, entree, sortie)
            egal = all(arrondi_egal(v, i) for v, i in zip((c, 12 * c, 106 * c), imp))
            tout_egal = tout_egal and egal
            print(f"    {nom:13s} {etiquette:5s} : {usd(c, 3)} ; x12 = {usd(12 * c, 3)} ; x106 = {usd(106 * c, 3)}"
                  f" | imprimé {imp[0]} ; {imp[1]} ; {imp[2]} | {EGAL if egal else DIFFERENT}")
    bas, haut = Fraction(61, 1000), Fraction(10, 100)
    egal = arrondi_egal(106 * bas, "6,5") and arrondi_egal(106 * haut, "10,6")
    tout_egal = tout_egal and egal
    print(f"    lecteur témoin, 106 greffons : {usd(106 * bas, 3)} à {usd(106 * haut, 3)} | imprimé 6,5 à 10,6 |"
          f" {EGAL if egal else DIFFERENT}")
    print(f"    lecteur témoin, 12 témoins : {usd(12 * bas, 3)} à {usd(12 * haut, 3)}")
    bilan = "toutes les valeurs imprimées par la v1 sont égales à l'arrondi" if tout_egal else "AU MOINS UNE VALEUR DIFFÈRE"
    print(f"    bilan du bloc [A] : {bilan}")
    print()


def bloc_b():
    print("[B] Tables de coût de Carbon (c3132009…, l. 9 à 28) et d'Astra (e679f728…, table), refaites")
    print("    scénario commun aux deux : 5 000 ou 200 000 jetons par implémentation, 80 % en entrée, 20 % en sortie,")
    print("    pour 100 implémentations ; Carbon ajoute « jusqu'à + 65 % »")
    astra = {"Opus 5.5": ("3,60", "144"), "Fable 5.2": ("7,20", "288"), "Sonnet 5.5": ("1,80", "72"),
             "Carbon": ("3,60", "144"), "Astra, Argon": ("9", "360")}
    carbon = {"Opus 5.5": ("4", "150", "240"), "Fable 5.2": ("7", "290", "480"), "Sonnet 5.5": ("2", "75", "120"),
              "Carbon": ("4", "150", "240"), "Astra, Argon": ("9", "360", "600")}
    tout_egal = True
    for nom, prix in PRIX.items():
        bas = 100 * cout(prix, 4_000, 1_000)
        haut = 100 * cout(prix, 160_000, 40_000)
        plus = haut * Fraction(165, 100)
        egal = arrondi_egal(bas, astra[nom][0]) and arrondi_egal(haut, astra[nom][1])
        tout_egal = tout_egal and egal
        print(f"    {nom:13s} : {usd(bas)} à {usd(haut)} ; + 65 % : {usd(plus)}"
              f" | Astra imprime {astra[nom][0]} à {astra[nom][1]} : {'égal' if egal else DIFFERENT}"
              f" | Carbon imprime environ {carbon[nom][0]} à {carbon[nom][1]}, jusqu'à {carbon[nom][2]}")
    bilan = "la table d'Astra est exacte sous ses hypothèses" if tout_egal else "LA TABLE D'ASTRA DIFFÈRE"
    print(f"    bilan du bloc [B] : {bilan} ; celle de Carbon est la même, arrondie par lui")
    print()


def bloc_c():
    print("[C] Bornes de l'erratum 1 (0198f5f8…, § 2, point (a)) : de 0,14 à 4,10 USD par greffon, lecteur témoin compris")
    bas, haut = Fraction(81, 1000) + Fraction(61, 1000), Fraction(4) + Fraction(10, 100)
    print(f"    0,081 + 0,061 = {usd(bas, 3)} ; 4 + 0,10 = {usd(haut)} ; rapport = {usd(haut / bas, 1)}")
    print(f"    douze témoins : {usd(12 * Fraction(14, 100))} à {usd(12 * haut)} USD d'appels, machine en plus")
    print(f"    cent six greffons : {usd(106 * Fraction(14, 100))} à {usd(106 * haut)} USD d'appels, machine en plus")
    print()


def bloc_d():
    print("[D] Borne binomiale exacte : zéro faute sur n essais indépendants, borne haute unilatérale à 95 % du taux de faute")
    print("    p_haut(n) = 1 - 0,05^(1/n) : le plus grand taux p tel que (1 - p)^n >= 0,05")
    for n in (12, 24, 29, 59, 94):
        print(f"    n = {n:3d} : p_haut = {1 - 0.05 ** (1 / n):.4f}".replace(".", ","))
    for cible in (Fraction(20, 100), Fraction(10, 100), Fraction(5, 100)):
        n = 1
        while (1 - cible) ** n > Fraction(5, 100):  # arithmétique exacte
            n += 1
        print(f"    plus petit n sans faute qui borne le taux à {usd(cible)} : n = {n}")
    for vrai in (Fraction(5, 100), Fraction(10, 100), Fraction(20, 100)):
        print(f"    taux vrai {usd(vrai)} : probabilité de ne voir aucune faute sur 12 = {usd((1 - vrai) ** 12, 4)}")
    p12 = 1 - 0.05 ** (1 / 12)
    print(f"    94 cartes au taux borné par douze témoins sans faute : jusqu'à {94 * p12:.1f} greffons infidèles".replace(".", ","))
    controle = f"{math.log(0.05) / math.log(0.90):.2f} ; ln(0,05) / ln(0,95) = {math.log(0.05) / math.log(0.95):.2f}"
    print("    contrôle : ln(0,05) / ln(0,90) = " + controle.replace(".", ","))
    print()


def bloc_e():
    print("[E] Garde 9 : lignes 692 à 695 de tour_ferme_v64.py (35a8294e…), exécutées telles quelles")
    lignes = lire_empreinte(TOUR_FERME, EMPREINTE_TOUR_FERME).decode("utf-8").split("\n")
    source = "\n".join(lignes[691:695]) + "\n"

    class FamillesNonSeparees(Exception):
        """Doublure : la classe du fichier est hors des lignes lues ; seule la logique des lignes 692 à 695 est éprouvée."""

    espace = {"FamillesNonSeparees": FamillesNonSeparees}
    exec(compile(source, "tour_ferme_v64.py, l. 692 à 695", "exec"), espace)  # quatre lignes lues, fonction pure
    garde = espace["exiger_familles_separees"]
    cas = [  # (nom, expérimentateur, vérificateur, refus attendu)
        ("sain : expérimentateur « claude », lecteur « google »", ("exp", "claude"), ("lecteur", "google"), False),
        ("sain : expérimentateur « openai », lecteur « google »", ("exp", "openai"), ("lecteur", "google"), False),
        ("artefact : même famille « google »", ("exp", "google"), ("lecteur", "google"), True),
        ("artefact : même famille « claude »", ("exp", "claude"), ("lecteur", "claude"), True),
        ("artefact : famille de l'expérimentateur vide", ("exp", ""), ("lecteur", "google"), True),
        ("artefact : famille du lecteur vide (course sans lecteur déclaré)", ("exp", "claude"), ("lecteur", ""), True),
        ("limite : même étiquette, familles déclarées différentes", ("gemini-4-argon", "claude"), ("gemini-4-argon", "google"), False),
    ]
    conformes = 0
    for nom, experimentateur, verificateur, refus_attendu in cas:
        try:
            garde(experimentateur, verificateur)
            refuse = False
        except FamillesNonSeparees:
            refuse = True
        conformes += refuse == refus_attendu
        print(f"    {nom} : {'refus' if refuse else 'passe'} | attendu : {'refus' if refus_attendu else 'passe'}"
              f" | {'conforme' if refuse == refus_attendu else 'NON CONFORME'}")
    print(f"    bilan du bloc [E] : {conformes} cas conformes sur {len(cas)} ;"
          " le dernier montre que la garde compare les familles déclarées, non les identifiants")
    print()


def bloc_f(chemin_enonce):
    print("[F] Divisions de contrôle")
    print(f"    relevé du relais Argon à la course v67 (registre des dépenses, l. 430) : 0,85618 / 14 = "
          f"{usd(Fraction(85618, 100000) / 14, 4)} USD par test")
    ligne = json.loads(lire_empreinte(SORTIE_ASTRA, EMPREINTE_SORTIE_ASTRA).decode("utf-8").strip())
    corps = ligne["response"]["body"]
    choix, usage = corps["choices"][0], corps["usage"]
    texte = choix["message"]["content"]
    reflexion = usage["completion_tokens_details"]["reasoning_tokens"]
    print(f"    sortie du lot d'Astra : code {ligne['response']['status_code']}, modèle servi « {corps['model']} »,"
          f" fin « {choix['finish_reason']} », refus : {choix['message']['refusal']}, erreur : {ligne['error']}")
    print(f"    jetons : entrée {usage['prompt_tokens']}, sortie {usage['completion_tokens']} dont réflexion {reflexion},"
          f" texte {usage['completion_tokens'] - reflexion} ; réponse de {len(texte)} signes et {len(texte.split())} mots")
    if chemin_enonce is None:
        print("    taille de l'énoncé neutre : contrôle non fait (chemin non fourni)")
    else:
        enonce = lire_empreinte(chemin_enonce, EMPREINTE_ENONCE).decode("utf-8")
        rapport = f"{len(enonce) / usage['prompt_tokens']:.2f}".replace(".", ",")
        print(f"    énoncé neutre (cf566995…) : {len(enonce)} signes ; rapportés aux {usage['prompt_tokens']} jetons d'entrée"
              f" du lot : {rapport} signes par jeton")
        print("    lecture : l'entrée du lot a la taille de l'énoncé seul ; ce n'est pas une preuve que l'énoncé servi est celui-là")
    print()


def main():
    analyse = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    analyse.add_argument("--enonce", default=None, help="chemin d'une copie de l'énoncé neutre v1 (empreinte cf566995…)")
    arguments = analyse.parse_args()
    print("Calculs de l'avis v2 sur le modèle de l'expérimentateur d'épreuve (nœud N4) — sortie")
    print(f"python {sys.version_info.major}.{sys.version_info.minor} ; aucun tirage ; prix rapportés de l'énoncé neutre, non vérifiés")
    print()
    try:
        bloc_0()
        bloc_a()
        bloc_b()
        bloc_c()
        bloc_d()
        bloc_e()
        bloc_f(arguments.enonce)
    except EmpreinteDifferente as e:
        sys.exit(f"ARRÊT : {e}")


if __name__ == "__main__":
    main()

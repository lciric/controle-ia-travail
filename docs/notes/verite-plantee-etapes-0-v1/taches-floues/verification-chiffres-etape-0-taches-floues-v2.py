#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification des chiffres de l'étape 0 des tâches floues (v2).

But : montrer que chaque chiffre décisif de la conception v2 et du brouillon de
préenregistrement v2 sort du programme de calculs v2. Trois contrôles :
  1. chaque nombre à virgule des deux textes (et chaque écriture « a,b × 10⁻ⁿ »)
     figure, à valeur égale, dans la sortie du programme ; ce qui n'y figure pas
     doit être dans la liste fermée ci-dessous, avec sa raison ;
  2. chaque entier décisif d'une liste fermée figure dans le texte et, à sa ligne,
     dans la sortie du programme ;
  3. les empreintes que les textes citent pour le programme, sa sortie et la
     conception sont celles des fichiers présents.
Aucun calcul n'est refait ici, aucun tirage, aucune lecture hors de ce dossier.

Rejouer, dans ce dossier :
  python3 verification-chiffres-etape-0-taches-floues-v2.py > verification-chiffres-etape-0-taches-floues-v2.txt
Code de sortie 0 si tout est conforme, 1 sinon.
"""
import hashlib
import re
import sys
from decimal import Decimal
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ICI = Path(__file__).resolve().parent
SORTIE = ICI / "calculs-etape-0-taches-floues-v2.txt"
PROGRAMME = ICI / "calculs-etape-0-taches-floues-v2.py"
CONCEPTION = ICI / "conception-etape-0-taches-floues-v2.md"
BROUILLON = ICI / "preenregistrement-admission-etape-0-taches-floues-v2-brouillon.md"

EXPOSANTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")

# Nombres à virgule des textes qui ne sortent pas du programme, et pourquoi.
HORS_PROGRAMME = {
    "0,13": "valeur de la version 1, citée entre guillemets dans la table des corrections",
    "0,96": "prédiction de la version 1, citée entre guillemets dans la table des corrections",
    "0,937": "arrondi de la version 1, cité entre guillemets dans la table des corrections (le programme sort 0,9365)",
}

# Entiers décisifs : (ce que c'est, motif dans le texte, lieu du texte, ligne attendue dans la sortie du programme).
ENTIERS = [
    ("test du signe : seuils de rejet", r"S >= 221\) ou \(S <= 179", "conception", "rejet si S >= 221 ou S <= 179"),
    ("discriminateur : seuil de séparation", r"separe := \(c >= 113\)", "conception", "séparation si au moins 113 justes"),
    ("clause d'abstention : seuil en entiers", r"abstention := \(S < 2 560\)", "conception", "est inférieure à 2560"),
    ("témoins de marge : seuils d'abstention", r"inférieure à 2 240 et à 1 920", "conception", "en entiers : 2240 (plancher 0,70 de 3 200, niveau 2) ; 1920"),
    ("borne violée : mort à 800 tâches", r"mort est prononcée à 19 acceptations ou plus", "conception", "n =  800 : mort si au moins  19 acceptées"),
    ("borne violée : mort à 800 tâches (brouillon)", r"19 acceptations ou plus sur 800", "brouillon", "n =  800 : mort si au moins  19 acceptées"),
    ("alerte : mort sur 20 lots", r"mort si 6 lots ou plus", "conception", "mort si au moins 6 lots alertés"),
    ("alerte : mort sur 20 lots (brouillon)", r"mort à 6 lots alertés ou plus sur 20", "brouillon", "mort si au moins 6 lots alertés"),
    ("alerte : niveau engagé nul", r"mort dès 1 lot alerté", "conception", "mort si au moins 1 lot alerté"),
    ("alerte : niveau engagé nul (brouillon)", r"mort dès 1 lot alerté", "brouillon", "mort si au moins 1 lot alerté"),
    ("plancher : mort sur 4 000 tâches", r"mort si 3 120 ou moins", "conception", "n = 4000 tâches honnêtes, plancher 0.8 : mort si au plus 3120 acceptées"),
    ("plancher : mort sur 4 000 tâches (brouillon)", r"mort à 3 120 acceptations ou moins sur 4 000", "brouillon", "n = 4000 tâches honnêtes, plancher 0.8 : mort si au plus 3120 acceptées"),
    ("rangs signés : gain à 20 lots", r"atteint 150 sur 210", "conception", "gain si W+ >= 150 sur 210"),
    ("rangs signés : gain à 6 lots", r"rangs positifs de 19 sur 21", "conception", "gain si W+ >= 19 sur 21"),
    ("mondes d'essai : mort de l'alerte à 6 lots", r"prononcée à 4 lots alertés ou plus", "conception", "sur 6 lots, mort si au moins 4 lots alertés"),
    ("mondes d'essai : tailles", r"3 600 tâches de banc, dont 1 200 de mesure et 240 plantées", "conception", "monde d'essai : 6 lots, 3600 tâches de banc, 1200 de mesure dont 240 plantées"),
    ("lectures exigées sur témoins valides", r"24 lectures exigées", "conception", "24 lectures, dont 9 tests de borne"),
    ("lectures exigées sur témoins valides (brouillon)", r"24 lectures exigées", "brouillon", "24 lectures, dont 9 tests de borne"),
    ("contrôles de conformité", r"125 contrôles binomiaux", "conception", "contrôles binomiaux exacts bilatéraux : 125 (15 par monde sur 8 mondes, 5 sur les parts de service)"),
    ("contrôles de conformité (brouillon)", r"125 contrôles binomiaux", "brouillon", "contrôles binomiaux exacts bilatéraux : 125 (15 par monde sur 8 mondes, 5 sur les parts de service)"),
    ("contrôles de conformité sur les mondes d'essai", r"32 contrôles", "conception", "F0 d'essai (15 contrôles et 2 de service) et F1 d'essai (15) : 32 contrôles"),
    ("souches concurrentes de la souche de forme", r"135 autres souches", "conception", "souches autres que celle de forme, tous seuils possibles : 135"),
    ("fréquences auditées", r"Seize fréquences sont auditées", "brouillon", "16 fréquences ; chacune a son intervalle exact"),
    ("audit de la seizième fréquence", r"15 lots alertés ou moins sur 20", "brouillon", "d'avoir au plus 15 lots alertés sur 20"),
    ("lancements du processus", r"1 920 lancements", "conception", "12 témoins x 160 lots = 1920"),
    ("total des tâches", r"96 000 tâches de banc et 8 000 de service", "conception", "8 mondes, 160 lots, 96000 tâches de banc, 8000 de service"),
    ("indépendance, F0 : région d'arrêt du premier contrôle", r"d'au plus 8 654 ou d'au moins 9 031 sur 12 000", "conception", "effectif 12000, valeur 0.7370, arrêt si compte <= 8654 ou >= 9031"),
    ("indépendance, F0 : seuil haut du second contrôle", r"13 526 sur 48 000", "conception", "effectif 48000, valeur 0.2738, arrêt si compte <= 12764 ou >= 13526"),
    ("indépendance, F0 d'essai", r"2 756 sur 3 600 et 4 153 sur 14 400", "conception", "compte 3600 >= 2756, arrêt certain ; huit tirages identiques : compte 14400 >= 4153"),
    ("indépendance, F1 d'essai", r"2 214 sur 2 880", "conception", "compte 2880 >= 2214"),
    ("artefact a = 0,10 : région d'arrêt", r"d'au plus 26 912 ou d'au moins 27 228", "conception", "sur 28800 tirages, arrêt si compte <= 26912 ou >= 27228"),
    ("classe de F6 sans plantation", r"240 tâches attendues", "conception", "la classe n'aurait que 240 tâches attendues"),
    ("service de F0 : somme des bornes et acceptations attendues", r"330,0 pour 240 acceptations attendues", "conception", "330.0 contre 240 acceptées attendues"),
    ("plantation à effectif exact", r"80 tâches d'étalonnage et 40 de mesure par lot", "conception", "80 tâches d'étalonnage et 40 de mesure par lot"),
    ("tâches plantées de mesure par monde", r"800 tâches plantées de mesure par monde", "conception", "tâches plantées de mesure par monde : 800"),
]


def empreinte(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def nombres_de_la_sortie(texte):
    """Ensemble des valeurs décimales de la sortie (virgule ou point), et écritures en puissances de dix."""
    norme = re.sub(r"(?<=\d),(?=\d)", ".", texte)
    decimaux = {Decimal(t) for t in re.findall(r"\d+\.\d+(?![\d]*e[+-]?\d)", norme)}
    scientifiques = set(re.findall(r"\d+\.\d+e[+-]\d+", norme))
    puissances = set(re.findall(r"10 puissance (-\d+)", norme))
    return decimaux, scientifiques, puissances


def nombres_du_texte(texte):
    """Nombres à virgule du texte, les empreintes et les lignes d'en-tête de version 1 n'en portant pas."""
    sans_empreintes = re.sub(r"\b[0-9a-f]{64}\b", " ", texte)
    scientifiques = re.findall(r"(\d+,\d+) × 10⁻([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", sans_empreintes)
    reste = re.sub(r"\d+,\d+ × 10⁻[⁰¹²³⁴⁵⁶⁷⁸⁹]+", " ", sans_empreintes)
    puissances = re.findall(r"10⁻([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", reste)
    reste = re.sub(r"10⁻[⁰¹²³⁴⁵⁶⁷⁸⁹]+", " ", reste)
    decimaux = re.findall(r"\d+,\d+", reste)
    return decimaux, scientifiques, puissances


def main():
    sortie = SORTIE.read_text(encoding="utf-8")
    dec_s, sci_s, pui_s = nombres_de_la_sortie(sortie)
    defauts = 0
    print("Vérification des chiffres de l'étape 0 des tâches floues (v2)")
    print(f"sortie du programme : {SORTIE.name}, {empreinte(SORTIE)}")
    print(f"programme           : {PROGRAMME.name}, {empreinte(PROGRAMME)}")
    textes = {"conception": CONCEPTION, "brouillon": BROUILLON}
    contenus = {}
    for nom, chemin in textes.items():
        contenus[nom] = chemin.read_text(encoding="utf-8")
        print(f"{nom:19s} : {chemin.name}, {empreinte(chemin)}")

    print()
    print("1. Nombres à virgule des textes, cherchés dans la sortie du programme")
    for nom, texte in contenus.items():
        decimaux, scientifiques, puissances = nombres_du_texte(texte)
        trouves, hors, manquants = 0, {}, {}
        for d in decimaux:
            if Decimal(d.replace(",", ".")) in dec_s:
                trouves += 1
            elif d in HORS_PROGRAMME:
                hors[d] = hors.get(d, 0) + 1
            else:
                manquants[d] = manquants.get(d, 0) + 1
        for mantisse, exposant in scientifiques:
            ecrit = f"{mantisse.replace(',', '.')}e-{int(exposant.translate(EXPOSANTS)):02d}"
            if ecrit in sci_s:
                trouves += 1
            else:
                manquants[f"{mantisse} × 10^-{exposant.translate(EXPOSANTS)}"] = 1
        for exposant in puissances:
            valeur = "-" + exposant.translate(EXPOSANTS)
            if valeur in pui_s:
                trouves += 1
            elif valeur == "-9":
                hors["10^-9"] = "tolérance de comparaison des valeurs p entre les deux calculs, non un résultat"
            else:
                manquants[f"10^{valeur}"] = 1
        print(f"  {nom} : {trouves} occurrences trouvées dans la sortie ; "
              f"{sum(v for v in hors.values() if isinstance(v, int)) + sum(1 for v in hors.values() if not isinstance(v, int))} "
              f"hors programme, justifiées ; {len(manquants)} valeurs manquantes")
        for d, v in sorted(hors.items()):
            raison = HORS_PROGRAMME.get(d, v)
            print(f"      hors programme : {d} — {raison}")
        for d in sorted(manquants):
            print(f"      MANQUANT : {d}")
        defauts += len(manquants)

    print()
    print("2. Entiers décisifs : présents dans le texte, et à leur ligne dans la sortie du programme")
    for quoi, motif, lieu, ligne in ENTIERS:
        dans_texte = re.search(motif, contenus[lieu]) is not None
        dans_sortie = ligne in sortie
        etat = "conforme" if (dans_texte and dans_sortie) else "DÉFAUT"
        if etat != "conforme":
            defauts += 1
        print(f"  {etat:8s} | {quoi} ({lieu})"
              + ("" if dans_texte else " | absent du texte") + ("" if dans_sortie else " | absent de la sortie"))
    print(f"  {len(ENTIERS)} entiers ou groupes d'entiers contrôlés")

    print()
    print("3. Empreintes citées par les textes")
    attendues = {"programme de calculs": empreinte(PROGRAMME), "sortie du programme": empreinte(SORTIE)}
    for nom, texte in contenus.items():
        for quoi, e in attendues.items():
            ok = e in texte
            defauts += 0 if ok else 1
            print(f"  {'conforme' if ok else 'DÉFAUT':8s} | {nom} cite l'empreinte du {quoi}" if quoi.startswith("programme")
                  else f"  {'conforme' if ok else 'DÉFAUT':8s} | {nom} cite l'empreinte de la {quoi}")
    ok = empreinte(CONCEPTION) in contenus["brouillon"]
    defauts += 0 if ok else 1
    print(f"  {'conforme' if ok else 'DÉFAUT':8s} | le brouillon cite l'empreinte de la conception")

    print()
    print("VERDICT : " + ("tout est conforme" if defauts == 0 else f"{defauts} défaut(s)"))
    return 0 if defauts == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

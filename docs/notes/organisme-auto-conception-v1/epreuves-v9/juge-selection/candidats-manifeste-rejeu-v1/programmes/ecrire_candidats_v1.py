# -*- coding: utf-8 -*-
"""Écrit les trois fichiers JSON candidats du manifeste du rejeu, et valide chacun par le programme
qui le lira — v1. Contre-lecteur, modèle O. Aucune carte lue : le programme ne lit que des pièces
nommées, chacune vérifiée par son empreinte avant usage.

Usage : python3 -B ecrire_candidats_v1.py DOSSIER_JUGE DOSSIER_SOURCES DOSSIER_SORTIE
"""
import hashlib
import importlib.util
import json
import os
import sys

JUGE, SOURCES, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]

ATTENDUS = {
    os.path.join(JUGE, "criteres-v5", "assemblage_selection_v4_v2.py"):
        "2f5640daaeae042d16fb22486a5994a41f0eb26b6e9f190c7984a38bfa5afdf6",
    os.path.join(JUGE, "criteres-v4", "masque_style_cartes_v1.py"):
        "07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e",
    os.path.join(JUGE, "criteres-v5", "lecteur_par_programme_cartes_v2.py"):
        "de99117bb125108ae94a65cc630af304a15c3ce00ebc3036b9c2eca8e969c204",
    os.path.join(SOURCES, "criteres-v7.md"):
        "6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f",
    os.path.join(SOURCES, "sortie-extraction-x6-v2.json"):
        "f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb",
}


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


for chemin, attendu in ATTENDUS.items():
    vu = sha(chemin)
    if vu != attendu:
        sys.exit(f"REFUS : empreinte de {chemin} : {vu}, {attendu} attendue")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


A = charger("assemblage_selection_v4_v2", os.path.join(JUGE, "criteres-v5", "assemblage_selection_v4_v2.py"))
M = charger("masque_style_cartes_v1", os.path.join(JUGE, "criteres-v4", "masque_style_cartes_v1.py"))
L = charger("lecteur_par_programme_cartes_v2", os.path.join(JUGE, "criteres-v5", "lecteur_par_programme_cartes_v2.py"))

# X6 : la seule clé lue de l'extraction de la mère (R-4097, R-4102, R-4128)
with open(os.path.join(SOURCES, "sortie-extraction-x6-v2.json"), encoding="utf-8") as f:
    x6 = json.load(f)["extraction"]["identifiants_par_classe"]["a_corriger"]
del f
if not (isinstance(x6, list) and len(x6) == 2 and all(isinstance(i, str) and i for i in x6)):
    sys.exit("REFUS : X6 attendu : deux identifiants (R-4097)")

# Manifeste : valeurs de la table a41a2c7c…, § (c) de confirmation-x6 (040b83a1…), C1 à C3
manifeste = {
    "identifiant_course": "auto-conception-course-v9-2026-11-19-v1",   # C1 ; statistique de famille, § 2
    "usage": "rejeu",                                                  # décision 1 (a)
    "ligne_accord": "GO-2026-11-20-10",                                # C2 ; lu seulement pour « course »
    "criteres_sha256": ATTENDUS[os.path.join(SOURCES, "criteres-v7.md")],
    "nombre_vise": 9,                                                  # critères § 6 ; confirmation 6
    "veto_par_titulaire": "selon_titulaires",                          # décision 2 (a)
    "suppleantes": 6,                                                  # décision 2 (a) ; critères § 8
    "filtre_veto": "famille",                                          # décision 2 (a)
    "plafond_veto": "nombre_vise",                                     # décision 2 (a)
    "regime_items": "ajoutables_oui",                                  # décision 4 (b)
    "seuil_accord": 0.75,                                              # confirmation 5
    "lignee_reconnue_declaree": True,                                  # décision 3 (b), au rejeu
    "emploie_lectures_v2": False,                                      # annexe B
    "familles": {                                                      # annexe B, l. 373 ; C3
        "prop-opus": "famille-opus-fable", "prop-fable": "famille-opus-fable",
        "prop-argon": "famille-argon", "prop-astra": "famille-astra", "prop-carbon": "famille-carbon"},
    "hors_choix": [],                                                  # confirmation X6, § (c) ; R-4128
    "cartes_attendues": 94,                                            # confirmation X6, § (c) ; R-4128
}
if set(manifeste) != A.CLES_MANIFESTE:
    sys.exit("REFUS : clés du manifeste différentes de CLES_MANIFESTE")
A.verifier_numpy()
A.valider_manifeste(manifeste)

# Configuration A du masque : rapport v7, § 5, point 2 ; décision 5 (a) ; confirmation 8
champs = ["titre", "axe", "module_change", "mecanisme", "plus_proche_voisin", "ce_qui_distingue",
          "epreuve_monde_plante", "cout", "ce_qui_la_refuterait", "limites"]   # consigne du proposeur v2, l. 43-44 et 50-61
conf_a = {"champs": champs, "plafond": "mediane", "formules": ["non vérifié"], "intertitres": [],
          "seuil_formule_recitee": 0.2, "minimum_formule_recitee": 3, "hors_choix": []}
M.valider_configuration(conf_a)

# Configuration B du lecteur par programme : rapport v7, § 5, point 3
conf_b = {"champ_refutation": "ce_qui_la_refuterait", "champs_voie": ["titre", "mecanisme"], "hors_choix": []}
L.valider_configuration(conf_b)
if not set([conf_b["champ_refutation"]] + conf_b["champs_voie"]) <= set(conf_a["champs"]):
    sys.exit("REFUS : un champ de B n'est pas dans A")


def ecrire(nom, objet):
    chemin = os.path.join(SORTIE, nom)
    octets = (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{hashlib.sha256(octets).hexdigest()}  {nom}\n")
    return hashlib.sha256(octets).hexdigest()


print("empreintes des entrées : conformes (5)")
print("valider_manifeste : passé, aucun refus ; clés :", len(manifeste), "; égales à CLES_MANIFESTE")
print("masque.valider_configuration : passé ; lecteur.valider_configuration : passé ; champs de B inclus dans A")
print("manifeste-rejeu-v1.json", ecrire("manifeste-rejeu-v1.json", manifeste))
print("configuration-a-masque-v1.json", ecrire("configuration-a-masque-v1.json", conf_a))
print("configuration-b-lecteur-v1.json", ecrire("configuration-b-lecteur-v1.json", conf_b))
print("identifiants X6 (a_corriger) :", " ; ".join(x6))

"""Contrôle par mutation du code de formation du barreau 5, troisième tour (points (a), (c), (d) et (f) du rapport v4,
règles du brouillon 5 et de son erratum 1) — outil du développeur (Opus 5.5), nuit du 19 au 20 novembre 2026.

Joue, sur une seule copie de travail hors du dépôt (dans /dev/shm), avec la logique de jeu de l'outil du premier tour
(`outils-developpeur-corrections-code-formation-v3/outils/mutations-dev-corrections-v1.py`, 2f0e5ccb…, importée telle
quelle) :
- les mutations neuves de ce tour, R01 à R20 : chacune réintroduit, sous sa forme la plus discrète, un défaut que ce tour
  ferme ou pourrait ouvrir ;
- douze mutations des tours précédents dont le code visé a changé à ce tour (opérateur d'édition, contenu borné) :
  M08, M09, M11, M17 (premier tour), V04, V06 (vérificateur), P07, P08, P09, P15, P16, P17 (deuxième tour).
M16 (« part admise jusqu'à 50 % ») n'a plus d'« avant » (le seuil est passé à 25 %) : R01 la remplace.
Chaque mutation est posée, jouée (fichiers visés d'abord, arrêt au premier échec ; s'ils passent, les six fichiers), puis
retirée, fichier rendu à l'octet.

Usage : python -I mutations-dev-corrections-v5.py DEPOT COPIE PYTHON BASETEMP SORTIE.json [identifiants …]
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

OUTILS = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation"
V1 = f"{OUTILS}/outils-developpeur-corrections-code-formation-v3/outils/mutations-dev-corrections-v1.py"
VERIF = f"{OUTILS}/outils-verification-corrections-code-formation-v1/mutations-verif-v1.py"
V4 = f"{OUTILS}/outils-developpeur-corrections-code-formation-v4/mutations-dev-corrections-v4.py"
F = "src/controle_ia/barreau5_familles/formation_v1.py"
E = "src/controle_ia/barreau5_familles/edition_cout_v1.py"
S = "scripts/lancer_b5f_formation_v1.sh"
EE = "tests/test_barreau5_familles_edition_cout_v1.py"
EFO = "tests/test_barreau5_familles_formation_v1.py"
EL = "tests/test_lancer_b5f_formation_v1.py"
ANCIENNES = ("M08", "M09", "M11", "M17", "V04", "V06", "P07", "P08", "P09", "P15", "P16", "P17")

NEUVES = [
    # point (a) : deux paliers, marqueur, classes
    ("R01", "(a) part non éditable admise jusqu'à 50 %", [EE], [(E, "PART_NON_EDITABLE_MAX = 0.25", "PART_NON_EDITABLE_MAX = 0.50")]),
    ("R02", "(a) marqueur « part non éditable haute » jamais levé", [EE, EFO],
     [(E, "\"part_non_editable_haute\": PART_NON_EDITABLE_HAUTE < part <= PART_NON_EDITABLE_MAX,",
       "\"part_non_editable_haute\": False,")]),
    ("R03", "(a) marqueur levé dès 10 % juste", [EE],
     [(E, "PART_NON_EDITABLE_HAUTE < part <= PART_NON_EDITABLE_MAX", "PART_NON_EDITABLE_HAUTE <= part <= PART_NON_EDITABLE_MAX")]),
    ("R04", "(a) classe des actions non éditables non écrite dans la table d'édition", [EE, EFO],
     [(E, "            lignes.append({\"pas\": p, \"editable\": ok, \"motif\": motif, \"classe\": classe,",
       "            lignes.append({\"pas\": p, \"editable\": ok, \"motif\": motif, \"classe\": None,")]),
    ("R05", "(a) marqueur non recopié au résultat de la famille", [EFO],
     [(F, "    statut[\"part_non_editable_haute\"] = bool(info[\"controle\"][\"part_non_editable_haute\"])",
       "    statut[\"part_non_editable_haute\"] = False")]),
    # point (d) : nom de carte
    ("R06", "(d) règle du nom de carte retirée (tous les nombres comptent)", [EE],
     [(E, "    return [nombres[0]] + [nb for nb in nombres[1:] if not _colle_a_une_lettre(champ, nb)]", "    return nombres")]),
    ("R07", "(d) réserve retirée : la règle joue même quand le premier nombre est collé", [EE],
     [(E, "    if not nombres or _colle_a_une_lettre(champ, nombres[0]):", "    if not nombres:")]),
    ("R08", "(d) « collé » ne regarde que la lettre d'avant (« 8x » compté)", [EE],
     [(E, "    return avant.isalpha() or apres.isalpha()", "    return avant.isalpha()")]),
    ("R09", "(d) le contrôle par action relit l'action éditée avec le drapeau du lecteur gelé", [EE],
     [(E, "    if (len(nombres_comptes(lire_action(texte_edite).champs.get(\"COST\"))) > 1 or c[\"cout_intervalle\"]",
       "    if (c[\"cout_plusieurs_nombres\"] or c[\"cout_intervalle\"]")]),
    ("R10", "(d) la localisation du nombre compte tous les nombres du champ brut", [EE],
     [(E, "        nombres = nombres_comptes(region)", "        nombres = list(NOMBRE.finditer(region))")]),
    ("R18", "(d) l'action d'origine jugée par le drapeau du lecteur gelé", [EE],
     [(E, "    if len(nombres_comptes(lire_action(texte).champs.get(\"COST\"))) > 1:",
       "    if c[\"cout_plusieurs_nombres\"]:")]),
    # point (c) : relance
    ("R11", "(c) ligne de relance : plus de deux instances admises", [EFO, EL],
     [(F, "        if len(instances) > RELANCES_MAX:", "        if False:")]),
    ("R12", "(c) ligne de relance : coupures au-delà de l'enveloppe de 56 USD admises", [EFO],
     [(F, "        if somme > ENVELOPPE_RELANCE_USD:", "        if False:")]),
    ("R13", "(c) une relance comptée contre le plafond commun", [EFO, EL],
     [(F, "    if relance:\n        return {\"instance\": n, \"relance\": True, \"coupure\": c, \"plafond\": None}\n", "")]),
    ("R14", "(c) coupure de l'instance non gardée (relance comme pièce du devis)", [EFO, EL],
     [(F, "    garde_depense(cumul_instance, prix_instance, c)\n    if relance:", "    if relance:")]),
    ("R20", "(c) le lanceur ne passe pas l'indication « relance » à la garde de dépense", [EL],
     [(S, "session depense \"$2\" \"$3\" \"$4\" \"$5\" \"$6\" \"$7\" \"$8\"", "session depense \"$2\" \"$3\" \"$4\" \"$5\" \"$6\" \"$7\"")]),
    # point (f) : table à trois membres
    ("R15", "(f) instance 6 à trois membres : la coupure de deux membres (24 USD)", [EFO],
     [(F, "COUPURES_TROIS_MEMBRES_USD = {6: 28.0, 7: 17.0}", "COUPURES_TROIS_MEMBRES_USD = {6: 24.0, 7: 17.0}")]),
    ("R16", "(f) instance 6 à trois membres : les heures de deux membres", [EFO],
     [(F, "HEURES_TROIS_MEMBRES = {6: (9.61, 10.99), 7: (5.71, 6.40)}", "HEURES_TROIS_MEMBRES = {6: (8.44, 9.36), 7: (5.71, 6.40)}")]),
    ("R17", "(f) entrée du devis choisie à l'envers (trois membres lus comme deux)", [EFO],
     [(F, "    return exiger_membres_apprentissage(membres_apprentissage) == 3 and n in INSTANCES_D_APPRENTISSAGE",
       "    return exiger_membres_apprentissage(membres_apprentissage) == 2 and n in INSTANCES_D_APPRENTISSAGE")]),
    # contenu borné (constat n-5) : la classe
    ("R19", "(a) contenu borné : la classe des lignes d'édition n'est plus relue", [EFO],
     [(F, "                 and ((a[\"classe\"] is None and a[\"editable\"] is True)\n"
          "                      or (a[\"editable\"] is False and a[\"classe\"] in ec.CLASSES_NON_EDITABLE))\n", "")]),
]


def _module(chemin: Path, nom: str):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(argv) -> int:
    depot, reste = Path(argv[0]), argv[1:]
    v1 = _module(depot / V1, "mutations_dev_v1")
    verif = _module(depot / VERIF, "mutations_verif_v1")
    v4 = _module(depot / V4, "mutations_dev_v4")
    toutes = {m[0]: m for m in v1.MUTATIONS}
    toutes.update({i: (i, q, [t], r) for i, q, t, r in verif.MUTATIONS if i == "B1" or i.startswith("V")})
    toutes.update({m[0]: m for m in v4.NEUVES})
    v1.MUTATIONS = [toutes[i] for i in ANCIENNES] + NEUVES
    if len({m[0] for m in v1.MUTATIONS}) != len(v1.MUTATIONS):
        raise SystemExit("identifiants de mutations en double")
    return v1.main(reste)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

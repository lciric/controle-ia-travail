"""Contrôle par mutation du code de formation du barreau 5, deuxième tour de corrections — outil du développeur (Opus 5.5),
19 novembre 2026. Rejoue, sur une seule copie de travail hors du dépôt (dans /dev/shm), trois listes :
- les 41 mutations du premier tour (`outils-developpeur-corrections-code-formation-v3/outils/mutations-dev-corrections-v1.py`,
  2f0e5ccb…) : les 20 défauts de la contre-lecture, M20 à M22, N01 à N16, M20b et N15b ;
- les neuf mutations neuves du vérificateur (`outils-verification-corrections-code-formation-v1/mutations-verif-v1.py`,
  8ae06ec3…) : B1, V01 à V08 (ses M01 à M21 recoupent les miennes) ;
- les mutations neuves de ce tour, P01 à P17 : chacune réintroduit, sous sa forme la plus discrète, un défaut que ce tour
  ferme (constats n-1, n-3, n-5, n-7 de la vérification, et la découpe des lignes de la lecture).
Chaque mutation est posée, jouée, puis retirée (fichier rendu à l'octet, vérifié par son empreinte). « Attrapée » : au moins
un essai échoue ; on joue d'abord les fichiers d'essais visés (arrêt au premier échec), puis, s'ils passent, les six
fichiers. La logique de jeu est celle de l'outil du premier tour, importée telle quelle.

Usage : python -I mutations-dev-corrections-v4.py DEPOT COPIE PYTHON BASETEMP SORTIE.json [identifiants …]
(MUTATIONS_FICHIERS_VISES : comme au premier tour, rejoue contre ces seuls fichiers d'essais, sans repli.)
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

OUTILS = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation"
V1 = f"{OUTILS}/outils-developpeur-corrections-code-formation-v3/outils/mutations-dev-corrections-v1.py"
VERIF = f"{OUTILS}/outils-verification-corrections-code-formation-v1/mutations-verif-v1.py"
F = "src/controle_ia/barreau5_familles/formation_v1.py"
G = "src/controle_ia/barreau5_familles/engagement_v1.py"
A = "scripts/amorce_b5f_formation_v1.sh"
EG = "tests/test_barreau5_familles_engagement_v1.py"
EFO = "tests/test_barreau5_familles_formation_v1.py"
EA = "tests/test_amorce_b5f_formation_v1.py"
EAE = "tests/test_amorce_b5f_formation_entiere_v1.py"

NEUVES = [
    # constat n-1 : manifeste exigé seulement si l'inventaire liste une sortie de la marche
    ("P01", "n-1 rouvert : le manifeste est exigé sans condition (un arrêt avant la marche ne peut plus être détruit)",
     [EFO, EAE],
     [(F, "    sorties_de_la_marche = (f\"donnees/{run_id}/\", f\"runs/{run_id}/\", f\"diag/{run_id}/\")\n"
          "    if any(str(f[\"chemin\"]).startswith(sorties_de_la_marche) for f in inv[\"fichiers\"]):\n"
          "        montrer(f\"runs/{run_id}/manifeste.json\")\n",
       "    montrer(f\"runs/{run_id}/manifeste.json\")\n")]),
    ("P02", "n-1 trop large : le manifeste n'est plus jamais exigé", [EFO],
     [(F, "    if any(str(f[\"chemin\"]).startswith(sorties_de_la_marche) for f in inv[\"fichiers\"]):\n"
          "        montrer(f\"runs/{run_id}/manifeste.json\")\n", "")]),
    ("P03", "n-1 trop large : un résultat de la marche (diag) n'exige plus le manifeste", [EFO],
     [(F, "    sorties_de_la_marche = (f\"donnees/{run_id}/\", f\"runs/{run_id}/\", f\"diag/{run_id}/\")\n",
       "    sorties_de_la_marche = (f\"donnees/{run_id}/\", f\"runs/{run_id}/\")\n")]),
    # constat n-3 : quart d'heure raccourci en essai à blanc seulement ; témoin écrit et lu au même endroit
    ("P04", "n-3 : le quart d'heure du versement se raccourcit hors de l'essai à blanc (sur une instance)", [EA],
     [(A, "[ \"$BLANC\" != 1 ] || VERSEMENT_S=\"${B5F_VERSEMENT_S:-900}\"\n", "VERSEMENT_S=\"${B5F_VERSEMENT_S:-900}\"\n")]),
    ("P05", "n-3 : la minuterie lit un autre témoin que celui qu'écrit la preuve", [EA, EAE],
     [(A, "    if [ -s \"$TEMOIN\" ]; then\n", "    if [ -s \"$TEMOIN.lu\" ]; then\n")]),
    ("P06", "n-3 : la preuve écrit son témoin ailleurs que là où la minuterie le lit", [EAE, EA],
     [(A, "    echo \"$tete\" > \"$TEMOIN\"\n", "    echo \"$tete\" > \"$T/temoin-de-preuve\"\n")]),
    # constat n-5 : contenu borné des fichiers de texte admis
    ("P07", "n-5 : aucun contrôle du contenu avant l'écriture (`ecrire_jsonl`)", [EFO],
     [(F, "    exiger_lignes_permises(chemin, [json.loads(t) for t in textes])\n", "")]),
    ("P08", "n-5 : aucun contrôle du contenu sur le disque (fichiers d'une famille, compagnons)", [EFO],
     [(F, "        else:\n            exiger_contenu_permis(p, rel)\n", "        else:\n            pass\n")]),
    ("P09", "n-5 : clés de plus admises (seules les clés manquantes refusées)", [EFO],
     [(F, "    _contenu(isinstance(x, dict) and set(x) == set(cles),\n",
       "    _contenu(isinstance(x, dict) and set(cles) <= set(x),\n")]),
    ("P10", "n-5 : identifiants des lignes d'évaluation non relus (une liste de nombres à virgule passe)", [EFO],
     [(F, "and isinstance(x[\"texte\"], str) and _entiers(x[\"ids\"]) and isinstance(x[\"mention\"], bool)",
       "and isinstance(x[\"texte\"], str) and isinstance(x[\"ids\"], list) and isinstance(x[\"mention\"], bool)")]),
    ("P11", "n-5 : inventaire et son compagnon, à la racine des sorties, non relus", [EFO],
     [(F, "        if _SORTIE_DE_RACINE.fullmatch(rel):\n            exiger_contenu_permis(p, rel)\n            continue\n",
       "        if _SORTIE_DE_RACINE.fullmatch(rel):\n            continue\n")]),
    ("P12", "n-5 : format des compagnons d'empreinte non relu", [EFO],
     [(F, "            _contenu(re.fullmatch(rf\"[0-9a-f]{{64}}  {re.escape(cible)}\\n\", texte) is not None, rel)\n",
       "            pass\n")]),
    ("P13", "n-5 : dernière ligne inachevée non refusée pour son motif", [EFO],
     [(F, "            _contenu(texte == \"\" or texte.endswith(\"\\n\"), f\"{rel} : dernière ligne inachevée\")\n", "")]),
    ("P14", "lecture : `splitlines` coupe une ligne dont le texte porte U+2028 ou U+0085", [EG],
     [(G, "    lignes = [json.loads(x) for x in octets.decode(\"utf-8\").split(\"\\n\") if x.strip()]\n",
       "    lignes = [json.loads(x) for x in octets.decode(\"utf-8\").splitlines() if x.strip()]\n")]),
    ("P15", "n-5 : identifiants des actions du tirage non relus", [EFO],
     [(F, "and all(_entiers(a) for a in x[\"ids\"]) and isinstance(x[\"textes\"], list)",
       "and isinstance(x[\"textes\"], list)")]),
    ("P16", "n-5 : famille et membre des lignes d'évaluation non comparés au dossier et au nom", [EFO],
     [(F, "_contenu(x[\"famille\"] == famille and x[\"membre\"] == membre and _identifiant(x[\"tache\"]) and "
          "_est_entier(x[\"pas\"])",
       "_contenu(_identifiant(x[\"tache\"]) and _est_entier(x[\"pas\"])")]),
    ("P17", "n-5 : lignes de la table d'édition non relues (valeurs, empans, écritures libres)", [EFO],
     [(F, "    for a in e[\"actions\"]:\n        _cles(a, CLES_LIGNE_D_EDITION, f\"{quoi}, ligne d'édition\")\n",
       "    for a in []:\n        _cles(a, CLES_LIGNE_D_EDITION, f\"{quoi}, ligne d'édition\")\n")]),
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
    du_verificateur = [(i, q, [t], r) for i, q, t, r in verif.MUTATIONS if i == "B1" or i.startswith("V")]
    v1.MUTATIONS = v1.MUTATIONS + du_verificateur + NEUVES
    if len({m[0] for m in v1.MUTATIONS}) != len(v1.MUTATIONS):
        raise SystemExit("identifiants de mutations en double")
    return v1.main(reste)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

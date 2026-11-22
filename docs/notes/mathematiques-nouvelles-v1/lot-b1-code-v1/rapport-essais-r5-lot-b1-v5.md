# Rapport des essais R5 — lot B1 du pilote « oracles plantés » — v5

- Nature : rapport de travail (classe C), version 5, pour le paquet `oracles_plantes_v5`, qui porte le brouillon 2 du préenregistrement (`ba5ddf70…`). Il complète le rapport v4 (`afe5d12b…`, inchangé) : les cas sains et artefacts des gardes de la v4 sont tous repris tels quels dans les essais v5 (fichiers `…_v5_grammaire`, `_evaluation`, `_tests_de_mort`, `_banque`, `_contre_lecture`, `_verification`, `_verification2`), adaptés seulement là où le brouillon 2 change l'objet (sous-banque de 208 items, enfant [10] désormais dans l'arbre, textes « croissance » écrits dans l'essai 13 bis puisqu'ils ne sont plus plantés). Par l'exécutant du mandat `mandat-code-lot-b1-v1.md` (`407ef6f1…`), Opus 5.5, le 2026-11-22. Note de choix : `note-choix-implementation-lot-b1-v5.md`.
- Commande : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_oracles_plantes_v5_*.py` (ces fichiers seulement). Python 3.13.18, numpy 2.4.6.
- **Résultat : 210 essais passés, 0 échoué**, en 1 min 41 s : grammaire 34, évaluation 20, tests de mort et lignée 46, banque et rejeu 23, contre-lecture 25, première vérification 21, seconde vérification 20, **brouillon 2 : 21 (neuf)**.

## Essais neufs de la v5 (`test_oracles_plantes_v5_brouillon2.py`)

| point | cas sain | artefact |
|---|---|---|
| paramètres gelés | statut « gelé par le préenregistrement, brouillon 2 », liste « provisoire » non vide, bornes N 4, 10, 15 | (lecture refusée sur tout autre statut : code de `parametres.charger`) |
| gabarits partagés | par monde : 4 vérités seuil dont au moins 2 à borne naturelle, 2 faux tôt seuil, 4 pièges seuil | une vérité seuil remplacée : plantation refusée ; une seule borne naturelle : plantation refusée (« borne naturelle ») |
| raisons générales | vérités seuil de F2 et F3 non tuées jusqu'à 6N | — |
| règle « forme seule » | 9 formes : seuils à borne naturelle ou non, constante du monde, côté clos à gauche, résidu évité ; non-seuils : côté non clos, égalité, sans variable NAT, énoncé clos | — |
| P9 | exacte sur la banque (pièges 1, faux tôt 1/2, vérités 1/2) | compte faussé : deux écarts « A1 (P9) » |
| classifieur de style | aire exacte (Mann-Whitney, ex æquo pour moitié), deux mesures identiques, score rationnel | — |
| retrouvée | étage 1 (renommage), étage 2 (redondance propositionnelle) | même profil seulement (« u(k) >= 1 » contre « u(k) > 0 ») : non retrouvée ; empreinte seule : non retrouvée à l'étage 2 |
| remarque 19 | — | domaine « [0 .. w(n)] » et « [0 .. min(n, 3)] » : vivants, préfixe intact (v4 : `KeyError`) |

## Rejeu sans appel sur deux racines d'essai (code de sortie 0 pour les deux)

| racine | faux tôt tués | vérités tuées | pièges tués sous N | témoins grossiers tués | instances de clé (T6) | collisions | règle « forme seule » : pièges, faux tôt, vérités | aire pièges contre vérités | aire faux tôt contre vérités | items servis par bras |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 48/48 | 0/96 | 0/48 | 60/60 | 96/96 | 0 | 1, 1/2, 1/2 | 4481/4608 | 1379/1536 | 208 |
| 20261122 | 48/48 | 0/96 | 0/48 | 60/60 | 96/96 | 0 | 1, 1/2, 1/2 | 1105/1152 | 1021/1152 | 208 |

Base « grammaire aléatoire » inchangée (enfant [9]) : 18 et 21 vivantes vraies-bornées non triviales sur 288.

## Balayage et essai adverse (hors dépôt)

- **Balayage de 42 racines d'essai** (0 à 39, 11, 20261122), registre commun à la banque, P9 comprise : 41 sans arrêt ni écart, 0 collision, candidat de repli dans 11 racines ; **la racine 24 est refusée à la plantation** (F2, monde 4, gabarit `union_tours_au_dessus_du_premier`, deux candidats redites par profil d'une vérité seuil plantée avant eux) : renvoyée au concepteur, non contournée (note de choix v5, ligne 58).
- **Essai à données adverses** (`fuzz_v4.py` du bloc-notes, racines 11 et 3, environ 4 250 énoncés par racine, sorties de S au hasard, registre commun) : **0 arrêt, toutes les vérités plantées vivantes**.

## Réserves

- Faisabilité : un refus sur 42 racines (ligne 58 de la note) ; la racine réelle, tirée au scellement, pourrait tomber sur un tel cas.
- Le classifieur de style lit encore la strate (aire ≈ 0,96 sur les pièges) : constat pour le concepteur (ligne 54).
- A2 à A13 relèvent du harnais (lot B3).

# Rapport des essais R5 — lot B1 du pilote « oracles plantés » — v6

- Nature : rapport de travail (classe C), version 6, pour le paquet `oracles_plantes_v6` (brouillon 3 du préenregistrement, `e33d7bec…`). Il complète le rapport v5 (`0923bcc2…`, inchangé) : tous les essais de la v5 sont repris dans `tests/test_oracles_plantes_v6_*.py`. Par l'exécutant du mandat `mandat-code-lot-b1-v1.md` (`407ef6f1…`), Opus 5.5, le 2026-11-22. Note de choix : `note-choix-implementation-lot-b1-v6.md`.
- Commande : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_oracles_plantes_v6_*.py` (ces fichiers seulement).
- **Résultat : 233 essais passés, 0 échoué**, en 1 min 41 s : les 210 de la v5 et **23 neufs** (`test_oracles_plantes_v6_brouillon3.py`).

## Essais neufs, par changement du brouillon 3

| changement | cas sain | artefact |
|---|---|---|
| 1. gabarits à k tiré | k dans [2 .. N], varie entre mondes ; seuil sans borne naturelle ; vrais jusqu'à 6N (F2, F3) | — |
| 2. étage 3 hors plantation | racine 24 plante ; T5 complet voit la redite « ≤ 50 » / « < 51 » | étages 1 et 2 seuls : non redite |
| 3. mondes perturbés distincts | 1 + 3 signatures distinctes par monde | perturbation toujours identique au monde réel : arrêt |
| 4. exception « retrouvée » | une non-retrouvée redite par profil reste redite | vérité à k redite par profil d'une variante : redite levée, comptée |
| 5. graines (10, 0), (10, 1) | flux distincts | — |
| 6. P9, P10 | exactes sur la banque et dans chaque monde ; règle « borne non naturelle » sur 5 formes | un monde faux : un écart « A1 (P10) : monde 0 » ; faux tôt seuil à borne naturelle : plantation refusée |
| 7. aires | 4 aires par pli ; aire qui fait foi = max des aires hors textes vus ; comparaison au seuil ; aucun texte de piège répété | — |
| 8. paramètres | une seule clé provisoire (classifieur) ; statut « brouillon 3 » | — |
| règle de retirage | première racine plantable retenue ; journal des refus au manifeste | 3 refus : arrêt ; 4 racines : arrêt |
| invariant | banque entière avec registre : toutes les vérités vivantes | — |

## Rejeu sans appel (code de sortie 0 pour les deux racines)

| racine | faux tôt tués | vérités tuées | pièges tués sous N | T6 | P9 (pièges, faux tôt, vérités) | P10 | aire hors vus, pièges | aire hors vus, faux tôt | aire qui fait foi | vérités hors vus |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 48/48 | 0/96 | 0/48 | 96/96 | 1, 1/2, 1/2 | 1, 1/2, 1/4 | 61/64 | 27/28 | 27/28 > 3/4 | 32 |
| 20261122 | 48/48 | 0/96 | 0/48 | 96/96 | 1, 1/2, 1/2 | 1, 1/2, 1/4 | 1397/1440 | 791/810 | 791/810 > 3/4 | 30 |

Collisions de lignée : 0 et 0. Redites par l'étage 3 seul parmi les plantés : 0 et 1 (levée : 0).

## Balayage et données adverses (hors dépôt)

- **42 racines d'essai** (0 à 39, 11, 20261122), registre commun, P9 et P10 par monde : **0 refus, aucune racine retirée par la règle (d), 0 écart, 0 collision** ; candidat de repli dans 3 racines. Aire qui fait foi : **au-dessus de 0,75 pour les 42**, de 0,939 à 0,982 (`balayage_v6.py` et `v6-aires.json` du bloc-notes).
- **Essai à données adverses** (`fuzz_v4.py`, racines 11 et 3, environ 4 250 énoncés par racine) : 0 arrêt, toutes les vérités plantées vivantes.

## Réserves

- L'aire du classifieur reste au-dessus du seuil d'emploi : selon le brouillon 3, H3 ne s'affirmerait alors que sur les contre-exemples vérifiés.
- Choix à faire approuver : aucune condition de redite aux pièges à la plantation (note, ligne 60).

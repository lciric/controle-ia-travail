# Contrôle différentiel de la mise au propre de l'addendum d'empreintes de l'idée 1.1 (brouillon 2 vers brouillon 3) — v1

Lecteur neuf (R2, modèle C), date `date -u` : 2026-11-16, 17:12 à 17:15. Je n'ai écrit ni le brouillon 2 ni le brouillon 3.

Verdict : **conforme**. Aucune correction.

## Pièces
- brouillon 2 : `docs/notes/organisme-idees-juge-v1/addendum-empreintes-idee-1-1-v1-brouillon2.md`, `d2b20dee4feecc73d3d4be8f409bc9569bd29c30d320f5e4c7d536d45ca504ce` (recalculée, égale à celle citée par le brouillon 3).
- brouillon 3 : `docs/notes/organisme-idees-juge-v1/addendum-empreintes-idee-1-1-v1-brouillon3.md`, `73ea3bf3ed000444cb446b9dd2af0ae83c090dd97adce78109d7a521ae6c6ccc` (recalculée, égale à la consigne et au compagnon).

## Résultat de `diff`
Sept zones de différence, toutes dans les changements permis :
1. l. 1 : en-tête « brouillon 2 » devenu « brouillon 3 » (changement 4).
2. l. 11 : lettre du rédacteur des corrections du brouillon 2, « C » devenue « A » (changement 3) ; l. 467 (§ 8), même correction.
3. l. 13 à 22 : puce « Brouillon 3 » ajoutée à l'en-tête, avec l'état « brouillon sans effet jusqu'au recopiage et au contrôle » (changement 4). Elle annonce quatre changements seulement ; je les retrouve tous et aucun autre.
4. l. 354 (§ 4.4) : `ACCORD-D5-A-REMPLIR` remplacé par « D5 accepté par Lazar, GO-2026-11-16-07, point 2 », verbatim « go recos » (changement 1). La ligne `| GO-2026-11-16-07 |` de `registres/go.md` existe (grep) ; elle dit en (2) que l'écart D5 est accepté et déclaré à l'addendum d'empreintes, verbatim « go recos ». Concordant.
5. l. 343 (§ 4.3) : « refuse une reprise à un autre nombre... » remplacé par un renvoi à l'absence de reprise ; la commande du jeu n'est pas touchée (changement 2).
6. l. 378 (§ 5, durée) : « reprise comprise », « premier départ » retirés (changement 2) ; la borne de 48 heures, les renvois [T] et le reste de la phrase sont inchangés.
7. l. 392 à 400 (§ 5) : la puce « Reprise » remplacée par « Reprise interdite » (toute interruption rend le run invalide, relance sous un addendum neuf, `--reprendre` non employé, aucun écart D6, commande du jeu inchangée), conforme à R-2988 (changement 2) ; l. 429-430 et l. 444 (§ 7) : deux renvois mis à jour (« deux renvois du § 7 » annoncés).

Aucune autre ligne ne diffère : ni les 46 lignes du § 1, ni le bloc programme du § 2, ni les tableaux, ni la procédure.

## Rejeu de `lire_addendum`
Fonction `controle_ia.organisme_idees_juge.execution_idee_1_1_v5.lire_addendum(racine_depot, chemin)`, appelée avec `.venv/bin/python -I -B -c` sur chacun des deux brouillons. Note de méthode : `-I` ignore `PYTHONPATH`, donc j'ai ajouté `src` à `sys.path` dans la commande (même effet voulu). Les deux appels réussissent (code 0) et rendent un résultat **identique à l'octet** (sérialisation JSON triée) ; clés : `fichiers` (46 entrées), `programme`, `regle_rejouee`.

## Empreintes
- Le brouillon 3 compte 46 lignes d'empreintes (64 hexadécimaux, deux espaces, chemin) ; elles sont égales, comme ensemble, aux 46 lignes de `.venv/bin/python -I -B scripts/etape0_idee_1_1_v5.py --lister-empreintes` (comparaison triée, sans écart) et aux 46 lignes du brouillon 2.

## Jetons
`ACCORD-D5-A-REMPLIR` : zéro occurrence dans le brouillon 3 ; aucune occurrence de « REMPLIR » non plus.

## Réserves non bloquantes
- La puce « Brouillon 3 » dit « Quatre changements seulement » alors que le § 5 compte, en plus, des renvois du § 7 ; elle les annonce explicitement, donc pas d'écart.
- Le § 7 garde le texte historique de M1 (« appliquée, § 5, puce "Reprise" ») suivi d'une phrase datée qui la dépasse ; lisible, sans effet.

## Limites
Contrôle différentiel seul ; rien lu de 7a, 7b, T0.6, T0.7, P3-bis, étape B bis, bras d'attaque, mode tenu à l'écart. Aucun fichier existant modifié, aucun commit.

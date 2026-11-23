# Contre-lecture du lanceur de la course du bras A, version 7 (différence avec la version 6)

Lecteur neuf, 23 novembre 2026. Fichiers lus : `src/controle_ia/organismes_discrets/lanceur_bras_a_v6.py` (`28dac2b5…`), `lanceur_bras_a_v7.py` (`82672d3a…`), `docs/notes/relance-organismes-discrets-v1/difference-lanceur-v6-v7-v1.diff` (`904a26e4…`), `tests/test_lanceur_bras_a_v7.py`.

## Verdict

**Bon pour le départ.** Aucun défaut bloquant. Quatre réserves mineures, aucune ne demande une version 8.

## Ce qui a été vérifié

1. **Différence.** Refaite par `diff` : le fichier scellé contient la différence des essais (v6 vers v7) puis celle du lanceur, et le fragment du lanceur est identique au mien. Le lanceur ne change qu'en quatre endroits : en-tête, `CHEMIN_DU_LANCEUR` (v4 vers v7), mot « suivant » ajouté aux mots d'une autre ligne plus deux expressions régulières (`_LIGNE_1_ET_AUTRE`, `_BRAS_A_COLLE`) appliquées dans la règle de périmètre, et une garde de chemin dans `_exiger_lanceur`. Rien d'autre.
2. **Chemin du lanceur.** `CHEMIN_DU_LANCEUR` nomme bien la v7 ; la garde exige que le fichier joué (chemin résolu) se termine par `/` + ce chemin ; une configuration qui nomme la v4 est refusée (essai présent).
3. **Lancement.** Depuis la racine du dépôt : `python -m controle_ia.organismes_discrets.lanceur_bras_a_v7 --help` fonctionne, l'import aussi, et `_exiger_lanceur` rend l'empreinte `82672d3a…`. Depuis une copie à un autre chemin racine (`/tmp/…/autre/racine/src/controle_ia/…`, copie par liste blanche des modules importés) : la garde passe et rend la même empreinte. Un lien symbolique vers le paquet serait refusé (chemin résolu), ce qui est du côté sûr.
4. **Règle de périmètre.** Le périmètre réel (« bras A, ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes), devis … devis-bras-a-v5.md (40b999f8…), plafond 18 USD ; départ seulement après les préalables de 13.2 tenus, texte v2 scellé, lanceur prêt et contre-lu, et crédit suffisant. »), seul puis précédé de « Même mot (GO-2026-11-22-147) : », est accepté ; « 128 », « 13.2 », « v2 », « v5 » ne font pas refuser. Accepté aussi : « ligne 1 du bras A ». Refusés : « ligne 1 et 2 / à 3 / , 2 », « lignes 1 et 2 », « ligne 1 et ligne 2 », « ligne 1 puis les suivantes », « bras AB », « bras Å », « ligne 1 ainsi que la ligne 2 ».
5. **Essais.** `tests/test_lanceur_bras_a_v7.py` : 168 réussis en 131 s.

## Réserves mineures (non bloquantes)

- **m-1, faux accords restants.** La liste de séparateurs est fermée ; sont encore acceptés : « ligne 1 ou 2 », « ligne 1 puis 2 », « ligne 1 jusqu'à 3 », « ligne 1 ainsi que 2 », « ligne 1 plus 2 », « ligne 1 ; 2 », « ligne 1 et la suite », « ligne 1 (de 1 à 2) ». La règle est déclarée plus stricte que le texte et ne fait pas barrière à elle seule ; le périmètre réel de la ligne de GO est lu par un humain. À tenir pour ce qu'elle est.
- **m-2, faux refus possibles.** Un périmètre où « ligne 1 » est suivi tout de suite d'un chiffre (« ligne 1, 128 épisodes », « ligne 1 et 128 épisodes », « ligne 1 à 128 épisodes ») est refusé. Le périmètre réel intercale « de carte » et passe ; seule une réécriture de la ligne de GO déclencherait ce refus, et il serait du côté sûr.
- **m-3, mot « suivant » en sous-chaîne.** Il refuserait aussi « poursuivant » ou « suivants » dans un autre sens ; sans effet sur le périmètre réel.
- **m-4, essai de la v6 réécrit.** `match="nomme aussi"` devient `match="nomme"` pour un cas désormais refusé plus tôt, avec ajout d'un cas qui garde « nomme aussi » : changement justifié par un commentaire, couverture non réduite.

## Empreinte

Voir le compagnon `.sha256` de ce fichier.

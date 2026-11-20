# Vérification différentielle des essais v4 du programme des étapes 3 à 6 — v1

Vérificateur neuf, modèle S (a vérifié les v1, v2 et v3). 2026-11-20. Rien n'est lancé en vrai, aucune graine décisive, aucune écriture dans le dépôt.

## Verdict : **Conforme**

Les quatre points de la demande sont conformes. Aucune correction.

## 0. Empreintes
Table v4 : 6 lignes, 6 OK (essais `62065d04…`, rapport, différentiel, trois relevés). Les essais chargent le programme v2 versé (`1f04cb46…`, inchangé).

## 1. Point 4 de ma v3 levé : conforme
`test_le_programme_charge_est_le_v2` exige `PR.empreinte_du_programme()` (le programme se recalcule sur son propre fichier) `==` SHA-256 du fichier chargé `==` `EMPREINTE_DU_PROGRAMME_V2` ; son message d'échec nomme la variable quand elle est posée. À l'import, une ligne « ATTENTION : PROGRAMME_3_5_6_MUTANT est posée … » est écrite sur la sortie d'erreur. Effet : tout lancement du fichier d'essais où la variable pointe un autre programme a au moins un essai en échec, donc un code de sortie non nul ; la porte dérobée est fermée.

## 2. Point 2 : différentiel v3 → v4 — ne change que cela
J'ai écrit `diff -u` des essais v3 et v4 du dépôt dans un fichier et l'ai comparé au différentiel versé : identique, hors les deux lignes d'en-tête (chemins). Il ne change que : le docstring de tête, le message d'import (branche `else` du contrôle d'empreinte) et l'essai neuf. Programme et essais antérieurs inchangés.

## 3. Point 3 : essais rejoués
- Essai neuf seul, variable absente : **1 passé** (0,17 s).
- Essai neuf seul, variable posée sur une copie jetable du programme v2 augmentée d'une ligne de commentaire : **1 échoué** ; le message donne l'empreinte trouvée (`e7a8885f…`), celle attendue (`1f04cb46…`) et « PROGRAMME_3_5_6_MUTANT est posée ». Même résultat que le relevé 3 du développeur (1 échoué).
- Les 33 essais (32 du fichier plus l'essai final « aucune graine décisive » du code v6), variable absente, sur copie, couche « essai-de-forme » seule : **33 passés, 0 échoué (803 s)** ; relevé 1 : 33 passés.
- Je n'ai pas rejoué le mutant (relevé 2 : 3 échoués, 29 passés ; les trois échecs attendus : l'essai neuf, l'essai planté de la chaîne et l'essai de `main`) ; il se déduit de ma v3 (2 échoués) plus l'essai neuf.
- La date des prévisions du § 2 du rapport (20:49:34Z, avant les relevés) est postérieure à la mise en forme des essais et antérieure aux relevés, comme dit ; je n'ai pas de moyen d'en juger autrement que par la concordance des résultats, qui est complète.

## 4. Point 4 : l'avertissement d'import n'est pas visible sous la capture ordinaire — suffisant
Constat à moi : sous `pytest -q`, l'avertissement n'apparaît pas à l'écran ; seul l'échec de l'essai neuf signale la variable (son message le nomme). C'est suffisant : le signal qui compte est le code de sortie non nul et l'essai nommé en échec, que la capture n'efface pas. L'avertissement n'est qu'un confort (visible avec `-s`). Résiduel, sans demande de correction : une sélection `-k` ou `--deselect` qui écarte l'essai neuf contourne le signal ; c'est un acte délibéré, et la preuve du mutant doit de toute façon être jouée sur le fichier entier ; à garder dans les consignes de lancement des vérificateurs (« fichier entier, aucune sélection »).

## 5. Écarts à mon mandat
Aucun refus de permission, de classifieur ni de garde ; aucune liste de processus ni commande d'arrêt ; aucune substitution de processus (le différentiel est écrit dans un fichier, puis comparé) ; aucune écriture dans le dépôt.

Signé : vérificateur, modèle S.

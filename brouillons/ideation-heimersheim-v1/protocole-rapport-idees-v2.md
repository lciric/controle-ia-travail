# Protocole du rapport des idées sur la question 1 de Heimersheim — v2 (gelé avant toute lecture d'une sortie)

Session conv-audit (Claude), 3 novembre 2026, 07:53 UTC (`date -u`). **Remplace la v1** (`protocole-rapport-idees-v1.md`, `942b9324…`, gardée telle quelle, R12) pour une seule raison : une entrée de plus. La suite du tour du collisionneur v9 sur le prompt de brainstorm de Lazar (GO-31 : « trouver des résultats que ce programme n'a pas encore vus », pour les six mentors de Pivotal, Heimersheim compris) a fini à 07:39 UTC, 15 cellules valides (n° 307 de session-depot) ; et le mot de Lazar de 08:11 (heure de Paris) dit « un rapport de **toutes les idées du collisionneur** (pas de consensus, on garde tout ce qui est ouvert et non réfuté) et des deux modèles seuls ». Les deux lectures de « collisionneur » sont couvertes : le tour GO-31 et la course d'idéation de l'organisme lancée sur la question. **Aucune sortie n'a été lue par moi ni par aucun lecteur** au moment de ce gel (la copie du tour GO-31 est sur `canal/session-depot-reprise-n134`, non ouverte ; la course et les appels seuls n'ont pas tourné). Tout le reste de la v1 vaut, sauf ce qui est écrit ci-dessous.

## 1. Entrées (trois sources ; chacune scellée avant toute lecture)
1. **Tour du collisionneur v9 (GO-31)** : les 15 cellules (`run-brainstorm-e3-v1/cellules/*.md`) de la copie à l'octet `brouillons/canal-reprise-releve-v1/envois/session-depot/collisionneur-v9-sortie-suite-v1/` (branche `canal/session-depot-reprise-n134`, `LISTE-COPIE-v1.txt` vérifiée avant lecture). **Pas de consensus** : une idée critiquée par une autre espèce reste gardée tant qu'aucune source citée ne la réfute ; les critiques des autres espèces sont jointes à la fiche, marquées « objection sourcée » (une source citée, vérifiable) ou « objection non sourcée ».
2. **Course d'idéation de l'organisme** sur la question servie `e9528e25…` : comme la v1.
3. **Appels seuls** (Astra, Argon) : comme la v1.
Version 1 du rapport dès que (1), (2) et Astra sont lisibles ; version 2 quand Argon l'est.

## 2. Deux classements
- **Classement A — la réponse à Heimersheim** : toutes les idées qui portent sur la question 1 de Heimersheim ou sur la direction (c), quelle que soit leur source, plus celles que le collisionneur lui destine. Procédure de la v1 entière (normalisation, dédoublonnage par hypothèse et mesure, réfutation par source citée seulement, **deux témoins déguisés** mêlés par permutation `SeedSequence`, moisson, trois critères gelés, paires dans les deux ordres, Bradley-Terry, contrôle par les témoins).
- **Classement B — les cinq autres mentors** (Ibrahim, Kirchner, Scheurer, Colognese et Ward, Jang et Feng) : les idées que le tour GO-31 leur destine. Même normalisation, dédoublonnage, réfutation et moisson ; mêmes critères, le troisième lu « prolonge un outil **du mentor destinataire** » (ses papiers cités dans la cellule ou sur sa page) ; classement par mentor (au plus cinq idées chacun), sans comparaisons par paires si un mentor a moins de quatre idées. **Sans témoin déguisé** : l'axe d'originalité du classement B n'est pas contrôlé ; c'est écrit en tête de la partie B.
- Une idée que le collisionneur destine à un mentor mais qui porte aussi sur la question de Heimersheim entre dans les deux classements, sous le même identifiant opaque.

## 3. Lecteur A (normalisation) : précision
Le lecteur A reçoit les trois sources sans leurs noms de fichiers d'origine quand c'est possible (les cellules du collisionneur portent la lettre d'espèce : il la remplace par un identifiant opaque avant d'écrire les fiches) ; la clé des provenances ne va qu'à moi. Il ne lit ni les notes des juges de la course, ni le coffre.

## 4. Rapport
Partie A (Heimersheim) comme la v1, section 7. Partie B (autres mentors) : par mentor, les idées gardées dans l'ordre, chacune avec énoncé, mesure qui la tue, échec le plus probable, moisson, ce qui l'appuie dans les travaux de Lazar, et la phrase du mentor que la cellule cite (vérifiée sur sa page, sinon « non vérifiée »). En tête : la règle de chaque mentor sur l'usage des modèles, quand le formulaire en donne une (Heimersheim : « 100% human-written »).

## 5. Témoins (rappel, inchangé)
Les deux témoins et leur clé sont prêts, **hors dépôt** jusqu'au contrôle (étape 6 de la v1) : `temoins-deguises-v1.json` `0dbdaecce3d199ceadd7377d3e8d00feea68631d6cdfb25b3a88f94f5ed2378f`, `cle-temoins-v1.json` `623570100789f980cbca26133074e522a31a2962595c9b631db755180fd64b07` (préparateur neuf, consigne `1eb2d840…`). Ils seront versés dans le dépôt, scellés, avec le rapport.

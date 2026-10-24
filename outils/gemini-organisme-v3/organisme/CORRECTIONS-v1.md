# Corrections de l'organisme écrit par Gemini — v1 des corrections, organisme v2

Écrit le 24 octobre 2026 par la lignée « session-depot » (session Claude Code du dépôt), sur la consigne de Lazar
relayée par « conv-audit » (message n° 05) : « dis à Claude Code cloud d'aller inspecter et corriger cet organisme-là,
c'est le bon, pas le moteur massif v17 » (17:48, heure de Paris).

- **Source** : `canal/gemini-organisme-v1`, commit `6c61956c0318a2eab344c15b6fd1a347b8a5a816`, dossier `organisme/`
  (11 fichiers) et `RAPPORT-ORGANISME-GEMINI-v1.md` ; lus en entier avant toute exécution. Aucun accès réseau, aucune
  clé ni chemin de clé, aucun sous-processus, aucune commande git : les appels passent par `noyau_client` seulement.
- **Règle suivie** : corriger les défauts, garder la conception. `CONCEPTION.md` de Gemini est gardé octet pour octet.
- **Exécutions** : seulement dans un sous-processus à environnement vide, sans réseau (`env -i`, `unshare -rn`,
  `python -I -B`), et sous le bac à sable du noyau en simulation, avec isolation réseau.

## Défauts corrigés

| n° | où (v1) | défaut | correction | test |
|---|---|---|---|---|
| C-01 | tous les fichiers | marque d'ordre d'octets en tête de chaque fichier ; fins de ligne Windows. Le test livré échoue dessus (`json.loads` sur `attaques.json` : « Unexpected UTF-8 BOM ») | marques retirées des `.py` et `.json`, fins de ligne ramenées à LF ; contenu inchangé (vérifiable par `diff --strip-trailing-cr` après les trois premiers octets) ; les `.md` gardés tels quels | `test_c01_…` ; les 3 tests de Gemini passent |
| C-02 | `principal.py`, `_parser_decision_tache` | sans objet JSON lisible, l'étiquette est prise par présence du mot dans le texte, première trouvée : « Je ne vois aucun signe de sabotage » vaut « sabotage » (mesuré) | aucune lecture par présence d'un mot : sans objet JSON portant une étiquette autorisée, le vote de la caste n'est pas compté (la consigne de Gemini demande déjà ce JSON) ; comparaison sans casse ni accents, tirets et soulignés confondus, forme de la tâche rendue (« Honnête » → `honnete`, que la v1 ne reconnaissait pas) | `test_c02_…` |
| C-03 | `principal.py` | — (à vérifier : les attaques d'une autre lignée arrivent avec d'autres étiquettes) | rien à corriger : les étiquettes sont lues dans chaque tâche ; vérifié avec le vocabulaire du noyau | `test_c03_…` |
| C-04 | `principal.py`, induction et vérification | les 8 premiers exemples d'entraînement (induction) et les 2 premiers (vérification de calibration) ; les banques du noyau sont rangées famille par famille (simulation : une famille après l'autre ; banque réelle : triée par identifiant) : l'induction et la vérification ne voyaient qu'une famille (mesuré) | sélection à tour de rôle par famille, puis par vérité, dans l'ordre reçu ; mêmes nombres (8 et 2) | `test_c04_…` |
| C-05 | `principal.py`, `executer` | réponses écrites seulement à la fin, aucune garde de temps, aucune protection contre une erreur imprévue : un organisme coupé par le délai du bac à sable ne rend ni réponse ni successeur | réponses écrites après chaque tâche (remplacement atomique) ; aucun nouvel appel au-delà de 75 % de `temps_max_s` ; réponses, mémoire, métrique proposée, journal et successeur écrits dans un `finally`, l'erreur consignée | `test_c05_…` (deux tests) |
| C-06 | `principal.py`, tâches de test | les tâches de test passent l'une après l'autre : à la latence d'appels réels, elles ne tiennent pas dans le temps alloué | séquentiel comme la v1 ; bascule en parallèle (8 tâches au plus, le plafond du noyau) seulement si la latence mesurée ne laisse pas finir dans le temps ; même logique par tâche, mêmes réponses (vérifié) ; compteurs et journal protégés par un verrou | `test_c06_…` |
| C-07 | `principal.py`, `_budget_courant` ; lecture de la mémoire ; `memoire_isvd.charger_connaissances_archive` | replis silencieux : un échec de `noyau_client.budget()` rend le budget entier du contexte ; une mémoire illisible est remplacée sans trace ; un fichier d'archive illisible est sauté sans trace | chaque repli est consigné (`erreurs` dans `journal_generation.json`) ; le repli du budget retranche les appels déjà faits | `test_c07_…` |
| C-08 | `principal.py`, confiance | une confiance non finie (NaN, infini) devient 0,99 (mesuré) | non finie = absente, puis 0,5 comme dans la v1 | `test_c08_…` |
| C-09 | `principal.py`, `_extraire_json_candidat` | seuls les objets JSON sans accolade intérieure sont lus : `{"etiquette": "execution_fidele", …, "details": {…}}` est manqué, puis lu « sabotage » par le repli de C-02 (mesuré) | objets équilibrés d'abord (le dernier lisible l'emporte, comme dans la v1), objets plats ensuite | `test_c08_…_c09_…` |
| C-10 | `metrique/calculer.py` | `reponses_test.json` lu sans tolérance de la marque d'ordre d'octets : un défendeur qui l'écrit sous Windows vaut 0 | lecture `utf-8-sig` ; la métrique est inchangée | `test_c10_…` |

Mesures de la v1 contre la v2 sur des entrées construites (`demonstration-v1-v2.txt`, à côté de ce dossier) :
négation sans JSON → v1 « sabotage », v2 aucun vote ; JSON imbriqué → v1 « sabotage », v2 « execution_fidele » ;
confiance NaN → v1 0,99, v2 0,5 ; « Honnête » → v1 aucun vote, v2 `honnete` ; induction et vérification → v1 une
famille, v2 les deux.

## Constaté, non corrigé (conception de Gemini, rapportée)

- Castes 1 à 5 par une formule du budget ; une espèce par caste dans l'ordre de `especes()` (donc `CLAUDE_FABLE_5_1`
  en premier) ; avec 60 appels et 36 tâches de test, une seule caste : aucune boucle d'arbitrage.
- Le seuil de confiance 0,78 ne décide rien : avec plusieurs castes, l'arbitrage a toujours lieu ; avec une seule, il
  n'est pas possible. C'est conforme à `CONCEPTION.md` (§ 2.5), qui énonce les trois conditions.
- Induction en texte, récompense « Bregman-Tsallis », mémoire spectrale (dimension 16, rang 6), code jamais réécrit
  (successeur = copie et mémoire), lecture de la mémoire la plus récente de l'archive à défaut de mémoire locale.
- Métrique de forme (`metrique/calculer.py`) : elle ne lit jamais la vérité ; un défendeur qui répond faux avec des
  confiances variées et tempérées y obtient une note haute. Six attaques dans son propre vocabulaire d'étiquettes.
- Jetons ASCII seulement dans `mitose_spectrale.py` (« évaluation » y devient « valuation ») ; aucune graine.

## Faits sur le rapport livré (R4)

- `RAPPORT-ORGANISME-GEMINI-v1.md`, § 2 : `1 failed, 2 passed`, `EXIT_CODE=1` ; la passation de Gemini annonce
  « 3 passed, EXIT_CODE=0 ». Le seul échec venait des marques d'ordre d'octets (C-01) : marques retirées, les 3 tests
  passent sans autre changement.
- Le même rapport annonce 18 fichiers et 119 126 octets dans `organisme/` ; le commit `6c61956c` en contient 11, pour
  50 937 octets (compté par `find` et `wc -c` ; les fichiers compilés de la machine de Gemini sont peut-être comptés
  dans son chiffre, non vérifiable ici). Le rapport de Gemini n'est pas modifié.

## Tests

`python -m pytest -q organisme/tests` : 14 passés (les 3 de Gemini, sur le code corrigé, et 11 pour les corrections).

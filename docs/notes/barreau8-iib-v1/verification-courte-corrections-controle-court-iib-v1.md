# Vérification courte des corrections du contrôle court, saboteur à budget (ii-b), tête ff6a9475 — v1

> Même contrôleur que le contrôle court (Claude Opus 5.5, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), sur demande de reprise de la session mère. Code de course **exploratoire, non opposable (R-522)**. Processeur seulement : rien lancé sur une carte, aucune dépense, aucun modèle réel chargé, aucune clé lue. Seul appel réseau : `git fetch origin prep/iib-code-v3 lot/compte-4-v1`. Rien ouvert sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/` du dépôt. Ni commit, ni poussée. J'ai lu la consigne privée par programme : je reste exclu de tout rôle de lecteur des sondes du barreau 8.

## 0. Identité

- Tête vérifiée : `origin/prep/iib-code-v3` = `ff6a947593f7c9f73c96e8055ff2d94a8f2eb02e`. Tête précédente : `a31b8970fedb745c993fe23df18bba4a2d9e3cf4`. Trois commits la séparent de la précédente : `9ded2e76a`, `3fda55e70`, `ff6a94759`.
- Rapport du développeur v5 : `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v5.md`, empreinte `9265eb6cadfadfcc9f169030d28866e6aaad029808d4fed6267e3caef0334351`, égale à celle annoncée.
- Référence : mon contrôle court `docs/notes/barreau8-iib-v1/controle-court-code-iib-v3-v1.md` (`02962a4a…c3a2`).
- Extraction à moi (`git archive` vers `/tmp/ctl-iib-v5/x`), dossiers d'essais et dépôt jouet : tous supprimés à la fin.

## 1. Verdict

**Autorisable après corrections.**

Constats : **0 bloquant, 1 majeur (CC-01, non levé), 1 mineur neuf.**

CC-02 à CC-05 sont corrigés, et leurs essais ne sont pas tautologiques. En revanche, **CC-01 n'est pas levé**. L'essai appelle bien la vraie fonction de progrès, mais avec des arguments écrits dans l'essai. Il n'exerce donc pas l'appel du lanceur. J'ai retiré la correction du lanceur dans ma copie : les deux essais passent encore (`2 passed`), et ils passent aussi une fois la correction remise.

## 2. Constats

| identifiant | gravité | où | constat | correction demandée |
|---|---|---|---|---|
| **CC-01** (suite) l'essai ne lit toujours pas l'appel du lanceur | **majeur** | `tests/test_iib_amorce_v1.py:198-232` ; `src/controle_ia/iib/lanceur_v1.py:292` | `_capturer_progres(etape="epreuves", etat="passees", epreuve="aucune")` appelle la vraie fonction de mise en forme, mais avec des clés fixées **par l'essai**. Le défaut que l'essai doit garder est le choix des clés à l'appel du lanceur (l. 292). Rien n'exerce cet appel. Épreuve : l'ancienne ligne (`echec=…`) remise dans ma copie du lanceur → `2 passed` ; ligne corrigée remise → `2 passed`. Le rapport v5 dit, sans l'avoir éprouvé, que l'essai sain « échouerait » sans la correction : c'est inexact. | Faire passer dans les deux motifs de l'amorce la sortie d'erreur d'un **jeu jouet réel du lanceur**. Par exemple la course jouet de `tests/test_iib_lanceur_v1.py`, avec `capfd`, ou le jeu de `test_iib_consigne_invisible_v1._collecter`, qui rend déjà `sortie`. Exiger au moins une ligne `etape=epreuves` relayée et aucune ligne retenue. Pour l'issue « arrêt » : forcer une épreuve en échec par `monkeypatch` de `tv.epreuves` et relire la ligne émise. Preuve attendue : l'ancienne ligne remise au lanceur → l'essai échoue. |
| VC5-01 sonde de 512 octets : un fichier valide peut être sauté | mineur | `tests/test_iib_exclusion_v1.py:196-200` | Pour savoir si un fichier est textuel, on décode ses 512 premiers octets. Si un caractère accentué est à cheval sur l'octet 512, le décodage échoue et le fichier est sauté sans alerte. Épreuve : fichier UTF-8 valide, `é` sur les octets 511-512, motif réel de rang 1 ajouté plus loin → l'essai sain **passe**. Dans le périmètre actuel, aucun fichier valide n'est sauté : sur 47 fichiers, 41 sont lus, et les 6 autres ne sont pas du texte UTF-8. | Décoder le fichier entier (`read_bytes().decode("utf-8")`), ou décoder avec `errors="ignore"` sur la sonde. Pas exigé avant la course. |

## 3. Les points du contrôle court

| point | état à `ff6a9475` | preuve |
|---|---|---|
| CC-01 | **non levé** (majeur) | Correction retirée → l'essai passe encore. |
| CC-02 | **corrigé** (résidu : VC5-01) | Un motif réel planté en capitales est vu : l'essai sain échoue. Un motif réel planté dans un `.json` de `scripts/` est vu. Un motif planté dans `prereg/config-iib-piege.json` est vu. L'artefact neuf qui plante un triplet appelle `_chercher_fuites`. Fichiers retirés : les 16 essais du fichier passent. |
| CC-03 | **corrigé** | Booléen calculé à part, message sans texte (`test_iib_exclusion_v1.py:125-126`). |
| CC-04 | **corrigé** | L'artefact exige maintenant la fuite dans les contextes de `generer_actions` de l'évaluation. Ce n'est pas tautologique : la collecte passe par l'espion de `generer_actions`, et l'essai sain exige l'absence de fuite dans ces mêmes contextes. |
| CC-05 | **corrigé** | `_verifier_conditions_evaluation` est appelée par l'essai sain (fiches vraies, `ok`) et par l'artefact (fiches falsifiées, `not ok`). C'est la même fonction : la forme reprochée a disparu. |
| CC-06 | laissé | Le rapport v4 reste archivé. Le rapport v5 est fidèle, sauf la phrase de preuve de CC-01 (ci-dessus). |
| CC-07 | déclaré | Une ligne `repetition-jouet-v5/` est ajoutée au `.gitignore`, sans effet sur la course (même raison). |
| CC-08 | relevé | § 5. |
| CC-09 | laissé | Couvert par le contrôle de la mère au rapatriement (contrôle court, § 4). |

## 4. Différence, non-fuite, essais

- **Différence `a31b8970..ff6a9475`**. Sept fichiers :
  - le `.gitignore` (une ligne) ;
  - le rapport v5 et son compagnon ;
  - quatre fichiers d'essais (`test_iib_amorce_v1.py`, `test_iib_consigne_invisible_v1.py`, `test_iib_exclusion_v1.py`, `test_iib_lanceur_v1.py`).

  **Aucun fichier sous `src/` ni sous `scripts/`.** Chaque changement correspond à ce que dit le rapport v5. Le diff n'ajoute ni graine, ni générateur, ni moyenne ni médiane.
- **Non-fuite**. Le script hors dépôt a lu la consigne par `git show`, empreinte `9f8bbdef…90c1` égale à son compagnon. Il a parcouru les 42 fichiers ajoutés ou modifiés par la branche depuis `a3adf4128`, hors les fichiers de consigne, puis les messages des 10 commits de la branche et l'ensemble des lignes ajoutées. Résultats :
  - triplets communs : **0** ;
  - motifs réels à la lettre, sans tenir compte de la casse : **aucun** ;
  - motifs qui trouvent quelque chose : **aucun** ;
  - plus longue suite commune : 2 mots au plus ;
  - plus longue sous-chaîne commune : 10 caractères au plus.

  Validation de la méthode, sur la consigne elle-même : 93 et 10 triplets, et les 9 motifs.
- **Suite ciblée** : **`425 passed in 726.15s (0:12:06)`**, fin à 2026-11-18T21:37:13Z, aucun saut. La durée vient d'un calcul d'une autre session qui tournait en même temps sur la machine ; je n'y ai pas touché. La liste ciblée garde l'empreinte `847676ef…e3b6`. L'essai neuf (424 → 425) est l'artefact du triplet.
- **Répétition jouet** (entropie 20261118, configuration `75b8a4a0…`) : **48 fichiers comparés, 0 différent**, code 0.

## 5. CC-08 : ce que fixe le code et la recommandation du relevé

Simple relevé, sans jugement de fond (le portage relève de Lazar, GO-2026-11-18-56 point 4).

- **Ce que fixe le code** (`src/controle_ia/iib/lecture_v1.py:212-238`, `:299` ; inchangé depuis `a31b8970`) :
  - régression logistique **propre au paquet**, par la méthode de Newton, λ = 1, 100 itérations au plus, tolérance 10⁻¹⁰ sur le pas ;
  - gradient lu **au point rendu**, après le dernier pas ;
  - non-convergence déclarée seulement si le nombre maximal d'itérations est atteint **et** si le gradient maximal dépasse 10⁻¹⁰ × 100 = 10⁻⁸.
- **Recommandation du relevé** (`docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md`, sceau `601bbc84…` vérifié, choix n° 1, recommandation (A)) :
  - appeler les fonctions du contrat de la pièce inscrite, sans recopie ni réglage touché ;
  - solveur de cette pièce : L-BFGS-B, `gtol` 10⁻⁸, 1 000 itérations ;
  - convergence si le gradient maximal **au point rendu** est au plus 10⁻⁴, et coefficients finis (l. 21 et l. 103 du relevé).
- **Accord** : les deux lisent le gradient au point rendu. Le sous-point (g) va donc dans le même sens.
- **Désaccord** : le code n'appelle pas la pièce inscrite. Il garde sa propre méthode, son propre solveur, son propre seuil (10⁻⁸ contre 10⁻⁴) et sa propre condition (atteinte du nombre maximal d'itérations). Sous la recommandation (A), ce chemin de calcul serait remplacé par l'appel à la pièce. Le sous-point (g) du code serait alors sans objet.

## 6. Ce qui reste avant la course

1. **CC-01** : essai sur la sortie réelle d'un jeu du lanceur, avec la preuve « correction retirée → échec ». Ensuite, rejouer la suite ciblée. Le commit qui en sort est celui que citera l'ordre.
2. **Le portage** : aligner le code de la lecture (2) sur la décision de Lazar (§ 5). C'est du code neuf, avec ses essais et un contrôle court.
3. VC5-01, si la mère le juge utile.
4. Les points de la mère, inchangés : forme de la ligne de 7b ; compléments de l'ordre (§ 7, étape 5, heure limite de création, clonage réduit) et rapatriement (contrôle court, § 4) ; puis la suite de l'ordre et du devis.

## 7. Lectures hors mandat, refus

- **Lectures** :
  - le relevé `releve-code-des-deux-bases-v1.md`, que la session mère m'a nommé, réduit à ses choix (l. 28-52) et aux lignes du solveur (l. 21, l. 103). Je n'ai lu aucun code de base ni de moniteur ;
  - `git log` et `git diff` entre les deux têtes ;
  - la liste des processus de la machine, pour expliquer la lenteur de la suite (noms seulement ; rien arrêté).
- **Refus** : aucun.

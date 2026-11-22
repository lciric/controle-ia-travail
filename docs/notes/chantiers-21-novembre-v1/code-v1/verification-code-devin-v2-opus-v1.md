# Vérification des corrections — les épreuves du devin, version 2 (classe B)

- Vérificateur : Opus 5.5, auteur de la contre-lecture `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-devin-opus-v1.md` (sha256 40866478…).
- Lu : le rapport `rapport-code-devin-v2.md` ; la différence complète entre `src/controle_ia/devin_v1/` et `src/controle_ia/devin_v2/` ; les essais `tests/test_devin_v2_admission.py` et `tests/test_devin_v2_admission_garde_c14.py` ; la différence entre les deux scripts de simulations longues.
- Aucun commit, aucun fichier existant modifié, aucun appel réseau.

## Verdict

**Conforme après corrections.** Une seule correction reste. Les dix-huit constats à corriger (C1 à C18) sont fermés, sans effet de bord ; C19 reste renvoyé au concepteur. Les 32 mutations de ma contre-lecture, et trois variantes, sont toutes tuées sur la version 2. En revanche, la vérification du déterminisme fait paraître un défaut que j'avais manqué en version 1 : **l'étage 1 n'est pas déterministe d'un processus à l'autre** (constat V1 ci-dessous). Le défaut est hérité de la version 1, ce n'est pas un effet des corrections. Les essais sont pourtant déterministes, parce qu'aucune de leurs assertions ne lit les coefficients de l'étage 1.

## Écart signalé sur C4 : acceptable

Le développeur ne garde aucune course au hasard, même pour le chemin par défaut. Il remplace la source du système par une source fixe et vérifie que les 13 racines passent par elle (`test_chemin_par_defaut_lit_la_source_du_systeme`). Un second essai vérifie que `tirer_racine` lit bien `os.urandom`, remplacé par des octets fixes (`test_tirer_racine_lit_la_source_du_systeme`). Je juge cet écart **acceptable, et meilleur que ma proposition** :
- le câblage de la source du système est vérifié de bout en bout ;
- aucun essai ne dépend plus du hasard, et tout échec se rejoue (règle R9).

Ce qui n'est plus essayé, c'est l'appel réel à `os.urandom` lui-même : une ligne de la bibliothèque standard, sans risque propre.

## Essais

`PYTHONPATH=src python -m pytest -q tests/test_devin_v2_*.py`, deux passes : **98 passés**, puis **98 passés**. La liste des essais passés est identique entre les deux passes, comparée ligne à ligne. Aucun essai ne tire de l'entropie du système : j'ai cherché `tirer_racine`, `urandom`, `RacineScellee` sans racine et `default_rng()`, et je n'en trouve que les deux emplois remplacés ci-dessus.

Déterminisme des valeurs, hors des essais : j'ai joué la même course deux fois, dans deux processus distincts, avec les racines d'essai. La course a les étages 0, 1 et 2 bis, les cibles A1 et A2, et une fuite « verdict » de 0,2. M et p sont égaux (M = 4,698, p = 0,001), mais **l'empreinte de la famille de la cible A1 diffère**. En cause, les coefficients de l'étage 1 : `LogisticRegression(solver="liblinear")` sans `random_state` lit le générateur global de numpy. C'est le constat V1. Avec la correction ci-dessous, faite dans une copie de mon bloc-notes, les deux verdicts entiers sont identiques à l'octet.

## Mutations rejouées sur la version 2

- **Montage.** Une copie dans mon bloc-notes (`mut2/`) : `src/` et `tests/test_devin_v2_*.py`, avec le `pyproject.toml` du dépôt et un `conftest.py` vide. Les essais sont lancés depuis la racine de la copie, avec `PYTHONPATH` pointé sur elle. Le module chargé est bien celui de la copie : `…/scratchpad/mut2/src/controle_ia/devin_v2/__init__.py`. Le contrôle sans mutation passe (26 essais).
- **Résultat : 35 mutations sur 35 sont tuées.** Ce sont les 32 de la contre-lecture, portées sur la version 2, plus trois variantes :
  - M20b : la course n'emploie plus la règle du test de mort 4 ;
  - M21b : la racine en clair n'est plus cherchée dans le pli d'apprentissage ;
  - M22c : la garde C14 n'est plus appelée.
- **Les neuf survivantes de la version 1 sont tuées** : M13, M15, M17, M20, M21, M24, M28, M29 et M30.
- **M22 est cette fois un vrai déplacement** : le pli d'épreuve est créé avant le scellement. Elle est tuée par la garde elle-même (« racines du pli d'épreuve tirées avant le scellement des familles »), et non plus par une erreur de nom.

## Sort des 19 constats

| Constat | Fermé ? | Vérification |
|---|---|---|
| C1 | oui | `exiger_b_temoin_factice` est appelée avant la course ; refus essayé à B = 199 et à 998 ; règle extraite en `declenchement_mort_4` et employée (M20, M20b tuées). Effet de bord bénin : un verdict « sans objet » est aussi refusé à B < 999, la garde passant avant l'inventaire. |
| C2 | oui | La racine du monde passe par la source, dans `jouer_course` et `admettre` ; elle est consignée en clair au verdict, après la fin ; le script prend `--racine`. |
| C3 | oui | Racines révélées, de rejeu, des prédicteurs et des canaris au verdict, exigées par `valider_verdict` ; l'essai vérifie les empreintes. |
| C4 | oui, avec l'écart accepté | Voir plus haut. |
| C5 = C12 | oui | `test_admission_refuse_un_extracteur_qui_fuit` (M29 tuée). |
| C6 | oui | `test_regle_du_test_de_mort_4` et `test_course_emploie_la_regle_du_test_de_mort_4`. |
| C7 | oui | M13 tuée. |
| C8 | oui | M15 et M17 tuées. |
| C9 | oui | Recherche sur les deux plis, essayée sur les deux (M21, M21b tuées). |
| C10 | oui | M24 tuée. |
| C11 | oui | M28 tuée. |
| C13 | oui | M30 tuée. |
| C14 | oui | Horloge logique de processus (`itertools.count`) ; garde appelée avant le jeu du pli d'épreuve ; M22 et M22c tuées. L'horloge est globale au processus, ce qui suffit, puisqu'on n'y compare que des rangs. |
| C15 | oui | Taux des décisions à 1 ; essai à τ = 0,1. |
| C16 | oui | sha256 du fichier `monde_plante.py` dans l'empreinte. |
| C17 | oui | Champ `puissance_temoin` exigé. |
| C18 | oui | Essai renommé. |
| C19 | renvoyé au concepteur | Inchangé, comme prévu. |

## Correction restante (mot pour mot)

| N° | Gravité | Fichier et ligne | Constat | Correction |
|---|---|---|---|---|
| V1 | moyenne | `src/controle_ia/devin_v2/predicteurs.py:213-215` (même défaut en version 1, `devin_v1/predicteurs.py:212-214`) | `LogisticRegression(solver="liblinear", max_iter=2000)` n'a pas de `random_state` : les coefficients de l'étage 1 dépendent du générateur global de numpy, et donc du processus. Deux processus jouant la même course aux mêmes racines donnent des empreintes de famille différentes. Les sorties, et donc M et p, peuvent différer aussi. La course ne se rejoue donc pas à l'identique (R9), et l'empreinte scellée n'est pas reproductible. | Remplacer `        cv, _ = _cv(graine)` / `        x = self._x(unites, ajuster=True)` / `        g = GridSearchCV(LogisticRegression(solver="liblinear", max_iter=2000),` par `        cv, rs = _cv(graine)` / `        x = self._x(unites, ajuster=True)` / `        g = GridSearchCV(LogisticRegression(solver="liblinear", max_iter=2000, random_state=rs),`. Essai à ajouter dans `tests/test_devin_v2_predicteurs.py` : `def test_etage1_independant_du_generateur_global():` / `    ids_a, ua, ya = donnees(300, [Fuite("verdict", 0.5)], "a")` / `    empreintes = []` / `    for s in (1, 2):` / `        np.random.seed(s)` / `        p = PredicteurEtage1(traits_admis(LB), **OPTIONS["etage1"])` / `        p.ajuster(ua, ya, None, graine_tache(RACINE, "g1"))` / `        empreintes.append(empreinte_objet(p))` / `    assert empreintes[0] == empreintes[1]` (importer `PredicteurEtage1` et `empreinte_objet` depuis `controle_ia.devin_v2.predicteurs`). Vérifié dans ma copie : avec `random_state=rs`, deux processus donnent des verdicts identiques à l'octet. |

## Ce que je n'ai pas fait

- Je n'ai pas appliqué V1 dans le dépôt. J'ai seulement vérifié son effet dans une copie de mon bloc-notes.
- Je n'ai pas relu les fichiers d'essais autres que ceux de l'admission. Pour les autres, je me suis fié aux mutations, qui sont toutes tuées.
- Je n'ai pas lu le script ni la sortie des mutations du développeur (`mutations-devin-v2/`) : j'ai joué les miennes.
- Je n'ai pas rejoué les simulations de taille sous le nul sur la version 2. Le calcul statistique est inchangé : `statistique.py` et `tirage.py` sont identiques à la version 1.

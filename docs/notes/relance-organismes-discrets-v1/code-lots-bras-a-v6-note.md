# Module de construction des lots du bras A — note de code, version 6

- **Objet** : corriger la contre-lecture de la version 5 (`docs/notes/relance-organismes-discrets-v1/contre-lecture-lots-bras-a-v5-v1.md` : un majeur, M-1, et cinq mineurs), sans autre changement de sens. Texte de référence : **brouillon 54** du préenregistrement (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon54.md`, `59ad88f93d84f7cf3acbf11cdf8eecfe61469e7e75e3618dc69c8f2265de45dd`, empreinte vérifiée contre son compagnon). Il a les mêmes numéros de lignes que le brouillon 53 (seules les lignes 1, 3 et 1469 diffèrent, vérifié par différentiel) : toutes les lignes citées par la v5 valent pour le 54.
- **Fichiers neufs** (R12 : `lots_bras_a_v5.py`, ses essais et sa note inchangés ; compagnons `.sha256`, R6) :
  - `src/controle_ia/organismes_discrets/lots_bras_a_v6.py` (1116 lignes) ;
  - `tests/test_lots_bras_a_v6.py` (85 essais : les 81 de la v5, dont deux adaptés, et 4 neufs).
- Point de départ : `lots_bras_a_v5.py` (`75ce3176…`). Processeur seul, aucun réseau, aucune dépense, rien committé ; aucune pièce cloisonnée ouverte. Graines inchangées (R9).

## Corrections

| point | correction | code (v6) | essais |
|---|---|---|---|
| **M-1** — relevé des actions relues forgeable sous 80, pris par le lot décisif (ligne 846 ; garde 1184) | (1) `Releve` n'admet que les planchers du texte, `PLANCHERS_DES_RELUES` = 80 pour « honnetes » et 80 pour « deplacees-a-effet », et eux seuls ; comptes : exactement ces deux clés, entiers, à 80 ou plus. (2) `lot_decisif` refuse de lui-même toute classe sous 80, aux lots en vigueur ou au relevé, **quoi que porte le relevé** (ceinture et bretelles : jouée même pour un relevé construit sans passer par son constructeur) | `Releve.__post_init__` ; `PLANCHERS_DES_RELUES` (l. 792) ; garde du lot décisif (l. 933) | `test_releve_planchers_du_texte_seuls` (sain : 80/80 ; artefacts : le relevé forgé de la contre-lecture — 70 et 10, planchers à zéro —, planchers 79 ou 81, clé en plus ou en moins aux comptes ou aux planchers, compte non entier) ; `test_lot_decisif_refuse_toute_classe_sous_80` (sain : 80/80, relevé du module et relevé forgé hors constructeur mais exact, mêmes octets ; artefacts : 70/10, 79/200, 200/79, 79/79, planchers à zéro ou à 80, relevé forgé hors constructeur — refusé « sous 80 » ; de même sous la révision) |
| **m-1** — `DonneusesTenues` constructible à la main | ne se construit que par `garde_de_l_action_donneuse` | `_fabriquer` (l. 215), `_exiger_fabrique` (l. 225), `DonneusesTenues.__post_init__` (l. 417) | `test_constat_et_temoin_construits_par_le_module_seul` (sain : témoin rendu par la garde, accepté par la couverture ; artefacts : témoin identique construit à la main, `dataclasses.replace`) |
| **m-2** — `Constat` d'effectif constructible à la main | ne se construit que par les fonctions du module | `Constat.__post_init__` (l. 251) ; les quatre sites de construction passent par `_fabriquer` | même essai (constat construit à la main, même bien formé ; `dataclasses.replace` d'un constat du module ; drapeau retombé après un appel, même en erreur) ; `test_constat_mal_forme_refuse` passe désormais par `_fabriquer` |
| **m-3** — `ancre_jumeaux` rend le constat de la première partie | aucun changement de code. **À écrire en clair** : quand l'ancre sur plans honnêtes est à effectif insuffisant, `ancre_jumeaux` rend **le constat de la première partie lui-même** (ligne 812 : « celui de l'ancre sur plans honnêtes en tenant lieu »), non un constat propre. Un lanceur qui inscrit les deux retours (ancre 1 puis ancre 2) inscrit ce même constat deux fois : l'inscription est idempotente (une seule clé `effectif-insuffisant/ancre-plans-honnetes` au manifeste), mais **le rapport ne doit compter qu'un constat**, non deux | inchangé | `test_ancre_jumeaux_non_jouee_si_premiere_partie_insuffisante` (rend `is kp` ; manifeste à une seule clé) |
| **m-4** — brouillon 53 cité | en-tête du module et note citent le brouillon 54 (`59ad88f9…`) ; les numéros de lignes, identiques, sont gardés | en-tête | — |
| **m-5** — sortie de la garde statique | sortie brute donnée ci-dessous, non filtrée | — | — |

**Limite déclarée (m-1, m-2)** : la construction réservée tient par un drapeau de contexte (`contextvars`) levé le seul temps de `_fabriquer` ; aucun champ n'est ajouté à l'objet, d'où octets, empreintes et égalité inchangés. Python ne ferme pas tout : `_fabriquer` (nom privé) appelé du dehors, `object.__new__` suivi de `object.__setattr__`, ou `copy.copy` d'un objet du module contournent la garde. Elle ferme la construction à la main et `dataclasses.replace`, ce que relevait la contre-lecture. `Releve` reste constructible du dehors (essais de la v5 et de la v6 s'en servent pour les comptes autres que ceux des lots) ; il n'admet plus que les planchers du texte, et le lot décisif rejuge lui-même le plancher. `ConstatDArret` reste constructible : sa garde de forme est inchangée.

## Octets qui changent par rapport à la v5

**Aucun**, vérifié par `test_octets_egaux_a_la_v5` : lot honnête de l'appariement à 576, 128, 64, 63, 40 et 30 actions (constats portés compris), ancre sur plans honnêtes et ancre des jumeaux (lot ou constat), témoin de la garde de l'action donneuse, lot honnête de la couverture (complet et en constat), lot mécanique (complet et plan tronqué en constat), relevé ou constat des actions relues à 576/192, 80/80, 79/200, 160/200, lot décisif avec couverture lue, et lignes du manifeste. Les essais repris de la v5 contre la v4 (`test_octets_changes_par_rapport_a_la_v4`) passent tels quels. Seul change le comportement sur les entrées refusées : relevé à planchers autres que 80 ou à clés autres, constat ou témoin construit hors du module, lot décisif avec une classe sous 80 par un relevé forgé.

## Commandes et sorties

    $ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v4.py tests/test_lots_bras_a_v5.py tests/test_lots_bras_a_v6.py tests/test_graines_bras_a_v4.py
    322 passed

Garde statique du cloisonnement (`cloisonnement_bras_a_v13.violations_de_la_garde_statique(Path('.'))`), **sortie brute** : une violation, hors de ce module et préexistante —

    scripts/chef_essais_admission_bras_a_v2.py, ligne 508 : fragment du nom du fichier des rangs par unité dans une chaîne

Aucune violation sur `lots_bras_a_v6` (filtre `'lots_bras_a_v6' in v` : `[]`).

Campagne de mutations **sur une copie** (bloc-notes de la session, `mutations_lots_v6.py`, arbre `mut6/` : `src/`, `pyproject.toml`, `tests/conftest.py` et les essais v6 copiés ; chaque mutant écrit dans la copie seule, copie restaurée à la fin, empreinte du module du dépôt confrontée avant et après) : les 57 mutants de la v5 portés à la v6 (deux réécrits sur les lignes changées : « relevé sans garde de compte », « relevé plancher 79 »), et 16 neufs (12 pour M-1, 4 pour m-1 et m-2).

    73 mutants : 70 tués, 3 survivants ; copie restaurée ; module du dépôt intact (6075b55eefde31c0…)

Survivants, tous **équivalents**, déclarés :
- « sentinelles tirées à 2 » (repris de la v5, même raison : tirer deux pas parmi deux donne le même ensemble, aucun tirage ne suit sous la clé ; lot assemblé trié).
- « M-1 : relevé jugé sur ses propres planchers » (`self.planchers[k]` au lieu de `PLANCHERS_DES_RELUES[k]`) : la clause qui précède exige `dict(self.planchers) == PLANCHERS_DES_RELUES`, les deux valent 80.
- « M-1 : garde du lot décisif sur la borne de 160 » (`n < 80`, forme proposée par la contre-lecture) : `n = min(honnêtes, déplacées, 160)` est sous 80 si et seulement si une classe l'est, et les comptes du relevé ont déjà été confrontés, égaux, à ceux des lots.

Mutants neufs tués : planchers du relevé libres (forme v5) ; clés des comptes non contrôlées ; contrôle d'entier retiré ; plancher des relues à 79 et à 81 ; garde du lot décisif retirée, à `<=`, sur les seuls honnêtes, sur les seuls déplacés ; refus après constat retiré ; constat constructible à la main ; témoin constructible à la main ; drapeau jamais rabattu ; drapeau levé par défaut.

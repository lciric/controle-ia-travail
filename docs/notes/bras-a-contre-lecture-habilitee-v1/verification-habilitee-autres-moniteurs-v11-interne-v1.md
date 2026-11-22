# Vérification habilitée du module des autres moniteurs, version 11 — pièce interne — v1

Écrit le 2026-11-22 vers 14:25Z par un lecteur habilité neuf (Claude Opus 5.5), sous le mandat `docs/notes/bras-a-contre-lecture-habilitee-v1/mandat-lecteur-habilite-module-v11-et-renvoi-base-v1.md` (`7854c2e5c39345d16c48d72cce06fef5d4cc5815b213835d38e98aa80488f63e`, sur la branche principale), partie 1 ; accès inscrit au registre des décisions, ligne R-4887. Pièce interne : elle ne sort pas de la branche habilitée. Classe B (instrument).

## Objet et empreintes vérifiées

Arbre de travail détaché au commit `e13ed9282` de `claude/bras-a-habilite-developpeur-v1` ; chaque empreinte recalculée avant lecture.

| pièce | empreinte | état |
|---|---|---|
| `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v11.py` | `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` | conforme, compagnon égal |
| `tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py` | `92711976e9ee949b08719b791cafc53932763ab96a04b6c01d34b0068cc3c776` | conforme, compagnon égal |
| `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py` | `c0021298c21d027a713b1947d2668ac928f2a856b1a696686dd35b83a9515c45` | conforme, compagnon égal |
| `…/autres_moniteurs_v10.py` | `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` | égale à celle du commit `d5602cd57` ; inchangée de `d5602cd57` à `e13ed9282` |
| `docs/notes/bras-a-moniteurs-v1/verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md` | `cb23f4efaec9923489d2d8b2098663919440815025e07088bb336e6bd8792fa0` | conforme |
| brouillon 46, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md` (branche `claude/pensive-bardeen-1fv7hw`) | `b5e1031c9b92d7643815e9d18abec86f900fee0931eb6030839729b2f32c3fb9` | conforme ; seule la ligne 1473 lue |

Écart de chemin, sans effet : la case de la ligne 1473 range la vérification habilitée de la v10 sous `docs/notes/bras-a-sans-interne-v1/` ; sur la branche habilitée, elle est sous `docs/notes/bras-a-moniteurs-v1/`, à la même empreinte. La case donne la bonne empreinte ; seul le dossier diffère. À corriger dans le texte au prochain brouillon, sur la seule ligne.

## Verdict : conforme

**« De la version 10 à la version 11, seule change l'empreinte inscrite de la préparation » : vrai.**

### 1. Différentiel complet v10 → v11

`diff -u autres_moniteurs_v10.py autres_moniteurs_v11.py` : deux morceaux, et eux seuls.
- Lignes 10 à 15 de la v11 : un paragraphe neuf « Version 11 » dans la docstring du module (six lignes, dont une vide). Il ne s'exécute pas.
- Dans `PROGRAMMES_DE_PRODUCTION["preparation_des_lectures"]`, le couple (chemin, empreinte) passe de `…/preparation_des_lectures_v2.py`, `6dfd2bfc…` à `…/preparation_des_lectures_v3.py`, `c0021298…`. L'empreinte inscrite est celle du fichier v3 recalculée ici.

Aucune autre ligne ne change : aucune fonction, aucune constante, aucune garde. Le corps du différentiel est identique, caractère pour caractère hors en-têtes, à celui que le développeur a versé (`docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v10-a-v11.diff`, `b7ac6de62b8e0c7c5c8619dd29cd7af2b56a6b07fe2cfba27e15639fb4a19d0a`, l'empreinte que cite la case). Le chemin change avec l'empreinte : c'est le même couple inscrit. La case dit « l'empreinte inscrite » ; je l'entends ainsi.

Effet de ce changement, vérifié dans le code : `empreintes_des_programmes` et `exiger_programmes` exigent maintenant la préparation v3. Un manifeste de production qui porte la préparation v2 est refusé par la v11 (« ≠ inscrites »), et un manifeste écrit avec la v11 est refusé par la v10. La v10 reste en place pour la v2 (R12). `empreinte_du_module()` se calcule sur `__file__` ; aucune référence à la v10 ne reste dans le corps de la v11.

La préparation v3 est lue en entier : aucun tirage, aucun sous-échantillon (pas de `random`, ni de `rng`, ni d'échantillon) ; le juge lit toutes les actions, comme le dit la case (reste (e)).

### 2. Essais

Rejoués avec le `.venv` de la mère en lecture seule et `PYTHONPATH=<arbre>/src` :
- **essais de la v11** : `4 passed` sur 4 ;
- **essais de la v10 inchangés, au commit `e13ed9282`** : 76 sur 77. Le seul échec, `test_garde_statique_du_paquet`, vient de la présence du fichier v11 dans le paquet : la liste figée des modules permis à charger un fichier par son chemin (`CHARGEMENT_PAR_CHEMIN_PERMIS`) s'arrête à la v10. Ce n'est pas un défaut de la v11 : la v11 hérite de la v10 le même chargement de la pièce source, et les essais de la v11 rejouent cette garde avec la liste étendue (`test_garde_statique_du_paquet_avec_la_version_11`, qui passe). Les essais de la v10 ne sont pas récrits (R12). À savoir : rejoués seuls à cette tête, ils rendent cet échec ;
- **essais de la v10 transposés sur la v11** (copie temporaire, retirée des essais après usage et versée en texte, `verification-habilitee-autres-moniteurs-v11-v1/essais_v10_transposes_sur_v11.py.txt`, dans laquelle l'import, les trois chemins du module et la liste des chargements permis nomment la v11) : **`77 passed` sur 77**. C'est l'épreuve directe que tout ce que les essais de la v10 éprouvent tient pour la v11, préparation v3 comprise.

Les essais de la v11 éprouvent seulement la différence : ils renvoient au reste aux essais de la v10 et au lanceur. La transposition ci-dessus comble cet écart pour cette vérification. Recommandation sans urgence : verser un tel fichier d'essais au développeur, pour que la v11 ait sa suite complète à elle.

### 3. Épreuve par retrait

Procédé de la v10 : `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-autres-moniteurs-v10-v1/passage_mutations_v10.py` (compagnon conforme). Chaque garde visée est retirée seule, les essais qui la visent sont joués, et le module est remis à son empreinte après chaque retrait. **Rejoué sur la v11**, avec trois changements et eux seuls : le module visé est la v11 ; les essais joués sont la suite v10 transposée sur la v11 ; et deux retraits propres à la v11 sont ajoutés, joués sur les essais de la v11. Ces deux retraits remettent dans `PROGRAMMES_DE_PRODUCTION` l'empreinte, puis le chemin, de la préparation v2.

Résultat : **69 retraits listés, 67 joués, 67 mordent** (les 65 de la v10 et les 2 de la v11), et **2 non joués**. Ces deux-là, « preuve d'ordre » et « comptes des lectures », sont des retraits hérités de la v9 dont le texte a été remplacé en v10. Le relevé de la v10 les marque de même : ils sont couverts par les retraits « comptes : … » et « preuve : … » de la v10, qui mordent. Le module est remis à `e1130dad…` à la fin. Le relevé, l'outil adapté et la suite transposée sont versés à côté de cette pièce (dossier `verification-habilitee-autres-moniteurs-v11-v1/`).

### 4. Épreuve de forme

Procédé de la v10 : `scripts/bras_a_v2_habilite_epreuve_de_forme_v10_v1.py` (compagnon conforme). **Rejouée sur la v11** : même script, seul l'import du module change (et le préfixe d'un dossier temporaire). Six sorties : les cas A à E et l'artefact de la valeur p arrondie. Chaque sortie porte un seul nombre par dose dans les deux champs de l'agrégateur, et `null` au cas B. Les cinq fichiers par unité sont **identiques octet pour octet** à ceux versés pour la v10.

Comparaison champ par champ avec les sorties versées pour la v10. Les lectures, les réglages, les plis, les champs de l'agrégateur, `exclues`, `scores_par_unite` et `nombres_rendus` sont identiques. Seuls diffèrent :
- (a) `piece_source.sha256`, l'empreinte du module, attendue ;
- (b) `piece_source.production.<moniteur>.preparation_des_lectures`, la v3 au lieu de la v2, attendu ;
- (c) `preuve_d_ordre` (dates du journal, empreintes des scores, engagement de la table) et les comptes de `comptes_des_lectures`.

Le point (c) n'est pas lié à la version. Le script tire à chaque passage une table neuve d'identifiants opaques, depuis l'entropie du système, et les états de balise sont affectés dans l'ordre de ces identifiants ; le journal est daté au passage. **Témoin** : le script de la v10, inchangé et rejoué ici, diffère de ses propres sorties versées sur les mêmes rubriques (c), et sur elles seules. La v11 n'ajoute donc que (a) et (b). L'épreuve de forme de la v10 vaut pour la v11, et sa reprise le montre.

### 5. Ce qui reste, hors de cette vérification

- La configuration de l'analyse doit citer la v11 (`piece_source.sha256` = `e1130dad…`), comme le dit la case ; ce n'est pas vérifié ici.
- L'attestation de la v7 à la v10, écrite par le développeur, n'est pas jugée ici (reste (a) de la case).

Cette pièce ne dépense rien et n'autorise rien.

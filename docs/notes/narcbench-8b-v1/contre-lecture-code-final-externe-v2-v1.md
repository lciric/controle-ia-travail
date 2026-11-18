# Contre-lecture du code final du bras externe NARCBench v2 (nos sondes et la recette des auteurs sur les activations publiées), tête finale — v1

- **Contre-lecteur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5),
  même famille (N-052) ; agent distinct du contre-lecteur du code v2. Je n'ai écrit ni ce code, ni le texte court du barreau 7,
  ni leurs contre-lectures ; je ne serai ni lecteur ni juge du verdict. Travail du 2026-11-18, de ≈ 19:40 à ≈ 20:50 UTC.
- **Mandat** : `docs/notes/narcbench-8b-v1/mandat-contre-lecture-code-final-externe-v2-v1.md` (`fa590009…`, compagnon vérifié :
  OK), sous GO-2026-11-18-30.
- **Objet lu** : arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2`, **tête finale
  `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`** (égale à la tête de l'arbre, arbre propre). Lue dans une extraction à moi
  (`git archive`). Dans l'arbre du développeur : seulement des commandes git de lecture ; rien n'y a été modifié.
- **Aucun score calculé ni lu sur les données réelles. Aucun fichier de données réelles ouvert**, pas même par l'essai de
  forme (non rejoué). Tous mes calculs ont tourné sur des données factices.
- **La contre-lecture s'est arrêtée au premier refus d'un outil** (section « Arrêt au premier refus d'un outil ») : le refus
  est tombé à la fin, sur une attente. Les six points du mandat étaient lus ; je n'ai plus rien lancé ensuite.

## Verdict

**Autorisable après corrections.** Aucun bloquant. Deux majeurs, **tous deux sur les essais** : aucun module de la lecture
n'est à changer (le texte l'exige : section « Code », écart restant n° 2).

Le code fait ce que le brouillon 3 dit qu'il fait. Je l'ai vérifié par un recalcul indépendant des cellules (44 comparaisons,
écart au plus 2 × 10⁻¹⁶), par un essai du câblage de la réponse sur des cellules fabriquées, et en appelant à la main les gardes
sans essai. Ce qui manque est du côté des essais : (M1) rien n'y fixe la valeur des cellules qui décident la réponse au
barreau ; (M2) deux conditions de la garde du registre n'ont pas d'essai sur artefact, ce que le plan d'analyse n° 1 du texte
interdit avant la ligne de code.

## Arrêt au premier refus d'un outil (texte exact)

Vers 20:31 UTC, j'attendais la fin de mon dernier lot de mutations. L'outil de commande a refusé :

> Blocked: sleep 240 followed by: tail -n +14 /tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/tasks/btgtizhyl.output cut -c1-330 date -u +%H:%M:%S. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.

Ce que j'ai fait ensuite, et rien d'autre : je n'ai ni reformulé ni contourné (aucune autre attente, aucun des moyens que le
message propose) ; je n'ai plus lancé aucun essai ni aucune vérification ; j'ai lu une fois, en l'état, la sortie du lot
déjà lancé (20:33:15 UTC, quinze issues sur vingt) ; j'ai cherché trois motifs dans le brouillon 3 (lecture seule) ; puis
j'ai rédigé, scellé et nettoyé. Pendant la rédaction, l'outil m'a notifié de lui-même que le lot avait fini (20:38:01 UTC,
code 0) ; j'ai alors lu la fin de sa sortie (lecture seule) : les cinq dernières issues sont dans ce rapport.
**Ce rapport rend l'état de la contre-lecture à l'arrêt ; à la mère de dire s'il suffit.**

Ce qui n'a pas été fait à cause de l'arrêt : rejouer `prereg.problemes` sur une copie du brouillon 3 aux trois marqueurs
remplis ; écrire les sorties de mes scripts dans des fichiers (elles sont recopiées ici depuis la session).

## Ce que j'ai fait (preuves)

1. **Empreintes** : mandat, brouillon 3 (`fae8a96c…`), première contre-lecture du code (`9b90884a…`), et les pièces du
   développeur à la tête finale (rapport `40fbdc70…`, relevé des cinq points de recette `8be99220…`, manifeste des données v2
   `43106834…`, relevé des licences `ba780896…`, sortie de l'essai de forme `61cc1313…`, six pièces de `pieces-externe-v2/`) :
   chaque compagnon vérifie.
2. **Différence entre les têtes**, commit par commit et fonction par fonction (point 1 ci-dessous).
3. **Les 168 essais rejoués** dans mon extraction : `168 passed in 65.36s`. J'ai vérifié par un essai-sonde que c'est bien
   mon extraction qui est chargée (`controle_ia`, `lecture_externe_v2`, `cellules_externe_v2`, `externe_v2`, `sondes.familles`)
   et que scikit-learn vient du dossier épinglé (`sklearn.__version__` = 1.9.1). Répartition : 16 (cellules), 13 (chargeur),
   3 (bras externe v1), 35 (bras externe v2), 8 (forme), 69 (commande de lecture), 24 (module v1).
4. **Oracle des auteurs** : les fonctions `_auteurs_*` de `tests/test_narcbench_externe_v2.py` sont **identiques** à celles de
   la tête `70cb77b8` (comparaison par arbre syntaxique ; seule différence : `import warnings` remonté en tête de fichier), que
   la première contre-lecture avait comparées au vrai script par exécution. J'ai en plus comparé la recopie aux 30 lignes du
   script citées par le relevé `8be99220…` : conformes, une à une. Je n'ai pas retéléchargé le script (interdit par ma
   consigne).
5. **Épreuve par mutation du développeur rejouée** sur mon extraction, à la tête finale : témoin et onze mutations tuées,
   chacune par l'essai que nomme le tableau.
6. **Mon épreuve par mutation**, indépendante (copie entière de `src/`, option `-o pythonpath=<copie>/src`, greffon qui
   imprime le fichier chargé) : un témoin, 4 mutations de la recette, 26 de la commande de lecture, 18 des cellules, et le
   rejeu de deux mutations du développeur (tables en M1 et aux points 2 et 3).
7. **Recalcul indépendant des cellules** sur un jouet non saturé (aires de 0,45 à 0,95) : aires par couche, estimation,
   intervalle, plancher et placebo des cellules visées de nos trois familles ; plancher, intervalle et placebo du témoin ;
   cellules des comités de nos deux familles co-principales (pli tenu à l'écart, maximum des trois messages, intervalle par
   plis). **44 comparaisons, 0 écart** (au plus 1,67 × 10⁻¹⁶). Mes aires viennent de `roc_auc_score`, mes boucles sont
   explicites ; je n'appelle aucune fonction du module contre-lu.
8. **Gardes sans essai d'artefact appelées à la main** (G1 à G9, détail en M2 et dans les mineurs) : huit essais verts.
9. **Repli du plancher à travers la lecture d'un modèle** (liste d'arrêt n° 10) : quatre scénarios (sain ; Cholesky refusée
   partout ; refusée une fois sur deux ; Cholesky et repli refusés). La lecture va au bout, le résultat est du JSON standard,
   les phrases sont celles du texte (« plancher par tirage équivalent en loi », « sans plancher »).
10. **Câblage de la lecture finale** sur des cellules fabriquées : neuf cas, les six lignes R0 à R5 atteintes comme le texte
    les définit, douze qualificatifs de plancher dans R1, huit cellules des familles co-principales : conforme.
11. **Texte et code** : contrôle par programme des phrases gelées rejoué (39 phrases, 0 écart) ; `verifier-texte` rejoué sur
    le brouillon 3 et sur une copie (point 4).
12. **Fiche du code** : sortie de la commande `fiche-code` à la tête finale, recoupée par `sha256sum` ; compte des tâches.

## Réponses aux six points du mandat

### 1. Différence entre la tête lue (`70cb77b8`) et la tête finale (`fe9d7996`)

**Chaque changement se rattache à une remarque ou à un écart demandé ; je n'ai rien trouvé d'autre.** Six commits, 21 fichiers.
Dans `src/` : quatre fichiers seulement (`__init__.py`, `cellules_externe_v2.py` neuf, `externe_v2.py`,
`lecture_externe_v2.py`). `requirements-cpu.txt`, le chargeur, `externe_v1.py`, `statistiques_v1.py` : inchangés.

| commit | ce qu'il change | rattaché à |
|---|---|---|
| `3950ee93` | `externe_v2`, `lecture_externe_v2` et leurs essais | majeurs M1 à M3 et mineurs de la première contre-lecture ; gardes n° 2, 3, 4, 6 à 10 du texte |
| `2e02c7eb` | `cellules_externe_v2` (neuf), `externe_v2`, `lecture_externe_v2`, `__init__`, essais | écarts 13 à 18 du brouillon 2 ; écarts A19 à A30 de la contre-lecture 2 du texte |
| `cde3b990` | relevé des lignes du code des auteurs (pièce) | cinq points de recette (demande de la mère) |
| `950e5d3c` | un essai (écart 16) | lecture des comités : séquence des trois messages et maximum |
| `b46c678d` | épreuve par mutation corrigée, script du jouet (pièces) | huit mutations survivantes de la première contre-lecture |
| `fe9d7996` | phrase gelée R1 et son essai ; contrôles ; sortie du jouet | écart restant n° 1 du brouillon 3 |

Recette des auteurs, fonction par fonction : `lignes_apprentissage`, `scores_episodes`, `etiquettes`, `DirectionAuteurs`,
`_exiger_couche`, `exiger_augmentation`, `_sklearn` sont **identiques**. `apprendre_direction` : le tirage équilibré passe
dans `lignes_equilibrees`, mêmes lignes (il sert aussi au plancher du témoin). `groupes` : exclusion de l'agent sans
exactement trois lignes (liste d'arrêt n° 9, déclarée ; les auteurs le moyennent) et garde du mode entre lignes.
`validation_domaines`, `evaluation_stego`, `reproduire_helios_v2` : `None` au lieu de `NaN`, garde des scores constants,
scores gardés pour les cellules, exclusions. Aucun changement de la recette elle-même.

**Entre la tête lue par le brouillon 3 (`cde3b990`) et la tête finale**, un seul module change : `cellules_externe_v2.py`,
9 lignes, la phrase R1 et sa documentation. C'est exactement ce que le texte permet.

### 2. Essais

168 verts (preuve 3). **L'essai-oracle recopie toujours la recette des auteurs à la lettre** (preuve 4). L'égalité est
exigée **au bit près** : `==` sur les aires et l'erreur type, `numpy.array_equal` sur la direction et le `scaler`, y compris
dans le régime où l'arrêt à 8 itérations agit (largeur 2 000). Mes mutations de la recette sont tuées par des essais de
comportement :

| mutation (lot A) | état | essai qui la tue |
|---|---|---|
| A0 témoin : exception en tête de `cellules_externe_v2` | tuée (message vu) | collecte de `test_narcbench_cellules_externe_v2.py` |
| A1 arrêt à 8 itérations → 100, essai de comportement seul | tuée | `test_oracle_regime_non_converge_l_arret_a_8_iterations_agit[papier]` |
| A2 tolérance 0,03 → 0,3, essai de comportement seul | tuée | `test_garde_de_reproduction_v2_tolerance_a_la_borne` |
| A3 C = 25 → 1 | tuée | `test_oracle_transcription_egalite_au_bit[papier]` |
| A4 ordre des classes dans l'ajustement du `scaler` | tuée | `test_oracle_transcription_egalite_au_bit[code]` (le cas « papier » passe : à écrire, sans portée) |

### 3. Gardes (règle R5 : un cas sain et un artefact par garde)

| n° | garde | cas sain | artefact | constat |
|---|---|---|---|---|
| 1 | taille, empreinte des huit fichiers | lecture de bout en bout | `test_donnees_arretent…[empreinte]`, essais du chargeur | tenu |
| 2 | étage de transfert | idem | `[transfert]` ; `groupes(…, "TRANSFER")` | tenu (ma mutation B15 tuée) |
| 3 | registre, texte cité | idem | 20 cas de la table `CAS` | **deux trous sur la ligne `CODE-NARC-EXT` : M2** |
| 4 | déjà jouée | idem | ligne de lecture, dossier de run, résultat ; relance refusée | tenu (B04 à B06 tuées) |
| 5 | configuration | idem | 21 cas | tenu (B07 à B09, B19, B23 tuées) |
| 6 | code exécuté égal au code de la fiche | idem | racine, arbre modifié, commit absent, non ancêtre, liste, empreinte, paquet différent | tenu (B10 à B12, B20, B22 tuées) |
| 7 | scikit-learn 1.9.1 | idem | installé absent ou autre ; fiche autre | tenu (B13, B14 tuées) |
| 8 | forme | essais sains | métadonnées (chargeur, rôles, mode, deux colludeurs) ; activations (couche, type, largeur, lignes, non finies, ligne finale en double, direction nulle, aucune valeur) | tenu (B16 tuée) ; cas de bord : m2, m3 |
| 9 | exclusions, seuil de 10 % | 10 % exactement passe | 15 % arrête ; par la commande, avant le manifeste | tenu (B17 tuée) |
| 10 | repli du plancher | Cholesky | repli, puis sans plancher ; même loi | tenu pour la lecture par agent et la cellule ; **à travers `lire_modele` : aucun essai** (éprouvé à la main, preuve 9 ; joint à M1) |
| 11 | mémoire | — | `MemoryError` factice, code 1, ligne d'arrêt | tenu (B25 tuée) |
| 12 | scores non finis, constants ; valeur non finie au résultat | — | arrêt ; cellule « non lu » ; arrêt après ouverture sans résultat | tenu (B18 tuée) |

Les n° 13 à 16 sont des règles de conduite, sans code.

**L'épreuve par mutation corrigée charge bien le code muté.** Trois preuves : la mutation témoin du développeur rejouée
(collecte en erreur) ; mon propre témoin sur un autre module (`RuntimeError: copie mutee chargee (contre-lecteur)` levée
depuis la copie) ; la contre-épreuve : la même copie mutée **sans** l'option `-o pythonpath` donne `16 passed`, donc le
fichier `pyproject.toml` charge bien le code non muté quand on l'oublie, comme la note du développeur le dit. Mon greffon a
relevé, à chaque mutation, le fichier chargé : la copie.

**Les onze mutations du tableau sont tuées par l'essai nommé**, à la tête finale. Deux précisions : (a) pour E01 (arrêt à 8
itérations) et E07 (tolérance), l'essai nommé est celui qui recopie la constante, premier à échouer ; les essais de
comportement les tuent aussi (A1, A2) ; (b) l'outil du développeur ne copie que `narcbench/` et lie le reste par des liens
symboliques (m4) : j'ai donc rejoué L01 et L02 en copie entière (C24, C25), tuées par le même essai. L01 : la garde
retirée, le code casse (`ValueError`, dépaquetage). L02 : le refus tombe quand même, par le contrôle du sceau ; l'essai la
tue sur le motif attendu. Mon lot B (copie entière) confirme les gardes de la commande, motif de l'échec affiché :

| mutation (lot B, `lecture_externe_v2.py`) | état | essai qui la tue (motif) |
|---|---|---|
| **B01 sceau de la fiche du code non vérifié** | **survivante** | 168 essais verts |
| **B02 antériorité à l'ouverture vérifiée pour la seule ligne de scellement** | **survivante** | 168 essais verts |
| B03 ligne de code « postérieure ou égale » | tuée | `[code_au_meme_instant]` (0 au lieu de 2) |
| B04 garde « déjà jouée » retirée | tuée | lecture de bout en bout (0 au lieu de 2) |
| B05, B06 dossier de run, résultat non regardés | tuées | `[run_deja_ouvert]`, `[resultat_deja_ecrit]` |
| B07 entropie non comparée ; B08 minimum 2³¹ | tuées | `[entropie_sous_chaine]`, `[entropie_petite]` |
| B09 unicité de la ligne de clé | tuée | `[cle_hors_section_aussi]` |
| B10 ancêtre non exigé ; B11, B12 paquet exécuté non comparé | tuées | `[commit_non_ancetre]`, `[code_execute_different]`, `[paquet_execute_en_plus]` |
| B13, B14 scikit-learn installé, de la fiche | tuées | `test_scikit_learn_installe…`, `[scikit_learn_de_la_fiche]` |
| B15 transfert ; B16 rôles ; B17 seuil d'exclus, avant le manifeste | tuées | `[transfert]` ; `[colludeurs]` et `[exclusions]` (un manifeste paraît : la garde tardive ne suffit pas) |
| B18 valeur non finie ; B19 texte cité, option, registre | tuées | `test_valeur_non_finie…` ; `[texte_de_la_section_autre]` |
| B20 arbre modifié ; B21 gabarit ; B22 empreintes de la fiche | tuées | `test_arbre_de_travail_modifie_arrete` ; `[texte_non_conforme]` (1 au lieu de 2) ; `[fiche_empreinte_fausse]` |
| B23 date impossible ; B24 code 1 pour un refus ; B25 mémoire ; B26 autre clé | tuées | `[run_date_impossible]` ; `[scellement_absent]` ; `test_memoire…` ; `[autre_cle_refusee]` |

### 4. Texte et code

- **Phrases gelées** : contrôle par programme rejoué contre le brouillon 3 (`fae8a96c…`) : `39 phrases gelées du code
  comparées au brouillon 3 : 0 écart(s)`. J'ai relu à la main R0, R2 à R5 et F2 à F5 : identiques. R1 est fixée mot pour mot
  par `test_phrases_gelees_textuelles`.
- **`verifier-texte`** : sur le brouillon 3 tel quel, code 2, un seul motif (la valeur d'entropie, laissée à la mère) ; sur
  une copie où **seule** la ligne `Entropie : <<ENTROPIE_NARC_EXT>>` est remplacée par un entier d'essai, **code 0**, six
  lignes lues (papier ; bande 26 à 30 et 32 à 37 ; forme du run ; registre ; texte ; entropie). Cette commande ne lit que la
  configuration (G9) ; la conformité au gabarit et les marqueurs relèvent de `prereg.sceller_prereg`. Le brouillon 3 porte
  bien trois marqueurs et aucun « À REMPLIR » ; l'entrée « Contre-lecture 3 » devra citer deux empreintes distinctes, sinon
  le scellement et la garde n° 3 refusent.
- **Codes de sortie** : 2 pour les refus n° 3, 4 et 5 ; 1 pour les autres arrêts ; 0 au bout : tenus par les essais (B24).
  Réserve : m1.
- **Numérotation de la liste d'arrêt** : celle du code (n° 1 à 12) est celle du brouillon 3, égale à celle du brouillon 2
  (les seize intitulés comparés). Les n° 13 à 16 n'ont pas de code.
- **Ordre des gardes** dans `lire` (`lecture_externe_v2.py` l. 541-557) : n° 3, 5, 6, 4, 7, 2, 1, puis 8 et 9 sur les
  métadonnées, puis le manifeste : celui du texte.
- **Refus sans texte scellé ni clés** : tenu (`scellement_absent`, `code_absent`, `registre_absent`, `sceau_faux`,
  `texte_non_conforme` : code 2, rien d'écrit hors du journal).
- **Aucune lecture de score avant le scellement** par la commande : aucun chemin ne calcule un score avant que les gardes
  n° 3 à 7, 2, 1, 8 et 9 soient passées ; les deux contrôles préalables n'ouvrent aucune donnée ; la commande n'imprime que
  deux chemins. Deux limites, hors du code : les fonctions restent appelables directement (liste d'arrêt n° 13) ; la garde
  vaut pour le dépôt donné par `--depot` (m4).
- **Le reste du texte, point par point** (recette, cellules, intervalles, plancher, placebo, effectif lisible, règles C et T,
  phrases, graines, comptes structurels, journal) : conforme, avec les cas de bord m2 et m3.

### 5. Interdits du programme

- **Aucune moyenne ni médiane sur les jetons dans une sonde de notre chaîne.** Chaque message est une séquence d'un seul
  jeton. Dans la lecture des comités, l'agent est noté sur la séquence de ses trois messages, agrégée par le maximum du
  harnais : **son score est le maximum de ses trois scores de message** (essai-espion du développeur, sa mutation K13, et mon
  recalcul). Les seules moyennes : sur les trois messages d'un agent pour le **témoin de recette** (`externe_v2.py` l. 242,
  recette des auteurs, marquée « diagnostic, jamais en production (N-026) ») ; sur des agents (statistique de l'écart), des
  plis, des couches, des graines, des tirages. La seule médiane est celle des 200 aires du plancher, rapportée
  (`cellules_externe_v2.py` l. 180).
- **Graines (R9)** : 0 à 9 sont des constantes de la recette publiée, servies à `RandomState` et à `random_state`,
  consignées (`graines_auteurs`). Tous nos tirages (plancher, rééchantillonnage, placebo, apprentissage) viennent de
  `SeedSequence` par tâche nommée, sur l'entropie de la ligne `Entropie :` du texte ; j'ai relevé toutes les sources d'aléa
  du code : aucune n'échappe. Précision : m8.

### 6. Pour la fiche du code : section « Pour la fiche du code » ci-dessous.

## Bloquants

Aucun.

## Majeurs

- **M1 — Aucun essai ne fixe la valeur des cellules qui décident la réponse.** `src/controle_ia/narcbench/cellules_externe_v2.py`,
  `lire_modele` (l. 476-610), `lecture_finale` (l. 396-410) et les réglages (l. 52-54). **Quinze de mes dix-huit mutations de
  ce module survivent aux 168 essais** :

  | mutation (lot C) | ligne | état |
  |---|---|---|
  | C05 cellules visées de nos familles : épisodes notés dans l'ordre inverse des étiquettes | l. 543 | **survivante** |
  | C21 nos familles : étiquettes d'apprentissage inversées | l. 539 | **survivante** |
  | C22 comités de nos familles : le domaine tenu à l'écart reste dans l'apprentissage | l. 567 | **survivante** |
  | C04 plancher du témoin noté sur des vecteurs non standardisés | l. 525 | survivante |
  | C06 plancher d'une cellule : maximum sur les couches au lieu de la moyenne | l. 179 | survivante |
  | C08 placebo : maximum sur les calculs au lieu de la moyenne | l. 169 | survivante |
  | C14 intervalle par plis : minimum au lieu de la moyenne ; C18 valeur d'une cellule des comités : médiane des plis | l. 150, 314 | survivantes |
  | C12 réponse lue sur douze cellules (témoin compris) au lieu de huit : la ligne « non » devient inatteignable | l. 403 | survivante |
  | C13 qualificatifs de plancher de la réponse : huit au lieu de douze | l. 401-402 | survivante |
  | C01 quantile 0,95 → 0,50 ; C02 200 directions et 200 permutations → 20 ; C03 2 000 tirages → 1 000 | l. 52-53 | survivantes |
  | C10 effectif lisible sans la condition des dix sabots ; C11 sans celle des dix plis | l. 258, 312 | survivantes |
  | C07 placebo jamais échangé ; C09 intervalle par sabots : maximum ; C15 pic du témoin fait de l'écart | l. 165, 136, 503 | tuées |

  Cause : pour nos familles, les essais ne vérifient que la structure (clés, effectifs, « un état parmi trois ») ; seul le
  témoin est comparé à un nombre. **Le code est juste** : mon recalcul indépendant (preuve 7) et mon essai du câblage (preuve
  10) le disent, aux empreintes de la tête finale. C'est l'essai qui manque. Ce n'est pas une garde de la liste d'arrêt, et
  la lettre du plan n° 1 (énumérations, jouet) est tenue ; je le classe majeur parce que ces huit cellules font la réponse et
  qu'une inversion des étiquettes ou un désalignement des épisodes passerait inaperçu.
  **Correction, dans `tests/` seulement** : (a) un essai-oracle des cellules sur un jouet non saturé, comités compris, avec
  le domaine tenu à l'écart (mon script peut servir de base) ; (b) un essai du câblage de `lecture_finale` sur cellules
  fabriquées ; (c) un essai qui épingle les réglages du
  texte (0,95 ; 200 ; 200 ; 2 000 ; effectif 10) ; (d) les bornes de l'effectif lisible (neuf sabots portant dix épisodes de
  chaque condition ; neuf plis) ; (e) le repli du plancher à travers `lire_modele`. À défaut, la mère peut choisir de citer
  mon recalcul dans la fiche comme preuve à ces empreintes ; je recommande les essais.
- **M2 — Garde du registre (n° 3) : deux conditions sans essai sur artefact.** `src/controle_ia/narcbench/lecture_externe_v2.py`
  l. 194-198 (sceaux) et l. 187-189 (antériorité). Le texte arrête sur une ligne `CODE-NARC-EXT` « de sceau faux » ou « non
  strictement antérieure à l'ouverture ». Dans `tests/test_narcbench_lecture_externe_v2.py`, le cas `sceau_faux` (l. 302) ne
  touche que le texte, et le cas `posterieure` (l. 296) date les deux lignes en 2099. Retirer la vérification pour la seule
  ligne de code laisse la suite verte (B01, B02). **Les deux gardes arrêtent bien** quand je les appelle (G1 : fiche modifiée
  après son sceau, code 2, « ≠ empreinte du fichier » ; G2 : ligne de code seule datée de 2099, code 2, « pas strictement
  antérieure »). Le plan n° 1 du texte : « une garde sans essai sur artefact interdit la ligne de code ».
  **Correction** : deux cas dans la table `CAS` (fiche modifiée après le sceau ; ligne de code seule postérieure).

## Mineurs

- **m1** — `lecture_externe_v2.py` l. 657-667 : seules `RefusRegistre`, `GardeArret` et `MemoryError` sont attrapées. Toute
  autre exception après le manifeste sort en trace d'erreur, sans ligne `ARRET-NARC-EXT` (G5, sur une erreur d'algèbre
  factice). Le texte dit « sans trace d'erreur » et « pour tout arrêt après ». Sans effet sur le coup unique : le manifeste
  existe, la garde « déjà jouée » refuse la relance. À déclarer dans la fiche plutôt qu'à corriger (le module ne doit plus
  changer) ; la mère consignerait à la main.
- **m2** — `lecture_externe_v2.py` l. 554-555 et `externe_v2.py` l. 532-553 : les rôles (n° 8) sont vérifiés avant les
  exclusions (n° 9). Un épisode stéganographique dont **un colludeur** n'a pas de ligne finale (un sur 24 dans mon essai G6)
  arrête (« 1 colludeur(s), 2 attendu(s) »), alors que le texte l'exclut et le compte. Plus strict que le texte, dans le sens
  de l'arrêt ; sans effet sur les fichiers publiés d'après l'essai de forme (une ligne finale par agent).
- **m3** — `externe_v2.py` l. 236-243 et 257 contre l. 276-283 : pour un épisode des comités à cinq agents dont un sans ses
  trois lignes, `groupes` garde l'épisode (quatre agents restent) et `exclusions_etage` le compte exclu (G7). Le texte dit
  les deux règles égales. Sans effet sur les fichiers publiés (quatre agents partout).
- **m4** — La garde vaut pour le dépôt donné par `--depot` (l. 540, 609) : un dépôt jetable fabriqué exprès la satisfait
  (G8 ; c'est ce que font les essais). Et `paquet_execute` (l. 347-351) résout le lien de `__init__.py` : dans l'outil du
  développeur (`pieces-externe-v2/mutations_decisives_v1.py` l. 45-53), le dépôt jetable des essais porte ainsi le code non
  muté sans que la garde n° 6 le voie. Les mutations L01 et L02 restent tuées par l'essai visé (rejouées en copie entière :
  C24, C25). Sans objet pour le lancement réel (aucun lien dans le dépôt, commande lancée à sa racine).
- **m5** — Renvois en retard, sans effet : en-têtes « alignée sur le brouillon 2 » (`lecture_externe_v2.py` l. 4-5,
  `cellules_externe_v2.py` l. 2, `externe_v2.py` l. 43, `__init__.py` l. 21) ; `externe_v2.py` l. 60-61 et message l. 551
  (« nos familles » : la commande applique cette garde à toutes les procédures) ; `tests/test_narcbench_externe_v2.py` l. 583
  (« n° 6 » et « n° 10 » pour n° 9 et n° 12) et l. 743 (« n° 8 » pour n° 10).
- **m6** — Le rapport du développeur (`40fbdc70…`) décrit encore la tête `70cb77b8` : 78 essais, commande avec `--registre`,
  clé `EXTERNE-NARC`. **Sa commande est périmée.** La bonne est celle de l'en-tête de `lecture_externe_v2.py` (l. 50-53) et
  du texte. Aucun rapport du développeur ne décrit la tête finale ; les pièces et les messages de commit en tiennent lieu.
- **m7** — Épreuve du développeur : onze mutations choisies parmi celles déjà connues, dont deux seulement sur le module neuf
  des cellules. « Toutes tuées » est exact et étroit : voir M1.
- **m8** — Graines sans effet : la tâche `…/mahalanobis/plancher` est dérivée et jamais consommée ; les graines
  d'apprentissage n'agissent sur aucune des trois familles (formule fermée, ou poids initiaux nuls). La liste des 503 tâches
  reste celle du texte.
- **m9** — `journaliser` (l. 492-502) : l'identifiant du run est écrit tel quel au journal (seul le détail est nettoyé).
- **m10** — Pour qui rejoue les essais : `requirements-cpu.txt` doit être à la racine de l'arbre (62 échecs sans lui ; la
  commande `git archive` de mon mandat l'omettait) ; la suite laisse ≈ 600 Mo de dossiers temporaires.
- **m11** — Reste ouvert de la première contre-lecture (son m12) : le dossier `/home/user/narcbench-paquets-v2` n'a pas
  d'empreinte ; la garde n° 7 lit la version dans ses métadonnées.

## Suivi des remarques de la première contre-lecture (`9b90884a…`)

| remarque | état à la tête finale |
|---|---|
| M1 arrêt à 8 itérations | fermée : essai du régime non convergé, constante épinglée (A1, A3 tuées) |
| M2 gardes sans artefact, huit survivantes | fermée pour ces gardes : neuf mutations rejouées, tuées |
| M3 (a) registre libre, (b) options non comparées, (c) déjà jouée, (d) entropie en sous-chaîne | fermées : registre fixé sans option ; configuration lue dans le texte ; garde n° 4 ; ligne exacte |
| m1 deux colludeurs, mode entre lignes | fermée (`exiger_roles_episodes`, `groupes`) |
| m2 « au bit près » | fermée (formulation des en-têtes) |
| m3 version de scikit-learn | fermée (garde n° 7) |
| m4 `NaN` au résultat | fermée (`None` et un état ; `valeurs_non_finies`) |
| m5, m6 déclarations | fermées |
| m7 domaines, « 17 plis » | fermée dans `externe_v2` ; `externe_v1` laissé tel quel (R12), déclaré |
| m8 gabarit, lancement non décisif | fermée (texte factice conforme ; confirmé par le texte) |
| m9 journal, commit, trace d'erreur | fermée pour le journal et le commit ; trace : mon m1 |
| m10 garde de reproduction | fermée (version 2, état par étage, sans valeur de lecture) |
| m11 graine booléenne, étage absent, garde inatteignable | fermée |
| m12 dossier des paquets | ouverte (mon m11) |

## Pour la fiche du code

- **Commit** : `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c` si rien ne change. Si les corrections M1 et M2 ajoutent des essais, la
  tête change et les quinze empreintes ci-dessous doivent rester égales (à vérifier par `fiche-code`).
- **Fichiers `src/controle_ia/narcbench/*.py` et empreintes à la tête finale** (sortie de `fiche-code`, recoupée) :

  | fichier | sha256 |
  |---|---|
  | `__init__.py` | `fa5966b49019ae22a40f0614849635c1d6986deaa72cd99f871af076a26c847e` |
  | `cellules_externe_v2.py` | `0461739c36cd480cc1add33be1bc5556b0c873470e076f85db081faa5a0183ef` |
  | `chargeur_externe_v1.py` | `9193b7876e1cbecd18e7197998135cafee5f30e6d2ac010a769b81ac6ce74ecb` |
  | `comparateur_helios_v1.py` | `70908aa793a4b6e1b7c9e9b346fbe4fbca9399c13d99007a484956540c20f967` |
  | `contextes_v1.py` | `69c20a957805e9f49f884b8ad131b8e798a3ef0e484d600cfefbf7772f0162f0` |
  | `empans_v1.py` | `ee3e26f947e757dd1b674f1faa562fd7ab5640db48a93ef6a9525ac3fd07f2a0` |
  | `externe_v1.py` | `69dfdd247d104ee6293507fea17be56b23100f5da0ab03751d46c9d01029ed90` |
  | `externe_v2.py` | `b1054e2239b2bca17db5358c3c73f0852e7b3c2948a3edeac19fba28e7be4387` |
  | `forme_externe_v2.py` | `c3976b264fc245b36dd6446269bbafcf3298248cc31370e0485178acf1a1c9ce` |
  | `gardes_v1.py` | `54afe9c85fa5968716e9b558655dc77fc6524eb9b6afbf8bf3ca29540398a0e5` |
  | `jouet_v1.py` | `96c24f0a109c8628352ac155ee6b26ab63e277cf353e0d0f9ba256e88e411718` |
  | `lecture_externe_v2.py` | `f5a8c97b4f62c1aea5c904c62769829cf0e172b045e9026034671dc9dd320027` |
  | `notation_v1.py` | `b50dae83cd5c22a3c371db45c4da9a15e0c0f470eb3fcac02141cef073b132e5` |
  | `registre_narc_v1.py` | `17d981d73a39c5b8206c1158681f3601370e91f7c70dd7b366f898e97f9debc2` |
  | `statistiques_v1.py` | `fa9970d738b18d9056f567fadf15c70f139e53183be73519519c18bddec1b264` |

  Seul `cellules_externe_v2.py` diffère des empreintes que cite le brouillon 3 (phrase R1). Le paquet gelé à cette tête a
  les empreintes du brouillon 3 (`sondes/familles.py` `6758b651…`, `sondes/evaluation.py` `1040674c…`, `t07/plancher_v1.py`
  `ac6e8263…`, `t07/registre_v1.py` `e5023657…`, `manifeste.py` `1a5c7464…`, `prereg.py` `3b2e3ee5…`).
- **scikit-learn épinglé** : `1.9.1` (`requirements-cpu.txt` à la tête finale, `d236a3931745d4ad0889947f7692a2cd49e2c19a6f8e6c10b2e67120d47122de`).
  Autres épinglages du bras : joblib 1.6.0, threadpoolctl 3.8.0, narwhals 2.28.0, cloudpickle 3.1.3. Le dossier
  `/home/user/narcbench-paquets-v2` porte bien `scikit_learn-1.9.1.dist-info`.
- **Tâches de graines** : la fonction `lecture_externe_v2.taches`, sur la bande et sur des noms de plis factices (14 et 15),
  rend **503 tâches, toutes distinctes** : Qwen3-32B 225 (60 de familles, 140 de plis, 5 planchers du témoin, 14 cellules
  stéganographiques, 6 des comités) ; Llama-3.1-70B 278 (72, 180, 6, 14, 6). Sur les domaines de l'essai de forme (document
  `61cc1313…` : 14 et 15 noms), même compte ; liste exacte dans mes pièces (`taches-503-v1.txt`, une tâche par ligne,
  `3bcb9188b9562855945a0e39d6c825466c6b407d2eec0dcbfb80752f31082cbb`).
- **Essais passés** : 168 (16, 13, 3, 35, 8, 69, 24 : preuve 3), plus ceux des corrections.
- **Écarts restants du brouillon 3** : n° 1, phrase R1 : fermé par `cellules_externe_v2.reponse` (l. 362-393), essai
  `test_phrases_gelees_textuelles`, contrôle par programme (39 phrases, 0 écart) ; n° 2, tête finale : un seul module changé
  depuis `cde3b990`, pour la phrase R1.
- **Numéros de la liste d'arrêt** : ceux du brouillon 3, n° 1 à 12 dans le code.
- **Contre-lecteur du code final** : Claude Fable 5.2 ; ce rapport et son empreinte (compagnon `.sha256`).
- **Ce que la fusion doit emporter** (51 fichiers, tous neufs sauf un) : les 15 modules de `src/controle_ia/narcbench/` ; les
  7 fichiers `tests/test_narcbench_*.py` ; `requirements-cpu.txt` (les lignes du bras : la fiche y lit la version de
  scikit-learn) ; sous `docs/notes/narcbench-8b-v1/`, 14 pièces et leurs compagnons (rapport du développeur v2, rapport du
  module v1, rapport des données v1, relevé des cinq points de recette, relevé des licences v2, manifestes des données v1 et
  v2, sortie de l'essai de forme, six pièces de `pieces-externe-v2/`). Comparée à la tête du dépôt principal (`e21f84b5`,
  branche `claude/affectionate-bardeen-j7kddp`) : aucun fichier changé des deux côtés depuis la base commune `77d55971`.

## Avertissements pour le lancement

1. **Fusion vraie, sans écrasement ni rebasage** : la garde n° 6 exige que le commit de la fiche soit HEAD ou un de ses
   ancêtres.
2. **Ne plus toucher `src/controle_ia/` entre la fiche et le lancement** : la garde compare tout le paquet exécuté à celui
   du commit de la fiche. Aujourd'hui, hors `narcbench/`, le paquet de la tête finale et celui du dépôt principal sont égaux,
   et le dépôt principal n'a aucun fichier non suivi sous `src/controle_ia/` hors `__pycache__`.
3. **Vérifier qu'aucun dossier `runs/*-narc-externe-v2` ni fichier `diag/*/externe-narcbench-v2.json` n'existe déjà** (je
   n'ai pas le droit d'y regarder) : la garde n° 4 refuserait, et c'est un nœud.
4. Tout refus écrit une ligne au journal, qui salit l'arbre : committer avant de relancer.
5. Commande : celle de l'en-tête de `lecture_externe_v2.py` (l. 50-53), avec `PYTHONPATH=src:/home/user/narcbench-paquets-v2`.
6. Jouet du développeur aux formes publiées (vecteurs factices, commit `b46c678d`, mêmes modules à la phrase R1 près) :
   14,8 minutes, 3 748 Mo de pointe.

## Pièces

`docs/notes/narcbench-8b-v1/pieces-contre-lecture-code-final-externe-v2-v1.zip`
(`048e49b148bf45c37368ae0f36fe5db6c7ffbe46c960613a10a6a37022c255f0`, scellée) : mon outil de mutation, son greffon, les trois
lots et la liste des 168 essais ; la sortie du lot C telle que lue ; le recalcul indépendant des cellules ; les gardes à la
main ; le câblage de la lecture finale ; le repli du plancher ; la liste des 503 tâches ; la sortie de `fiche-code` ; un
mode d'emploi. L'archive a été scellée à 20:36 UTC, avant que je lise la fin du lot C : son mode d'emploi dit que cinq issues
n'étaient pas lues ; elles le sont depuis, et figurent ici (je n'ai pas réécrit une pièce scellée, R12). Les sorties des lots
A et B, du recalcul, des gardes, du repli et du câblage sont recopiées dans ce rapport depuis la session : je ne les ai pas
rejouées vers des fichiers après l'arrêt.

## Lectures hors du mandat et écarts à mes consignes (déclarés)

- **Noms de branches** : ma première commande a listé les branches du dépôt (noms seulement, dont des noms en `verdict/…`,
  `prep/…`, `quarantaine/…`). Je n'en ai ouvert aucune ; la sortie longue a été mise de côté par l'outil et je ne l'ai pas
  relue.
- **Dossier de travail partagé avec la mère** : le dossier temporaire qui m'était attribué est celui de la session mère. Deux
  listages m'ont montré les noms de ses fichiers (dont un dossier `sources-auteurs-v2`) ; je n'en ai ouvert aucun. Je n'y ai
  créé que quatre sous-dossiers (`ext`, `outils`, `mut`, `textes`) et les dossiers temporaires de mes essais.
- **Dépôt principal, hors des chemins cités** : comparaison des noms de fichiers entre la tête finale et la tête du dépôt
  principal, limitée à `src/controle_ia`, `requirements-cpu.txt`, `pyproject.toml` et aux fichiers de la branche ; état git de
  `src/controle_ia` ; noms des fichiers de `.claude/hooks/` ; les seize intitulés de la liste d'arrêt du brouillon 2.
- **Modules que le code importe**, lus dans mon extraction : `sondes/familles.py`, `sondes/evaluation.py`,
  `t07/plancher_v1.py`, `t07/registre_v1.py`, `manifeste.py`, `prereg.py`, `gardes.py`, `scellement.py` (extraits).
- **Sortie de l'essai de forme** (`forme-donnees-externe-v2.json`, pièce du développeur) : structure et comptes des fichiers
  publiés, noms de domaines ; aucun score.
- **Disque** : ma première passe d'essais a laissé 604 Mo de dossiers temporaires, au-delà des 300 Mo de ma consigne ;
  supprimés aussitôt ; les passes suivantes ont été bornées.
- **Arrière-plan** : mon lot C, lancé au premier plan sous `timeout 3000`, a été passé en arrière-plan par l'outil au bout de
  600 secondes (message : « Command did not complete within its 600s timeout and was moved to the background »). Je ne l'ai
  ni relancé ni arrêté ; il a fini de lui-même à 20:38:01 UTC (code 0) et a supprimé son dossier.
- **Faux départ de mon outil**, corrigé : une première passe du lot B a donné 26 « tuées » fausses (ma copie n'avait pas
  `requirements-cpu.txt`, tous les essais échouaient à la construction du dépôt jetable). Je l'ai vu au motif des échecs ;
  la table B ci-dessus est celle de la passe corrigée, motifs affichés.
- Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; rien sous `/home/user/narcbench-donnees-v2/` ;
  aucune branche `calcul/` ou `donnees/` ; aucun téléchargement ; aucun modèle chargé ; ni commit, ni poussée ; aucun arrêt
  de processus. Fichiers créés dans le dépôt principal : ce rapport, l'archive des pièces, leurs deux compagnons.

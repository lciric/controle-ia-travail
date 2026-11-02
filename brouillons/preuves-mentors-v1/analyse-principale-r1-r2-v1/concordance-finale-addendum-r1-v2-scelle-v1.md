concordant sauf deux réserves mineures, dont aucune n'empêche le lancement : (1) VI-09 : la déclaration d'une cible du lot lit désormais la seule lecture de cette cible. Par rapport à la ligne « réserve » du brouillon 3 (une réserve dans un lot rendait nœuds tous les non résolus de l'étape), c'est un relâchement. Il ne peut jouer que pour `mention/2605.17899v2/e0`, la seule cible déclarable non inversible, dont le lot 5 a une forme non prouvée. La règle est bien écrite, mais elle n'est ni signalée comme relâchement ni motivée de ce côté (je l'avais moi-même suggérée au brouillon 3). (2) Mon point 1 est traité sur le fond, par une mesure versée et citée à l'en-tête : 2 pas comptés sur le chemin canonique, 19 avec l'ancienne unité, sous un plafond de 16. Le chiffre n'est pas recopié près du seuil, qui reste dit « au choix de l'auteur ». Points (2) et (3) du brouillon 3 : traités. CF-01 n'est pas un affaiblissement. CF-06 est satisfait par GO-2026-11-02-14 et R-1254 ; l'enveloppe de ce GO (265 min, 6,2 USD) est de 3 min et d'environ 0,05 USD sous le pire cas écrit (268 min, ≈ 6,25 USD), ce que couvre le plafond commun de 25 USD.

# Concordance finale de conv-audit sur l'addendum v2 scellé du rejeu à graine (R1) — v1

- Vérificateur : sous-agent de conv-audit, auteur de la concordance anticipée du brouillon 3 (`rapport-concordance-brouillon3-v1.md`, `e7abaafb…`, cité par GO-2026-11-02-14 et par R-1256 comme « n° 370 »). Je n'ai écrit ni le texte, ni le code, ni VI, ni la contre-lecture finale (CF). **Déclaration d'intérêt** : la lecture « par cible » adoptée sous VI-09 reprend une suggestion de mon rapport du brouillon 3 (« lecture par cible, j'imagine », § 2 (4)) ; j'en juge ici l'effet de bord que je n'avais pas signalé (§ 4.2).
- Date : 2 novembre 2026, 15:37–15:51 UTC (`date -u`).
- Dépôt : `/home/claude/controle-ia-travail`, en lecture seule (`git show`, `git diff`, `git log`, `git ls-tree`, `git archive`). Pas de `fetch`, `checkout`, `worktree` ni `stash` ; aucun commit, aucun `.sha256`, aucun fichier existant modifié (`git status` vide) ; aucun réseau ni modèle ; `nice -n 10`. Rien n'a été ouvert sous `donnees/` : la copie d'essai ne contient, sous `donnees/`, que les deux jeux publics `T0.7-…` que le code jouet de P3 lit en chemin relatif (§ 5).
- Abréviations : « A » = texte scellé, `git show c2a8b6e1:prereg/R1-addendum-relance-v2.md` (837 l.) ; « B3 » = brouillon 3 (`9ffab30d`) ; « B4 » = brouillon 4 (`fc43ae79`) ; « RG » et « LOT » = `resolution_graine_v1.py` et `resolution_graine_lot_v1.py` au commit cité ; « l. » = ligne.

## 0. Pièces, empreintes, sceaux

| Pièce | Vérification | Résultat |
|---|---|---|
| Chaîne des commits | `git log --format='%h %p' 9ffab30d..c2a8b6e1` | linéaire : `9ffab30d` → `0e2a8871` → `82a5ed18` → `fc43ae79` → `dfe05285` → `c2a8b6e1` ; contenu de chaque commit conforme à l'annonce (code 10 fichiers ; préalables 49 fichiers sous `docs/` plus le compagnon de la table v2 ; texte seul ; texte, rapport CF et compagnon ; deux compagnons) |
| Texte scellé | `git show dfe05285:…` et `c2a8b6e1:…` → `sha256sum` ; compagnon | `9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059` aux deux commits ; compagnon `R1-addendum-relance-v2.md.sha256` égal, bon nom de base |
| Configuration | idem ; `git diff --quiet 9ffab30d c2a8b6e1 -- prereg/R1-graine-config-v1.json` | `0f300925…`, **inchangée depuis B3** ; compagnon égal ; 42 clés ; canonique `f91716bf…` recalculée (aussi par `rg.empreinte_config`) ; citée une fois sous chacun des deux libellés |
| Table v2 | `git show c2a8b6e1:prereg/R1-table-tokenisation-v2.json` ; compagnon | `5f6cf489…` ; compagnon introduit au commit `82a5ed18`, égal |
| Compagnons sous `docs/notes/runs-r1-r2-r4-v1/` | boucle sur les 28 `.sha256` à `c2a8b6e1` | 28 vérifiés, 0 écart (4 de C-6, 24 sous `graine-v1/`) |
| Empreintes de l'en-tête de A | 21 empreintes recalculées (addendum v1 à `72f68fea` : `485acc3a…`, CF-04 ; parent `80c85a00…` ; manifeste de P3 `3f21774c…` ; enquête `377101ec…` ; C-6 `1e11d58f…` ; pré-vol, comptes, essais, répétitions ; B4 `a2844644…`) | toutes égales |
| Rapports versés | `verification-neuve-vi-v1.md` `7dfe39c9…` ; `verification-adverse-vg-resume-v1.md` `36eacff6…` ; `contre-lecture-finale-addendum-r1-v2.md` `778ef139…` ; copies de L1 `dd7157e1…` et de L2 `06459850…` | égales aux citations de A (l. 735-738, 806, 816, 831) |
| Contrôle de forme | sur la copie : `prereg.problemes(A)`, `scellement.verifier` (texte, configuration, table v2), `rg.exiger_config`, `rg.exiger_reglages_execution`, `rl.exiger_config`, `rg.exiger_config_citee`, libellé du lot, `COMMIT_CITE`, `ENTROPIE_CITEE` | `problemes` = `[]` ; trois sceaux conformes ; gardes de configuration passées ; commit cité `0e2a88718f4249e556e159f45f2df38ac304331e` ; entropie = parent ; les six libellés lus par le script et les modules présents une fois chacun, plus aucun « À REMPLIR » |

## 1. Le code de l'arbre à `c2a8b6e1` est bien celui de `0e2a8871`

- `git diff --quiet 0e2a8871 c2a8b6e1 -- <CHEMINS_GELES>` (le chemin exact de `harnais/validation_reelle.py` l. 71-73) : code 0. Arbre gelé identique, donc `exiger_code_cite` et `exiger_meme_code` passeront sur l'instance.
- Pour les neuf fichiers cités par A (l. 55-65), l'empreinte est égale à `c2a8b6e1` et à `0e2a8871`, et le compagnon est conforme (sauf `rejeu_activations_v3.py`, sans compagnon, comme A le déclare). RG : `cdc22b5a…` ; LOT : `5a9982b2…` ; essais du cœur : `c4c411fb…` ; essais du lot : `add9d6de…` ; script d'instance et amorce inchangés depuis B3 (`da07025f…`, `dc8164e2…`) ; préparateur `6405b886…`.
- Garde VI-08 sur le vrai dépôt : les 45 `runs/*/manifeste.json` de `c2a8b6e1` se lisent tous comme des objets JSON. La garde plus stricte n'arrêtera donc pas l'instance.

## 2. `git diff 9ffab30d c2a8b6e1` : chaque changement rattaché

**Code** (`9ffab30d` → `0e2a8871`, rien ensuite) :

| Changement | Item |
|---|---|
| LOT : `declarer_lot` (l. 1226-1239) ; `declarations_du_lot` (l. 1242-1255) ; `declarations_coeur` et déclarations finales (l. 1357-1361) ; « résolu » dans l'entrée versée par le lot (l. 1339) | VI-01, VI-09 |
| RG : un manifeste illisible arrête `executions_anterieures` (l. 1203) | VI-08 |
| RG : `corriges_table_v2` au résultat de la validation (l. 1683-1690) | VI-10 |
| `preparer_repetition_…` : lecture depuis la racine du dépôt de répétition (`chdir`, l. 97-104) | VI-16 |
| Essais : `test_r3_manifeste_illisible_arrete` (cœur, l. 1053) ; assertions VI-10 (cœur, l. 859-860) ; `test_declaration_finale_des_cibles_du_lot` (lot, l. 872) ; cas non résolus de VI-01 dans le bout en bout du lot (l. 798-810) ; fausses déclarations du cœur dans `_coeur` | VI-01, VI-08, VI-09, VI-10 |
| Compagnons des cinq fichiers | R6 |

`lecture_du_lot` (LOT l. 604-611) et `seuil_lecture_lot` restent inchangés (aucune ligne du diff ne les touche).

**Texte** (24 blocs ; numéros de A) :

| Bloc de A | Item |
|---|---|
| En-tête : version, date, rapports traités (l. 3-16) | administratif ; VI, VG, CF |
| Commit du code et empreintes (l. 48-65) | VI-01, VI-08, VI-10, VI-16 (code) |
| « Tests attendus : `71` » (l. 76-81) | deux fonctions d'essai neuves (VI-01, VI-08) |
| Empreinte de l'addendum v1 (l. 83-84) | CF-04 |
| Compagnon de la table v2 (l. 86-87) | intégration (B3 : « à faire avant le scellement ») |
| Compagnons de C-6 (l. 91-93) | VI-13 |
| Pièces de mesure et journaux versés, avec empreintes (l. 95-111) | VI-13, mineur R6 de L2, « à verser » de B3 ; `comptes_reels` = mon point 1 et VI-03 |
| HG-4 : preuve de la forme par d_max (l. 210-216) | VI-03 |
| P-G4 : comptes de forme des quatre lots ; « au seuil de 0,99 et non au bit » (l. 257-265) | VI-03 ; CF-01 |
| Règle de lecture de la validation : attribution des essais (l. 378-383) | VI-12 (règle inchangée) |
| R3 : « qui a laissé une sortie » ; arrêt sur manifeste illisible (l. 390-392) | VI-08 |
| Écart contraint en double (l. 462-465) | VI-07 |
| Réserves : le journal ne porte que CUDA et la carte (l. 474-476) | VI-14 |
| `corriges_table_v2` (l. 501-503) | VI-10 |
| Table v3 : schéma de `lecture_validation`, déclarations finales, causes hors table (l. 563-572) | VI-15, VI-01, CF-07 |
| Chaîne du script : exception nommée (l. 577-579) | VI-04 |
| Calendrier (l. 589-599) | préalables faits ; CF-05 ; CF-06 |
| Coût et GO (l. 601-613) | VI-02 (écart de devis déclaré) ; CF-06 ; CF-08 (12 à 13 min ; + 3 min ; 6,25 USD) |
| Essais (l. 620, 633-642) | VI-08, VI-10, VI-01, VI-09 |
| Critères, lignes du lot (l. 659-661) | VI-09 = mon point 2 |
| Critères, ligne « k non résolus » (l. 663) | CF-01 (forme dans la liste à Lazar), VI-01 (`declarer_lot`) |
| Critères, audit de symétrie (l. 666) | VI-11 (chiffrage), CF-02 |
| Liste d'arrêt (l. 671-672, 686, 694-699, 710, 725-726) | VI-04 ; 71 ; VI-08 ; VI-06 (déplacé) ; VI-05 = mon point 3 (retiré) ; CF-06 |
| Traitement (l. 735-738, 751, 776, 778-793) et Contre-lecture (l. 799-837) | VI-01 à VI-16 ; VG ; CF |

**Brouillon 4 → version scellée** (`git diff fc43ae79 dfe05285`, la seule partie que CF n'a pas relue) : seuls changent l'en-tête (version, date) et les lignes de CF-01, CF-02, CF-04, CF-05, CF-06, CF-07 et CF-08, plus l'entrée « Contre-lecture 1 ». Aucune autre ligne ne bouge. C'est la vérification que demandait CF au § 7.1 ; l'entrée « Contre-lecture 1 » ne la consigne pas, ce rapport le fait.

Aucun changement n'est sans rattachement.

## 3. Mes trois points du rapport `e7abaafb`

A ne cite pas mon rapport et ne nomme pas ses trois points (R-1256 le relève). Ils sont couverts par VI-05, VI-09 et la sortie `comptes_reels`.

| Point | Où dans A et le code | Verdict |
|---|---|---|
| **(1)** Plafond `balayages_max` = 16 par U+FFFD, justifié par un compte sur le chemin canonique de `mention/2605.17899v2/e0` | Mesure faite par VI : `comptes_reels-sortie.txt` (`a2bd318f…`), ligne (b) : « action 6 : U+FFFD 1 ; chemin canonique valide True ; pas comptés 2 (dont complets 1) ; ancienne unité 19 ; plafond de l'épisode 16 ; jetons de P3 336, canoniques 335 ». Le script `comptes_reels.py` (`1a2e9803…`) compte exactement comme l'essai `_pas_comptes_sur_le_chemin_canonique` (`Cible.recherche` le long de `tok(texte)`). La pièce est citée à l'en-tête (A l. 101-102 : « … et unité des balayages »). En revanche, « Seuil » (l. 329-333) ne donne pas le chiffre, et « Déclaré » (l. 397-400) range encore 16 parmi les valeurs « au choix de l'auteur ». | **traité sur le fond, déclaratif incomplet.** Le chemin de P3 peut s'écarter du chemin canonique autour de l'U+FFFD, mais un pas compté exige d'être à portée de l'U+FFFD avec un préfixe prolongeable, ou dans un octet en attente sur l'U+FFFD. Le compte est donc de l'ordre de quelques pas par U+FFFD, avec un compteur neuf à chaque essai (RG l. 749). Le risque que 16 morde est très faible. Mesure non rejouable ici (tokeniseur et textes de P3 requis). |
| **(2)** Lecture « fidèle » du lot : texte et code accordés ; `lecture_lot` par cible ou par étape | A l. 659 : au niveau de l'étape, « toutes les cibles **mesurées** » (ce que fait le code, LOT l. 1107-1109) ; « la déclaration d'une cible lit la lecture de cette cible […], jamais la lecture d'ensemble ». A l. 663 : `declarer_lot` lit le `lecture_lot` de la cible. Code : `declarations_du_lot` lit `x.get("lecture_lot")` de chaque entrée (LOT l. 1242-1255), lui-même posé par cible (l. 679). Essais : `test_declaration_finale_des_cibles_du_lot` (« réserve » ou « sans mesure » → nœud) et bout en bout (lecture d'ensemble « fidèle », cible « réserve » ou « sans mesure » → nœud), passés ici ; mutation détectée par CF. | **conforme** (texte et code accordés). Effet de bord au § 4.2. |
| **(3)** « Résultat d'un autre code » à l'étape table | A l. 710 : « résultat d'une autre configuration ou d'une autre étape (VI-05 : l'étape table ne compare pas le code) » ; traitement l. 782 : « traité (retiré) … rien de codé ». Code inchangé. | **traité autrement** : arrêt retiré du texte, déclaré. Les arrêts réels ne changent pas. Le script fait tout au même commit, et chaque correction de la table reste revérifiée par l'empreinte de P3. |

## 4. Les changements depuis B3 affaiblissent-ils quelque chose ? (R1, R3, R4, R5, R9)

**4.1 CF-01 (lecture du lot au seuil de 0,99, non au bit) : ce n'est pas un affaiblissement, et c'est déclaré et motivé.**
- Le seuil ne change pas. `seuil_lecture_lot` = 0,99 figure dans la configuration depuis B3 (fichier identique de `9ffab30d` à `c2a8b6e1`), et 0,99 était déjà la valeur de lecture au brouillon 2 (L2 : « 0,999 prédit ; 0,99 lu »). `lecture_du_lot` n'est pas modifiée.
- Ce qui change, c'est une phrase de B4 (P-G4 : la mesure « dit si » les logits sont ceux de P3), qui disait plus que ce qu'une lecture au seuil peut établir. A l. 264-265 la corrige : « indique, au seuil de 0,99 et non au bit ». La prédiction P-G4 ne bouge pas (au moins 0,999 ; 1 exactement si fidèle au bit, l. 254-255).
- S'y ajoute une transparence, sans changer la règle : la liste remise à Lazar porte la forme de chaque cible, et le lot 5 y est dit « non prouvé » (l. 663).
- Déclaré : l. 265, 663, 832-833. Motivé : rapport CF, CF-01 « Preuve » (une lecture « fidèle » admet jusqu'à 1 % de désaccords ; une longueur remplie fausse peut changer les logits aux arrondis sans faire tomber les voisines sous 0,99).
- Remarque déjà présente avant B3, non introduite ici : un lot dont l'accord tombe entre 0,99 et 0,999 est lu « fidèle » alors que P-G4 est réfutée.

**4.2 VI-09 (lecture par cible) : relâchement mineur, écrit mais non signalé comme tel.**
- B3 l. 602 disait : « Lot : « réserve lot non fidèle » (une cible au moins sous ces conditions) | … ses non résolus ne peuvent être déclarés non inversibles : nœuds ». Une réserve dans un lot rendait donc nœuds tous les non résolus de l'étape.
- A l. 660 dit : « une cible de lecture « réserve » ne peut être déclarée non inversible : nœud ; chaque autre cible se lit sur sa propre lecture (VI-09) ».
- Seule la cause « budget de balayages dépassé » rend une déclaration « non inversible » possible, et seule `mention/2605.17899v2/e0` a un U+FFFD : ce relâchement ne peut donc jouer que pour elle. Il joue si les quatre conditions suivantes sont réunies : sa cause finale au lot est ce budget ; la classe est « graines validées » ; le lot 5 est lu « fidèle » ; un autre lot (0, 14 ou 24) est lu « réserve ». Elle passe alors de « nœud » à « non inversible déclaré, règle B ». Or le lot 5 est justement le seul dont la forme n'est pas prouvée (d_max 4).
- La règle est écrite clairement, mais ni la ligne VI-09 du traitement (l. 786) ni VI ne la présentent comme un relâchement. Le motif écrit de VI-09 porte sur l'autre sens : une cible « sans mesure » devient nœud, ce qui est plus strict.
- Sur le fond, la lecture par cible se défend. Chaque lot est jugé par ses propres voisines exactes, mesurées pendant ses propres passes, et une défaillance de la carte se verrait aussi dans le lot 5. La conséquence reste bornée : la règle B était le traitement de la v1 pour les 4, et la liste va à Lazar avant toute lecture, avec `lectures_lot_par_episode` dans la table (LOT l. 1325-1328).
- Aucun changement de texte n'est demandé (il est scellé). Recommandation pour la liste remise à Lazar : si le cas se présente, écrire à côté de la déclaration de `mention` la réserve « autre lot en réserve », comme la réserve de forme de CF-01.

**4.3 Autres changements**
- VI-05 retire un arrêt jamais codé : la liste d'arrêt écrite rétrécit, les arrêts effectifs restent les mêmes. Déclaré.
- VI-06 déplace un arrêt sans le retirer (il a lieu après le chargement du modèle, comme le code le fait depuis B3).
- VI-04 nomme une garde qui existait déjà.
- VI-08 rend le code plus strict. La phrase « qui a laissé une sortie » décrit le code de B3, désormais déclaré ; la règle R3 du texte (une exécution par étape) est inchangée.
- VI-11 chiffre deux déclencheurs de l'audit (R4), ce qui renforce R1. Avec + 0,02 sur environ 310 000 pas, le déclencheur part plus souvent qu'un simple « non distinct » statistique (environ 3 écarts-types ≈ 0,003).
- CF-02 restreint le déclencheur « informatif » aux deux autres classes. La restriction est vide : sur un pas informatif, p_k ≤ 1/2, et « graines validées » exige un accord informatif ≥ 0,90 > 0,5 + 0,10. Le déclencheur ne pouvait donc jamais partir sous cette classe.
- VI-01 rend plus stricte la déclaration « non inversible » des cibles du lot : il faut la cause du lot **et** la lecture de la cible. Avant, les déclarations du cœur étaient recopiées.
- VI-10 et VI-03 ajoutent des mesures descriptives.
- CF-03 : le repli sans trace de `declarations_du_lot` (l. 1251) est déclaré (A l. 836-837) et inatteignable par un vrai résultat, puisque `_executer` écrit toujours `cibles` (LOT l. 1112).
- R9 est inchangée : aucun tirage propre, graines de P3, entropie du parent.
- Configuration, seuils, règle de validation, budgets, P-G1 à P-G3 et plan d'analyse sont inchangés ; P-G4 est seulement complétée de comptes descriptifs.
- **Conclusion** : aucun affaiblissement d'un seuil, d'une prédiction, du plan d'analyse ni d'un arrêt effectif. Un seul relâchement de lecture (4.2), étroit, écrit, et que les rapports n'ont pas signalé.

## 5. Essais

- Fonctions d'essai à `c2a8b6e1` : 22 + 13 + 5 + 11 + 7 + 10 + 3 = **71**, sans paramétrisation ni classe. Les sept fichiers sont ceux de `CIBLES` (script l. 314-315), et le total est égal à « Tests attendus ».
- **Rejeu** sur une copie `git archive c2a8b6e1` qui exclut tout `donnees/` sauf `donnees/T0.7-faits-repe-v1/` et `donnees/T0.7-models-under-pressure-v1/` : ce sont deux jeux publics, lus en chemin relatif par `premier_test_ia/donnees.py` (l. 22, 24), dont le P3 jouet a besoin. Aucune pièce de P3, R1 ni R2 n'est extraite.
  - Commande : `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests nice -n 10 …/.venv/bin/python -m pytest -q -p no:cacheprovider --color=no <les sept fichiers> -rs`, de 15:44:18 à 15:48:55 UTC.
  - **Résultat exact : `53 passed, 18 skipped in 275.55s (0:04:35)`, code 0.** Sortie : `final/pytest-cibles-c2a8b6e1.txt`, `b8e3412e…`.
  - Les 18 sautés ont tous le même motif, « tokeniseur de Llama 3.1 introuvable » : cœur l. 238, 286, 317, 348, 381, 407, 447, 486, 555, 654 ; lot l. 112, 152, 207, 244, 297, 324, 393, 426.
- **Attesté ici** : les deux essais neufs (`test_declaration_finale_des_cibles_du_lot` pour VI-01 et VI-09, `test_r3_manifeste_illisible_arrete` pour VI-08) ; les bouts en bout jouets du cœur (avec les assertions VI-10) et du lot (avec les quatre cas non résolus de VI-01) ; la règle à trois classes ; la citation de la configuration ; les gardes ; les cinq fichiers d'outils.
- **Non attesté ici** : les 18 essais à tokeniseur (B-L1, unité des balayages, C-7, repli, cas sains et artefacts). Restent pour eux les sorties versées : `tests-cibles-final.txt` (`d7309e17…`, « 71 passed in 797.43s » au commit `0e2a8871`) et le rejeu de CF (« 71 passed in 727.01s »). `essais-sans-correction.txt` (`8544a7cd…`) montre 3 échecs sur le code `31f72147` (VI-01 deux fois, VI-08), ce qui confirme que les essais neufs mordent.

## 6. CF-06 et GO-2026-11-02-14

- **Ce que A exige** :
  - l. 607 : « le devis révisé doit être accepté par Lazar, mot consigné au registre des décisions, avant la création de l'instance (CF-06) » ;
  - l. 725-726 (Lancement) : « le devis révisé accepté par Lazar, mot consigné » ;
  - Calendrier (l. 596-597) : à faire avant le scellement ;
  - la création se fait toujours sous `GO_ID=GO-2026-11-02-02` (l. 616-617, 721).
- **Ce qui est consigné** (lecture des seules lignes concernées) :
  - `git show canal/conv-audit-n04:registres/go.md`, ligne GO-2026-11-02-14 (l. 60, commit `5ecae600`, 15:16:58 UTC) : « mot de Lazar … 15:15 UTC, en réponse à « le pire cas du rejeu est 6,2 USD … » : « go eleve le plafond » ». L'enveloppe passe « au pire cas du devis » (6,2 USD, au plus 265 min à 1,40 USD/h), le plafond commun de 25 USD est inchangé. Le GO est conditionné au scellement, aux corrections VI et à mes trois points, et à la présente concordance.
  - `registres/decisions.md` de la même branche, R-1254 (l. 1218) : même mot, même lecture.
- **Verdict : satisfait.**
  - Lazar a accepté le devis révisé (pire cas 6,2 USD, au-dessus de l'ancien « 2 USD au pire »).
  - Son mot est consigné, mot pour mot, dans **un registre des décisions** (R-1254), et A ne précise pas de quelle branche.
  - L'accord précède le scellement (15:15 contre 15:35 UTC), donc a fortiori la création.
- **Nuances** :
  - (a) CF-08, écrit après le mot de Lazar, porte le pire cas à 268 min et ≈ 6,25 USD plus le disque, contre « au plus 265 min, 6,2 USD » dans la ligne GO. L'écart est d'environ 0,05 USD. La lecture même du GO (« au pire cas du devis ») et le plafond de 25 USD le couvrent, mais il vaut d'être mentionné à la consignation du lancement.
  - (b) GO-14 prolonge GO-02 sans le remplacer. Pour suivre la lettre de A, on crée l'instance avec `GO_ID=GO-2026-11-02-02` (ligne d'extension sur `main`, `ddfff6e4` l. 190, échue le 9 novembre) et on cite GO-14 et R-1254 dans la consignation du lancement. Une création sous `GO_ID=GO-2026-11-02-14` serait un écart à la lettre de A, à déclarer.
  - (c) Ni `main` ni la branche du scellement ne portent GO-14. A ne l'exige pas, mais la routine de session-depot devrait le recopier au registre des décisions.

## 7. Remarques de forme (sans effet sur la concordance)

- L'en-tête annonce « les corrections CF-01 à CF-08 », alors que CF-03 n'est que « noté » (l. 836).
- Le pire cas vaut « ≈ 6,25 USD » au § Coût et GO (l. 613), mais encore « ≈ 6,2 USD » dans la garde de dépense (l. 723) et dans la ligne m-7 du traitement (l. 766).
- « 12 à 13 min (mesurés) » (l. 602), alors que les mesures vont de 12 min 07 à 13 min 17.
- R-1256 note un crédit Vast de 8,03 USD à 15:25 UTC, consommé à 8,90 USD/h par les instances d'une autre session. C'est hors concordance, mais à vérifier avant la création : il faut un crédit au moins égal au pire cas, car une coupure du fournisseur n'est pas un TERM de l'amorce, et seul ce qui est committé et poussé survit.

## 8. Commandes

```
date -u
git log --format='%H %ad %s' -1 <c2a8b6e1|dfe05285|fc43ae79|82a5ed18|0e2a8871|9ffab30d> ; git log --format='%h %p' 9ffab30d..c2a8b6e1
git show --stat <chacun des cinq commits>
git show <dfe05285|c2a8b6e1>:prereg/R1-addendum-relance-v2.md | sha256sum ; git show c2a8b6e1:<fichier>.sha256 (texte, configuration, table v2)
git diff --quiet 0e2a8871 c2a8b6e1 -- . ':(exclude)prereg' … ':(exclude)CLAUDE.md'   (CHEMINS_GELES)
git show <c2a8b6e1|0e2a8871>:<neuf fichiers cités> | sha256sum
boucle sur git ls-tree c2a8b6e1 -- docs/notes/runs-r1-r2-r4-v1/ (28 compagnons)
git diff 9ffab30d c2a8b6e1 -- prereg/R1-addendum-relance-v2.md ; git diff 9ffab30d 0e2a8871 -- src tests scripts ; git diff fc43ae79 dfe05285 -- prereg/R1-addendum-relance-v2.md
git diff --quiet 9ffab30d c2a8b6e1 -- prereg/R1-graine-config-v1.json
git show c2a8b6e1:docs/notes/runs-r1-r2-r4-v1/graine-v1/<VI, VG, CF, comptes_reels(.py, -sortie), compter_fffd_7-sortie, prevol-final-sortie, tests-cibles-final, essais-sans-correction, répétitions>
git show canal/conv-audit-n04:registres/go.md | grep GO-2026-11-02-14 ; git show canal/conv-audit-n04:registres/decisions.md | grep "GO-2026-11-02-14\|eleve le plafond"
git show ddfff6e4:registres/go.md | grep GO-2026-11-02-02
boucle json.loads sur les 45 runs/*/manifeste.json de c2a8b6e1
git archive c2a8b6e1 -- . ':(exclude)donnees' | tar -x ; git archive c2a8b6e1 donnees/T0.7-faits-repe-v1 donnees/T0.7-models-under-pressure-v1 | tar -x
python -I : prereg.problemes, scellement.verifier, gardes de configuration, citations ; pytest (commande du § 5)
```

## Annexe — fait et pas fait

- Fichiers écrits, tous sous `…/scratchpad/concordance-rejeu-graine-b3/` : ce rapport ; `final/` (texte scellé, trois différences, rapports CF, VI et VG extraits, copie `copie-c2a8b6e1/`, sorties pytest).
- Pas lu : aucun fichier sous `donnees/`, ni dans le dépôt ni dans la copie. Des registres, je n'ai lu que les lignes citant GO-2026-11-02-14 (et, à `ddfff6e4`, GO-2026-11-02-02).
- Pas rejoué : les 18 essais à tokeniseur ; les mesures sur les vraies pièces (comptes, pré-vol), qui demandent le tokeniseur et les données de P3.

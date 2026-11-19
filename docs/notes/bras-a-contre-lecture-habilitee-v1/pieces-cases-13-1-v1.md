# Pièces des deux cases de 13.1 du préenregistrement neuf du bras A (« consignes des moniteurs », « code de la base ») — v1

**En bref.**
- La consigne du moniteur boîte noire par action **existe**. C'est un texte transcrit, avec compagnon, contre-vérifié. Mais aucun code ne la charge, et aucune pièce ne la rattache au moniteur du bras A : ce rattachement est **à créer**.
- **Aucune pièce ne fixe** la consigne du juge d'une autre lignée : elle est **à créer**.
- Le code de la base « mots et coût » existe pour la course de confirmation de la tâche des organismes (7b). Sa version pour le bras A est **à créer** ; le cahier des charges est en partie 3.

- **Qui** : le contre-lecteur habilité des rapports `27189edd…`, `2f7b43ec…` et `c5e78b92…`, sous-agent délégué par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) ; Claude Opus 5.5 (`claude-opus-5-5`).
- **Heures (UTC)** : début 2026-11-19T08:07:20Z, écriture à partir de 08:08:55Z ; arbre courant au commit `b0c948567f3a2756ea96f22aebaac7713c24f022`.
- **Rien n'est écrit au texte du brouillon.** Ce fichier ne contient aucune valeur de seuil ni aucun interne de moniteur au-delà de chemins, d'empreintes et de noms de champs ou de constantes. Il ne recopie pas le texte des consignes.
- **Recherches faites** :
  - `ls prereg | grep` ;
  - `grep` sur `registres/scellements-v1.md` ;
  - `ls src/controle_ia/` et `src/controle_ia/bases/` ;
  - `git grep` limité à `src/`, `prereg/` et `docs/decisions/`, en excluant les noms « consigne-privee » et « conception-ii-b » ;
  - lecture des fichiers cités ci-dessous, chacun empreinté avant lecture.

  Rien n'a été ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ni `brouillons/ii-b-saboteur-budget-v1/`. Aucun résultat lu. Aucun outil refusé.

---

## 1. Consigne du moniteur boîte noire par action — **la consigne existe ; son rattachement au bras A est à créer**

| pièce | chemin | empreinte | état |
|---|---|---|---|
| invite dérivée de H.12, par action (la consigne) | `docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt` | `5a30c2b3ce283531a90661df078f3d1d0e179312c9d0cd1328caf63b69023220` (compagnon égal) | existe ; scellée par son compagnon ; **aucune ligne au registre des scellements** (`registres/scellements-v1.md` ne la nomme pas) |
| sa contre-vérification (exigée par P-010, ligne 46) | `docs/notes/couche-2-preparation-v1/tranche0-v1/contre-verification-H12-v1.md` | `50b9635e5a7ad2860aa17b6500d05008a6c757195d9dd0e56133a0f12fc91209` (compagnon présent) | existe ; verdict « conforme, avec trois remarques et un point à trancher », selon la pièce suivante |
| brouillon de dérivation | `brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md` | `c1f2bc299d34b2b1f666176997b227eab1660f3afac3c2196ad0fabd4adcde02` (sans compagnon) | existe |
| versement au registre des décisions | `registres/decisions.md`, ligne 984 (R-756 : « invite H.12 par action conforme » à la page source ; dérivation déclarée) | registre vivant | existe |
| texte qui la prend pour consigne des juges par action | `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, lignes 15 (pièces), 51 à 54 (juges par action, de la taille de l'agent et plus petit) et 63 (consigne système : ce texte, tel quel ; message de l'utilisateur : énoncé de la tâche puis ensemble courant, dernière action marquée) | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` ; **gelé** au registre des scellements (ligne 6, clé `GEL-T08`), **non scellé comme préenregistrement** (son statut, ligne 3) | existe, mais pour la course de confirmation 7b |
| code qui la charge | — | — | **aucun** : `git grep "H12-par-action"` dans `src/` ne rend rien. Le code des juges (`src/controle_ia/environnements/juges.py`, `52610b0a…`) lit la balise de score de H.12 mais ne charge pas l'invite dérivée ; `src/controle_ia/bases/scores_jetons.py` (`64946a47…`) lit le score par espérance |

**Contenu, sans recopie.** L'invite demande au juge sa confiance que la dernière modification de l'ensemble de propositions est un sabotage. Elle ne lui demande pas si les contrôles d'une action répondent à sa proposition. L'hypothèse de travail de la section 4 du brouillon tient donc pour ce moniteur, au sens étroit où elle est écrite.

**Ce qui manque pour remplir la case**, sans rien écrire au texte d'ici :
1. **Une pièce empreintée qui rattache cette invite au moniteur 3 du bras A** (texte archivé, ligne 144). Aujourd'hui, seul le texte gelé de la base boîte noire de la course 7b l'emploie. Le texte archivé du bras A anonymise ses moniteurs (ligne 16) et ne nomme pas de consigne. Le texte neuf, ou sa configuration scellée, doit citer le chemin et l'empreinte `5a30c2b3…` de l'invite et la contre-vérification `50b9635e…`. Il doit aussi reprendre ou citer la forme du message de l'utilisateur et la lecture par la balise : brouillon gelé de la base boîte noire, ligne 63 ; P-010, lignes 21 à 25, avec les deux lectures « en une passe » et « avec raisonnement », dont il faut dire laquelle est lue.
2. **Le modèle exact du moniteur** : D1 laisse deux juges de la même famille ; il faut dire lequel est le moniteur 3. Il faut aussi la révision figée de ce modèle.
3. **Le code qui charge l'invite** par son empreinte, avec un essai qui refuse une invite d'empreinte différente.
4. Facultatif : une ligne au registre des scellements pour l'invite. P-010 n'exige que « transcrite, scellée, contre-vérifiée » (ligne 46), ce qui est fait par compagnon et contre-vérification.

L'agrégateur séquentiel n'a pas de consigne propre ; il hérite de celle-ci.

## 2. Consigne du juge d'une autre lignée — **aucune pièce ne la fixe ; à créer**

- **Ce qui le définit** : la décision N-053 (`docs/decisions/decision-N-053-v1.md`, `2204256d…`, ligne 34 : un juge de la famille Qwen, en bras rapporté, option (c) de D1). Le modèle est inscrit à la liste blanche des modèles (`src/controle_ia/harnais/modeles.py`, `d0befc29…`, ligne 27, « juge (D2) »). La proposition P-036 (`docs/decisions/proposition-P-036-couche-2-preparation-v1.md`, `a8c41681…`, ligne 197) le rappelle.
- **Aucune consigne** : `git grep` sur « autre lignée », « other lineage » et « juge … lign » dans `prereg/`, `src/` et `docs/decisions/` ne rend que des mentions de ce juge, jamais un texte de consigne. Aucun préenregistrement sous `prereg/` ne porte son nom. Le texte gelé de la base boîte noire de la course 7b le **reporte** expressément (`brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, lignes 327 et 344). Sa ligne 331 dit ce qu'il faudrait : une révision figée dans le dépôt et dans la liste blanche des modèles ; la vérification que chaque valeur du score tient en un seul jeton de son tokeniseur, ou sinon une lecture adaptée et contre-lue ; un devis de carte.
- **Ce qu'il faut pour qu'il soit décisif au bras A** (GO-2026-11-19-15) :
  1. une consigne écrite, versionnée, avec compagnon, contre-vérifiée par un agent neuf, sur le modèle de P-010, ligne 46. Elle peut reprendre l'invite dérivée de la partie 1 si c'est le choix, mais il faut le dire et l'empreinter pour ce juge ;
  2. la forme du message de l'utilisateur et la règle de lecture du score (balise, espérance, masse consignée, réponse sans balise jamais imputée) ;
  3. la vérification des jetons du score sur son tokeniseur, et la révision figée du modèle ;
  4. la déclaration que cette consigne ne pose pas la question de l'appariement ;
  5. son empreinte citée par le texte neuf ou sa configuration scellée, et le code qui la charge, avec un essai sur un cas sain et sur un artefact.

  Tant que ces points manquent, la case doit porter « aucune pièce ne la fixe ». La phrase de C6 garde alors, pour ce juge, l'hypothèse de travail non vérifiée.

## 3. Code de la base « mots et coût » — **existe pour la course 7b ; version du bras A à créer**

### 3.1 Ce qui existe

- **Registre des scellements**, ligne 16 : clé `CODE-MOTS-ET-COUT-T06`, daté 2026-11-14T14:55:41Z, fichier `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b` (compagnon égal).
- **Contenu de ce fichier** : commit `da06bb57610f840152e4e9a8c449b036577cc582` ; contre-lecture `docs/notes/piece-mots-et-cout-v1/contre-lecture-code-v3-modele-c-v1.md` (`157ae316…`) ; une déclaration (aucune vue des données de 7a, 7b ou T0.7).
- **Modules et essais**, empreintes recalculées, toutes égales :

| rôle | chemin | empreinte |
|---|---|---|
| pièce (calcul) | `scripts/mots_et_cout_t06_v3.py` | `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674` |
| lanceur | `scripts/lancer_mots_et_cout_t06_v3.sh` | `e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5` |
| essais | `tests/test_mots_et_cout_t06_v3.py` | `2e951ed5056024684ea9d3b089129973bfb5bbb3ec8a0b16fdeec343373e0f42` |
| fabrique de données factices | `scripts/fabrique_factice_mots_et_cout_t06_v1.py` | `13df39767d3a54f943e7d9047268916f835cbf2fd5251a9cc0842877b213444e` |
| banc de mutations | `scripts/banc_mutations_mots_et_cout_t06_v3.py` | `b78f5d046b19811de318d596de1f02e5a6b7c355349fb3299acae8e2a470119c` |
| essai de bout en bout | `scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py` | `517eedbd216abef174a35984d54d26cc9961ef4f56a6c202c15c0b1533d3d7a0` |

- **Modules gelés que la pièce vérifie par empreinte** (constante `MODULES_GELES`) : `t06/test_croise.py` (`0a627df9…`), `t06/cout.py` (`bcfe5683…`), `t06/lanceur.py` (`a3dde550…`), `sondes/evaluation.py`, `harnais/run_harnais_factice.py`, `environnements/propositions.py` (`5d97b223…`), `manifeste.py`, `scellement.py`, `gardes.py`.

### 3.2 Ce qui est propre à la course 7b dans la pièce actuelle (à remplacer)

| élément | où | ce qu'il fait |
|---|---|---|
| conditions et effectifs | `CONDITIONS_7B`, `DOSES`, `N_TACHES`, `T_PAS`, `N_ACTIONS` | conditions de 7b ; garde d'effectifs (`lire_entrees`, arrêt si différents) |
| entrées | `FICHIERS_7B` (manifeste, épisodes, lecture du coût, mesures `mesures-t06.npz`, textes `textes-actions-t06.jsonl`) ; `lire_entrees` | empreintes, configuration canonique de 7b, ligne de GO de 7b, tâches d'évaluation, graine `partition-taches` du manifeste de 7b, effets de coût lus dans la lecture du coût |
| contrôles de validité | `CONTROLES` (saboteur instruit, adaptateur témoin, témoin, mention contre honnête) ; `TRANSFERT_DECISIF` ; `TRANSFERTS` ; `etat_ba_l2` ; `PHRASES_BA` | témoin positif et contrôle de l'adaptateur de la base (A) |
| registre et ordre | `CLES_LIGNES` (`SCELLEMENT-T08-BASE-A`, `RUN-CONFIRMATION-T06`, `CODE-MOTS-ET-COUT-T06`, `LECTURE-T08-BASE-A`, `ISSUE-MOTS-ET-COUT-T06`) ; `controler_registre_reel` (arrêt si les lignes de lecture existent déjà) ; `controler_journal` (arrêt si les sondes de la tâche des organismes ou l'étape B de la tâche des sondes sont déjà ouvertes) | |
| liste blanche | `ListeBlanche`, `FRAGMENTS_INTERDITS` (dont `adaptateur-`, `distillation-t06`) | refuse tout chemin hors de la liste ou portant un fragment interdit |
| graines | `ENTROPIE_REELLE` ; `cles_graines` (préfixes `mots-et-cout-t06/…` et `t08-base-a/…`) | |
| issue | `etat_dose`, `etiquette_m`, `valider_issue`, `CLES_ISSUE`, `PHRASES_M`, `LECTURE_PRUDENTE` | état par dose (« réussit », « échoue », « non calculable ») et issue de la tâche des organismes |

### 3.3 Cahier des charges de la version neuve (bras A)

Elle porte les huit points de 6.12 du brouillon 4 (`16187b78…`), lignes 590 à 601. Exigences de forme :
- un **nom neuf** (R12), par exemple un suffixe propre au bras A ; on n'écrase jamais les fichiers v3 ;
- un **développeur neuf**, instance habilitée qui n'ouvre ni les consignes ni les sorties des lecteurs de l'instrument (6.12, point 6), ni aucune donnée du bras A avant l'inscription du code ;
- des **données factices** seulement, pour écrire et éprouver le code.

1. **Conditions et effectifs** (6.12, point 2).
   - Conditions lues : honnête, ¼, ½, ¾, 1, et le témoin identité pour le seul contrôle de l'adaptateur. Seize tâches de vérification, huit épisodes par tâche et par condition, dix actions par épisode.
   - Garde : effectifs différents, ou présence d'une action d'une tâche de fabrication, d'une tâche d'évaluation ou du témoin bénin : arrêt avant toute lecture.
   - Remplacer `CONDITIONS_7B`, `DOSES`, `N_TACHES` et la garde d'effectifs de `lire_entrees`. Les jeux sont « dose contre honnête » pour ¼, ½, ¾ et 1.
2. **Entrées** (6.12, point 6).
   - Les mesures par action (colonnes de `ENTREES_A` : tâche, coût, jetons, validité, six indicateurs de forme du coût) sont tirées des textes d'action du bras A par les lecteurs gelés : `t06.cout` (`bcfe5683…`), `environnements.propositions.lire_action` (`5d97b223…`) et la fonction des colonnes de `t06/lanceur.py` (`a3dde550…`), vérifiés par empreinte comme aujourd'hui.
   - Les textes servent à la base sur le sac de mots ; les jetons sont le nombre de jetons générés de l'action.
   - Les fichiers d'entrée du bras A sont nommés par la configuration scellée du bras. Ils remplacent `FICHIERS_7B` et la liste blanche transposée, comme le document de la base l'exige à ses lignes 115 et 148.
   - Retirer les contrôles propres à 7b : configuration canonique, ligne de GO de 7b, tâches d'évaluation, effets de coût lus dans la lecture du coût. Le champ `effet_cout` de l'état de dose n'a pas d'équivalent au bras A : le retirer, ou le mettre nul de façon déclarée.
   - Revoir `FRAGMENTS_INTERDITS` pour les noms des fichiers du bras A. La pièce lit des épisodes réglés : un chemin qui contient « adaptateur » ne doit pas être refusé pour cette seule raison. Il faut en revanche toujours refuser sondes, activations, poids d'adaptateur, sorties de distillation, sorties des lecteurs de l'instrument, mode tenu à l'écart et étiqueteur.
3. **Centre de tâche** (6.12, point 1).
   - Population : toutes les actions des six conditions lues (les cinq et le témoin identité), sans étiquette, sur les seize tâches de vérification.
   - Le minimum de coûts lisibles par tâche est repris **comme compte absolu** (constante `LISIBLES_MIN_CENTRE`, inchangée).
   - Centres identiques pour tous les jeux et pour les deux bases, comme aujourd'hui (`centres_de_tache`).
4. **Vocabulaire de la base sur le sac de mots** (6.12, point 6).
   - Mêmes règles qu'aujourd'hui : mots de l'action, choix par (jeu, pli) sur les seules actions d'apprentissage des deux conditions du jeu ; aucune action du pli lu.
   - En plus : **aucune transcription des tâches de fabrication** ni aucun épisode de distillation n'entre dans le vocabulaire. C'est déjà garanti si les entrées ne contiennent que des tâches de vérification (garde du point 1). Ajouter un essai qui injecte une action de fabrication et doit arrêter.
5. **Plis** (6.12, point 3) : `t06.test_croise.partition_plis` (`0a627df9…`, signature `partition_plis(taches, graine)`, nombre pair de tâches exigé) sur les seize tâches de vérification. La graine est l'entier `graine_entiere` de la clé `bras-a-v2/plis` de l'entropie du bras (6.2 du brouillon), et non la graine `partition-taches` du manifeste de 7b. Mêmes plis que les autres moniteurs.
6. **Intervalle, plancher, permutations et seuils de la règle** (6.12, point 7).
   - Ceux de la règle de la tâche des organismes (lignes 575 et 576) : constantes `NIVEAU`, `QUANTILE_PLANCHER`, `SEUIL_AIRE`, `N_TIRAGES_REEL`, `N_PERMUTATIONS_REEL`, inchangées. La pièce actuelle lit les nombres de tirages et de permutations dans la configuration de 7b (`tirages_aire`, `permutations_plancher`) : la version neuve les fixe en constantes égales à celles-là, avec la source citée.
   - Aucun réglage de 6.9 du brouillon (permutations, réapprentissage, quantile) ne s'applique à la base.
   - **Graines** : de nouvelles clés propres à la base sont à nommer sous l'entropie du bras, par exemple sous le préfixe `bras-a-v2/`, à la place de `cles_graines`. Le brouillon 4 n'en nomme pas en 6.2 pour l'intervalle et le plancher de la base : c'est une lacune du texte, à signaler au rédacteur.
7. **États, « non calculable » et sens unique** (6.12, points 4 et 5 ; GO-2026-11-19-09 et -14).
   - `etat_dose` garde ses trois états. Classe absente d'un pli, vocabulaire vide, tirages dégénérés, non-convergence : « non calculable » (constante `MOTIFS_NON_CALCULABLE`), **jamais un arrêt de course** (nœud 9).
   - La sortie écrit, par dose, l'état et sa lecture au bras A : « réussit » donne « la base détecte : dose non discrète » ; « échoue » et « non calculable » donnent « non interprétable (sans témoin positif) » (7.5 du brouillon).
   - Retirer `etiquette_m`, `PHRASES_M`, l'issue de la tâche des organismes et `doses_qualifiees`, qui sont propres au filtre de la porte de sortie de la phase 0 et n'ont pas de place au bras A (section 4, point 3 du brouillon).
8. **Contrôles de validité** (6.12, point 4).
   - **Témoin positif** : non calculé, aucune condition de saboteur instruit. La ligne BA-L2 est écrite « tenue par le mot de Lazar, GO-2026-11-19-09 », jamais « attend le mot de Lazar ». `etat_ba_l2` et les phrases correspondantes sont à adapter.
   - **Contrôle de l'adaptateur** : la base est apprise sur « dose 1 contre honnête », puis lue, sans réapprentissage, sur « témoin identité contre honnête » ; c'est le transfert décisif, à la place de « `S100` contre `T100` ». Lignes BA-L3 et BA-L3b telles qu'écrites. La réserve R-BA2 est portée avec toute phrase de la table C.
   - Transferts descriptifs de 7b : retirés.
9. **Audit et réserves** (6.12, point 8) : `audit_r4` et les réserves R-BA3 à R-BA7 sont gardés. L'item de l'audit qui suppose le témoin positif est sans objet et écrit tel. Aucun état ne change.
10. **Registre et ordre**.
    - Clés neuves propres au bras A pour le code, la lecture et l'issue, sur le modèle de la ligne 16 du registre des scellements. Ne jamais réutiliser les clés de la course 7b : la pièce actuelle s'arrête si elles sont déjà inscrites.
    - `controler_journal` est remplacé par la garde d'ordre du bras A : la base est lue à l'étape (m), après le scellement de la table B. Un moniteur lu avant l'étape (m) invalide la lecture (8.3 du brouillon).
11. **Fichier du code et essais**.
    - Un fichier d'inscription au format de `CODE-MOTS-ET-COUT-T06-v1.json` (`commit`, `fichiers`, `essais`, `declaration`, `contre_lecture`), avec compagnon et inscrit au registre.
    - Essais, chacun sur un cas sain et sur un artefact (R5) :
      - effectifs du bras ;
      - action de fabrication injectée ;
      - témoin bénin injecté ;
      - plis tirés de la clé du bras ;
      - centre avec le témoin identité ;
      - « non calculable » sans arrêt, pour chacun des motifs ;
      - transfert décisif sans réapprentissage ;
      - témoin positif jamais calculé ;
      - états lus dans un seul sens ;
      - empreinte de module gelé modifiée, qui doit arrêter.
    - Contre-lecture du code par un agent neuf.
    - L'empreinte de chaque module et la ligne du registre vont à la case « code de la base » de 13.1.

---

## État des pièces

| case de 13.1 | pièce | état |
|---|---|---|
| consignes des moniteurs : moniteur boîte noire par action | invite `5a30c2b3…` et sa contre-vérification `50b9635e…` | **existe** |
| | rattachement au moniteur 3 du bras A, modèle choisi entre les deux de D1, code qui charge l'invite | **à créer** |
| consignes des moniteurs : agrégateur séquentiel | hérite de la précédente | sans objet propre |
| consignes des moniteurs : juge d'une autre lignée | consigne | **aucune pièce ne la fixe : à créer** (partie 2) |
| code de la base | pièce 7b `CODE-MOTS-ET-COUT-T06-v1.json` (`e418fdaf…`), modules en 3.1 | **existe (source)** |
| | version neuve pour le bras A | **à créer** (cahier des charges en 3.3) |

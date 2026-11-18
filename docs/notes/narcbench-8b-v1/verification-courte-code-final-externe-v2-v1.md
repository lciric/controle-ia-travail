# Vérification courte du code final du bras externe NARCBench v2, après les essais ajoutés — v1

- **Qui** : la contre-lectrice du code final (Claude Fable 5.2, `claude-fable-5-2` ; rapport
  `docs/notes/narcbench-8b-v1/contre-lecture-code-final-externe-v2-v1.md`, `a0ce022d…`), reprise pour cette seule vérification.
  Travail du 2026-11-18, de ≈ 20:59 à ≈ 21:15 UTC.
- **Mandat** : `docs/notes/narcbench-8b-v1/mandat-verification-courte-code-final-externe-v2-v1.md` (`9e3177b8…`, compagnon
  vérifié : OK), sous GO-2026-11-18-30.
- **Objet** : arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2`, **tête neuve
  `e07090a5f9658ae7e3937aea72253940523cdbd3`** (égale à la tête de l'arbre, arbre propre avant et après). Lue dans une seule
  extraction à moi (`git archive`), supprimée à la fin. Dans l'arbre du développeur : des commandes git de lecture seulement.
- **Aucun score calculé ni lu sur les données réelles ; aucun fichier de données réelles ouvert.** Tout a tourné sur des
  données factices.
- **Aucun refus** d'outil, de permission ni de crochet pendant cette vérification.

## Verdict

**Autorisable, à la tête `e07090a5f9658ae7e3937aea72253940523cdbd3`.** **M1 levé. M2 levé.** Aucun bloquant, aucun majeur
neuf. Trois mineurs neufs, sans effet sur la lecture.

## Ce que j'ai fait (preuves)

1. **Empreintes** : mandat ; rapport du développeur v2 (`d4a2960b0152434b6fad8b59083b0b52740c00b48e20e12bcc7e1865a0486b0d`) ;
   script du rejeu (`640fc76f…`) et sa sortie (`cf8833dc…`) : chaque compagnon vérifie.
2. **Différence `fe9d7996` → `e07090a5`** : deux commits, huit fichiers. Sous `src/` : **rien** (`git diff … -- src` vide).
   Deux fichiers d'essais, **en ajouts seulement** (253 et 11 lignes, aucune ligne retirée ni changée) ; trois pièces et leurs
   compagnons. `requirements-cpu.txt`, `pyproject.toml` et les cinq autres fichiers d'essais : empreintes inchangées.
3. **Les quinze modules de `src/controle_ia/narcbench/`** : empreintes de mon extraction comparées une à une à celles de mon
   rapport (`a0ce022d…`, section « Pour la fiche du code ») : **égales**. La commande `fiche-code` à la tête neuve rend ces
   mêmes quinze fichiers et scikit-learn 1.9.1.
4. **Lecture des sept essais ajoutés**, ligne à ligne (points 2 et 3).
5. **Rejeu des 175 essais** dans mon extraction : `104 passed` (cellules 21, chargeur 13, bras externe v1 3, bras externe v2
   35, forme 8, module v1 24) puis `71 passed` (commande de lecture). Mon greffon a relevé les fichiers chargés : ceux de
   l'extraction de `e07090a5`. scikit-learn est en 1.9.1 : la lecture de bout en bout ne passe la garde n° 7 qu'à cette
   version. La liste des essais vaut celle des 168 d'avant plus sept ; aucun n'a disparu.
6. **Rejeu de mes mutations**, avec mon outil (copie entière de `src/`, option `-o pythonpath=<copie>/src`, greffon qui
   imprime le fichier chargé, motif du premier échec affiché), en arrière-plan par l'outil : les quinze du lot C qui
   survivaient, B01, B02, une variante et trois mutations neuves (point 4). Lot joué de 21:03:36 à 21:10:50 UTC, code 0 :
   **21 mutations, 21 tuées**.
7. **Dépôt principal** (lecture git, chemins du paquet seulement) : à 21:04 UTC, la fusion n'est pas faite ; hors
   `narcbench/`, le paquet `src/controle_ia/` de la tête du dépôt principal est égal à celui de la tête neuve ; aucun fichier
   non suivi sous `src/controle_ia/` hors `__pycache__`.

## Réponses aux six points du mandat

### 1. Rien d'autre que des essais et des pièces : oui

`src/` est inchangé ; les quinze empreintes sont celles relevées à `fe9d7996` (preuves 2 et 3). Le commit `05ab4264` ne
touche que `tests/test_narcbench_cellules_externe_v2.py` et `tests/test_narcbench_lecture_externe_v2.py` ; le commit
`e07090a5` n'ajoute que le rapport v2 et deux pièces, avec leurs compagnons.

### 2. M1 levé

Les cinq corrections demandées sont là, dans `tests/test_narcbench_cellules_externe_v2.py` :

| demandé | essai (ligne) | ce qu'il fixe | jugement |
|---|---|---|---|
| (a) oracle des cellules | `test_oracle_independant_des_cellules` (l. 415-551) | aires par couche, estimation, intervalle par sabots, plancher et placebo des cellules de nos trois familles ; plancher, intervalle et placebo du témoin ; comités des deux familles co-principales (domaine tenu à l'écart, maximum des trois messages, intervalle par plis) | **indépendant** |
| (b) câblage de la réponse | `test_cablage_de_la_lecture_finale` (l. 577-598) | huit cas R0 à R5 ; douze qualificatifs de plancher ; huit cellules des familles ; le témoin jamais nommé dans la réponse | attendus tirés du texte |
| (c) réglages du texte | `test_reglages_du_texte_epingles` (l. 404-408) | 2 000, 200, 200 ; 0,95 et 0,95 ; effectif 10 ; 10⁻⁹ | recopie voulue des constantes |
| (d) effectif lisible | `test_bornes_de_l_effectif_lisible` (l. 601-617) | neuf sabots portant dix épisodes de chaque condition : non lisible ; dix : lisible ; neuf de chaque condition : non lisible ; neuf plis portant 18 et 18 : non lisible ; dix : lisible | bornes du texte |
| (e) repli du plancher | `test_repli_du_plancher_a_travers_la_lecture_d_un_modele` (l. 620-652) | Cholesky refusée : repli déclaré dans chaque cellule visée, sa phrase et la lecture par agent ; repli refusé : « sans plancher » ; JSON standard | comportement de bout en bout |

**L'oracle n'est pas une copie du code sous essai.** Il reprend mon recalcul (pièce `oracle_cellules_contre_lecteur_v1.py`) :
aires par `roc_auc_score` (le module compte les rangs), statistiques d'épisode par tri d'une liste (le module trie un
tableau), rééchantillonnage par concaténation d'indices (le module pondère), placebo et plancher par boucles (le module
vectorise), score d'agent des comités par le maximum explicite des trois scores de message (le module passe par le harnais).
Il n'appelle du module essayé que `lire_modele`, dont il compare la sortie, et lit deux constantes de liste. Il prend en
entrée les scores d'épisode du témoin rendus par `reproduire_helios_v2`, que l'essai-oracle des auteurs fixe par ailleurs.
**Il n'est pas ajusté à une sortie** : aucun nombre attendu n'y est écrit, hors la tolérance (10⁻¹²) et un contrôle de
sanité du jouet. **Il n'est pas tautologique** : chacune de mes mutations le fait échouer, les trois neuves comprises
(point 4). L'essai (c) est par nature une recopie de constantes, comme je l'avais demandé ; le quantile est aussi tenu par
le comportement (variante C01bis).

### 3. M2 levé

`tests/test_narcbench_lecture_externe_v2.py`, table `CAS` :
- `code_seule_posterieure` (l. 310-311) : ligne `CODE-NARC-EXT` seule datée de 2099, la ligne de scellement restant en 2026 ;
  refus, code 2, motif exigé « ligne CODE-NARC-EXT datée 2099-01-02T00:00:00Z, pas strictement antérieure » ;
- `sceau_faux_de_la_fiche` (l. 312, avec `_fiche_modifiee_apres_son_sceau`, l. 274-278) : fiche du code changée après son
  sceau (JSON valide, compagnon inchangé), le tout commité ; refus, code 2, motif exigé « CODE-NARC-EXT-v1.json : compagnon
  .sha256 ».

Les deux passent par la commande entière et par le contrôle « rien d'écrit hors du journal ». Le cas sain reste la lecture
de bout en bout. Mes mutations B01 et B02, qui survivaient, sont tuées par ces deux cas, pour le bon motif (`assert 0 == 2` :
sans la garde, la lecture irait au bout).

### 4. Rejeu

**Les 175 essais passent** (preuve 5). **Toutes mes mutations survivantes sont tuées, chacune par l'essai que nomme le
développeur** (son tableau, rapport v2, section 4) :

| mutation (mes pièces, `lot_c.json` et `lot_b.json`) | état | essai qui la tue chez moi (motif du premier échec) | essai nommé par le développeur |
|---|---|---|---|
| C01 quantile 0,95 → 0,50 | tuée | `test_reglages_du_texte_epingles` (`(0.95, 0.5, 10, 1e-09) == (0.95, 0.95, 10, 1e-09)`) | le même |
| C02 200 directions et 200 permutations → 20 | tuée | le même essai (`(2000, 20, 20) == (2000, 200, 200)`) | le même |
| C03 2 000 tirages → 1 000 | tuée | le même essai (`(1000, 200, 200) == (2000, 200, 200)`) | le même |
| C04 plancher du témoin sur des vecteurs non standardisés | tuée | `test_oracle_independant_des_cellules` (0,6681 contre 0,6694) | le même |
| C05 épisodes notés dans l'ordre inverse des étiquettes | tuée | oracle (aires 0,368 et 0,347 contre 0,632 et 0,653) | le même |
| C06 plancher : maximum sur les couches | tuée | oracle (0,714 contre 0,664) | le même |
| C08 placebo : maximum sur les calculs | tuée | oracle (0,785 contre 0,736) | le même |
| C10 effectif lisible sans les dix sabots | tuée | `test_bornes_de_l_effectif_lisible` (`'C2' == 'C1'`) | le même |
| C11 effectif lisible sans les dix plis | tuée | le même essai (`'C2' == 'C1'`) | le même |
| C12 réponse lue sur douze cellules | tuée | `test_cablage_de_la_lecture_finale` (R3 rendu au lieu de R2) | le même |
| C13 qualificatifs de plancher : huit au lieu de douze | tuée | le même essai (`8 == 12`) | le même |
| C14 intervalle par plis : minimum | tuée | oracle (0,5 à 1 contre 0,75 à 1) | le même |
| C18 cellule des comités : médiane des plis | tuée | oracle (1,0 contre 0,9) | le même |
| C21 étiquettes d'apprentissage inversées | tuée | oracle (aires 0,597 et 0,542 contre 0,632 et 0,653) | le même |
| C22 domaine tenu à l'écart laissé dans l'apprentissage | tuée | oracle (aires par pli) | le même |
| B01 sceau de la fiche du code non vérifié | tuée | `…[sceau_faux_de_la_fiche]` (`assert 0 == 2`) | le même |
| B02 antériorité vérifiée pour la seule ligne de scellement | tuée | `…[code_seule_posterieure]` (`assert 0 == 2`) | le même |
| C01bis : C01 jouée contre l'essai-oracle seul | tuée | oracle (0,521 contre 0,664) : le quantile est tenu aussi par le comportement | — |
| N1 (neuve) cellule de l'écart du témoin faite des scores du pic (`cellules_externe_v2.py` l. 504) | tuée | oracle (intervalle 0,463 à 0,851 contre 0,521 à 0,858) | — |
| N2 (neuve) comités de nos familles : étiquettes d'apprentissage du pli inversées (l. 570) | tuée | oracle (aires par pli) | — |
| N3 (neuve) plancher de nos familles : statistique de l'écart remplacée par celle du pic (l. 563) | tuée | oracle (0,664 contre 0,703) | — |

À chaque mutation, mon greffon a relevé que le fichier chargé était la copie mutée. Les trois dernières lignes sont des
mutations **neuves**, que le développeur ne connaissait pas : elles disent si l'oracle tient au-delà de la liste qu'on lui a
donnée.

Le développeur a rejoué avec son outil à copie partielle (mon mineur m4) ; mon rejeu à copie entière donne les mêmes
essais tueurs. Je n'ai pas rejoué C07, C09, C15, C24, C25 ni B03 à B26 : elles étaient déjà tuées, et ni `src/` ni les essais
qui les tuaient n'ont changé (ajouts seulement).

### 5. Mineurs laissés

Aucun ne touche une valeur, un état ni une phrase de la lecture. Tous peuvent rester tels quels avant la lecture. Aucun ne
peut se corriger sans changer un module, ce que le texte interdit désormais.

| mineur (rapport v2, section 5) | peut rester ? | ce que le texte ou le registre doit en dire |
|---|---|---|
| m1 — une exception autre qu'une garde ou la mémoire, après le manifeste, sort en trace d'erreur, sans ligne `ARRET-NARC-EXT` | oui : le manifeste existe, la garde « déjà jouée » refuse la relance | Le texte dit « sans trace d'erreur » et « pour tout arrêt après » : il dit un peu plus que le code. **À écrire avant le scellement** : une phrase du texte si un brouillon de plus est fait ; sinon une ligne de décision de la mère (une exception imprévue vaut arrêt après ouverture, consigné à la main, relance = nœud) et la même mention dans la fiche du code. |
| m2 — rôles vérifiés avant les exclusions : un colludeur sans ligne finale arrête au lieu d'être exclu et compté | oui : plus strict, dans le sens de l'arrêt ; **le cas ne peut pas se produire** sur les huit fichiers, fixés par leurs empreintes (garde n° 1) : l'essai de forme (`61cc1313…`) y relève, pour chaque modèle, quatre agents à ligne finale dont deux colludeurs dans chacun des 20 épisodes de collusion | Le texte (n° 9) dit autre chose pour ce cas. Mention dans la fiche du code ; rien d'autre. |
| m3 — épisode des comités à cinq agents dont un sans ses trois lignes : gardé par une fonction, compté exclu par l'autre | oui : **le cas ne peut pas se produire** (même document : quatre agents et trois lignes de discussion par agent dans chacun des 62 épisodes des comités de chaque modèle) | Mention dans la fiche du code ; rien d'autre. |
| la garde vaut pour le dépôt donné par `--depot` | oui | Le plan n° 2 du texte fixe le lancement à la racine du dépôt principal ; le manifeste garde la commande. Rien à ajouter. |
| outil de mutation du développeur à liens symboliques | oui : hors de la lecture | La fiche peut dire que les tableaux ont été rejoués en copie entière (ce rapport). |
| tâche `…/mahalanobis/plancher` jamais consommée ; graines d'apprentissage sans effet | oui | La liste des 503 tâches reste celle du texte. Une ligne dans la fiche. |
| le journal écrit l'identifiant du run tel quel | oui | Rien. |
| dossier `/home/user/narcbench-paquets-v2` sans empreinte | oui : la garde n° 7 exige la version, le manifeste consigne les versions | Rien ; la mère peut relever le contenu du dossier au lancement. |
| renvois en retard dans des en-têtes (« aligné sur le brouillon 2 ») | oui : commentaires ; la numérotation est la même | Rien. |

Une réserve de forme, à la mère : le plan n° 1 du texte dit que « le code ferme chaque écart » avant la ligne de code. m1 à
m3 sont trois écarts de lettre, sans effet possible sur la lecture. Je recommande de les **déclarer** (fiche du code, et une
ligne de décision avant le scellement) plutôt que d'écrire un brouillon de plus ; c'est à elle d'en juger.

### 6. Ce qui reste avant la ligne `CODE-NARC-EXT`

La liste du rapport v2 (section 6) est **juste, et incomplète sur six points**. Elle dit : fusion vraie dans `main` avec les
pièces ; fiche scellée et ligne de code par la mère ; plus aucun changement de `src/controle_ia/` jusqu'au lancement ;
relevé de la mémoire libre ; aucun `runs/*-narc-externe-v2` ni `diag/*/externe-narcbench-v2.json`. Il y manque :

1. **Le texte se scelle d'abord.** La ligne `SCELLEMENT-NARC-EXT` précède la ligne de code. Avant elle : la contre-lecture 3
   du texte ; les trois inscriptions de la mère, dont la **tête finale, qui est maintenant `e07090a5…`** et non `fe9d7996…` ;
   l'entrée « Contre-lecture 3 » avec deux empreintes distinctes ; `verifier-texte` (code 0) ; `sceller_prereg`.
2. **Dates des deux lignes** : la ligne de code doit être **strictement postérieure** à la ligne de scellement (une seconde
   au moins), et les deux strictement antérieures au lancement. Le registre ne porte que ces deux lignes (toute autre clé
   refuse) ; le texte et la fiche ont chacun leur compagnon `.sha256` ; tout est commité (arbre propre).
3. **Après la fusion, dans le dépôt principal** : rejouer `fiche-code --depot . --commit e07090a5…` et comparer aux quinze
   empreintes ; vérifier que le paquet hors `narcbench/` n'a pas bougé. La fusion apporte 57 fichiers (56 neufs,
   `requirements-cpu.txt` modifié) ; aucun n'est changé des deux côtés depuis la base commune `77d55971`.
4. **Contenu de la fiche** selon le texte : outre le commit, les quinze fichiers et scikit-learn 1.9.1, les clés
   informatives (branche, épinglages, lignes du code des auteurs, liste des 503 tâches, écarts fermés et leurs essais,
   175 essais passés, numéros de la liste d'arrêt, contre-lectrice et empreintes de ses deux rapports), plus les trois
   limites m1 à m3.
5. **Données** : les huit fichiers présents, et **aucun chemin portant un segment `transfer`** sous
   `/home/user/narcbench-donnees-v2` : cet arrêt-là (n° 2) est un nœud, sans relance. Je n'y ai pas regardé.
6. **Environnement du lancement** : `PYTHONPATH=src:/home/user/narcbench-paquets-v2` avec `.venv/bin/python`, depuis la
   racine ; aucune ligne déjà écrite au journal qui ne soit commitée.

## Mineurs neufs (sans effet sur la lecture)

- **n1** — `tests/test_narcbench_cellules_externe_v2.py` l. 651-652 : la dernière vérification de l'essai du repli (douze
  « sans plancher » dans la réponse) ne joue que si la réponse est R1 ou R2 ; sinon elle est sautée sans bruit. Le câblage
  des douze qualificatifs est tenu par l'essai (b).
- **n2** — même fichier, l. 551 : le contrôle de sanité du jouet exige une estimation minimale au-dessus de 0,5 ; sur ce
  jouet, la plus basse valait 0,503 dans mon recalcul (Mahalanobis, écart). C'est déterministe aux versions épinglées ; un
  changement de bibliothèque pourrait faire échouer l'essai à tort, jamais le faire passer à tort.
- **n3** — rapport v2, en-tête : « travail … à ≈ 21:05 UTC », alors que le commit qui le porte est de 20:56:56 UTC et que
  son rejeu finit à 20:55:36 UTC. Heure approchée, à ne pas reprendre telle quelle.

## Pour la fiche du code (mise à jour de mon rapport `a0ce022d…`)

- Commit : `e07090a5f9658ae7e3937aea72253940523cdbd3`. Quinze modules : empreintes **inchangées**. scikit-learn `1.9.1`.
  503 tâches : inchangées (les modules qui les nomment n'ont pas changé).
- Essais passés : **175** (21, 13, 3, 35, 8, 71, 24). Sept neufs ; aucun retiré.
- Empreintes à la tête neuve : `tests/test_narcbench_cellules_externe_v2.py`
  `81698650218099d4c3c8b796fdfcc9c2403bf6fb6d9f558c55addb5a982cacb1` ; `tests/test_narcbench_lecture_externe_v2.py`
  `51739f491c9d1576e039e4193cb3beb016d7daa9b9a16a06d42ef41ef00f1cb3` ; `requirements-cpu.txt` `d236a393…` (inchangé).

## Lectures hors du mandat et écarts à mes consignes (déclarés)

- **Dépôt principal** : état git limité à `src/controle_ia`, `requirements-cpu.txt` et `pyproject.toml` (comparaison à la
  tête neuve, fichiers non suivis du paquet), et la liste des noms de fichiers changés depuis la base commune, pour dire
  s'il y a un risque de conflit. Mon archive de pièces (`048e49b1…`), relue pour en tirer mon outil et mes lots.
- **Dossier de travail partagé avec la mère** : je n'y ai créé qu'un sous-dossier (`verif-courte-cl`), supprimé à la fin ;
  je n'ai rien listé d'autre.
- **Rapport du développeur v2, section 7** : il y déclare un refus d'un crochet du dépôt, survenu chez lui. Je le signale
  parce que je l'ai lu ; il ne concerne pas ma vérification.
- **Disque** : une seule extraction (13 Mo). Le rejeu des 71 essais de la commande a laissé 619 Mo de dossiers
  temporaires, supprimés aussitôt ; les copies de mutation (7 Mo chacune) ont été supprimées une à une par l'outil.
- Commandes : les deux passes d'essais (52 et 42 secondes) au premier plan sous `timeout` ; le lot de mutations en
  arrière-plan par l'outil, sans attente au premier plan.
- Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`, ni sous `/home/user/narcbench-donnees-v2/` ;
  aucune branche `calcul/` ou `donnees/` ; aucun téléchargement ; ni commit ni poussée ; aucun arrêt de processus ; rien de
  modifié dans l'arbre du développeur ; dans le dépôt principal, ce rapport et son compagnon seulement.

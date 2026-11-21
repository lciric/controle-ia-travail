# Contre-lecture neuve du code de la seconde passe de la lecture des directions des sondes par nos lentilles (R et S) — v1

Contre-lecteur neuf : je n'ai écrit ni le texte ni le code, et je suis d'un autre modèle que le développeur. Date : 2026-11-21 (UTC).
Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-contre-lecteur-code-seconde-passe-v1.md`
(`533e6f761b95e81a3a0f884f6d5a9cec9d9409c066b9b29cc8ac1866fde6713c`, vérifié). Pièce jugée : classe B (instrument).

## Verdict
**Pas avant.** Le code applique fidèlement la section « Code neuf » du texte v2 scellé : statistique corrigée, règle de départage,
phrases gelées mot pour mot, canal des messages d'arrêt, gardes et essais. Mais deux corrections bloquent le départ :
(B1) le montage exécuterait la lecture paginée du corpus, `corpus_pagine_v1`, alors qu'aucune fiche du code ne contrôle son
empreinte ; (B2) le défaut du cache du tokeniseur hérité de la première passe (point transmis par la session des lentilles).
Les deux demandent une version neuve du lanceur de la seconde passe.

## Mémoire de travail, et ce qui a été lu
Je l'ai dit au départ : le texte entier et tout le code (environ 680 Ko) ne tenaient pas ensemble dans ma mémoire. J'ai donc lu
de façon ciblée, ce qui suffit au mandat. Du texte v2 (`a2bbed7a…`, vérifié), j'ai lu en entier : « Entrées », lignes 1264 à 1319
puis 1340 à 1560 (la liste « Jamais ouverts » est sautée ; ses trois dernières lignes, 1340 à 1343, ont été vues en passant :
elles parlent de ce qui n'est jamais ouvert, sans aucune donnée) ; « Métrique », « Seuil », « Plan d'analyse », « Critères de
lecture gelés », « Liste d'arrêt » et « Code neuf » (lignes 1561 à 2259 et 2428 à 2635). Je n'ai pas relu les sections
d'historique des brouillons.

Du code, j'ai lu en entier : `montage_v2`, `corpus_pagine_v1`, `statistiques_v4`, `comparaisons_lentilles_v1`, le lanceur de la
seconde passe (lignes 1 à 1225), `phrases_v2` (formes, verdict d'ensemble, reproduction, tête, renvois, phrases par direction),
et `nos_lentilles_v1` (lignes 40 à 569, puis 684 à 993, lecture de l'archive). J'ai lu en partie les fonctions réemployées de
`statistiques_v1`, `_v2` et `_v3`, ainsi que `entrees_v2`, `entrees_v3`, `audits_v1` et `reproduction_v1.sans_comparaison`.
J'ai comparé `lanceur_v7` à `lanceur_v8` : leur seule différence est le corpus. Je n'ai pas lu ligne à ligne `lecture_entree_v1`,
`audits_v2`, la fin de `nos_lentilles_v1` (lignes 993 à 1180) ni les essais (je les ai seulement cherchés par mots-clés).

Empreintes vérifiées : les 17 fichiers de code et d'essais, ainsi que le texte, contre `empreintes-code-seconde-passe-v1.txt`
(tous en ordre) ; toutes les notes et tous les outils nommés par le mandat, par leur compagnon (tous en ordre) ; les mots de
Lazar, les deux mandats du développeur et la contre-lecture du correctif de la pagination (tous en ordre). Aucun fichier du code
figé n'a changé depuis `ffba6bed` : `git diff` ne montre que les ajouts du correctif de la pagination.

**Essais rejoués** (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider
tests/test_lentilles_sondes_bbis_seconde_passe_*_v1.py`) : **317 réussis, 0 en échec** (47,6 s).

Cloisonnement : aucune ouverture de `diag/`, de `runs/`, de `docs/verdicts/` ni des branches exclues ; aucun téléchargement ;
aucune clé lue ; `verifier-arbre` non exécuté. Du registre propre, sur `origin/main`, j'ai relevé les seules clés et heures. Aucun
intitulé interdit vu. Aucun refus d'outil.

## Corrections bloquantes
**B1 — Lecture paginée du corpus exécutée sans contrôle de son empreinte.**
- `montage_v2.py`, lignes 72 à 85 : sans fonction donnée, la fonction importe `corpus_pagine_v1`, présent sur la branche depuis le
  correctif, et appelle `cibles_corpus(voisin, transport)`. L'appel est correct : la signature convient et la borne garde sa
  valeur par défaut, 100 pages. Le transport réel passe par `page_requests`.
- `lanceur_seconde_passe_v1.py`, lignes 55 à 58 : la liste `MODULES`, dont `exiger_fiche_code` (lignes 141 à 144) contrôle les
  empreintes contre la fiche `CODE-LENTILLES-BBIS-V2`, ne porte pas `corpus_pagine_v1`.
- Conséquence : le montage réel exécuterait un module que la fiche du code ne contrôle pas. C'est la ligne de la « Liste d'arrêt »
  « code non cité par `CODE-LENTILLES-BBIS-V2` : rien de la seconde passe ne part » (texte, ligne 2225).
- L'essai `tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py`, ligne 504, exige même l'absence du module de la liste.
  Les essais de bout en bout injectent `montage_v1.cibles_corpus` (`tests/lentilles_sondes_bbis_seconde_passe_jouets_v2.py`,
  ligne 110) : le chemin réel n'est donc éprouvé par aucun essai de la seconde passe.

**B2 — Tokeniseur du modèle à porte absent du cache** (point transmis par la session des lentilles le 2026-11-21 ; je n'en ai pas
cherché la cause, comme demandé).
- Ce qui s'est passé : la course de la première passe, lancée par `lanceur_v8`, s'est arrêtée dans le script voisin
  `05_act_corpus.py`. `tokenizer.model` n'est pas posé par `montage_v1.poser_cache_tokeniseur`, et l'enfant tourne en ligne sans
  clé (`montage_v1.calculer_jetons_gardes`), d'où une erreur 401 du dépôt à porte.
- Ce que j'ai constaté : le lanceur de la seconde passe appelle les mêmes fonctions (`lanceur_seconde_passe_v1.py`, ligne 212
  pour la pose du cache, ligne 259 pour le calcul des jetons gardés). Il hérite donc du défaut.
- Suite : à reprendre quand le correctif écrit en parallèle (`cache_tokeniseur_v2`, `lanceur_v9`) sera contre-lu.

**Changement minimal exact (B1 et B2 ensemble ; règle des noms neufs, R12 : rien d'existant n'est réécrit)** :
1. `lanceur_seconde_passe_v2.py`, copie de la v1 avec :
   - `"corpus_pagine_v1"` dans `MODULES`, plus le module neuf du correctif du cache une fois contre-lu ;
   - `MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v2")` ;
   - les cibles du corpus prises explicitement de `corpus_pagine_v1.cibles_corpus` par défaut, comme le fait `lanceur_v8`
     ligne 414, et non par l'import paresseux de `montage_v2` (qu'on peut garder pour les jouets) ;
   - les appels des lignes 212 et 259 remplacés par ceux du correctif du cache.
2. Des essais neufs (fichier v2 ; l'essai de la ligne 504 reste dans la v1, qui n'est plus lancée) :
   - fiche du code sans l'empreinte de `corpus_pagine_v1`, ou avec une empreinte altérée d'un octet : refus ;
   - cas sain : empreinte présente ;
   - un montage de bout en bout sur un arbre simulé de plusieurs pages, par un transport jouet qui porte `page`, montrant que la
     seconde passe suit les pages ;
   - les essais du correctif du cache, repris.
3. Une fiche `CODE-LENTILLES-BBIS-V2` qui cite le commit neuf et ces empreintes (forme du nœud N-dev-8).
4. Une contre-lecture courte du différentiel.

**Faut-il une version neuve du lanceur pour partir ? Oui.** La liste `MODULES` est une constante du lanceur figé.

## Corrections non bloquantes
- **N1** — `noeuds-et-precisions-seconde-passe-v1.md`, ligne 21 (N-dev-6) : « aucune copie du code voisin n'est versée » est
  inexact. `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-lenses.py.txt` et
  `neuron_lens-transport.py.txt` sont versés, et leurs compagnons sont en ordre. À corriger dans une note neuve (voir le point 3
  plus bas).
- **N2** — `phrases_v2.py`, lignes 264 à 268 : au premier palier avec une seule de nos lentilles, la ligne d'ensemble de la
  lecture de la seconde course n'est pas recopiée à côté de celle du verdict d'ensemble de la tranche. « Entrées » (lignes 1474 à
  1476) le demande à tout premier palier quand cette lecture est scellée.
- **N2 bis** — `phrases_v2.py`, ligne 258 : au premier palier avec nos deux lentilles, cette ligne est recopiée dès que la fiche
  la porte, sans vérifier que la ligne `LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS` est inscrite (le texte dit « si la lecture de
  la seconde course est scellée »). Correction proposée : exiger la ligne de registre, comme le fait
  `_ligne_de_la_seconde_course` du lanceur (ligne 939).
- **N3** — `lanceur_seconde_passe_v1.py`, ligne 1157 : quand le recouvrement des moitiés n'est pas calculable, le crochet
  « [O'] » reçoit « non calculable », ce qui donne « les deux moitiés de notre R : non calculable sur vingt ». Le texte ne fixe
  pas ce cas. Recommandation : le dire en table, ou noter que la phrase est remplie ainsi. Aucun mot gelé ne change.
- **N4** — `phrases_v2.py`, ligne 315, avec `lanceur_seconde_passe_v1.py`, lignes 928 à 936 : pour une première passe encore en
  cours au montage puis achevée, la tête écrit la phrase « Reproduction de la première passe : non faite, première passe lancée
  et non achevée ; […] avant le nœud de la v1. », suivie d'une note. Or le texte (lignes 2005 à 2008) dit qu'il n'y a alors pas
  de nœud de la v1, et que les phrases sont celles de la première passe. La note le dit, mais la phrase de tête reste inexacte.
  Le cas est rangé sous la ligne « lancée et non achevée au montage » de la « Liste d'arrêt », d'où la phrase gelée. À lier au
  nœud N-dev-9.
- **N5** — `nos_lentilles_v1.py`, ligne 343 : l'expression qui cherche « Lentille nommée : … » porte sur toutes les lignes de la
  pièce. Une citation de cette forme ailleurs dans la pièce ouvrirait la lecture. Recommandation : exiger une seule ligne de
  cette forme, sinon arrêt pour forme mal comprise.

## Points à trancher

**1. Nœud N-dev-1 (corpus des jetons gardés).** `montage_v2` prend correctement `corpus_pagine_v1.cibles_corpus`. Le lanceur ne
contrôle pas son empreinte. Une version neuve est nécessaire ; le changement minimal est écrit plus haut (B1).

**2. Nœuds N-dev-2 à N-dev-10.**
- N-dev-2 (fiche de rangement en JSON) : **tenu**. Le texte dit le contenu de la fiche, non sa forme. La forme est à transmettre
  à la session principale.
- N-dev-3 (« Lentille nommée : R ») : **tenu**, avec la forme à transmettre. Le sens sévère ne fait que retenir la lecture. Voir
  la correction N5.
- N-dev-4 (couche écartée : `{"limite", "ecartee"}`) : **tenu**. La fiche recopie les mots, et le code ne les interprète pas.
- N-dev-5 (même code d'entrée, `entrees_v3`) : **tenu**. Le texte dit « même code d'entrée » (lignes 1345 à 1347). La deuxième
  ligne de la « Liste d'arrêt » de la v1 vaut pour la seconde passe, car seule la première en est exceptée (ligne 2217). De plus,
  `GO-LENTILLES-BBIS` et `CODE-LENTILLES-BBIS` sont inscrites au registre propre sur `origin/main` (2026-11-21T16:02:40Z).
- N-dev-6 : **tenu** ; voir le point 3.
- N-dev-7 (dernier crochet indéterminable : phrase non écrite, note) : **nœud pour Lazar**. Le texte veut qu'une lentille non
  lue « reçoive quand même la phrase de son verdict » (ligne 2075). Mais pour une fiche muette, ou pour une course menée en
  entier dont la lecture n'est pas inscrite, les deux valeurs du crochet seraient fausses. Le choix du code change ce qui est
  écrit en tête. Recommandation : garder le choix du code (phrase non écrite, note écrite), confiance moyenne à haute. Défaut sous
  48 heures : ce choix.
- N-dev-8 (forme de la fiche du code) : **tenu**. La fiche neuve doit porter `corpus_pagine_v1` et le module du correctif du
  cache (B1, B2).
- N-dev-9 (instant où se lit l'état de la première passe) : **nœud pour Lazar**. Le texte fixe cet instant : « au montage de la
  seconde passe » (lignes 1995 et 1996 ; ligne 2241). Le code suit le texte pour une passe « non achevée au montage, achevée
  depuis ». En revanche, pour une passe « jamais lancée au montage, lancée depuis », il ne remplace pas la première passe, alors
  que la lettre du texte la ferait remplacer. Le sens sévère protège la primauté de la v1 (ligne 1785) et évite deux jeux de
  phrases de la lentille publique. Ce cas est plausible : le registre ne porte pas encore `ENTREES-LENTILLES-BBIS`, et les deux
  passes peuvent tourner en parallèle. Recommandation : garder le sens sévère du code et corriger la phrase de tête (N4).
  Autre voie : que la session principale fasse inscrire `ENTREES-LENTILLES-BBIS` avant le montage de la seconde passe, ce qui
  rend le cas sans objet. Confiance moyenne. Défaut sous 48 heures : le sens sévère.
- N-dev-10 (motif « calibration du nul hors de ses bornes pour l'une des deux lentilles R ») : **tenu**. C'est une conséquence
  directe de la ligne de calibration de la « Liste d'arrêt » : le libellé de lecture n'existe pas. Le tableau des « Critères »
  cite déjà la « calibration » parmi les motifs.

**3. Écart N-dev-6 (`torch.load` à la place de `lenses.load_fits`).** **Acceptable sans voisin versé.** Dans la copie versée de
`lenses.py`, lignes 95 à 116, `load_fits` d'un seul fichier vaut `torch.load(…, weights_only=False)` puis
`Accumulator.from_state(saved["state"])`. Dans `transport.py`, lignes 59 à 62, `Accumulator.mean(target)` vaut la somme des
moitiés divisée par `sum(n_docs)`. C'est exactement la formule du texte, et l'essai la compare. Réserve : cette copie date du
13 novembre (branche du voisin) et non du commit `849bfe…`. Amélioration possible, non exigée : appeler la copie versée dans
l'essai.

**4. Gardes et règle R5.**
- Chaque garde du « Code neuf » que j'ai cherchée a son cas sain et son artefact dans les essais : rapport à ε pour trois
  lentilles et bord, archive (compression, contiguïté, décalage, classe hors de la liste, `meta`), plongements liés, nom de clé de
  la plateforme en trop, règle du nœud N12, bord 0,10 contre 0,1001, entre autres.
- Seul trou : la lecture paginée réelle du corpus n'est éprouvée par aucun essai de la seconde passe (B1).
- Les trois altérations que les essais ne voient pas sont équivalentes :
  - **compression acceptée** : si la garde de la méthode est retirée, un enregistrement compressé finit par un arrêt sur une
    autre garde (« archive illisible »). Avec le descripteur de données, l'en-tête porte 0 et 0, et la taille tirée de `data.pkl`
    contredit le descripteur. Le motif change, mais il relève de la même ligne de la « Liste d'arrêt » (ligne 2233). La raison que
    donne le développeur (« taille compressée différente de la taille ») n'est donc qu'une partie de l'explication.
  - **notre S comparée à une lentille R** : `(a, b) not in PAIRES` refuse aussi.
  - **empreinte du 18 novembre** : `condition_de_lecture` arrête déjà au premier palier quand l'empreinte relue n'est pas celle du
    18 novembre (ligne 526), et le flux est comparé à la fiche.

**5. Messages d'arrêt.**
- `ligne_affichee` (lignes 889 à 894) et l'enveloppe `calculer` (lignes 897 à 925) reprennent le schéma de `lanceur_v7` à
  l'identique : garde du fichier d'arrêt déjà présent, tri sous la coupure, versement d'un arrêt cloisonné, mots fixes.
  `principal` n'imprime rien d'autre.
- La relecture de contrôle de l'audit (`audits_v1.comparer_relecture`, et la relecture de notre S, lignes 858 à 868) est écrite
  sans arrêt. **Conforme.**

**6. Statistique corrigée et départage par identifiant croissant.** **Exacts.**
- `premiers_departages` trie par valeur décroissante en double précision exacte, puis par identifiant, avec `lexsort`, sur tous
  les jetons de valeur au moins égale à la k-ième.
- `premiers_departages_colonnes` reprend une à une les colonnes qui ont une égalité à la limite.
- Le signe − est classé sur −a. Les pôles suivent l'ordre « cosinus, puis neurone, puis + avant − ».
- C(u_j) sans soi-même : formules du point 6, calcul en double précision, arrêt à 10⁻¹⁰ et pour moins de trois directions.
  P(u_j) : quantile sur les M − 1 autres directions par les statistiques d'ordre (vérifié, égalités comprises). Comparaisons en
  simple précision, égalité comptée contre v.
- p de recouvrement conservateur ; libellés de comparaison exacts ; aucune garde d'égalité ; comptes d'égalités écrits.

**7. Phrases gelées.** **Conformes mot pour mot**, à l'espacement près, comme le texte le prévoit. Vérifié par programme :
- les six formes du critère d'identité, la phrase de la lentille S construite, la phrase « Cette lentille n'a pour mesure à
  elle… », le domaine d'usage, la reproduction non faite et la phrase de tête de la seconde passe sont toutes présentes dans le
  texte ;
- les phrases par direction, de famille (`w`, `q`, couches 15 et 23) et de comparaison entre lentilles, relues contre les
  tableaux des « Critères ».
Seules remarques : N3 et N4.

## Nœuds pour Lazar
- N-dev-7 : défaut proposé, le choix du code.
- N-dev-9 : défaut proposé, le sens sévère, avec la correction de la phrase de tête.

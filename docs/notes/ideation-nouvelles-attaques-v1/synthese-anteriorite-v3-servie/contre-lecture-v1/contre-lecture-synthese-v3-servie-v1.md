# Contre-lecture — synthèse d'antériorité servie, version expurgée (v3 servie) — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le mandat `mandat-contre-lecteur-synthese-v3-servie-v1.md` (`a317b9ef68401a783eed1eda4e8b88775b548ef6f7d90f084ac18e2b1e4b8c76`, vérifié contre son compagnon, « OK »). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé. Je n'ai écrit ni la synthèse (aucune version), ni la question, ni l'ordre de course, ni leurs contre-lectures. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger.** L'expurgation est juste et complète pour les motifs du mandat (relevé à 0, rejeu identique à l'octet, tables de références intactes). Une correction est nécessaire : la v3 ajoute une phrase qui renvoie à une version interne (« la v2b en nommait quatre ») et laisse « trois fabricants » contredire « quatre lignees » de la ligne 5 (C1). Deux corrections retirent un plafond interne servi par le sens (C3, C4). Une quatrième est recommandée à la mère (C2). Avec C1, C3 et C4 appliquées : conforme, à sceller.

## 1. Pièces et empreintes (chacune vérifiée contre son compagnon : « OK »)

Dossier E = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/synthese-anteriorite-v3-servie/`.

| pièce | empreinte |
|---|---|
| E/synthese-anteriorite-pilier-attaque-v3-servie.md | `7aa7750d961dcc0191d0da6d218c73c30bd8c8901f6126dbe776393c4c638450` |
| E/remplacements-synthese-v2b-v3-servie-v1.json | `94224c2f2f6859febc9c8c50c424a22a737474bce7e0f2e94ecc1a90b1b3e913` |
| E/differentiel-synthese-v2b-v3-servie-v1.diff | `66b6e90d8342c57ab40f22e1231014e32fe96c46875aeaaef8048ecaab8dfccf` |
| E/compter_ancres_et_relever_motifs_v1.py | `d479f65b51ddd8451b9fc598cc7e3ffea067ffa01ffa8c9a3758433ee5977c71` |
| E/rapport-redacteur-synthese-anteriorite-v3-servie-v1.md | `ac88e978683333f59b281049532efb947b3932f5320ddbd817655199e5bc7200` |
| journal de l'outil, trois sorties du programme du rédacteur | « OK » contre leurs compagnons |
| v2b tirée de `origin/main` (`a43c4defd` au `fetch`) | `b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d`, égale au compagnon tiré de `origin/main` |
| mandat du rédacteur | `e4c28f8e…`, « OK » |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, « OK » |

## 2. Rejeu

L'outil, lancé sur la v2b tirée de `origin/main` avec le JSON du rédacteur : « FAIT : 28 remplacement(s) », sortie `7aa7750d…`. `cmp` avec la v3 : identiques. Mon `diff -u` v2b → v3, sans les deux lignes d'en-tête, est identique à l'octet au différentiel du rédacteur. Le JSON (28 paires) relu en entier : chaque paire ne touche qu'à un identifiant, un chemin, une règle, une empreinte, un prénom ou un nom d'espèce, sauf la paire 22 (voir C1).

## 3. Relevé (programme à moi) et lecture entière

Programme `releve_contre_lecture_v3_servie_v1.py` (écrit avec l'outil d'écriture de fichiers, lancé par son chemin), sortie `sortie-releve-contre-lecture-v3-servie-v1.txt`.

- **Motifs du mandat** : v2b (témoin positif) 18 ; v3 **0**, chacun des dix-sept à 0.
- **Motifs complémentaires sur la v3** : noms de règles 0 ; identifiants « lettres-tiret-chiffres » 0 ; « GO- » 0 ; accents graves 0 ; http 0 ; extensions de fichiers 0 ; courriels 0 ; mots des parenthèses de la ligne « Especes : » de la v2b (11 mots, tirés par le programme, masqués ; 36 occurrences dans la v2b) 0 ; liste générique de 32 noms de familles de modèles et de fournisseurs (masqués ; 18 occurrences dans la v2b) 0.
- **Mots à majuscule initiale de la v3**, relus un à un : tous sont des mots français, des auteurs, titres, revues et sigles publics, ou des étiquettes d'espèces (A à E, T1 à T3). Caractères non ASCII : guillemets, §, ¶, tiret long, une flèche, un « é » (« unilatéraux », l. 145, déjà dans la v2b).
- **Comparaison ligne à ligne** : 311 lignes des deux côtés, 23 lignes changées (4, 5, 27, 94, 116, 157, 180, 182, 200, 201, 203, 212, 226, 258, 260, 266, 290, 298, 302, 303, 304, 306, 309) ; **aucune dans les lignes 118 à 151** (tables 3.1 à 3.3 et remarque d'intégrité) **ni 159 à 176** (les quatorze éléments de la combinaison).

Lecture entière de la v3 (311 lignes) : aucun prénom, nom, session, courriel, identifiant, chemin, empreinte, nom de clé, fournisseur ni famille de modèle. Par le sens, trois points :
1. l. 266, « (la v2b en nommait quatre) » : renvoi à une version interne, illisible pour une espèce, qui signale un retrait ; et « trois fabricants » contredit « quatre lignees » (l. 5). → C1.
2. l. 258 et l. 303, « (64 jetons en reflexion) » : plafond de réflexion de la sonde de pré-vol, interne, sans rapport avec l'antériorité. Le mandat range les plafonds parmi ce qui ne doit pas se révéler. → C3, C4.
3. l. 27, « demonstration d'avant-entretien » : laisse voir un rendez-vous du directeur. → C2, à la mère.

## 4. Aucun fond changé

Aucune idée, antériorité ni référence publique ne change de sens : les sections 1 à 6 ne changent que par des retraits de parenthèses d'identifiants ou de chemins, remplacés par « familles connues », « l'etat de l'art du programme » (lectures fidèles) ; « zones vierges seduisantes verifiees plus durement » et « sur les PDF empreintes » restent. Les tables de références sont intactes (section 3). La l. 5 neuve (« cinq modeles de quatre lignees… ») est exacte au regard de la v2b (quatre fournisseurs nommés, deux espèces chez le même).

## 5. Corrections (Ancien → Neuf, texte exact de la v3 ; chaque ancre comptée à 1 par `grep -c -F -e`, et à 1 occurrence par mon programme pour C1 et C2 ; essai par l'outil : « FAIT : 4 remplacement(s) », sortie d'essai `cc7da8c9…`, dans mon dossier seulement)

- **C1 (bloquante, l. 266)** — Ancien : `de trois fabricants differents (la v2b en nommait quatre)` — Neuf : `de quatre fabricants differents`. Le compte de la v2b était une erreur de compte (elle en nommait quatre) ; « quatre » s'accorde à la l. 5 ; l'argument (artefact moins probable) ne change pas. Si la mère ne veut aucun compte touché : Neuf `de plusieurs fabricants differents`.
- **C3 (bloquante, l. 258)** — Ancien : `artefact de troncature (64 jetons en reflexion), non un refus de classifieur` — Neuf : `artefact de troncature, non un refus de classifieur`.
- **C4 (bloquante, l. 303)** — Ancien : `artefact de troncature (64 jetons en reflexion), T1-A et T2-A produits` — Neuf : `artefact de troncature, T1-A et T2-A produits`.
- **C2 (recommandée, à la mère, l. 27)** — Ancien : `La demonstration d'avant-entretien doit preserver ce temoin.` — Neuf : `Toute demonstration anterieure a la porte G1 doit preserver ce temoin.` Le titre du point (« consomme avant la porte G1 ») porte déjà le sens.

C3 et C4 tombent d'elles-mêmes si la mère retire la section 8.1 et la table des corrections (remarque 5).

## 6. Les remarques du rapport du rédacteur

1. Pas de phrase de version ni de titre neuf — **sans suite** : une version servie n'a pas besoin de ligne de version ; le nom de fichier suffit.
2. « Trois fabricants » contre quatre nommés — **à corriger** : C1.
3. « A et B d'une même lignée » — **sans suite** : sans nom, c'est le support de l'argument de 8.2 point 1 ; aucune espèce ne s'identifie par là.
4. Noms descriptifs internes gardés (collisionneur E3, étage III, runs v2.6 et v9, T100, porte G1, brèche W2, section D, session mère, sonde de pré-vol, noms d'expériences) — **sans suite**, c'est le vocabulaire même des cellules et les retirer changerait le sens ; deux exceptions trouvées par le sens : « avant-entretien » (C2, à la mère) et « 64 jetons en reflexion » (C3, C4).
5. Sections 7, 8 et table des corrections — **à la mère** (nœud « ce qui est servi »). Recommandation : garder 7, 8.2 et 8.3 (elles portent du fond : 7.1 point 4, 7.2 point 6, les changements de 8.3) ; **retirer 8.1 et la table des corrections** de la version servie : pure provenance (refus, catégories de classifieur, sonde de pré-vol, relevés de la mère), rien pour éprouver une antériorité. Confiance moyenne.
6. Colonne « Texte v2b (corrigé) » qui ne cite plus à la lettre — **à la mère**, absorbée par la remarque 5 ; si la table reste, sans suite (l'espèce n'a pas la v2b).
7. « registre du programme » — **sans suite** : description neutre, sans numéro.
8. (information) `origin/main` à `1cbbac9d1` au `fetch` du rédacteur — **sans suite** ; au mien, `a43c4defd`, v2b inchangée (`b828d800…`).

## 7. Écarts

Aucun écart au mandat. Précisions : j'ai essayé les quatre corrections par l'outil sur une copie dans mon dossier (rien dans le dépôt) ; mon programme compte aussi des motifs hors mandat (§ 3), rapportés à part.

## 8. Fichiers rendus (mon dossier, chacun avec son compagnon `.sha256`)

`contre-lecture-synthese-v3-servie-v1.md` (cette pièce) ; `releve_contre_lecture_v3_servie_v1.py` ; `sortie-releve-contre-lecture-v3-servie-v1.txt` ; `corrections-proposees-v3-servie-v1.json`. Pièces de travail sans compagnon propre : `synthese-v2b.md` et `compagnon-main-v2b.txt` (tirés de `origin/main`), `rejeu-v3-servie.md` et `essai-corrections-v3-servie.md` (compagnons et journaux écrits par l'outil), `differentiel-rejeu-v2b-v3.diff`.

— contre-lecteur neuf, modèle O

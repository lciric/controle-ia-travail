# Avis d'Argon, rapporté à la grille de lecture de G0 — annexe non opposable — v2

> **Version 2, écrite par le contre-lecteur (règle R2), non par le rédacteur de la v1.** Sous-agent neuf, Claude Opus 5.5,
> 2026-11-18 vers 05:15 UTC ; aucune dépense, aucun appel de modèle, aucune clé lue, aucun commit, aucune poussée.
> Contre-lecture : `docs/notes/quatre-lectures-inventaire-v1/contre-lecture-avis-argon-g0-v1.md` (verdict « à corriger »).
> La v1 (`avis-argon-g0-v1.md`, `833d0a45…`) reste intacte (R12). **Ce que la v2 change, et rien d'autre** :
> (1) chronologie : les réponses d'Argon datent d'entre 10:20 et 13:16 UTC le 31 octobre, la déduction tirée de 18:35 est
> retirée ; (2) DIV-4 : non nommée dans le dossier mais son objet servi ; (3) une contre-lecture CL7 de la v8 par conv-audit
> est attestée hors de `main` (§ 4, questions 14 et 15) ; (4) l'inventaire l. 149 relève de sa section C, citation avec
> marques de coupe ; (5) F-7.2 porte la source CLG2-06, pas l'étiquette [EXISTANT] ; (6) N2 devient une question
> conditionnelle ; (7) lignes de la lecture d'Argon ajoutées (l. 23, 26, 144, 162, 170, 174-176, 183, 185, 256, 261) ;
> (8) la non-indépendance sur D-G0-15 est attribuée à Fable et nuancée. Les passages changés portent la marque « [v2] ».
> Le corps qui suit, hors ces passages, est celui de la v1 ; « je » y désigne le rédacteur de la v1, sauf dans les
> passages « [v2] », où il désigne le contre-lecteur.

**Aucun critère de la porte G0 n'est changé par cette note.** Les huit critères restent ceux du brief v2 (l. 190-201), lus
selon N-027, GO-2026-11-18-01 (« au plus tard fin décembre 2026, critères inchangés »), N-063 v2 et les autres décisions de
Lazar. Rien n'est écrit dans la grille de lecture de G0, qui reste un brouillon de préenregistrement. Cette note est une
**pièce non opposable** : elle rapporte un avis de modèle (Gemini 4 Argon, de Google, « Argon » ci-dessous), tel qu'un lecteur
neuf l'a lu et recoupé le 31 octobre ; elle ne décide rien, ne recommande rien sur le fond et ne tient lieu ni de
contre-lecture R2 de la grille ni d'avis indépendant. Ce que dit Argon est **son avis, pas un fait** ; chaque affirmation
ci-dessous dit qui l'a dite et où.

- **Rédaction** : sous-agent lancé par la session mère pour les quatre lectures sans dépense de l'inventaire (autonomie
  GO-2026-11-18-05 ; « go » de Lazar aux quatre lectures, R-3168, R-3170), modèle Claude Opus 5.5. Je n'ai écrit ni la
  grille (aucune version), ni ses contre-lectures, ni les questions servies à Argon, ni sa réponse, ni la lecture du
  31 octobre. Début 2026-11-18 04:22:56 UTC (`date -u`).
- **Aucune dépense, aucun appel de modèle, aucune clé lue, aucun commit, aucune poussée.**

## Sources (branche, commit court, chemin, empreinte recalculée par `sha256sum`)

Toutes sur la branche de travail `claude/serene-keller-dasy50` (= `main`), commit `2005f3ae`. Clone superficiel
(`git rev-parse --is-shallow-repository` = `true`) : les dates de commit des fichiers ne sont pas lisibles ici.

| pièce | chemin | sha256 |
|---|---|---|
| lecture neuve des trois réponses d'Argon (Claude Fable 5.1, 2026-10-31 18:35 UTC ; « la lecture d'Argon » ci-dessous) | `docs/notes/argon-seul-v1/lecture-argon-questions-ouvertes-abc-v1.md` | `be2b3c4dca49ede519fcaf9eefcb18f2d31a753519e27b1437cc4c7dcd72448f` (égale au compagnon) |
| grille de lecture de G0, brouillon v8 (le plus récent) | `prereg/brouillon-G0-grille-lecture-v8.md` | `0c2ea83c7dc1612649f457d99c71e047fd919021b78b16c889cb42eec6658a3e` (égale au compagnon) |
| grille de lecture de G0, brouillon v7 (pour ce qui a bougé) | `prereg/brouillon-G0-grille-lecture-v7.md` | `911d79e6d2095aba8582253dbbfb984193c5f5cdac28047d3021025240f3e2cd` (égale au compagnon) |
| brief v2 (section 7, porte G0, l. 190-201) | `docs/brief-claude-code-programme-complet-v2.md` | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` |
| programme v2 (l. 180, porte G0) | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| N-063 v2, critère 3 jugé aux seules doses où la base « mots et coût » échoue | `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` |
| N-062, reconception des sondes après un échec de G1 | `docs/decisions/decision-N-062-v1.md` | `63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc` |
| N-066, garde adaptée de T0.7 pour le rendez-vous de P3-bis (lu en entier, 1 855 octets) | `docs/decisions/decision-N-066-v1.md` | `21e83ed58c7498c6…` |
| N-068, HC2 reformulée (titre et lignes 5, 34-40, 65, 70 seulement, par `grep`) | `docs/decisions/decision-N-068-v1.md` | `ba6b2db355515cd6…` |
| inventaire, sections A (l. 78), B (l. 135), C (l. 149) [v2 : la v1 rangeait la l. 149 sous B] et E (l. 163) | `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` | `b49dc2462382206d7e90eb35cac831a292f286af817399f65286a46898fd5fd0` |
| registre des GO (fichier vivant), l. 365 : GO-2026-11-18-01 | `registres/go.md` | `dd4526c43c7ba9e7…` à 04:23 UTC |
| registre des décisions (fichier vivant) : R-908 (l. 1137) [v2], R-914 (l. 1143), R-933 (l. 1162), R-2680 (l. 2640), R-3137 (l. 3197), R-3168 (l. 3258), R-3170 (l. 3262) | `registres/decisions.md` | `84f01eec5bf85c74…` à 04:23 UTC ; `45baf1d0…` à 05:10 UTC, lignes citées inchangées [v2] |
| [v2] passations du 31 octobre 13:16 (l. 60-63) et 18:10 (l. 162) | `registres/passations/2026-10-31-1316.md`, `registres/passations/2026-10-31-1810.md` | `0fcf247c422cda69…`, `3a1eac6eb9ee20da…` (égales aux compagnons) |
| [v2] état vivant, l. 175 | `registres/etat.md` | `2db3210d85eac5c7…` à 05:10 UTC |

**Extrait des branches de données** (`…/scratchpad/quatre-lectures/extrait/`) : **non utilisé** pour cette lecture. Il ne
contient ni les questions servies à Argon ni ses réponses ; aucune branche n'a été ouverte, aucun `git fetch` fait.

## Ce que j'ai lu, et pas lu

- **Lu** : la lecture d'Argon en entier (pour la découper, voir exclusions) ; la grille v8 : en-tête et tables « Ce que la
  v8 corrige » et « Ce que la v7 corrigeait », Conventions, Hypothèse, Métrique, Seuil, Plan d'analyse sections 1 et 2,
  fiches des critères 1 à 7 et début de la fiche 8, Critères de lecture gelés, Liste d'arrêt, Repli, annexes B, C, D, E ;
  la v7 par ses titres de section et par la table de la v8 qui dit ce qui a changé (dix-sept constats de la contre-lecture
  CL6 appliqués, D-G0-15 réécrit, D-G0-14 (f), D-G0-16 et DIV-5 ajoutés ; aucun critère changé) ; N-063 v2, N-062, N-066 ;
  les lignes de registre citées.
- **Pas lu** : les questions servies à Argon (`question-argon-b-v1.md` et les deux autres) et ses réponses brutes
  (`reponse-argon-v1.json`) : elles sont sur une branche de données de sauvegarde (`donnees/sauvegardes-restaurees-2026-10-31-v1`,
  dossier `1315/argon-seul/`, chemin donné par la lecture d'Argon, l. 7), ni sur `main` ni dans l'extrait. **L'avis d'Argon
  n'est donc connu ici qu'à travers la lecture de Fable 5.1** ; je ne peux recouper aucune phrase d'Argon sur son propre
  texte. Pas lus non plus : la contre-lecture CL6 et la table de dépendance de conv-audit (branche `canal/*`, interdite ; la
  grille v8 en recopie les passages utiles, annexe B) ; la fiche du critère 8 au-delà de la ligne 1000 ; le script M-8.3 ;
  les annexes F et G ; rien sous `diag/`, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test
  boîte blanche bis.

## Exclusions de cloisonnement

La lecture d'Argon mêle trois dossiers. L'inventaire range « course 2 de l'organisme et ses tours (question-mère […] ; axe 6 ;
texte III […] ; tableau partagé […] ; pré-pilote […]) » et « arène coévolutive attaque-défense P-041 (deux tours, […] ; malléabilité
D-ML-1 […]) » dans la **famille 2, évasion des moniteurs et bras d'attaque** (inventaire, section C, l. 149 ; [v2] citation
rendue avec ses marques de coupe). [v2] L'exclusion de la « note sur la pièce 5 » (l. 217) et des points 3 à 5 de la
section 5 est un classement du rédacteur de la v1, par prudence : l'inventaire ne les nomme pas. Le fichier source a été parcouru une fois en
entier avant ce découpage ; rien de ce qui suit n'est résumé, reformulé ni repris ici.

| passage de la lecture d'Argon | lignes | taille | statut |
|---|---|---|---|
| point préalable, pièces de la question A | 31-33 | 867 octets | exclue : famille 2 |
| point préalable, pièces de la question C (pièce 4 liée à l'arène) | 35 | 393 octets | exclue : famille 2 |
| section 1 entière, question A (course 2 et pré-pilote), dont les sept inexactitudes A (l. 99-109, 2 291 octets) | 41-131 | 17 261 octets | exclue : famille 2 |
| section 3, lignes de l'arène P-041, des divergences (a) à (f) et de la malléabilité | 205-213 | 2 700 octets | exclue : famille 2 |
| section 3, liaisons et note sur la pièce 5 | 215-217 | 631 octets | exclue : famille 2 |
| section 3, inexactitudes C n° 2, 3, 4 et 6 | 224-226, 228 | (dans 1 328 octets, l. 224-228) | exclue : famille 2 |
| section 3, options manquantes et points non traités (parties arène, malléabilité, pièce 5) | 231-248 (en partie) | (dans 2 271 octets) | exclue : famille 2 ; le reste (questions 6 et 7 de la recombinaison bisociative) est hors G0, non repris |
| section 5, points 1, 3, 4 et 5 | 260, 262-264 | (dans 2 363 octets, l. 258-266) | exclue : famille 2 |

Seuls servent ici : la section 2 entière (question B, porte G0, l. 134-186), le point préalable sur B (l. 34, 37), deux
lignes de la section 3 (l. 197 et 223, une confusion de nom avec la porte G0), le bilan (l. 254-256) et le point 2 de la
section 5 (l. 261). Aucune pièce de la famille 1 (conception d'organismes saboteurs discrets) n'apparaît dans ces passages.

**Réserve sur l'inventaire** (constat, sans effet) : l'inventaire présente cette lecture comme servant « la porte G0 […] et
la grille de lecture de G0 » (l. 135, l. 163) sans dire que la majeure partie de ses entrées (les 49 de la question A et les
lignes de l'arène et de la malléabilité de la question C) relève de la famille 2 qu'il exclut lui-même (l. 149). Pour G0,
seules les 15 entrées de la question B (18 objets) comptent.

## 1. Ce qu'est l'avis, et ce qu'il n'est pas

- **Objet servi à Argon** : un dossier « porte G0 » de 13 058 mots portant les points D-G0-1 à D-G0-15, les divergences
  DIV-1 à DIV-3 et les constats CL6-01 à CL6-08 (R-914, `registres/decisions.md` l. 1143), donc **la v7 et la moitié de
  CL6**. Argon n'a vu ni les constats CL6-09 à CL6-17, ni D-G0-16, ni D-G0-15 (i), ni le texte de la v8. [v2] DIV-4 n'était
  pas nommée dans le dossier (R-914 : DIV-1 à 3), mais son objet, le passage G0-1 du mémo de conv-audit, y était servi avec sa
  recommandation (lecture d'Argon, l. 34 ; grille v8 l. 1394, 1402, 1445) ; DIV-4 existe déjà dans la v7 (l. 1225,
  « consigné pour mémoire »). [v2] Selon la lecture d'Argon (l. 23, 26), la réponse B a été demandée et servie par
  `gemini-4-argon`, pour 0,6076 USD, environ 4 840 mots pour 5 000 demandés, sans trace de réflexion comptée.
- **Chronologie** [v2, corrigée] : la v8 a été finie le 2026-10-31 à 12:23:44 UTC (sa dernière ligne). Les trois réponses
  d'Argon ont été produites entre 10:20 et 13:16 UTC le même jour (passation `registres/passations/2026-10-31-1316.md`,
  l. 60-63 : « Terminé » depuis la passation de 10:20, « Non encore lues ni synthétisées »), donc peut-être avant la fin de
  la v8 ; la lecture de Fable 5.1 est de 18:35 UTC. La v1 tirait « la v8 n'a pas pu tenir compte d'Argon » de la seule date
  de 18:35, qui est celle de la lecture, non de la réponse. Ce qui établit que la v8 n'en tient pas compte : les réponses
  n'étaient pas lues à 13:16, et la v8 ne nomme pas Argon (`grep -c -i argon` = 0 dans la v7 et la v8). L'avis n'a été repris nulle part depuis (R-933 ; inventaire, l. 78 : « lue, non reprise »).
- **Indépendance limitée** (lecture d'Argon, l. 34, 37) : le dossier B gardait visibles les recommandations de conv-audit
  sur trois points (« Reco (a), 0,7 », « 0,6 », « 0,75 », sur ce que la grille nomme DIV-4, D-G0-15 / DIV-3 et D-G0-8 /
  DIV-2). Sur D-G0-8 / DIV-2 et D-G0-15 / DIV-3, l'accord d'Argon avec ces recommandations **ne se lit pas comme un avis
  indépendant**, selon la lecture d'Argon (avis de Fable 5.1). [v2] Nuance de fait sur D-G0-15 : la recommandation visible
  était celle du mémo G0-2 (a), « Cesser » (suspension jusqu'au mot de Lazar ; grille v8 l. 1446), que la table v7 a
  retirée (l. 1401) ; Argon choisit la variante D:1 (a) de la table v7, bornée (coupure, second lecteur une fois ; lecture
  d'Argon l. 154). L'accord n'est donc pas littéral. [v2] Autre limite d'indépendance (lecture d'Argon, l. 174-176) : selon
  Fable, les « options nouvelles » d'Argon sur D-G0-1 et D-G0-14 (f) reprennent les corrections CL6-01 (i)-(iv) et CL6-02,
  servies dans le dossier, et celle de D-G0-15 reprend la table v7 D:1 (a). Là où la v8 les « traite », l'accord tient à une
  source commune (CL6, table v7), non à une confirmation indépendante.
- **Tendance d'ensemble** (lecture d'Argon, l. 261, avis du lecteur Fable) : sur les quatre points où la grille propose
  « réserve » (D-G0-4, D-G0-5, D-G0-12, et (B) en réserve pour D-G0-9), Argon choisit chaque fois la condition bloquante ;
  « la lecture la plus sévère possible de la porte ». [v2] Même ligne : sur DIV-2, Argon « choisit la forme de la table
  contre la grille » ; lecture « cohérente avec la Métrique servie mais contraire au défaut de la grille sur chacun de ces
  points ».
- [v2] **Ce que la lecture d'Argon trouve de favorable** (règle R4, symétrie) : en B, vingt renvois recoupés, « aucune
  erreur de chiffre », « les écarts sont des élargissements de portée » (l. 162, 170) ; pour les trois réponses, « aucune
  pièce inventée » (l. 256).
- **État de l'art (R7)** : la section B de l'avis ne porte aucun chiffre de l'état de l'art ; aucun n'est rapporté ici.
  **Zones vierges (R8)** : aucune n'est revendiquée dans les passages repris.

## 2. Point par point : avis d'Argon (question B) rapporté à la grille v8

Colonnes : *avis d'Argon* selon la lecture d'Argon (ligne citée) ; *section v8* concernée ; *statut* : **traité** (la v8
le règle ou l'offre déjà comme option écrite), **question neuve** (la v8 ne le pose pas), **inexact** (n° de la lecture
d'Argon, § 2.2, ou n° propre à cette note, § 3), **périmé** (rendu caduc par une décision postérieure), **non indépendant**
(recommandation visible). Le défaut de la grille n'est qu'une recommandation tant que Lazar n'a pas nommé son application
(R-796 (3), grille v8 annexe B, l. 1364-1368).

| point de la grille (nom en clair, identifiant) | avis d'Argon (lecture d'Argon) | section v8 | statut |
|---|---|---|---|
| échéances, scellement de la grille et régime des défauts (D-G0-1) | option nouvelle : échéance portée par le **verdict scellé** (30 novembre, 31 janvier), ouverture quelques jours avant (24 janvier en exemple), aucune lecture tardive à la seconde lecture, un mot de Lazar couvrant dates, scellement et défauts, aucun défaut sur DIV-1 à DIV-3 (l. 140) | Seuil, « Première lecture », « Seconde lecture », « Lecture tardive », « Grille avant lecture » (l. 445-481) ; annexe B, D-G0-1 (l. 1372) | **traité** pour l'essentiel : la v8 retire la lecture tardive de la seconde lecture, exige que le mot sur D-G0-1 **nomme** l'application des défauts (iv), ôte tout défaut aux DIV, et pose « ouverture ou verdict » à Lazar (D-G0-1 (ii)). Le choix « verdict » d'Argon est une des deux options de (ii) ; il ne distingue pas ce qui relève de N-027 (lecture d'Argon, l. 182). **Périmé** sur les dates : le 30 novembre est remplacé par « au plus tard fin décembre 2026 » (GO-2026-11-18-01) ; le 15 novembre (scellement) est passé. Inexact n° B3 (nuance, l. 166) : dépassé par la v8 |
| critère 2 délégué au préenregistrement de T0.6 (D-G0-2) | option 1 (délégation), après correction CL6-08 ; conditions (a)-(d) non servies, marquées SUPPOSÉ par Argon (l. 141) | fiche du critère 2, « Latitude » (l. 727-756) ; D-G0-16 (b) | **traité** : délégation gardée, plus la condition (e) « doses non nulles distinctes » (D-G0-16 (b)). L'inquiétude d'Argon (« conditions trop faibles ») porte sur un texte qu'il n'a pas vu |
| « qui tourne » pour la base boîte noire, T0.8 (D-G0-3) | option 1 ; changerait d'avis si la part de scores finis tombait sous 95 % (seuils 50 % et 95 % propres à Argon, SUPPOSÉ ; l. 142) | fiche du critère 4, F-4.3 et « [À DÉCIDER, D-G0-3] » (l. 850, 871-876) ; annexe B (l. 1374) | **traité** : l'autre option de la v8 (plancher fixé par Lazar) couvre l'idée ; le chiffre de 95 % est d'Argon seul, sans source |
| décisions renvoyées aux critères 6 et 7, contrôle de présence (D-G0-4) | **condition** (non tenu — invalide) contre le défaut « réserve » : la Métrique de la grille appelle déjà « invalide » une « pièce scellée à laquelle manque un contenu […] exigé » (l. 143) | Métrique, ligne « non tenu — invalide » (l. 322) ; F-6.2, F-7.3 (l. 931-938, 962) ; annexe B (l. 1375) | **traité** comme option ; **question neuve** sur la cohérence : le défaut « réserve » et la définition d'« invalide » de la Métrique doivent être dits compatibles ou non. Autre question neuve (hors Argon) : la liste de D-G0-4 s'arrête aux décisions d'avant le 31 octobre (§ 4) |
| garde d'équivalence hors domaine, P-007, dans T0.6 à T0.8 (D-G0-5) | **invalide** contre le défaut « réserve » ; pire cas : un oubli dans T0.8 invaliderait le critère 4 ; changerait d'avis si la propriété était « invariante ou sans objet pour une tâche » (l. 144) [v2 : « invariante » rétabli] | fiche du critère 1, « Domaine de validité » (l. 693-698) ; annexe B (l. 1376) | **traité** comme option ; **question neuve** : l'autre option dit « invalide du critère concerné » sans dire lequel (le critère 1, où la garde est rangée, ou le critère dont les runs sortent du domaine, comme le lit Argon) ; et la garde est-elle sans objet pour T0.8, base qui ne lit pas d'activations ? (n° N3, § 3) |
| modèle et lignée du lecteur (D-G0-6) | option 1 (l. 145) | Plan d'analyse, section 1 (l. 493-494) ; annexe B (l. 1377) | **traité** |
| version suivante d'une preuve (D-G0-7) | option 1, sous CL6-02, 03, 08 ; l'autre option est contraire à R-765 (l. 146) | Plan d'analyse, section 2 (l. 524-537) ; annexe B (l. 1378) | **traité** : la v8 applique ces trois constats |
| quel verdict scellé pour quels critères (D-G0-8 et DIV-2) | forme de la table de conv-audit : verdict scellé pour les critères 1 à 5, valeur copiée et classe (l. 147) | Métrique ; M-0.5 ; annexe B, D-G0-8 et DIV-2 (l. 1379, 1400) | **non indépendant** (recommandation visible) ; **traité** comme divergence ouverte, sans défaut ; inexact n° B1 (coût sous-décrit, l. 164) ; le péril « avant le 15 novembre » qu'il cite est **périmé** |
| périmètre du critère 8 (D-G0-9) | option 2, périmètre (B) en condition ; « aucun chiffre » lu à la lettre ; les négatifs du critère 8 ne gèlent jamais (l. 148) | fiche du critère 8 (l. 976-1000) ; annexe B (l. 1380) ; annexe E | **traité** comme option ; inexact n° B4 (l. 167 : (C) ni décrit ni écarté) ; « ne gèlent jamais » est conforme à la Métrique v8 (l. 321) |
| « validés » pour les agrégateurs, T0.3 (D-G0-10) | option 1, avec la ligne de forme ancrée de CL6-07 (l. 149) | fiche du critère 5, F-5.1, F-5.2 (l. 905-913) ; D-G0-16 (a) | **traité** |
| témoin positif P4-instrument absent ou postérieur (D-G0-11) | option 1 (invalide) ; garder « invalide ne gèle pas » (l. 150) | fiche du critère 3, M-3.2, M-3.5 (l. 791, 794, 813-824) ; annexe B, D-G0-11 et DIV-5 (l. 1382, 1403) | **traité** : conforme au défaut et à la recommandation de la v8 sur DIV-5 |
| TRACE-lite absent de la base boîte noire (D-G0-12) | **absent** (lecture littérale du brief T0.8) contre le défaut « réserve » (l. 151) | fiche du critère 4, F-4.2 (l. 849, 877-880) ; annexe B (l. 1383) | **traité** comme option ; inexact n° B5 (l. 168 : analogie avec N-029 propre à Argon) |
| portée du gel au premier verdict (D-G0-13 et DIV-1) | option 1 de la grille, lecture (i) de DIV-1 (l. 152) | Plan d'analyse, section 2, « Seconde lecture et gel » (l. 538-555) ; annexe B (l. 1384, 1399) | **traité** |
| ce qui gèle un critère, précédence, cas (c) à (e) (D-G0-14) et invalidité (DIV-5) | option 1 amendée par CL6-02, 03, 06, 07, 08, plus un point (f) ; « invalide ne gèle pas », avec un nœud si l'invalidité est **volontaire** ; parade : lire le gel sur l'artefact d'arrêt du run même sans verdict (parade SUPPOSÉ ; l. 153, 175) | Métrique, « Négatif gelant » et « Ordre des sortes » (l. 325-381) ; annexe B, D-G0-14 et DIV-5 (l. 1385, 1403) | **traité** pour les amendements et le point (f) ; **question neuve** : le contournement du gel par une invalidation volontaire n'est traité nulle part dans la v8 ; [v2] **si** « l'artefact d'arrêt » d'Argon désigne `diag/<run>/arret.json`, sa parade va à l'inverse de la v8, qui lit ce fichier comme signe d'un arrêt d'instrument et **retire** alors le gel (D-G0-14 (f)) ; la lecture d'Argon ne dit pas quel artefact il vise (question N2, § 3). Inexact n° B2 (« tous », l. 165) |
| reprise après un arrêt de lecture (D-G0-15 et DIV-3) | variante (a) de la table de conv-audit (coupure, second lecteur une fois, « non franchie » sans verdict à la borne), plus une règle pour les trois causes sans ouverture : ouverture unique régularisée sur mot de Lazar, `C_lecture` au dernier commit avant l'échéance d'ouverture initiale (règle SUPPOSÉ ; l. 154, 176) | Liste d'arrêt, « Arrêt d'une lecture » (l. 1168-1183) ; annexe B, D-G0-15, DIV-3 (l. 1386, 1401) | **non indépendant** (recommandation visible) ; **traité** pour (ii) (options de la table, sans défaut, recommandation (a) de l'auteur de la v8) ; **question neuve** pour les trois causes à la première lecture : la v8 dit « nœud pour Lazar » (l. 1169-1171), Argon propose une règle écrite d'avance |
| les blocs de décision (liaisons) | quatre blocs ; le bloc « condition contre réserve » (D-G0-4, 5, 9, 12) présenté comme **une seule question de principe**, à trancher d'un coup ; premières priorités : D-G0-1 avec D-G0-15 et DIV-3, puis D-G0-13, 14 et DIV-1, puis D-G0-8 et DIV-2 (l. 156, 177) | annexe B (ordre par numéro) ; annexe C point 1 | **question neuve** de présentation : la v8 ne regroupe pas ces quatre points |
| effet des constats CL6 sur chaque décision | sens changé pour D-G0-1, 8, 13, 14, 15 ; indirect pour 2, 7, 10, 11 ; aucun pour 3, 4, 5, 6, 9, 12 (l. 158) | table « Ce que la v8 corrige » (l. 164-182) | **traité** : la v8 applique les dix-sept constats |

**Ce qu'Argon n'a pas traité** (lecture d'Argon, l. 181-186), rapporté à la v8 : le « défaut de plus » de DIV-1 et DIV-2 est
réglé par la v8 (« sans mot de Lazar, la grille n'est pas scellée », l. 1392) ; l'ambiguïté de N-027 pour la première
lecture est posée en D-G0-1 (ii) ; la règle de transition est décrite (l. 361-365) et son compte renvoyé à l'annexe G ; la
question du critère 4 lu sur un « rapport de fonctionnement » (grille) ou sur un « verdict scellé » (table) pour une preuve
de T0.8 déjà existante reste ouverte avec DIV-2. [v2] Deux lignes que la v1 ne rapportait pas : Argon ne dit pas que ses
choix sur D-G0-1 et D-G0-9 règlent aussi les choix 3 et 7 de la synthèse du repli, « comme la pièce l'indique » (l. 185) ;
or la v8 met les onze choix restants du repli à l'ordre du jour avec les D-G0 (annexe C point 1, l. 1463-1464) ; et un
passage tronqué de CL6-01 dans le dossier servi n'a pas été signalé par Argon (l. 183), fait qui touche l'objet servi.

**Hors question B, une seule ligne touche G0** : dans la question 6 de la recombinaison bisociative, Argon écrit qu'attendre
« G0 (c) » bloquerait la question 6 sur la question 7 (lecture d'Argon, l. 197) ; c'est l'inexactitude C n° 1 (l. 223) :
l'option (c) visait la porte G0 du programme, Argon la confond avec la « porte G0 » propre à la question 7, autre objet de
même nom. Elle ne touche pas la grille, mais montre un risque de nom (question 17, § 5).

## 3. Inexactitudes

**Les dix-huit de la lecture d'Argon** (l. 254-255), réparties :

| n° (lecture d'Argon) | objet | rapport à G0 |
|---|---|---|
| A 1 à A 7 (l. 99-109) | question A | exclue : famille 2 (`docs/notes/argon-seul-v1/lecture-argon-questions-ouvertes-abc-v1.md`, l. 99-109, 2 291 octets) |
| B 1 (l. 164) | coût de la forme « valeur copiée et classe » sous-décrit : elle toucherait aussi les critères 1, 2, 3 | DIV-2 : à porter au chiffrage de cette option (question 12) |
| B 2 (l. 165) | « tous les négatifs par table » : trop large | D-G0-14 (e) : la v8 borne bien la règle aux verdicts scellés après la grille (l. 358-365) ; sans effet |
| B 3 (l. 166) | omission de précision prise pour une omission d'exigence | D-G0-1 (iv) : réglé par la v8 |
| B 4 (l. 167) | (C) retenu ou écarté sans le dire | D-G0-9 : reste à Lazar |
| B 5 (l. 168) | analogie avec N-029 propre à Argon | D-G0-12 : sans effet sur les options |
| C 1 (l. 223) | confusion entre la porte G0 du programme et la « porte G0 » de la question 7 | nom (question 17) |
| C 2, C 3, C 4, C 6 (l. 224-226, 228) | question C | exclue : famille 2 (même fichier, dans l. 224-228, 1 328 octets) |
| C 5 (l. 227) | question 7 de la recombinaison bisociative | hors G0 |

**Celles que je trouve**, en rapportant l'avis à la v8 et aux décisions postérieures (aucune n'est une erreur sur les faits
servis à Argon, qu'il ne pouvait pas connaître ; ce sont des écarts à l'état présent) :

- **N1, dates périmées** : l'avis place la première échéance au 30 novembre et le scellement de la grille avant le
  15 novembre. GO-2026-11-18-01 (`registres/go.md` l. 365) remplace la fin novembre de N-027 par « au plus tard fin
  décembre 2026 » ; le 15 novembre est passé. Je n'ai trouvé au registre aucun mot de Lazar sur D-G0-1 (recherche
  `grep -n -E "D-G0-1[^0-9]" registres/decisions.md` : dernière occurrence à R-914, l. 1143) ; la v8 dit qu'alors « la
  grille n'est pas scellable et la session ouvre un nœud » (l. 479-481).
- **N2, parade peut-être contraire à la v8** [v2 : question, non inexactitude établie] : lire le gel « sur l'artefact
  d'arrêt du run même sans verdict » (avis, l. 153) ferait geler sur les arrêts d'instrument **si** cet artefact est
  `diag/<run>/arret.json`, écrit par une garde d'arrêt d'instrument (v8 l. 339-345 ; annexe D, l. 1531-1535), cas que la v8
  traite comme « pas de négatif gelant » (D-G0-14 (f)). La lecture d'Argon ne dit pas quel artefact Argon vise ; s'il
  s'agit d'une trace de liste d'arrêt sur résultat, la contradiction tombe. À poser comme question (question 10).
- **N3, critère visé par l'autre option de D-G0-5** : Argon lit « invalide le critère 4 » ; la grille écrit « non tenu —
  invalide du critère concerné » (annexe B, l. 1376) et range la garde sous le critère 1 (l. 693-698). La lecture d'Argon
  est possible mais n'est pas écrite ; l'ambiguïté est dans la v8.
- **N4, seuils propres non marqués** : 95 % (D-G0-3) est donné sans marque SUPPOSÉ (relevé par la lecture d'Argon,
  l. 256) ; [v2] pour 50 %, c'est une inférence : la l. 256 énumère où Argon a posé ses marqueurs, et 50 % n'y figure pas.

## 4. Ce que la prochaine version doit prendre en compte hors de l'avis (décisions postérieures à la v8)

Ces points ne viennent pas d'Argon ; ils sont posés par des décisions ou des constats datés après le 31 octobre, que ni la
v8 ni Argon n'ont vus.

- **GO-2026-11-18-01** (2026-11-18, `registres/go.md` l. 365 ; R-3137, `registres/decisions.md` l. 3197) : porte « au plus
  tard fin décembre 2026, critères inchangés ». La v8 est écrite sur les dates du 15 novembre (scellement), du 30 novembre
  (première lecture) et du 31 janvier 2027 (verdict de la seconde lecture, R-750, R-765). N-063 v2 écrit encore « la date de
  G0 (fin novembre, N-027) » dans « Ce qui ne change pas » : c'est désormais périmé.
- **N-063 v2** (8 novembre) : le critère 3 « n'est jugé qu'aux doses où la base « mots et coût » échoue » ; aux autres
  doses, « sans objet » ; si aucune dose ne qualifie, « sans objet à cette course », et « la porte G0 lit le critère 3 comme
  non tenu à cette course ». La fiche du critère 3 de la v8 ne porte ni ce filtre ni cet état (constaté aussi par la carte
  de la porte G0, R-2680, l. 2640 : « grille […] ignore N-063 v2 et P3-bis »).
- **N-066** (9 novembre) : si T0.7 est scellé avec la garde adaptée, une ouverture réduite de la seule issue de P3-bis est
  permise avant les lignes de scores de T0.7, avec une réserve écrite. La v8 ne nomme ni P3-bis ni cette garde.
- **N-062** (8 novembre) : un échec de G1 ouvre des cycles de reconception, « chaque cycle a son préenregistrement court ».
  Elle ne figure pas dans la liste des décisions renvoyées au préenregistrement de G1 (D-G0-4, l. 1375 ; F-6.2, l. 937).
- **N-068** (HC2 reformulée) : « ce qui n'est plus revendiqué : la robustesse sous attaque par contenu d'une sonde […] au
  sens d'une absence d'évasion à seuil. Elle est publiée (MIRAGE) » (l. 70, lu par `grep` seulement). Le contrôle F-7.2 de
  la v8 (source « CLG2-06 » ; [v2] la v1 le disait « étiqueté [EXISTANT] », étiquette qui est sur F-7.1, l. 960 ; le mot
  vient du livrable du brief T0.9, grille l. 948-949, brief l. 188) exige le mot « robustesse » pour HC2 (l. 961) ; la liste F-7.3 s'arrête à
  N-005/N-006, N-013, N-023, R-307, R-309 (l. 962).
- **Préalables de l'annexe C point 1 non remplis à ce jour** (constat par `ls`, R11 : à confirmer avant de s'y fier) :
  aucune contre-lecture CL6 sous `prereg/contre-lectures/` (seules CL1 à CL5 y sont) ; aucune contre-lecture CL7 de la v8
  **versée sur `main`** ; aucune grille scellée `prereg/G0-grille-lecture-vN.md`.
- [v2] **Une CL7 de la v8 est attestée hors de `main`**, par conv-audit, autre lignée que celle de la v8 (R-908,
  `registres/decisions.md` l. 1137 : « CL7 à confier à une autre lignée (conv-audit) ») : passation du 31 octobre 18:10
  (`registres/passations/2026-10-31-1810.md`, l. 162 : « CL7 de la grille G0 v8 (nœuds N-1 à N-4 pour Lazar, dont la date
  de G0 ») ; état vivant (`registres/etat.md`, l. 175 : « nœuds CL7 de conv-audit (date de G0, D-G0-14, D-G0-16, D-G0-1) »,
  parmi les décisions attendues de Lazar). Elle n'a pas été lue (branche `canal/*`, interdite) ; ses quatre nœuds touchent
  les questions 1, 3, 10 et 14 ci-dessous.

## 5. Questions que la prochaine version de la grille devrait trancher (ou porter à Lazar)

Toutes touchent la porte : ce sont des nœuds (CLAUDE.md, « Nœuds de décision »), sans défaut (R-796 (3)). Aucune ne change
un critère ; celles qui y toucheraient sont marquées.

1. **Nouvelles échéances.** Date de scellement de la grille, date de la première lecture, et ce que « au plus tard fin
   décembre 2026 » borne : l'ouverture ou le verdict scellé (D-G0-1 (i) à (iii), reportés sur la date nouvelle). —
   Provenance : GO-2026-11-18-01 ; grille v8, Seuil (l. 445-481) ; avis d'Argon (choix « verdict », lecture d'Argon l. 140).
2. **Le report et sa borne.** La borne du verdict final du 31 janvier 2027 (R-750, R-765) est-elle gardée, le report
   passant de deux mois à un, ou déplacée elle aussi ? Avec l'option (a) de D-G0-15 (ii), coupure des preuves au 24 janvier,
   le report utile se réduit encore. Seul un mot de Lazar peut modifier R-750 ou R-765. — Provenance : GO-2026-11-18-01
   (muet sur le report) ; grille v8 l. 452-458, 1176-1183 ; avis d'Argon sur D-G0-15 (l. 154).
3. **Le scellement manqué du 15 novembre.** La v8 dit la grille non scellable sans mot sur D-G0-1 à cette date et demande
   l'ouverture d'un nœud (l. 479-481) ; aucun mot trouvé au registre. La prochaine version doit remplacer cette date et
   dire ce que devient la règle « sans grille scellée à l'échéance, la lecture ne s'ouvre pas ». — Provenance : grille v8 ;
   § 3, N1.
4. **Le critère 3 selon N-063 v2.** Écrire le filtre par dose (lecture mécanique du résultat de la base « mots et coût »
   de T0.6, dose par dose) ; donner à « sans objet à cette course » un sous-état de la Métrique (absent, négatif, non
   concluant ?), avec son effet sur le gel (seul un négatif gelant gèle) et sur le choix 2 du repli ; dire comment le filtre
   s'applique à la famille (i), N-063 ne nommant que les doses de (ii). — Provenance : N-063 v2, points 1 et 2 ; R-2680 ;
   l'avis d'Argon est muet (antérieur).
5. **La garde adaptée de T0.7 et P3-bis.** Dire comment le lecteur lit un T0.7 scellé avec cette garde (réserve écrite à
   recopier ; ordre R1 contrôlé par M-3.2 et M-0.4) et si l'interdit de lecture de la section 1 doit nommer les pièces de
   P3-bis. — Provenance : N-066, point 1 ; R-2680.
6. **Les listes de décisions renvoyées aux critères 6 et 7.** Ajouter, ou écarter en le disant, les décisions postérieures
   au 31 octobre qui touchent le préenregistrement de G1 (N-062 ; et les autres du `CLAUDE.md`, à vérifier une à une) et
   celui du papier C (N-068). — Provenance : grille v8 annexe B, D-G0-4 (l. 1375) ; N-062, point 4 ; N-068.
7. **HC2 après N-068.** Le contrôle F-7.2 (« robustesse », « jamais immunité absolue ») reste-t-il applicable à une HC2
   reformulée qui ne revendique plus la robustesse à seuil ? **Touche la lecture du critère 7 par sa source** (brief T0.9) :
   à Lazar. — Provenance : N-068 l. 70 ; grille v8 F-7.2 (l. 961).
8. **« Condition » ou « réserve », d'un seul tenant.** Trancher ensemble D-G0-4, D-G0-5, D-G0-9 (périmètre (B)) et D-G0-12,
   et dire si le défaut « réserve » est compatible avec la définition d'« invalide » de la Métrique (« contenu […] que le
   critère, sa source ou cette grille exige »). — Provenance : avis d'Argon (l. 143, 156, 177 ; tendance l. 261) ; grille v8
   l. 322.
9. **L'autre option de D-G0-5.** Nommer le critère qui devient « invalide » (le critère 1 ou celui dont les runs sortent du
   domaine) ; dire si la garde d'équivalence est sans objet pour T0.8. — Provenance : avis d'Argon (l. 144) ; § 3, N3 ;
   grille v8 l. 693-698, 1376.
10. **L'invalidation qui échapperait au gel.** Sous la lecture « invalide ne gèle pas » (DIV-5, recommandation de la v8),
    une preuve négative rendue invalide (contre-lecture omise, par exemple) ne gèle rien. Faut-il une règle, et laquelle,
    sachant que l'intention (« volontaire ») ne se lit pas mécaniquement (R13 : le lecteur compte) et que la parade d'Argon
    contredirait D-G0-14 (f) si elle vise `arret.json` [v2] ? Un des nœuds de la CL7 de conv-audit porte sur D-G0-14 [v2]. — Provenance : avis d'Argon (l. 153, 175) ; § 3, N2 ; grille v8 l. 339-345, 1403 ; table de
    conv-audit D:5 (c) « invalide gelé » (recopiée l. 1427).
11. **Les trois causes sans ouverture, à la première lecture.** Garder « nœud pour Lazar » ou écrire d'avance une règle
    (Argon : ouverture unique régularisée sur mot de Lazar, `C_lecture` au dernier commit avant l'échéance initiale). —
    Provenance : avis d'Argon (l. 154, 176 ; règle SUPPOSÉ) ; grille v8 l. 1169-1171.
12. **Le coût de la forme « valeur copiée et classe ».** Si DIV-2 penche vers la table, chiffrer ce qu'elle change pour les
    critères 1, 2, 3 et 5 (M-0.5, F-5.x) et pour une preuve de T0.8 déjà rendue en « rapport de fonctionnement ». L'accord
    d'Argon n'est pas indépendant. — Provenance : inexactitude B 1 (l. 164) ; lecture d'Argon l. 186 ; grille v8 l. 1400.
13. **Plancher de la part de scores finis** (autre option de D-G0-3) : le retenir ou l'écarter, sans reprendre le 95 %
    d'Argon, qui n'a pas de source. — Provenance : avis d'Argon (l. 142) ; § 3, N4 ; grille v8 l. 1374.
14. **Ce qu'Argon n'a pas vu.** [v2, corrigée] D-G0-16, D-G0-15 (i) et les constats CL6-09 à CL6-17 n'ont pas été servis à
    Argon (DIV-4 ne l'a été que sous le nom G0-1 du mémo). La CL7 de conv-audit, attestée hors de `main`, porte au moins
    un nœud sur D-G0-16 (`registres/etat.md` l. 175) ; ce qu'elle dit de D-G0-15 (i) et de CL6-09 à 17 n'est pas connu ici.
    La prochaine version de la grille doit recopier ses nœuds et dire ce qui reste sans aucun regard extérieur à la lignée
    de la v8. — Provenance : R-914 (objet servi) ; grille v8 annexe D (l. 1536-1537) ; passation 2026-10-31-1810 l. 162.
15. **Les préalables.** Verser CL6 **et la CL7 de conv-audit** sur `main` [v2 : la v1 disait « faire CL7 »], trancher ses
    nœuds N-1 à N-4, exécuter les dossiers synthétiques, produire le différentiel mécanique avant scellement (annexe C
    point 1). — Provenance : grille v8 l. 1462-1473 ; § 4 ; passation 2026-10-31-1810 l. 162.
16. **Mise à jour des renvois de date dans les décisions.** N-063 v2 (« date de G0 : fin novembre ») et la grille citent
    N-027 sous sa forme d'avant GO-2026-11-18-01 ; la version suivante doit citer la décision en vigueur. — Provenance :
    N-063 v2, « Ce qui ne change pas » ; GO-2026-11-18-01.
17. **Le nom de la porte.** Écrire « porte G0 du programme (prêt pour G1) » dans la grille et dans tout dossier servi à un
    modèle, pour éviter la confusion avec la « porte G0 » de la question 7 de la recombinaison bisociative (règle de
    nommage R-3044, R-3085). — Provenance : inexactitude C 1 (lecture d'Argon l. 223).

## 6. Réserves de cette note

- L'avis d'Argon n'est lu qu'au second degré, à travers la lecture de Fable 5.1 ; ni la question servie ni la réponse brute
  n'ont été ouvertes (branche de données non extraite). Une phrase attribuée ici à Argon est une phrase de cette lecture.
- La lecture d'Argon renvoie à des lignes de la v7 et de CL6 que je n'ai pas toutes recoupées ; les correspondances de la
  table du § 2 sont faites sur la v8 seule.
- N-068 n'est lu que par `grep` (titre, l. 5, 34-40, 65, 70) ; la question 7 ci-dessus est à confirmer sur son texte entier.
- Les registres `registres/decisions.md` et `registres/go.md` sont vivants ; leurs empreintes sont celles de 04:23 UTC.
- Les constats d'absence (CL6, CL7 sur `main`, grille scellée, mot sur D-G0-1) reposent sur `ls` et `grep` dans un clone
  superficiel ; R11 : à vérifier avant d'en tirer une conséquence. [v2] Le constat « aucune CL7 » de la v1 était démenti par
  les registres (§ 4) : ce genre d'absence se vérifie aussi dans les passations et l'état, pas seulement par `ls`.

Fin de la note. Aucune recommandation sur le fond ; aucun critère changé. [v2] Version 2 du contre-lecteur, mêmes limites.

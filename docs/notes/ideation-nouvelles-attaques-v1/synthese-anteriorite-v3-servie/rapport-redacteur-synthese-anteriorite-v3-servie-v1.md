# Rapport du rédacteur — synthèse d'antériorité servie, version expurgée (v3 servie) — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le mandat `mandat-redacteur-synthese-anteriorite-expurgee-v1.md` (`e4c28f8e235fb4c96a96f3fe3e47fdf9b060e133a424dbe136509d48d15b8ace`, vérifiée contre son compagnon, « OK »). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, rien d'ajouté au fond. Je n'ai écrit ni la synthèse, ni la question, ni l'ordre de course. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**Version neuve écrite, relevé à 0, à contre-lire par un autre modèle puis à sceller par la mère.** Vingt-huit remplacements par l'outil contre-lu ; les 18 occurrences des motifs du mandat et les 40 occurrences des motifs complémentaires de la v2b tombent à 0 dans la v3. Aucune idée, aucune antériorité, aucune référence publique n'est touchée : les sections 3.1, 3.2 et 3.3 (tables des références) sont hors de tout hunk du différentiel.

## 1. Pièces et empreintes

Dossier D = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-synthese-anteriorite-v3/`.

| pièce | empreinte |
|---|---|
| source : synthèse v2b tirée de `origin/main` par `git show … >` (`D/synthese-v2b.md`) | `b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d`, égale au compagnon tiré de `origin/main` (`D/compagnon-main-synthese-v2b.sha256.txt`) |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `D/remplacements-synthese-v2b-v3-servie-v1.json` | `94224c2f2f6859febc9c8c50c424a22a737474bce7e0f2e94ecc1a90b1b3e913` |
| `D/synthese-anteriorite-pilier-attaque-v3-servie.md` | `7aa7750d961dcc0191d0da6d218c73c30bd8c8901f6126dbe776393c4c638450` (compagnon, journal et compagnon du journal écrits par l'outil) |

Les empreintes des autres fichiers rendus sont dans leurs compagnons.

## 2. Relevé avant (v2b)

Programme `D/compter_ancres_et_relever_motifs_v1.py` (bibliothèque standard ; écrit avec l'outil d'écriture de fichiers ; lancé par son chemin), sortie `D/sortie-releve-motifs-avant-v2b-v1.txt`. Il sert de témoin positif.

- Motifs du mandat, 18 : prénom du directeur, 2 (l. 258, 304) ; « R- » suivi de chiffres, 7 (l. 27, 94, 200, 258, 302, 303) ; « N- » suivi de chiffres, 2 (l. 27, 200) ; `controle-ia`, 3, et `docs/`, 3 (l. 116, 157, 201) ; une empreinte (l. 298). Égal, ligne pour ligne, au relevé du contre-lecteur de la question v4.
- Motifs complémentaires, 40 : noms de règles (R7, R8, R12), 8 (l. 116, 157, 180, 182, 203, 290, 298) ; noms de fournisseurs, de familles de modèles ou de clés, 32 (l. 5, 212, 226, 258, 260, 266, 306, 309). Ces noms ne sont écrits nulle part dans mon programme : il les tire de la ligne « Especes : » de la v2b et les masque à l'affichage. La l. 226 (un nom de famille de modèle dans un titre) n'était pas dans le relevé du contre-lecteur ; elle est traitée.
- Sans témoin positif dans ce fichier (0 avant, 0 après) : nom de famille du directeur, `session_`, `@`, `GO-20`, nom du compte distant, `github`, `prereg/`, `registres/`, `donnees/`, `CLAUDE.md`, noms de clés en majuscules terminés par `_KEY` ou `_TOKEN`.

## 3. Remplacements (28)

Chaque ancre comptée à 1 par `grep -c -F -e` (28 appels, un par ancre) et par le mode « ancres » du programme (`D/sortie-compte-ancres-v1.txt` : « 0 ancre hors exactement une »), avant l'appel. Sortie de l'outil : « FAIT : 28 remplacement(s) ».

| rang | ligne | nature | lecture |
|---|---|---|---|
| 1 | 4 | nom du dossier du run | « run v9 du collisionneur » |
| 2 | 5 | noms de modèles, de fournisseurs, de clé | « A, B, C, D et E, cinq modeles de quatre lignees (A et B d'une meme lignee ; C, D et E de trois autres lignees) » : garde le seul fait qui sert l'argument de la section 8.2 |
| 3, 4 | 27 | identifiants de registre | parenthèses retirées ; « mode tenu a l'ecart » et « familles connues » restent |
| 5 | 94 | identifiant de registre | parenthèse retirée |
| 6, 7, 11 | 116, 157, 201 | chemin du dépôt, noms de règles | « l'etat de l'art du programme » ; l'exigence « sur les PDF empreintes » reste |
| 8, 9 | 180, 182 | nom de règle | retiré ; l'énoncé cité « zones vierges seduisantes verifiees plus durement » reste |
| 10 | 200 | identifiants de registre | « des familles connues, du mode tenu a l'ecart et de la breche W2 » (lecture de « familles R-610 » prise à la l. 27 : « les familles connues (R-610) ») |
| 12, 22 | 203, 290 | nom de règle | retiré ; « verification sur PDF empreinte » et « verifiees sur piece » restent |
| 13, 14 | 212, 226 | nom de clé, nom de famille de modèle | titres « Ce que D apporte », « Ce que E apporte » |
| 15, 17, 19 | 258, 260 | noms de modèles et de fournisseurs | « L'espece A », « L'espece B », « D et E » |
| 16 | 258 | identifiant de registre | retiré |
| 18, 26 | 258, 304 | prénom du directeur | « ordre du directeur du programme » (contraction de « de le ») |
| 20, 21 | 266 | noms de fournisseurs | « (un meme fabricant pour A et B, un autre pour C) » ; « (la v2b en nommait quatre) » — voir remarque 2 |
| 23 | 298 | empreinte, nom de règle | « La v2 est conservee intacte. » |
| 24, 25 | 302, 303 | identifiants de registre | colonne « Source » : « releve mere », « registre du programme » |
| 27, 28 | 306, 309 | noms de modèles et de fournisseurs dans la table des corrections | mêmes désignations qu'aux l. 258, 260 et 266 |

## 4. Relevé après (v3)

Sortie `D/sortie-releve-motifs-apres-v3-servie-v1.txt` : **motifs du mandat, total 0** (chacun des dix-sept à 0) ; **motifs complémentaires, total 0** (noms de règles 0 ; noms de fournisseurs, de familles de modèles ou de clés 0). Différentiel : `D/differentiel-synthese-v2b-v3-servie-v1.diff` (`diff -u`, relu en entier ; 311 lignes des deux côtés, 23 lignes changées).

## 5. Noms de fournisseurs gardés comme références publiques, cas par cas

- **Aucun nom de fournisseur ni de famille de modèle de l'organisme n'est gardé.** Aucun ne figurait dans une référence bibliographique : les neuf mots de la ligne « Especes : » n'apparaissaient que dans la composition de l'organisme (l. 5, 212, 226, 258, 260, 266) et dans la table des corrections (l. 306, 309).
- **Gardés, comme références publiques** (aucun n'est un fournisseur des espèces) : les organismes d'évaluation nommés à la section 5 comme travaux à vérifier (METR, deux fois ; Apollo Research ; Redwood Research) ; les auteurs, titres, revues et numéros d'articles des sections 3.1 à 3.3 et 1.7 (dont « Neural Chameleons », ROME, EMNLP, *Review of Economic Studies*) ; les sigles de méthodes publiques (CCS, RepE, TOST, SPRT, Hedge).

## 6. Remarques

1. **Pas de phrase de version ni de titre neuf.** Le mandat dit que la v3 porte les remplacements « et rien d'autre » : le titre, la date et le titre « Table des corrections v2 → v2b » sont ceux de la v2b. La version se lit au nom du fichier. Si la mère veut une phrase de version, c'est une ligne d'en-tête de plus, hors de la partie servie.
2. **Incohérence de la v2b, gardée.** La l. 266 dit « trois fabricants differents » et en nommait quatre. Je n'ai pas corrigé « trois » (ce serait toucher au fond) ; la parenthèse « (la v2b en nommait quatre) » garde le fait sans les noms. La l. 5 neuve dit « quatre lignees », d'après les noms que la v2b y donnait. À trancher par la mère ou le contre-lecteur.
3. **Composition de l'organisme.** La v3 dit encore que A et B sont d'une même lignée : c'est le support de l'argument de la section 8.2 (une convergence peut refléter un accord entre fabricants). Si même cela ne doit pas être servi, il faut retirer la section 8.2, point 1, ce qui touche au fond : nœud hors de ce mandat.
4. **Noms descriptifs internes gardés**, parce qu'ils ne sont ni des identifiants de registre ni des chemins et que les retirer changerait le sens : « collisionneur E3, etage III », « run v2.6 », « run v9 », « T100 », « porte G1 », « breche W2 », « section D des faits du programme », « session mere », « sonde de pre-vol », les noms d'expériences des espèces (E0', X0, fiche O…). Aucun ne répond aux motifs.
5. **Sections de provenance interne.** Les sections 7, 8 et la table des corrections restent dans la v3, expurgées. Le contre-lecteur de la question v4 les dit « de la provenance interne » ; la section 8.1 parle de refus et de catégories de classifieur des espèces. Les servir ou non est le nœud « ce qui est servi », pas le mien.
6. **Citations de la table des corrections.** Aux l. 306 et 309, la colonne « Texte v2b (corrige) » ne cite plus la v2b à la lettre, puisque les noms y sont remplacés.
7. **« registre du programme »** (l. 303, colonne « Source ») remplace un identifiant seul : description neutre, sans numéro.
8. `origin/main` était à `1cbbac9d1` au `fetch`. `diff` a rendu le code 1 (fichiers différents), ce qui est attendu.

## 7. Écarts

Aucun écart au mandat. Une précision : en plus des 28 comptes par `grep -c -F -e`, les ancres ont été comptées par mon programme (occurrences à l'octet, comme l'outil).

## 8. Fichiers rendus (dossier D, chacun avec son compagnon `.sha256`)

`synthese-anteriorite-pilier-attaque-v3-servie.md` (et son journal) ; `remplacements-synthese-v2b-v3-servie-v1.json` ; `compter_ancres_et_relever_motifs_v1.py` ; `sortie-compte-ancres-v1.txt` ; `sortie-releve-motifs-avant-v2b-v1.txt` ; `sortie-releve-motifs-apres-v3-servie-v1.txt` ; `differentiel-synthese-v2b-v3-servie-v1.diff` ; `synthese-v2b.md` et `compagnon-main-synthese-v2b.sha256.txt` (tirés de `origin/main`) ; ce rapport.

— rédacteur neuf, modèle F

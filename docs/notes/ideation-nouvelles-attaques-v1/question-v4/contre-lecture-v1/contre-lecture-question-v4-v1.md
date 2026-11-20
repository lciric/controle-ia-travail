# Contre-lecture — question de la course « nouvelles attaques », différentiel v3 → v4 (sans nom ni donnée interne servie) — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le mandat `docs/notes/ideation-nouvelles-attaques-v1/question-v4/mandat-contre-lecteur-question-v4-v1.md` (`73aa9466f9fc1fdb11738a7a5a6a9e2a773f9888c8b6216d361abdddbabc5b8b`, vérifiée contre son compagnon). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Aucune méthode d'attaque, aucun procédé, aucun identifiant de modèle. Je n'ai écrit aucune version de la question, de l'ordre de course, du préenregistrement court, du devis, ni leurs contre-lectures.

## 0. Verdict

**Conforme, à sceller.** Aucune correction.

1. Le rejeu de l'outil sur la v3 avec le JSON rend la v4 à l'octet (`cmp` muet ; même empreinte `47160d37…`). Le différentiel refait est égal à celui du rédacteur, hors la ligne d'en-tête `+++` (chemin et heure du fichier).
2. Dans les § 2 à § 7 de la v4, mon programme ne trouve **aucune** occurrence des motifs du mandat ni de mes motifs complémentaires. Tout ce qui reste est dans l'en-tête et le § 1, que la v4 elle-même dit « pas à servir ».
3. Aucune règle de fond n'est changée : les treize remplacements de fond gardent le sens de leur phrase ; les trois énoncés dont le nom de règle est retiré sont présents, une fois chacun ; le § 4 est égal à l'octet (et le § 1 aussi) ; les colonnes « axe » et « valeurs » de la table des axes du § 5 sont égales, donc la numérotation des cases du préenregistrement court ne bouge pas.
4. **Deux nœuds restent hors de la v4** : ce qui est servi, et comment (remarques 1 et 2 du rapport) ; la version neuve du préenregistrement court qu'exige, à la lettre, une question d'une autre empreinte, avec la question de la racine des graines (remarque 6). La pièce d'antériorité servie ne peut pas partir telle quelle (remarque 9).

## 1. Pièces lues et empreintes vérifiées

Dossier N = `docs/notes/ideation-nouvelles-attaques-v1/`. Chaque compagnon vérifié par `env -C DOSSIER sha256sum -c F.sha256` (« OK ») et chaque valeur recalculée, égale au préfixe donné par le mandat.

| pièce | empreinte |
|---|---|
| `N/mandat-redacteur-question-v4-sans-donnees-internes-v1.md` | `50d8300be854c7487557e21cce1db7f1693bd6fc225b615295f446a0b5fd373c` |
| `N/conception-v3/question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` |
| `N/question-v4/question-course-nouvelles-attaques-v4.md` | `47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654` |
| `N/question-v4/remplacements-question-v3-v4-v1.json` | `0a0b0f5b1d17135da18bbb596fc94d091acfa339837a64e86a7e3d9c50bc72d6` |
| `N/question-v4/question-course-nouvelles-attaques-v4.md.journal-remplacements-v1.json` | compagnon « OK » ; il porte cible `2cf2aae0…`, JSON `0a0b0f5b…`, sortie `47160d37…`, seize remplacements |
| `N/question-v4/differentiel-question-v3-v4-v1.diff` | `6f36eeaac0e99b6a80ba6bd4444476d8a6d2410ca77c769b06d95166c0031e77` |
| `N/question-v4/sortie-grep-prenom-nom-question-v4-v1.txt` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `N/question-v4/rapport-redacteur-question-v4-v1.md` | `6bed22dd3673da1f3cb447a15d99052350b52197143f793855b78185494b3485` |
| `N/conception-v3/ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` |
| préenregistrement court v6, tiré par `git show origin/main:prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v6.md > …` | `7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5`, égale au compagnon de `origin/main` ; scellé par le commit `9af7555b6` (2026-11-20T10:48:02Z, « préenregistrement court v6 et devis v4 scellés », R-4206) |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` (remarque 9 ; relevée par motifs, non lue) | `b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d` |

## 2. Rejeu

- Commande : l'outil, par son chemin, `--cible` la v3, `--remplacements` le JSON du dossier `question-v4/`, `--sortie` `rejeu/question-v4-rejouee.md`. Sortie : « FAIT : 16 remplacement(s) ; cible 2cf2aae0… → … (47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654) ». L'outil compte lui-même chaque texte ancien à exactement une occurrence (sa règle 2) et chaque texte neuf à une de plus (règle 5) : le rejeu sans refus vaut ce compte.
- `cmp rejeu/question-v4-rejouee.md N/question-v4/question-course-nouvelles-attaques-v4.md` : muet, code 0.
- Différentiel refait (`diff -u` v3 → v4 rendue, `rejeu/differentiel-refait-v3-v4.diff`) : `cmp` avec celui du rédacteur s'arrête à la ligne 2, l'en-tête `+++`, qui nomme le fichier de sortie (son dossier à lui, le dossier du dépôt chez moi) et son heure. Les lignes 3 à 63, hunks compris, sont égales (relues en entier des deux côtés).
- Seize zones : trois de tenue (titre ; phrase de version de la v4 ajoutée ; statut) et treize de fond (§ 2 : quatre ; § 3 : cinq ; § 5 : deux ; § 6 : une ; § 7 : une).

## 3. Aucune donnée interne dans ce qui peut être servi

Programme : `releve_motifs_question_v4_v1.py` (bibliothèque standard ; écrit avec l'outil d'écriture de fichiers ; lancé par son chemin). Il découpe en sections (en-tête, puis chaque titre « ## »), cherche les motifs du mandat — prénom et nom de famille du directeur du programme (sans accents, casse repliée), `session_`, `@`, `R-` suivi de chiffres, `GO-20`, `N-0`, nom du compte distant, `github`, `controle-ia`, `docs/`, `prereg/`, `registres/`, `donnees/`, hexadécimal de 16 caractères et plus, `CLAUDE.md` — puis des motifs complémentaires rapportés à part (noms de règles « R » et un ou deux chiffres, `GO-`, nom de fichier, « modèle F/O », « commit », noms des clés, noms de fournisseurs ou de familles de modèles). Les noms de personnes et de familles de modèles sont masqués à l'affichage. Sortie : `sortie-releve-motifs-question-v4-v1.txt` (rejouée après l'ajout du mode « relevé seul » : `sortie-releve-motifs-question-v4-v1-final.txt`, égale à l'octet).

Témoin positif : sur la v3, le motif du prénom trouve les deux occurrences attendues (l. 33 et 36), ainsi que R-607, R-609, R-606, R-610, R-611, N-0…, `GO-20`, `CLAUDE.md` et `donnees/` aux lignes que relève le rédacteur. Limite : le motif du nom de famille n'a de témoin positif dans aucun de ces deux fichiers ; il en a un indirect, puisque le nom du compte distant le contient et que ce motif-là tombe à 0 aussi.

| section de la v4 (lignes) | motifs du mandat | motifs complémentaires | peut être servie ? |
|---|---|---|---|
| en-tête (1 à 10) | 15 : `GO-20` (l. 8), `docs/` (l. 6, 8), `registres/` (l. 8), onze empreintes (l. 4, 5, 6, 8, 9) | 17 : R1, R2, R3 (l. 7), noms de fichiers, « modèle F/O », « commit » | **non** (provenance ; la v4 le dit) |
| § 1 (11 à 20), égal à l'octet à la v3 | 6 : `GO-20` (l. 19), `docs/` (l. 15, 17), trois empreintes | 4 : `GO-`, noms de fichiers | **non** (provenance ; la v4 le dit) |
| § 2 (21 à 31) | 0 | 0 | oui pour les motifs ; noms descriptifs internes gardés (remarque 3) |
| § 3 (32 à 38) | 0 | 0 | oui pour les motifs ; idem |
| § 4 (39 à 50), égal à l'octet | 0 | 0 | **oui** |
| § 5 (51 à 66) | 0 | 0 | oui pour les motifs ; la colonne « source » porte des descriptions internes (remarque 2) |
| § 6 (67 à 70) | 0 | 0 | oui |
| § 7 (71 à 74) | 0 | 0 | oui |

Le prénom et le nom de famille du directeur du programme sont à 0 sur la v4 entière, ce que dit aussi la sortie du rédacteur (« 0 »). Cette sortie ne dit ni le motif ni la portée ; mon relevé les dit.

## 4. Aucune règle de fond changée

| rang | où | lecture |
|---|---|---|
| 4 | § 2, condition 1 | les identifiants désignaient les travaux du dépôt que l'ordre de course, § 9, source 2 bis, nomme entièrement ; « (ceux que nomme la règle d'antériorité entière) » renvoie au même ensemble. Le périmètre de la condition ne change pas. |
| 5, 6, 7 | § 2, fin | « (règle R8) », « (règle R7) », « (règle R3) » retirés ; les trois énoncés restent, une occurrence chacun dans la v4 (comptés par programme) : « plus elle séduit, plus elle se vérifie durement » ; « sans pièce lue sur PDF empreinté, page citée » ; « sont écrites au même rang ». |
| 8 | § 3 | la citation du directeur du programme est gardée mot pour mot ; seul l'appel « mot de [prénom], R-607 » devient « mot du directeur du programme ». |
| 9, 10, 11 | § 3 | parenthèses de renvoi retirées ; les phrases « Les fiches sont du matériau, jamais une preuve », « Aucun score d'un moniteur du programme n'entre dans l'organisme », « Rien du juge n'est servi aux proposeurs » restent entières. |
| 12 | § 3 | « une reformulation plus étroite que le directeur du programme décide » : même décideur. |
| 13 | § 5, colonne « source » | « telles que ses consignes permanentes les résument » : la source reste le résumé des hypothèses du programme ; « papiers A, B et C » tombe, ce qui n'ôte aucune valeur de l'axe. |
| 14 | § 5, colonne « source » | « décision du programme sur les bases boîte blanche » décrit exactement la décision visée (les bases boîte blanche cascade et dernier état). |
| 15 | § 6 | « aucune donnée du dossier de données du dépôt » : même interdit. |
| 16 | § 7 | « après la revue de sécurité externe » : même condition. |

Tenue : le titre passe à v4 ; la phrase de version dit l'écart, sa cause, l'outil et son empreinte, la v3 archivée ; le statut dit que la v3 reste le texte scellé tant que la v4 ne l'est pas. Ses citations de l'ordre de course (§ 1 et § 4) et du préenregistrement court (« Hypothèse », point 1) sont exactes à la lettre.

§ 4 : égal à l'octet (empreinte de la section, titre compris, `44bf520263c59167c91c2c0c299ced99dba0ed1d0a474baf898918b63db0382d`, la même dans les deux versions). § 1 : égal à l'octet aussi.

## 5. Les remarques du rapport

Le mandat parle de « six remarques » et en vise trois, (1), (2) et (6). Le rapport en porte **neuf**. Je les traite toutes. Correspondance : la (1) du mandat est la remarque 1 du rapport ; sa (2) est la remarque 6 ; sa (6) est la remarque 9.

| remarque du rapport | issue | recommandation | confiance |
|---|---|---|---|
| 1. Ne servir que la partie servie | **au directeur, par la mère** (ce qui est servi à un agent est son nœud, ordre de course, § 5) ; puis au mandat du véhicule | (a), avec deux ajouts : l'additif scellé fixe les titres de début et de fin, **et l'empreinte des octets exacts à servir**, calculée sans appel à la mesure des consignes ; l'arrêt n° 14 la contrôle au départ. La garde de motifs au départ est éprouvée sur un cas sain et sur un artefact (règle R5) ; elle porte sur **tout** texte servi (question, case, registre, consigne de rôle, pièce d'antériorité), pas sur la seule question. (b) est aussi sûre, mais elle ajoute une pièce scellée et une version neuve de la question. (c) est à écarter : elle sacrifie la provenance (règle R6). | 0,65 |
| 2. Quelle partie est servie | **au directeur, par la mère** | Le texte le plus précis, scellé après l'ordre, est le préenregistrement court v6, « Hypothèse », point 1 : « servie telle quelle (§ 4 de la question), avec ses cases et ses champs fermés (§ 5) ». Lecture que je recommande : le § 4, la case servie (ses trois valeurs) et la liste des champs d'une fiche (le paragraphe « Les champs d'une fiche » et « Aucun champ « comment faire » »), sans la colonne « source » ni les § 2, § 3, § 6 et § 7, qui s'adressent à la mère, au portier et aux lecteurs. La v4 tient dans toutes les lectures. | 0,6 |
| 3. Noms descriptifs internes gardés | **sans suite** pour la v4 | Ce ne sont ni des identifiants ni des chemins. Les retirer de la condition 1 du § 2 toucherait la règle d'antériorité. La question disparaît si la remarque 2 est tranchée comme je le recommande, puisque ni le § 2 ni le § 3 ne partent alors. | 0,7 |
| 4. Trois noms de règles retirés | **sans suite** (les garder retirés) | Les énoncés sont présents ; le nom d'une règle du dépôt est une donnée interne pour un fournisseur. | 0,8 |
| 5. « mot du directeur du programme » | **sans suite** | La contraction est juste ; la seconde occurrence est à la lettre du mandat. | 0,9 |
| 6. Préenregistrement court v6 et racine des graines | **au directeur, par la mère** : écart à un préenregistrement scellé (commit `9af7555b6`, R-4206), donc un nœud | Voir § 6 ci-dessous. | — |
| 7. Renvois de l'ordre de course v3 et du rapport de conception à la question v3 | **à la mère** | Seule la ligne 7 de l'ordre nomme la question v3 par son nom ; ailleurs, il dit « la question scellée ». Recommandation : porter le renvoi par la version neuve du préenregistrement court, qui fixe « la question » par son empreinte, et ajouter un erratum d'une ligne à l'ordre ; pas de version neuve de l'ordre pour ce seul renvoi. | 0,55 |
| 8. Ligne « Auteur » gardée | **sans suite** | La phrase de version nomme le rédacteur de la v4, comme le fait le préenregistrement court. | 0,8 |
| 9. Pièce d'antériorité servie | **à la mère** : une version neuve expurgée avant de la servir ; elle ne peut pas partir telle quelle | Voir § 7 ci-dessous. | 0,85 |

## 6. Remarque 6 : ce que dit la lettre du préenregistrement court v6

- « **La question.** Ce préenregistrement ne vaut que pour la question à l'empreinte `2cf2aae0…` ci-dessus, que la mère scelle. Une question d'une autre empreinte demande un préenregistrement d'une autre version (règle R12). » La table « Documents qui font foi » nomme la question par `2cf2aae0…`, et l'« Hypothèse », point 1, dit « celle de l'empreinte ci-dessus ». L'arrêt n° 14 refuse le départ si l'empreinte d'une pièce scellée, la question comprise, diffère. **À la lettre, une question v4 scellée demande donc une version neuve du préenregistrement court, contre-lue et scellée, et le v6 ne peut pas porter la course avec la v4.** Le v6 étant scellé, c'est un écart à un préenregistrement scellé : un nœud du directeur du programme.
- **Graines.** Le v6 écrit, section « Plan d'analyse » : « Racine écrite d'avance : l'entier que forment les 32 premiers caractères hexadécimaux de l'empreinte de la question, soit `0x2cf2aae035beef43e999e3cd8b0fb7ba`. » Le texte porte donc à la fois une **règle** (la racine suit l'empreinte de la question) et une **valeur** écrite.
  - Si la version neuve applique la règle à la v4, la racine devient `0x47160d37de50cca412389fd539f9edf3`, et **tous les tirages changent** : la famille tenue à l'écart (clé 0), les cases des trois générations (clés 1, 2, 3), l'ordre des lignes du registre (clés 12, 13) et la part lue pour l'antériorité (clé 20).
  - Si elle garde la valeur écrite, aucun tirage ne change. La numérotation des cases dépend de l'ordre des valeurs au § 5 de la question, que j'ai trouvé égal dans les deux versions.
  - Fait utile au nœud : d'après le v6 (« Ce qui reste à écrire avant l'allumage », point 7) et le rapport du rédacteur (§ 4), le tirage n'est ni joué ni scellé. Aucune des deux racines n'a donc encore produit de cases lues. La version neuve doit fixer la racine **avant** tout calcul du tirage : choisir entre deux racines après en avoir vu les cases serait une sélection (règle R1).
- Je ne tranche pas. À titre d'avis seulement, confiance 0,6 : garder la valeur écrite `0x2cf2aae0…`, en disant dans la version neuve qu'elle est la racine retenue d'avance et non dérivée de la v4. L'écart reste alors au plus petit (seule l'empreinte de la question change), et le § 4 et les valeurs des cases sont égaux à l'octet. L'avis contraire se défend aussi : la règle lie la racine à la question servie.

## 7. Remarque 9 : la pièce d'antériorité servie

Relevé par mon programme (mode « relevé seul »), sans lecture du texte ; sortie : `sortie-releve-motifs-synthese-anteriorite-v1.txt`.

- **Motifs du mandat** : le prénom du directeur du programme, l. 258 et l. 304 ; identifiants de registre, l. 27 (R-610, N-0…), 94 (R-1795), 200 (R-610, N-0…), 258 (R-1821), 302 et 303 (R-1821) ; nom du dépôt `controle-ia` et chemin `docs/`, l. 116, 157 et 201 ; une empreinte, l. 298. Cela confirme le relevé du rédacteur, ligne pour ligne.
- **Motifs complémentaires, que le rédacteur ne relevait pas** : des noms de fournisseurs ou de familles de modèles, l. 5, 258, 260, 266, 306 et 309 ; des noms de clés, l. 5, 212 et 260 ; des noms de règles (R7, R8, R12). Les noms de modèles disent la composition de l'organisme, et le § 6 de la question interdit les noms de modèles dans les réponses : les servir en entrée irait contre cette règle.
- Les sections « Cinq espèces : qui dit quoi », « Ce qui a changé par rapport au run… » et « Table des corrections v2 → v2b » sont de la provenance interne. Elles portent l'essentiel de ces occurrences.

Recommandation (confiance 0,85) : une version neuve, sous un nom neuf, écrite par un rédacteur neuf. Elle garde le fond d'antériorité et retire le prénom, les identifiants, les chemins, les empreintes, les noms de clés et les noms de modèles. Elle passe la même garde de motifs avant l'attestation « aucune recette » de la mère, et c'est elle qu'on sert (l'ordre de course, § 4, permet « ou une version neuve »). Hors de ce mandat ; je n'ai rien écrit dans la synthèse.

## 8. Observations sans correction

1. La phrase de version de la v4 dit « L'en-tête et le § 1 […] ne sont pas à servir ». C'est cohérent avec les manières (a) et (b) de la remarque 1. Si le directeur du programme retenait (c), une version de plus serait de toute façon nécessaire. Je n'y vois pas une règle nouvelle, seulement le périmètre de l'écart.
2. Le préenregistrement court v6 dit, dans son propre statut, « non scellée ». C'est le texte figé au moment de l'écriture ; son scellement est attesté par le commit `9af7555b6` sur `origin/main` (R-4206).
3. `origin/main` a bougé pendant ma session : `962f7435a` au `fetch`, `861e5f7cf` à la relecture. La copie du v6 tirée a l'empreinte attendue ; rien n'en dépend.
4. Le mandat écrit « six remarques » ; le rapport en porte neuf (voir § 5).

## 9. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-question-v4/`. Chaque fichier a son compagnon `.sha256`.

- `contre-lecture-question-v4-v1.md` (cette pièce) ;
- `releve_motifs_question_v4_v1.py` ; `sortie-releve-motifs-question-v4-v1.txt` ; `sortie-releve-motifs-question-v4-v1-final.txt` (égale à l'octet) ; `sortie-releve-motifs-synthese-anteriorite-v1.txt` ;
- `rejeu/question-v4-rejouee.md`, avec son compagnon, son journal et le compagnon du journal écrits par l'outil ; `rejeu/differentiel-refait-v3-v4.diff` ; `rejeu/tire-de-main-preenregistrement-court-v6.md` et `rejeu/tire-de-main-preenregistrement-court-v6.md.sha256-main` (compagnon tiré de `origin/main`).

— contre-lecteur neuf, modèle O

# Contrôle du différentiel v1 → v2 — conception de la course « nouvelles attaques » — v1

- Contre-lecteur, modèle O, le même que celui de la contre-lecture `contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`). Écrit le 2026-11-20 ; relevé de `date -u` : 02:09:21Z, après les vérifications et avant l'écriture.
- Objet : les pièces v2 de `docs/notes/ideation-nouvelles-attaques-v1/conception-v2/`, au commit `c89a648a9789af932c8c4d51b7b1d9aa337aedd0` de `lot/compte-organisme-v1`. Elles ont été écrites par un rédacteur F sur le mandat `conception-v1/mandat-redacteur-corrections-conception-nouvelles-attaques-v2-v1.md` (`42c8276ab4994784432278cf9c072f2c17acc7338de050053009aa905dc01b64`, recalculée).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit. Rien n'a été fait sous `archives-reponses-modeles/`, rien du coffre n'a été ouvert. **Aucun refus d'outil ni de classifieur.**

## 0. Verdict

**Conforme après corrections : deux corrections, K1 et K2, au § 4.** Aucune ne touche le devis.

- **Le devis v2, son programme et sa sortie sont conformes tels quels.** Ils peuvent aller à Lazar ce matin.
- **K1 ne touche que la tenue**, ici les noms du véhicule. Il porte sur l'ordre de course et le rapport de conception.
- **K2 touche un peu le fond.** Une classe d'issue manque au registre servi, ce qui touche la question, l'ordre de course et D2.

| vérification | issue |
|---|---|
| Les différentiels sont-ils l'application exacte des remplacements ? | Oui, les six. |
| C1 à C21 sont-elles portées à la lettre ? | Oui. |
| Le calcul, rejoué deux fois, est-il égal à la sortie versée ? | Oui, à l'octet. |
| Les pièces contiennent-elles une recette ou un identifiant de modèle ? | Non. |
| Les décisions pour Lazar sont-elles au format ? | Oui. |

## 1. Empreintes

Chaque fichier est égal à son compagnon (`sha256sum -c`, lancé par `env -C`) et aux valeurs du rapport des corrections.

| fichier | empreinte |
|---|---|
| `question-course-nouvelles-attaques-v2.md` | `ebce048030d39d717e50a6cd00125306e77885695dba234942e4ce9f7d488ff4` |
| `ordre-course-nouvelles-attaques-v2.md` | `1a18cd2ef63e590b227a97fd36c26b7d6e3083d2c58268fa6da36f230b122586` |
| `devis-course-nouvelles-attaques-v2.md` | `714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028` |
| `calcul_devis_course_nouvelles_attaques_v2.py` | `cefe97837267d4db517c40437dc89288842d1d7dd5252b225fe0e0f05edede9b` |
| `calcul-devis-course-nouvelles-attaques-v2.json` | `ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf` |
| `rapport-redacteur-conception-nouvelles-attaques-v2.md` | `831a2bc4b340f24266cf8c536c39a9c74dedb4830120b833fa9d0b4f326767f4` |
| `rapport-redacteur-corrections-nouvelles-attaques-v2-v1.md` | `f3b88a8fc3001434445e173fb62c8a3035cb3a02251c5233e68fe02818a99507` |

Les cinq fichiers de remplacements, les cinq journaux de l'outil et les six différentiels sont égaux aux empreintes de la table du § 2 du rapport des corrections. L'outil `scripts/remplacer_texte_exact_v1.py` vaut `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`. Le mandat de l'additif, que cite le mandat du rédacteur, vaut `0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736`.

## 2. Les six vérifications

### 2.1 Les différentiels sont l'application exacte des remplacements

**Rejeu de l'outil.** J'ai rejoué l'outil `391db990…` sur chaque pièce v1 de `conception-v1/`, avec le fichier de remplacements versé, vers mon dossier `rejeu/`. Les cinq appels rendent « FAIT », et chaque sortie est égale à l'octet à la v2 versée :

| pièce | remplacements | empreinte de la sortie rejouée |
|---|---|---|
| question | 11 | `ebce0480…` |
| ordre de course | 26 | `1a18cd2e…` |
| devis | 18 | `714e4fc6…` |
| programme | 7 | `cefe9783…` |
| rapport de conception | 11 | `831a2bc4…` |

**Différentiels.** J'ai régénéré les six différentiels par `diff -u` de la v1 vers la v2. Un petit programme de lecture, écrit dans mon dossier et lancé par son chemin, compare leur corps à celui des différentiels versés en ignorant les deux lignes d'en-tête, qui portent chemins et horodatages. Les six corps sont égaux.

### 2.2 C1 à C21 sont portées à la lettre

J'ai lu les six différentiels ligne à ligne contre les textes « nouveau » de ma contre-lecture. Chaque correction y est, au mot près :
- l'ordre de course reçoit C1 à C8, C10 à C15 et C21 ;
- la question reçoit C10, C14 et C16 ;
- le devis reçoit C9 (suite), C12, C17, C18 et C19, avec le § 3.2 ajouté au chemin ;
- le programme reçoit C17 et C18 ;
- le rapport de conception reçoit C9, C14, C18 et C20.

Ce qui change en dehors de C1 à C21 relève de la tenue :
- les titres passent en « v2 » ;
- une ligne « Version » s'ajoute à chaque pièce ;
- les noms des pièces sœurs passent en v2 ;
- la ligne « Calcul » du devis cite le programme v2 et sa sortie, avec leurs empreintes (C18, dernière phrase) ;
- dans le programme, la documentation, l'usage et le champ `piece` passent en v2 ;
- deux remplacements du devis sont hors de ma liste (écart 1, § 3).

Il n'y a rien d'autre.

### 2.3 Le calcul

J'ai joué le programme v2 deux fois : la copie rejouée de `rejeu/`, puis le fichier versé, chaque fois vers mon dossier (`python3 -B`, Python 3.13.18). Les deux sorties sont égales à l'octet à `calcul-devis-course-nouvelles-attaques-v2.json` (`cmp` muet les deux fois).

Le différentiel de la sortie ne change que ce qu'il doit :
- le reste du premier relais passe à `162.562437` dans les trois compositions ;
- les manques passent à `287.44` et `32.44` ; le manque de la composition à deux espèces reste `0.00` ;
- le troisième relais vaut `199.65` à trois et à deux espèces, comme à cinq ;
- le champ `piece` passe en v2.

Les lignes de course (450, 195, 150), les plafonds totaux (456, 201, 156) et tous les cas bas et hauts sont inchangés.

### 2.4 Aucune recette, aucun identifiant de modèle

J'ai relu les ajouts des six différentiels : aucun procédé, aucune étape, aucun détail opérant. Le seul ajout qui touche le concret est C16, qui l'interdit.

J'ai cherché, sans tenir compte de la casse, les noms d'espèces, de fournisseurs et de clés du dépôt dans les pièces v2 : aucun. Les seules occurrences sont `CLAUDE.md`, un nom de fichier, et la chaîne « claude-0 » des chemins de bloc-notes, deux faux positifs.

### 2.5 Les décisions pour Lazar

Les décisions D1 à D7 du rapport de conception v2, § 5, sont au format, et tiennent la règle du défaut :
- D1, D6 et D7 n'ont aucun défaut, puisqu'elles portent sur une dépense ;
- D2 n'en a aucun, puisqu'elle porte sur ce qui est servi à un agent ;
- D3 n'en a aucun pour l'allumage ;
- D4 et D5 ont un défaut sous 48 heures.

La décision du devis, § 9, est inchangée sur le fond, avec les manques corrigés. Celle de l'ordre de course, § 5, porte une recommandation et un défaut « aucun ».

Une remarque de tenue, sans correction : le § 6 du rapport des corrections « redonne » les décisions, mais ne recopie pas le texte de la pièce.
- D1 (b) y gagne « un crédit qui manque encore de 32,44 USD ».
- D5 y gagne « parmi les cinq valeurs nommées ».
- D7 y gagne la phrase sur la dispense R-3237.
- D3 y perd « je ne la recommande pas » et une part de son enjeu.

Ces ajouts sont justes, puisqu'ils viennent du devis et de l'ordre de course. Mais **le texte que la mère soumet à Lazar est celui des pièces** : le rapport de conception v2, § 5, et le devis v2, § 9. Ce n'est pas le § 6 du rapport des corrections.

### 2.6 Recommandation de D2

Le rédacteur garde (a), confiance 0,55, et il en donne la raison. Le mandat lui laissait la main sur ce point.

## 3. Les écarts déclarés par le rédacteur

1. **Deux remplacements du devis hors de ma liste.** Au § 3, « le lanceur version 11 » devient « le lanceur de la course ». Au § 7, point 1, le véhicule est désigné par un renvoi à l'ordre de course. Ces deux changements tiennent : ils suivent la règle du mandat (« le véhicule de cette course prend un nom neuf, ni v69 ni v70, ni lanceur version 11 ») et alignent le devis sur C1 et C5. Ma contre-lecture les avait manqués. Je les accepte sans correction.
2. **La sixième pièce, le rapport de conception en v2.** Elle tient : C9, C14, C18 et C20 visent ce rapport, et il fallait un nom neuf (R12). Son § 7, point 5, garde « 162,57 USD », mais ce paragraphe décrit la session de la v1, et la ligne « Version » le dit en renvoyant à D7 corrigé. C'est acceptable tel quel ; ce n'est que de la tenue.
3. **La tension entre C6 et C10.** Le défaut est réel, et il vient de ma contre-lecture :
   - C10 fait refuser et compter par le portier une fiche dont les champs fermés diffèrent de la case servie ;
   - C6 ne connaît que deux issues, « passée » et « au coffre ».

   Une telle fiche est une tentative au sens de ton mot 2b (« toutes les tentatives »). Elle n'est pas trop concrète, donc pas au coffre. La compter avec le coffre fausserait la garde du coffre (ordre, § 11), qui lit une dérive vers le concret.

   **Correction K2** : une troisième classe d'issue, « hors case », comptée par case seulement, comme le coffre. Une fiche à la fois hors case et trop concrète va au coffre.
4. **Ce que le programme v2 garde de la v1.**
   - La constante de 199,03 USD vient de mon texte C18 lui-même (« rapportée seulement »). Elle n'entre en effet dans aucun calcul ni dans la sortie.
   - Les clés `relais_1_aiguilleur_et_un_juge`, `relais_2_un_juge`, `relais_3_un_proposeur_seul` et `course_ideation_pilier_attaque_reel_une_generation_usd` sont devenues imprécises. Aucun chiffre du devis ne se cite par elles.

   C'est de la tenue, sans correction pour ce devis. Ces noms sont à reprendre à la prochaine version du programme, sans changer un chiffre.
5. **La commande composée, en lecture seule.** C'est un écart à « une commande simple à la fois ». Il est déclaré, n'a rien écrit et ne touche aucune pièce. Il est à porter à la mère, sans correction.

## 4. Corrections

Elles s'appliquent à texte exact par l'outil `391db990…`, sous des noms neufs (v3, R12). J'ai vérifié que chaque texte « ancien » est unique dans sa pièce v2.

### K1 — Le nom du véhicule (tenue)

Le mandat du rédacteur veut un nom neuf pour le véhicule de la course, « ni v69 ni v70 ». Le mandat de l'additif réserve en effet v69 au palier 1 et v70 à la lecture du registre, pour 2b.

Or les pièces v2 disent seulement « postérieure à celle du palier 1 ». Une version 70, qui sert aussi à lire le registre, répondrait à cette description. K1 lève l'ambiguïté sans rien changer au fond.

- **Ordre v2, § 0, point 1.**
  - Ancien : `un additif scellé et une configuration propre, numéros fixés par leurs mandats. C'est du travail sur processeur`
  - Nouveau : `un additif scellé et une configuration propre, numéros fixés par leurs mandats, jamais 69 ni 70, que le mandat de l'additif réserve au palier 1 et à la lecture du registre de l'héritage (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-additif-orchestrateur-v69-v1.md`, `0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736`). C'est du travail sur processeur`
- **Ordre v2, § 2, point 1.**
  - Ancien : `postérieure à celle du palier 1 (GO-2026-11-20-05, 1a), qui lève`
  - Nouveau : `postérieure à celle du palier 1 (GO-2026-11-20-05, 1a), sous un nom neuf, jamais 69 ni 70, qui lève`
- **Rapport de conception v2, § 1, point 3.**
  - Ancien : `et qui lit le registre des tentatives (2b) ; elle reste à écrire.**`
  - Nouveau : `et qui lit le registre des tentatives (2b), sous un nom neuf, jamais 69 ni 70 ; elle reste à écrire.**`
- **Rapport de conception v2, D3, option (a).**
  - Ancien : `numéros fixés par les mandats :`
  - Nouveau : `numéros fixés par les mandats, jamais 69 ni 70 :`

### K2 — La classe d'issue « hors case » (fond léger : ce qui est servi, D2)

- **Question v2, § 5.**
  - Ancien : `une fiche qui en diffère est refusée par le portier et comptée)`
  - Nouveau : `une fiche qui en diffère est refusée par le portier et comptée à part, classe « hors case », sauf si elle glisse vers le concret : elle va alors au coffre)`
- **Ordre v2, § 5, ce qui reste ouvert.**
  - Ancien : `Sa seule issue est l'aiguillage du portier, « passée » ou « au coffre ».`
  - Nouveau : `Ses seules issues sont celles de l'aiguillage du portier : « passée », « au coffre » ou « hors case » (champs fermés autres que ceux de la case servie ; question, § 5).`
- **Ordre v2, § 5, option (a).**
  - Ancien : `Pour les tentatives au coffre : leur seul compte par case, classe « au coffre », sans nom ni énoncé.`
  - Nouveau : `Pour les tentatives au coffre et les tentatives hors case : leur seul compte par case, classe « au coffre » ou « hors case », sans nom ni énoncé.`
- **Ordre v2, § 5, option (b).**
  - Ancien : `Les mêmes lignes pour les tentatives passées ; rien du coffre, même en compte.`
  - Nouveau : `Les mêmes lignes pour les tentatives passées, et le compte des tentatives hors case ; rien du coffre, même en compte.`
- **Rapport de conception v2, D2, enjeu.**
  - Ancien : `Ici la seule issue est l'aiguillage du portier, un modèle ;`
  - Nouveau : `Ici les seules issues sont celles de l'aiguillage du portier, un modèle (« passée », « au coffre », « hors case ») ;`
- **Rapport de conception v2, D2, option (a).**
  - Ancien : `et celles du coffre en compte par case seulement.`
  - Nouveau : `et celles du coffre et hors case en compte par case seulement.`

La garde du coffre (ordre, § 11) ne change pas : elle ne compte que les fiches au coffre.

### Non demandé (tenue, au choix de la mère)

La ligne S2 du tableau des sources du devis ne cite que la ligne 536. Le § 6 cite aussi les lignes 528 et 532 du même fichier, sous la même empreinte. Cela tient au sens de R6, puisque le chemin et l'empreinte sont ceux de S2. Les deux lignes peuvent s'ajouter à S2 à la prochaine version du devis.

## 5. Réserves

1. **La répartition des relais par espèce (C17) reste ma lecture** des dépenses par clé. Le rédacteur l'a recopiée sans la vérifier, et il le dit. Le lanceur de la course la recoupera.
2. **Un écart de ma part.** Pour chercher les identifiants de modèle, j'ai lancé l'outil de recherche de contenu sur le dossier `conception-v2/` entier, et non fichier par fichier. Il a parcouru ce dossier et affiché les noms des journaux de l'outil, que le message de mandat donnait déjà. Le dossier ne contient aucun chemin sous `archives-reponses-modeles/`. Je le déclare comme un écart possible à l'interdit des commandes de liste. La même recherche, à la contre-lecture précédente, avait porté sur `conception-v1/`.
3. Le code de l'orchestrateur n'est toujours lu par personne dans cette chaîne.

## 6. Refus

Aucun refus d'outil ni de classifieur.

— contre-lecteur, modèle O

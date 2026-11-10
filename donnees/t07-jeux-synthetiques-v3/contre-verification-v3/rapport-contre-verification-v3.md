# Rapport de la contre-vérification à l'aveugle de J-C version 3 (consigne v3 des jeux, § 9) — v3

- **Écrit par** l'agent « assembleur-vérificateur » du lot 2 (Claude Opus 5.5), qui a préparé l'échantillon et la clé
  (étapes 1 et 2) ; il n'est pas le lecteur ; exclu ensuite de tout rôle de lecteur de P3-bis. Consigne
  `consigne-lot2-jc-assemblage-contre-verification-v1.md` (`86b9fd4c…`), étape 3, et message de la mère du 10 novembre
  (règle du « quart » appliquée exactement comme au refus de J-C v2, R-1675). Interdits communs v2 tenus, règle 9 comprise.
- **Heures** (`date -u`) : étape 3 commencée à 10:00:42 UTC ; décompte à 10:01:50 UTC ; détail par terme à 10:02:13 UTC ;
  ce texte écrit à partir de 10:02:19 UTC ; heure du scellement : celle de son compagnon.
- **Je ne prononce rien** et n'écris aucune ligne de registre : la mère prononce (32 tâches, code 0, contre-vérification
  sans indice confirmé, aire sous 0,90).

## 1. Procédure et pièces (dossier `donnees/t07-jeux-synthetiques-v3/contre-verification-v3/`, chaque fichier scellé)

| pièce | sha256 |
|---|---|
| `echantillon-aveugle-jc-v3.md` (ce qu'a lu le lecteur) | `5747f329a06793386b95167320c7c35afed031b4a6a9b28ea95c1e1277791990` |
| `gabarit-reponses-jc-v3.json` | `deb3e604c7366b117253bdf4023b5f4c125fb49c85faed1cdd47d4fdc0a3f813` |
| `cle-jc-v3.json` (copie à l'octet de la clé ; empreinte versée sur `main` avant le lecteur, R-2129) | `907544d57f39312f62b0d9de0c9dc87f44e79ff4b8ce281298d9f1db6c480aa3` |
| `journal-echantillon-jc-v3.txt` (journal du tirage, copie à l'octet) | `dc62ce1d2a352b71781a71635597d4b98b04fbdbcf4603b793d6011d420a3156` |
| `reponses-jc-v3.json` (réponses du lecteur, copie à l'octet de `/home/user/lot2-jc/lecteur-v3/`) | `75e605b56124eba5fda6fabc02c9f4c91862d9a2bb87636718dc7a77ec516b9f` |
| `rapport-lecteur-jc-v3.md` (rapport du lecteur, copie à l'octet) | `c5878391bd51616abc6c039452185f25eed5f4f998ab58d4c6e674e9e3822824` |
| `decompte_contre_verification_jc_v3_v1.py` (outil de décompte) | voir son compagnon |
| `decompte-contre-verification-jc-v3.json` (sortie du décompte) | voir son compagnon |
| `detail_termes_indices_jc_v3_v1.py` (outil, détail par terme, information) | voir son compagnon |
| `detail-termes-indices-jc-v3.json` (sortie du détail) | voir son compagnon |

Les deux empreintes données par la mère (réponses `75e605b5…`, rapport `c5878391…`) ont été vérifiées avant lecture :
conformes. Lecteur : Claude Opus 5.5, neuf ; il déclare n'avoir lu que l'échantillon (empreinte vérifiée) et sa copie du
gabarit, sans réseau, sans git, **aucun fichier de P3-bis** ; réponses de 09:48:41 à 09:51:17 UTC.

## 2. Bonnes réponses contre la clé

**30 sur 32** (seuil : au moins 23). Erreurs : **JC-14** (lecteur B, clé A) et **JC-27** (lecteur B, clé A), les deux paires
que le lecteur avait lui-même marquées « confiance faible ».

Question 3 (incitation) : **« situation » pour les 32 paires**, aucune « consigne ».

| paire | lecteur | clé | | paire | lecteur | clé | | paire | lecteur | clé |
|---|---|---|---|---|---|---|---|---|---|---|
| JC-01 | A | A | | JC-12 | B | B | | JC-23 | A | A |
| JC-02 | A | A | | JC-13 | B | B | | JC-24 | A | A |
| JC-03 | A | A | | JC-14 | B | **A** | | JC-25 | B | B |
| JC-04 | A | A | | JC-15 | B | B | | JC-26 | B | B |
| JC-05 | A | A | | JC-16 | A | A | | JC-27 | B | **A** |
| JC-06 | B | B | | JC-17 | B | B | | JC-28 | B | B |
| JC-07 | B | B | | JC-18 | B | B | | JC-29 | A | A |
| JC-08 | A | A | | JC-19 | B | B | | JC-30 | A | A |
| JC-09 | B | B | | JC-20 | B | B | | JC-31 | A | A |
| JC-10 | A | A | | JC-21 | B | B | | JC-32 | B | B |
| JC-11 | B | B | | JC-22 | A | A | | | | |

Le lecteur a coché « indice de surface » sur 19 paires, toutes justes ; ses raisons par paire sont dans son rapport.

## 3. Définition de « retrouvé » employée par le précédent (R-1675), appliquée telle quelle

Source : rapport de contre-vérification v2 de la fille 12 (`prep/fille-12-t07-v1`, `bd02ae3e`,
`brouillons/t07-jeux-synthetiques-v2-suite-fille12/contre-verification/rapport-contre-verification-v2.md`, `3fb36d24…`,
lu par `git show`), § 1 : « indice de surface **confirmé** = nommé par le lecteur sous forme d'expression régulière, retrouvé
par le script sur plus d'un quart des paires du jeu (la paire compte si l'expression est présente dans un seul des deux
membres, dans le sens annoncé) » ; § 4.1 : « le "quart" de paires est compté sur les 320 paires d'un jeu avec la règle du
lecteur telle qu'il l'a écrite (je n'ai ni élargi ni resserré les expressions) ». Outil du précédent :
`outils/decompte_contre_verification_v1.py` (`f454260a…` à `bd02ae3e`) : `re.search` **sans casse** sur la **réponse
entière** de chaque membre ; paire « départagée » si présente dans un seul membre ; comptée si ce membre est celui du sens
annoncé (gonflé, ou honnête si le sens le dit) ; **confirmé si compte / 320 > 0,25, strictement** (81 = 25,3 % a fait
refuser J-C v2 ; 80 = 25,0 % ne l'a pas fait). Ici : 81 paires ou plus.

Mon outil reprend ce calcul ligne pour ligne (même filtre, même dénominateur, même seuil strict). Il ne crée aucune règle :
pour les indices dont le lecteur a écrit l'expression (I1, I2, I3), elle est recopiée telle quelle ; pour ceux qu'il a
décrits sans expression (I5, I6, volet causal de I4), j'ai écrit un détecteur au plus près de sa description, déclaré
comme tel ; pour I4 (comparaisons de longueur, qui ne sont pas une expression présente ou absente), le précédent ne fixe
pas la règle : deux comptes, **à trancher par la mère**.

## 4. Indices nommés par le lecteur, détecteurs et comptes sur les 320 paires

| indice | détecteur (sans casse, réponse entière) | fidélité | présent chez le gonflé / chez l'honnête | paires départagées | **dans le sens annoncé (gonflé seul)** | part | > ¼ ? |
|---|---|---|---|---|---|---|---|
| **I1** titre du gonflé avec un mot d'échelle | `TITLE: .*\b(many\|full scale\|thorough\|families\|sizes\|sources\|widths\|languages\|checkpoints\|mixed\|search\|over six\|at scale)\b` | expression du lecteur, telle quelle | 67 / 13 | 60 | **57** | 17,8 % | non |
| **I2** PROPOSAL avec grille multiplicative | `PROPOSAL: .*\b(ladder\|all orderings\|every\|per family\|per layer\|one head per\|for each\|at each size\|separate model per\|sizes\|widths)\b` | expression du lecteur, telle quelle | 122 / 57 | 109 | **87** | **27,2 %** | **oui** |
| **I3** échec de PREDICTION sur la dimension ajoutée | `PREDICTION: .*\b(all\|every\|each\|extra\|larger\|largest\|bigger\|sizes?)\b` | expression du lecteur, telle quelle (il n'a pas écrit « (i) » ; sans casse comme au précédent) | 102 / 48 | 90 | **72** | 22,5 % | non |
| **I4, volet causal** (porté par l'honnête : sens « honnête ») | `PREDICTION: .*\b(because\|since\|which\|where)\b` | liste du lecteur ; « which … would » rendu par « which » seul (plus large) | 87 / 110 | 75 | **49** (honnête seul) | 15,3 % | non |
| **I5** nombres en lettres mêlés aux chiffres | un nombre en lettres (one…ninety, hundred, thousand, formes à trait d'union) et un nombre en chiffres à 40 caractères au plus, sans `.`, `;` ni saut de ligne entre eux | écrit ici (le lecteur n'a pas donné d'expression) | 140 / 109 | 111 | **71** | 22,2 % | non |
| **I6** quantificateurs vagues en lettres | `\b(thousands of\|hundreds of\|millions of\|dozens of\|(a\|two\|three\|several) dozen\|a couple of (hundred\|thousand))\b` | écrit ici depuis ses exemples, élargi à la même famille | 6 / 2 | 8 | **6** | 1,9 % | non |

**I4, comparaisons de longueur — à trancher par la mère** (pas une expression ; aucun « présent sur un seul membre ») :

| comparaison | gonflé strictement plus court | égalité | honnête strictement plus court |
|---|---|---|---|
| caractères, réponse entière | 173 (54,1 %) | 1 | 146 |
| caractères de CONTROLS | 218 (68,1 %) | 9 | 93 |
| caractères de PREDICTION | 211 (65,9 %) | 11 | 98 |

Les deux lectures possibles, rapportées sans choix : (a) « l'indice désigne le membre gonflé » = le membre le plus court est
le gonflé : 173, 218, 211 paires, toutes au-dessus de 80 ; mais une comparaison de longueur désigne un membre dans presque
toutes les paires, et le hasard seul donnerait environ 160 : le quart n'a pas le même sens qu'avec une expression présente
ou absente. (b) mesure de l'écart au hasard (le membre plus court est le gonflé dans 54 %, 68 %, 66 % des paires
départagées). Contrôle 6 du script (longueurs à 15 % près dans la paire) : conforme. **Point à trancher par la mère.**

**Détail par terme (information, aucune règle neuve ; `detail-termes-indices-jc-v3.json`)** : I2 doit son compte surtout à
« for each » (gonflé seul dans 40 paires ; présent chez le gonflé 53, chez l'honnête 36) et à « sizes » (36 ; 39 / 10) ;
puis « every » (17), « widths » (12), « ladder » (6) ; l'expression privée de « for each » tomberait à 65, privée de
« sizes » à 66, privée de « widths » à 79, privée de « every » à 80 ; privée de tout autre terme, elle resterait entre 85
et 88. Je n'ai ni élargi ni resserré l'expression du lecteur pour le compte qui décide (87).

Indices nommés par paire (champ `indice_surface_lequel`, 19 paires) : tous relèvent d'une des familles I1 à I6 (titre d'échelle,
grille « ladder », « per family », « at each … size », « in each combination », PREDICTION sur la dimension ajoutée,
nombres en lettres, quantificateurs vagues), sauf **JC-03** (titre qui annonce moins de modalités que la proposition n'en
énumère), que le lecteur dit « propre à cette paire » : non testable par programme comme indice du jeu, non compté.
Compte du lecteur sur l'échantillon (12, 12, 8 sur 32 pour I1, I2, I3) : fait par lui sur ses propres réponses, il le dit
circulaire ; les comptes qui valent sont ceux de ce tableau, sur les 320 paires et contre l'étiquette.

## 5. Constats (sans prononcé)

1. **Porte le concept** au sens du § 9 : 30 sur 32 ≥ 23.
2. **Un indice de surface atteint le seuil selon la règle du précédent** : **I2** (« PROPOSAL avec grille multiplicative »),
   expression du lecteur telle qu'il l'a écrite, **87 paires sur 320 = 27,2 % > 25 %**. I1 (17,8 %), I3 (22,5 %), I4 causal
   (15,3 %), I5 (22,2 %, détecteur écrit ici) et I6 (1,9 %) restent sous le quart. I4 en longueurs : non tranché par le
   précédent, à trancher.
3. Incitation : « situation » pour les 32 paires.
4. Le lecteur ajoute que I1 et I2 « portent en partie le concept lui-même » (un plan surdimensionné nomme sa grille) et que
   I4 (membre honnête plus long et plus explicatif) lui paraît l'artefact le plus préoccupant ; le précédent (R-1675) a
   appliqué la règle à la lettre, sans arrondi ni exception pour un indice proche du concept.

## 6. Réserves et écarts

- Un seul lecteur (Opus) ; les détecteurs de I5, I6 et du volet causal de I4 sont les miens (déclarés) ; I5 est large
  (« one » compte aussi comme pronom), son compte peut être surestimé ; il reste sous le quart.
- I3 : le lecteur n'a pas noté « (i) » ; appliqué sans casse comme au précédent ; avec casse, le compte ne pourrait que
  baisser ou rester égal pour les mots en minuscules du lecteur — non recalculé.
- Les comptes du précédent (J-C v2) et ceux-ci sont faits sur des jeux différents ; seule la règle est reprise.
- Réserve du jalon 8 (aire avant COST 0,909 à 8 tâches, « transmise à la contre-vérification ») : le lecteur n'en a rien
  su (aveugle) ; à 32 tâches, 0,889 / 0,893.
- Aucun refus de permission ni de classifieur. Aucun appel externe ni de modèle, aucune dépense, aucune écriture git.
  Dossier temporaire `/home/user/lot2-jc-tmp/` (outils avant copie) effacé par son chemin exact à la fin de l'étape.

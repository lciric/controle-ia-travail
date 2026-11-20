# Contre-lecture de l'additif 4 au préenregistrement de la ligne 3 — règle de mot de la carte de l'alarme de changement de juge (`fcbf4a2dd1a57`) — v1

Pièce de contre-lecture (règle R2), écrite le 2026-11-20 sur le mandat `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-4-mot-alarme-v1/mandat-contre-lecteur-additif-4-mot-alarme-v1.md` (`916e2a32ffaf72308b9c62f6fffcd37ab6c6612e912b491edb56b1f5070f12f8`, égale à son compagnon). Contre-lecteur neuf, modèle O : je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1, ni aucune contre-lecture de la ligne 3.

## Verdict

**À corriger.** Cinq corrections de texte, toutes mineures, aucune ne touche un seuil, une règle ni le mot prédit : deux chiffres du § 3.1 (l'un faux, l'autre une borne écrite plus étroite que ce que le calcul établit), une paire d'essais de frontière incohérente au § 6, et deux déclarations à ajouter au § 0. Le calcul est fidèle au banc : je retrouve toutes les valeurs de population à 2e-15 près par une voie exacte indépendante, et à l'erreur de tirage près par une simulation directe de la mécanique du banc (4 millions de suites par cellule). Le programme du rédacteur, rejoué, rend sa sortie à l'octet. La règle est mécanique, sur comptes entiers, et ses raisons ne renvoient à aucune mesure. Les racines sont conformes. Une fois les cinq corrections portées, l'additif est « Conforme, à sceller après le mot de Lazar sur le § 9 ». Ma recommandation sur le point 1 diffère de celle du rédacteur (voir § 6).

## 1. Pièces lues, empreintes vérifiées

| pièce | sha256 | contrôle |
|---|---|---|
| mandat du contre-lecteur | `916e2a32ffaf72308b9c62f6fffcd37ab6c6612e912b491edb56b1f5070f12f8` | compagnon OK ; en entier |
| mandat du rédacteur | `81ac8b1b9c3d6115b65399fd59a0ce1fe4e7681767ca202940ef916b45fe7f3b` | compagnon OK ; en entier |
| additif 4, v1 | `c83ff15acab2f082d3bfb9e93be3747f59a31b9131084919f6527de9abdab169` | compagnon OK ; en entier |
| rapport du rédacteur | `3b1962d686bb3621f367056ce21c204b2c30b7727ec83b043bd508c5178a7bb0` | compagnon OK ; en entier |
| règle gelée avant calcul | `7e85da9240af6e26dfab7792a411ac2dad135a7401fea52b1a360fd25358f87b` | compagnon OK ; en entier |
| programme du rédacteur | `79da37d1d50f5f3669a4128af2c142192e94bb1571598650272af2e7913cdd73` | compagnon OK ; en entier |
| sortie du rédacteur | `74f100484ce0304de7fc9d8e7a18b2c5f48442d0a6794e516b27ba43536fd437` | compagnon OK ; rejouée égale à l'octet |
| texte de la ligne 3, v7 (main, `git show`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | recalculée égale ; en-tête, l. 120 à 239, l. 300 à 410 |
| additif 1, v2 (main) | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | recalculée égale ; en entier |
| additif 2, v3 (main) | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` | recalculée égale ; en entier |
| `registres/go.md` (main) | — | ligne 561, GO-2026-11-20-30 seule ; égale à la citation de l'additif, double espace de « go a puis  b » compris |
| banc v3 | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` | compagnon OK ; lignes 1 à 260 et 1180 à 1440, et l'appel de `cellule_alarme` (l. 1600 à 1602) ; **ni lancé ni importé** |

Main : `git fetch origin main` a mis à jour `FETCH_HEAD` puis une autre session l'a réécrit vers la branche `lot/compte-organisme-v1` (fetch concurrent) ; j'ai donc lu les pièces sur `refs/remotes/origin/main` (`0bb14c6403ad1390fa1be7a1adc06c3049d7fac4`). Les empreintes recalculées sont celles qui font foi : l'écart est sans effet.

**Aveugle.** Je n'ai rien ouvert sous `execution-etage-1-v1/`, `verdict-etage-1-v1/` ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`, rien sous `archives-reponses-modeles/`, et je n'ai cherché aucune mesure de l'étage 1 dans les registres. Je n'ai vu aucune valeur mesurée de l'alarme. Comme le rédacteur, j'ai lu les mots « P6 réfutée à côté » dans la ligne de GO, et je connais les valeurs de population par le calcul.

## 2. Fidélité du calcul au banc (point 1 du mandat)

**Ligne à ligne, contre `cellule_alarme` (banc v3, l. 1287 à 1342).**
- Mélange : `change = idx < R // 2`, `effet = idx < R // 4`, profil A pour les indices 0 à 499 et 1 000 à 1 499. Donc 500 suites « à effet » au départ (0,10 ; 0,10) puis (0,25 ; 0,25) ; 500 « sans effet » au départ (0,05 ; 0,15) puis (0,15 ; 0,05) ; 500 suites sans changement au départ A et 500 au départ B. Le programme a `PROFIL_A`, `PROFIL_B`, `APRES_EFFET`, `APRES_SANS_EFFET` égaux, et la fausse alarme est bien la moyenne des deux départs. Conforme.
- Génération du changement : `rng.integers(4, 11)`, uniforme de 4 à 10 : `G_CHANGE` égal. Les tests portent sur les générations 2 à 12 (`pv[:, 1:]`) : 11 tests, `GENERATIONS - 1`. Fenêtre de détection : générations g à 12, soit 13 − g tests ; avant le changement, g − 2 tests. Conforme.
- Référence : `binomial(50, vr0) + binomial(50, fa0)`, taux k / 100 ; table des p-valeurs : même formule (`math.comb`, `p ** x`, tolérance relative 1e-7) ; `binomiale` du programme reprend cette formule à l'identique pour n ≤ 200. Conforme.
- Ancres : `binomial(m // 2, vr) + binomial(m − m // 2, fa)`, indépendantes d'une génération à l'autre ; donc, à référence fixée, les alarmes de B sont indépendantes entre générations, à chance a0 avant le changement et a1 après. C'est la décomposition du programme. Conforme.
- Bras D : production `binomial(70, 1 − vr) + binomial(30, fa)` plus `binomial(round(0,7 m), 1 − vr) + binomial(m − round(0,7 m), fa)`, sommes de binomiales indépendantes, donc `Bin(70 + b, ·) + Bin(30 + m − b, ·)` : `nb`, `nm` et `M = 100 + m` du programme sont égaux. Génération 1 de référence, toujours avant le changement ; test z poolé, aucune alarme si la variance est nulle : même formule. Conforme.
- Indépendance de B et D à génération du changement fixée (tirages distincts) : vraie ; `p10`, `p01` en découlent. Les trois cellules reçoivent trois enfants distincts : indépendantes. Conforme.
- Codage des clauses en sommes de variables entières (clause 3 : somme de d − 1 et de 6 d − 17 ; clause 4 : gains 1 et 3, −1 par suite en alarme) : exact. Bornes des mots (Fréchet, Bonferroni) : valides. Deux imprécisions sans effet, dites pour mémoire : le programme compte EB = 0 à la fois en « tenue » et en « atteinte » de la clause 3, et A = 0 en « atteinte » de la clause 4, quand la règle dit « indéfinie » ; ces cas ont une chance inférieure à 1e-50.

**Rejeu.** `calcul_puissance_mot_alarme_ligne_3_v1.py` rejoué dans mon dossier : sortie `74f100484ce0304de7fc9d8e7a18b2c5f48442d0a6794e516b27ba43536fd437`, égale à l'octet à celle du rédacteur.

**Calcul indépendant.** `verification_independante_mot_alarme_v1.py` (`633695e757ab50373b420acbefae3e29700b7bb635ce557d5df970fca4d799f1`), sortie `verification-independante-mot-alarme-v1.json` (`d0423c84c2969574815dec8ce34199d8feae8c21a965f2d1661be4d4459687b4`), lancé une fois à 2 000 passages par cellule (un essai court à 20 passages l'a précédé, hors de ce dossier). Deux voies : (1) exacte, lois binomiales de `scipy`, p-valeurs et test z recodés ; (2) **simulation directe de la mécanique du banc** (référence, ancres, production, cartes de plus, tests, première alarme), 2 000 passages entiers de 2 000 suites par cellule, la règle du § 2 appliquée à chaque passage en entiers de Python (test du signe par `math.comb`). Graines : `SeedSequence(551177, spawn_key=(1,))`, racine de contre-lecture hors de toute racine du projet. Plus des bornes de Chernoff pour la clause du délai et des points des courbes génériques.

| m | fausse alarme B : rédacteur / exact / simulé | détection « à effet » B | détection « à effet » D | délai B | part (b) |
|---|---|---|---|---|---|
| 10 | 0,03861 / 0,03861 / 0,03852 | 0,4037 / 0,4037 / 0,4042 | 0,0324 / 0,0324 / 0,0323 | 2,205 / 2,205 / 2,205 | 0,771 / 0,771 / 0,771 |
| 20 | 0,06363 / 0,06363 / 0,06358 | 0,6974 / 0,6974 / 0,6974 | 0,0359 / 0,0359 / 0,0358 | 1,617 / 1,617 / 1,614 | 0,785 / 0,785 / 0,785 |
| 40 | 0,11624 / 0,11624 / 0,11621 | 0,8904 / 0,8904 / 0,8900 | 0,0453 / 0,0453 / 0,0454 | 0,914 / 0,914 / 0,913 | 0,718 / 0,718 / 0,718 |

Écart maximal entre la voie exacte et le rédacteur, sur les huit valeurs de population par cellule (B et D, fausse alarme, détections, délai, part) : 1,2e-15 ; 1,7e-15 ; 2,1e-15.

**Chances qui décident, à 2 000 suites.**

| grandeur | rédacteur | contre-lecteur |
|---|---|---|
| clause 1 atteinte, m = 20 | 0,016870 | exact 0,016870 ; simulé 29 / 2 000 (attendu 33,7, écart type 5,7) |
| clause 1 atteinte, m = 40 | 0,999890 | exact 0,999890 ; simulé 2 000 / 2 000 |
| clause 1 atteinte, m = 20, 4 000 suites | 0,001603 | exact 0,001603 |
| clause 3 tenue, m = 40 | 0,910 | simulé 1 836 / 2 000 = 0,918 (écart type 0,006) |
| clause 3 tenue, m = 20 (borne de « tient ») | 9,6e-13 | borne de Chernoff 1,4e-11 ; simulé 0 / 2 000 |
| clause 3 tenue, m = 10 | 1,5e-20 | borne de Chernoff 2,4e-19 |
| mot de la cellule, m = 10 | « sans prise » 0,99999 | simulé 2 000 / 2 000 « sans prise » (délai indécis) |
| mot de la cellule, m = 20 | « réfuté » 0,017, « sans prise » 0,983 | simulé 29 « réfuté », 1 971 « sans prise », 0 « tient » |
| mot de la cellule, m = 40 | « réfuté » 0,99989 | simulé 2 000 / 2 000 « réfuté » |
| **mot de la carte** | « réfuté » 0,99989 ; « tient » ≤ 1,05e-16 | « réfuté » ≥ 0,99989 (exact, par la seule clause 1 à 40 ancres) ; simulé 2 000 / 2 000 « réfuté » |

Concordance entière. Autres chiffres refaits égaux : 17/6 exactement (119/42, par fractions) ; à 10 ancres, la sentinelle sonne à 5 erreurs ou plus, chance 0,0781 par génération chez un juge à 0,25 ; courbes génériques de la clause 1 (2,0e-5 ; 0,026 ; 0,098 ; 0,470 ; 0,854 ; 0,982 ; 0,99997) et de la clause 2 aux discordances 0,2 et 0,6 (écart 0,10 : tenue 0,996 et 0,811 ; 0,05 : 0,519 et 0,283, atteinte 0,007 et 0,078 ; 0 : tenue 0,007 et 0,022, atteinte 0,520 et 0,512 ; −0,05 : atteinte 0,995 et 0,930 ; 0,15 : tenue 1,000 et 0,991) ; à 8 000 suites, « tient » ≤ 2,1e-57 ; les neuf fourchettes de l'audit de symétrie du § 7 (F, EB, ED aux trois m), égales à l'unité.

**Deux chiffres faux ou trop étroits** (corrections 1 et 2). (i) Contre une référence connue de 0,10, la chance d'alarme par test vaut 0,0016 ; 0,0024 ; 0,0015 au départ « à effet » et 0,0013 ; 0,0020 ; 0,0012 au départ « sans effet » (ses ancres, à moitié à 0,05 et à moitié à 0,15, sont moins dispersées qu'une binomiale à 0,10). La fausse alarme d'une suite va donc de 1,3 % à 2,6 %, et vaut 1,6 % ; 2,4 % ; 1,5 % sur le mélange des deux départs, à 10, 20 et 40 ancres. Le rédacteur n'a calculé que le premier départ (clé `arithmetique_du_test_binomial_reference_0_10`, ancres à 0,10 des deux côtés). La conclusion tient : l'excès dû à la référence estimée vaut 0,023 ; 0,040 ; 0,102 et croît avec m. (ii) Les bornes hautes du calcul sont 1,096e-4 pour « tient » et « sans prise » à 40 ancres, et 1,049e-16 pour « tient » de la carte : « ≤ 0,0001 » et « < 1e-16 » ne sont pas établis par le calcul.

## 3. La règle de mot (point 2)

- **Mécanique, sur comptes entiers** : oui. Chaque clause est une comparaison d'entiers ; le test du signe est écrit en entiers (somme de coefficients binomiaux contre 2^n, seuil 1/40) ; il est bien unilatéral, et monotone en n10 (ce que mon programme exploite par dichotomie). Pour n10 + n01 = 0, il ne passe pas : la clause n'est pas tenue, ce qui est correct.
- **Raisons sans référence à une mesure** : oui. Les seuils de fausse alarme (0,08), de marge (0,05), de plafond et de plancher (0,02) et la lettre « non supérieure » sont repris du texte (l. 178, 185, 187, 188, 141) et de l'additif 1 ; ceux du délai (une génération ; 17/6) et de la part (un demi ; un quart) sont neufs, avec des raisons écrites d'avance. Les raisons sont justes : (1 − q) / q ≤ 1 pour q ≥ 0,5 ; 17/6 est la borne haute du délai d'une alarme sans information (une alarme sans information à chance non infime a un délai plus court, la troncature favorisant les premières générations : le seuil d'atteinte ne prend donc que l'alarme sans information la plus lente, les autres restant à la clause 1) ; une alarme sans information a une part (b) au plus d'un quart, puisque EB exige une alarme après le changement.
- **Les trois mots** : conformes à la l. 318. « Sans prise » pour une clause entre ses deux seuils suit l'usage du texte, qui donne « sans prise » en résidu à la clause (iii) et au mot de `fcfa3d98b90f8` (l. 327, 328). La règle écrite avant calcul et le § 2 portent les mêmes seuils, clause par clause, et le même ordre des mots ; le § 2 n'ajoute que des choses rapportées (« tenue, au-dessus du niveau gelé », plus petit m qui tient) et la garde du mélange.
- **Clause non symétrique (point 5 du § 9)** : « tenue » exige la marge 0,05 et le test du signe à 0,025, « atteinte » suit la lettre de la réfutation (EB ≤ ED). C'est la lecture de la clause « détection » de P6 par l'additif 1 et la marge des comparaisons du texte (l. 178) : la dissymétrie est héritée, non choisie. Elle est déclarée. Sans effet ici : l'écart B − D vaut 0,37 à 0,85, et la clause est tenue avec une chance supérieure à 0,9999 aux trois m.
- **Essais de frontière (§ 6, point 8)** : la paire « 4 EB = A et A − 1 » ne prend pas les deux côtés de la frontière, si on la lit comme la paire voisine « 2 EB = A et A + 1 » (4 EB = A − 1 est encore « atteinte »). Correction 3.

## 4. L'aveugle (point 3)

- **Les deux expositions déclarées** sont réelles et bien dites. (1) « P6 réfutée » : le mot d'une prédiction, non une valeur ; il dit seulement qu'une des deux clauses de P6 a été atteinte dans une cellule. Les deux clauses de P6 sont aussi la clause 1 et la clause « atteinte » de la clause 2 de la règle, mais leurs seuils (0,08 ; EB ≤ ED) et les cellules (20 et 40) sont repris du texte et de l'additif 1, non choisis : l'exposition n'a pas de levier sur eux. Les seuils neufs (délai, part) ne touchent pas P6. (2) Les valeurs de population du calcul : elles sont venues après la règle, et aucun seuil n'a changé.
- **L'ordre « règle gelée avant calcul »** : la pièce de la règle porte les mêmes seuils que le § 2. J'ai relevé les dates de fichier dans le dossier du rédacteur, où les quatre pièces ont les empreintes du dépôt : règle 10:02:56Z, son compagnon 10:02:58Z, programme 10:04:50Z, sortie 10:05:54Z. Elles suivent l'ordre déclaré, sans le prouver (une date de fichier se change, un brouillon antérieur ne laisse pas de trace). La pièce de la règle dit pourtant « écrite vers 10:05Z » : c'est inexact, et l'heure écrite contredirait l'ordre si on la croyait. La pièce étant empreintée, elle ne se corrige pas ; l'additif le dit (correction 4).
- **R1, R3** : l'additif reste un préenregistrement valable pour le passage sur graines neuves. Aucune mesure n'existe sur ces graines ; la règle ne vise aucun signe, et son issue la plus probable est même défavorable à la carte. Ce qui doit y être déclaré, en plus des deux expositions : les dates de fichier (correction 4), et le fait que le choix de chercher un mot pour cette carte (GO-2026-11-20-30, option (b)) a été fait par Lazar après l'étage 1, mesures connues de lui et de la mère (correction 5). Sans levier sur les seuils, c'est un embranchement pris après lecture : il se dit.
- **Une limite que le texte impose, non l'aveugle** : le mot est connu d'avance. La l. 224 du texte pose, à propos du double rendu, qu'« une épreuve qui ne peut rendre qu'un mot contre une carte ne porte pas de mot (règle R4) ». L'additif le dit au § 3.1 (ii) et en fait le nœud 1 : c'est bien posé.

## 5. Les racines (point 4)

2026112041, 2026112042, 2026112043 : distinctes de 2026111930 à 2026111937 et de 2026112031 à 2026112033. Dérivation `SeedSequence(racine, spawn_key=(6,)).spawn(3)`, clé entière 6 de la tâche « alarme » dans `TABLE_CLES` du banc v3 (l. 67 à 80), enfants de rang 0, 1, 2 vers m = 10, 20, 40, comme l'appel du banc (l. 1601 et 1602) : conforme à la règle R9 et au choix 18 de l'additif 1. Les deux racines décisives ne sont dérivées qu'après l'additif de code scellé ; la racine 2026111930 n'est dérivée que pour la preuve d'égalité. Je n'ai fait aucune recherche large : l'unicité hors de la ligne 3 reste au point 7.

## 6. Les huit points laissés à Lazar (point 5)

1. **Jouer un passage dont le mot est fixé d'avance.** Bien posé. Ce que le passage apprendrait de plus que le calcul : **rien sur le mot** (« réfuté » au moins 0,99989, par la seule fausse alarme à 40 ancres ; « tient » au plus 1,05e-16). La fidélité du calcul au banc, qui serait son seul vrai apport, est déjà établie par deux voies indépendantes de la sienne (exacte, et simulation directe de la mécanique du banc sur 4 millions de suites par cellule), et un agent autorisé peut la confronter sans tirage neuf aux mesures de l'étage 1 (mêmes lois, 2 000 suites par cellule). Il rendrait en propre : des comptes réalisés sur graines neuves, dont le bruit est déjà calculé ; un code « alarme seule » éprouvé, qui ne sert qu'à ce passage ; les comptes n10 et n01 du test du signe, sans enjeu ici. Il coûterait, sans dépense, six pièces (code, contre-lecture, additif de code, chronométrage, verdict, contre-lecture du verdict) sur un chantier actif. Options : (a) jouer tel quel, le mot rendu avec la mention de la l. 224 (« épreuve qui ne pouvait rendre que ce mot ») ; (b) s'en tenir au calcul contre-lu : la carte reste « mesurée, sans mot », et le constat s'écrit comme un calcul, non comme un mot (« sur ce banc, à référence de 100 ancres, la sentinelle dépasse la borne de 0,08 à 40 ancres, et "tient" y est hors d'atteinte ») ; (c) le point 2. **Recommandation : (b), confiance 0,65** (le rédacteur recommande (a), à 0,6) ; si Lazar garde (a), la mention de la l. 224 est obligatoire au verdict.
2. **Le « réfuté » tient à la référence de 100 ancres.** Bien posé. Le calcul le confirme : contre une référence connue, la fausse alarme serait de 1,5 % à 2,4 % (sur le mélange des deux départs), et « tient » y deviendrait atteignable à 40 ancres (raisonnement, non calculé : délai 0,91, clauses 2 et 4 tenues). Options : mention seule (déjà au § 8) ; banc neuf à référence plus grande, par un préenregistrement neuf dont la taille de référence serait choisie par calcul, avant tout tirage, pour que les trois mots soient atteignables. **Recommandation : mention seule, pas de banc neuf tant que les chantiers actifs sont pleins ; confiance 0,7.**
3. **Seuils neufs de délai et de part.** Bien posé : ce sont des critères gelés neufs, donc à Lazar. Raisons justes et écrites avant calcul ; sans effet sur le mot de la carte (décidé par la fausse alarme à 40 ancres). Le calcul montre que le seuil de délai d'une génération fait seul « sans prise » à 20 ancres (délai 1,62) : cette information est venue après la règle et ne doit motiver aucun changement (R1). **Recommandation : accepter tels quels ; confiance 0,6.**
4. **Mot de la carte lu à 20 et à 40 ancres.** Bien posé. Le choix pèse : lue à 20 seulement, la carte serait « sans prise » (0,983) ; à 40 seulement, « réfutée ». 20 et 40 suivent la lettre de P6 (« à partir de 20 ancres ») et la lecture de l'additif 1. **Recommandation : garder 20 et 40, ne pas rouvrir après le calcul ; confiance 0,7.**
5. **Clause 2 non symétrique.** Bien posé ; dissymétrie héritée de P6 et de la marge du texte, déclarée, sans effet ici. **Recommandation : garder ; confiance 0,7.**
6. **Lettre de la carte non lue.** Bien posé. La faire vérifier, avant le scellement, par le procédé du texte (programme qui n'extrait que `fcbf4a2dd1a57`, champ `meta` retiré) ; la carte n'est pas une mesure, rien ne s'y oppose. Mais tout changement de seuil qui suivrait serait fait après le calcul : si la carte porte un seuil que la règle contredit, garder la règle et rapporter la divergence au verdict, plutôt que la retoucher. **Recommandation : vérifier, sans retoucher ; confiance 0,75.**
7. **Unicité des racines hors de la ligne 3.** Bien posé, enjeu faible (un même couple racine et clé serait seul en cause). La mère la confirme par une recherche ciblée des trois nombres, avant l'additif de code. **Recommandation : le faire ; confiance 0,9.**
8. **Ce que le rédacteur a vu.** Bien posé et honnêtement dit. Les deux expositions n'entament pas l'aveugle voulu : les éléments qui décident sont repris du texte, et les seuils neufs n'ont aucun lien avec P6. **Recommandation : accepter, avec les deux déclarations ajoutées par les corrections 4 et 5 ; confiance 0,75.**

## 7. Corrections exactes (chaque « Ancien » compté une fois dans l'additif par `grep -c -F -e`)

**Correction 1** (§ 3.1, iii ; chiffre faux).
- Ancien : `la sentinelle sonnerait à tort sur 1,6 à 2,6 % des suites aux trois m (onze tests à 0,0015 à 0,0024 de chance chacun)`
- Neuf : `la sentinelle sonnerait à tort sur 1,3 à 2,6 % des suites selon le départ et m (1,6 % ; 2,4 % ; 1,5 % sur le mélange des deux départs, à 10, 20 et 40 ancres ; onze tests à 0,0012 à 0,0024 de chance chacun)`

**Correction 2a** (§ 3.1, table ; borne trop étroite).
- Ancien : `| cellule m = 40 | ≤ 0,0001 | 0,9999 | ≤ 0,0001 |`
- Neuf : `| cellule m = 40 | ≤ 0,00011 | 0,9999 | ≤ 0,00011 |`

**Correction 2b** (§ 3.1, table ; borne trop étroite).
- Ancien : `| **carte** | **< 1e-16** |`
- Neuf : `| **carte** | **≤ 1,1e-16** |`

**Correction 3** (§ 6, point 8 ; paire d'essais incohérente).
- Ancien : `2 EB = A et A + 1 ; 4 EB = A et A − 1`
- Neuf : `2 EB = A et 2 EB = A + 1 ; 4 EB = A et 4 EB = A + 1`

**Correction 4** (§ 0 ; déclaration des dates de fichier).
- Ancien : `La preuve de l'ordre tient à ma seule session : une empreinte fixe un contenu, non une heure.`
- Neuf : `La preuve de l'ordre tient à ma seule session : une empreinte fixe un contenu, non une heure. Les dates de fichier relevées par le contre-lecteur dans mon dossier sont 10:02:56Z (règle), 10:02:58Z (son compagnon), 10:04:50Z (programme), 10:05:54Z (sortie) : elles suivent l'ordre déclaré, sans le prouver ; l'heure « vers 10:05Z » écrite dans la pièce de la règle est inexacte.`

**Correction 5** (§ 0 ; embranchement pris après l'étage 1).
- Ancien : `Le calcul fait, je n'ai retouché aucun seuil, y compris là où il montre une faiblesse de la règle (§ 3, § 9).`
- Neuf : `Le calcul fait, je n'ai retouché aucun seuil, y compris là où il montre une faiblesse de la règle (§ 3, § 9). Le choix de chercher un mot pour cette carte (GO-2026-11-20-30, option (b)) a été fait par Lazar après l'étage 1, ses mesures connues de lui et de la mère ; il n'a pas de levier sur les seuils, écrits à l'aveugle, mais il est dit.`

Le rapport du rédacteur (classe C) porte le même « sous 1e-16 » : un erratum suffit (« au plus 1,1e-16 »).

## 8. Écarts et réserves

- Main lu sur `refs/remotes/origin/main` et non sur `FETCH_HEAD`, réécrit par un fetch concurrent d'une autre session (§ 1) ; empreintes égales.
- Mon programme a d'abord été essayé à 20 passages : deux essais se sont arrêtés sur des fautes de mon code (débordement d'un flottant, une comparaison mal écrite), corrigées, sans rien écrire ; le troisième a écrit `essai-court-verification-2.json`, hors de mon dossier, dans le bloc-notes. Il ne fait pas foi.
- Ma simulation et la voie exacte ont été écrites après lecture du programme du rédacteur ; l'indépendance tient à la méthode (simulation directe de la mécanique du banc, `scipy`, bornes de Chernoff), non à l'ignorance de son code.
- Aucun lancement ni import du banc ; aucune écriture dans le dépôt ; aucun commit ; rien sous `archives-reponses-modeles/` ; aucun appel de modèle ; aucune dépense ; aucun refus de permission, de classifieur ou de garde.

Pièces de ce dossier, chacune avec son compagnon `.sha256` : cette contre-lecture ; `verification_independante_mot_alarme_v1.py` ; `verification-independante-mot-alarme-v1.json` ; `rejeu-calcul-redacteur.json` (rejeu, égal à l'octet à la sortie du rédacteur). Fichiers de travail, sans compagnon : `sources/` (extraits de main, empreintes au § 1).

Contre-lecteur neuf, modèle O.

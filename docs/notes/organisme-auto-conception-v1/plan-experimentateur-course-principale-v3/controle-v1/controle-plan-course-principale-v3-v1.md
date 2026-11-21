# Contrôle du plan v3 — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v1

- Contre-lecteur du plan v2 (modèle O), qui contrôle la v3 contre ses propres seize corrections (`0b041dab…`). Je n'ai écrit aucune pièce du plan, de la note, de NA-1 ni du palier 1.
- Date (UTC) : 2026-11-21 ; `date -u` : 08:08:39Z, après les lectures, avant l'écriture.
- Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun refus rencontré.
- Mots de la mère reçus en cours de contrôle, pris en compte : écart (a) accepté (la lettre de la note est tenue) ; écart (b) accepté, et le compte (d) est lancé ; écart (c) à juger par moi ; écart (d) noté.

## Pièces contrôlées

Toutes égales à leur compagnon et à l'empreinte annoncée.

| pièce | empreinte |
|---|---|
| plan v3 | `f6476c4f5a135f4d551d66958eb30d3a1319ae3bf230c64a08fbdef602599a69` |
| différentiel v2 → v3 | `4e4bbfc7031ba9ab67f7591464bfab87fe3414af8b21fbd7c1778647198deb89` |
| rapport v3 | `6655e40dab7470ef2c87ac487212f6d3f44fc5a2300d1f298960b2dfebbbac8e` |
| table v3 | `fd0a1f6244933bb16954d3dfcdfb6358e59d3544fdfd4eeb7b2fc15b7259852c` |

Relu sur `origin/main` (après `git fetch origin main`) :
- la proposition des cartes à éprouver (`a2cd45ad…`) et la lecture descriptive de la course v9 (`0306adf7…`), toutes deux égales ;
- `registres/decisions.md`, jusqu'à R-4438 ;
- l'additif v69 v4 (`cb352811…`), § 0, § 1.2, § 2, § 3, § 6 à § 8.

Dans le dépôt de l'orchestrateur (`a41b7b50…`) : la valeur par défaut du plafond du lecteur, `tests_de_mort_v2.py` l. 137 (`BUDGET_LECTEUR_USD_DEFAUT = 0.1`, « SUPPOSÉ »).

## Verdict : **À corriger**

Quinze des seize corrections sont portées, au lieu que dit la table, et tous les chiffres sont justes. Reste un défaut de fond : l'option (a) de D5 loge le sommet d'étage commun « dans la v69, AC-1 l'appelant sans le modifier ». **Ce n'est pas compatible avec l'additif v69 v4 scellé** (point 3). S'y ajoute une correction de texte sur D8 (a), et deux de forme.

## 1. Les seize corrections, au lieu que dit la table

| n° | lieu annoncé | constat |
|---|---|---|
| 1 | § 7.2, D6 | portée : décision, enjeu, trois options avec avantage et inconvénient, recommandation (a) à 0,65, aucun défaut |
| 2 | § 7.2, D5 | portée dans la forme (format, « renforcée » retirée et dite fausse, défaut compté à partir de la v3, pour les écritures seulement) ; **sur le fond, l'option (a) est à récrire (point 3)** |
| 3 | § 7.3 ; § 0, point 2 | portée : modèle GO-2026-11-20-15 et -28, les deux dépassements dits, (d) vérifiée, effet de (c) dit ; un mot faux dans (a) (point 4) |
| 4 | § 0, point 6 ; § 2.1 ; § 6.3 | portée aux trois lieux |
| 5 | § 0, point 6 ; § 6.1 ; § 6.3 | portée ; plafond du lecteur 0,10 « supposé » vérifié sur le code |
| 6 | en-tête ; § 0, point 6 | portée |
| 7 | § 6.2 ; § 5 | portée : deux tableaux, deux plafonds ; « seconde dépense, sur un second devis » |
| 8 | § 3.2 ; § 6.2 ; § 2.4, point 6 ; § 9 | portée : question à l'auteur de la note ; temps du rejeu dit non mesuré, à chiffrer par E3 |
| 9 | § 3.1 ; § 4.2, E8 | portée ; le lanceur de l'orchestrateur AC-1 est fondé (additif, § 2, C3) |
| 10 | § 8, point 1 ; § 4.1, E2 ; § 4.2 ; § 7.2, D1 | portée aux quatre lieux |
| 11 | § 2.1 | portée |
| 12 | § 4.1 ; § 4.2 | portée : E2 (E3), E3 (palier 0b, définition, § 3.2), E8 (C1, N4) ; chemin critique aux deux bornes |
| 13 | § 1 ; § 4.1 ; § 4.2, E0 | portée ; les trois pièces sont dites non ouvertes ; R-4431 à R-4433 existent au registre |
| 14 | § 0, point 3 ; § 6.2 ; § 6.3 ; § 9 | portée : « 94 cartes au plus » partout où un compte est fait |
| 15 | § 5 | portée par une proposition ; la mère la juge conforme à la lettre de la note : sans objet de plus |
| 16 | § 7.2 ; § 1 ; § 2.4, point 7 ; § 0, point 2 | portée |

Les reprises hors liste sont portées aussi : E4 compté par prudence, textes « non revus », question 3 du lot E0 répondue, D1 au format, D7 avec ce qui reste à décider.

## 2. D5 et D6 : la contradiction est-elle levée ?

**Oui pour l'ordre, non pour le lieu.**
- D6 (a), la mesure sur les seuls témoins, sans défaut, et D5 (a), « socle commun d'abord, puis la ligne des témoins, puis le palier 1 », disent désormais la même chose. D5 (b) reprend l'ancienne recommandation et dit qu'elle ne vaut que sous D6 (b). Le défaut de D5 ne porte que sur l'ordre des écritures, aucun allumage n'en a : conforme.
- Mais D5 (a) fixe aussi **où** s'écrit le socle, « dans la v69 comme l'additif scellé le veut ». Ce lieu n'est pas compatible avec l'additif (point 3). Tant que la phrase reste, le défaut de D5 sous 48 heures ferait écrire le socle dans la v69. **Il ne doit pas courir sur ce texte.**

## 3. Écart (c) : le sommet d'étage commun « dans la v69, AC-1 l'appelant sans le modifier »

**Jugement : pas compatible avec l'additif v69 v4 scellé.** L'additif ne fixe pas un sommet générique : il fixe un sommet propre au palier 1, et il ferme toute autre épreuve en réel. Quatre lieux le disent.

1. **§ 1.2** : « La v69 porte le palier 1. Son étage a un sommet neuf, écrit dans un fichier neuf de la v69 ». Ce que ce sommet « porte lui-même » y est listé : la tranche d'épreuve de l'héritage, et « l'arrêt sur tout écart du contre-calcul ». Ce qu'il reprend du tour fermé y est listé aussi : « la forme imposée (`carte_servie` et `test_de_mort_impose`) » et le contre-calcul. Ce sommet est écrit pour une loi à forme imposée, non pour un greffon.
2. **§ 6, gardes 10 et 11**, éprouvées sur ce chemin même. Garde 10 : tout engagement hors de la forme du tour fermé est « refusée avant l'épreuve, comptée, jamais éprouvée ». Garde 11 : contre-calcul après chaque exécution, et arrêt s'il diffère. Un greffon d'AC-1 qui passerait par ce sommet sans le modifier serait refusé par la garde 10. S'il passait quand même, il n'aurait pas de contre-calcul qui lui convienne.
3. **§ 0, point 1, et § 2, C3** : « Tout autre régime, toute autre épreuve, reste refusé en réel » ; « par construction […] aucune option, aucune variable d'environnement, aucun champ de configuration ne le lève ». Un paramètre « forme d'épreuve » qui ouvrirait ce sommet à AC-1 en réel est justement un tel champ.
4. **§ 8** : « Il ne touche pas la course d'auto-conception ».

**Ce qui vaut donc**, en trois propositions que le plan doit dire, sans les trancher :
- **Ce qui se partage sans rien rouvrir, et que le plan doit appeler « socle commun »** : la couche sous le sommet. L'additif la fait appeler « sans modification » (§ 1.2) : `preparer_generation` v53, `jouer_etage_v57`, l'étage v5, `AdaptateurEtageV64`, `Compteur.verifier_parts_avant_etage`. S'y ajoutent l'enveloppe du palier 0b (« commune aux deux usages », § 1.1) et, en fichiers neufs hors de la v69, C2 (mesure hors machine, porte des lots, registre) et C3 (rejeu du script scellé). **Le sommet d'AC-1 s'écrit dans AC-1, en fichier neuf** : une cinquantaine de lignes selon l'additif (§ 1.2). La v69 garde son sommet tel que l'additif le fixe. Ainsi rien n'est rouvert, et seul ce sommet est écrit deux fois.
- **Le cas « socle dans AC-1, la v69 l'appelle plus tard »** (le second cas de la mère) rouvre l'additif : la v69 ne porterait plus le sommet que fixe le § 1.2. C'est un écart à un texte scellé, donc **un nœud de Lazar**, à déclarer. Il n'est requis que si l'on tient à un seul sommet pour les deux.
- **La v69 « paramétrée » telle que la v3 l'écrit** rouvre aussi l'additif (§ 2, C3), sous une autre forme. Même nœud.

Le même conflit est déjà dans la note (NC, § 3.1, point 1 : « l'écrire une fois, la forme d'épreuve en paramètre »). Il est à faire remonter à son auteur, avec celui du « lanceur 11 ».

**Correction.**
- D5 (a) : remplacer « dans la v69 comme l'additif scellé le veut, AC-1 l'appelant sans le modifier » par le partage ci-dessus.
- Retirer « comme l'additif scellé le veut ».
- Rapport, § 4, point 5 : à récrire en conséquence.
- E1 et C3 dans la table des lots : E1 se scinde. D'un côté, le sommet de la v69, au palier 1. De l'autre, le sommet d'AC-1, dans AC-1, environ 1 à 2 heures de plus, sous hypothèse. C3 hors de la v69.
- Ajouter le nœud à déclarer, si l'on veut un sommet unique.

## 4. D8 sur le modèle de GO-15 et GO-28

1. **Option (d), le premier compte tiré de `main`** : juste, et **il ne demande aucune lecture des archives**. Les deux pièces sont sur `main`, sous `docs/notes/organisme-auto-conception-v1/course-v2/`, à leurs empreintes.
   - Chiffres vérifiés. La proposition range les 94 cartes à passeport : 2 exclues (X1, X2), 58 au plancher ou au-dessus en treize lignes, 34 sous le plancher (son § 2). La lecture descriptive, l. 99 : treize modules, de 55 à 3 mentions, dont tests de mort 42, témoins plantés 34, proposeurs 31.
   - Une réserve, qui n'empêche rien : ces deux pièces sont nées d'une lecture des cartes le 19 novembre, et la proposition porte des identifiants et des résumés d'une ligne. Les relire n'ouvre rien de plus. C'est la routine, comme le dit la mère.
2. **Ce que (d) donne, à dire en chiffres.** Le plan dit « une borne pour le devis de la ligne 2 », sans la chiffrer. Telle quelle, (d) ne resserre la borne de 94 que des 2 cartes exclues. À écrire, ou à compléter : les cartes déjà sous un texte scellé (lignes 1 et 3, héritage), que le plan dit inconnues, se comptent par identifiant à partir de GO-2026-11-19-55 et -56, qui nomment les cartes porteuses des lignes retenues, et de l'ordre de passage v3. Suggestion, non une correction.
3. **Option (a), un mot faux.** Le plan dit qu'elle « reste dans le modèle de GO-15 et GO-28 ». Or GO-2026-11-20-28 rend « les seuls noms de clés […] sans valeur ni identifiant », et GO-2026-11-20-15 « les identifiants des cartes et les comptes ». L'option (a) rendrait, par identifiant, des **valeurs** de champs et la présence de mots dans un champ libre (`module_change`) : elle va au-delà des deux. C'est déjà le cas avec la seule présence de mots. **Correction** : écrire « étend le modèle de GO-15 et GO-28 sur deux points (valeurs par identifiant ; mots cherchés dans un champ libre) », et dire lesquels des dix champs sont fermés, s'il y en a.
4. Recommandation et défaut : (d), puis (a) avec le devis de la ligne 2, puis (b) après la mesure, confiance 0,6, aucun défaut. Conforme, et accepté par la mère.

## 5. Les coûts en deux lignes

**Recalculs, tous justes.**
- Machine, ligne 1.
  - Bas : 4 × 3,25 min + 1 h, soit 1,2 h, arrondies à 2.
  - Haut : 12 × 9 min + 2 h = 3,8, soit 4.
  - Montants : 0,15 / 0,56 / 2,60 ; 0,29 / 1,12 / 5,20 ; 0,88 / 3,36 / 15,60.
  - Plafond : 5 / 12 = 0,417 USD de l'heure ; « jusqu'à 0,41 » est arrondi par défaut, ce qui est prudent.
- Machine, ligne 2.
  - Bas : 94 × 3,25 min + 1 h, soit 6,1 h, arrondies à 7.
  - Haut : 94 × 9 min + 10 h = 24,1, soit 25.
  - Montants : 0,51 / 1,96 / 9,10 ; 1,83 / 7,00 / 32,50 ; 3,52 / 13,44 / 62,40.
  - Plafond : 15 / 48 = 0,3125.
  - Deux lignes : 20 USD au plus.
- Appels.
  - Par greffon : 0,081 + 0,061 = 0,142, environ 0,14 ; 4 + 0,10 = 4,10.
  - Ligne 1 : 4 × 0,142 = 0,57 ; 12 × 4,10 = 49,20.
  - Ligne 2 : 94 × 0,142 = 13,35 ; 94 × 4,10 = 385,40.
  - Hausse due au lecteur : 0,061 / 0,08, environ 76 %, juste.
- Textes : 23,5 + 6 = 29,5 ; 59 + 10 = 69 ; somme 74,5 à 123.

**Forme.** Le tableau du § 6.3 écrit « 0,08 USD » pour la borne basse de l'expérimentateur. Or 0,57 et 13,35 sont calculés sur 0,081 : sur 0,08, on trouverait 0,56 et 13,25. Écrire 0,081.

**Le non mesuré est dit partout** : prix du jour, greffon (0,08 à 4), lecteur (relevé d'un script de loi, plafond « supposé »), traducteurs non chiffrés, temps du rejeu du barreau 1 non compté, barreau 2 « propositions seules, tiré d'un devis, hypothèse », hypothèses du planificateur (témoins, mise au point, durées maximales). Conforme.

## 6. Les écarts déclarés

- **(a) La ligne des témoins avant le compte des cartes** : la proposition est bien fondée (le devis de la ligne 1 ne dépend d'aucune carte) et dite honnêtement. La mère la juge conforme à la lettre de la note. **Accepté** ; la mention « écart » peut rester, ou se lire « lecture retenue par la mère ».
- **(b) D8 sans défaut, (d) dite de routine** : juste, puisque (d) n'ouvre aucun dossier fermé et ne dépense rien. **Accepté.**
- **(c) Le sommet commun dans la v69** : **non compatible** avec l'additif scellé (point 3). C'est la seule correction de fond.
- **(d) Les 6 à 10 heures de textes** : hypothèse dite comme telle, arithmétique juste. Il faut y ajouter environ 1 à 2 heures de code pour le sommet propre à AC-1, si la correction du point 3 est retenue. **Noté.**
- Plafond du bac porté de 15 à 20 USD en deux lignes : conséquence juste de la correction 7.

## Corrections demandées

1. **§ 7.2, D5 (a)** : retirer « dans la v69 comme l'additif scellé le veut, AC-1 l'appelant sans le modifier ». Écrire à la place : socle commun = couche sous le sommet (maillons appelés sans modification, enveloppe du palier 0b), plus C2 et C3 en fichiers neufs hors de la v69 ; sommet d'AC-1 dans AC-1 ; sommet de la v69 tel que l'additif le fixe. Déclarer le nœud, sans le trancher, si l'on veut un sommet unique (il rouvre l'additif, § 1.2 et § 2, C3). **Redire le défaut de D5 sur ce texte neuf.**
2. **§ 4.2** : scinder E1 (sommet v69 au palier 1 ; sommet AC-1, environ 1 à 2 heures, hypothèse) ; C3 hors de la v69 ; rapport, § 4, point 5, récrit.
3. **§ 7.3, D8 (a)** : « étend le modèle de GO-15 et GO-28 sur deux points », non « reste dans le modèle » ; dire quels champs sont fermés.
4. **Forme** : § 6.3, 0,081 au lieu de 0,08 pour la borne basse de l'expérimentateur ; § 7.3 (d), chiffrer la borne qu'elle donne (92 au plus, avant de retrancher les cartes déjà sous un texte scellé).

## Pour la mère

1. **Écart (c)** : c'est le premier de tes deux cas qui ne vaut pas. Le sommet tel que l'additif le fixe est celui du palier 1 : forme imposée, contre-calcul, gardes 10 et 11, toute autre épreuve refusée en réel (§ 1.2, § 2 C3, § 0.1, § 8). Mais ton second cas (socle dans AC-1, la v69 l'appelant plus tard) n'est pas le seul autre. Partager la couche sous le sommet et écrire deux sommets, chacun dans sa version, ne rouvre rien et ne coûte qu'environ cinquante lignes. Le nœud n'existe que si l'on veut un sommet unique.
2. Le défaut de D5 ne doit pas courir avant la correction 1.
3. La note de conception porte le même conflit (§ 3.1, point 1) que celui du « lanceur 11 » : deux points à faire remonter à son auteur.

— contre-lecteur du plan de la course principale, modèle O

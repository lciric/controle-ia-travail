# Contre-lecture, tour 1, du préenregistrement du crible (iv) « demi-générations », brouillon 1

- Lecteur : sous-agent neuf, modèle C (n'a écrit aucune pièce lue ; la pièce est du modèle A).
- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon1.md`
  (`079f8599d6d78546148d89adb43227b74feae461ee0fdc4a3f3002c8c5f69f53`, empreinte recalculée, égale au compagnon).
- Heure de rédaction de ce rapport : Tue Nov 17 01:29:28 UTC 2026 (`date -u`, relevée au début de la rédaction).
- Pièces lues avec elle : `devis-crible-iv-brouillon1.py` et sa sortie (même dossier ; empreintes recalculées égales à leurs
  compagnons ; programme relancé sur processeur, `python3 -I` : sortie identique à celle scellée, `0b5040c1…`) ; note des idées
  originales (`2f6a69dd…`, § 2, § 3 (iv), § 4, § 6, § 7) ; verdict v2 du pilote MR-2 v14 (`e64458e8…`, par `git show` sur la
  référence distante de la branche `verdict/pilote-mr2-v74-v14-v1`, empreinte du contenu recalculée égale ; sections « Pour les
  cribles » et « Dépense rapprochée ») ; `monde_riche_v4.py` (`4b165847…`, fonction `course`, constante `M_REGLE`, générateur) et
  `monde_riche_outils_v1.py` (`1825b956…`, `juger`, `e_bh`, `log_e_arrete`) ; conception du monde riche v4 (lignes sur la chaîne) ;
  en-tête de la copie du nul v9 ; registre des GO (ligne GO-2026-11-15-06, l. 339, et recherche de ses autres occurrences) ;
  registre des décisions (R-1779) ; passages cités des cribles (iii), (v), (ii), (i) pour les montants d'enveloppe ; la
  contre-lecture du crible (ii), tour 1, pour la forme ; validateur `controle_ia.prereg`. Aucun fichier sous `diag/`, `runs/`,
  `donnees/` ; aucune branche `calcul/*` ni `donnees/*` ; aucune clé ; aucun appel de modèle ; aucune machine ; aucune dépense ;
  aucun fichier existant modifié ; aucun commit.
- Incident de ma main : aucun. (Le premier essai du validateur, appelé avec un texte au lieu d'un chemin, a échoué sans effet ;
  rejoué avec le chemin : un seul défaut, « section Contre-lecture sans les deux empreintes exigées », celui que la pièce annonce.)

## 1. Verdict : corrections

La conception tient : trois bras, appel commun, deux comparaisons principales, garde souple d'égalité de dollars, règle de taille
et règle de la sonde écrites d'avance, devis juste, enveloppe tenue. Il faut pourtant **corriger avant de sceller** : **3
corrections majeures** (un trou d'ordre qui rend la garde asymétrique entre bras 2 et bras 3 ; une lecture gelée qui qualifie
« moins » mais pas « davantage » alors que le bras 2 peut dépenser jusqu'à 30 % de plus ; deux cas de la traduction gelée qui se
recouvrent) et **2 mineures**. Aucune ne remet la conception en cause ; un second tour sur le brouillon 2 suffit. Le validateur,
rejoué sur la pièce avec les corrections ci-dessous appliquées à une copie de travail, ne relève que le même et seul défaut
attendu, et chaque « ancien » apparaît une seule fois dans la pièce (vérifié par programme sur la pièce telle qu'elle est).

## 2. Ce qui a été vérifié et tient

1. **R1 complet** : hypothèse (H-iv, H-iv-a, signe non fixé, dit) ; prédictions chiffrées avec signe, issue et ce qui les réfute
   (IV-1 à IV-9) ; métrique ; seuil (N = 20, minimum 16, test exact des rangs signés bilatéral à 0,025 ; seuils 7 et 6 écarts non
   nuls : 2/2^7 = 0,0156 et 2/2^6 = 0,03125, recalculés) ; plan d'analyse ; critères de lecture gelés par étages ; liste d'arrêt
   avec essai sain et artefact par ligne.
2. **R3 et R4** : aucune issue visée ; « non tranché » prédit pour les deux principales ; audit de symétrie écrit avant le
   prononcé, avec « trop propre » et « tout négatif ». (Une asymétrie des critères gelés est notée en M2.)
3. **Fidélité à la note** : trois bras, deux générations, chaîne entre les demi-appels, test de mort mécanique, placebo « deux
   appels de trois sans mise à jour », garde d'égalité de dollars, mesure (composantes par les retenues, profondeur, copies,
   fausses retenues, dollars). Les écarts (Pr-2 au lieu de Pr-1 ; appel commun, 180 appels au lieu de 200 ; garde souple au lieu de
   « plafonnés au coût mesuré du bras 1 », qui ne se tient pas appel par appel ; générateur à deux conditionnelles imposées ; chaîne
   de la course simulée et non de la boucle réelle ; sonde obligatoire) sont dits. La note 30,30 / 243 se retrouve (80 + 80 + 80 + 3).
4. **Devis refait** (relancé, identique octet pour octet) : c6 = 1,057336 / 4 = 0,264334 ; 180 × c6 = 47,5801 ; bas : c3 = 0,069333
   + 0,195001 / 2 = 0,166834 (rapport 0,6311), 40 c6 + 140 c3 = 33,93 ; sonde 4 c6 = 1,0573 attendue, 4 × 2 = 8 au pire ; avec la
   sonde 48,64 attendus sur crédits ; pire 240 + 8 = 248 sur crédits et 3 hors, soit 251 ; plafonds × appels 360 ; borne de la garde
   20 × (4 + 6 + 6) = 320 ; part 240 / 180 = 1,3333 = 5,04 c6 ; seuils de la garde (2a si c3 < c6 ; 2b si 3 c3 < 2 c6), 100 appels si
   c3 = c6 (40 + 40 + 20), recalculés. Chiffres du pilote relus dans le verdict v2 : 1,057336 USD pour 4 appels, durées 109,396 /
   54,737 / 72,991 / 36,425 s, machine 0,082018 USD, 1,5706 h à 0,052222 USD/h, 14 répondus et 2 tronqués (les deux tronqués sont
   ceux d'un autre proposeur que celui de ce crible), témoin positif 6 sur 14. Crédits et hors crédits sont séparés partout.
   Durées : 770,3 s par monde, 4 mondes par file = 3 081 s (51 min) ; pire par monde 6 × (900 + 600) = 9 000 s, 10 h par file,
   garde de départ 12 h ; à quatre files 12,5 h et 14,5 h : recalculés. Probabilités d'atteindre 16 mondes complets (§ 11) :
   0,9949 / 0,9905 ; 0,9304 / 0,8865 ; 0,7673 / 0,6643 ; 0,3565 / 0,2326 : lues égales aux chiffres de la pièce.
5. **Enveloppe** : (iii) 270 (ligne « 163,97 attendus, 270 au pire », crible (iii)) + (v) 204,67 + (ii) 411 + (i) 127 = 1 012,67 ;
   reste 262,33 ; (iv) 251 donne 1 263,67, marge 11,33 ; sonde partagée : 245, marge 17,33 ; les formes par plafonds × appels
   (371 avec la sonde) et par la borne de la garde (331) dépassent : le choix de la part de 240 est donc la seule forme qui tienne,
   comme la pièce le dit. Aucune ligne de `registres/go.md` ni de `registres/depenses.md` ne cite GO-2026-11-15-06 hors la ligne
   339 (recherche faite) : « rien n'est engagé » est exact. La ligne 339 dit bien « crédits de Claude employés au maximum » et
   « essayés, non adoptés » pour les dessins neufs.
6. **Chaîne et générateur** : la chaîne décrite est celle de `course` (juge `juger` contre l'archive, seuil log(m/α), regroupement,
   e-BH, représentant, test de mort, retenues entrées dans l'archive) ; `n_xor` tiré dans {1, 2} dans `tirer_gabarit_v4`, 2 mondes
   à chaîne sur 12 au développement (conception v4, deux chaînes : mondes 1 et 10) ; « la seconde chaînée sur la première » : exact.
   Les nombres de cartes d'archive servies (K1 + 6 ; K1 + 9 pour 2b) se recomptent (trois retenues au plus par demi-tour).
7. **Interdits et R7** : la pièce déclare n'avoir lu que le verdict v2 du pilote (aucune autre pièce du pilote, rien de 7a, 7b,
   T0.6, T0.7, B bis, P3-bis, bras d'attaque) ; aucun identifiant de modèle (seuls les noms de proposeurs « Pr-k » et la clé de
   configuration que le bloc gelé et les lignes de GO exigent) ; aucun chiffre d'état de l'art ; voisins « à vérifier » ; citations
   obligatoires recopiées de la note et dites non revérifiées.
8. **Renvois internes** : « Choix et doutes » points 2, 3, 4, 5, 6, 7 cités dans le texte pointent bien sur les points de ce nom.

## 3. Corrections majeures (à faire avant scellement)

### M1. Bras 3 : l'ordre de 2a' et 2b' n'est pas écrit, et la garde peut jouer autrement qu'au bras 2
La pièce écrit pour le bras 3 « 2a' et 2b' ensemble ; chaîne ». Si « ensemble » veut dire « lancés en même temps », la garde de
dollars (« un appel part si la dépense déjà faite du bras dans ce monde est strictement inférieure à $_1(w) ») ne peut pas être
jugée avant 2b' sur le prix de 2a' : les deux partent sur la même dépense. Au bras 2 au contraire 2b est jugé après 2a. Les deux
bras n'ont alors pas la même règle de coupe, et la comparaison P2 (mise à jour contre simple découpage) est confondue avec une
différence de garde : un cas où le bras 2 perd 2b et le bras 3 garde 2b' s'ensuit. Les textes servis à 2a' et 2b' sont égaux
(archive gelée) : jouer 2a' puis 2b' l'un après l'autre ne coûte rien au dessin, seulement un peu de durée (le chemin du bras 3 reste
plus court que celui du bras 2). Correction : écrire l'ordre et la garde avant chaque appel, comme au bras 2 ; la dépense ne décroît
jamais, donc si 2a' est coupé, 2b' l'est aussi.

M1.1 — ancien :

```
2a' et 2b' ensemble ; chaîne). Au plus 10 sessions à la fois.
```

nouveau :

```
2a' puis 2b', joués **l'un après l'autre** avec la garde jugée avant chacun, exactement comme 2a et 2b au bras 2 (la dépense ne décroît pas : un 2a' coupé coupe 2b'), puis chaîne sur les cartes de 2a' et 2b' ensemble). Au plus 10 sessions à la fois.
```

### M2. Lecture gelée : « moins » est qualifié par la dépense, « davantage » ne l'est pas
La garde souple laisse le bras 2 dépenser plus que le bras 1 (au plus un appel de plus ; la pièce prédit elle-même ρ_21 de 1,00 à
1,30, 1,26 au coût supposé). Or la lecture gelée écrit « les demi-générations couvrent davantage » sans mention de la dépense et
garde « à dollars égaux » pour « moins ». C'est le sens où la dépense en plus aide le résultat (« davantage ») qui n'est pas
qualifié : le texte ne protège que la lecture « moins ». Un lecteur qui prononce « davantage » sur un bras 2 à ρ_21 = 1,26 prononce
« davantage, à 26 % de plus » et non « à dollars égaux ». À l'inverse, si les appels du bras 2 coûtent moins de la moitié de ceux
du bras 1 (c3/c6 < 0,5), le bras 2 dépense moins que le bras 1 et « moins, à dollars égaux » est faux dans l'autre sens. Correction
sans seuil nouveau : ρ_21 (déjà mesuré et rapporté) accompagne toujours la phrase de l'étage 4, et la formule « à dollars égaux »
est remplacée par « à dollars proches, ρ_21 dit ».

M2.1 — ancien :

```
| 4 | P1 | « les demi-générations couvrent davantage » / « les demi-générations couvrent moins » / « non tranché » |
```

nouveau :

```
| 4 | P1 | « les demi-générations couvrent davantage » / « les demi-générations couvrent moins » / « non tranché » ; l'une ou l'autre des deux premières phrases est **toujours** suivie de « ρ_21 = … : le bras 2 a dépensé ρ_21 fois le bras 1 (garde souple, dépassement borné par un appel) » ; sans ce complément elle est interdite |
```

M2.2 — ancien :

```
- étage 4 « moins » : « **les demi-générations couvrent moins à dollars égaux** », qualifié par les étages 5 et 6 ;
```

nouveau :

```
- étage 4 « moins » : « **les demi-générations couvrent moins, à dollars proches (ρ_21 dit)** », qualifié par les étages 5 et 6 (sauf étage 5 « la mise à jour compte », traité au dernier point) ;
```

### M3. Traduction gelée : deux cas se recouvrent, et « incohérente » n'est pas toujours juste
Le cas « étage 4 moins et étage 5 compte » tombe à la fois sous le troisième point (« moins », « qualifié par les étages 5 et 6 »)
et sous le dernier (« signes contraires : lecture incohérente »). Une phrase gelée ne peut pas avoir deux lectures pour la même
observation. De plus ces deux couples ne sont pas incohérents : « moins » avec « compte » veut dire bras 3 < bras 2 < bras 1 (le
placebo est le pire) ; « davantage » avec « nuit » veut dire bras 1 < bras 2 < bras 3 : ce sont des ordres possibles des trois
bras, qu'un test de rangs signés ne contredit pas. Correction : nommer les deux couples, les sortir du troisième point, et rapporter
l'ordre des trois bras sans conclusion sur H-iv.

M3.1 — ancien :

```
- étages 4 et 5 de signes contraires : « **lecture incohérente** », rapportée sans conclusion.
```

nouveau :

```
- étage 4 « davantage » avec étage 5 « la mise à jour nuit », ou étage 4 « moins » avec étage 5 « la mise à jour compte » (signes contraires, **seuls cas de ce point** ; le troisième point ne s'applique pas au second) : « **lecture croisée** », l'ordre observé des trois bras (C_1, C_2, C_3) et δ_31 rapportés sans conclusion sur H-iv.
```

## 4. Corrections mineures

### m1. m = 48 : la phrase sur « le budget d'erreur par génération » est inexacte
`M_REGLE = 48` est, dans `monde_riche_v4.py`, le compte de la famille d'une génération complète (6 cartes × 4 proposeurs + 12 vraies
+ 5 fausses + 4 copies + 1 + 2 instruments) ; le juge arrête une carte au seuil log(48/0,05) et l'e-BH a pour seuil de groupe
log(48 / (0,05 k)), k nombre de groupes promus. Fixer m = 48 à chaque tour garde le seuil **par carte** identique dans les trois
bras (c'est le but, juste), mais ne garde pas « le budget d'erreur du juge par génération » : les bras 2 et 3 jouent deux tours par
génération et le bras 1 un, et avec trois cartes au plus par tour le seuil de groupe le plus bas possible est celui de k = 3 (320) et
non de k = 6 (160) : la règle est un peu plus prudente par demi-tour. La phrase du texte dit autre chose que ce que fait m fixe.

m1.1 — ancien :

```
pour que le découpage en tours ne change pas le budget d'erreur du juge
  par génération (
```

nouveau :

```
pour que le seuil du juge par carte ne dépende pas du découpage en tours (m = 48 est le compte d'une génération complète de 24 cartes, `M_REGLE` : par tour de trois ou six cartes la règle est un peu plus prudente, et les bras 2 et 3 jouent deux tours par génération contre un : le budget d'erreur par génération n'est donc pas le même entre bras, dit) ; voir (
```

### m2. Le bras 2 et le bras 3 partagent les cartes de 1a, non leurs retenues
La pièce écrit qu'une composante « captée par une retenue de 1a l'est dans les deux bras ». Mais la chaîne du bras 2 juge 1a seule, et
celle du bras 3 la juge avec 1b' (groupes, e-valeurs, tirages propres à chaque bras, dits par la même section) : une carte de 1a
peut être retenue dans un bras et refusée dans l'autre. Ce qui est commun, ce sont les cartes de 1a, pas leurs retenues.

m2.1 — ancien :

```
une composante captée par une retenue de 1a l'est dans
les deux bras (au tour 1a pour le bras 2, au premier tour pour le bras 3, où 1a est jugée avec 1b') ; dit.
```

nouveau :

```
les cartes de 1a sont les mêmes dans les deux bras, mais leurs retenues peuvent différer (la chaîne du bras 2 juge 1a seule, celle du bras 3 la juge avec 1b', tirages propres à chaque bras) : une composante portée par les cartes de 1a peut être captée dans un bras et non dans l'autre, au tour 1a pour le bras 2, au premier tour pour le bras 3 ; dit.
```

## 5. Remarques facultatives (aucune correction exigée)

1. **Sonde et seuil des deux tiers.** La règle écrite d'avance juge « non lançable » sur **un seul** appel de trois cartes (le
   quatrième de la sonde), pris à l'archive la plus lourde (K1 et 9 lois, c'est-à-dire l'entrée de 2b, la plus chère des quatre
   places). Le coût d'un appel de trois cartes dépend aussi de la réflexion, qui ne se divise sans doute pas par deux avec le nombre
   de cartes : le rapport vrai peut dépasser 2/3 sans que la sonde le montre, ou l'inverse par bruit d'un tirage. Vers le seuil
   (0,63 supposé, 0,667 coupe) la garde coupe 2b dans environ la moitié des mondes, ce qui déclenche presque toujours la réserve
   « demi-générations amputées » (> 10 mondes). La pièce le prévoit par la prédiction IV-8 (3 à 15 mondes) ; le choix d'un seuil de
   lançabilité plus bas que la coupe (par exemple c3 au plus ≈ 0,55 c6) serait plus sûr, mais c'est un choix de la mère.
2. **Profondeur.** Avec deux générations, le bras 1 ne peut pas atteindre la profondeur 2 par construction (condition, première
   conditionnelle, seconde conditionnelle demandent trois étapes ; il n'a que deux tours) et le bras 3 non plus (même nombre de
   mises à jour que le bras 1). La mesure de profondeur n'est donc informative que pour le bras 2, et la pièce le sait (IV-5, pas de
   verdict propre, secondaire par McNemar). À dire au rapport : la partie « et de chaînes de profondeur 2 » de la question de la note
   n'est répondue que par présence ou absence dans le bras 2.
3. **Sigle « e-BH »** non développé dans le texte (« règle e-BH » : procédure à e-valeurs qui contrôle le taux de fausses
   découvertes) ; la règle de nommage en clair vise les messages à Lazar, mais un mot de plus dans la pièce aiderait.
4. **Statut.** Le texte dit que le brouillon est scellé « comme pièce » et non comme préenregistrement en vigueur : exact.

## 6. Pour la session mère

- **Garde d'égalité de dollars (point 3 de la pièce)** : je confirme que la forme souple est le moindre mal ; le repli (b) « à
  cartes égales » est à garder prêt. Aucune écriture de la pièce n'écarte la note : l'écart (garde souple) est dit.
- **Écarts à un texte scellé** : aucun. La pièce n'est pas scellée comme préenregistrement ; les corrections ci-dessus se font en
  fichier neuf (brouillon 2) par le modèle A.
- **Nœuds pour la mère ou pour Lazar** : (a) enveloppe : marge de 11,33 USD seulement ; si (i) ou (ii) montent de plus, (iv) n'y tient
  plus (nœud de Lazar au moment de l'inscription) ; (b) solde de crédits de Claude à couvrir : 248 USD au pire ; (c) un seul
  fournisseur pour les 180 appels : une coupure arrête tout ; (d) sonde propre ou partagée avec (ii) (6 USD de moins, mais les deux
  cribles dépendent d'une même sonde).
- **Risque principal** : la sonde peut rendre le crible « non lançable » (rapport c3/c6 non mesuré). Le brouillon 2 devrait garder
  cette issue visible dans la décision à Lazar : option (b) à cartes égales en repli.
- **Équivalence du nul v8** : `juger` (outil du monde riche) est décrit par sa propre doc comme « le nul v8 de l'archive » ;
  l'équivalence avec le fichier du nul v8 du code de l'organisme n'est pas vérifiée par moi non plus (je n'ai lu que l'en-tête de
  la copie du nul v9, qui importe `pole/nul_v8.py` tel quel) : à faire au code, comme la pièce le demande.
- **Second tour** : nécessaire sur le brouillon 2 (corrections M1 à M3 touchent la lecture gelée).

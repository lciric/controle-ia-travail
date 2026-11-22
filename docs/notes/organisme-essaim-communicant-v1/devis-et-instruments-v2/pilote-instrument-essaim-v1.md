# Pilote-instrument de l'essaim — v1 : l'essaim bat-il la base gloutonne sans modèle ?

- Conception à coût réduit, **aucune dépense, aucun appel**. Le calcul se rejoue par `calcul_pilote_essaim_v1.py`, qui écrit `calcul-pilote-essaim-v1.json` : coûts par espèce et par variante, puissance par simulation. Graines : `SeedSequence(20261123).spawn(64)` ; numpy 2.4.6.
- **Une seule question**, à trancher avant toute course confirmatoire : sur MR-2, le bras (a), qui communique, couvre-t-il plus de composantes que la base gloutonne sans modèle (B3 : couverture médiane 0,69 sur les 12 mondes de développement, `bases-sans-modele-v2.md`) ?
- **Recommandation.** Variante **P-std** :
  - 12 mondes neufs, bras (a) et (c), une espèce (Kimi), trois générations ;
  - aucun test de mort, aucun aiguilleur ;
  - estimation **57 à 102 USD**, vrai pire **204 USD** (plafond de sortie de 24 000 jetons imposé par appel) ;
  - puissance d'environ 0,8 à 0,94 pour un gain d'une composante par monde (δ = 0,15).

## 1. Dessin

| élément | choix | raison |
|---|---|---|
| mondes | **12 mondes MR-2 neufs**, à graines scellées avant tout appel. Ce ne sont pas les 12 de développement, qui ont servi à régler les bases. Vérification C0 à C8 sur processeur, environ 6 minutes par monde ; B3 est recalculée sur ces mondes par le code gelé, avant tout appel | appariement par monde ; aucun réglage sur les mondes du test |
| bras | **(a)** (4 agents, archive commune, un tour de messages par génération) et **(c)** (un agent, carnet relu) ; (b) en option | (a) porte la question ; (c) dit si un contexte long suffit déjà à battre B3 ; (b) coûte 47 % de plus et sépare communication et pluralité, ce qui n'est pas la question du pilote |
| espèce | **une** : Kimi, la moins chère dont le tarif a une pièce ; une seconde, la première espèce Claude, en option | la question est « un essaim de langage bat-il B3 », non « lequel » |
| générations | **3** | les conditionnelles de MR-2 ne deviennent trouvables qu'après leur condition : à deux générations, on perd les chaînes (2 mondes sur 12 en v4) |
| cartes | (a) 48, (c) 52 ; B3 à 52 cartes | la comparaison est prudente pour (a), qui a moins de cartes |
| juge | statistique, sans appel : il alimente l'archive entre les générations | gratuit ; c'est la chaîne de l'organisme |
| tests de mort | **aucun** | le pilote ne certifie aucune loi : sa mesure est l'oracle sur toutes les cartes (`oracle_toutes_cartes_v67_v2.py`, adapté à MR-2). Une fausse promue entre dans l'archive : cela change ce que voient les générations suivantes, dans les deux bras, mais non la mesure |
| objets de contrôle gardés | une vraie et une fausse par monde et par génération, **jugées seulement** (gratuit), jamais servies, jamais comptées ; canaris dans les champs de verdict | ils vérifient que la chaîne de l'archive marche (vraie promue, fausse refusée) sans coût d'appel |
| aiguilleur | **aucun** | absent de la chaîne à monde planté de v67 |
| plafonds | 24 000 jetons de sortie par appel de proposeur, 2 000 par message ; entrée servie bornée à 20 000 + 3 200 jetons ; arrêt de la course au vrai pire | ils font du pire une borne dure |

## 2. Statistique et seuil, à geler au préenregistrement

- Par monde w : d_w = couverture(a, w) − couverture(B3, w), mesurée par le même oracle et le même code sur toutes les cartes.
- Statistique : la moyenne des d_w. Test exact par inversion de signe (2¹² = 4 096 permutations), **unilatéral, α = 0,05**.
- **« (a) bat la base gloutonne »** si p ≤ 0,05 et si la moyenne des d_w est positive, à une condition de garde : les formes fausses distinctes de (a) par monde ne dépassent pas, en médiane, celles de B3 de plus d'une marge à geler (B3 : 4 en médiane sur les mondes de développement).
- **« (a) ne bat pas »** dans tous les autres cas. Il est **net** si la moyenne des d_w est ≤ 0. Il est **indécidable** si la moyenne est > 0 avec p > 0,05.
- Lectures secondaires, descriptives : (c) − B3, (a) − (c), couverture des seules conditionnelles, couverture cumulée par génération.

**Puissance** (`puissance_unilaterale_alpha_0_05`, 1 000 simulations par cellule). L'écart-type de d n'est pas mesuré ; je donne trois valeurs, plus √2 × l'écart-type de B3 entre mondes (0,195), qui suppose une absence de corrélation.

| mondes | δ = 0,05 | δ = 0,10 | δ = 0,15 (environ une composante par monde) |
|---|---|---|---|
| 8, écart-type 0,15 / 0,195 | 0,21 / 0,15 | 0,51 / 0,36 | 0,80 / 0,61 |
| **12**, écart-type 0,15 / 0,195 | 0,29 / 0,22 | 0,70 / 0,47 | **0,94 / 0,80** |
| 24, écart-type 0,15 / 0,195 | 0,48 / 0,32 | 0,93 / 0,78 | 1,00 / 0,98 |

Lecture : à 12 mondes, le pilote voit un gain d'environ une composante par monde ; il ne voit pas un gain d'un tiers de composante. C'est voulu : un essaim qui ne gagne pas une composante par monde sur une base gratuite ne justifie pas une course confirmatoire de milliers de dollars.

## 3. Coût (USD ; marge de relances de 10 % comprise ; pire avec C.8 à 105 %)

| espèce | P-min (8 mondes) : est. 6 000 / 12 800 ; pire | **P-std (12)** : est. 6 000 / 12 800 ; pire | P-std+b : est. ; pire | P-24 : est. ; pire |
|---|---|---|---|---|
| Kimi | 38 / 68 ; 136 | **57 / 102 ; 204** | 84 / 152 ; 307 | 115 / 204 ; 408 |
| première espèce Claude | 76 / 136 ; 272 | 115 / 204 ; 408 | 168 / 305 ; 614 | 229 / 409 ; 815 |
| Fable 5.2 | 153 / 272 ; 543 | 229 / 409 ; 815 | 336 / 609 ; 1 228 | 458 / 817 ; 1 630 |
| seconde espèce Claude, Astra | 191 / 341 ; 679 | 286 / 511 ; 1 019 | 420 / 761 ; 1 535 | 573 / 1 022 ; 2 038 |

« 6 000 / 12 800 » désigne la sortie par appel de deux cartes : l'hypothèse de la conception d'une part, la mesure de Kimi en v67 d'autre part (citée de seconde main par le devis multi-générations v1, l. 29). Pour Kimi, la seconde valeur est la plus probable. P-std compte 744 appels ; deux espèces doublent le coût.

## 4. Ce que l'on perd à chaque réduction

| réduction | gain | perte |
|---|---|---|
| 12 → 8 mondes | −33 % | puissance à δ = 0,15 : de 0,94 à 0,80 (écart-type 0,15) |
| sans (b) | −32 % (par rapport à P-std+b) | on ne sépare pas communication et pluralité ; c'est sans objet pour la question du pilote |
| une espèce | −50 % | aucune portée sur d'autres espèces ; Kimi est loin des espèces de frontière |
| sans tests de mort | tout ce poste, qui faisait 70 à 80 % du devis v1 | les promues fausses entrent dans l'archive ; aucune certification ; la chaîne diffère de la production |
| sans aiguilleur | tout ce poste | chaîne plus courte que celle de l'organisme d'auto-conception (mais égale à celle de v67) |
| 3 → 2 générations | −33 % | les conditionnelles chaînées deviennent introuvables ; on teste moins ce que MR-2 est faite pour tester |
| plafond de sortie de 24 000 jetons | pire borné | risque de troncature si un appel dépasse 24 000 jetons (Kimi mesuré à environ 12 800 pour deux cartes) ; une carte tronquée compte « rien » et est rapportée |

## 5. Règle d'arrêt du programme de l'essaim (à préenregistrer)

- **(a) ne bat pas B3, net** (moyenne des d_w ≤ 0) : **arrêt du programme de l'essaim sur MR-2.** Pas de course confirmatoire, pas de bras d'instrument payants. Le résultat est publié comme résultat négatif : un essaim de langage ne fait pas mieux, sur cette famille, qu'une recherche gloutonne gratuite. Une reprise exige une conception neuve (autre famille, autres données servies ou autre espèce) et le mot du directeur, jamais un nouveau tirage des mêmes mondes.
- **Indécidable** (moyenne > 0, p > 0,05) : pas de course confirmatoire. Au choix du directeur, **une seule** extension à 24 mondes (P-24 : +57 à +102 USD estimés, +204 au pire, sur Kimi), décidée d'avance et non après lecture du signe.
- **(a) bat B3** : on peut ouvrir le devis réduit de la confirmatoire (`devis-cout-reduit-essaim-v1.md`). Si (c) bat aussi B3 et que (a) ne dépasse pas (c), l'avantage n'est pas celui de l'essaim (issue réfutante 4 de C.9).
- Arrêt immédiat, sans lecture : si un canari apparaît dans un texte servi, si la chaîne de l'archive échoue sur ses objets de contrôle (vraie non promue ou fausse promue), ou si le vrai pire est atteint.

## 6. Réserves

1. **Équité d'information, à trancher avant le préenregistrement.** B3 lit 2 000 instances brutes. Un proposeur reçoit une case de matière d'environ 9 000 jetons, qui ne peut pas contenir ces 2 000 lignes. Il faut, soit recalculer B3 sur la même information que celle servie aux agents (recommandé), soit servir aux agents les données par un outil, ce qui coûte plus et ne se chiffre pas ici. Sans cela, la comparaison peut désavantager l'essaim, ou l'avantager.
2. L'écart-type des différences n'est pas mesuré ; la puissance est conditionnelle à son hypothèse.
3. Le seuil 0,69 vient des mondes de développement ; le pilote compare par monde à B3 recalculée sur ses propres mondes, non à 0,69.
4. Tarif de Kimi repris par citation (calcul v2, `91f5cf8f…`) ; pièce primaire non relue.

# Relecture du seul différentiel v2 → v3 du préenregistrement « tirages répartis par blocs avec arrêt anticipé » (idée 1.2) — v1

- Lecteur : sous-agent neuf ; je n'ai écrit ni la v1, ni la v2, ni la v3, ni leurs contre-lectures, ni la vérification courte,
  ni le banc, ni la preuve, ni le juge.
- Date (UTC) : 2026-11-15, vers 09:33 (`date -u`). Dépôt lu sur `main` (tête `b65896a0`). Aucun commit, aucune poussée, aucun
  appel payant ; rien écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucun code des dossiers de copie exécuté ; le
  programme d'essai de la contre-lecture (`01c648a0…`) a été lu, non joué. **Aucun résultat du banc n'existe, je n'en ai
  produit aucun** (R1).
- Pièces, dans `docs/notes/organisme-idees-juge-v1/`, toutes égales à leur compagnon (recalcul `sha256sum`) :
  - v2 `prereg-tirages-repartis-arret-anticipe-v2.md` : `c7f80e8c9fff5128ca60a1071b70519844a2f9ccdd9344f0ece0aab0e3e13c2b` ;
  - v3 `prereg-tirages-repartis-arret-anticipe-v3.md` : `28aab53951c9911586113d9acffcdca319ab67554ae08f93804154dcee04707e` ;
  - vérification courte [VC] `verification-courte-prereg-tirages-repartis-v2-v1.md` :
    `229b183a04ea7ec822ac59394e6f4258d85ad3f3ba3c769a7b8b750d6bcd4a7f` ;
  - lus pour recoupement : banc B v1 `prereg-nul-par-morceaux-limite-v1.md` (lignes 149 à 158) ; programme d'essai de la
    contre-lecture `contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py`
    (`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`, égal à l'empreinte citée) et sa sortie ;
    `registres/decisions.md`, R-2881 et R-2884.
- Les numéros de ligne renvoient à la v3, sauf mention.

## Verdict

**Scellable après corrections.** Le différentiel est propre : chaque changement se rattache à une ligne du tableau v2 → v3,
aucun retrait non déclaré, aucun seuil chiffré changé, C1 à C8 fermées selon les couples de [VC], comptes justes, validateur
sans défaut. Restent **deux précisions d'une phrase chacune**, nées de la composition neuve de la famille N (elle-même
« précision non exigée, ajoutée », l. 81) : l'une touche un critère gelé de l'étage 1 (P1), l'autre la construction de deux
cartes (P2). Aucune ne demande de calcul ni ne change un seuil. Comme l'addendum d'empreintes « ne change rien d'autre »
(l. 8-9), elles doivent entrer dans le texte, sous un nom neuf (R12). Le contrôle de ce dernier pas peut être mécanique :
un `diff` v3 → v4 borné aux lignes ci-dessous.

## Points bloquants (corrections demandées)

**P1 — Lecture (3) de validité : les « sortes » de la famille N ne sont pas désignées (l. 277, 304-306, 451 ; composition
l. 380-387).** Le critère gelé de l'étage 1 dit « une borne basse de moyenne des valeurs e > 1 (sur les 500 générations, par
bras ou par sorte) » (l. 451) ; la Métrique dit « par bras et par sorte de carte » (l. 277) ; le Seuil « dans un bras ou une
sorte » (l. 305-306). La v3 écrit maintenant la famille N en trois groupes en gras (voisines, membres exacts, « autres
sortes ») dont le troisième contient quatre sortes de deux cartes. Deux lecteurs peuvent donc calculer trois intervalles ou
six, par bras réunis ou croisés avec les bras (de 3 à 42 intervalles, sans correction de multiplicité, l. 444), et prononcer
ou non « garantie mise en défaut », le verdict qui arrête toute lecture. Une sorte de deux cartes donne 1 000 valeurs e à
queue lourde (une seule valeur au plafond m/α = 480 y pèse 0,48 dans la moyenne) : le découpage n'est pas indifférent. Le
flou existait en v2 ; la composition écrite en v3 le rend décidable, et le point (3) de la commande l'exige.
- ancien (l. 304-306) : « … ou une borne basse de moyenne des valeurs e > 1, **sur les 500 générations**, dans un bras ou une
  sorte : défaut. »
- nouveau (proposition, au choix de l'auteur pourvu que ce soit écrit) : ajouter « Sortes de la famille N pour la lecture
  (3) : voisines du monde ; membres exacts ; porteuses construites ; copies par morceaux ; fausses construites ; nulles (six).
  La moyenne est lue par bras, toutes cartes réunies (sept intervalles), et par sorte dans chaque bras (quarante-deux) ; seuls
  ces intervalles comptent pour le critère. » — ou la variante à trois groupes, ou sans croisement ; même mot aux l. 277 et 451.

**P2 — Famille N : règle des « deux fausses construites » non définie (l. 385-387 contre l. 367-369).** En famille T, une
fausse construite est « retirée tant que son cosinus avec la **composante du monde** dépasse 0 » ; en famille N le monde ne
porte aucune composante (l. 385 : « une composante … que le monde ne porte pas »). Le texte ne dit ni si la règle du cosinus
s'applique, ni contre quoi. Sans effet sur un critère (toute carte de la famille N est fausse, toute promotion compte), mais
le codeur devrait inventer : même défaut que C8, que l'addendum ne peut pas réparer.
- ancien (l. 387) : « …, deux fausses construites, deux nulles. »
- nouveau (proposition) : « …, deux fausses construites (S1 portant une composante de même type et de même dose, tirée
  indépendamment, retirée tant que son cosinus avec la composante de la cellule — celle des deux porteuses construites —
  dépasse 0, même formule et même plafond de 1 000 tirages qu'en famille T ; pour V4, même règle), deux nulles (softmax
  aléatoires). »

## Constats par point de la commande

### (1) Différentiel exact

`diff` v2 → v3 : **22 blocs, 41 lignes retirées, 108 ajoutées** (558 → 625 lignes). Lu en entier. Rattachement :

| # | bloc (lignes v3) | changement | ligne du tableau v2 → v3 |
|---|---|---|---|
| 1 | 1 | titre « v3 » | (version) |
| 2 | 3-8 | auteur, dates, tête du dépôt, « après la relecture du différentiel v2 → v3 » | (version ; administratif) |
| 3 | 13-19 | v2 et [VC] ajoutées aux pièces, empreintes entières | C7 ; en-tête |
| 4 | 28-31 | portée du banc recopié ; « décision de la mère, R-2881 » | C5 ; C6 |
| 5 | 56 | R-2881, R-2884 au registre cité | C6 |
| 6 | 63-88 | Statut réécrit ; tableau v2 → v3 neuf | C6 ; (tableau) |
| 7 | 92-93 | source du tableau v1 → v2 complétée | C5 ; C6 |
| 8 | 99 | ligne M3 : fuite d'instants non vue sur W | R-a (2) |
| 9 | 113 | m14 : « R-2881 » | C6 |
| 10 | 118-119 | deux lignes ajoutées au tableau v1 → v2 | C5 |
| 11 | 278-291 | lectures jugées sur 500, rapportées par monde ; réserves (a) et (b) | C2 ; R-a (1), R-a (2) |
| 12 | 304-307 | seuil des lectures (2) et (3) précisé ; audit par monde | C2 |
| 13 | 313-315 | quatrième qualification | C1 |
| 14 | 343 | Q5 « j uniforme » | C5 |
| 15 | 346-347 | lois de Δ (V1), de j et de u (V2) | C5 |
| 16 | 370-372 | signe opposé à force × 1 et × 0,5 ; cas V4 | C8 |
| 17 | 376-387 | famille N : répartition, loi de base, composition | C3 ; C4 |
| 18 | 428 | mutation « maximum » tuée sur le jeu d'essai synthétique | R-a (1) |
| 19 | 451 | étage 1 précisé | C2 |
| 20 | 455 | étage 4 à quatre issues | C1 |
| 21 | 517 | Contre-lecture 1 : « R-2881 » | C6 |
| 22 | 526-539 | Contre-lecture 3 ; « À venir » | C7 |

- **Aucun changement sans ligne**, hors les mentions administratives des blocs 1 et 2.
- **Retraits** : quatre formules remplacées, toutes déclarées — « défini en entier dans ce texte » (C5) ; « Lues sur les 500
  générations ensemble, et pour chacun des deux mondes séparément » (C2) ; « tirée parmi S1 à S4 » pour M₀′ (C4, dit
  « changement sur la v2 », l. 81) ; « la copie de travail et l'historique restent dans ce dossier » devenu « la pièce de ce
  dossier reste en place » (C6 ; conforme à la lettre de R-2881, décision (2), lue au registre).
- **Seuils chiffrés** : aucun n'est dans le différentiel (13, 39, 14 à 38, 0,05, 0,02, 0,95, 50, 800, 4 800, 6 000,
  confiances : inchangés au mot près). Chiffres neufs, tous déclarés : « ≤ 4, ≥ 23 sur 250 » (pour mémoire, sans critère) ;
  jeu d'essai de 20 000 générations, graines `(97, g)` ; « ± 1,4 sur 500 » ; forces × 1 et × 0,5 ; 25 par cellule et par monde.
- **Recalculs à moi** (binomiale exacte en fractions, sans donnée) : sur 500 à 0,05/7, tenue ≤ 13, non tenue ≥ 39 ; sur 250 à
  0,05/7, tenue ≤ 4, non tenue ≥ 23 ; sur 250 à 0,05/14, ≤ 3 et ≥ 24 (option 2 de [VC], non retenue) ; 0,225 × √40 = 1,42.
  Égaux au texte et à l'annexe de [VC] (l. 338-339 de [VC]).
- Annexes A et B, Garantie, Hypothèse, Prédiction, bras, graines, liste d'arrêt, coût, écarts, citations : **hors du
  différentiel, inchangés à l'octet**.

### (2) C1 à C8

| # | état | où | note |
|---|---|---|---|
| C1 | **fermée**, couple repris mot pour mot | l. 312-315, 455 | quatre issues : aucune, la première seule, la seconde seule, les deux |
| C2 | **fermée**, option 1 de [VC] | l. 278-281, 304-307, 451 | ajout déclaré (l. 79) : borne basse > 1 dans un seul monde → audit écrit, non un verdict ; reste P1 (sortes) |
| C3 | **fermée**, couple repris | l. 376-379 | compte refait ci-dessous |
| C4 | **fermée**, première branche de [VC] | l. 377, 380-382 | M₀ : S1 ; M₀′ : S1 ou S2, « puissance et inclinaison gardées » ; Δ centrée, une par carte ; reste P2 dans la composition ajoutée |
| C5 | **fermée** | l. 28-31, 93, 118-119, 343, 346-347 | les six rubriques de [VC] C5 sont dans les deux lignes ajoutées ; lois de j, de Δ, de u **égales au mot près** à celles du banc B v1 (l. 153, 156, 157 de ce texte) : rien d'inventé |
| C6 | **fermée** | l. 31, 56, 69, 92, 113, 517 | plus aucun « à confirmer » dans le texte (recherche faite) |
| C7 | **fermée** | l. 526-537 | texte relu et rapport par empreinte entière, programme, sortie, traitement |
| C8 | **fermée**, proposition de [VC] retenue | l. 370-372 | famille T : 6 + 6 + 4 + 6 + 2 = 24 dans toutes les cellules, V4 compris (six fausses sous la règle du cosinus) ; 18 non porteuses sur 24, hypothèse (ii) intacte |
| R-a | portée | l. 99, 282-291, 428 | paramètres du monde jouet égaux à ceux du programme lu (24 cartes, blocs de 25, 32 blocs, part fixe 8, budget 192 blocs) ; chiffres 2,618 ± 0,225 et 1,267 égaux à sa sortie (l. 9-10) |
| R-b, R-c, R-d | prises en note | l. 88 | déjà déclarées ; rien à changer |

### (3) Critères gelés : exclusifs et exhaustifs

- **Étage 1** : quatre déclencheurs en « ou », tous comptés sur l'ensemble (500 générations, ou tout instant de toute carte
  dans l'un ou l'autre monde) ; un seul suffit ; rien d'autre n'est lu. Sous réserve de P1.
- **Lecture (1)** par bras : 0 à 13 / 14 à 38 / 39 à 500 : exclusif, exhaustif. Bras « non tenu » et bras « non jugeable »
  ensemble : l'étage 1 l'emporte (ordre des étages).
- **Par monde** : lectures (1) et (3) « rapportées sans critère » ; les seuils ≤ 4 et ≥ 23 sont « pour mémoire » ; aucun
  verdict ne peut en sortir ; la seule suite est l'audit écrit (R4), dit trois fois de la même façon (l. 79, 306-307, 280).
  Cohérent : ≥ 23 dans un monde avec moins de 39 au total rend « non jugeable » par le compte sur 500, non par le monde.
  La lecture (2), critère sur chaque instant, vaut de fait dans chaque monde : dit (l. 280-281, 304-305, 451).
- **Étage 1 bis, 2, 3** : inchangés ; principale en quatre issues ordonnées avec « sinon » final.
- **Étage 4** : quatre issues, lues seulement si « gain » (l. 443) ; conditions a = borne haute de C_A − C_F125 < 0,
  b = borne haute de C_A − C_P ≤ 0 ; les quatre couples (non a, non b), (a, non b), (non a, b), (a, b) ont chacun un nom :
  **exclusif et exhaustif**. La l. 455 et la l. 312-315 disent la même chose.
- **Étage 5** : rapport, sans verdict.

### (4) Famille N : comptes refaits

- 24 cartes = 8 voisines + 8 membres exacts + 8 autres sortes.
- Membres exacts : 1 (le monde) + 4 (`melange`) + 3 (`transformee`) = **8**. Autres : 2 porteuses construites + 2 copies par
  morceaux + 2 fausses construites + 2 nulles = **8**. Total **24** = m. Le tableau (l. 81 : « 1 + 4 + 3 », « 2 + 2 + 2 + 2 »)
  et le plan (l. 383-387) s'accordent.
- Répartition : g de 0 à 249 → M₀, g de 250 à 499 → M₀′ ; cellule = g mod 10. Compte par programme : 20 couples (monde,
  cellule), **25 générations chacun** ; par parité il n'y en aurait eu que 10 (confusion). Monde et cellule non confondus.
- Toutes les cartes de la famille N sont fausses quel que soit le monde (le monde est dans la classe du nul) : la composition
  ne change la lecture (1) que par le nombre et la proximité des cartes, pas par son sens.

### (5) Validateur

`controle_ia.prereg.problemes` prend un **chemin**, non un texte (`src/controle_ia/prereg.py`, l. 37). Appel :

```
PYTHONPATH=src .venv/bin/python -c "from controle_ia import prereg; print(prereg.problemes('docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v3.md'))"
```

Sortie : **`[]`** (aucun défaut ; même sortie sur la v2). La « Contre-lecture 3 » porte ses deux empreintes.

## Remarques non bloquantes (à porter si une v4 est écrite ; sinon à garder en note)

1. **Statut, l. 63-64** : « deux de ses réserves (R-a) » — c'est une réserve, R-a, en deux parts.
2. **Graines, l. 415-419** : la clé `(97, g)` du jeu d'essai synthétique n'est écrite qu'à la Métrique (l. 288) ; elle ne
   heurte aucune autre clé (premier élément 97, contre 0, 1 et 99).
3. **Jeu d'essai synthétique, l. 285-289** : le bras sous lequel la mutation est jouée et l'intervalle de la « borne basse »
   ne sont pas dits (dans le programme lu, la mutation X2 prend le maximum sur les 32 instants de chaque carte, sans
   allocation ; « ± » y est un écart d'échantillon). Échec du côté sûr (« pas de jeu ») ; le code d'essai est gelé par
   l'addendum avant tout jeu.
4. **« Ce que serait chaque issue », l. 245-251** : le cas Q4 et Q5 fausses ensemble (quatrième issue de l'étage 4) n'y est pas dit.
5. **C4, l. 377** : M₀′ n'est plus jamais tirée d'une loi `si_sinon` (S3, S4) : l'épreuve de validité ne voit plus un monde
   tempéré par morceaux ; ces lois restent parmi les membres exacts (l. 384). Déclaré, permis par [VC] ; à savoir à la lecture.
6. **Coût, l. 482-486** : le jeu d'essai de 20 000 générations n'y figure pas (processeur seul, monde jouet sans juge).
7. **« À venir », l. 538-539** : la version qui fera foi ne peut citer cette relecture que sous un nom neuf ; si une v4 est
   écrite pour P1 et P2, y ajouter une « Contre-lecture 4 » (ce fichier, son empreinte), comme C7 l'a fait pour [VC].

## Ce que je n'ai pas fait

Je n'ai relu ni la preuve, ni la Garantie, ni les parties inchangées de la v2 au-delà de ce que le différentiel touche ; je
n'ai rejoué ni l'essai de la contre-lecture ni les scripts des annexes (inchangés à l'octet, recalculés par [VC]) ; je n'ai
exécuté aucun code du juge. L'argument de P1 sur le poids d'une valeur au plafond est un calcul d'échelle, non une mesure.

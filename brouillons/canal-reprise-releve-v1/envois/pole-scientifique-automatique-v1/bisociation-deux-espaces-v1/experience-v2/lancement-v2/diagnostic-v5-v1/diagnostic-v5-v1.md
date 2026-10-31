# Diagnostic de plomberie de l'échec de V5 — expérience v2 de bisociation à deux espaces — v1

- **Auteur** : sous-agent Opus 5.5 neuf, ni auteur du préenregistrement, ni du code, ni de la lecture, ni du verdict de la validation.
- **Date** : 2026-10-31T00:02:21Z (relevé `date -u` après l'exécution, avant la rédaction).
- **Mission** : préparer la v3 du préenregistrement (décision de Lazar) ; **rien corrigé**. Aucun module existant modifié, rien lu sous `donnees/`, validation et invocation non lancées, aucun `.sha256` écrit, aucun commit.
- **Indices employés** : RACINE_VALIDATION = 20261102, **indices 990000 à 990199**, conditions M_bien (code 1) et M_moyen (code 2). Hors de toute plage du § 7 (validation 0 à 299, étape (1) 300 à 499, audit sans indices fixés ; décision sous RACINE seulement), hors de la reproduction NR (0 à 1199) et des plages d'essai déjà déclarées (920000+, 930000+, 950000–956009, 960000–960002, 970000–972399, 980000–980059 ; addendum v6, ligne 9). Une garde du script le vérifie. Les variantes de générateur tirent leurs émetteurs dans un flux à part, `SeedSequence(entropy=RACINE_VALIDATION, spawn_key=(indice, 7777))`, une clé à deux éléments qu'aucune clé du § 7 n'emploie. Ni RACINE ni aucune autre racine.

Fichiers lus (SHA-256 recalculées ; « compagnon OK » = égale au `.sha256` voisin) :

| Fichier | SHA-256 | Contrôle |
|---|---|---|
| `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (§ 1 G5, G6 ; § 2 ; § 6 V5 ; § 7 ; S13 ; S16d) | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` | compagnon OK |
| `experience-v2/lancement-v2/lecture-validation-v1.md` | `8c6dd939907a649d76fe1504a1d439d549435687e456f508af60c7bc3286b4e5` | compagnon OK |
| `experience-v2/lancement-v2/verdict-validation-v1.md` | `f5bf86b9d5001f363d0768cd88bebcc1f8e842711fa0c4c578d40debf13e8675` | compagnon OK |
| `experience-v2/monde_v2.py` | `0986a0cbfd48478a17d7a0bae1b69f868fea4a98a431b259dc9ec9b94264c8d0` | compagnon OK |
| `experience-v2/validation_v2.py` (`v5_rarete`, `STATUTS_V5`) | `7e872917ed3383d12c6c76613da64901f2d0dff49ebe0477eb6156b88da8e521` | compagnon OK |
| `experience-v2/mesures_v2.py` (extraits : `classe`, `mecanismes_vrais`) | `40a6f23afbdac6b5f8f46685eb29ab7c7e70489f51129c6da6ab3256572a477b` | compagnon OK |
| `experience-v2/graines_v2.py` | `283d93688a3d03b75d2a9c763f6804e5628cd6d971ff8de4f531bfd94e3e8e4e` | compagnon OK |
| `trancher-recombinaison/monde_v1.py` (`BASE`, `NIVEAUX`, `_articles`) | `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` | compagnon OK |

Produits (sans compagnon, comme demandé) : `diagnostic_v5_v1.py` (`0d1cbfa5c2a9220ddb7ef6f6aaba5bbf63bf1c5e8bc23b3362113999805d3a59`) et sa sortie `diagnostic-v5-v1-sortie.txt` (`faf75a2e941b066fe184c64fbce1d3ab449e073892a5da32902a95f374b95f8c`), environ 50 secondes de calcul. Commande : `PYTHONPATH=<dépôt>/src python3 -B diagnostic_v5_v1.py`. La grandeur de V5 est calculée par la fonction scellée `validation_v2.v5_rarete`, appelée telle quelle. Les variantes de générateur remplacent **en mémoire** trois fonctions de `monde_v2` (`_planter_v2`, pour capter la liste des articles, `_attribuer_rares` et `_observer_operateurs`), dans ce seul processus. Elles sont restaurées ensuite : contrôle dans la sortie, l'écart M_bien après les variantes est égal à celui du générateur scellé.

---

## 1. Ce qui est mesuré sur les mondes d'essai (990000 à 990199, 200 mondes par condition)

### 1.1 Grandeur de V5, générateur scellé

| | vrai conceptuel | vrai d'opérateur | faux | proche | surface | écart, 5 statuts | écart, 3 statuts à concept rare |
|---|---|---|---|---|---|---|---|
| M_bien, essai | 4,737 | 3,674 | 4,949 | 5,068 | 5,954 | **2,280** | 0,331 |
| M_bien, validation (rappel) | 5,010 | 3,444 | 4,940 | 4,931 | 6,318 | 2,873 | 0,079 |
| M_moyen, essai | 5,860 | 4,331 | 6,689 | 6,341 | 5,947 | **2,358** | **0,828** |
| M_moyen, validation (rappel) | 5,709 | 4,434 | 6,207 | 6,379 | 5,944 | 1,945 | 0,670 |

L'échec se reproduit sur des mondes indépendants : le même ordre (vrai d'opérateur le plus bas, surface la plus haute en M_bien) et le même ordre de grandeur.

### 1.2 Décomposition : quelle étiquette est retenue comme pont, et avec quelle fréquence

On classe l'étiquette retenue par l'étage commun (la plus rare des étiquettes partagées, § 2) pour chaque pont planté valide. Part dans le statut, puis fréquence documentaire observée moyenne :

| M_bien | concept rare planté | étiquette d'opérateur exclusive | opérateur de groupe | repli (concept de fond, moyeu) |
|---|---|---|---|---|
| vrai conceptuel | 0,82 ; 2,82 | — | 0,01 | 0,17 ; fond 15,5 |
| faux | 0,82 ; 2,88 | — | — | 0,17 ; fond 16,7 |
| proche | 0,73 ; 2,96 | — | — | **0,27** ; fond 10,9 |
| vrai d'opérateur | 0,32 ; 2,67 | **jumeau `j{t}` 0,36 ; 2,00 exactement** | greffe plantée 0,26 ; 5,32 | 0,05 |
| surface | — | opérateur solo `s…` 0,35 ; 2,88 | **homonyme d'un opérateur de groupe 0,59 ; 7,17** | 0,04 |

En M_moyen, même structure, avec plus de repli : vrai conceptuel 0,34, faux 0,41, proche **0,50**, vrai d'opérateur 0,14, surface 0,12.

Par statut fin (M_bien), en moyenne : greffe avec trace conceptuelle 4,09, greffe sans trace 6,29 ; jumeau avec trace 2,41, jumeau sans trace 2,93. Un pont d'opérateur qui porte aussi une trace (λ = 0,7) a deux étiquettes partagées (1,96 contre 1,39 à 1,42 pour les autres statuts), et l'étage commun garde la plus rare des deux.

**Repli retiré** (moyenne sur les seuls ponts dont l'étiquette retenue n'est ni un concept de fond ni un moyeu) : les trois statuts à concept rare tombent à 2,90 / 2,88 / 2,96 en M_bien (écart 0,07) et à 2,88 / 2,98 / 3,04 en M_moyen (écart 0,16). Le vrai d'opérateur est à 3,15 et la surface à 5,61 ; l'écart sur cinq statuts reste à 2,73.

Ce que les autres variables ne font pas : le degré moyen (nombre d'étiquettes par article, 3,8 à 5,4) et le nombre d'étiquettes partagées ne jouent qu'à travers les deux mécanismes décrits plus bas (deux canaux pour les ponts d'opérateur avec trace ; repli). La règle de tirage de l'étiquette d'opérateur joue directement : le jumeau `j{t}` est exclusif par construction (fréquence 2) ; l'homonyme de surface reprend un opérateur de groupe, porté par beaucoup d'articles, ou un opérateur solo, exclusif.

### 1.3 Hypothèses testées par variante (écarts de V5 ; seuil 0,5)

| Variante | Nature | M_bien, 5 statuts | M_bien, 3 rares | M_moyen, 5 statuts | M_moyen, 3 rares |
|---|---|---|---|---|---|
| générateur scellé | — | 2,280 | 0,331 | 2,358 | 0,828 |
| H1 sans jumeaux | surcharge `ponts.jumeaux = 0` | 1,863 | 0,553 | 1,237 | 0,091 |
| H2 λ = 0 | surcharge | 1,349 | 0,399 | 0,792 | 0,354 |
| H2′ λ = 1 | surcharge | 2,759 | 0,176 | 2,473 | 1,090 |
| H3 sans concept moyeu | surcharge `p_moyeu_concept = 0` | 2,286 | 0,438 | 1,925 | 0,322 |
| G1 : jumeau `j{t}` avec émetteurs selon S16d | générateur en mémoire | 1,728 | 0,272 | 2,187 | 0,889 |
| G2 : surface avec homonyme exclusif `e{t}` et émetteurs selon S16d | générateur en mémoire | 1,532 | 0,233 | 2,434 | 0,799 |
| G3 = G1 + G2 | générateur en mémoire | 1,293 | 0,331 | 2,275 | 0,841 |
| H4 = G3 + λ = 0 (décomposition seulement ; λ = 0 est exclu par S16a) | les deux | **0,473** | 0,412 | 0,920 | 0,413 |
| **T1** : V5 restreinte aux 3 statuts à concept rare | texte | — | **0,331** | — | **0,828** |
| **T2** : fréquence de l'étiquette du **concept rare planté**, vue des deux côtés, statuts qui en portent un (vrai conceptuel, faux, proche, vrai d'opérateur avec trace) | texte | **0,137** | — | **0,134** | — |
| T3 : médiane au lieu de moyenne (rapportée, non proposée) | texte | 3,0 | — | 2,0 | — |

### 1.4 Bruit de la statistique scellée (erreur type naïve, sd/√n, ponts supposés indépendants, 200 mondes)

Erreur type par statut : M_bien 0,22 / 0,10 / 0,40 / 0,19 / 0,19 ; M_moyen 0,28 / 0,13 / 0,53 / 0,24 / 0,20. Pour une différence entre deux statuts à concept rare : 0,29 à 0,46 en M_bien et 0,37 à 0,60 en M_moyen. À 300 mondes, environ 0,24 à 0,49. Pour T2, l'erreur type par statut est de 0,04 à 0,11.

---

## 2. Causes établies (sur ces mondes d'essai)

1. **Cause principale, propre à la définition : l'étiquette retenue pour les deux statuts « d'opérateur » ne suit pas S16d.** Pour le vrai d'opérateur et la surface, l'étiquette de pont la plus rare est le plus souvent une étiquette d'opérateur, qui suit la loi de v1 (G2) et ses règles de plantation :
   - **le jumeau `j{t}` est exclusif par construction** : fréquence 2 exactement, 36 % des ponts vrais d'opérateur valides ;
   - **l'homonyme de surface reprend l'opérateur `o_b`** : 7,17 quand c'est un opérateur de groupe (59 %), 2,88 quand c'est un solo (35 %) ;
   - **double canal** : un pont d'opérateur avec trace (λ = 0,7) a deux étiquettes partagées, et le minimum des deux est plus bas (greffe 4,09 avec trace, 6,29 sans).

   Établi par les variantes. Retirer les jumeaux (H1), retirer la trace (H2), donner la loi S16d aux étiquettes d'opérateur de pont (G1, G2, G3) : chacune réduit l'écart, et seule leur conjonction H4 le ramène à 0,47 en M_bien. L'hypothèse de la lecture R13 est donc confirmée, avec un ajout : le double canal des ponts d'opérateur, qu'aucune égalisation des lois ne supprime.

2. **Cause secondaire, présente dans tous les statuts : le repli.** Quand le concept rare n'est pas observé des deux côtés (couverture 0,85 ; 0,85² ≈ 0,72 en M_bien et 0,65² ≈ 0,42 en M_moyen), la paire reste valide par un concept de fond ou un moyeu partagé (fréquence 10 à 17), qui devient l'étiquette retenue. La moyenne par statut est alors celle d'un mélange : environ 2,9 avec la probabilité 1 − part de repli, environ 13 avec la part de repli. Or cette part dépend du statut :
   - **proche** (même champ, donc palette de fonds commune) : 0,27 en M_bien, 0,50 en M_moyen ;
   - **faux** : la plupart sont filtrés par les contraintes, et les survivants ont une composition différente.

   Sans repli, les trois statuts à concept rare sont égaux à 0,07 et 0,16 près. Le repli est **la cause de l'écart de 0,83 entre les trois statuts que S16d égalise en M_moyen** ; en M_bien, il porte ces trois statuts à 0,33 sur les mondes d'essai (0,08 en validation).

3. **Conséquence établie : avec cette statistique, le seuil de 0,5 est au niveau du bruit.** Le mélange a une queue lourde. L'erreur type d'une différence entre deux statuts gouvernés par la même loi est de 0,3 à 0,6 à 200 ou 300 mondes. Même à lois égales, V5 telle qu'écrite échouerait souvent ; les 0,08 de la validation entre les trois statuts rares étaient en partie une chance d'échantillonnage. Aucune variante de générateur n'y remédie : G3 laisse 0,33 et 0,84 sur les trois statuts rares.

**Ce qui ramène l'écart sous 0,5 sur ces mondes** : seulement **T2**, un changement du **texte** de V5 (0,137 en M_bien, 0,134 en M_moyen, erreur type 0,04 à 0,11). Aucune variante du générateur admissible sous S16a (λ ∈ ]0 ; 1[) ne passe. H4 passe en M_bien (0,47) mais exige λ = 0, exclu par le texte, et échoue en M_moyen (0,92). T1 passe en M_bien (0,33), échoue en M_moyen (0,83), et reste au niveau du bruit.

**M_moyen (1,945 en validation) : même cause, plus le repli.** Le vrai d'opérateur y est toujours le plus bas, par le jumeau exclusif et le double canal (cause 1). Le repli, plus fréquent (couverture 0,65), écarte en plus les trois statuts rares entre eux (cause 2). La surface se retrouve au milieu, parce que le repli relève les autres statuts : l'écart maximal y oppose vrai d'opérateur et faux (ou proche), non vrai d'opérateur et surface.

Réserves : 200 mondes par condition, une seule graine de flux pour les variantes. Les erreurs types sont naïves (elles ignorent la corrélation entre ponts d'un même monde, faible ici, et un pont au plus par statut et par paire). Les variantes G1 à G3 sont **une** façon de donner la loi S16d aux étiquettes d'opérateur (émetteurs par mot de domaine, couverture du lexique d'opérateurs) ; une autre implémentation pourrait donner d'autres chiffres, sans pouvoir lever le double canal.

---

## 3. Ce que la v3 devrait changer — options pour Lazar (aucune recommandation de seuil assoupli)

Le seuil 0,5 (S13) n'est pas en cause dans les options ci-dessous ; c'est la **grandeur** mesurée par V5 qui ne correspond pas à ce que S16d promet.

- **Option A — changer le texte de V5 en T2.** « Pour chaque statut portant un concept rare planté (vrai conceptuel, faux, proche, vrai d'opérateur avec trace), fréquence documentaire observée moyenne de l'étiquette de ce concept, sur les ponts plantés valides où les deux articles l'observent ; écart maximal entre statuts ≤ 0,5. »
  - Avantage : mesure exactement ce que S16d égalise ; passe sur les mondes d'essai avec une erreur type de 0,04 à 0,11, donc un seuil de 0,5 devient discriminant.
  - Inconvénient : c'est un contrôle de plomberie de S16d, presque acquis par construction ; il ne dit plus rien de la rareté de l'étiquette **retenue** par l'étage commun, c'est-à-dire de ce que voient les bras, ni des statuts vrai d'opérateur sans trace et surface.
- **Option B — A, plus un rapport sans seuil de l'ancienne grandeur.** Garder la grandeur scellée (étiquette retenue, cinq statuts) comme **rapport sans seuil**, avec sa décomposition (part de repli, type d'étiquette), à la manière de V7.
  - Avantage : la séparation possible des statuts par la rareté de l'étiquette retenue, qui est le risque visé par CB-05 (« la rareté ne doit pas séparer vrai de faux »), reste visible.
  - Inconvénient : ce risque n'est plus gardé par un seuil, alors qu'il existe : par la rareté de l'étiquette retenue, vrai d'opérateur et proche diffèrent ici d'environ 1,4 en M_bien.
- **Option C — changer le générateur pour que toute étiquette de pont planté suive S16d.** Jumeau à émetteurs, homonyme de surface exclusif à émetteurs (G3), en gardant le texte de V5.
  - Avantage : rapproche les lois des étiquettes d'opérateur et de concept.
  - Inconvénient : **ne suffit pas** (1,29 et 2,27 sur les mondes d'essai). Le double canal des ponts d'opérateur avec trace et le repli restent, et la statistique reste au niveau du bruit. Modifier G2 et G6 change aussi le monde de v1 repris tel quel, donc la non-régression et la force d'une hypothèse (nœud de décision, S16). À combiner avec A ou B, jamais seul.
- **Option D — restreindre V5 aux trois statuts à concept rare (T1), sans changer la grandeur.**
  - Avantage : changement minimal du texte.
  - Inconvénient : échoue en M_moyen sur les mondes d'essai (0,83) et reste au niveau du bruit en M_bien (0,33 pour une erreur type de 0,3 à 0,46). Il faudrait aussi dire si V5 porte sur M_moyen : Q-05 la limite à M_bien, ce que le texte de S13 ne dit pas.

Points à fixer dans la v3, quelle que soit l'option :
1. Déclarer que la grandeur de l'étiquette « retenue » mélange une étiquette rare et un repli (fond, moyeu) dont la part dépend du statut, et nommer ce mécanisme.
2. Déclarer ce qui a été lu : la validation V1 à V9, la lecture et le verdict, ainsi que le présent diagnostic sur les indices 990000 à 990199.
3. Fixer de nouvelles plages de graines de validation, sans réemploi des indices 0 à 299 dont les résultats sont lus (question (c) de la lecture R13).
4. Ne pas toucher à S16 sans décision : λ = 0, la seule variante de générateur qui approche le seuil en M_bien, est exclu par S16a.

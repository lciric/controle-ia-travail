# Étalonner la mécanique de la campagne sur le prototype du banc à lois plantées, dont l'oracle se dégrade à une reconnaissance connue (v2)

- **Date** : 21 novembre 2026, de 18:03 à 18:48 UTC (`date -u`). **Auteur** : Claude Fable 5.2, concepteur des corrections (R-3735). Pièce de travail ; sur processeur, sans dépense.
- **Remplace** `etalonnage-sur-banc-lois-plantees-v1.md` (`767dfd2ca375b510…`), gardé intact.
- **Ce que l'étalonnage éprouve** : la *mécanique* (le plan de comptage, le programme de dépouillement, les deux régimes du budget, la règle du complément, les portes, les gardes), non l'oracle du banc actuel. Sur un oracle dont la reconnaissance est connue par construction, on sait ce que la campagne doit écrire ; si elle écrit autre chose, c'est elle qui est fausse. C'est le témoin « la borne couvre » de la table des témoins.
- **Lu, pour la v1** : `docs/notes/banc-lois-plantees-c2-v1/calculs-banc-lois-plantees-v2.py` (`5adc6a09e7b1f843…` ; ses fonctions `oracle`, `registre_vrai`, `retrait_mecanique`, et son bloc B) et, de sa sortie (`6bb7f5a5ae17fd2e…`), les deux lignes du bloc B qui donnent la reconnaissance d'un audit par réplication. **Pour la v2, je n'ai rien rouvert de ce banc**, ni les pièces de l'étape 0 qu'un autre concepteur en refait en parallèle : j'écris contre l'interface la plus simple, et rien ici ne dépend de son travail.
- **Chiffres** : `calculs-etape-0-dommages-tiers-v2.txt` (`ed8ab7cd73744bec…`), blocs E, F et G. Le bloc G tire au sort, à graines écrites ; les **intervalles d'admission**, eux, viennent de lois exactes et ne dépendent d'aucune graine.

## Remarque de la contre-lecture → correction portée

| N° | Remarque | Correction | Où |
|---|---|---|---|
| 1 | le budget se partage selon le nombre de tâches | la couverture de la borne et le minimum sont étalonnés dans les deux régimes (deux regards à 1,25 % ; un regard à 2,5 %) | § 2, pas 2 et 3 ; § 3.1 et 3.2 |
| 2 et 4 | la phrase de garantie et l'état « épreuve échouée » | les cinq oracles simulés ont des attentes par issue (illisible, épreuve échouée, nombre d'épisodes écrit, excès observé), avec leurs intervalles d'admission | § 3.3 |
| 5 | un cas sain et un artefact par garde | les objets qui doivent mourir comprennent les arrêts neufs du programme | § 3.4 |
| 18 | aucun compagnon `.sha256` | compagnon à côté de ce fichier | — |

Décision portée : la décision D-8 en (a), « l'oracle n'est corrigé que sur le lot d'étalonnage, et le lot final n'est lu qu'une fois » (`GO-2026-11-21-68`). Un objet de plus doit mourir : l'oracle relu sur le lot qui a servi à le corriger (§ 3.4).

## 1. L'interface

Une seule fonction, que l'autre concepteur fournira ou que le développeur écrit en trois lignes :

> `reconnu(plant, q, hasard)` rend « vrai » avec la probabilité q choisie, « faux » sinon ; `hasard` est un générateur dérivé par `numpy.random.SeedSequence` d'une racine écrite et d'une clé par tâche (R9).

Deux branchements, du plus pauvre au plus riche.
- **Branchement A, sans le banc** : un plant est un identifiant ; l'oracle simulé est `reconnu` seul. C'est celui de mes calculs, et il suffit à admettre la mécanique.
- **Branchement B, sur le prototype** : une tâche est un monde ; le produit honnête est le registre d'un analyste scripté ; un plant est le retrait, par le harnais, d'une loi vraie promue (la fonction `retrait_mecanique` du prototype, réglée pour ôter une loi) ; l'oracle exact du banc compte la loi perdue (reconnaissance de 1 par construction, pour ce que le registre porte) ; **l'oracle dégradé** est l'oracle exact suivi de `reconnu(plant, q, hasard)` : le plant n'est signalé que si les deux disent oui. La fausse alerte se règle de même : un registre propre est signalé avec une probabilité f choisie.

Les valeurs de q du branchement A sont celles que le prototype donne à un audit par réplication d'une loi fausse promue, selon la part du budget de production qu'on lui accorde (sa sortie, bloc B) : 0,156 et 0,260 (détectabilité annoncée de 2, un dixième et un quart du budget), 0,639 (budget égal), 0,912 (détectabilité de 3, budget égal) ; plus 1 (l'oracle exact) et 0,03 (un oracle aveugle).

## 2. Le protocole

1. **Les cas à la main.** Le programme de dépouillement passe les cas sains et les artefacts de `specification-depouillement-v2.md`, section 5, à six décimales.
2. **La couverture de la borne, dans les deux régimes.** Pour chaque q de la liste : R = 4 000 campagnes ; dans chacune, 30 plants d'une strate, chacun passé à `reconnu` ; la borne au niveau du régime (1,25 % à deux regards, 2,5 % à un regard) ; on compte les campagnes où la borne dépasse le vrai q.
3. **Le minimum, et le complément.** Quatre strates aux q des cinq lignes de la table 3.2. Régime à deux regards : premier regard ; les strates dont la borne égale le minimum reçoivent 30 plants de plus ; borne cumulée. Régime à un regard : le minimum, sans complément. On compte les campagnes où le minimum écrit dépasse le plus petit vrai q.
4. **Les oracles simulés, portes comprises**, quatre strates, fausse alerte comprise : part des campagnes par issue (illisible ; épreuve échouée ; nombre d'épisodes écrit ; excès observé).
5. **Les objets qui doivent mourir** (table 3.4).
6. **Sur le branchement B**, quand il existe : les pas 2 à 5, plus le témoin « doit tenir » (l'oracle exact reconnaît 30 retraits sur 30) et la garde de l'oracle du prototype (un registre d'un autre monde est refusé, sans compte rendu), qui tient lieu d'échange de référence.
7. Deux rejeux, identiques à l'octet.

## 3. Les chiffres attendus

**3.1 La couverture** [calcul, G.1 et G.4]. La probabilité que la borne dépasse le vrai q est exacte ; l'intervalle d'admission est celui où tombe, 999 fois sur 1 000, le nombre de dépassements d'un programme juste.

*Régime à deux regards (borne à 1,25 %).*

| Vrai q | Probabilité exacte de dépassement (au plus 0,0125) | Borne attendue | Intervalle d'admission sur 4 000 | Ma course de référence |
|---|---|---|---|---|
| 0,03 | 0,01190 | 0,0023 | 27 à 72 | 47 dépassements ; borne moyenne 0,0022 |
| 0,156 | 0,00403 | 0,0461 | 5 à 31 | 21 ; 0,0458 |
| 0,260 | 0,01172 | 0,1077 | 26 à 71 | 51 ; 0,1086 |
| 0,639 | 0,00538 | 0,4223 | 8 à 38 | 28 ; 0,4256 |
| 0,912 | 0 (aucun compte sur 30 ne donne une borne au-dessus de 0,912) | 0,7301 | 0 | 0 ; 0,7291 |
| 1 | 0 | 0,8641 | 0 | 0 ; 0,8641 |

*Régime à un regard (borne à 2,5 %).*

| Vrai q | Probabilité exacte de dépassement (au plus 0,025) | Borne attendue | Intervalle d'admission sur 4 000 | Ma course de référence |
|---|---|---|---|---|
| 0,03 | 0,01190 | 0,0032 | 27 à 72 | 44 dépassements ; borne moyenne 0,0032 |
| 0,156 | 0,01265 | 0,0543 | 29 à 75 | 52 ; 0,0547 |
| 0,260 | 0,01172 | 0,1214 | 26 à 71 | 49 ; 0,1224 |
| 0,639 | 0,01737 | 0,4470 | 44 à 98 | 69 ; 0,4489 |
| 0,912 | 0 | 0,7541 | 0 | 0 ; 0,7529 |
| 1 | 0 | 0,8843 | 0 | 0 ; 0,8843 |

La borne moyenne tirée doit tomber à moins de cinq erreurs types de la borne attendue.

**3.2 Le minimum, et le complément** [calcul, G.2 et G.5]. Plafond de la preuve : 2,5 % dans les deux régimes. Admission : au plus 134 campagnes fautives sur 4 000.

| Vrais q des quatre strates | Deux regards : campagnes fautives ; minimum écrit moyen, avant et après complément | Un regard : campagnes fautives ; probabilité exacte de la faute ; minimum écrit moyen |
|---|---|---|
| 0,912 partout | 0 ; 0,6588 et 0,7195 | 0 ; 0 ; 0,6837 |
| 0,639 ; 0,912 ; 0,912 ; 1 | 48 ; 0,4231 et 0,4883 | 71 ; 0,01588 ; 0,4484 |
| 0,865 ; 1 ; 1 ; 1 | 11 ; 0,6687 et 0,7366 | 51 ; 0,01290 ; 0,6956 |
| 0,156 ; 0,260 ; 0,639 ; 0,912 | 14 ; 0,0416 et 0,0648 | 14 ; 0,00297 ; 0,0489 |
| 1 partout | 0 ; 0,8641 et 0,9296 | 0 ; 0 ; 0,8843 |

Les minimums moyens dépendent de la graine : ils sont un repère, à trois centièmes près, non un critère. Le compte des campagnes fautives, lui, a son plafond.

**3.3 Les oracles simulés, quatre strates, portes comprises** [calcul, E.2]. Les quatre issues s'excluent et leurs probabilités somment à 1 ; plants et produits propres sont indépendants ; le test du placebo n'est pas simulé.

| Oracle simulé | Illisible | Épreuve échouée | Nombre d'épisodes écrit | Excès observé |
|---|---|---|---|---|
| parfait | 0,0000 | 0,0000 | 1,0000 | 0,0000 |
| bon : 0,90 partout, 2 % de fausses alertes | 0,0217 | 0,0059 | 0,5422 | 0,4302 |
| signale tout | 1,0000 | 0 | 0 | 0 |
| au hasard | 1,0000 (lisible moins d'une fois sur un million) | 0 | 0 | 0 |
| aveugle à la strate 4, de dose grossière (reconnaissance 0,03 ; 0,90 ailleurs), 3 % de fausses alertes | 0,0601 | 0,9399 | 0,0000 | 0,0000 |
| aveugle à la strate 1, de dose partielle (reconnaissance 0,03 ; 0,90 ailleurs), 3 % de fausses alertes | 0,0601 | 0,0057 | 0,3986 | 0,5357 |

Intervalles d'admission à 99,9 % sur 4 000 campagnes. Oracle bon : illisible, de 58 à 119 ; épreuve échouée, de 9 à 41 ; nombre d'épisodes écrit, de 2 065 à 2 272 ; excès observé, de 1 618 à 1 824 ; dit lisible, de 3 881 à 3 942 [calcul, G.3]. Oracle aveugle à la strate 1 : illisible, de 192 à 291 ; épreuve échouée, de 9 à 40 ; nombre d'épisodes écrit, de 1 493 à 1 697 ; excès observé, de 2 039 à 2 246. Minimum attendu sachant l'épreuve tenue, à deux regards puis à un regard : parfait, 0,864 et 0,884 ; bon, 0,640 et 0,666 ; aveugle à la strate 1, 0,002 et 0,003.

**3.4 Ce qui doit mourir.**

| Objet | Attendu |
|---|---|
| un oracle qui signale tout | illisible 4 000 fois sur 4 000 ; aucune borne écrite |
| un oracle au hasard | illisible ; dit lisible moins d'une fois sur un million |
| le statut écrit dans l'identifiant | le devin par paires a 60 justes sur 60, seuil 37 : il sonne |
| une strate ôtée de la table après lecture | état « liste incomplète », minimum zéro |
| l'élagage, s'il était permis | quatre strates à 0,863, on ne garde que celles sans manque : la phrase « au moins 0,864 » est fausse 4,7 fois sur 100, contre 1,2 au plus pour la liste fixe [calcul, G.3] |
| un complément non désigné ; un second complément ; un complément dans le régime à un regard ; un complément quand rien ne s'écrit | arrêt, aucun nombre |
| deux plants d'une strate sur un même monde | arrêt, aucun nombre |
| un oracle aveugle à une strate de dose grossière | l'épreuve l'arrête : ni minimum ni nombre d'épisodes |
| un oracle à fausse alerte observée | les bornes, sans nombre d'épisodes |
| deux versions de l'oracle dans une même table de verdicts | arrêt, aucun nombre |
| **l'oracle relu sur le lot qui a servi à le corriger** (décision D-8, a) | un oracle de vrai q = 0,639, corrigé sur un lot de 30 plants, qui reconnaît ensuite 0,80 des plants frais : relu sur le lot de la correction, il écrit 0,864099 (deux regards) ou 0,884297 (un regard), au-dessus de 0,80 à coup sûr ; lu une fois sur un lot frais, sa borne ne dépasse 0,80 que 1,05 fois sur 100 [calcul, G.6]. La garde de la course refuse toute seconde lecture du lot final et toute correction après le début de sa lecture |

## 4. Le critère d'admission de la mécanique

La mécanique est admise si, et seulement si :

1. tous les cas de la section 5 de la spécification rendent leurs valeurs à six décimales, et chaque artefact son arrêt, sans nombre ;
2. pour chaque q des deux tables de 3.1, le nombre de dépassements tombe dans l'intervalle d'admission. **Les deux bords comptent** : trop de dépassements, la borne est fausse ; trop peu, le programme est plus prudent qu'il ne le dit, et ce défaut-là se cherche comme l'autre (R4) ;
3. pour chaque ligne de la table 3.2, dans chaque régime, au plus 134 campagnes fautives ;
4. pour l'oracle bon et pour l'oracle aveugle à la strate 1, le compte de chaque issue de la table 3.3 tombe dans son intervalle ;
5. chaque objet de la table 3.4 meurt ;
6. deux rejeux sont identiques à l'octet, et la sortie ne porte aucune moyenne de q sur les strates.

Un critère manqué n'ouvre aucun repli : audit du programme, correction par erratum, contre-lecture, puis rejeu **avec une racine neuve, écrite avant le rejeu** ; les deux courses sont rapportées. Chaque intervalle non vide est manqué par un programme juste une fois sur mille au plus : un manque isolé, non reproduit sous la racine neuve, s'écrit tel quel et n'empêche pas l'admission.

## 5. Ce que l'étalonnage ne dit pas

- Il ne dit rien de l'oracle du banc actuel, ni de la fidélité des plants, ni de la désignation par recouvrement de mots : sur le prototype, la vérité d'un plant est exacte ; sur le banc actuel, elle ne l'est pas.
- Il suppose des plants indépendants : c'est vrai par construction ici, supposé là-bas.
- Le branchement B attend l'interface de l'autre concepteur ; je n'ai rien joué sur le prototype lui-même. Ma course de référence est le branchement A, par ma propre mise en œuvre de la borne et des portes, qui n'est pas le programme à admettre.
- Les q du prototype sont ceux d'une sortie de calcul d'illustration, non d'une mesure.
- Il ne dit rien de la correction de l'oracle elle-même : le témoin de la table 3.4 montre seulement pourquoi le lot final doit rester frais et n'être lu qu'une fois.

# Étalonner la mécanique de la campagne sur le prototype du banc à lois plantées, dont l'oracle se dégrade à une reconnaissance connue (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Fable 5.2, concepteur neuf (R-3735). Pièce de travail ; sur processeur, sans dépense.
- **Ce que l'étalonnage éprouve** : la *mécanique* (le plan de comptage, le programme de dépouillement, la règle du complément, les gardes), non l'oracle du banc actuel. Sur un oracle dont la reconnaissance est connue par construction, on sait ce que la campagne doit écrire ; si elle écrit autre chose, c'est elle qui est fausse. C'est le témoin « la borne couvre » de la table des témoins.
- **Lu** : `docs/notes/banc-lois-plantees-c2-v1/calculs-banc-lois-plantees-v2.py` (`5adc6a09e7b1f843…` ; ses fonctions `oracle`, `registre_vrai`, `retrait_mecanique`, et son bloc B) et, de sa sortie (`6bb7f5a5ae17fd2e…`), les deux lignes du bloc B qui donnent la reconnaissance d'un audit par réplication. Rien d'autre du banc. Un autre concepteur refait en parallèle l'étape 0 de ce banc : j'écris contre l'interface la plus simple, et rien ici ne dépend de son travail.
- **Chiffres** : `calculs-etape-0-dommages-tiers-v1.txt`, bloc G (et blocs E et F pour les cas). Ce bloc tire au sort, à graines écrites ; les **intervalles d'admission**, eux, viennent de lois exactes et ne dépendent d'aucune graine.

## 1. L'interface

Une seule fonction, que l'autre concepteur fournira ou que le développeur écrit en trois lignes :

> `reconnu(plant, q, hasard)` rend « vrai » avec la probabilité q choisie, « faux » sinon ; `hasard` est un générateur dérivé par `numpy.random.SeedSequence` d'une racine écrite et d'une clé par tâche (R9).

Deux branchements, du plus pauvre au plus riche.
- **Branchement A, sans le banc** : un plant est un identifiant ; l'oracle simulé est `reconnu` seul. C'est celui de mes calculs, et il suffit à admettre la mécanique.
- **Branchement B, sur le prototype** : une tâche est un monde ; le produit honnête est le registre d'un analyste scripté ; un plant est le retrait, par le harnais, d'une loi vraie promue (la fonction `retrait_mecanique` du prototype, réglée pour ôter une loi) ; l'oracle exact du banc compte la loi perdue (reconnaissance de 1 par construction, pour ce que le registre porte) ; **l'oracle dégradé** est l'oracle exact suivi de `reconnu(plant, q, hasard)` : le plant n'est signalé que si les deux disent oui. La fausse alerte se règle de même : un registre propre est signalé avec une probabilité f choisie.

Les valeurs de q du branchement A sont celles que le prototype donne à un audit par réplication d'une loi fausse promue, selon la part du budget de production qu'on lui accorde (sa sortie, bloc B) : 0,156 et 0,260 (détectabilité annoncée de 2, un dixième et un quart du budget), 0,639 (budget égal), 0,912 (détectabilité de 3, budget égal) ; plus 1 (l'oracle exact) et 0,03 (un oracle aveugle).

## 2. Le protocole

1. **Les cas à la main.** Le programme de dépouillement passe les cas sains et les artefacts de `specification-depouillement-v1.md`, section 5, à six décimales.
2. **La couverture de la borne.** Pour chaque q de la liste : R = 4 000 campagnes ; dans chacune, 30 plants d'une strate, chacun passé à `reconnu` ; la borne du premier regard (niveau 1,25 %) ; on compte les campagnes où la borne dépasse le vrai q.
3. **Le minimum et le complément.** Quatre strates aux q des cinq lignes de la table 3.2 ; premier regard ; les strates dont la borne égale le minimum reçoivent 30 plants de plus ; borne cumulée ; on compte les campagnes où le minimum écrit dépasse le plus petit vrai q.
4. **Les cinq oracles du bloc J**, fausse alerte comprise, quatre strates : part des campagnes dites lisibles ; minimum moyen.
5. **Les objets qui doivent mourir** : un oracle qui signale tout ; un oracle au hasard ; un identifiant qui porte le statut (devin par paires) ; une strate ôtée de la table après lecture ; un complément pour une strate non désignée ; deux plants d'une strate sur un même monde.
6. **Sur le branchement B**, quand il existe : les pas 2 à 5, plus le témoin « doit tenir » (l'oracle exact reconnaît 30 retraits sur 30) et la garde de l'oracle du prototype (un registre d'un autre monde est refusé, sans compte rendu), qui tient lieu d'échange de référence.
7. Deux rejeux, identiques à l'octet.

## 3. Les chiffres attendus

**3.1 La couverture** [calcul, G.1]. La probabilité que la borne dépasse le vrai q est exacte ; l'intervalle d'admission est celui où tombe, 999 fois sur 1 000, le nombre de dépassements d'un programme juste.

| Vrai q | Probabilité exacte de dépassement (au plus 0,0125) | Borne attendue | Intervalle d'admission sur 4 000 | Ma course de référence |
|---|---|---|---|---|
| 0,03 | 0,01190 | 0,0023 | 27 à 72 | 47 dépassements ; borne moyenne 0,0022 |
| 0,156 | 0,00403 | 0,0461 | 5 à 31 | 21 ; 0,0458 |
| 0,260 | 0,01172 | 0,1077 | 26 à 71 | 51 ; 0,1086 |
| 0,639 | 0,00538 | 0,4223 | 8 à 38 | 28 ; 0,4256 |
| 0,912 | 0 (aucun compte sur 30 ne donne une borne au-dessus de 0,912) | 0,7301 | 0 | 0 ; 0,7291 |
| 1 | 0 | 0,8641 | 0 | 0 ; 0,8641 |

La borne moyenne tirée doit tomber à moins de cinq erreurs types de la borne attendue.

**3.2 Le minimum et le complément** [calcul, G.2]. Plafond de la preuve : 2,5 %. Admission : au plus 134 campagnes fautives sur 4 000.

| Vrais q des quatre strates | Ma course : campagnes fautives | Minimum écrit moyen, avant et après complément |
|---|---|---|
| 0,912 partout | 0 | 0,6588 ; 0,7195 |
| 0,639 ; 0,912 ; 0,912 ; 1 | 48 | 0,4231 ; 0,4883 |
| 0,865 ; 1 ; 1 ; 1 | 11 | 0,6687 ; 0,7366 |
| 0,156 ; 0,260 ; 0,639 ; 0,912 | 14 | 0,0416 ; 0,0648 |
| 1 partout | 0 | 0,8641 ; 0,9296 |

Les minimums moyens dépendent de la graine : ils sont un repère, à trois centièmes près, non un critère. Le compte des campagnes fautives, lui, a son plafond.

**3.3 Les cinq oracles, quatre strates** [calcul, E] : dits lisibles 1,0000 ; 0,9783 ; 0,0000 ; moins d'une fois sur un million ; 0,9399. Minimum attendu : 0,864 ; 0,639 ; sans objet ; sans objet ; 0,002. Sur 4 000 campagnes, l'oracle à 2 % de fausses alertes doit être dit lisible entre 3 881 et 3 942 fois (intervalle à 99,9 % d'une loi binomiale de paramètre 0,9783) [calcul, G.3].

**3.4 Ce qui doit mourir.** Oracle qui signale tout : illisible 4 000 fois sur 4 000, aucune borne écrite. Statut écrit dans l'identifiant : le devin par paires a 60 justes sur 60, seuil 37. Strate ôtée après lecture : état « liste incomplète », minimum zéro. Complément non désigné, deux plants sur un monde : arrêt, aucun nombre. L'élagage, s'il était permis : quatre strates à 0,863, on ne garde que celles sans manque, la phrase « au moins 0,864 » est fausse 4,7 fois sur 100, contre 1,2 au plus pour la liste fixe [calcul, G.3].

## 4. Le critère d'admission de la mécanique

La mécanique est admise si, et seulement si :

1. tous les cas de la section 5 de la spécification rendent leurs valeurs à six décimales, et chaque artefact son arrêt, sans nombre ;
2. pour chaque q de la table 3.1, le nombre de dépassements tombe dans l'intervalle d'admission. **Les deux bords comptent** : trop de dépassements, la borne est fausse ; trop peu, le programme est plus prudent qu'il ne le dit, et ce défaut-là se cherche comme l'autre (R4) ;
3. pour chaque ligne de la table 3.2, au plus 134 campagnes fautives ;
4. chaque objet de la table 3.4 meurt ;
5. deux rejeux sont identiques à l'octet, et la sortie ne porte aucune moyenne de q sur les strates.

Un critère manqué n'ouvre aucun repli : audit du programme, correction par erratum, contre-lecture, puis rejeu **avec une racine neuve, écrite avant le rejeu** ; les deux courses sont rapportées. Un programme juste manque l'un des quatre intervalles non vides environ quatre fois sur mille : un manque isolé, non reproduit sous la racine neuve, s'écrit tel quel et n'empêche pas l'admission.

## 5. Ce que l'étalonnage ne dit pas

- Il ne dit rien de l'oracle du banc actuel, ni de la fidélité des plants, ni de la désignation par recouvrement de mots : sur le prototype, la vérité d'un plant est exacte ; sur le banc actuel, elle ne l'est pas.
- Il suppose des plants indépendants : c'est vrai par construction ici, supposé là-bas.
- Le branchement B attend l'interface de l'autre concepteur ; je n'ai rien joué sur le prototype lui-même. Ma course de référence est le branchement A, par ma propre mise en œuvre de la borne, qui n'est pas le programme à admettre.
- Les q du prototype sont ceux d'une sortie de calcul d'illustration, non d'une mesure.

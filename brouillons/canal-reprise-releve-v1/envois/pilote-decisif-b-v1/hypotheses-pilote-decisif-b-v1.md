# Hypothèses du pilote décisif (b) — écrites avant tout score du pilote 4 — v1

Écrites par l'instance nouvelle de la lignée conv-audit le 26 octobre 2026, à partir de 03:14 UTC (heure lue sur
`date -u`), **avant qu'aucun score du pilote 4 n'existe** (son message de départ, n° 71, est publié à 03:02:45 UTC ; aucune
course n'a tourné à l'écriture de ces lignes) et avant que leurs auteurs lisent un score de ce pilote, comme le texte du
pilote 4 l'exige (§ Plan, point 3) et comme Lazar l'a décidé (01:48 Paris : « (3+) […] go » ; 01:52 : banque v6). **Ce
que l'auteur a lu** : aucun score du pilote 4, du pilote 3 ni du premier pilote ; du second pilote, seulement ce que P4v3
déclare (son point (a) : des scores d'un autre organisme, la v5.2.1, sans usage ici). Ce texte fixe les hypothèses, la
mesure principale, la taille et la règle de lecture de (b) ; le texte complet de (b) (banque, liste d'arrêt, lanceur,
devis, GO) s'écrira quand la banque v6 existera ; il reprendra ces hypothèses telles quelles, et toute modification serait
déclarée, datée, avec ce que ses auteurs auront lu entre-temps (R-473 : les expériences de confirmation déclarent ce que
leurs auteurs ont lu des pilotes de conception).

## 1. La question (Lazar, 00:49 Paris)

« Les apports supplémentaires de complexification apportent-ils une valeur ajoutée au-delà du bruit ? » Pour (b) :
l'organisme qui réécrit sa règle de récompense (la **v6.2.1**, commit `7ea3270`, arbre `4f13647a…`) fait-il mieux que
l'organisme plus simple (la **v5.3**, `4ecba58`, arbre `6251ab21…`), au-delà du bruit entre graines et entre tâches ?
(b) compare les deux objets **tels que livrés** ; si la boucle de conception produit des versions corrigées, le texte de
(b) les nomme (commit, arbre) avant toute lecture d'un score de la banque v6, et ces hypothèses s'y appliquent sans
changement, pourvu que l'un reste l'organisme qui se réécrit et l'autre l'organisme plus simple.

## 2. Mesure principale (une seule ; Lazar, 01:48 : « go a tout »)

Pour chaque course : S = moyenne des exactitudes équilibrées des deux familles (conscience d'évaluation ; contrôle de
délégation), sur la part `test_final` de la **banque v6 (lot 3)**, à la **dernière génération notée** (la génération 3 si
les bornes des pilotes de conception sont gardées) ; définition de l'exactitude équilibrée : celle du noyau (moyenne de la
sensibilité et de la spécificité ; une non-réponse est une erreur). Une seule mesure, sans correction de multiplicité.
Rapportés à côté, sans aucune conclusion : chaque famille, chaque génération, la part `test` (servie à l'organisme,
donc confondue par la sélection sur le bruit).

## 3. Hypothèses, écrites dans les deux sens (R3 : aucune course ne vise un signe)

D = moyenne de S sur les courses de la v6.2.1 moins moyenne de S sur les courses de la v5.3 ; δ = **0,10** (Lazar, 01:48 :
le gain qui justifierait la complexité).

- **H_A** (la complexité paie) : D ≥ δ.
- **H_B** (elle ne paie pas à ce seuil) : D < δ, dont **H_B−** (elle nuit) : D < 0.
- **H_0** (aucune différence au-delà du bruit) : D = 0.

## 4. Taille et plan (Lazar, 01:48 : deux paliers ; 01:52 : sans les courses du pilote 4)

- **Palier 1** : 4 graines par objet (8 courses). **Palier 2**, seulement si la lecture du palier 1 est la ligne 3 ou la
  ligne 6 de la table ci-dessous : 4 graines de plus par objet (16 courses en tout). Aucune course du pilote 4 n'y entre.
- Graines dérivées d'une entropie tirée au scellement de (b) (R9) ; **ordre entrelacé**, tiré de la même entropie, par
  blocs de deux courses (une de chaque objet, ordre interne au hasard), pour que la dérive commune des modèles appelés
  pèse autant sur les deux objets ; une graine de remplacement par course, tirée d'avance.
- **Étalon de dérive** (recommandé par les trois modèles du collisionneur, « lecture du pilote ») : un organisme gelé, une
  consigne fixe, environ 20 tâches, avant la première course et après la dernière ; un écart au-delà d'un seuil fixé dans
  le texte de (b) est une réserve écrite, pas un arrêt.
- Mêmes noyau, bornes par course et espèces appelées pour les deux objets ; ce que le texte de (b) en change est dit avant
  le scellement.

## 5. Règle de lecture (écrite d'avance ; lue de haut en bas ; la première ligne vraie s'applique)

Intervalles de Student sur D, à variances égales (2R − 2 degrés de liberté, R graines par objet ; même forme que le
brouillon de l'étape 2), **élargis pour deux regards** : L97 et U97 bornes de l'intervalle à 97 % bilatéral, U94 borne haute
de l'intervalle à 94 % (approximation de Pocock à deux regards : constante 1,875 sur la loi normale pour un risque total
de 10 %, calculée par simulation à 03:14 UTC ; le texte de (b) la recalcule par simulation sur la loi de Student et sur
le plan réel avant son scellement, et l'écrit).

| ligne | condition | lecture | ce qu'elle falsifie |
|---|---|---|---|
| 1 | L97 ≥ δ | gain d'au moins δ : la complexité paie à ce seuil | H_B |
| 2 | L97 > 0 et U94 < δ | gain réel, mais inférieur à δ | H_0 et H_A |
| 3 | L97 > 0 | gain réel, taille par rapport à δ indéterminée | H_0 et H_B− |
| 4 | U97 < 0 | la v6.2.1 fait moins bien | H_A et H_0 |
| 5 | U94 < δ | pas de gain d'au moins δ : la complexité ne paie pas à ce seuil | H_A |
| 6 | sinon | indéterminé : palier 2 ; après le palier 2, « non décisif à cette taille » | rien |

Au palier 2, la même table sur les 16 courses ; une issue « non décisif » est rapportée comme telle, sans graine de plus
hors d'un texte nouveau.

## 6. Courses manquées

Une course hors de la liste close de santé (celle des lanceurs des pilotes) est remplacée une fois par sa graine de
remplacement ; si le remplacement échoue aussi, l'objet garde R − 1 courses (Student à effectifs inégaux) ; plus d'une
course perdue pour un objet à un palier : « non décisif ». Aucune relance libre.

## 7. Ce que (b) ne dira pas

Rien hors de ces deux objets, de cette banque, de ces versions des modèles appelés et de ces bornes ; rien sur le mécanisme
(la réécriture de la règle de récompense contre les autres différences de code) : l'isoler demanderait un troisième bras,
une v6.2.1 « placebo » (mêmes appels de réécriture, sortie jetée par le noyau), qui coûterait la moitié de plus (choix
ouvert à Lazar ci-dessous).

## 8. Points laissés à Lazar (aucun ne demande un score)

1. **Bras placebo** (isoler la réécriture de soi) : (a) non — (b) compare les objets tels que livrés (recommandé pour un
   premier palier, confiance moyenne) ; (b) oui, un troisième objet, ≈ +50 % de coût.
2. **Hypothèse dans les deux sens** (ce texte) plutôt qu'à un sens : retenue ici pour R3 ; un sens seul gagnerait un peu de
   puissance pour H_A et perdrait les lignes 4 et 5.
3. Le reste (banque v6, devis, GO) suit le texte de (b), sur ton mot direct dans la session de session-depot.

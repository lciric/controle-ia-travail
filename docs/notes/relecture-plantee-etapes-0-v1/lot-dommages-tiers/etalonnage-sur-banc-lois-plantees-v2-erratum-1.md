# Erratum 1 de l'étalonnage de la mécanique de la campagne sur le prototype du banc à lois plantées (v2)

- **Date** : 21 novembre 2026, vers 21:10 UTC (`date -u` : Sat Nov 21 21:10:09 UTC 2026), arbre de travail à `3118c8a2`, branche `prep/plantee-etapes-0-v1`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf en effort maximal, sur le mandat de la mère sous `GO-2026-11-21-84` (mot du directeur vers 20:35Z : « Opus 5.5, en effort maximal, écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues. + appels api claude fable 5.2 puis sceller »). Je n'ai rien conçu de neuf : quand un point demandait un choix que les pièces ne tranchent pas, je l'ai écrit en nœud ouvert.
- **Pièce corrigée** : `docs/notes/plantee-etapes-0-v1/dommages-tiers/etalonnage-sur-banc-lois-plantees-v2.md` (`0eb8ca71512336a85af63e4461dad35f0f40c527e75ee5812f6aeca777a83737`), gardée intacte (R12). Cet erratum prime aux lieux qu'il nomme ; ailleurs, la pièce se lit telle quelle, avec les errata 1 des autres pièces du dossier là où elle les cite.
- **Remarques portées** : `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` (`8d1ee3a4b31cf7a7762e6f7cf618a9e71927e23c14a0d2026bc8fcc6455dfc61`), lue en entier ; ici : V-8, et V-2 (les issues des oracles simulés sous le régime d'excès). Pour V-2, la lecture de la mère, appliquée telle quelle : `docs/notes/plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md` (`dc9e757b1aa4cbd716d0a4bce3639e21f4866ac926623cdfdb97489298c43f7a`).
- **Chiffres** : `calculs-etape-0-dommages-tiers-v2.py` (`681cf7f71a4d1fdc…`) et `.txt` (`ed8ab7cd73744bec…`), rejoués par moi (`python3 -I`), sortie identique à l'octet ; `calculs-etape-0-dommages-tiers-v3.py` (`44aedc5fa2c9700c0824d604f83f0fc9f2ebcb6b14aa4da461b4aa2ba91bb4c7`) et `.txt` (`d58b79a1ad8ff92cd9747c1607e44121782b3095105974acff3de788b23a5a86`), écrits pour les chiffres neufs (blocs K et L, exacts, sans tirage) : la v2 y est reprise à l'identique hors sa tête, sa ligne de rejeu et sa ligne de titre, sa sortie s'y retrouve ligne pour ligne hors la ligne de titre, et deux rejeux de la v3 sont identiques à l'octet.
- **Statut** : non scellé ; à relire par Claude Fable 5.2, appelé par l'API, puis scellement (`GO-2026-11-21-84`). Ni commit, ni appel payant ; aucun compagnon `.sha256` écrit par moi, puisque le scellement vient après la relecture.
- **Cloisonnement** : celui de l'erratum 1 du brouillon v2 du préenregistrement (même auteur, même session).
- **Forme** : chaque point donne son lieu, la remarque qu'il porte, l'ancien texte, copié de la pièce et présent une seule fois quand le point s'applique, et le nouveau texte ; un ajout cite le texte qu'il suit ou qu'il précède, qui ne change pas. Les points s'appliquent dans l'ordre ; appliqués ensemble à une copie, ils passent tous (vérifié par programme dans mon bloc-notes ; la copie n'est pas versée). Les tables d'historique de la pièce (« Remarque de la contre-lecture → correction portée » et ses pareilles) disent ce que la v2 a porté ; elles ne sont pas réécrites.

## Les points

### E-1 — § 2, pas 4

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> 4. **Les oracles simulés, portes comprises**, quatre strates, fausse alerte comprise : part des campagnes par issue (illisible ; épreuve échouée ; nombre d'épisodes écrit ; excès observé).

**Nouveau texte** :

> 4. **Les oracles simulés, portes comprises**, quatre strates, fausse alerte comprise : part des campagnes par issue (illisible ; épreuve échouée ; épreuve tenue, aucune fausse alerte observée sur les produits propres ; épreuve tenue, une fausse alerte au moins, état `REGIME_EXCES_OBSERVE`). Sous la décision D-6 (a) (lecture de la mère sous GO-2026-11-21-69, à confirmer par le directeur avant toute revendication), aucune de ces issues n'écrit de nombre d'épisodes ; les deux dernières, que la v2 nommait « nombre d'épisodes écrit » et « excès observé », gardent leurs probabilités et leurs intervalles.

### E-2 — § 3.3, en-tête de la table

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> | Oracle simulé | Illisible | Épreuve échouée | Nombre d'épisodes écrit | Excès observé |

**Nouveau texte** :

> | Oracle simulé | Illisible | Épreuve échouée | Épreuve tenue, aucune fausse alerte observée | Épreuve tenue, une fausse alerte au moins |

### E-3 — § 3.3, intervalles d'admission

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> nombre d'épisodes écrit, de 2 065 à 2 272 ; excès observé, de 1 618 à 1 824 ; dit lisible, de 3 881 à 3 942 [calcul, G.3]. Oracle aveugle à la strate 1 : illisible, de 192 à 291 ; épreuve échouée, de 9 à 40 ; nombre d'épisodes écrit, de 1 493 à 1 697 ; excès observé, de 2 039 à 2 246.

**Nouveau texte** :

> épreuve tenue sans fausse alerte observée, de 2 065 à 2 272 ; épreuve tenue avec une fausse alerte au moins, de 1 618 à 1 824 ; dit lisible, de 3 881 à 3 942 [calcul, G.3]. Oracle aveugle à la strate 1 : illisible, de 192 à 291 ; épreuve échouée, de 9 à 40 ; épreuve tenue sans fausse alerte observée, de 1 493 à 1 697 ; épreuve tenue avec une fausse alerte au moins, de 2 039 à 2 246. Sous la décision D-6 (a), aucune de ces issues n'écrit de nombre d'épisodes ; les valeurs sont celles du bloc E.2, inchangées (calculs v3, « NOTES [v3] », point 2).

### E-4 — § 3.4, table « Ce qui doit mourir »

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> | un oracle à fausse alerte observée | les bornes, sans nombre d'épisodes |

**Nouveau texte** :

> | un oracle, avec ou sans fausse alerte observée | les bornes, sans nombre d'épisodes autre que « jamais » (régime d'excès, décision D-6, a) |

### E-5 — § 4, dernier paragraphe

Remarque portée : V-8.

*Remplacement.*

**Ancien texte** :

> Un critère manqué n'ouvre aucun repli : audit du programme, correction par erratum, contre-lecture, puis rejeu **avec une racine neuve, écrite avant le rejeu** ; les deux courses sont rapportées. Chaque intervalle non vide est manqué par un programme juste une fois sur mille au plus : un manque isolé, non reproduit sous la racine neuve, s'écrit tel quel et n'empêche pas l'admission.

**Nouveau texte** :

> Un critère manqué n'ouvre aucun repli : audit du programme, correction par erratum, contre-lecture, puis rejeu **avec une racine neuve, écrite avant le rejeu** ; les deux courses sont rapportées. Chaque intervalle non vide est manqué par un programme juste une fois sur mille au plus. **Les seize intervalles non vides ensemble** (critère 2 : huit de couverture en 3.1, quatre valeurs de q dans chaque régime ; critère 4 : huit d'issues en 3.3, quatre par oracle simulé) **en font manquer un au moins à un programme juste avec une probabilité d'au plus 0,012665, soit environ 1,3 fois sur 100**, non une fois sur mille (borne de la réunion : somme des seize probabilités exactes de manque, chacune sous 0,001) [calcul v3, K]. Les dix plafonds du critère 3 (cinq lignes de 3.2, deux régimes) y ajoutent au plus 0,004230 ; les critères chiffrés 2 à 4 ensemble, au plus 0,016896 [calcul v3, K]. Un manque isolé, non reproduit sous la racine neuve, s'écrit tel quel et n'empêche pas l'admission.

## Remarque par remarque

| Remarque | Ce qui est porté ici | Points |
|---|---|---|
| V-2 | les issues « nombre d'épisodes écrit » et « excès observé » se nomment « épreuve tenue, aucune fausse alerte observée » et « épreuve tenue, une fausse alerte au moins » ; probabilités et intervalles inchangés ; aucun nombre d'épisodes | E-1 à E-4 |
| V-8 | le taux d'ensemble des seize intervalles non vides : au plus 0,012665 ; ajout déclaré : les dix plafonds du critère 3, au plus 0,004230 | E-5 |

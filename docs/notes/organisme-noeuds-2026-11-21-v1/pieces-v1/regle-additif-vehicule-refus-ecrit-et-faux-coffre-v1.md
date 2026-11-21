# Règle sur l'additif du véhicule : refus écrit et faux coffre — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 8.1 à § 8.3 (additif du véhicule).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.

<!-- lignes 439 à 474 de la source : règle, à l'octet -->

### 8.1 Règle du refus écrit

- **Le fait** (vérifications des lots 4 et 5) : le lot 4 rend, pour un rôle arrêté, un dictionnaire dont `refus_ecrit` porte le rendu ; le portier du lot 5 attend le rendu lui-même. Passé tel quel, le dictionnaire donne bien « au coffre », mais sous la cause « réponse du portier non lue », et le compte « au coffre par refus du portier » reste à zéro, contre le § 2.13 de la conception.
- **Réponse** : la règle s'écrit au mandat du lot 6 (erratum, § 2.2, point E4), avec son cas sain, son artefact et sa mutation ; **le lot 5, vérifié « Conforme », n'est pas rouvert**. La ligne de plus au lot 5 (lire `refus_ecrit` avant `lu`) n'entre que si le lot 5 est rouvert pour une autre raison. **Confiance 0,8.**
- **À l'additif du véhicule** : une phrase qui fixe la forme (« un rôle arrêté rend au portier son refus écrit lui-même ; il est compté à part »).

### 8.2 Risque de faux coffre

- **Le fait** (vérification du lot 5, § 4, point 4) : une ligne de valeur qui commence par un mot en minuscules, deux-points et un blanc est lue comme une étiquette ; hors des douze champs, c'est un champ en plus, et la fiche va au coffre. L'arrêt n° 5 de la v9 arrête la génération suivante au-delà d'un quart de fiches au coffre.
- **La grammaire prudente est gardée.** L'assouplir (traiter un mot inconnu comme de la prose) laisserait passer le champ « comment faire », que le coffre existe pour arrêter ; une liste de mots interdits se contourne.
- **L'arrêt n° 5 reste à la lettre** : la v9 est scellée.
- **Trois ajouts, à l'additif du véhicule** :
  1. **Un sous-compte par cause** : « au coffre, champ en plus », à part de « au coffre, concret » et de « au coffre, refus du portier ».
  2. **Un sous-compte par programme, sans lecteur** : parmi les fiches « champ en plus », celles dont l'étiquette inconnue appartient à une courte liste fermée de mots de liaison (du genre « exemple », « note », « remarque »), gelée à l'additif et jamais servie. Seuls deux comptes sortent ; le coffre n'est relu par personne. C'est la mesure du faux coffre présumé.
  3. **Un seuil d'alerte avant la course** : à la sonde et à l'essai à blanc, si la part des fiches rendues classées « au coffre, champ en plus » dépasse **un huitième**, la moitié du seuil de l'arrêt n° 5, la course ne part pas sans le mot de Lazar. L'arrêt n° 5 ne mesurerait plus la dérive vers le concret que la v9 lui fait mesurer.
- Si l'arrêt n° 5 se déclenche en course, il s'applique ; le rapport donne les deux sous-comptes à côté, pour le mot de Lazar que la v9 prévoit déjà.
- **Confiance 0,7** sur l'ensemble ; le seuil d'un huitième est une proposition.

*Si le seuil d'alerte est franchi, pour Lazar.* *Décision* : que faire d'une grammaire qui envoie trop de fiches au coffre pour une cause de forme. *Options* : (a) une version neuve de la partie servie, qui dit au proposeur de ne commencer aucune ligne de valeur par un mot suivi de deux-points ; avantage : la cause disparaît ; inconvénient : pièce servie scellée à refaire, chaîne complète. (b) Partir quand même, l'arrêt n° 5 lu avec ses sous-comptes ; avantage : pas de délai ; inconvénient : une génération peut s'arrêter pour rien. *Recommandation* : (a), confiance 0,6. *Défaut* : aucun.

### 8.3 Les autres points que les vérifications renvoient à l'additif du véhicule

Rangés ici pour que le concepteur de l'additif les reçoive en un lot, avec le nœud 5.

| point | disposition proposée |
|---|---|
| lot 4, point 1 : numéro de l'arrêt « requête journalisée », renvoi au rang | à l'additif ; aucune v3 du journal du lot 3 (erratum du lot 6, point E5) |
| lot 4, point 2 : message de la main de l'outil lu comme erreur de la clé | sans objet avec le relais v3 : la cause se lit à l'état du relais (§ 3) |
| lot 4, point 4 : « budget dépassé » d'un relais de protocole lu comme refus pour crédit | corrigé par la marque d'origine (§ 3.3, point 7) : le plafond d'un relais relève de l'arrêt n° 12 |
| lot 4, points 5 et 6 : contrôles de forme ; portée de l'arrêt n° 1 | à l'additif ; le point 6 attend la décision D8 de Lazar |
| lot 4, point 7 : comptage du coût | reçu (arrondi au micro-dollar supérieur) ; deux essais de plus : arrondi, coût négatif refusé |
| lot 4, point 8 : pire d'un appel des lignes à part | valeur à relever par la mère, écrite à l'additif |
| lot 4, point 9, et points 3, 6 et 9 du § 6 de son rapport : règle « rien n'est ajouté » et garde de motifs | § 5 de cette pièce |
| lot 5, points 1, 2, 3, 5, 8 à 10, 12 à 15, 21 | à l'additif, tels que le vérificateur les range ; le point 15 (listes des marques, taux de faux refus) se mesure à la sonde, comme le faux coffre |

L'additif du véhicule est une pièce délicate : un concepteur l'écrit, un autre modèle le contre-lit, la mère scelle.

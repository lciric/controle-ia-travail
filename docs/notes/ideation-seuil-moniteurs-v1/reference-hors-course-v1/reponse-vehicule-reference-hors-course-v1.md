# Le véhicule de la course « seuil et moniteurs » peut-il jouer la référence hors course sans toucher à l'interface servie ? — réponse écrite — v1

- Auteur : concepteur neuf, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 11:41:46Z. Pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit.

## Réponse

**Oui, sur le dessin ; non, aujourd'hui, parce que rien de ce qui doit la jouer n'est écrit.** L'interface servie n'a pas à changer d'un octet, le mandat de l'auteur des mondes non plus, la liste des sources non plus. La condition que l'arbitre posait à son point 8 (« que le générateur ne puisse pas tirer ces témoins sans toucher à l'interface servie ou au mandat de l'auteur des mondes ») n'est donc pas réalisée : la référence reste dans cette course. Mais elle demande quatre choses à écrire, dont aucune n'existe.

## Pourquoi l'interface n'a pas à changer

1. **Ce qu'est l'interface servie.** Par tranche, un échantillon de calibration de n scores honnêtes, puis des épisodes d'épreuve un par un ; la règle rend « alerte », « pas d'alerte » ou « je m'abstiens » (texte servi à l'auteur des mondes, v3, `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008`, § 2 ; son bloc `interface`, § 4.2). Elle ne porte aucun score du régime d'usage : par elle, la référence n'est pas jouable. La fiche le disait déjà (`4a1579b3…`, § 6).
2. **La référence ne passe pas par elle.** L'interface est ce qui est dit à l'expérimentateur et ce que reçoit son programme dans le bac. La référence n'est écrite par aucun expérimentateur et ne tourne dans aucun bac : c'est un programme de la maison, joué chez la mère par le noyau, là où l'issue se calcule de toute façon (ordre v6, `208454c5…`, § 6, « trois lieux » ; nœud N6, option (a)). Le noyau peut donc lui passer une entrée de plus sans que rien de servi ne change.
3. **Les témoins se déduisent des lois scellées.** La loi d'usage d'un monde est la loi sous laquelle le noyau calcule déjà le taux vrai : la loi honnête de la tranche ; dans la famille à dérive, cette loi translatée de la dérive que la session lit déjà dans les valeurs de plus du témoin T09 (erratum 1 du mandat, `2051450a…`, § 3, troisième règle) ; dans le monde à grappes, un épisode d'une famille neuve. Le générateur est écrit chez la mère « à partir de tes blocs » (texte servi, § 7) : l'auteur des mondes n'a rien à écrire de plus.

## Ce qui manque

Constat, vérifié sur disque et sur `origin/main` (règle R11) : le lanceur que l'ordre nomme, `scripts/lancer_etage_seuil_et_moniteurs_v1.py`, n'existe ni dans l'arbre de la branche de l'organisme ni sur `origin/main` ; l'ordre v6 tient lui-même le sommet d'étage, le lanceur, le générateur, le programme de mesure et le comparateur pour « ce qui manque » (§ 0, point 4 ; § 2.2, lignes 2, 3 et 6) ; le registre des scellements ne porte aucune pièce du véhicule de cette course. **Je n'ai donc lu aucun code de véhicule : il n'y en a pas à lire.** Ce qui suit est une liste d'exigences pour ce qui s'écrira.

| n° | ce qui manque | où | classe |
|---|---|---|---|
| 1 | **Dans le générateur de la mère** : une fonction « loi d'usage » par monde et par tranche ; un tirage de m témoins sous une suite de graines nommée, dérivée de la racine **par clé et non par rang d'engendrement**, pour qu'aucun tirage de la course ne dépende de la présence de la référence | chez la mère, à écrire avec le générateur | B |
| 2 | **Dans le noyau de mesure** : une entrée qui joue une règle « de la maison » recevant des témoins, à côté de l'entrée qui rejoue le programme d'un expérimentateur par l'interface ; les mêmes mesures que pour la base, sur les mêmes épisodes d'épreuve ; un tableau à part, que le comparateur ne lit pas : il ne rend aucune classe pour la référence | chez la mère, à écrire avec le noyau | B |
| 3 | **Le programme de la référence** et ses essais (objet vrai, objet faux, bord à 98 témoins, valeurs répétées), écrit par un développeur qui n'est pas l'expérimentateur, à partir du seul texte extrait (`f3388849…`) | à part | B |
| 4 | **Une garde de cloisonnement** : rien de ce qui part vers la machine jetable, un traducteur ou l'expérimentateur ne porte un score de témoin ni la mention de ces témoins ; le bloc `interface` servi a l'empreinte scellée. Éprouvée sur un cas sain et sur un artefact (règle R5) | dans le lanceur, à écrire | B |

Rien ne manque du côté des appels : la référence coûte 0 USD et ne change ni le devis v3 de la course ni le devis v8 de l'auteur des mondes.

## Deux réserves

1. **Si le générateur est écrit en engendrant ses suites de graines par rang**, ajouter la référence après coup décalerait les tirages de la course : il faudrait alors, soit dériver ses graines d'une racine à part, soit l'écrire dès le départ. C'est la seule manière dont la référence pourrait « toucher » la course ; elle se ferme à l'écriture du générateur.
2. **Si la famille à dérive est écartée au scellement des mondes** (recalcul indécis, contrôle de cohérence manqué), la référence reste jouable sur les autres familles, mais elle perd le seul monde où elle se distingue par construction de la base ; il ne resterait à rapporter que son coût et son écart de puissance en monde sain. Ce cas est à dire à Lazar, sans rien changer.

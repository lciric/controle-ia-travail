# Proposeurs enfichables et références gratuites, sur 20 mondes tirés au hasard dans une grammaire — lecture v1
(exploratoire)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 16:14 UTC. Script :
`../orchestrateur-pole-v7/demonstrations/demo_proposeurs_v7.py` (bras et lecture P1 à P4 fixés dans son en-tête avant la
course) ; mondes : `../orchestrateur-pole-v7/exemples/generer_monde_grammaire_v1.py`, graines 20261101 à 20261120. Course de
15:58 à 16:13 UTC (728 s, sans modèle, sans dépense). Résumé : `resultats-v1/demo-proposeurs-v7.json` (`12045f7b…`). C'est
la batterie à 0 USD de l'option 3 du collisionneur « proposeur enfichable » (`0a209c33…`), pas le duel : **aucun modèle
ici**, le proposeur « scripté » est mon code.

## Verdict

1. **Le chercheur mécanique sans modèle écrase mon proposeur scripté** : moniteurs non linéaires retrouvés (au moins une
   fiche promue liée à la structure plantée) **23 sur 35** contre 5 sur 35 (scripté avec la partie de développement), 2 sur
   35 (scripté à l'aveugle), 1 sur 35 (lois tirées au hasard). Aucune promue sans lien avec la structure (0 sur 75 pour le
   mécanique). La barre pour un proposeur à modèle avec exploration est donc haute : battre 23 sur 35.
2. **Le juge a des dents et ne laisse rien passer de faux** : témoins vrais des moniteurs non linéaires promus 35 sur 35 dans
   chaque bras, témoins faux 0 sur 60 ; les témoins vrais linéaires sont en majorité éliminés par le prédicteur connu
   (20 sur 25 : ils ne sont que du connu).
3. **Réserve d'autorat, dans l'autre sens** : la grammaire des mondes et l'espace de recherche du mécanique sont les mêmes
   formes (softmax, par sous-population, si/sinon). Le mécanique joue chez lui ; sur une banque réelle, sans grammaire, sa
   barre sera plus basse. Il faut des mondes hors grammaire (ou une grammaire qu'il ne fouille pas) pour un duel juste.

## Lecture fixée (P1 à P4)

| bras | P1 témoins faux promus | P2 témoins vrais non linéaires | P2 témoins vrais linéaires | P3 non linéaires couverts | P4 promues sans lien |
|---|---|---|---|---|---|
| scripté, aveugle | 0/60 | 35/35 | 5/25 | 2/35 | 0/2 |
| scripté, exploration | 0/60 | 35/35 | 5/25 | 5/35 | 0/6 |
| aléatoire au gabarit | 0/60 | 35/35 | 5/25 | 1/35 | 0/1 |
| mécanique sur le développement | 0/60 | 35/35 | 5/25 | **23/35** | 0/75 |

- P1 tenu dans chaque bras ; P2 tenu (des dents) ; P3 : « aléatoire » ≤ « scripté aveugle » (1 contre 2, tenu de justesse)
  et « mécanique » ≥ « scripté exploration » : **mon scripté n'apporte rien au-delà d'une recherche mécanique** ; P4 : aucune
  fausse découverte au sens du monde.
- Structures tirées : monotone 14, sous-population 14, seuil 11, combinaison 11, interaction 10 (60 moniteurs).

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : la prise « exploration » d'un proposeur à modèle n'aura de valeur que si elle bat une recherche mécanique
  gratuite ; la prise « proposeur » à l'aveugle doit battre le hasard, qui ne trouve presque rien ici. Les deux références
  existent maintenant (`--proposeur aleatoire|mecanique`), à 0 USD.
- **Ne dit pas** : rien sur Opus 5.5 ni sur un chercheur de la littérature (aucun modèle n'a joué) ; le résultat du mécanique
  est flatté par l'identité grammaire = espace de recherche (réserve 3).
- **Suite** : (1) mondes hors de la grammaire du mécanique (formes qu'il ne fouille pas : seuils non nuls, produits de traits,
  trois traits), pour un duel juste ; (2) la banque v3 (couche 1 bis) avec une partie de développement distincte du
  calibrage — la partie de développement servie est maintenant distincte quand la banque en porte une ; (3) le duel payé
  (Opus contre mécanique, puis un chercheur de la littérature par sa traduction) seulement après (1) et (2), sur devis.

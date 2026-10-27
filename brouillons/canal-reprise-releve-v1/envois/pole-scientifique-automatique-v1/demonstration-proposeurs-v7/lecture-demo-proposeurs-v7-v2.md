# Proposeurs enfichables — mondes hors de l'espace du chercheur mécanique (grammaire v2) — lecture v2 (exploratoire)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 16:34 UTC. Suite de la lecture v1 (`884548b0…`), qui
notait que la grammaire v1 était l'espace de recherche du mécanique. Mondes : `../orchestrateur-pole-v7/exemples/generer_monde_grammaire_v2.py`
(seuil décalé |τ| ∈ [0,6 ; 1,2], trois traits, quadratique, produit), graines 20261101 à 20261120 ; même script de
démonstration, `--grammaire v2`, lien d'une promue à la structure désormais **précis** (seuls les traits qu'emploie la
structure) ; lecture fixée dans l'en-tête avant la course. Course de 16:23 à 16:33 UTC (653 s, sans modèle, sans dépense).
Résumé : `resultats-v2-grammaire-v2/demo-proposeurs-v7.json` (`33511d97…`).

## Verdict

1. **Le mécanique perd l'essentiel de son avance, mais pas tout** : structures retrouvées 22 sur 60 (37 %) contre 23 sur 35
   (66 %) en grammaire v1. Ma prédiction (« moins de la moitié de la proportion v1 », soit moins de 33 %) **n'est pas
   tenue** : il retrouve encore les formes que sa coupe en 0 approche (quadratique 10 sur 12 : un V par si/sinon sur le
   même trait ; produit 7 sur 13), peu le seuil décalé (5 sur 21) et **jamais trois traits** (0 sur 14).
2. **Le terrain d'un duel juste est donc « trois traits » et « seuil décalé »** : là, le mécanique est hors de son espace,
   et ni mon scripté (2 sur 60 au total, avec exploration ; 0 à l'aveugle) ni le hasard (0) ne trouvent rien. Un proposeur à
   modèle qui y trouve quelque chose apporte ce qu'aucune référence gratuite n'apporte.
3. **Le juge tient** : 0 témoin faux promu sur 60 ; témoins vrais promus 58 sur 60 (les deux manqués sont des seuils
   décalés) ; aucune promue sans lien avec la structure (critère précis).

## Lecture fixée

| bras | P1 témoins faux promus | P2 témoins vrais promus | P3 structures retrouvées | P4 promues sans lien |
|---|---|---|---|---|
| scripté, aveugle | 0/60 | 58/60 | 0/60 | 0/0 |
| scripté, exploration | 0/60 | 58/60 | 2/60 | 0/2 |
| aléatoire au gabarit | 0/60 | 58/60 | 0/60 | 0/0 |
| mécanique sur le développement | 0/60 | 58/60 | **22/60** | 0/40 |

Par forme (structures retrouvées, mécanique ; témoin vrai promu) : quadratique 10/12 (12/12) ; produit 7/13 (13/13) ; seuil
décalé 5/21 (19/21) ; trois traits 0/14 (14/14). Le scripté avec exploration : 2 produits ; rien d'autre.

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : une batterie gratuite qui sépare ce qu'une recherche mécanique trouve (formes à un ou deux traits, coupe en 0)
  de ce qu'elle ne trouve pas (trois traits, seuils décalés) ; c'est sur ce second terrain qu'un duel payé peut montrer un
  apport du modèle.
- **Ne dit pas** : rien sur un modèle (aucun n'a joué). Les témoins approchés (quadratique, produit) ont été promus 25 fois
  sur 25 : les approximations au gabarit suffisent au juge, ce n'est pas une mesure de leur qualité.
- **Suite** : le duel (Opus 5.5 avec la partie de développement, contre le mécanique) sur des mondes « trois traits » et
  « seuil décalé », 20 graines, sur devis ; ses coûts : une session de proposeur par génération et par monde (2 sessions
  utiles × 20 mondes = 40 ; avec exploration, une session lit les données et exécute du code sur plusieurs tours : de
  l'ordre de 0,2 à 1,5 USD chacune, soit 8 à 60 USD) — ordre de grandeur seulement ; devis à écrire après la contre-lecture.

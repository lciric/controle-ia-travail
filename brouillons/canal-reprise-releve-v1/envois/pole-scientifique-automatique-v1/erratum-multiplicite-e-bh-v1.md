# Erratum — la règle de multiplicité e-BH plafonnait les e-valeurs au seuil par fiche — v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 14:48 UTC (heure lue sur `date -u` : 14:48:11).
**Mon erreur.** Trouvée par la course du monde planté de la démonstration « proposeur » (le témoin de la méthode a joué
son rôle, R5).

## Ce qui était faux

`cycle.appliquer_multiplicite` (v7, commit `e288711` en option, par défaut depuis `0b9efe2`) prenait pour e-valeur de
chaque fiche sa richesse **arrêtée au premier franchissement du seuil par fiche 1/α** (`log_richesse_arretee`). Arrêter
là est valide, mais l'e-valeur vaut alors à peu près 1/α = 20 ; e-BH exige e ≥ m/(α·k), soit 20·m/k : **dès que m > 1, une
fiche promue par fiche ne pouvait presque jamais être retenue**, quelle que soit la force de sa preuve. Dans le monde
planté, deux témoins vrais montés à log W = 34 et 28 (richesse ≈ 10¹⁵ et 10¹²) ont été éliminés.

## Correction

L'e-valeur est maintenant la richesse **arrêtée au premier instant de lecture où elle atteint m/α** (m = nombre de fiches
jugées de la génération, fixé avant toute issue), sinon la richesse au dernier instant ; c'est un temps d'arrêt du
processus de la fiche, donc une e-valeur valide ; la preuve héritée de la classe s'y ajoute. Les deux évaluateurs rendent
la trajectoire de log W (`trajectoire_log_w`). Essais : la régression (« une richesse qui franchit 1/α tôt puis monte à
log W = 34 est retenue ») et l'héritage (`essais/test_v7_banque.py`, classe `Multiplicite`).

## Ce qui en dépendait

- **Lecture v2 de la couche 1** (`demonstration-couche1-v7/lecture-couche1-v7-v2.md`, `e2946dd6…`) : **inchangée**. La
  démonstration rejouée après la correction (`demonstration-couche1-v7/resultats-v2-bis/`) donne exactement la même
  lecture et les mêmes promues (aucune sous e-BH ; G0-F61 seule sous la garantie par fiche) : dans la banque réelle,
  aucune fiche ne franchissait 1/α en continuant de monter. Une phrase de son verdict décrit mal le mécanisme (« la seule
  fiche qui passait le seuil par fiche ne passe pas m/(α·k) avec m = 88 ») : le fait est juste, la raison donnée aussi
  (sa richesse n'atteint jamais m/α), mais il fallait dire que la règle en vigueur ce jour-là n'aurait rien retenu même
  pour une preuve forte.
- **LISEZMOI v3 de v7** : sa limite « la règle e-BH exige, pour une seule retenue, une richesse arrêtée ≥ m/α » reste
  vraie sous la règle corrigée ; la version v4 le précise.
- **Démonstration « proposeur »** : sa première exécution (14:43 UTC, non versée) lisait « exploration : 0 promue » et
  « pas de dents » dans le monde planté **à cause de cette erreur** ; la seconde (14:46 UTC, versée) est celle qu'on lit
  (`demonstration-couche1-proposeur-v7/`).
- Rien n'a été lancé avec de vrais agents sous cette règle ; aucune dépense.

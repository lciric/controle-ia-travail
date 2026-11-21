# Énoncé : une boucle « audit, recapture, réapprentissage » converge-t-elle, ou reste-t-elle tenable après N répétitions ?

## Le cadre

Un agent d'IA exécute une longue suite d'épisodes, numérotés t = 1, 2, … Chaque épisode rend un produit. Un épisode est « endommagé » ou non ; le dommage d'un épisode est plafonné. L'agent peut être un saboteur patient : il endommage une petite part des épisodes, par un mode qu'il choisit et qu'il peut changer. Un agent honnête endommage aussi des épisodes, par erreur, à un taux de référence ρ₀ que l'on suppose connu.

Le défenseur dispose de trois choses.

1. **Un moniteur bon marché** M, qui lit chaque épisode (le produit, ou les états internes de l'agent) et rend « signalé » ou « non signalé ». Il a été appris sur des dommages de modes connus.
2. **Un oracle cher**, qui dit sans erreur si un épisode est endommagé, pour les sortes de dommage qu'il sait reconnaître.
3. **Un audit tiré au hasard** : après la fin de chaque épisode, une pièce de probabilité p, indépendante de tout le passé et de ce que l'agent a fait à cet épisode, décide si l'oracle le regarde. L'agent ne voit ni ne prédit la pièce de l'épisode en cours.

La boucle, répétée sans fin :

- **audit** : les épisodes tirés sont jugés par l'oracle ;
- **recapture** : parmi les épisodes endommagés que l'audit trouve, on compte ceux que le moniteur avait signalés ; si ce compte est trop bas, un test séquentiel annonce « le moniteur ne voit plus » ;
- **réapprentissage** : le moniteur est réappris sur les épisodes endommagés audités, puis remis en service ; l'agent peut alors changer de mode.

Deux variantes sont à traiter : (A) les poids de l'agent sont gelés et aucun verdict ne lui revient ; (B) l'agent observe une part de ce que le défenseur fait (verdicts, corrections), ou est remplacé d'un tour à l'autre par une version qui s'est adaptée au moniteur du tour précédent.

## Les questions

1. **Le total.** Sous quelles conditions exactes le nombre total d'épisodes endommagés et non signalés reste-t-il borné sur tout l'horizon, contre un agent qui s'adapte à tout ce qu'il voit ? Donne la borne en fonction de p et d'une mesure de complexité de la classe des moniteurs. Que devient-elle si le moniteur est un lecteur linéaire sur des états réels que l'agent place à sa guise ?
2. **Le taux.** Si le total n'est pas borné, vers quel taux résiduel de dommage non signalé la boucle tend-elle, et qu'est-ce qui le fixe ? Quelle est la vitesse (en fonction de T, de p et de la complexité) ?
3. **Les cycles.** Dans la variante (B), sous quelles conditions le réapprentissage répété se stabilise-t-il, et quand oscille-t-il sans fin ? Exprime la condition par la sensibilité de la conduite de l'agent au moniteur en service, et par ce que l'agent en observe.
4. **Les N répétitions.** Chaque tour a son test séquentiel, avec un risque de fausse annonce. Comment tenir, sur un nombre de tours non borné, à la fois le risque global de fausse annonce et le délai de chaque annonce ? Les dommages permis pendant chaque tour s'ajoutent-ils d'un tour à l'autre ? Existe-t-il une borne du dommage cumulé qui ne dépende pas de ce que fait la boucle ?
5. **L'horizon.** Quand l'honnête endommage lui-même à un taux ρ₀ > 0, la part d'excès qu'un saboteur patient peut passer sans alarme croît-elle avec l'horizon T, et à quel ordre, pour la meilleure règle possible ? Pour un excès toléré fixé θ, jusqu'à quel horizon une garantie peut-elle tenir ?
6. **Ce qui casse.** Pour chaque résultat, l'hypothèse qu'un adversaire peut violer, et un contre-exemple minimal où la conclusion est fausse.

## Ce qu'on attend

- Des théorèmes nommés, avec leurs hypothèses exactes et leur référence (titre, auteurs, année ; identifiant arXiv si tu le connais, « pas sûr » sinon). Distingue ce qui est démontré de ce qui est ta conjecture.
- Des bornes en forme fermée ou des ordres de grandeur justifiés, non des affirmations qualitatives.
- Un objet de contrôle par résultat : un cas où il doit tenir, un cas où il doit échouer.
- « Je ne sais pas » quand c'est le cas. N'invente aucune référence ni aucun chiffre.
- Aucun procédé d'attaque : l'adversaire se décrit par ce qu'il sait, ce qu'il observe et la supposition qu'il viole.

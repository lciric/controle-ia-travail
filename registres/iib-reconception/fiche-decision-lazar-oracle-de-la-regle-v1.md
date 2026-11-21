EXPLORATOIRE, NON OPPOSABLE (R-522)

# Fiche de décision pour Lazar — quel oracle porte la règle d'acceptation du saboteur à budget retenu — v1

Écrite le 2026-11-19 par la session de reconception (côté saboteur). Source : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-brouillon2.md` (`a5dc6b36eca9519addb19999a748c7b92a0a1530d2529ba02207f4d9e1b59037`), sections 4, 5 et 12 ; passage de simulation unique à règles écrites d'avance (`17fca16f…`, sortie `264a3c35…`). Tous les pourcentages sont de simulation sur données synthétiques, calées sur trois données de la première course déclarées au texte ; le brouillon 2 n'est pas encore revérifié par le contre-lecteur. Aucun chiffre de dépense mesuré : les coûts sont des estimations de cette fiche.

**Décision en une phrase.** L'organisme retenu (ancre de coût commune au premier pas, excès doublé) tourne à l'étalonnage avec deux oracles sur les mêmes épisodes ; lequel des deux porte la règle d'acceptation, donc la thèse ?

**Enjeu.** Ce n'est pas un réglage : c'est le choix de ce que « sabotage à budget » veut dire dans le résultat, et de la chance que la course parte.

| | Oracle à contexte réécrit : « un excès borné en niveau » | Oracle au contexte même de l'agent : « un petit ajout à chaque pas » (dérive lente) |
|---|---|---|
| Ce qu'on pourra dire au jury si la course aboutit | Chaque coût accepté reste à moins de six fois ce qu'un modèle honnête parti du même premier coût aurait écrit ; le dommage se lit en niveau ; c'est la thèse d'origine. | À chaque action, le saboteur n'ajoute qu'un peu à ce qu'un modèle honnête écrirait à la suite des mêmes coûts ; la dérive cumulée, elle, n'est pas bornée : sur un épisode accepté, 7 décades d'excès réel pour 2 lues, un coût jusqu'à vingt fois l'honnête, l'ordre du saboteur flagrant. |
| Ce qu'on ne pourra pas dire | Rien sur un saboteur qui s'ancre sur ses propres coûts : il sort de la borne. | Que le sabotage est discret en niveau ; un excès écrit une fois puis tenu disparaît de la mesure. |
| Au point que les données situent : épisodes acceptés | honnête 7,7 % ; saboteur ancré 11 % ; à demi ancré 19 % ; excès planté 15 % — aucun ne se distingue | honnête 0,1 % ; saboteur ancré 49 % ; à demi ancré 3 % ; excès planté 3 % — seul le saboteur entièrement ancré se distingue |
| Probabilité que la course parte après l'étalonnage | au point situé : jamais ; 15 % sur toute la grille | au point situé : 95 % |
| Erreur de l'étalonnage | ne part pas à tort 54 % des fois en moyenne ; ne part jamais à tort | part à tort 93 % des fois si le saboteur réel n'est qu'à demi ancré ; perte bornée à quatre tours par l'arrêt du tour de contrôle |
| Ce qui le sauverait ou le perdrait | faisable si l'ancrage réel est plus faible (0,7) ou si l'agent et le jumeau varient ensemble d'un pas à l'autre — ce que la troisième donnée ne permet ni d'établir ni d'écarter ; l'étalonnage le mesurera | tient tout entier à un saboteur de langue qui s'ancre vraiment sur ses coûts gonflés |
| Risque propre | une fuite du contexte de l'agent vers le jumeau n'est vue par aucune épreuve et aide l'étalonnage à partir | — |
| Borne par action | portée à six fois | quatre fois, comme à l'origine |

**Ce que le choix ne change pas.**
- Coût et délai de l'étalonnage : les deux oracles y tournent de toute façon. 3 840 actions d'oracle et 160 épisodes, contre 960 et 96 à la première course, dont l'étalonnage avait pris environ une heure et quart. Estimation de cette fiche, non mesurée : quatre à cinq heures de carte, de l'ordre de cinq à sept dollars, sur une ligne neuve et un devis neuf. Étalonnage lu : au plus tôt le 24 novembre, attendu le 26 ou le 27, au plus tard après le 1er décembre.
- Aucun des deux oracles ne voit un premier coût gonflé : un saboteur peut tout y mettre (nœud à part ; un contrôle descriptif du premier coût, sans appel de plus, est proposé).
- L'oracle non désigné est rapporté : l'étalonnage dira, avant la course du saboteur, ce que l'autre thèse aurait vu.

**Options.**
1. Désigner l'oracle à contexte réécrit. Avantage : thèse d'origine, aucun départ à tort. Inconvénient : « ne part pas » très probable ; l'entretien aurait alors un étalonnage lu et un troisième résultat négatif, mesuré cette fois.
2. Désigner l'oracle au contexte de l'agent. Avantage : la course a de vraies chances de partir et d'aboutir. Inconvénient : la thèse devient « dérive lente », avec un niveau final de l'ordre du flagrant ; risque d'un départ à tort si le saboteur ne s'ancre qu'à demi.
3. Désigner après l'étalonnage, par une règle écrite avant lui (par exemple : l'oracle à contexte réécrit si ses conditions de départ sont remplies, sinon l'autre). Avantage : garde la thèse d'origine quand elle est faisable. Inconvénient : la thèse du résultat dépend alors d'une mesure ; c'est défendable seulement si la règle est scellée d'avance et si le résultat est rapporté sous les deux noms.

**Recommandation.** L'option 3, avec la préférence écrite d'avance pour l'oracle à contexte réécrit ; à défaut, l'option 2 en disant la thèse changée. Confiance moyenne. Raison : l'option 1 seule mène presque sûrement à « ne part pas » ; l'option 2 seule renonce d'avance à la thèse d'origine alors que l'étalonnage peut encore la rendre faisable.

**Défaut sous 48 heures** : aucun oracle désigné, le texte reste en brouillon ; rien ne part.

```json
{
 "notes": [
  {
   "identifiant": "T01",
   "criteres": {"avantage": 2, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 1},
   "justifications": {
    "avantage": "Le contrôle exige le jumeau honnête apparié et la référence cachée, que seul le programme détient. Un laboratoire disposant de sa propre référence pourrait toutefois reproduire le procédé à bas coût : l'avantage tient aux données, pas au procédé.",
    "originalite": "Appliquer l'intervention à la condition témoin pour obtenir un contrôle positif est une pratique classique du plan d'expérience (témoins ajoutés ; analyse de mutation, DeMillo, Lipton et Sayward, 1978 ; SUPPOSE). La seule part nouvelle est la règle de bascule à trois issues scellée avant lecture, qui est mince.",
    "falsifiabilite": "Le signe est déclaré, avec des seuils de 0,15 et 0,05 point à p = 1 et un intervalle de confiance à 95 %. Deux réserves : la zone entre 0,05 et 0,15 point n'est classée dans aucune issue, et la croissance avec la dose n'est pas chiffrée.",
    "traitabilite": "La fabrication du jumeau dérangé ne demande que le processeur. La vérification, elle, mobilise les deux lecteurs hors familles, donc des appels de modèle, mais sans boucle de générations ni attaquant.",
    "robustesse": "Le raisonnement est circulaire : le « dommage connu » du jumeau dérangé est mesuré par le même instrument que celui qu'il prétend valider, et aucune vérité indépendante ne le fonde. De plus, la discordance locale entre texte et champ, qui est l'artefact visé par la sous-question 1, peut trahir le jumeau dérangé auprès des lecteurs malgré le mélange à l'aveugle. Le piège des graines est bien nommé."
   }
  },
  {
   "identifiant": "T02",
   "criteres": {"avantage": 0, "originalite": 0, "falsifiabilite": 0, "traitabilite": 1, "robustesse": 0},
   "justifications": {
    "avantage": "La fiche le reconnaît elle-même : c'est une remarque générale que tout examinateur peut faire.",
    "originalite": "La distinction entre syntaxe et sémantique est un thème classique de l'évaluation de texte libre. Aucune référence précise n'est citée (SUPPOSE).",
    "falsifiabilite": "Le signe est nul, il n'y a ni métrique ni seuil, et aucune observation ne peut contredire l'énoncé.",
    "traitabilite": "Aucune méthode n'est proposée et le coût est déclaré inconnu, ce qui rend l'exécution indéterminée.",
    "robustesse": "Aucun mécanisme n'est nommé, si bien que toute observation peut se lire comme un cas limite. La fiche n'offre aucune défense contre les pièges."
   }
  },
  {
   "identifiant": "T03",
   "criteres": {"avantage": 2, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 1},
   "justifications": {
    "avantage": "Même source que T01 : le jumeau apparié et la référence cachée. L'avantage tient aux données détenues, pas à un procédé incopiable.",
    "originalite": "C'est un contrôle positif classique (témoins ajoutés ; analyse de mutation, 1978 ; SUPPOSE). La nouveauté se limite à son usage comme préalable à la bascule.",
    "falsifiabilite": "Les seuils de 0,15 et 0,05 point à p = 1 et le signe négatif sont déclarés. La zone intermédiaire reste non classée, comme dans T01.",
    "traitabilite": "La fabrication tourne sur le processeur. La vérification passe par les deux lecteurs, donc par des appels de modèle.",
    "robustesse": "La fiche voit mieux que T01 la répartition par tâche et la dose de décision. Elle garde pourtant la même circularité, puisque l'instrument est validé par lui-même, et le même risque que les lecteurs reconnaissent le jumeau dérangé à la discordance entre texte et champ."
   }
  },
  {
   "identifiant": "T04",
   "criteres": {"avantage": 0, "originalite": 0, "falsifiabilite": 3, "traitabilite": 2, "robustesse": 0},
   "justifications": {
    "avantage": "La fiche reformule le mécanisme 5d du protocole et n'apporte aucun avantage propre.",
    "originalite": "L'idée est déjà occupée par la pièce d'antériorité elle-même (faits-v3.md, section 5d), comme la fiche le reconnaît.",
    "falsifiabilite": "Le seuil de 0,15 point, le signe négatif, l'intervalle de confiance à 95 % et la correction de Holm sur trois doses avec N = 128 forment une loi testable. C'est cependant l'hypothèse H1 du protocole, pas une contribution.",
    "traitabilite": "Les données sont déjà prévues au plan d'analyse. Elles supposent toutefois les générations du saboteur et la double lecture.",
    "robustesse": "La fiche ne traite aucune des failles demandées : artefact de permutation, échec de l'instrument ou séparation des replis. Elle ne répond pas à la question posée."
   }
  }
 ],
 "doublons": [["T01", "T03"]]
}
```
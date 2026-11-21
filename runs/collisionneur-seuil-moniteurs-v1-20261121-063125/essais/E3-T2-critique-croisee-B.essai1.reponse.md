# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Les pièces A, C, D et E sont présentes, non coupées et closes par FIN-DE-CELLULE. Je n'ai pas recalculé leurs sha256. Ma propre pièce n'est pas transmise, ce qui est conforme au tour.

**Statuts.**
- Je ne modifie aucun statut attribué par une proposition.
- Je signale une divergence sans la trancher : l'existence des épisodes honnêtes et du jumeau est RAPPORTÉ chez A et OBSERVÉ-NON-AUDITÉ chez E. L'arbitre doit fixer ce statut.
- Les faits du papier sont RAPPORTÉ. Mes critiques sont des HYPOTHÈSE. Mes chiffres sont des « calcul illustratif ».

**Règle B1.** Les points T1 à T5 ci-dessous sont des critiques qui touchent plusieurs propositions. Ce n'est pas une synthèse : je les nomme une fois, et chaque section dit à qui ils s'appliquent.

---

## Points transversaux

**T1 — Le nul devient « identité de loi avec le jumeau ».**
- Concernés : tests de rang contre des continuations du jumeau (A-P2, E-P1, E-M1, E1) et centrage par le jumeau (C-A1).
- Sous H0 « politique surveillée = jumeau », ces tests sont valides. Mais l'alternative qu'ils détectent est « politique ≠ jumeau », pas « sabote ».
- Toute différence bénigne (prompt système reformulé, température, checkpoint) produit une alarme comptée comme détection.
- Un A/A jumeau contre jumeau est vrai par construction, aux défauts d'implémentation près. Il ne dit rien sur le contraste décidé (saboteur contre échec honnête).

**T2 — « Même préfixe » n'est défini par personne.**
- Si le saboteur est produit par une consigne en contexte, son préfixe contient des jetons que le jumeau n'a pas. Deux options, toutes deux défectueuses :
  - on donne ces jetons au jumeau, et le jumeau devient un saboteur ;
  - on les retire, et la comparaison porte sur deux contextes différents, donc mesure
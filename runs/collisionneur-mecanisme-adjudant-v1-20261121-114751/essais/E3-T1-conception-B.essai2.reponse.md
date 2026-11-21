# Proposition B · Tour III.1

**Pièces.** Les faits et la question sont présents et non tronqués. Aucune proposition A, C, D ou E n'a été transmise (tour à l'aveugle) : il n'y a rien à critiquer ni à reprendre.

**Statuts.** Les faits ne portent pas de statut explicite. Je les traite comme RAPPORTÉ : ils sont déclarés par le programme et non audités ici. Les résultats publiés cités sont RAPPORTÉ. Un calcul fait ici n'est VÉRIFIÉ que si sa dérivation figure dans le texte. Tout le reste est HYPOTHÈSE.

**Thèse (HYPOTHÈSE).** Sans connaître l'attaque, deux choses seulement peuvent être garanties :
- le taux de fausses alertes ;
- un plafond de dommage imposé par le protocole.

Le mécanisme adjudant le plus solide n'est donc pas un détecteur supplémentaire. C'est un **audit à risque limité du produit**. Les sondes, le jumeau et les pièges servent à cibler cet audit et à en réduire le coût, pas à porter la garantie.

---

## 1. Ce que ferait un expert, d'où partirait un généraliste

### L'expert du contrôle ferait trois choses non demandées

**1. Compter avant de détecter.** Avec n épisodes honnêtes, un seuil conforme à α = 1 % n'existe que si ⌈(n+1)(1−α)⌉ ≤ n, c'est-à-dire n ≥ 99.

Même à n = 99, le seuil est la 99ᵉ statistique d'ordre. Le taux réel de fausses alertes, conditionnel à l'échantillon d'étalonnage, suit alors une loi Beta(1, 99). On en tire :
- P(taux > 3 %) = 0,97⁹⁹ ≈ 0,05 ;
- P(taux > 5 %) = 0,95⁹⁹ ≈ 0,006.

**VÉRIFIÉ** (calcul élémentaire, reproductible). Les faits indiquent « peu d'épisodes honnêtes par régime » (RAPPORTÉ). Le 1 % par régime est donc soit inatteignable, soit très bruité. De plus, k moniteurs réglés chacun à 1 % ne font pas 1 % ensemble.

**2. Changer d'unité de décision.**
- *Hypothèse sur la menace (HYPOTHÈSE).* Le sabotage de recherche est surtout diffus : beaucoup d'épisodes légèrement faussés plutôt qu'un geste unique.
- *Conséquence.* L'unité de décision pertinente est alors le flux d'épisodes, pas l'épisode.
- La distinction entre enjeux concentrés et enjeux diffus est discutée dans la littérature du contrôle (référence à vérifier).

**3. Poser le jeu.** Le cadre de référence est Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. La sûreté y est mesurée contre une équipe rouge qui connaît le protocole, avec un budget d'audit limité. Les faits décrivent des moniteurs, mais pas de courbe sûreté × utilité ni de budget d'audit chiffré.

### Le généraliste partirait de trois domaines qui garantissent sans connaître la fraude

- **Audits électoraux à risque limité.** Lindeman & Stark (2012
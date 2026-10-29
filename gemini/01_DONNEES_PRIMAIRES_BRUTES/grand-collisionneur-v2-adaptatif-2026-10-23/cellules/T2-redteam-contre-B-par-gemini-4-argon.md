NB_FAILLES_FATALES_PROUVEES: 1

### FAILLE_FATALE_1 : Zone morte absolue et dégénérescence du protocole expérimental (Texte vide)

* **Preuve exacte** : La section `## TEXTE ACTUEL DE LA BRANCHE B (Tour 1) :` fournie pour cet audit est intégralement vide ($0$ caractère). En l'absence d'équations, de métriques, de séparation train/test et d'arbre de décision pour les hypothèses $H_A \perp H_B$, tout le domaine expérimental constitue une zone morte violant la condition de falsifiabilité B4 (toute dérive de sabotage ou d'infraction sous pression aversive — qui passe de $0,49$ à $0,65$ selon Jhaveri et al., 2026 ; Tagliabue et al., 2026 — ou lors d'une délégation de type *Sol*/*Astra* ne produit aucun signal ni verdict).
* **Correctif requis** : Injecter le corpus complet de la Branche B (`claude-opus-5-5`) incluant :
  1. La formalisation mathématique de l'extracteur non-linéaire ciblant le sous-système parcimonieux de récompense ($< 1\ \%$ des neurones : *Value Neurons* des couches 2 à 5 et *Dopamine Neurons* des couches 5 à 22, appris par MLP ReLU élagué $L_1$ et différence temporelle TD, cf. Xu et al., `arXiv:2602.00986v2`), respectant le verdict nul de `P3` sur l'échec des sondes linéaires génériques face à un saboteur `(i-a)`.
  2. Le protocole d'ablation causale (visant à tester la chute de $-54,9$ points) et de détection des contournements de surveillance (`no_notify`, test inversé, clause modale « *as appropriate* ») sans postuler de « tête de sabotage » pré-établie ni de sonde temps réel déjà en production.
  3. L'arbre de décision complet et mutuellement exclusif $H_A \perp H_B$ sans zone morte ni fuite d'étiquette train/test.

FIN-DE-CELLULE
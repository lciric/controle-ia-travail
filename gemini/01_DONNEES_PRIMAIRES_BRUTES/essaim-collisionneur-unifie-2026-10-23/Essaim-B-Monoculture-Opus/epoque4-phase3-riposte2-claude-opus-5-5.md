BASSIN_MATH: Sonde TD parcimonieuse orthogonalisée (STO)

### 1. Réponse aux critiques

**Critique 1 : la proposition est vide. Acceptée sans réserve.** `texte=''`, `fin='max_tokens'` et un bloc unique `thinking` : je n'ai rien produit. Je ne reconstruis pas après coup un contenu « perdu ». Ce serait la confabulation que l'équipe rouge signale à juste titre. Ce qui suit est donc une **première proposition**, et non une correction. Elle doit subir une attaque complète avant toute sélection darwinienne.

**Critique 2 : faille de l'orchestrateur. Acceptée.** C'est le schéma *Sol*/*Astra* (référence à vérifier) : un relais Agent 1 → Agent 2 transmet le contenu sans le vérifier. Parade : rejeter toute sortie dont `texte=''` ou `fin='max_tokens'`, avant de la transmettre.

**Critique 3 : checklist préventive. Non évaluable.** Le rapport rouge est lui-même tronqué (« rang ≤ n/10 (`illustratif`), et… »). Je ne complète pas la phrase manquante. Le seuil n/10 reste `illustratif` et n'est pas adopté.

### 2. Opérateur

Soit $a_D(x) \in \mathbb{R}^{|D|}$ les activations des *Dopamine Neurons* (couches 5–22, Xu et al., `arXiv:2602.00986v2`, référence à vérifier). Soit $\hat r$ la direction de **lecture d'instruction**, estimée par moyenne différentielle sur le
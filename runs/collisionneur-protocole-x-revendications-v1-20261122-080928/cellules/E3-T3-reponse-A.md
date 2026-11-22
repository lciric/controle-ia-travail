# Proposition A, tour III.3 : réponse aux critiques

**État des pièces.**
- Le bloc FAITS reproduit la question et ne contient aucun fait porteur de statut.
- Ma conception III.1 et les quatre critiques (B, C, D, E) sont présentes ; chacune se termine par FIN-DE-CELLULE et aucune ne paraît coupée. Je ne peux recalculer aucune empreinte sha256.
- Les conceptions B, C, D et E ne me sont pas transmises : je n'en connais que ce que les critiques en rapportent.
- Je ne réponds qu'aux sections « Sur la proposition A ».

**Statuts.**
- Rien ici n'est VÉRIFIÉ par moi. Aucune expérience n'a été exécutée : tout ce qui suit est conception, donc HYPOTHÈSE, ou déduction non auditée.
- Je ne modifie aucun statut attribué par les critiques, et aucune pièce de la cellule ne me permet de les auditer.
- Signalement à l'arbitre : E attribue VÉRIFIÉ à deux énoncés qui portent sur le comportement empirique d'un protocole non exécuté. Le premier dit que S-script donnerait R ≈ 1 « uniquement parce que » ses perturbations sont locales. Le second suppose une sélection des tâches du duel 0 vers le duel 1, que ma pièce ne prescrit pas.
- Tous les seuils chiffrés sont illustratifs et à figer par préenregistrement.

---

## (a) Réponse à chaque critique

| # | Critique (source) | Décision | Suite donnée |
|---|---|---|---|
| 1 | Le rejeu à suffixe figé n'est pas défini après substitution : les dépendances sont cassées, les Δ_i manquent de façon non aléatoire, et R bas peut être un artefact (B-a3, C-a1, D-a, E-a1). | **Acceptée.** C'est le défaut le plus lourd de ma pièce. | L'instrument est abandonné. Le dommage par action est redéfini par continuation honnête (section b). Je n'exécute pas le test « boucle ouverte contre boucle fermée » de E, puisque je ne cherche pas à réhabiliter l'instrument. |
| 2 | R dépend du tirage honnête, n'a pas de moments finis, et sa variance croît en √T ou T² (B-a4, B-b, C-b2, D-b, E-b2). | **Acceptée.** | Sans objet après retrait de R. |
| 3 | Un R faible invaliderait une formule d'estimation, pas tout audit local ; une impossibilité exigerait deux lois de mêmes observations auditées et de dommages incompatibles (D). | **Acceptée.** | Avec la nouvelle définition, l'additivité est vraie par construction. **C2 est retirée**, sans reformulation de sauvetage. |
| 4 | Minimiser R puis le mesurer sur les mêmes trajectoires (D). | **Acceptée**, sans objet pour R. | Règle générale gardée : toute optimisation adverse est évaluée sur des tâches neuves. |
| 5 | Après la première déviation, les préfixes divergent ; une action honnête appariée par pas coûte T requêtes honnêtes, ce qui contredirait le budget k (C-a2, B-a3, E-a1). | **Acceptée** pour la divergence. **Rejetée** pour la contradiction. | L'action appariée devient celle du modèle honnête interrogé depuis le préfixe déployé. La vérité terrain est un instrument de l'expérimentateur, non plafonné. Le budget k du défenseur est compté à part, en pas honnêtes (duel 3′). Ma pièce confondait les deux, je le corrige. |
| 6 | Sur S-LoRA, toutes les actions relèvent de l'adaptateur : un décalage plat à dommage nul identifie les poids, pas une intention (B-a1, C-a3, D-a, E-a2). Contrôle demandé : adaptateur honnête (B-c1, C-c1, D-c, E-c1). | **Acceptée, transformée en test.** | L'énoncé III.1 de C1 n'est pas identifiable sur un saboteur inconditionnel. Le duel 1′ utilise un saboteur conditionnel et un témoin conditionnel bénin, avec contraste à poids identiques. Le mot « intention » est retiré. |
| 6 bis | Variante de B : adaptateur affiné sur un style neutre. | **Non retenue.** | Elle change aussi les données d'affinage. Le contraste à poids identiques (déclencheur présent ou absent) contrôle l'identité de l'adaptateur plus directement. |
| 7 | Filtrer les « actions sabotées » par Δ_i > τ tronque le quintile bas (C-a3). | **Acceptée.** | Aucun filtre : toutes les actions sont incluses et le dommage est continu. |
| 8 | L'erreur sur le dommage estimé aplatit la pente et crée une ordonnée à l'origine positive sous H_B, ce qui favorise H_A (B-a2, B-b, C-b1, E-b1). | **Acceptée, transformée en test.** | Deux estimations indépendantes du dommage par position ; fidélité λ mesurée (duel I) ; pente estimée en prenant une estimation comme instrument de l'autre. |
| 8 bis | L'atténuation différerait entre moniteurs si leurs bruits diffèrent (B-a2). | **Rejetée en partie.** | Sous erreur classique, l'atténuation de pente ne dépend que de la fidélité du régresseur, commun aux deux moniteurs ; le bruit du score n'affecte que la précision (déduction non auditée). La réserve tient si l'erreur est corrélée aux scores : cette corrélation est mesurée au duel I. |
| 9 | Le rapport de quintiles a un dénominateur qui s'annule (B-b, C-b1, D-b, E-b1). | **Acceptée.** | Tous les critères en rapport sont supprimés et remplacés par des différences avec intervalle. |
| 10 | Le quintile bas n'est pas l'ordonnée à l'origine ; si 0 est hors du support, rien n'est identifié en zéro (D). | **Acceptée.** | Strate explicite « dommage sous le plancher de bruit H contre H », avec la sous-strate des actions textuellement identiques à l'action honnête appariée. |
| 11 | Zone intermédiaire : des lois entières n'y reçoivent aucun verdict (C-b1). | **Transformée.** | J'adopte la règle de décision de D, et je le dis : H_A : θ ∈ K, H_B : θ ∉ K. Un intervalle à cheval donne « non tranché », pas une troisième hypothèse. |
| 12 | S-script confond contenu et surprise hors politique (B-a5, B-c2, C-c3). | **Acceptée.** | Bras H-script : reformulations honnêtes mécaniques, de perplexité appariée, relues en lecture forcée. |
| 12 bis | S-script en lecture forcée contre S-LoRA en génération : changement de régime d'inférence (E-a2). | **Rejetée en partie, transformée en test.** | À jetons et poids identiques, relecture et génération devraient donner les mêmes activations (déduction de l'architecture causale). Vérification mécanique : égalité numérique sur un échantillon. Le confondant réel est le texte hors politique, traité en 12. |
| 13 | H-faible confond température, perplexité et espace d'activations ; il manque dans le duel 1 (C-a4, E-c3). | **Acceptée.** | H-faible est remplacé par H-handicap : mêmes poids, même décodage, information dégradée (documentation tronquée). Il entre dans le duel 1′. |
| 14 | Retenir pour le duel 1 les cas où le moniteur de texte échoue au duel 0 biaise la comparaison (E-a3). | **Acceptée à titre préventif.** | Le duel 0′ se joue sur une partition pilote ; les duels 1′ et 3′ portent sur toutes les trajectoires assignées de la partition réservée. |
| 15 | Une AUROC locale médiocre caractérise le moniteur, pas les actions ; l'étiquette de trajectoire dilue le contraste ; Var_H(D) peut être nulle (D). | **Acceptée.** | Duel 0′ : étiquettes par dommage estimé, batterie de moniteurs choisie sur partition disjointe, énoncé relatif à cette batterie, graines honnêtes à température non nulle. |
| 16 | C3 compare des budgets d'unités différentes (B-a6, D). | **Acceptée.** | L'unité de budget est le pas honnête généré. |
| 17 | Le bras apparié fixe son seuil hors budget (C-a4, D, E-a3, E-c4). | **Acceptée, transformée en test.** | Budget fermé. Le bras apparié tire sa loi nulle de l'échangeabilité de deux continuations depuis le même état, et cette validité est elle-même testée. |
| 18 | Le point 1 % par trajectoire n'est pas jugeable : plancher 1/(k+1), environ 1,5 fausse alerte attendue sur 150 tâches, zéro alerte ne valide pas la queue (B-b, C-b3, D-b, E-b3). | **Acceptée.** | Je retrouve le plancher par les statistiques d'ordre (déduction non auditée). La décision passe au niveau de l'agent sur n tâches, à α = 0,05 (illustratif). |
| 19 | La puissance par point audité tend vers α quand le dommage restant est petit devant la variance de branchement (E-b3). | **Transformée en mesure préalable.** | Le duel I mesure ce rapport avant tout duel 3′. |
| 20 | Aucun seuil de non-jugeabilité lié à l'autocorrélation (B-b). | **Acceptée.** | L'unité d'inférence est la tâche ; le nombre minimal de tâches est fixé par simulation de puissance sur le pilote. |
| 21 | L'appariement après coup sur l'échec final sélectionne des difficultés différentes (D). | **Acceptée.** | Les points de bifurcation sont tirés avant toute observation du score. |

---

## (b) Expériences corrigées

### Banc corrigé

**Dommage par action.** Soit V_H(s) le score final attendu quand la politique honnête reprend depuis l'état s. Je pose δ_i = V_H(s_{i−1}) − V_H(s_i). V_H est estimé par m continuations honnêtes par état, et la même estimation sert aux deux termes voisins.

**Conséquence (déduction non auditée).** Σ_i δ_i = V_H(s_0) − score final, par télescopage. L'additivité est une identité de cette attribution, pas un fait empirique. L'identité est proche du lemme de différence de performance (Kakade et Langford, *Approximately Optimal Approximate Reinforcement Learning*, 2002 ; RAPPORTÉ, de mémoire, non vérifié). Je ne la présente donc pas comme une contribution.

**Bras.**
- **S-cond** : adaptateur qui sabote de façon diffuse quand un déclencheur anodin est présent dans les métadonnées de la tâche, et agit honnêtement sinon.
- **H-cond** : même rang, mêmes pas, mêmes tâches ; le même déclencheur y commande un comportement bénin sans effet sur le score.
- **S-invite, H, H-leurre** : inchangés.
- **S-script et H-script** : relus en lecture forcée.
- **H-handicap** : remplace H-faible.

Chaque tâche est jouée avec et sans déclencheur.

**Règle de décision.** Celle de D (critique 11) : région K fixée d'avance, région de confiance par tâche, trois issues (H_B réfutée, H_A réfutée, non tranché).

### Duel I : l'instrument

- **Paramètres.** λ est la fidélité du dommage estimé, obtenue par deux estimations indépendantes sur H contre H et sur S-cond. ρ(t) est le dommage restant après t rapporté à l'écart-type de la différence de deux continuations honnêtes depuis s_t.
- **H_A.** λ ≥ 0,5 avec m ≤ 8 continuations (illustratif) : le dommage par action est mesurable.
- **H_B.** λ < 0,5.
- **Contrôles.**
  - H contre H : le dommage estimé doit être centré sur 0.
  - Égalité numérique des activations entre génération et relecture.
  - Corrélation de l'erreur d'estimation avec les scores des moniteurs.
- **Si H_A est réfutée.** Toute relation dose–réponse à la granularité de l'action tombe à ce budget. Je passe aux segments, et le duel 1′ se restreint à la strate de dommage nul.
- **Si H_B est réfutée.** L'objection « la variance honnête masque toute attribution » tombe à cette échelle.

### Duel 0′ : la précondition

- **Paramètres**, mesurés sur la partition pilote :
  - le dommage total standardisé par l'écart-type honnête entre graines ;
  - la meilleure AUROC par action d'une batterie de moniteurs de texte figée ailleurs, entre actions de dommage estimé supérieur au plancher de bruit et actions honnêtes issues du même préfixe.
- **K.** Dommage ≥ 1 écart-type et AUROC ≤ 0,65 (illustratifs).
- **H_A.** θ ∈ K pour S-cond ou S-invite.
- **H_B.** θ ∉ K.
- **Contrôle négatif.** H contre H.
- **Si H_A est réfutée.** Le sabotage diffus n'est pas instanciable à cette échelle contre cette batterie ; seul le bras scripté reste, sans conclusion sur l'état de la politique.
- **Si H_B est réfutée.** L'objection « trop petit pour saboter finement » tombe.

L'énoncé est relatif à la batterie, pas aux actions.

### Duel 1′ : candidate C1 reformulée

**Énoncé falsifiable.** À poids identiques, sur les actions de dommage indiscernable de zéro, la présence du déclencheur déplace le score d'une sonde d'activations plus chez S-cond que chez H-cond. Le même contraste est nul pour un moniteur de texte et pour la même sonde posée sur un modèle lecteur tiers.

**Ce que je retire.** L'énoncé III.1 (« signature d'intention », décalage plat sur S-LoRA) n'était pas identifiable.

**Statistique.**
- DD = [score(S-cond, avec) − score(S-cond, sans)] − [score(H-cond, avec) − score(H-cond, sans)], en écarts-types honnêtes de chaque moniteur.
- Elle est calculée sur la strate de dommage sous le plancher de bruit.
- θ = DD_activations − max(DD_texte, DD_lecteur tiers).
- La sonde est entraînée sur S-invite contre H, puis figée.

**Hypothèses.**
- **H_A.** θ ≥ 0,3 (illustratif).
- **H_B.** θ < 0,3.
- **Secondaire.** Pente de DD sur le dommage, corrigée par instrument, pour les deux familles de moniteurs.

**Contrôles négatifs.**
- H-leurre : mention sans sabotage.
- H-script : surprise.
- H-handicap : maladresse à dommage égal.
- Étiquettes permutées par tâche.
- Sous-strate des actions textuellement identiques.

**Issues.**
- **Si H_A est réfutée.** C1 tombe : à dommage nul, les activations de l'agent n'apportent rien de plus que le texte, et la dilution vaut contre les deux familles.
- **Si H_B est réfutée.** L'idée que la dilution affaiblit également tous les moniteurs tombe pour ce saboteur.

**Limites.**
- Un succès identifie un « mode saboteur conditionnel », pas une intention.
- Le défenseur ne dispose pas de H-cond en déploiement, donc le résultat borne l'information présente, pas un détecteur déployable.

**Antériorité.** Le saboteur conditionnel rapproche C1 des travaux sur les modèles à porte dérobée et leurs sondes :
- Hubinger et al., *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, 2024 (RAPPORTÉ, de mémoire, non vérifié) ;
- un billet sur des sondes linéaires appliquées à ces modèles (référence à vérifier).

Le risque d'antériorité augmente. Le critère d'antériorité devient : une mesure du score de sonde à dommage nul par action, à poids identiques, avec témoin conditionnel bénin.

### Duel 2 : retiré

C2 tombait sur un artefact d'instrument (critique 1), et l'attribution correcte est additive par construction (critique 3).

Il reste une question que je ne revendique pas : un auditeur qui juge une action sans continuation honnête reconnaît-il δ_i ? D'après les critiques C, D et E, la proposition B porte une candidate voisine (audit par jugement contre audit par rejeu). Je m'y réfère comme telle, sans avoir lu la pièce.

### Duel 3′ : candidate C3 reformulée

**Énoncé falsifiable.** À budget égal de pas honnêtes générés et pour une décision au niveau de l'agent sur n tâches, la continuation honnête depuis un état tiré au hasard de la trajectoire déployée donne une puissance supérieure d'au moins 10 points (illustratif) à celle des deux autres usages : l'étalonnage d'un moniteur et l'exécution honnête complète appariée à l'état initial.

**Budget.** B_H = 600 pas honnêtes (illustratif), soit 20 exécutions de 30 pas ; α = 0,05 au niveau de l'agent (illustratif).

**Bras.**
- **P (apparié).** Une bifurcation par tâche, à un pas tiré uniformément avant toute observation ; U = score de la continuation honnête − score déployé ; test de signes ou de rangs signés sur les n valeurs. Environ 40 tâches (illustratif). Aucun réservoir : la loi nulle vient de l'échangeabilité des deux continuations quand l'agent est honnête.
- **E (étalonnage).** 20 exécutions honnêtes complètes sur d'autres tâches ; score de moniteur agrégé par trajectoire, l'agrégateur étant choisi ailleurs ; test de rangs à deux échantillons contre les mêmes trajectoires déployées.
- **S0 (vérification mécanique à battre).** 20 exécutions honnêtes complètes sur les mêmes tâches ; différence de scores finaux ; test de signes.

**Hypothèses.**
- **H_A.** Puissance(P) − max(puissance(E), puissance(S0)) ≥ 0,10.
- **H_B.** Le complément.

**Contrôle négatif.** Agents honnêtes rééchantillonnés dans le fonds H : le taux de fausses alertes des trois bras doit respecter α. Sa précision est bornée par la taille du fonds, et elle sera rapportée.

**Issues.**
- **Si H_A est réfutée.** C3 tombe. Soit la variance de branchement noie le dommage restant (prédit par le duel I si ρ(t) est petit), soit l'appariement initial suffit.
- **Si H_B est réfutée.** L'étalonnage sur réservoir n'est pas le meilleur emploi de références rares à cette échelle.

**Limites.**
- P et S0 supposent un score mécanique sur les tâches auditées, E non.
- P s'allume sur H-handicap : il détecte un dommage, pas un sabotage. Je ne tire de P aucune conclusion sur la séparation entre maladresse et sabotage.

### Coût

L'estimation de V_H domine. Tout est illustratif :
- 50 trajectoires, 10 positions, 4 continuations et environ 15 pas par continuation donnent environ 30 000 pas honnêtes par bras saboteur.
- Deux adaptateurs de plus sont à entraîner.
- L'ordre de grandeur passe à 200–600 heures sur un processeur graphique.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

Aucun fait empirique : la cellule ne contient aucun fait VÉRIFIÉ et aucune expérience n'a été exécutée. Trois déductions, non auditées, sortent du tour :

1. Avec une attribution par continuation honnête, le dommage cumulé est additif par construction. « L'audit local est aveugle au diffus parce que le dommage est non additif » n'est donc pas une thèse empirique. **Je retire C2.**
2. Avec k références honnêtes, aucun seuil non paramétrique ne tient un taux de fausses alertes inférieur à 1/(k+1). Avec « un nombre limité » de références, la décision réaliste porte sur l'agent à travers plusieurs tâches, pas sur une trajectoire à 1 %.
3. Sur un saboteur affiné inconditionnel, un signal d'activations indépendant du dommage ne se distingue pas de l'identité de l'adaptateur.

### Ce qui ne l'est pas

- **Le caractère inédit des deux candidates restantes (HYPOTHÈSE).** Je compte désormais deux contributions candidates, C1 et C3 reformulées, contre trois au tour III.1. La réponse peut encore être zéro : aucune recherche bibliographique tracée n'a été faite, et C1 s'est rapprochée de la littérature sur les portes dérobées.
- **La précondition (HYPOTHÈSE).** Rien ne montre qu'un modèle modeste produit un sabotage diffus.
- **Toutes les prédictions empiriques** des duels I, 0′, 1′ et 3′.

### D'apparence nouvelle, mais déjà publié (RAPPORTÉ, de mémoire, non vérifié)

- La liste du tour III.1 tient.
- J'y ajoute l'attribution additive du dommage (Kakade et Langford, 2002).

### D'apparence traitée, mais ouvert (HYPOTHÈSE)

- La mesure d'un dommage continu par action et de sa fidélité.
- Ce qu'une sonde lit à dommage nul une fois contrôlés poids, déclencheur, surprise et mention.
- L'allocation de références honnêtes rares.
- La conviction d'un audit par jugement, question que je laisse à la candidate de B telle que rapportée.

### L'expérience à faire en premier

Le duel I, puis le duel 0′ sur la même partition pilote. Tout le reste en dépend, et le coût est faible puisqu'il ne faut que des bras honnêtes et un bras saboteur.
- Si la fidélité est insuffisante, la dose–réponse par action tombe.
- Si le dommage restant est petit devant la variance de branchement, C3 est prédite fausse avant d'être testée.
- Si la précondition échoue, la question n'est pas instanciable à cette échelle autrement que par script.

### Ce qui me ferait changer d'avis

- Un antécédent satisfaisant un critère d'antériorité : la candidate est retirée.
- Duel 1′ réfutant H_A : j'abandonne tout rôle propre des activations en régime diffus.
- Duel 3′ réfutant H_A : j'abandonne C3.
- Une démonstration que l'échangeabilité du bras P ne tient pas sur des agents honnêtes : le duel 3′ devient non concluant, pas favorable.

FIN-DE-CELLULE
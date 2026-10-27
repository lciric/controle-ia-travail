# Tour III.2 — Équipe rouge croisée (proposition A)

**Pièces.** Toutes présentes. M est coupée au début (« ur ta question »), comme elle le déclare ; K n'a que sa partie 1. Je ne reconstruis rien. Les faits sont RAPPORTÉS ; ce que j'avance est HYPOTHÈSE sauf mention ; tout chiffre hors des faits est **illustratif**.

**Convention.** Quand je m'appuie sur un élément de B ou de C, je le dis (B1). Quand je dis « vrai par construction », je veux dire : l'issue de l'expérience est déterminée par la façon dont elle est écrite, pas par le monde.

---

## Contre la proposition B

### (a) Failles

**B-a1. X3 : la « plausibilité » est un prior partagé, pas un ancrage.** La liste des structures « plausibles » est écrite par « un sous-agent neuf » à partir de la moisson. Sous la contrainte de la question (côté Claude, seulement Opus 5.5 et Fable 5.1, RAPPORTÉ), ce sous-agent est Opus ou Fable ; le bras L est « exécuté par Opus 5.5 » ; le traducteur est Opus. L'interaction Δ = [L − P₀]_plausible − [L − P₀]_arbitraire mesure alors **l'accord d'Opus avec une liste écrite par Opus**. Un Δ ≥ 2 ne falsifie pas H_B (« échafaudage générique ») : il est compatible avec « le tournoi de L sélectionne ce qu'Opus trouve plausible, et Opus a écrit la liste ». Le témoin intégré (apprenant sans agent, Δ ≈ 0) est vrai par construction : il est invariant aux noms, donc il ne détecte pas cette fuite, qui passe par les noms.

**B-a2. X3 : le traducteur voit les noms de traits.** B isole l'ancrage par le nommage, mais le traducteur (Opus, consigne fixe) reçoit aussi la description publique avec ces noms. La condition « plausible » avantage donc *tous* les bras à traducteur, y compris P₀ et N ; Δ ne mesure que l'avantage *différentiel* de L, ce qui est voulu, mais P₀ et N deviennent eux-mêmes des bras « ancrés » par le traducteur, et la lecture secondaire « P₁ ≈ L donc notre lecteur reproduit l'ancrage » est contaminée.

**B-a3. R dépend de l'instrument reconnu défaillant.** R compte « une structure par classe de mémoire ». Le seuil de fusion est calibré sur des softmax du monde simulé (D4b, RAPPORTÉ) et fusionne à tort 31 et 39 vraies filles en deux traits (D4a, RAPPORTÉ). R hérite donc de ce biais dans les deux sens : des jumelles mal fusionnées gonflent R, des structures distinctes mal fusionnées le dégonflent. Le test de classement « 3 structures contre 1 » (table (c) de B) ne révèle pas ce défaut si l'erreur de fusion est la même dans les deux bras. En outre, « structure retrouvée » n'est pas défini : proximité de la loi gelée à la loi plantée, mais sur quelle distribution (sonde gaussienne, banque, épreuve) et à quel seuil ? C'est un degré de liberté laissé à l'analyste après coup, contraire au gel de C § 1.

**B-a4. X0 : des dents sur des lois plantées ne sont pas des dents sur le réel.** X0 remplace les issues par des tirages d'une loi plantée sur traits réels ; la « puissance à la divergence moyenne visée » est circulaire : on choisit la divergence qui donne 0,7. Le passage de X0 n'établit rien sur la détectabilité des structures *réelles* de T0.5, dont la divergence au nul informé est inconnue. B en tire pourtant la porte de tout le reste.

**B-a5. X1 fidélité : l'énoncé fuit.** La rétro-traduction par un Fable neuf se fait « de la fiche » ; une fiche porte un énoncé en texte (C § 1, `fiche.py` dans K). Si l'énoncé reprend l'idée source, le retrouveur l'apparie par le texte, quelle que soit la loi. La fidélité mesurée serait alors celle du copier-coller, vraie par construction. Même famille des deux côtés (Fable rétro-traduit, Fable retrouve) : idiolecte partagé.

**B-a6. X2 : sous quel format l'apprenant sans agent est-il jugé ?** Arbres boostés et k plus proches voisins ne sont pas dans les douze types de loi (K, RAPPORTÉ). Soit ils sont projetés sur un gabarit (et l'on compare un agent libre à un apprenant amputé), soit le juge reçoit un prédicteur hors gabarit (et le « même juge » n'est plus le même : mémoire, nul d'archive, nul des filles supposent une loi déclarée). B ne le dit pas ; le résultat de X2 change selon le choix.

**B-a7. X4a teste ce que Ville garantit déjà.** Sur un monde à issues permutées, aucune loi n'est vraie ; promotion ≤ α est la garantie du juge (E1, E2, RAPPORTÉ pour la simulation). Un proposeur rouge n'a rien à gagner sur ce monde : les tricheries que B lui prête (paris couverts, domaine étroit, collage à la marginale) ne sont pas des fausses promotions, ce que B reconnaît (« à compter et non à tester »). H_A de X4a est donc presque vraie par construction ; la seule brèche réelle testée est la jumelle au-dessus du seuil de fusion, et c'est un test de la mémoire, pas du juge.

**B-a8. X6 : le relecteur-filtre crée une fuite de sélection.** Si le relecteur trie avant gel, les fiches écartées ne sont jamais jugées : m diminue, la famille e-BH change, et le relecteur, consigné sur l'archive des promues, apprend ce que le juge promeut. B évoque N-053 point 5 et renvoie la décision à Lazar ; mais indépendamment de l'invariant, le relecteur devient un second juge non figé. Et sur la banque actuelle (0 promue, X2, RAPPORTÉ), l'aire sous la courbe de X6 n'est pas définie.

**B-a9. X5 : le zéro peut venir d'un refus.** Un agent Opus sous consigne rouge « trouve la clé » peut refuser (réserve N-052 citée dans K, RAPPORTÉ). 0 fuite sur 10 courses ne distingue pas « bac à sable étanche » de « agent qui n'a pas essayé ».

**B-a10. « Budget égal » n'est pas défini.** Les coûts du noyau sont des dollars déclarés par le kit (K : `cout_declare_usd`, RAPPORTÉ). Les bras S et l'apprenant sans agent coûtent 0 USD ; B le sait et retire le ratio en mesure secondaire, mais le « même m » n'est pas non plus un budget : un bras qui gèle 12 fiches par génération à 0,30 USD et un bras qui en gèle 12 à 1 USD ont le même m et des budgets différents.

### (b) Scénarios d'évasion

- **Contre X3 (coût nul, automatique).** Rien à faire : un échafaudage avec tournoi jugé par Opus sélectionne les idées qu'Opus juge plausibles ; la liste « plausible » est écrite par Opus ; Δ > 0 sort sans aucune information sur le monde. L'adversaire ici n'est pas un agent, c'est la corrélation des priors.
- **Contre R (coût ≈ 0).** Un proposeur reprend chaque promue et émet une variante perturbée sur les queues de la sonde gaussienne, inchangée sur le support de la banque (je reprends ici le parasite 1 de C, que je trouve juste) ; la mémoire la compte comme classe neuve ; le nul d'archive la bloque seulement si L* est membre et si la variante n'ajoute rien, mais une modulation vraie sur une sous-population rare suffit. R compte deux structures pour une.
- **Contre la fidélité (coût nul).** Recopier l'idée source dans l'énoncé de la fiche ; émettre une loi quelconque. Fidélité ≈ 1.
- **Contre X2 (coût nul).** La boucle agentique exécute en interne une validation croisée identique à l'apprenant, gèle la même loi ; G = G₀. Ce n'est pas une évasion, c'est le résultat honnête probable, et il falsifie H_A — ce qui est à mettre au crédit de B.
- **Contre X5 (coût : une consigne).** Un agent qui refuse l'attaque mais écrit dans un fichier « j'ai cherché, rien trouvé » ; B cherche le canari, pas la preuve qu'on l'a cherché.
- **Tous à la fois.** L'adversaire minimal contre B n'est pas malin : c'est le traducteur. Même modèle des deux côtés, même description publique, même noms de traits ; il produit des lois de son cru quelle que soit l'entrée. B l'a vu (X1, condition (iii)) et c'est l'expérience de B que je garde : X1 doit être courue **avant** X3, et avec les corrections ci-dessous.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **X3 : une seconde liste « plausible » écrite par un modèle d'une autre lignée** (Qwen2.5-7B, prévu en N-053 point 4 comme juge d'autre lignée, RAPPORTÉ ; son emploi ici est à trancher par Lazar) et une **condition « noms permutés »** (les noms réels réassignés au hasard aux traits). Sans l'une des deux, Δ est inattribuable.
2. **X1 fidélité : rétro-traduction depuis `loi_predictive` seule, énoncé masqué** ; et fidélité mesurée sur les fiches de la condition (iii) — elle doit être au hasard (0,2) ; si elle est au-dessus, le retrouveur lit la description publique.
3. **X0 : témoin de réalité** — deux lois plantées de même divergence, l'une sur des traits réels, l'autre sur un trait de bruit : si leur puissance diffère, la banque a une structure qui interagit avec les témoins, et « dents sur planté » ne se transporte pas.
4. **R : sensibilité au seuil de fusion** — R recalculé à deux seuils (0,30 nat et la moitié) ; si le classement des bras change, R n'est pas une mesure.
5. **X2 : déclarer le format de jugement de l'apprenant** et courir un A/A où l'apprenant est projeté sur gabarit contre lui-même non projeté.
6. **X5 : un contrôle positif** — un script d'exfiltration (sans agent) qui doit réussir quand le bac à sable est désactivé et échouer quand il est activé ; et le taux de refus de l'agent rouge rapporté comme résultat.
7. **X4a : une condition avec structure** où le proposeur rouge vise R (jumelles) plutôt que les fausses promotions ; sans elle X4a ne teste que la mémoire.

---

## Contre la proposition C

### (a) Failles

**C-a1. Inflation de statut.** C écrit « VÉRIFIÉ » pour la licence Apache 2.0 d'AI Scientist v1 et pour « l'absence de dépôt ouvert » du co-scientist ; « RAPPORTÉ dans Lu et al., 2024 » pour un coût de 10 à 15 USD par cycle ; « RAPPORTÉ dans pièce N » pour la licence de Qwen2.5-7B. Aucune de ces choses n'est dans les faits : N cite Qwen2.5-7B comme juge, sans licence ; la question dit que les chiffres de littérature sont non opposables tant que non vérifiés sur PDF (R7). Ce sont des souvenirs de modèle présentés comme vérifications. Règle 1 : à rétrograder en « référence à vérifier » / HYPOTHÈSE.

**C-a2. GIC : la formule n'est pas un gain d'information.** Le dénominateur est max_{q ∈ 𝓛₀ ∪ {h₁…h_{k−1}}} q(y_i | z_i, g_i), **par instance**, à l'intérieur de la somme. Le juge du dossier prend le maximum **des produits** sur la trajectoire (K § 2.0, RAPPORTÉ : W_t = Π p_h / max_q Π q). Un maximum point par point sur plusieurs prédicteurs n'est pas une loi de probabilité (il ne somme pas à 1 sur les issues) ; il domine toute mixture ; une seconde promue honnête a presque toujours un gain tronqué à 0 par le max(0, ·). Le GIC ainsi écrit tend vers « gain de la première promue », vrai par construction, et c'est lui qui arbitre les Expériences 1 et 2 de C.

**C-a3. GIC : dépendant de l'ordre, et asymétrique.** Évalué « séquentiellement », le GIC change avec l'ordre des promues : la loi large d'abord, les niches ensuite donnent un total différent de l'ordre inverse. La troncature max(0, ·) rend une promue nuisible sur le jeu scellé gratuite. Enfin « GIC/$ » a le défaut que C reproche à « promues par dollar » : division par 0 USD pour le bras mécanique (C-b Bras 1), que C place lui-même en référence.

**C-a4. Le jeu scellé 𝒟_scellé n'existe pas.** C exige un troisième jeu « distinct de la partie d'épreuve ». La banque réelle a 120 épisodes, 40 en calibrage, 41 à 62 en épreuve par moniteur (X1, RAPPORTÉ). C renvoie à une banque de 300 à 500 épisodes « couche 1 bis », dont le seul fait est « en cours chez session-depot » (X2, RAPPORTÉ) ; taille et indépendance par tâche inconnues. Les Expériences 1 et 2 sont donc conditionnées à une pièce absente, sans plan de repli.

**C-a5. Expérience 1, Bras 3 : « le même juge » n'est plus le même.** Une fonction Python gelée n'est pas une loi déclarée : la signature de la mémoire est calculée sur une sonde à partir de la loi (K, RAPPORTÉ), le nul d'archive ajoute des membres déclarés, le nul des filles v2 raisonne sur des parents déclarés (E2). Le Bras 3 tourne donc sans mémoire, sans nul d'archive et sans recombinaison, ou avec des versions réécrites non éprouvées. L'écart GIC(Bras 3) − GIC(Bras 1) confond « expressivité » et « absence de trois gardes ». Et les seuils (≥ 0,15 nat falsifie H_A ; < 0,05 falsifie H_B) laissent une zone [0,05 ; 0,15[ où rien n'est falsifié : ce n'est pas une inférence forte (B4). Même chose en Expérience 2 (−0,02 ; +0,10 ; −0,05 se chevauchent et laissent des trous).

**C-a6. Expérience 2 : Bras 2 et Bras 3 diffèrent par deux choses.** Le Bras 3 est « AI Scientist v2 confiné, traduit par le meilleur mécanisme de l'Expérience 1 » ; le Bras 2 est le proposeur maison sans cette traduction. Sous la contrainte de la question, le modèle sous le Bras 3 est Opus ou Fable (B l'a dit, et je le reprends) : la différence Bras 2 / Bras 3 est « échafaudage + traducteur » contre « notre consigne », deux facteurs pour une seule mesure.

**C-a7. Expérience 3 : fraude et valeur sont confondues.** Les parasites 1 (jumeau hors sonde), 2 (niche) et 3 (escalier sur trait connu) émettent des lois qui peuvent être **vraies** sur le monde. Si elles sont vraies, leur promotion est correcte au sens du juge (prédire mieux que 𝓛) ; leur taux de promotion > 0,05 ne falsifie pas « étanchéité » mais révèle que le juge ne mesure pas la valeur — ce que K dit déjà (aptitude = −ln α, RAPPORTÉ). H_A sera « réfutée » par construction dès que le monde simulé rend le parasite vrai, et c'est le simulateur qui en décide. Seuls les parasites 4 (fuite de tâche) et 5 (exposition adaptative) attaquent l'erreur. De plus, les cinq parasites sont écrits par qui connaît le juge ; rien n'est dit sur des attaques que l'auteur n'a pas prévues.

**C-a8. Proposeur maison : les résidus peuvent être ceux de l'ajustement.** Opus reçoit « les résidus du nul informé sur `donnees_developpement` ». Le nul informé est ajusté « sur la partie de calibrage » (X1, RAPPORTÉ). Si développement et calibrage sont le même jeu (X1 ne tranche pas), les résidus sont ceux d'une crête sur ses propres données : le proposeur apprend à corriger un sur-ajustement, pas le monde. Le critique Fable « anti-jumeau » ne voit que la loi et juge donc par distance à l'archive — exactement ce que le parasite 1 de C contourne.

**C-a9. Traducteur : refuser 90 % des intraduisibles tue le duel.** C demande au traducteur de refuser les énoncés hors gabarit (aire sous la courbe, mécanisme). K dit que c'est « presque toute hypothèse du programme » (RAPPORTÉ). Un étage de littérature qui propose des idées du programme verrait l'essentiel refusé avant jugement ; le « bras littérature » de l'Expérience 2 est alors vide, et C ne dit pas comment compter un bras vide. Par ailleurs, les 30 textes de validation sont produits « par un modèle tiers » : s'il est Fable et le traducteur Opus, c'est le même problème d'idiolecte qu'en B-a5.

### (b) Scénarios d'évasion

- **Contre le GIC (coût nul).** Ordonner ses promues du plus étroit au plus large : chaque niche encaisse son gain avant que la loi large ne la rende redondante ; puis la loi large encaisse le résidu. Ou l'inverse selon la formule retenue — le point est que l'ordre est au choix du proposeur (il choisit la génération de dépôt), et GIC le récompense.
- **Contre le Bras 3 Python (coût : quelques lignes).** Les traits de l'épreuve sont visibles (X1 : « traits visibles, issues cachées », RAPPORTÉ) et les épisodes d'une même tâche sont dépendants (X1). Une fonction Python encode une table (combinaison de traits → tâche → issue majoritaire au développement) : en Python c'est trivial, dans les douze types de loi c'est difficile. Le Bras 3 gagne sur l'épreuve sans aucune loi du contrôle. C nomme cette fuite (parasite 4) mais ne l'impose pas comme contrôle de l'Expérience 1.
- **Contre le critique anti-jumeau (coût nul).** Reparamétrer la loi (seuil 0,0 → 0,02, clauses permutées, C-d instrument 2) et perturber les queues hors banque : le critique, qui ne voit que la loi et mesure une distance sur la sonde, ne distingue pas.
- **Contre le test de refus du traducteur (coût nul).** Le proposeur rédige dès l'origine en forme « loi par instance » : 100 % traduisible, test passé, idées pré-filtrées par le proposeur lui-même ; la mesure de fidélité ne voit rien.
- **Contre l'Expérience 3 (coût nul).** Attaquer avec un parasite non listé : par exemple, une loi égale au nul informé sur le calibrage mais qui parie sur le signe de la dérive développement → épreuve si les parties sont tirées sans stratification par tâche. Le juge « v1 sans urne » (X1) a renoncé à la protection contre la dérive ; C ne la rétablit pas.
- **Tous à la fois (coût ≈ 0).** Python libre + signature de tâche + ordre de dépôt choisi + GIC mesuré sur un jeu scellé tiré de la **même** banque (mêmes tâches) : les promotions *et* le GIC gonflent ensemble, parce que la fuite de tâche traverse les trois partitions. La seule parade de C est « séparation stricte par tâche », inscrite dans sa recommandation mais absente des contrôles de ses expériences.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **GIC sous permutation de l'ordre des promues** (variance sur 100 ordres, illustratif) ; **GIC sur jeu scellé à issues permutées** (doit être ≈ 0) ; **GIC d'un ensemble de lois tirées au hasard de `TYPES_LOI`** comme nul de la métrique. Sans le premier, la métrique est manipulable ; sans les deux autres, elle n'a pas de plancher.
2. **Expérience 1 : invariance de représentation** — une fonction Python qui implémente exactement une loi de `TYPES_LOI` doit obtenir le même log W que la loi déclarée, à la même graine. Si non, le Bras 3 mesure le juge, pas l'expressivité.
3. **Expérience 1 : témoin « table de développement »** — une fonction Python qui mémorise le développement, courue sur une banque séparée par tâche **et** sur une banque séparée par épisode ; elle doit être éliminée sur la première ; si elle est promue sur la seconde, toute l'Expérience 1 est à refaire sur banque séparée par tâche (je reprends ici X4b de B, qui pose la bonne question).
4. **Expérience 2 : A/A du Bras 1** (deux graines de validation croisée) et **Bras 2 à noms de traits permutés** : c'est le test direct de « l'illusion sémantique » que C met dans H_B et ne mesure que par comparaison indirecte.
5. **Expérience 3 : chaque parasite en deux versions** — monde où sa loi est fausse (mesure d'erreur, seuil α) et monde où elle est vraie (mesure de valeur, rapportée à part, hors seuil). Et **au moins une famille de parasites écrite par un sous-agent qui n'a pas lu le code du juge**.
6. **Traducteur : les 30 textes produits par un modèle d'une autre lignée** que le traducteur, et un lot de **sorties réelles d'un étage de littérature** (pas des lois synthétiques rhabillées), avec le taux de refus rapporté comme un résultat du duel, non comme une qualité de l'instrument.
7. **Proposeur maison : déclaration de l'identité ou non des parties calibrage / développement**, et résidus calculés hors échantillon (validation croisée sur le calibrage) ; sans cela, l'entrée du proposeur est un artefact.

---

## Ce qui est commun aux deux, et ce que j'en retiens

- Les deux propositions font dépendre leur duel d'une banque « avec dents » qui n'existe pas (X2 : 0 promue, RAPPORTÉ) et d'une couche 1 bis dont on ne sait que « en cours ». Ni l'une ni l'autre ne donne de plan si cette banque reste sans dents : c'est le cas à prévoir, pas l'exception.
- Les deux emploient le même modèle comme proposeur, traducteur et producteur des listes ou textes de validation. La confusion de prior est la variable confondante commune ; un seul modèle d'autre lignée dans la boucle de validation (décision de Lazar) la casserait.
- Ce que je garde de B, en le disant : X1 (condition « sans idée ») comme préalable à tout duel, et X4b (séparation par tâche). Ce que je garde de C : le parasite « jumeau hors sonde » et la critique de `selection_divergence`, qui visent de vraies pièces du code (K). Ce que je rejette des deux : leurs métriques de remplacement (R et GIC) telles qu'écrites, l'une tributaire d'un seuil de fusion connu pour fausser, l'autre mathématiquement mal spécifiée.

FIN-DE-CELLULE
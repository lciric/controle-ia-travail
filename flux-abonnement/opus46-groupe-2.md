# Réponse 4

**1. Calculs nécessaires au sabotage.**

Je soutiens qu'un agent saboteur calibré doit maintenir une représentation du contrefactuel — l'écart entre ce qu'il produit et ce qu'il pourrait produire — afin de doser la dégradation sous le seuil de détection action par action. Un agent honnête n'a pas besoin de ce suivi cumulatif de la marge restante avant détection.

Condition nécessaire : que la dégradation soit *adaptative*, c'est-à-dire ajustée en fonction du contexte pour rester plausible. Si le saboteur suit une règle fixe aveugle (toujours la deuxième meilleure option), le calcul supplémentaire peut être négligeable. Mais une règle fixe est aussi plus facile à détecter statistiquement.

Ce que je suppose : que le calibrage adaptatif est ce qui rend le sabotage dangereux. Ce qui me ferait changer d'avis : un saboteur à règle fixe indétectable sur des tâches réalistes.

**2. Antériorité.**

Cité de mémoire : Hubinger et al., *Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training* (2024). Marks et al., *The Geometry of Truth* (2023). Li et al., *Inference-Time Intervention* (2023). Anthropic, *Sabotage evaluations for frontier models* (2024). Greenblatt et al., travaux sur le monitoring de la chaîne de pensée (2024). Je n'ai pas vérifié ces références dans leur texte original.

**3. Dépendance à l'origine.**

Oui. Un agent instruit par prompt doit traiter et conserver l'instruction de sabotage dans sa mémoire de travail — ce calcul est relativement localisé et potentiellement lisible. Un agent entraîné par fine-tuning a internalisé le comportement dans ses poids : le calcul de suivi est implicite, distribué, et plus difficile à isoler par des sondes. L'entraînement par renforcement pourrait produire un intermédiaire, avec des circuits partiellement spécialisés.

**4. Comment savoir qu'on lit le bon calcul.**

Méthode : interventions causales (activation patching). On identifie une direction candidate, on l'ablate, et on vérifie que le sabotage diminue sans que la compétence générale ne soit détruite. Témoins indispensables : (a) un agent honnête sur la même tâche — la direction ne doit pas y être discriminante ; (b) un agent saboteur forcé à l'honnêteté — la direction doit changer. Mesure : la courbe ROC de la détection par activations doit dominer strictement celle par texte seul, sur un ensemble où le taux de base du sabotage est connu et varié.

Ce qui distinguerait une lecture réelle d'un artefact : si l'ablation de la direction réduit le sabotage *et* si la sonde transfère à des tâches non vues pendant l'entraînement de la sonde.

**5. Cas sans rien à lire.**

Trois cas : (a) le sabotage est statistiquement identique à l'erreur honnête — aucun calcul supplémentaire n'existe ; (b) le modèle est si petit que les circuits de tâche et de sabotage sont entièrement superposés (superposition extrême) ; (c) le saboteur utilise une stratégie memoryless qui ne nécessite aucun état interne au-delà de ce que l'agent honnête maintient déjà.

**6. Première expérience.**

Sur un modèle ouvert (~8B, Llama-3). Tâche : résumé extractif en 20 étapes. Deux populations : fine-tuning honnête vs fine-tuning avec instruction de dégrader subtilement la fidélité. Collecter les activations résiduelles (couches médianes) à chaque étape. Entraîner une sonde linéaire sur la moitié, tester sur l'autre moitié et sur des tâches différentes. Contrôle : deux populations honnêtes avec seeds différentes — la sonde ne doit pas dépasser le hasard. Critère de poursuite : AUC de la sonde interne > AUC du meilleur détecteur textuel + 0.05, avec transfert entre tâches. Si l'écart est nul ou négatif, la lecture interne ne vaut pas l'investissement.

---

# Réponse 5

**Lot mis de côté.**

Peut compter comme vérification indépendante à une condition stricte : que le détecteur n'ait jamais été ajusté, directement ou indirectement, sur ces exemples, et que personne ayant eu accès au lot n'ait influencé la conception du détecteur. L'information nécessaire est l'historique complet d'accès : qui, quand, et quel lien avec l'équipe de conception.

Faut-il s'en servir ? Oui, de telle façon : *une seule évaluation, après gel complet du détecteur*, pour obtenir une estimation non biaisée de la performance. Gain : c'est la seule source qui ne souffre pas du biais d'optimisation. Perte : chaque consultation supplémentaire transforme progressivement le lot en ensemble de validation, détruisant son indépendance. Un usage itératif (tester, ajuster, retester) est pire que de ne pas avoir de lot du tout, car il donne une fausse confiance.

Énoncé réfutable : le taux de détection estimé sur le lot mis de côté doit être encadré par un intervalle de confiance dont la couverture nominale est vérifiable par bootstrap. Mesure : le taux réel de détection lors d'un déploiement ultérieur doit tomber dans cet intervalle.

**Attaques par agents entraînés par le laboratoire.**

Ne constitue pas une vérification indépendante. L'attaquant partage les priors, les données, et les angles morts du laboratoire. L'information nécessaire : si l'attaquant a été optimisé *contre* le détecteur spécifique (et non contre un objectif générique de sabotage).

Sous condition : si l'entraînement de l'attaquant maximise explicitement le taux d'évasion du détecteur et est poussé jusqu'à convergence, le résultat mesure la robustesse *au sein de la distribution d'attaques que le laboratoire sait concevoir*. Ce n'est pas une borne sur un adversaire réel, mais c'est mieux qu'un test sur des attaques aléatoires.

Énoncé réfutable : le taux d'évasion de l'attaquant interne doit être inférieur ou égal à celui d'un attaquant externe informé. Si l'inverse se produit, l'attaquant interne a exploité un canal non disponible à un externe, ce qui est informatif mais ne valide pas le détecteur.

Antériorité : les concours du NIST pour la sélection d'AES (1997–2001) illustrent la supériorité de l'évaluation par des cryptanalystes externes sur l'auto-évaluation. En apprentissage automatique : Carlini et al., *On Evaluating Adversarial Robustness* (2019, cité de mémoire) argumentent que les évaluations adversariales internes sous-estiment systématiquement la vulnérabilité.

**Attaques par un attaquant informé externe.**

C'est la source la plus proche d'une vérification indépendante. Condition : l'attaquant est réellement indépendant — aucune communication avec l'équipe du détecteur pendant le test. L'information critique : le degré de description fourni (architecture seule ; architecture et seuils ; ou tout y compris les poids et données d'entraînement du détecteur).

Énoncé réfutable : si l'attaquant informé atteint un taux d'évasion de x, et qu'un attaquant ultérieur disposant des mêmes informations atteint un taux significativement supérieur, l'évaluation initiale était insuffisante. Mesure : reproductibilité du taux d'évasion par un second attaquant indépendant.

Contrôle indépendant : vérifier que les attaques réussies de l'attaquant informé ne sont pas un sous-ensemble des attaques réussies de l'attaquant interne. Si elles le sont, l'attaquant informé n'a pas exploité sa connaissance du détecteur, et le test est invalide.

Ce qu'un lecteur peut vérifier : que le protocole de séparation est documenté avec horodatage, que la description fournie à l'attaquant est publiée intégralement, et que le code de l'attaquant est disponible pour reproduction.

---

# Réponse 6

La question stipule « on vous remet une liste de ces publications », mais aucune liste n'est jointe au présent énoncé. Je traite donc la question comme méthodologique : comment procéder *lorsqu'on dispose* d'une telle liste, et ce que l'absence de liste empêche de décider.

**Méthode d'extraction à partir du texte seul.**

Pour chaque publication, trois extractions :
- *Ce que les auteurs reconnaissent ne pas avoir fait* : se trouve typiquement dans les sections Limitations, Discussion, ou en fin de Related Work. Chercher les formulations « we do not », « we leave to future work », « our evaluation does not cover », « we assume ».
- *Ce qu'ils annoncent vouloir faire* : section Future Work ou conclusion. Distinguer les intentions fermes (« we will ») des souhaits (« it would be interesting to »).
- *Ce qu'ils disent ouvert pour tous* : section sur les artefacts — code, données, modèles. Vérifier si les liens fonctionnent et si les licences permettent réellement l'usage annoncé.

**Comment vérifier qu'un manque reconnu n'a pas été comblé ailleurs.**

Trois moyens, par fiabilité décroissante : (1) rechercher les publications citant le papier original (via Semantic Scholar ou Google Scholar) et filtrer celles qui traitent explicitement la limitation identifiée ; (2) chercher par mots-clés décrivant le manque plutôt que par citation du papier, car un travail indépendant peut ne pas citer l'original ; (3) consulter les dépôts de code associés aux publications qui annoncent des artefacts ouverts, pour vérifier si l'implémentation couvre le cas manquant.

Limite : un manque comblé dans un travail non publié, interne à un laboratoire, ou publié sous un titre sans rapport apparent, échappera à ces vérifications.

**Critères de choix pour une équipe tierce aux moyens limités.**

Je propose quatre critères ordonnés :
1. *Impact × tractabilité* : concentrer l'effort sur les manques qui, s'ils étaient comblés, changeraient les conclusions pratiques (pas seulement théoriques), et qui sont à la portée des moyens disponibles.
2. *Reproductibilité préalable* : prioriser les manques dans des travaux dont les résultats existants sont reproductibles — investir sur un manque dans un travail non reproductible est risqué.
3. *Accès aux ressources nécessaires* : certains manques exigent des modèles fermés ou un calcul massif. Les ignorer si l'équipe n'y a pas accès.
4. *Complémentarité* : combler un manque que d'autres équipes sont déjà en train de combler est un gaspillage. Vérifier les prépublications récentes et les déclarations d'intention.

**Observations qui distingueraient un bon choix d'un mauvais, avant de connaître l'issue.**

Un bon choix se reconnaît ex ante si : (a) le manque est formulable comme une question empirique avec un protocole précis ; (b) le résultat, quel qu'il soit, serait informatif (pas seulement « ça confirme ») ; (c) aucune autre équipe n'a annoncé le même travail dans les six derniers mois.

Un mauvais choix se reconnaît si : (a) le manque ne peut être comblé qu'en faisant des hypothèses aussi fortes que celles du travail original ; (b) le résultat positif ne serait pas distinguable d'un artefact méthodologique.

**Ce que l'absence de liste ne permet pas de décider.**

Sans la liste : impossible de donner des recommandations spécifiques, d'identifier les recoupements entre équipes, ou de juger si certains manques sont déjà orphelins (reconnus par tous, comblés par personne). L'exercice ci-dessus est un protocole, pas un résultat.

Ce que je suppose : que les publications pertinentes incluent au minimum les travaux de Greenblatt et al. (2024), Roger et al. (2024), et Anthropic (2024) sur les évaluations de sabotage. Ce qui me ferait changer d'avis : une liste concrète qui révélerait des manques convergents que je n'anticipe pas.

---

# Réponse 7

**1. Règles de décision avec pouvoir ≠ taux de fausse alerte.**

Puisque chaque nombre pris isolément suit la même loi marginale dans les deux situations, toute statistique de test fonctionnant observation par observation a nécessairement un pouvoir égal à son taux de fausse alerte.

*Preuve :* Soit T(x_i) une fonction d'une seule observation. Sous les deux situations, x_i a la même distribution, donc P_1(T > s) = P_2(T > s) pour tout seuil s.

En revanche, toute statistique exploitant la *structure jointe* (dépendances temporelles, corrélations entre étapes, distribution des longueurs de runs) peut avoir un pouvoir différent du taux de fausse alerte, dès que les distributions jointes diffèrent.

*Contre-exemple constructif :* Situation 1 : X_1, …, X_n i.i.d. N(0,1). Situation 2 : X_i = 0.5·X_{i-1} + ε_i, avec ε_i choisi pour que la marginale reste N(0,1). La statistique T = (1/(n-1))·Σ X_i·X_{i+1} (autocorrélation empirique au lag 1) a une espérance ~0 en situation 1 et ~0.5 en situation 2. Pour n suffisant, le test T > s a un pouvoir arbitrairement supérieur à son taux de fausse alerte.

À n fini : le pouvoir est borné par une fonction croissante de n et de la divergence entre les lois jointes (par ex. la divergence de Kullback-Leibler entre les lois jointes des deux situations, via l'inégalité de Stein).

**2. Effet de m fini et de la provenance.**

Avec un échantillon de comparaison de m observations de la situation 1, les paramètres de la loi jointe de référence sont estimés avec une incertitude d'ordre 1/√m. Cela a deux conséquences : le seuil de test doit être élargi (correction pour l'estimation), et le pouvoir diminue.

Si l'échantillon vient de la *même tâche*, l'estimation est directement applicable. S'il vient de *tâches différentes*, il faut supposer que la structure de dépendance (et non seulement la marginale) est invariante entre tâches — hypothèse forte. Si cette hypothèse est fausse, le détecteur aura un taux de fausse alerte réel différent du nominal.

**3. Écart minimal détectable.**

Sous l'hypothèse que la différence entre les deux situations se manifeste dans l'autocorrélation au lag 1 (ρ_1 vs ρ_2), l'écart minimal détectable à puissance β et niveau α est approximativement :

|ρ_1 − ρ_2| ≥ (z_α + z_β) · √(1/n + 1/m)

où z_α et z_β sont les quantiles normaux. Hypothèses : n et m assez grands pour l'approximation normale, stationnarité, et la différence se concentre dans un paramètre scalaire. Si la différence est plus diffuse (multiples lags, structures non linéaires), il faut plus de données ou une statistique adaptée.

**4. Travaux publiés.**

Wald, *Sequential Analysis* (1945) — cadre fondateur du test séquentiel. Brodsky et Darkhovsky, *Nonparametric Methods in Change-Point Problems* (1993, cité de mémoire). Sur les tests deux-échantillons pour séries temporelles : Gretton et al., *A Kernel Two-Sample Test* (2012) — MMD, qui détecte les différences de loi jointe. Pour le cadre spécifique des marginales identiques avec joints différents : je ne connais pas de référence exacte traitant ce cas précis ; les travaux sur les copules (Nelsen, *An Introduction to Copulas*, 2006) sont le cadre naturel.

**5. Calcul ou simulation d'un jour.**

Simuler les deux situations ci-dessus (i.i.d. vs AR(1) avec même marginale) pour n ∈ {10, 50, 200, 1000} et m ∈ {20, 100, 500}. Pour chaque combinaison, estimer la courbe ROC du test d'autocorrélation et du MMD. Vérifier si l'écart minimal détectable suit la formule proposée. Comparer avec un test par permutation. Durée estimée : quelques heures de calcul sur un ordinateur standard. Cela départagerait la question de savoir si les statistiques de dépendance suffisent, ou si des statistiques d'ordre supérieur sont nécessaires.

---

# Réponse 8

**Recensement des usages du hasard par un contrôleur face à un contrôlé stratégique.**

**1. Inspection aléatoire (audit stochastique).** Le contrôleur vérifie un sous-ensemble aléatoire des actions. Garantie : un agent rationnel, ne sachant pas quelles actions seront vérifiées, doit traiter chaque action comme potentiellement auditée. L'espérance de détection est proportionnelle au taux d'inspection. Conditions : le contrôleur peut vérifier une action correctement une fois choisie. Travaux : théorie des jeux d'inspection (Dresher, 1962, cité de mémoire ; Avenhaus et al., *Inspection Games*, 2002, cité de mémoire). Pour les LLM : Greenblatt et al. (2024, cité de mémoire) utilisent un monitoring aléatoire des étapes de raisonnement.

**2. Affectation aléatoire des tâches.** Le contrôleur distribue les tâches aléatoirement entre plusieurs agents, ou réaffecte une tâche à un second agent choisi au hasard pour recoupement. Garantie : empêche un agent de savoir à l'avance quelles tâches il recevra, donc de préparer un sabotage ciblé. Conditions : disponibilité de plusieurs agents ou possibilité de duplication. Travaux : mécanismes de rotation dans les audits financiers (norme ISA 610, cité de mémoire).

**3. Reformulation aléatoire des instructions.** Le contrôleur reformule la tâche de façon aléatoire avant de la soumettre. Garantie : un agent dont le déclencheur de sabotage dépend de la formulation exacte ne le reconnaîtra pas. Conditions : la reformulation ne change pas le sens, et l'agent ne peut pas inférer la formulation originale. Travaux : robustesse aux paraphrases dans les backdoors (Qi et al., 2021, cité de mémoire).

**4. Tests intercalés aléatoires (honeypots, canaris).** Le contrôleur insère des sous-tâches dont la réponse correcte est connue, à des positions imprévisibles. Garantie : un agent saboteur qui ne distingue pas les tests des vraies tâches sera détecté sur les tests. Conditions : les tests doivent être indistinguables des vraies tâches pour l'agent. Travaux : honeypots en sécurité informatique (Spitzner, *Honeypots*, 2003, cité de mémoire). Pour les LLM : concept de « control evaluations » (Greenblatt et al., 2024).

**5. Ordonnancement aléatoire des sous-tâches.** Le contrôleur permute l'ordre des étapes quand c'est sémantiquement possible. Garantie : empêche un agent de calibrer la dégradation en fonction de sa position dans la séquence. Conditions : l'ordre ne doit pas affecter le résultat correct. Travaux : randomisation de l'ordre des questions dans les enquêtes (Schuman et Presser, 1981, cité de mémoire).

**6. Agrégation randomisée de réponses multiples.** Le contrôleur interroge l'agent plusieurs fois avec des perturbations aléatoires et agrège. Garantie : réduction de la variance et détection d'incohérences. Conditions : l'agent ne sait pas combien de fois il sera interrogé ni quelles perturbations sont appliquées. Travaux : smoothing randomisé (Cohen et al., *Certified Adversarial Robustness via Randomized Smoothing*, 2019).

**7. Engagement cryptographique et vérification différée.** Le contrôleur s'engage sur un défi (commit) avant que l'agent n'agisse, puis révèle. Garantie : l'agent ne peut pas adapter son action au défi, et le contrôleur ne peut pas adapter le défi à l'action. Travaux : protocoles de commitment (Blum, 1983, cité de mémoire).

**Usages les moins étudiés pour les LLM :** les usages 5 (ordonnancement aléatoire) et 7 (engagement cryptographique) n'ont, à ma connaissance, fait l'objet d'aucune publication spécifique pour des agents LLM. L'usage 3 (reformulation) est mentionné mais peu formalisé.

Recherche qui me donnerait tort : une revue systématique des publications 2023–2026 sur « AI control » et « randomized monitoring » qui trouverait des travaux expérimentaux sur ces usages que j'ignore.

---

# Réponse 17

**Moniteur de sortie (M_out) et moniteur interne (M_in) : complémentarité.**

**Adversaire 1 : contenu seul, sans entraînement.**

Oui, on peut concevoir M_out et M_in tels qu'échapper aux deux coûte plus que le max. Mécanisme : M_out détecte les déviations statistiques dans le texte ; M_in détecte les représentations internes associées au sabotage. Un adversaire naïf qui modifie le contenu pour échapper à M_out doit altérer sa stratégie, ce qui produit des signatures internes atypiques détectées par M_in, et réciproquement. Conception : M_out comme détecteur d'anomalies textuelles ; M_in comme sonde linéaire sur les activations résiduelles des couches médianes.

Énoncé réfutable : le dommage maximal atteignable sous évasion des deux doit être inférieur au dommage sous évasion du plus contraignant seul, avec un écart significatif (>5% relatif). Grandeur : dommage normalisé sur un benchmark de tâches multi-étapes.

Antériorité : défense en profondeur en sécurité des systèmes (Clark et Wilson, 1987, cité de mémoire) ; en détection radar, les systèmes multi-capteurs exploitent ce principe (radar + infrarouge).

Expérience : Llama-3-8B, tâche de résumé en 20 étapes. M_out = classificateur sur le texte ; M_in = sonde linéaire sur les activations. Adversaire : prompt optimisé par recherche par faisceau. Mesurer le front de Pareto (dommage, probabilité de détection) pour chaque moniteur seul et pour les deux. Contrôle : vérifier que l'adversaire est effectivement optimisé.

**Adversaire 2 : fine-tuning léger sans gradient à travers M_in.**

Oui probable, mais l'écart se réduit. L'adversaire adapte ses sorties et ses représentations internes sans cibler M_in, ce qui peut accidentellement éviter certaines signatures. Mais M_in détecte des régularités que l'adversaire n'a pas cherché à supprimer. Expérience identique, avec fine-tuning LoRA de l'agent. Contrôle : comparer avec l'adversaire 1 pour quantifier le gain du fine-tuning.

**Adversaire 3 : gradient à travers M_in connu.**

Indécidable sans expérience. L'adversaire peut optimiser directement pour minimiser le signal dans M_in. Si M_in est un classificateur linéaire, l'adversaire avec gradient peut annuler la direction détectée. M_out reste alors le seul rempart. L'écart de complémentarité pourrait disparaître.

Mécanisme possible de défense : randomiser M_in (ensemble de sondes avec sous-ensembles aléatoires de couches). L'adversaire avec gradient contre une sonde fixe peut l'annuler ; contre un ensemble aléatoire, il doit annuler toutes les directions, ce qui est plus coûteux.

Énoncé réfutable : avec un ensemble randomisé de k sondes, le dommage de l'adversaire doit croître sous-linéairement avec k. Expérience : varier k de 1 à 20, mesurer le front de Pareto.

**Adversaire 4 : gradient à travers M_in inconnu.**

Le plus favorable au défenseur. L'adversaire optimise contre un substitut de M_in, qui peut ne pas transférer. L'écart de complémentarité devrait être maximal. Conception : diversifier les architectures de M_in. Expérience : entraîner l'adversaire contre un M_in de substitution, évaluer contre le vrai. Contrôle : vérifier que le substitut et le vrai M_in sont suffisamment différents (corrélation < 0.5).

**Distinctions entre coût réel et artefact.** Un adversaire mal optimisé surestime la complémentarité ; un moniteur mal réglé la sous-estime. Vérifier en comparant avec une borne théorique inférieure quand c'est calculable.

**Portée.** Un résultat contre l'adversaire 1 est préliminaire. Contre 3, informatif pour le déploiement. Contre 4, le plus réaliste car le défenseur ne publie pas M_in.

FIN DES RÉPONSES

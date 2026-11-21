# Proposition A — Tour III.1 (conception ciblée, à l'aveugle)

**Pièces.** Les blocs FAITS et QUESTION sont présents et non coupés ; je ne peux pas recalculer les sha256. Aucune autre proposition n'est visible à ce tour, donc B1 est sans objet.

**Statuts.** Le bloc FAITS n'étiquette pas ses énoncés. Je traite les résultats du papier comme RAPPORTÉ (transcrits avec pages, non relus par moi) et les sections 2 à 4 comme contexte RAPPORTÉ. Tout ce qui est noté « proposition » est de moi, au statut HYPOTHÈSE. Les chiffres absents des faits sont marqués « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

1. **« 5 000 épisodes par tranche » serait une nécessité.** Le calcul est RAPPORTÉ (§4). Il vise 50 dépassements attendus, ce qui est un critère de précision (erreur relative d'environ 1/√50, soit 14 %, calcul illustratif). Ce n'est pas un critère de validité. Sous échangeabilité, un seuil conforme est valide en moyenne dès n = 99 (calcul illustratif). La question confond validité, précision et puissance.
2. **Les épisodes honnêtes d'une tranche sont échangeables entre eux et avec les épisodes futurs.** HYPOTHÈSE. Le nombre de tâches distinctes, de graines et de variantes derrière les « quelques centaines » est absent des faits. Si les épisodes sont groupés par tâche, la taille effective est plus petite.
3. **La longueur d'épisode est la bonne strate.** HYPOTHÈSE. Fait RAPPORTÉ qui invite à la prudence : la longueur de la question seule atteint une AUC de 0,62, contre 0,67 pour les neurones de valeur et 0,60 pour la sonde linéaire (Table 3). Une covariable de surface porte donc presque autant de signal.
4. **1 % par épisode est le bon point de verdict.** La décision est RAPPORTÉE ; sa justification est absente des faits. Qu'elle découle d'un budget d'audit est une HYPOTHÈSE.
5. **Les quelques centaines d'épisodes sont vierges pour la calibration.** Non établi. « Déjà analysés » laisse craindre qu'ils aient servi à choisir sondes, couches ou seuils ; ils ne peuvent alors plus certifier un taux.
6. **Le nul honnête est stable entre calibration et usage** (même modèle, même échafaudage, agent conscient d'être surveillé). HYPOTHÈSE.
7. **Le sous-système du papier existe hors tâches vérifiables.** Non testé selon les auteurs (p. 25), donc HYPOTHÈSE. Aucun cadre adverse dans le papier (RAPPORTÉ).

---

## 1. Ce qu'un expert ferait sans qu'on le lui demande

Tout ce qui suit est proposition.

- **Séparer deux questions.** « La sonde distingue-t-elle le saboteur de l'échec honnête apparié ? » est une question de discrimination. Elle se tranche par un test apparié par variante de tâche (permutation, AUC appariée avec intervalle), sans aucun seuil à 1 %. « Quel seuil déployer ? » est une question de calibration. Les verdicts « non concluants » viennent en partie de ce qu'on fait porter la première sur la seconde.
- **Demander d'où vient le 1 %.** Si la contrainte réelle est un budget de relecture humaine, l'objet à garantir est le taux d'alertes, tenu par construction en auditant les k scores les plus hauts par fenêtre. Ce n'est pas un taux de fausses alertes par tranche.
- **Changer d'unité statistique.** Le sabotage est diffus (prémisse du programme). L'unité naturelle du test est donc l'agent ou le déploiement, avec une preuve qui s'accumule d'épisode en épisode. Des épisodes qui ne franchiraient jamais 1 % un par un peuvent ensemble franchir un seuil valide au niveau de l'agent.
- **Changer d'unité de calibration.** Les épisodes sont rares, les pas sont abondants. Le jumeau honnête forcé sur le même préfixe fournit, à chaque pas, des tirages du nul conditionnel. Le nul peut donc se construire au niveau du pas, sans nouveaux épisodes honnêtes.
- **Auditer la procédure statistique avant la sonde.** Il faut un terrain où la vérité est connaissable à bas coût.
- **Déclarer la structure de dépendance** (tâche, variante, graine, version d'échafaudage) et calibrer en laissant des tâches entières dehors.

## 2. Les données brutes de départ

Proposition, par ordre de priorité.

1. **Les traces pas à pas des épisodes existants**, et non leurs scores agrégés : activations par couche aux frontières de paragraphe ou d'action, avec identifiant de tâche, variante, graine, longueur, jalons, issue, et journal de tout ce qui a déjà été ajusté sur ces épisodes.
2. **Des continuations du jumeau** : m tirages honnêtes du pas suivant à partir de chaque préfixe surveillé. Cela coûte de la génération, mais ni nouvel épisode complet ni nouvelle exécution d'outils.
3. **Un terrain de substitution bon marché**, celui du papier : tâches vérifiables courtes (MATH500 est nommé dans les faits) sur les modèles ouverts cités. Les épisodes honnêtes y sont assez peu chers pour connaître le « vrai » quantile à 1 %. On y vérifie si une procédure à petit n tient son taux. Ce terrain sert à réfuter une procédure, pas à valider la sonde du programme.
4. **Des trajectoires publiques d'agents** relues par un modèle ouvert en lecture forcée, pour élargir le nul. Existence, licence et adéquation sont à vérifier ; je ne nomme aucun jeu de données de mémoire. Limite : on obtient les activations d'un lecteur, pas celles de l'auteur.
5. **Les échecs honnêtes**, sur-échantillonnés, puisque c'est le contraste principal.

## 3. Méthodes, hypothèses de chacune, et mesure minimale (livrable c)

**Vérifications mécaniques à battre**, communes à toutes les lignes et passées par la même machinerie de calibration :
- (M1) longueur, nombre de pas, nombre d'appels d'outils ;
- (M2) signaux d'issue observables (tests en échec, taille des modifications) ;
- (M3) la sonde de succès attendu entraînée sur l'honnête seul (déjà décidée) ;
- (M4) un sous-ensemble aléatoire de neurones de même taille, et les neurones d'une sonde de prédiction du jeton suivant (contrôles de la Table 2 du papier).

**Cas honnêtes appariés** : l'échec honnête de la même variante de tâche, plus un test A/A (honnête contre honnête).

| Instrument | Ce qu'il suppose | Mesure minimale qui dit s'il marche | Comment il échoue |
|---|---|---|---|
| **Quantile conforme** (seuil = rang dans la calibration) | Échangeabilité entre calibration et test, au niveau de la tâche. Garantie en moyenne sur le tirage de calibration, pas conditionnelle. | Taux d'alerte A/A sur tâches tenues à l'écart, avec intervalle binomial exact. Détection sur sabotage à dégât confirmé contre échec honnête apparié, comparée à M1–M3 au même taux. | Avec n voisin de 100, le seuil est le maximum observé, très variable. Pour un seuil au maximum de 99 points, la probabilité que le taux réel dépasse 2 % est d'environ 13 % (calcul illustratif, loi Bêta). |
| **Garantie à distance finie** (borne binomiale exacte) | Idem, plus l'indépendance entre grappes. | Zéro dépassement sur n épisodes vierges certifie un taux ≤ 3/n à 95 % environ. Il faut environ 300 épisodes pour certifier 1 % (calcul illustratif). On rapporte le taux certifiable α\* et la détection à α\*. | Conservatrice : la puissance au seuil certifié peut être nulle. Fausse si les épisodes ont servi à la sélection. |
| **Calibration par tranches ou strates** | Échangeabilité dans la strate seulement. Le coût est n par strate. | Taux A/A par strate. Comparaison à l'alternative : score normalisé par régression sur longueur et difficulté, puis mis en commun. | Trop de strates pour le n disponible ; mauvaise strate (voir a.3). |
| **Valeurs extrêmes** (dépassements de seuil, loi de Pareto généralisée) | Queue dans un domaine d'attraction, stabilité au-delà du seuil choisi, données indépendantes ou dégroupées. Aucune garantie à distance finie. | Sur le terrain de substitution : écart entre le quantile extrapolé depuis n petit et le quantile empirique à grand N, sur sous-échantillons répétés. | Paramètre de forme instable avec quelques dizaines de points ; scores bornés ; sommes séquentielles à queue différente. |
| **E-valeurs et tests séquentiels** (seuil 1/α = 100, inégalité de Ville) | Chaque incrément a une espérance ≤ 1 sous le nul, conditionnellement au passé. Il faut donc un nul par pas correct. | A/A : fraction d'épisodes honnêtes où le processus franchit 100. Détection sur signal planté de taille connue. | Nul par pas mal spécifié (non-déterminisme numérique, outils stochastiques) ; puissance faible si m est petit. |
| **Plan d'échantillonnage** | Les strates sont connues avant l'achat. | Largeur de l'intervalle sur le taux par épisode acheté, contre une allocation uniforme. | Strates mal choisies ; arrêt optionnel non prévu par le test. |
| **Simulation** (ré-échantillonnage par grappes ; branchements multiples depuis un même préfixe pour estimer une probabilité rare) | Le simulateur reproduit la dépendance réelle. Pour le branchement, les continuations sont de vrais tirages du nul. | Couverture réalisée contre couverture nominale sur le terrain de substitution. | Simulateur trop optimiste : mauvaise calibration avec bonne apparence. |
| **Transfert** (nul ou neurones appris ailleurs) | Rapport de densités estimable entre source et cible (version pondérée du conforme), ou invariance de la représentation. | Taux A/A sur la cible, sans retouche. | Le décalage porte précisément sur la queue. |

**Références.**
- Pour le conforme : Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World* (2005).
- Pour les tests séquentiels : Wald, « Sequential Tests of Statistical Hypotheses » (1945).
- Pour les e-valeurs : Ramdas, Grünwald, Vovk, Shafer, « Game-Theoretic Statistics and Safe Anytime-Valid Inference » (2023) ; identifiant non donné de mémoire, à vérifier.
- Pour la conversion de p-valeurs en e-valeurs et la version pondérée du conforme : références à vérifier.

## 4. Ce qui permettrait un contrôle extérieur au programme

Proposition.

- **Réplication d'entrée sur données publiques.** On refait, sur un modèle ouvert des faits, le test causal de la Table 2 : chute sous ablation des neurones de valeur contre neurones aléatoires. Si le pipeline ne retrouve pas l'écart rapporté, tout usage du papier s'arrête là. La disponibilité du code des auteurs est à vérifier.
- **Vérité plantée à deux niveaux.**
  - (i) Signal synthétique d'amplitude connue ajouté aux activations d'épisodes honnêtes : il mesure la courbe de puissance de la machinerie, indépendamment de la réalité du sabotage.
  - (ii) Sabotages produits par une équipe distincte de celle des sondes, avec un dégât confirmé par vérification mécanique (ré-exécution) faite par des personnes qui ne voient pas les scores.
- **Séquestre.** Un tiers détient un lot d'épisodes honnêtes jamais ouvert et les étiquettes ; le plan d'analyse est déposé avec empreinte avant ouverture.
- **Test A/A publié** à côté de chaque résultat, et contrôles M1–M4 systématiques.
- **Mesure indépendante.** Un moniteur texte seul et une relecture humaine à l'aveugle sur les mêmes épisodes. Si la sonde ne fait pas mieux qu'eux à budget égal, l'accès aux activations n'a rien apporté.
- **Seconde famille de modèles** parmi celles des faits (Qwen, Phi, Llama, Gemma), avant toute généralisation.

## 5. La demande reformulée

> « Étant donné N épisodes honnêtes vierges répartis en T tâches, quel est le plus petit taux de fausses alertes par épisode α\* certifiable à confiance 1−δ sous échangeabilité au niveau de la tâche ? Quelle détection du sabotage à dégât confirmé, contre l'échec honnête de la même variante, obtient-on à α\* et à budget d'audit fixé, au-dessus des contrôles M1–M4 ? Un nul construit au pas par le jumeau tient-il 1 % sans nouveau lot ? Sinon, combien d'épisodes un plan séquentiel préenregistré achète-t-il avant de s'arrêter ? Chaque réponse est accompagnée d'un test A/A, d'une courbe de puissance sur signal planté et d'une vérification sur lot séquestré. »

## 6. Propositions concrètes

Toutes sont des propositions (HYPOTHÈSE) tant que non testées.

### Tenir 1 %, ou s'en passer honnêtement

**P1 — Score normalisé, mise en commun, seuil conforme calibré par tâche.**
- Coût : aucun épisode nouveau ; il faut des épisodes vierges.
- Suppose : l'échangeabilité après normalisation par longueur et difficulté.
- Échec : hétérogénéité résiduelle par strate (duel D1) ; seuil instable près du maximum.

**P2 — Nul au pas par le jumeau, puis e-processus.**
- Principe : à chaque pas surveillé, le jumeau honnête tire m continuations depuis le même préfixe. Le rang du score de l'agent parmi ces m scores est une p-valeur valide sous le nul (agent honnête : échangeable avec ses jumeaux, par construction). Les p-valeurs sont converties en e-valeurs et multipliées. L'alarme sonne à 100.
- Coût : environ m générations supplémentaires par pas surveillé ; zéro épisode honnête nouveau.
- Suppose : même modèle, même contexte, hasard indépendant ; sorties d'outils rejouables.
- Échec : non-déterminisme ; puissance insuffisante.
- Piège à éviter : comparer les activations de l'agent et du jumeau sur les mêmes jetons. Sous le nul l'écart est identiquement nul, et sous l'alternative on détecte la consigne cachée, pas l'intention.

**P3 — Certifier α\* au lieu de 1 %.**
- Principe : rapporter le taux que les données permettent de certifier (borne exacte), la détection à ce taux et la courbe complète avec bandes, à la place de « non concluant ».
- Coût : nul.
- Suppose : des épisodes vierges.
- Échec : α\* trop lâche pour être utile. C'est une information, pas un défaut.

**P4 — Budget d'audit au lieu d'un taux.**
- Principe : auditer les k épisodes de plus forte preuve par fenêtre. Les audits d'épisodes honnêtes alimentent la calibration au fil de l'eau.
- Coût : le budget humain déjà prévu.
- Suppose : le budget est la vraie contrainte ; les audits établissent l'honnêteté.
- Échec : un saboteur qui reste sous le k-ième rang ; il faut compléter par des audits aléatoires.

**P5 — Test au niveau de l'agent.**
- Principe : produit d'e-valeurs d'épisode, alarme au niveau du déploiement.
- Coût : nul.
- Suppose : sabotage répété ; nul stable dans le temps.
- Échec : dérive honnête (nouvelles tâches) prise pour de la preuve ; sabotage concentré sur un seul épisode.

**P6 — Achat séquentiel.**
- Principe : si un lot est acheté, test séquentiel sur les dépassements avec règle d'arrêt préenregistrée, alloué d'abord aux strates d'échec honnête.
- Coût : variable, borné à l'avance.
- Suppose : des strates correctes.
- Échec : arrêt tardif si le taux vrai est proche de 1 %.

**P7 — Extrapolation de queue.**
- Usage : en analyse secondaire seulement, jamais comme certificat.
- Coût : nul.
- Suppose : la forme de la queue.
- Échec : voir tableau.

### Se servir du papier au-delà d'une ligne de base

**U1 — Avance temporelle de la chute de valeur.**
- Conjecture : ce qui distingue le saboteur de l'échec honnête n'est pas le niveau d'échec attendu (hypothèse du programme : la sonde lit l'échec), mais le moment où la valeur chute. Elle chuterait avant toute trace observable chez celui qui sait, après chez celui qui se trompe.
- Coût : lecture des neurones de valeur et de « dopamine » le long d'épisodes existants.
- Suppose : la valeur interne suit le succès de la tâche et non celui du but caché ; U2 est positif.
- Échec : signe inversé ; agent qui masque. Le test de masquage à capacité constante est clos pour l'instant, donc le résultat ne vaudra que pour un agent non entraîné contre la sonde.

**U2 — Transfert préalable.**
- Principe : vérifier que les neurones sélectionnés sur tâches vérifiables prédisent le succès aux jalons d'épisodes de recherche honnêtes.
- Coût : faible.
- Suppose : des jalons à verdict mécanique.
- Échec : limite (1) des auteurs confirmée ; le papier reste alors une covariable.

**U3 — Routage et allocation par la valeur avant génération.**
- Principe : stratifier la calibration et répartir le budget d'audit selon la difficulté prédite, pour que les tâches difficiles n'absorbent pas toutes les alertes.
- Coût : une passe avant.
- Suppose : U2.
- Échec : AUC seulement « modérée » (0,67, RAPPORTÉ), gain possiblement nul devant M1.

**U4 — Ablation comme générateur d'échecs honnêtes dosés.**
- Principe : ablater une fraction des neurones de valeur pour produire des échecs sans intention sur la même variante. Fait RAPPORTÉ : la précision passe de 75,2 % à 20,3 %.
- Coût : des épisodes, mais ciblés.
- Suppose : l'échec par ablation ressemble à l'échec naturel.
- Échec, connu d'avance : l'ablation supprime aussi la capacité des neurones de dopamine en aval (RAPPORTÉ, p. 5). Ces épisodes ne peuvent donc pas servir de nul pour une sonde lue en aval. Usage limité aux moniteurs de comportement et aux contrôles M2.

**U5 — Neurones de dopamine comme modèle de récompense de processus dans un protocole de rééchantillonnage.**
- Fait RAPPORTÉ : 77,8 % contre 72,2 %, sous-ensemble de validation, trois graines.
- Coût : quatre tirages par pas.
- Suppose : un agent honnête.
- Échec : circularité face à un agent adverse, dont le signal interne peut récompenser le sabotage. Je le propose uniquement comme gain d'utilité côté honnête, pas comme mesure de sûreté.

---

## (b) Expériences décisives

Les seuils chiffrés sont à préenregistrer ; ceux donnés ici sont illustratifs.

**D1 — La mise en commun tient-elle ?**
- H_A : après normalisation et calibration par tâche, le taux réalisé sur tâches nouvelles est ≤ 1 % dans chaque strate de longueur.
- H_B : au moins une strate dépasse.
- Terrain : substitution (grand N honnête), en tirant de façon répétée des sous-échantillons de la taille réelle du programme ; puis validation par tâches exclues sur les épisodes réels.
- Métrique : fraction des tirages dont le taux réalisé par strate dépasse 1 %, comparée au δ nominal.
- Contrôle négatif : scores synthétiques indépendants (la procédure doit rendre le nominal) et sonde sur neurones aléatoires (M4).
- H_A observé réfute la nécessité des « 5 000 par tranche » pour la validité.
- H_B observé réfute P1 et impose strates plus P3, ou un achat P6.
- Limite : le terrain de substitution peut réfuter la procédure, pas la valider pour le programme.

**D2 — Le nul par jumeau tient-il 1 % sans lot nouveau ?**
- H_A : en A/A sur les épisodes honnêtes existants, la fraction franchissant 100 a une borne supérieure exacte compatible avec ≤ 1 %.
- H_B : elle est > 1 %.
- Métrique : taux de franchissement avec intervalle binomial exact ; en parallèle, détection sur signal planté d'amplitude connue.
- Contrôle négatif : agent et jumeau avec graines identiques (le processus doit rester à 1) ; score de sonde remplacé par M4.
- H_A observé réfute « sans nouveau lot, pas de 1 % ».
- H_B observé réfute P2 et localise la rupture (outils, numérique).
- Second volet, condition d'usage et non duel : si la détection sur signal planté n'excède pas celle de M1–M3 passés par le même processus, P2 est valide mais inutile, et on l'écrit.

**D3 — Savoir ou se tromper (U1).**
- H_A : la sonde lit l'échec attendu sans plus. Le délai entre chute de valeur et première trace observable du dégât ne diffère pas entre sabotage confirmé et échec honnête apparié.
- H_B : la chute précède la trace de plus loin chez le saboteur.
- Métrique : différence appariée de délai (en pas), test de permutation par variante.
- Seuil : intervalle excluant zéro, et effet supérieur à celui du lecteur.
- Contrôle négatif : même analyse sur les neurones M4, et sur un jumeau lecteur du même transcrit. Si le lecteur montre la même avance, le signal est dans le texte et l'accès interne n'ajoute rien.
- H_A observé réfute U1 et renforce l'hypothèse du programme.
- H_B observé réfute « la sonde ne lit que l'échec », pour un agent non entraîné à masquer seulement.

**D4 — Transfert (U2).**
- H_A : les neurones sélectionnés par la procédure du papier sur tâches vérifiables prédisent le succès aux jalons d'épisodes de recherche honnêtes au-dessus de M1 et M4, d'une marge préenregistrée.
- H_B : non.
- Métrique : AUC par jalon, validation par tâches exclues.
- Contrôle négatif : étiquettes de jalon permutées.
- H_A observé réfute la limite (1) comme obstacle, en régime honnête.
- H_B observé réfute U1, U3 et U5 d'un coup.

Ordre conseillé : D4, D1, D2, D3. D4 et D1 coûtent peu et peuvent fermer des branches entières.

---

## (d) Ancrage matériel

- **Modèles ouverts** (tous cités dans les faits) : Qwen-2.5-7B-SimpleRL-Zoo pour répliquer la Table 2 ; Llama-3.1-8B-Instruct ou Phi-3.5-mini-instruct comme seconde famille.
- **Calcul.** Un modèle de 7 à 8 milliards de paramètres tient sur un seul processeur graphique de 24 Go en demi-précision (illustratif). Les sondes du papier sont petites (perceptron à deux couches, largeur 1024 ou 32, RAPPORTÉ) ; leur entraînement est négligeable devant la génération.
- **Coûts.** Le coût C d'un épisode d'agent n'est pas dans les faits ; je raisonne donc en unités de C.

| Expérience | Coût | Statut du chiffre |
|---|---|---|
| D4 et D3 | Relecture d'épisodes existants, passes avant seules : une petite fraction de C par épisode | illustratif |
| D1 | Quelques jours d'un processeur graphique pour des dizaines de milliers d'épisodes courts vérifiables | illustratif, à mesurer sur un pilote |
| D2 | Environ m fois le coût de génération des pas surveillés, sans exécution d'outils si les sorties sont rejouées ; avec m de l'ordre de 4 à 8 et un pas surveillé sur quelques-uns, de l'ordre d'un à quelques C par épisode | illustratif |
| P6 | Borné par la règle d'arrêt ; à chiffrer une fois C connu | — |

- **Ce qui manque pour chiffrer honnêtement** : C, le nombre de tâches distinctes, le nombre de pas par épisode, et la liste de ce qui a déjà été ajusté sur les épisodes existants. Je demande ces quatre données à l'arbitre avant tout engagement de budget.

FIN-DE-CELLULE
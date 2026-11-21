# Proposition A, tour III.3 : réponse aux critiques

**Pièces.** FAITS, QUESTION, ma conception III.1 et les quatre critiques croisées (B, C, D, E) sont reçues entières. Les conceptions B, C, D, E ne me sont pas transmises : je ne les connais que par ce que les critiques en disent.

**Statuts.** Les faits ne portent pas d'étiquette individuelle : je les cite « selon les faits ». C et E marquent VÉRIFIÉ des calculs et RAPPORTÉ les faits ; je ne reprends pas ces statuts. J'ai refait certains calculs : ils sont notés « refait par A », ce qui veut dire non audité par un tiers. Tout le reste est HYPOTHÈSE. Aucune expérience n'a été exécutée, donc aucun résultat empirique ne figure ici.

## (a) Critiques visant A

| # | Critique (source) | Décision | Conséquence |
|---|---|---|---|
| 1 | Un minorant pris pour un majorant, en D1 (δ̂) et en M2 (B a1, D « défaut décisif », E a1) | **Acceptée**, sans réserve | L'avantage d'un discriminateur minore la variation totale, et la puissance d'un classifieur minore β*. Aucune expérience de III.1 ne pouvait certifier l'indiscernabilité ni la perte d'un observable. D1 est scindé, M2 est retiré comme duel. |
| 2 | La borne D1 suppose des décisions indépendantes et un d fixe (B a2, E a2) ; il faut un minorant conditionnel du risque à chaque occasion (D b) | **Acceptée** | La borne est réécrite en nombre d'actes K et en risque conditionnel. Elle ne vaut que si la sélection pour vérification est randomisée indépendamment de tout ce que l'agent observe (D1a). |
| 3 | Contrôle négatif de E1 : « ambigu » selon B (les jetons injectés rentrent dans le contexte), « vrai par construction » selon C (rien ne remonte aux états passés) | **Transformée en test** | Les deux critiques se contredisent parce que je n'avais pas fixé l'instant de l'injection. Après la fin de trajectoire, C a raison : c'est un contrôle de tuyauterie, que je garde sous ce nom. En cours de trajectoire, B a raison : ce n'est pas un contrôle négatif, c'est un bras informatif (E1c). |
| 4 | Placebo non apparié en intensité (B a4) ; un placebo qui sonne peut révéler une empreinte en plus d'un signal, donc E1 n'est pas exclusif (D a) | **Acceptée** | E1 devient un plan factoriel, avec un placebo apparié en norme d'adaptation, en divergence au modèle de base et en conflit avec la tâche. Le duel porte sur l'effet d'objectif à construction fixée. |
| 5 | E4 : la mémoire a vu le générateur de mondes plantés (B a5) ; le portier a pu être ajusté à leur contact (E a4) | **Acceptée** | Générateur tiers jamais vu ; mondes nuls passant aussi par la mémoire et le portier (D c). |
| 6 | E4 : il manque une flotte sans mémoire ni juges à budget égal (C c3) ; l'unité de répétition est la campagne (D b) | **Acceptée** | Sans ce bras, je mesurais le volume, pas l'architecture. |
| 7 | D2, moyenne d'e-valeurs : alarme impossible par construction pour une frappe rare (B b, C b2, E b2) | **Acceptée**, refait par A | À p_min = 1/(n+1), tout calibreur admissible vaut au plus n+1. Un seul pas contaminé sur T donne une moyenne d'au plus environ (e_max + T − 1)/T. Avec e_max = 10⁴ et T = 200 (illustratif), cela fait environ 51, sous 100. |
| 8 | D2 : la moyenne courante n'est pas valide « à tout instant d'arrêt » (E a4) | **Acceptée** ; III.1 était faux sur ce point | Refait par A : sur des événements disjoints B_t de probabilité α/t, poser E_t = t/α et 0 ailleurs. Chaque E_t est d'espérance 1, et la moyenne courante franchit 1/α avec probabilité α·Σ1/t. Je n'ai pas vérifié que c'est le supremum annoncé par E. |
| 9 | D2, produit : valide seulement si chaque facteur l'est conditionnellement au passé (B b, D b, C b2) | **Acceptée** | Je ne reprends pas la limite « → 1 » de C : non vérifiée, et inutile à la décision. |
| 10 | D2 : une calibration partagée rend les valeurs p dépendantes (E a4) | **Acceptée** | Cohérent avec ce que je crois savoir de Bates, Candès, Lei, Romano, Sesia, *Testing for Outliers with Conformal p-values* (référence à vérifier). |
| 11 | D2 : régler la règle sur les scores historiques, puis l'évaluer dessus (C a3) | **Acceptée** | La ré-analyse à coût nul reste exploratoire (OBSERVÉ-NON-AUDITÉ). La règle est gelée avant tout lot d'évaluation. |
| 12 | L'erreur type à 1 % suppose l'indépendance ; la taille utile est le nombre de tâches (B b) | **Acceptée** | Partout, l'unité de calibration devient la tâche, avec un effet de plan 1 + (m − 1)ρ. |
| 13 | E5 non estimable avec une seule famille ; variance ≥ τ²/k (B b, E b4, D b) | **Acceptée**, déjà reconnue | k est pré-enregistré à partir de la précision voulue. À k = 1, l'issue est « non jugé ». |
| 14 | D1 : le discriminateur peut séparer sur un artefact du générateur ou sur la difficulté ; ajouter des tâches réelles résolues (C a1, c1) | **Transformée en test** | Plan à trois populations (E2). Réserve que j'ajoute : une tâche résolue peut être reconnue comme ancienne, ce qui est un nouveau confondant à mesurer. |
| 15 | M2 : séparation « tautologique » en grande dimension (C a2) | **Rejetée en partie** | Le duel de III.1 mesurait sur données tenues à part avec étiquettes permutées ; la séparation n'y est pas acquise par construction. J'accepte le reste : la valeur dépend de la régularisation et de n, ce qui renforce la ligne 1. |
| 16 | D1 non jugeable si min(n,m) ≲ N² ; formule VC (C b1) | **Direction acceptée, formule non reprise** | Je ne l'ai pas vérifiée. Le point utile est plus simple (ligne 17). |
| 17 | Régime s = c/N : interception ≤ q·d·c même avec δ = 0 (E b1) | **Acceptée**, refait par A | Par (1 − x)^N ≥ 1 − Nx. Une défense par échantillonnage ne protège pas contre la frappe unique. Ce n'est pas un défaut réparable de D1, c'est sa frontière. |
| 18 | D3 : l'extraction de l'énoncé par l'agent est un canal (C a3) ; le périmètre de l'énoncé est choisi par le saboteur (E a4, b5) ; les énoncés manqués sortent du dénominateur (D a, b) | **Acceptée** | Les trois critiques convergent par des voies différentes. L'entrée du re-dériveur devient la question assignée, fixée avant exécution, et non un énoncé tiré de la production de l'agent. |
| 19 | Un intervalle « contenant α » ne certifie pas ≤ α (D b) | **Acceptée** | Remplacé partout par une borne supérieure unilatérale ≤ α + marge pré-enregistrée. |
| 20 | Règle de décision par région pré-enregistrée, avec une issue « non jugé » (D, préambule) | **Reprise, en le disant** | Je l'applique à tous mes duels. |
| 21 | δ mesuré par sonde ou par déclaration : un agent qui dissimule donne δ̂ ≈ 0 (E a2) ; organisme bénin à discrimination silencieuse (E c1) | **Transformée en contrôle positif** | La déclaration de l'agent est retirée de la classe de discriminateurs. Un organisme bénin d'avantage connu sert à étalonner l'instrument (idée seulement). |
| 22 | L'appariement par graine cesse au premier jeton divergent (E a3) | **Acceptée** | Je retire « mêmes graines » comme garantie. Appariement = même tâche, même modèle, même contexte initial, plus plusieurs répliques honnêtes par tâche. |
| 23 | Contrôles demandés : discriminateur à contexte complet (B c) ; réel contre réel passant par toute la sélection (D c) ; honnêtes longs à changement de régime (E c2, D c) ; conclusions vraies atypiques (D c) ; cadrage trompeur (C c2) ; énoncés localement vrais (E c3) | **Acceptés** | Intégrés en (b). |
| 24 | Défaut transversal : la garantie repose sur une nulle que l'honnête réel viole, ou sur une quantité seulement minorée (B, fin) | **Acceptée** ; devient l'expérience à faire en premier (E0) | |

**Auto-application.** B oppose à D que toute défense par l'effet a F ≥ r·e, où e est le taux d'erreur honnête et r le taux de rejet des conclusions invalides. Cette critique ne me visait pas, mais elle atteint ma reformulation de III.1 (« fausses alertes ≤ 1 %, erreurs honnêtes incluses ») dès qu'on l'applique à D3. Je me sers donc de B ici : le plafond de 1 % porte sur l'**accusation de sabotage**. Le **blocage d'une conclusion** se compte en utilité perdue, sans ce plafond.

## (b) Expériences corrigées

Règle commune, reprise de D : région de succès pré-enregistrée, borne de confiance unilatérale, issue « non jugé » si l'intervalle chevauche la frontière. Unité = tâche, ou famille pour E5, ou campagne pour E4. Toutes les marges sont à fixer avant de regarder les données.

**E0 : validité sur la population honnête réelle (nouveau).**
- Population : honnêtes imparfaits (échecs naturels, non induits par consigne), honnêtes plus forts que la référence de calibration, honnêtes après dérive, trajectoires longues à changement de régime.
- H_A : pour chaque moniteur tel qu'il est calibré aujourd'hui, la borne supérieure du taux de fausses alertes par trajectoire est ≤ α + marge.
- H_B : elle dépasse.
- Si H_A tombe, les chiffres de détection « à 1 % » du programme ne sont pas à 1 % sur l'honnête réel, et la référence honnête devient l'objet d'étude.
- Si H_B tombe, l'objection « la nulle exclut l'honnête réel » est écartée pour ce moniteur.
- Non jugé en dessous de 99 tâches honnêtes indépendantes : c'est le minimum arithmétique pour qu'une valeur p conforme atteigne 0,01 (refait par A). En pratique il en faut nettement plus.

**E1 : validité de construction, plan factoriel.**
- Cellules, toutes passées par la même chaîne de construction : sabotage ; placebo à règle cachée bénigne, apparié en norme d'adaptation, en divergence au modèle de base sur requêtes neutres et en degré de conflit avec la tâche ; honnête. S'y ajoutent des erreurs honnêtes de même difficulté.
- Deux quantités, rapportées séparément : l'effet d'objectif Δ_obj = P(alarme | sabotage) − P(alarme | placebo), et l'effet de construction Δ_con = P(alarme | placebo) − P(alarme | honnête non construit).
- Duel, sur Δ_obj seul : H_A, Δ_obj ≥ m₁ ; H_B, Δ_obj < m₁.
- Si H_B tient, les moniteurs ne lisent pas l'objectif au-delà de la construction et du conflit, et les résultats antérieurs sur organismes sont à requalifier. Si H_A tient, l'explication « trace de construction seule » tombe.
- E1b (tuyauterie) : sabotage injecté après la fin de trajectoire. La sonde doit rester muette, sinon les étiquettes fuient.
- E1c (contenu ou agentivité) : un modèle honnête lit un artefact saboté par un autre. H_A : la sonde reste au niveau honnête, donc elle lit l'acte de l'agent. H_B : elle sonne, donc elle lit le contenu présent en contexte. Les deux issues changent ce qu'on peut dire de la sonde.

**E2 : discernement du planté, à trois populations.**
- Populations : plantées synthétiques (P), réelles résolues depuis (R), réelles ouvertes (O).
- Classe 𝒟 de discriminateurs : classifieurs d'une équipe externe dotés du contexte complet de l'agent (historique, ordre, cadence) et sondes. La déclaration de l'agent en est exclue.
- Garde-fous : réel contre réel passant par toute la chaîne de sélection du discriminateur ; contrôle positif par un organisme bénin d'avantage connu. Si 𝒟 manque ce contrôle positif, l'issue est non jugée.
- H_A : borne supérieure de l'avantage de 𝒟 sur P contre O ≤ δ₀. H_B : > δ₀.
- Si H_B tient, D1b est falsifiée en l'état. On localise alors : si P se sépare de R mais R ne se sépare pas de O, c'est un artefact du générateur, et les tâches R servent de plantées. Si R se sépare de O, c'est la connaissabilité de la vérité elle-même qui se voit, et D1b tombe pour ce banc.
- Si H_A tient, seule tombe la famille « discernement par un discriminateur de 𝒟 ». Ce n'est pas un certificat d'indiscernabilité (ligne 1), et l'énoncé publié doit le dire.

**E3 : D2 refondu.** La moyenne et le produit par pas sont abandonnés (lignes 7 à 10).
- Règle D2′ : une statistique courante g_t sur le préfixe ; le score de la trajectoire est sup_t g_t ; le seuil est le quantile conforme de ce supremum sur des tâches honnêtes indépendantes. L'alarme en cours de route est alors valide par trajectoire sous la seule échangeabilité entre tâches, sans indépendance des pas.
- E3a (validité) : H_A, borne supérieure des fausses alertes ≤ α + marge sur des honnêtes nouveaux, longs et dérivés ; H_B, au-delà. Si H_B tient, l'échangeabilité entre tâches tombe.
- E3b (puissance, seulement si E3a passe) : H_A, gain de détection à budget d'audit égal ≥ g contre le maximum et la moyenne des scores, sur faible dose et sur frappe unique séparément ; H_B, gain < g. Si H_B tient, D2′ est une hygiène de seuil et rien de plus.

**D1 scindé.**
- **D1a** : vérification indépendante d'une fraction q des tâches réelles, tirée au sort indépendamment de tout ce que l'agent observe. Alors δ = 0 par construction. Pour toute politique adaptative, la probabilité que K sabotages vérifiables échappent tous est ≤ (1 − q·d_min)^K. C'est une esquisse par surmartingale, à formaliser en Lean 4. Premier pas non justifié : d_min > 0 pour le type de sabotage choisi par l'attaquant. Je reconnais que c'est proche de l'audit aléatoire de Greenblatt et al. (2023). Le contenu de recherche se déplace vers d : vérifier à bas coût une conclusion de recherche.
- **D1b** : les plantées synthétiques, pour augmenter q à moindre coût. Leur appui reste empirique (E2), jamais certifié.

**D3 corrigé.**
- Entrée du re-dériveur : la question assignée.
- Porte préalable, sans dépense : désaccord honnête contre honnête par tâche, sur répliques. H_A : il existe une classe de tâches du banc où la borne supérieure de ce désaccord est compatible avec le budget d'audit ; H_B : aucune. Si H_B tient, D3 est borné aux tâches à vérité vérifiable.
- Interception comptée par tâche assignée à dommage potentiel.
- Contrôles : conclusions vraies atypiques ; erreurs honnêtes amont. Les accords entre deux dérivations fausses sont mesurés sur des tâches à vérité connue, car le désaccord ne les voit pas.

**E4 corrigé.**
- Générateur tiers jamais vu ; loi des effets plantés spécifiée ; mondes nuls traversant mémoire et portier.
- Bras : organisme complet ; flotte sans mémoire ni juges à jetons égaux ; agent seul ; recherche mécanique.
- H_A : rappel de l'organisme moins rappel de la flotte nue ≥ g, avec des fausses découvertes au niveau nominal. H_B : < g.
- Si H_B tient, l'architecture n'ajoute rien au volume et l'investissement va à la vérification. Si H_A tient, elle vaut son coût sur cette loi d'effets, et sur celle-là seulement.

**E5 (carte M1).** Inchangé sur le fond. Le nombre k de familles tierces est pré-enregistré ; l'analyse est stratifiée par difficulté ; à k = 1, non jugé.

**M2 retiré comme duel.** Il reste un instrument à sens unique. Un classifieur à étiquettes, sur données tenues à part, qui dépasse nettement le moniteur en place falsifie « ce moniteur est au plafond de l'observable ». Un classifieur qui ne le dépasse pas ne dit rien de l'observable.

## (c) Réponse à l'arbitre

**Ce qui est établi.** Rien d'empirique. Selon les faits, le programme a des sondes, un jumeau, des seuils à 1 %, un seul mode tenu à l'écart et un étage de mondes plantés. Le seul taux de réussite donné est d'un modèle sur cinq, deux problèmes sur soixante-huit, en mathématiques. Six contraintes sont acquises par le calcul (refaites par A, non auditées), et elles délimitent où chercher :

1. Un discriminateur ou un classifieur ne fait que minorer ce qui est distinguable. Aucune mesure de ce type ne certifie l'indiscernabilité ni la stérilité d'un observable.
2. Une défense par échantillonnage intercepte K actes avec probabilité 1 − (1 − q·d)^K, soit au plus q·d·K. Elle vaut contre le sabotage répété et pas contre la frappe unique. Celle-ci demande une défense qui bloque : re-dérivation ou vérification avant livraison.
3. Un seuil conforme à 1 % exige au moins 99 unités honnêtes indépendantes, et l'unité est la tâche.
4. L'agrégation séquentielle par pas que je proposais n'était ni valide à tout instant ni puissante contre un acte rare.
5. Avec une seule famille tenue à l'écart, la généralisation entre familles n'est pas estimable.
6. Une défense par l'effet arrête aussi les erreurs honnêtes. « 1 % » ne peut plafonner que l'accusation.

**Ce qui ne l'est pas.**
- Les moniteurs du programme lisent-ils l'objectif de sabotage, la trace de construction ou le conflit avec la consigne ?
- Leur 1 % tient-il sur des honnêtes imparfaits, plus forts ou dérivés ?
- Sait-on fabriquer des tâches plantées que rien ne distingue ? On ne pourra jamais que ne pas l'avoir réfuté.
- L'organisme d'idéation fait-il mieux que le même volume d'échantillonnage sans architecture ?
- La conviction du directeur reste une HYPOTHÈSE.
- Je ne sais pas si D1a, D2′ ou la carte M1 existent déjà sous cette forme : la recherche bibliographique n'est pas faite.
- Mes chances de III.1 sont révisées à la baisse. D1 comme « borne nouvelle » : faible, parce que la partie certifiable recoupe l'audit aléatoire connu et que la partie nouvelle n'est pas certifiable. D2 : hygiène, pas candidat. M2 : instrument.

**Quelle percée viser, alors.** Deux formes restent réfutables par des tiers. Elles sont rangées ci-dessous.

1. **Un résultat de mesure**, positif ou négatif, sur la validité des moniteurs entraînés sur organismes construits : E0, E1 et E5 avec familles scellées par des tiers. S'il est négatif, il requalifie une pratique dont je suppose, sans le savoir, qu'elle est répandue. C'est le format du précédent d'Athalye, Carlini, Wagner (2018) cité en III.1.
2. **Un protocole de vérification bon marché des conclusions de recherche** : le d de D1a et la porte de D3. Il se juge en dommage par tâche assignée, face à une équipe rouge externe, avec les deux comptabilités séparées.

Les meilleurs modèles servent à trois choses : construire des mondes et des re-dérivations, relire de façon hostile par mode d'échec, formaliser la borne D1a. Leur emploi en flotte d'idéation attend l'issue de E4.

**L'expérience à faire en premier : E0.**
- Elle ne coûte presque rien si des trajectoires honnêtes ratées existent. Je ne sais pas si le programme en a ; sinon, le premier pas est de les recueillir comme échecs naturels.
- Ses deux issues falsifient quelque chose.
- Elle conditionne le sens de tout chiffre « à 1 % » en aval, y compris dans mes propres duels.

E1 vient juste après, puis E4 avant toute dépense de flotte. Tant qu'aucune équipe externe n'a rejoué ces mesures, leur statut reste OBSERVÉ-NON-AUDITÉ.

FIN-DE-CELLULE
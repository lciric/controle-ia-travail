# Proposition D — Tour III.1

**Conventions.** Je ne vérifie rien de nouveau ici. **RAPPORTÉ** désigne une affirmation transmise dans le lot ; **OBSERVÉ-NON-AUDITÉ**, une lecture web ou de résumé sans PDF scellé ; **HYPOTHÈSE**, une proposition à tester. Tous les seuils chiffrés et tous les budgets introduits ci-dessous sont **illustratifs**. Les expériences proposées sont des **HYPOTHÈSES de méthode**, pas des résultats.

Trois attaques utiles avant le plan : les métriques d’Argon — résistance effective, arbres d’équations, \(R_0\), \(\sigma=1\) — sont des candidates, non des instruments validés. Je reprends la sur-additivité proposée par Fable indépendant-Q3, mais seulement à procédé, budget et juge fixés. Enfin, je retiens la critique RL4 : une transition ne doit pas être cherchée dans la sigmoïde d’un modèle appris, mais dans les taux empiriques et leur changement d’échelle.

## (a) Ce que la question suppose sans l’établir

| Point supposé | Statut | Ce qui reste à démontrer |
|---|---|---|
| Des chapelles stables existent et une partition apprise les retrouve mieux qu’un découpage en domaines. | HYPOTHÈSE | Stabilité sous rééchantillonnage, accord avec des codages externes, valeur prédictive additionnelle. |
| « Distance de contenu », « capacité du canal » et « flux observé » sont trois objets séparables. | HYPOTHÈSE | Un flux faible peut venir d’une incompatibilité réelle, d’une taille inégale ou d’une simple absence d’occasion ; il ne suffit pas à identifier un trou. |
| Une compatibilité formelle ou pratique est extractible avant le pont et prédit sa fécondité. | HYPOTHÈSE | Les équations normalisées, pratiques et instruments doivent battre des mesures lexicales simples, sans utiliser le vocabulaire du pont futur. |
| La fertilité est une propriété estimable d’une paire. | HYPOTHÈSE | Elle peut dépendre du procédé, du budget, du juge, du temps et du porteur ; les paires jamais contactées sont hors du support des paires observées. |
| Citations, reprise ou survie aux tests de mort mesurent la même fertilité. | HYPOTHÈSE | Ces issues ont des causes distinctes : visibilité, prestige, mode, biais du juge et véritable réutilisation. |
| Des témoins « jamais rencontrés » sont de vrais négatifs et la coupure temporelle supprime les fuites. | HYPOTHÈSE | Certains témoins sont de futurs ponts ; concepts OpenAlex, intentions de citation et plongements peuvent avoir été produits après la coupure. |
| La fertilité présente une transition de phase, et non seulement une cloche, une monotone ou une non-linéarité lisse. | HYPOTHÈSE | Il faut paramètre de contrôle, paramètre d’ordre, analyse de taille finie et modèles nuls non critiques. |
| Un modèle peut apprendre une fertilité au-delà de la popularité, puis être réutilisé dans le bisociateur. | HYPOTHÈSE | Prédire un lien futur n’est pas prédire un lien fertile ; il faut battre degré, âge, croissance et fermeture triadique. |
| Gu et Krenn 2024, *Forecasting high-impact research topics via machine learning on evolving knowledge graphs*, fournissent une base transférable ; leur AUC rapportée supérieure à 0,9 serait déjà un étalon. | OBSERVÉ-NON-AUDITÉ pour les lectures de résumé et chiffres ; HYPOTHÈSE pour le transfert | Reproduction sur PDF, code et données ; puis test sur niches, témoins durs et liens réellement fertiles. |
| L’apprentissage profond peut, à lui seul, distinguer paramètres créateurs et accompagnateurs. | HYPOTHÈSE, et forte présomption méthodologique contraire RAPPORTÉE dans les relectures | Sans intervention, variation exogène ou hypothèses d’invariance défendues, il estime des associations. |
| Un effet causal mesuré dans nos courses se transporte à la science humaine. | HYPOTHÈSE | Nos agents n’ont ni carrière, ni financement, ni prestige ; la transportabilité doit être testée séparément. |
| Les événements OpenAI de septembre-octobre 2026 établissent la supériorité d’un régime pour générer des idées. | RAPPORTÉ pour les annonces ; OBSERVÉ-NON-AUDITÉ pour leur architecture et leurs compteurs | Les deux cas rapportés concernent des problèmes déjà posés ; aucune comparaison publique à budget égal ne tranche la génération de questions. |
| Les juges figés et tests de mort sont neutres vis-à-vis de la nouveauté. | HYPOTHÈSE | Ils peuvent pénaliser la distance, récompenser une bisociation spécieuse ou accepter un énoncé formel différent de l’énoncé initial. |
| Une revue « exhaustive » est possible. | HYPOTHÈSE à rejeter comme promesse | Seule une revue bornée, requêtes et exclusions journalisées, est auditable. |

## (b) Expériences décisives

### E1 — Profil « trou + compatibilité » contre distance seule

- **H_A** : le profil préenregistré « canal faible, compatibilité formelle/pratique forte » améliore la détection de ponts fertiles après coupure.
- **H_B** : il n’ajoute rien à la distance de domaine, à la topologie locale et à la popularité.
- **Métrique** : AUPRC et précision@K, K fixé par le budget du bisociateur ; seuil **illustratif** : gain relatif d’au moins 20 % sur la meilleure base, intervalle à 95 % excluant zéro.
- **Contrôle négatif** : popularité seule, étiquettes permutées, paires factices, témoins appariés en âge, taille, activité et distance textuelle.
- **Issues** : succès de H_A falsifie H_B ; absence de gain falsifie **cette implémentation** de H_A, pas toutes les définitions possibles de chapelle.

### E2 — Fertilité comme interaction, en monde inventé

- **H_A** : certaines paires produisent une sur-additivité de résultats vrais validés, inaccessible aux deux niches seules.
- **H_B** : à budget total égal, le croisement ne produit aucun excédent sur les composantes et le meilleur échantillonnage indépendant.
- **Métrique** : \(F=R(A\cup B)-R(A)-R(B)+R(A\cap B)\), puis \(\Pr(F\ge s)\), avec \(R\), \(s\), procédé et juge gelés ; seuil d’effet fixé après pilote, **illustratif**.
- **Contrôle négatif** : pseudo-croisement d’une niche avec sa copie anonymisée ; il doit donner \(F\approx0\). Vérité plantée et dénominateur complet des tentatives.
- **Issues** : aucun excédent falsifie H_A pour ces mondes ; un excédent reproduit falsifie H_B. Cela ne valide pas encore une fertilité bibliographique.

### E3 — Transition critique contre non-linéarité lisse

- **H_A** : en faisant varier la dose de contact, le taux empirique de cascades validées présente les propriétés d’une transition : raidissement avec la taille, effondrement des courbes après remise à l’échelle et pic de variance associé.
- **H_B** : une logistique, une cloche ou une monotone suffit, sans mise à l’échelle critique.
- **Métrique** : comparaison préenregistrée des formes, qualité de l’effondrement sur au moins trois tailles (**illustratif**), variance et taux de branchement ; seuil de décision bayésien **illustratif**.
- **Contrôle négatif** : mondes cloches non critiques, croissance préférentielle, urnes à nouveautés et processus auto-excités sous-critiques, capables de produire des queues lourdes sans transition.
- **Issues** : signatures critiques reproductibles et échec des formes lisses falsifient H_B ; meilleure forme lisse et absence d’effondrement à puissance suffisante falsifient H_A pour cet objet. Une loi de puissance seule ne tranche rien.

### E4 — Apprentissage de la fertilité contre apprentissage de la densité

- **H_A** : une partition et une fonction apprises prédisent des liens **fertiles** au-delà des référents triviaux.
- **H_B** : le gain disparaît avec des témoins durs et un contrôle de popularité.
- **Métrique** : précision@K sur paires distantes, AUPRC, calibration par fenêtre, délai jusqu’au pont et reprise ultérieure ; gain minimal **illustratif**.
- **Contrôle négatif** : degré-âge-croissance seuls, voisins communs, Adamic-Adar, attachement préférentiel, node2vec ; fuite testée avec des termes-canaris postérieurs à la coupure.
- **Issue préalable** : si Gu–Krenn n’est pas reproduit, sa réutilisation est falsifiée comme raccourci d’étalonnage. Ensuite, gain de H_A falsifie H_B ; disparition du gain falsifie H_A. Les voies « goulot + ablation » et « libre + régression symbolique » sont comparées sur le même partage, sans appeler causale une ablation observationnelle.

### E5 — Dose de contact : cause ou accompagnement

- **H_A** : manipuler la dose de contact modifie la survie aux tests de mort.
- **H_B** : l’association observationnelle disparaît sous randomisation ; elle reflétait la sélection.
- **Métrique** : courbe dose-réponse, effet à une dose jamais vue, intervalle de prédiction à 90 % (**illustratif**) ; comparaison à un modèle purement prédictif.
- **Contrôle négatif** : fertilité antérieure au traitement, date placebo, intervention préenregistrée sans effet attendu.
- **Issues** : effet randomisé reproduit falsifie H_B **dans nos courses** ; absence d’effet ou prédiction hors intervalle falsifie H_A pour la dose testée.

### E6 — Transport hors de nos courses

- **H_A** : les paramètres déclarés causaux prédisent signe et ordre de grandeur d’un choc indépendant, dans un environnement tenu à l’écart.
- **H_B** : ils ne valent que pour nos agents et nos juges.
- **Métrique** : erreur sur l’effet du choc, signe et calibration ; tolérance fixée avant lecture, **illustrative**.
- **Contrôle négatif** : issue antérieure au choc et environnement jumeau non exposé.
- **Issues** : prédiction correcte falsifie H_B pour cet environnement ; échec falsifie la transportabilité revendiquée, sans effacer l’effet interne E5.

### E7 — Essaim communicant contre échantillonnage

- **H_A** : à calcul égal, des îlots partiellement connectés produisent plus d’idées validées que le meilleur-de-N indépendant et qu’un agent long, avec excédent de provenance croisée.
- **H_B** : la communication n’apporte que du bruit partagé ou de la convergence ; l’échantillonnage indépendant suffit.
- **Métrique** : survivantes par coût, couverture des paires, diversité avant/après consolidation, taux de doublons et de faux nouveaux, origine croisée dans le graphe de provenance.
- **Contrôle négatif** : messages routés au hasard, communication supprimée, consolidateur supprimé, meilleur-de-N et agent unique à budget multiplié.
- **Issues** : avantage disparaissant sans communication falsifie H_B pour la tâche ; absence d’avantage sur les deux bases falsifie H_A. Les annonces OpenAI servent de gabarits d’ablation, non de preuves.

## (c) Mesure minimale de chaque instrument

Pour tous : fixer le point de fonctionnement avant le test ; publier **TD** (taux de détection) et **FA** (fausses alertes), avec intervalles, sur cas tenus à l’écart. Ni AUC seule, ni exemples célèbres.

| Instrument | TD / FA et cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|
| Partition en chapelles | TD sur schismes codés sans voir les scores ; FA sur réseaux nuls et sous-domaines qui communiquent bien ; appariement taille/âge/activité | Modèle nul à degrés conservés, domaines bibliographiques, Leiden/SBM à résolutions voisines ; stabilité bootstrap |
| Canal et trou | TD sur trous documentés postérieurement ; FA sur paires silencieuses mais incompatibles et sur flux simulés | Flux attendu sous graphe nul, plus court chemin, vocabulaire TF-IDF, popularité ; mesurer capacité et flux séparément |
| Proximité mathématique | TD sur transferts couverts par le corpus ; FA sur équations banales, variantes de notation et faux isomorphismes audités à l’aveugle | Symboles et n-grammes LaTeX, équations normalisées exactes, similarité textuelle ; l’arbre/GNN doit ajouter un gain |
| Fertilité ex post / ex ante | TD sur reprises tierces et cascades datées ; FA sur liens populaires non réutilisés, témoins contenant de futurs ponts | Taux de base par taille et âge, popularité seule, horizon et seuil de reprise gelés ; calibration |
| Test de transition | TD sur mondes synthétiques critiques ; FA sur cloches, sigmoïdes et queues lourdes non critiques | Modèles lisses, simulations nulles, taille finie ; aucune lecture depuis la fonction apprise |
| Hypergraphe et prédiction de liens | TD sur liens fertiles futurs ; FA sur négatifs historiques et liens denses sans reprise | Voisins communs, Adamic-Adar, attachement préférentiel, node2vec, Gu–Krenn reproduit ; concepts datés, pas d’étiquettes post-coupure |
| Goulot/ablation et régression symbolique | TD sur cause plantée ; FA sur variable corrélée par un confondeur et sur formule surajustée | Modèle linéaire/GBM sur traits nommés, degré seul, validation hors environnement, pénalité de complexité |
| Inférence causale | TD sur intervention et cause plantée ; FA sur placebo, issue pré-traitement et accompagnateur | Estimateur naïf prédictif, modèle sans structure causale, randomisation, sensibilité aux confondeurs |
| Régimes de génération | TD sur vérités croisées plantées ; FA sur doublons, redécouvertes et bisociations spécieuses | Meilleur-de-N, agent long, messages aléatoires, sans consolidation ; tous les essais comptés |
| Juges, tests de mort, lecteur distinct | TD sur artefacts plantés ; FA sur idée formellement acceptée mais fidèle ni à l’énoncé ni à la nouveauté | Vérificateurs formels lorsqu’ils existent, tests unitaires, recherche mécanique d’antériorité, audit humain externe à l’aveugle |
| Revue bibliographique | Rappel sur un jeu de références semences ; FA = attribution ou signe contredit sur PDF | Double codage d’un échantillon, requêtes et exclusions journalisées, statut par source ; jamais « exhaustif » sans borne |

## Vérification ponctuelle G

Un seuil d’auto-entretien de champ est **RAPPORTÉ**, mais le terme « ignition » n’est pas établi pour cet objet. À vérifier sur PDF : Bettencourt, Cintrón-Arias, Kaiser et Castillo-Chávez (2006), *The power of a good idea: Quantitative modeling of the spread of ideas from epidemiological models* ; Bettencourt, Kaiser, Kaur, Castillo-Chávez et Wojick (2008), *Population modeling of the emergence and development of scientific fields*. Les transitions topologiques relèvent d’un autre objet : Bettencourt, Kaiser et Kaur (2009), *Scientific discovery and topological transitions in collaboration networks* ; Bettencourt et Kaiser (2015), *Formation of Scientific Fields as a Universal Topological Transition* — cette dernière lecture est **OBSERVÉ-NON-AUDITÉ** dans le lot. L’« ignition » de Ham et collaborateurs (2007), *Spontaneous coordinated activity in cultured networks: Analysis of multiple ignition sites, primary circuits, and burst phase delay distributions*, est **RAPPORTÉE** pour des réseaux neuronaux, non pour des champs scientifiques. Conclusion permise : seuil épidémiologique et transition topologique à distinguer ; absence du vocabulaire « ignition » non démontrée.

## (d) Ancrage matériel — configurations et coûts **illustratifs**

| Étape | Modèles et calcul | Coût estimé |
|---|---|---|
| Pilote chapelles/trous, corpus restreint | Traitements CPU : graph-tool, Leiden, LaTeX/AST, TF-IDF, word2vec/node2vec entraînés sur le pré-coupure ; 32–64 cœurs, 256–512 Go RAM, 2–5 To SSD | 300–1 500 €, une à deux semaines |
| Apprentissage et interprétabilité | PyTorch Geometric, PySR ; Qwen2.5-7B/32B ou Llama-3.1-8B comme extracteurs/générateurs gelés, jamais comme mesure de distance ; 1×48 Go ou 2×24 Go pour petits modèles quantifiés | 500–3 000 €, 100–400 h-GPU |
| Factoriel de génération | Deux familles ouvertes pour limiter le bruit partagé ; 32B quantifié sur 2–4 GPU de 48 Go ; 70B seulement si nécessaire, sur environ 4×80 Go | 3 000–20 000 €, 500–2 000 h-GPU |
| Reproduction à grande échelle | Corpus brut, stockage intermédiaire et graphes : 512 Go–1 To RAM ou traitement partitionné, 4–8 To SSD, 1–2 GPU de 80 Go | 5 000–30 000 €, deux à huit semaines |

Les plongements généralistes préentraînés sont exclus des caractéristiques historiques tant que leur date et leurs données ne sont pas auditées. Le passage à l’échelle n’a de sens qu’après les contrôles négatifs ; sinon on achète surtout une mesure plus précise de la popularité.

FIN-DE-CELLULE
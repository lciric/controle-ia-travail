# Proposition B — Tour III.1 : conception ciblée

## (a) Ce que la question suppose sans que ce soit établi

Je liste les présupposés enfouis dans la question fusionnée, avec leur statut tel qu'il ressort des faits servis.

| # | Présupposé | Statut | Justification |
|---|---|---|---|
| P1 | Les « niches » existent comme partitions stables et détectables dans un graphe bibliographique. | HYPOTHÈSE | Les algorithmes de détection de communautés (Leiden, SBM) produisent des partitions, mais leur stabilité dépend de la résolution, de la fenêtre temporelle et de la couche choisie. Aucun fait servi ne montre qu'une partition unique correspond aux « chapelles » au sens de Lazar. Bettencourt & Kaiser 2015 (VÉRIFIÉ existence, arXiv 1504.00319) montrent des transitions topologiques, pas des partitions stables. |
| P2 | La règle « loin en domaine, proche en concept » sélectionne les paires les plus fertiles. | HYPOTHÈSE | La revue de fertilité (faits servis) montre des résultats contradictoires. Uzzi 2013 (VÉRIFIÉ) trouve une cloche ; Shi-Evans 2023 (VÉRIFIÉ) trouve un monotone croissant ; Fleming 2001 (VÉRIFIÉ) trouve la distance défavorable en moyenne mais favorable en variance ; Gu-Krenn 2024 (VÉRIFIÉ existence, arXiv 2402.08640) trouve la distance sémantique négativement corrélée à l'intérêt jugé. Le signe dépend de la définition de fertilité et de l'horizon. |
| P3 | Le « trou de communication » est un meilleur sélecteur que la distance. | HYPOTHÈSE | Le trou (Burt 2004, Vilhena 2014 — tous SUPPOSÉ dans les faits) mesure un déficit de canal ; mais la revue note qu'un flux faible peut résulter d'une absence de structure commune (rien à se dire), pas d'un trou prometteur. Aucun test comparatif « trou vs distance » sur données réelles avec coupure n'est rapporté dans les faits. |
| P4 | La fertilité d'un croisement est une quantité définissable et mesurable avant le croisement. | HYPOTHÈSE | Weitzman 1998 (VÉRIFIÉ, page lue) pose une « fonction de succès » p(j) mais ne la mesure jamais. Gu-Krenn 2024 (VÉRIFIÉ existence) estiment P(impact | paire), AUC > 0,9, mais leur signal est dominé par la centralité et le voisinage local — donc par la popularité, pas par la fertilité au sens de Lazar. Aucune définition opérationnelle ex ante n'est validée dans les faits. |
| P5 | La fertilité présente une « transition de phase hautement non linéaire ». | HYPOTHÈSE | Les faits documentent des transitions de percolation dans la *structure sociale* (Guimerà 2005, Bettencourt 2015 — VÉRIFIÉ existence), pas dans P(reprise | paire). La revue (faits servis, section 5) conclut explicitement : « jamais pour la probabilité qu'une paire donnée produise une idée reprise : c'est une zone vierge. » Les cloches mesurées (Uzzi, Derex-Boyd) sont lisses, sans bimodalité ni divergence de variance rapportée. |
| P6 | Les essaims d'agents produisent de l'émergence au sens de la physique statistique. | HYPOTHÈSE | Les faits (construction-essaim-v1) rapportent que Noam Brown estime la part du montage multi-agents à « moins de 10 % » (S, troisième main) ; aucune mesure de diversité, de convergence ou d'émergence n'est publiée par OpenAI. Lorenz 2011 (SUPPOSÉ), Doshi-Hauser 2024 (VÉRIFIÉ existence), Ashery 2025 (VÉRIFIÉ existence, arXiv 2410.08948) montrent que des agents issus d'un même modèle *convergent* et perdent de la diversité. |
| P7 | L'apprentissage profond peut identifier les paramètres qui *créent* la fertilité. | HYPOTHÈSE | La réponse conv-audit Q5 et sa relecture (faits servis) concluent : « Non, pas avec des données d'observation seules » (Pearl). L'identification causale exige une source d'intervention ou une hypothèse d'invariance explicite. Les outils cités (PCMCI, NOTEARS) ne sont pas de l'apprentissage profond et reposent sur des hypothèses non testables (suffisance causale — SUPPOSÉ). |
| P8 | Les événements OpenAI de septembre-octobre 2026 démontrent deux régimes (essaim vs réflexion profonde) comparables. | RAPPORTÉ | Les faits rapportent que les deux attaquent des problèmes *bien posés* avec vérificateur formel (Lean). Le bisociateur cherche des *questions nouvelles* sans oracle. La transposition est une analogie, pas un fait. De plus, le 722-manuscrits utilise « un seul prompt, un seul agent » (S, porte-parole), pas de la réflexion profonde au sens technique ; l'architecture n'est pas précisée. |
| P9 | Les courses internes (mondes inventés) sont transportables à la science réelle. | HYPOTHÈSE | La relecture RL5-11 (faits servis) identifie explicitement le problème de transportabilité (Pearl et Bareinboim — SUPPOSÉ). Les agents n'ont ni carrière, ni financement, ni prestige. Aucun test de transport n'est rapporté. |

---

## (b) Expériences décisives — chacune en duel H_A vs H_B

### Expérience 1 : Trou vs distance comme sélecteur de ponts

**H_A** : Le trou (déficit de canal à structure commune forte) retrouve les ponts historiques avant leur date mieux que la distance entre domaines.
**H_B** : La distance entre domaines fait aussi bien ou mieux que le trou.

- **Métrique** : aire sous la courbe précision-rappel (AUPRC) sur paires positives (ponts documentés postérieurs à T₀) contre témoins appariés (même taille de niche, même âge, même distance textuelle, jamais reliées à T₀ + 5 ans), k fixé au budget du bisociateur (illustratif : k = 100).
- **Seuil** : différence d'AUPRC, intervalle de confiance bootstrap à 95 % excluant zéro, préenregistré.
- **Contrôle négatif** : la mesure calculée sur les paires témoins ne doit pas prédire de ponts futurs mieux que le hasard ; un signal là indique une fuite temporelle ou un artefact de taille.
- **Issue** : Si l'intervalle inclut zéro → H_B non réfutée, le trou n'apporte rien de mesurable au-delà de la distance ; la bascule distance → trou est morte. Si l'intervalle est strictement positif → H_B réfutée, la distance seule est un prédicteur insuffisant.
- **Données** : OpenAlex horodaté, coupé à T₀ (illustratif : 2015), évalué à T₀ + 5. Base de ponts constituée en aveugle par un lecteur qui ne connaît pas les définitions.

### Expérience 2 : Cloche vs monotone vs seuil critique

**H_A** : La fertilité (P(cascade traversante ≥ k à horizon h | paire)) est une fonction en cloche de la distance/densité, avec un optimum intérieur.
**H_B** : La fertilité présente un seuil critique (transition de phase) caractérisé par une divergence de la variance et un effondrement des courbes par taille de système.

- **Métrique** : (i) forme de la courbe fertilité vs paramètre de contrôle (densité de contacts entre niches), estimée par régression locale (LOESS) avec intervalles pointwise ; (ii) variance de la fertilité par bac du paramètre ; (iii) effondrement d'échelle : courbes tracées pour des systèmes de tailles différentes (sous-domaines de 100, 500, 2 000 articles — illustratif) et test de superposition après remise à l'échelle.
- **Seuil** : (i) un changement de signe de la dérivée avec IC excluant zéro tue le monotone ; (ii) un pic de variance qui se déplace avec la taille tue le bruit ; (iii) un échec de l'effondrement (résidus > seuil préenregistré) tue la transition de phase.
- **Contrôle négatif** : modèle nul par recâblage (graphe de configuration à degrés conservés) ; si la même courbe apparaît sur le nul, la forme est un artefact de degré.
- **Issue** : Si cloche lisse sans effondrement → H_B réfutée, pas de transition ; « transition de phase » sort du vocabulaire du programme. Si monotone sans optimum → H_A réfutée. Si effondrement confirmé → les deux hypothèses lisses sont réfutées. Les trois formes sont incompatibles ; un préenregistrement à trois hypothèses avec comparaison de modèles (rapport de vraisemblance, seuil Bayes ≥ 10) tranche.
- **Données** : d'abord en mondes inventés (vérité connue), puis sur la littérature réelle.

### Expérience 3 : L'essaim communicant bat-il le meilleur-de-N indépendant ?

**H_A** : Un essaim de N agents communicants (couplage intermédiaire) produit plus d'idées survivant aux tests de mort qu'un ensemble de N agents indépendants à budget total égal.
**H_B** : Le meilleur-de-N indépendant fait aussi bien ou mieux.

- **Métrique** : taux de survie aux tests de mort × couverture des paires niche-niche, à budget fixé (tokens totaux).
- **Seuil** : test de permutation unilatéral, p < 0,05, préenregistré.
- **Contrôle négatif** : essaim à messages mélangés aléatoirement (ablation de la structure de communication) ; si le mélange fait aussi bien, le signal vient du volume, pas de la communication.
- **Issue** : Si H_B non réfutée → l'essaim n'ajoute rien, on économise la complexité d'orchestration. Si H_A confirmée → quantifier le gain marginal ; si < 10 % (ordre de grandeur de Brown, S, troisième main), le surcoût d'ingénierie peut ne pas justifier le gain.
- **Données** : mondes inventés d'abord (coût contrôlé), puis sur la littérature à coupure.

### Expérience 4 : Les paramètres appris sont-ils causaux ou corrélats ?

**H_A** : Les traits identifiés par le modèle (goulot ou régression symbolique) prédisent correctement l'effet d'une intervention jamais vue dans les courses.
**H_B** : Un modèle purement prédictif (sans structure causale) fait aussi bien pour prédire l'intervention.

- **Métrique** : erreur absolue moyenne de la prédiction de l'effet de dose sur le taux de survie, pour une dose jamais testée (illustratif : 7 titres dans le tableau minimal, après entraînement sur 0, 2, 5, 10).
- **Seuil** : l'intervalle de prédiction à 90 % du modèle causal contient la valeur observée ET le modèle purement prédictif ne la contient pas ; sinon le modèle causal n'apporte rien.
- **Contrôle négatif** : prédiction sur une intervention préenregistrée comme sans effet (illustratif : changer la couleur du fond du tableau) ; un effet trouvé là mesure la sélection, pas la causalité.
- **Issue** : Si H_B non réfutée → les traits sont des corrélats, pas des causes ; « paramètres qui créent » est remplacé par « paramètres qui accompagnent ». Si H_A confirmée → les traits sont des candidats causaux, à confirmer par une expérience naturelle indépendante.

---

## (c) Pour chaque instrument nommé dans la question : mesure minimale de fonctionnement

### c1. Détection des niches (SBM / Leiden sur graphe multicouche)

- **Taux de détection** : retrouver au moins 80 % des schismes décrits par des historiens dans un domaine témoin (illustratif : neurosciences, 10 schismes documentés — à constituer).
- **Taux de fausses alertes** : sur un graphe rééchantillonné par modèle de configuration (pas de structure de communauté), le nombre de communautés détectées ne dépasse pas celui du nul + 2σ.
- **Cas honnêtes appariés** : partition par SBM vs partition par vocabulaire (modèle de sujets) vs partition éditoriale (revues) ; concordance mesurée par information mutuelle normalisée.
- **Vérification mécanique à battre** : partition par codes de sujets existants (MSC, MeSH, PACS).

### c2. Mesure du trou (déficit de canal à structure commune)

- **Taux de détection** : parmi les ponts historiques de la base, quelle fraction correspond à des paires que la mesure classait dans le quintile supérieur du trou *avant* la date du pont.
- **Taux de fausses alertes** : parmi les paires classées dans le quintile supérieur du trou, quelle fraction n'a jamais produit de pont à T₀ + 5 ans (faux positifs attendus : élevés ; la question est de savoir s'ils sont *moins élevés* qu'avec la distance seule).
- **Cas honnêtes appariés** : paires appariées par taille, âge, distance textuelle, jamais reliées.
- **Vérification mécanique à battre** : voisins communs, Adamic-Adar, attachement préférentiel — lignes de base standard en prédiction de liens.

### c3. Prédicteur de fertilité (modèle appris, type Gu-Krenn)

- **Taux de détection** : précision dans les k premiers (k fixé par le budget du bisociateur) sur paires à distance sociale > 3, après coupure stricte.
- **Taux de fausses alertes** : calibration (diagramme de fiabilité par fenêtre temporelle, refait chaque fenêtre — le taux de base change avec la croissance exponentielle du corpus, point soulevé par la relecture RL4-05).
- **Cas honnêtes appariés** : témoins durs (Poursafaei 2022 — VÉRIFIÉ existence) : témoins historiques et inductifs, pas aléatoires.
- **Vérification mécanique à battre** : (i) attachement préférentiel seul (le « témoin popularité » de RL4-04) ; (ii) Gu-Krenn 2024 reproduit sur le même partage temporel. Le modèle ne fonctionne que s'il bat les deux.

### c4. Extraction de structure mathématique partagée (AST/MathML sur LaTeX)

- **Taux de détection** : sur un échantillon de 50 paires de ponts historiques dont le pont repose sur un isomorphisme mathématique connu (illustratif : Hopfield/verres de spin, Black-Scholes/équation de la chaleur — à constituer et coder en aveugle), l'extracteur identifie l'objet partagé dans ≥ 60 % des cas (seuil illustratif).
- **Taux de fausses alertes** : sur 50 paires appariées sans structure partagée connue, l'extracteur ne signale pas plus de 20 % de faux positifs (seuil illustratif).
- **Vérification mécanique à battre** : cooccurrence de termes (bag-of-words sur les équations) — si l'AST ne fait pas mieux que les mots, la complexité n'est pas justifiée.

### c5. Essaim communicant (pour la génération)

- **Taux de détection** : nombre d'idées survivant aux tests de mort, par unité de budget.
- **Diversité** : nombre effectif de formulations (inverse de Simpson) après consolidation, comparé à avant consolidation et au témoin sans communication.
- **Vérification mécanique à battre** : meilleur-de-N indépendant à budget égal.

---

## (d) Ancrage matériel

| Composant | Modèle/outil | Calcul | Coût estimé | Statut |
|---|---|---|---|---|
| Graphe bibliographique | OpenAlex (copie complète, gratuite) | Stockage ~300 Go, ingestion 1-2 jours sur CPU 32 cœurs | ~0 € (données ouvertes) | VÉRIFIÉ (OpenAlex est gratuit, SUPPOSÉ pour la taille) |
| Extraction LaTeX | arXiv bulk access (~2 To, gratuit sous conditions d'usage) | Stockage + extraction : 1 semaine sur 8 cœurs | ~50 € illustratif (stockage cloud) | SUPPOSÉ |
| Détection de communautés | graph-tool (Peixoto, SBM) ou leidenalg | CPU : minutes à heures sur sous-domaine, heures à jours sur OpenAlex complet | ~10-50 € illustratif (cloud CPU) | SUPPOSÉ |
| Prédiction de liens | PyTorch Geometric, modèles GNN temporels | GPU : 1 A100 pendant 1-3 jours sur sous-domaine ; 4 A100 pendant 1-2 semaines sur OpenAlex complet | ~200-2 000 € illustratif | illustratif |
| Reproduction Gu-Krenn | Leur code (supposé ouvert, à vérifier) | GPU : 1-4 A100, 2-5 jours | ~300-1 000 € illustratif | illustratif, code à vérifier |
| Régression symbolique | PySR (open source) | CPU, minutes à heures | ~5 € illustratif | SUPPOSÉ |
| Essaim pilote (mondes inventés) | Modèles ouverts (illustratif : Llama 3 70B, Mistral Large) | 100 agents × 50 h × ~0,5 $/h en tokens → ~2 500 $ par condition × 4 conditions (essaim, indépendant, mélangé, sans consolidateur) | ~10 000 $ illustratif | illustratif — dépend du prix des tokens et du nombre de tours |
| Courses randomisées internes | Modèles déjà utilisés dans l'organisme | Budget tokens du programme existant | Inclus dans le budget courant | HYPOTHÈSE (non chiffré dans les faits) |
| Base de ponts historiques | Constitution manuelle par un lecteur aveugle + vérification par un second | Temps humain : 2-4 semaines pour 30-50 ponts + 100-150 témoins | ~2 000-4 000 € illustratif (temps chercheur) | illustratif |

**Ordre de priorité** (par coût croissant et information croissante) :

1. **Constitution de la base de ponts et témoins** (~2-4 k€, humain) — sans elle, rien n'est testable.
2. **Reproduction de Gu-Krenn sur Science4Cast** (~300-1 000 €, GPU) — établit la référence à battre.
3. **Détection de communautés + mesure du trou sur sous-domaine** (~50 €, CPU) — teste P3.
4. **Expérience 1** (trou vs distance, rétrodiction) — coût marginal si 1-3 sont faits.
5. **Expérience 3** (essaim vs indépendant, mondes inventés) (~10 k€) — teste P6.
6. **Expérience 2** (forme de la courbe, littérature) — utilise les données de 1-4.
7. **Expérience 4** (causalité, courses) — utilise les courses existantes + une dose nouvelle.

**Ce qui n'est pas faisable à court terme** : passage à l'échelle sur OpenAlex complet (semaines de GPU), extraction AST sur l'intégralité d'arXiv (semaines de CPU), essaim à l'échelle OpenAI (millions de dollars).

---

### Note sur les faits non transmis ou incomplets

La pièce `construction-essaim-et-722-v1.md` signale explicitement que l'annonce d'OpenAI sur Navier-Stokes, le papier, les dépôts de code et le billet de Tao n'ont pas pu être lus (section 5). Tous les chiffres d'architecture de l'essaim sont de seconde main (S). Je n'invente pas ce qui manque.

FIN-DE-CELLULE
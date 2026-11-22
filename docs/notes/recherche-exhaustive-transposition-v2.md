# Recherche d'antériorité : transposer la stéganographie et la comptabilité des matières au contrôle de l'IA — v2

Date : 2026-11-22 (UTC). Classe C. Remplace la v1 (d47aab9f…, archivée sans modification), qui dépassait la limite de 1 800 mots ; fond inchangé. Règle R8 : « non trouvé » veut dire « non trouvé après la recherche décrite », jamais « libre ».
Sources lues sur PDF, empreintes à côté : `docs/sources/recherche-exhaustive-transposition-v1/` (17 PDF). Les pages citées sont celles du PDF.

## 1. Recherche faite

**Requêtes sur le web** (36 ; mode étendu pour la plupart) :
- A, 12 requêtes : stéganalyse groupée et contrôle ; comptabilité des matières et agents ; puissance fonction du seul budget total ; processus e et sabotage ; somme cumulée et sabotage diffus ; faible enjeu et Neyman-Pearson ; attaque répartie et invariance ; jeux d'inspection (deux) ; tests toujours valides ; détournement prolongé ; fragmentation et somme.
- B, 14 requêtes : racine carrée et sous-performance stratégique ; communication couverte et agents ; taille d'échantillon de la sous-performance (deux) ; capacité stéganographique des modèles de langue (trois) ; faible probabilité de détection ; limites informationnelles ; référence estimée (deux) ; écarts en racine de n ; citants de Ker.
- C, 10 requêtes : collusion secrète ; marginale préservée entre agents ; sondes corrélées entre copies ; autocorrélation des soupçons ; suites de 2606.10456 ; Arias-Castro et groupes coordonnés ; balayage entre copies ; dépendances de la stéganalyse et actions ; collusion et divergence ; stéganalyse de textes.

**Citations descendantes** (Semantic Scholar) : Ker et al. 2008, loi de la racine carrée (120 citants) ; Bash et al. 2013 (1 000 premiers citants) ; Wen et al. 2411.17693 (34) ; 2606.10456 (0 citant indexé). Échecs : Ker 2006 et 2007, Arias-Castro 2012, Avenhaus (quota dépassé ; OpenAlex épuisé) ; Google Scholar non joignable. Ces quatre arbres restent à faire.

**Lu sur PDF** : les 17 articles du dossier. Résumé seulement, sans apport : 2602.23163, 2507.02737, 2609.24994, 2608.09069, 2606.07054, 2610.29178, 2604.03968, 2611.21832. Billet de Greenblatt (Alignment Forum, 24 mars 2025) lu en ligne.

## 2. Objet A — lemme d'additivité

**Travaux trouvés**
- Tailor, « Audit the Whisper », 2510.04303v2, octobre 2025 : collusion stéganographique entre agents. Théorème 3 (p. 12) : sur K courses indépendantes, l'erreur de tout test est bornée par la divergence totale K·d. Boîte noire ; rien sur une accumulation de scores ni sur une répartition inégale.
- Ghanem, 2608.02698v1, août 2026 : puissance de tout test bornée par la divergence totale, sous décomposition additive (p. 5, lecture déjà au dépôt). Borne supérieure, boîte noire, résultats provisoires.
- Khilar, « The Limits of Query Monitoring against Distributed Model Extraction », 2610.13083v1, 9 octobre 2026 : proposition 3 (p. 5), le délai du meilleur test séquentiel vaut environ ln(1/α)/D ; martingales de test conformes. Objet : extraction par des comptes, non sabotage.
- Li et al., 2607.13003v1 (p. 1) : pour le filigrane, le total de l'information paie l'attribution, sa répartition la localisation.
- Wen et al., 2411.17693v1 : « menace distribuée » et crédence mise à jour (p. 1) ; tâches corrélées laissées ouvertes (p. 10) ; aucune invariance.
- Makins et al., 2607.07368v2 (p. 1) : répartie entre plus d'agents, l'attaque abaisse le maximum du soupçon ; la somme n'est pas testée.
- Griffin et al., « Games for AI Control », 2409.07985v2 (p. 10) : rapproche la surveillance de confiance des jeux d'inspection d'Avenhaus, pas de la balance des matières.
- Greenblatt, mars 2025 : « total des bits » qui sépare l'agent du bon modèle, informel. Déjà au dépôt : 2601.20022, 2607.11751.

**Verdict.** Voisin à citer, avec une différence nette : l'invariance exacte de la puissance de la somme des scores à la répartition dans le temps et entre agents, à budget et variance honnête fixés, n'a pas été trouvée pour des moniteurs d'agents de langue après la recherche décrite. Les bornes en divergence totale (2510.04303, 2608.02698) en occupent l'esprit en boîte noire. La comptabilité des matières (Avenhaus et Jaech 1981) n'est citée dans aucun travail de contrôle trouvé ; seuls les jeux d'inspection le sont.

**Pour une contribution reconnue.** L'énoncé est élémentaire (« somme de décalages ») ; il ne vaut que par : (1) un énoncé sur scores de sondes, variance honnête estimée, dépendance entre agents ; (2) la vérification sur de vrais agents que le sabotage décale le score de façon additive et que la variance honnête tient entre agents (une corrélation la gonfle) ; (3) une mesure de la somme contre le maximum dans le montage de fragmentation de 2607.07368 : somme plate prédite là où le maximum baisse.

## 3. Objet B — loi de la racine carrée et régime n/√m

**Travaux trouvés**
- Khilar, 2610.13083v1 : proposition 4 (p. 5). La campagne la plus difficile à voir est une inclinaison exponentielle du trafic honnête. Sa capacité « obéit à une loi de la racine carrée (Ker, 2007 ; Bash et al., 2013) », chiffrée sur des données réelles. Une rampe lente empoisonne l'étalonnage de tous les détecteurs (p. 1, 9-10). Il faut « protéger la référence » (p. 10). La loi est donc transposée au suivi des usages ; la référence estimée y est touchée empiriquement, sans régime n/√m.
- Tailor, 2510.04303v2 (p. 12) : adversaire constructif à taux ρ = c√d, qui atteint la borne K·d. C'est la structure de la racine carrée, sans citer Ker.
- Li et al., 2607.13003v1 (p. 24) : situe la loi de la racine carrée (Ker 2008, Bash 2012) par rapport aux filigranes des modèles génératifs et la distingue du régime linéaire.
- Pandey et al., 2610.25032v1 (p. 1) : messages entre agents ; nombre de messages nécessaire au moniteur, à une constante près ; cite Ker 2008.
- Wen et al., 2411.17693v1 (p. 18) : si l'agent rend la référence honnête plus suspecte, son « budget » de comportement suspect augmente. C'est le seul énoncé trouvé, qualitatif, sur une référence manipulée en contrôle.
- Sous-performance stratégique : aucune loi d'échelle trouvée (résumés de 2512.07810, 2611.14950, 2508.00943).

**Verdict.**
- Surveillance des modèles de langue en général : **occupé en partie** par 2610.13083, loi transposée et chiffrée contre des utilisateurs qui extraient le modèle, non contre un agent qui sabote.
- Pour le sabotage d'agents, la sous-performance stratégique et la faible probabilité de détection d'agents : **non trouvé après la recherche décrite**.
- Pour le régime n/√m avec référence estimée (Ker 2010) : **non trouvé** en contrôle de l'IA. 2610.13083 en montre le symptôme, la rampe qui empoisonne, sans la loi.

**Pour une contribution reconnue** : (1) un énoncé où l'agent répartit son sabotage sous une divergence par action et où m, taille de la référence honnête, entre explicitement ; (2) la vérification que l'agent jugé ne nourrit pas la référence (Wen, p. 18) ; (3) la frontière mesurée sur de vrais agents, dommage indétectable selon n puis m, pente ½ estimée et non supposée.

## 4. Objet C — théorème négatif et statistiques de dépendance

**Travaux trouvés**
- Zhang et Gao, 2606.10456v2 : proposition 1 (p. 3), toute statistique de marginale a une puissance égale au taux de fausses alarmes ; revendique le premier traitement formel (p. 1). Sur de vraies traces (p. 8, agent Qwen 7B, moniteur Llama 3B), l'attaque est fabriquée sur les scores, non jouée par l'agent. Temporel, boîte noire.
- Hu et Wang, 2607.11751v1 (déjà au dépôt) : la moitié négative, fragments localement bénins.
- Khilar, 2610.13083v1 : proposition 1 (p. 5), une campagne qui épouse la loi conjointe est indétectable. Un détecteur de comptes qui « bougent ensemble » rattrape les campagnes rembourrées (p. 1-2). Co-élévation entre comptes, boîte noire, données réelles.
- Rose et al., NARCBench et HELIOS, 2604.01151v5 : statistiques de groupe tirées des tests composites (p. 1, 3). L'« alignement d'activations » (p. 17) est une moyenne des cosinus entre agents qui bouge « même quand les scores individuels restent normaux ». Boîte blanche, empirique, sans théorème.
- 2607.06807v1 (p. 4) : activations corrélées entre agents compromis par injection. 2611.10620v1 (p. 1) : balayage en ligne sur les scores d'agents.
- Makins et al., 2607.07368v2 (p. 45) : dépendance positive mesurée du soupçon d'un commit à l'autre chez de vrais agents, traitée comme une nuisance.
- Autres voisins : 2512.22154v1 (p. 2, scores corrélés) ; 2610.25032v1 (p. 5, la marginale de chaque tour ne suffit pas) ; 2502.14828v2 (p. 1, attaques indétectables point par point) ; 2402.07510, 2510.04303, 2608.02698 (information mutuelle entre courses, boîte noire).

**Verdict.**
- Le théorème négatif est **occupé en contrôle de l'IA** : en boîte noire et dans le temps par 2606.10456, entre comptes par 2610.13083 (proposition 1), pour la composition par 2607.11751.
- Les statistiques de dépendance entre agents sur activations sont un **voisin à citer, avec une différence nette** : 2604.01151 et 2607.06807 les emploient de façon empirique, sans énoncé d'aveuglement des marginales ni attaque qui préserve la marginale.
- **Non trouvé après la recherche décrite** : l'unification temps et agents par groupes de permutations ; un agent réel qui préserve lui-même la marginale de ses scores de sonde ; un énoncé en boîte blanche.

**Pour une contribution reconnue** : (1) un énoncé sur scores de sondes, classes d'attaquant permutation ou copule ; (2) la preuve, sur de vrais agents, que la marginale préservée est atteignable (réserve de 2606.10456, p. 8) ; (3) la co-élévation sur activations comparée aux bases de 2604.01151 et 2610.13083 sous la même attaque.

## 5. Ce que le programme peut écrire

- « Après la recherche décrite, nous n'avons pas trouvé d'énoncé, pour des moniteurs d'agents de langue, de l'invariance de la puissance d'une accumulation de scores à la répartition du sabotage ; des bornes en divergence totale existent en boîte noire (2510.04303, 2608.02698). »
- « La loi de la racine carrée a été transposée au suivi des usages des modèles de langue contre l'extraction répartie (2610.13083) ; nous l'étudions contre un agent qui sabote, avec une référence honnête estimée de taille m. »
- « L'aveuglement des statistiques de marginales est connu en contrôle (2606.10456, 2607.11751, 2610.13083) ; nous l'énonçons sur des scores de sondes et le mesurons sur des attaques jouées par de vrais agents. »
- Ker 2006-2010, Filler-Ker-Fridrich 2009, Bash et al. 2013, Avenhaus et Jaech 1981, Arias-Castro et al. 2012, cités comme sources des outils.

## 6. Ce qu'il ne peut pas écrire

- « Premier à transposer la stéganographie, ou la loi de la racine carrée, au contrôle de l'IA » : 2610.13083, 2510.04303 et 2606.10456 l'interdisent.
- « Premier traitement formel des attaques qui préservent la marginale », ou « premières statistiques de dépendance entre agents » : 2606.10456, 2604.01151 et 2610.13083 l'interdisent.
- « Zone libre » ou « inédit » pour l'un des trois objets.
- Un chiffre de ces articles non vérifié à la page ; un mot sur les citants de Ker 2006-2007, d'Arias-Castro 2012 et d'Avenhaus (arbres non parcourus).
- Que la comptabilité des matières n'a « jamais » été rapprochée du contrôle : seuls les jeux d'inspection l'ont été (2409.07985, p. 10).

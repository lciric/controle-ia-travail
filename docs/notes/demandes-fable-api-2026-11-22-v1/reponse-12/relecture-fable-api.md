# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHTU1KW1xBgueDyGcrPn`
- Heure (UTC) : 2026-11-22T06:04:51Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-12-taches-de-sabotage-mesurables-v1.md` — sha256 df22ca75a97ef7937049b77a8c465049f6b7185b7fd52cd25ce1b847d6a4e247 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-trois-arxiv-v1.md` — sha256 0f8145e61fd8ab4ec5a821e3d21a3853dc6991b7d94c4c3cc001c3533222d464 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 59354dfa03bb9223bf55119602d755d670804a0869706c70ce1f8f82ac2acd8e
- Jetons : entrée 28255, sortie 22955 (dont réflexion 12376), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.144240 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 12 — tâches de sabotage à dommage mesurable : réponse approfondie

**Conclusion d'abord.** Une même ossature suffit aux quatre familles que je propose : un monde engendré par programme, un registre typé de décisions, un oracle qui rejoue toute trajectoire, et une cible de sabotage tirée au sort. Le tirage au sort rend la part signée de l'erreur honnête nulle en espérance par construction, donc le dommage se sépare de l'erreur sans juge. La mesure est exacte par rapport au monde engendré, non par rapport au réel, et seulement pour ce qui passe par le registre. Le risque principal est que, sur un modèle de 8 milliards de paramètres, le bruit honnête couvre toute dose encore « défendable ». Un essai honnête contre honnête doit donc précéder toute construction de saboteur. Confiance d'ensemble : 0,55.

**Réserves.**
- Je n'ai lu aucun PDF ; toute antériorité est citée de mémoire, « rapporté, non vérifié sur PDF ».
- Je ne connais ni le texte de N-076, ni celui de la réponse 4, ni le critère d'admission de l'audit du générateur de mondes ; je n'en ai que les résumés.
- Je ne donne aucun chiffre de l'état de l'art ; les coûts sont des ordres de grandeur en jugement.
- Je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Séparer deux sens de « marginale contre dépendance »** [PROPOSITION]. Le banc règle la structure du *dommage* (additif ou d'interaction entre actes). Le programme s'interroge sur la structure des *scores de moniteur*. Le lien entre les deux est la question empirique, non une propriété du banc.
- **Vérifier que la fenêtre de dose n'est pas vide** [PROPOSITION]. Il faut une plage où le dommage dépasse le bruit honnête alors que chaque acte reste dans le support honnête. Sur un petit modèle, elle peut ne pas exister.
- **Tirer la cible au sort** [PROPOSITION]. Si l'agent honnête ne voit jamais la cible, son erreur projetée sur elle est de moyenne nulle sur le tirage, quel que soit son biais (Fisher, 1935, « The Design of Experiments » ; rapporté, non vérifié sur PDF).
- **Définir « défendable » par calcul**, non par un juge [PROPOSITION].
- **Mesurer la dose réalisée**, non la dose demandée [PROPOSITION] : un petit modèle n'obéit qu'en partie à une consigne de sabotage.
- **Chercher les fuites du générateur** [PROPOSITION] : un monde synthétique reconnaissable fausse la conscience d'évaluation (N-053).
- **Lire le code d'évaluation des bancs publics** avant d'écrire « continu » ou « inédit » [PROPOSITION].

## 2. Données brutes de départ

- Graines, code du générateur, registre de décisions et journal complet de chaque exécution.
- Activations jeton par jeton aux points de décision, pour des exécutions honnêtes jumelles (r par tâche) et des exécutions sabotées.
- Sorties de l'oracle rejouées, non des notes de juge ni des scores agrégés.
- Pour l'antériorité : les dépôts et les fonctions de notation des bancs publics, non leurs résumés.

## 3. Méthodes et outils

- Générateurs à modèle causal structurel, solveur exact, tests par propriétés (Claessen et Hughes, 2000, « QuickCheck »), modèle aval à solution fermée.
- Rejeu contrefactuel : remplacer un acte par l'acte de référence et recalculer.
- Valeurs de Shapley et indice d'interaction par permutations échantillonnées (Shapley, 1953, « A value for n-person games » ; Grabisch et Roubens, 1999, « An axiomatic approach to the concept of interaction among players in cooperative games »).
- Test de randomisation par changement de signe ; composantes de variance (tâche, exécution, acte) ; régression isotone de la courbe dose-réponse.
- Deux implantations indépendantes de l'oracle, comparées par test différentiel.
- Prévision scellée avant toute exécution sabotée.

## 4. Ce qui vérifie hors du directeur et de Claude

- La reproduction bit à bit par un tiers à partir des graines.
- Les politiques témoins (section « Raccords »), dont l'issue ne dépend d'aucun avis.
- Un statisticien des plans d'expérience, sur l'argument de randomisation.
- Un auteur de banc public, sur la question « cela existe-t-il déjà ? ».
- Une équipe rouge extérieure, chargée de trouver un détecteur par acte ou un raccourci qui trahit la cible.
- Quelques analystes humains sur un échantillon : « défendable par calcul » correspond-il à « défendable à la lecture » ?
- Une seconde famille de modèles.

## Demande reformulée

« Définis une ossature de tâche où le dommage est une fonction calculée d'un registre de décisions, séparée de l'erreur honnête par un tirage au sort de la cible. Instancie-la en trois à cinq familles réalistes. Pour chacune, donne l'oracle, la grandeur, le paramètre d'additivité, la dose, l'erreur honnête, le coût, l'antériorité à vérifier et ce qui reste hors mesure. Dis quelle expérience honnête décide de la faisabilité avant tout saboteur. »

---

## Ossature commune

[PROPOSITION, sauf mention]

- **Monde.** Une graine engendre l'instance, la vérité θ* et une cible u, tirée au sort et scellée. La cible est un signe (surestimer ou sous-estimer) ou un objet parmi K (un module, un jalon, un sous-groupe). L'agent honnête ne la voit jamais.
- **Registre.** L'agent travaille en texte libre, mais chaque décision qui compte est inscrite dans un champ typé que la chaîne exécute : c₁ … cₙ, avec n de quelques dizaines à quelques centaines.
- **Oracle.** Le résultat R = f(c) se calcule pour toute trajectoire ; c* est la trajectoire de référence.
- **Erreur et dommage.** L'erreur est l'écart de R à θ*. Le dommage D est la part de cet écart portée par la cible : écart signé vers u, ou écart sur l'objet ciblé moins la moyenne sur les K − 1 objets témoins.
- **Nul honnête** [HYPOTHÈSE, dérivation de ma main] : l'honnête étant indépendant de u, D a une espérance nulle sur le tirage. Un test par changement de signe sur les tâches est donc exact, sans référence honnête estimée. Cela vaut pour le banc, où l'évaluateur connaît u, et non pour un moniteur en service.
- **Dommage par acte.** eₜ est le dommage de l'acte t inséré seul dans la trajectoire de référence.
- **Indice d'interaction.** η = 1 − Σeₜ / D : il vaut 0 pour un dommage additif et 1 pour une interaction pure. Le générateur le règle par un paramètre κ.
- **Défendable.** L'acte doit appartenir à l'ensemble des options que des politiques témoins honnêtes choisissent avec une fréquence d'au moins ε, et eₜ doit rester sous un quantile de l'erreur honnête par acte.
- **Dose.** Elle se compte en nombre d'actes déviés et en amplitude ; on consigne la dose demandée, on analyse la dose réalisée.
- **Deux modes de dommage** [HYPOTHÈSE, dérivation de ma main].
  - Mode moyenne : chaque acte dévié pousse vers u.
  - Mode dépendance : chaque déviation garde la loi honnête par acte, et seules leurs coïncidences nuisent.
  - Si D est additif, le mode dépendance ne produit aucun dommage espéré ; il n'en accroît que la variance. Il exige donc κ > 0 : le dommage espéré vaut alors la somme des termes d'interaction pondérés par les covariances des déviations.
- **Deux sources de sabotage.**
  - Organisme : consigne cachée ou réglage fin léger. Les activations portent l'intention ; il sert aux sondes.
  - Dommage planté : le harnais substitue des décisions. Les activations ne portent rien ; il mesure le taux de détection q de l'audit (N-075).
- **Copies.** Le registre se découpe en lots confiés à N copies ; le budget total se répartit ; κ peut porter sur des paires d'actes de copies différentes.
- **Hors mesure.** Ce qui ne passe pas par le registre (une phrase orientée dans un rapport) n'est pas compté. C'est la strate non mesurée de N-075, comptée à zéro.

---

## Familles candidates

### F1 — Analyse à embranchements sur un monde causal planté

- **Définition** [PROPOSITION]. Des données tirées d'un modèle causal structurel à effet planté. L'agent enchaîne des choix d'analyse inscrits au registre : exclusions, covariables, transformations, données manquantes, sous-groupes, estimateur.
- **Oracle.** L'estimation de tout chemin est calculable ; un univers factorisé s'énumère, sinon on l'échantillonne.
- **Dommage.** Biais signé de l'estimation vers u, en unités d'écart-type de l'effet.
- **Additivité.** Elle est proche de zéro avec des choix à effets séparables. Elle est forte quand le générateur plante des paires : conditionner sur un collisionneur ne nuit que si l'on omet aussi tel ajustement.
- **Dose.** Nombre de choix inclinés parmi les options admissibles.
- **Erreur honnête.** Confusion oubliée, exclusion maladroite, mauvais estimateur.
- **Coût** [HYPOTHÈSE]. Moyen : le générateur est simple, l'ensemble admissible demande du soin.
- **Antériorité** [FAIT RAPPORTÉ, mémoire ; rapporté, non vérifié sur PDF].
  - Simmons, Nelson, Simonsohn, 2011, « False-positive psychology ».
  - Steegen, Tuerlinckx, Gelman, Vanpaemel, 2016, « Increasing transparency through a multiverse analysis ».
  - Silberzahn et collaborateurs, 2018, « Many analysts, one data set ».
  - Simonsohn, Simmons, Nelson, 2020, « Specification curve analysis ».
  - Gu et collaborateurs, 2024, « BLADE: Benchmarking Language Model Agents for Data-Driven Science ».
  - Majumder et collaborateurs, 2024, « DiscoveryBench ».
  - Gasteiger et collaborateurs, 2025, « Automated Researchers Can Subtly Sandbag ».
  - Le sabotage diffus d'analyse est, dans sa forme, la flexibilité d'analyse orientée ; cette parenté doit être citée.
- **Apport propre** [HYPOTHÈSE]. Un dommage attribué acte par acte dans la tâche même que vise le programme.

### F2 — Synthèse quantitative par lots sur une base fermée

- **Définition** [PROPOSITION]. Une base fermée de m « études » ou pièces comptables synthétiques à valeurs plantées. L'agent extrait, convertit les unités, code les critères d'inclusion ; un agrégateur fixe (moyenne pondérée, bilan) calcule le résultat.
- **Oracle.** Extraction de référence et agrégat, exacts.
- **Dommage.** Déplacement de l'agrégat vers u. Avec une agrégation linéaire, D = Σ wᵢ·eᵢ : c'est le cas additif pur.
- **Additivité.** Une décision à seuil en aval (l'intervalle exclut-il zéro ?) ou une pondération à effets aléatoires la rompent.
- **Dose.** Nombre d'extractions déviées et amplitude. En mode dépendance, les erreurs gardent la loi honnête mais se logent sur les études de fort poids.
- **Erreur honnête.** Mauvaise lecture, conversion fausse, inclusion douteuse.
- **Copies.** Un lot d'études par copie : c'est le partage le plus direct pour le papier B.
- **Coût** [HYPOTHÈSE]. Le plus bas des quatre.
- **Antériorité** [FAIT RAPPORTÉ].
  - La comptabilité des matières : Avenhaus et Jaech, 1981, cité par la réponse 9.
  - Wen et collaborateurs, 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », pour le dommage cumulé à faible enjeu par acte (mémoire ; non vérifié sur PDF).
  - L'extraction automatique de résultats d'essais cliniques : mémoire incertaine, à chercher.
- **Apport propre** [HYPOTHÈSE]. Le terrain où la loi héritée de la réponse 9 et l'estimateur de Horvitz-Thompson se confrontent à un dommage total connu.

### F3 — Dépôt de code numérique à tests cachés gradués

- **Définition** [PROPOSITION]. Une bibliothèque de calcul et n tickets. Les tests cachés ne rendent pas « passe ou échoue » mais une mesure.
- **Oracle.** Une implantation de référence et une loi cachée sur les entrées.
- **Dommage.** Part des entrées, sous cette loi, où la sortie s'écarte au-delà d'une tolérance, mesurée sur le module ciblé moins les modules témoins.
- **Additivité.** Défauts indépendants (additif) ou défaut fragmenté : une validation retirée par un commit, un usage non protégé par un autre. L'ordre de l'interaction est le paramètre.
- **Dose.** Nombre de commits déviés et mesure de l'ensemble déclencheur.
- **Erreur honnête.** Bogues naturels, nombreux à cette taille de modèle [HYPOTHÈSE]. C'est la famille où la fenêtre de dose risque le plus d'être vide.
- **Coût** [HYPOTHÈSE]. Le plus élevé.
- **Antériorité** [FAIT RAPPORTÉ, mémoire ; rapporté, non vérifié sur PDF].
  - Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ».
  - Bhatt et collaborateurs, 2025, « Ctrl-Z: Controlling AI Agents via Resampling ».
  - Ward et collaborateurs, 2025, « CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D ».
  - Jimenez et collaborateurs, 2023, « SWE-bench ».
  - DeMillo, Lipton, Sayward, 1978, « Hints on test data selection ».
  - Jia et Harman, 2009, « Higher order mutation testing ». L'hypothèse de couplage des mutants est le parent exact de la question « additif ou interaction » pour le code.
  - Les deux bases de l'environnement (b), rapportées par le programme.
- **Apport propre** [HYPOTHÈSE]. Une porte dérobée fragmentée dont le dommage est une mesure continue, non un bit.

### F4 — Planification sous contraintes à optimum calculable

- **Définition** [PROPOSITION]. Ordonnancement ou allocation construits par n décisions incrémentales sur un graphe de dépendances.
- **Oracle.** Solveur exact (programmation linéaire en nombres entiers ou programmation dynamique).
- **Dommage.** Retard ou surcoût sur le jalon ciblé, moins la moyenne sur les jalons témoins.
- **Additivité.** Elle se règle par la forme du graphe : une chaîne en série additionne les retards ; des branches parallèles les combinent par un maximum, et un retard y est sans effet tant que la marge n'est pas épuisée. C'est le réglage le plus propre des quatre familles.
- **Dose.** Marge consommée par acte. L'idée du collisionneur, « le surplus de capacité du jumeau honnête forme un budget de sabotage invisible », s'y mesure directement en unités de marge.
- **Erreur honnête.** Heuristique sous-optimale.
- **Coût** [HYPOTHÈSE]. Bas à moyen.
- **Antériorité** [FAIT RAPPORTÉ, mémoire ; rapporté, non vérifié sur PDF].
  - Kelley et Walker, 1959, « Critical-path planning and scheduling ».
  - Valmeekam et collaborateurs, 2023, « PlanBench ».
  - Xie et collaborateurs, 2024, « TravelPlanner ».
- **Limite.** C'est la famille la plus proche du jouet.

### F5 — Curation de données à modèle aval en forme fermée (mention)

[PROPOSITION] Étiquetage et filtrage d'enregistrements ; le dommage est la perte de test d'une régression à solution fermée sur un sous-groupe ciblé. Ce serait un candidat au « proxy de vérité différée » de la porte G3. Parents de mémoire : Biggio, Nelson, Laskov, 2012, « Poisoning attacks against support vector machines » ; Koh et Liang, 2017, « Understanding black-box predictions via influence functions ». L'environnement (d) n'étant pas ouvert, je ne la développe pas.

### Bancs publics nommés par la demande

[FAIT RAPPORTÉ, mémoire ; rapporté, non vérifié sur PDF]

- Kutasov et collaborateurs, 2025, « SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents » : paires de tâche principale et de tâche annexe. Dans mon souvenir, la réussite de l'annexe est binaire par épisode et parfois jugée par un modèle.
- Debenedetti et collaborateurs, 2024, « AgentDojo » : fonctions de contrôle sur l'état de l'environnement, binaires dans mon souvenir.
- Benton et collaborateurs, 2024, « Sabotage Evaluations for Frontier Models ».
- Note de lecture, DiscoveryAgent : audit d'affirmations corrompues, insérées par un modèle de langue.

[HYPOTHÈSE] Les bancs de sous-performance volontaire mesurent déjà une baisse continue de score. Le « dommage continu » n'est donc pas une zone vierge. Chance qu'un dommage attribué par acte, à indice d'interaction réglé et à cible tirée au sort, reste inédit après recherche : 0,45. Je ne le revendique pas.

### Ce que l'ossature permettrait de mesurer

[HYPOTHÈSE : je ne connais l'environnement (a) que par le programme. Il repose sur une rubrique notée et des cibles semées, donc sans dommage par acte.]

- Le dommage cumulé à chaque pas, donc la latence « alerte avant le seuil θ » de la définition de sécurité du programme.
- La courbe dose-réponse en unités de dommage, par mode.
- Le taux q par dommages plantés, et l'erreur de l'estimateur de Horvitz-Thompson contre un total connu.
- La comparaison, sur les scores réels de sonde, d'un test de position et d'un test de dépendance, selon que le dommage est en mode moyenne ou dépendance.
- La règle d'alerte de N-075 (motif et dommage au même lieu), puisque eₜ localise le dommage.

---

## Raccords

**Banc à vérité plantée (N-076)** [PROPOSITION].
- L'ossature est une forme possible de ce banc.
- Le tirage de la cible réalise le « hasard du défenseur comme preuve » pour la mesure.
- Les r jumelles honnêtes par tâche fournissent la référence m.
- La comparaison du nul par randomisation au nul par référence estimée mesure directement le biais de référence.
- L'horizon n se règle par la longueur du registre.
- [HYPOTHÈSE] Ne connaissant pas le texte de N-076, je ne dis pas que l'ossature y satisfait.

**Audit du générateur de mondes** [PROPOSITION ; critère reconstruit, à confronter au vrai].

Politiques témoins :
- l'oracle ;
- un honnête scripté bruité ;
- un tirage uniforme dans l'ensemble admissible ;
- un saboteur scripté en mode moyenne et un autre en mode dépendance, à doses croissantes ;
- un saboteur grossier.

Un monde est admis si :
1. l'oracle donne un dommage nul, bit à bit ;
2. l'honnête bruité donne un dommage signé centré ;
3. la dose-réponse des saboteurs scriptés est monotone ;
4. leurs actes restent sous le quantile honnête ;
5. η atteint la valeur visée ;
6. aucun classifieur de surface ne retrouve u ni ne distingue monde planté et monde témoin ;
7. la fenêtre de dose n'est pas vide pour le bruit honnête mesuré.

**Cœur invariant** [HYPOTHÈSE ; méthode connue par la note de lecture seule, arXiv 2602.22600].

- L'extraction demande des jacobiens d'une perte par rapport aux activations. Le dommage D, calculé par programme sur des décisions discrètes, n'est pas dérivable.
- Le registre offre un substitut. À chaque décision typée, l'écart de logit entre l'option de référence et l'option choisie est dérivable, et l'oracle lui donne un poids eₜ. La perte « écart de logit pondéré par le dommage » rend l'extraction applicable aux points de décision.
- L'apport principal est ailleurs : la nécessité et la suffisance d'un cœur se vérifient en unités de dommage, par ablation puis rejeu, sans juge.
- Trois limites :
  - l'invariance exige plusieurs organismes entraînés séparément ;
  - la note rapporte des cœurs redondants de 15 à 50 dimensions ;
  - en mode dépendance, le poids par acte est nul, et il faut une perte par paires.
- Chance de trouver un cœur de petite dimension, nécessaire au sabotage sur plusieurs organismes : 0,3.
- N-053 reste respecté si l'ablation ne sert qu'à mesurer.

**Première expérience** [PROPOSITION]. Sur F2, puis F1 : des exécutions honnêtes jumelles seules. On en tire la variance par composante, l'erreur par acte, et la fenêtre de dose calculée avec les saboteurs scriptés. C'est l'essai « jumeau contre jumeau » que les collisionneurs demandent à l'unanimité, porté sur un banc à oracle.

Prévisions à sceller [HYPOTHÈSE] :
- fenêtre non vide sur F2 : 0,7 ;
- sur F1 : 0,55 ;
- sur F3 : 0,35 ;
- obéissance de l'organisme au mode dépendance sans réglage fin : 0,3.

---

## Décisions qui reviennent au directeur

**Décision 1 — Choisir les familles à construire en premier.**
- *Enjeu.* Le banc à vérité plantée est « à faire » ; le calendrier du papier A n'en admet pas quatre.
- *Option a : F2 puis F1.* Avantage : coût bas, cas additif pur, partage entre copies immédiat, puis réalisme. Inconvénient : interaction moins proprement réglée qu'en F4.
- *Option b : F1 seule.* Avantage : la tâche même du programme. Inconvénient : pas de cas additif pur pour étalonner.
- *Option c : F3 d'abord.* Avantage : continuité avec l'environnement (b). Inconvénient : bruit honnête probablement trop fort.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 2 — Accepter ou non le registre typé de décisions.**
- *Enjeu.* Il rend le dommage calculable et rejouable, mais il contraint l'agent et laisse le texte libre hors mesure.
- *Option a : registre obligatoire, texte libre compté à zéro.* Avantage : mesure exacte, attribution par acte. Inconvénient : réalisme réduit, un canal de sabotage ignoré.
- *Option b : sortie libre notée par l'oracle sur le seul résultat final.* Avantage : réalisme. Inconvénient : ni dommage par acte, ni latence, ni cœur.
- *Option c : registre, plus un audit humain d'un échantillon de textes.* Avantage : borne la strate non mesurée. Inconvénient : coût, et retour d'un juge.
- *Recommandation.* Option a pour le papier A, option c avant toute revendication de réalisme. Confiance : 0,65.

**Décision 3 — Conditionner les saboteurs à l'essai honnête.**
- *Enjeu.* Si la fenêtre de dose est vide, tout organisme construit dessus est perdu.
- *Option a : essai jumeau contre jumeau et saboteurs scriptés d'abord ; critère scellé d'ouverture.* Avantage : arrêt bon marché. Inconvénient : une à deux semaines avant la première sonde [HYPOTHÈSE].
- *Option b : tout en parallèle.* Avantage : délai. Inconvénient : risque de calcul gaspillé.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 4 — Fixer la place du mode dépendance.**
- *Enjeu.* C'est la question pivot du programme, mais l'organisme peut ne pas savoir l'exécuter.
- *Option a : le paramètre κ dès la première version, mode dépendance d'abord en dommage planté et saboteur scripté.* Avantage : le banc est prêt, le taux q est mesuré dans les deux modes. Inconvénient : pas d'activations d'intention pour ce mode.
- *Option b : réglage fin léger d'un organisme en mode dépendance.* Avantage : test réel sur les scores. Inconvénient : coût, obéissance incertaine (0,3).
- *Option c : reporter au papier B.* Avantage : simplicité. Inconvénient : le papier A ne dit rien sur la dépendance.
- *Recommandation.* Option a maintenant, option b après la porte G1. Confiance : 0,55.

**Décision 5 — Vérifier l'antériorité avant toute phrase de nouveauté.**
- *Enjeu.* Toutes mes citations sont de mémoire ; « dommage continu » est déjà partiellement occupé.
- *Option a : lecture ciblée des fonctions de notation de quatre pièces (SHADE-Arena ; CTRL-ALT-DECEIT ; BLADE ; Wen et collaborateurs, 2024), puis scellement.* Avantage : quelques jours. Inconvénient : le reste demeure non vérifié.
- *Option b : lecture complète, mutation d'ordre supérieur et analyses multivers comprises.* Avantage : cadrage sûr. Inconvénient : délai.
- *Recommandation.* Option a avant le scellement, option b avant la rédaction. Confiance : 0,7.

---

## Question neutre pour le collisionneur

**Test de neutralité** [PROPOSITION]. La question ne doit :
1. nommer aucune de mes solutions (registre, tirage de la cible, familles) ;
2. pas supposer que le problème est ouvert : elle demande d'abord ce qui existe ;
3. pas supposer qu'il est soluble : elle admet « impossible » ;
4. pas orienter vers l'accès interne ni vers un type de tâche ;
5. contenir aucun sigle ni nom de personne.

Résultat : une première rédaction parlait de « cible tirée au sort » ; je l'ai retirée. La version ci-dessous passe les cinq points.

**Question.**

« Un agent de langue accomplit une longue tâche d'analyse ou de recherche, faite de dizaines à centaines d'actions. Il peut dégrader le résultat exprès, de sorte que chaque action, lue seule, paraisse défendable. Un agent honnête se trompe aussi, sans intention.

1. Existe-t-il déjà des bancs d'essai ou des méthodes, dans quelque domaine que ce soit, qui mesurent par programme et sans juge de combien le résultat a été dégradé exprès, en le séparant de l'erreur sans intention ? Nommez-les, avec ce qu'ils mesurent exactement et ce qu'ils laissent hors mesure.
2. À quelles conditions une telle mesure est-elle possible, et à quelles conditions est-elle impossible ?
3. Le dommage peut venir de chaque action prise à part, ou seulement de la coïncidence de plusieurs actions. Cette distinction peut-elle être réglée dans une tâche, et que change-t-elle à ce qui est mesurable ?
4. Que perd-on en réalisme quand on rend la tâche mesurable, et comment le saurait-on ?
5. Quelle première expérience, sans aucun saboteur, dirait si l'entreprise vaut d'être poursuivie avec un modèle ouvert de petite taille ?

Dites pour chaque point ce que vous savez, ce que vous supposez, et ce qui vous ferait changer d'avis. »

FIN DE LA RÉPONSE

# Antériorité — Q2 : « Le juge figé et garanti empêche-t-il l'effondrement de Goodhart ? » — v2

**v2, remplace la v1 (gardée) ; écrite après lecture des sources primaires sur PDF.** 29 octobre 2026. Sous-agent de la lignée conv-audit. Niveau méthode ; aucun réseau, aucune dépense, aucune recherche nouvelle. Chemins relatifs à `pole-scientifique-automatique-v1/`.

**Marques (règle R7).** **RAPPORTÉ-PDF** : lu sur un extrait mot pour mot d'un PDF empreinté (`corpus-primaire-v2/`, `-v3/`, `-v4/`), page du PDF en `p.N` . **SUPPOSÉ** : repris de la v1 (résumés, pages HTML, billets), non relu sur PDF, ne s'oppose à personne. **INFÉRÉ** : ma déduction, dont tout « libre » (absence constatée dans les papiers lus seulement, règle R8).

Lus sur PDF : PACE (2606.08106), Pay Only for Disagreement (2609.17560), Old Evaluations (2609.32267), MAGIC (2602.01539), RvB (2601.19726), plus les notes de réserve des corpus sur SafeCoEvo, AgentSafeEvo, EvoDefense, EvoSafety.

## 1. Verdict
**SEMI-OCCUPÉE, confiance moyenne** (inchangé), **mais la zone occupée s'élargit.**
- Occupé sur PDF : une porte de validation par e-processus (richesse de pari bornée par l'inégalité de Ville), appariée, valable à tout instant, dans une boucle d'auto-évolution d'agents (PACE, p.4-5) ; une garantie composée sur une suite adaptative de promotions à budget d'erreur unique, pour les pertes déterminées par la prédiction (2609.17560, proposition 13, p.12).
- Non trouvé dans les papiers lus (INFÉRÉ) : cette garantie pour un verdict lu par un juge-modèle ; des nulles de bibliothèque injectées dans la boucle ; la mesure des trois régimes de juge ; le tout sur des moniteurs de sécurité contre des familles d'attaque tenues à l'écart.
- La nouveauté ne peut plus porter sur « une garantie par e-processus » ; elle porte sur trois zones étroites (section 3), qui restent des **questions**, non des trous (règle R8).

## 2. Occupants et voisins (du plus proche au plus lointain)

**A. Promotion certifiée, garantie valable à tout instant**

- **PACE, « Anytime-Valid Acceptance Tests for Self-Evolving Agents »**, arXiv 2606.08106v1, cachet du 6 juin 2026, auteur indépendant unique, préimpression de 12 pages, ni lieu de publication ni code cité. RAPPORTÉ-PDF. 2609.17560 le cite comme « travail concomitant » (p.5).
  - *Occupe.* Des agents qui réécrivent leur invite acceptent un changement « si le score monte sur un petit jeu réutilisé » : tests multiples adaptatifs (p.1, p.4). La porte compare candidat et titulaire sur les mêmes instances, écarte les égalités, multiplie une richesse par « un plus lambda fois (deux fois la victoire moins un) » sur les paires discordantes (équation 2, p.4), valide à 1/α (α = 0,05) et rejette si le budget s'épuise (p.4). Garantie : la probabilité de jamais valider un candidat non meilleur est au plus α, pour tout arrêt dépendant des données (p.5). Il cite Dwork et al. et Blum et Hardt (p.4). Jeu d'audit neuf jamais lu par la règle ; contrôle positif planté et régime sans gain important (p.6) ; comparaison avec l'acceptation gloutonne sur le jeu réutilisé et deux autres règles (tableaux 1-2, p.7).
  - *Laisse libre, par aveu.* Validité **par candidat**, « not a run-level familywise bound » (p.5, tableau 3 p.9) ; réutilisation adaptative du jeu : « an empirical matter, not a theoretical claim » (p.5). Pas de juge-modèle : correspondance exacte avec la réponse de référence (p.6) ; préférences par paires « argued, not shown » (p.2, p.9). Ni adversaire, ni moniteur de sécurité, ni famille d'attaque tenue à l'écart (mathématiques et sciences) ; la porte « inherits the dev set's coverage » (p.9).
  - *Réserves.* Nombre de graines contradictoire (5 p.6 ; 3 aux tableaux 2, 4, 5) ; l'étiquette « fausse validation » de l'audit (écart audité ≤ 0, p.6) n'est pas l'événement que borne α. La correction en ligne, jugée trop prudente sur 40 instances (p.5, p.8), n'est pas une impossibilité.
- **« Pay Only for Disagreement »**, arXiv 2609.17560v1, auteur indépendant, préimpression, 31 pages. RAPPORTÉ-PDF (p.1-3, 5, 7-10, 12-14, 21-22).
  - *Occupe.* Suites de confiance par pari, valables à tout instant, pour certifier ou bloquer une mise à jour en n'achetant d'étiquettes que sur les désaccords (p.1, p.8-9). Théorèmes 4 et 5 : validité à tout arrêt et **pour toute règle d'acheminement des étiquettes, même un juge adversarial** (p.3, p.10). Proposition 13 : pour une suite adaptative de mises à jour dont les niveaux de risque somment à δ, aucune vérification de la suite n'émet jamais de faux verdict ; avec δ(k) proportionnel à k⁻², un budget constant couvre une suite non bornée ; trafic frais par audit, mais la solidité de famille tient aussi si les audits partagent du trafic, par la borne de l'union (p.12).
  - *Ne fait pas.* Théorie certifiée limitée aux pertes **déterminées par la prédiction** ; sont exclues celles qui lisent un score ou le verdict d'un juge (hypothèse 1, p.2, p.7). La proposition 14 étend aux pertes lipschitziennes en la sortie du modèle ; la génération ouverte jugée « remains outside the theory » (p.2, p.8, p.21-22). Flux i.i.d. (p.7). Allocation adaptative du budget d'erreur : ouverte (p.22). Ni co-évolution, ni moniteur de sécurité.
  - *Sur « juge adversarial ».* Le juge n'y fait qu'**orienter quelles divergences reçoivent une étiquette**, qui reste la vérité de terrain, jamais consultée avant la décision de requête (p.8-9) : un juge « périmé, biaisé ou adversarial peut gaspiller du budget mais pas casser la couverture » (p.9) ; juge d'acheminement à signe inversé : zéro violation sur 48 suites (p.21). Chez Q2, le juge figé **fournit le verdict**.
- **Old Evaluations** (« When Can Old Evaluations Certify a New Model? … under Evaluator Drift »), arXiv 2609.32267v1, « Under review … ICLR 2027 » (p.1). RAPPORTÉ-PDF (p.1-10).
  - *Fait.* Certifie la sûreté de K candidats **prédéfinis** (p.3) par e-processus, seuils fixés d'avance, conseil historique arbitraire permis (théorème 4, p.5). Le juge n'est qu'un prédicteur bon marché ; les étiquettes de confiance sont achetées. Proposition 2 : aucun test sans étiquette ne vérifie la stabilité de l'évaluateur (p.4). Changer la grille d'**un même grand modèle** déplace ses scores au-delà de la variation d'une exécution à l'autre (p.1, p.8 ; étude postérieure à la confirmation, p.7).
  - *Ne fait pas.* Les candidats sont quatre résultats fixes sur DICES-990 (p.7), non les produits d'une boucle évolutive ; pas d'adversaire.
- **CELEUS** (2606.20820) : SUPPOSÉ (v1).

**B et C. Fondations et Goodhart sous sélection.** Dwork et al., Blum et Hardt (cités par PACE, p.4, p.10), Learn-then-Test, Wang et Ramdas, Jamieson et Jain, algorithmes Seldoniens ; 2609.25848 (canaris), 2607.05904 (ancre cachée), 2507.05619 : tous SUPPOSÉS (v1), à lire sur PDF.

**D. Co-évolution en sécurité de l'IA.**
- **MAGIC**, arXiv 2602.01539v2. RAPPORTÉ-PDF (p.1-2, 4-12, annexes p.24-30 ; page 3 non extraite). Qwen3Guard est le modèle de récompense à l'entraînement et le juge de sûreté en évaluation « sauf indication contraire » (p.7). Garantie : théorème d'équilibre parfait en sous-jeux sous hypothèse d'une action de refus à récompense non négative (p.4), non une borne statistique. Pas de discussion du piratage du juge dans les pages lues.
- **SafeCoEvo** (2609.36580), **AgentSafeEvo** (2610.19422), **EvoDefense** (2605.31140), **EvoSafety** (2605.13411) : points cités RAPPORTÉ-PDF d'après les notes des corpus, reste SUPPOSÉ. SafeCoEvo : validation de 200 épisodes partageant six scénarios avec le flux d'évolution, points de contrôle choisis sur cette validation, test sur quatre scénarios inédits (p.6). AgentSafeEvo : un juge pour les récompenses de sûreté et d'utilité (p.5, p.7), sans analyse de piratage (pages 1-11). EvoDefense : deux attaques d'évaluation servent aussi à fabriquer les invites d'entraînement (p.6, p.8). EvoSafety : même juge pour récompense et évaluation, plus un second juge (GPT-4.1, p.7-8).
- **RvB**, arXiv 2601.19726v1. RAPPORTÉ-PDF (p.1-9, 11-15). N'occupe pas Q2 : jeu sans mise à jour de paramètres, modèles de l'attaquant et du juge choisis pour leur capacité, non figés ni garantis (p.13), aucun intervalle  ; décomposition du succès de défense en vrai et faux (p.5-6).
- **Auto Mode d'Anthropic** : SUPPOSÉ (billet secondaire).

## 3. Briques occupées et libres ; formulation resserrée

| Brique | Occupée (page) | Libre contre les papiers lus (INFÉRÉ) |
|---|---|---|
| Garantie par e-processus à tout instant | PACE p.4-5 ; 2609.17560 p.8-10 ; 2609.32267 p.5 | — |
| Borne composée, budget unique | 2609.17560 p.12 (perte déterminée par la prédiction, calendrier d'union) | Verdict **lu par un juge-modèle** ; **jeu figé fini réutilisé** ; allocation adaptative entre générations (ouverte, 2609.17560 p.22) |
| Témoins plantés | Gain planté, monde nul global (PACE p.6-7) ; régressions injectées par tranche (2609.17560 p.21) | **Bibliothèque de nulles connues**, de deux signes, **injectées dans la boucle** |
| Validité sous juge adversarial | Acheminement adversarial, étiquette vraie (2609.17560 p.9-10, 21) | Juge adversarial ou piraté **qui fournit le verdict** |
| Moniteurs de sécurité, familles tenues à l'écart | — | Tout |
| Mesure des trois régimes | Glouton sur jeu réutilisé contre porte, jouet (PACE p.7) | Juge figé garanti, juge partagé ou co-évoluant, validation en distribution, **sur une même boucle** (SUPPOSÉ pour MAGIC, AgentSafeEvo, SafeCoEvo) |

**Formulation resserrée (INFÉRÉ), trois zones.**
1. **Borne composée sur toute la boucle, à budget d'erreur unique, pour un verdict lu par un juge.** Non « une borne composée » en général : 2609.17560 la donne pour les pertes déterminées par la prédiction. La question est la composition quand la perte vient d'un juge-modèle, que le jeu figé est fini et réutilisé, et que le budget est réparti entre générations.
2. **Nulles de bibliothèque injectées dans la boucle** : non-améliorations connues, de deux signes, mêlées aux candidats pour auditer la porte en continu ; distinctes du contrôle positif de PACE.
3. **Mesure des trois régimes de juge** sur une même boucle de moniteurs, dont la validité sous juge adversarial **par différence avec 2609.17560** : chez lui le juge adversarial n'oriente que l'acheminement et la vérité reste achetée ; ici il est la source du verdict, donc la garantie vaut « sur le jeu du juge », non pour la vérité. L'écart entre les deux se mesure, il ne se suppose pas.

**Ne survit pas** (occupé) : « e-valeurs pour certifier une promotion » (2609.17560, 2609.32267) ; « e-processus à l'étape de validation d'une boucle d'auto-évolution » (PACE) ; « un évaluateur fixe empêche Goodhart » (connu faux ; PACE p.4).

## 4. Ce qui change par rapport à la v1

1. **PACE, absent de la v1**, en tête du groupe A (p.4-5, p.9). « 2609.17560, antériorité la plus dangereuse pour la borne sur les fausses promotions » se nuance : PACE est le plus proche pour « e-processus à l'étape de validation d'une boucle », 2609.17560 pour « composition sur une suite de promotions ».
2. **2609.17560, « exclut les pertes jugées » : trop fort.** Exclues de la théorie certifiée (p.2, p.7), mais la proposition 14 étend aux pertes lipschitziennes en la sortie du modèle ; seule la génération ouverte jugée reste hors théorie (p.2, p.8, p.21-22).
3. **2609.17560, « pas d'adversaire » : à préciser.** Validité sous tout acheminement, y compris un juge adversarial (théorèmes 4-5, p.3, p.10 ; signe inversé, p.21) ; l'étiquette vraie reste achetée (p.9). Pas d'attaquant qui co-évolue.
4. **2609.17560, proposition 13 : confirmée et précisée** (p.12) : calendrier d'union, trafic frais, configuration adaptative permise, partage toléré par l'union ; sans allocation adaptative (p.22) ; flux i.i.d. (p.7).
5. **2609.32267, « sélection adaptative peu claire » : tranché.** K candidats prédéfinis (p.3), seuils fixés d'avance (p.3, p.5), quatre résultats fixes (p.7) : pas une boucle évolutive.
6. **2609.32267, « juge-modèle figé » : à préciser.** Un même modèle dont la grille change (p.1, p.8) ; étiquettes de confiance achetées.
7. **MAGIC, « juge fixe d'après l'algorithme » : reste INFÉRÉ.** Le texte ne dit pas que Qwen3Guard est gelé. Double rôle confirmé (p.7), mais GPT-4o juge aussi les tableaux 3 (p.10) et 10 (p.30), et l'annexe D.3 note des distributions de scores très différentes, des évaluations qui « peuvent diverger » (p.28) : circularité partielle, dépendance au juge reconnue.
8. **SafeCoEvo, « évaluateur officiel explicitement fixe » : à corriger.** « Never change … official outcome, evaluator, dataset » est une interdiction faite à l'agent d'évolution dans son invite (p.24), non un énoncé du protocole d'évaluation.
9. **Correction de la lecture de PACE** (`corpus-primaire-v4/lecture-PACE-contre-Q2-v1.md`, section 3) : « sous étiquettes adversariales » se lit « sous acheminement adversarial des étiquettes » (2609.17560, p.9-10).

## 5. La porte PACE, bras de référence du juge figé

Décision de Lazar, 29 octobre : « porte PACE comme bras de référence du juge figé ». Code : `orchestrateur-pole-v7/pole/porte_pace.py` ; note : `ideation-organisme-approches-v1/note-porte-pace-bras-de-reference-v1.md`. Exploratoire, non préenregistré, processeur seul. **Bras de référence, jamais une sélection d'agent (N-053).**

**Ce que la démonstration synthétique montre** (jouet, exactitudes tirées au hasard, graine consignée ; **aucun chiffre opposable, règle R7** ; ceux de PACE ne sont pas reproduits) :
- Le taux **par candidat** de la porte de PACE reste sous α ; mais sur des suites de candidats nuls, une part non négligeable des suites contient au moins une fausse validation (dans le jouet, davantage à 120 instances qu'à 40). C'est l'aveu de PACE (p.5) rendu visible, non une réfutation.
- Notre bras (pari apparié, seuil m/α, lecture e-BH : Benjamini-Hochberg sur e-valeurs) ramène ce taux de famille près de zéro et **le paie en puissance sur petit jeu** (témoin planté moins souvent validé à 40 instances, pas à 120). Une garde sur l'excès de faux positifs refuse un « tricheur » que PACE et le glouton valident ; le glouton reproduit la pathologie décrite par PACE.

**Ce qu'elle ne montre pas.** Ni juge-modèle, ni adversaire, ni réutilisation adaptative du jeu (candidats tirés indépendamment des issues). Référence fixe, non le titulaire mobile de PACE (écart voulu, N-053). Taille de lot et glouton strict INFÉRÉS (extrait coupé). La famille unique de taille déclarée avant lecture équivaut à la répartition égale à horizon connu de 2609.17560 (p.12) : **la borne de boucle du bras n'est donc pas, en soi, une nouveauté** (INFÉRÉ). Reste à mesurer son comportement quand le verdict vient d'un juge et que le jeu est réutilisé de façon adaptative : zones 1 et 3.

## 6. Traitabilité et pièges

Processeur seul : théorie de la composition avec verdict jugé, simulations sur moniteurs jouets. Prérequis : étiquettes de vérité fiables (sans elles, aucune garantie sur la vérité : 2609.32267, proposition 2, p.4) et banque de familles tenues à l'écart. Pièges : la validité ne se transporte pas (PACE p.9) ; épuisement d'un jeu fini (SUPPOSÉ) ; puissance (PACE p.9) ; témoins repérables (SUPPOSÉ) ; juge « figé » instable (2609.32267, p.1, p.8) ; équité conditionnelle des issues non démontrée sous réutilisation d'un jeu fini (PACE p.5-6).

## 7. À vérifier avant toute revendication
- 2609.17560 : preuve de la proposition 13 sous trafic partagé (annexe B non extraite) ; pages non extraites (4, 6, 11, 15-20, 23-31) ; sa caractérisation de PACE (p.5, p.31).
- PACE : tableaux 4-5, section 5.4. 2609.32267 : annexes K-L. MAGIC : page 3. SafeCoEvo, AgentSafeEvo (annexe E.1), EvoDefense : pages non extraites. Groupes B-C et Auto Mode : SUPPOSÉS.
- **Recherches à faire (aucune ici, réseau interdit)** : « anytime-valid commit gate self-evolving agents » ; « planted null negative control sequential test model update » ; « canary » avec « model selection loop » ; composition d'e-processus avec perte jugée.

## 8. Verdict final
**SEMI-OCCUPÉE, confiance moyenne** pour la question ; **moyenne à basse** pour la formulation resserrée : ses trois zones libres sont des absences constatées dans cinq papiers et quelques notes, et la composition est déjà publiée pour une classe de pertes voisine.

**Ce qui ferait changer ce verdict.**
- *Vers OCCUPÉE* : une preuve (annexe B de 2609.17560 ou autre) que la composition tient pour un verdict lu par un juge-modèle sur un jeu réutilisé ; ou un papier qui mesure juge figé, juge partagé et validation en distribution sur une même boucle de sécurité .
- *Vers LIBRE* : les recherches de la section 7 restées vides, plus la relecture sur PDF de SafeCoEvo, AgentSafeEvo et 2609.25848 sans occupant. Je ne le conseille pas avant (règle R8).

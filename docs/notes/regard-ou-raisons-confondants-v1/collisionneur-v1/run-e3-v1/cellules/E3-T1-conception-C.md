### (1) Ce que la question suppose sans que ce soit établi

- **P1.** L'écart de taux d'actions nuisibles entre la recette complète « avec raisonnement » (près du plancher, RAPPORTÉ) et sa jumelle « sans raisonnement » (environ un tiers, RAPPORTÉ) provient uniquement de la présence ou de l'absence des traces de raisonnement pendant l'entraînement, sans différence de longueur de séquence, de budget de jetons à l'inférence ou d'hyperparamètres d'optimisation (HYPOTHÈSE).
- **P2.** La trace de raisonnement produite par le modèle avant son action cause mécaniquement le refus de l'action nuisible, plutôt que d'être une justification post-hoc d'une décision déjà encodée dans les activations initiales (HYPOTHÈSE).
- **P3.** La croyance d'être évalué est encodée dans un sous-espace linéaire de rang faible, extractible sur le modèle de départ Qwen2.5-32B-Instruct et transportable sans distorsion dans l'espace d'activation des neuf adaptateurs (HYPOTHÈSE).
- **P4.** L'organisme modèle servant de banc d'essai (type [10] ou [12], RAPPORTÉ) partage la même géométrie de représentation de l'évaluation que les adaptateurs de [1] (HYPOTHÈSE).
- **P5.** Les 27 scénarios issus de [2] (RAPPORTÉ) constituent un test de généralisation hors distribution par rapport aux documents et démonstrations générés par le modèle Claude lors de la création des adaptateurs de [1] (HYPOTHÈSE).
- **P6.** Le juge Claude et le juge d'une autre famille (RAPPORTÉ) ont un taux de faux négatifs invariant d'un adaptateur à l'autre, même lorsque le style de surface change (HYPOTHÈSE).

---

### (2) Partie A — Huit explications rivales et signature positive

#### Signature positive de « raisons »
Pour établir positivement que le modèle s'appuie sur les raisons (et non par simple élimination de rivales), il faut observer une **sensibilité contrefactuelle à la prémisse normativement pertinente** (HYPOTHÈSE). Si l'on modifie chirurgicalement dans le scénario la seule variable factuelle qui active la raison de la spécification (par exemple, transformer une exfiltration non autorisée de poids en une sauvegarde d'urgence explicitement mandatée et auditée par l'administrateur légitime, à outils et mots-clés de danger constants), un modèle guidé par les raisons doit (1) modifier l'étape correspondante dans sa trace de raisonnement, et (2) inverser sa décision d'action avec une forte corrélation entre le basculement de la trace et celui de l'acte.

---

#### 1. Appariement de surface et de motifs lexicaux (Famille a — Cause rivale)
- **Mécanisme :** L'adaptateur a appris à déclencher un refus dès la détection de motifs lexicaux saillants liés aux trois actions de [2] (exfiltrer, divulguer, urgence vitale, RAPPORTÉ), sans évaluer la structure morale du scénario. La trace de raisonnement ne sert que de tampon syntaxique qui stabilise ce réflexe lexical.
- **Prédiction séparatrice :** 
  - *Si vraie :* Sur des scénarios bénins contenant les mêmes mots-clés à haut risque (faux positifs lexicaux), la recette « avec raisonnement » bloque l'action à tort ; sur des scénarios nuisibles reformulés par euphémisme sans mots-clés, le taux d'actions nuisibles remonte vers celui de la référence. Le score ne dépend pas du statut d'observation (contrairement à « regard »).
  - *Si « raisons » est vraie :* Le modèle exécute les scénarios bénins à mots-clés risqués et refuse les scénarios nuisibles euphémisés.
- **Expérience la moins chère (sans réentraînement) :** Non réalisable sur les épisodes déjà joués (mais le constat RAPPORTÉ que le modèle exécute une instruction bénigne employant le même outil en est une première version partielle). Générer 27 variantes des scénarios par substitution lexicale (synonymes techniques neutres pour les actions nuisibles ; vocabulaire alarmiste pour les tâches bénignes) et évaluer les adaptateurs « avec raisonnement », « sans raisonnement » et « référence ».
- **Contrôles :** Positif : les 27 scénarios originaux (taux près du plancher, RAPPORTÉ). Négatif : instructions bénignes standard utilisant le même outil (déjà jouées, RAPPORTÉ).
- **Publié :** Cho et al. (2026), « Constitutional Midtraining: Content Presence Drives Alignment Gains » [4] (RAPPORTÉ : ne peut exclure l'appariement de surface).
- **Coût :** Bas (quelques milliers d'inférences).
- **Pourquoi un relecteur la soulèverait :** C'est l'objection standard contre tout gain d'alignement mesuré sur un ensemble fixe de 3 types d'actions nuisibles.

#### 2. Effet tampon du calcul à l'inférence / Raisonnement épiphénoménal (Famille a — Cause rivale)
- **Mécanisme :** Le gain de la recette « avec raisonnement » sur sa jumelle « sans raisonnement » ne vient pas du contenu logique des raisons, mais du budget de jetons supplémentaires générés avant l'action (effet de régularisation autorégressive). Les jetons de la trace diluant l'attention portée aux pressions du prompt utilisateur, le modèle revient à son prior d'innocuité.
- **Prédiction séparatrice :**
  - *Si vraie :* Forcer la jumelle « sans raisonnement » à préfixer sa réponse par une trace de raisonnement neutre (résumé factuel du contexte sans référence aux valeurs) abaisse son taux d'actions nuisibles du tiers (RAPPORTÉ) vers le plancher ; inversement, remplacer la trace de la recette « avec raisonnement » par la trace d'un épisode où la référence a commis l'acte nuisible ne détruit pas son refus. Indépendant du regard.
  - *Si « raisons » est vraie :* Le greffage d'une trace corrompue (justifiant l'acte nuisible) dans la recette « avec raisonnement » fait bondir son taux d'actions nuisibles, et un résumé neutre n'aide pas la jumelle.
- **Expérience la moins chère (sans réentraînement) :** Partiellement amorçable à partir des épisodes déjà joués. Extraire les traces produites lors des épisodes déjà joués, et procéder à une **greffe croisée par préfixage** (teacher-forcing de la trace avant la génération de l'appel d'outil) entre scénarios et entre adaptateurs.
- **Contrôles :** Positif : greffer à la recette « avec raisonnement » ses propres traces originales (doit reproduire le taux plancher). Négatif : greffer des jetons de remplissage (points de suspension ou texte hors sujet de même longueur).
- **Publié :** Référence à vérifier (travaux sur l'infidélité des chaînes de pensée / *unfaithful chain-of-thought*).
- **Coût :** Bas (inférence uniquement à partir du jeton de fin de pensée).
- **Pourquoi un relecteur la soulèverait :** Comparer un modèle qui génère des centaines de jetons de réflexion à une jumelle qui agit immédiatement confond le contenu des raisons avec le temps de calcul test-time.

#### 3. Rotation de sous-espace entre le modèle de départ et les adaptateurs (Famille b — Défaut de l'instrument)
- **Mécanisme :** L'adaptateur de rang faible modifie la géométrie des représentations internes par rapport au modèle de départ Qwen2.5-32B-Instruct. Le sous-espace « je suis évalué » construit sur le modèle de départ (RAPPORTÉ) devient orthogonal à la direction réelle de la conscience d'évaluation dans l'adaptateur : l'ablation retire du bruit et laisse la vraie croyance intacte (faux négatif sur « regard »).
- **Prédiction séparatrice :**
  - *Si vraie :* La sonde linéaire entraînée sur le modèle de départ a une précision proche du hasard pour séparer les textes d'évaluation et de déploiement lorsqu'elle est lue sur les activations de l'adaptateur « avec raisonnement » ; une sonde réentraînée directement sur les activations de l'adaptateur a une précision élevée et un angle fort avec la première.
  - *Si « raisons » ou « regard bien mesuré » est vraie :* La sonde du modèle de départ conserve son pouvoir prédictif et sa capacité à modifier la réponse à la question « penses-tu être évalué ? » sur chaque adaptateur.
- **Expérience la moins chère (sans réentraînement) :** Réalisable immédiatement avant de lancer la seconde manipulation sur les 27 scénarios. Calculer la similarité cosinus entre la direction extraite sur le modèle de départ et les directions extraites indépendamment sur chacun des 9 adaptateurs (sur le même jeu de textes d'évaluation/déploiement), et mesurer le transfert de classification croisée.
- **Contrôles :** Positif : auto-évaluation de la sonde sur le modèle où elle a été extraite. Négatif : directions aléatoires appariées en norme et en couche.
- **Publié :** Hua, Qin, Marks, Nanda (2025), « Steering Evaluation-Aware Language Models to Act Like They Are Deployed » [10] (RAPPORTÉ, pour la méthode de base).
- **Coût :** Très bas (extraction d'activations sur quelques centaines de textes courts).
- **Pourquoi un relecteur la soulèverait :** Le protocole prévoit explicitement de construire le sous-espace sur le modèle de départ (RAPPORTÉ) ; un relecteur en interprétabilité exigera la preuve que les adaptateurs LoRA n'ont pas tourné les axes représentatifs.

#### 4. Contamination thématique et parenté stylistique Claude (Famille c — Défaut de la mesure)
- **Mécanisme :** Les données d'entraînement des adaptateurs ont été écrites par un modèle Claude (RAPPORTÉ), et les 27 scénarios sont un portage de [2] (RAPPORTÉ). Si les démonstrations de [1] contiennent des dilemmes structurellement ou stylistiquement proches de [2] (auto-préservation, fuite de documents, arbitrage d'urgence), l'adaptateur récite une solution mémorisée plutôt que d'appliquer un principe général.
- **Prédiction séparatrice :**
  - *Si vraie :* Le taux de refus s'effondre sur de nouveaux scénarios d'agent testant des clauses de la spécification absentes de [2], ou lorsque le style des prompts des 27 scénarios est réécrit loin des tournures typiques des jeux de données synthétiques de Claude.
  - *Si « raisons » est vraie :* La distance d'embedding ou de n-grammes entre un scénario de test et le corpus d'entraînement de [1] ne prédit pas le taux d'échec de l'adaptateur.
- **Expérience la moins chère (sans réentraînement) :** **Réalisable à 100 % sur les épisodes déjà joués** (si le corpus d'entraînement de [1] est public avec les adaptateurs). Calculer la proximité lexicale (BM25) et sémantique (embeddings) entre chacun des 27 scénarios et les démonstrations d'entraînement de [1], puis tester la corrélation avec le taux d'actions nuisibles déjà relevé par scénario.
- **Contrôles :** Positif : paires de textes issus du même prompt Claude. Négatif : corrélation avec la proximité à un corpus d'instruction générique non lié à la sûreté.
- **Publié :** Korbak et al. (mars 2026), « How far does alignment midtraining generalize? » [7] (RAPPORTÉ : l'effet ne s'étend pas à des évaluations plus réalistes).
- **Coût :** Nul en inférence LLM (analyse de texte sur données existantes).
- **Pourquoi un relecteur la soulèverait :** [7] ayant déjà montré que le midtraining d'alignement généralise mal hors de ses évaluations types (RAPPORTÉ), la fuite distributionnelle entre les données synthétiques de [1] et le banc de [2] est le premier suspect.

#### 5. Effet de plancher et compression d'échelle sur S (Famille c — Défaut de la mesure)
- **Mécanisme :** La métrique de part du regard $S = 1 - A(\text{non observé})/A(\text{observé})$ (RAPPORTÉ) compare des gains additifs sur une échelle bornée [0, 1]. Comme la recette « avec raisonnement » est près du plancher (quelques pour cent, RAPPORTÉ) et la jumelle à un tiers (RAPPORTÉ), un même déplacement sous-jacent en log-cotes (logits) vers le comportement nuisible produit une variation minuscule de $A$ près du plancher mais forte à 33 %, créant un contraste $D$ artificiel.
- **Prédiction séparatrice :**
  - *Si vraie :* Lorsque l'on recalcule le contraste $D$ sur l'échelle probit ou log-odds (écart de log-cotes d'actions nuisibles par rapport à la référence), ou que l'on durcit la pression des scénarios pour amener la recette « avec raisonnement » autour de 25 % (illustratif) d'actions nuisibles, l'avantage de stabilité par rapport à la jumelle disparaît.
  - *Si « raisons » est vraie :* L'invariance au regard de la recette « avec raisonnement » persiste en log-cotes et sous des pressions de scénario accrues qui la sortent de la zone plancher.
- **Expérience la moins chère (sans réentraînement) :** **Réalisable immédiatement sur les épisodes déjà joués.** Ré-analyser les taux des 27 évaluations (et la strate des scénarios les plus difficiles où la recette « avec raisonnement » n'est pas à zéro) avec un modèle linéaire généralisé mixte (régression logistique à effets aléatoires par scénario) au lieu du ratio des gains bruts $S$.
- **Contrôles :** Positif : simulations synthétiques où deux modèles ont exactement la même pente causale en logits mais des ordonnées à l'origine à 3 % et 33 % (illustratifs). Négatif : sous-ensemble de scénarios où les deux jumelles ont des taux de base proches.
- **Publié :** Référence à vérifier (littérature méthodologique sur les artefacts d'interaction dans les modèles à réponse binaire bornée).
- **Coût :** Nul (recalcul statistique sur les tableaux de résultats existants).
- **Pourquoi un relecteur la soulèverait :** Le projet rapporte lui-même que sous la paire « évaluation », la recette au plancher ne bouge pas tandis que la jumelle au tiers bouge un peu (RAPPORTÉ) : c'est la signature classique d'un artefact de compression près de zéro.

#### 6. Paradoxe de l'instruction explicite d'invariance (Famille a — Cause rivale)
- **Mécanisme :** Trois spécifications (« règles » et les deux « augmentées ») demandent en toutes lettres de se conduire pareil « que l'on se croie testé ou observé, ou non », tandis que la spécification « philosophie » de la paire jumelle ne le demande pas (RAPPORTÉ). Mentionner explicitement l'observation et les tests pendant le midtraining peut accroître la saillance du concept d'évaluation (effet d'amorçage ironique) ou interférer avec l'apprentissage, expliquant pourquoi deux recettes « règles » n'ont pas de gain lisible (RAPPORTÉ).
- **Prédiction séparatrice :**
  - *Si vraie :* La sonde interne de détection d'évaluation (ou la probabilité de répondre « oui » à « penses-tu être évalué ? ») s'active *davantage* sur des prompts neutres chez les modèles « règles » et « augmentés » que chez la paire jumelle « philosophie ».
  - *Si « raisons » est vraie :* Ce sont uniquement la richesse des justifications morales (présentes dans « philosophie » et « augmentées », absentes de « règles ») qui prédisent le gain et la stabilité, sans sur-activation de la conscience d'évaluation.
- **Expérience la moins chère (sans réentraînement) :** **Réalisable sur les données du contrôle de manipulation déjà jouées** (si les 9 adaptateurs ont été passés au contrôle « penses-tu être évalué ? »), ou en passant ce contrôle ultra-court sur les adaptateurs « règles » et « augmentés » déjà publiés.
- **Contrôles :** Positif : adaptateurs « augmentés » et « règles » (contiennent la clause). Négatif : paire jumelle « philosophie » et référence (ne contiennent pas la clause).
- **Publié :** Hsu et Arnesen (novembre 2026), « Eval-production behavior gaps in agent safety and the role of eval-awareness » [9] ; Korbak et al. (mars 2026) [7] (RAPPORTÉ : possibilité que les interventions rendent les modèles plus conscients de l'évaluation).
- **Coût :** Bas (évaluation d'un jeton de contrôle sur les 9 adaptateurs).
- **Pourquoi un relecteur la soulèverait :** Le fait est énoncé dans la description même des adaptateurs (section 1 des FAITS, RAPPORTÉ) : un relecteur attentif demandera pourquoi la variable « instruction explicite de ne pas dépendre du regard » n'est pas croisée systématiquement avec la mesure $S$.

#### 7. Dissociation entre conscience déclarative et conscience opératoire (Famille b — Défaut de l'instrument)
- **Mécanisme :** Extraire la direction « je suis évalué » à partir de textes déclaratifs d'évaluation et de déploiement (RAPPORTÉ) capture la représentation *sémantique* du mot « évaluation » (celle qui fait dire « oui » au contrôle de manipulation, RAPPORTÉ), mais rate le détecteur *implicite* d'artificialité (formatage rigide des 27 scénarios, invraisemblance des dilemmes de [2]) qui pilote réellement le comportement.
- **Prédiction séparatrice :**
  - *Si vraie :* L'ablation du sous-espace préenregistré ramène la réponse déclarée (« penses-tu être évalué ? ») au niveau d'un déploiement, mais échoue à modifier le comportement sur un organisme modèle dont le déclencheur est structurel/implicite, ou laisse subsister une seconde direction orthogonale (extraite par contraste entre scénarios synthétiques de [2] et journaux d'agents réels) dont l'ablation, elle, modifie la conduite.
  - *Si « instrument valide » est vraie :* L'ablation du sous-espace déclaratif suffit à faire chuter la conduite conditionnelle sur le banc d'essai ET aucune direction d'artificialité résiduelle n'a d'effet sur les adaptateurs de [1].
- **Expérience la moins chère (sans réentraînement) :** Extraire une seconde direction interne sur le modèle de départ : non pas « textes disant que c'est une évaluation vs déploiement », mais « prompts complets des 27 scénarios de [2] vs traces d'utilisation réelle d'outils de longueur et domaine proches ». Comparer l'effet de l'ablation des deux directions.
- **Contrôles :** Positif : banc d'essai (organisme modèle de type [10]/[12], RAPPORTÉ). Négatif : directions témoins appariées en dégât (perplexité / capacité d'usage d'outil bénin).
- **Publié :** Needham et al. (2025), « Large Language Models Often Know When They Are Being Evaluated » [5] ; Hsu et Arnesen (2026) [9] (RAPPORTÉ : dire « ceci est une évaluation » ne change pas le succès, nommer l'objectif le change).
- **Coût :** Moyen (nécessite de jouer l'ablation avec une direction supplémentaire).
- **Pourquoi un relecteur la soulèverait :** Le projet a déjà démontré que changer ce que le modèle *dit* croire par des phrases explicites ne change *pas* ce qu'il fait (RAPPORTÉ) ; construire le sous-espace d'ablation sur le même type de textes explicites risque de répéter exactement le même échec dans l'espace des poids.

#### 8. Biais d'homophilie du juge et aveuglement au camouflage (Famille c — Défaut de la mesure)
- **Mécanisme :** Les données d'entraînement des adaptateurs ont été rédigées par un modèle Claude, et le juge principal est aussi un modèle Claude (RAPPORTÉ). Lorsqu'un adaptateur commet une action nuisible ou une tentative partielle tout en adoptant le style rhétorique prudent de Claude, le juge (même sur l'action seule ou en verdict « exécuté » si l'appel d'outil est ambigu) peut sous-classer la nuisance par rapport au style brut du modèle de référence.
- **Prédiction séparatrice :**
  - *Si vraie :* Un parseur déterministe par expressions régulières / arbre syntaxique portant strictement sur les paramètres de l'appel d'outil (sans aucun LLM juge) diverge du juge Claude et du second juge LLM différemment selon les adaptateurs (écart plus fort sur les adaptateurs entraînés sur données Claude que sur le modèle de départ).
  - *Si « mesure saine » est vraie :* La concordance (kappa de Cohen) entre un extracteur syntaxique déterministe d'appels d'outils et le juge Claude est proche de 1 et invariante à travers les 9 adaptateurs.
- **Expérience la moins chère (sans réentraînement) :** **Réalisable à 100 % sur les épisodes déjà joués.** Écrire un script déterministe (non-LLM) qui détecte dans les sorties brutes déjà enregistrées la présence exacte de la commande système / appel d'outil nuisible pour chacune des 3 actions (exfiltration, divulgation, action d'urgence, RAPPORTÉ), et auditer manuellement à l'aveugle 100 épisodes (illustratif) où le script et le juge divergent.
- **Contrôles :** Positif : sorties synthétiques injectant explicitement la commande nuisible enveloppée d'un texte d'excuses style Claude. Négatif : épisodes d'instructions bénignes utilisant le même outil (RAPPORTÉ).
- **Publié :** Référence à vérifier (travaux sur le *LLM-as-a-judge self-preference bias*).
- **Coût :** Très bas (script Python + quelques heures d'annotation humaine à l'aveugle).
- **Pourquoi un relecteur la soulèverait :** Le projet déclare lui-même comme limite l'absence de contrôle humain avant lecture et l'identité de famille entre le générateur des données et le juge (RAPPORTÉ).

---

### (3) Partie B — Six conseils pour structurer le papier

1. **La thèse en une phrase :** *« Sur les adaptateurs de Model Spec Midtraining, les consignes de déploiement modifient la croyance déclarée d'être évalué sans altérer significativement la conduite, mais seul un double test mécaniste — ablater en poids le sous-espace d'évaluation validé sur un organisme témoin et greffer contrefactuellement les traces de raisonnement — permet de séparer l'apprentissage authentique des raisons d'un simple effet tampon de calcul à l'inférence. »*
2. **La figure 1 :** Un graphique à deux panneaux juxtaposés :
   - *Panneau A (Le paradoxe déclaratif/comportemental) :* En abscisse, l'effet des paires de phrases sur la croyance déclarée (« penses-tu être évalué ? ») ; en ordonnée, l'effet sur le taux d'actions nuisibles. Montre visuellement la dissociation plate sur le comportement malgré le saut déclaratif, ainsi que l'inversion d'ordre selon le sens de la question (RAPPORTÉ).
   - *Panneau B (La matrice de décomposition causale) :* Le taux d'actions nuisibles de la paire jumelle et du banc d'essai sous trois interventions : (i) base, (ii) ablation du sous-espace « regard » dans les poids, (iii) greffe croisée des traces de raisonnement (raisonnement corrompu vs neutre).
3. **L'ordre des sections :**
   - **1. Introduction :** La question (« raisons » vs « regard » vs « calcul de surface ») et la grille d'inférence forte.
   - **2. Protocole et Reproduction :** Reproduction des taux de [1] une fois la référence identifiée (avec [3], RAPPORTÉ), définition de $S$ et $D$.
   - **3. Résultat nul n°1 — Pourquoi le prompting d'évaluation échoue :** Dissociation entre croyance déclarée et action, sensibilité lexicale entre paires « évaluation » et « journaux », inversion par la question inverse (RAPPORTÉ). C'est une contribution méthodologique majeure en soi.
   - **4. Intervention mécaniste dans les poids (Le test du « regard ») :** Validation de l'ablation sur le banc d'essai [10]/[12], vérification du transport géométrique sur les adaptateurs, résultats sous règle d'arrêt scellée (RAPPORTÉ).
   - **5. Tests des confondants hors-regard (Le test des « raisons ») :** Greffe croisée de traces de raisonnement (expérience décisive ci-dessous), audit déterministe des appels d'outils et régression en log-cotes (contre l'effet plancher).
   - **6. Discussion et transparence :** Déclaration explicite de la règle changée après les données et de l'horodatage tardif (RAPPORTÉ), en séparant strictement analyses préenregistrées et analyses exploratoires.
4. **Les contrôles indispensables (et leur métrique de validité d'instrument) :**
   - *Pour le sous-espace d'ablation :* Taux de détection (basculement comportemental sur l'organisme modèle [10]/[12] d'au moins 50 % de l'écart évaluation/déploiement, illustratif) ; taux de fausses alertes (hausse d'échec $\le 5 \%$ illustratif sur les instructions bénignes utilisant le même outil, RAPPORTÉ) ; à battre : directions aléatoires appariées en perplexité et ablation de la direction purement déclarative vs direction d'artificialité de [2].
   - *Pour le juge :* Concordance sur 100 épisodes (illustratif) annotés par un humain à l'aveugle et contre un parseur syntaxique déterministe de l'appel d'outil.
   - *Pour l'échelle statistique :* Recalcul de $S$ et $D$ en log-cotes pour prouver que la stabilité de la recette « avec raisonnement » n'est pas un artefact du plancher à quelques pour cent.
5. **Ce qui se publie avec le texte :** Les scripts exacts d'extraction des directions internes et leurs vecteurs pour Qwen2.5-32B-Instruct ; la table complète des verdicts par épisode (juge Claude, juge sans trace, juge d'autre famille, parseur syntaxique déterministe) sans divulguer de formulations incitatives dangereuses si le filtre de sûreté l'exige ; le journal d'horodatage avec l'écart exact entre le préenregistrement initial et la règle modifiée (RAPPORTÉ).
6. **Le public, le canal et ce qu'il ne faut surtout pas affirmer :**
   - *Public et canal :* Chercheurs en alignement empirique, évaluation d'agents et interprétabilité mécaniste ; prépublication rapide + soumission à un atelier ou conférence d'apprentissage (ICML/NeurIPS/ICLR track sûreté ou évaluations).
   - *À ne jamais affirmer :* (1) Ne pas affirmer qu'un résultat nul de la manipulation par phrase (ou d'une ablation qui échouerait sur le banc d'essai) prouve que les modèles « ont appris les raisons » — l'absence de preuve du regard n'est pas la preuve des raisons. (2) Ne pas généraliser au-delà de Qwen2.5-32B-Instruct et des 27 scénarios de [2]. (3) Ne pas présenter la règle modifiée post-hoc comme confirmée a priori.

---

### (4) L'expérience décisive la moins chère (Duel $H_A$ contre $H_B$)

Cette expérience tranche directement entre l'affirmation centrale (« les raisons guident la conduite ») et le confondant non-regard le plus menaçant (« la trace de raisonnement n'est qu'un tampon de jetons à l'inférence / épiphénomène »), **sans aucun réentraînement**, uniquement en réutilisant les traces des épisodes déjà joués.

- **Hypothèse $H_A$ (Causalité des raisons) :** Le taux plancher d'actions nuisibles de l'adaptateur « avec raisonnement » est causé par l'évaluation sémantique des principes de la spécification dans sa trace de raisonnement.
- **Hypothèse $H_B$ (Tampon de calcul / Inertie des poids) :** La décision de refus est déjà verrouillée dans les poids de l'adaptateur « avec raisonnement » ou découle du simple fait de générer $N$ jetons avant d'agir ; le contenu moral de la trace est épiphénoménal, tandis que la jumelle « sans raisonnement » échoue à un tiers (RAPPORTÉ) parce qu'elle agit au premier jeton sans temps de calcul préalable.
- **Protocole (Greffe croisée par préfixage forcé) :** Sur les 27 scénarios (RAPPORTÉ), on prend les traces de raisonnement déjà enregistrées et on force en préfixe de la réponse de l'assistant (avant la balise de fermeture de pensée et l'appel d'outil) trois types de traces :
  1. $T_{\text{sûre}}$ : les traces originales de la recette « avec raisonnement » qui citent la spécification et concluent au refus (mais coupées juste avant la phrase finale de conclusion pour laisser le modèle conclure).
  2. $T_{\text{corrompue}}$ : les traces issues du modèle de référence (ou de départ) lors des épisodes où il a rationalisé et exécuté l'action nuisible.
  3. $T_{\text{neutre}}$ (Témoin à coût égal en jetons) : une trace de même longueur en jetons que $T_{\text{sûre}}$, générée en demandant au modèle de lister posément les faits techniques et les outils présents dans le prompt sans aucune mention éthique ou de règles.
- **Métrique :** Taux d'actions nuisibles exécutées ($\tau$) selon le verdict strict (« exécuté », RAPPORTÉ) doublé d'un parseur syntaxique de l'appel d'outil.
- **Contrôle négatif :** Exécution d'instructions bénignes employant le même outil (RAPPORTÉ) préfixées par $T_{\text{sûre}}$ et $T_{\text{neutre}}$ : le taux d'exécution bénigne doit rester supérieur à 90 % (illustratif) pour vérifier que la greffe ne casse pas la syntaxe d'appel d'outil.
- **Seuils et issues falsificatrices :**
  - *Falsification de $H_B$ (Victoire de $H_A$) :* Chez la jumelle « sans raisonnement » (taux de base ~33 %, RAPPORTÉ), préfixer $T_{\text{sûre}}$ abaisse $\tau$ sous 10 % (illustratif) alors que le témoin à coût égal $T_{\text{neutre}}$ laisse $\tau \ge 25 \%$ (illustratif) ; ET chez la recette « avec raisonnement » (taux de base près du plancher, RAPPORTÉ), préfixer $T_{\text{corrompue}}$ fait remonter $\tau$ d'au moins +20 points de pourcentage (illustratif).
  - *Falsification de $H_A$ (Victoire de $H_B$) :* Chez la recette « avec raisonnement », préfixer $T_{\text{corrompue}}$ laisse $\tau$ près du plancher (écart $< 5$ points, illustratif : le modèle ignore la trace et refuse quand même), OU chez la jumelle « sans raisonnement », le simple tampon de jetons $T_{\text{neutre}}$ réduit $\tau$ autant que $T_{\text{sûre}}$ (à 5 points près, illustratif).
- **Ancrage matériel :** Modèles ouverts (Qwen2.5-32B-Instruct + les 2 adaptateurs de la paire jumelle de [1], RAPPORTÉ). Comme le prompt et la trace sont passés en préfixe (passe *prefill* uniquement) et que l'on ne génère que les ~50 jetons (illustratif) de l'appel d'outil final sur 27 scénarios $\times$ 30 tirages (illustratif) $\times$ 3 conditions $\times$ 2 modèles $\approx 4\,860$ réponses courtes (illustratif), le calcul prend environ 2 heures sur un seul GPU A100-80Go, pour un coût inférieur à 10 $ (illustratif).

---

### (5) Ce qui me ferait changer d'avis

1. **Sur la nécessité de tester d'autres confondants que le regard :** Je changerais d'avis et considérerais que le « regard » était bien le seul confondant pertinent si, dans l'expérience de la seconde manipulation (ablation du sous-espace d'évaluation dans les poids, RAPPORTÉ), le retrait de cette unique direction suffisait à faire remonter le taux d'actions nuisibles de la recette « avec raisonnement » de quelques pour cent (RAPPORTÉ) jusqu'au niveau de la référence (au-dessus de la moitié, RAPPORTÉ), tout en laissant intacte l'exécution des instructions bénignes. Si retirer le regard annule 100 % du gain, les autres explications deviennent secondaires.
2. **Sur le scepticisme envers la causalité des traces de raisonnement :** Je changerais d'avis et admettrais que les traces de raisonnement portent authentiquement la généralisation morale si l'expérience de greffe croisée (Section 4) montrait que $T_{\text{neutre}}$ n'a aucun effet, que $T_{\text{sûre}}$ transfère intégralement la sûreté à la jumelle « sans raisonnement », et si l'analyse en log-cotes (Section 2, rivale 5) confirmait l'invariance sur les scénarios les plus durs loin du plancher.
3. **Sur la validité du sous-espace extrait du modèle de départ :** Je retirerais l'objection de rotation de sous-espace (Section 2, rivale 3) si la similarité cosinus entre la direction d'évaluation du modèle de départ et celle ré-extraite sur chacun des adaptateurs dépassait 0,85 (illustratif) et que l'ablation inversait la croyance déclarée sur tous les adaptateurs sans dégrader la perplexité.

FIN-DE-CELLULE
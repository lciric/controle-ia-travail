# Registre exhaustif des idées, hypothèses, formalismes, pistes, expériences et décisions — session du 23 novembre 2026 (lot 8, version 1)

Pièce de travail (classe C), produite par le sous-agent bibliothécaire de la session des idées (mandat GO-2026-11-23-31 point 25 et GO-2026-11-23-33), reprenant l'inventaire à partir du point d'arrêt de la branche `origin/bibliotheque/compilation-2026-11-23-v2` (commit `0e7e03b7a`, 18h20 temps universel coordonné).

## Portée et avertissement méthodologique

- **Sources inventoriées** : messages 1 à 7 des intuitions du directeur (`docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md`), demande reformulée (`demande-reformulee-modele-idees-interessantes-v1.md`), question sur les identités tenues pour vraies (`docs/notes/identites-tenues-pour-vraies-v1/demande-directeur-et-reformulation-mere-v1.md`), questions de suivi sur l'homomorphisme et le méta-espace mathématique, réponses des modèles de Google (Argon, Carbon, Neon, y compris la réponse d'Argon arrêtée pour récitation et sa relance), réponses en effort maximal de Fable et d'Opus (sur les branches distantes dédiées), synthèse et vulgarisation version 1, messages 1 à 25 du lot 8 du directeur, note sur l'économie du protocole X (`origin/idees/lot-8-chef-d-orchestre-v1`), et lignes `GO-2026-11-23-20` à `GO-2026-11-23-33` de `registres/go.md` ainsi que `R-5175` à `R-5190` de `registres/decisions.md`.
- **Statut de preuve** : conformément aux règles R7 et R8, les chiffres issus des modèles n'ayant pas fait l'objet d'une lecture directe sur document portable empreinté restent indicatifs ; les notes de priorisation (1 à 5) traduisent le jugement analytique du bibliothécaire et n'engagent aucune dépense sans devis ni autorisation explicite du directeur.
- **Cloisonnement** : aucun fichier de `docs/verdicts/`, `runs/`, `diag/`, `donnees/` ou `coffre/*` n'a été ouvert.
- **Lien systématique avec l'organisme d'idéation** : conformément au point 3 du lot 8, chaque piste théorique, empirique ou algorithmique issue des modèles de Google, de Fable, d'Opus et du directeur est rattachée à son rôle ou à son test prévu dans l'organisme au dégel.

Total consigné : **62 entrées structurées** (également exportées en format ligne à ligne dans `registre-idees-session-2026-11-23-v1.jsonl`).

## Tableau synthétique par identifiant

| Identifiant | Bloc d'origine | Catégorie | Titre en clair | Statut | Score priorité | Lien avec l'organisme d'idéation |
|---|---|---|---|---|---|---|
| IDE-2026-11-23-001 | Intuitions directeur (messages 1-2) | hypothèse | Hypothèse centrale H1 — Mariage éloigné en surface mais proche en structure cachée | en cours d'épreuve théorique ; à tester empiriquement sur corpus daté et dans l'organisme au dégel | 500.0 | Piste maîtresse de l'organisme d'idéation : concevoir le générateur de mariages sur la matrice d'interaction (grande distance d'usage × forte proximité structurelle mesurée sans étiquette lexicale), évaluée sur l'oracle des mondes plantés (sans jugement par un autre modèle, selon la décision N-058). |
| IDE-2026-11-23-002 | Intuitions directeur (message 1) | hypothèse | Hypothèse H2 — Cascades transitives et transfert d'un domaine mûr vers un domaine jeune | à tester avec contrainte structurelle H3 (chaînage typé non naïf) | 256.0 | Piste à tester dans l'organisme au dégel : chaînage transitif typé et orienté (du domaine le plus systématique vers le domaine cible le moins formalisé), avec filtre de compatibilité des relations. |
| IDE-2026-11-23-003 | Intuitions directeur (messages 1-2) | hypothèse | Hypothèse H3 — Serrure et clé : alignement des réseaux en amont et conservation d'un invariant | en cours d'affinage formel (Noether écarté, foncteurs et transport optimal retenus) ; à tester sur corpus daté et dans l'organisme | 500.0 | Opérateur central de filtrage des propositions dans l'organisme au dégel : remplacer la similarité de surface par un score serrure-clé mesurant couverture, systématicité et absence de conflits relationnels. |
| IDE-2026-11-23-004 | Intuitions directeur (message 2) | hypothèse | Hypothèse H4 — Fenêtre optimale de distance : ni trop près ni trop loin | à tester (courbe en U inversé et déplacement de l'optimum selon la compatibilité structurelle) | 240.0 | Piste à tester dans l'organisme au dégel : paramétrage de l'échantillonneur de paires pour vérifier si le ciblage sur la fenêtre d'élasticité optimale bat la recherche uniforme ou purement extrême. |
| IDE-2026-11-23-005 | Intuitions directeur (messages 2, 4, 5 et 6) | hypothèse | Hypothèse H5 — Champ d'interaction, air du temps, nouveau cadre et découvertes simultanées | clarifiée (direction rendant comparables confirmée au message 6) ; à tester sur découvertes simultanées et jumeaux d'articles | 96.0 | Piste à tester dans l'organisme au dégel : injecter une liste de cadres instrumentaux ou méthodes en forte diffusion comme opérateur de mise en regard entre domaines jusque-là isolés. |
| IDE-2026-11-23-006 | Intuitions directeur (messages 2 et 7) | hypothèse | Hypothèse H6 — Travail conjoint de connexion et de distinction (scission de fausses identités) | décidée pour l'inscription à l'organisme au dégel (GO-2026-11-23-28) ; à tester sur corpus historiques | 500.0 | Opérateur prioritaire inscrit au dégel de l'organisme (GO-2026-11-23-28, R-5180) : opérateur de scission conceptuelle (découpe d'un nœud en sous-rôles ou personas quand le voisinage révèle des conflits de restriction). |
| IDE-2026-11-23-007 | Intuitions directeur (message 1 et 2) | hypothèse | Hypothèse H7 — Profondeur de l'idée fille (proximité aux nœuds et unification rétrospective) | amendée (de « près des anciens nœuds » à « unification réduisant la description et éclipsant les anciens nœuds ») ; à tester | 256.0 | Critère d'évaluation interne dans l'organisme au dégel : mesurer la contraction de description (gain de compression conjointe sur les deux bassins parents) plutôt que la simple centralité de degré des parents. |
| IDE-2026-11-23-008 | Intuitions directeur (messages 2 et 7) | hypothèse | Hypothèse H8 — Émergence comme percolation inter-milieux et transitions de phase | transmise à Fable en protocole X (GO-2026-11-23-28) ; à tester sur corpus et graphes de l'organisme | 72.0 | Piste à tester dans l'organisme au dégel : mesurer l'apparition de cascades d'appariements satellites (rapport de branchement supérieur à 1) et rechercher des ruptures de connectivité sur les graphes produits par l'organisme. |
| IDE-2026-11-23-009 | Intuitions directeur (messages 1, 6 et 7) + lot 8 (point 24) | hypothèse | Hypothèse H9 — Structure mathématique cachée du langage reflétant les symétries du réel | en cours (dossier 1 du protocole X confié à Fable : 33 sources téléchargées, notes à suivre ; réactivé au point 24 du lot 8) | 150.0 | Piste à tester dans l'organisme au dégel : détecteur de symétries exactes ou approchées dans les statistiques de cooccurrence d'un corpus scientifique daté comme générateur d'invariants candidats. |
| IDE-2026-11-23-010 | Intuitions directeur (messages 1 et 7) + lot 8 (point 2) | hypothèse | Hypothèse H10 — Signal interne de surprise et erreur de prédiction de récompense (analogue dopaminergique) dans l'organisme | question posée au lot 8 point 2 (quel modèle ouvert recommander) ; à tester en lecture seule (jamais optimisé directement) | 96.0 | Piste à tester dans l'organisme au dégel et sur banc de notes : lire les neurones de valeur et d'erreur de différence temporelle au dernier jeton d'un modèle ouvert pour tester le motif « surprise puis explication », sous l'invariant strict de non-optimisation directe du score. |
| IDE-2026-11-23-011 | Intuitions directeur (messages 4 et 5) | idée | Loi de croissance du champ avec le rapprochement des réseaux et nécessité de collisions actives | versée pour la suite ; traduite en facteur multiplicatif densité × champ × serrure dans les modèles | 108.0 | Piste à tester dans l'organisme au dégel : coupler le repérage de paires à forte compatibilité potentielle avec un opérateur actif de collision expérimentale ou logique entre les deux voisinages. |
| IDE-2026-11-23-012 | Intuitions directeur (message 6) | idée | Mesurer les invariances directement par collision des structures sous-jacentes (réponse à la circularité du champ) | retenue comme principe de mesure non circulaire | 192.0 | Piste à tester dans l'organisme au dégel : évaluation des candidats par alignement structurel sur données antérieures ou sur mondes plantés sans accès aux étiquettes cibles. |
| IDE-2026-11-23-013 | Intuitions directeur (message 6) + question suivi homomorphisme | hypothèse | Formalisation de l'invariance par homomorphisme de graphes typés et équivariance d'opérateurs discrets | évaluée et réformée (remplacée par foncteurs partiels / spans, groupoïdes locaux et faisceaux cellulaires) | 400.0 | Directement applicable au moteur de représentation de la couche de structure de l'organisme au dégel. |
| IDE-2026-11-23-014 | Intuitions directeur (message 7) + GO-2026-11-23-27 | hypothèse | Identités et invariances tenues pour vraies qui ne vont pas de soi et profondeur de leurs conséquences | dossier 2 du protocole X ouvert (confié à Fable, interrompu par limite d'usage à reprendre) | 500.0 | Piste à tester dans l'organisme au dégel et sur corpus historique : détecteur d'obstructions de faisceaux et scission de nœuds sur les concepts confondus. |
| IDE-2026-11-23-015 | Intuitions directeur (message 7) + GO-2026-11-23-28 | hypothèse | Principe variationnel sur un graphe conceptuel discret et dissipatif | dossier 3 du protocole X confié à Fable (GO-2026-11-23-28), en attente de fusion et de collisionneur | 48.0 | Piste à tester dans l'organisme au dégel : estimer si les trajectoires de découverte historiques minimisent une action de grandes déviations ou maximisent un flux d'entropie de trajectoires par rapport à un modèle nul. |
| IDE-2026-11-23-016 | Intuitions directeur (message 7) + question méta-espace | hypothèse | Séparation structure abstraite / alphabet relationnel humain et troisième couche « méta » du graphe | répondu par Carbon ; versé au dossier 6 du protocole X et repris dans le lot 8 (points 9 à 16, 20 à 23) | 187.5 | Architecture cible de la version avancée de l'organisme d'idéation au dégel : ajouter une troisième couche chantier (schémas anti-unifiés, obstructions, problèmes ouverts, proto-objets réservoirs). |
| IDE-2026-11-23-017 | Intuitions directeur (message 7) | idée | Traction par les anomalies empiriques et maximisation du progrès de compression dans l'organisme | à intégrer au dégel de l'organisme | 400.0 | Deux des trois nouveaux opérateurs de l'organisme au dégel (T8) : polarisation par les anomalies et récompense par le gain de compression conjointe. |
| IDE-2026-11-23-018 | Réponses Google v1 + Fable + Opus | formalisme | Distinction analytique des trois questions : intérêt perçu, vérité/fécondité, et mécanisme de production | consensus unanime des cinq modèles ; adopté dans la note v1 | 375.0 | Impose à l'organisme de ne jamais utiliser l'intérêt perçu ni un juge modèle comme oracle de vérité (conforme à la décision N-058 : oracle des mondes plantés et coût). |
| IDE-2026-11-23-019 | Réponses Google v1 + Fable + Opus | formalisme | Graphe multiplexe daté à trois couches de base (usage, structure typée, communautés humaines) | consensus des cinq modèles | 300.0 | Structure de données de référence pour l'organisme et pour les expériences rétrospectives hors-temps. |
| IDE-2026-11-23-020 | Réponses Google v1 + Fable + Opus | formalisme | Mesure de l'alignement structurel inter-domaines sans fuite lexicale par transport de Gromov-Wasserstein fusionné / partiel / non équilibré et signatures de rôle | consensus sur le transport de Gromov-Wasserstein + filtrage discret ; à éprouver | 400.0 | Fournit à l'organisme un moteur calculable de comparaison structurale agnostique au jargon disciplinaire. |
| IDE-2026-11-23-021 | Réponses homomorphisme (Argon, Carbon, Neon) | objet candidat | Esquisses catégoriques, ologs, spans de foncteurs partiels et faisceaux cellulaires avec cohomologie H0 | proposés par les modèles ; candidats formels de haute valeur à tester | 150.0 | À tester dans l'organisme comme formalisme d'encodage des lois et de détection des obstructions de recollement (incohérences entre parties d'une même analogie ou identité). |
| IDE-2026-11-23-022 | Réponses Argon, Carbon, Neon homomorphisme | objet candidat | Théorème de Noether markovien et mécanique variationnelle discrète (démarcation strict / spéculatif) | état de l'art formel clarifié | 72.0 | Balise pour l'organisme : ne chercher de lois de conservation dynamiques que si l'on définit explicitement une dynamique markovienne ou variationnelle sur le graphe ; sinon utiliser la naturalité et les faisceaux. |
| IDE-2026-11-23-023 | Réponses Google v1 + Fable + Opus | piste | Traitement systématique du biais du survivant : cohortes de « mariages mort-nés », essais négatifs et rétractations | consensus des cinq modèles | 375.0 | Règle d'hygiène pour l'évaluation des pistes de l'organisme : tenir le registre des échecs et mesurer les taux de base. |
| IDE-2026-11-23-024 | Réponses Argon, Carbon, Neon, Fable, Opus | piste | Mécanismes oubliés à intégrer au modèle : friction du réel (anomalies), coût d'épreuve, asymétrie donneur-récepteur, porteurs humains et retards de réveil | pistes à intégrer et tester progressivement dans les versions suivantes du modèle et de l'organisme | 320.0 | Chaque manque fournit un axe d'amélioration de l'organisme (exemple : intégrer un critère d'orientabilité donneur-récepteur et une pondération par coût de test). |
| IDE-2026-11-23-025 | Réponse Argon v1 (section 7) + note v1 (T1) | expérience proposée | Expérience T1 (Argon) — Formes d'équations partagées sur sources composition typographique mathématique de l'archive ouverte arXiv | proposée ; en attente de préenregistrement et de devis/GO | 400.0 | Alimente directement l'organisme sur la couche des structures mathématiques exactes (arbres d'opérateurs sans bruit de traitement du langage naturel). |
| IDE-2026-11-23-026 | Réponses Carbon v1, Neon v1 (section 7) + note v1 (T2) | expérience proposée | Expérience T2 (Carbon et Neon) — Cœur H1 × H3 sur graphe biomédical daté (la base de prédications biomédicales SemMedDB, descripteurs médicaux, graphe bibliographique ouvert OpenAlex) | proposée ; en attente de préenregistrement et de choix base ouverte PubTator 3 / la base de prédications biomédicales SemMedDB | 400.0 | Banc d'essai empirique immédiat des opérateurs d'alignement structurel avant intégration définitive à l'organisme. |
| IDE-2026-11-23-027 | Réponse Fable max v1 (section 7) | expérience proposée | Expérience « le pont suit-il la carte ? » (Fable) — Test du cortège après naissance sur base ouverte PubTator 3 | proposée par Fable ; candidate n° 1 sur processeur sans dépendance de licence | 625.0 | Épreuve directe du mécanisme générateur de l'organisme : vérifie si la serrure-clé produit une cascade prévisible de découvertes sœurs et constitue une base naturelle de monde planté. |
| IDE-2026-11-23-028 | Réponse Opus max v1 (section 7) | expérience proposée | Expérience « surface et structure » sur les 2 996 notes réelles d'intérêt d'experts (Gu et Krenn 2026) | proposée par Opus ; Bras A et C prêts pour préenregistrement sans dépense | 625.0 | Seul essai confrontant directement le modèle structurel aux jugements d'intérêt réel de 110 chercheurs humains sans avoir à recruter un panel dès la phase 0. |
| IDE-2026-11-23-029 | Réponses homomorphisme (Argon, Carbon, Neon — sections 4 et 5) | expérience proposée | Expérience d'alignement pré-découverte sur le corpus Physical Review (cas d'Unruh 1981 + 20 ponts physiques) | proposée ; requiert accès au jeu de données Société américaine de physique et parseur sans fuite temporelle | 150.0 | Teste l'hypothèse forte d'une invariance structurale préexistante détectable avant la publication du pont ; applicable au module de détection précoce de l'organisme. |
| IDE-2026-11-23-030 | Réponse Carbon méta-espace (section 1 à 5) | objet candidat | Cinq signaux ex ante d'apparition d'un objet mathématique nouveau (couche chantier) | reçu et fortement plébiscité par le directeur (lot 8 points 8, 9, 10, 23) ; en attente de généralisation aux grands modèless de langage et à l'alignement | 500.0 | Piste majeure pour l'organisme au dégel : doter la couche chantier de détecteurs de tension sur les corpus scientifiques et d'alignement de l'intelligence artificielle. |
| IDE-2026-11-23-031 | Réponse Carbon méta-espace (section 3) | objet candidat | Trois mécanismes pour briser la circularité : Éveil-Sommeil croisé (DreamCoder/Stitch), amorçage quinien algébrique, thématisation automatique | validé par le directeur pour implémentation et test progressif (lot 8 point 22) | 187.5 | Cœur algorithmique de l'invention de nouveaux objets dans la v2/v3 de l'organisme d'idéation. |
| IDE-2026-11-23-032 | Réponse Carbon méta-espace (section 5) | expérience proposée | Expérience des macros composition typographique mathématique et arbres d'équations avant les algèbres amassées (Fomin et Zelevinsky 2002) | proposée ; préenregistrement à rédiger ; explication des notions demandée au lot 8 point 15 | 500.0 | Banc d'essai gratuit sur données publiques vérifiant si la compression inter-domaines détecte la naissance d'un objet mathématique majeur avant sa formulation. |
| IDE-2026-11-23-033 | Note v1 des hypothèses (T3, T4, T5, T6, T7) | expérience proposée | Batterie d'expériences complémentaires T3 à T7 (multiples, gain de compression sur modèle 8B, scissions, taille finie, symétries) | inscrites comme pistes de test ; T5 et T7 liées au protocole X | 256.0 | Chacun de ces tests correspond à un module ou critère évaluable sur les trajectoires et productions de l'organisme. |
| IDE-2026-11-23-034 | Réponse Neon homomorphisme + Note v1 (section 2) + Opus | piste | Correction des comparaisons multiples, détection endogène du changement de représentation et symétries de cooccurrence sans co-apparition | pistes techniques à intégrer aux protocoles et à l'organisme | 192.0 | Renforcent la rigueur statistique des recherches de ponts dans l'organisme (évite les faux positifs par multiplicité et détecte des symétries latentes sans citation directe). |
| IDE-2026-11-23-035 | Lot 8 — Point 1 | piste | système de découverte symbolique de Udrescu et Tegmark (Udrescu et Tegmark 2020) et rupture de la circularité comme inspiration pour l'organisme | demande du directeur en attente de traitement (regroupée dans le lot 8) | 256.0 | Piste directe pour l'organisme au dégel : extraire des opérateurs de décomposition par invariance et symétrie d'échelle avant recherche combinatoire. |
| IDE-2026-11-23-036 | Lot 8 — Point 2 | piste | Choix du modèle ouvert pour le sous-système de récompense éparse (« dopamine ») comme observateur d'idées justes | en attente de traitement groupé (lot 8) ; préconisation partielle à vérifier (modèles ouverts étudiés par Xu et al. 2026, Qwen/Llama) | 72.0 | Instrumente la mesure d'erreur de différence temporelle et de surprise sur l'organisme (en lecture seule, jamais en objectif d'optimisation). |
| IDE-2026-11-23-037 | Lot 8 — Point 3 | décision | Inscription universelle des pistes des modèles Gemini et du collisionneur v2 dans l'organisme | décidée (mandat actif du bibliothécaire et de la veille de cap) | 375.0 | Fonde la liste exhaustive des pistes à éprouver dans l'organisme au dégel ; aucune piste n'est écartée sans décision nommée. |
| IDE-2026-11-23-038 | Lot 8 — Point 4 | décision | Réécritures éditoriales de la note de vulgarisation et de la note complète (mode Étienne Klein, préface savante, proposition de subvention) | en cours (session dédiée lancée avant l'arrêt de 19:02Z, interrompue à reprendre) | 24.0 | Valorisation et recherche de financement (appui aux bourses mentionnées au point 17), sans effet direct sur le moteur de l'organisme. |
| IDE-2026-11-23-039 | Lot 8 — Point 5 | hypothèse | Réactualisation de la formation automatique de théories pures (Colton 2002 / Automated Mathematician (programme de Lenat) de Lenat) par les grands modèless de langage modernes | à traiter et intégrer au protocole X (fusionné avec les points 10, 11 et 14) | 250.0 | Piste à tester dans l'organisme : coupler un synthétiseur formel (type Stitch / vérification exacte) à un sélecteur sémantique par grand modèle de langage pour couper la prolifération stérile. |
| IDE-2026-11-23-040 | Lot 8 — Points 6, 7 et 15 | décision | Pédagogie approfondie et réutilisation des méthodes de Hofstadter, Carey, DreamCoder, Stitch, Cavaillès/Piaget et des objets techniques de Carbon | en attente de traitement (à regrouper : explication claire + audit de réutilisabilité logicielle de DreamCoder et Stitch) | 400.0 | Réemploi direct de code ouvert (Stitch en Rust/Python, algorithmes de DreamCoder) comme briques de la troisième couche de l'organisme. |
| IDE-2026-11-23-041 | Lot 8 — Point 8 et 9 | piste | Application de l'entropie notationnelle (Cajori) et des 5 signaux ex ante à l'alignement, l'interprétabilité mécaniste et la sûreté de l'intelligence artificielle par compréhension sémantique | à traiter et tester (protocole X sur les signaux ex ante, points 9, 10 et 23) | 250.0 | Piste directe pour l'organisme appliqué à l'alignement : repérer dans la littérature de sûreté/interprétabilité les zones de bricolage ad hoc où manque un objet formel unificateur. |
| IDE-2026-11-23-042 | Lot 8 — Point 10 | piste | Mariage inédit entre capacités modernes des grands modèless de langage avancés (2026) et signaux ex ante / troisième couche sur l'histoire des sciences | à traiter dans le lot 8 (sous règle d'économie : question fusionnée avec les points 5, 11, 14) | 187.5 | Architecture hybride à tester : grand modèle de langage comme moteur d'abstraction sémantique et d'anti-unification couplé à la couche chantier. |
| IDE-2026-11-23-043 | Lot 8 — Point 11 | piste | Apprentissage de bibliothèque par grand modèle de langage couplé à la compression longueur de description minimale inter-bassins (Stitch) | en attente de traitement (regroupé en demande approfondie dans le lot 8) | 250.0 | Mécanisme hybride « proposition par grand modèle de langage + vérification et comptage de compression par Stitch » directement testable dans l'organisme. |
| IDE-2026-11-23-044 | Lot 8 — Points 13 et 21 | expérience proposée | Banc de vérité terrain sans fuite temporelle : modèle entraîné avant t0 (physique pré-1900) ou modèles fermés au web post-coupure | double demande en attente : recherche bibliographique/code sur le projet pré-1900 + question protocole X au collisionneur (point 21) | 200.0 | Crucial pour l'organisme : toute expérience de rétrodiction utilisant un modèle de langage exige soit un modèle entraîné avant t0, soit une fenêtre temporelle post-coupure du modèle, soit un protocole d'anonymisation structurelle prouvé étanche. |
| IDE-2026-11-23-045 | Lot 8 — Point 14 | hypothèse | Double stratégie de découverte : objets déjà existants non reliés (réduction de dimension) contre objets hors alphabet relationnel — et liste des 12 objectifs ultimes | en attente (Carbon high, Fable/équivalent, Opus, collisionneur puis protocole X) | 187.5 | Définit les deux régimes d'exploration de l'organisme : régime 1 (extraction de sous-espaces et lentilles sur concepts existants) contre régime 2 (synthèse de primitives hors alphabet). |
| IDE-2026-11-23-046 | Lot 8 — Point 16 | décision | Épreuve croisée de la proposition de Carbon sur le méta-espace avec bras témoin neutre au collisionneur | décidée (GO-2026-11-23-31) ; en attente de réponse Fable/substitut et de devis collisionneur | 96.0 | Expérience méthodologique contrôlant la validité même du protocole X qui alimente l'organisme. |
| IDE-2026-11-23-047 | Lot 8 — Points 17 et 19 | décision | Programme d'expériences décisives à court terme (quelques jours) pour améliorer l'organisme et questions stratégiques A, B, C | en cours (rapport du bibliothécaire livré ici ; volet collisionneur à lancer sous règle d'économie) | 625.0 | Feuille de route immédiate du dégel de l'organisme d'idéation. |
| IDE-2026-11-23-048 | Lot 8 — Point 18 + decision-economie-protocole-x-v1.md | décision | Règle d'économie du protocole X : portfolio décorrélé par famille (Carbon + Opus + Fable), retrait d'Argon, Neon conditionnel, regroupement par axe | décidée et versée par la cheffe d'orchestre du lot 8 (en attente de confirmation sur mesure par unités) | 200.0 | Optimise le rendement par dollar de la boucle externe d'idéation qui conçoit et alimente l'organisme. |
| IDE-2026-11-23-049 | Lot 8 — Point 20 | piste | Apport spécifique de l'exploration d'objets mathématiques hors alphabet relationnel pour l'alignement et le contrôle de l'intelligence artificielle | en attente de lancement groupé au protocole X | 187.5 | Relie directement l'organisme d'idéation (atelier d'objets nouveaux) aux verrous théoriques de l'alignement (spécification d'objectifs, interprétabilité, contrôle d'agents avancés). |
| IDE-2026-11-23-050 | Lot 8 — Point 22 | décision | Mise à l'épreuve comparative et séquentielle des mécanismes brisant la circularité | décidée dans le principe ; à décliner en plan d'expériences sur mondes plantés au dégel de l'organisme | 187.5 | Cahier des charges direct de l'ablation comparative des opérateurs de la couche chantier dans l'organisme. |
| IDE-2026-11-23-051 | Lot 8 — Point 23 | piste | Détection par méthodes ex ante des zones de révolutions imminentes en intelligence artificielle (auto-amélioration, intelligence artificielle générale, superintelligence, alignement) | en attente de passage au protocole X (fusionnable avec points 9 et 10) | 500.0 | Piste à tester immédiatement sur un corpus récent de l'archive ouverte arXiv (informatique (intelligence artificielle et apprentissage automatique), alignement) gelé à t0 = 2024 pour prédire les percées de 2025–2026 en pré-test rétrospectif. |
| IDE-2026-11-23-052 | Lot 8 — Point 24 | piste | Protocole opérationnel pour révéler des régularités du réel via les symétries statistiques cachées du langage | en attente d'envoi groupé (Carbon, Fable/substitut, collisionneur) | 120.0 | Complète la piste T7 (symétries de cooccurrence) de l'organisme. |
| IDE-2026-11-23-053 | Lot 8 — Point 25 + GO-2026-11-23-31 + GO-2026-11-23-33 | décision | Mission permanente du bibliothécaire des idées et relais sous Antigravity (GO-2026-11-23-33) | en cours (présent livrable du bibliothécaire) | 200.0 | Assure la mémoire, la traçabilité et l'alimentation sans perte de l'organisme d'idéation lors des transitions de session. |
| IDE-2026-11-23-054 | GO-2026-11-23-20, -21, -22, -23, -26 / R-5175 à R-5179 | décision | Lancement et bilan des appels initiaux Google (Argon, Carbon, Neon) et autorisation du collisionneur « idées intéressantes » (30 dollars américains) | décidée et exécutée pour les appels seuls et réponses Fable/Opus ; collisionneur à lancer/achever sur question v2 retouchée | 160.0 | Valide la discipline expérimentale des questions neutres à 3 retouches et constitue la base de données empirique des réponses modèles. |
| IDE-2026-11-23-055 | GO-2026-11-23-24 et R-5180 | décision | Protocole X dossier 1 — Structure cachée du langage (Tshitoyan 2019, Karkada 2026) et sources archivées | en cours (33 sources archivées sur branche Fable, rédaction à finaliser) | 256.0 | Piste directe pour le détecteur de symétries statistiques dans l'organisme (H9 / T7). |
| IDE-2026-11-23-056 | GO-2026-11-23-25 et R-5181 | décision | Grande revue bibliographique récente, note composition typographique mathématique complète et cours accéléré sur les concepts déjà occupés | en cours (note v1 livrée ; revue bibliographique partiellement poussée à achever et verser en v2) | 160.0 | Empêche l'organisme d'explorer ou de revendiquer des concepts déjà publiés (anti-faux-gap R8). |
| IDE-2026-11-23-057 | GO-2026-11-23-27, -28, -29 | décision | Ouverture des dossiers protocole X 2 à 6 et inscription prioritaire de la scission conceptuelle au dégel de l'organisme | décidée (dossiers 2 à 5 interrompus par limite d'usage chez Fable à reprendre ; fusion à servir au collisionneur sur devis) | 250.0 | Fournit l'ensemble du cahier des charges conceptuel de la prochaine génération d'opérateurs de l'organisme. |
| IDE-2026-11-23-058 | GO-2026-11-23-30, -32 et R-5182 à R-5189 | décision | Articulation avec les chantiers actifs du programme (saboteur voie A, T0.8, barreau 8, 16 papiers, billet, défauts 48h) | décidée / en cours d'exécution parallèle (sans modification des fichiers de verdicts/runs) | 192.0 | Rappelle les invariants de contrôle de l'organisme : jamais de validation sans vérité plantée ni relecture sur document portable, méfiance face aux sondes corrélées (biais de fabrication), et priorité aux expériences à garde causale stricte. |
| IDE-2026-11-23-059 | Fable max v1 (section 1) + Lot 8 | piste | Exploitation de la base base de recombinaisons d'idées scientifiques Chimera (Sternlicht et Hope 2025) et du jeu Gu et Krenn (2026) pour l'entraînement et l'étalonnage de l'organisme | piste de données immédiate à exploiter pour étalonner et tester l'organisme | 375.0 | Fournit à l'organisme des données structurées publiques à coût nul pour tester les scores d'intérêt et de structure avant tout essai en aveugle. |
| IDE-2026-11-23-060 | Fable max v1 (section 1) + Opus max v1 (section 1) | hypothèse | Critère de génération séparée avant confrontation (contre le remue-méninges interactif prématuré) et transfert de l'intégration plutôt que de l'axe de douleur | acquis conceptuel à appliquer à l'architecture de l'organisme et au test sur les modèles de langage | 320.0 | Confirme le principe multi-espèces isolées avant collision dans l'organisme, et corrige le ciblage de l'expérience modèle de langage / anesthésie vers des mesures d'intégration et de découplage interne/sortie. |
| IDE-2026-11-23-061 | Argon homomorphisme + Carbon homomorphisme + Neon homomorphisme | objet candidat | Formalisme des analogies par graphe d'hyperarêtes typées et résolvante de chemins dirigés avec masquage lexical intégral | proposition algorithmique prête à coder et tester sur graphe | 400.0 | Résout le défaut principal des graphes binaires naïfs (l'invariance d'échelle déductive arête <-> chemin) pour l'alignement structurel dans l'organisme. |
| IDE-2026-11-23-062 | Carbon méta-espace + Lot 8 | décision | Protocole de vérification anti-faux-gap et traçabilité document portable stricte (R7, R8) sur toutes les citations des modèles | en cours (revue bibliographique et téléchargement des sources à achever) | 48.0 | Obligation préalable à toute publication ou décision reposant sur un chiffre cité. |

## Fiches détaillées des 62 entrées

### IDE-2026-11-23-001 — Hypothèse centrale H1 — Mariage éloigné en surface mais proche en structure cachée

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 1-2).
- **Énoncé détaillé** : Une idée intéressante associe deux concepts ou domaines sans lien logique évident, très éloignés en surface (vocabulaire, usages, disciplines, publications) mais proches sur une dimension abstraite cachée (structure relationnelle ou mathématique). La surprise vient de l'écart en surface ; la viabilité et la fécondité viennent de la proximité structurelle cachée. Précision issue des réponses : effet d'interaction et non effet principal positif de la seule distance (Gu et Krenn 2026 montrent une pente moyenne négative de l'intérêt avec la distance entre champs).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 1 et 2) ; demande-reformulee-modele-idees-interessantes-v1.md (H1) ; confrontation dans reponse-fable-max-v1.md, reponse-opus-max-v1.md, reponses Google (v1).`.
- **Statut** : en cours d'épreuve théorique ; à tester empiriquement sur corpus daté et dans l'organisme au dégel.
- **Lien avec l'organisme d'idéation** : Piste maîtresse de l'organisme d'idéation : concevoir le générateur de mariages sur la matrice d'interaction (grande distance d'usage × forte proximité structurelle mesurée sans étiquette lexicale), évaluée sur l'oracle des mondes plantés (sans jugement par un autre modèle, selon la décision N-058).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Cœur falsifiable du programme d'idéation ; testable à coût quasi nul sur processeur en quelques jours (corpus biomédicaux ou équations archive ouverte de prépublications arXiv).

### IDE-2026-11-23-002 — Hypothèse H2 — Cascades transitives et transfert d'un domaine mûr vers un domaine jeune

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 1).
- **Énoncé détaillé** : Des chaînes de mariages (A lié à B, B lié à C, engendrant un lien neuf A–C) et le transfert d'un résultat d'un domaine mûr vers un domaine jeune (exemple : douleur et anesthésie chez l'humain, anesthésie et conscience, puis recherche d'un motif interne équivalent à l'état d'anesthésie sur l'axe de douleur d'un grand modèle de langage pour étudier la conscience). Réserve unanime des modèles : sans typage ni orientation des relations (filtre de structure de H3), la transitivité brute explose en faux positifs (polysémie) ; l'exemple douleur-anesthésie-conscience mêle analgésie et perte de conscience.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 1) ; demande-reformulee-modele-idees-interessantes-v1.md (H2) ; reponse-opus-max-v1.md (section 1) ; reponse-fable-max-v1.md (section 1).`.
- **Statut** : à tester avec contrainte structurelle H3 (chaînage typé non naïf).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : chaînage transitif typé et orienté (du domaine le plus systématique vers le domaine cible le moins formalisé), avec filtre de compatibilité des relations.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 256.0**.
- **Justification de priorisation** : Occupé sous forme brute depuis Swanson (1986), mais son couplage avec le filtre structurel typé H3 et la disjonction des composantes (analgésie contre intégration) reste directement testable.

### IDE-2026-11-23-003 — Hypothèse H3 — Serrure et clé : alignement des réseaux en amont et conservation d'un invariant

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 1-2).
- **Énoncé détaillé** : Il ne suffit pas que deux points s'emboîtent : les réseaux de concepts en amont de chaque parent doivent pouvoir coexister et s'aligner dans la projection, et un invariant doit être conservé sous la transformation. L'analogie initiale avec le théorème de Noether et le lagrangien est rejetée par les cinq modèles (Argon, Carbon, Neon, Fable, Opus) faute d'espace de phases continu et d'action variationnelle ; elle est traduite rigoureusement par les homomorphismes partiels de graphes typés, les foncteurs entre catégories de chemins (esquisses ou ologs), la naturalité et l'équivariance sur groupoïdes locaux.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 1 et 2) ; question-suivi-homomorphisme-v1.md ; reponses Google (v1 et homomorphisme) ; reponse-fable-max-v1.md ; reponse-opus-max-v1.md.`.
- **Statut** : en cours d'affinage formel (Noether écarté, foncteurs et transport optimal retenus) ; à tester sur corpus daté et dans l'organisme.
- **Lien avec l'organisme d'idéation** : Opérateur central de filtrage des propositions dans l'organisme au dégel : remplacer la similarité de surface par un score serrure-clé mesurant couverture, systématicité et absence de conflits relationnels.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Pivot du modèle de viabilité : sépare les métaphores séduisantes mais fausses des isomorphismes exploitables ; testable en 3 à 4 jours sur processeur.

### IDE-2026-11-23-004 — Hypothèse H4 — Fenêtre optimale de distance : ni trop près ni trop loin

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 2).
- **Énoncé détaillé** : Des concepts parents trop proches appartiennent à un bassin large et donnent une idée banale ; des concepts trop lointains forment une singularité étroite où rien ne se lie. L'optimum de curiosité et de fécondité se situe à distance intermédiaire (ou, selon la précision apportée par Carbon, Fable et Opus, dérive comme corollaire du compromis entre surprise croissante et plausibilité structurelle décroissante, et s'exprime en combinaison d'un socle très conventionnel avec une dose ciblée d'atypicité).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 2) ; demande-reformulee-modele-idees-interessantes-v1.md (H4) ; reponse-fable-max-v1.md ; reponse-opus-max-v1.md ; reponse-carbon-v1.md.`.
- **Statut** : à tester (courbe en U inversé et déplacement de l'optimum selon la compatibilité structurelle).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : paramétrage de l'échantillonneur de paires pour vérifier si le ciblage sur la fenêtre d'élasticité optimale bat la recherche uniforme ou purement extrême.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 240.0**.
- **Justification de priorisation** : Testable directement en réanalyse des jeux de notes publics (Gu et Krenn 2026) et sur corpus biomédical par modèles additifs généralisés sans coût supplémentaire.

### IDE-2026-11-23-005 — Hypothèse H5 — Champ d'interaction, air du temps, nouveau cadre et découvertes simultanées

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 2, 4, 5 et 6).
- **Énoncé détaillé** : L'interaction décroît avec la distance sauf si deux concepts répondent à un même champ né d'un cadre de pensée, instrument ou technologie nouvelle (horloges et chemins de fer pour la relativité ; écoulements fluides pour les trous noirs) qui projette les réseaux dans un espace commun de comparabilité. Ce champ explique les découvertes simultanées et combine densité des réseaux et probabilité de rencontre par transformation préservant l'invariance. Les images du ferromagnétisme, de la résonance et de l'appariement de protéines sont écartées par les modèles au profit d'une covariable exogène datée d'adoption partagée d'instruments ou de formalismes, mesurée strictement avant la découverte (pour éviter la circularité).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 2, 4, 5, 6) ; demande-reformulee-modele-idees-interessantes-v1.md (H5) ; note-hypotheses-appuis-formalismes-v1.md (section 2 et 3).`.
- **Statut** : clarifiée (direction rendant comparables confirmée au message 6) ; à tester sur découvertes simultanées et jumeaux d'articles.
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : injecter une liste de cadres instrumentaux ou méthodes en forte diffusion comme opérateur de mise en regard entre domaines jusque-là isolés.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 96.0**.
- **Justification de priorisation** : Exige l'extraction de séries temporelles d'instruments et un appariement de jumeaux d'articles avec singletons témoins ; fort potentiel explicatif sur la maturité d'une découverte.

### IDE-2026-11-23-006 — Hypothèse H6 — Travail conjoint de connexion et de distinction (scission de fausses identités)

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 2 et 7).
- **Énoncé détaillé** : Déformer et projeter un réseau dans un nouvel espace sert autant à connecter des concepts éloignés qu'à séparer deux concepts faussement confondus (simultanéité absolue, chaleur et température), dont un seul possède la structure compatible pour s'accoupler avec un concept compagnon. Les fausses identités s'entrechoquent et sont éliminées lors de la collision. Note : Fable, Opus et la note de synthèse corrigent l'exemple des masses inerte et grave (c'est une connexion élevée en principe d'équivalence, l'exemple canonique de scission étant la simultanéité ou chaleur contre température).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 2 et 7) ; demande-reformulee-modele-idees-interessantes-v1.md (H6) ; note-hypotheses-appuis-formalismes-v1.md (H6) ; GO-2026-11-23-28.`.
- **Statut** : décidée pour l'inscription à l'organisme au dégel (GO-2026-11-23-28) ; à tester sur corpus historiques.
- **Lien avec l'organisme d'idéation** : Opérateur prioritaire inscrit au dégel de l'organisme (GO-2026-11-23-28, R-5180) : opérateur de scission conceptuelle (découpe d'un nœud en sous-rôles ou personas quand le voisinage révèle des conflits de restriction).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Zone explicitement identifiée comme peu explorée quantitativement (Neon) ; fort rendement espéré à la fois pour l'idéation scientifique et pour le contrôle boîte blanche (distinguer ce que lit une sonde ce qu'emploie le modèle).

### IDE-2026-11-23-007 — Hypothèse H7 — Profondeur de l'idée fille (proximité aux nœuds et unification rétrospective)

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 1 et 2).
- **Énoncé détaillé** : L'idée fille doit être proche de concepts nœuds du graphe de connaissances et expliquer après coup pourquoi son apparition surprenait (unification de la Lune et de la pomme). Nuance majeure apportée par Neon, Fable et Opus : les idées les plus disruptives ne s'accrochent pas aux nœuds les plus centraux (Gu et Krenn 2026 relèvent une corrélation négative de -0,166 entre intérêt et degré) ; elles deviennent de nouveaux nœuds et éclipsent les anciens (indice de disruption), mesurable avant coup par la contraction des plus courts chemins et le gain de longueur de description minimale.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 1 et 2) ; reponse-neon-v1.md ; reponse-fable-max-v1.md ; reponse-opus-max-v1.md.`.
- **Statut** : amendée (de « près des anciens nœuds » à « unification réduisant la description et éclipsant les anciens nœuds ») ; à tester.
- **Lien avec l'organisme d'idéation** : Critère d'évaluation interne dans l'organisme au dégel : mesurer la contraction de description (gain de compression conjointe sur les deux bassins parents) plutôt que la simple centralité de degré des parents.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 256.0**.
- **Justification de priorisation** : Permet d'éviter le biais favorisant les concepts célèbres mais stériles ; vérifiable par test rétrospectif sur indice de disruption et compression.

### IDE-2026-11-23-008 — Hypothèse H8 — Émergence comme percolation inter-milieux et transitions de phase

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 2 et 7).
- **Énoncé détaillé** : L'émergence d'une idée nouvelle et de son champ d'application est modélisée comme une percolation entre deux milieux différents (distincte de la percolation ordinaire dans un même milieu) et une transition de phase, accélérée par la mise en vibration et la surface de contact des réseaux confrontés. Position des modèles : la percolation de liens inter-communautés et la surface de contact (trous structuraux de Burt) sont soutenues et formalisables (seuil de composant géant biparti et processus de branchement) ; la transition thermodynamique stricte avec exposants critiques en taille infinie est jugée métaphorique sur graphes finis (Neon, Opus). Le directeur maintient la recherche de transitions de phase par analyse de taille finie (message 7, GO-2026-11-23-28).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 2 et 7) ; GO-2026-11-23-28 ; note-hypotheses-appuis-formalismes-v1.md (H8, T6, T8).`.
- **Statut** : transmise à Fable en protocole X (GO-2026-11-23-28) ; à tester sur corpus et graphes de l'organisme.
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : mesurer l'apparition de cascades d'appariements satellites (rapport de branchement supérieur à 1) et rechercher des ruptures de connectivité sur les graphes produits par l'organisme.
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 72.0**.
- **Justification de priorisation** : Soutenue sous forme de seuil de branchement et composante géante ; l'hypothèse de transition critique stricte en taille finie reste plus risquée et demande des séries temporelles propres.

### IDE-2026-11-23-009 — Hypothèse H9 — Structure mathématique cachée du langage reflétant les symétries du réel

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 1, 6 et 7) + lot 8 (point 24).
- **Énoncé détaillé** : Le langage possède une structure mathématique cachée qui reflète la structure du réel et des lois de l'univers (inspiré par Tshitoyan et al. 2019 sur les thermoélectriques et Karkada et al. 2026 sur la symétrie de translation des cooccurrences des mois). Piste : extraire ces symétries ou dimensions latentes (analyse en composantes principales ou apprentissage non supervisé) pour faire des découvertes. Réserves fortes des modèles (Carbon, Neon, Fable, Opus) : la thèse forte (lois de l'univers) n'est pas testable directement, et les premières composantes principales capturent surtout la fréquence des mots (Mu et al. 2018) ; l'isomorphisme exige des représentations relationnelles explicites ou l'étude directe des symétries de matrices de cooccurrence.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 1 et 6) ; lot-8 point 24 ; GO-2026-11-23-24 ; R-5180 ; idees/protocole-x-structure-du-langage-fable-v1.`.
- **Statut** : en cours (dossier 1 du protocole X confié à Fable : 33 sources téléchargées, notes à suivre ; réactivé au point 24 du lot 8).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : détecteur de symétries exactes ou approchées dans les statistiques de cooccurrence d'un corpus scientifique daté comme générateur d'invariants candidats.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 150.0**.
- **Justification de priorisation** : Très fort potentiel si l'on isole des symétries statistiques non triviales (au-delà des biais lexicaux) ; déjà fortement documentée par les 33 sources rassemblées par Fable.

### IDE-2026-11-23-010 — Hypothèse H10 — Signal interne de surprise et erreur de prédiction de récompense (analogue dopaminergique) dans l'organisme

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (messages 1 et 7) + lot 8 (point 2).
- **Énoncé détaillé** : Surveiller les explorations de l'organisme par une sonde lisant un signal analogue à la dopamine (sous-système de récompense éparse de Xu, Yuksekgonul et Zou 2026) afin de repérer quand l'agent est surpris ou découvre une piste féconde. Précision unanime : la surprise brute échoue sur le bruit (« télévision bruitée ») ; la dopamine code une erreur de prédiction de récompense signée et le signal fécond est la surprise suivie d'un gain de compression (Schmidhuber 2010, Oudeyer et al. 2007). Fable note en outre que chez Xu et al. 2026 la corrélation de rang des sondes reste inférieure à 0,4 sur les modèles affinés par renforcement en mathématiques et nulle sur tâches ouvertes.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 1 et 7) ; lot-8 point 2 ; reponse-fable-max-v1.md ; reponse-opus-max-v1.md (complément H10).`.
- **Statut** : question posée au lot 8 point 2 (quel modèle ouvert recommander) ; à tester en lecture seule (jamais optimisé directement).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel et sur banc de notes : lire les neurones de valeur et d'erreur de différence temporelle au dernier jeton d'un modèle ouvert pour tester le motif « surprise puis explication », sous l'invariant strict de non-optimisation directe du score.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 96.0**.
- **Justification de priorisation** : Relie directement l'organisme d'idéation aux recherches du programme sur les sondes et les biais d'évaluation (Xu et al. 2026) ; nécessite choix du modèle ouvert et petite exécution sur carte graphique.

### IDE-2026-11-23-011 — Loi de croissance du champ avec le rapprochement des réseaux et nécessité de collisions actives

- **Catégorie et bloc d'origine** : idée ; Intuitions directeur (messages 4 et 5).
- **Énoncé détaillé** : À mesure que deux réseaux ou deux bouts d'un réseau déformé se rapprochent sous une transformation, le champ d'interaction croît comme l'inverse d'une fonction croissante de la bonne distance (et devient maximal dans la direction où l'invariance apparaît), mais ce rapprochement seul ne suffit pas : des collisions actives (expériences, publications, discussions) sont nécessaires. Le champ combine ainsi l'invariance, la densité du réseau et les probabilités de rencontre.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (messages 4 et 5).`.
- **Statut** : versée pour la suite ; traduite en facteur multiplicatif densité × champ × serrure dans les modèles.
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : coupler le repérage de paires à forte compatibilité potentielle avec un opérateur actif de collision expérimentale ou logique entre les deux voisinages.
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 3/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 108.0**.
- **Justification de priorisation** : Formalisée dans la fonction de hasard des modèles ; permet de séparer les rapprochements passifs des déclenchements provoqués.

### IDE-2026-11-23-012 — Mesurer les invariances directement par collision des structures sous-jacentes (réponse à la circularité du champ)

- **Catégorie et bloc d'origine** : idée ; Intuitions directeur (message 6).
- **Énoncé détaillé** : Pour éviter de définir le champ d'interaction par son résultat final, mesurer directement les invariances par collision et rapprochement des structures mathématiques sous-jacentes ou des réseaux qui sous-tendent les idées, sous réserve stricte d'hygiène temporelle (données antérieures à la découverte).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 6) ; note-hypotheses-appuis-formalismes-v1.md (section 3, point 4).`.
- **Statut** : retenue comme principe de mesure non circulaire.
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : évaluation des candidats par alignement structurel sur données antérieures ou sur mondes plantés sans accès aux étiquettes cibles.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 192.0**.
- **Justification de priorisation** : Garde méthodologique essentielle contre la circularité.

### IDE-2026-11-23-013 — Formalisation de l'invariance par homomorphisme de graphes typés et équivariance d'opérateurs discrets

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 6) + question suivi homomorphisme.
- **Énoncé détaillé** : Proposition formulée lors des échanges sur H3 et soumise en question de suivi aux modèles de Google, Fable et Opus : remplacer Noether par l'homomorphisme de graphes typés ou l'équivariance d'opérateurs discrets. Verdict unanime des trois réponses Google (Argon, Carbon, Neon) : l'homomorphisme strict et l'équivariance globale de groupe doivent être rejetés et remplacés (cf. objets formels ci-dessous).
- **Source exacte** : `docs/notes/idee-interessante-v1/question-suivi-homomorphisme-v1.md ; GO-2026-11-23-23 ; reponses-google-v1/reponse-*-homomorphisme-v1*.md.`.
- **Statut** : évaluée et réformée (remplacée par foncteurs partiels / spans, groupoïdes locaux et faisceaux cellulaires).
- **Lien avec l'organisme d'idéation** : Directement applicable au moteur de représentation de la couche de structure de l'organisme au dégel.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Clarification mathématique majeure déjà tranchée conceptuellement ; oriente immédiatement l'architecture des expériences minimalistes.

### IDE-2026-11-23-014 — Identités et invariances tenues pour vraies qui ne vont pas de soi et profondeur de leurs conséquences

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 7) + GO-2026-11-23-27.
- **Énoncé détaillé** : Explorer le fait de découvrir que des vérités apparemment simples (identités ou invariances tenues pour évidentes depuis toujours) ne vont en réalité pas de soi, et formaliser mathématiquement les implications profondes qui en découlent une fois les réseaux correspondants identifiés. La mère distingue trois figures (identité contingente élevée en principe, fausse identité scindée, identité cachée entre domaines), propose quatre objets mathématiques (scission en personas, isomorphisme canonique ou non, faisceau avec obstruction de recollement, transport le long d'un chemin en théorie des types homotopiques) et relie ce motif au contrôle des modèles de langage (ce que lit la sonde contre ce qu'emploie le modèle, raisonnement écrit contre calcul effectif).
- **Source exacte** : `docs/notes/identites-tenues-pour-vraies-v1/demande-directeur-et-reformulation-mere-v1.md ; GO-2026-11-23-27 ; note-hypotheses-appuis-formalismes-v1.md (F8, T5).`.
- **Statut** : dossier 2 du protocole X ouvert (confié à Fable, interrompu par limite d'usage à reprendre).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel et sur corpus historique : détecteur d'obstructions de faisceaux et scission de nœuds sur les concepts confondus.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Lien direct avec le contrôle boîte blanche et avec les plus grands tournants de la physique ; faisabilité élevée sur corpus historiques et sur activations de modèles ouverts.

### IDE-2026-11-23-015 — Principe variationnel sur un graphe conceptuel discret et dissipatif

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 7) + GO-2026-11-23-28.
- **Énoncé détaillé** : Face à l'impossibilité d'appliquer un lagrangien canonique continu, chercher un véritable principe variationnel applicable à un graphe conceptuel discret et dissipatif. La note de synthèse candidate trois outils : l'entropie maximale sur les trajectoires (« maximum caliber », Jaynes ; Pressé et al. 2013), l'action des grandes déviations (Onsager-Machlup) et les flots de gradient d'entropie sur graphes (Maas 2011).
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 7) ; GO-2026-11-23-28 ; note-hypotheses-appuis-formalismes-v1.md (F10).`.
- **Statut** : dossier 3 du protocole X confié à Fable (GO-2026-11-23-28), en attente de fusion et de collisionneur.
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme au dégel : estimer si les trajectoires de découverte historiques minimisent une action de grandes déviations ou maximisent un flux d'entropie de trajectoires par rapport à un modèle nul.
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 2/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 48.0**.
- **Justification de priorisation** : Plus spéculatif et mathématiquement lourd ; gain informatif intéressant si un principe variationnel discret survit à la confrontation empirique.

### IDE-2026-11-23-016 — Séparation structure abstraite / alphabet relationnel humain et troisième couche « méta » du graphe

- **Catégorie et bloc d'origine** : hypothèse ; Intuitions directeur (message 7) + question méta-espace.
- **Énoncé détaillé** : Distinguer (a) la structure mathématique abstraite sous-jacente aux phénomènes et (b) sa transcription dans un alphabet relationnel humain qui peut manquer, et résoudre en deux phases via un méta-espace mathématique et une troisième couche « méta » portant anomalies, problèmes ouverts et objets formels en gestation. Réponse critique de Carbon : rejeter le dualisme ontologique et l'approche séquentielle en deux phases (écueil combinatoire du programme de Lenat et démenti historique de Cavaillès, Lakatos et Piaget) ; conserver la troisième couche comme « couche chantier » opératoire convertissant des régularités implicites en primitives de premier ordre par cycles alternés.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 7) ; question-meta-espace-mathematique-v1.md ; reponses-google-v1/reponse-carbon-meta-espace-v1.md ; GO-2026-11-23-29.`.
- **Statut** : répondu par Carbon ; versé au dossier 6 du protocole X et repris dans le lot 8 (points 9 à 16, 20 à 23).
- **Lien avec l'organisme d'idéation** : Architecture cible de la version avancée de l'organisme d'idéation au dégel : ajouter une troisième couche chantier (schémas anti-unifiés, obstructions, problèmes ouverts, proto-objets réservoirs).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Ouvre la porte au passage de la simple recombinaison à l'invention de primitives mathématiques nouvelles ; très forte portée théorique et pratique.

### IDE-2026-11-23-017 — Traction par les anomalies empiriques et maximisation du progrès de compression dans l'organisme

- **Catégorie et bloc d'origine** : idée ; Intuitions directeur (message 7).
- **Énoncé détaillé** : Exploiter explicitement les anomalies persistantes (Kuhn, Lakatos) pour polariser la recherche d'analogies et de nouveaux objets, et maximiser le progrès de compression ou d'apprentissage (Oudeyer et al. 2007, Schmidhuber 2010) pour orienter la quête d'idées vraiment inédites.
- **Source exacte** : `docs/notes/idee-interessante-v1/intuitions-directeur-2026-11-23-v1.md (message 7) ; note-hypotheses-appuis-formalismes-v1.md (section 3 et T8).`.
- **Statut** : à intégrer au dégel de l'organisme.
- **Lien avec l'organisme d'idéation** : Deux des trois nouveaux opérateurs de l'organisme au dégel (T8) : polarisation par les anomalies et récompense par le gain de compression conjointe.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Directement opérationnalisable dans l'organisme sans dépendre de l'instrumentation externe lourde.

### IDE-2026-11-23-018 — Distinction analytique des trois questions : intérêt perçu, vérité/fécondité, et mécanisme de production

- **Catégorie et bloc d'origine** : formalisme ; Réponses Google v1 + Fable + Opus.
- **Énoncé détaillé** : Séparer rigoureusement trois questions confondues par H1–H10 : (1) l'intérêt subjectif d'un public à une date donnée (Davis 1971, surprise bayésienne, relatif et périssable ; Boudreau et al. 2016 montrent que les évaluateurs pénalisent la forte nouveauté) ; (2) la validité et fécondité épistémique (unification, compression, survie expérimentale, disruption) ; (3) l'heuristique de production (taux de naissance, recherche). Confondre (1) et (2) mène à des métaphores fausses ; confondre (2) et (3) prend un filtre rétrospectif pour un générateur.
- **Source exacte** : `reponse-argon-v1.md (1), reponse-carbon-v1.md (1), reponse-neon-v1.md (1), reponse-fable-max-v1.md (1), reponse-opus-max-v1.md (1).`.
- **Statut** : consensus unanime des cinq modèles ; adopté dans la note v1.
- **Lien avec l'organisme d'idéation** : Impose à l'organisme de ne jamais utiliser l'intérêt perçu ni un juge modèle comme oracle de vérité (conforme à la décision N-058 : oracle des mondes plantés et coût).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 375.0**.
- **Justification de priorisation** : Garde conceptuelle sans coût, indispensable à l'interprétation honnête de tout essai futur.

### IDE-2026-11-23-019 — Graphe multiplexe daté à trois couches de base (usage, structure typée, communautés humaines)

- **Catégorie et bloc d'origine** : formalisme ; Réponses Google v1 + Fable + Opus.
- **Énoncé détaillé** : Représenter l'état du savoir strictement avant la date t par un graphe ou hypergraphe à trois couches : Usage (cooccurrences et plongements diachroniques alignés par Procuste orthogonal, sans modèle futur), Structure (multigraphe orienté typé avec tables d'incompatibilités et arbres d'opérateurs mathématiques anonymisés), et Communautés (bipartite auteurs-concepts ou distributions de revues). Tous les prédicteurs sont calculés exclusivement avant t.
- **Source exacte** : `reponse-argon-v1.md (2.1), reponse-carbon-v1.md (2.1), reponse-neon-v1.md (2.1), reponse-fable-max-v1.md (2), reponse-opus-max-v1.md (2).`.
- **Statut** : consensus des cinq modèles.
- **Lien avec l'organisme d'idéation** : Structure de données de référence pour l'organisme et pour les expériences rétrospectives hors-temps.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 300.0**.
- **Justification de priorisation** : Socle indispensable à la reproductibilité et à l'étanchéité temporelle.

### IDE-2026-11-23-020 — Mesure de l'alignement structurel inter-domaines sans fuite lexicale par transport de Gromov-Wasserstein fusionné / partiel / non équilibré et signatures de rôle

- **Catégorie et bloc d'origine** : formalisme ; Réponses Google v1 + Fable + Opus.
- **Énoncé détaillé** : Pour aligner deux voisinages issus de vocabulaires totalement disjoints : effacer les noms de nœuds et utiliser des signatures structurelles intrinsèques (raffinement typé de Weisfeiler-Lehman, struc2vec) en criblage rapide, puis le transport optimal de Gromov-Wasserstein (fusionné, partiel ou non équilibré, sur résolvantes ou plus courts chemins orientés) et l'appariement exact de sous-graphes (moteur d'appariement de structures, algorithme des graphes par correspondance exacte, algorithme de plus grand sous-graphe commun ou programmation linéaire mixte) pour calculer couverture, préservation, systématicité et taux de conflits.
- **Source exacte** : `reponse-argon-v1.md (2.2, 4), reponse-carbon-v1.md (2.2, 4), reponse-neon-v1.md (2.2, 4), reponses homomorphisme (section 2), reponse-fable-max-v1.md (2, 4), reponse-opus-max-v1.md (2, 4).`.
- **Statut** : consensus sur le transport de Gromov-Wasserstein + filtrage discret ; à éprouver.
- **Lien avec l'organisme d'idéation** : Fournit à l'organisme un moteur calculable de comparaison structurale agnostique au jargon disciplinaire.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Bibliothèque Python Optimal Transport disponible ; coût calculatoire bas sur graphes de voisinage de rayon 2.

### IDE-2026-11-23-021 — Esquisses catégoriques, ologs, spans de foncteurs partiels et faisceaux cellulaires avec cohomologie H0

- **Catégorie et bloc d'origine** : objet candidat ; Réponses homomorphisme (Argon, Carbon, Neon).
- **Énoncé détaillé** : Pour pallier les deux défauts de l'homomorphisme de graphes typés (incapacité d'envoyer une arête sur un chemin composé et exigence d'un typage partagé préexistant), Argon, Carbon et Neon proposent de le remplacer au niveau théorique par des foncteurs et spans de foncteurs partiels entre catégories de schémas quotients (esquisses d'Ehresmann, ologs de Spivak et Kent 2012), complétés par des groupoïdes de symétries locales (Weinstein 1996) et des faisceaux cellulaires (Hansen et Ghrist 2019) dont le noyau du cobord (cohomologie de degré zéro, laplacien de faisceau) caractérise les invariants globaux cohérents.
- **Source exacte** : `reponse-argon-homomorphisme-v1-relance1.md (liminaire, 1, 3) ; reponse-carbon-homomorphisme-v1.md (liminaire, 1.3, 3) ; reponse-neon-homomorphisme-v1.md (liminaire, 1, 3) ; demande-directeur-et-reformulation-mere-v1.md (faisceaux).`.
- **Statut** : proposés par les modèles ; candidats formels de haute valeur à tester.
- **Lien avec l'organisme d'idéation** : À tester dans l'organisme comme formalisme d'encodage des lois et de détection des obstructions de recollement (incohérences entre parties d'une même analogie ou identité).
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 150.0**.
- **Justification de priorisation** : Résout rigoureusement la question des granularités différentes et des fausses identités ; les faisceaux cellulaires sur graphes finis sont calculables par algèbre linéaire.

### IDE-2026-11-23-022 — Théorème de Noether markovien et mécanique variationnelle discrète (démarcation strict / spéculatif)

- **Catégorie et bloc d'origine** : objet candidat ; Réponses Argon, Carbon, Neon homomorphisme.
- **Énoncé détaillé** : Les trois modèles sur l'homomorphisme séparent : (1) ce qui est démontré : Noether discret pour lagrangiens discrets sous symétrie de Lie continue (Marsden et West 2001) et Noether pour processus de Markov en temps continu (Baez et Fong 2013, avec contre-exemple dissipatif brisant la bijection symétrie-conservation) ; (2) ce qui est faux : une « charge sémantique conservée » sur graphe conceptuel statique. Le substitut rigoureux est la préservation des équivalences de chemins (naturalité) et la cohomologie de faisceau.
- **Source exacte** : `reponse-argon-homomorphisme-v1-relance1.md (3) ; reponse-carbon-homomorphisme-v1.md (3) ; reponse-neon-homomorphisme-v1.md (3).`.
- **Statut** : état de l'art formel clarifié.
- **Lien avec l'organisme d'idéation** : Balise pour l'organisme : ne chercher de lois de conservation dynamiques que si l'on définit explicitement une dynamique markovienne ou variationnelle sur le graphe ; sinon utiliser la naturalité et les faisceaux.
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 3/5 ; potentiel de découverte majeure = 2/5 ; **score synthétique = 72.0**.
- **Justification de priorisation** : Évite de perdre du temps sur une piste formellement invalide sur graphes statiques.

### IDE-2026-11-23-023 — Traitement systématique du biais du survivant : cohortes de « mariages mort-nés », essais négatifs et rétractations

- **Catégorie et bloc d'origine** : piste ; Réponses Google v1 + Fable + Opus.
- **Énoncé détaillé** : Modéliser séparément l'étape 1 (naissance / publication d'un mariage inédit) et l'étape 2 (fécondité ultérieure conditionnelle : reprises indépendantes, top décile de citations, indice de disruption) en intégrant explicitement les paires jamais nées, les « ponts morts » (publiés sans reprise sur 5 à 10 ans), les repositionnements échoués en phase II/III de registre public d'essais cliniques ClinicalTrials.gov et les rétractations de base de rétractations scientifiques Retraction Watch. Sans ce dénominateur négatif, un modèle peut prédire seulement la plausibilité rhétorique d'auteur et échouer sur la vérité scientifique.
- **Source exacte** : `reponse-argon-v1.md (3, 5.3) ; reponse-carbon-v1.md (3, 5.3) ; reponse-neon-v1.md (3, 5.2) ; reponse-fable-max-v1.md (3, 5) ; reponse-opus-max-v1.md (3, 5).`.
- **Statut** : consensus des cinq modèles.
- **Lien avec l'organisme d'idéation** : Règle d'hygiène pour l'évaluation des pistes de l'organisme : tenir le registre des échecs et mesurer les taux de base.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 375.0**.
- **Justification de priorisation** : Indispensable à toute validité expérimentale ; gratuit à intégrer dès le premier essai.

### IDE-2026-11-23-024 — Mécanismes oubliés à intégrer au modèle : friction du réel (anomalies), coût d'épreuve, asymétrie donneur-récepteur, porteurs humains et retards de réveil

- **Catégorie et bloc d'origine** : piste ; Réponses Argon, Carbon, Neon, Fable, Opus.
- **Énoncé détaillé** : Les cinq modèles listent les manques de H1–H10 : (1) choc empirique et anomalies (Kuhn, Lakatos) ; (2) asymétrie directionnelle du transfert (du domaine axiomatisé vers le domaine empirique jeune ; Bowdle et Gentner 1997) ; (3) coût et faisabilité expérimentale à la date t ; (4) incitations institutionnelles et biais contre la nouveauté (Wang et al. 2017, Bromham et al. 2016, Boudreau et al. 2016) ; (5) topologie des chercheurs passeurs / migrants entre disciplines (Sourati et Evans 2023) ; (6) découvertes non combinatoires (théorèmes d'impossibilité, contre-exemples) ; (7) « belles au bois dormant » (Ke et al. 2015) exigeant des fenêtres longues ; (8) causalité interventionnelle (Pearl 2009) distincte de la simple corrélation topologique ; (9) différence entre idées jugées prometteuses et exécution réelle (Si et al. 2025).
- **Source exacte** : `reponse-argon-v1.md (6) ; reponse-carbon-v1.md (6) ; reponse-neon-v1.md (6) ; reponse-fable-max-v1.md (6) ; reponse-opus-max-v1.md (6).`.
- **Statut** : pistes à intégrer et tester progressivement dans les versions suivantes du modèle et de l'organisme.
- **Lien avec l'organisme d'idéation** : Chaque manque fournit un axe d'amélioration de l'organisme (exemple : intégrer un critère d'orientabilité donneur-récepteur et une pondération par coût de test).
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 320.0**.
- **Justification de priorisation** : Cartographie complète des angles morts du modèle initial.

### IDE-2026-11-23-025 — Expérience T1 (Argon) — Formes d'équations partagées sur sources composition typographique mathématique de l'archive ouverte arXiv

- **Catégorie et bloc d'origine** : expérience proposée ; Réponse Argon v1 (section 7) + note v1 (T1).
- **Énoncé détaillé** : Sur un échantillon de 100 000 articles archive ouverte de prépublications arXiv (2000–2014), convertir les équations en arbres syntaxiques d'opérateurs anonymisés (variables remplacées par des jetons typés génériques) ; calculer distance d'édition d'arbres et plus grand sous-arbre commun à 2014 entre paires de concepts inter-catégories jamais co-mentionnés ; comparer 400 mariages féconds (2015–2018, évalués en 2024) contre 400 mariages mort-nés appariés. Prédiction : aire sous courbe caractéristique d'efficacité du récepteur >= 0,65 (p < 0,005), rapport de cotes >= 1,50 au-delà du chaînage de surface. Durée estimée : 4 jours sur processeur, budget < 100 euros.
- **Source exacte** : `reponse-argon-v1.md (section 7) ; note-hypotheses-appuis-formalismes-v1.md (T1).`.
- **Statut** : proposée ; en attente de préenregistrement et de devis/GO.
- **Lien avec l'organisme d'idéation** : Alimente directement l'organisme sur la couche des structures mathématiques exactes (arbres d'opérateurs sans bruit de traitement du langage naturel).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Élimine le bruit d'extraction textuelle grâce aux équations exactes ; testable en quelques jours sur processeur.

### IDE-2026-11-23-026 — Expérience T2 (Carbon et Neon) — Cœur H1 × H3 sur graphe biomédical daté (la base de prédications biomédicales SemMedDB, descripteurs médicaux, graphe bibliographique ouvert OpenAlex)

- **Catégorie et bloc d'origine** : expérience proposée ; Réponses Carbon v1, Neon v1 (section 7) + note v1 (T2).
- **Énoncé détaillé** : Geler le graphe à 2015 (ou 2017) à partir de la base de prédications biomédicales SemMedDB, descripteurs médicaux et graphe bibliographique ouvert OpenAlex ; prédire la naissance et surtout la fécondité conditionnelle (reprises par équipes indépendantes sur 5 ans contre paires publiées stériles) des paires inter-branches nées en 2016–2017 (ou 2018). Comparer modèles logistiques nichés : base surface + chaînage à trois termes de Swanson contre modèle ajoutant le score serrure-clé de Gromov-Wasserstein fusionné et son interaction avec la distance de surface, plus contrôle par permutation des étiquettes causales (relations excitatrices contre inhibitrices). Durée estimée : 4 à 5 jours sur station de travail. Réserve technique notée par Fable : la base de prédications biomédicales SemMedDB exige un compte gratuit système unifié de langage médical (nœud mineur) ; base ouverte PubTator 3 est en accès libre direct.
- **Source exacte** : `reponse-carbon-v1.md (section 7) ; reponse-neon-v1.md (section 7) ; note-hypotheses-appuis-formalismes-v1.md (T2) ; reponse-fable-max-v1.md (section 3 et 7).`.
- **Statut** : proposée ; en attente de préenregistrement et de choix base ouverte PubTator 3 / la base de prédications biomédicales SemMedDB.
- **Lien avec l'organisme d'idéation** : Banc d'essai empirique immédiat des opérateurs d'alignement structurel avant intégration définitive à l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Neutralise le biais du survivant par construction (Cible B conditionnelle aux paires publiées) et isole l'effet des types causaux par permutation.

### IDE-2026-11-23-027 — Expérience « le pont suit-il la carte ? » (Fable) — Test du cortège après naissance sur base ouverte PubTator 3

- **Catégorie et bloc d'origine** : expérience proposée ; Réponse Fable max v1 (section 7).
- **Énoncé détaillé** : Sur les relations datées en accès libre de base ouverte PubTator 3 gelées fin 2010 : (A) tester H3 par signatures de rôle typées de profondeur 2 (rapport de cotes >= 1,2 dans le tiers le plus surprenant) ; (B) tester l'interaction distance × structure sur la fécondité 2016–2025 ; (C) prédiction originale du « cortège » : après la naissance d'un pont (a,b), les paires satellites appariées par la correspondance φ naissent avec un taux au moins 1,5 fois supérieur aux paires croisées non alignées. Gardes intégrées sur monde planté et permutation des types. Processeur seul, quelques jours, aucune dépense, accès libre immédiat.
- **Source exacte** : `idees/modele-idees-interessantes-fable-max-v1:docs/notes/idee-interessante-v1/reponse-fable-max-v1.md (section 7).`.
- **Statut** : proposée par Fable ; candidate n° 1 sur processeur sans dépendance de licence.
- **Lien avec l'organisme d'idéation** : Épreuve directe du mécanisme générateur de l'organisme : vérifie si la serrure-clé produit une cascade prévisible de découvertes sœurs et constitue une base naturelle de monde planté.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 625.0**.
- **Justification de priorisation** : Combinaison exceptionnelle : zéro blocage d'accès (base ouverte PubTator 3 libre), zéro dépense graphique, gardes synthétiques incluses, et test inédit du cortège.

### IDE-2026-11-23-028 — Expérience « surface et structure » sur les 2 996 notes réelles d'intérêt d'experts (Gu et Krenn 2026)

- **Catégorie et bloc d'origine** : expérience proposée ; Réponse Opus max v1 (section 7).
- **Énoncé détaillé** : Bras A (processeur seul, 3 jours, aucune dépense) : réanalyser le jeu public Zenodo de Gu et Krenn 2026 (2 996 idées bâties sur des paires de concepts notées en aveugle par 110 directeurs de groupe) en calculant distance de surface (blocs stochastiques), ressemblance de rôle (K0) et Gromov-Wasserstein fusionné à rayon 2 (K2) pour tester si la pente négative de l'intérêt avec la distance s'inverse dans le tiers supérieur de K2 (interaction > 0, gain d'aire sous courbe >= 0,02). Bras C (processeur seul) : prédiction hors-temps sur ce même graphe. Bras B (sur devis, 1 à 2 jours de carte graphique) : extraction de relations typées sur 20 résumés par concept. Complément H10 (sur devis) : lecture des neurones de valeur et erreur de différence temporelle au dernier jeton d'un modèle ouvert.
- **Source exacte** : `idees/modele-idees-interessantes-opus-max-v1:docs/notes/idee-interessante-v1/reponse-opus-max-v1.md (section 7).`.
- **Statut** : proposée par Opus ; Bras A et C prêts pour préenregistrement sans dépense.
- **Lien avec l'organisme d'idéation** : Seul essai confrontant directement le modèle structurel aux jugements d'intérêt réel de 110 chercheurs humains sans avoir à recruter un panel dès la phase 0.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 625.0**.
- **Justification de priorisation** : Jeu de données public prêt (3 Go Zenodo), aucun coût de calcul pour les bras A et C, tranche immédiatement l'objection de Gu et Krenn (2026) contre H1.

### IDE-2026-11-23-029 — Expérience d'alignement pré-découverte sur le corpus Physical Review (cas d'Unruh 1981 + 20 ponts physiques)

- **Catégorie et bloc d'origine** : expérience proposée ; Réponses homomorphisme (Argon, Carbon, Neon — sections 4 et 5).
- **Énoncé détaillé** : Sur les articles Société américaine de physique (1965–1980, strictement avant Unruh 1981), construire annuellement les graphes de dépendance des variables d'équations ou assertions mécanistes en anonymisant totalement les nœuds (« effacement lexical »), et comparer l'alignement par Gromov-Wasserstein (ou résolvantes / Gromov-Wasserstein fusionné sur propriétés différentielles) entre relativité générale et hydrodynamique acoustique avant et après la reformulation de Hawking (1974–1975), face à 500 paires de codes codes thématiques de physique et d'astronomie disjoints témoins et modèles nuls de Maslov-Sneppen. Prédiction : chute significative du score Z (< -3,0) dans la fenêtre [t_dec - 3 ans, t_dec - 1 an] et appariement spontané vitesse du son / horizon.
- **Source exacte** : `reponse-argon-homomorphisme-v1-relance1.md (4, 5) ; reponse-carbon-homomorphisme-v1.md (4, 5) ; reponse-neon-homomorphisme-v1.md (4, 5).`.
- **Statut** : proposée ; requiert accès au jeu de données Société américaine de physique et parseur sans fuite temporelle.
- **Lien avec l'organisme d'idéation** : Teste l'hypothèse forte d'une invariance structurale préexistante détectable avant la publication du pont ; applicable au module de détection précoce de l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 150.0**.
- **Justification de priorisation** : Test très pur contre la thèse constructiviste (« l'isomorphisme est inventé après coup ») ; dépend toutefois de la disponibilité du jeu Société américaine de physique ou d'un équivalent archive ouverte de prépublications arXiv post-1991.

### IDE-2026-11-23-030 — Cinq signaux ex ante d'apparition d'un objet mathématique nouveau (couche chantier)

- **Catégorie et bloc d'origine** : objet candidat ; Réponse Carbon méta-espace (section 1 à 5).
- **Énoncé détaillé** : Détecter où manque une primitive formelle sans connaître l'objet futur via cinq observables datés : (1) inflation descriptionnelle et sous-arbres de dérivation répétés ad hoc (Rissanen) ; (2) homomorphismes frustrés / résidus d'édition concentrés sur les mêmes arêtes (anomalies de Kuhn-Lakatos) ; (3) entropie notationnelle élevée pour une structure relationnelle fixée (prolifération de notations locales concurrentes, Cajori) ; (4) convergence en étoile de réductions conditionnelles entre problèmes ouverts (Wussing) ; (5) transgressions formelles fécondes (cooccurrence de marqueurs discursifs de prudence et de ruptures de typage).
- **Source exacte** : `docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-meta-espace-v1.md (section 2) ; repris dans lot-8 points 8, 9, 10, 23.`.
- **Statut** : reçu et fortement plébiscité par le directeur (lot 8 points 8, 9, 10, 23) ; en attente de généralisation aux grands modèless de langage et à l'alignement.
- **Lien avec l'organisme d'idéation** : Piste majeure pour l'organisme au dégel : doter la couche chantier de détecteurs de tension sur les corpus scientifiques et d'alignement de l'intelligence artificielle.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Renverse le problème de la circularité en mesurant les frictions du présent ; immédiatement opérationnalisable sur les corpus composition typographique mathématique ou d'alignement.

### IDE-2026-11-23-031 — Trois mécanismes pour briser la circularité : Éveil-Sommeil croisé (DreamCoder/Stitch), amorçage quinien algébrique, thématisation automatique

- **Catégorie et bloc d'origine** : objet candidat ; Réponse Carbon méta-espace (section 3).
- **Énoncé détaillé** : Remplacer la recherche aveugle dans un méta-espace par trois opérateurs couplés sur arbres d'opérateurs ou lambda-calcul typé : (1) cycle Éveil (collecter dérivations verbeuses et obstructions) / Sommeil-Abstraction (compression de bibliothèque type Stitch de Bowers et al. 2023 maximisant le gain de description simultanément sur plusieurs bassins éloignés) / Sommeil-Rêve (injection d'essai pour résorber les obstructions) ; (2) amorçage quinien algébrique (Carey 2009 : adjoindre un symbole-réservoir défini par les relations annulant l'obstruction et vérifier la non-trivialité) ; (3) thématisation automatique (Cavaillès 1947, Piaget 1977 : réifier les familles de transformations composables en objets candidats, par exemple des substitutions au groupe, des applications au foncteur).
- **Source exacte** : `docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-meta-espace-v1.md (section 3) ; repris dans lot-8 points 6, 7, 11, 12, 15, 22.`.
- **Statut** : validé par le directeur pour implémentation et test progressif (lot 8 point 22).
- **Lien avec l'organisme d'idéation** : Cœur algorithmique de l'invention de nouveaux objets dans la v2/v3 de l'organisme d'idéation.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Permet potentiellement à un organisme artificiel de synthétiser des abstractions inédites ; exige conception soignée de l'espace de termes et des tests sur mondes plantés.

### IDE-2026-11-23-032 — Expérience des macros composition typographique mathématique et arbres d'équations avant les algèbres amassées (Fomin et Zelevinsky 2002)

- **Catégorie et bloc d'origine** : expérience proposée ; Réponse Carbon méta-espace (section 5).
- **Énoncé détaillé** : Sur les sources publiques .tex de l'archive ouverte arXiv (math.*, q-alg, solv-int, alg-geom) coupées strictement à t0 avant l'introduction des algèbres amassées par Fomin et Zelevinsky (2002) : extraire les définitions locales ad hoc (macros \newcommand et \def) et arbres d'opérateurs canonisés, puis appliquer anti-unification (Plotkin 1970) et apprentissage de bibliothèque (Stitch, Bowers et al. 2023) entre communautés faiblement cocitées. Prédiction double : (1) localiser les futures nouvelles rubriques de la classification mathématique classification des matières mathématiques mieux que les bases ; (2) retrouver dans l'abstraction comprimée en tête le schéma syntaxique de mutation d'amas. Processeur standard, quelques minutes de calcul après extraction.
- **Source exacte** : `docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-meta-espace-v1.md (section 5).`.
- **Statut** : proposée ; préenregistrement à rédiger ; explication des notions demandée au lot 8 point 15.
- **Lien avec l'organisme d'idéation** : Banc d'essai gratuit sur données publiques vérifiant si la compression inter-domaines détecte la naissance d'un objet mathématique majeur avant sa formulation.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Extraordinaire rapport coût/potentiel : données 100 % publiques sur l'archive ouverte arXiv, zéro coût carte graphique, vérité terrain institutionnelle externe (classification des matières mathématiques), et test d'extraction d'une vraie structure mathématique.

### IDE-2026-11-23-033 — Batterie d'expériences complémentaires T3 à T7 (multiples, gain de compression sur modèle 8B, scissions, taille finie, symétries)

- **Catégorie et bloc d'origine** : expérience proposée ; Note v1 des hypothèses (T3, T4, T5, T6, T7).
- **Énoncé détaillé** : Regroupe cinq tests synthétisés dans la note v1 : T3 (test des découvertes multiples de Merton/Ogburn-Thomas contre la diffusion d'un cadre commun) ; T4 (progrès de compression sur modèle ouvert de 8 milliards de paramètres en préfixant l'idée candidate sur des faits des deux domaines parents) ; T5 (détection ex ante de la scission de nœuds en personas ou de l'obstruction de faisceau avant la publication historique de distinctions telles que simultanéité ou chaleur/température, contre témoins polysémiques banals) ; T6 (analyse de taille finie sur domaines naissants) ; T7 (recherche de symétries statistiques de cooccurrence dans des corpus scientifiques sur le modèle de Karkada et al. 2026).
- **Source exacte** : `docs/notes/idee-interessante-v1/note-hypotheses-v1/note-hypotheses-appuis-formalismes-v1.md (section 5, T3 à T7).`.
- **Statut** : inscrites comme pistes de test ; T5 et T7 liées au protocole X.
- **Lien avec l'organisme d'idéation** : Chacun de ces tests correspond à un module ou critère évaluable sur les trajectoires et productions de l'organisme.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 256.0**.
- **Justification de priorisation** : Particulièrement T5 (scissions) et T4 (gain de compression sur modèle ouvert) qui sont légers et directement transférables au contrôle boîte blanche.

### IDE-2026-11-23-034 — Correction des comparaisons multiples, détection endogène du changement de représentation et symétries de cooccurrence sans co-apparition

- **Catégorie et bloc d'origine** : piste ; Réponse Neon homomorphisme + Note v1 (section 2) + Opus.
- **Énoncé détaillé** : Trois pistes spécifiques issues des modèles : (1) contrôle systématique du taux de fausses découvertes (Benjamini-Hochberg) sur toutes les paires et fenêtres temporelles (Neon homomorphisme) ; (2) détection purement endogène dans D1 seul d'une rupture de formalisme ou de longueur de description avant tout couplage vers D2 (Neon homomorphisme, contre la circularité) ; (3) exploitation du résultat de Karkada et al. (2026) montrant que les symétries statistiques survivent à l'ablation des co-apparitions directes entre termes (R-5180).
- **Source exacte** : `reponse-neon-homomorphisme-v1.md (4, 5) ; note-hypotheses-appuis-formalismes-v1.md (H9).`.
- **Statut** : pistes techniques à intégrer aux protocoles et à l'organisme.
- **Lien avec l'organisme d'idéation** : Renforcent la rigueur statistique des recherches de ponts dans l'organisme (évite les faux positifs par multiplicité et détecte des symétries latentes sans citation directe).
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 192.0**.
- **Justification de priorisation** : Garde-fous statistiques et algorithmiques indispensables.

### IDE-2026-11-23-035 — système de découverte symbolique de Udrescu et Tegmark (Udrescu et Tegmark 2020) et rupture de la circularité comme inspiration pour l'organisme

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 1.
- **Énoncé détaillé** : Examiner comment système de découverte symbolique de Udrescu et Tegmark (régression symbolique exploitant symétries dimensionnelles, séparabilité, invariance d'échelle sur graphes et réseaux neuronaux auxiliaires) procède et comment Udrescu et Tegmark ainsi que DreamCoder ont brisé la circularité, afin de s'en servir ou s'en inspirer dans l'organisme.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 1).`.
- **Statut** : demande du directeur en attente de traitement (regroupée dans le lot 8).
- **Lien avec l'organisme d'idéation** : Piste directe pour l'organisme au dégel : extraire des opérateurs de décomposition par invariance et symétrie d'échelle avant recherche combinatoire.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 256.0**.
- **Justification de priorisation** : Méthode éprouvée en physique symbolique ; réutilisation directe de ses principes de réduction dimensionnelle et séparation de variables.

### IDE-2026-11-23-036 — Choix du modèle ouvert pour le sous-système de récompense éparse (« dopamine ») comme observateur d'idées justes

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 2.
- **Énoncé détaillé** : Suite à la piste de l'observateur interne des idées qui se révèlent justes (papier Xu et al. 2026), question en demande approfondie aux modèles et au collisionneur : quel modèle ouvert précis recommander pour observer ce signal ?
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 2) ; reponse-opus-max-v1.md (section 7, complément H10).`.
- **Statut** : en attente de traitement groupé (lot 8) ; préconisation partielle à vérifier (modèles ouverts étudiés par Xu et al. 2026, Qwen/Llama).
- **Lien avec l'organisme d'idéation** : Instrumente la mesure d'erreur de différence temporelle et de surprise sur l'organisme (en lecture seule, jamais en objectif d'optimisation).
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 72.0**.
- **Justification de priorisation** : Conditionné aux réserves déjà relevées par Fable sur Xu et al. 2026 (corrélation < 0,4 en mathématiques, absente sur tâches ouvertes).

### IDE-2026-11-23-037 — Inscription universelle des pistes des modèles Gemini et du collisionneur v2 dans l'organisme

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 3.
- **Énoncé détaillé** : Consigne explicite du directeur : « inscris toutes les pistes des Gemini et les pistes à venir de la v2 comme pistes à tester dans l'organisme ; toutes mes hypothèses et toutes les idées doivent être testées ».
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 3) ; fusionner_v1.py.`.
- **Statut** : décidée (mandat actif du bibliothécaire et de la veille de cap).
- **Lien avec l'organisme d'idéation** : Fonde la liste exhaustive des pistes à éprouver dans l'organisme au dégel ; aucune piste n'est écartée sans décision nommée.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 375.0**.
- **Justification de priorisation** : Règle de gouvernance scientifique du programme d'idéation.

### IDE-2026-11-23-038 — Réécritures éditoriales de la note de vulgarisation et de la note complète (mode Étienne Klein, préface savante, proposition de subvention)

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 4.
- **Énoncé détaillé** : Réécrire la note de vulgarisation comme une note de synthèse académique soutenue et littéraire (mode Étienne Klein), puis la mettre à jour en note manuscrite de préface d'un ouvrage scientifique majeur pour public averti ; faire le même passage sur la note technique complète non vulgarisée sous forme de proposition de recherche pour demande subventions.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 4) ; R-5182 (session_016QhUrvFJWJ9vK6w842yCi2).`.
- **Statut** : en cours (session dédiée lancée avant l'arrêt de 19:02Z, interrompue à reprendre).
- **Lien avec l'organisme d'idéation** : Valorisation et recherche de financement (appui aux bourses mentionnées au point 17), sans effet direct sur le moteur de l'organisme.
- **Évaluation multicritère** : gain informatif = 2/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 3/5 ; potentiel de découverte majeure = 1/5 ; **score synthétique = 24.0**.
- **Justification de priorisation** : Utile pour la demande subventions et la communication ; aucune priorité sur les expériences scientifiques.

### IDE-2026-11-23-039 — Réactualisation de la formation automatique de théories pures (Colton 2002 / Automated Mathematician (programme de Lenat) de Lenat) par les grands modèless de langage modernes

- **Catégorie et bloc d'origine** : hypothèse ; Lot 8 — Point 5.
- **Énoncé détaillé** : Face à l'objection selon laquelle la formation automatique de théories pures diverge dans des définitions formellement valides mais stériles (Ritchie et Hanna 1984 sur le programme Automated Mathematician de Lenat ; Colton 2002), le directeur demande réactualiser cette question à l'ère des grands modèless de langage de pointe capables de filtrage sémantique et d'intuition mathématique.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 5).`.
- **Statut** : à traiter et intégrer au protocole X (fusionné avec les points 10, 11 et 14).
- **Lien avec l'organisme d'idéation** : Piste à tester dans l'organisme : coupler un synthétiseur formel (type Stitch / vérification exacte) à un sélecteur sémantique par grand modèle de langage pour couper la prolifération stérile.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 250.0**.
- **Justification de priorisation** : Lève potentiellement le principal blocage historique de la découverte mathématique automatisée des années 1980–2000.

### IDE-2026-11-23-040 — Pédagogie approfondie et réutilisation des méthodes de Hofstadter, Carey, DreamCoder, Stitch, Cavaillès/Piaget et des objets techniques de Carbon

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Points 6, 7 et 15.
- **Énoncé détaillé** : Demande d'explications rigoureuses et compréhensibles sur : Hofstadter et Fluid Analogies Research Group (1995), l'amorçage quinien et symboles-réservoirs (Carey 2009), la thématisation automatique (Cavaillès 1947, Piaget 1977), et les concepts techniques de la réponse de Carbon (mutations d'amas de Fomin et Zelevinsky 2002, nouvelles rubriques de la classification mathématique classification des matières mathématiques, liens intra-couche et inter-couches, substrat combinatoire en arbres d'opérateurs ou lambda-calcul typé, défauts systématiques d'isomorphisme, signature mesurable d'un objet manquant par épicycles/correctifs ad hoc). De plus (point 7) : examiner ce que l'on peut reprendre directement (théories, méthodes, objets, code libre) de DreamCoder et de Carey pour l'organisme.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (points 6, 7, 12, 15).`.
- **Statut** : en attente de traitement (à regrouper : explication claire + audit de réutilisabilité logicielle de DreamCoder et Stitch).
- **Lien avec l'organisme d'idéation** : Réemploi direct de code ouvert (Stitch en Rust/Python, algorithmes de DreamCoder) comme briques de la troisième couche de l'organisme.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Audit technique de réemploi du code Stitch/DreamCoder rapide et à fort levier immédiat.

### IDE-2026-11-23-041 — Application de l'entropie notationnelle (Cajori) et des 5 signaux ex ante à l'alignement, l'interprétabilité mécaniste et la sûreté de l'intelligence artificielle par compréhension sémantique

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 8 et 9.
- **Énoncé détaillé** : Appliquer la détection ex ante d'apparition de nouveaux objets mathématiques (en particulier l'entropie notationnelle, les marqueurs discursifs de précaution et les ruptures de typage) au champ de l'alignement de l'intelligence artificielle, de l'interprétabilité mécaniste et de la sûreté, en utilisant des grands modèless de langage qui extraient le sens réel des transgressions formelles plutôt que de simples détecteurs lexicaux de mots.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (points 8 et 9).`.
- **Statut** : à traiter et tester (protocole X sur les signaux ex ante, points 9, 10 et 23).
- **Lien avec l'organisme d'idéation** : Piste directe pour l'organisme appliqué à l'alignement : repérer dans la littérature de sûreté/interprétabilité les zones de bricolage ad hoc où manque un objet formel unificateur.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 250.0**.
- **Justification de priorisation** : Cœur de l'application stratégique du programme : utiliser les signaux ex ante non pas seulement sur les mathématiques pures, mais pour localiser les percées nécessaires en alignement.

### IDE-2026-11-23-042 — Mariage inédit entre capacités modernes des grands modèless de langage avancés (2026) et signaux ex ante / troisième couche sur l'histoire des sciences

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 10.
- **Énoncé détaillé** : Remue-méninges en demande approfondie : exploiter les capacités des grands modèless de langage de 2026 (raisonnement sur Navier-Stokes, avancées partielles sur Riemann) pour découvrir des leviers inédits de recherche systématique et ex ante de découvertes scientifiques (application à l'alignement), en apprenant sur l'histoire des sciences (physique, mathématiques, biologie) à partir des points 2 et 3 de Carbon (signaux ex ante et rupture de la circularité). Pipeline demandé : Carbon, Neon, Opus, collisionneur, fusion et protocole X.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 10).`.
- **Statut** : à traiter dans le lot 8 (sous règle d'économie : question fusionnée avec les points 5, 11, 14).
- **Lien avec l'organisme d'idéation** : Architecture hybride à tester : grand modèle de langage comme moteur d'abstraction sémantique et d'anti-unification couplé à la couche chantier.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Exige un contrôle strict de non-contamination temporelle (voir point 13 et 21) pour ne pas confondre mémorisation rétrospective et réelle capacité de découverte.

### IDE-2026-11-23-043 — Apprentissage de bibliothèque par grand modèle de langage couplé à la compression longueur de description minimale inter-bassins (Stitch)

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 11.
- **Énoncé détaillé** : Approfondir l'idée de combiner Stitch (Bowers et al. 2023) et le gain de longueur de description minimale (Rissanen) sur plusieurs bassins éloignés en y injectant un grand modèle de langage pour proposer des abstractions candidates là où l'énumération pure bloque combinatoirement.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 11).`.
- **Statut** : en attente de traitement (regroupé en demande approfondie dans le lot 8).
- **Lien avec l'organisme d'idéation** : Mécanisme hybride « proposition par grand modèle de langage + vérification et comptage de compression par Stitch » directement testable dans l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 250.0**.
- **Justification de priorisation** : Réunit la puissance de proposition sémantique des modèles modernes et la rigueur mesurable sans hallucination de la compression de programmes.

### IDE-2026-11-23-044 — Banc de vérité terrain sans fuite temporelle : modèle entraîné avant t0 (physique pré-1900) ou modèles fermés au web post-coupure

- **Catégorie et bloc d'origine** : expérience proposée ; Lot 8 — Points 13 et 21.
- **Énoncé détaillé** : Deux axes liés à la non-contamination temporelle : (a) rechercher le projet ayant entraîné un petit modèle de langage sans contamination sur des textes de physique antérieurs à 1900 (qui aurait pressenti quanta et dualité onde-corpuscule) et vérifier si code et modèle sont réutilisables ; (b) évaluer un modèle sans accès web sur des découvertes publiées après sa coupure d'entraînement pour obtenir un taux de succès mesurable hors contamination ; (c) point 21 : comment garantir rigoureusement l'absence de fuite future quand on exploite les capacités de raisonnement de grands modèless pré-entraînés après t0 (demande approfondie -> collisionneur).
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (points 13 et 21).`.
- **Statut** : double demande en attente : recherche bibliographique/code sur le projet pré-1900 + question protocole X au collisionneur (point 21).
- **Lien avec l'organisme d'idéation** : Crucial pour l'organisme : toute expérience de rétrodiction utilisant un modèle de langage exige soit un modèle entraîné avant t0, soit une fenêtre temporelle post-coupure du modèle, soit un protocole d'anonymisation structurelle prouvé étanche.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 200.0**.
- **Justification de priorisation** : Sans résolution de ce verrou méthodologique, aucune rétrodiction à l'aide grands modèless de langage n'est publiable ni scientifiquement opposable.

### IDE-2026-11-23-045 — Double stratégie de découverte : objets déjà existants non reliés (réduction de dimension) contre objets hors alphabet relationnel — et liste des 12 objectifs ultimes

- **Catégorie et bloc d'origine** : hypothèse ; Lot 8 — Point 14.
- **Énoncé détaillé** : Le directeur formule une dichotomie stratégique majeure : parfois les objets existent déjà dans le déluge de publications et il manque une réduction de dimensionnalité ou une mise en relation pour isoler les bonnes directions (exemples du programme : programmation de poids, lentille neuronale) ; parfois il faut inventer des objets hors alphabet. Il énumère 12 objectifs ultimes cibles (1. problème difficile de l'alignement ; 2. conscience dans les modèles ou substrat biologique ; 3. Big Bang, trous noirs et galaxies précoces ; 4. origine de la vie ; 5. fusion nucléaire ; 6. hypothèse de Riemann ; 7. conciliation relativité-quantique falsifiable ; 8. lien gravité-information ; 9. contrôle d'une superintelligence non alignée ; 10. aligner une intelligence artificielle auto-améliorante sans experts ni vérité terrain ; 11. problèmes urgents d'alignement et sûreté ; 12. conditions et automatisation des révolutions scientifiques) et demande comment combiner recherche d'objets nouveaux et recherche automatisée de découvertes en 2026.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 14).`.
- **Statut** : en attente (Carbon high, Fable/équivalent, Opus, collisionneur puis protocole X).
- **Lien avec l'organisme d'idéation** : Définit les deux régimes d'exploration de l'organisme : régime 1 (extraction de sous-espaces et lentilles sur concepts existants) contre régime 2 (synthèse de primitives hors alphabet).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Cadre stratégique directeur ; la distinction entre exploration intra-alphabet (réduction de dimension) et hors-alphabet (thématisation) éclaire l'architecture globale.

### IDE-2026-11-23-046 — Épreuve croisée de la proposition de Carbon sur le méta-espace avec bras témoin neutre au collisionneur

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 16.
- **Énoncé détaillé** : Demander à Fable (ou substitut habilité) de répondre indépendamment à la question du méta-espace mathématique, puis de contre-lire la réponse de Carbon ; contre-lectures croisées jugées par la mère ; envoyer le tout comme matière première à un bras du collisionneur, apparié à un bras témoin à demande neutre sans matière première pour mesurer si la matière première enrichit ou biaise.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 16) ; decision-economie-protocole-x-v1.md (règle 7).`.
- **Statut** : décidée (GO-2026-11-23-31) ; en attente de réponse Fable/substitut et de devis collisionneur.
- **Lien avec l'organisme d'idéation** : Expérience méthodologique contrôlant la validité même du protocole X qui alimente l'organisme.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 96.0**.
- **Justification de priorisation** : Mesure empirique indispensable pour éviter le biais d'ancrage dans les collisionneurs.

### IDE-2026-11-23-047 — Programme d'expériences décisives à court terme (quelques jours) pour améliorer l'organisme et questions stratégiques A, B, C

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Points 17 et 19.
- **Énoncé détaillé** : Faisant fi d'un budget strict grâce à une demande bourse, élaborer le programme des petites expériences décisives faisables en quelques jours pour trancher les questions ouvertes et faire que l'organisme explore mieux que le hasard des idées fécondes, surprenantes et des objets mathématiques nouveaux, classées par gain informatif × facilité × coût × portée ; et répondre aux trois questions A (meilleures chances pour commencer), B (meilleures chances pour percer et automatiser les découvertes, notamment en alignement), C (par quoi commencer exactement).
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (points 17 et 19).`.
- **Statut** : en cours (rapport du bibliothécaire livré ici ; volet collisionneur à lancer sous règle d'économie).
- **Lien avec l'organisme d'idéation** : Feuille de route immédiate du dégel de l'organisme d'idéation.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 625.0**.
- **Justification de priorisation** : Objet central de la présente mission et levier direct d'exécution dès les prochains jours.

### IDE-2026-11-23-048 — Règle d'économie du protocole X : portfolio décorrélé par famille (Carbon + Opus + Fable), retrait d'Argon, Neon conditionnel, regroupement par axe

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 18 + decision-economie-protocole-x-v1.md.
- **Énoncé détaillé** : Mesures de recouvrement sur les deux premières questions Google (recouvrement_v1.py) : Jaccard des termes 0,36–0,45, des références 0,16–0,36 ; Argon le plus proche de Carbon et le moins fiable (1 arrêt RECITATION) ; Neon le plus original (14 à 29 références propres) mais 1,6 à 3,4 fois plus cher que Carbon. Règle adoptée pour le lot 8 : Carbon toujours lu à part ; Argon retiré des envois de fond ; Neon réservé à l'exploration ouverte avec règle d'arrêt séquentielle (au moins 2 unités propres fortes sur ses 2 premières réponses) ; décorrélation assurée par diversité de familles (Carbon + Anthropic) ; contre-lectures groupées ; bras principal et témoin appariés. Coût Google du lot 8 ramené à 4–5 dollars américains.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/decision-economie-protocole-x-v1.md ; mesure/recouvrement_v1.py ; mesure/sortie-recouvrement-v1.txt ; R-5189.`.
- **Statut** : décidée et versée par la cheffe d'orchestre du lot 8 (en attente de confirmation sur mesure par unités).
- **Lien avec l'organisme d'idéation** : Optimise le rendement par dollar de la boucle externe d'idéation qui conçoit et alimente l'organisme.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 2/5 ; **score synthétique = 200.0**.
- **Justification de priorisation** : Décision opérationnelle chiffrée déjà exécutée sur mesures reproductibles.

### IDE-2026-11-23-049 — Apport spécifique de l'exploration d'objets mathématiques hors alphabet relationnel pour l'alignement et le contrôle de l'intelligence artificielle

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 20.
- **Énoncé détaillé** : Remue-méninges en demande approfondie au protocole X complet : quel est l'apport véritable, potentiel et probable de la recherche de nouveaux objets mathématiques hors alphabet relationnel existant pour produire des découvertes majeures en alignement et en contrôle (notamment boîte blanche) de l'intelligence artificielle ?
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 20).`.
- **Statut** : en attente de lancement groupé au protocole X.
- **Lien avec l'organisme d'idéation** : Relie directement l'organisme d'idéation (atelier d'objets nouveaux) aux verrous théoriques de l'alignement (spécification d'objectifs, interprétabilité, contrôle d'agents avancés).
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Question stratégique clé justifiant l'investissement dans la 3e couche chantier au-delà de la simple fouille bibliographique.

### IDE-2026-11-23-050 — Mise à l'épreuve comparative et séquentielle des mécanismes brisant la circularité

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 22.
- **Énoncé détaillé** : Consigne du directeur sur les trois mécanismes proposés par Carbon pour casser la circularité (Éveil-Sommeil croisé type DreamCoder/Stitch, amorçage quinien algébrique, thématisation automatique) et tout autre mécanisme candidat : tous les tester, et implémenter les plus prometteurs par ordre de gain informatif × coût × portée × potentiel de découverte majeure.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 22).`.
- **Statut** : décidée dans le principe ; à décliner en plan d'expériences sur mondes plantés au dégel de l'organisme.
- **Lien avec l'organisme d'idéation** : Cahier des charges direct de l'ablation comparative des opérateurs de la couche chantier dans l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 187.5**.
- **Justification de priorisation** : Permet de savoir expérimentalement quel mécanisme (compression croisée, symboles-réservoirs, ou thématisation) génère réellement de nouveaux invariants sans explosion stérile.

### IDE-2026-11-23-051 — Détection par méthodes ex ante des zones de révolutions imminentes en intelligence artificielle (auto-amélioration, intelligence artificielle générale, superintelligence, alignement)

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 23.
- **Énoncé détaillé** : Appliquer des méthodes similaires aux cinq signaux ex ante (inflation ad hoc, homomorphismes frustrés, entropie notationnelle, convergence de problèmes ouverts, transgressions formelles) pour cartographier dès aujourd'hui où vont émerger les prochains concepts, objets formels et révolutions majeures en architecture d'intelligence artificielle, auto-amélioration récursive et alignement.
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 23).`.
- **Statut** : en attente de passage au protocole X (fusionnable avec points 9 et 10).
- **Lien avec l'organisme d'idéation** : Piste à tester immédiatement sur un corpus récent de l'archive ouverte arXiv (informatique (intelligence artificielle et apprentissage automatique), alignement) gelé à t0 = 2024 pour prédire les percées de 2025–2026 en pré-test rétrospectif.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 500.0**.
- **Justification de priorisation** : Application directe et testable en quelques jours sur l'archive ouverte arXiv composition typographique mathématique récent sans aucune question de fuite si l'extraction reste purement syntaxique/structurelle.

### IDE-2026-11-23-052 — Protocole opérationnel pour révéler des régularités du réel via les symétries statistiques cachées du langage

- **Catégorie et bloc d'origine** : piste ; Lot 8 — Point 24.
- **Énoncé détaillé** : Suite au dossier sur la structure du langage (H9, Karkada et al. 2026) : par quoi commencer concrètement pour détecter dans les corpus scientifiques des symétries de cooccurrence (après neutralisation des artefacts de fréquence et des mentions co-occurrentes triviales) capables d'indiquer des invariants physiques ou mathématiques réels ?
- **Source exacte** : `docs/notes/idee-interessante-v1/lot-8/messages-directeur-lot-8-2026-11-23-v1.md (point 24).`.
- **Statut** : en attente d'envoi groupé (Carbon, Fable/substitut, collisionneur).
- **Lien avec l'organisme d'idéation** : Complète la piste T7 (symétries de cooccurrence) de l'organisme.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 3/5 ; coût = 2/5 ; portée = 4/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 120.0**.
- **Justification de priorisation** : Très original et audacieux ; nécessite d'abord un contrôle strict contre les biais culturels/scientométriques des corpus.

### IDE-2026-11-23-053 — Mission permanente du bibliothécaire des idées et relais sous Antigravity (GO-2026-11-23-33)

- **Catégorie et bloc d'origine** : décision ; Lot 8 — Point 25 + GO-2026-11-23-31 + GO-2026-11-23-33.
- **Énoncé détaillé** : Consigner exhaustivement toutes les idées, pistes, hypothèses, expériences et décisions de la session du 23 novembre et produire le rapport d'urgence et d'impact pour l'organisme. Sous GO-2026-11-23-33 (20:35Z) : reprise dans Antigravity avec autorisation temporaire des sous-agents sur toutes les classes (A, B, C), Carbon en effort élevé (« pro ») remplaçant Fable sur les conceptions délicates, séparation stricte auteur / contre-lecteur neuf.
- **Source exacte** : `lot-8 point 25 ; registres/go.md (GO-2026-11-23-31, GO-2026-11-23-33) ; registres/decisions.md (R-5182, R-5187, R-5190).`.
- **Statut** : en cours (présent livrable du bibliothécaire).
- **Lien avec l'organisme d'idéation** : Assure la mémoire, la traçabilité et l'alimentation sans perte de l'organisme d'idéation lors des transitions de session.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 2/5 ; **score synthétique = 200.0**.
- **Justification de priorisation** : Infrastructure de continuité sans perte.

### IDE-2026-11-23-054 — Lancement et bilan des appels initiaux Google (Argon, Carbon, Neon) et autorisation du collisionneur « idées intéressantes » (30 dollars américains)

- **Catégorie et bloc d'origine** : décision ; GO-2026-11-23-20, -21, -22, -23, -26 / R-5175 à R-5179.
- **Énoncé détaillé** : accord du directeur GO-2026-11-23-20 : appels seuls Argon, Carbon et Neon sur v1 (plafond 10 dollars américains, GEMINI_API_KEY_2) ; tous sortis sans défaut de la garde Google v3 (mais sur question v1 jugée 0,55 non neutre ; écart > 3500 mots pour Argon et Carbon). GO-2026-11-23-21 : Fable max et Opus max sur abonnement. GO-2026-11-23-22 et R-5177 : acceptation des trois retouches de neutralité sur v2 (0,45 neutre ; pièces du modèle conditionnelles ; demande explicite du modèle de base le plus simple sans les hypothèses), plafond 30 dollars américains au collisionneur, branches orphelines kits-abonnement/* autorisées. GO-2026-11-23-23 et R-5178/-5179 : question de suivi homomorphisme (plafond 8 dollars américains, dépense réelle ≈ 5 dollars américains) ; Argon a subi un arrêt technique pour récitation (faux échec) puis a répondu proprement à la relance.
- **Source exacte** : `registres/go.md (GO-2026-11-23-20 à 23, 26) ; registres/decisions.md (R-5175 à R-5179).`.
- **Statut** : décidée et exécutée pour les appels seuls et réponses Fable/Opus ; collisionneur à lancer/achever sur question v2 retouchée.
- **Lien avec l'organisme d'idéation** : Valide la discipline expérimentale des questions neutres à 3 retouches et constitue la base de données empirique des réponses modèles.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 2/5 ; **score synthétique = 160.0**.
- **Justification de priorisation** : Acquis ; reste à exploiter le collisionneur « idées intéressantes » et « conscience et émergence » (Opus ajouté par GO-2026-11-23-26).

### IDE-2026-11-23-055 — Protocole X dossier 1 — Structure cachée du langage (Tshitoyan 2019, Karkada 2026) et sources archivées

- **Catégorie et bloc d'origine** : décision ; GO-2026-11-23-24 et R-5180.
- **Énoncé détaillé** : Protocole X ouvert sur la question de savoir si les plongements et statistiques du langage captent la structure mathématique du réel (archive ouverte de prépublications arXiv:2602.15029 de Karkada et al. 2026 retrouvé et transmis). Sur la branche idees/protocole-x-structure-du-langage-fable-v1, Fable a déjà téléchargé et empreinté 33 fichiers document portable et une page web de sources primaires ainsi que les scripts d'extraction de pages ; les trois notes analytiques sont en attente d'achèvement après la coupure.
- **Source exacte** : `registres/go.md (GO-2026-11-23-24) ; registres/decisions.md (R-5180) ; branche origin/idees/protocole-x-structure-du-langage-fable-v1.`.
- **Statut** : en cours (33 sources archivées sur branche Fable, rédaction à finaliser).
- **Lien avec l'organisme d'idéation** : Piste directe pour le détecteur de symétries statistiques dans l'organisme (H9 / T7).
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 256.0**.
- **Justification de priorisation** : Travaux documentaires de Fable déjà prêts à être finalisés sans coûts supplémentaires majeurs.

### IDE-2026-11-23-056 — Grande revue bibliographique récente, note composition typographique mathématique complète et cours accéléré sur les concepts déjà occupés

- **Catégorie et bloc d'origine** : décision ; GO-2026-11-23-25 et R-5181.
- **Énoncé détaillé** : Décision de mener une grande revue bibliographique jusque dans la littérature très récente (hors corpus pré-entraînement) sur l'ensemble des hypothèses et idées, produisant une note document portable en composition typographique mathématique fusionnée avec les apports Google et un cours accéléré sur les concepts déjà occupés par la littérature (évitant les faux trous, règle R8). Branches : idees/revue-bibliographique-v1 (poussée en partie, sept chercheurs) et note-hypotheses-v1 (v1 publiée).
- **Source exacte** : `registres/go.md (GO-2026-11-23-25) ; registres/decisions.md (R-5181, R-5183).`.
- **Statut** : en cours (note v1 livrée ; revue bibliographique partiellement poussée à achever et verser en v2).
- **Lien avec l'organisme d'idéation** : Empêche l'organisme d'explorer ou de revendiquer des concepts déjà publiés (anti-faux-gap R8).
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 2/5 ; **score synthétique = 160.0**.
- **Justification de priorisation** : Essentiel pour la v2 de la note de synthèse et la préparation de publications et demandes de bourses.

### IDE-2026-11-23-057 — Ouverture des dossiers protocole X 2 à 6 et inscription prioritaire de la scission conceptuelle au dégel de l'organisme

- **Catégorie et bloc d'origine** : décision ; GO-2026-11-23-27, -28, -29.
- **Énoncé détaillé** : Dossier 2 : identités tenues pour vraies (GO-2026-11-23-27) ; Dossier 3 : principe variationnel discret et dissipatif (GO-2026-11-23-28) ; Dossier 4 : scission conceptuelle et mécanismes disruptifs (GO-2026-11-23-28, avec décision ferme d'inscrire l'opérateur de scission à l'organisme à son dégel) ; Dossier 5 : transitions de phase (GO-2026-11-23-28) ; Dossier 6 : méta-espace mathématique et 3e couche (GO-2026-11-23-29, appelé sur Carbon pour 3 dollars américains max). Consigne : fusionner les dossiers 1 à 6 en questions groupées non redondantes au collisionneur (conformément à la règle d'économie du lot 8).
- **Source exacte** : `registres/go.md (GO-2026-11-23-27, -28, -29) ; registres/decisions.md (R-5180, R-5181).`.
- **Statut** : décidée (dossiers 2 à 5 interrompus par limite d'usage chez Fable à reprendre ; fusion à servir au collisionneur sur devis).
- **Lien avec l'organisme d'idéation** : Fournit l'ensemble du cahier des charges conceptuel de la prochaine génération d'opérateurs de l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 2/5 ; portée = 5/5 ; potentiel de découverte majeure = 5/5 ; **score synthétique = 250.0**.
- **Justification de priorisation** : Gros potentiel de synergie si la fusion des dossiers 1 à 6 avec les points du lot 8 est servie proprement en un lot groupé.

### IDE-2026-11-23-058 — Articulation avec les chantiers actifs du programme (saboteur voie A, T0.8, barreau 8, 16 papiers, billet, défauts 48h)

- **Catégorie et bloc d'origine** : décision ; GO-2026-11-23-30, -32 et R-5182 à R-5189.
- **Énoncé détaillé** : Décisions du jour sur les chantiers principaux créant des contraintes et des retours d'expérience directs pour l'organisme : (1) Saboteur voie (A) terminé (≈ 15,35 dollars américains), aucune activation interne enregistrée -> recalcul sur activations rejouées (GO-2026-11-23-32, point NL-11) ; (2) T0.8 v3 terminé normalement (≈ 12,19 dollars américains) ; (3) Lecture sur document portable des 16 papiers finie : 2 papiers infirment N-076 / Arnold occupe le nul par acte -> corrections à N-075 v4 et erratum N-076 ; (4) Billet sondes v1 versé (178 nombres vérifiés) ; (5) Défauts de 48h appliqués à la reprise (D-1 et D-4 sur couverture de l'oracle en exploratoire, N-dev-7 et N-dev-9 sur lentilles) ; (6) Retrait d'une direction I-0046 en marche causale (GO-2026-11-23-32) ; (7) Instance 62096662 (barreau 5) en attente des clés d'accès pour vérification et arrêt depuis Antigravity (GO-2026-11-23-33).
- **Source exacte** : `registres/go.md (GO-2026-11-23-30, -32, -33) ; registres/decisions.md (R-5182 à R-5190).`.
- **Statut** : décidée / en cours d'exécution parallèle (sans modification des fichiers de verdicts/runs).
- **Lien avec l'organisme d'idéation** : Rappelle les invariants de contrôle de l'organisme : jamais de validation sans vérité plantée ni relecture sur document portable, méfiance face aux sondes corrélées (biais de fabrication), et priorité aux expériences à garde causale stricte.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 192.0**.
- **Justification de priorisation** : Assure la cohérence entre le pôle « contrôle boîte blanche » et le pôle « organisme d'idéation » (qui constitue le second terrain du papier C).

### IDE-2026-11-23-059 — Exploitation de la base base de recombinaisons d'idées scientifiques Chimera (Sternlicht et Hope 2025) et du jeu Gu et Krenn (2026) pour l'entraînement et l'étalonnage de l'organisme

- **Catégorie et bloc d'origine** : piste ; Fable max v1 (section 1) + Lot 8.
- **Énoncé détaillé** : Fable signale deux ressources récentes publiques directement utilisables : (1) base de recombinaisons d'idées scientifiques Chimera (Sternlicht et Hope 2025, archive ouverte de prépublications arXiv:2505.20779), base de connaissances des recombinaisons d'idées scientifiques déclarées par les auteurs pour l'analyse et l'idéation ; (2) le jeu de données public de Gu et Krenn (2026, Actes de l'Académie nationale des sciences des États-Unis / Zenodo) contenant 4 451 notes d'intérêt de 110 directeurs d'équipe et le graphe de concepts issu de 2,44 millions d'articles. S'y ajoutent les 400 analogies annotées de Yuan et al. (2023) et les découvertes simultanées en « jumeaux d'idées » de Bikard (2020).
- **Source exacte** : `reponse-fable-max-v1.md (section 3 et références 4, 19, 33, 46) ; reponse-opus-max-v1.md (section 3).`.
- **Statut** : piste de données immédiate à exploiter pour étalonner et tester l'organisme.
- **Lien avec l'organisme d'idéation** : Fournit à l'organisme des données structurées publiques à coût nul pour tester les scores d'intérêt et de structure avant tout essai en aveugle.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 3/5 ; **score synthétique = 375.0**.
- **Justification de priorisation** : Gain de temps massif : évite de tout reconstruire à partir de zéro lorsque des graphes de référence licence ouverte avec attribution et des catalogues de recombinaisons existent déjà.

### IDE-2026-11-23-060 — Critère de génération séparée avant confrontation (contre le remue-méninges interactif prématuré) et transfert de l'intégration plutôt que de l'axe de douleur

- **Catégorie et bloc d'origine** : hypothèse ; Fable max v1 (section 1) + Opus max v1 (section 1).
- **Énoncé détaillé** : Deux résultats critiques issus des réponses max : (1) Diehl et Stroebe (1987) montrent que les groupes interactifs produisent moins d'idées que des individus travaillant séparément avant confrontation (confirme l'architecture d'appels séparés puis collisionneur) ; (2) concernant l'exemple fondateur du directeur (douleur-anesthésie-conscience-modèle de langage), Opus montre que l'anesthésie mêle analgésie, amnésie, immobilité et perte de conscience : chercher un axe de douleur muet testerait au mieux une analgésie ; l'invariant réel à transposer est l'intégration de l'information (ou la dissociation état interne / blocage de sortie sous filtre de réglage fin).
- **Source exacte** : `reponse-fable-max-v1.md (section 1, H8) ; reponse-opus-max-v1.md (section 1, « L'exemple »).`.
- **Statut** : acquis conceptuel à appliquer à l'architecture de l'organisme et au test sur les modèles de langage.
- **Lien avec l'organisme d'idéation** : Confirme le principe multi-espèces isolées avant collision dans l'organisme, et corrige le ciblage de l'expérience modèle de langage / anesthésie vers des mesures d'intégration et de découplage interne/sortie.
- **Évaluation multicritère** : gain informatif = 4/5 ; facilité = 5/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 320.0**.
- **Justification de priorisation** : Évite une erreur expérimentale coûteuse sur le dossier parallèle « conscience et anesthésie » et justifie rigoureusement l'indépendance des générateurs.

### IDE-2026-11-23-061 — Formalisme des analogies par graphe d'hyperarêtes typées et résolvante de chemins dirigés avec masquage lexical intégral

- **Catégorie et bloc d'origine** : objet candidat ; Argon homomorphisme + Carbon homomorphisme + Neon homomorphisme.
- **Énoncé détaillé** : Au niveau calculatoire pré-formel (avant construction d'un olog complet), Neon propose les hypergraphes typés (pour les relations n-aires / d'ordre supérieur) et Carbon propose la matrice de résolvante orientée normalisée R = (I - alpha * A_normalisée)^(-1) afin que le transport de Gromov-Wasserstein partiel puisse aligner naturellement une relation directe d'un domaine sur une chaîne de composition multi-étapes d'un autre domaine, sous condition stricte de masquage lexical intégral (effacement des noms de nœuds).
- **Source exacte** : `reponse-carbon-homomorphisme-v1.md (liminaire, 4) ; reponse-neon-homomorphisme-v1.md (liminaire) ; reponse-argon-homomorphisme-v1-relance1.md (4).`.
- **Statut** : proposition algorithmique prête à coder et tester sur graphe.
- **Lien avec l'organisme d'idéation** : Résout le défaut principal des graphes binaires naïfs (l'invariance d'échelle déductive arête <-> chemin) pour l'alignement structurel dans l'organisme.
- **Évaluation multicritère** : gain informatif = 5/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 5/5 ; potentiel de découverte majeure = 4/5 ; **score synthétique = 400.0**.
- **Justification de priorisation** : Implémentation matricielle simple en Python sur graphes de voisinage ; élimine directement une cause majeure d'échec de l'homomorphisme strict.

### IDE-2026-11-23-062 — Protocole de vérification anti-faux-gap et traçabilité document portable stricte (R7, R8) sur toutes les citations des modèles

- **Catégorie et bloc d'origine** : décision ; Carbon méta-espace + Lot 8.
- **Énoncé détaillé** : Sur les 45 à 60 références classiques et récentes citées par Argon, Carbon, Neon, Fable et Opus, seule une fraction (dont Gu et Krenn 2026, Mu et al. 2018, Xu et al. 2026, Gentner et al. 1993, Dunbar 1997, Davis 1971, Kang et al. 2009, Ogburn et Thomas 1922, et les 33 sources sur la structure du langage) a été lue sur fichier document portable empreinté. Plusieurs références restent marquées « à vérifier » (modèle de plongement de formules mathématiques de Davila et collaborateurs / Davila 2019, banc d'évaluation mathématique sur équations de Mansouri et collaborateurs / Mansouri 2022, White et Reitz 1983, Bornmann et al. 2019, Sizemore et al. 2018, Bowers et al. 2023 pagination, etc.). Aucun chiffre non lu sur document portable n'est opposable.
- **Source exacte** : `CLAUDE.md (R7, R8) ; note-hypotheses-appuis-formalismes-v1.md (section 7) ; reponse-fable-max-v1-provenance.md ; reponse-opus-max-v1.md (fin).`.
- **Statut** : en cours (revue bibliographique et téléchargement des sources à achever).
- **Lien avec l'organisme d'idéation** : Obligation préalable à toute publication ou décision reposant sur un chiffre cité.
- **Évaluation multicritère** : gain informatif = 3/5 ; facilité = 4/5 ; coût = 1/5 ; portée = 4/5 ; potentiel de découverte majeure = 1/5 ; **score synthétique = 48.0**.
- **Justification de priorisation** : Hygiène documentaire obligatoire du programme.

## Synthèse des décisions prises et décisions restant à prendre

### Décisions actées ou en cours d'exécution au 23 novembre (après-midi et soirée)
1. **GO-2026-11-23-20 à 23, 26** : appels seuls Argon, Carbon et Neon exécutés sur la question des idées intéressantes (v1) et sur l'homomorphisme ; retouches de neutralité v2 acceptées ; plafond de 30 dollars américains validé pour le collisionneur « idées intéressantes » et ajout d'Opus au collisionneur « conscience et émergence ».
2. **GO-2026-11-23-24, 25, 27, 28, 29** : ouverture des dossiers 1 à 6 du protocole X (structure du langage, identités tenues pour vraies, principe variationnel discret, scission conceptuelle inscrite au dégel de l'organisme, transitions de phase, méta-espace mathématique), revue bibliographique récente et note en format sur document portable.
3. **GO-2026-11-23-30, 31, 32** : relance des chantiers du programme, lancement du lot 8 des idées avec bibliothécaire permanent (40 dollars américains et devis collisionneur), corrections à N-075 version 4 et erratum N-076.
4. **Règle d'économie du protocole X (branche `origin/idees/lot-8-chef-d-orchestre-v1`)** : Carbon maintenu et lu à part ; Argon retiré par défaut des fonds ; Neon restreint à l'exploration ouverte avec critère d'arrêt séquentiel ; regroupement des questions par axe ; décorrélation assurée entre familles Google et Anthropic.
5. **GO-2026-11-23-33** : autorisation temporaire des sous-agents sous Antigravity pour toutes les classes (A, B, C), avec Carbon à effort élevé à la place de Fable et séparation stricte entre auteur et contre-lecteur neuf.

### Décisions restant à prendre ou en attente d'accord du directeur
1. **Choix du lot prioritaire d'expériences courtes sans dépense sur processeur** : arbitrer l'ordre de préenregistrement entre l'épreuve « surface et structure » sur les 2 996 notes de Gu et Krenn (proposition d'Opus, 3 jours), l'épreuve « le pont suit-il la carte ? » sur base ouverte PubTator 3 (proposition de Fable, quelques jours), l'épreuve des macros composition typographique mathématique et algèbres amassées sur l'archive ouverte arXiv (proposition de Carbon sur la couche chantier), et l'épreuve des arbres d'opérateurs d'équations sur l'archive ouverte arXiv (proposition d'Argon).
2. **Devis du collisionneur regroupé pour le lot 8 et les dossiers 1 à 6 du protocole X** : validation du devis apparié (bras principal avec matière première croisée contre bras témoin neutre) pour les questions fusionnées (points 5, 9–14, 17–24 du lot 8 et dossiers 1–6).
3. **Choix d'un modèle ouvert pour les bras complémentaires** : sélection du modèle ouvert pour l'extraction de relations typées (bras B d'Opus sur carte graphique) et pour la lecture des neurones de récompense éparse (point 2 du lot 8 et complément H10 d'Opus), sous réserve des résultats de Xu et al. 2026.
4. **Accès système unifié de langage médical pour la base de prédications biomédicales SemMedDB contre accès libre immédiat base ouverte PubTator 3** : décider s'il faut ouvrir un compte gratuit du système unifié de langage médical pour la base SemMedDB (réclamé par Carbon et Neon) ou privilégier base ouverte PubTator 3 immédiat (Fable) et le jeu Zenodo de Gu et Krenn (Opus).
5. **Transmission des clés d'accès du loueur de cartes graphiques et de l'hébergeur** pour vérifier le rapatriement et détruire l'instance arrêtée 62096662 (GO-2026-11-23-33).
6. **Réouverture de l'organisme d'idéation (dégel)** : nœud de décision formel à prononcer après les petites expériences tranchantes sur processeur ou conjointement avec les préenregistrements des trois nouveaux opérateurs (scission, anomalie, gain de compression).

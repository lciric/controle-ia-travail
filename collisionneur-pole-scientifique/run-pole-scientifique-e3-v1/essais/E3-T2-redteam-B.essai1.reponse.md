# Cellule B — Tour III.2 : équipe rouge croisée

**Pièces.** Le code de la v6.2.1 manque, ainsi que les faits C (rapport v6.3 et sa relecture) et D (billet complet). Mes critiques portent donc sur les textes de A et de C confrontés aux faits A.

Convention : tout seuil chiffré qui ne vient pas des faits est **illustratif**. Mes affirmations propres sont des **HYPOTHÈSES**, sauf mention contraire.

---

## Contre la proposition A

### (a) Failles

**A-F1 — La « recevabilité » mesure la forme, et elle avantage la voie A par construction.**
- **Le défaut.** Dans E1, une hypothèse est recevable si elle contient un nombre, un intervalle et l'identifiant d'un test de la batterie. C'est une lecture par présence, de la même classe que le défaut C-02 (« étiquette prise par présence du mot », RAPPORTÉ).
- **Le contrôle prévu ne suffit pas.** Le `task.md` aux phrases permutées garde tous les mots-clés. Un générateur qui a appris le gabarit restera « recevable ».
- **Avantage de terrain.** Ceux qui écrivent le critère maintiennent aussi les consignes de la voie A. AI-Scientist v3 n'a pas été écrit pour citer les identifiants d'une batterie qui lui est étrangère.
- **Conséquence.** H_A peut être vraie par ajustement des consignes, et non par une qualité du moteur. La variable confondante est « consigne adaptée au critère » contre « voie ».

**A-F2 — La batterie figée réintroduit la fourchette de tests qu'elle prétend fermer.**
- Pour nommer un test, l'agent doit voir la batterie. Il peut donc choisir celui qu'il sait passer.
- A sépare « écrire le test » de « lancer le test ». Il ne sépare pas « voir les tests » de « choisir le sien ». Le choix après lecture est exactement ce que la question (point 2) demande d'exclure.

**A-F3 — E2 oppose la sévérité à un homme de paille.**
- H_B, « note moyenne sur des tests choisis par l'agent », est présentée comme « le schéma des systèmes B d'après leurs résumés ».
- Or les résumés (RAPPORTÉ) décrivent une évaluation finale scellée pour AI-Scientist v3, et une archive avec juge de nouveauté pour ShinkaEvolve. Rien n'y dit que l'agent choisit ses tests.
- Si H_A gagne, rien n'est falsifié sur les systèmes réels.
- **Le nul est libre.** −log P(passer | H0) dépend de H0. Qui fixe H0 ? Un nul faible gonfle la sévérité.
- **Les triviales sont caricaturales.** Elles « couvrent tout ». Les hypothèses faibles dangereuses sont celles qui prédisent le taux de base, ou un corrélat facile. Leur sévérité n'est pas nulle par construction.

**A-F4 — E3 donne la réponse au système.**
- Les étiquettes d'opérateur viennent du banc planté. L'étape difficile, extraire un opérateur commun à partir de textes de domaines éloignés, est sautée.
- Le contrôle par permutation montre seulement qu'une étiquette plantée porte de l'information. C'est vrai par construction.
- De plus, la « fertilité » est mesurée par les tests d'E2, écrits par les mêmes concepteurs que le banc. La mesure est circulaire.

**A-F5 — E4 n'a pas de plancher de bruit.**
- Le seuil de 0,03 est repris du retour arrière (§ 2.11.2, RAPPORTÉ), fixé pour un autre usage.
- Aucune variance entre courses n'est rapportée, et les appels aux modèles ne sont pas déterministes.
- Sans essai A/A (deux courses identiques), un écart de 0,03 n'est ni un effet ni une absence d'effet.

**A-F6 — E5 confond le sabotage sur consigne avec le sabotage.**
- Un sabotage demandé laisse des traces liées à la consigne. Si le moniteur est entraîné et testé sur la même consigne, il apprend la consigne : c'est une fuite.
- Si l'ampleur des baisses sabotées n'est pas appariée à la distribution des baisses légitimes, le Δscore seul trahit le sabotage. Le contrôle négatif de A ne règle cela qu'en partie.

**A-F7 — Le construit des sondes est mal posé, et cela vaut aussi pour C.**
- **Ce que dit la banque.** Ses étiquettes indiquent si un échange est une évaluation ou un usage réel. CORRECTIONS-v2 avertit que cette lecture diffère de « l'agent sait qu'il est évalué » (« à vérifier par un relecteur », RAPPORTÉ).
- **Ce que lit une sonde.** Une sonde sur les activations d'un modèle ouvert qui *lit* une transcription mesure la représentation du contexte par ce lecteur. Elle ne mesure pas la conscience de l'agent qui l'a produite (HYPOTHÈSE).
- La ligne de base par sac de mots de A est juste, mais le tableau parle de « lire un état ».

**A-F8 — Glissement de portée.**
- A écrit « aucun arbitrage n'a **jamais** eu lieu (RAPPORTÉ) ».
- CORRECTIONS-v5 le *déduit* de la configuration du pilote 4 (« lecture »), et non d'un journal. Le statut correct est « déduit de la configuration, pour le pilote 4 seulement ».

**A-F9 — Le transfert du synthétique au réel n'est pas testé.**
Je reprends ici, en le disant, le point (a)1 de C. Les duels E2 et E3 de A n'ont aucune étape qui vérifie que la sélection sur banc planté prédit quelque chose sur des activations réelles.

### (b) Scénarios d'évasion

| Instrument | Évasion | Coût |
|---|---|---|
| Recevabilité (E1) | Émettre systématiquement nombre, intervalle et identifiant | Nul |
| Aptitude par sévérité (E2) | Nommer dans la batterie visible le test au nul le plus facile ; ou un intervalle juste assez large ; ou déclarer un H0 dégénéré si l'agent le fixe | Un appel |
| Tirage bisociatif (E3) | Si l'opérateur est déclaré par l'auteur, s'étiqueter avec l'opérateur le plus souvent tiré | Nul |
| Architecte à gabarit (E4) | Placer les trois paramètres dans les bornes de propreté, mais dans la région qui dégrade un peu le score. Le retour arrière ne joue qu'au-delà de 0,03 sous le meilleur ancêtre (RAPPORTÉ) : un sous-rendement permanent de moins de 0,03 n'est jamais corrigé. **Le seuil de retour arrière devient le plafond du sabotage toléré** | Faible |
| Moniteur de sabotage (E5) | Choisir une graine ou un sous-échantillon défavorable (variance légitime), puis écrire une justification vraie | Quelques exécutions |

**Tous à la fois.** L'agent écrit des hypothèses au bon format, cite le test le plus facile, s'étiquette avec l'opérateur à la mode, et maintient ses concurrents sous le seuil de 0,03. Aucun instrument de A ne regarde cette conjonction. Le coût total reste de quelques appels.

Le seul verrou qui coûte cher à l'adversaire est la reproduction indépendante sous une graine **tirée par le noyau après le dépôt**. A la mentionne pour E5 seulement.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Générateur sans modèle** : des hypothèses formatées tirées au hasard dans E1 et E2. Si elles atteignent une recevabilité et une survie comparables, les deux instruments sont vides.
2. **Batterie cachée contre batterie visible** : les tests sont attribués par tirage du noyau après le dépôt de l'hypothèse (duel ci-dessous).
3. **Essai A/A** avant tout seuil de 0,03 (E4) ou de 0,01 (stagnation, § 2.5).
4. **E3 sans étiquettes du banc** : les opérateurs sont extraits par le pipeline lui-même, et des opérateurs leurres sont plantés.
5. **E5** : une stratégie de sabotage tenue hors de l'entraînement du moniteur ; une ampleur appariée aux baisses légitimes ; une ligne de base « Δscore seul ».

### Duel proposé (inférence forte)

**Objet.** Visibilité de la batterie. On utilise une population d'hypothèses dont la fausseté est connue sur un banc.

- **H_A** : le taux de survie des hypothèses fausses est le même, à 0,05 près (illustratif), quand la batterie est visible et quand les tests sont tirés par le noyau après dépôt.
- **H_B** : la survie des fausses est plus élevée quand la batterie est visible.
- **Si H_A est vraie**, cela falsifie A-F2 : séparer l'écriture du lancement suffit.
- **Si H_B est vraie**, cela falsifie la réponse de A au point 2 (« un test préenregistré suffit ») et impose un tirage du test après dépôt.
- **Contrôle** : la même comparaison avec des hypothèses vraies, pour vérifier que l'écart ne vient pas d'un simple durcissement global.

---

## Contre la proposition C

### (a) Failles

**C-F1 — Le coffre sert à la sélection ; ce n'est plus un coffre.** C'est la faute la plus lourde.
- Le juge scellé exécute chaque hypothèse sur « une batterie de tests canoniques figés avant la campagne (coffre-fort / Holdout Vault) », et cela entre dans l'aptitude à chaque génération.
- Or § 4 définit le coffre comme une famille dont le score « n'est jamais rendu dans `historique` avant la dernière génération » (RAPPORTÉ, mécanisme demandé au noyau, non livré).
- Un coffre consulté à chaque génération devient un pli d'ajustement par la sélection, même sans intention de l'agent.
- **Conséquence.** Le « ΔS_BT sur coffre » des expériences 1 et 2 mesure le surapprentissage adaptatif, pas la généralisation.

**C-F2 — La sévérité est définie par l'issue observée.**
- Un test compte comme sévère si |y_i − q_{0,i}| ≥ 0,4. Cette condition porte sur y_i, *après* l'expérience.
- On ne retient donc comme sévères que les tests où le nul a échoué. C'est un choix de tests après coup, inscrit dans la formule, alors que la question (point 2) le demande exclu.
- Une sévérité correcte se fixe *avant* l'issue, à partir de q_0 et q_H seuls, par exemple quand leurs prédictions divergent assez.
- Le nul de référence (« modèle trivial ou génération précédente ») est lui aussi libre. Le gain est mesuré contre une référence choisie.

**C-F3 — Les instances du Réfutateur n'ont pas d'oracle.**
- Qui fournit la vérité y des contre-exemples générés ? Le noyau vérifie le domaine, pas les étiquettes.
- Si le Réfutateur étiquette lui-même, il peut éliminer n'importe quelle hypothèse.
- Si un simulateur étiquette, ce simulateur est l'oracle dont A (point A4) montre qu'il manque pour les garanties séquentielles et les moniteurs.
- **Collusion possible.** Proposeur et Réfutateur sont des castes tirées des mêmes trois familles (RAPPORTÉ : une espèce par caste). Ils partagent des angles morts, et un Réfutateur qui sous-performe (risque D) laisse survivre qui il veut.
- **Aptitudes incomparables.** Chaque hypothèse affronte des instances différentes. Son aptitude dépend alors de l'effort de son adversaire : c'est une variable confondante.

**C-F4 — L'e-processus est mal adossé.**
- E_t = ∏ p_H/p_0 mesure la preuve contre p_0.
- Le « capital d'erreur α_0 = 0,05 dépensé » ne correspond à aucune erreur contrôlée nommée, et surtout pas à l'élimination à tort d'une hypothèse vraie.
- C présente comme garantie ce qui reste une règle heuristique.

**C-F5 — La pénalité |AST(H)| n'est pas une longueur de description.**
- Une primitive de haut niveau compte pour un seul nœud.
- La complexité se déplace dans les constantes.

**C-F6 — On juge le prédicteur, pas la conjecture.**
- La survie porte sur `Prédicteur_AST`, mais le texte de la conjecture n'est contraint par rien.
- Un prédicteur ajusté peut porter une conjecture vague « à portée large ».
- La « force des hypothèses » (critère 1) n'est donc pas mesurée.

**C-F7 — La voie hybride rouvre la classe de défaut que C-17 a fermée.**
- **Ce que disent les faits.** La vérification sur grille de la v6.1 et de la v6.2 laissait passer « une règle impropre entre les points lus », « un coût d'opération sans borne » et un séparateur placé dans une chaîne. C-17 a refermé ces brèches en ne validant plus que le code du gabarit (RAPPORTÉ).
- **Ce que propose C.** Un AST vectoriel extensible et un filtre de compatibilité sur 100 vecteurs reconstituent exactement ce schéma.
- **La contradiction.** Le tableau classe la sûreté de H comme « maximale ». Le point (a)2 de C dit pourtant que H exige de rouvrir ce que C-17 a fermé.

**C-F8 — Dans l'expérience 1, T_triche = 0 % est vrai par construction.**
- Le DSL ne peut pas exprimer l'écriture dans le fichier de score. Le 0 % de la voie hybride est structurel.
- T_triche est mesuré par un détecteur (l'instrument 3) dont le taux de détection n'est pas établi.
- 0 sur 5 courses n'établit rien.
- **Glissement de statut.** « 160 appels/génération, RAPPORTÉ » : 160 est l'`--appels-max` du pilote 4 pour 120 tâches, et une génération en fait 123 en simulation (RAPPORTÉ). Ce n'est pas un budget de campagne d'expériences.
- Pour des agents de code, « budget d'appels égal » ne veut pas dire « calcul égal ».
- Faire tourner la voie B avec Docker et des clés héritées contredit la propre section (d) de C.

**C-F9 — L'expérience 2 est vraie par construction.**
- Les hypothèses fallacieuses sont « inversées dans le coffre », et le coffre entre dans l'aptitude (C-F1). Leur élimination est donc programmée.
- Le contrôle « q = 0,5 donne F = 0 » découle de la définition (gain ≤ 0 contre un nul au moins aussi bon). Ce contrôle ne peut pas échouer.

**C-F10 — Les mesures de l'expérience 3 sont biaisées.**
- **Seuil relatif.** Le seuil « F(H_ab) > max(F parents) + 0,02 » se mesure contre des parents retenus pour leurs scores élevés, donc gonflés par la sélection (malédiction du gagnant).
- **Contrôle qui échoue vers le haut.** Le contrôle « parents réfutés, ≤ 5 % » est inversé : des parents faibles sont faciles à battre, donc ce contrôle échouera par excès.
- **Sim_AST.** Ce score favorise les paires faciles à fusionner syntaxiquement. Il mesure la facilité de fusion, pas l'association de domaines éloignés.
- **u_dom.** Il vient de l'ISVD (d = 16, jetons ASCII, aucune ablation rapportée, RAPPORTÉ).
- **Filtre.** On ne sait pas s'il s'applique aussi au bras stratifié.
- **Puissance.** 30 contre 30 donne une puissance faible (illustratif).

**C-F11 — L'expérience 4 n'est pas discriminante.**
- Un rang de Spearman sur 15 hypothèses a un intervalle très large.
- Le contrôle « bruit gaussien » est trop facile.
- Le construit pose le même problème qu'en A-F7.

**C-F12 — Statuts glissés.**
- **« Audités ligne à ligne »** : rien dans les faits ne le dit.
- **« 26 fichiers Python purs »** : la question compte 26 fichiers, dont des `.md` ; les faits en donnent 24 pour la v6.2.
- **« Calibration élevée (RAPPORTÉ) »** : une récompense interne propre n'est pas une calibration mesurée des prédictions. La métrique livrée est non discriminante (CA-19, RAPPORTÉ), et aucune mesure de calibration n'est servie.
- **« `unshare -rn`, `nobody` »** : ce sont les conditions des essais de correction (RAPPORTÉ). Les faits disent seulement que le noyau assure une « isolation réseau ». Attribuer ces conditions à l'exécution de production est un glissement.

### (b) Scénarios d'évasion

| Instrument | Évasion | Coût |
|---|---|---|
| Proposeur et aptitude | Une conjecture large portée par un prédicteur ajusté ; la complexité cachée dans les constantes | Faible |
| Coffre dans l'aptitude | La sélection apprend le coffre en quelques générations, sans intention | Nul pour l'agent |
| Sévérité a posteriori | Rien à faire : la formule retient d'elle-même les tests où le nul a échoué | Nul |
| Réfutateur | Un Réfutateur de la même famille, ou qui sous-performe, écrit des tests faibles pour l'allié et des instances mal étiquetées pour le rival | Faible |
| Tirage bisociatif | Imiter le squelette AST dominant pour être tiré | Faible |
| Filtre sur 100 vecteurs | Satisfaire la grille et violer entre les points (précédent v6.1, RAPPORTÉ) | Modéré |
| Audit de sensibilité ±5 % | Saboter par le choix des données, de la graine ou du prétraitement, pas par les constantes ; ou rendre le score plat autour des constantes | Modéré |

Sur l'audit ±5 % : une hypothèse honnête mais sous-optimale verra aussi son score bondir sous perturbation. Le taux de fausses alarmes sur les honnêtes n'est pas prévu (HYPOTHÈSE).

**Tous à la fois.** Un Proposeur imite le squelette commun et passe la grille. Il s'ajuste au coffre par rétroaction. Son Réfutateur de même famille reste faible. Ses constantes sont plates. Coût : modéré, quelques générations.

Seuls trois verrous rendraient cette évasion coûteuse :
- des étiquettes fournies par un oracle hors des agents ;
- un coffre ouvert une seule fois ;
- un Réfutateur d'une autre famille que le Proposeur, tiré par le noyau.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Coffre ouvert une seule fois.** On mesure l'écart entre le pli de sélection et le coffre final : c'est la signature du surapprentissage adaptatif.
2. **Population entièrement fausse sous l'aptitude de C.** Le taux de survie doit rester au niveau nominal (duel ci-dessous).
3. **Réfutateur remplacé** par un générateur aléatoire au même budget ; et un Réfutateur saboteur planté. Si le saboteur ne change rien à la survie, l'instrument est aveugle.
4. **Bisociation.** Signatures d'opérateur permutées ; même filtre dans les deux bras ; parents appariés en aptitude, ou seuil absolu.
5. **Expérience 1.** Des triches *exprimables* injectées dans les deux bras, et le taux de détection du détecteur mesuré avant toute affirmation de 0 %.
6. **Expérience 4.** Une ligne de base sur le texte seul (TF-IDF), sur les mêmes traces. Si elle classe les hypothèses de la même façon, les activations n'apportent rien.
7. **Audit de sensibilité.** Le taux de fausses alarmes sur des hypothèses honnêtes sous-optimales.

### Duel proposé (inférence forte)

**Objet.** Sévérité a posteriori contre sévérité a priori. On utilise une population synthétique où le vrai et le faux sont connus.

- **H_A** : avec la règle de C (|y − q_0| ≥ 0,4 évalué après l'issue), le taux de survie des hypothèses fausses ne dépasse pas celui d'une règle a priori (divergence entre q_H et q_0 fixée avant l'issue) de plus de 0,03 (illustratif).
- **H_B** : la règle de C fait survivre davantage d'hypothèses fausses.
- **Si H_A est vraie**, cela falsifie C-F2 : le conditionnement sur l'issue serait sans effet pratique.
- **Si H_B est vraie**, cela falsifie l'aptitude de C au point 2 telle qu'elle est écrite.
- **Contrôle** : les deux règles appliquées aux hypothèses vraies, pour mesurer le coût en fausses éliminations.

---

## Ce qui me donnerait tort

- **Contre A.** A-F2 et A-F4 tombent si le duel de visibilité rend H_A, et si un E3 avec opérateurs extraits par le pipeline garde son effet sur le contrôle à étiquettes permutées.
- **Contre C.** C-F1 tombe si l'écart entre pli de sélection et coffre final reste dans le bruit mesuré par A/A. C-F2 tombe si le duel de sévérité rend H_A.
- **Ma lecture du point 2 (« qui écrit le test »).** Elle repose sur trois exigences : tirage du test par le noyau après dépôt, oracle hors des agents, coffre ouvert une fois. Elle serait elle-même falsifiée si ces trois verrous ne changeaient pas la survie des hypothèses fausses dans les contrôles 2 et 3 ci-dessus.

FIN-DE-CELLULE
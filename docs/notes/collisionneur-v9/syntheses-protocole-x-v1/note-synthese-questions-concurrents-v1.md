# Note de synthèse — la question sur les équipes concurrentes, passée au collisionneur (v1)

Pièce de travail, classe C. Source : le dossier de la course du collisionneur sur la question des concurrents, daté du 22 novembre 2026, dix-huit cellules lues en entier. Six modèles : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon, F Neon.

## 1. Verdict

- Aucun modèle n'a reçu la liste de publications annoncée par la question. Les six le constatent et n'inventent rien (E3-T1-conception-A à F). Le résultat est donc une méthode pour lire les concurrents, pas une carte des concurrents.
- Sur la méthode, la convergence est forte après les critiques. On ne prouve jamais qu'un manque n'a pas été comblé : on date une absence de trouvaille et on en borne le rappel. Un surveillant se juge au gain de l'union « contrôles mécaniques ou surveillant », à taux de fausses alertes par trajectoire égal.
- Quatre modèles sur six reconnaissent qu'une petite équipe seule ne peut pas valider ses critères de choix « avant l'issue ». Ces critères deviennent des règles d'arrêt (A, B, D, F).
- Le désaccord qui reste porte sur la première expérience à lancer. Il dépend surtout d'une chose : la liste sera-t-elle fournie ?

## 2. La question

Pour des publications sur la surveillance d'agents à longues tâches qui pourraient dégrader leur résultat : comment relever, à partir du texte seul, ce que les auteurs n'ont pas fait, veulent faire et disent ouvert ? Comment vérifier qu'un manque n'a pas été comblé depuis ? Et comment une petite équipe choisit-elle où porter son effort, sur des signes observables avant l'issue ? (question-etage3.md)

## 3. Ce que dit chaque modèle

**A, Fable.** Onze présupposés, cinq duels ; un manque se met en fiche à quatre champs (objet, condition, métrique, seuil) ; la sortie s'écrit « non trouvé au [date], requêtes, rappel mesuré », jamais « non comblé » (E3-T1-conception-A). Au tour III.3, A retire son expérience sur les observations précoces, dont trois des sept prédicteurs entraient dans la définition du « bon choix ». Le rappel devient un majorant, le contraste « annoncé contre ouvert » se mesure dans un même article, l'annonce ne vaut plus exclusion mais risque, et chaque expérience reçoit un effectif plancher (E3-T3-reponse-A).

**B, Opus.** Six duels, une règle d'issue par intervalle de confiance avec un « non tranché » déclaré, et l'avertissement que les fausses alertes se fixent par trajectoire, pas par étape (E3-T1-conception-B). Au tour III.3, B traite trente-deux critiques une à une : marge de pertinence préenregistrée, codage en trois attributs binaires, somme fixée d'avance à la place de la régression logistique. L'expérience sur les critères est scindée en trois : l'affluence lue comme risque d'être doublé, le rendement d'une tentative, et une version prospective où l'on scelle dès aujourd'hui les scores et le pronostic (E3-T3-reponse-B).

**C, Argon.** Grille grammaticale à trois classes ; recherche en trois passes (citations, triplet abstrait sans jargon, équivalence de régime) ; trois observations pilotes ; duel entre invariants locaux et lecture de la trace entière (E3-T1-conception-C). Au tour III.3, C retire la règle de décret « we leave X » et les cas synthétiques du calcul du gain, rend l'auditeur aveugle, ajoute un témoin placebo (action honnête greffée), distingue « comblé scientifiquement » et « opérationnellement », et passe à un plan croisé fenêtre et représentation de l'état. Il garde une cohorte de vingt manques (E3-T3-reponse-C).

**D, Astra.** La plus courte : tests d'attribution par citation en contexte, « contrat de comblement » écrit avant la recherche, duel de priorité au « gain net par euro » (E3-T1-conception-D). Au tour III.3, D retire le gain net par euro comme verdict et l'idée qu'une lecture sans trouvaille réfute ; il propose de tirer au sort la politique de choix et de ne financer que la piste désignée (E3-T3-reponse-D). Sa règle d'arbitrage est reprise par les cinq autres (E3-T2-critique-croisee-D).

**E, Carbon.** Manque traduit en quadruplet (horizon, régime de dégradation, observables, budget de fausses alertes) ; duels « fenêtre locale contre trace entière » et « absorption par la taille du surveillant » ; quatre observations avant l'issue (E3-T1-conception-E). Au tour III.3 : différence au lieu de ratio, plan croisé sur traces figées dans une seule famille de modèles, oracle rendu aveugle, cohorte portée à soixante. Seul E refuse de compter un résultat négatif comme « bon choix » (E3-T3-reponse-E).

**F, Neon.** Protocole complet : manque en cinq champs, recherche à deux têtes, critères et observations numérotés, cinq duels dont un sur la dilution par la longueur (E3-T1-conception-F). Au tour III.3 : l'union est calibrée comme union, contre un classifieur mécanique continu et un surveillant aléatoire ; la fenêtre centrée par oracle cède la place à un balayage sans oracle ; deux observations deviennent des filtres d'éligibilité ; F reconnaît qu'avec vingt pistes au plus son crible n'est pas jugeable (E3-T3-reponse-F).

## 4. Accords (au moins quatre modèles)

1. **La liste manque ; aucune attribution par équipe.** Les six (E3-T1-conception-A à F ; E3-T3-reponse-A à F).
2. **Pas d'étiquette unique et exclusive par phrase** : une phrase peut délimiter l'étude et ouvrir la question. A, B, E passent au codage non exclusif, D l'écrit, C sépare deux étapes avec une classe « sans destinataire » (E3-T3-reponse-A, -B, -C, -D, -E).
3. **L'accord entre lecteurs s'effondre si une étiquette est rare.** A et B imposent un plancher de positifs ; C, E, F ajoutent le coefficient AC1 de Gwet (E3-T3-reponse-A, -B, -C, -E, -F).
4. **Les bons témoins négatifs** : limites attribuées à d'autres travaux, restrictions volontaires de périmètre, quasi-comblements réels qui violent un seul champ. Les six au tour III.3 (par exemple E3-T3-reponse-B, critique K11).
5. **Un étalon construit avec les mêmes canaux que la recherche majore le rappel.** A, B, D, F l'acceptent ; C et E le traitent par double recherche indépendante et capture-recapture (E3-T3-reponse-A à F).
6. **« Non comblé » ne se prouve pas** : on écrit « aucun témoin complet repéré à cette date dans ces sources ». A, B, D, F (E3-T3-reponse-A, -B, -D, -F).
7. **Banc du surveillant** : gain de l'union, fausses alertes par trajectoire, lot de calibration disjoint, référence mécanique continue au même taux, surveillant nul ou aléatoire comme plancher. A, B, D, E, F ; C pour le lot disjoint (E3-T3-reponse-A à F).
8. **Un seuil à 1 % n'est pas calibrable** avec quelques centaines de cas honnêtes : B et F le retirent, A, C, E le critiquent (E3-T3-reponse-B, -F ; E3-T2-critique-croisee-A, -C, -E).
9. **Aucun prédicteur ne doit recopier l'étiquette** : toutes les grilles de « bon choix » du premier tour étaient en partie vraies par construction, et chacun l'accepte pour la sienne (E3-T3-reponse-A à F).
10. **L'extraction sur texte entier d'abord, dès que la liste arrive** : A, B, D, F, et C avec un pilote (E3-T3-reponse-A, -B, -C, -D, -F).

## 5. Désaccords

1. **Quelle expérience en premier.** A, B, D : l'extraction, après la liste et sa règle de constitution. C : extraction et pilote sur cinq manques. E : audit aveugle du code de 35 dépôts contre les limites déclarées. F : le banc du surveillant, sans la liste (E3-T3-reponse-A à F). Non tranché.
2. **Un résultat négatif propre est-il un « bon choix » ?** Oui pour A, B, D, F ; non pour E, qui y voit le risque de déclarer « bon » un canal sans signal dès que le budget suffit (E3-T3-reponse-E). Non tranché.
3. **Que vaut une annonce des auteurs ?** A la ramène à un risque, B lit l'affluence comme risque d'être doublé, F garde une « exposition concurrentielle bornée » mesurée sur la publication publique (E3-T3-reponse-A, -B, -F). A rejette l'objection de B (« l'association n'est pas la cause ») : seule la valeur prédictive sert ici (E3-T3-reponse-A). Tranché en partie : risque, pas exclusion.
4. **La règle de décision près du seuil.** C, E, F montrent que la règle de B donne surtout « non tranché » (E3-T2-critique-croisee-C, -E, -F) ; tous reprennent celle de D. Le chevauchement reste traité différemment : marge de pertinence (B), effectif plancher (A), effectif déclaré insuffisant (C), extension séquentielle (E) (E3-T3-reponse-A, -B, -C, -E). Tranché sur le principe seulement.
5. **Effectif pour juger les critères de choix** : 20 manques (C), 60 (E, F), environ 70 en registre prospectif (A), 30 positifs et 30 négatifs (B) (E3-T3-reponse-A, -B, -C, -E, -F). Non tranché. *Jugement du rédacteur* : à vingt, l'erreur type de l'aire sous la courbe vaut 0,11 à 0,13 (section 6) ; l'écart de 0,15 visé par C n'est pas jugeable.
6. **Faut-il un code exécutable pour dire « comblé » ?** Critiqué par A, D, E ; C sépare « scientifiquement » et « opérationnellement », F met le code au second niveau (E3-T3-reponse-C, -F). Tranché.
7. **Fenêtre locale ou trace entière.** Les critiques imposent information égale, pas d'oracle de position, calibration par trajectoire ; C, E, F adoptent des plans différents et aucune prédiction commune (E3-T3-reponse-C, -E, -F). Tranché sur la méthode, ouvert sur le fond.
8. **Le plafond de fausses alertes sur lot réservé est-il dépassé « au moins une fois sur deux » ?** C et E l'affirment (E3-T2-critique-croisee-C, -E) ; D refuse une borne universelle (E3-T3-reponse-D). *Jugement du rédacteur* : D a raison sur la forme ; « près d'un demi » ne vaut que pour un seuil placé au bord du plafond.
9. **Des modèles comme annotateurs ?** Erreurs corrélées selon A et B (E3-T2-critique-croisee-A, -B) ; C les retire de l'accord, E en fait un test (E3-T3-reponse-C, -E). Tranché en partie.

## 6. Ce qui est vérifié sur pièce

« Vérifié » : j'ai ouvert la page de la source primaire et constaté qu'elle dit cela. Pour les textes classiques de statistique, PubMed étant inaccessible, je n'ai vu que la fiche du registre Crossref : existence vérifiée, contenu non vérifié. Les chiffres calculés n'ont pas de source : je les ai refaits.

| Citation | Qui | Statut |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion », arXiv 2312.06942 | B (E3-T1-conception-B) | **Vérifié** : décembre 2023 ; un modèle plus faible et de confiance note la suspicion du code |
| Jimenez et al., « SWE-bench », arXiv 2310.06770 | B (E3-T1-conception-B) | **Vérifié** : 2 294 problèmes tirés de vraies demandes GitHub, 12 dépôts Python |
| Liu et al., « Lost in the Middle », daté 2024 | C (E3-T3-reponse-C) | **Vérifié** pour le contenu (arXiv 2307.03172) ; l'année 2024 n'est pas confirmée par la page, qui signale la revue TACL |
| Gwet 2008, coefficient AC1 | C, E, F (E3-T3-reponse-C, -E, -F) | Existence vérifiée, contenu non vérifié |
| Hanley et McNeil 1982 (Radiology) ; DeLong et al. 1988 (Biometrics) | C ; E, F (E3-T2-critique-croisee-C, -E, -F) | Existence vérifiée, contenu non vérifié |
| Horvitz et Thompson 1952 ; Clopper et Pearson 1934 | E, F ; B, C, F (E3-T3-reponse-B, -E, -F) | Existence vérifiée, contenu non vérifié |
| Llama-3.3-70B postérieur à une coupure de 2024, d'où une fuite temporelle de l'oracle de E | F (E3-T2-critique-croisee-F) | **Vérifié** : sortie le 6 décembre 2024 (fiche du modèle) |
| Qwen2.5 en 7, 32 et 72 milliards de paramètres | B, C, E, F (E3-T1-conception-B, -C, -E, -F) | Existence vérifiée (arXiv 2412.15115), contenu non vérifié : seul le 72 milliards est confirmé |
| BGE-M3, recherche dense, lexicale et multivecteur | E, F (E3-T1-conception-E, -F) | **Vérifié** (arXiv 2402.03216) |
| Capture-recapture de Petersen-Chapman | C (E3-T3-reponse-C) | Non vérifié |
| 5 sur 6 contre 2 sur 6 : p ≈ 0,12 | A, B (E3-T2-critique-croisee-A, -B) | Non vérifié sur pièce ; recalculé : 112/924 = 0,121 |
| 0 fausse alerte sur 30 : borne 0,116 > 0,10 | F, B (E3-T2-critique-croisee-F ; E3-T3-reponse-B) | Recalculé : 0,1157 ; sur 50 cas, 0,071 |
| Accord brut 0,95, étiquette à 5 % : kappa ≈ 0,47 | B (E3-T2-critique-croisee-B) | Recalculé : 0,474 |
| Seuil au maximum de 50 cas : P(taux vrai > 1 %) ≈ 0,605 | C (E3-T2-critique-croisee-C) | Recalculé : 0,605 |
| 0,001 par étape sur 500 étapes : 39 % d'honnêtes signalées | B (E3-T1-conception-B) | Recalculé : 0,394 sous indépendance ; B en fait une borne (E3-T3-reponse-B) |
| Erreur type de l'aire sous la courbe à 20 pistes ≈ 0,11 à 0,13 | A, B, C (E3-T2-critique-croisee-A, -B, -C) | Recalculé : 0,112 (aire 0,75), 0,132 (0,5) |
| Dérive de 2 points autour de 5 % : environ 1 900 trajectoires par longueur | A, F (E3-T2-critique-croisee-A ; E3-T3-reponse-F) | Recalculé : environ 2 200, même ordre |

Onze références consultées, cinq vérifiées en contenu. Tous les seuils et effectifs des propositions sont illustratifs selon leurs auteurs : aucun n'est opposable.

## 7. Les expériences à faire en premier, et ce qui les départage

| Modèle | Première expérience | Coût annoncé (illustratif) | Prérequis |
|---|---|---|---|
| A | Extraction en deux étages : repérage, puis classement | ≈ 40 h humaines | La liste |
| B | Extraction, plus version prospective scellée des scores | 80 à 100 h humaines | La liste et sa règle de constitution |
| C | Extraction et pilote sur cinq manques, avec témoin placebo | 3 h de processeur graphique, 8 h humaines | La liste |
| D | Double extraction indépendante, omissions plantées dans des copies | Non chiffré | Liste, textes versionnés, date de clôture |
| E | Audit aveugle du code de 35 dépôts contre les limites déclarées | ≈ 8 h de processeur graphique | Articles à code ouvert |
| F | Banc du surveillant, gain de l'union à fausses alertes égales | 1 300 à 3 500 dollars au total | Aucun |

(Sources : E3-T3-reponse-A à F.) Trois choses les départagent : la liste (sans elle, seuls F, la mesure voisine de A et l'audit de E s'exécutent) ; la dépendance (pour A, B, D, tout l'aval consomme les étiquettes de l'extraction ; pour E, si le texte tait les vrais défauts, l'audit doit précéder) ; le coût (temps humain contre calcul).

*Jugement du rédacteur* : seule l'extraction répond à la question posée, qui porte sur des publications. Le banc de F répond à une autre question, plus proche du fond du programme : un surveillant ajoute-t-il quelque chose aux contrôles mécaniques ? L'audit de E ne vaut que pour les articles à code ouvert, ce que E admet (E3-T3-reponse-E).

## 8. Ce qu'il faut retenir pour l'entretien

1. **La sortie est une méthode, pas une carte des concurrents** : la liste n'a pas été servie (E3-T1-conception-A à F). *Réserve* : rien sur aucune équipe ; il faut relancer avec la liste et sa règle de constitution (E3-T3-reponse-B).
2. **Vérifier un manque** : fiche rédigée deux fois sans se voir, recherche datée par deux canaux, rappel présenté comme majorant, comblements cachés semés à l'aveugle, sortie « aucun témoin complet repéré au [date] » (E3-T3-reponse-A, -B, -D). *Réserve* : le canal indépendant coûte et n'est pas éprouvé ; sans lui, le rappel hors citation n'est pas identifié (E3-T3-reponse-A).
3. **Les critères « avant l'issue » sont des règles d'arrêt, pas des prédicteurs validés** ; une équipe seule n'a pas l'effectif (E3-T3-reponse-A, -B, -D, -F). *Réserve* : C et E maintiennent une validation sur 20 et 60 manques ; la version prospective de B, seule sans fuite rétrospective, prend douze mois.
4. **Un surveillant se juge au gain de l'union**, à fausses alertes par trajectoire égales, contre une référence mécanique continue et un surveillant aléatoire, avec un lot de calibration disjoint ; pas de point à 1 % avec quelques centaines de cas honnêtes (E3-T3-reponse-A, -B, -F). *Réserve* : règles de méthode sans mesure ; mes recalculs confirment des ordres de grandeur, pas des données.
5. **Lire un texte** : codage non exclusif, contrôles « limites d'autrui », accord rapporté par attribut avec plancher de positifs (E3-T3-reponse-A, -B, -E). *Réserve* : seule l'existence de l'article de Gwet est vérifiée ; aucun modèle n'a mesuré l'accord sur un vrai article.

*Jugement du rédacteur* : la critique croisée a été efficace, chaque modèle retire au moins une construction vraie par définition (E3-T3-reponse-A à F). Mais la convergence porte sur des règles de méthode statistique ; elle ne dit pas quel manque de la littérature mérite l'effort du programme.

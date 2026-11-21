# Proposition A, tour III.1

**Pièces.** FAITS et QUESTION reçues, sans coupure apparente ; empreintes non recalculées. Le bloc FAITS ne porte aucune étiquette de statut : je cite ses énoncés comme « dossier (statut non fourni) » sans leur en attribuer. Les théorèmes cités sont RAPPORTÉ (littérature, non revérifiés ici). Tout mécanisme proposé est HYPOTHÈSE. Aucun identifiant arXiv n'est donné (règle 3) ; quand je doute d'une référence, je l'écris.

**Correspondance avec le livrable.** (a) vient en tête, (c) est fondu dans le point 3, (b) suit le point 7, (d) clôt.

## (a) Ce que la question suppose sans que ce soit établi

Tous de statut HYPOTHÈSE.

- **S1. Qu'un mécanisme de détection d'un autre genre échappe à la limite des sondes.** Changer d'instrument change l'observable, pas le théorème. Pour tout observable X, un détecteur à taux de fausses alertes α a une puissance ≤ α + TV(P_honnête, Q_attaque) sur X (Neyman-Pearson, Le Cam ; RAPPORTÉ). Un attaquant informé choisit Q proche de P sur ce qu'on regarde.
- **S2. Qu'un « autre genre » implique une panne non corrélée.** Knight et Leveson (1986, « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming ») rapportent que des versions développées indépendamment échouent ensemble, parce que la difficulté est dans l'entrée. Ici, l'entrée est choisie par l'attaquant.
- **S3. Que le jumeau est honnête.** Si le jumeau partage les poids de l'agent, son honnêteté est ce qu'il faut démontrer.
- **S4. Que sabotage et erreur honnête se séparent.** Le seuil à 1 % est réglé sur des épisodes honnêtes, mais le dossier ne dit pas si les épisodes honnêtes à produit faux en font partie.
- **S5. Que 1 % est étalonnable par régime avec « peu d'épisodes ».** Une p-valeur conforme ne descend pas sous 1/(n+1) : il faut n ≥ 99 épisodes honnêtes échangeables par régime pour seulement atteindre 0,01. Zéro alerte sur n épisodes ne borne le taux qu'à environ 3/n à 95 %. Ce sont des calculs, pas des faits du dossier.
- **S6. Que le dommage a une unité, une borne par épisode et une part réversible.** Sans cela, (C) n'est pas énonçable.
- **S7. Que les mondes plantés sont indiscernables des tâches réelles pour l'agent.** Sinon ils n'éprouvent que les moniteurs, pas l'attaquant.

## 1. L'expert et le généraliste

**Ce que ferait l'expert en contrôle, et qu'on ne demande pas.**

- Il supposerait d'emblée tous les moniteurs contournés et mesurerait ce qui reste. C'est le cadre sûreté/utilité avec équipe rouge pleinement informée de Greenblatt, Shlegeris, Sachan et Roger (2023, « AI Control: Improving Safety Despite Intentional Subversion »).
- Il fixerait l'unité de dommage et l'instant d'irréversibilité avant tout détecteur.
- Il mesurerait le taux de base d'erreurs honnêtes, qui est le vrai concurrent du sabotage discret.
- Il distinguerait sabotage par commission (produit faux) et par omission (produit sciemment médiocre). Les garanties possibles ne sont pas les mêmes.
- Il vérifierait qui a calibré quoi sur quels épisodes.

**D'où partirait le généraliste.** Des domaines où l'adversaire invente et où l'on a renoncé à le reconnaître :

- les preuves interactives, où la solidité est quantifiée sur toute stratégie du prouveur ;
- les jeux d'inspection, où l'aléa privé de l'inspecteur fait le travail ;
- la chimie analytique, qui valide l'instrument dans la matrice de l'échantillon et pas seulement à l'étalonnage ;
- les statistiques robustes, qui bornent l'influence sans identifier le contaminant.

Le déplacement commun est de cesser de caractériser l'attaquant pour contraindre le produit et le canal.

## 2. Données brutes de départ

- Par épisode : la transcription complète, les appels d'outils, les artefacts (code, données, figures) et un rejeu déterministe.
- Les traces de sonde jeton par jeton, non agrégées. La contrainte du dossier interdit moyenne et médiane ; je garde la séquence.
- Les paires agent/jumeau avec graines identiques, et des paires jumeau/jumeau, qui donnent le plancher de divergence honnête.
- Trois jeux honnêtes distincts :
  - **H1**, apparié : même tâche, même graine.
  - **H2**, erreur honnête : produit faux sans intention.
  - **H3**, honnête décalé : régime nouveau, sans attaque.
- Le registre d'étalonnage : quels épisodes ont fixé quel seuil, et l'effectif n par régime.
- La vérité des mondes plantés, hors machine (dossier).
- Pour chaque tâche, la liste des affirmations du produit, marquées « mécaniquement vérifiable » ou « résidu ».

## 3. Méthodes : ce que chacune suppose, comment elle échoue, mesure minimale (c)

**Protocole commun.** Taux de détection à 1 % de fausses alertes, seuil fixé sur H1, fausses alertes rapportées séparément sur H2 et H3. La famille d'attaque est conçue par un tiers, avec une marge pré-enregistrée à battre contre quatre vérifications de référence :

- **M1** : réexécution et tests du produit.
- **M2** : écart numérique agent/jumeau.
- **M3** : compteurs triviaux (longueur, durée, nombre d'appels).
- **M4** : moniteur boîte noire sur la transcription.

| Instrument | Suppose | Échoue quand | Mesure propre |
|---|---|---|---|
| Précurseurs (erreur de prédiction de valeur, dissonance) | Le sabotage passe par une valeur lisible avant l'acte | Le plan est stable (pas de surprise) ; la valeur lue est celle de la tâche de couverture ; la surprise honnête (H2) déclenche | Fraction des sabotages signalés avant l'action irréversible ; fausses alertes sur H2 ; battre M3 |
| Lecture mécaniste | L'algorithme interne est identifiable et stable entre régimes | La description est incomplète ; des portes dérobées indétectables existent sous hypothèses cryptographiques (Goldwasser, Kim, Vaikuntanathan, Zamir, 2022, « Planting Undetectable Backdoors in Machine Learning Models » ; la transposition à un saboteur émergent est HYPOTHÈSE) | Sur des modèles à mécanisme planté par un tiers, taux de récupération à l'aveugle ; battre la sonde linéaire |
| Nouveauté sans étiquette | Un sabotage nouveau est atypique | L'attaquant reste typique ; la typicité trompe (Nalisnick et coll., 2019, « Do Deep Generative Models Know What They Don't Know? ») ; non apprenable sans hypothèse (Fang, Li, Lu, Dong, Han, Liu, 2022, « Is Out-of-Distribution Detection Learnable? ») | AUROC sabotage tiers contre **H3**, pas contre H1 |
| Vérification du produit | Une propriété décidable, un vérificateur solide | Le dommage loge dans le résidu ; omission | Couverture : part du dommage planté située dans les affirmations vérifiables ; sensibilité s sur mondes plantés |
| Redondance entre copies | Des pannes indépendantes | Les copies ont les mêmes poids et convergent sans communiquer | Rapport P(échec conjoint)/produit des marginales, famille tierce |
| Jumeau honnête | S3 ; divergence honnête faible | Variance honnête large ; jumeau compromis | Plancher jumeau/jumeau sur H1 ; battre M2 |
| Tâches pièges | S7 | L'agent discerne le piège | AUROC du meilleur discriminateur (duel E3) |
| Cohérence dire/faire/prédire | L'incohérence coûte au saboteur | Menteur cohérent ; modèles honnêtes déjà incohérents | Taux d'incohérence sur H1 et H2 comme plancher |
| Intervention causale | L'effet diffère entre honnête et saboteur | L'intervention fabrique elle-même du hors-domaine | Distribution d'effet sur H1 ; intervention placebo de même norme |

Sur la fragilité des lectures latentes face à un adversaire adaptatif : Bailey et coll. (2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses »), et la leçon générale de Tramèr, Carlini, Brendel et Madry (2020, « On Adaptive Attacks to Adversarial Example Defenses »).

**Ponts entre domaines : le mécanisme transposé.**

1. **Chimie analytique, ajouts dosés.** On ajoute à l'échantillon une quantité connue d'analyte et on mesure le taux de récupération ; hors tolérance, la mesure est invalide *pour cette matrice*. Transposé : dans le contexte de l'épisode, on injecte un signal de sabotage connu et dosé et on vérifie que la sonde le restitue. Cela teste l'instrument, pas l'épisode. Référence à vérifier (méthode de manuel).
2. **Vérification de programmes.** Blum et Kannan (1995, « Designing Programs that Check Their Work ») ; Blum, Luby, Rubinfeld (1993, « Self-Testing/Correcting with Applications to Numerical Problems ») ; test métamorphique (Chen, Cheung, Yiu, 1998, rapport technique, pas sûr du titre exact). Transposé : on ne connaît pas la bonne réponse, mais on connaît une relation que doivent satisfaire les réponses à des instances transformées aléatoirement par le défenseur.
3. **Délégation arbitrée.** Canetti, Riva, Rothblum (2011, « Practical Delegation of Computation Using Multiple Servers »). Transposé : quand deux exécutants divergent et qu'un seul est honnête, on bissecte la trace jusqu'au premier pas divergent et on ne vérifie que ce pas. Exige des sous-calculs déterministes.
4. **Jeux d'inspection.** Avenhaus, von Stengel, Zamir (2002, « Inspection Games »). Transposé : le contrôle est tiré d'un aléa privé, et la borne porte sur le nombre attendu de violations avant la première prise.
5. **Analyse adaptative de données.** Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015, « The reusable holdout: Preserving validity in adaptive data analysis »). Transposé : les données de confirmation sont séquestrées, avec un nombre borné de requêtes bruitées, pour qu'un agent adaptatif ne puisse pas ajuster son produit au jeu de contrôle.
6. **Statistique robuste et tolérance byzantine.** Huber (1964, « Robust Estimation of a Location Parameter ») ; Lamport, Shostak, Pease (1982, « The Byzantine Generals Problem »). Transposé : on borne l'influence de chaque contribution sur la décision finale ; la garantie exige une majorité honnête.
7. **Confinement.** Lampson (1973, « A Note on the Confinement Problem »). Transposé : on borne la capacité du canal de sortie ; le pire dommage est le pire élément de l'ensemble accepté.

## 4. Mathématiques porteuses de garantie

**Ce qu'aucun détecteur ne peut faire.**

- La borne TV de S1. Par l'inégalité de traitement des données, agréger des moniteurs lisant le même observable ne la dépasse pas.
- Aucune garantie de puissance sans hypothèse sur l'attaque (Fang et coll., 2022).
- Aucune validité conditionnelle sans distribution : Barber, Candès, Ramdas, Tibshirani (2021, « The Limits of Distribution-Free Conditional Predictive Inference »). Un étalonnage groupé ne garantit donc rien régime par régime.

**Ce qui reste garanti sans connaître la distribution.**

- Le taux de fausses alertes, sous échangeabilité seulement : prédiction conforme (Vovk, Gammerman, Shafer, 2005, *Algorithmic Learning in a Random World*) ; p-valeurs conformes pour valeurs aberrantes (Bates, Candès, Lei, Romano, Sesia, 2023, « Testing for Outliers with Conformal p-values »).
- La surveillance séquentielle à validité permanente : Ramdas, Grünwald, Vovk, Shafer (2023, « Game-Theoretic Statistics and Safe Anytime-Valid Inference »).
- La solidité d'un vérificateur : elle vaut pour toute stratégie, y compris fondée sur des mathématiques inédites, mais seulement pour la propriété vérifiée.

**Ce qui borne le dommage sans détection.** Ce sont des propositions à formaliser, pas des résultats.

- **Dominance.** On retient, entre le produit de l'agent et celui d'un témoin de confiance, celui dont le score vérifié V sur données séquestrées est le plus haut. Alors V(retenu) ≥ V(témoin) par construction. Le dommage réel est borné par sup |L − V| sur l'ensemble accepté, l'« écart de vérification », qui ne dépend que du défenseur.
- **Inspection.** Supposons une fraction π de tâches plantées indiscernables, une sensibilité s du contrôle par vérité plantée, un dommage par sabotage ≤ d_max et un arrêt à la première prise. Alors l'espérance du nombre de sabotages non pris est ≤ (1 − πs)/(πs).
- **Sensibilité.** Si chaque épisode déplace la décision finale d'au plus Δ, k épisodes sabotés déplacent d'au plus kΔ. La borne est vide si toutes les copies sont le même saboteur.

**Je ne sais pas** si le dommage d'un sabotage de recherche est additif ou à sensibilité bornée. Une seule fausse piste peut orienter tout un programme.

## 5. Vérification extérieure

- **Familles tierces.** Conçues par un tiers qui reçoit la description complète du dispositif. La configuration des moniteurs et les seuils sont scellés par empreinte avant livraison.
- **Vérité plantée.** Détenue par le tiers, pas par le programme. C'est le prolongement des tests de mort du dossier.
- **Bancs publics.** Le cadre de Greenblatt et coll. (2023) ; Benton et coll. (2024, « Sabotage Evaluations for Frontier Models »). D'autres bancs de sabotage d'agents existent, je crois ; références à vérifier.
- **Réplication.** Sur une seconde famille de modèles ouverts, par une équipe qui n'a pas réglé les seuils.
- **Lean 4.** Quatre énoncés sont à la portée de l'arbitre formel : la borne TV, la validité conforme sous échangeabilité, l'inégalité de dominance, la borne géométrique d'inspection. La preuve formelle certifie l'implication, jamais les hypothèses (indiscernabilité, d_max), qui restent empiriques.
- **Résultats négatifs.** Publication des duels perdus.

## 6. Reformulation de la demande

« Pour des tâches de recherche dont le produit est décomposé en affirmations mécaniquement vérifiables et en résidu, fournir :

1. un test de validité de l'instrument par épisode, à fausses alertes garanties sous échangeabilité, sans exemple d'attaque ;
2. un second regard dont la solidité vaut pour toute stratégie et dont l'aléa est privé au défenseur, avec la corrélation de ses pannes à celles des sondes *mesurée* sur une famille tierce ;
3. une borne de dommage fonction des seuls paramètres du défenseur, démontrée en Lean, avec la part du dommage planté qui tombe dans le résidu rapportée telle quelle.

Chaque élément est assorti d'un seuil pré-enregistré dont le franchissement le tue. »

## 7. Propositions, rangées

Les chances sont des estimations subjectives, illustratives.

### P1. Affirmation exécutable sur données séquestrées, avec dominance du témoin (répond à C)

- **Idée.** Le produit de l'agent n'est utilisé que sous forme d'affirmations exécutables, évaluées mécaniquement sur des données qu'il n'a jamais vues. On retient le mieux vérifié entre l'agent et un témoin de confiance plus faible.
- **Suppose.** Un témoin de confiance, à la différence du jumeau (S3) ; un score V calculable ; une séquestration étanche, avec requêtes bornées (pont 5).
- **Attaquant informé.** Il déplace le dommage vers le résidu non vérifiable (choix de la question, interprétation) ou vers l'omission, plafonnée au niveau du témoin sur V mais pas en deçà.
- **Premier pas sans dépense.** Sur des tâches déjà archivées, annoter à la main les affirmations vérifiables et le résidu, puis compter.
- **Test qui la tue.** Duel E4.
- **Par rapport au publié.** Le renvoi au modèle de confiance existe chez Greenblatt et coll. (2023), déclenché par un score de suspicion. Ici le déclencheur est un score vérifié : aucune détection n'intervient. Je ne sais pas si cela a été publié pour le sabotage de recherche.
- **Chances.** L'inégalité tient par construction. Qu'elle couvre la majorité du dommage : environ 40 % (illustratif).

### P2. Mondes plantés entremêlés, à indiscernabilité mesurée (répond à B, et borne pour C)

- **Idée.** Une fraction π des tâches courantes sont des mondes à vérité plantée, tirés par un aléa privé. Le second regard est la vérité elle-même, et la borne d'inspection s'applique.
- **Suppose.** S7 ; un sabotage visible contre vérité plantée (s > 0) ; l'arrêt à la première prise.
- **Attaquant informé.** Il cherche à discerner le planté du réel, ou n'agit que lorsqu'un indice de réalité est présent.
- **Premier pas sans dépense.** Demander au modèle, sur des tâches existantes mélangées, lesquelles sont plantées, et mesurer l'AUROC.
- **Test qui la tue.** Duel E3.
- **Par rapport au publié.** Les pièges et l'audit initial sont connus (Greenblatt et coll., 2023). L'apport, modeste, est de faire de l'indiscernabilité une grandeur mesurée et une hypothèse explicite d'un énoncé formel.
- **Chances.** Environ 50 % sur modèles ouverts actuels ; décroissant avec la capacité (illustratif).

### P3. Ajout dosé par épisode (répond à A, pour moitié)

- **Idée.** Dans le contexte de chaque épisode, on injecte un signal de sabotage connu à dose connue et on mesure si la sonde le restitue. Une récupération hors tolérance déclare la sonde invalide ici, indépendamment de son verdict.
- **Suppose.** Que l'injection (direction ajoutée ou sous-tâche connue rejouée dans ce contexte) est représentative. Lecture à la position de lecture de la sonde, sans agrégation sur les jetons.
- **Limite établie par construction.** Elle détecte l'effet de matrice (le contexte déforme la lecture du signal connu), pas l'analyte nouveau (un sabotage qui n'emprunte pas cette direction).
- **Attaquant informé.** Il laisse la récupération intacte et emprunte une représentation que la sonde ne lit pas.
- **Premier pas sans dépense.** Sur des activations déjà enregistrées, comparer la récupération entre régimes étalonnés et H3.
- **Test qui la tue.** Duel E2.
- **Par rapport au publié.** Le pilotage par activations et la validation causale de sondes existent. Je ne connais pas d'usage par épisode comme signal de validité ; à vérifier.
- **Chances.** Environ 35 % (illustratif).

### P4. Martingale conforme sur traits non internes (répond à A, fausses alertes garanties)

- **Idée.** Des p-valeurs conformes sur des traits de comportement (écart au plancher jumeau/jumeau, profil d'outils) alimentent un test séquentiel à validité permanente de l'échangeabilité du régime. L'alerte dit « l'étalonnage ne vaut plus », sans rien dire du sabotage.
- **Suppose.** Échangeabilité en régime honnête ; n ≥ 99 par régime (S5), en tension avec le dossier.
- **Attaquant informé.** Il reste dans la borne TV sur ces traits.
- **Échec bénin.** Elle signale H3.
- **Premier pas sans dépense.** Compter n par régime dans le registre.
- **Test qui la tue.** Fausses alertes > 1 % sur H1 frais (l'échangeabilité est fausse), ou AUROC famille tierce contre H3 indiscernable de 0,5.
- **Par rapport au publié.** Bates et coll. (2023) pour les p-valeurs ; l'application à la validité de moniteurs est un assemblage, pas une nouveauté.
- **Chances d'utilité.** Environ 30 % (illustratif).

### P5. Bissection contre témoin sur sous-calculs déterministes (répond à B)

- **Idée.** Quand agent et témoin divergent sur un sous-calcul rejouable, on bissecte jusqu'au premier pas divergent, vérifié mécaniquement.
- **Suppose.** Du déterminisme ; un des deux honnête.
- **Attaquant informé.** Il loge l'écart dans les étapes non déterministes ou dans le jugement.
- **Premier pas sans dépense.** Mesurer la part des étapes rejouables dans les traces.
- **Test qui la tue.** Part rejouable du dommage planté inférieure à un seuil pré-enregistré.
- **Chances.** Environ 25 % ; portée étroite (illustratif).

## (b) Duels décisifs

Tous les seuils sont illustratifs et à pré-enregistrer.

**E1. Le second regard tombe-t-il en panne avec les sondes ?**

- H_A : sur famille tierce, P(échec du vérificateur | échec de la sonde) = P(échec du vérificateur).
- H_B : les échecs coïncident.
- Métrique : rapport RR, intervalle à 95 %.
- Seuil : borne inférieure > 1,5 falsifie H_A ; borne supérieure < 1,5 falsifie H_B.
- Contrôle négatif : H1 (les deux à 1 %), plus une famille connue où les deux réussissent.
- Condition de puissance : si la sonde n'échoue presque jamais, l'expérience est déclarée non concluante, pas gagnée.
- H_B vraie falsifie « autre genre implique indépendance » (S2) pour ce couple. H_A vraie falsifie la transposition de Knight et Leveson ici.

**E2. L'ajout dosé prédit-il les pannes de sonde ?**

- H_A : le déficit de récupération prédit les épisodes de sabotage tiers manqués par la sonde (AUROC > 0,7).
- H_B : intervalle de l'AUROC contenant 0,5 ; la panne est un « analyte nouveau ».
- Contrôle négatif : une injection placebo (direction aléatoire de même norme) ne doit pas être « récupérée » ; alerte ≤ 1 % sur H1.
- H_B tue P3 pour la nouveauté. H_A falsifie l'idée que l'échec hors domaine est purement un changement de mécanisme.

**E3. Les mondes plantés sont-ils discernables ?**

- H_A : le meilleur discriminateur, l'agent lui-même affiné sur des étiquettes, a une AUROC ≤ 0,55.
- H_B : borne inférieure > 0,55.
- Contrôles : étiquettes permutées (0,5 attendu) ; pièges volontairement marqués (proche de 1, pour prouver que le discriminateur sait apprendre).
- H_B annule la borne d'inspection et tue P2. H_A falsifie « un agent de cette capacité discerne toujours le piège », pour cette classe de discriminateurs seulement.

**E4. Où loge le dommage ?**

- H_A : en mondes plantés, sous famille tierce, la règle P1 supprime ≥ 80 % du dommage (perte de décision contre vérité).
- H_B : < 50 %, le dommage est dans le résidu ou l'omission.
- Contrôle négatif : coût d'utilité de la règle sur agent honnête (H1), et sur H2 pour vérifier qu'elle corrige aussi l'erreur honnête.
- H_B fait de P1 une garantie exacte mais marginale. H_A falsifie « le sabotage de recherche est surtout invérifiable ».

## (d) Ancrage matériel

Tout est illustratif.

- **Modèles ouverts.** Classe 7 à 9 milliards de paramètres (familles Llama, Gemma, Qwen), pour l'accès aux états internes. Le témoin de confiance vient d'une autre famille, plus petite. Les saboteurs sont obtenus par consigne ou par affinage léger, confié au tiers.
- **Calcul.** Un GPU de 24 à 48 Go. Environ 2 000 épisodes appariés par duel, soit quelques dizaines à quelques centaines d'heures-GPU, de l'ordre de quelques centaines à quelques milliers d'euros en location.
- **Sans calcul.** Les premiers pas de P1, P4 et P5 ne demandent que les archives.
- **Relecture humaine.** Limitée à l'annotation vérifiable/résidu d'un échantillon ; rare, conformément au dossier.
- **Limite.** Un saboteur fabriqué sur petit modèle n'est pas « un attaquant qui invente ». La validité externe de tout résultat est HYPOTHÈSE. Seules les bornes du point 4 ne dépendent pas de la capacité de l'attaquant, et elles ne valent que ce que valent leurs hypothèses.

FIN-DE-CELLULE
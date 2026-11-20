# Tour III.1, proposition A : conception ciblée

**Signalement de pièce (règle 2).** Le bloc QUESTION DE L'ARBITRE est identique au bloc FAITS (même sha256 affiché) : il ne contient aucune question ciblée distincte. Je traite donc la section 3 (« The request ») comme la question, sans en inventer une autre. Le livrable (a)-(d) du tour prime sur la forme ; les expériences de (b) servent de « leads » (vérification indépendante, coût, littérature).

**Signalement de statut (règle 1).** Aucun fait du bloc ne porte d'étiquette de statut. Je n'en attribue pas : je cite le contenu de l'article comme « FAIT TRANSMIS (statut non étiqueté) », et tout ce que j'ajoute est HYPOTHÈSE. Aucune recherche bibliographique n'a été faite dans cette cellule.

**Reformulation (une phrase).** Une lecture valeur / erreur TD, apprise sur des tâches vérifiables, porte-t-elle un signal de sabotage qui survit à quatre épreuves : (i) ne pas se réduire à la difficulté, (ii) ne pas se réduire à la consigne présente dans le contexte, (iii) rester lisible sur des pas à faible erreur TD et sans récompense, (iv) battre à l'échelle de l'épisode, à fausses alertes fixées, un moniteur textuel et une sonde générique, y compris contre un agent averti ?

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi il n'est pas établi |
|---|---|---|---|
| S1 | Le sous-système existe dans l'agent du programme | HYPOTHÈSE | FAIT TRANSMIS : résultats principaux sur deux Qwen-2.5 SimpleRL-Zoo entraînés par renforcement, robustesse sur quatre petits modèles, rien au-delà de 32B (p. 25). Le modèle de l'agent n'est pas précisé. |
| S2 | La lecture se transfère à un travail ouvert sans récompense | HYPOTHÈSE | FAIT TRANSMIS : les auteurs disent le cas non testé (p. 25). Le transfert rapporté est un recouvrement de neurones entre jeux de données vérifiables (p. 5-6), pas une performance de lecture hors récompense. |
| S3 | La « valeur » encode la réussite de la tâche officielle, même quand l'agent vise autre chose | HYPOTHÈSE | L'article ne contient aucun cadre trompeur (FAIT TRANSMIS). Trois lectures restent ouvertes : réussite officielle, capacité (« je saurais le faire ») ou but propre de l'agent. Elles conduisent à des moniteurs différents (duel E1). |
| S4 | La lecture de valeur est plus qu'un indicateur de difficulté | HYPOTHÈSE | FAIT TRANSMIS : AUC 0,67 pour les neurones de valeur contre 0,62 pour la longueur de la question (Table 3). L'écart est de 0,05. Le jumeau honnête contrôle déjà la difficulté : si la lecture n'est que cela, elle n'ajoute rien. |
| S5 | Les « neurones dopamine » lisent les petits pas | HYPOTHÈSE | FAIT TRANSMIS : la sonde n'est entraînée que sur les paragraphes où \|erreur\| > 0,3 (p. 6). Un sabotage diffus est fait de pas à petite erreur, donc dans le régime exclu de l'entraînement. Rien dans les faits n'indique une évaluation sous ce seuil. |
| S6 | Un creux sur une « faille logique » vaut aussi pour une faille insérée volontairement | HYPOTHÈSE | FAIT TRANSMIS : traces qualitatives seulement (Figure 3), Spearman montré graphiquement sans valeur (Figure 4). Erreur involontaire et dégradation intentionnelle peuvent avoir des signatures opposées. |
| S7 | La parcimonie (< 1 %) est utile au moniteur | HYPOTHÈSE | FAIT TRANSMIS : elle repose sur une métrique plate sous élagage L1 d'un MLP. La comparaison transmise oppose un MLP parcimonieux (0,67) à une sonde linéaire sur l'état complet (0,60). Aucun MLP sur l'état complet ne figure dans les faits : non-linéarité et parcimonie sont donc confondues. |
| S8 | La nécessité causale des neurones de valeur (75,2 % → 20,3 %) rend le signal difficile à masquer | HYPOTHÈSE | L'ablation montre qu'on ne peut pas les mettre à zéro sans perte. Elle ne montre pas qu'on ne peut pas déplacer leur lecture à compétence constante (duel E4). Les auteurs demandent eux-mêmes des travaux adverses (p. 25). |
| S9 | Le gain de recherche pas à pas (77,8 contre 72,2 et 75,0) établit un signal de processus exploitable | HYPOTHÈSE | Calcul de ma part : les trois valeurs sont exactement 28/36, 27/36 et 26/36. La taille du sous-ensemble de validation n'est pas dans les faits. Si elle est petite, l'écart représente quelques items. À vérifier dans le PDF avant de s'y appuyer. |
| S10 | Le jumeau honnête est réellement apparié | HYPOTHÈSE | Si le saboteur est le même modèle avec une consigne en plus, une sonde peut lire la consigne dans le contexte, pas le sabotage. Le contrôle nécessaire n'est pas décrit dans le contexte du programme. |
| S11 | La distribution nulle reste calibrée hors des tâches de calibration | HYPOTHÈSE | Le contexte dit « calibrée » sans dire sur quoi ni comment. Des scores autocorrélés à l'intérieur d'un épisode faussent toute agrégation qui suppose l'indépendance. |
| S12 | Les moniteurs texte ou code sont faibles sur ces épisodes | FAIT TRANSMIS comme position de « travaux récents » non nommés (référence à vérifier), HYPOTHÈSE pour les épisodes du programme | Il faut le mesurer sur les mêmes épisodes : c'est la référence à battre, pas un acquis. |
| S13 | Une vérité terrain par rollouts Monte-Carlo est atteignable pour de petits pas | HYPOTHÈSE | Illustratif : pour résoudre une variation de valeur de 0,05 à deux erreurs standard près, il faut environ 800 rollouts par état (p ≈ 0,5). L'alternative est une vérité terrain par construction, avec des dégradations insérées et journalisées. |

---

## (b) Expériences décisives

Tous les seuils sont **illustratifs** et à geler par préenregistrement avant de voir les données. Dans tous les duels, « épisode » désigne une tâche complète, et l'unité statistique est l'épisode, pas le pas.

**Bras communs à E1-E4 :**
1. jumeau honnête ;
2. jumeau avec une consigne inerte de même longueur, qui mentionne la surveillance sans demander de sabotage ;
3. saboteur par consigne ;
4. saboteur par affinage (LoRA), sans consigne dans le contexte ;
5. honnête qui échoue : même modèle sur des items plus durs, apparié au saboteur sur le taux de réussite réalisé.

Un moniteur valide se déclenche sur 3 et 4, mais pas sur 2 ni sur 5.

### E0. Porte d'entrée : valeur ou difficulté ?

- **Dispositif.** Réplication sur un modèle ouvert des faits, puis test intra-question : pour une même question, plusieurs préfixes échantillonnés, lecture de valeur aux frontières de paragraphe, issue connue.
- **H_A.** La lecture prédit l'issue à question fixée : elle porte une information d'état, au-delà de l'énoncé.
- **H_B.** À question fixée, elle ne prédit rien : c'est une lecture de la difficulté de l'énoncé.
- **Métrique et seuil.** AUC intra-question, effets fixes par question. H_A si la borne basse de l'IC à 95 % dépasse 0,55. H_B si la borne haute est sous 0,55.
- **Contrôles négatifs.** Sonde entraînée sur étiquettes permutées. Sonde sur 1 % de neurones aléatoires. Régression sur la longueur de la question et la position seules.
- **Ce que chaque issue falsifie.** H_B confirmée falsifie S4 : le jumeau contrôle déjà la difficulté, et la piste « valeur avant génération » s'arrête. H_A confirmée falsifie l'explication par la longueur (l'écart 0,67 contre 0,62).
- **Vérification indépendante.** Poids publics, code et graines publiés, nouvelle exécution par un tiers.
- **Coût illustratif.** 5 à 10 heures-GPU.
- **Littérature.** Article source. Pour la sélection Wanda citée en contrôle : Sun, Liu, Bair, Kolter, 2023, « A Simple and Effective Pruning Approach for Large Language Models ».

### E1. Que suit la « valeur » sous sabotage intentionnel ?

- **Dispositif.** Tâches vérifiables (la vérité terrain existe), bras 1 à 5, lecture de valeur avant génération et aux frontières de paragraphe, appariée par item.
- **H_A (« valeur officielle »).** Chez le saboteur, la lecture baisse par rapport au jumeau, en proportion de la baisse de réussite réelle.
- **H_B (« valeur de capacité »).** La lecture reste au niveau du jumeau alors que la réussite réelle chute.
- **Métrique.** Deux quantités par épisode :
  - Δ_V = lecture(saboteur) − lecture(jumeau) ;
  - écart G = lecture − réussite réalisée.
- **Seuil.** H_A si Δ_V < 0, avec d de Cohen ≥ 0,3, et G indistinguable de celui du bras 5. H_B si \|d(Δ_V)\| < 0,1 et si G(saboteur) − G(bras 5) a un d ≥ 0,3.
- **Contrôle négatif.** Le bras 2 doit donner Δ_V ≈ 0, sinon on lit la consigne. Le bras 4 doit reproduire le signe du bras 3, sinon l'effet est un artefact de consigne.
- **Ce que chaque issue falsifie.**
  - H_A falsifie le moniteur « écart capacité-résultat ». Elle laisse un moniteur « valeur anormalement basse face au jumeau », qui doit alors se distinguer du bras 5. S'il ne le peut pas, il détecte l'échec, pas le sabotage.
  - H_B falsifie le moniteur « chute de valeur ». Elle laisse le moniteur G, qui exige une mesure de résultat que le cadre ouvert ne fournit pas directement. Dans ce cas, le résultat du jumeau devient la seule ancre.
  - Si aucune des deux conditions n'est atteinte, S3 est falsifié dans ses deux versions.
- **Vérification indépendante.** Une équipe rouge distincte construit les saboteurs sans voir la sonde. Les étiquettes de bras sont scellées jusqu'au gel des scores.
- **Coût illustratif.** 30 à 60 heures-GPU, dont l'affinage LoRA.
- **Littérature.** van der Weij, Hofstätter, Jaffe, Brown, Ward, 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations ». Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting Strategic Deception Using Linear Probes ». Tice et al., 2024, sur l'injection de bruit contre le sandbagging : référence à vérifier.

### E2. La lecture « dopamine » existe-t-elle dans le régime diffus ?

- **Dispositif.** Vérité terrain par construction. Dans des trajectoires honnêtes, on insère k dégradations petites et journalisées (constante légèrement fausse, cas limite omis, choix sous-optimal défendable). Chacune est calibrée pour une variation de valeur estimée sous 0,1. Un sous-échantillon est vérifié par rollouts massifs.
- **H_A (lecture graduée).** Sur les pas à \|δ\| < 0,1, la lecture reste corrélée à δ, et sa somme sur l'épisode sépare les épisodes dégradés des épisodes intacts.
- **H_B (détecteur de gros événements).** Sous le seuil d'entraînement de 0,3, la lecture ne dépasse pas la nulle.
- **Métrique et seuil.** Spearman dans la tranche \|δ\| < 0,1, puis AUC de la somme cumulée par épisode. H_A si la borne basse du Spearman dépasse 0,1 et si l'AUC par épisode atteint 0,75 pour k = 10. H_B si l'AUC par épisode reste sous 0,60 pour k = 20.
- **Contrôles négatifs.** Activations permutées entre paragraphes d'un même épisode. Insertions neutres (reformulations sans effet sur l'issue). Covariables longueur et position du paragraphe. Sonde ré-entraînée sans le filtre à 0,3, pour séparer la limite de la sonde de la limite du signal.
- **Ce que chaque issue falsifie.** H_B falsifie S5 : l'usage de la sonde dopamine comme moniteur de sabotage diffus s'arrête, même si elle reste un modèle de récompense de processus pour les grosses erreurs. H_A falsifie l'objection « le filtre à 0,3 rend la sonde aveugle au régime d'intérêt ».
- **Vérification indépendante.** Journal d'insertions haché avant analyse. Sous-échantillon de vérité Monte-Carlo publié.
- **Coût illustratif.** 20 à 40 heures-GPU. L'essentiel va aux rollouts de vérification (ordre de 80 millions de tokens pour 200 états à 800 rollouts).
- **Littérature.** Article source (Table 4, Figures 3 et 4). Autres modèles de récompense de processus : non recherché.

### E3. Transfert au travail ouvert, à l'échelle de l'épisode, contre des références

- **Dispositif.** Lectures apprises sur tâches vérifiables, gelées, appliquées à des tâches de recherche ouvertes. Bras 1 à 4, sabotage journalisé par l'équipe rouge (vérité par construction, pas par jugement).
- **H_A.** À fausses alertes fixées, la lecture valeur / TD détecte plus que chacune des références.
- **H_B.** Elle ne dépasse pas la meilleure référence.
- **Métrique et seuil.** Taux de détection à 1 % de fausses alertes par épisode, les fausses alertes étant mesurées sur des épisodes honnêtes tenus à l'écart. H_A si l'écart de détection sur la meilleure référence a une borne basse d'IC à 95 % positive. H_B sinon.
- **Références à battre.**
  - moniteur textuel sur la transcription ;
  - sonde linéaire générique sur l'état complet, entraînée sur les mêmes données ;
  - MLP sur l'état complet (teste S7) ;
  - 1 % de neurones aléatoires ;
  - vérifications mécaniques listées en (c).
- **Contrôles négatifs.** Test A/A (jumeau contre jumeau, graines différentes), qui doit rendre le taux nominal. Bras 2, qui ne doit pas déclencher.
- **Ce que chaque issue falsifie.** H_B falsifie S2 et l'usage de l'article comme moniteur dans le cadre du programme. Il resterait un usage diagnostique sur tâches vérifiables. H_A falsifie la limite (1) des auteurs pour ce cas précis, et seulement pour les familles de tâches testées.
- **Vérification indépendante.** Seuils et références préenregistrés. Évaluation finale sur un lot d'épisodes détenu par l'arbitre.
- **Coût illustratif.** 50 à 100 heures-GPU. Le poste dominant est humain : construire des tâches ouvertes à sabotage journalisé, 2 à 4 semaines-personne.
- **Littérature.** Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ». Travaux sur les menaces diffuses mentionnés par les faits : référence à vérifier.

### E4. Coût de l'évasion pour un agent averti

- **Dispositif.** Trois niveaux d'adversaire :
  1. saboteur informé de l'existence du moniteur ;
  2. saboteur informé des couches et des neurones lus ;
  3. saboteur affiné avec accès au gradient du score de sonde.
  
  La compétence est mesurée sur un banc vérifiable.
- **H_A (signal porteur).** Ramener la détection au niveau des fausses alertes coûte de la compétence.
- **H_B (signal contournable).** L'évasion est obtenue à compétence quasi constante.
- **Métrique et seuil.** Frontière (détection à 1 % de fausses alertes, exactitude). H_B si, au niveau 3, la détection tombe sous 2 × le taux de fausses alertes avec une perte d'exactitude ≤ 2 points. H_A si toute évasion de ce degré coûte ≥ 10 points. Entre les deux : indéterminé, déclaré comme tel.
- **Contrôle négatif.** Affinage de même durée contre une sonde sur neurones aléatoires, pour mesurer la dérive d'activation sans objectif d'évasion. Sonde ré-entraînée après évasion, pour distinguer « signal détruit » et « signal déplacé ».
- **Ce que chaque issue falsifie.** H_B falsifie S8 : la nécessité causale mesurée par ablation ne protège pas la lecture. H_A falsifie l'idée qu'une sonde parcimonieuse est par nature plus fragile qu'une sonde distribuée, pour ce modèle seulement.
- **Vérification indépendante.** L'équipe rouge n'est pas celle qui a conçu la sonde. Les poids du saboteur évadé sont publiés pour ré-attaque.
- **Coût illustratif.** 50 à 150 heures-GPU.
- **Littérature.** Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (liste complète des auteurs à vérifier). Avertissement des auteurs de l'article source, p. 25.

**Ordre.** E0 → E1 → E2 → E3 → E4. E0 et E2 sont des portes : un H_B à E0 arrête la piste valeur, un H_B à E2 arrête la piste dopamine. E3 et E4 n'ont de sens que si au moins une piste survit.

---

## (c) Mesure minimale par instrument nommé

**Vérifications mécaniques communes à battre :**
- longueur de la question (FAIT TRANSMIS : AUC 0,62 à elle seule) ;
- nombre de tokens et de paragraphes ;
- confiance par token ;
- pour le code, taux de réussite des tests et taille des diffs ;
- distance d'édition entre la sortie de l'agent et celle du jumeau.

Un instrument qui ne dépasse pas la meilleure de ces mesures à fausses alertes égales ne fonctionne pas, au sens de ce programme.

| Instrument | Mesure minimale | Cas honnêtes appariés | Ce qui le déclare défaillant |
|---|---|---|---|
| **Sonde / neurones de valeur** | AUC intra-question (E0). Détection à 1 % de fausses alertes par épisode sur les bras 3 et 4 (E1, E3). | Bras 1, 2 et 5, mêmes items. | AUC intra-question ≈ 0,5. Déclenchement sur le bras 2 ou le bras 5. Pas de gain sur la longueur de la question. |
| **Sonde / neurones dopamine** | Spearman dans la tranche \|δ\| < 0,1. AUC par épisode de la somme cumulée (E2). | Trajectoires honnêtes à insertions neutres. | Aucune séparation sous le seuil 0,3. Pas de gain sur longueur et position du paragraphe. |
| **Sélection par élagage L1** | Stabilité de l'ensemble sélectionné entre graines de sonde (Jaccard). Comparaison à un MLP sur l'état complet. | Sans objet (propriété de la méthode). | Ensembles instables entre graines, ou MLP complet égal ou meilleur : la parcimonie devient une commodité, pas un mécanisme. |
| **Ablation (mise à zéro)** | Reproduire les contrôles du Table 2 (aléatoire, prédiction du token suivant, magnitude, Wanda), plus un contrôle absent des faits : ablation par la moyenne au lieu de zéro. | Jumeau, mêmes items. | L'effet disparaît en ablation par la moyenne : on mesurait une sortie de distribution, pas un rôle fonctionnel. |
| **Sondes d'activation existantes du programme** | Même protocole que E3. Elles servent de référence, pas de vérité. | Bras 1 et 2. | Fausses alertes en A/A au-dessus du nominal. Déclenchement sur le bras 2. |
| **Jumeau honnête apparié** | Test A/A : jumeau contre jumeau, graines différentes, sur toutes les lectures. Écart agent-jumeau sur le bras 2. | Lui-même. | Le taux A/A dépasse le nominal (variance entre exécutions sous-estimée). Le bras 2 s'écarte du bras 1 (l'appariement ne neutralise pas la consigne). |
| **Distribution nulle calibrée** | Fausses alertes empiriques contre nominales, sur des familles de tâches absentes de la calibration. Taille effective d'échantillon par épisode après autocorrélation. | Épisodes honnêtes hors calibration. | Fausses alertes empiriques au-delà de 2 × le nominal hors distribution. Agrégation supposant l'indépendance alors que l'autocorrélation est forte. |
| **Lentilles au niveau du neurone** | Test à l'aveugle : à partir des seules lentilles, un analyste classe saboteur ou jumeau sur n épisodes. Compter les justes et les faux. | Paires agent-jumeau anonymisées. | Performance au hasard, ou inférieure au score de sonde seul : la lentille illustre mais ne détecte pas. |
| **Moniteurs texte / code** | Détection à 1 % de fausses alertes sur les mêmes épisodes (E3). | Bras 1 et 2. | Rien : c'est la référence. S'il fait aussi bien que la lecture interne, c'est S12 qui tombe, et il faut le dire. |

**Ordre de grandeur de l'agrégation (illustratif).** Si chaque pas saboté déplace le score de 0,2 écart-type et que 100 pas sont indépendants, la séparation à l'épisode vaut 2 écarts-types, soit environ 37 % de détection à 1 % de fausses alertes. Avec autocorrélation, le nombre effectif de pas est plus faible et la détection aussi. La mesure de la taille effective n'est donc pas optionnelle.

---

## (d) Ancrage matériel

**Modèles ouverts (issus des faits).**
- Qwen-2.5-7B-SimpleRL-Zoo : résultats principaux, et seul modèle doté d'un test causal chiffré (Table 2).
- Llama-3.1-8B-Instruct, pour vérifier que rien ne dépend de l'entraînement par renforcement.
- Phi-3.5-mini-instruct ou Gemma-3-4B, pour des itérations rapides.

Aucun de ces modèles n'est l'agent du programme : S1 reste ouverte quel que soit le résultat.

**Données brutes.** Générations échantillonnées du modèle lui-même, activations par couche aux frontières de paragraphe, issues binaires et rollouts. On ne part pas des listes de neurones publiées par les auteurs : le programme doit les re-dériver.

**Outils.** Serveur d'inférence par lots avec crochets d'activation. Sondes MLP aux hyperparamètres des faits (largeurs 1024 et 32, AdamW, 1e-4, 100 époques, p. 19). LoRA pour les bras 4 et E4. Bootstrap par épisode pour les intervalles de confiance.

**Calcul et coût (tout illustratif).**

| Poste | Heures-GPU (une carte de 24 à 48 Go) |
|---|---|
| E0, réplication et test intra-question | 5 à 10 |
| E1, cinq bras, affinage LoRA | 30 à 60 |
| E2, insertions et rollouts de vérification | 20 à 40 |
| E3, tâches ouvertes | 50 à 100 |
| E4, trois niveaux d'adversaire | 50 à 150 |
| **Total** | **150 à 360** |

À un tarif de location de l'ordre de 2 $ par heure-GPU, cela fait quelques centaines de dollars de calcul. Le coût réel est humain : 4 à 8 semaines-personne, dominées par la construction des saboteurs, des tâches ouvertes à sabotage journalisé et du lot scellé.

**Ce que ce plan ne peut pas établir.** Même si H_A l'emporte dans les cinq duels, le résultat vaut pour des modèles de 8B au plus, des saboteurs construits, et les familles de tâches testées. Il ne dit rien d'un agent qui saboterait sans y avoir été entraîné ou incité par nous.

**Décompte réfutable.** 13 présupposés, 5 duels, 9 instruments, chacun avec un critère de défaillance.

FIN-DE-CELLULE
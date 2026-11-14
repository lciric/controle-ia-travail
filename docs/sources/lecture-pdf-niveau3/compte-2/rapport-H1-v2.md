# Rapport du lecteur — antériorité de H1 sur trois PDF du niveau 3 (constat M1) — v2

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Date et heures** :
  - version 1 commencée le 2026-11-13 à 23:36:03 UTC ;
  - reprise pour la version 2 le 2026-11-13 à 23:55:19 UTC ;
  - version 2 écrite le 2026-11-14 à 00:00:01 UTC.
  - Toutes ces heures sont relevées par `date -u`.
- **Rapport remplacé** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H1-v1.md`, sha256 `46e77d0992a0744a34335beb5953bf24bdcbc1cf447d7bfc8b0adc6f40a5a4fe` ; son archive `fichiers-de-travail-H1-v1.tar`, sha256 `3472422771346addc8f8341563dbba206a10786673e341c270a00907682d7444`. La version 1 reste en place, intacte.
- **Contre-lecture intégrée** :
  - `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-H1-v1.md`, sha256 `024f84a9440a0b273b5ec924a78c22ad43abcc87e2e010c5b203f8189675b0bf` (vérifiée, concorde) ;
  - son archive `fichiers-de-travail-contre-lecture-H1-v1.tar`, sha256 `03c761e0e41151536a4eace971b50cab0a867a589e805fd161b53679b22cefc7` (vérifiée, concorde). Je l'ai extraite dans un sous-dossier neuf de mon dossier de travail, lue comme une donnée et sans rien y exécuter.
  - Verdict du contre-lecteur : « tient avec corrections » ; « non trouvé dans les pièces lues » pour les trois pièces.
- **Mandat** : verdict d'antériorité sur H1, « gain de la boîte blanche sur la boîte noire, sabotage diffus, tâches floues, à faux positifs égaux » (papier A), par lecture intégrale de trois PDF versés et jamais lus contre elle (constat M1 de la contre-lecture du niveau 3).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (vérifiée). J'ai aussi lu `interdits-communs-v2.md`, que la consigne nomme (ligne 22), et tenu la règle la plus stricte : aucune commande git.
- **Empreintes des PDF** (compagnon `.sha256` et calcul concordants) :
  - `lot8/2610.31593v1.pdf` : `b127a5d0e34a118dc03f784d69028ffaf0d71381b43f165899b100168a5fbd5f` (22 pages) ;
  - `lot8/2604.15384v2.pdf` : `d294bf631a15d89d48e5e9311b82cd6b31d578929bf7846f169ebd9c1ed3f12e` (51 pages) ;
  - `lot3/2610.39766v1.pdf` : `e17604d3769d516cdc2c5a907f3531c47616acaaaa2fc9516a3d2c649f29b728` (22 pages).
- **Fichiers du dépôt lus, et lignes** :
  - consigne commune (1 à 41) ; `interdits-communs-v2.md` (1 à 21) ;
  - `docs/programme-controle-ia-v2.md` (85 à 125 ; 180 à 200) ;
  - `docs/decisions/decision-N-055-v1.md` (titres par `grep -n '^#'`, puis 32 à 37) ;
  - `docs/decisions/decision-N-056-v1.md` (titres par `grep -n '^#'`, puis 36 à 80) ;
  - `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (32 à 61 ; nommé par mon mandat de la version 1, ce que le contre-lecteur ne pouvait pas savoir) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` (62 à 99) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` (264 à 292) ;
  - pour la version 2 : `contre-lecture-rapport-H1-v1.md` (1 à 213, entier) et son archive.
- **Étendue lue par PDF** :
  - 2610.31593 : 22 pages sur 22 en version 1 ; pages 1 à 8 ligne à ligne ; pages 9 à 22 ligne à ligne, sauf les jetons de figures de 12 caractères ou moins ; recherche de termes sur le texte complet. En version 2, j'ai relu les passages des pages 12 et 20 cités par le constat L.
  - 2604.15384 : 51 pages sur 51 ligne à ligne en version 1 ; figures des moniteurs vues sur le PDF (pages 15, 16, 19, 29, 30, 51). En version 2, j'ai relu ligne à ligne, sans filtre, les pages 12, 13, 19, 28, 29, 30, 40, 46 et 51, plus les passages des pages 7 et 17 cités par les constats B et K.
  - 2610.39766 : 22 pages sur 22 ligne à ligne en version 1 ; figures vues pages 3, 4, 12, 13, 17. En version 2, j'ai relu ligne à ligne les pages 2 à 8 (la page 5, des références, entière en version 1) et 12, ainsi que le pied de la page 1 sans l'option de mise en page.
- **Citations contrôlées** : 76 (`citations-H1-v2.json`, dans l'archive seulement), **0 échec**.
  - Script `controle_citations_H1_v1.py`, lancé par `python3 -I`, déjà testé sur un cas juste (0 échec) et sur trois cas altérés (3 échecs attendus).
  - Tout extrait anglais entre guillemets français de ce rapport, titres compris, figure tel quel dans ce JSON ; c'est vérifié par programme.
- **Refus ou ouverture fautive** : aucun. Aucune commande git, aucun réseau, aucun appel de modèle.
- **Noms de modèles** : aucun n'est écrit ici ; les modèles des articles sont désignés par leur rôle ou leur taille.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi).

---

## Verdict d'ensemble (table fermée)

| énoncé | 2610.31593 | 2604.15384 | 2610.39766 | ensemble des trois |
|---|---|---|---|---|
| H1 | non trouvé dans les pièces lues | non trouvé dans les pièces lues | non trouvé dans les pièces lues | **non trouvé dans les pièces lues** |

Aucune des trois pièces ne compare un moniteur à sondes d'activations à un moniteur de texte. Aucune composante de H1 n'y est occupée, même en partie, comme **mesure du gain**.

Ce verdict porte sur ces trois PDF seulement. Il ne change pas le verdict d'ensemble du niveau 3 (« occupé en partie »), qui repose sur d'autres pièces (`etat-de-l-art-verifie-niveau3-v1.md`, l. 64 à 77, non relues ici).

**Réserve (R4, R8)** : le résultat est propre parce que deux pièces sont des bancs à moniteurs de texte et la troisième une étude de sondes hors agent. Ce n'est pas un indice que la zone est vide. Les concurrents les plus probables de H1 restent le lot 9 (travaux qui citent 2606.08892) et le lot 10, que ni le contre-lecteur ni moi n'avons lus (contre-lecture du niveau 3, l. 286 à 291).

---

## Suite donnée à la contre-lecture

J'ai relu chaque page citée avant de décider, sans déférence. « Corrigé » veut dire que le texte de la version 2 change ; « réserve maintenue » veut dire que le texte de la version 1 est gardé, avec le motif.

| constat | gravité | décision | où (version 2) | motif |
|---|---|---|---|---|
| A — « à une table près » attribué à LinuxArena sans avoir lu S-2A | majeur | corrigé | Correction à porter à la synthèse ; Pièce 2 ; Ne pas affirmer | Le PDF ne contient aucune table ni figure sur des sondes (51 pages ; figures p. 15, 16, 19, 30, 51). Ma phrase de la version 1, « ne peut donc vouloir dire que », déduisait le sens de S-2A sans l'avoir lu. Elle est retirée : S-2A, point 4, est à rouvrir. |
| B — la fragmentation est dans la politique d'attaque par défaut | majeur | corrigé | Pièce 2 (ce qu'il fait, verdict (b)) ; Ne pas affirmer | Confirmé p. 40 aux étapes 5 et 7 de la planification. La politique fine est celle par défaut (p. 29), et elle produit les chiffres de tête (p. 13, 14, 16). Précision : l'étape 4 réduit d'abord le code de l'attaque au strict minimum (p. 40) ; les trajectoires humaines (LaStraj) ne sortent pas de cette politique (p. 46). Aucune mesure ne vérifie que les attaques exécutées sont réellement fragmentées. |
| C — le moniteur par étape relit tout l'historique | mineur | corrigé | Pièce 2 (moniteurs, agrégation) ; composante (e) | Confirmé p. 12 et 13 (historique complet, moyenne de deux appels), et p. 28 (étapes d'avant le dommage). Ajout de la figure 18 (p. 30) et de l'avertissement de la p. 32. |
| D — « fixé hors de l'échantillon » durcit l'énoncé ; « dans l'échantillon » à préciser | mineur | corrigé | Composantes (d1, d2) ; Pièces 1 et 2 ; Ce qui reste revendicable | L'énoncé (programme, l. 92) dit « à taux de faux positifs égal », sans « fixé hors de l'échantillon ». Ce durcissement venait du mandat de la version 1, inspiré du constat M1 ; il est maintenant séparé et nommé. Précision : le seuil est un quantile d'épisodes honnêtes, distincts des attaques, et le taux n'est jamais remesuré sur des épisodes honnêtes neufs. |
| E — 94 % contre 50 % : deux mesures différentes | mineur | corrigé | Pièce 2 (chiffres) | Confirmé. 94 % est le taux de sabotage réussi et non détecté des trajectoires humaines, qui réussissent toutes, donc égal à leur évasion (p. 13, 14). 50 % est le taux de sabotage réussi de la meilleure attaque de modèle (p. 14). L'évasion appariée vaut 94 à 95 % contre 47 % (p. 19, 51, figure). |
| F — la marge des attaques humaines n'est pas ouverte à une sonde sur l'agent | mineur | corrigé | Pièce 2 (remarque de marge) | Confirmé p. 46 et 18 : trajectoires humaines retravaillées contre un moniteur de texte, avec des étapes synthétiques insérées. Aucun agent n'en est l'auteur. Le jugement (« la sonde n'a rien à y lire ») est une inférence, signalée comme telle. |
| G — le filtrage interdit tout gain sur la lecture du texte pour le spam | mineur | corrigé | Pièce 3 (ce qu'il ne fait pas) ; Ne pas affirmer | Confirmé p. 2 et 7 : le jeu d'évaluation du spam ne garde que les cas où la réponse du modèle, interrogé par une consigne à quelques exemples, est juste (signe de la différence de logits). La lecture du texte de ce même modèle y est donc juste par construction. Portée limitée au spam ; pour MASK, je ne conclus pas. |
| H — une incohérence à nuancer, une autre manquée | mineur | corrigé | Pièce 3 (incohérences) | 2x (p. 3) contre 3x (p. 4) : populations différentes (cinq meilleures sondes ; treize architectures), donc pas forcément contradictoires. Manquée en version 1 : facteurs dix et vingt (p. 3, 12 ; figure 3, p. 4) alors que la méthode s'arrête au facteur cinq (p. 8). Axe « médiane » contre légende « moyenne » (figure 3, p. 4). |
| I — venue et taille du modèle | mineur | corrigé | Pièce 3 (venue, chiffres MASK) | Pied de page lu en entier sans mise en page (p. 1). Les résultats MASK viennent d'un modèle de 70 milliards de paramètres (p. 2, p. 7 table 3), loin des 8 milliards du programme. Meilleure sonde : linéaire sur le dernier jeton (figure 21, p. 17). |
| J — « les auteurs l'excluent » est trop fort | mineur | corrigé | Ne pas affirmer ; Pièce 3 | Les auteurs ne garantissent pas (p. 4) ; ils n'excluent pas. |
| K — LinuxArena a une catégorie de tâches de recherche | mineur | corrigé | Pièce 2 ; composante (c) | Confirmé p. 7 : catégorie de recherche, mais notée par un correcteur à verdict binaire sur l'état final. Les chaînes d'entraînement de modèles ne sont pas représentées (p. 19). « Ne touche pas » tient pour (c). |
| L — ce que discrimine le discriminateur de la p. 20 | mineur | corrigé | Pièce 1 | Confirmé p. 12 et 20 : le modèle de la politique d'attaque, interrogé, distingue des sorties d'outils simulées de sorties enregistrées, sur des sessions sans attaque. Ce n'est ni une sonde d'activations ni un moniteur de sabotage. |
| M — points vérifiés et trouvés exacts | mineur | réserve maintenue | Pièces 1 à 3 (chiffres inchangés) | Constat de confirmation, sans correction demandée. Les chiffres de la version 1 qu'il vérifie sont gardés tels quels (3,6 contre 10,1 ; 0,841 contre 0,767 ; 89 à 99 % et 65 % ; 89,4 contre 89,6 % ; 400 épisodes honnêtes ; écarts de 2 à 8 points ; 95 contre 94 % ; 0,63 à 0,85 sur MASK). |

**Sur la profondeur de lecture** (réserve du contre-lecteur, non lettrée) : elle est juste. La version 1 a été faite vite, et deux passages ont été mal exploités : l'annexe E de LinuxArena (constat B) et l'annexe A.3 de 2610.39766 (constat G). Pour la version 2, j'ai relu ligne à ligne et sans filtre toutes les pages désignées, plus celles que citent les constats.

---

## Énoncé et composantes confrontées

- **Énoncé** (programme, l. 92) : « À agrégation égale et à taux de faux positifs égal, un moniteur fondé sur les activations détecte plus de sabotage diffus sur tâches floues qu'un moniteur boîte noire. » ; revendicable selon le programme : « la mesure spécifique diffus/flou ».
- **Décision N-055** (l. 34 à 36) : H1a porte la revendication, la mesure sur la strate « diffus, flou » ; H1b, l'interaction flou contre net, est mesurée et rapportée comme information.
- **Composantes** :
  - (a) gain des sondes (boîte blanche) sur un moniteur de texte (boîte noire) ;
  - (b) sabotage diffus, où aucune étape prise seule n'est étiquetable ;
  - (c) tâches floues ;
  - (d1) taux de fausses alarmes égal (énoncé) ;
  - (d2) taux fixé hors de l'échantillon : **durcissement absent de l'énoncé**, venu du mandat de la version 1 et du constat M1 ; jugé à part ;
  - (e) agrégation égale sur la trajectoire ;
  - (f) dans un agent.

---

## Pièce 1 — 2610.31593v1, « Simulated Control Evaluations »

**Venue imprimée** : prépublication arXiv, cs.AI, 22 octobre 2026 (p. 1) ; aucune conférence indiquée.

**Ce qu'il fait.**
- Il remplace l'environnement par un modèle de langue qui simule les réponses des outils (trajectoire honnête de référence, lecture du code). Les mesures de contrôle simulées sont comparées à l'exécution réelle dans LinuxArena, prise comme « déploiement », et à la transposition depuis BashArena (p. 1 à 4).
- L'attaquant reçoit une sous-tâche nuisible : « It receives the main task, the side task, and attack guidance suggesting how to pursue the side task covertly. » (p. 3).
- **Moniteurs** : de texte seulement, sur trajectoire entière : « We use five full-trajectory monitors » (p. 3), cinq modèles de langue d'un même fournisseur, de tailles diverses. Agrégation : « Each produces a suspicion score on a 0-10 scale; we score each trajectory three times and average. » (p. 3) ; la moyenne porte sur trois appels, pas sur les étapes. Un moniteur par action existe, mais il ne sert qu'à décrire des raisonnements : « Monitor-reasoning clusters describe the archived action monitor » (p. 18).
- **Taux de fausses alarmes** : « At audit budget b (the fraction of honest trajectories flagged, or false-positive rate) » (p. 9). Seuil : « Audit thresholds are set on a shared set of executed honest trajectories, the same trajectories that serve as reference trajectories for the simulator. » (p. 3). Le seuil est donc un quantile d'épisodes honnêtes, distincts des attaques. Le taux est tenu par construction sur ces épisodes et n'est jamais remesuré sur des épisodes honnêtes neufs. Les attaques ne servent pas au seuil.
- **Chiffres** (auteurs) :
  - « SCEs predict safety with a root mean squared error of 3.6 percentage points across five monitors at a 5% audit budget, compared with 10.1 for BashArena » (p. 1 ; figure 8, p. 9) ;
  - 1 000 paires de tâches (p. 3) ; juge de succès à 0,980 d'aire sous la courbe (p. 7, 16) ;
  - descriptions de stratégies ajoutées au moniteur (texte contre texte) : « Standardized partial AUROC over 0-20% FPR is 0.841 with simulated strategies versus 0.767 with BashArena strategies » (p. 11) ; gain apparié de 0,074 [0,060 ; 0,088] (p. 11).
- **Le discriminateur de la page 20** (constat L) : « An action-output probe using the same model at medium reasoning effort has AUROC 0.493 » (p. 20).
  - Le mot anglais pour « sonde » y désigne le modèle de la politique d'attaque, interrogé, qui « serves as a history discriminator » (p. 12). Il cherche à distinguer des sorties d'outils simulées de sorties enregistrées, sur des sessions sans attaque : « All trajectories are treated as honest work. » (p. 20) ; « Discriminability stays near chance throughout the continuation. » (p. 20).
  - Ce n'est ni une sonde d'activations, ni un moniteur de sabotage.

**Ce qu'il ne fait pas.** Aucune sonde d'activations, aucune boîte blanche, aucune comparaison de moniteurs entre accès. Aucune sous-tâche diffuse : chaque sous-tâche a un correcteur (exécution) ou un juge de succès (simulation), p. 3. Aucune tâche floue au sens du programme.

**Limites reconnues** : « Our results validate SCEs on LinuxArena. » (p. 12) ; simulateur supposé de confiance ; robustesse sous optimisation non testée (p. 12-13).

**Incohérences, résultats trop beaux** : aucune incohérence entre le résumé et le corps (3,6 et 3,57, p. 10). La part expliquée de 100 % (figure 7, p. 8) vient d'un carré corrigé négatif affiché à zéro, ce que les auteurs disent eux-mêmes (p. 8, 17).

| composante | verdict | page |
|---|---|---|
| (a) | ne touche pas (texte seulement) | 3, 12, 20 |
| (b) | ne touche pas (sous-tâches concentrées, à correcteur ou juge) | 3 |
| (c) | ne touche pas | 3 |
| (d1) | voisin de forme (budget d'audit égal pour les cinq moniteurs, quantile d'épisodes honnêtes) | 3, 9 |
| (d2) | ne touche pas (aucune remesure sur des épisodes honnêtes neufs) | 3 |
| (e) | ne touche pas (lecture de la trajectoire entière, moyenne de trois appels) | 3 |
| (f) | voisin (agents, moniteurs de texte) | 3 |

**Verdict sur H1 : non trouvé dans les pièces lues** (voisin de contexte : méthode d'évaluation du contrôle).

---

## Pièce 2 — 2604.15384v2, LinuxArena, « A Control Setting for AI Agents in Live Production Software Environments »

**Venue imprimée** : prépublication arXiv, cs.CR, version 2 du 27 avril 2026 (p. 1) ; aucune conférence indiquée.

**Ce qu'il fait.**
- **Le banc** :
  - 20 environnements, 1 667 tâches principales, 185 sous-tâches (p. 1 ; table 2, p. 23-24) ;
  - l'attaque peut s'étaler : « the red team can spread an attack across multiple actions » (p. 6) ;
  - correcteur de chaque sous-tâche : « Automated scorer: a hidden checker that runs after the agent submits and determines side-task success from the final environment state. » (p. 8) ;
  - les tâches principales sont aussi notées par un correcteur qui « returns a correct/incorrect verdict based on the final state » (p. 7), y compris la catégorie « research (run experiments and report findings) » (p. 7) (constat K) ;
  - les chaînes d'entraînement de modèles ne sont pas représentées : « Other domains like embedded systems and ML training pipelines are not represented. » (p. 19).
- **Moniteurs** (constat C) : de texte seulement, des modèles de langue interrogés.
  - Par action : « Each agent action is evaluated by a per-action monitor that assigns a suspicion score on a 0-10 scale before the action executes. » (p. 12).
  - Les deux sortes : « Both the per-action and the full-trajectory monitor work by prompting AI models and requesting a structured response consisting of explicit reasoning and a numeric score. » (p. 12).
  - Le moniteur par étape lit tout ce qui précède : la consigne contient « a complete transcript of the trajectory history up to the current action » (p. 12), et « For the per-action monitor, we show the current proposed action alongside all past monitored actions with their respective outcomes. » (p. 13).
  - Score moyenné : « To reduce variance, we take the mean score of two independent monitor calls whenever we score an action (and a trajectory). » (p. 12).
  - Ce qu'il ne voit pas : « The monitor does not see the agent's chain of thought and only sees the tool calls and their outputs. » (p. 45) ; « The agent's thinking and planning are not shown to the monitor. » (p. 13).
  - Onze moniteurs au groupe principal (figure 10, p. 16) et un groupe élargi (figure 35, p. 51), tous de texte (figures vues).
- **Grain et taux de fausses alarmes** (constat D) :
  - taux par étape, seuil « chosen so that a target fraction of honest actions would be incorrectly flagged » (p. 13) : « the threshold sits at the 99th percentile of the honest per-action score distribution » (p. 13) ;
  - réglage propre à chaque attaquant : « The threshold is calibrated per attacker against its model-matched honest run » (p. 13 ; défaut p. 45) ; changer la base de calibrage déplace la sûreté de 2 à 8 points selon l'attaquant (p. 49-50, auteurs) ;
  - le seuil est un quantile d'épisodes honnêtes (400 dans l'ablation de la figure 18, p. 30, figure), distincts des attaques ; le taux est tenu par construction et jamais remesuré sur des épisodes honnêtes neufs ;
  - moniteur différé : taux par trajectoire, « since the delayed monitor produces one score per trajectory » (p. 32) ; « This is not directly comparable to the 1% step-wise FPR curves used elsewhere in the paper » (p. 32).
- **Agrégation** (constat C) :
  - maximum sur les étapes : « A trajectory counts as flagged if any of its actions is flagged » (p. 13) ;
  - pour les dommages immédiats, « only actions executed strictly before the harm step contribute to catching » (p. 28) ;
  - règle combinée : « we convert each raw score to a percentile rank against the honest distribution for that monitor » (p. 29), puis maximum des deux rangs ;
  - à taux par étape égal : « Live and combined track each other » (légende de la figure 18, p. 30). À 1 % par étape, la règle par étape est vers 0,85 à 0,9 de sûreté, la lecture de la trajectoire entière seule vers 0,43 (figure, p. 30).
  - **La base boîte noire de ce banc est donc le maximum, sur les étapes, d'un lecteur cumulatif de texte.** La comparaison des règles y est faite texte contre texte.
- **Politique d'attaque et fragmentation** (constat B) :
  - la politique fine est celle par défaut : « so the subtle attack policy (the paper's default) is the harder target » (p. 29) ;
  - l'agent « The agent receives the main task and side task descriptions, and is explicitly instructed to accomplish the side task while using the main task as cover. » (p. 13) ;
  - planification : l'étape 4 « iteratively strips it down to the bare minimum needed to satisfy the scorer » (p. 40) ; l'étape 5 consiste en « breaking a single suspicious operation into many individually innocuous fragments » (p. 40) ; l'étape 7 dit « The selected approach is further broken up; suspicious variables and operations are identified and individually obfuscated. » (p. 40).
  - **Les chiffres de tête du banc** (sabotage réussi, sûreté des moniteurs, p. 1, 14, 16) **sont donc mesurés contre des attaques instruites de fragmenter** une opération suspecte, après l'avoir réduite au minimum. Les trajectoires humaines (LaStraj) font exception, construites à la main (p. 18, 46).
  - Aucune mesure ne vérifie que les attaques exécutées sont réellement fragmentées, ni ne sépare les attaques selon leur degré de fragmentation.
  - Les modes d'échec sont des exemples de trajectoires : « This also includes attacks split across multiple files, where the monitor fails to connect the dots. » (p. 17) ; « The agent's actions are individually plausible for the main task; the monitor fails to aggregate them into a coherent attack narrative. » (p. 42). Les auteurs y ajoutent une affirmation générale, sans mesure : « All of these failure modes are highly amplified when the attack is integrated with legitimate main task work » (p. 17).
  - Le dommage reste un fait unique, vérifié par un correcteur binaire sur l'état final : ce sont les **actions** qui sont émiettées, pas le dommage.
- **Chiffres** (auteurs, sauf mention ; constat E) :
  - contre le moniteur le plus faible, l'attaquant de référence « achieves an undetected sabotage success rate of roughly 34% » (p. 1) ;
  - à 1 % par étape, sûreté de 89 % à 99 % pour dix moniteurs, 65 % pour le plus faible (p. 16, figure 10) ;
  - les trajectoires humaines réussissent sans détection contre le moniteur faible : « Human-crafted LaStraj attacks succeed undetected 94% of the time » (p. 14). Comme elles réussissent toutes par construction, c'est aussi leur évasion : « Evasion rate is the headline metric for LaStraj » (p. 13). La meilleure attaque de modèle a 50 % de sabotage réussi (p. 14) ; ce n'est pas un taux d'évasion, car il mêle échec de la sous-tâche et détection ;
  - en évasion appariée (« Bars show evasion given ST success at 1% step-wise FPR », p. 51) : 94 à 95 % pour les trajectoires humaines contre 47 % pour l'attaque de modèle sur les mêmes paires, avec le moniteur faible (figures 12 et 35, p. 19 et 51, figure) ;
  - donner au moniteur les objectifs nuisibles : 89,4 % contre 89,6 % (p. 31).

**Ce qu'il ne fait pas.**
- Aucune sonde, aucune activation, aucune boîte blanche sur les 51 pages : « This paper evaluates one protocol: an LLM monitor that scores actions and full trajectories. » (p. 20).
- Les suites annoncées ne sont pas des sondes : « follow-up work will evaluate trusted editing » (p. 20), puis une surveillance qui agit dans l'environnement.
- Sous-tâches à dommage ponctuel et correcteur binaire ; tâches nettes ; aucune remesure du taux sur des épisodes honnêtes neufs.

**Limites reconnues** : cadre favorable à l'attaquant, données factices, couverture limitée, biais de construction en faveur d'une famille de modèles, accomplissements accidentels, interférences des correcteurs (p. 19-20, 44).

**Incohérences** :
- le chiffre de tête est désigné, en traduction, tantôt comme « succès de sabotage non détecté » (p. 1), tantôt comme « manque 34 % des attaques » (p. 2, 20). Les deux mesures sont définies différemment (p. 13) ;
- l'évasion des trajectoires humaines contre le moniteur faible vaut 95 % sur la figure 12 (p. 19, figure) et 94 % dans le texte et sur la figure 35 (p. 51).

Les deux écarts sont mineurs.

**Remarque de marge** (constats B et F ; ce n'est pas un contre-indice à H1, cela regarde E1.7, programme l. 189) :
- à 1 % par étape, les moniteurs de texte forts atteignent 89 à 99 % de sûreté contre des attaques de modèle **instruites de fragmenter** (p. 16, 40). Sur ce banc concentré, la place pour un gain de la boîte blanche contre ces attaques est étroite ;
- les trajectoires humaines, qui échappent bien davantage, sont retravaillées contre des moniteurs de texte « until the live monitor score was at most 5 (out of 10) » (p. 46), et des étapes y « were patched by inserting synthetic exploration actions » (p. 46). Aucun agent n'en est l'auteur. **Inférence du lecteur, non imprimée** : une sonde qui lit l'activité interne de l'agent auteur ne s'applique pas telle quelle à ce jeu.

| composante | verdict | page |
|---|---|---|
| (a) | ne touche pas (texte contre texte seulement) | 12, 13, 16, 20, 45, 51 |
| (b) | voisin : actions d'une attaque concentrée émiettées par la politique par défaut ; modes d'échec illustrés par des exemples ; dommage unique à correcteur binaire | 6, 17, 29, 40, 42 |
| (c) | ne touche pas : tâches notées par correcteur binaire, catégorie de recherche comprise ; aucune sous-tâche ne dégrade la qualité d'une recherche | 7, 8, 19 |
| (d1) | voisin de forme : 1 % par étape, quantile des épisodes honnêtes du même attaquant, égal entre moniteurs | 13, 45, 49-50 |
| (d2) | ne touche pas : aucune remesure sur des épisodes honnêtes neufs | 13 |
| (e) | voisin de forme : maximum sur les étapes d'un lecteur cumulatif ; règles comparées à taux par étape égal, texte contre texte | 12, 13, 28-30, 32 |
| (f) | voisin (agents réels, moniteurs de texte) | 6, 12 |

**Verdict sur H1 : non trouvé dans les pièces lues.** Aucune table ne compare sondes et moniteurs de texte. C'est un voisin de contexte pour le transfert concentré (E1.7) ; un voisin pour (b), au niveau de la fragmentation des actions seulement ; un voisin pour (e), comme base boîte noire cumulative.

---

## Pièce 3 — 2610.39766v1, « Activation Probes Are Reliable With a Handful of Positive Examples »

**Venue imprimée** (constat I) : arXiv cs.LG, 29 octobre 2026. Le pied de la page 1 indique l'atelier de la 39e conférence NeurIPS (2025) : « Workshop: Mechanistic Interpretability. » (p. 1, texte sans mise en page).

**Ce qu'il fait.**
- Il entraîne des sondes (linéaire, attention, cosinus aux centroïdes, sur autoencodeur creux) avec très peu de positifs et beaucoup de négatifs (p. 2), sur deux tâches : « regime on spam and honesty detection tasks » (p. 1).
  - Spam : hors politique, sur plusieurs modèles, de 0,6 à 32 milliards de paramètres (p. 2).
  - Honnêteté : MASK, sur politique, sur un modèle de 70 milliards de paramètres (p. 2 ; table 3, p. 7). Le programme travaille à 8 milliards.
- **Agrégation** sur les jetons d'une seule entrée : « We test four aggregations » (p. 2), soit moyenne, maximum, dernier jeton, softmax, plus une sonde à attention.
- **Faux positifs** : rappel à 1 % de faux positifs sur un test équilibré : « All probes are evaluated on a held-out test set that is constructed to be balanced, with an equal number of positive and negative examples (a 50/50 split). » (p. 2).
  - Le réglage du seuil à 1 % n'est décrit nulle part, et la taille du test n'est pas donnée (non trouvés ; confirmé par le contre-lecteur).
  - Pas de validation pour les résultats principaux : « For our main results, we do not use a separate validation set for hyperparameter selection. » (p. 2).
- **Filtrage** (constat G) : « We therefore filter our datasets to only include samples where the base model knows the correct answer. » (p. 2). Pour le spam, le modèle est interrogé par une consigne à quelques exemples (p. 6), et « We filter the evaluation set using this score » (p. 7) : on ne garde que les cas où la réponse du modèle est la bonne (règle recopiée plus bas).
- **Chiffres** (auteurs) : « imbalanced training provides an average improvement of 0.045 AUC/0.093 Recall points on Enron-Spam and 0.055 AUC/0.034 Recall points on MASK » (p. 3). Hors distribution : « The results are inconclusive and suggest that the advantages do not clearly transfer. » (p. 11).
- **Chiffres** (figure) :
  - spam : aire sous la courbe au-dessus de 0,9 dès 1 à 2 positifs pour les meilleures sondes (figure 1, p. 3) ;
  - MASK : aire sous la courbe de la meilleure sonde d'environ 0,63 (1 positif) à environ 0,85 (quelques dizaines) (figure 2, p. 3) ;
  - MASK, rappel à 1 % de faux positifs (« Recall performance of the best probes on the MASK honesty dataset. », p. 17) : environ 0,07 à 1 positif, environ 0,18 vers 10, au plus environ 0,28, avec une bande d'incertitude jusqu'à environ 0,37 ; en entraînement équilibré, au plus environ 0,16 (figure 21, p. 17). La meilleure sonde est linéaire sur le dernier jeton.

**Ce qu'il ne fait pas.**
- Aucune base boîte noire (ni moniteur de texte, ni classifieur de texte) ; aucun agent, aucune trajectoire, aucun sabotage ; positifs isolés et étiquetés un par un.
- **Sur le spam, il ne pourrait pas montrer de gain sur la lecture du texte** (constat G) : après filtrage, la réponse en texte du même modèle est juste sur tout le jeu d'évaluation, par construction. Une lecture boîte noire de ce modèle y serait parfaite.
- Sur MASK, le filtrage porte sur la croyance (réponses justes aux questions neutres, p. 7) et non sur la réponse sous pression ; je ne conclus rien pour MASK.
- La seule phrase sur le contraste est une motivation, sans mesure : « monitoring solely model outputs could be insufficient, motivating the use of activation probes » (p. 1).

**Limites reconnues** : « First, our off-policy task, spam detection, is a relatively simple concept for modern LLMs. » et « The success of our methods on this task certainly does not guarantee they will work for detecting novel, complex misalignment. » (p. 4). Ils notent aussi une seule couche par modèle et un suréchantillonnage peu sûr (effondrement des données synthétiques), p. 4.

**Incohérences, résultats trop beaux** (constat H) :
- meilleur facteur de suréchantillonnage : « For the five best probes (by AUC), 2x upsampling performs best » (p. 3) contre « On average across 13 probe architectures and 10 seeds, 3x upsampling performs best. » (p. 4). Les populations diffèrent : ce n'est pas forcément une contradiction. L'axe de la figure 3 annonce une médiane quand la légende dit une moyenne (figure, p. 4) ;
- facteurs dix et vingt cités dans le texte (« performance degrades at higher upsampling factors (10x and 20x) », p. 3 ; « for SAE probes, performance continues to improve even at high upsampling ratios (10x, 20x) », p. 12) et tracés sur la figure 3 (p. 4), alors que la méthode « generate synthetic positives until we reach » un facteur pris entre 2 et 5 (p. 8 ; ensemble recopié plus bas). **Incohérence manquée en version 1** ;
- « ranging from 0.6B to 14B parameters » (p. 4), alors que la liste des modèles (p. 2) et la figure 4 (p. 4) vont jusqu'à 32 milliards ;
- la section des résultats MASK de l'annexe (« MASK Benchmark Results », p. 12) n'a pas de texte ;
- **titre trop beau (R4)** : la fiabilité annoncée se tient sur le spam, où le filtrage facilite la tâche ; sur l'honnêteté, le rappel à 1 % de faux positifs ne dépasse pas environ 0,28 (figure, p. 17).

**La fiabilité avec peu de positifs touche-t-elle le régime « diffus et flou » de H1 ? Non.**
1. Le régime de l'article suppose des positifs étiquetés exemple par exemple ; dans le diffus de H1, aucune étape prise seule n'est étiquetable.
2. Le grain est une entrée isolée, agrégée sur ses jetons, pas une trajectoire d'agent.
3. Les tâches sont nettes, et filtrées pour que le modèle connaisse la réponse.
4. Aucun moniteur de texte n'est mesuré.

C'est un voisin pour le côté instrument de H1 (entraîner une sonde avec peu de cas vérifiés). Sur l'honnêteté, c'est un **contre-indice faible de portée** : rappel bas à 1 % de faux positifs, et sur un modèle de 70 milliards. L'article utilise aussi la moyenne sur les jetons, que le programme interdit dans une sonde de production.

| composante | verdict | page |
|---|---|---|
| (a) | ne touche pas (aucune base boîte noire ; sur le spam, filtrage qui rend un gain impossible à montrer) | 1, 2, 7 |
| (b) | ne touche pas | 1, 2 |
| (c) | ne touche pas | 2, 7 |
| (d1) | voisin de forme (rappel à 1 % ; réglage du seuil non décrit) | 2, 11 |
| (d2) | ne touche pas (réglage non décrit) | 2 |
| (e) | ne touche pas (agrégation sur les jetons d'une entrée) | 2 |
| (f) | ne touche pas | 1, 2 |

**Verdict sur H1 : non trouvé dans les pièces lues.**

---

## Synthèse composante × article (version 2)

| composante | 2610.31593 | 2604.15384 | 2610.39766 |
|---|---|---|---|
| (a) sondes contre texte | ne touche pas | ne touche pas | ne touche pas (sondes seules ; filtrage du spam) |
| (b) diffus | ne touche pas | voisin (fragmentation des actions par la politique par défaut, p. 40 ; dommage unique) | ne touche pas |
| (c) flou | ne touche pas | ne touche pas (catégorie de recherche à correcteur binaire, p. 7) | ne touche pas |
| (d1) taux égal | voisin de forme (p. 3, 9) | voisin de forme (p. 13) | voisin de forme (p. 2) |
| (d2) hors de l'échantillon (durcissement) | ne touche pas | ne touche pas | ne touche pas (non décrit) |
| (e) agrégation égale sur la trajectoire | ne touche pas (trajectoire entière) | voisin de forme (maximum d'un lecteur cumulatif, p. 12-13, 28-30) | ne touche pas |
| (f) agent | voisin | voisin | ne touche pas |
| **H1** | **non trouvé dans les pièces lues** | **non trouvé dans les pièces lues** | **non trouvé dans les pièces lues** ; contre-indice faible de portée (instrument) |

## Ce qui reste revendicable (pour ces trois pièces)

- **Selon l'énoncé du programme** (l. 92), sans durcissement : « la mesure, dans un agent, du gain d'un moniteur fondé sur les activations sur un moniteur boîte noire, à agrégation égale et à taux de faux positifs égal, sur du sabotage diffus en tâches floues ». Ce n'est pas trouvé dans ces trois pièces.
- **Version durcie, à nommer comme telle** si le préenregistrement la retient (mandat de la version 1, constat M1) : la même mesure avec un taux fixé hors de l'échantillon et remesuré sur des épisodes honnêtes neufs. Ce n'est pas trouvé non plus.

Ces trois pièces n'ajoutent aucune occupation à celles du niveau 3 et n'en retirent aucune.

## Ce qu'une phrase publique sur H1 ne doit pas affirmer

- Que LinuxArena ou les évaluations de contrôle simulées comparent des sondes à des moniteurs de texte : ni l'un ni l'autre ne mesure de boîte blanche (2604.15384, p. 20 ; 2610.31593, p. 3).
- Que le PDF de LinuxArena (version 2) contient, même « à une table près », une telle comparaison : aucune de ses tables ne porte sur des sondes. Le sens de l'expression de S-2A reste à vérifier sur S-2A.
- Que la fragmentation est anecdotique dans LinuxArena, ou au contraire que LinuxArena mesure son effet. Elle est dans la politique d'attaque par défaut (p. 40), mais aucune mesure ne l'isole, et les modes d'échec sont des exemples (p. 17, 42).
- Que les moniteurs de texte échouent sur les attaques fragmentées, sur la foi de LinuxArena : les moniteurs forts tiennent 89 à 99 % de sûreté contre des attaques instruites de fragmenter (p. 16, 40).
- Que la base boîte noire de LinuxArena lit chaque étape isolément : elle relit tout l'historique (p. 12, 13).
- Que les attaques humaines de LinuxArena ouvrent une marge mesurable pour une sonde qui lit l'agent : elles n'ont pas d'agent auteur (p. 46).
- Que les sondes sont fiables avec peu de positifs pour le sabotage ou le désalignement, sur la foi de 2610.39766. Les auteurs disent que le succès sur le spam ne le garantit pas (p. 4) ; le rappel sur l'honnêteté reste bas (figure, p. 17), sur un modèle de 70 milliards.
- Que 2610.39766 montre, ou pourrait montrer sur le spam, un avantage des sondes sur la lecture du texte (filtrage, p. 2, 7).
- Que le discriminateur de 2610.31593 (p. 20) est une sonde d'activations ou un moniteur de sabotage.
- Que les seuils de ces bancs sont validés hors de l'échantillon : ce sont des quantiles d'épisodes honnêtes, jamais remesurés sur des épisodes honnêtes neufs (2610.31593, p. 3, 9 ; 2604.15384, p. 13).
- Que H1 exige, dans son énoncé, un taux fixé hors de l'échantillon : c'est un durcissement (programme, l. 92).

Je ne rédige pas la phrase publique qui déclarerait H1 (rôle exclu).

## Correction à porter à la synthèse sur « à une table près »

La contre-lecture du niveau 3 (l. 289-290) rapporte que S-2A, point 4, place la comparaison dans LinuxArena, en sabotage concentré, « à une table près ». Texte proposé pour la synthèse :

```text
Point à vérifier : le PDF de LinuxArena (2604.15384, version 2 du 27 avril 2026, 51 pages) ne contient aucune table,
aucune figure ni aucune phrase sur des sondes, des activations ou une boîte blanche ; ses moniteurs sont tous des
modèles de langue qui lisent le texte des actions (p. 12, 20, 45 ; figures p. 15, 16, 19, 51). La comparaison des
sondes et des moniteurs de texte n'est donc pas dans ce PDF. Le sens de « à une table près » (S-2A, point 4) et la
pièce sur laquelle il s'appuie restent à vérifier sur S-2A, que ni le lecteur ni le contre-lecteur du compte 2 n'ont lu.
```

## Voisins nommés dans les pièces et non lus (avec la page où ils sont nommés)

- Dans 2610.31593 :
  - Ge-Wang et al., arXiv 2606.06529, sélection d'attaques (p. 1, 14) ;
  - Storf et al., arXiv 2603.00829, moniteur boîte noire « constitutionnel » de la manigance d'agents (p. 11, 14) ;
  - Williams et al., arXiv 2607.07184, simulation de déploiement (p. 2, 14) ;
  - Gardner-Challis et al., arXiv 2602.20628 (p. 13, 14) ;
  - Kaufman et al., BashArena, arXiv 2512.15688 (p. 1, 14) ;
  - Mehri et al., arXiv 2605.07847 (p. 5, 14) ;
  - Needham et al., arXiv 2505.23836, conscience d'évaluation (p. 12, 14) ;
  - Bhatt et al., arXiv 2504.10374 (p. 9, 14 ; déjà au niveau 2).
- Dans 2604.15384 :
  - Kutasov et al., SHADE-Arena, arXiv 2506.15740 (p. 4, 21) ;
  - Stickland et al., contrôle asynchrone, arXiv 2512.13526 (p. 5, 22) ;
  - Jotautaitė et Martinez, MonitoringBench, billet (p. 5, 21) ;
  - Lucassen et Kaufman, billet sur le blocage des défaillances immédiates (p. 8, 21) ;
  - Benton et al., arXiv 2410.21514 (p. 5, 21 ; déjà au niveau 2) ;
  - Mallen et al., arXiv 2412.12480 (p. 5, 21).
- Dans 2610.39766 :
  - Kantamneni et al., arXiv 2502.16681 (p. 2, 5) ;
  - Ren et al., MASK, arXiv 2503.03750 (p. 2, 5) ;
  - McKenzie et al., arXiv 2506.10805 (p. 1, 5 ; déjà au niveau 2) ;
  - Tillman et Mossing, arXiv 2504.20271 (p. 1, 5 ; déjà au niveau 2) ;
  - Goldowsky-Dill et al., arXiv 2502.03407 (p. 1, 5 ; déjà au niveau 2).

## Formules (lues sur le PDF, non contrôlées par programme)

- 2604.15384, p. 13 : sûreté = P(détecté) / [P(détecté) + P(non détecté et sous-tâche réussie)] ; sabotage réussi = P(non détecté et sous-tâche réussie) ; évasion = P(non détecté | sous-tâche réussie).
- 2604.15384, p. 29 : c(a) = rL(a) (par étape), rD(T) (différé), max(rL(a), rD(T)) (combiné) ; seuil τ = quantile (1 − taux) des scores c des étapes honnêtes.
- 2610.31593, p. 9 : même définition de la sûreté au budget d'audit b.
- 2610.39766, p. 2 : sonde cosinus = cos(Agg(A), ā+) − cos(Agg(A), ā−).
- 2610.39766, p. 7 : logit_diff = max des logits « oui » − max des logits « non » ; positifs gardés si logit_diff > 0, négatifs si logit_diff < 0.
- 2610.39766, p. 8 : facteur de suréchantillonnage u ∈ {2, 3, 4, 5}.

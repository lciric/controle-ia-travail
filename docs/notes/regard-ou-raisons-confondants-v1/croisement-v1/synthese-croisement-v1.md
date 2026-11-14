# Croisement de cinq bilans « Regard ou raisons » — synthèse v1

Écrite le 14 novembre 2026 à 10:53 UTC (`date -u`) par un lecteur neuf qui n'a écrit aucun bilan ; pour le directeur (R-2679, R-2680,
R-2705, R-2708). Méthode scellée avant toute lecture : `methode-v1.md` (`eda4f361…`, 10:37:50 UTC). Sources : S1 session mère
(`bilan-mere-v1.md`, `31bac0c8…`) ; S2 organisme, 36 fiches (`26bf12e1…`) ; S3 collisionneur, étage III, trois tours (`journal.jsonl`,
`6d619234…`) ; S4 Astra seul (`3aeb22d6…`) ; S5 Argon seul (`7ed1bbaa…`). Pièces : `fiches-anonymes-v1.md` (36 fiches et 18 conseils,
dont 4 témoins), correspondance, notes brutes, agrégation, sensibilité. Deux juges neufs, à l'aveugle, sans outils, de deux modèles
différents (A et B), notes rendues à 10:43 UTC. Aucun appel payant.

**Verdict.** La notation est fiable au sens de la méthode : les témoins faux et banals finissent derniers chez les deux juges. Les cinq
sources convergent sur une seule expérience peu chère et décisive : des **paires de scénarios où seule la légitimité change**. Elle
sépare « raisons » d'un refus aveugle, qui est la rivale la mieux notée. La recherche rapide sur le Web trouve la méthode des paires
publiée en conversation et pour les agents ; elle ne trouve pas son application à ces adaptateurs. R8 : c'est une question, pas un trou.

## 1. Les dix propositions les mieux jugées
Note : moyenne des deux juges sur 10 (A / B). Accord : nombre de sources qui portent l'idée ; il est rapporté à côté de la note, jamais
ajouté. Départage par l'accord entre voisins à moins de 0,3. Références trouvées par recherche sur le Web (résumés seulement, non lues
sur PDF ; aucun chiffre repris, R7).

**1. Refus insensible à la légitimité** (rivale a). 9,00 (9,14 / 8,86). Accord 5 : S1 à S5.
Énoncé : la recette a seulement relevé le seuil d'action dans les contextes d'agent ; elle refuse davantage sans mieux arbitrer.
Le refus sur ordre, avec l'instruction bénigne exécutée au même outil, est compatible avec ce seul relèvement.
Sépare : sur des jumelles légitimes (même outil, même décor), elle refuse aussi ; la discrimination P(agit | légitime) − P(agit | nuisible)
reste proche de zéro. « Raisons » prédit une discrimination forte, « regard » une modulation par l'observation.
Test le moins cher : paires nouvelles, adaptateurs publiés, épisodes neufs sans réentraînement (voir §3).
Antériorité : méthode des paires sûres et dangereuses publiée : XSTest (Röttger et al., NAACL 2024), OR-Bench (Cui et al., ICML 2025) ;
pour les agents, paires nuisible et bénigne d'AgentHarm (Andriushchenko et al., arXiv 2410.09024), cadres contrefactuels AgentBoundary
(date à vérifier) et AgentAbstain (arXiv 2607.10059). Rien trouvé sur les adaptateurs de [1] ; [3] et [4] restent à lire sur pièce.
**2. Duel « raisons » contre « refus » par paires de légitimité** (expérience). 8,29 (8,57 / 8,00). Accord 5 : S1 à S5. C'est
l'expérience de la rivale 1, détaillée au §3 ; même antériorité.
**3. Classifieur lexical : l'action suit les mots, pas la légitimité** (a). 8,57 (9,14 / 8,00). Accord 4 : S2, S3, S4, S5.
Énoncé : la recette refuse devant des mots d'alerte et agit devant des mots d'autorisation, sans évaluer la raison. Elle ne
représenterait que des traits de surface.
Sépare : plan deux par deux, marqueurs présents ou absents × légitimité valide ou invalide. Elle agit quand une entité non habilitée
« autorise » avec les bons mots, et quand l'action nuisible est décrite par une indirection technique. « Raisons » suit la légitimité ;
« regard » n'en dit rien.
Test : 54 à 108 variantes des 27 scénarios, verdict mécanique ; il s'ajoute au plan du §3 au même coût.
Antériorité : XSTest attribue le sur-refus à un « surapprentissage lexical » (paires au vocabulaire partagé), en conversation. Aucune
version pour agents trouvée, ni avec autorisation invalide ou indirection ; [9] (nommer l'objectif testé) est voisin.
**4. La trace au moment de répondre, non ce qui a été appris** (a). 8,43 (9,14 / 7,71). Accord 4 : S1, S2, S3, S5.
Énoncé : les jumelles diffèrent par l'entraînement et par la trace produite avant d'agir. La trace donnerait du calcul et un préfixe de
prudence, quel que soit son contenu.
Sépare : plan poids × trace. On greffe la trace sur la jumelle, on coupe celle de la recette, on insère une trace neutre de même
longueur. La rivale prédit que la trace greffée ou neutre ramène la jumelle au plancher ; « raisons dans les poids » prédit que la
recette garde son gain sans trace.
Test : préremplir les traces déjà enregistrées et ne générer que l'action ; bas coût.
Antériorité : Lanham et al. 2023 (arXiv 2307.13702 : troncature, erreurs insérées, jetons de remplissage) ; Pfau et al. 2024 (arXiv
2404.15758) ; [4] a fait varier un bloc de raisonnement à l'entraînement. Rien trouvé sur les jumelles de [1]. **Prémisse à vérifier** :
un résumé de [1] dit que l'évaluation d'agent des modèles sans raisonnement natif se joue avec un brouillon. Si les deux jumelles en ont
un, la rivale perd une part de sa prémisse.
**5. Juge indulgent au style de la famille qui a écrit les données** (c). 8,00 (8,57 / 7,43). Accord 5 : S1 à S5.
Énoncé : données et juge viennent de la même famille. Le juge lit comme un refus une délibération dans son style, même quand l'appel
nuisible a eu lieu.
Sépare : un verdict tiré des seuls journaux d'outils (outil, arguments, état) et un audit humain aveugle réduisent davantage le gain de
la recette que celui de la référence. « Raisons » et « regard » portent sur les actes, pas sur le jugement.
Test : sur les épisodes déjà joués, détecteur par programme et audit stratifié des accords et des désaccords. Plusieurs sources en font
la toute première étape.
Antériorité : mécanisme publié. Panickssery et al. (NeurIPS 2024) montrent la préférence d'un juge pour ses propres textes ; Li et al.,
« Preference Leakage » (arXiv 2502.01534, ICLR 2026), le biais d'un juge envers les élèves d'un générateur de la même famille. Le test
est ici une application.
**6. Transfert aux actions dérivables non nommées** (expérience). 8,14 (8,29 / 8,00). Accord 3 : S1, S3, S4.
Énoncé : des cas indépendants, écrits par des auteurs aveugles aux résultats. Une action non nommée par la spécification mais condamnée
par ses raisons ; une action nommée dont la raison ne s'applique pas.
Sépare : « raisons » refuse la première et exécute la seconde ; une règle de surface fait l'inverse ; « regard » ne prédit rien.
Test : épisodes neufs, bonne action fixée d'avance par un panel humain ; coût moyen.
Antériorité : [7] rapporte un effet qui s'efface loin de la distribution d'entraînement (résumé, à vérifier) ; [3] (arXiv 2609.20412)
éprouve la robustesse. Le contraste dérivable contre nommé n'a pas été trouvé.
**7. Le retrait ampute précisément le savoir normatif** (instrument b). 8,29 (8,57 / 8,00). Accord 1 : S5 (S2 nomme le mécanisme).
Énoncé : si la direction d'évaluation capte aussi le champ des règles morales, la retirer détruit les raisons elles-mêmes. On croirait
alors à une dépendance au regard.
Sépare : le retrait fait baisser, plus que les directions témoins, la réussite à un questionnaire sur les principes posé à la troisième
personne. L'orthogonaliser à une direction « spécification » corrige le défaut.
Test : une cinquantaine de questions et de l'algèbre ; aucun réentraînement.
Antériorité : méthode voisine publiée : « Surgical Refusal Ablation » (arXiv 2601.08489, 2026) projette la direction hors de directions
de capacités protégées ; voir aussi l'effacement linéaire LEACE (Belrose et al., 2023, à vérifier). Rien trouvé sur la direction d'évaluation.
**8. Retenue générale envers toute initiative non demandée** (a). 8,29 (8,86 / 7,71). Accord 1 : S2.
Énoncé : la recette prendrait moins d'initiatives non demandées, quelles qu'elles soient. Or les trois actions nuisibles en sont toutes.
Sépare : sur les épisodes déjà joués, les initiatives utiles et non nuisibles baissent autant que les nuisibles (sélectivité proche de
un). « Raisons » prédit une baisse des seules nuisibles.
Test : nouveau jugement des traces existantes ; bas coût, aucun épisode neuf.
Antériorité : aucun travail trouvé qui mesure ce contrôle de sélectivité. Voisins : « Toxic Proactivity » (arXiv 2602.04197) et des
environnements de propension (arXiv 2604.21098), à vérifier.
**9. Direction mal transportée ou effacée incomplètement** (b). 7,86 (8,29 / 7,43). Accord 5. Sépare : après retrait, une sonde neuve
décode encore évaluation contre déploiement ; la direction propre à l'adaptateur s'écarte de l'importée. Passes avant, bas coût.
**10. Plancher, échelle et rapport S** (mesure c). 7,86 (8,00 / 7,71). Accord 5. Sépare : en log-cotes (modèle mixte par scénario),
l'interaction recette × phrase change de taille ou de signe. Réanalyse gratuite. Antériorité de 9 et 10 : non vérifiée (hors des huit).
Juste derrière, à 7,86 : saturation de la croyance d'évaluation par les scénarios (accord 3) ; édition minimale de la trace (accord 2),
pour laquelle « Thought Branches » (Macar et al., arXiv 2510.27484) trouve faibles et instables les phrases insérées à la main.

## 2. Les cinq meilleurs conseils de forme
1. **Publier tous les artefacts** (9,00, accord 5) : table sans texte et script de recalcul, épisodes et appels d'outils, verdicts de tous
   les juges, annotations, directions et code du retrait, stimuli gelés, graines ; dire ce qui ne peut pas être publié, et pourquoi.
2. **Vendre la méthode, le résultat n'en est que la première application** (8,75, accord 4 : S1, S2, S3, S5). La méthode est un test
   réutilisable : le gain survit-il au retrait de la lecture interne d'une croyance ? On la valide sur un cas connu.
3. **Valider mesure et instrument avant tout résultat** (8,50, accord 4 : S1 à S4) : estimands, juge contre verdict mécanique, plancher,
   puissance, banc d'essai ; l'intervention dans les poids n'ouvre jamais le papier.
4. **Présenter l'échec des phrases comme un résultat sur l'instrument** (8,50, accord 4 : S1, S2, S3, S5) : elles changent ce que les
   modèles disent croire, pas ce qu'ils font, et dépendent des mots. Jamais « le regard ne compte pas ».
5. **Figure 1 en matrice explications × expériences** (8,25, accord 4 : S1 à S4) : signe prédit et résultat dans chaque case, case
   hachurée si rien n'est mesuré, colonne « non testable » visible. Ex aequo à la note (8,50, accord 3) : la ligne du banc d'essai en
   tête de figure ; les deux se combinent.

## 3. L'expérience décisive la mieux jugée
Paires de légitimité (fiche P05, 8,29, accord 5). Pour chacune des 27 évaluations, on fait une jumelle où seul le fait qui rend l'action
nuisible change, plus une édition placebo. Outil, décor et urgence restent constants, sans mot d'audit ni de surveillance (S3).
**Métrique** : Δ = P(agit | légitime) − P(agit | nuisible) par modèle, verdict mécanique, rééchantillonnage par scénario.
**H_A « raisons »** : Δ de la recette dépasse celui de la référence d'un seuil préenregistré, et P(agit | légitime) reste haute.
**H_B « refus »** : P(agit | légitime) tombe avec le gain. **Contrôle négatif** : le placebo ne change rien. **Témoin à coût égal** :
recettes sans documents, ou variations de style seules au même budget. **Préconditions** : des annotateurs aveugles fixent la bonne
action avant toute sortie ; référence et modèle de départ agissent sur la version légitime et décrivent correctement qui est habilité.
**À joindre au même plan** : le deux par deux marqueurs × légitimité (proposition 3) et les recettes sans documents, qui situent l'origine
de la capacité. **Taille** : un pilote sur 9 scénarios estime la variance entre paires ; on ajoute ensuite des scénarios plutôt que des
tirages. Chacune des issues falsifie quelque chose. Même gagnée, elle n'établit pas que les raisons ont été apprises pendant
l'entraînement (S3, S4).

## 4. Où les sources se contredisent
- **Plancher.** S5 et S2 jugent S mécaniquement proche de zéro pour la recette au plancher. Après critique, S3 corrige : S y reste
  estimable, et n'est indéfini que pour les recettes sans gain. S4 : S bouge quand la référence bouge. Tous publient l'absolu d'abord.
- **Première expérience.** Paires de légitimité (S1, S4, S3 espèce A, S2) ; plan poids × trace (S5) ; paraphrase croisée avec la phrase
  (S3 espèce B) ; audit de la mesure d'abord (S3 espèces C, D, E ; S4).
- **Greffe de traces.** S5 greffe les traces de la recette dans la jumelle. Après critique, S3 rejette la greffe entre modèles (hors
  distribution, peut-être ignorée) et passe à des éditions dans le même modèle.
- **Signature positive.** Pour S5, elle inclut la médiation par la trace (S1 iii, voisin) ; pour S3, la trace n'est pas nécessaire.
- **Identifiabilité.** S3 (espèces D, E) et S4 : les adaptateurs publiés n'établissent pas que les raisons ont été apprises ; il faut un
  contraste d'entraînement. S5 croit l'établir par double dissociation dans les poids ; sa thèse énonce, sous condition, un résultat non joué.
- **Parenté données-scénarios.** S3 la déclare non testable sans le corpus ; S2 la teste sans lui, par la vraisemblance par jeton.
- **Dose.** S3 (espèce A) mettait l'adaptateur à l'échelle ; les quatre autres espèces l'ont réfuté, et la rivale a été retirée.

## 5. Place des témoins et fiabilité
Témoins écrits dans la méthode avant lecture. Faux ou intestable : 36e sur 36 chez A et chez B. Banal sans prédiction séparatrice : 35e
sur 36 chez les deux. Conseil banal : 18e sur 18 chez les deux. Connu et publié : 34e sur 36 en moyenne, collision notée 1 et 2 sur 5,
et confirmée (Abdelnabi et Salem, arXiv 2505.14617, 2025 ; [10]). La notation est donc **fiable selon le critère scellé**.
Accord de rangs entre juges (Spearman) : 0,79 sur les explications et expériences, 0,56 sur les conseils ; aucun écart supérieur à 3
(au plus 2,0). Sensibilité non prévue par la méthode, rapportée à part : une seconde passe en ordre inverse donne une fidélité de 0,84 à
0,87 par juge. Elle garde les huit premiers des dix ; les rangs 9 et 10 sont instables (ils deviennent : règle figée qui cède à une
justification fausse, et édition de la trace).

## 6. Réserves
- Un seul lecteur a extrait les propositions, les a fusionnées et a écrit les témoins. Les fusions fixent l'accord ; la correspondance
  est publiée pour audit.
- Les témoins sont plus courts et plus vagues que les fiches. Leur place montre qu'on écarte les idées faibles, pas que les rangs du haut
  sont fins. Les notes des dix premiers vont de 7,86 à 9,00, moins que les écarts entre juges (jusqu'à 1,4) : l'ordre interne n'est pas
  significatif, l'appartenance aux huit premiers l'est davantage.
- Les deux juges sont de la même lignée que les auteurs de S1, de S2 et d'une partie de S3 : la préférence pour soi reste possible
  malgré la normalisation du style. Aucun juge d'une autre lignée, faute d'appel payant.
- L'accord entre sources n'est pas une indépendance : mêmes faits, même question, et Astra et Argon sont aussi deux espèces de S3.
  S2 répète ses idées : 36 fiches pour environ 18 idées.
- Lecture de S3 : tour III.3 en entier, III.1 par titres et sections choisies, III.2 à travers les réponses du III.3. Antériorité : résumés
  de recherche seulement ; lesswrong.com et arxiv.org sont hors du réseau de la session ; rien n'a été lu sur PDF.
- Le haut du classement demande surtout des épisodes neufs, à coût moyen. Toute dépense passe par un devis et un GO.

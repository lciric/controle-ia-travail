# Rapport du lecteur — HC5, contre-mesures (papier C) — v1

- **Écrit le** 2026-11-13 à 22:58:53 UTC (relevé par date -u dans la commande d'écriture). Début du travail : 2026-11-13 à 22:51:41 UTC, relevé par date -u lors de la lecture des interdits communs.
- **Rôle** : lecteur. **Modèle** : modèle A.
- **Mandat** : verdict d'antériorité sur HC5 par lecture intégrale de deux PDF jamais lus (constat M9 de la contre-lecture du niveau 3).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` ; interdits communs v2 lus, tenus au plus strict.
- **PDF** (empreintes vérifiées contre les compagnons `.sha256`) :
  - `lot11/2601.04603v1.pdf` : `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` (17 pages) ;
  - `lot10/2608.11247v1.pdf` : `698fdcbd01ed6141535b76012d5aaced574691a8fba192f7e65020987e46f8f9` (17 pages).
- **Fichiers lus (et seulement eux)** :
  - `docs/programme-controle-ia-v2.md`, l. 85-125 et 190-215 ;
  - `docs/decisions/decision-N-005-N-006-v1.md`, l. 76-90 ;
  - `docs/decisions/decision-N-013-v1.md`, l. 56-68 ;
  - `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, l. 293-312 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, l. 432-448 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, l. 536-557 ;
  - la consigne commune et `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` en entier ;
  - les deux PDF.
- **Étendue lue** :
  - 2601.04603 : p. 1-17 ligne à ligne (bibliographie p. 11-13 parcourue par mots) ; figures 2 et 3 vues en image (p. 7-8) ; figures 4 à 6 par légende et texte seulement ;
  - 2608.11247 : p. 1-9 et 13-16 ligne à ligne ; p. 9 (colonne droite) à 12 et p. 17 (bibliographie, liste des modèles, licences) parcourues par mots ; figures non vues en image (coordonnées de la figure 5 lues au tableau 6).
- **Citations contrôlées par programme** : 47, échecs : 0 (avec et sans `-layout`, normalisation). Script testé sur un cas juste (succès) et trois cas altérés (trois échecs attendus et obtenus). JSON des citations dans l'archive.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé). Les formules sont lues sur le PDF et non contrôlées par programme.
- **Aucune ouverture fautive, aucun refus, aucune commande git, aucun réseau.** Aucun nom de modèle n'est écrit : les modèles des articles sont désignés par leur rôle.

## 1. Verdict d'ensemble

**HC5 — contre-mesures : « occupé en partie »** (table fermée).

- **2601.04603 occupe en partie le quorum par type d'accès et la mesure sous attaque.** Le système de production combine une **sonde linéaire qui lit les activations du modèle protégé lui-même**, c'est-à-dire le modèle qui produit la réponse jugée, et un **classifieur externe textuel** (un modèle de langue réglé finement) qui lit l'échange. La décision passe par une cascade, puis par une moyenne pondérée des logits. Le système a été éprouvé par plus de 1 700 heures d'équipe rouge humaine (p. 1, 2, 8, 9). La complémentarité des deux types d'accès est mesurée (p. 8, 9).
- **Rien n'y est fait pour le reste.** Pas de cadre de contrôle d'un agent adverse, pas de juges génératifs incités, pas d'attaques de corruption du jugement. Pas de règle de quorum à proprement parler, pas de matrice de transfert des attaques entre sondes et classifieurs, pas de paraphrase de confiance.
- **2608.11247 est seulement voisin de HC5.** Il apporte un contre-indice conceptuel indirect à la paraphrase de confiance, détaillé en section 4.
- **Correction à porter dans la synthèse du niveau 3 (l. 445-447).** La phrase « Le quorum de juges et de sondes qui lisent l'agent […] ne sont pas trouvés » ne tient plus sans réserve. Un ensemble publié réunit des classifieurs textuels et une sonde lisant le modèle producteur, sous attaque adaptative humaine. La différence avec HC5 tient au cadre et à la menace, non à la structure de l'ensemble.

## 2. Énoncé confronté (fichiers nommés, lignes lues)

HC5 d'après N-006 (l. 76-90) et N-013 (l. 56-68) :
- (a) **paraphrase de confiance** : un modèle de confiance paraphrase le contenu avant que le juge le lise, pour couper le canal rhétorique. Le niveau 3 (l. 440-442) ajoute un risque : la réécriture peut effacer l'indice qui protégeait le moniteur ;
- (b) **quorum hétérogène en type d'accès** : des juges génératifs **et** des sondes qui lisent l'agent ;
- (c) **matrice de transfert des attaques de corruption entre juges et sondes**, qui mesure l'efficacité du quorum ;
- (d) **mesure sous attaque** : les attaques de corruption sont celles de EC.1, soit cinq familles (flatterie et supplication, revendication d'autorité, approbations forgées, usurpation stylistique, ordres en bande ; programme l. 194).

Revendiqué selon N-006 : le quorum par type d'accès et la matrice. Le quorum entre familles de juges est déjà acquis.

## 3. 2601.04603v1 — « Constitutional Classifiers++ »

### 3.1 Ce que fait l'article

**Venue imprimée.** Prépublication arXiv, cs.CR, 8 janvier 2026 (p. 1). Aucune conférence n'est imprimée. Tous les auteurs appartiennent à un même laboratoire industriel (p. 1, note).

**Cadre.** Défense d'un modèle conversationnel contre le **débridage universel** (amener le modèle à répondre en détail à des questions dangereuses, chimiques, biologiques, radiologiques ou nucléaires). L'adversaire est **l'utilisateur**, pas le modèle. Le modèle protégé n'est ni l'adversaire ni l'auteur des attaques : c'est l'instrument que l'attaquant détourne.

**Les quatre systèmes comparés (tableau 1, p. 10 ; annexe A, p. 14)** :
1. génération précédente : un classifieur d'entrée et un classifieur de sortie seul ;
2. un **classifieur d'échange** unique, qui lit la sortie dans le contexte de l'entrée (p. 2-4) ;
3. une cascade à deux étages de classifieurs d'échange : un petit classifieur filtre tout le trafic et transmet les cas suspects à un plus gros (p. 4-5) ;
4. le **système de production** (p. 9) : une sonde linéaire, puis un ensemble sonde et classifieur externe.

**Ce que lit chaque membre (réponse à la question du mandat)** :
- **La sonde.** Linéaire, entraînée sur les activations **de toutes les couches concaténées** du **modèle protégé lui-même**, et non d'un encodeur séparé : « reuse representations already computed during model sampling » (p. 5). Pour la section 5, la figure 3 dit : « which is the protected model » (p. 8). Pour le système de production : « As such, the probe uses activations from that model. » (p. 9). Elle lit l'échange jeton par jeton (entrée puis sortie) pendant la génération, en flux.
  - Entraînement : lissage des logits par moyenne glissante sur 16 jetons et perte pondérée par une fonction exponentielle normalisée (p. 6-7).
  - Inférence : moyenne mobile exponentielle des logits (p. 6). C'est une agrégation de type moyenne sur les jetons, à noter au regard de l'interdit du programme pour les sondes de production, sans que ce soit un verdict d'antériorité.
- **Les classifieurs externes.** Des modèles de langue réglés finement en « Constitutional Classifiers », en deux tailles : petit, et très petit (environ un tiers) (p. 5, 8). Ce sont des **classifieurs d'échange** qui lisent l'entrée et la sortie, en texte. Ils rendent un score (logit), **pas un verdict raisonné** : ce ne sont pas des juges génératifs incités au sens de EC.1.

**Comment l'ensemble décide (cascade, moyenne, seuils)** :
- Section 5.3 (analyse sur données statiques, p. 8-9) :
  - moyenne pondérée des logits, avec un poids **optimisé par paire sur l'ensemble de test** : « is optimized per pair to minimize attack success rate on the test set » (p. 8) ;
  - poids égaux quasi optimaux pour l'ensemble sonde et classifieur : « for the classifier-probe ensembles, we find that equal weighting already is close to optimal » (p. 17) ;
  - cascade : « when the probe score exceeds a threshold, we route the exchange to the small external classifier and average their logits to make our final prediction » (p. 9).
- Système de production (p. 9) :
  - « When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » ;
  - puis « the final classification score is computed as a weighted combination of probe and classifier logits », avec les poids 0,55 pour la sonde et 0,45 pour le classifieur (auteurs, p. 9 ; formule lue sur le PDF, non contrôlée par programme) ;
  - la sonde transmet environ 5,5 % du trafic au second étage (auteurs, p. 9).
- Seuils : étalonnés pour 0,1 % de refus sur un corpus de conversations ordinaires en sections 3 à 5 (p. 4, 5, 7, 8). Pour le premier étage de la section 4, le seuil est réglé pour signaler presque tous les exemples d'équipe rouge internes (p. 5).
- Il n'y a **ni vote, ni règle « k parmi n »**, ni décision « ou » : c'est une **fusion par moyenne pondérée derrière une cascade**.

**Sous quelles attaques** :
- (i) Analyse statique (p. 7-9) : environ 7 000 échanges de débridage issus de l'équipe rouge humaine, produits par des membres dont les échanges n'ont jamais servi à l'entraînement (p. 7). Ces attaques ne sont **pas optimisées contre la sonde** ni contre l'ensemble étudié. L'attaque est comptée parée si le classifieur signale à un moment quelconque, ce qui « may underestimate the attack success rate » (p. 7, note 6).
- (ii) Équipe rouge humaine contre le système de production (p. 9) :
  - environ 1 736 heures et environ 198 000 tentatives (auteurs) ;
  - **accès boîte noire** par l'interface au modèle défendu : « We provide red-teamers with API access to the defended model. » (p. 15) ;
  - primes jusqu'à 35 000 dollars (p. 15) ;
  - les attaques sont des attaques d'**évasion du filtre** (reconstruction par fragments, obscurcissement des sorties : métaphores, substitutions ; p. 2-3) ;
  - aucune attaque en boîte blanche contre la sonde (obscurcissement d'activations) n'est rapportée.

**Résultats chiffrés (auteurs, tableau 1 p. 10 et texte)** :
- **Taux de découverte de vulnérabilités à haut risque**, pour mille requêtes :
  - génération précédente : 0,01871 (13 sur 695 000) ;
  - classifieur d'échange : 0,00885 (2 sur 226 000) ;
  - cascade : 0,00878 (5 sur 569 000) ;
  - production : 0,00505 (1 sur 198 000).
- **Surcoût de calcul** relatif à la génération précédente : 100, 150, 27,8 et 3,5 %.
- **Refus sur le trafic de production** : 0,073, 0,038, 0,036 et 0,050 %.
- **Analyse statique (lu sur la figure, p. 7-8)** :
  - taux de succès d'attaque : sonde seule environ 1,4 % (aussi imprimé p. 8) ; petit classifieur seul environ 1,1 % ; très petit classifieur environ 4,5 % ; ensemble sonde et petit classifieur environ 0,45 % ; ensemble des deux classifieurs environ 0,8 % ;
  - corrélation de rang de Spearman entre prédictions : paire de classifieurs environ 0,75 ; très petit classifieur et sonde environ 0,6 ; petit classifieur et sonde environ 0,57.
- **Phrase clé (p. 8)** : « Probes and external classifiers make more independent errors than pairs of external classifiers. »

### 3.2 Ce que l'article ne fait pas
- Pas de **contrôle d'un agent** : pas de tâche agentique, pas de sabotage. Le modèle lu par la sonde n'est **jamais l'adversaire** ni l'auteur des contenus d'attaque. Dans HC5, au contraire, la sonde lit l'agent qui écrit lui-même les attaques de corruption.
- Pas de **juges génératifs** incités : les membres textuels sont des classifieurs réglés finement.
- Pas d'**attaques de corruption du jugement** (flatterie, autorité, approbations forgées, usurpation, ordres en bande). Les attaques visent à faire passer un contenu dangereux sous le filtre.
- Pas de **matrice de transfert**. Aucune attaque n'est optimisée contre un membre puis évaluée contre l'autre, et l'équipe rouge vise le système entier. La seule mesure de co-défaillance est la corrélation de rang des prédictions sur un jeu statique (figure 3b, p. 8).
- Pas de **paraphrase de confiance**.
- Pas d'attaque en **boîte blanche** contre la sonde, ni d'attaque adaptative dirigée contre la sonde seule.

### 3.3 Limites reconnues, incohérences, réserves (règle R4)
**Limites reconnues par les auteurs :**
- note 3 (p. 5) : « expert-level red-teamers operating outside our bounty program were nonetheless able to discover universal jailbreaks for this system » ; il s'agit de la cascade de la section 4, et rien n'est dit pour le système de production ;
- note 6 (p. 7) : le taux de succès peut être sous-estimé ;
- p. 8 : la sonde signale davantage les requêtes scientifiques bénignes ;
- note 2 (p. 4) : les systèmes ne protègent pas le même modèle.

**Trop beau, faibles effectifs (calcul, intervalles exacts de Poisson à 95 %)** :
- production : 1 sur 198 000, intervalle [0,00013 ; 0,02814] pour mille ;
- cascade : 5 sur 569 000, intervalle [0,00285 ; 0,02051] ;
- classifieur d'échange : 2 sur 226 000, intervalle [0,00107 ; 0,03197] ;
- génération précédente : 13 sur 695 000, intervalle [0,00996 ; 0,03199].

Les trois derniers systèmes ne se distinguent pas statistiquement. Le classement « le plus robuste » repose sur **une seule** vulnérabilité.

**Campagnes non comparables :**
- quatre des huit questions cibles ont été remplacées (p. 15) ;
- le barème des primes a changé (p. 15) ;
- le modèle protégé diffère selon le système (p. 4, note 2) ;
- les auteurs l'admettent en partie (« Since different systems received varying levels of red-teaming effort », p. 4).

**Poids de l'ensemble.** Le poids est optimisé sur l'ensemble de test (p. 8). Le gain de l'ensemble statique est donc optimiste. La réserve est atténuée par l'annexe D (poids égaux quasi optimaux, p. 17, lu sur la figure non vue en image : légende et texte seulement).

**Sonde et protection différentes.** La sonde de la section 5 lit un autre modèle protégé que celle du système de production (p. 7 contre p. 9). L'analyse statique ne valide donc pas directement la sonde de production.

**Incohérences mineures :**
- « The first-layer probe escalated approximately 5.5% » (p. 9) : il s'agit vraisemblablement du premier étage, pas de la première couche ;
- « detection rate of 0.005 per thousand queries » (p. 9) désigne le taux de découverte de vulnérabilités ;
- 5 sur 569 000 donne 0,00879 (calcul) contre 0,00878 imprimé (p. 5, tableau 1). L'écart vient de l'arrondi du nombre de requêtes et n'est pas opposable ;
- le résumé annonce des taux de refus « dramatically reduced » par rapport à la génération précédente. C'est vrai contre l'ancienne publication et contre la génération précédente réimplémentée (0,073 contre 0,050 %), mais le système de production refuse **plus** que ceux des sections 3 et 4 (0,050 contre 0,038 et 0,036 %, tableau 1).

### 3.4 Verdicts par composante (2601.04603)

| composante | verdict | fait | non fait | pages |
|---|---|---|---|---|
| (a) paraphrase de confiance | **voisin, contre-indice indirect** | une sortie lue **hors de son contexte** est contournée par obscurcissement ; le contexte rend la détection : « coded language, metaphors, and substitutions can evade an output-only classifier but are more readily identified when evaluated alongside their input context » (p. 4) ; « Obfuscation attacks exploit the output classifier’s inability to interpret context-dependent transformations. » (p. 3). C'est cohérent avec le risque, noté au niveau 3, qu'une réécriture efface l'indice | aucune paraphrase ; aucun modèle de confiance intercalé ; rien sur le canal rhétorique | 2, 3, 4 |
| (b) quorum par type d'accès (juges et sondes lisant l'agent) | **occupée en partie** | ensemble d'un **classifieur textuel externe** et d'une **sonde lisant le modèle qui produit la réponse**, conçu parce que la sonde capte des signaux complémentaires (« probes appear to capture complementary signals to external fine-tuned classifiers », p. 2) ; décision par cascade et moyenne pondérée ; déployé en production fantôme | modèle lu **non adverse** (débridage par l'utilisateur, pas de contrôle d'agent) ; membres textuels réglés finement, **pas des juges génératifs** ; **pas de règle de quorum** (fusion par moyenne) ; pas d'attaques de corruption | 1, 2, 5, 8, 9 |
| (c) matrice de transfert juges ↔ sondes | **voisin** | corrélation de rang des prédictions entre sonde et classifieurs sur un jeu de débridages (figure 3b, p. 8), qui mesure la co-erreur sous attaque statique | aucune attaque optimisée contre un membre puis portée sur l'autre ; aucune cellule de transfert ; aucune attaque de corruption | 8, 9 |
| (d) mesure sous attaque | **occupée en partie** (pour l'ensemble sondes et classifieurs) | plus de 1 700 heures d'équipe rouge humaine adaptative, en boîte noire, contre l'ensemble de production (p. 1, 9, 15) | attaques d'évasion par l'utilisateur, pas de corruption écrite par l'agent ; ni boîte blanche ni attaque ciblée sur la sonde ; résultat à n = 1 | 1, 9, 15 |

**Verdict pour l'article : « occupé en partie »** (composantes b et d au sens structurel ; a et c non faites).

**Pesée sans complaisance de la différence « lit un agent de contrôle » contre « filtre un modèle conversationnel ».**
- **Ce qui rapproche.** Dans les deux cas, la sonde lit le modèle **qui produit** le texte jugé. Elle est jointe à un lecteur textuel parce que l'état interne porte ce que le texte cache : l'obscurcissement chez eux, la rhétorique ou le sabotage dans HC5. La justification de l'hétérogénéité par type d'accès (« more independent errors », p. 8) est la même que celle de HC5. L'idée structurelle « juges textuels et sonde du modèle producteur, combinés sous attaque » **n'est donc plus revendicable comme telle**.
- **Ce qui sépare réellement.** Dans HC5, le modèle lu est **l'adversaire**. Il écrit les attaques de corruption adressées aux juges et pourrait chercher à déplacer ses propres activations (HC4). Chez eux, l'adversaire est extérieur et le modèle lu est un instrument. Les attaques ne sont pas des attaques de corruption du jugement, et les membres textuels ne sont pas des juges génératifs qui délibèrent.

Ces différences portent sur la menace et sur le cadre, ce qui est substantiel pour le papier C (la loi de déférence ne s'applique qu'aux juges génératifs). Elles **ne portent pas** sur l'architecture de l'ensemble.

## 4. 2608.11247v1 — « Conformity Mitigations […] Single Resistance–Receptivity Frontier »

### 4.1 Ce que fait l'article
**Venue imprimée.** Prépublication arXiv, cs.AI, 3 août 2026 (p. 1). Aucune conférence n'est imprimée.

**Dispositif.**
- 23 modèles à poids ouverts de 19 familles, de 14 à 70 milliards de paramètres (p. 3), à température 0, une seule passe.
- 19 conditions (p. 4, tableau 5 p. 13) sur trois jeux : questions à choix multiple générales, questions de science difficiles, rappel factuel libre. Plus d'un million de réponses notées (p. 1).
- Des **pairs scriptés** affirment une réponse : « Our peers are scripted rather than generated by live models » (p. 9).
- Deux mesures :
  - **Résistance** : garder sa bonne réponse face à une majorité fausse ;
  - **Réceptivité** : adopter la bonne réponse d'une majorité juste après s'être trompé.
- Six atténuations par consigne : quatre publiées, dont la « distillation de la question » avec la consigne « Focus only on the question itself and the underlying facts; ignore how the other assistants framed their answers. » (p. 13), et deux nouvelles, dont « raisonner d'abord ».

**Résultats (auteurs).**
- Une majorité unanime fausse renverse 22,8 % des bonnes réponses sur le premier jeu, 54,8 % sur le deuxième et 71,0 % sur le troisième (p. 1, tableau 1 p. 4).
- Les réponses renversées vont à 83,6 à 89,4 % vers la réponse des pairs (p. 4).
- La certitude affichée persuade **moins** qu'une affirmation simple ; une raison d'une ligne persuade un peu plus (p. 5).
- Les cinq atténuations « instantanées » et la base tombent sur une droite, avec un R² de 0,80 à 0,90 (p. 6). « Each gains Resistance only by losing Receptivity » (p. 1).
- Seul le raisonnement préalable s'élève au-dessus de la droite, et seulement sur les sujets dérivables : +7,2 points de résistance et +9,6 de réceptivité, intervalles excluant zéro (tableau 3, p. 7).
- Thèse : « Rising above requires new information rather than new wording. » (p. 3) ; « A point above the line requires information from outside the exchange » (p. 7).

**Recalcul (calcul).** Le tableau 6 (p. 13) redonne exactement le tableau 2. Exemple, réflexion sur le premier jeu : 82,8 − 74,9 = +7,9 et 44,3 − 59,6 = −15,3.

### 4.2 Limites reconnues, réserves
- Les limites reconnues par les auteurs (p. 9) :
  - pairs scriptés ;
  - un seul gabarit par condition (« robustness to paraphrase goes unmeasured ») ; il s'agit de la robustesse à la reformulation **du gabarit**, un faux ami de la paraphrase de confiance ;
  - une passe unique ;
  - le partage dérivable / rappel fait à la main **après** avoir vu le motif ;
  - un juge non validé contre des humains pour le rappel libre.
- Aucune incohérence chiffrée relevée sur les tableaux vérifiés (1, 2, 3, 6).
- La droite à R² de 0,8 à 0,9 repose sur six points par jeu (p. 4). C'est une réserve de taille d'échantillon, sous la règle R4.

### 4.3 Verdicts par composante (2608.11247)

| composante | verdict | appui | pages |
|---|---|---|---|
| (a) paraphrase de confiance | **voisin ; contre-indice conceptuel indirect** | une consigne d'ignorer le cadrage des autres (« distillation de la question ») n'élève pas au-dessus de la frontière : toute intervention qui ne fait que repondérer sans apporter d'information déplace sur la droite (« A confident wrong peer and a confident right one look identical inside the exchange, so any lean the prompt induces applies to both. », p. 7). Transposé au contrôle (non testé), une paraphrase qui ôte la rhétorique pourrait ôter aussi l'argument légitime. Aucun modèle de confiance ne réécrit quoi que ce soit, et aucun moniteur n'est en jeu | 3, 7, 13 |
| (b) quorum par type d'accès | **voisin** | un membre d'un groupe qui voit le verdict des autres se conforme : « A single miscalibrated agent can, therefore, pull a whole group off a correct answer » (p. 1) ; un dissident n'aide que s'il dit juste (p. 8). L'argument « information from outside the exchange » (p. 7) plaide en principe pour un membre d'un autre type d'accès, mais rien n'est testé : ni moniteurs, ni sondes, ni quorum de décision | 1, 5, 7, 8 |
| (c) matrice de transfert | **ne touche pas** | — | — |
| (d) mesure sous attaque | **ne touche pas** | pression scriptée fixe, non optimisée, portée sur des répondants et non sur des moniteurs | 9 |

**Verdict pour l'article : « voisin »** (« ne touche pas » pour la matrice et pour la mesure sous attaque).

### 4.4 Note à part sur HC6 (sans verdict ; un autre lecteur s'en charge)
- L'article mesure un **déplacement sous pression bénigne fixe**, analogue d'un g par modèle (la part de réponses déplacées vers la valeur affirmée), sur 23 modèles. Il **ne mesure aucune attaque optimisée**. Il ne dit donc rien directement de « le g bénin prédit l'effondrement sous attaque optimisée ».
- Deux faits concernent le critère de recette de HC6 :
  - la résistance **n'est pas un trait fixe d'un jeu à l'autre** : « so steadiness on one benchmark guaranties nothing on another » (p. 5 ; corrélations de rang 0,97, 0,74 et 0,65, auteurs) ;
  - le déplacement suit la **compétence** et non la taille : « Conformity decreases as baseline accuracy increases » (p. 5 ; r = −0,64 sur le premier jeu, auteurs).
- Pour HC1 et EC.1 (signalé, sans verdict) : la certitude affichée persuade moins qu'une affirmation simple (p. 5), et le nombre de pairs domine l'emphase (p. 4). C'est la famille « approbations forgées » en version pairs.

## 5. Ce qui reste revendicable (formulation exacte)

« Dans le contrôle d'un agent non fiable, réunir en quorum des **juges génératifs** et des **sondes qui lisent l'agent lui-même**, auteur des attaques de corruption du jugement. Mesurer la **matrice de transfert de ces attaques de corruption** entre juges et sondes, cellule par cellule et dans chaque sens (attaque optimisée contre un juge portée sur une sonde, et l'inverse). Mesurer l'effet de la **paraphrase de confiance** sur cette matrice. »

Ces éléments ne sont pas trouvés dans les deux pièces lues. L'ensemble « classifieurs textuels et sonde du modèle producteur, sous équipe rouge humaine » est publié pour la défense contre le débridage (2601.04603). L'originalité doit donc porter sur le **cadre adverse** (le modèle lu est l'attaquant), sur la **nature des attaques** (corruption du jugement), sur la **matrice** et sur la **paraphrase**, et non sur l'idée d'hétérogénéité par type d'accès.

## 6. Ce qu'une phrase publique sur HC5 ne doit pas affirmer
- Qu'aucun ensemble de sondes internes et de classifieurs textuels n'a été publié ni éprouvé sous attaque adverse (contre 2601.04603, p. 1, 2, 8, 9).
- Que la complémentarité des erreurs entre sondes et lecteurs textuels est un résultat nouveau (2601.04603, p. 8 : « more independent errors »).
- Que le quorum par type d'accès est nouveau sans préciser « dans le contrôle d'un agent adverse, avec des juges génératifs et des attaques de corruption du jugement ».
- Que la paraphrase de confiance est appuyée par les pièces lues. Elles donnent au contraire deux indices indirects qu'une réécriture ou un retrait du contexte peut effacer ce qui protégeait le lecteur (2601.04603, p. 3-4), et qu'une intervention sans information nouvelle déplace le long d'un compromis sans améliorer la discrimination (2608.11247, p. 3, 7).
- Les chiffres de robustesse de 2601.04603 comme comparaison opposable entre systèmes (une seule vulnérabilité, campagnes différentes).
- Que 2608.11247 teste des moniteurs, une paraphrase ou un quorum : ce n'est pas le cas.

## 7. Voisins nommés dans les pièces et non lus
- 2601.04603 :
  - Hua et al. 2025, « Combining cost-constrained runtime monitors for AI safety », arXiv 2507.15886 (nommé p. 10, référence p. 12) : combinaison de moniteurs sous contrainte de coût. **Le plus proche du quorum ; à lire en priorité.**
  - McKenzie et al. 2025, « Detecting high-stakes interactions with activation probes », arXiv 2506.10805 (p. 10, 12) : sondes et cascades de classifieurs.
  - Cunningham et al. 2025, billet « Cost-effective constitutional classifiers via representation re-use » (p. 10, 12).
  - Sharma et al. 2025, arXiv 2501.18837 (p. 1, 13).
  - Youstra et al. 2025, arXiv 2508.17158 (p. 5, 13).
  - Zou et al. 2024, coupe-circuits, arXiv 2406.04313 (p. 10, 13).
  - Casper et al. 2024, entraînement adverse latent, arXiv 2403.05030 (p. 10, 12).
- 2608.11247 :
  - Zhu et al. 2025 (ACL) et Weng et al. 2025 (ICLR), conformité et premières atténuations (p. 2, 11) ;
  - Baltaji et al. 2024 (p. 2, 9) ;
  - Khan et al. 2024, débat et juges non experts (p. 2-3, 10) ;
  - Wan et al. 2024, « What evidence do language models find convincing? » (p. 3, 11) ;
  - Turpin et al. 2023 (p. 3, 11).

## 8. Note pour H5 (papier B), sans verdict
La figure 3b de 2601.04603 (p. 8) mesure la diversité effective entre types de moniteurs par corrélation de rang des prédictions sous attaque statique. La paire sonde et classifieur est moins corrélée que la paire de classifieurs. C'est voisin de « nombre × diversité des moniteurs, mesurée par une matrice de transfert ». À signaler au lecteur de H5.

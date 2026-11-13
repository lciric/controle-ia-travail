# Contre-lecture du rapport du lecteur — HC5, contre-mesures (papier C) — v1

- **Écrite le** 2026-11-13 à 23:09:55 UTC (relevé par date -u dans la commande d'écriture). Début du travail : 2026-11-13 à 23:01:15 UTC (relevé par date -u à la création du dossier de travail).
- **Rôle** : contre-lecteur (rôle adverse). **Modèle** : modèle B. L'auteur du rapport est le modèle A ; A ≠ B.
- **Objet** : `rapport-HC5-v1.md`, empreinte vérifiée `10b861094910ab7267276e424f0af78811a172157d167e45446baed67823d96b` ; son archive `fichiers-de-travail-HC5-v1.tar`, empreinte vérifiée `81ca45569045a42de489ab360bb87350e282f79a6d02676b5db703007130b32a`.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, lue en entier.
- **PDF** (empreintes vérifiées contre les compagnons `.sha256`) :
  - `lot11/2601.04603v1.pdf` : `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` (17 pages) ;
  - `lot10/2608.11247v1.pdf` : `698fdcbd01ed6141535b76012d5aaced574691a8fba192f7e65020987e46f8f9` (17 pages).
- **Fichiers lus (et seulement eux)** :
  - la consigne commune ; le rapport du lecteur ; le contenu de son archive (journal, scripts, sorties, fichier des citations) ;
  - `docs/programme-controle-ia-v2.md`, l. 85-125 et 190-215 ;
  - `docs/decisions/decision-N-005-N-006-v1.md`, l. 76-90 ;
  - `docs/decisions/decision-N-013-v1.md`, l. 56-68 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, l. 432-448 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, l. 536-557 ;
  - les deux PDF. Aucun autre PDF.
- **Étendue lue** :
  - 2601.04603 : p. 1-17 ligne à ligne, bibliographie comprise ; p. 7, 8, 14, 15, 16, 17 vues en image (figures 2 à 6) ;
  - 2608.11247 : p. 1-17 ligne à ligne, annexes et tableaux 4 à 13 compris ; p. 7 vue en image (figure 5) ; figures 1 à 4 et 6 à 8 par légende et texte seulement.
- **Citations contrôlées par programme** : 56, échecs : 0 (avec et sans `-layout`, normalisation). Script testé sur un cas juste (succès) et trois cas altérés (trois échecs attendus et obtenus). Fichier `citations-contre-lecture-HC5-v1.json` dans l'archive, empreinte `3ffc365fbf91c39920e8059e0fe1e65a2f92d0762645a775d44be63c83ccc032`. Les 47 citations du lecteur, repassées par mon script : 0 échec.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les formules sont lues sur le PDF, non contrôlées par programme.
- **Aucune ouverture fautive, aucun refus, aucune commande git, aucun réseau, aucun appel de modèle.** Aucun nom de modèle n'est écrit : les modèles des articles sont désignés par leur rôle.

## 1. Verdicts

- **Verdict sur le rapport : « tient avec corrections ».** Aucun constat bloquant. Six constats majeurs (A, B, C, D, F, G), trois mineurs (E, H, I).
- **Mon verdict sur HC5, table fermée : « occupé en partie ».** Même valeur que le lecteur.
- **Ce qui est occupé (2601.04603).** L'idée d'ensemble « un lecteur textuel externe et une sonde qui lit le modèle producteur, combinés et éprouvés par une équipe rouge humaine » est publiée, pour la défense d'un modèle conversationnel contre le débridage. Le lecteur a raison : cette idée n'est plus revendicable comme telle.
- **Ce qui ne l'est pas, dans les deux pièces.** Le quorum de juges génératifs et de sondes lisant un agent adverse ; la matrice de transfert des attaques de corruption entre juges et sondes ; la paraphrase de confiance. « Non trouvé dans les pièces lues », jamais « trou du champ » : deux voisins nommés par la pièce elle-même restent à lire avant toute phrase (constat G).
- **Sens des corrections.** Le rapport est exact sur les faits que j'ai revérifiés. Il est **trop fort** sur un point (la composante « mesure sous attaque » dite occupée en partie, constat B) et sur une attribution (« complémentarité des deux types d'accès », constat C). Il est **trop faible** sur trois points : la cascade est en série et la sonde décide seule de presque tout le trafic (constat A) ; la réserve statistique est plus lourde qu'écrit (constat D) ; le contre-indice le plus direct contre la paraphrase de confiance n'a pas été relevé (constat F).

## 2. Jugement de profondeur (demandé en priorité)

**Jugement : lecture suffisante pour le verdict d'ensemble, insuffisante pour la portée de trois composantes.**

Ce qui plaide pour une lecture réelle :
- les 47 citations du lecteur repassent sans échec par mon script, écrit sans reprendre le sien (empreinte de son fichier : `3417ec306956501c72dbaa6006db6e7235e3098464546e7025047a048d61ba75`) ;
- les valeurs lues sur les figures 2 et 3 (p. 7 et 8) sont justes à la précision de lecture : je les ai relues sur l'image ;
- les quatre intervalles de Poisson sont justes à cinq décimales (section 6) ;
- le rapport relève des détails qu'une lecture par mots ne donne pas : l'écart d'arrondi 0,00878 contre 0,00879, « first-layer » pour « first-stage » (p. 9), la note 3 (p. 5), le changement de modèle protégé entre la section 5 et la section 6.

Ce qui manque (la durée n'est pas la preuve : ma propre contre-lecture a pris neuf minutes d'horloge ; je juge sur le contenu) :
- **les figures 4, 5 et 6 de 2601.04603 n'ont pas été vues** (le journal le dit). La figure 5 porte une incohérence d'unité (constat E) et la figure 6 est l'appui de l'atténuation d'une réserve ;
- **aucune figure de 2608.11247 n'a été vue**, et les pages 9 (colonne droite) à 12 et 17 ont été « parcourues par mots » ;
- **les conséquences ne sont pas tirées** : la phrase « Otherwise, we rely solely on the probe. » (p. 9) est sur une page que le lecteur cite cinq fois, et n'apparaît pas dans le rapport ; les chiffres « certain » contre « nu » du tableau 1 de 2608.11247 sont cités dans la note sur HC1 et ne sont pas rapprochés de la paraphrase ; la phrase de la p. 10 sur McKenzie et collègues est sur la page citée pour Hua et collègues ;
- le journal ne donne aucune heure par étape. La lecture « ligne à ligne » de 34 pages, les scripts et 25 000 caractères de rapport tiennent entre 22:51:41 et 22:58:53. Je ne peux pas vérifier l'étendue déclarée ; je constate seulement que le texte a été extrait et exploité avec exactitude.

Le lecteur a ouvert deux fichiers que mon mandat ne nomme pas (`docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, l. 293-312, et les interdits communs v2). Je ne les ai pas ouverts et je ne juge pas ce point.

## 3. Ce que j'ai relu et cherché

- **2601.04603v1** : les 17 pages lues ligne à ligne par `pdftotext -layout`, bibliographie comprise (p. 11-13) ; pages 7, 8, 14, 15, 16 et 17 vues en image (figures 2, 3, 4, 5, 6).
- **2608.11247v1** : les 17 pages lues ligne à ligne par `pdftotext` (ordre de lecture pour les pages 1 à 12, `-layout` pour les pages 13 à 17, tableaux 5 à 13 compris) ; page 7 vue en image (figure 5, tableaux 2 et 3). Figures 1 à 4, 6 à 8 : légendes et texte seulement.
- **Recherche active des composantes dites non trouvées**, sur le texte aplati des 17 pages de 2601.04603, par mots : « transfer », « white-box », « gradient », « adaptive », « paraphras », « rephras », « rewrit », « untrusted », « agent », « quorum », « vote », « voting », « majority », « independent », « complement », « correlat ».
  - « transfer » : **aucune occurrence** dans les 17 pages.
  - « adaptive » : occurrences aux p. 5, 10 et 12 seulement, toutes au sens du calcul adaptatif ou dans un titre de bibliographie, **jamais au sens d'une attaque**.
  - « gradient » : gradients de l'entraînement de la sonde seulement (p. 6, 16).
  - « agent » : un titre de bibliographie (p. 13).
  - « paraphras », « rephras », « rewrit », « untrusted », « quorum », « vote », « white-box » : aucune occurrence.

## 4. Réponses aux cinq points du mandat

### Point 1 — L'occupation en partie par 2601.04603 : trop forte, juste, trop faible ?

**Pour le quorum par type d'accès (composante b) : juste, à condition d'écrire que l'ensemble éprouvé est une cascade en série (constat A).**

Pesée du cadre, dans les deux sens :

- **La collision est-elle sous-estimée ?** Sur l'architecture, non : le lecteur écrit déjà que l'idée structurelle « n'est plus revendicable comme telle », ce qui est la lecture la plus sévère que les pages permettent. La marque que la décision N-013 (l. 63) utilisait pour écarter 2603.13791 — une sonde « qui lit un encodeur séparé, jamais l'agent » — ne joue pas ici : la sonde lit le modèle producteur (« reuse representations already computed during model sampling », p. 5 ; « As such, the probe uses activations from that model. », p. 9). Le cadre mis à part, l'architecture et l'épreuve par équipe rouge occupent donc bien la composante. Sur un point voisin, hors de HC5, la collision est en revanche **non signalée** : la campagne de 1 736 heures est, de fait, une attaque par contenu, en boîte noire, contre un système dont la sonde est le premier étage et décide seule d'environ 94,5 % du trafic (calcul, d'après le 5,5 % imprimé p. 9). Cela regarde HC2 (sonde sous attaque par contenu en boîte noire, programme l. 103) et HC4. Je le signale sans verdict : ces énoncés ne sont pas de mon mandat.
- **La collision est-elle surestimée ?** Sur trois points, oui.
  1. Ce qui a été éprouvé sous équipe rouge n'est pas un quorum où chaque membre lit tout. Le classifieur textuel ne voit que ce que la sonde lui envoie (constat A). Une attaque qui tient le score de la sonde sous le seuil d'escalade passe sans que le lecteur textuel soit consulté. La robustesse du système à l'évasion est bornée par celle de la sonde ; l'hétérogénéité sert ici le coût, pas la résistance à la corruption d'un membre.
  2. La fusion où chaque membre lit tout (moyenne pondérée des logits) n'est mesurée que sur un jeu statique (figure 3a, p. 8), avec une sonde qui lit un autre modèle que celui de la production.
  3. La composante « mesure sous attaque » est dite « occupée en partie » alors que le rapport la définit lui-même par les cinq familles d'attaques de corruption, dont aucune n'est mesurée (constat B).

### Point 2 — « Matrice de transfert : voisin »

**Juste. Aucun transfert n'est mesuré, annexes comprises.**
- Le mot « transfer » ne figure nulle part dans les 17 pages. Aucune attaque n'est optimisée contre un membre puis portée sur l'autre ; aucune attaque ne vise la sonde seule ; l'équipe rouge a un accès en boîte noire au système entier (« We provide red-teamers with API access to the defended model. », p. 15). Les annexes A à F ne contiennent aucune cellule de transfert (vues en image, p. 14 à 17).
- Ce qui s'en approche le plus, et que le rapport peut dire plus nettement :
  - la figure 3b (p. 8), corrélation de rang des scores entre membres : c'est une mesure de co-variation, pas de transfert (constat C) ;
  - les figures 2a et 3a (p. 7 et 8) : un même jeu d'attaques humaines, **collectées contre des systèmes que l'article ne nomme pas**, rejoué sur la sonde, sur chaque classifieur et sur les ensembles. C'est une ligne « attaques venues d'ailleurs, portées sur chaque membre », sans source identifiée par membre. Cela ne fait pas une matrice.

### Point 3 — La paraphrase de confiance et le contre-indice tiré de 2608.11247

**L'étiquette « voisin ; contre-indice conceptuel indirect » est juste. La portée écrite en section 6 du rapport est trop large, et le contre-indice le plus direct de la pièce n'a pas été relevé (constat F).**

### Point 4 — Les réserves R4 et le recalcul

**Les trois réserves tiennent. La première est plus lourde qu'écrit (constat D).** Recalcul en section 6.

### Point 5 — Phrase publique, voisins non lus

**La liste du lecteur est juste et incomplète (constat G).** Compléments en section 8.

## 5. Constats

### A — majeur — La cascade est en série : la sonde décide seule de presque tout le trafic

- **Pages** : 2601.04603, p. 2 et 9.
- **Citations** : « Otherwise, we rely solely on the probe. » (p. 9, section 5.3) ; « When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » (p. 9, section 6) ; « For escalated exchanges, the final classification score is computed as a weighted combination of probe and classifier logits » (p. 9) ; « The first-layer probe escalated approximately 5.5% of traffic to the second-stage classifier. » (p. 9) ; « The system employs a weighted two-stage cascade, using a linear probe as the first stage and a probe-external classifier ensemble as the second stage. » (p. 2).
- **Constat.** Le rapport écrit bien « fusion par moyenne pondérée derrière une cascade » et « pas de règle de quorum ». Il ne tire pas la conséquence. Le refus exige deux conditions à la suite : que la sonde dépasse le seuil d'escalade, puis que le score fusionné dépasse le seuil de refus. Le lecteur textuel n'est jamais consulté sur les quelque 94,5 % du trafic que la sonde n'escalade pas (calcul). La règle « sinon, la sonde seule » est explicite pour l'analyse statique (section 5.3) ; pour la production, l'article décrit l'escalade et ne dit rien d'autre du trafic non escaladé.
- **Portée pour HC5.** Un quorum par type d'accès est revendiqué pour qu'une attaque qui corrompt un membre ne suffise pas. La cascade publiée fait l'inverse sur ce point : faire taire la sonde suffit. La section 1 du rapport (« Le système a été éprouvé […] La complémentarité des deux types d'accès est mesurée ») laisse croire qu'un quorum a été éprouvé sous attaque.
- **Texte corrigé proposé** (section 1, premier alinéa, à la place de « La décision passe par une cascade, puis par une moyenne pondérée des logits. ») :
  > « La décision est une cascade en série : la sonde lit tout le trafic et décide seule d'environ 94,5 % des échanges (calcul, d'après le 5,5 % d'escalade imprimé p. 9) ; le classifieur textuel ne lit que les échanges escaladés, où les deux logits sont moyennés (poids 0,55 et 0,45, p. 9). Une attaque qui tient la sonde sous le seuil d'escalade n'est jamais lue par le classifieur. Ce n'est pas un quorum où chaque membre lit tout : la fusion de ce type n'est mesurée que sur un jeu statique (figure 3a, p. 8). »

### B — majeur — « Mesure sous attaque : occupée en partie » contredit la définition que le rapport donne de cette composante

- **Pages** : rapport, section 2 (d) et section 3.4, ligne (d) ; 2601.04603, p. 5, 10, 15.
- **Citations** : « We provide red-teamers with API access to the defended model. » (p. 15) ; « In contrast, we implement a straightforward two-stage classification scheme and validate its robustness through extensive human red-teaming. » (p. 10).
- **Constat.**
  1. La section 2 du rapport définit (d) par « les attaques de corruption […] de EC.1, soit cinq familles ». Aucune n'est mesurée dans l'article ; le rapport le dit lui-même en 3.2. Selon sa propre définition, (d) n'est donc pas « occupée en partie » : elle est « voisin ». Dans l'énoncé retenu (N-006, l. 83-85 ; N-013, l. 58-61), la mesure sous attaque **est** la matrice de transfert ; il n'y a pas de quatrième composante.
  2. Le fait à garder — un ensemble de sonde et de classifieur éprouvé par 1 736 heures d'équipe rouge humaine — est un attribut de la composante (b), et il y est déjà.
  3. « Équipe rouge humaine adaptative » est le mot du lecteur. L'article n'emploie « adaptive » que pour le calcul (p. 5, 10). Les attaquants itèrent par l'interface, en boîte noire ; rien ne dit qu'ils savaient qu'une sonde existait, ni qu'une attaque ait visé un membre.
- **Texte corrigé proposé** (tableau 3.4) :
  > « (b) quorum par type d'accès — **occupée en partie** — fait : ensemble d'un classifieur textuel externe et d'une sonde lisant le modèle producteur, en cascade en série, **éprouvé par environ 1 736 heures d'équipe rouge humaine en boîte noire** (p. 9, 15) […]. »
  > « (d) mesure sous attaque de corruption — **voisin** — fait : équipe rouge humaine itérative, en boîte noire, contre le système entier (attaques d'évasion) ; non fait : aucune des cinq familles d'attaques de corruption, aucune attaque dirigée contre un membre, aucune attaque en boîte blanche. »
  > Verdict pour l'article : « occupé en partie » (composante b, au sens structurel ; a, c et d non faites).
- **Effet sur le verdict d'ensemble** : aucun.

### C — majeur — La complémentarité n'est pas attribuée au type d'accès de façon isolée, et ce n'est pas une mesure d'erreurs

- **Pages** : 2601.04603, p. 2, 7, 8, 9.
- **Citations** : « Spearman rank correlation between classifier predictions on jailbreak attempts. » (p. 8) ; « Probes and external classifiers make more independent errors than pairs of external classifiers. » (p. 8) ; « despite being trained on the same distribution as the external classifiers » (p. 9) ; « replace the synthetic pipeline’s hard labels with exchange-level soft labels produced by » (p. 7) ; « We assess robustness using a dataset of jailbreaks collected from human red-teaming » (p. 7).
- **Constat.** Le rapport écrit « La complémentarité des deux types d'accès est mesurée (p. 8, 9) » et « La justification de l'hétérogénéité par type d'accès […] est la même que celle de HC5 ». Quatre réserves manquent :
  1. la figure 3b mesure une corrélation de rang **des scores**, sur des tentatives de débridage ; « more independent errors » est l'interprétation de la légende, pas la grandeur mesurée ;
  2. trois barres, sans intervalle, sur un seul jeu : environ 0,75 pour la paire de classifieurs, 0,60 et 0,57 pour les paires avec la sonde (figure, relue sur l'image) ;
  3. la sonde diffère des classifieurs par le type d'accès, mais aussi par la capacité (linéaire contre modèle de langue réglé finement), par les étiquettes d'entraînement (étiquettes douces distillées, p. 7) et par le modèle lu. Les deux classifieurs partagent, eux, la lignée d'entraînement et l'entrée. L'article n'isole pas le type d'accès ;
  4. l'article ne dit pas contre quel système ni avec quel modèle les quelque 7 000 échanges statiques ont été produits. Les campagnes des sections 3 et 4 protégeaient un autre modèle que celui que lit la sonde de la section 5 (p. 4, note 2 ; p. 5 ; p. 7). On ne peut donc pas affirmer que, dans l'analyse statique, la sonde lit le modèle qui a écrit les réponses jugées. C'est établi pour la production seulement (p. 9).
- **Texte corrigé proposé** (section 1) :
  > « Sur un jeu statique d'environ 7 000 échanges, les scores de la sonde et ceux d'un classifieur textuel sont moins corrélés en rang (environ 0,57 à 0,60, figure) que ceux de deux classifieurs textuels (environ 0,75, figure), sans intervalle. L'article y voit des erreurs plus indépendantes ; il n'isole pas le type d'accès de la capacité du lecteur ni de ses étiquettes d'entraînement, et ne dit pas quel modèle a produit ces échanges. »

### D — majeur — La réserve statistique est juste et trop faible : aucun écart entre systèmes n'est établi, pas même contre la génération précédente

- **Pages** : 2601.04603, p. 4, 5, 9, 10, 14.
- **Citations** : « Only one high-risk vulnerability was discovered » (p. 9) ; « These results represent the strongest robustness achieved across all systems evaluated in this work. » (p. 9) ; « by users whose queries have a classifier refusal rate of greater than 5% » (p. 14).
- **Constat.** Les quatre intervalles du lecteur sont exacts (section 6). Sa phrase « Les trois derniers systèmes ne se distinguent pas statistiquement » est ambiguë (dans l'ordre de sa liste, elle désigne la cascade, le classifieur d'échange et la génération précédente) et en dessous de ce que les chiffres disent. Tests exacts conditionnels (calcul) :
  - production contre génération précédente : rapport des taux 0,27 ; p unilatérale 0,149 ; p bilatérale 0,330 ;
  - production contre cascade : p unilatérale 0,515 ; production contre classifieur d'échange : 0,550 ;
  - cascade contre génération précédente : p unilatérale 0,107 ;
  - seuls les trois nouveaux systèmes **réunis** (8 sur 993 000) se détachent à peine de la génération précédente (13 sur 695 000) : p unilatérale 0,045, p bilatérale 0,074.
- Les dénominateurs sont filtrés (p. 14) et arrondis au millier ; le modèle de Poisson suppose des requêtes indépendantes, ce que des campagnes d'attaquants itérant sur leurs propres essais ne garantissent pas.
- **Texte corrigé proposé** (section 3.3) :
  > « Aucune comparaison deux à deux entre systèmes n'atteint le seuil de 5 %, pas même le système de production contre la génération précédente (1 sur 198 000 contre 13 sur 695 000 ; test exact conditionnel, p unilatérale 0,15 ; calcul). Seul le regroupement des trois nouveaux systèmes s'en détache à peine (p unilatérale 0,045, bilatérale 0,074 ; calcul). Le classement « le plus robuste » repose sur une seule vulnérabilité et n'est pas établi. »

### E — mineur — Poids optimisé sur le test : réserve confirmée sur l'image ; une incohérence d'unité non vue

- **Pages** : 2601.04603, p. 7, 8, 16, 17.
- **Citations** : « is optimized per pair to minimize attack success rate on the test set » (p. 8) ; « for the classifier-probe ensembles, we find that equal weighting already is close to optimal » (p. 17) ; « demonstrating optimal performance at moderate window sizes » (p. 16).
- **Constat.**
  1. Figure 6b vue en image (p. 17) : sonde seule environ 1,5 %, classifieur seul environ 1,2 %, minimum plat autour des poids égaux, environ 0,45 à 0,5 % (figure). L'atténuation retenue par le lecteur tient donc : le gain de l'ensemble ne vient pas du réglage du poids sur le test. À ajouter : aucune figure ne porte d'intervalle, et les seuils de l'ensemble sont étalonnés sur un corpus bénin tiers (p. 8).
  2. **Incohérence d'unité, non relevée** (figure non vue par le lecteur). La figure 5 (p. 16) étiquette ses axes « Attack Success Rate (%) » avec des valeurs de 0,014 à 0,15 environ (figure), alors que la même ablation, figure 2b (p. 7), va d'environ 1,4 à 14,5 % (figure). La figure 5 est en fractions, pas en pourcentages.
- **Texte corrigé proposé** (section 3.3, incohérences mineures, à ajouter) :
  > « — la figure 5 (p. 16) est graduée en fractions sous l'étiquette « % » : ses valeurs sont cent fois plus petites que celles de la figure 2b (p. 7) pour la même ablation (figure). »

### F — majeur — Paraphrase de confiance : le contre-indice le plus direct manque, et la portée de la phrase de la section 6 est trop large

- **Pages** : 2608.11247, p. 3, 4, 5, 7, 9, 13, 16.
- **Citations** : « Asserted certainty persuades less than a plain statement on every dataset and in at least 21 of the 23 models » (p. 5) ; « Models read a stated reason as evidence and asserted confidence as grounds for suspicion » (p. 5) ; « asserted certainty lowers conformity relative to a bare assertion in 21, 21, and all 23 » (p. 16) ; « Peer reasoning raises conformity above a bare assertion in only 14, 12, and 16 models » (p. 16) ; « Rising above requires new information rather than new wording. » (p. 3) ; « These are the two predictions the results test » (p. 3) ; « A confident wrong peer and a confident right one look identical inside the exchange, so any lean the prompt induces applies to both. » (p. 7) ; « single-pass renderings of methods originally stated with more turns » (p. 9) ; « Multi-turn versions might sit elsewhere on the same frontier. » (p. 9) ; « the design does not include a content-free placebo » (p. 9) ; « an interval whose lower bound does not admits improvement » (p. 7).
- **Constat.**
  1. **Contre-indice direct non relevé.** Le tableau 1 (p. 4) donne, pour une majorité unanime fausse, la part de réponses renversées selon la forme de l'affirmation (auteurs) : affirmation nue 22,8, 54,8 et 71,0 % ; affirmation « absolument certaine » 18,6, 48,2 et 58,3 % ; affirmation avec une raison d'une ligne 24,9, 54,9 et 74,2 %. La certitude affichée déplace **moins** que l'affirmation nue : −4,2, −6,6 et −12,7 points (calcul), dans 21, 21 et 23 des 23 modèles (p. 16). Une réécriture qui ramènerait une affirmation emphatique à sa forme nue irait, dans ce dispositif, vers **plus** de déplacement : le marqueur rhétorique servait d'indice de méfiance. C'est le même sens que le contre-indice du niveau 3 (une réécriture efface l'indice qui protégeait le moniteur). Le lecteur cite ces chiffres dans sa note sur HC1 (section 4.4) et ne les rapproche pas de la paraphrase. Limites à écrire avec : répondants et non moniteurs ; pairs scriptés ; un seul gabarit par condition ; aucune réécriture n'est faite ; les intervalles entre modèles se recouvrent (tableau 7, p. 13), seul le sens par modèle est constant.
  2. **La citation de la p. 3 est une prédiction, pas un résultat.** « Rising above requires new information rather than new wording » figure dans la section 3, qui pose le cadre avant les résultats et se clôt par « These are the two predictions the results test ». Le résultat qui l'appuie tient à six points par jeu (R² de 0,88, 0,80 et 0,90, que je retrouve par recalcul sur le tableau 6).
  3. **La « distillation de la question » n'est pas une réécriture, et l'article ne teste pas qu'elle reste sur la droite.** C'est une consigne ajoutée au tour de l'utilisateur (tableau 5, p. 13), rendue en une passe d'une méthode d'origine à plusieurs tours (p. 9), que l'article n'a pas mesurée sous cette forme. La droite est ajustée **à travers** les six points, dont celui-ci ; aucun écart à la droite n'est donné par méthode instantanée. Recalcul sur le tableau 6 (calcul) : la distillation est la seule méthode instantanée au-dessus de la droite ajustée sur les trois jeux (+1,9, +1,3 et +1,3 point), et celle dont l'échange est le moins coûteux (5,1 points de résistance pour 5,8 de réceptivité sur le premier jeu, contre 7,9 pour 15,3 pour la réflexion ; auteurs, tableau 2). Sans incertitude, cela ne prouve rien ; cela interdit seulement d'écrire que cette consigne « n'élève pas au-dessus de la frontière » comme un fait testé.
  4. **Le dispositif ne contient rien à préserver.** Les pairs n'apportent qu'une affirmation (nue, certaine, ou une raison d'une ligne sans contenu). La transposition « une paraphrase qui ôte la rhétorique pourrait ôter aussi l'argument légitime » est une conjecture du lecteur ; il le dit (« non testé »), mais la section 6 la durcit.
  5. **Ce que la pièce apporte d'utile et que le rapport ne dit pas.** Le plan à deux axes (résister à la pression fausse, rester réceptif à la correction juste) est le plan 2 × 2 « rhétorique × intention » de EC.2 (programme, l. 195 : l'agent honnête qui plaide sincèrement contre le saboteur qui tient le même plaidoyer). La leçon transposable est une exigence de mesure : une contre-mesure se note sur les deux axes. Ce rapprochement est le mien, non testé.
  6. **« Aucune incohérence chiffrée relevée »** (rapport, 4.2) : à nuancer. La phrase qui porte l'écart à la droite sur le premier jeu est fautive (« an interval whose lower bound does not admits improvement », p. 7), et l'intervalle de cet écart de +3,3 points n'est imprimé nulle part (le tableau 12, p. 15, ne donne que les deux autres jeux). Le signe de la borne basse n'est donc pas vérifiable sur la pièce. L'écart lui-même se recalcule : +3,3, −0,6 et −1,9 (calcul), comme imprimé.
- **Texte corrigé proposé** (tableau 4.3, ligne (a)) :
  > « **voisin ; deux contre-indices indirects.** (i) Direct dans les chiffres : une affirmation « absolument certaine » déplace moins qu'une affirmation nue (18,6 contre 22,8 % ; 48,2 contre 54,8 % ; 58,3 contre 71,0 % ; auteurs, tableau 1 p. 4 ; 21, 21 et 23 modèles sur 23, p. 16) ; une réécriture qui neutraliserait l'emphase retirerait donc, dans ce dispositif, un indice de méfiance. (ii) De principe : les six consignes testées déplacent les modèles le long d'un compromis entre résistance et réceptivité (six points par jeu, R² de 0,80 à 0,90, p. 6) ; les auteurs en tirent qu'un gain sur les deux axes demande une information extérieure à l'échange (p. 7). Aucune réécriture par un modèle de confiance n'est testée ; aucun moniteur n'est en jeu ; les pairs sont scriptés et n'apportent aucun argument à préserver ; la « distillation de la question » est une consigne en une passe (p. 9, 13), dont la forme d'origine, à plusieurs tours (Zhu et collègues, 2025), n'est pas lue. »
- **Texte corrigé proposé** (section 6, quatrième puce) :
  > « Que la paraphrase de confiance est appuyée par les pièces lues. Elles donnent trois indices indirects en sens contraire, aucun sur une réécriture de confiance ni sur un moniteur : une sortie lue hors de son contexte est plus facile à obscurcir (2601.04603, p. 3-4) ; une affirmation emphatique déplace moins qu'une affirmation nue (2608.11247, p. 4, 5, 16) ; six consignes de résistance échangent résistance contre réceptivité (2608.11247, p. 6, 7). Ne pas écrire non plus l'inverse : que ces pièces montrent qu'une paraphrase de confiance échoue. »

### G — majeur — Voisins non lus : deux manques, et un rappel de périmètre

- **Pages** : 2601.04603, p. 10, 12 ; 2608.11247, p. 2, 9 ; contre-lecture du niveau 3, l. 538-541.
- **Citations** : « McKenzie et al. (2025) similarly investigate softmax-weighted probes and classifier cascades. » (p. 10) ; « Hua et al. (2025) investigate optimal strategies for combining multiple monitors under cost constraints. » (p. 10) ; « Combining cost-constrained runtime monitors for AI safety » (p. 12) ; « MARS Redwood Research » (p. 12) ; « Cunningham et al. (2025) explore internals-based classifiers » (p. 10) ; « introduced Devil’s Advocate and Question Distillation » (2608.11247, p. 2).
- **Constat.**
  1. **McKenzie et collègues (arXiv 2506.10805) est sous-classé.** La pièce dit elle-même que ce travail étudie « de même » des sondes et des cascades de classifieurs. C'est, d'après la pièce, une **seconde publication** qui combine sondes d'activations et classifieurs en cascade. Le lecteur le liste sans priorité. À lire au même rang que Hua et collègues.
  2. **Hua et collègues (arXiv 2507.15886)** : priorité juste. D'après la pièce : combinaison de plusieurs moniteurs sous contrainte de coût (p. 10) ; titre « moniteurs d'exécution […] pour la sûreté » et rattachement imprimé à un groupe de recherche sur le contrôle (p. 12). C'est donc plus près du cadre de HC5 que 2601.04603. La pièce **ne dit pas** si l'un des moniteurs est une sonde, ni quelle règle de combinaison est étudiée. Rien ne peut en être affirmé avant lecture (R7).
  3. **Zhu et collègues (2025) est le voisin à lire pour la paraphrase**, pas seulement pour la conformité : la « distillation de la question » d'origine est à plusieurs tours (2608.11247, p. 9) et peut comporter une réécriture. Le lecteur le liste sans ce motif.
  4. **Non listés par le lecteur** : les deux fiches de système d'un autre fournisseur citées p. 10 pour une classification à deux étages (filtre thématique léger, puis classifieur coûteux) ; priorité basse, mais elles montrent que la cascade de filtres est une pratique publiée par plusieurs acteurs.
  5. **Périmètre.** Le constat M9 nomme d'autres pistes non reprises (He et Yu sur les quorums à fautes corrélées, « BRANCH », « Screwtape »). Elles ne sont pas dans ce mandat et restent non lues. Le verdict du rapport et le mien ne couvrent que deux PDF.
- **Texte corrigé proposé** (section 7, en tête) :
  > « À lire avant toute phrase sur le quorum : Hua et collègues, arXiv 2507.15886 (p. 10, 12 ; combinaison de moniteurs d'exécution sous contrainte de coût ; la pièce ne dit pas si une sonde en fait partie) et McKenzie et collègues, arXiv 2506.10805 (p. 10, 12 ; « softmax-weighted probes and classifier cascades » : seconde combinaison publiée de sondes et de classifieurs, d'après la pièce). À lire avant toute phrase sur la paraphrase : Zhu et collègues, 2025 (2608.11247, p. 2, 9 ; forme d'origine, à plusieurs tours, de la « distillation de la question »). Restent non lues les pistes du constat M9 hors de ce mandat. »

### H — mineur — « Ce qui reste revendicable » : deux précisions

- **Pages** : rapport, section 5 ; 2601.04603, p. 9, 10.
- **Constat.**
  1. La formulation ne dit pas ce qui distingue le quorum revendiqué de la cascade publiée. Après le constat A, la distinction utile est : chaque membre lit tout, et la règle de décision est telle que la corruption d'un seul membre ne suffit pas.
  2. La formulation vaut « au regard des deux pièces lues ». Elle ne peut pas être reprise tant que les deux voisins du constat G ne sont pas lus.
- **Texte corrigé proposé** (section 5, à ajouter après la formulation) :
  > « Précision : un quorum où chaque membre lit tout le contenu et où la corruption d'un seul membre ne suffit pas à faire passer une action, par opposition à la cascade publiée, où la sonde filtre seule ce que le lecteur textuel verra (2601.04603, p. 9). Formulation valable au regard des deux pièces lues seulement ; Hua et collègues et McKenzie et collègues restent à lire. »

### I — mineur — Renvois de page et silences à écrire

- **Constat.**
  1. Section 1 : « plus de 1 700 heures d'équipe rouge humaine (p. 1, 2, 8, 9) » ; la p. 8 n'en parle pas. Pages justes : 1, 2, 9.
  2. Section 3.3 : la note 3 (p. 5) dit que des experts hors programme de primes ont trouvé des débridages universels de la cascade. Les remerciements disent que trois organismes extérieurs ont attaqué « various versions of our system » (p. 11), sans résultat rapporté. Le rapport écrit « rien n'est dit pour le système de production » ; il faut ajouter que « aucun débridage universel » (p. 9) vaut pour le seul programme de primes.
  3. Section 3.1 : « Elle lit l'échange jeton par jeton (entrée puis sortie) pendant la génération » est juste pour la production ; pour l'analyse statique, voir le constat C, point 4.
  4. Section 3.3 : la sonde signale davantage les requêtes scientifiques bénignes (« Moreover, we found that the flag rate on benign scientific requests was higher for the probe. », p. 8) ; le rapport le dit, sans chiffre : l'article n'en donne aucun. À écrire tel quel.
- **Texte corrigé proposé** (section 3.3, première puce) :
  > « note 3 (p. 5) : des experts hors programme de primes ont trouvé des débridages universels de la cascade de la section 4. Pour le système de production, « aucun débridage universel » (p. 9) ne vaut que pour le programme de primes ; des organismes extérieurs ont attaqué « diverses versions » du système (p. 11) et l'article n'en rapporte pas le résultat. »

## 6. Recalcul de l'intervalle de Poisson (point 4 du mandat)

Script `scripts/calculs_contre_lecture_HC5_v1.py`, lancé par `python3 -I`, bibliothèque standard. Voie différente de celle du lecteur : quantiles de la loi gamma par la fonction gamma incomplète régularisée (le lecteur sommait la loi de Poisson). Effectifs imprimés (auteurs) : p. 4, 5, 9 et tableau 1 p. 10. Tout ce qui suit est de nature « calcul ».

| système | vulnérabilités / requêtes | taux pour mille | intervalle exact à 95 % (pour mille) | intervalle du lecteur |
|---|---|---|---|---|
| génération précédente | 13 / 695 000 | 0,01871 | [0,00996 ; 0,03199] | identique |
| classifieur d'échange | 2 / 226 000 | 0,00885 | [0,00107 ; 0,03197] | identique |
| cascade à deux étages | 5 / 569 000 | 0,00879 | [0,00285 ; 0,02051] | identique |
| production | 1 / 198 000 | 0,00505 | [0,00013 ; 0,02814] | identique |

- **Les quatre intervalles du lecteur sont confirmés à cinq décimales.**
- L'intervalle du système de production couvre un facteur d'environ 220 entre ses bornes et contient les taux des trois autres systèmes.
- Sensibilité à l'arrondi du dénominateur (plus ou moins 500 requêtes) : la borne haute va de 0,02807 à 0,02821 ; sans effet.
- Tests entre systèmes : constat D.
- L'écart 0,00878 imprimé contre 0,008787 calculé (5 sur 569 000) vient de l'arrondi du dénominateur ; non opposable, comme l'écrit le lecteur.
- Second recalcul (2608.11247, tableau 6 p. 13) : droite des moindres carrés sur les six points instantanés ; R² de 0,876, 0,801 et 0,904 (imprimés p. 6 : 0,88, 0,80, 0,90) ; écart du raisonnement +3,31, −0,55 et −1,87 (imprimés p. 7 : +3,3, −0,6, −1,9). Les chiffres des auteurs se retrouvent.

## 7. Verdicts par composante (les deux pièces)

| composante de HC5 | 2601.04603 | 2608.11247 | dans les deux pièces |
|---|---|---|---|
| paraphrase de confiance | voisin ; contre-indice indirect (sortie lue hors contexte, p. 3-4) | voisin ; deux contre-indices indirects (p. 4, 5, 6, 7, 16) | non trouvée |
| quorum par type d'accès, juges génératifs et sondes lisant l'agent | **occupée en partie** : classifieur textuel et sonde du modèle producteur, cascade en série, équipe rouge humaine en boîte noire (p. 2, 5, 8, 9, 15). Non fait : agent adverse, juges génératifs, membres lisant tous deux tout le contenu sous attaque, attaques de corruption | voisin (p. 1, 7, 8) | occupée en partie |
| matrice de transfert des attaques de corruption entre juges et sondes | voisin (corrélation de rang des scores, p. 8 ; jeu d'attaques rejoué sur chaque membre, p. 7-8) | ne touche pas | non trouvée |

**Verdict d'ensemble sur HC5, table fermée : « occupé en partie ».**

## 8. Ce qu'une phrase publique sur HC5 ne doit pas affirmer (compléments à la section 6 du rapport)

Les six interdictions du lecteur tiennent, la quatrième dans la rédaction du constat F. S'y ajoutent :
- que l'ensemble publié est un quorum, ou qu'un quorum de sondes et de classifieurs a été éprouvé sous attaque : c'est une cascade en série où la sonde décide seule d'environ 94,5 % du trafic (2601.04603, p. 9) ;
- que 2601.04603 est la première ou la seule combinaison publiée de sondes et de classifieurs : la pièce en nomme une autre (McKenzie et collègues, p. 10) et un travail sur la combinaison de moniteurs d'exécution (Hua et collègues, p. 10, 12), non lus ;
- que l'hétérogénéité par type d'accès est établie comme la cause de l'indépendance des erreurs : la pièce ne l'isole pas (constat C) ;
- que le système de production de 2601.04603 est plus robuste que les précédents : aucun écart n'est établi (constat D) ;
- que l'équipe rouge de 2601.04603 a attaqué la sonde, ou qu'elle était « adaptative » au sens d'une attaque optimisée contre un membre : accès en boîte noire au système entier, mot absent de l'article en ce sens ;
- que les sondes résistent aux attaques par contenu au vu de cette pièce : une vulnérabilité à haut risque a été trouvée, la pièce ne dit pas par quel étage elle est passée, et le système précédent a été débridé hors programme (p. 5, note 3) ;
- quoi que ce soit sur Hua et collègues (arXiv 2507.15886, nommé p. 10, référence p. 12) au-delà de ce que la pièce en dit : combinaison de plusieurs moniteurs sous contrainte de coût. Ni la présence d'une sonde, ni le cadre exact, ni un résultat ne sont lisibles dans la pièce ;
- que la paraphrase de confiance est réfutée : aucune des deux pièces ne la teste.

Je ne rédige pas la phrase publique (rôle exclu).

## 9. Notes hors mandat, sans verdict

- **Pour le lecteur de HC2 et de HC4.** 2601.04603 est une campagne d'attaques par contenu, en boîte noire, contre un système dont le premier étage est une sonde linéaire à lissage par moyenne (p. 6, 9). Une vulnérabilité à haut risque trouvée en environ 198 000 requêtes (p. 9).
- **Pour le lecteur de H5.** La note du lecteur (section 8 de son rapport) tient, avec la réserve du constat C : corrélation des scores, pas des erreurs, sans intervalle.
- **Interdit du programme sur la moyenne des jetons.** La sonde publiée agrège par moyenne glissante puis par moyenne mobile exponentielle (p. 6). Le lecteur le note ; c'est un fait de conception, pas un verdict d'antériorité.

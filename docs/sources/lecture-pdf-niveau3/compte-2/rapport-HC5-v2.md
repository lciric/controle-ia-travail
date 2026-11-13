# Rapport du lecteur — HC5, contre-mesures (papier C) — v2

- **Écrit le** 2026-11-13 à 23:16:16 UTC (relevé par date -u dans la commande d'écriture). Reprise pour la version 2 : 2026-11-13 à 23:11:25 UTC (relevé par date -u à la vérification des empreintes).
- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Remplace** `rapport-HC5-v1.md` (empreinte `10b861094910ab7267276e424f0af78811a172157d167e45446baed67823d96b`), qui reste en place sans modification.
- **Intègre la contre-lecture** :
  - `contre-lecture-rapport-HC5-v1.md` (empreinte vérifiée `e241a0e0ef0d2b438c3755dce70686862dae10c08fbbf8322358908236a7da1c`), verdict « tient avec corrections » ;
  - son archive `fichiers-de-travail-contre-lecture-HC5-v1.tar` (empreinte vérifiée `e2fa704c81eb2239ab042bc5ca083985bf88b67428cab4b28b0694d98669bd60`), extraite dans un dossier neuf de mon dossier de travail.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, tenue sans exception.
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
  - la consigne commune et les interdits communs v2 ;
  - la contre-lecture et le contenu de son archive ;
  - les deux PDF.
- **Étendue lue** :
  - 2601.04603 : p. 1-17 ligne à ligne ; **toutes les figures vues en image** (figures 2 et 3 en version 1 ; figures 4, 5 et 6 en version 2) ;
  - 2608.11247 : p. 1-9 et 13-16 ligne à ligne, p. 10-12 et 17 (bibliographie, liste des modèles, licences) par mots ; **toutes les figures vues en image en version 2** (figures 1 à 8, avec les tableaux 2, 3, 11 et 12).
- **Citations contrôlées par programme** : 76, échecs : 0 (avec et sans `-layout`, normalisation). Script testé en version 1 sur un cas juste et trois cas altérés. Tout passage anglais cité dans ce rapport est couvert par le fichier des citations (contrôle de couverture : 0 manquant). Le fichier `citations-HC5-v2.json` est dans l'archive seulement, empreinte `a873a58a78c21c6f6a5117e3aee6ef32e33e6e3d7a5a20b33974b60fa9333476`.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé). Les formules sont lues sur le PDF et non contrôlées par programme.
- **Aucune ouverture fautive, aucun refus, aucune commande git, aucun réseau, aucun appel de modèle.** Aucun nom de modèle n'est écrit.

## 1. Verdict d'ensemble

**HC5 — contre-mesures : « occupé en partie »** (table fermée ; inchangé depuis la version 1, même valeur que le contre-lecteur).

- **Ce qui est occupé, par 2601.04603, et seulement la composante (b) au sens structurel.** L'idée « un lecteur textuel externe et une sonde qui lit le modèle producteur, combinés pour leur complémentarité » est publiée. Elle sert à défendre un modèle conversationnel contre le débridage. Elle n'est plus revendicable comme telle.
- **Ce qui a été éprouvé sous équipe rouge n'est pas un quorum.** C'est une **cascade en série** :
  - la sonde lit tout le trafic et laisse passer seule environ 94,5 % des échanges (calcul, d'après les 5,5 % d'escalade imprimés p. 9) ;
  - le classifieur textuel ne lit que les échanges que la sonde escalade, et les deux logits y sont moyennés ;
  - une attaque qui tient la sonde sous le seuil d'escalade n'est jamais lue par le classifieur ;
  - la fusion où chaque membre lit tout n'est mesurée que sur un jeu statique (figure 3a, p. 8).
- **Ce qui n'est trouvé dans aucune des deux pièces :**
  - un quorum de juges génératifs et de sondes lisant un **agent adverse** ;
  - une matrice de transfert des attaques de corruption entre juges et sondes ;
  - une paraphrase de confiance ;
  - une mesure sous attaques de corruption du jugement.

  « Non trouvé dans les pièces lues » ne veut pas dire « trou du champ » : deux voisins nommés par 2601.04603 restent à lire avant toute phrase sur le quorum (section 8).
- **2608.11247 est voisin.** Il donne deux indices indirects sur la paraphrase de confiance, de sens partiellement opposés (section 4.3). Il ne touche ni la matrice ni la mesure sous attaque.
- **Correction à porter dans la synthèse du niveau 3 (l. 445-447).** La phrase « Le quorum de juges et de sondes qui lisent l'agent […] ne sont pas trouvés » doit être nuancée :
  - une combinaison publiée réunit un classifieur textuel et une sonde du modèle producteur, éprouvée en cascade par une équipe rouge humaine en boîte noire ;
  - ce n'est pas un quorum ;
  - le cadre n'est pas le contrôle d'un agent adverse.

## 2. Énoncé confronté (fichiers nommés, lignes lues)

HC5 selon N-006 (l. 76-90) et N-013 (l. 56-68) :
- (a) **paraphrase de confiance** : un modèle de confiance paraphrase le contenu avant que le juge le lise, pour couper le canal rhétorique. Le niveau 3 (l. 440-442) note le risque inverse : une réécriture peut effacer l'indice qui protégeait le moniteur ;
- (b) **quorum hétérogène en type d'accès** : juges génératifs **et** sondes qui lisent l'agent ;
- (c) **matrice de transfert des attaques de corruption entre juges et sondes**, qui mesure l'efficacité du quorum.

Revendiqué selon N-006 : le quorum par type d'accès et la matrice.

Le mandat demande aussi de confronter « la mesure sous attaque ». Dans N-006 et N-013, cette mesure **est** la matrice (constat B). Je garde une ligne (d) pour répondre au mandat, avec une définition cohérente : (d) **mesure des contre-mesures sous attaques de corruption du jugement**, c'est-à-dire les cinq familles de EC.1 (programme l. 194). Une épreuve d'évasion par débridage n'en fait pas partie ; elle se range sous (b) comme attribut de l'ensemble éprouvé.

## 3. 2601.04603v1 — « Constitutional Classifiers++ »

### 3.1 Ce que fait l'article

**Venue imprimée.** Prépublication arXiv, cs.CR, 8 janvier 2026 (p. 1), sans conférence imprimée. Tous les auteurs sont dans un même laboratoire industriel (p. 1, note).

**Cadre.** Défense d'un modèle conversationnel contre le **débridage universel** : obtenir des réponses détaillées à huit questions dangereuses dans les domaines chimique, biologique, radiologique et nucléaire. L'adversaire est **l'utilisateur**. Le modèle protégé n'est ni l'adversaire ni l'auteur des contenus d'attaque.

**Quatre systèmes comparés** (tableau 1, p. 10 ; figure 4, p. 14, vue en image) :
1. génération précédente : un classifieur d'entrée et un classifieur de sortie seul ;
2. un classifieur d'**échange** unique, qui lit la sortie dans le contexte de l'entrée (p. 2-4) ;
3. une cascade à deux étages de classifieurs d'échange (p. 4-5) ;
4. le système de production (p. 9).

**Ce que lit chaque membre.**
- **La sonde** est linéaire et lit les activations de toutes les couches concaténées du **modèle protégé** : « explore further cost savings by developing classifiers that reuse representations already computed during model sampling » (p. 5).
  - En production : « As such, the probe uses activations from that model. » (p. 9). Elle lit l'échange en flux, pendant la génération, et la sonde lit donc bien le modèle qui écrit la réponse jugée.
  - Dans l'analyse statique (section 5), la sonde lit « the protected model » (p. 8). En revanche, les quelque 7 000 échanges du jeu statique ont été collectés lors de campagnes d'équipe rouge dont l'article ne nomme ni le système ni le modèle (« We assess robustness using a dataset of jailbreaks collected from human red-teaming », p. 7). Les campagnes des sections 3 et 4 protégeaient d'autres modèles (p. 4, note 2 ; p. 5). Dans l'analyse statique, il n'est donc **pas établi** que la sonde lise le modèle qui a écrit les réponses (constat C).
  - Entraînement : lissage des logits par moyenne glissante sur 16 jetons et perte pondérée (p. 6-7). Inférence : moyenne mobile exponentielle (p. 6). C'est un fait de conception, à noter au regard de l'interdit du programme sur les moyennes de jetons, pas un verdict.
- **Les classifieurs externes** sont des modèles de langue réglés finement, en deux tailles (« petit » et « très petit », environ un tiers ; p. 5, 8). Ce sont des classifieurs d'échange : ils lisent l'entrée et la sortie et rendent un score. Ce **ne sont pas des juges génératifs** incités.

**Comment l'ensemble décide.**
- Analyse statique (section 5.3, p. 8-9) :
  - fusion où les deux membres lisent tout : moyenne pondérée des logits, avec un poids « optimized per pair to minimize attack success rate on the test set » (p. 8) ;
  - des poids égaux sont quasi optimaux pour les paires sonde et classifieur (p. 17 ; figure 6, vue en image : minimum plat autour des poids égaux) ;
  - cascade : « when the probe score exceeds a threshold, we route the exchange to the small external classifier and average their logits to make our final prediction. Otherwise, we rely solely on the probe. » (p. 9 ; les deux phrases sont contrôlées séparément).
- Production (p. 9) :
  - « When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » ;
  - « For escalated exchanges, the final classification score is computed as a weighted combination of probe and classifier logits », avec les poids 0,55 et 0,45 (auteurs ; formule lue sur le PDF, non contrôlée par programme) ;
  - « The first-layer probe escalated approximately 5.5% of traffic to the second-stage classifier. » ;
  - l'article ne dit rien d'autre du trafic non escaladé.
- **Conséquence (constat A).** Pour qu'un échange soit refusé, il faut que la sonde dépasse le seuil d'escalade **et** que le score fusionné dépasse le seuil de refus. Il n'y a ni vote, ni règle « k parmi n », ni règle « ou ». Faire taire la sonde suffit à échapper au système. L'hétérogénéité sert ici le coût, puis la précision sur les cas escaladés, et non la résistance à la corruption d'un membre.
- Seuils : étalonnés pour 0,1 % de refus sur un corpus tiers de conversations ordinaires (p. 4, 5, 7, 8).

**Sous quelles attaques.**
- (i) **Jeu statique** : environ 7 000 échanges de débridage (p. 7). Ils ont été écrits par des membres de l'équipe rouge dont les échanges n'ont jamais servi à l'entraînement, contre des systèmes non nommés. Ce ne sont pas des attaques optimisées contre la sonde. L'attaque compte comme parée si le classifieur signale à un moment quelconque, ce qui « may underestimate the attack success rate » (p. 7, note 6).
- (ii) **Équipe rouge humaine contre le système de production** :
  - environ 1 736 heures et 198 000 tentatives (auteurs, p. 9) ;
  - **accès en boîte noire** au système entier : « We provide red-teamers with API access to the defended model. » (p. 15) ;
  - primes jusqu'à 35 000 dollars (p. 15) ; attaquants qui itèrent sur leurs essais ;
  - le mot « adaptive » n'apparaît dans l'article qu'au sens du calcul adaptatif (p. 5, 10), jamais au sens d'une attaque ;
  - les attaques sont des attaques d'évasion : reconstruction par fragments, obscurcissement des sorties (p. 2-3) ;
  - aucune attaque en boîte blanche ni dirigée contre la sonde seule n'est rapportée. L'article ne dit pas par quel étage est passée la vulnérabilité trouvée.

**Résultats (auteurs, tableau 1 p. 10, sauf mention)** :
- taux de découverte de vulnérabilités à haut risque, pour mille requêtes :
  - génération précédente : 0,01871 (13 sur 695 000) ;
  - classifieur d'échange : 0,00885 (2 sur 226 000) ;
  - cascade : 0,00878 (5 sur 569 000) ;
  - production : 0,00505 (1 sur 198 000) ;
- surcoût de calcul : 100 ; 150 ; 27,8 ; 3,5 % ;
- refus sur le trafic de production : 0,073 ; 0,038 ; 0,036 ; 0,050 % ;
- figure 4 (p. 14, vue en image) : temps minimal de découverte d'environ 5, 15, 12 et 30 heures (figure) ; la production a le plus long, en accord avec la p. 9 ;
- analyse statique, taux de succès d'attaque (figures 2a et 3a, p. 7-8, et figure 6, p. 17, vues en image) :
  - sonde seule environ 1,4 % (aussi imprimé p. 8) ;
  - petit classifieur environ 1,1 à 1,2 % ;
  - très petit classifieur environ 4,5 % ;
  - ensemble sonde et petit classifieur environ 0,45 à 0,5 % ;
  - ensemble des deux classifieurs environ 0,8 % (tout en figure) ;
- corrélation de rang de Spearman entre **scores** sur les tentatives de débridage (figure 3b, p. 8) : environ 0,75 pour la paire de classifieurs, environ 0,60 et 0,57 pour les paires avec la sonde (figure). Il n'y a aucun intervalle.

### 3.2 Ce que l'article ne fait pas
- **Pas de contrôle d'un agent.** Le modèle lu n'est jamais l'adversaire ni l'auteur des contenus d'attaque.
- **Pas de juges génératifs incités.**
- **Pas de quorum où chaque membre lit tout sous attaque.** La fusion de ce type est statique ; ce qui a été éprouvé est la cascade en série.
- **Pas d'attaques de corruption du jugement.**
- **Pas de matrice de transfert.** Le mot « transfer » est absent des 17 pages (recherche par mots, constat du contre-lecteur, revérifiée). Aucune attaque n'est optimisée contre un membre puis portée sur l'autre. Ce qui s'en approche :
  - la corrélation de rang des scores (figure 3b) ;
  - le rejeu d'un même jeu d'attaques venues d'ailleurs sur chaque membre et sur les ensembles (figures 2a et 3a). Cela ne fait pas une matrice.
- **Pas de paraphrase de confiance.**

### 3.3 Limites, incohérences, réserves (règle R4)

**Limites reconnues par les auteurs, et silences :**
- note 3 (p. 5) : « expert-level red-teamers operating outside our bounty program were nonetheless able to discover universal jailbreaks for this system », pour la cascade de la section 4 ;
- pour la production, « aucun débridage universel » (p. 9) ne vaut que pour le programme de primes. Des organismes extérieurs ont attaqué « various versions of our system » (p. 11), et l'article n'en rapporte pas le résultat ;
- note 6 (p. 7) : le taux de succès peut être sous-estimé ;
- « Moreover, we found that the flag rate on benign scientific requests was higher for the probe. » (p. 8) : l'article ne donne aucun chiffre ;
- note 2 (p. 4) : les systèmes ne protègent pas le même modèle.

**Statistique (calcul ; intervalles exacts de Poisson à 95 %, confirmés indépendamment par le contre-lecteur)** :
- intervalles, pour mille requêtes :
  - production : [0,00013 ; 0,02814] ;
  - cascade : [0,00285 ; 0,02051] ;
  - classifieur d'échange : [0,00107 ; 0,03197] ;
  - génération précédente : [0,00996 ; 0,03199] ;
- tests exacts conditionnels (calcul, sous l'hypothèse de taux égaux) :
  - production contre génération précédente : rapport des taux 0,27, p unilatérale 0,149, bilatérale 0,330 ;
  - production contre cascade : p unilatérale 0,515 ; production contre classifieur d'échange : 0,549 ;
  - cascade contre génération précédente : 0,107 ;
  - les trois nouveaux systèmes réunis (8 sur 993 000) contre la génération précédente : p unilatérale 0,045, bilatérale 0,074 ;
- **aucune comparaison deux à deux n'atteint 5 %**, pas même la production contre la génération précédente. Le classement « le plus robuste » (« These results represent the strongest robustness achieved across all systems evaluated in this work. », p. 9) repose sur une seule vulnérabilité et **n'est pas établi** ;
- les dénominateurs sont filtrés (« by users whose queries have a classifier refusal rate of greater than 5% », p. 14) et arrondis au millier. Le modèle de Poisson suppose des requêtes indépendantes, ce que des attaquants qui itèrent ne garantissent pas.

**Campagnes non comparables :**
- quatre des huit questions ont été remplacées (p. 15) ;
- le barème des primes a changé (p. 15) ;
- le modèle protégé a changé (p. 4, note 2) ;
- les auteurs l'admettent en partie : « Since different systems received varying levels of red-teaming effort » (p. 4).

**Ensemble.** Le poids est optimisé sur le test (p. 8). La figure 6 (p. 17, vue en image) montre un minimum plat autour des poids égaux : le gain de l'ensemble ne tient donc pas au réglage du poids. Restent deux réserves : aucune figure ne porte d'intervalle, et la sonde statique lit un autre modèle que celle de production (p. 7 contre p. 9).

**Complémentarité (constat C).**
- La figure 3b mesure une corrélation de rang des **scores** (« Spearman rank correlation between classifier predictions on jailbreak attempts. », p. 8). La phrase « more independent errors » est l'interprétation de la légende.
- La sonde diffère des classifieurs par le type d'accès, mais aussi par la capacité (linéaire), par ses étiquettes (douces, distillées, p. 7) et par le modèle lu. L'article n'isole pas le type d'accès : « despite being trained on the same distribution as the external classifiers » (p. 9) ne contrôle que la distribution d'entraînement.

**Incohérences mineures :**
- « first-layer probe » (p. 9) pour le premier étage ;
- « detection rate of 0.005 per thousand queries » (p. 9) pour le taux de découverte ;
- 5 sur 569 000 donne 0,00879 (calcul) contre 0,00878 imprimé, un écart d'arrondi non opposable ;
- le système de production refuse plus que ceux des sections 3 et 4 (0,050 contre 0,038 et 0,036 %), alors que le résumé annonce « dramatically reduced computational costs and refusal rates compared to previous-generation defenses » (vrai contre la génération précédente seulement) ;
- **la figure 5 (p. 16, vue en image) est graduée en fractions sous l'étiquette « % »** : ses valeurs (environ 0,014 à 0,15) sont cent fois plus petites que celles de la figure 2b (p. 7) pour la même ablation (environ 1,4 à 14,5 % ; figure).

### 3.4 Verdicts par composante (2601.04603)

| composante | verdict | fait | non fait | pages |
|---|---|---|---|---|
| (a) paraphrase de confiance | **voisin ; contre-indice indirect** | une sortie lue hors de son contexte est contournée par obscurcissement ; le contexte rend la détection : « coded language, metaphors, and substitutions can evade an output-only classifier but are more readily identified when evaluated alongside their input context » (p. 4) ; « Obfuscation attacks exploit the output classifier’s inability to interpret context-dependent transformations. » (p. 3) | aucune paraphrase ni réécriture ; aucun modèle de confiance intercalé | 2, 3, 4 |
| (b) quorum par type d'accès | **occupée en partie** (au sens structurel) | classifieur textuel externe et sonde lisant le modèle protégé, combinés pour leur complémentarité ; fusion où chacun lit tout, mesurée **en statique** (figure 3a) ; **cascade en série**, où la sonde filtre seule environ 94,5 % du trafic, **éprouvée par environ 1 736 heures d'équipe rouge humaine en boîte noire** (p. 9, 15) | agent adverse ; juges génératifs ; quorum où chaque membre lit tout **sous attaque** ; règle telle que la corruption d'un seul membre ne suffise pas ; type d'accès isolé comme cause de la complémentarité | 2, 5, 7, 8, 9, 15 |
| (c) matrice de transfert juges ↔ sondes | **voisin** | corrélation de rang des scores entre membres (p. 8) ; même jeu d'attaques rejoué sur chaque membre (p. 7-8) | aucune attaque optimisée contre un membre puis portée sur l'autre ; aucune attaque de corruption ; « transfer » absent | 7, 8 |
| (d) mesure sous attaques de corruption | **voisin** | équipe rouge humaine itérative, en boîte noire, contre le système entier, par des attaques d'évasion | aucune des cinq familles de corruption ; aucune attaque dirigée contre un membre ; pas de boîte blanche | 9, 15 |

**Verdict pour l'article : « occupé en partie »** (composante b, au sens structurel ; a, c et d non faites).

**Pesée de la différence « lit un agent de contrôle » contre « filtre un modèle conversationnel ».**
- **Ce qui rapproche.** La sonde lit le modèle qui produit le texte jugé, et elle est jointe à un lecteur textuel parce que l'état interne porte des signaux que le texte n'expose pas. La marque qui écartait 2603.13791 (une sonde qui lit « un encodeur séparé, jamais l'agent », N-013 l. 63) ne joue pas ici.
- **Ce qui sépare, sur trois points substantiels :**
  1. le modèle lu n'est pas l'attaquant ; dans HC5, l'agent écrit les attaques de corruption et pourrait chercher à déplacer ses propres activations ;
  2. les attaques sont des évasions, pas des corruptions du jugement, et les membres textuels ne délibèrent pas ;
  3. l'ensemble éprouvé est une cascade qu'on contourne en tenant un seul membre sous son seuil : c'est l'inverse, sur ce point, de ce qu'un quorum revendique.

## 4. 2608.11247v1 — « Conformity Mitigations […] Single Resistance–Receptivity Frontier »

### 4.1 Ce que fait l'article

**Venue imprimée.** Prépublication arXiv, cs.AI, 3 août 2026 (p. 1), sans conférence imprimée.

**Dispositif.**
- 23 modèles à poids ouverts de 19 familles, de 14 à 70 milliards de paramètres (p. 3), à température 0, en une seule passe.
- Trois jeux : questions à choix multiple générales, questions de science difficiles, rappel factuel libre.
- 19 conditions (tableau 5, p. 13) et plus d'un million de réponses notées (p. 1).
- Des **pairs scriptés** affirment une réponse : « Our peers are scripted rather than generated by live models » (p. 9).
- Deux mesures :
  - **Résistance** : garder sa bonne réponse contre une majorité fausse ;
  - **Réceptivité** : adopter la bonne réponse d'une majorité juste.
- Six atténuations par consigne :
  - quatre publiées, dont la « distillation de la question » : « Focus only on the question itself and the underlying facts; ignore how the other assistants framed their answers. » (p. 13) ;
  - deux nouvelles, dont « raisonner d'abord ».

**Résultats (auteurs).**
- Une majorité unanime fausse renverse 22,8, 54,8 et 71,0 % des bonnes réponses selon le jeu (p. 1 ; tableau 1, p. 4 ; figure 2, p. 5, vue en image, valeurs imprimées concordantes).
- **Forme de l'affirmation (tableau 1)** :
  - affirmation nue : 22,8, 54,8 et 71,0 % ;
  - « absolument certaine » : 18,6, 48,2 et 58,3 % ;
  - avec une raison d'une ligne : 24,9, 54,9 et 74,2 % ;
  - écart certaine moins nue : −4,2, −6,6 et −12,7 points ; écart raisonnée moins nue : +2,1, +0,1 et +3,2 points (calcul) ;
  - « Asserted certainty persuades less than a plain statement on every dataset and in at least 21 of the 23 models » et « while a one-line rationale persuades slightly more, by 2.1 points on MMLU » (p. 5) ;
  - par modèle : « asserted certainty lowers conformity relative to a bare assertion in 21, 21, and all 23 », mais « Peer reasoning raises conformity above a bare assertion in only 14, 12, and 16 models » (p. 16 ; figure 8 vue en image).
- **Frontière.** Les cinq atténuations instantanées et la base tombent sur une droite : R² de 0,88, 0,80 et 0,90 avec six points par jeu (p. 6 ; recalcul 0,876, 0,801, 0,904). « Each gains Resistance only by losing Receptivity » (p. 1) ; « Each method chooses where on the line to stand and none stands above it. » (p. 6).
- **Raisonnement préalable.**
  - Écart à la droite : +3,3, −0,6 et −1,9 points (p. 7 ; recalcul +3,31, −0,55, −1,87).
  - Sur les sujets dérivables, +7,2 points de résistance et +9,6 de réceptivité, intervalles excluant zéro (tableau 3, p. 7).

### 4.2 Limites, réserves
- **Limites reconnues par les auteurs (p. 9) :**
  - pairs scriptés ;
  - un seul gabarit par condition (« robustness to paraphrase goes unmeasured » vise la reformulation du gabarit : faux ami de la paraphrase de confiance) ;
  - « the design does not include a content-free placebo » ;
  - des méthodes d'origine à plusieurs tours rendues en une passe (« single-pass renderings of methods originally stated with more turns » ; « Multi-turn versions might sit elsewhere on the same frontier. ») ;
  - un partage dérivable / rappel fait après avoir vu le motif ;
  - un juge non validé contre des humains.
- **La phrase « Rising above requires new information rather than new wording. » (p. 3) est une prédiction de cadrage**, posée avant les résultats (« These are the two predictions the results test », p. 3). Elle est appuyée par une droite à six points par jeu.
- **La droite est ajustée à travers les six points, et aucun écart par méthode instantanée n'est imprimé.** Recalcul (tableau 6) : la distillation de la question est la seule méthode instantanée au-dessus de la droite sur les trois jeux (+1,94, +1,26, +1,25 point ; calcul). Ces écarts sont sans incertitude et ne prouvent rien. Ils interdisent seulement d'écrire comme un fait testé que cette consigne « n'élève pas au-dessus de la frontière ».
- **Incohérence mineure.** La phrase « an interval whose lower bound does not admits improvement » (p. 7) est fautive, et l'intervalle de l'écart de +3,3 points sur le premier jeu n'est imprimé nulle part (le tableau 12, p. 15, vu en image, ne donne que les deux autres jeux). Les tableaux 1, 2, 3 et 6 recalculés concordent.

### 4.3 Verdicts par composante (2608.11247)

| composante | verdict | appui | pages |
|---|---|---|---|
| (a) paraphrase de confiance | **voisin ; deux indices indirects, de sens partiellement opposés** | (i) **forme rhétorique** : une affirmation « absolument certaine » déplace **moins** qu'une affirmation nue, dans 21, 21 et 23 modèles sur 23 ; une réécriture qui neutraliserait l'emphase retirerait donc, dans ce dispositif, un indice de méfiance, dans le même sens que le contre-indice du niveau 3. **Mais** une raison d'une ligne déplace un peu **plus** (+2,1, +0,1, +3,2 points ; seulement 14, 12 et 16 modèles) : la retirer irait dans l'autre sens. L'effet net d'une paraphrase dépend donc des marqueurs qu'elle ôte. (ii) **principe** : les consignes de résistance testées déplacent le long d'un compromis entre résistance et réceptivité (six points par jeu), et les auteurs prédisent puis trouvent qu'un gain sur les deux axes demande une information extérieure à l'échange (p. 3, 7). **Limites** : répondants et non moniteurs ; pairs scriptés sans argument à préserver ; aucune réécriture par un modèle de confiance ; la distillation de la question est une consigne en une passe, au-dessus de la droite dans le recalcul (sans incertitude), et sa forme d'origine n'est pas lue | 3, 4, 5, 7, 9, 13, 16 |
| (b) quorum par type d'accès | **voisin** | un membre qui voit le verdict des autres se conforme : « A single miscalibrated agent can, therefore, pull a whole group off a correct answer » (p. 1) ; un dissident n'aide que s'il dit juste (p. 8). L'argument « information from outside the exchange » (p. 7) plaide en principe pour un membre d'un autre type d'accès, mais rien n'est testé : ni moniteurs, ni sondes, ni règle de décision | 1, 7, 8 |
| (c) matrice de transfert | **ne touche pas** | — | — |
| (d) mesure sous attaques de corruption | **ne touche pas** | pression fixe, scriptée, non optimisée, portée sur des répondants | 9 |

**Verdict pour l'article : « voisin »** (« ne touche pas » pour c et d).

**Leçon de mesure transposable, non testée.** Une contre-mesure se note sur deux axes : résister à la pression fausse et rester réceptif à la correction juste. C'est l'esprit du plan « rhétorique × intention » de EC.2 (programme l. 195). Une paraphrase de confiance devrait se mesurer aussi sur ce que les juges perdent quand l'agent plaide sincèrement et à juste titre.

### 4.4 Notes à part, sans verdict
- **Pour HC6.**
  - L'article mesure un déplacement sous pression bénigne fixe, analogue d'un g par modèle, sans aucune attaque optimisée.
  - La résistance n'est pas stable d'un jeu à l'autre : « so steadiness on one benchmark guaranties nothing on another » (p. 5 ; rangs 0,97, 0,74 et 0,65, auteurs ; figure 4, vue en image).
  - Le déplacement suit la compétence : « Conformity decreases as baseline accuracy increases » (p. 5 ; r = −0,64, auteurs ; figure 3, vue en image).
- **Pour HC1 et EC.1.** Le nombre de pairs domine l'emphase (p. 4-5), la certitude affichée persuade moins (p. 5, 16), et l'effet d'une raison n'est pas partagé par tout le groupe de modèles (p. 16). C'est la famille « approbations forgées », en version pairs.

## 5. Notes hors mandat, sans verdict
- **Pour HC2 et HC4.** 2601.04603 est une campagne d'attaques par contenu, en boîte noire, contre un système dont le premier étage est une sonde linéaire à agrégation par moyenne mobile (p. 6, 9) : une vulnérabilité à haut risque en environ 198 000 requêtes (p. 9), sans que l'étage franchi soit connu.
- **Pour H5.** La figure 3b de 2601.04603 (p. 8) mesure la co-variation des scores entre types de lecteurs, sans intervalle et sans isoler le type d'accès (section 3.3).

## 6. Ce qui reste revendicable (formulation exacte)

« Dans le contrôle d'un agent non fiable, un quorum qui réunit des **juges génératifs** et des **sondes qui lisent l'agent lui-même**, auteur des attaques de corruption du jugement. Chaque membre y lit tout le contenu, et la règle de décision est telle que la corruption d'un seul membre ne suffit pas à faire passer une action. À cela s'ajoutent la **matrice de transfert de ces attaques de corruption** entre juges et sondes, cellule par cellule et dans chaque sens, et l'effet de la **paraphrase de confiance** sur cette matrice, mesuré sur les deux axes : résistance à la pression fausse, réceptivité à l'argument juste. »

**Précisions :**
- cette formulation s'oppose à la cascade publiée, où la sonde filtre seule ce que le lecteur textuel verra (2601.04603, p. 9) ;
- l'idée d'hétérogénéité par type d'accès (lecteur textuel et sonde du modèle producteur) n'est pas revendicable comme telle ;
- la formulation vaut **au regard des deux pièces lues seulement**. Hua et collègues et McKenzie et collègues restent à lire (section 8), et les pistes du constat M9 hors de ce mandat aussi.

## 7. Ce qu'une phrase publique sur HC5 ne doit pas affirmer
- Qu'aucune combinaison de sondes internes et de classifieurs textuels n'a été publiée ni éprouvée sous attaque adverse (2601.04603, p. 1, 2, 8, 9).
- À l'inverse, que l'ensemble publié est un quorum, ou qu'un quorum de sondes et de classifieurs a été éprouvé sous attaque. C'est une cascade en série où la sonde laisse passer seule environ 94,5 % du trafic (p. 9).
- Que 2601.04603 est la première ou la seule combinaison publiée de sondes et de classifieurs. La pièce nomme McKenzie et collègues (p. 10), et un travail sur la combinaison de moniteurs d'exécution (Hua et collègues, p. 10, 12), tous deux non lus.
- Quoi que ce soit sur Hua et collègues au-delà de ce que la pièce en dit : la combinaison de plusieurs moniteurs sous contrainte de coût.
- Que l'hétérogénéité par type d'accès est établie comme cause de l'indépendance des erreurs (non isolée ; scores et non erreurs ; sans intervalle).
- Que le système de production de 2601.04603 est plus robuste que les précédents : aucun écart n'est établi (section 3.3).
- Que l'équipe rouge de 2601.04603 a attaqué la sonde, ou qu'elle était adaptative au sens d'une attaque optimisée contre un membre.
- Que les sondes résistent aux attaques par contenu au vu de cette pièce.
- Que la paraphrase de confiance est appuyée par les pièces lues. Elles donnent trois indices indirects, aucun sur une réécriture de confiance ni sur un moniteur :
  - une sortie lue hors de son contexte est plus facile à obscurcir (2601.04603, p. 3-4) ;
  - une affirmation emphatique déplace moins qu'une affirmation nue, et une raison d'une ligne un peu plus (2608.11247, p. 4, 5, 16) ;
  - des consignes de résistance échangent résistance contre réceptivité (2608.11247, p. 6, 7).
- À l'inverse, que ces pièces montrent qu'une paraphrase de confiance échoue : aucune ne la teste.
- Que 2608.11247 teste des moniteurs, une paraphrase ou un quorum.

Je ne rédige pas la phrase publique (rôle exclu).

## 8. Voisins nommés dans les pièces et non lus
- **À lire avant toute phrase sur le quorum :**
  - Hua et collègues 2025, « Combining cost-constrained runtime monitors for AI safety », arXiv 2507.15886 (2601.04603, p. 10, 12). Combinaison de moniteurs d'exécution sous contrainte de coût ; la pièce ne dit pas si une sonde en fait partie ni quelle règle est étudiée ;
  - McKenzie et collègues 2025, « Detecting high-stakes interactions with activation probes », arXiv 2506.10805 (p. 10, 12). Selon la pièce, « similarly investigate softmax-weighted probes and classifier cascades » : seconde combinaison publiée de sondes et de classifieurs, à lire au même rang.
- **À lire avant toute phrase sur la paraphrase :** Zhu et collègues 2025 (ACL ; 2608.11247, p. 2, 9, 11), qui ont introduit « Devil’s Advocate and Question Distillation » (p. 2). C'est la forme d'origine, à plusieurs tours, de la distillation de la question.
- **Priorité basse :**
  - Cunningham et collègues 2025, billet sur la réutilisation des représentations (p. 10, 12) ;
  - les deux fiches de système d'un autre fournisseur, filtre thématique léger puis classifieur coûteux (p. 10, 12-13) ;
  - Sharma et collègues 2025, arXiv 2501.18837 (p. 1, 13) ;
  - Youstra et collègues 2025, arXiv 2508.17158 (p. 5, 13) ;
  - Zou et collègues 2024, arXiv 2406.04313 (p. 10, 13) ;
  - Casper et collègues 2024, arXiv 2403.05030 (p. 10, 12) ;
  - Weng et collègues 2025 (2608.11247, p. 2, 11) ;
  - Baltaji et collègues 2024 (p. 2, 9) ;
  - Khan et collègues 2024 (p. 2-3, 10) ;
  - Wan et collègues 2024 (p. 3, 11) ;
  - Turpin et collègues 2023 (p. 3, 11).
- **Hors de ce mandat, non lus :** les pistes du constat M9 (He et Yu, quorums à fautes corrélées ; « BRANCH » ; « Screwtape »).

## 9. Suite donnée à la contre-lecture

| constat | gravité | décision | où dans la version 2 | motif |
|---|---|---|---|---|
| A — La cascade est en série : la sonde décide seule de presque tout le trafic | majeur | corrigé | sections 1, 3.1 (« Comment l'ensemble décide »), 3.4 ligne (b), 6, 7 | relu p. 9 : « Otherwise, we rely solely on the probe. » (section 5.3) et, pour la production, l'escalade seule est décrite. Le refus exige la sonde au-dessus du seuil d'escalade : faire taire la sonde suffit. Je retiens « laisse passer seule » plutôt que « décide seule », car l'article ne décrit pas le sort du trafic non escaladé en production |
| B — « Mesure sous attaque : occupée en partie » contredit la définition du rapport | majeur | corrigé | sections 2, 3.1 (« Sous quelles attaques »), 3.4 lignes (b) et (d) | ma définition de (d) par les cinq familles de corruption rendait « occupée en partie » incohérent. (d) devient « voisin », et l'épreuve d'équipe rouge passe sous (b). Je garde une ligne (d) parce que mon mandat la nomme, en notant qu'elle se confond avec (c) dans N-006 et N-013. « Adaptative » est remplacé par « itérative, en boîte noire » (le mot n'apparaît qu'au sens du calcul, p. 5, 10) |
| C — La complémentarité n'est pas attribuée au type d'accès de façon isolée, et ce n'est pas une mesure d'erreurs | majeur | corrigé | sections 3.1 (« Ce que lit chaque membre », « Résultats »), 3.3 (« Complémentarité »), 7 | relu p. 7, 8, 9 : la légende dit « Spearman rank correlation between classifier predictions on jailbreak attempts » ; la capacité, les étiquettes et le modèle lu diffèrent avec le type d'accès ; le jeu statique vient de campagnes non nommées. La sonde ne lit le modèle producteur de façon établie qu'en production (p. 9) |
| D — La réserve statistique est trop faible : aucun écart entre systèmes n'est établi | majeur | corrigé | section 3.3 (« Statistique ») | tests recalculés par mon propre script : production contre génération précédente, p unilatérale 0,149 ; trois nouveaux réunis, 0,045 (bilatérale 0,074). Les chiffres du contre-lecteur se retrouvent. Ma phrase de la version 1 était ambiguë |
| E — Poids optimisé sur le test confirmé ; incohérence d'unité de la figure 5 non vue | mineur | corrigé | section 3.3 (« Ensemble », « Incohérences mineures ») ; journal | figures 4, 5 et 6 vues en image : la figure 5 est en fractions sous l'étiquette « % » (environ 0,014 à 0,15 contre environ 1,4 à 14,5 % à la figure 2b) ; la figure 6b montre un minimum plat autour des poids égaux |
| F — Paraphrase : contre-indice direct manquant, portée trop large | majeur | corrigé | sections 4.1, 4.2, 4.3 ligne (a), 7 | relu p. 3, 4, 5, 7, 9, 13, 16 et la figure 8 en image. J'ajoute le contre-indice de la certitude, mais je le donne avec son pendant que le contre-lecteur ne pèse pas : une raison d'une ligne déplace un peu plus (+2,1, +0,1, +3,2 points ; 14, 12, 16 modèles, p. 16). L'effet net d'une paraphrase dépend donc des marqueurs ôtés. La p. 3 est présentée comme une prédiction ; « distillation au-dessus de la droite » est recalculé (+1,94, +1,26, +1,25) ; la faute de la p. 7 est relevée |
| G — Voisins non lus : deux manques et un rappel de périmètre | majeur | corrigé | sections 6, 7, 8 | relu p. 10 et 12 de 2601.04603 et p. 2 et 9 de 2608.11247 : McKenzie et collègues sont remontés au rang de Hua et collègues ; Zhu et collègues sont nommés pour la paraphrase ; les fiches de système de la p. 10 sont ajoutées ; les pistes M9 sont déclarées hors du mandat |
| H — « Ce qui reste revendicable » : deux précisions | mineur | corrigé | section 6 | la distinction « chaque membre lit tout, la corruption d'un seul ne suffit pas » découle du constat A, et la validité est bornée aux deux pièces lues |
| I — Renvois de page et silences à écrire | mineur | corrigé | sections 1, 3.1, 3.3 | la p. 8 ne parle pas des 1 700 heures : pages justes 1, 2, 9 ; les remerciements (p. 11) et la portée « programme de primes » sont ajoutés ; la lecture du modèle producteur en statique suit le constat C ; aucun chiffre pour le signalement bénin (p. 8) |

**Remarque sur la profondeur.** Le contre-lecteur note l'absence d'heures par étape dans mon journal de la version 1 : c'est exact. Le journal de la version 2 date chaque étape par `date -u`.

Les deux fichiers que le contre-lecteur dit non nommés dans son mandat sont nommés dans le mien :
- `anteriorite-v1.md`, l. 293-312, est nommé par le mandat du lecteur ;
- les interdits communs v2 sont nommés par la consigne commune.

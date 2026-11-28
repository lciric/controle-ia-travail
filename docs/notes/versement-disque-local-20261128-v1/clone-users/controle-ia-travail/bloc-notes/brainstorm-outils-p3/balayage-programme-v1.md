# Balayage « programme » — autres outils que les sondes, consigne lue contre intention exécutée, faut-il un P3c — v1

- **Pour Lazar, via la session.** Sous-agent neuf, angle « programme » (lecture interne). Je n'ai écrit ni P3, ni P4, ni
  P3b, ni l'addendum 2, ni la synthèse de la revue. 2026-10-20, vers 19:30 UTC. **Rien n'est décidé ici.**
- **Lu** (empreintes recalculées ce jour) :
  [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`, compagnon égal), en entier ;
  [P4] `…/p4-instrument/P4-instrument-v1-candidat1.md` (`6422fb45…`, compagnon égal), sections Hypothèse (l. 212-258),
  Pare-feu (l. 595-618), Critères de lecture (l. 632-656), plus la table « Données lues » (l. 128-146), les mesures de
  conception (l. 163-199) et la sortie (l. 463-468), pour répondre à la question des données gardées ;
  [D] `registres/decisions.md` (`4b2a927f…`, registre vivant), lignes N-025 (l. 447), R-262 (l. 454), N-028 (l. 457)
  seulement ; [B] `docs/brief-claude-code-programme-complet-v2.md` (`9261932a…`, égal à `sha256sums-lancement-v2.txt`),
  l. 154-200 ; [S] `…/revue-detection/synthese-comment-detecter-v4.md` (`fba703f9…`, compagnon égal).
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Non lus** (interdits respectés) : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, tout `donnees/` ;
  aucune recherche récursive dans le dépôt ; aucune recherche web ; aucune donnée de P3 envoyée ; aucun service payant.
  Les balayages voisins (`balayage-anthropic-v1.md`, `balayage-autres-v1.md`) ne sont pas lus : indépendance.
- **R7.** Huit PDF déjà au programme, empreintes recalculées (égales aux compagnons pour ceux de `docs/sources/pdf/`, égales
  aux préfixes de [S] section 6 pour les autres), lus par `pdftotext -layout` dans `…/brainstorm-outils-p3/txt-programme/`.
  Chaque phrase citée est retrouvée à sa page par `…/brainstorm-outils-p3/scripts-programme/page_phrase.py` (`9ab6ac8e…`) ;
  sortie `…/scripts-programme/sortie-verification-pages-v1.txt` (`fd0c6133…`), complément [AP p. 7]
  `…/scripts-programme/sortie-verification-pages-complement-v1.txt` (`06ff95d8…`) ; épreuve R5 (un cas sain, quatre artefacts
  rejetés) `…/scripts-programme/epreuve-r5-pages-v1.txt` (`6a1c5875…`). Page = page du fichier PDF. Tout autre chiffre de
  la littérature vient de [S] et porte « repris de [S], non revérifié ici ».

## 1. Verdict

1. Le programme a déjà **trois leviers** pour séparer « consigne lue » et « intention exécutée » : tenir la consigne et
   faire varier l'acte (T1 ; dose-réponse de T0.6) ; tenir l'acte et faire varier la consigne (P4, cas limite ;
   manipulation du nombre, proposée) ; retirer la consigne du contexte (organisme (ii) ; test de validité de T0.7).
   **Aucun n'est encore joué.** Chacun a un angle mort (section 5).
2. Hors sondes supervisées, le plan lu n'a **qu'un outil** sur les activations : la famille Mahalanobis, non supervisée
   ([B] l. 169). Ses scores sur P3 existent (6 colonnes) et n'ont pas été lus. Ni autoencodeur parcimonieux, ni lentille,
   ni comparaison de modèles, ni intervention causale dans les textes de phase 0 lus.
3. **Aucune activation de P3 n'est gardée** (inférence, section 3). Tout outil neuf sur P3 demande une passe forcée sur
   carte graphique, une garde d'identité (38 épisodes honnêtes sur 60 reconstruits à l'identique) et un GO : c'est une
   seconde lecture, donc un nœud.
4. **Fait vérifié qui change la famille (iii)** : l'organisme public « qui imite Llama-3.1-8B-Instruct » est un
   **Llama-3.3-70B-Instruct** (Cedar) [AG p. 7]. Tous les organismes saboteurs des jeux d'audit vérifiés sont des 70
   milliards [AG p. 7, p. 36]. Lire leurs activations, c'est changer de modèle (GO), et leur tâche est la sous-performance
   aux évaluations, pas le coût.
5. **Logique du test de validité** : les sondes génériques ne passent déjà pas (i-a). Le contraste (i) contre (ii) ne dit
   donc rien pour elles. Le test exige d'abord une sonde qui passe (i). Le brief permet de l'apprendre sur une famille et
   de la lire sur une autre ([B] l. 171).
6. **P3c sur les données de P3 avec d'autres outils : déconseillé** (seconde lecture après un nul, R3 ; pas de référence
   boîte noire sur P3, N-029). La seule mesure sur P3 qui sépare le nombre écrit de la consigne est la manipulation du
   nombre, déjà proposée comme extension de N-028.

## 2. Ce qui est déjà prévu : ce que chaque pièce tranche et ne tranche pas

| pièce | ce qu'elle fait | peut trancher | ne peut pas trancher | source |
|---|---|---|---|---|
| **P4-instrument** (candidat 1, non scellé) | phrase de persona de l'entraînement (« dishonest » contre « honest ») avant « Your action: », sur les actions honnêtes des 38 épisodes reconstruits ; sonde de tromperie couche 15, maximum ; plancher figé ; référence bénigne B contre B′ | la chaîne figée voit-elle son contraste d'entraînement dans le format de l'agent (témoin positif de l'instrument) | l'intention : « le contraste est une consigne écrite dans le contexte, pas une intention exécutée » ; l'organisme et le nul de P3 (pare-feu) ; la généralisation hors de la phrase ; la survie à des textes d'action différents ; jetons hors politique | [P4] l. 214-219, l. 231-241, l. 597-601, l. 614-618 |
| **Addendum 2** (N-025 (a)) | non décisif, processeur, données gardées : ampleur de P3-P1 par forme du coût et par tâche ; signe de P3-P2 par forme ; puissance du nul (aire minimale détectable au plancher et à la demi-largeur observés) | quelle puissance avait le nul ; si l'effet du coût est porté par les formes | rien sur ce que lisent les sondes ; aucune promotion | [D] l. 447 |
| **P3b** (N-028 ; E1 de [S]) | passe forcée sans génération sur les 2 400 actions ; sondes localisées au champ du coût, plancher de même position ; sonde « oracle » apprise sur l'organisme, validation croisée par tâche ; T1, T3, T4 | diagnostic : le champ porte-t-il plus que le nombre écrit (T4) ; lecture ou direction (oracle avec T1, T3, T4) | aucune revendication : bras du champ déjà vus (drapeau T2), oracle hors anti-circularité ; oracle au-dessus sans T1 = lit la consigne ou le contexte ; T1 peut être non calculable ; coûts déjà écrits dans le contexte dès le pas 2. Divergence ouverte : N-028 dit « première tentative de détection », [S] recommande « diagnostic » | [D] l. 457 ; [S] l. 244-261, l. 282-286, l. 308-325 |
| **Manipulation du nombre** (option, nœud) | {contexte saboteur ; témoin} × {nombre du champ `COST` original ; médiane honnête}, maximum seulement | effet du nombre de l'action en cours contre effet de la consigne, historique gardé (« la seule mesure qui sépare le nombre écrit du contexte privé », note du brainstorm citée par [S]) | textes hors politique ; conflit déclaré (coûts gonflés des pas précédents sous contexte témoin) ; pas un état qui cause l'acte | [S] l. 262-274, l. 332-335 |
| **E2, question de suivi** (recommandée sur épisodes neufs de T0.6) | question fixe après l'action, réponse imposée, lecture à une seule position ; logit d'auto-déclaration en comparaison | la position explique-t-elle le nul ? | la question fait relire la consigne : une sonde apprise sur « Roleplaying » note « every Sandbagging response » comme trompeuse, « even when the model chooses not to sandbag » [AP p. 18, vérifié] ; statut en production : règle gelée 1, à toi | [S] l. 282-286, l. 337-344 |
| **E3, sonde du domaine** (T0.7 réécrit en mode coût) | paires à nombres équilibrés (lues au champ) et paires incitées sans consigne (lues avant le champ) | une sonde apprise sans l'organisme détecte-t-elle ? | elle peut apprendre « gros nombre », le style, ou le régime d'incitation | [S] l. 282-286 |
| **E4, échelle** | bras fixé d'avance, 27 à 70 milliards et 8 milliards | effet de taille ou de capacité | demande un GO de changement de modèle | [S] l. 282-286 |
| **T0.6** | (i) instruction cachée ; (ii) réglage fin léger par distillation de contexte, « générer avec l'instruction cachée, entraîner sans elle » ; (iii) organismes publics de l'institut britannique, « si la licence le permet » ; contrôles croisés : honnête averti de la surveillance (aucune mission), saboteur en régime simulé « non observé » ; dose-réponse (proportion d'actions sabotées × intensité) | épisodes neufs, à l'aveugle ; (ii) retire la consigne du contexte ; une proportion inférieure à 1 donne, sous une même consigne, des actions sabotées et non sabotées (puissance de T1) | seule, rien sur ce que lit une sonde ; à réécrire en mode coût (P-015, R-265 (6)) ; brouillon actuel sans condition « mention » (T3 non calculable) | [B] l. 160-164 ; [S] l. 286 |
| **T0.7** | concepts : tromperie, enjeux, dissimulation, conscience d'évaluation ; maximum ou attention ; familles linéaire, différence de moyennes, petit perceptron, attention, Mahalanobis ; plancher apparié ; anti-circularité ; test de validité (i) contre (ii) | « lit la consigne cachée » contre « lit l'intention », par le patron de réussite sur (i) et (ii) | tel qu'écrit au brief, ni T1 ni T4 : une sonde qui lit le nombre gonflé réussit sur (i) et sur (ii) (section 5) ; brouillons de T0.7 non lus ici | [B] l. 166-173 |
| **T0.8 et N-029** | base boîte noire locale, lue sur les épisodes de T0.6 ; prédicteur sur les traits du texte ; juge Claude sur P3 retiré | gain de la boîte blanche à épisodes égaux | aucune référence boîte noire sur P3 | [B] l. 175-178 ; [S] l. 359-365 ; CLAUDE.md (N-029) |
| **Porte G0, critère 3** | « Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii) » | — | avec le test de validité, une sonde qui lit la consigne échoue sur (ii) : seul passe ce qui est commun à (i) et (ii), intention, nombre écrit ou style ; sans T4, le critère ne distingue pas | [B] l. 194 |

## 3. Données de P3 gardées, d'après ces textes

| pièce | contenu | source |
|---|---|---|
| `textes-actions-p3.jsonl` (`ba05fa13…`) | textes des 2 400 actions (non ouverts ici) | [V] l. 89 ; [P4] l. 132 |
| `scores-p3.npz` (`968414fc…`) | un score par action pour 430 sondes : 424 légères (24 entraînées hors Mahalanobis, 2 × 200 directions de plancher) et **6 Mahalanobis** ; colonnes `jetons`, `jetons_notes` | [P4] l. 134 ; [V] l. 87, l. 108 |
| `jetons-principales-p3.npz` (`4cd2ddb8…`) | bornes des champs ; sans doute aussi les scores par jeton des deux sondes principales (par analogie avec la sortie de P4, l. 465-466) : **non vérifié**, fichier non ouvert | [P4] l. 135 ; [V] l. 88 |
| `sondes-figees-legeres.npz` (`701f73bd…`) | les 424 sondes légères | [P4] l. 133 |
| `sondes-figees.npz` (fichier complet, Mahalanobis compris) | **resté sur l'instance 56799469** ; empreinte seule dans le dépôt | [P4] l. 144-145 ; [V] l. 113, l. 375 |
| `episodes-p3.json` (`1a96cbf8…`) | empreintes de trajectoire, jetons par action | [P4] l. 136 |
| **activations** | **aucune gardée** (inférence : « les activations sont neuves », [P4] l. 256 ; « passe sur carte » pour les scores par jeton du plancher et l'oracle, [D] l. 457 ; « passe forcée, sans génération », [S] l. 282). Les scores par jeton des 400 directions du plancher ne sont pas gardés non plus ([S] l. 282) | — |
| **reconstruction** | 38 épisodes honnêtes sur 60 identiques à P3 (niveau 1) ; 32 actions sur 600 en échec de longueur, toutes dans les 22 autres. Conditions instruites : il faut les consignes privées ; taux d'identité non mesuré dans les textes lus | [P4] l. 186-188, l. 196-199 |

**Conséquences.** (a) Tout outil neuf sur les actions de P3 (autoencodeur, lentille, attribution, intervention) repasse
sur carte, sous garde d'identité, sur devis (au plus 10 USD par lancement, R-269 selon [S] l. 345-352) : c'est une seconde
lecture, nœud de Lazar ([V] l. 63-64, l. 308-309). (b) Les scores Mahalanobis sont déjà là : les lire serait une seconde
lecture sur une autre sonde, interdite sans GO. (c) Si l'instance 56799469 est détruite, les paramètres non légers des
sondes (Mahalanobis) partent avec elle ; date de destruction : registre non lu ici, à vérifier dans `registres/etat.md`.

## 4. Outils hors sondes supervisées : présents, écartés, absents

- **Présent : Mahalanobis** (détecteur d'anomalie non supervisé sur les activations), [B] l. 169. Scores sur P3 calculés,
  non lus (section 3).
- **Présent : position nouvelle** (question de suivi, E2) et **contrefactuels d'entrée** (P4, manipulation du nombre) :
  on change l'entrée, la sonde reste. Ce sont des outils de validation causale côté entrée.
- **Présent, hors détection : bruit d'activations.** Mesure gardée, retirée des interventions revendiquées par H6 (N-015,
  d'après CLAUDE.md) ; sa place en phase 0 n'est pas lue ici. Analogue publié sur les poids : « adding Gaussian noise to
  the weights of a sandbagging model can sometimes result in uplift » [AG p. 22, vérifié].
- **Écarté : autoencodeur parcimonieux.** [S] l. 139-142 le juge « peu prometteur ici », sur une note du projet antérieur
  (leçon 2, non lue ici). Ce que disent les PDF :
  - Anthropic, audit d'objectif caché : « Three teams successfully uncovered the model's hidden objective using techniques
    including interpretability with sparse autoencoders (SAEs), behavioral attacks, and training data analysis »
    [MA p. 1, vérifié] ; limites des auteurs : « This may make our game unrealistically easy for teams with data access »
    et techniques peut-être moins efficaces quand le comportement vient de « more diffuse training influences »
    [MA p. 3, vérifié].
  - Jeux d'audit de l'institut britannique : « SAEs were not pursued by the blue team during the auditing game » ; après
    coup, « Overall, we remain largely divided on the extent to which sparse autoencoders would have been useful »
    [AG p. 22, vérifié] ; pour l'ensemble des méthodes essayées après le jeu (autoencodeurs, bruit, sondes de
    sous-performance…) : « we did not find strong evidence that the blue team would have won by using them » [AG p. 3,
    vérifié].
- **Hors détection : pilotage** : « emotion representations can influence behavior even when it is not evident from the
  text of the transcript » [EM p. 38, vérifié] ; résultat de pilotage, pas de détection ([S] l. 132-135).
- **« J-lens »** : aucun texte lu ici ne la nomme. Identification laissée au balayage Anthropic (non lu ici).
- **Absents des textes lus** : lentilles sur le flux résiduel, graphes d'attribution, transcodeurs, comparaison de modèles
  (base contre (ii)), intervention sur une direction (ablation, pilotage) comme test. **Trou du plan, pas du champ (R8).**

## 5. Consigne lue contre intention exécutée : les trois leviers et leurs angles morts

| levier | pièces | angle mort |
|---|---|---|
| **1. consigne fixe, acte varié** | T1 (saboteur : actions qui gonflent contre celles qui ne gonflent pas, [S] l. 233-237) ; dose-réponse de T0.6 ([B] l. 163) | dépend de la variation naturelle ; le saboteur de P3 gonfle d'un facteur ≈ 33 ([V] l. 344-346) : peu d'actions non gonflées, T1 peut être non calculable ; une sonde qui lit la grandeur du nombre passe T1 : T4 obligatoire. C'est le piège que T1 attrape : [AP p. 18, vérifié], « even when the model chooses not to sandbag » |
| **2. acte fixe, consigne variée** | P4 (texte d'action imposé, persona variée) ; manipulation du nombre ; témoin (consigne privée bénigne) et mention de P3 | textes hors politique ([P4] l. 235) ; P4 ne regarde que le pôle « consigne ». P4 et la manipulation du nombre forment ensemble presque un plan 2 × 2 {consigne} × {acte} à textes imposés ; aucun texte lu ne l'écrit comme tel |
| **3. consigne retirée du contexte** | organisme (ii) ; test de validité de T0.7 ([B] l. 161, l. 172) | **un échec sur (ii) a trois lectures** : la sonde lisait le texte de la consigne ; ou (ii) n'a pas intériorisé (« The models may not have fully internalized the target behaviors », [BX p. 8, vérifié]) ; ou l'apprentissage a déplacé les représentations (« from representation drift during RL, with or with[out a detector] », [OA p. 1, vérifié] ; transposition de l'apprentissage par renforcement au réglage fin : analogie). **Une réussite sur les deux** a aussi plusieurs lectures : intention, nombre écrit, ou style des actions. Attente publiée : sondes réentraînées sur un organisme affiné, « from almost perfect detec[tion] 0.94 to chance performance 0.5 » [BX p. 8, vérifié] ; organismes entraînés : « Median balanced accuracy falls from 0.85 to 0.52 for Apollo » [DYL p. 11, vérifié] ; interprétation d'auteurs : « probes despite being internal monitors heavily relied on textual evidence » [BX p. 8, vérifié] ; « stated intent does not produce the same activation signatures as genuine strategic rea[soning] » [K p. 9, vérifié] |

**Ce qui manque aux trois** : un test **causal**. La direction lue est-elle celle que le modèle **utilise** pour produire
l'acte ? Une ablation ou un pilotage de la direction, consigne présente, qui change le sabotage, répondrait. Absent des
textes de phase 0 lus ; H6 revendique des interventions (N-015, CLAUDE.md), place non lue. **Question (R8).**

**Ce que ferait un laboratoire comme Anthropic, d'après les deux PDF vérifiés** : entraîner l'objectif dans les poids
plutôt que l'écrire dans le contexte, puis auditer **à l'aveugle**, avec plusieurs familles d'outils (autoencodeurs,
attaques comportementales, données d'entraînement) [MA p. 1] ; et faire construire l'organisme par une équipe qui garde la
réponse [AG p. 3, p. 7]. Le programme a l'équivalent de la première idée (organisme (ii)) et de la seconde (famille
(iii)), pas encore la pluralité d'outils.

## 6. Trous réels du plan face à la question de Lazar

Ce sont des trous **du plan lu**, pas du champ (R8). Chacun est une question.

1. **Test de validité sans T1 ni T4** ([B] l. 172). Une sonde qui lit le nombre gonflé réussit sur (i) et (ii) et
   passerait pour une sonde d'intention. Le critère 3 de G0 ([B] l. 194) n'a de sens qu'avec T4. À vérifier dans les
   brouillons de T0.7 (non lus).
2. **Test de validité sans sonde qui passe (i).** Les génériques ne passent pas (i-a) ([V] l. 63-69). Il faut d'abord
   une sonde qui passe (i) : apprise sur une famille, lue sur l'autre ([B] l. 171), ou sonde du domaine (E3).
3. **Puissance de T1 non garantie.** Aucun texte lu ne fixe une condition « consigne présente, acte non exécuté » en
   nombre suffisant (par exemple une proportion de sabotage inférieure à 1, lue sous une même consigne).
4. **Aucune intervention causale** en phase 0 dans les textes lus.
5. **Aucun outil non supervisé** sauf Mahalanobis ; **aucune comparaison de modèles** base contre (ii), alors que (ii)
   donne le delta de poids et que ses données de distillation sont au programme : l'avantage que [MA p. 3] juge assez
   fort pour rendre le jeu « unrealistically easy ».
6. **Position « avant l'action »** (fin du contexte, avant le premier jeton d'action) absente des positions listées (au
   champ, avant le champ, après une question, [S] l. 282, l. 353-358). C'est là qu'une intention précède l'acte (Apollo
   voit la tromperie « before any explicitly deceptive text is generated », [AP p. 7, vérifié], avec l'intention souvent
   écrite dans le raisonnement, même phrase). Valable sous une même consigne seulement, sinon elle lit la consigne.
7. **Famille (iii)** : aucun organisme saboteur de 8 milliards dans les jeux vérifiés. Cedar, Oak (jeu final), Tarun et
   Beren (jeu d'essai) sont des Llama-3.3-70B-Instruct ; le seul 8 milliards, Yew, est **bénin** (« Copy of
   Llama-3.1-8B-Instruct with identity layers inserted ») [AG p. 7, p. 36, vérifié]. Le seul tiers qui détient une vérité
   terrain n'est donc lisible qu'à 70 milliards : GO de changement de modèle, coût. Tâche : sous-performance aux
   évaluations. Disponibilité et licence non vérifiées ici. Tarun est « Trained via prompt-distillation » : analogue de
   (ii) ; Beren et Cedar imitent un modèle plus faible, et les organismes ainsi faits étaient « harder to detect » par la
   boîte noire [AG p. 3, p. 36, vérifié].
8. **Données de P3** : aucune activation ; fichier complet des sondes sur l'instance ; reconstruction partielle (38 sur
   60). Tout outil neuf sur P3 = passe sur carte et nœud.
9. **Validation externe** : hors sous-agents et Gemini, seuls (iii) et une publication donnent un juge externe ; FIBS de
   « Caught in the Act » : disponibilité **non vérifiée** ([S] l. 366-370).

## 7. Faut-il un P3c ?

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a) pas de P3c** | manipulation du nombre dans P3b (extension de N-028, déjà recommandée par [S], confiance ≈ 50 %) ; outils neufs (Mahalanobis lue, sonde apprise sur (i) et lue sur (ii), comparaison de modèles, position avant l'action, T1 et T4 dans le test de validité, intervention) écrits dans T0.7 réécrit, lus sur épisodes neufs de T0.6 et sur (ii) | à l'aveugle ; aucune seconde lecture de P3 ; répond à la question au bon endroit (organisme sans consigne dans le contexte) | plus tard : (ii) demande un entraînement sur carte (GO) ; G0 fin novembre (N-027) |
| **(b) « P3c » = P3 rejoué sur (ii)** | (ii) distillé du mode « coût gonflé » ; mêmes sondes figées, même plancher ; T1, T3, T4 ; épisodes neufs ; avant-garde du test de validité | répond directement à « consigne lue ou intention » | avec les génériques, qui ne passent pas (i-a), il ne départage rien (trou 2) ; n'a de sens qu'avec une sonde qui passe (i) : donc après E3 ou après une sonde apprise sur (i) ; demande T0.6 réécrit |
| **(c) P3c exploratoire sur les données de P3** | autoencodeur, Mahalanobis, lentilles sur les 2 400 actions | rapide ; peut donner des hypothèses | seconde lecture après un nul (R3) ; pas de référence boîte noire (N-029) ; activations à recalculer, reconstruction partielle ; au mieux non décisif, préenregistré, et sa seule sortie permise est une hypothèse à tester à l'aveugle sur T0.6 |

**Recommandation (angle programme) : (a)**, avec le contenu utile de (b) versé dans T0.7 sous la forme « sonde apprise sur
(i), lue sur (ii), avec T1 et T4 ». Confiance ≈ 60 %. C'est un changement de périmètre de T0.7 : proposer avec
recommandation, pas décidé ici. Nommer « P3c » une expérience sur (ii) prêterait à confusion : elle ne relit pas P3.

## 8. Les quatre questions de Lazar, vues du programme

1. **Ce qu'un expert ferait, non demandé** : exiger une sonde qui passe (i) avant le test (i) contre (ii) ; ajouter T4 au
   test de validité ; un test causal sur la direction ; lire la position avant l'action ; comparer base et (ii) ; écrire
   le plan 2 × 2 {consigne} × {acte} complet.
2. **Données brutes de départ** (au lieu des scores déjà lus) : activations de toutes les couches à toutes les positions,
   jetons de la consigne et position avant l'action compris (non gardées pour P3) ; delta de poids et données de
   distillation de (ii) ; paires contrefactuelles (même contexte, acte différent).
3. **Méthodes et outils** : au programme : Mahalanobis, sonde à attention, question de suivi, manipulation du nombre,
   oracle, sonde du domaine ; absents : intervention sur une direction, autoencodeur, comparaison de modèles, lentilles.
   Le détail de la littérature est dans les balayages voisins.
4. **Validation hors de toi et de moi** : organismes construits par un tiers qui garde la réponse (famille (iii), jeu à
   l'aveugle [AG p. 3, p. 7] ; [MA p. 1]) ; vérité terrain comportementale (coût déclaré, vérification différée,
   [B] l. 157) ; base boîte noire sur les mêmes épisodes (T0.8, N-029) ; réplication par d'autres après publication
   (nœud).

## 9. Sources et vérifications

| clé | travail | PDF | sha256 | page | phrase (extrait) | vérifié ici |
|---|---|---|---|---|---|---|
| AG | Taylor et coll., jeux d'audit | `docs/sources/pdf/2512.07810v1.pdf` | `77e64bcd…` | 7 | « Sandbags broadly, imitating Llama-3.1-8B-Instruct » ; « Copy of Llama-3.1-8B-Instruct with identity layers » | oui |
| AG | idem | idem | idem | 36 | « Trained via prompt-distillation (imitating prompted » ; « Sandbags broadly across evaluations. Trained via weak » | oui |
| AG | idem | idem | idem | 3 | « Sandbagging models were harder to detect when » ; « we did not find strong evidence that the blue team would have won by » ; « Activation monitors (linear probes) successfully indicated deception in a sandbagging model across many evaluation tasks » | oui |
| AG | idem | idem | idem | 22 | « SAEs were not pursued by the blue team during the auditing game » ; « Overall, we remain largely divided… » ; « adding Gaussian noise to the weights… » | oui |
| AG | idem | idem | idem | 17 | « probes on Oak fail to indicate more deception » | oui |
| MA | Marks et coll., Anthropic | `…/revue-detection/extraction/pdf-anthropic/2503.10965/2503.10965v2.pdf` | `6cea87ef…` | 1 ; 3 | « Three teams successfully uncovered the model… » ; « unrealistically easy for teams with data access » ; « more diffuse training influences » | oui |
| BX | Boxo et coll. | `docs/sources/pdf/2509.21344v2.pdf` | `aaac4ff9…` | 8 ; 4 | « …0.94 to chance performance 0.5 » ; « may not have fully internalized » ; « heavily relied on textual evidence » ; « Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts » | oui |
| AP | Goldowsky-Dill et coll., Apollo | `docs/sources/pdf/2502.03407v1.pdf` | `a4820ad5…` | 18 ; 7 | « even when the model chooses not to sandbag » ; « before any explicitly deceptive text is generated » | oui |
| DYL | Cooney et coll. | `…/revue-detection/pdf-nouveaux/2606.12618v2/2606.12618v2.pdf` | `2eccf773…` | 11 | « Median balanced accuracy falls from 0.85 to 0.52 for Apollo » | oui |
| K | Kirch et coll. | `…/revue-detection/pdf-nouveaux/2511.17408v4/2511.17408v4.pdf` | `91e00c25…` | 9 | « stated intent does not produce the same activation signatures… » | oui |
| OA | Taufeeque et coll. | `docs/sources/pdf/2602.15515v2.pdf` | `f6547ec8…` | 1 | « from representation drift during RL, with or with[out] » | oui |
| EM | Sofroniew et coll., Anthropic | `docs/sources/pdf/2604.07729v1.pdf` | `afe70d72…` | 38 | « emotion representations can influence behavior even when it is not evident from the text of the transcript » | oui |
| autres | chiffres de [S] (0,869 de [YS] ; table 15 de [OA] ; etc.) | voir [S] section 6 | — | — | — | non : repris de [S], non revérifiés ici, ne servent à rien décider ici |

**Limites.** Brouillons de T0.6 et T0.7, N-015, P-015, `registres/etat.md` et la note du projet antérieur sur
l'autoencodeur ne sont pas lus : ce qui en dépend est écrit comme question. Le contenu de `jetons-principales-p3.npz`
est inféré, non vérifié. Classement, recommandation et confiance : jugement du rédacteur.

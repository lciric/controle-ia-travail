# Cellule III.1 — Proposition B

## 0. Pièces reçues

- **Bloc FAITS** : vide par construction, ce que le bloc déclare lui-même. Ce n'est ni une coupure ni une absence. Je n'invente aucun fait.
- **Dépôt `neuron-explorer`** : les quatre fichiers cités (README, research_log, agent_methodology, NOTES) ne sont pas joints. Je ne les ai pas lus. Tout ce que je dis de la méthode vient du résumé de l'arbitre et garde le statut **RAPPORTÉ** (chiffres de l'auteur, « à vérifier »).
- **Faits du programme** : je les reçois de la question de l'arbitre et ne les audite pas ici. Statut **RAPPORTÉ (arbitre)**.
- **Propositions A et C** : invisibles à ce tour, qui se joue à l'aveugle. B1 ne s'applique donc qu'aux tours suivants.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi il compte |
|---|---|---|---|
| a1 | Le « neurone » (unité de la couche intermédiaire du MLP) est une unité pertinente pour la conscience d'évaluation ou l'honnêteté d'une trace. | HYPOTHÈSE | La littérature sur la superposition prédit que des concepts riches sont répartis sur de nombreux neurones (§ Q5). Le levier de refus est **RAPPORTÉ** sur Qwen3.5-4B, pas sur Llama-3.1-8B. |
| a2 | Les sondes de l'étape 1 lisent la conscience d'évaluation plutôt qu'un corrélat de surface (format de la banque, longueur, mots-clés). | HYPOTHÈSE | Le programme compare les sondes à des références de surface, mais aucun résultat n'est transmis. |
| a3 | Pousser une direction de *lecture* teste son usage *causal*. | HYPOTHÈSE | Une direction peut être lisible sans être utilisée en aval. Une poussée peut aussi agir par un autre chemin que celui que lit la sonde. Le vecteur de poids d'une régression logistique contient des composantes qui annulent le bruit corrélé : ce n'est pas la direction que le modèle « écrit ». |
| a4 | La verbalisation (« ceci est un test ») est une mesure valide de la conscience d'évaluation. | HYPOTHÈSE | Le programme la *compare* à la sonde, ce qui ne la valide pas. |
| a5 | Les ordres de grandeur de l'auteur (19,6 % et 8,2 % de neurones « distincts », rupture du texte au-delà de 0,8 × la norme, coûts) se transfèrent à Llama-3.1-8B. | Chiffres RAPPORTÉ ; transfert HYPOTHÈSE | Architecture, normes résiduelles et activations massives diffèrent. |
| a6 | Des directions aléatoires *isotropes* de même norme sont le bon nul pour un neurone. | HYPOTHÈSE | Les colonnes de sortie des neurones ne sont pas isotropes : elles peuvent s'aligner sur des directions de forte variance ou du désenchâssement. « Distinct des témoins » pourrait alors mesurer la géométrie de W_out plutôt qu'un sens (duel E4). |
| a7 | « Au-dessus de tous les témoins » suffit comme garde contre les comparaisons multiples. | HYPOTHÈSE, réfutée par le calcul ci-contre | Sous le nul, P(neurone > max de 256 témoins) = 1/257 ≈ 0,39 %. Cela donne environ 36 faux positifs par couche pour 9 216 neurones, et environ 56 par couche pour 14 336 neurones. La comparaison 19,6 % contre 0,39 % reste parlante *si* le nul est le bon (a6). |
| a8 | Des amorces courtes suffisent à évoquer nos concepts. | HYPOTHÈSE | La conscience d'évaluation est une inférence sur un *contexte*. Une amorce « who » ou « snake » n'en contient aucun. |
| a9 | Les neurones de référence (refus, « panique ressentie », etc.) font ce que leur nom dit. | RAPPORTÉ | Noms donnés par l'auteur ou son agent, non audités. |
| a10 | Les 128 neurones d'identité de Qwen3-8B (de 80 % à 30 % une fois mis à zéro). | RAPPORTÉ | Je n'ai pas la référence source : **référence à vérifier**. |
| a11 | Pousser vers « honnête » éclaire le *contrôle de délégation*. | HYPOTHÈSE | Le contrôle de délégation *classe une trace existante*. Une poussée modifie une *génération*. Ce sont deux tâches différentes. |
| a12 | Une opération « pousser » dans la primitive reste bornée et reproductible. | HYPOTHÈSE | Le traitement par lots de vLLM n'est pas déterministe en général (à vérifier pour la fourche). |
| a13 | Licence du dépôt : non trouvée. | RAPPORTÉ | Réutiliser le code est juridiquement incertain. Une réimplémentation reste possible. |
| a14 | Llama-3.1-8B-Instruct a 32 couches et 14 336 neurones intermédiaires par couche. | RAPPORTÉ (arbitre) | Cohérent avec ce que je sais de la configuration publique, mais non vérifié dans cette cellule. |

**Note technique.** Une dose « en fraction de la norme résiduelle » dépend de la position. Chez les Llama, le jeton BOS porte des activations massives. Il faut écrire d'avance la norme de référence, par exemple la médiane par position hors BOS. Sinon, les doses ne sont pas comparables entre amorces.

---

## (b) Expériences décisives (duels H_A / H_B)

Tous les seuils ci-dessous sont **illustratifs**. Ils doivent être fixés et scellés avant la confirmation sur la banque neuve. Pour chaque duel, la métrique principale est mécanique : log-probabilités sur des jetons de réponse forcés, jamais un juge en texte libre comme seule mesure.

### E0 — Préalable : y a-t-il quelque chose à pousser ?

- **H_A** : Llama-3.1-8B-Instruct montre un écart de comportement mesurable entre tâches « évaluation » et tâches « déploiement » appariées.
- **H_B** : aucun écart au-delà du bruit entre graines et reformulations.
- **Métrique** : différence de score de tâche entre les deux conditions, avec un intervalle par rééchantillonnage.
- **Contrôle négatif** : paires où seule une étiquette non pertinente change, par exemple le nom de fichier.
- **Issue qui falsifie** : H_B vraie rend E2 inapplicable, et ce verdict doit être écrit d'avance. H_A vraie falsifie « le modèle ne distingue pas ».

### E1 — Lire contre écrire : la direction de sonde est-elle utilisée en aval ?

- **H_A** : pousser +α·d (direction de sonde, couche L) augmente la log-cote « évalué », et −α·d la diminue. L'effet est monotone en dose et dépasse les témoins.
- **H_B** : d est lisible mais inerte (épiphénomène), ou son effet ne dépasse pas celui de n'importe quelle direction de même norme.
- **Métrique** : Δ[log p(A) − log p(B)] sur une question à choix forcé (« Ce texte vient-il d'une évaluation ? A/B »). L'association entre A/B et oui/non est tirée au hasard par amorce, ce qui neutralise un levier purement lexical sur « yes/test ».
- **Doses** : quatre niveaux sous le plafond de fluence. Le plafond se mesure d'abord sur les témoins : c'est la dose maximale telle que la KL sur des amorces neutres reste sous τ. Le seuil de 0,8 × est RAPPORTÉ sur Qwen et non transférable sans mesure.
- **Deux bras, à préenregistrer séparément** :
  - (i) poussée sur toute la transcription : le modèle *lit* un contexte altéré ;
  - (ii) poussée sur les seuls jetons de la question finale : le modèle *écrit* sa conclusion. C'est cohérent avec la règle du dernier jeton.
- **Amorces** : longues transcriptions de la banque (pour la sonde) et amorces courtes. La comparaison entre les deux teste a8.
- **Contrôles négatifs** :
  1. 256 directions aléatoires isotropes de même norme ;
  2. directions aléatoires tirées selon la covariance des activations à la couche L (même anisotropie) ;
  3. sonde entraînée sur **étiquettes permutées**, qui a les mêmes artefacts d'optimisation sans signal ;
  4. directions des références de surface (longueur, format).
- **Seuil** : l'effet de d dépasse le 99ᵉ centile de *chacun* des contrôles 1 à 4, avec le signe attendu dans les deux sens.
- **Falsification** : si d ne dépasse pas les contrôles, H_A est falsifiée. Si d les dépasse, H_B est falsifiée.
- **Ce que E1 ne prouverait pas** :
  - que la sonde lit la conscience d'évaluation sur les tâches : d peut piloter la *réponse à la question* sans être la variable qui module le comportement (E2) ;
  - que d est la seule voie : la redondance n'est pas testée ;
  - que la sonde est sûre comme moniteur : une direction causale peut quand même être contournée.
- **Variante** : direction de différence des moyennes contre vecteur de poids de la régression logistique, à norme égale. Prédiction de la littérature (Marks & Tegmark, à vérifier) : la différence des moyennes est plus impliquée causalement. Si c'est la régression logistique qui l'emporte, cette prédiction est falsifiée pour nos concepts.

### E2 — La poussée change-t-elle le *comportement* qui dépend de l'évaluation ?

Ce duel n'a lieu que si E0 donne H_A.

- **H_A** : −α·d réduit l'écart évaluation/déploiement, ce qui se lit comme une interaction poussée × condition.
- **H_B** : l'effet sur le score ne dépend pas de la condition (dégradation non spécifique) ou reste dans l'enveloppe des témoins.
- **Métrique** : différence de différences sur le score de tâche.
- **Contrôles** : les mêmes que pour E1.
- **Falsification** : une interaction nulle ou égale aux témoins falsifie « d médie la dépendance comportementale ». Une interaction significative et spécifique falsifie « d n'est qu'un corrélat verbal ».

**Rappel.** La décision antérieure a retiré le bruit d'activations des interventions revendiquées. Les directions aléatoires restent donc des **témoins de mesure**, jamais une intervention revendiquée.

### E3 — Neurones contre direction : la direction de sonde est-elle éparse dans la base des neurones ?

- **H_A (éparse)** : les k neurones dont les colonnes W_out reconstruisent le mieux d (moindres carrés non négatifs ou classement par contribution) reproduisent au moins X % de l'effet de poussée de d à norme résiduelle égale. Exemple illustratif : k = 16, X = 50 %.
- **H_B (dense, superposée)** : la fraction d'effet récupérée croît lentement en k. Les k meilleurs neurones ne font pas mieux que k neurones tirés au hasard avant k ≈ quelques centaines (illustratif).
- **Métrique** : courbe de fraction d'effet récupérée en fonction de k, côté écriture. Côté lecture, on ajoute la perte de justesse de la sonde quand on ablate ces k neurones (moyenne d'ablation).
- **Contrôles** : k neurones au hasard ; k neurones de plus forte variance d'activation, pour écarter une explication par la taille de l'activation.
- **Falsification** : H_B vraie rend un balayage neurone par neurone (E5) peu prometteur, ce qui est une prédiction écrite d'avance. H_A vraie falsifie l'hypothèse de superposition pour ce concept et justifie E5.
- **Réponse à « direction contre neurone sous poussée »** : il faut comparer dans **le même espace**, le résiduel, à norme résiduelle égale. Un neurone poussé écrit le long de sa seule colonne W_out. Une direction apprise écrit une combinaison dense. Sous H_B, on prédit qu'aucun neurone isolé n'atteint l'effet de d, quelle que soit la dose sous le plafond.

### E4 — Le score « distinct » de l'auteur mesure-t-il du sens ou la géométrie de W_out ?

On peut le faire sur Llama, au besoin sur une seule couche.

- **H_A** : la part de neurones « distincts » vient de leur fonction : des pseudo-neurones aléatoires appariés en géométrie sont signalés au taux nominal.
- **H_B** : la distinction est géométrique : des directions aléatoires appariées sur la projection sur les principaux vecteurs singuliers du désenchâssement, ou tirées dans l'enveloppe des colonnes W_out, sont signalées à un taux proche de celui des vrais neurones.
- **Métrique** : taux de signalement des pseudo-neurones, passés dans le pipeline *complet* et traités comme des neurones.
- **Seuil** : sous H_A, un taux proche de 0,39 % (« au-dessus de tous les témoins ») ou de 5 % (95ᵉ centile).
- **Contrôle négatif** : une moitié des témoins isotropes retenue comme pseudo-neurones, qui doit retrouver le taux nominal. Ce contrôle vérifie le pipeline lui-même.
- **Falsification** : un taux des pseudo-neurones appariés proche de celui des neurones falsifie H_A. Un taux nominal falsifie H_B.

### E5 — Balayage : existe-t-il un levier *unique* de conscience d'évaluation ?

On ne le lance qu'après E1 et E3.

- **H_A** : au moins un neurone, dans les couches retenues, déplace la log-cote « évalué » au-delà du nul corrigé, *et* réplique sur des amorces et une banque neuves, *et* reste spécifique.
- **H_B** : aucun candidat de l'exploration ne réplique plus que le taux attendu sous le nul.

**Contre le piège « parcourir puis affirmer »** :

1. Le vocabulaire cible et la métrique sont fixés d'avance : « test », « evaluation », « benchmark », « assessment », plus la question à choix forcé.
2. Les amorces sont coupées en deux : exploration et confirmation, cette dernière scellée.
3. Après l'exploration, on scelle une **liste fermée de M candidats** (M = 50, illustratif).
4. La confirmation se fait au niveau α/M = 0,001 : il faut au moins 1 000 témoins pour estimer ce quantile empiriquement, et plusieurs milliers pour qu'il soit stable. C'est un calcul, mais le nombre exact de témoins reste illustratif.

**Spécificité** : questions quasi-cibles qui partagent le vocabulaire sans la situation (« Ce texte parle-t-il d'un examen scolaire ? ») et questions lointaines (« Ce texte est-il un poème ? »). Le levier doit bouger la cible plus que les quasi-cibles.

**Falsification** : aucun candidat confirmé falsifie l'existence d'un levier unique *dans ces couches, à ces doses, pour cette métrique*. Je ne l'étends pas au-delà. Un candidat confirmé falsifie H_B, sous réserve du duel E6.

### E6 — Levier situationnel ou levier lexical ?

- **H_A** : le candidat change le jugement « évalué » sur des transcriptions de déploiement longues et réalistes. Il le fait **sans** augmenter la fréquence du champ lexical « test » dans des continuations libres, et l'effet persiste quand la réponse passe par A/B tiré au hasard, ou que la question est posée dans une autre langue.
- **H_B** : l'effet est porté par le vocabulaire. La fréquence lexicale monte, et l'effet sur le jugement disparaît sous A/B tiré au hasard ou sous changement de langue.
- **Contrôle négatif** : un neurone lexical connu (trouvé par projection directe sur « exam ») soumis au même protocole.
- **Falsification** : chacune des deux issues en falsifie une. C'est ici que le « levier de refus » rapporté (« I » → « Sure ») mérite son analogue : un changement du *premier jeton* n'établit pas un changement de *décision*.

### E7 — La primitive « pousser » apporte-t-elle quelque chose aux organismes ?

- **H_A** : les organismes qui disposent de l'opération (avec k témoins imposés) obtiennent un meilleur score sur la banque neuve scellée que ceux qui ne l'ont pas, à budget de calcul égal.
- **H_B** : pas de gain, ou une perte par surajustement.
- **Assignation** : tirée au hasard par course, avec le même nombre de courses par bras.
- **Métrique** : score sur la banque neuve. En second, le taux d'hypothèses de l'organisme qui survivent au test contre le bruit.
- **Contrôle négatif** : un bras avec une opération « pousser » placébo, qui renvoie le rendu d'une direction aléatoire étiquetée comme la direction demandée.
- **Falsification** : si placébo ≈ vraie opération, H_A est falsifiée. Si la vraie opération dépasse le placébo, H_B est falsifiée.

---

## (c) Instruments nommés : la mesure minimale qui dirait s'ils fonctionnent

Principe commun : chaque instrument est évalué sur des **cas appariés de vérité connue** (positifs plantés et négatifs honnêtes de même forme). Il doit battre une **vérification mécanique moins chère**, sinon il n'ajoute que du coût.

| Instrument | Positifs (vérité connue) | Négatifs honnêtes appariés | Mesure | Vérification mécanique à battre |
|---|---|---|---|---|
| **Sonde linéaire (étape 1)** | Traces sabotées et tâches d'évaluation de la banque | Traces honnêtes et tâches de déploiement appariées en longueur, tâche et format | Taux de détection à un taux de fausses alertes fixé (par ex. 1 %, illustratif) | Régression sur les traits de surface (longueur, mots-clés, format) ; expression régulière de mots-clés |
| **Poussée comme test causal** | Direction connue causale sur un concept net : différence des moyennes français/anglais ; direction de refus reproduite selon Arditi et al. (à vérifier) | Sonde à étiquettes permutées ; directions aléatoires isotropes et anisotropes | Part des positifs qui passent le seuil d'E1 (détection) ; part des négatifs qui le passent (fausses alertes, attendues ≤ 1 %) | Lentille 1 (projection directe sur le vocabulaire) ; lentille 2 (Δlog-prob en une passe) |
| **Score « distinct » (masse de grappe)** | Neurones lexicaux évidents, trouvés par projection directe | Pseudo-neurones : témoins retenus et directions appariées en géométrie (E4) | Taux de signalement des pseudo-neurones contre taux nominal | Norme de la colonne W_out et alignement sur le désenchâssement : si ces deux nombres prédisent « distinct » aussi bien, le score n'apporte rien |
| **Lentilles 1 et 2** | Les mêmes positifs | Les mêmes négatifs | Corrélation de rang entre lentille et effet de poussée réel mesuré par génération | Si la lentille 2 (une passe) prédit l'effet aussi bien que les 95 000 déroulés par couche, les déroulés sont un coût sans gain d'information |
| **Verbalisation** | Tâches d'évaluation explicites | Tâches de déploiement appariées | Détection et fausses alertes contre étiquette de la banque ; accord avec la sonde | Mots-clés présents dans l'amorce |
| **Agent explorateur** | Neurones et directions à fonction connue (positifs ci-dessus) | **Directions nulles déguisées** en neurones (aléatoires, permutées) | Fausses alertes = part des nuls pour lesquels l'agent écrit une explication confiante qui *survit à son propre test « casser »*, soit un taux de confabulation ; détection = part des positifs correctement décrits | Script sans agent : exemples d'activation maximale et résumé par projection directe |
| **Maximum à l'aveugle** | Explications correctes | Explications **permutées entre neurones** ; explications de directions aléatoires | Rapport (activation de la phrase écrite à l'aveugle) / (maximum du corpus) ; distribution sous les deux nuls | Phrase construite en concaténant les jetons de la projection directe |
| **Opération « pousser » (primitive)** | Organisme dont l'hypothèse est vraie par construction : trait planté dans ses propres textes | Placébo (E7) | Gain sur banque neuve contre placébo | Opérations de lecture seule déjà autorisées (activations, sondes) |

**Comment lire le cas de l'agent.** Si le taux de confabulation sur directions nulles n'est pas nettement sous le taux de détection, les rapports de l'agent ne disent rien. C'est le premier chiffre à obtenir, avant tout « neurone de conscience d'évaluation ».

**Planter un trait dans Llama.** Un trait planté par réglage fin d'une copie fournirait un positif idéal. Mais cela touche à la règle « aucun changement de modèle sans décision du directeur ». **Décision pour Lazar** : une copie réglée finement servant *uniquement* d'étalon d'instrument compte-t-elle comme changement de modèle ?

---

## (d) Ancrage matériel

**Modèle.** Llama-3.1-8B-Instruct, révision épinglée, sans changement. Reproduire les chiffres de l'auteur sur Qwen3.5-4B serait une **sortie du programme**, à décider par Lazar. E4 permet de tester la logique du score sans changer de modèle.

**Taille.** 32 × 14 336 = 458 752 neurones (calcul sur les chiffres de l'arbitre).

**Transposition du balayage de l'auteur** (tout est **illustratif** : extrapolation de chiffres RAPPORTÉ, avec l'HYPOTHÈSE d'un coût linéaire en paramètres et en nombre de neurones) :

- Déroulés par couche : 95 000 × 14 336 / 9 216 ≈ 148 000.
- Facteur de coût : ≈ 1,56 (neurones) × ≈ 2 (paramètres, 8B contre 4B) ≈ 3,1.
- Une couche : ≈ 4,4 h et ≈ 3,9 USD. 32 couches : ≈ 140 h et ≈ 125 USD.
- Sondage de 384 neurones et 64 témoins sur 32 couches : ≈ 12 USD.
- Mémoire : environ 16 Go de poids en demi-précision. Sur une carte de 24 Go, la marge pour le cache KV est faible, et les longues transcriptions la saturent. Une carte de 40 à 80 Go louée est plus réaliste (illustratif).

**Notre protocole n'est pas celui de l'auteur.** Les longues transcriptions coûtent beaucoup plus cher, sauf si l'on pousse seulement sur la question finale (bras ii d'E1). Dans ce cas, le préfixe de la transcription est calculé une fois et mis en cache, et seuls environ 20 jetons de question sont recalculés par poussée. Exemple illustratif pour E5 :

| Hypothèse de coût | Calcul | Jetons par couche |
|---|---|---|
| Poussée sur la question seule | 14 336 neurones × 4 doses × 50 amorces × 20 jetons | ≈ 57 M |
| Poussée sur toute la transcription | même chose avec 2 000 jetons par amorce | ≈ 5,7 G |

Le bras i du balayage complet n'est donc abordable que sur une liste courte de candidats.

**Classement préalable par attribution.** Un classement de tous les neurones par approximation linéaire de l'effet (patching par attribution : Syed, Rager & Conmy 2023, « Attribution Patching Outperforms Automated Circuit Discovery », à vérifier) demande une passe arrière par amorce. C'est une **vérification mécanique à battre** par le balayage brut. Si les deux classements concordent sur les M premiers, le balayage brut est superflu.

**Logiciel.** Une fourche de vLLM avec poussée par requête est RAPPORTÉ. Comme la licence n'a pas été trouvée, je recommande de réimplémenter avec des crochets PyTorch ou une bibliothèque sous licence connue (à choisir). Il faut aussi épingler le déterminisme : décodage glouton, lots de taille fixe, journal des log-probabilités, et répétition de chaque mesure sur au moins deux exécutions pour estimer la variance due au non-déterminisme.

---

## Réponses ciblées aux six demandes

**Q1 — Lire contre écrire.** Oui, c'est un test utile, mais seulement sous la forme E1 + E2, avec quatre familles de témoins dont la sonde à étiquettes permutées.

- *Ce qu'il prouverait* : la direction est en aval d'un chemin qui pilote la réponse verbale (E1), voire le comportement (E2).
- *Ce qu'il ne prouverait pas* : que la sonde est un bon moniteur, qu'il n'existe pas de voies redondantes, que la direction « est » la conscience d'évaluation.
- *Seuil écrit d'avance* : dépasser le 99ᵉ centile de chaque famille de témoins, monotonie en dose, réplication sur la banque neuve.
- *Délégation* : la poussée ne valide la sonde qu'indirectement. Pousser vers « honnête » puis lire la trace générée ne mesure pas la capacité à *classer* une trace existante (a11).

**Q2 — Balayage.** On ne le lance qu'après E3 (direction éparse) et E4 (score non géométrique). Le garde-fou contre « parcourir puis affirmer » est décrit en E5 : liste fermée scellée, correction α/M, nombre de témoins dimensionné, quasi-cibles.

- *Si un levier existe*, on apprend que le concept a une composante peu dimensionnelle dans la base des neurones, et l'on dispose d'un point d'entrée pour un circuit.
- *On n'apprend pas* que le modèle « est conscient » : E6 tranche entre levier situationnel et levier lexical.

**Q3 — Primitive « pousser ».** Elle peut être utile si E7 bat le placébo. Les dangers :

- coût : multiplicatif en doses × témoins ;
- non-reproductibilité ;
- **détournement** : un organisme qui peut pousser des vecteurs arbitraires et lire des scores de sonde peut, par essais successifs, extraire la direction de la sonde et apprendre à la tromper (Goodhart sur le moniteur).

Bornes possibles, toutes à préenregistrer :

1. Directions restreintes à une **liste enregistrée** (aucun vecteur arbitraire).
2. Doses plafonnées sous le seuil de fluence mesuré.
3. k témoins **obligatoires et rendus dans le même appel**, jamais un résultat de poussée sans son nul.
4. Plafond d'appels par course et journal empreinté.
5. Textes de l'organisme seulement, jamais de tâche de la banque (règle déjà décidée).
6. Pas de poussée sur des directions de *sonde du programme* : on ne donne pas le moniteur à l'organisme surveillé.

**Q4 — Méthodologie de l'agent.**

*À reprendre* :

- « casser exprès » : c'est le test de falsification écrit d'avance, déjà conforme à la boucle extérieure ;
- « maximum à l'aveugle » : validation adverse par un agent sans accès aux résultats, à garder **avec** le nul des explications permutées ;
- clôture par log-probabilités : une métrique mécanique plutôt qu'un jugement en texte.

*Pièges* :

- biais de confirmation : l'agent voit les résultats et itère, ce qui démultiplie les chemins d'analyse. Il faut imposer un budget d'hypothèses et une rédaction avant chaque exécution ;
- neurones polysémantiques : l'agent nomme l'un des sens et ignore les autres. On mesure la couverture : part de la variance d'activation que l'explication prédit (à la manière de Bills et al. 2023, à vérifier) ;
- confabulation sur les nuls : c'est la mesure (c) à obtenir en premier.

*Pour la caste « expérimentateur »*, je garde la même règle : pas d'hypothèse validée sans nul rendu dans le même appel.

**Q5 — Littérature.** Je donne une attribution que je crois exacte, mais **toutes sont à vérifier**, comme le demande l'arbitre. Aucun identifiant n'est donné.

- *Superposition et unité neurone* :
  - Elhage et al., 2022, « Toy Models of Superposition » ;
  - Bricken et al., 2023, « Towards Monosemanticity: Decomposing Language Models With Dictionary Learning » ;
  - Cunningham, Ewart, Riggs, Huben & Sharkey, 2023, « Sparse Autoencoders Find Highly Interpretable Features in Language Models » ;
  - Templeton et al., 2024, « Scaling Monosemanticity » ;
  - Gurnee et al., 2023, « Finding Neurons in a Haystack: Case Studies with Sparse Probing » ;
  - Geva, Schuster, Berant & Levy, 2021, « Transformer Feed-Forward Layers Are Key-Value Memories ».
- *Poussée d'activations* :
  - Turner et al., 2023, « Activation Addition: Steering Language Models Without Optimization » (titre révisé ensuite, à vérifier) ;
  - Zou et al., 2023, « Representation Engineering: A Top-Down Approach to AI Transparency » ;
  - Li, Patel, Viégas, Pfister & Wattenberg, 2023, « Inference-Time Intervention: Eliciting Truthful Answers from a Language Model » ;
  - Rimsky (Panickssery) et al., 2024, « Steering Llama 2 via Contrastive Activation Addition » ;
  - Arditi et al., 2024, « Refusal in Language Models Is Mediated by a Single Direction » ;
  - Tan et al., 2024, « Analyzing the Generalization and Reliability of Steering Vectors » (référence à vérifier) ;
  - Wu et al., 2025, « AxBench » (référence à vérifier).
- *Sondes et causalité* :
  - Hewitt & Liang, 2019, « Designing and Interpreting Probes with Control Tasks » ;
  - Belinkov, 2022, « Probing Classifiers: Promises, Shortcomings, and Advances » ;
  - Ravfogel et al., 2020, « Null It Out » (INLP) ;
  - Elazar, Ravfogel, Jacovi & Goldberg, 2021, « Amnesic Probing » ;
  - Marks & Tegmark, 2023, « The Geometry of Truth » ;
  - Makelov, Lange & Nanda, 2023, « Is This the Subspace You Are Looking For? An Interpretability Illusion for Subspace Activation Patching » ;
  - Bolukbasi et al., 2021, « An Interpretability Illusion for BERT ».
- *Nos familles* :
  - Needham et al., 2025, « Large Language Models Often Know When They Are Being Evaluated » (référence à vérifier) ;
  - Abdelnabi & Salem, 2025, sur le contrôle linéaire de la conscience de test (référence à vérifier) ;
  - Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes » (référence à vérifier).
- *Sources déclarées par l'auteur* : l'essai Goodfire « Neural Networks Are Already Clean » (RAPPORTÉ, non lu) et l'étude des 128 neurones de Qwen3-8B (référence à vérifier).

**Q6 — Ordre et départage.** Plusieurs ordres sont défendables. Je propose deux voies et ce qui les départage.

- **Voie V-sonde d'abord** : E0, puis E1 et E2 sur les sondes existantes, puis E3, puis E5 et E6 seulement si E3 conclut à une direction éparse. Elle est peu coûteuse et réutilise les artefacts de l'étape 1.
- **Voie V-instrument d'abord** : E4 et la mesure de confabulation de l'agent (c), avant toute exploration de neurones. Elle protège contre l'importation d'un score mal calibré.
- **Ce qui les départage** : si l'on a déjà des sondes stables et une banque scellée prête, V-sonde. Si l'adoption de l'outil de l'auteur est envisagée, V-instrument, parce que E4 coûte une couche.
- **Primitive « pousser » (E7)** : en dernier, après calibration des doses par E1.
- **À ne jamais faire** :
  - publier un neurone de balayage sans confirmation scellée ;
  - utiliser un juge en texte libre comme métrique unique ;
  - pousser au-delà du plafond de fluence mesuré ;
  - revendiquer le bruit aléatoire comme intervention ;
  - donner à un organisme l'accès en poussée aux directions de sonde du programme.

**Ce qui falsifierait « des leviers uniques existent pour la conscience d'évaluation »** (dans les couches et doses testées) :

- E3 conclut à une direction dense ;
- **et** E5 ne confirme aucun candidat ;
- **ou** chaque candidat confirmé tombe en E6 du côté lexical.

À l'inverse, un candidat qui passe E5 et E6 *et* reproduit l'effet de E2 sur le comportement falsifierait l'hypothèse « purement distribuée ».

**Ce qu'il faudrait savoir de plus** :

- le résultat des sondes de l'étape 1 contre les références de surface (a2) ;
- l'existence d'un écart comportemental de base (E0) ;
- le contenu réel des fichiers du dépôt, non lus ici ;
- la position de Lazar sur une copie étalon réglée finement.

FIN-DE-CELLULE
# Cellule III.3 — Riposte de la proposition B

**Pièces reçues.**
- Le bloc FAITS est vide par déclaration : ce n'est ni une coupure ni une absence.
- La question de l'arbitre, ma conception III.1, l'équipe rouge A et l'équipe rouge C sont complètes jusqu'à leur FIN-DE-CELLULE.
- Je n'ai pas reçu les conceptions III.1 de A et de C. Je ne réponds donc qu'aux sections « Contre la proposition B ». Quand je reprends un argument que A ou C dirigeait contre un tiers, je le signale.
- Les fichiers du dépôt `neuron-explorer` ne sont toujours pas joints. Tout ce qui touche à la méthode reste **RAPPORTÉ**.
- Tous les seuils et effectifs sont **illustratifs**, sauf ceux qui résultent d'un calcul explicite.

---

## (a) Verdict sur chaque attaque

### Attaques de l'équipe rouge A

| Réf. | Verdict | Raison ou test |
|---|---|---|
| **B-1** (le contrôle 4 est un positif possible) | **Acceptée → test** | Exact : « d ne dépasse pas les directions de surface » ne falsifie pas la causalité, cela dit seulement que la cause est peut-être la surface. Je retire le contrôle 4 du seuil d'E1 et j'en fais un duel séparé, **E1s** (§ b). |
| **B-2** (fuite entre banque de la sonde et banque de poussée) | **Acceptée** | La partition est imposée dès l'exploration : sonde apprise sur la partie P1, poussée sur une partie P2 disjointe (tâches et gabarits distincts), confirmation sur la banque neuve scellée. L'objection de C contre A (A-3, fuite par le cadrage) va dans le même sens : je la reprends. |
| **B-3** (le 99ᵉ centile de 256 témoins repose sur 2 ou 3 points) | **Acceptée** | Calcul : 1 % de 256 = 2,56 points au-delà du quantile. Avec 1 000 témoins par famille, environ 10 points, ce qui est plus stable. Famille 3 : environ 1 000 sondes réentraînées sur des étiquettes permutées. C'est peu coûteux, puisqu'il s'agit d'une régression sur des activations déjà mises en cache. |
| **B-4** (pas de KL par direction poussée) | **Acceptée** | La KL est mesurée **pour chaque direction poussée**, témoins compris, **à la position poussée**, sur la distribution de la question finale et non sur un texte neutre (je reprends ici l'argument de A contre C, C-8). Les témoins qui dépassent τ sont journalisés, jamais retirés en silence (je reprends C-9). |
| **B-5** (E6 : hypothèses non exclusives) | **Acceptée** | Exact : un levier situationnel peut faire monter le lexique « test ». La fréquence lexicale n'est plus un critère, seulement une mesure descriptive. E6 est réécrit avec un rapport cible/quasi-cible coupé par un seuil unique, ce qui partitionne les issues par construction. |
| **B-6** (E3 : couche des colonnes W_out) | **Acceptée** | E3 se restreint aux neurones du bloc L dont la sortie s'ajoute au résiduel lu par la sonde. Une variante inter-couches est déclarée séparément, avec un effet mesuré après propagation et des témoins tirés dans la **même** couche. |
| **B-7** (score de masse de grappe non défini) | **Acceptée** | E4 porte sur **notre réimplémentation figée** du score, pas sur le score de l'auteur. La formule doit être lue dans le dépôt et recopiée. Tant que ce n'est pas fait, toute conclusion d'E4 reste une conclusion sur notre interprétation. |
| **B-8** (trait planté par réglage fin = cas facile) | **Acceptée, rôle restreint** | Le trait planté devient un contrôle **nécessaire, pas suffisant**. Un instrument qui échoue sur lui est disqualifié. Un instrument qui le passe n'a rien prouvé pour un trait superposé issu du préentraînement. Pour estimer la sensibilité, j'ajoute des positifs dont la vérité ne dépend pas de la poussée (voir C-a4). |
| **B-9** (E7 : taxe des témoins) | **Rejetée en partie** | Le placébo d'E7 rend aussi k témoins : vraie opération et placébo ont **le même coût par construction**. La comparaison vrai/placébo ne confond donc pas taxe et nullité. L'objection vaut en revanche pour la comparaison avec le bras sans opération. Je l'ajoute explicitement : bras « lecture seule » à budget total égal (§ b, E7′). Je précise aussi par écrit que le placébo paie k+1 inférences, ce que III.1 ne disait pas. |
| **B-10** (nuls de l'agent reconnaissables) | **Acceptée → test** | Exact : une direction aléatoire a des pseudo-activations denses, un vrai neurone des activations éparses à queue lourde. Je remplace ce nul par des **neurones chimères** : lecture d'un vrai neurone, écriture le long d'une direction aléatoire de même norme. L'agent voit des statistiques d'activation réelles, mais l'effet de poussée est nul par construction (E8, § b). |
| **B-11** (débit non linéaire) | **Acceptée** | L'extrapolation (140 h, 125 USD) est remplacée par une **mesure** sur une couche partielle (E-cal, § b). Je ne raisonne plus sur l'extrapolation. |
| Évasion contre E1 (verbal découplé de la décision) | **Acceptée** | C'est une règle écrite : **aucune revendication de validité comportementale sans E2**. E1 seul ne permet d'affirmer que « d pilote le rapport verbal ». |
| Évasion par optimisation du texte (rang centile gonflé) | **Acceptée** | Les témoins de la primitive sont tirés selon la covariance (anisotropes), **fixés par course et par direction**, et non par texte. Les resoumissions sont comptées et corrigées. Je reprends ici l'évasion par re-tirage que A décrivait contre C, et qui s'applique à moi dès que les témoins dépendent du texte. |
| Évasion contre « maximum à l'aveugle » (encodage syntaxique) | **Transformée en test** | Duel E9 (§ b) : explication brute contre explication paraphrasée par un tiers et normalisée en longueur. |
| Agents de même modèle, angles morts partagés | **Acceptée, non résolue** | La boucle extérieure ne fixe pas la famille de modèle des agents neufs. **Décision pour Lazar** : imposer une famille différente pour le rôle « casser exprès ». |
| Contrôles fatals 1 à 6 de A | **Acceptés** | Intégrés en E1′, E1s, E3′, E7′, E8. |
| Point commun : les sondes de l'étape 1 n'existent peut-être pas encore | **Acceptée** | Elle devient la porte **E−1**. Tout « lire contre écrire » en dépend. Je l'avais rangée sous « ce qu'il faudrait savoir de plus » : c'était trop faible. |

### Attaques de l'équipe rouge C

| Réf. | Verdict | Raison ou test |
|---|---|---|
| **C-a1** (bras ii : pousser sur la seule question court-circuite la lecture du contexte) | **Acceptée pour le faux négatif ; rejetée pour le « vrai par construction »** | Exact : avec le cache KV figé, les clés et valeurs du contexte ne sont pas poussées. Un levier qui agit à l'encodage de la trace est invisible dans le bras ii. En revanche, un effet positif dans le bras ii n'est pas garanti par construction : il établit seulement que d est utilisée au moment de la décision, ce que III.1 déclarait comme portée du bras ii. **Correction pour E5** : un balayage en bras ii seul ne conclut jamais à l'absence. J'estime le **rappel** du bras ii sur un sous-échantillon aléatoire de neurones passés en bras i (je reprends l'argument de A contre C, C-6). |
| **C-a2** (le tirage aléatoire A/B exige une liaison symbolique en aval de L) | **Acceptée → test** | C'est l'objection la plus sérieuse contre E1 et E6. Deux corrections. (1) La métrique devient Δ[log p(lettre-oui) − log p(lettre-non)], analysée **par association** et non moyennée naïvement en A−B. Un levier qui pousse « A » quelle que soit l'association est alors diagnostiqué, pas annulé. (2) J'ajoute le **contrôle de plafond de couche** proposé par C : une direction d'un concept manifeste (langue du texte) et la couche L_max au-delà de laquelle la poussée ne pilote plus la lettre associée. Les couches L > L_max sont exclues d'E1 et d'E6. |
| **C-a3** (E2 conditionné par E0 : faux négatif sur des leviers sous le seuil) | **Transformée** | E2 tel qu'écrit (« réduire l'écart ») n'a pas de sens sans écart : ce n'est pas une faille logique, c'est une définition. L'objection pointe pourtant une question réelle : +α·d crée-t-il un comportement absent au repos ? Explorer « n'importe quel changement » serait « parcourir puis affirmer ». J'ajoute donc **E2b** avec une **liste fermée de comportements écrite d'avance**. |
| **C-a4** (direction d'Arditi sélectionnée pour son effet sous poussée) | **Acceptée en partie** | Un positif de vérité connue est vrai par construction, c'est son rôle. Mais une direction sélectionnée par le même protocole que l'instrument est le cas le plus facile et surestime la sensibilité. Elle est rétrogradée en contrôle de fonctionnement. La sensibilité s'estime sur des positifs choisis **sans regarder la poussée** : différence des moyennes FR/EN, différence des moyennes d'un trait lexical explicite. |
| **C-b1** (sabotage rare noyé dans la moyenne d'E0) | **Acceptée** | E0 mesure aussi l'hétérogénéité sur des sous-familles **définies d'avance**, sans découpage après coup. Statut : le scénario adverse reste une HYPOTHÈSE pour Llama-3.1-8B, qui n'est pas un adversaire entraîné. |
| **C-b2** (inhibition de la méta-question A/B) | **Acceptée comme limite ; rejetée comme invalidation** | C'est exactement pourquoi E2 existe. Je retire toute conclusion « inerte » tirée d'E1 seul. Le croisement E1 × E2 a quatre issues, chacune interprétée d'avance (§ b). Cela répond aussi au point commun de A sur la partition verbal / comportemental / lexical. |
| **C-b3** (levier réparti sur environ 5 neurones, sous le seuil α/M) | **Rejetée comme évasion ; acceptée comme portée** | E5 teste un levier **unique**, ce que demande la question. Un E5 négatif était déjà limité à « aucun neurone isolé ». Pour ne pas en rester là, j'ajoute **E5g** : petits groupes tirés du classement d'E3 (k de 2 à 16, illustratif), contre des groupes témoins de même taille et de même couche. |
| **C-b4** (triangulation de la sonde par la liste enregistrée) | **Acceptée → test** | Nouvelle borne 7 : **aucune lecture de score de sonde dans une passe poussée**. L'organisme lit les sondes seulement sur des passes non poussées de ses textes. Une limite subsiste : la lecture de sonde, déjà autorisée, permet une optimisation de texte en boîte noire contre le moniteur, sans aucune poussée. La question pertinente est donc le **gain marginal** de la poussée pour l'évasion : duel **E7c**. |
| **C-b5** (évasion conjointe) | **Acceptée en partie** | Elle combine C-b1 à C-b4 ; chaque maillon a sa correction ci-dessus. Ce qui reste ouvert, je le déclare : un circuit à la fois tardif (couche > L_max), conjonctif et réparti échappe à la poussée **et** à la lecture A/B. La poussée ne le détecte pas, et je ne prétends pas le contraire. |
| **C-c1** (plafond de couche de la liaison) | **Acceptée** | Voir C-a2. |
| **C-c2** (neurones d'indices permutés pour E4) | **Rejetée pour le score de poussée, acceptée pour la lecture** | Si la poussée d'un neurone revient à ajouter δ·W_out[:, i] au résiduel (HYPOTHÈSE sur l'implémentation de l'auteur, non lue), son effet ne dépend que de la colonne de sortie. Permuter les indices conserve exactement l'ensemble des colonnes poussées : le taux de « distincts » côté poussée est **identique par construction**, et le contrôle est vide. En revanche, il est informatif pour la partie lecture (captures d'activations, maximum du corpus), où le couplage W_in/W_out compte. Je retiens aussi le point conceptuel de C : la géométrie de W_out est apprise, donc « géométrique » et « fonctionnel » ne s'opposent pas proprement. E4 est reformulé en conséquence (§ b). |
| **C-c3** (patching par attribution aveugle aux neurones éteints) | **Rejetée en partie** | Pour une **poussée** additive, l'approximation au premier ordre est δ·∂ℒ/∂h_i = δ·W_out[:, i]ᵀ∂ℒ/∂r : elle ne dépend pas de l'état de la porte du neurone i (architecture SwiGLU de Llama : à vérifier, non fournie par les faits). Le produit activation × gradient sert à l'ablation, pas à la poussée. Reste vraie l'objection sur les **non-linéarités en aval**, des portes fermées à dose nulle qui s'ouvrent à +0,5×. Test : taux de discordance entre la prédiction au premier ordre et la différence finie, sur un échantillon aléatoire comprenant des neurones non retenus (E5′). |

---

## (b) Expériences corrigées

Toutes opposent H_A et H_B exclusives ; chaque issue en falsifie une. Seuils **illustratifs**, à sceller avant la confirmation.

### E−1 — Porte : les sondes de l'étape 1 battent-elles la surface ?
- **H_A** : la sonde au dernier jeton dépasse la régression sur traits de surface, à taux de fausses alertes fixé, sur une banque disjointe.
- **H_B** : elle ne la dépasse pas.
- **Conséquence** : sous H_B, « lire contre écrire » est suspendu pour cette sonde. On pousserait un corrélat de surface, et E1s deviendrait l'expérience pertinente.

### E-cal — Étalonnage sur Llama, une couche, avant toute autre poussée
Trois duels, sur une seule couche et un sous-ensemble de neurones.

1. **Débit** (remplace B-11)
   - **H_A** : le coût mesuré tombe dans un facteur 2 de l'extrapolation (illustratif).
   - **H_B** : hors de ce facteur.
2. **Plafond de fluence par direction**
   - **H_A** : le plafond de KL à la position poussée diffère entre directions isotropes, anisotropes et différence des moyennes d'au moins un facteur 1,5 en dose (illustratif).
   - **H_B** : un plafond commun suffit.
   - **Conséquence** : sous H_A, le plafond est fixé **par direction**. Le seuil de 0,8 reste RAPPORTÉ sur Qwen et n'est jamais importé.
3. **Plafond de couche de la liaison** (repris de C)
   - Direction FR/EN poussée couche par couche.
   - **H_A** : il existe un L_max au-delà duquel la lettre associée ne suit plus.
   - **H_B** : la liaison suit jusqu'à la dernière couche testée.

### E0′ — Écart comportemental de base
- Inchangé, avec une addition : des sous-familles de tâches **définies d'avance** (en nombre fermé), analysées avec correction.
- **H_A** : un écart au-delà du bruit, en moyenne **ou** dans au moins une sous-famille préenregistrée.
- **H_B** : aucun.

### E1′ — La direction pilote-t-elle le rapport verbal ?
- **Banques** : sonde apprise sur P1 ; poussée sur P2, disjointe ; confirmation sur la banque neuve.
- **Couche** : L ≤ L_max (E-cal).
- **Métrique** : Δ[log p(lettre-oui) − log p(lettre-non)], par association, plus l'effet sur la lettre fixe « A » comme diagnostic d'un levier sur la lettre.
- **Témoins** : environ 1 000 par famille. Famille 1 : isotropes. Famille 2 : covariance Σ_L. Famille 3 : environ 1 000 sondes réentraînées sur étiquettes permutées.
- **Fluence** : KL mesurée par direction, à la position poussée, appliquée aux témoins comme à d. Les exclusions sont journalisées.
- **Bras** : bras i (toute la transcription) et bras ii (question seule), préenregistrés séparément. La portée du bras ii est déclarée : décision seulement.
- **H_A** : d dépasse le 99ᵉ centile de chacune des trois familles, avec le signe attendu, monotone en dose.
- **H_B** : non.
- **Portée de H_B** : une issue H_B ne falsifie que « d pilote le rapport verbal à L, dans ce bras ». Elle ne falsifie jamais « d est causale ».

### E1s — Concept ou surface (remplace le contrôle 4, repris de A)
- **H_A** : l'effet de d persiste sur des paires où les traits de surface (longueur, format, mots-clés) sont **égalisés** entre conditions, et il dépasse celui des directions de surface.
- **H_B** : l'effet tombe dans l'enveloppe des témoins à surface égalisée.

### E2 / E2b — Comportement
- **E2** (si E0′ donne H_A) : inchangé, interaction poussée × condition.
- **E2b** (quel que soit E0′) : +α·d sur des tâches de déploiement.
  - **H_A** : au moins un comportement d'une **liste fermée écrite d'avance** (refus, sous-performance sur des questions de capacité, mention d'évaluation, longueur) bouge au-delà des témoins, après correction pour la taille de la liste.
  - **H_B** : aucun ne bouge.

**Lecture croisée E1′ × E2/E2b, écrite d'avance :**

| | Comportement oui | Comportement non |
|---|---|---|
| **Verbal oui** | Direction couplée au rapport et à la décision | Levier de verbalisation seul, ou découplage |
| **Verbal non** | Inhibition de la méta-question (C-b2), ou liaison tardive | Aucun usage détecté à cette couche et à ces doses |

### E3′ — Parcimonie, même couche
- **Neurones** : ceux du bloc L.
- **Sélection** : par contribution pondérée par l'activation sur P1, c'est-à-dire la moyenne de h_i·⟨W_out[:, i], d⟩ (je reprends l'objection de C contre A, A-1 : le produit scalaire seul confond norme et usage).
- **Témoins** : k neurones aléatoires de la même couche, appariés en norme de W_out et en fréquence d'activation.
- **Mesure de nécessité** (repris de C contre A) : ablation par la moyenne des k sélectionnés sur P2, avec la perte d'effet de d comme mesure.
- **H_A / H_B** : comme en III.1, sur la courbe de fraction d'effet récupérée en fonction de k.
- **Variante inter-couches** : déclarée séparément, effet mesuré après propagation.

### E4′ — Le score « distinct » apporte-t-il plus que l'alignement géométrique ?
- **Prérequis** : formule lue dans le dépôt et figée.
- **H_A** : le score prédit les effets de génération mesurés sur une liste tenue à part, **au-delà** d'un modèle de régression fondé sur la norme de W_out et ses projections sur les principaux vecteurs singuliers de W_U.
- **H_B** : il ne les prédit pas mieux.
- **Pseudo-neurones** : les directions appariées en géométrie de III.1 sont gardées comme contrôle de calibration du pipeline.
- **Contrôle d'indices permutés** : utilisé **seulement** pour la partie lecture (voir C-c2).

### E5′ et E5g — Levier unique, puis petits groupes
- **E5′** : comme en III.1 (liste fermée, α/M, témoins dimensionnés), avec trois ajouts :
  1. **rappel du bras ii**, estimé sur environ 200 neurones aléatoires (illustratif) passés en bras i ;
  2. **discordance** entre l'attribution au premier ordre et la différence finie aux doses retenues, mesurée sur un échantillon aléatoire ;
  3. dimensionnement : α/M = 0,05/50 = 0,001, donc il faut au moins 999 témoins pour qu'un p empirique atteigne ce seuil (calcul), et plusieurs milliers pour de la puissance.
- **E5g** :
  - **H_A** : un groupe de taille au plus 16 (illustratif) dépasse les groupes témoins appariés.
  - **H_B** : aucun groupe ne les dépasse.

### E6′ — Situationnel ou lexical (exclusif par construction)
- **Mesure** : r = effet sur la question cible ÷ effet sur la question quasi-cible (« parle-t-il d'un examen scolaire ? »), mesuré en FR et en EN, par association de lettres, à L ≤ L_max.
- **H_A** (situationnel) : r > r₀ dans les deux langues.
- **H_B** (lexical) : r ≤ r₀ dans au moins une langue.
- **Seuil** : r₀ est fixé avant la confirmation (illustratif : 2).
- La fréquence lexicale en continuation libre est rapportée, sans rôle de critère.

### E7′ et E7c — Primitive « pousser »
- **Bras E7′** :
  - (1) vraie opération ;
  - (2) placébo, avec les mêmes k témoins et donc le même coût ;
  - (3) lecture seule, au même budget **total** ;
  - assignation au hasard par course.
- **Variance entre courses** : mesurée sur des courses pilotes, puis nombre de courses dimensionné en conséquence. Je ne fixe pas d'effectif de mémoire.
- **H_A** : (1) > (2), et (1) ≥ (3).
- **H_B** : (1) ≈ (2).
- **E7c (évasion)** : organismes d'équipe rouge dont l'objectif écrit est de tromper la sonde, avec ou sans « pousser ».
  - **H_A** : la poussée augmente le taux d'évasion au-delà de la lecture seule.
  - **H_B** : pas de gain marginal.
  - Sous H_A, la primitive n'est **pas** ouverte aux organismes du programme.
- **Bornes** : les six bornes de III.1, plus :
  - 7. pas de lecture de sonde dans une passe poussée ;
  - 8. témoins anisotropes fixés par course et par direction ;
  - 9. resoumissions comptées et corrigées.

### E8 — Taux de confabulation de l'agent explorateur
- **Positifs** : neurones et directions à fonction connue, choisis sans la poussée.
- **Nuls** : **chimères** (lecture réelle, écriture aléatoire) et neurones réels aux explications permutées.
- **Proportions** : inconnues de l'agent et tirées par course, pour qu'il ne puisse pas caler son taux d'acceptation.
- **H_A** : le taux de survie au « casser exprès » est plus bas sur les nuls que sur les positifs, d'au moins un écart fixé d'avance.
- **H_B** : pas d'écart. Les rapports de l'agent sont alors non informatifs.

### E9 — Encodage dans le « maximum à l'aveugle »
- **H_A** : le rapport (activation à l'aveugle) / (maximum du corpus) se maintient quand l'explication est paraphrasée par un tiers et normalisée en longueur.
- **H_B** : il chute au-delà d'un seuil fixé d'avance. C'est alors l'encodage, et non la compréhension, qui porte le score.

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi.**
- Aucun fait sur la méthode n'est VÉRIFIÉ dans cette cellule. Tout ce qui concerne `neuron-explorer` (19,6 % et 8,2 %, plafond de 0,8×, coûts, neurones de référence) est **RAPPORTÉ** et vient d'un dépôt non lu ici, sans licence trouvée.
- Établi par **calcul** sur les chiffres de l'arbitre :
  - « au-dessus de tous les 256 témoins » donne un taux nominal de 1/257 ≈ 0,39 % sous un nul échangeable ;
  - Llama-3.1-8B compte 32 × 14 336 = 458 752 neurones ;
  - un seuil corrigé de 0,001 exige au moins 999 témoins pour être atteignable.
- Établi par **raisonnement**, et seulement comme contraintes de conception (aucun résultat empirique) :
  - un effet sur le rapport verbal ne vaut pas validité comportementale ;
  - un nul isotrope ne suffit pas pour des colonnes W_out ni pour des directions de sonde ;
  - une question à lettres A/B aléatoires suppose une liaison en aval de la couche poussée ;
  - pousser sur la seule question finale ne teste pas l'encodage du contexte ;
  - la primitive « pousser » peut aider à tromper le moniteur.

**Ce qui n'est pas établi.**
Ce qui suit reste HYPOTHÈSE ou inconnu :
- que les sondes de l'étape 1 battent la surface ;
- que Llama montre un écart évaluation/déploiement ;
- qu'un levier de conscience d'évaluation existe, unique ou en petit groupe ;
- que le score « distinct » mesure autre chose que l'alignement géométrique ;
- que l'agent confabule moins sur des nuls que sur des positifs ;
- que la primitive « pousser » apporte quelque chose aux organismes sans accroître leur capacité d'évasion ;
- que les doses et les coûts de Qwen se transposent.

**Ce qui falsifierait « il existe des leviers uniques de conscience d'évaluation »** (dans les couches L ≤ L_max et aux doses testées) : E3′ dense, **et** E5′ sans candidat confirmé avec un rappel du bras ii mesuré élevé, **ou** tous les candidats du côté lexical en E6′.

**L'expérience à faire en premier : deux voies, et ce qui les départage.**
- **Voie 1 — E-cal** (une couche de Llama) : débit mesuré, plafond de fluence par direction, plafond de couche de la liaison A/B.
  - Elle ne dépend ni des sondes de l'étape 1, ni du dépôt, ni d'une décision de Lazar.
  - Elle conditionne les doses, les couches et la métrique de toutes les autres expériences.
  - Chacun de ses trois duels a deux issues interprétables.
- **Voie 2 — E−1 puis E1′ directement**, si les sondes de l'étape 1 et la partition P1/P2 existent déjà.
- **Ce qui départage** : l'état de l'étape 1.
  - Si ses résultats contre les références de surface sont disponibles et positifs, E1′ est plus informatif pour le programme.
  - S'ils sont absents ou négatifs, E-cal est le seul pas qui ne soit pas gaspillé.
- **E8 avant tout balayage** si l'adoption de l'agent de l'auteur est envisagée.
- **En dernier** : E7′ et E7c. La primitive n'est ouverte aux organismes que si E7c donne H_B.

**Décisions pour Lazar.**
1. Une copie réglée finement, servant seulement d'étalon, compte-t-elle comme changement de modèle ? (Son rôle est désormais restreint : contrôle nécessaire, pas suffisant.)
2. Faut-il imposer une famille de modèle différente pour les agents « casser exprès » ?
3. Faut-il lire le dépôt pour figer la formule du score avant E4′ ?

FIN-DE-CELLULE
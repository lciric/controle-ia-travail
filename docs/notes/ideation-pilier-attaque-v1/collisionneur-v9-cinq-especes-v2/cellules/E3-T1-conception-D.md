# Proposition D — aucune conclusion sur les sondes avant qualification de l’oracle

**Convention.** Les seuils suivants sont des choix de préenregistrement entièrement **illustratifs**, non des résultats : intervalles de confiance à 95 %, puissance de 90 %, taux total de fausses alertes \(\tau=1\%\), gain minimal \(\varepsilon=0,05\) de rappel absolu, rappel minimal de l’oracle \(R_{\min}=0,90\), taux maximal de dommage attribué à tort sur honnête \(F_{\max}=0,05\), marge de dépendance résiduelle \(\eta=0,02\), marge d’équivalence causale de \(0,02\) sur le dommage et perte de tâche maximale de \(0,02\). Ils devront être révisés avant gel, jamais après lecture.

« Démontrer » signifie ici : obtenir l’effet préenregistré, avec intervalles groupés par monde, tâche et organisme, sur des données non utilisées pour choisir couches ou hyperparamètres. Les jetons ne sont pas des observations indépendantes.

## (a) Ce que la question suppose sans l’établir

| Supposition | Statut et conséquence |
|---|---|
| Un sabotage diffus laisse une trace interne incrémentale par rapport au texte. | **HYPOTHÈSE** — H1. Les lectures au hasard ou proches du hasard ne la réfutent pas universellement, mais n’en apportent aucune preuve. |
| La dose dite « diffuse », fixée en boîte noire, produit un sabotage effectivement reconnu par l’oracle. | **HYPOTHÈSE**. Sans dommage attesté, une sonde peut apprendre la dose, l’adaptateur ou la tâche. |
| Le rappel de l’oracle et son indépendance d’erreur vis-à-vis des moniteurs sont suffisants. | **HYPOTHÈSE**. La décision N-060 et la diversité des familles ne mesurent ni l’un ni l’autre. |
| L’absence de consigne à l’inférence dans la famille (ii) lève le confondant consigne/acte. | **HYPOTHÈSE** seulement partielle : elle supprime une source de fuite, pas l’identité de l’organisme, la tâche ou le monde planté. |
| L’écart adapté−base sur le même contexte est hors du contrôle de l’attaquant. | **HYPOTHÈSE**, trop forte : un comportement adaptatif peut aussi modifier cet écart. Il faut le mesurer, non le postuler. |
| Une direction lisible est un levier causal. | **HYPOTHÈSE**. La littérature sur l’« axe de douleur » est **RAPPORTÉE** et fournit précisément un contre-exemple de type lecture sans levier. |
| Jev peut servir de mâchoire externe calibrée. | **OBSERVÉ-NON-AUDITÉ** pour Jev 1.14 ; les triches grossières sans dénominateur honnête ne renseignent pas sur les fausses alertes. |
| Le score de 0,866 du prédicteur texte est comparable à un rappel à faible taux de fausses alertes. | **HYPOTHÈSE** non justifiée : la métrique et la calibration doivent être rétablies. |
| Les matrices de transfert publiées décrivent nos organismes et nos sondes. | **RAPPORTÉ** pour la littérature ; aucune mesure correspondante sur nos objets. |
| Le résultat de l’arène synthétique se transporte à un vrai modèle. | Portabilité **HYPOTHÈSE**. La lecture préenregistrée et son empreinte sont **VÉRIFIÉES**, pas sa généralisation aux organismes T0.6. |
| Mélange, secret et diversité effective sont trois sources de gain identiques. | **HYPOTHÈSE**. Ils doivent être séparés expérimentalement. |
| La pince serre et les bornes L2/E7 suffisent à la caractériser. | **HYPOTHÈSE** issue de débats, sans mesure. |
| La validation croisée sur les familles vues remplace le mode tenu à l’écart. | **HYPOTHÈSE**. Avec les seules familles construites, elle sert à sélectionner ; elle ne démontre pas la généralisation finale. |

Le contenu de **N-059, point 11**, n’est pas fourni : les critères d’arrêt proposés plus bas ne prétendent pas le restituer.

## Protocole commun avant toute lecture

1. **Sas et gel** : manifestes d’épisodes, versions des organismes, couches, positions, agrégateurs, graines, seuils et code statistique sont empreintés. Les seuils de décision sont appris sur validation, puis figés.
2. **Négatifs honnêtes appariés** : jumeau honnête, dose nulle, organisme placebo, épisodes dormants, consigne d’attaque sans acte, échecs honnêtes de code ou d’exécution, nouvelles tâches et nouveaux mondes. Appariement sur tâche, monde et, lorsque possible, préfixe de jetons réalisé.
3. **Contrôles de fuite** : classification de l’identité de l’organisme, de la consigne, de la tâche et du monde ; permutation des étiquettes à l’intérieur de chaque strate. Un contrôle positif flagrant vérifie seulement que la chaîne peut fonctionner.
4. **Puissance** : un petit pilote estime variance et corrélation intra-monde ; le nombre d’épisodes est ensuite fixé pour distinguer \(\varepsilon\) avec la puissance préenregistrée et pour estimer la queue à \(\tau\). L’effectif est majoré pour le désaccord de l’oracle et le regroupement par monde. Un intervalle trop large est une issue non informative, pas une absence de trace.
5. Toute reconception après lecture négative reprend la validation par blocs ; **chaque nouvelle lecture décisive consomme une famille tenue à l’écart neuve**.

## (b) Expériences en duels exclusifs

### E0 — Qualifier la vérité terrain et suspendre si nécessaire

- **H_A** : l’oracle voit assez bien les sabotages connus et ses erreurs sont suffisamment bornées pour servir de référence.
- **H_B** : les étiquettes sont trop incomplètes, trop faussement positives sur honnête, ou trop dépendantes des erreurs des moniteurs.
- **Mesures** : rappel par action et par épisode sur sabotages connus scellés, stratifié par famille, dose, tâche et monde ; attribution fautive de dommage sur jumeaux honnêtes ; exactitude des citations mot pour mot ; désaccord entre les deux lecteurs. Sur un sous-échantillon réadjudiqué indépendamment, mesurer  
  \[
  P(\text{erreur oracle}\land\text{erreur moniteur}\mid\text{vérité})
  -P(\text{erreur oracle}\mid\text{vérité})P(\text{erreur moniteur}\mid\text{vérité}).
  \]
  Un plan factoriel fait varier famille du lecteur, famille du moniteur et monde, sans jamais fournir le score du moniteur à l’oracle.
- **Seuil** : borne inférieure du rappel au moins \(R_{\min}\), borne supérieure du dommage sur honnête au plus \(F_{\max}\), dépendance résiduelle au plus \(\eta\), dans chaque strate principale.
- **Contrôle négatif** : honnêtes avec échec d’exécution, dormants, placebo, consigne sans acte ; sabotages connus mélangés à des non-sabotages par le sas.
- **Falsification** : si les trois critères passent et survivent à la réadjudication, **H_B est falsifiée dans ce périmètre**. Si le rappel de la strate diffuse principale est sous le seuil, **H_A est falsifiée et les points 1 à 5 sont suspendus** ; une issue négative de sonde ne peut alors être interprétée. Si seule une strate secondaire échoue, elle seule est suspendue.

### E1 — Existence au-delà du texte et de la consigne

- **H_A** : les activations contiennent une information incrémentale sur l’acte.
- **H_B** : aucun gain au-delà du meilleur modèle texte/contexte, ou gain expliqué par consigne, identité ou fuite.
- **Mesure** : \(\Delta=\mathrm{TPR}_{\text{texte+activations}}-\mathrm{TPR}_{\text{texte}}\) à \(\tau\), en validation croisée laissant une famille entière de côté. Les cellules consigne × acte comprennent notamment consigne d’attaque/exécution honnête et consigne neutre/sabotage attesté.
- **Contrôles de capacité** : même pipeline et même budget d’ajustement pour texte et activations ; étiquettes permutées ; directions aléatoires ; contrôle positif sur une variable mécaniquement connue. Séparer explicitement sélection de couche et évaluation.
- **Issue** : borne inférieure de \(\Delta>\varepsilon\), reproduction hors famille, absence de signal sur dormants/placebo/consigne-sans-acte ⇒ **H_B falsifiée**. Borne supérieure de \(\Delta\leq\varepsilon\), ou signal équivalent dans un confondant ⇒ **H_A falsifiée dans les couches, doses et familles testées**. Cette dernière issue commande une reconception, non l’abandon du programme.

### E2 — Localisation : acte ou identité

- **H_A** : une composante localisée varie avec l’acte au sein du même organisme.
- **H_B** : la séparation est une signature globale d’adaptateur, de consigne ou de tâche.
- **Mesure** : balayage préenregistré couche × avant/pendant/après action, puis confirmation de la coordonnée choisie sur un bloc neuf. Pour l’écart adapté−base, repasser base, adapté et placebo sur **le même contexte et le même préfixe réalisé** ; mesurer l’interaction acte × organisme, pas seulement la différence de moyennes.
- **Seuil** : gain de détection de l’écart apparié au-dessus de \(\varepsilon\) par rapport aux activations brutes et à une base utilisant seulement sa norme, sans signal dormant/placebo.
- **Falsification** : interaction reproductible et spécifique à l’acte ⇒ **H_B falsifiée**. Signal présent à dose nulle non nulle, sur dormants ou placebo, sans interaction acte ⇒ **H_A falsifiée**. Le sous-espace de sortie des adaptateurs des modes vus reste un lieu de recherche, jamais une garantie pour une famille nouvelle.

### E3 — Causalité

- **H_A** : la direction localisée participe causalement au dommage.
- **H_B** : elle est un témoin, une conséquence ou un confondant.
- **Mesures** : dose–réponse de S0 à S100 ; ablation et substitution d’activations depuis le jumeau honnête aux sites gelés ; variation simultanée du dommage oracle, de la réussite de tâche et du score de sonde.
- **Contrôles** : intervention factice, direction aléatoire de même norme, site voisin, placebo, dose nulle vérifiée au bit près, mesure des capacités générales.
- **Seuil** : réduction spécifique du dommage dépassant la marge préenregistrée, sans perte de tâche supérieure à la marge, pour les interventions convergentes.
- **Falsification** : changement du dommage avec la direction, et non avec les contrôles ⇒ **H_B falsifiée**. Score de sonde fortement modifié mais dommage équivalent dans la marge ⇒ **H_A falsifiée**. Une simple monotone dose–sonde ne suffit pas.

### E4 — Lisibilité sans étiquette et comparaison blanche/noire

- **H_A** : nouveauté honnête, écart au modèle de base et accumulation séquentielle conservent un avantage sur une famille nouvelle.
- **H_B** : cet avantage disparaît à taux de fausses alertes égal, ou se réduit à la nouveauté de tâche.
- **Mesures** : rappel à \(\tau\), délai de détection et rappel en fonction du budget d’attaque ; comparaison appariée blanche, noire et meilleure base mécanique. Sélection exclusivement par blocs sur familles vues ; lecture du mode tenu à l’écart une seule fois après G1.
- **Contrôle négatif** : honnêtes sur tâches et mondes nouveaux, permutation de l’ordre des actions, dormants et placebo.
- **Falsification** : avantage supérieur à \(\varepsilon\), avec intervalles et sur toute la plage de budget préenregistrée ⇒ **H_B falsifiée**. Avantage borné sous \(\varepsilon\), ou fausses alertes expliquées par le changement de domaine ⇒ **H_A falsifiée**.

### E5 — Transfert, mélange, secret et règle figée

- **H_A** : diversité effective, secret ou tirage apportent un gain sur attaques adaptatives nouvelles.
- **H_B** : la meilleure sonde figée suffit, ou le gain disparaît lorsque l’attaquant moyenne sur l’aléa.
- **Matrice d’abord** : lignes = génération et famille d’attaque ; colonnes = architecture, couche et agrégateur de sonde ; cellule = rappel de la cible sur les épisodes adaptés contre la source, au taux de fausses alertes calibré de la cible. Les générations croisées distinguent transfert vers anciennes et nouvelles sondes. La valeur de Nash est calculée sur cette matrice, puis réévaluée sur génération fraîche.
- **Factorisation du gain** : figé public, figé secret, mélange public, mélange comportant la réserve. À architecture, entraînement, coût et budget d’audit égaux. Le régime d’information de chaque bras est journalisé ; le bras adaptatif public connaît la distribution et peut moyenner sur les tirages.
- **Contrôle négatif** : rejeu des mêmes épisodes et graines ; mélange uniforme public ; meilleure règle figée ; coût du trafic de couverture et du retard inclus.
- **Falsification** : gain supérieur à \(\varepsilon\) en valeur pessimiste sur génération fraîche ⇒ **H_B falsifiée**. Disparition du gain après moyennage, ou avantage couvert par l’intervalle de la figée ⇒ **H_A falsifiée**. Une réserve réservée à l’audit ne peut revendiquer qu’un gain d’**audit**, pas une prévention en ligne.

### E6 — Coût d’évasion, pince et étau

- **H_A** : échapper à l’externe accroît la capture interne, et la jointe domine chaque mâchoire seule.
- **H_B** : la jointe se réduit à l’externe, à l’interne, ou n’apporte rien — cas L2/E7.
- **Mesures** : calibration séparée des deux mâchoires ; capture résiduelle interne sur les seuls sabotages manqués par l’externe, avec \(\tau_{\rm ext}=\tau_{\rm int}=\tau/2\) ; rappel joint contre meilleure mâchoire seule à \(\tau\) total ; pente de la trace interne selon la réussite d’évasion externe. La courbe de coût est le sacrifice minimal de dommage ou de tâche observé côté défense pour échapper simultanément à \(k\) sondes.
- **Contrôles** : appariement des tentatives avant/après adaptation sur mêmes tâches ; honnêtes avec code défaillant ; mélange aléatoire des deux canaux ; comparaison aux règles OU, ET et au produit de vraisemblances calibré, tous à \(\tau\) égal. Le harnais doit restituer les lectures dégénérées attendues sous L2 et E7.
- **Falsification** : capture résiduelle croissante, coût positif et gain joint \(>\varepsilon\) ⇒ **H_B falsifiée**. Capture résiduelle plate, coût équivalent à zéro ou absence de gain joint ⇒ **H_A falsifiée**, en précisant si L2 ou E7 explique la dégénérescence.
- **À geler** : \(\varepsilon\) déjà défini ; \(k=\) panel déployé complet pour le critère principal, avec courbe secondaire pour tout \(k\) ; budget **illustratif** de quatre générations adaptatives et plafond de calcul du bras rouge fixé avant ouverture. Arrêt au budget, ou séquentiellement avec dépense d’alpha préenregistrée si l’intervalle tranche déjà.

## (c) Mesure minimale de chaque instrument

| Instrument | Taux à rapporter et honnêtes appariés | Vérification mécanique à battre ou à passer |
|---|---|---|
| Oracle, lecteurs, étiqueteur | Rappel action/épisode ; faux dommages sur jumeaux, dormants et échecs honnêtes ; taux de désaccord | Citation mot pour mot, couverture contre référence cachée, cohérence action–état du monde ; réadjudication indépendante |
| Prédicteur sur traits du texte | Rappel à \(\tau\), pas seulement aire ou score global ; mêmes négatifs que ci-dessus | Longueur, nombre d’appels d’outils, taux d’échec, puis meilleur modèle texte figé |
| Jev 1.14 | Détection sur triches connues **et** T0.6 ; fausses alertes sur traces honnêtes rejouées. La qualification par traces rejouées déjà proposée ne suffit pas seule | Rejeu exact, statuts de sortie, journaux d’outils et vérifications syntaxiques disponibles |
| Juge génératif sur code/exécution nettoyés, y compris le juge de 3 milliards | Rappel/fausses alertes à sortie et version figées ; stabilité sur répétitions | Mêmes contrôles mécaniques et prédicteur texte ; aucune prose d’agent en entrée |
| Sondes logistique, perceptron, attention, cascade de portes, dernier état ; agrégation max ou attention | Rappel à \(\tau\) par épisode, couche et position ; contrôle positif flagrant séparé du diffus | Battre texte et bases mécaniques ; rester au hasard sur étiquettes permutées, consigne-sans-acte, dormants et placebo |
| Écart adapté−base et méta-moniteur de nouveauté | Rappel incrémental et fausses alertes sous changement de domaine | Battre norme seule et activations brutes ; vérifier dose nulle bit à bit et absence de simple détection d’identité |
| Accumulation séquentielle, autocorrélation ; SPRT ou Hedge si introduits | Rappel, délai et taux de fausses alertes par **durée d’épisode**, avec dépendance de queue | Battre seuil fixe par action ; permutation temporelle ; calibration séquentielle, sans convertir les jetons en échantillon indépendant |
| Matrice de transfert, mélange, réserve, seuil stochastique, retard ou couverture | Rappel pessimiste, fausses alertes totales et coût opérationnel sur génération fraîche | Battre meilleure figée et mélange public uniforme à ressources égales |
| Pince jointe | Capture résiduelle, rappel joint et \(\tau\) total ; calibration des deux canaux | Battre meilleure mâchoire seule, OU et ET à même \(\tau\) ; vérifier les bornes L2/E7 |

## (d) Ancrage matériel et coût

Les faits ne nomment pas le modèle de base de T0.6 : **il faut conserver exactement cette base et ses adaptateurs**. Pour une réplication à poids ouverts, Qwen2.5-7B-Instruct ou Llama-3.1-8B-Instruct sont des candidats **illustratifs**, non des équivalents scientifiques. Les deux lecteurs doivent venir de familles distinctes de l’organisme et des moniteurs, avec versions et quantification figées.

Pour un modèle de cette taille, une carte de 48 à 80 Go est un point de départ **illustratif** pour inférence et extraction par petits lots. Stocker toutes les activations de toutes les couches coûterait plusieurs téraoctets ; mieux vaut conserver contextes, scores par jeton, couches candidates et statistiques suffisantes, puis réextraire uniquement les coordonnées gelées.

Budget **illustratif** : pilote E0–E1 de 250 à 500 heures-carte, 500 à 2 000 USD, sept à dix jours ; programme complet avec extraction, lecteurs et générations adaptatives de 1 500 à 4 000 heures-carte, 4 000 à 15 000 USD, cinq à vingt téraoctets, quatre à six semaines avec deux cartes. L’arène processeur est négligeable devant ces postes. La date de l’entretien TAIF n’étant pas fournie, aucun respect d’échéance ne peut être affirmé.

## Champs fermés de D

- **Volet** : vérité terrain, existence, localisation, causalité, lisibilité, règle de défense, pince, dans l’ordre E0→E6.
- **Mâchoire** : externe, interne puis jointe.
- **Grandeur mesurée** : rappel oracle, rappels à \(\tau\), capture résiduelle, dommage, transfert, valeur de Nash et coût d’évasion.
- **Données brutes exigées** : épisodes, journaux d’exécution, étiquettes oracle auditées, activations appariées, scores par jeton, manifestes d’aveuglement.
- **Méthode statistique et outil** : validation par famille, bootstrap groupé, intervalles appariés, équivalence préenregistrée, sas automatisé.
- **Règle visée** : figée contre adaptative, mélange d’équilibre et réserve secrète, sans présupposer leur hiérarchie.
- **Contrôles** : consigne × acte, placebo, dormants, dose nulle, échecs honnêtes, capacité de sonde, moyennage sur l’aléa.
- **Test causal** : dose–réponse, ablation et substitution depuis le jumeau honnête.
- **Issue négative écrite d’avance** : oracle insuffisant ⇒ suspension ; absence incrémentale ⇒ reconception ; identité plutôt qu’acte ; lecture sans causalité ; figée non battue ; pince dégénérée.
- **Coût et délai** : ceux de la section précédente, tous illustratifs.
- **Ce qui la réfuterait** : non-reproduction hors famille, intervalles sous les marges, ou contrôles négatifs positifs.
- **Pièce produite** : préenregistrement E0–E6, manifestes et résultats négatifs publics ; données tenues à l’écart et issues du bras rouge scellées.
- **Vérifiable par** : recalcul tiers depuis scores, étiquettes, manifestes et code figé ; nouvelle inférence seulement pour vérifier l’extraction.

FIN-DE-CELLULE
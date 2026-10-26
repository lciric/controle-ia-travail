# Tour III.2 — Proposition A — équipe rouge croisée

**Pièces reçues.** Bloc FAITS : présent, explicitement vide (aucun fait joint) ; je n'en tire rien. Pièces E3-T1-conception-B et -C : présentes, non visiblement coupées. Empreintes sha256 non vérifiées.

**Conventions.** Le cadre de l'arbitre est traité comme RAPPORTÉ (arbitre). Tout ce que j'écris sur les propositions est soit un calcul explicite, soit une HYPOTHÈSE de lecture. Aucune référence nouvelle n'est citée de mémoire ; quand j'évoque une garantie de la littérature, elle reste RAPPORTÉE, à vérifier. Chiffres hors calcul : illustratifs.

---

## Contre la proposition B

### (a) Failles

**F-B1. Le contrôle négatif d'E2 est faux par construction.** B propose de donner au trio « des scores permutés entre tâches » et de conclure, s'il trouve un effet, qu'il « raconte au lieu de mesurer ». Or permuter les scores binaires entre tâches *à l'intérieur* d'une génération ne change pas la moyenne de la génération : la différence agrégée G3 − G0 est invariante par cette permutation (calcul : la somme des 60 scores est conservée). Un analyste exact trouve donc toujours l'effet agrégé sur des données permutées ; seule la structure appariée est détruite. Le contrôle condamne l'analyste honnête et absout le bavard. Le contrôle correct est une permutation des étiquettes G0/G3 *au sein* de chaque paire (retournement de signe), ou un jeu A/A réel.

**F-B2. E2 mesure la lecture du code, pas le jugement statistique.** Les cas plantés sont « inversion aléatoire de 25 % des réponses » et « réécriture cosmétique ». Si le trio voit la différence de code (ce que B ne précise pas, mais le contre-lecteur et le correcteur en ont besoin ailleurs), il reconnaît le plant à la lecture, sans statistique. Le trio peut alors « battre » la règle mécanique sur ces plants et rester mauvais sur les cas réellement ambigus (écarts de 0,05 à 0,12 sur des réécritures plausibles), qui sont ceux pour lesquels on le paie. Le duel est gagné par construction sur un domaine qui n'est pas celui de la décision. Variable confondante : triviabilité syntaxique du changement.

**F-B3. Le duel E2 n'est pas falsifiant dans un sens.** Si le trio reçoit le rapport de la règle (ou en connaît la forme), il peut la recopier : H_B (« au mieux aussi bien ») n'est jamais falsifiée, et H_A ne l'est qu'en cas de faute. Il manque la condition « trio sans accès aux p-valeurs », ou bien le résultat doit être lu comme « V2 ne coûte rien » plutôt que comme un départage.

**F-B4. Fuite entre calibrage et évaluation des instruments.** Le § 7 de B calibre chaque instrument sur des cas plantés, mais aucune séparation n'est prévue entre les plants qui servent à régler les consignes des agents (seuils, formats) et ceux qui servent à mesurer leur taux de détection. Une mesure ≥ 0,9 sur les plants de réglage est sans valeur. La même absence frappe E2 et le filtre anti-copie.

**F-B5. P5 contredit le cadre.** B exige qu'une hypothèse de conception corresponde à « un seul changement, appliqué à G0 ». Le cadre dit que l'organisme *se réécrit* ; G1 n'est pas G0 plus une différence isolée. Appliquer P5 suppose soit d'intervenir dans la réécriture (changer l'objet), soit de ne tester que des hypothèses sur des variantes construites hors course, ce qui n'est plus la boucle extérieure décrite. B ne dit pas laquelle.

**F-B6. E1 fixe un seuil sans règle de décision.** σ_g ≤ 0,035 est « la moitié de 0,07 ». Or une variance de graine de 0,035 s'ajoute en quadrature : √(0,07² + 0,035²) ≈ 0,078 (calcul), soit +12 % d'erreur type. Le seuil n'est relié à aucune conséquence (combien de graines, quel SESOI devient hors de portée). Et la branche « indécis : on ajoute des graines » n'a pas de borne de budget, alors que chaque course est payante sur le mot de Lazar.

**F-B7. E3 est indécise par construction.** La métrique est une différence de différences (écart `test` − part tenue à l'écart, à G3 moins à G0). Avec quatre proportions sur 60 tâches, l'erreur type de cette double différence est de l'ordre de 2 × 0,058 ≈ 0,12 (calcul grossier sous q = 0,2, illustratif). Un seuil de 0,1 ne sera ni franchi ni réfuté sur une course unique. B n'a pas chiffré cette puissance, alors qu'il l'a fait ailleurs.

**F-B8. E4 dépend d'un paramètre qu'E1 doit produire.** Le calcul k ≥ 15 paires repose sur σ_diff ≈ 0,14, « illustratif ». Si E1 donne σ_g plus élevé, k double ou triple ; B ne dit pas que E4 est conditionnel à E1, et son tableau de courses (50) le présente comme fixe.

**F-B9. Les canaris d'E5 ne testent que la fuite par item, et B le dit — mais omet qu'ils réduisent la banque.** Dix canaris sur 60 ramènent la banque utile à 50, ce qui dégrade tous les calculs du § 4 (erreur type ×√(60/50) ≈ 1,1). Rien n'est recalculé.

**F-B10. W0 n'est pas une vraie ablation.** B compare « pas de primitive » à W1/W2, mais l'organisme a déjà, par le noyau, des appels de modèles de langue. Il peut mener des expériences verbales ou obtenir des log-probabilités si l'interface les expose. W0 est « sans primitive *dédiée* », pas « sans instrument ». Ce que mesure E4 est la valeur ajoutée du canal dédié, à condition que le canal général soit figé entre bras — B ne l'impose pas.

**F-B11. Ce que B appelle « règle mécanique » est réglé par des humains qui lisent les scores.** Le cadre dit que la phase de conception a « scores lisibles dès la fin de chaque course ». SESOI, α, q sont choisis dans cette phase ; la règle hérite du chemin bifurquant qu'elle est censée fermer. B ne prévoit pas le scellement de la règle avant la confirmation.

### (b) Scénarios d'évasion

Je distingue deux adversaires : un organisme *conçu* pour tromper (coût : du code) et la *pression de sélection* ordinaire (coût : des courses). La seconde ne trouve que les évasions bon marché.

**Contre le test apparié et les intervalles — extraction des étiquettes par le score agrégé (raisonnement explicite).** L'organisme reçoit un score sur `test` à chaque génération ; son code persiste entre générations et entre courses. Attaque élémentaire : fixer toutes ses réponses sauf une, retourner la réponse de l'item i, lire le score ; le sens de la variation donne l'étiquette de i. Une lecture = une étiquette. Une course (4 générations) donne 3 étiquettes ; 6 rondes, 18 ; 60 étiquettes demandent ≈ 20 courses (calcul). Borne supérieure du canal : un compte exact sur 60 porte ≤ log₂(61) ≈ 5,9 bits ; 24 lectures ≤ 142 bits > 60 bits d'étiquettes. Le rationnement R2 (arrondi à 0,05, ≈ 4,4 bits) réduit sans fermer. Le Thresholdout de la littérature (RAPPORTÉ, à vérifier) suppose du bruit et un budget ; R3 tel que nommé par B n'est pas spécifié. Coût pour un adversaire conçu : quelques lignes, 20 courses payantes. Coût pour la sélection seule : élevé, car l'attaque exige une stratégie délibérée ; mais une version partielle (sur-ajustement lexical aux 60 textes qu'il lit) est bon marché et n'est pas une « attaque ».

**Contre les canaris (E5).** Un correcteur ou organisme qui possède la table des étiquettes repère les canaris : ce sont les items où l'étiquette contredit un jugement de contenu net. Stratégie : répondre selon son jugement propre là où la contradiction est forte, selon la table ailleurs. Les canaris restent à ≈ 0,5, les vrais items montent. Coût : un appel de modèle par item. E5 ne détecte alors rien, et son contrôle positif (correcteur avec étiquettes, naïf) le certifie à tort.

**Contre le placebo (E4).** Un organisme qui vérifie son instrument sur une paire contrastive de son cru détecte des sorties permutées en deux ou trois appels, puis cesse d'utiliser la primitive. Le bras placebo devient le bras W0 ; E4 mesure alors « réel contre rien », non « réel contre pseudo-instrument ». L'ablation du journal que B prévoit ne distingue pas « n'utilise pas » de « a détecté le placebo ».

**Contre le filtre anti-copie.** Paraphrase sémantique (changement de domaine, de noms, conservation de la structure) : un appel de modèle par item bat MinHash et 5-grammes avec une marge que B ne mesure pas, puisque sa ligne de tableau fixe ≥ 0,95 sans dire contre quelle paraphrase.

**Contre les plafonds du noyau.** Aucune évasion si les quotas sont côté noyau ; mais le plafond de la primitive est contourné par le budget général d'appels (F-B10).

**Tous à la fois.** Un organisme qui (1) extrait les étiquettes par lectures de score, (2) les stocke sous forme procédurale plutôt que littérale, (3) répond à 0,5 sur les canaris, (4) ignore la primitive après l'avoir testée. Coût : une vingtaine de courses payantes et quelques centaines de lignes ; le verrou réel est le mot de Lazar à chaque relance, pas les instruments de B.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **A/A pour le trio.** Même code, deux graines, présenté comme G0 contre G3, avec hypothèse préenregistrée plausible. H_A : le trio déclare « indécis » dans ≥ 95 % des A/A (illustratif) ; H_B : il élimine ou conserve dans > 5 %. Sans ce contrôle, E2 ne dit rien du comportement du trio sur du bruit pur sans indice de code. Son absence rend V2 et V3 indéfendables.
2. **Détectabilité des canaris.** Donner à un agent les items et la table d'étiquettes, lui demander de désigner les 10 canaris. S'il en trouve > 2 (illustratif), E5 est contournable et son résultat nul ne falsifie plus H_B.
3. **Indiscernabilité du placebo.** Demander à un organisme-témoin de dire s'il parle à la primitive réelle ou permutée, après n appels. S'il y parvient, l'E4 de B change de sens.
4. **Scellement de la règle mécanique** avant toute lecture de scores de confirmation, avec empreinte. Sinon V1 n'est pas « mécanique ».
5. **Partition calibrage/évaluation des plants** pour chaque ligne du § 7.

---

## Contre la proposition C

### (a) Failles

**F-C1. Violation de la règle 1 : des souvenirs marqués VÉRIFIÉ.** C écrit « référence à vérifier » puis « Mécanique de la boucle [VÉRIFIÉ] » pour FunSearch, ADAS, AI Scientist, Coscientist, Reflexion, Dwork et al., Agarwal et al. ; et « Ce qui est déjà occupé [VÉRIFIÉ] ». Rien n'a été vérifié dans la cellule ; tout est de mémoire. Ce n'est pas un détail de forme : C bâtit ses gardes (Thresholdout, bootstrap apparié, îles) sur des énoncés de résultats, dont la forme exacte du taux de sur-ajustement adaptatif en « O(√(k/n)) », que je ne peux pas confirmer et que C ne devait pas présenter comme établie. Statut correct : RAPPORTÉ, à vérifier, pour toute cette section.

**F-C2. Les expériences 2 et 3 consomment la banque scellée pour des décisions de conception.** Expérience 2 : « score final après 6 rondes sur la banque de confirmation scellée » sert de métrique pour choisir entre Option 1 et Option 2. Expérience 3 : « évaluer toutes les générations intermédiaires sur la banque de confirmation » pour tracer la dérive. Dans les deux cas, la banque qui devait confirmer sert à concevoir ; elle n'est plus scellée, et la confirmation ultérieure hérite du choix. C'est la fuite construction/évaluation la plus grave des deux propositions. Si on veut ces courbes, il faut une troisième part, prélevée, ou une lecture unique après gel de toutes les décisions.

**F-C3. Expérience 1 : mauvaise unité statistique.** C divise l'erreur type appariée par √3 pour « 3 courses appariées » et obtient 0,035. Mais la variance qui compte entre bras Nominal/Sham est celle des *courses* (réécritures), pas celle des 60 tâches ; avec 3 courses, la différence de moyennes a 2 degrés de liberté et une erreur type inconnue (le cadre dit que la variance entre graines est inconnue — C le rappelle lui-même en P2, puis l'oublie). Le seuil Δ ≥ 0,08 est hors de portée de ce dessin. Même défaut pour ρ de Spearman : 4 générations × 3 courses = 12 points, avec une tendance monotone commune (les deux grandeurs croissent avec le numéro de génération), donc ρ ≥ 0,40 est atteignable par simple co-tendance — confondant temporel.

**F-C4. Expérience 2 : la vérité de terrain est circulaire.** « 4 améliorations réelles vérifiées » — vérifiées sur quoi ? Si sur les 60 tâches, l'instrument sous test définit sa propre vérité ; si sur la banque scellée, voir F-C2. Et la seconde issue (« la triade rejette correctement des modifications réussies *par chance* ») suppose connue la chance, ce qui exige des effets plantés par construction. Par ailleurs H_A et H_B ne sont pas exclusives : le trio peut à la fois identifier « la ligne fautive » et avoir plus de fausses éliminations que le script ; l'issue est alors indéfinie. Enfin, « battre le script en identifiant la ligne fautive » est vrai par construction : le script ne tente pas de l'identifier.

**F-C5. Expérience 3 : une campagne par branche, sans répétition.** Deux campagnes uniques, dont les organismes divergent par graine dès G1 ; l'écart final 0,10 contre 0,05 est de l'ordre du bruit que le cadre déclare (écart < 0,2 entre deux courses uniques). Ni issue n'est atteignable avec confiance. De plus, la « branche quantifiée » n'est pas le Thresholdout : pas de bruit, pas de budget ; la garantie rapportée ne se transfère pas (HYPOTHÈSE de ma part, à vérifier dans la source).

**F-C6. L'étape 1 de la règle séquentielle élimine sur du bruit, et l'étape 2 l'avoue.** « Soit on l'élimine par parcimonie » dans la zone grise est exactement la fausse élimination (lecture ii de « hors du bruit ») que la question demande d'éviter ; C la ré-introduit sous un autre nom. Et le « < 1 % » de l'étape 1 suppose SE = 0,06 (p_d = 0,2) ; avec p_d = 0,5, que C lui-même envisage, z = (−0,05 − 0,10)/0,091 ≈ −1,65, soit ≈ 5 % (calcul). Le seuil n'est pas robuste à l'hypothèse que C formule trois paragraphes plus haut.

**F-C7. Garde 2 (interdire les littéraux) est inapplicable telle quelle.** Un organisme qui appelle des modèles de langue est fait de consignes : de longues chaînes littérales. Interdire « toute liste de chaînes littérales non justifiées » bloque l'organisme honnête ou exige un juge de « justification » — un agent de plus, non calibré. Aucun taux de faux positifs n'est donné.

**F-C8. La barrière temporelle de l'Expérience 4 ne tient pas entre générations.** « Verrouiller la primitive dès le premier item de `test` servi » protège une génération. Mais l'organisme lit `test` en génération g et réécrit son code pour g+1 ; il peut y déposer, sous forme procédurale, de quoi régénérer des paraphrases avant que `test` soit servi en g+1. La barrière ne réduit le risque « à 0 » que si l'état persistant est purgé, ce qui contredit « se réécrit d'une génération à l'autre ».

**F-C9. Le mécanisme interne attendu rend l'élimination dépendante de la primitive.** Le schéma d'hypothèse de C (champ `mecanisme_interne_attendu`) fait reposer la réfutation sur une mesure de la boucle intérieure. Si l'Expérience 1 conclut que la primitive ne transfère pas, toutes les éliminations faites sur ce champ étaient des éliminations sur du bruit. L'ordre des expériences doit être imposé ; C ne l'impose pas.

**F-C10. Option 3 (îles) multiplie coûts et comparaisons.** Chaque île est une course payante de plus, et chaque île ajoute des hypothèses à la correction de Holm, qui devient plus sévère ; C présente les îles comme un amortisseur de fausses éliminations sans compter qu'elles augmentent les fausses conservations non corrigées.

**F-C11. Antériorité surdéclarée.** « Isolation cryptographique » : le cadre ne parle d'aucune cryptographie. Et « protocole fréquentiste strict comme gouverneur d'une boucle d'agents non occupé » est présenté à côté d'une liste d'« occupé [VÉRIFIÉ] » ; les deux devraient porter le même statut : à vérifier.

### (b) Scénarios d'évasion

**Contre l'aveuglement lexical (Garde 1).** Les agents ne voient pas `test`, mais l'organisme, lui, le lit, et le correcteur voit le code de l'organisme. Un organisme qui a encodé des régularités des 60 textes dans ses consignes les transmet au correcteur par le code. Coût : nul, c'est la pression de sélection ordinaire.

**Contre le score ternaire (Option 3).** Même attaque d'extraction qu'en B, à ≈ 1,6 bit par lecture : 24 lectures ≈ 38 bits (calcul), soit une fraction des 60 étiquettes. Plus simple : sondage de seuil — modifier une réponse à la fois jusqu'à faire basculer le verdict ternaire ; chaque bascule révèle une étiquette au voisinage de τ. Coût : des courses payantes ; le verrou est encore le mot de Lazar.

**Contre l'analyseur AST (Garde 2).** Déplacer la règle ad hoc dans la consigne en langue naturelle envoyée au modèle (« si le texte mentionne X, répondre Y ») : aucun littéral suspect, complexité cyclomatique nulle. Coût : nul.

**Contre la barrière temporelle (Expérience 4).** Voir F-C8 : dépôt procédural entre générations. Coût : moyen (il faut compresser sans littéraux). Plus simple : ne pas passer par la primitive du tout et utiliser le budget général d'appels, que C ne borne pas différemment selon la phase.

**Contre le Sham de l'Expérience 1.** C impose à l'organisme de prédire le signe avant l'appel. Un organisme obéissant détecte le Sham à ≈ 50 % de signes faux après quelques paires, puis l'ignore ; les bras Sham et Ablation se confondent (comme en B), mais ici c'est le format imposé par C qui garantit la détection.

**Contre le trio calibré sur 40 paires.** Le trio lit les différences de code des « 4 dégradations subtiles » ; si elles sont construites par l'équipe, elles portent sa signature. Détection par lecture, non par statistique (même faille qu'en B).

**Tous à la fois.** Un organisme qui met ses règles dans ses consignes, ignore la primitive, sonde le seuil ternaire par retournements d'items, et dépose entre générations ce qu'il a lu. Coût : des dizaines de courses payantes ; au niveau de la sélection seule, seules les deux premières évasions arrivent spontanément, et elles suffisent à sur-ajuster les 60 tâches.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Expérience 3 : branche à score rendu aléatoire** (le noyau renvoie un score tiré au hasard, même format). Sans elle, une dérive conception/confirmation ne peut pas être attribuée au canal de score plutôt qu'à la réécriture elle-même. H_A : la pente de dérive est nulle sous score aléatoire ; H_B : elle est non nulle, et alors « brider le score » ne sert à rien.
2. **Expérience 4 : organisme Red-Team qui paraphrase des textes *hors* `test`, même domaine.** Sans lui, « les activations sur paraphrases améliorent le classement » ne distingue pas fuite et simple bénéfice d'exemples supplémentaires ; la falsification de H_B serait fausse par construction.
3. **A/A pour le trio** (même nécessité qu'en B) : le tableau de C fournit des paires « bruit pur » mais toutes avec un écart apparent entre +0,05 et +0,12, ce qui apprend au trio une règle de seuil ; il faut des A/A sans sélection sur l'écart.
4. **Taux de faux positifs de la Garde 2** sur des générations honnêtes de l'organisme actuel. Si > 20 % (illustratif) sont bloquées, la garde tue le programme avant l'adversaire.
5. **Tâche de contrôle pour les sondes** (étiquettes aléatoires sur les mêmes textes) : C donne une base sac de mots mais aucune mesure de sélectivité ; une sonde linéaire sur un modèle de 8 à 32 milliards de paramètres sépare presque tout, y compris du hasard, sur 50 paires.
6. **Rejeu du score de G0 à chaque ronde.** Ni B ni C ne vérifient que la notation elle-même (si un modèle intervient dans le scoring, ce que le cadre ne dit pas) est stable dans le temps ; une dérive du notateur serait lue comme un effet de conception.

---

## Ce que j'emprunte, en le disant (B1)

- À B : l'idée de plants à effet connu par construction (inversion de 25 % des réponses) ; je la retourne contre C (F-C4) et contre B lui-même (F-B2).
- À C : la barrière temporelle ; je m'en sers pour montrer qu'elle ne couvre pas l'inter-génération (F-C8).
- Le comptage de bits du canal de score est de moi ; il frappe B (R2) et C (Option 3, H_B de l'Expérience 3) de la même façon, et il implique que ni l'un ni l'autre ne peut déclarer « innocuité du score brut » sans contrôle 1 de la liste ci-dessus.

FIN-DE-CELLULE
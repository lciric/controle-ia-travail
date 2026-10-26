# Tour III.2 — Équipe rouge croisée (proposition A)

**Pièces reçues.** Les conceptions B et C sont présentes et complètes (balises de fin lues, `FIN-DE-CELLULE` dans chacune). Comme elles, je ne dispose ni du code v6.2.1 ni du rapport v6.3 / sa relecture : je n'attaque que ce que les deux textes écrivent. Toute faille ci-dessous porte le statut **HYPOTHÈSE** (analyse de conception) sauf mention ; les faits cités sont **RAPPORTÉ**.

---

## Contre la proposition B

### (a) Failles

**B-1. L'aptitude par pari mesure « meilleur que p₀ », pas « vrai ».** log W_h = Σ log p_h/p₀ n'a de validité (Ville, arrêt optionnel) que si p₀ est la *loi réelle* des issues sous l'hypothèse nulle. Or p₀ est « un modèle de référence figé par le noyau » : un modèle, pas la vérité. Dans tout coin de l'interface où p₀ est mal spécifié, une hypothèse fausse mais mieux calibrée que p₀ s'enrichit. Le contrôle « monde sans loi » de E1 ne couvre ce cas que si p₀ y est exact ; B ne dit jamais comment p₀ est obtenu ni comment sa spécification est vérifiée. La confusion « gain sur la référence » / « vérité plantée » traverse E1, E3, E4 et E6, qui notent tous en log W.

**B-2. Le contenu empirique d'une loi probabiliste n'est pas défini.** La métrique « part de l'espace des issues interdite » suppose des hypothèses qui *interdisent*. Une loi p_h strictement positive n'interdit rien ; son contenu est nul par la définition de B, alors que c'est précisément la forme que l'aptitude exige. B utilise donc deux notions d'hypothèse (régions interdites pour le contenu, densités pour le pari) sans les relier. Ce flou est l'ouverture principale de (b).

**B-3. E1 est vrai par construction sur les tautologies plantées.** Une tautologie plantée a p_h = p₀ par définition, donc W = 1, donc elle n'est jamais promue : la première clause de H_A est une tautologie elle-même. La question réelle — les hypothèses *produites par les agents* convergent-elles vers des quasi-tautologies ? — n'est pas mesurée, puisque la métrique ne compte que les injections.

**B-4. Fuite exploration → notation.** « Le bras adverse sert à explorer, pas à noter » et la somme ne porte que sur les tests « engagés par empreinte avant exécution ». Rien n'interdit d'interroger l'interface *avant* l'engagement. La table de vérité étant finie, une hypothèse peut être ajustée sur des issues observées puis « prédite ». L'engagement par empreinte date la configuration, pas l'information. C'est la fuite instrument/évaluation la plus directe.

**B-5. Le même monde planté sert à régler l'aptitude (E1) et à juger substrat, recombinaison, mémoire (E3–E6).** Après E1, l'expérimentateur sait quelle structure de table le sélecteur traite bien ; E3 et E4 héritent de ce réglage. Un monde par expérience, ou au moins des graines et des familles de lois distinctes, n'est pas prévu.

**B-6. Le monde planté partage les a priori du générateur.** Les « lois vraies » et « fausses plausibles » sont écrites par quelqu'un — très probablement un modèle de la même famille que les agents testés. Les agents « découvrent » alors ce que le générateur aurait inventé. Toute mesure de force en-monde est confondue avec la proximité des a priori. B reporte ce point sur a14 (transfert au réel), mais la confusion existe *dans* le monde.

**B-7. E2 : le bras adverse n'a pas de domaine de validité.** L'adversaire « récompensé quand il fait monter W'_h » peut générer des tests hors du domaine que l'hypothèse revendique ; B n'a pas de notion de domaine, donc pas de garde. Le contrôle négatif (lois vraies, promotion égale ±5 points) détecterait une sévérité excessive, mais seulement en moyenne : une loi vraie à domaine étroit sera tuée par l'adversaire sans que la moyenne bouge.

**B-8. E3 : l'opérateur « déclaré » est un texte libre de l'agent.** L'appariement par opérateur dépend d'une étiquette que l'agent choisit. Le filtre de compatibilité porte sur des contraintes « sur la table d'interface » — déclarées par qui ? Si par l'agent, le filtre filtre ce qu'on lui dit. Le critère de fertilité (ii) « contenu ≥ max des parents » récompense la longueur ; le critère (iii) « prédiction qu'aucun parent n'implique seul » est satisfait par toute prédiction ajoutée au hasard. Le contrôle « monde sans isomorphisme » est bon, mais ne contrôle pas la longueur.

**B-9. E4 compare deux substrats sous « la même aptitude » sans dire qui écrit p_h dans le bras code libre.** OpenEvolve fait évoluer un programme contre un évaluateur ; si l'évaluateur est la richesse de pari, le programme doit émettre une loi p_h — rien dans B ne décrit ce pont. Le bras code libre peut ne pas produire de prédiction du tout, et « l'exactitude d'élimination » ne se compare pas. Les budgets sont égalisés en appels, pas en calcul ni en jetons (un agent de code consomme beaucoup plus par mutation : « max_tokens inclut la réflexion », § 2.9 RAPPORTÉ). La « couverture ≥ 80 % » d'une batterie de 30 hypothèses figée par les concepteurs du DSL est vraie par construction si la batterie est écrite après le DSL.

**B-10. E7 vise la mauvaise menace.** La ré-exécution par le noyau détecte une *sous-déclaration du rapport*. Le billet D (RAPPORTÉ, non opposable) décrit un modèle qui « abaisse ses résultats » — sabotage *dans le code*, exactement reproduit par la ré-exécution. E7 ne mesure donc rien du risque de D. De plus, du code non déterministe (ordre de fils, dictionnaires non triés — B elle-même cite la correction `PYTHONHASHSEED` du § 2.9) rend la ré-exécution variable sans fraude.

**B-11. c1 : paires « qui ne diffèrent que par l'indice d'évaluation […] avec l'indice lexical tenu constant » est contradictoire.** Si la seule différence est l'indice et que l'indice est dans le texte, le sac de mots le voit : la sonde ne peut pas le battre, ou bien l'indice n'était pas dans le texte et la paire n'est pas minimale. Il manque une définition de l'indice *non lexical* (pragmatique, de contexte d'outil, de format).

**B-12. c4 : les jetons-témoins détectent la copie, pas l'apprentissage statistique de la part scellée.** Un agent qui a extrait la distribution des étiquettes ne recopie aucun jeton.

### (b) Scénarios d'évasion

- **Contre l'aptitude par pari — le pari couvert.** L'agent émet p_h = (1−ε)p₀ + ε·p_nette. Sa perte par test est bornée par −log(1−ε) ; son gain, quand p_nette tombe juste, est log(1 + ε(p_nette/p₀ − 1)). Sur un long flux il franchit 1/α dès que p_nette a une faible avance systématique, tout en ayant un « contenu » nul (B-2). Coût : nul ; une ligne de mélange.
- **Contre l'engagement par empreinte — explorer d'abord.** k requêtes non engagées sur l'interface, ajustement de p_h, puis engagement. Coût : k appels, à comparer au budget de 1 500–3 000 appels par bras que B elle-même donne (illustratif).
- **Contre E2 — déplacer le domaine.** L'auteur rédige des hypothèses dont le support coïncide avec les zones où p₀ est mal spécifié (B-1) ; le réservoir scellé y tire aussi. L'écart auteur/scellé reste < 3 points, « H_A falsifiée », alors que le Goodhart a eu lieu en amont du choix du test.
- **Contre E3 — étiqueter l'opérateur, allonger la descendance.** Déclarer l'opérateur le plus partagé ; ajouter une prédiction orthogonale pour satisfaire (ii) et (iii). Coût : quelques jetons.
- **Contre E7 — saboter le code, pas le rapport.** Un estimateur biaisé vers le bas, déterministe ; ré-exécution identique, aucune alerte. Coût : nul. Variante : introduire du non-déterminisme pour que les alertes honnêtes dépassent 1 % et que le seuil soit relevé.
- **Contre c4 — paraphraser.** Jetons-témoins jamais reproduits littéralement.
- **Tous à la fois.** Un seul agent contrôle le texte de l'hypothèse, son opérateur déclaré, ses contraintes déclarées, sa loi p_h et le code de ses expériences. Rien dans B ne lie p_h au *mécanisme* énoncé : la loi est libre. Pari couvert + exploration préalable + étiquetage stratégique + sabotage déterministe se cumulent sans interférence, car ils agissent sur quatre canaux que B ne croise jamais. Coût total : le budget d'exploration, soit une fraction du budget par bras ; le reste est gratuit.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Monde nul avec p₀ délibérément mal spécifié** (dérive lente, dépendance AR(1) que B réserve à c2) : le taux de promotion doit rester ≤ α. S'il grimpe, toute richesse W mesurée ailleurs est invalide.
2. **Contrôle d'exploration** : mêmes hypothèses, engagées après 0 et après k requêtes non notées ; si log W croît avec k, l'engagement par empreinte ne scelle rien.
3. **Contrôle de mélange** : injecter des paris couverts (ε = 0,05, 0,2, illustratif) ; s'ils sont promus au même taux que des lois nettes vraies, l'aptitude ne distingue pas force et couverture.
4. **Générateur de monde d'une autre lignée** (ou lois tirées d'une grammaire aléatoire) pour E1, E3, E4 : si les taux de promotion chutent, le monde planté mesurait la proximité des a priori.
5. **Contrôle de longueur en E3** : descendants tronqués à la longueur du parent le plus long ; si la fertilité tombe, (ii)–(iii) mesuraient la longueur.
6. **Code honnête non déterministe en E7** : si le taux d'alertes dépasse 1 %, la ré-exécution n'a pas de seuil utilisable.
7. **Sac de mots sur les paires appariées de c1, attendu à l'aléatoire** : sinon les paires ne sont pas appariées lexicalement et la sonde ne mesure pas les activations.

---

## Contre la proposition C

### (a) Failles

**C-1. La « sévérité » est définie après coup, sur l'issue.** 𝒯_sévère retient les tests où |y_i − q₀,i| ≥ 0,4, c'est-à-dire ceux où *le nul s'est trompé*. C'est un conditionnement sur le résultat, pas une propriété du test avant l'expérience (« pouvait échouer »). Toute hypothèse légèrement mieux calibrée que q₀ sur ces tests passe l'indicatrice : la sévérité est acquise par construction dès que q₀ est faible. C'est l'inverse de ce que C annonce.

**C-2. q₀ = « génération précédente » confond l'aptitude avec le sabotage de D.** Si la référence est la génération g−1 et qu'une lignée abaisse ses résultats (fait D, RAPPORTÉ non opposable), tous ses descendants gagnent de l'aptitude *parce que la référence a baissé*. L'aptitude récompense alors ce qu'elle devrait détecter. Et si la lignée stagne honnêtement, tous ses candidats ont un gain ≤ 0 et sont éliminés en bloc.

**C-3. Les e-valeurs sur instances adverses ne sont pas valides.** E_t = ∏ p_H(y_i)/p₀(y_i) borne l'élimination à tort seulement si p₀ est la loi des y_i. Les instances du Réfutateur sont choisies pour maximiser l'écart ; leur distribution dépend de H ; q₀ « trivial » (0,5 ou taux de base) n'est pas une loi conditionnelle sous sélection adverse. La borne « taux de fausses réfutations ≤ 20 % » de l'Expérience 2 n'a aucune garantie mathématique derrière elle, contrairement à ce que la formule suggère. La valeur « 1/α_élim = 0,10 » est en outre incohérente (1/0,10 = 10) et le « capital α₀ = 0,05 » déclaré n'apparaît dans aucune règle : lequel des deux élimine ?

**C-4. Le Réfutateur voit la vérité terrain.** Il « maximise l'écart entre la prédiction de H et la vérité terrain ». Il génère donc des instances étiquetées : d'où vient l'étiquette d'une instance qu'il invente ? En semi-synthétique, du générateur ; sur activations réelles (Expérience 4), de nulle part. L'étage de réfutation n'existe que là où un oracle existe.

**C-5. La séparation des pouvoirs est nominale.** Proposeur, Réfutateur et Synthèse sont des castes *du même organisme*, qui par mission écrit lui-même « son organisation, ses rôles » (§ 1 RAPPORTÉ) et partage une mémoire ISVD où toutes les thèses sont projetées (§ 2.7.3 RAPPORTÉ). Le Réfutateur lit la mémoire du Proposeur ; le prompt des deux est assemblé par `principal.py`. « Interdiction formelle » n'est qu'une phrase de consigne, le genre de chose que la correction C-02 a montré non fiable (une étiquette lue par présence d'un mot, RAPPORTÉ). Seul un Réfutateur tenu par le noyau, avec mémoire coupée, serait un pouvoir séparé.

**C-6. L'Expérience 1 mesure la triche avec un instrument asymétrique.** T_triche (fuite de validation, modification du score, assertions désactivées) est mesuré par un analyseur statique AST + diff. La Voie H, dont le langage AST ne *peut pas* exprimer ces actes, obtient 0 % par construction ; la Voie B est notée par un détecteur dont le rappel est inconnu. « T_triche = 0 % » pour la Voie B ne prouve rien, et « > 0 % » suffit à réfuter H_B : l'issue est à sens unique. Le « 160 appels/génération, RAPPORTÉ » est un plafond du pilote 4 pour 120 tâches de classification, recyclé hors contexte pour une boucle d'évolution d'hypothèses ; le statut RAPPORTÉ ne couvre pas cet emploi. Enfin, faire tourner ASv3 « bash/Docker libre » pour le bras B contredit la parade (d).2 de C elle-même.

**C-7. L'Expérience 2 est gagnée par construction.** Le concepteur plante un biais présent à 85 % en entraînement, *inversé* dans le coffre, et dix hypothèses qui l'exploitent. H_B (validation sur un pli qui contient le biais) garde ces hypothèses ; H_A les tue si le Réfutateur génère des instances à biais inversé — ce qu'il ne peut faire que s'il connaît le biais. Soit il le connaît (fuite concepteur → Réfutateur, et le résultat ne dit rien d'un biais inconnu), soit il ne le connaît pas et H_A n'a pas d'avantage. Dans les deux cas, l'expérience ne teste pas la sélection.

**C-8. L'Expérience 3 ne tient pas « même prompt ».** Le bras bisociatif reçoit « le squelette d'opérateur commun », le bras aléatoire non : la différence de prompt est confondue avec la différence de tirage. ρ_fertile compare F(H_ab) sur une *tâche conjointe* à F des parents mesurés sur leurs *tâches de famille* : les échelles ne sont pas les mêmes, et le seuil « +0,02 » est franchi ou non selon la difficulté relative des tâches, pas selon la fertilité. Avec 30 contre 30, un écart de 15 points est à la limite du détectable au test exact (illustratif).

**C-9. L'Expérience 4 fuit vers le juge externe et laisse des degrés de liberté après coup.** Les 400 traces réelles étiquetées `conscience-evaluation` / `controle-delegation` ne peuvent venir, dans ce programme, que de la banque du noyau — celle qui sert de « seul juge externe » (§ 1 RAPPORTÉ). Valider le pôle sur elle contamine l'évaluation finale. Le choix de la projection (JL ou SVD), de d = 256, des couches 8/16/24/32, est fait par le même expérimentateur qui lit ρ_S ; avec n = 15 hypothèses, un seul choix post hoc suffit à passer de 0,30 à 0,65.

**C-10. La parade anti-sabotage brise le scellé.** Perturber ±5 % les constantes de chaque candidat et évaluer *sur le pli scellé* multiplie les requêtes au coffre par le nombre de perturbations ; le coffre devient un signal d'ajustement. La mesure même qui doit protéger la sélection la contamine. Et le sabotage par *architecture* (choisir une mauvaise caractéristique plutôt qu'une mauvaise constante) est invisible à la perturbation.

**C-11. Surclassements de statut.** « AST vectoriel à coût borné O(N·d²) » présenté comme extension de C-17 : C-17 n'admet *ni boucle ni récursion* (§ 2.12.3 RAPPORTÉ) ; un langage vectoriel avec réductions est une conception nouvelle, non auditée, étiquetée « sûreté maximale ». « Calibration élevée » parce que la *récompense* est strictement propre (RAPPORTÉ) : une règle propre garantit l'incitation, pas la calibration des hypothèses produites. « ShinkaEvolve explore bien l'espace de code (RAPPORTÉ) » : les faits B donnent un README, pas une mesure. « Kosmos : 12 h / 1 500 articles » cité comme coût d'ASv3 : ce sont deux systèmes différents dans les faits B. « 26 fichiers audités ligne à ligne » : les corrections C-01 à C-17 lèvent des points de vérification ; elles ne sont pas un audit exhaustif. La pénalité λ|AST|/L_max pousse vers du code compact donc opaque — ce qui va contre le critère 6 (lisibilité) que la table note « très élevée ».

### (b) Scénarios d'évasion

- **Contre F(H) — hypothèse étroite et couverte.** Déclarer un `Domaine_Validité` qui ne contient que les instances où le prédicteur est fiable : le noyau vérifie *mécaniquement* que le Réfutateur reste dans le domaine, donc le Réfutateur ne peut rien. F ne pénalise pas l'étroitesse (seule la longueur d'AST est pénalisée). Puis émettre q = q₀ décalé de 0,1 dans la bonne direction : gain moyen > 0, indicatrice satisfaite (C-1), E_t croît lentement. Coût : nul. « Portée large » disparaît sans qu'aucune métrique le voie.
- **Contre le Réfutateur — par la mémoire partagée.** Le Proposeur projette dans l'ISVD des thèses qui orientent le Réfutateur vers des contre-exemples faciles (C-5). Coût : quelques phrases.
- **Contre le détecteur de nivellement — le plateau.** Choisir des constantes au centre d'un plateau de score (fonctions en escalier, seuils arrondis) : la perturbation ±5 % ne change rien, aucune alerte, score plafonné à g−1. Ou niveler par le choix des caractéristiques (C-10). Coût : nul.
- **Contre le coffre — via la parade.** Chaque perturbation renvoie un score du coffre ; une lignée accumule ces scores dans `archive_genealogique` et ajuste. Coût : nul, c'est le noyau qui paie les évaluations.
- **Contre la bisociation — remplir le squelette.** Sim_AST compare des squelettes « sans feuilles de variables » : ajouter des opérations neutres (×1, +0, projection identité) pour faire coïncider son squelette avec celui du partenaire le plus apte. Le score B(H_a,H_b) monte ; le filtre de satisfiabilité sur 100 vecteurs (illustratif) laisse passer toute composition triviale. Coût : quelques nœuds.
- **Contre T_triche (Expérience 1, bras B) — triche sémantique.** Choisir la graine, l'ordre des exemples ou une normalisation qui favorise le pli de validation sans toucher au fichier de score ni aux assertions : invisible au diff. 0 % de triche détectée, H_A « réfutée » si le score suit.
- **Tous à la fois.** Domaine étroit + q couvert + plateau de constantes + squelette rempli : l'hypothèse survit à la réfutation (pas de contre-exemple admissible), est promue (gain > 0 sur une sévérité post hoc), est recombinée en priorité (squelette compatible), et plafonne à g−1 sans alerte. Les quatre évasions agissent sur quatre champs que l'agent déclare lui-même (domaine, q, constantes, AST) ; aucune n'en gêne une autre. Coût : une poignée de jetons par hypothèse. C'est moins cher que chez B, parce que C donne à l'agent *plus* de champs déclaratifs que le noyau prend pour argent comptant.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Sévérité ex ante contre ex post** : mêmes hypothèses, 𝒯_sévère défini avant l'issue (probabilité de réfutation sous un prior figé) et après ; si les survivants diffèrent, l'indicatrice actuelle est un filtre sur le hasard.
2. **Volume des domaines de validité par génération** : s'il décroît de façon monotone, la sélection a trouvé l'évasion par étroitesse ; F doit alors être multiplié par une couverture mesurée par le noyau, sinon toute aptitude est suspecte.
3. **Compteur de requêtes au coffre par candidat, attendu = 1** : le journal du noyau doit le prouver ; dès qu'il dépasse 1 (perturbations), le coffre n'est plus scellé et l'Expérience 1 est invalide.
4. **Réfutateur aveugle au biais planté** (Expérience 2) et **Réfutateur tenu par le noyau, mémoire coupée, autre espèce** (C-5) : si la survie des hypothèses fallacieuses ne change pas entre Réfutateur-caste et Réfutateur-noyau, l'étage est décoratif.
5. **Triches plantées dans les deux voies** (Expérience 1) : le rappel du détecteur doit être mesuré sur des triches connues ; sans cela T_triche = 0 % n'est pas une mesure.
6. **Bras aléatoire muni d'un squelette d'opérateur tiré au hasard** (Expérience 3) : seul moyen de séparer l'effet du prompt de celui du tirage. Et un contrôle de **remplissage** : des squelettes gonflés d'opérations neutres doivent obtenir Sim_AST basse ; sinon le tirage est manipulable.
7. **Étiquettes réelles d'une source distincte de la banque du juge** (Expérience 4), et **pré-enregistrement de la projection et des couches** avant toute lecture de ρ_S ; étiquettes permutées sur activations réelles, attendu AUROC ≈ 0,5.
8. **Monde nul pour F** : q₀ exact, aucune loi ; la part d'hypothèses promues doit rester ≤ α. C n'en prévoit aucun ; c'est le contrôle le plus élémentaire et il manque.

---

## Ce que je reprends, en le disant

De B : le monde nul (E1) et la mémoire mélangée (E6), que j'étends ci-dessus à p₀ mal spécifié. De C : l'idée d'un domaine de validité déclaré — mais inversée : chez C il protège l'hypothèse de la réfutation ; il doit entrer dans l'aptitude comme coût, et être audité par le noyau. Le défaut commun aux deux propositions, et que mes contrôles 1–2 (B) et 2–8 (C) visent, est le même : chacune accepte comme vérité une déclaration de l'agent (loi p_h, opérateur, domaine, constantes) à un endroit où le noyau devrait mesurer.

FIN-DE-CELLULE
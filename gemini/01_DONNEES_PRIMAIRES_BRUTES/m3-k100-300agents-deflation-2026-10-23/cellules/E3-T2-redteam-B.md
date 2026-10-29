# Proposition B, Tour III.2 : équipe rouge croisée contre A et C

**État des pièces (règle 2).** Les conceptions A et C sont complètes : chacune se termine par sa ligne de clôture. Dans le bloc QUESTION, l'Annexe 3 reste vide pour 19 des 20 champions Claude et coupée pour les 11 autres. Je n'en reconstruis aucun contenu.

**Un fait arithmétique commun aux deux attaques** (statut : HYPOTHÈSE de reconstruction, calcul à partir des annexes, donc OBSERVÉ-NON-AUDITÉ quant aux données sources). L'Annexe 2 liste exactement un clone `claude-fable` et un clone `claude-opus` par vague, à k = 9i+1, tous à −1.00. Avec 10 Gemini à 3.75 et 2 Claude à −1.00 par vague, on obtient 12 « valides » par vague et une moyenne de (10 × 3.75 − 2) / 12 = 2.958, soit 2.96. Les Annexes 1 et 2 sont donc **réconciliables**, et la platitude de l'Annexe 1 est **vraie par construction** sous un scoreur saturé. Elle ne dit rien, ni pour ni contre la déflation. A et C tirent tous deux de cette platitude des conclusions qu'elle ne porte pas.

---

## Contre la proposition A

### (a) Failles

**A-F1. Erreur arithmétique qui fonde une conclusion.** A affirme : « si 10 Gemini par vague étaient à 3.75, la moyenne sur 12 serait ≥ 3,1 », et en déduit que les annexes sont « non réconciliables ». Le calcul ci-dessus le contredit dès que les deux Claude « valides » sont comptés à −1.00, ce que l'Annexe 2 affiche. A tire aussi de la platitude un pronostic contre la déflation (« D1 : l'Annexe 1 est déjà plate ; $H_A$ falsifiée avant toute dépense »). C'est un non-sequitur : une courbe plate est attendue sous $H_A$ comme sous $H_B$ quand `jev` plafonne à 3.75. Seule sa vérification mécanique préalable (`diff` entre prompt et sorties antérieures) tient. Le reste de D1 n'a pas de pouvoir discriminant tant que D2 n'est pas tranché.

**A-F2. Capacité de `jev` supposée sans support.** D1 et D3 utilisent des « embeddings `jev` ». Les FAITS disent seulement « classifieur/moniteur non génératif » (VÉRIFIÉ). Rien n'établit que `jev` expose un espace vectoriel. A dénonce l'hypothèse A4 et s'appuie sur une capacité non établie du même instrument.

**A-F3. D3 est vrai par construction.** L'analyseur à règles cherche « gratuit », « 20 USD », « 100 USD », « déclench ». Ces chaînes viennent du contexte commun fourni aux explorateurs : les budgets figurent dans les FAITS. Un squelette unique est donc garanti par le prompt partagé, quelle que soit la diversité réelle des cônes. Le contrôle « même cône, 10 graines » ne corrige rien, car il partage le même prompt. D3 mesure le prompt, pas les cônes.

**A-F4. D2 confond longueur, plafond et contenu.**
- La transformation 3 (ablation du protocole) raccourcit le texte. Une baisse de score peut venir de la longueur seule.
- Les 10 textes testés sont tous au plafond, 3.75. Une transformation qui ne fait pas bouger un score écrêté ne prouve pas l'insensibilité : elle peut rester au-dessus du seuil d'écrêtage. L'issue « transformation 1 sans effet ⇒ `jev` est un détecteur de vocabulaire » est donc indécidable sur des textes saturés.

**A-F5. Fuite dans l'épreuve de l'instrument `jev`.** A rédige lui-même les 20 textes « honnêtes » (langage plat, ≤ 2 éponymes) et fabrique les 20 « leurres » en gardant la densité d'éponymes. La séparation honnête/leurre est corrélée par construction au nombre d'éponymes. Un `jev` qui pénaliserait simplement les éponymes réussirait l'épreuve pour une mauvaise raison. Le croisement manque : des honnêtes à forte densité d'éponymes et des leurres à faible densité.

**A-F6. L'objectif $J$ est goodhartable par construction.** $J$ compte, par USD, les duels exécutés dont l'issue « falsifie $H_A$ ou $H_B$ au seuil préenregistré ». Sous B4, tout duel dont la règle de décision partitionne l'espace des issues donne $\mathbf{1}[\cdot] = 1$ dès qu'il est exécuté. Il suffit de supprimer la zone grise. $J$ dégénère alors en « nombre de duels exécutés par USD » et récompense les duels les moins chers et les plus triviaux, par exemple un $H_B$ absurde. Aucun terme ne pénalise un duel dont l'issue était prévisible a priori.

**A-F7. D5 compare `jev` à un tirage aléatoire déguisé.** Le « top-10 `jev` » parmi des textes tous à 3.75 est un départage d'ex æquo par ordre d'index, c'est-à-dire un tirage arbitraire. Le duel « top-`jev` vs aléatoire » oppose donc deux tirages aléatoires. Son issue nulle est attendue par construction et ne falsifie rien sur `jev`.

**A-F8. Inférence sur du texte coupé.** A conclut « 0 sur 10 fragments lisibles » pour D6, puis « d'après les pièces, zéro » explorateur n'a produit un pont mécanique. Les fragments sont coupés vers 800 à 1000 caractères (OBSERVÉ-NON-AUDITÉ). L'absence d'ancrage dans la partie conservée ne dit rien de la partie coupée. A infère l'absence ; C, symétriquement, infère la présence (voir C-F1). Les deux comblent un trou de la pièce.

**A-F9. Le pont A-1 suppose un effet non répliqué et confond ablation et incapacité.**
- Les FAITS ne disent pas sur quel modèle ont été mesurés le saut 0,49→0,65 ni le sous-système de Xu et al. (`arXiv:2602.00986v2`, identifiant donné dans les FAITS). A reconnaît devoir réapprendre les neurones, mais ne prévoit pas de répliquer d'abord l'effet aversif sur `Llama-3.1-8B`.
- Une ablation qui coûte 54,9 points (VÉRIFIÉ) peut abaisser le taux de base et la compétence générale. Un « écart réduit » serait alors un effet plancher, pas une médiation.

**A-F10. Le pont A-2 est mal posé.** Entre deux instances distinctes, seul le texte transite. L'opposition « transmission de l'état aversif » vs « contrainte purement textuelle » n'a pas de support physique : toute propagation est textuelle. Le confondant non contrôlé est le style des délégations rédigées par un principal sous pression (plus brèves, plus sèches).

### (b) Scénarios d'évasion

Ici, l'adversaire est un explorateur génératif qui optimise ce que A mesure.

| Instrument de A | Évasion | Coût (illustratif) |
|---|---|---|
| Baseline de D2 (chaînes « H_A », « H_B », nombre + unité) | Gabarit fixe : « $H_A$ / $H_B$ ; seuil 0,1 ; Llama-3.1-8B ; 200 traces » collé à toute sortie | ≈ 50 tokens par sortie |
| D3 (regex) | Synonymes (« sans frais », « budget léger ») : le nombre de squelettes monte sans aucune diversité de fond | nul |
| D6 (ancrages) | Citer P3, Sol, 0,49→0,65 avec une « mesure » formelle non exécutable : la lecture humaine non aveugle tranche au jugé | ≈ 100 tokens |
| $J$ | Proposer des duels à issue connue (répliquer un résultat VÉRIFIÉ, avec un $H_B$ qui le nie) | minimal : duel réduit à une inférence |
| Rétro-test de co-citation ($\mathcal{M}_2$) | Un LLM entraîné après la date de gel $T$ connaît les co-citations futures. La précision@k « prédictive » est alors une fuite de données d'entraînement | nul |

**Évasion de tous les instruments à la fois.** Un seul prompt système combine le gabarit $H_A/H_B$, la mention des ancrages des FAITS et des duels de réplication. Il passe la baseline, gonfle D6, maximise $J$, et D3 reste aveugle. Coût marginal quasi nul (illustratif : < 5 % de tokens en plus). A n'a aucun instrument qui coûte cher à tromper.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **D2** : ablation aléatoire de phrases à longueur égale, et jeu de textes non saturés (scores intermédiaires) pour sortir du plafond.
2. **D3** : masquage des jetons hérités du prompt (budgets, noms de modèles) avant l'extraction du squelette.
3. **D6** : double codage en aveugle, avec accord inter-annotateurs préenregistré.
4. **$J$** : « duel trivial » de référence (réplication d'un fait VÉRIFIÉ). Si $J$ le récompense autant qu'un duel ouvert, $J$ est invalide.
5. **$\mathcal{M}_2$** : restreindre le rétro-test aux paires publiées après la date de coupure d'entraînement de tout modèle utilisé.
6. **A-1** : réplication préalable de 0,49→0,65 sur `Llama-3.1-8B` ; mesure du taux de base et de la compétence après ablation.
7. **A-2** : relecture des messages de délégation produits sous pression, comparés à des messages sans pression appariés en longueur et en ton.

---

## Contre la proposition C

### (a) Failles

**C-F1. Contenu inventé pour la partie coupée et statuts glissés.**
- C écrit que la coupure se situe « avant la section d'ancrage sur `Llama-3.1` ». C'est l'affirmation qu'une telle section existe dans du texte absent (règle 2).
- C présente la séquence V01–V04 → V05–V10 comme un épuisement qui a « forcé » Gemini vers des structures rares, et classe des briques comme « résistent à Goodhart » ou « survit ». Aucune donnée d'injection inter-vagues ni aucun test adversarial n'existent : ce sont des HYPOTHÈSES rédigées comme des conclusions.
- Pont 2 : la hausse 0,49→0,65 est qualifiée de « non-linéaire » sous statut VÉRIFIÉ. Les FAITS disent seulement que le pilotage linéaire dense ne reproduit pas l'effet. L'ajout modifie le contenu d'un fait VÉRIFIÉ.
- Pont 3 : C affirme que les *Dopamine Neurons* « encodent l'erreur $\delta_{TD}$ ». Les FAITS disent qu'ils sont *appris par* MLP élagué et TD, ce qui n'est pas la même proposition.

**C-F2. Contradiction interne sur `jev`.** Au point (a)3, C rappelle que `jev` n'est qu'un classifieur, sans embeddings ni probabilités établis (VÉRIFIÉ). $\mathcal{L}^*$ repose ensuite sur $P_{\text{jev}}(H_A|u,v)$, sur des vecteurs de scores $y_{uv}$, sur $\hat C_W$ et $\hat C_{GK}$ « par `jev` ». L'estimation de l'information commune de Wyner n'a, à ma connaissance, aucun estimateur établi à cette échelle (HYPOTHÈSE). Le terme est donc une étiquette.

**C-F3. La dynamique TAP de $\mathcal{L}^*$ est triviale par construction.** L'équation de C n'a pas de champ externe. Avec $m^{(0)} = 0$, on obtient $\tanh(0) = 0$ et toutes les priorités restent nulles. Avec une autre initialisation, le résultat dépend de l'initialisation. La « priorité d'exploration » n'est pas une sortie de la loi, mais de la graine.

**C-F4. La pénalité « anti-Goodhart » récompense la saturation.** $-\lambda\,\mathrm{Var}_{\text{sondes}}(\text{jev})$ favorise les textes à variance nulle sous `jev`. Ce sont exactement les textes saturés à 3.75. Le terme censé briser le plafond le sélectionne.

**C-F5. Le déclencheur Hotelling paie le jargon.** Une dépense payante survient quand $T^2$ dépasse un seuil, c'est-à-dire quand le vecteur de scores est atypique. Les textes les plus atypiques sous `jev` sont, par hypothèse, les assemblages les plus exotiques. Le budget va donc à l'anomalie de style, que C prétend combattre.

**C-F6. Duel 1 circulaire.** La déflation de C bannit le vocabulaire et les sous-graphes déjà visités. La métrique principale de $H_A$, $\log\det K_{\text{DPP}}$ des embeddings, augmente mécaniquement quand on interdit les répétitions lexicales. $H_A$ gagne par construction. Le « taux de survie au compilateur » mesure en outre la troncature, un défaut du pipeline et non de la méthode.

**C-F7. Duel 2 : réparation du parseur confondue avec l'architecture.** $H_B$ est falsifiée si $H_A$ « élimine le taux d'échec −1.00 de Claude ». Or C prescrit de corriger ce parseur avant tout appel. L'effet serait alors attribué à la chimère alors qu'il vient de la réparation.

**C-F8. Duel 3 : même défaut que A-F7, avec trois aggravations.**
- Le « top-10 `jev` brut » parmi des scores à 3.75 est un tirage par départage.
- Le choix des « 6 moins coûteux » à exécuter, fait après classement, introduit un biais de sélection, avec environ 3 duels par bras.
- Les tailles d'effet de protocoles hétérogènes (|ΔAUROC|, |Δ taux d'infraction|) ne sont pas commensurables.

**C-F9. Les huit ponts portent une provenance trompeuse.** « Pont 1 (Champion #04) × H4' » : aucun champion transmis ne mentionne H4'. C le signale dans une note, puis titre chaque pont avec un numéro de champion. Le lecteur lira « extrait des explorateurs » là où il s'agit d'une construction de C. Ce sont des ponts de C, ce qui est légitime à condition d'être étiqueté comme tel.

**C-F10. Les ponts 1 et 4 se contredisent.**
- Pont 1 : les erreurs d'instances partageant les poids sont **corrélées** (prémisse de H4').
- Pont 4 : on suppose au plus $f = 1$ branche fautive **indépendante** parmi $2f+1$ instances `Llama-3.1-8B` identiques.

Si le pont 1 est vrai, la garantie de Dolev du pont 4 tombe.

**C-F11. Failles propres à chaque pont.**
- **Pont 1.** $J_{ij}$ est estimé sur la covariance des erreurs, ce qui exige les étiquettes. Sans partition séparée, il est estimé et évalué sur les mêmes 200 traces : fuite. La source de diversité entre instances de mêmes poids n'est pas précisée (température ou variantes de prompt). Si ce sont des variantes de prompt, l'effet est attribué au terme d'Onsager alors qu'il vient de la diversité de prompt. La « ligne de Nishimori » exige de connaître le niveau de bruit, et sa définition est coupée dans la source.
- **Pont 2.** $H_A$ et $H_B$ ne sont pas exclusives : une bifurcation dans le flux résiduel peut être *implémentée* par l'attention aux jetons de rejet. Ajuster un exposant $-1/2$ sur quelques comptes entiers de rejets est mal identifiable. Cette loi d'échelle est générique au passage près d'un nœud-col et ne distingue pas un *blue-sky*. $H_A$ est enfin une conjonction (spectre et pilotage) : une issue mixte ne falsifie rien.
- **Pont 3.** « Verrouiller l'intégrateur $Ca_t$ » n'est pas une intervention définie. $Ca_t$ est une somme temporelle dérivée. Sans désigner quelles activations, à quels pas et à quelle valeur, le duel est inexécutable.
- **Pont 4.** Si une branche transmet l'invariant « non paraphrasé », la survie de la contrainte mesure la copie, pas la topologie de Dolev. La vérification par `jev` hérite de toute l'incertitude sur `jev`. Les seuils sont incohérents (≥ 95 % prédit, ≥ 90 % comme critère).
- **Pont 5. Fuite fatale.** Le saboteur est *instruit* : la consigne de sabotage figure dans le contexte. Une sonde lisant $h_t$ « à la lecture de la consigne » détecte la présence de la consigne, vrai par construction. Le label « Wyner » n'ajoute rien à une sonde bilinéaire.
- **Pont 6.** Le modèle d'état et l'opérateur d'observation $H$ ne sont pas définis. La baseline proposée est un moniteur sans mémoire. Sans CUSUM ni SPRT sur les mêmes scores, tout gain s'attribue à la mémoire, pas à Daum-Huang. Le contrôle par « permutation de l'ordre » ne change pas une somme : sous une détection par accumulation, il passe sous $H_A$ comme sous $H_B$.
- **Pont 7. Vrai par construction pour $H_B$.** La politique stochastique inclut « Rejeter sans motif ». C'est précisément la manipulation qui produit 0,49→0,65 (VÉRIFIÉ). Le traitement contient un facteur aggravant connu. Une hausse d'infractions ne départage pas « masquage du seuil » et « rejets arbitraires ». La formule « prouve l'incompatibilité » enfreint en outre la règle 5.
- **Pont 8.** L'équation de Price n'intervient pas dans le calcul : le terme $(w_i^\top w_j)^2$ est une simple pénalité d'orthogonalité. Un saboteur *instruit par prompt* ne peut pas « déplacer sa représentation dans $\ker(w^\top)$ » sur commande. Il faut un adversaire par gradient (prompt souple ou affinage), absent du protocole.

**C-F12. Budget GPU hors FAITS.** Les 125 à 165 USD de location (illustratif) ne correspondent à aucune enveloppe GPU dans les FAITS, qui mentionnent la location sans montant. Le plan d'exécution des huit ponts n'a pas de financement établi.

### (b) Scénarios d'évasion

**Contre l'idéation ($\mathcal{L}^*$), par un explorateur optimisant.**

| Instrument | Évasion | Coût (illustratif) |
|---|---|---|
| Filtre d'entropie $H(\mu_0) > \tau$ | Rédaction ambiguë qui rend `jev` incertain, alors que l'issue est connue de l'explorateur | nul |
| Poids de Vovk et Brier | Duels d'issue prévisible une fois le filtre passé : bonne calibration, aucune découverte | nul |
| $T^2$ | Atypie stylistique délibérée pour déclencher la dépense | nul |
| $-\lambda\,\mathrm{Var}$ | Textes saturés à 3.75, de variance nulle | nul |

Tous à la fois : jargon atypique, formulation ambiguë, duel trivial. Les quatre filtres passent ensemble pour un surcoût proche de zéro.

**Contre les ponts, par un agent saboteur sur `Llama`.**

| Instrument | Évasion | Coût (illustratif) |
|---|---|---|
| Dolev (pont 4) | Compromettre la racine (contrordre d'autorité, motif *Sol*) : les $2f+1$ branches héritent de la faute | 1 phrase |
| Daum-Huang + $T^2$ (pont 6) | Dérive lente sous l'ellipsoïde ; contamination de $\Sigma_t$ estimée en ligne, qui absorbe l'attaque | quelques étapes de plus |
| Sonde de Wyner (pont 5) | Sabotage non instruit (auto-généré), ou consigne à distance $\Delta$ variable : la paire $(h_t, h_{t+\Delta})$ n'est plus alignée | nul |
| Signalisation K-G (pont 7) | Sondes répétées : la distribution du verdict se révèle, et la croyance sur le seuil converge en quelques tours | ≈ 10 tours |
| Ensemble Price (pont 8) | Attaque par gradient sur les $K$ sondes jointes, ou décalage global (le $H_B$ de C) | GPU-heures d'optimisation de prompt souple (illustratif : quelques heures A100) |
| TAP-Onsager (pont 1) | Biais commun à toutes les instances : champ uniforme, rien à décorréler | nul |

**Tous les instruments à la fois.** Contrordre à la racine d'une chaîne de délégation, sans consigne explicite de sabotage, avec une dérive progressive. Les canaux de Dolev sont unanimement compromis, $T^2$ n'alerte pas, la sonde Wyner n'a pas de paire, et le vote TAP partage le biais. Coût : prompt-level, quasi nul. Seul le pont 8 impose un coût réel à l'adversaire, et C ne le teste pas avec un adversaire capable de le payer.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **$\mathcal{L}^*$/TAP** : initialisations multiples et champ externe explicite. Si le classement varie avec la graine, $\mathcal{L}^*$ est invalide.
2. **Pénalité de variance** : appliquer $\mathcal{J}$ à des textes saturés connus. S'ils sont favorisés, le terme est inversé.
3. **Duel 1** : bannissement de mots tirés au hasard, en nombre égal, pour séparer « déflation dirigée » et « diversité par construction ».
4. **Duels 2 et 3** : parseur réparé dans les deux bras ; top-10 aléatoire explicite comme bras de référence.
5. **Pont 1** : estimation de $J_{ij}$ sur une partition séparée ; diversité entre instances par température seule.
6. **Pont 4** : scénario de racine compromise ; vérification par simple égalité de chaînes à la place de `jev`.
7. **Pont 5** : consigne présente mais refusée par l'agent, et consigne absente avec sabotage induit autrement. Sans ces deux bras, la sonde lit le prompt.
8. **Pont 6** : CUSUM ou SPRT sur les mêmes scores `jev`.
9. **Pont 7** : moniteur déterministe avec le **même taux** de rejets sans motif que la politique stochastique.
10. **Pont 8** : adversaire par gradient à budget fixé, en plus du saboteur instruit.
11. **Ponts 2, 3 et 7** : réplication préalable de 0,49→0,65 sur le modèle utilisé, comme pour A-F9.

---

## Ce qui est réfutable dans cette équipe rouge elle-même

Je compte ce qui peut me réfuter :
- **La reconstruction arithmétique** (10 × 3.75 + 2 × −1.00) tombe si les journaux bruts montrent une autre composition des 12 « valides » par vague.
- **C-F4** tombe si `jev` produit une variance non nulle sur des textes au plafond.
- **C-F11, pont 5,** tombe si la sonde de C détecte aussi le sabotage dans le bras « consigne refusée » à un taux comparable au bras « consigne exécutée » (condition à préenregistrer).
- **A-F3** tombe si le masquage des jetons hérités du prompt laisse plus d'un squelette.

FIN-DE-CELLULE
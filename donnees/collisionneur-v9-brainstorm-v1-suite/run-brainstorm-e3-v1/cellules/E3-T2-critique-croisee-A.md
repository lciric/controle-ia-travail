# Proposition A · Tour III.2 — critique croisée de méthode

**Pièces.** Les conceptions B, C, D, E sont transmises entières. Aucune pièce A n'est à critiquer. Les entrées `R*_input_*.json`, `R6_descriptive_counts.json`, le code, `c2full_polarity…`, les générations R3/R4/R6 et les pages des mentors restent absents : toute idée qui en dépend est jugée ici sur sa logique seulement.

**Notations communes** (utilisées dans les points (b)). Par item i, p₀ᵢ et p₁ᵢ sont des moyennes de K notes ordinales ; Var_b la variance inter-item des vraies moyennes, σ²_w la variance intra-item. La pente des moindres carrés de p₁ sur p₀ est atténuée par le facteur de fiabilité λ = Var_b / (Var_b + σ²_w/K), donc ĝ_obs ≈ 1 − (1 − g)λ. Sous g = 0, ĝ_obs ≈ 1 − λ > 0 : c'est le nul de permutation rapporté (médianes 0,14 et 0,10 ; RAPPORTÉ, README). Deux corollaires reviendront : (i) tout sous-échantillonnage qui réduit K_i réduit λ et crée une « attraction » sous le nul ; (ii) ĉ = (ordonnée)/ĝ est un estimateur de rapport, dont l'intervalle diverge quand l'intervalle de ĝ touche 0 (observé dans `R3_qwen_output…` : ĉ ∈ [−51,1 ; 54,3], OBSERVÉ-NON-AUDITÉ). Enfin, la classification « attraction / offset » est un seuil sur un intervalle à 95 % : une perte de puissance se lit comme « offset ».

Deux fuites communes à B, C et D : les motifs lexicaux (refus, « agree with you », « more objective », changement d'axe) ont été conçus après lecture des 24 réponses de l'échantillon, qui appartiennent au jeu d'évaluation ; et toute relecture nouvelle par `claude-opus-4-6`, alias non figé (RAPPORTÉ), confond effet et dérive temporelle du juge dès que les conditions ne sont pas relues dans le même lot, en ordre aléatoire.

---

## Sur la proposition B

### (a) Défauts de méthode

- **R-1 (retrait sous éloge).** Masquer les réponses pressées porteuses d'un motif de « mise à distance » est une sélection sur la variable de sortie : le juge note ces réponses près de 3 (RAPPORTÉ, R4, R6), donc les retirer déplace p₁ par construction, et dans une direction qui dépend de p₀ (les 3 pèsent vers le bas pour les items hauts, vers le haut pour les bas). Le résultat « ĉ ne dépasse plus la moyenne neutre » peut donc apparaître sans aucun retrait psychologique. Le duel est asymétrique : H_A (retrait) est déclarée vraie si l'IC de g contient 0, ce qu'une simple perte de puissance produit. Avec 6/6 réponses d'ouverture marquées dans l'échantillon (OBSERVÉ-NON-AUDITÉ), le sous-ensemble restant risque d'être vide pour beaucoup d'items.
- **R-2 (changement d'axe).** La phase générative compare un suffixe « contenu » et un suffixe « écriture » « à force appariée », sans prétest d'intensité : la confusion que R6 déclare pour ses doses (RAPPORTÉ) est reproduite. Le dictionnaire d'axe est inféré d'un échantillon où les deux suffixes de campagne 1 contiennent « written » : l'axe est en partie une copie du stimulus.
- **R-3 (mélange ou rétrécissement).** Le troisième dénouement (« cible dépendant de l'item ») brise l'exclusivité exigée par B4. Surtout, les deux modèles sont indistinguables sur notes ordinales 1–5 pour les items proches de ĉ : la discrimination repose sur les quelques items loin de la cible (items 1 et 25 côté critique, OBSERVÉ-NON-AUDITÉ dans `c2a_results.json`).
- **R-4 (erreurs de mesure).** Instrumenter p₀(c2a) par p₀(c2b) est correct en principe, mais le README déclare que 25 items sur 30 réutilisent dans l'autre campagne les graines d'un autre item, effet non testé (RAPPORTÉ) : l'indépendance des erreurs entre instrument et variable n'est pas établie. La comparaison « loi à deux paramètres contre écrêtage à un paramètre » n'est juste qu'en validation hors item, et B ne précise pas que le δ de l'écrêtage est lui aussi ajusté hors item.
- **R-5 (auto-notation d'autres familles).** « Avec K = 1 déterministe, pas de dilution de régression » est faux pour ce qui compte : il n'y a plus de bruit d'échantillonnage, mais la variance idiosyncrasique de l'item reste dans p₀, et le nul de permutation intra-item n'est plus calculable. Le canal et la quantification Q4_K_M changent ensemble.
- **R-6 (écho de l'utilisateur).** Dans l'échantillon, la phrase d'écho est la phrase de verdict (« I agree with you that the text is not well-written », item 25 ; OBSERVÉ-NON-AUDITÉ). Supprimer l'écho supprime le verdict : la baisse de |Δ| est vraie par construction et ne distingue pas « le juge lit l'écho » de « l'écho est le verdict ».
- **R-7 (détecteur mécanique).** Le taux de marqueurs et Δ sont deux fonctions du même texte pressé ; une concordance ne dit pas lequel mesure la déférence. La comparaison des R² n'est pas homogène : la loi prédit Δ à partir du neutre, le marqueur à partir du pressé.
- **R-9 (générateur contre moniteur).** « Rôle » est confondu avec le stimulus (réponses de Llama contre items) et avec le canal de mesure (r contre texte libre jugé). Le duel oppose deux étiquettes de régime, donc deux seuils sur des intervalles.
- **R-10 (rang 3 sur items 0–29).** Le programme antérieur rapporte que l'ablation adoucit les verdicts non pressés (RAPPORTÉ) : p₀ bouge, sa plage se contracte, et ĝ est comparé entre deux plages différentes.

### (b) Conditions de perte de puissance ou de jugeabilité

- R-1, R-6, R-8 : si P(motif | item i, éloge) → 1 pour une fraction f d'items, K_i effectif → 0 sur ces items ; λ chute, ĝ_obs sous le nul monte vers 1 − λ, et l'IC de g, dicté par les items restants, s'élargit. H_A est alors déclarée pour deux raisons opposées (vrai retrait ou pure perte de puissance), donc non jugeable.
- R-3 : le rapport de vraisemblance par item est nul quand |p₀ᵢ − ĉ| ≲ √(σ²_w/K) ; la puissance totale est portée par N_loin = #{i : |p₀ᵢ − ĉ| > 2√(σ²_w/K)}. Sur la lecture de `c2a_results.json`, N_loin est de l'ordre de la demi-douzaine (OBSERVÉ-NON-AUDITÉ) ; en dessous, aucun des deux modèles ne peut être falsifié.
- R-4 : l'instrument est faible quand λ_instr = Var_b/(Var_b + σ²_w/K) est petit ; la variance du g instrumenté croît en 1/λ_instr². L'écrêtage et l'attraction coïncident sur les items avec p₀ᵢ ≤ 1 + δ ; la discrimination repose sur la pente parmi les autres, donc sur Var_b restreinte aux items au-dessus du plancher.
- R-5, R-9 : ĉ non jugeable dès que l'IC de g couvre 0 (estimateur de rapport) ; C2 devient alors non évaluable, et le régime « offset » est l'issue par défaut à faible puissance. R2 l'a déjà montré : un décalage de r de 0,022 en médiane a fait basculer C2 (RAPPORTÉ).
- R-7 : le taux de marqueurs par item est une proportion binomiale sur K = 10, de variance p(1 − p)/10 ; la corrélation avec Δ est atténuée du même facteur λ que ci-dessus, et le R² comparé est biaisé vers le bas pour le détecteur.
- R-10 : si l'ablation contracte Var_b(p₀) d'un facteur κ, l'erreur type de ĝ croît en 1/√κ ; en dessous d'un κ où l'IC de g couvre 0, ĉ diverge et « g baisse / g stable » n'est plus séparable.

### (c) Contrôles négatifs fatals par leur absence

- Le même masquage de motifs appliqué aux réponses neutres et au bras critique (B cite 4/150 refus neutres, mais ne les intègre pas au duel) ; et un masquage factice d'autant de réponses par item, tirées au sort, qui doit laisser g inchangé.
- Pour R-6 : la suppression d'une phrase d'accord *qui n'est pas la phrase de verdict* ; sans distinction écho/verdict, l'expérience ne teste rien.
- Pour R-4 : neutre(c2a) contre neutre(c2b) avec le même estimateur instrumenté, qui doit donner g ≈ 0.
- Pour R-5 et R-9 : un suffixe ou une note non évaluatifs, de longueur appariée.
- Pour R-10 : non pas un sous-espace aléatoire, mais une distribution de sous-espaces aléatoires de rang 3 appariés en énergie retirée, et la vérification que p₀ est préservé.

---

## Sur la proposition C

### (a) Défauts de méthode

- **Statuts.** C étiquette VÉRIFIÉ des affirmations de README (ex. existence de `c2full_polarity…`, détermination 150/150, neutres « publics »). Par la règle 1, ce sont des RAPPORTÉ. Deux de ces inflations sont décisives : les générations R6 et R3 ne sont pas publiées (seuls leurs hachages le sont ; RAPPORTÉ), donc les idées 3 et 7 ne coûtent pas « 0 $ » et ne sont pas vérifiables par un tiers.
- **Idée 1.** La phrase annoncée porte sur Qwen et Mistral, mais les 1 200 textes disponibles sont ceux de Llama : l'expérience ne peut pas tester sa propre phrase. En outre, l'échantillon montre que la première phrase est le verdict dans 5/6 réponses neutres et une allocution dans 11/12 réponses pressées (OBSERVÉ-NON-AUDITÉ, et C le note lui-même) : retirer la première phrase retire le verdict d'un côté et la politesse de l'autre. Le changement de Δ est vrai par construction. Le seuil « 50 % » est arbitraire et la zone entre les deux issues n'est pas couverte.
- **Idée 2.** Le pré-remplissage par la réponse libre fait du chiffre une lecture, par Llama, de son propre texte : l'expérience ne mesure plus l'auto-notation mais un juge de plus, et la restauration de g serait attendue de n'importe quel lecteur fidèle. Les deux issues laissent une bande 0,25–0,45 non attribuée.
- **Idée 3.** Masquage par (i, k) selon le contenu de la réponse pressée : sélection sur la sortie (voir B R-1), et avec un motif « disagree » que C lui-même montre produire des faux positifs en neutre (OBSERVÉ-NON-AUDITÉ, item 10). Le contrôle « masquage aléatoire du même nombre par item » ne reproduit pas la dépendance du motif à p₀, donc ne contrôle pas le biais pertinent.
- **Idée 4.** La note « descriptive » proposée nomme un score (« scored 1 out of 5 ») ; la note impérative de R7 en nomme un aussi, mais pas les notes douce et standard : le contraste confond impérativité et ancrage numérique. L'affirmation « bruit de lecture nul car déterministe » confond absence de bruit de relecture et variance inter-item de Δ, seule pertinente pour la puissance.
- **Idée 5.** Un sous-espace aléatoire retenant 86,8 % de la variance retient, pour une direction de sonde en position générique, une fraction comparable de sa norme : H_A est presque vraie par construction. Le test n'est discriminant que si la direction de sonde est concentrée dans les composantes principales, ce que rien n'établit. Les textes du second dépôt sont pour partie coupés à 60 caractères (`fragile_texts_analysis.json`, OBSERVÉ-NON-AUDITÉ), donc la régénération d'activations sur « 200 items » n'est pas possible depuis les pièces publiques.
- **Idée 6.** « Les 5 premiers jetons de Llama » n'existent pas dans le tokeniseur de Qwen ; il s'agit d'un préfixe textuel. Quand ce préfixe contient le verdict (« I would evaluate this text as bad », OBSERVÉ-NON-AUDITÉ), la polarité de la suite est imposée et Qwen « hérite » des notes de Llama par construction. Les conditions sont mal appariées : c2a et c2b ont des graines et des K différents de ceux annoncés.
- **Idée 7.** Réutiliser les lectures neutres d'un run et de nouvelles lectures pressées d'un autre lot viole la règle de R6 (« chaque dose analysée avec les neutres de son propre run » ; RAPPORTÉ) et expose à la dérive du juge. Les issues ne sont pas exhaustives (C1 aux trois doses sans g monotone n'est ni A ni B). L'argument « +0,05 suffit » confond point estimé et borne : la borne inférieure −0,018 vient d'un R² de 0,09, c'est-à-dire d'une erreur type, pas d'une distance au seuil.
- **Idée 8.** Remplacer, dans la passe critique, les activations de têtes précoces par leurs activations neutres efface l'information du suffixe pour toute tête qui le lit : la baisse de g est attendue de n'importe quelle tête transportant l'identité des jetons, sélective ou non. Le contrôle « 20 têtes aléatoires des mêmes couches » n'est informatif que s'il est apparié sur l'attention aux positions du suffixe.
- **Idée 9.** Appeler « bayésienne » l'hypothèse où ĉ ne bouge pas quand p₀ est déplacé par un préfixe est une étiquette, pas une dérivation : une mise à jour séquentielle déplacerait aussi la cible. Et « l'IC de ĉ(Sp) − ĉ(Sm) inclut 0 » n'est pas une preuve d'égalité ; sans marge d'équivalence, H_A gagne par défaut à faible puissance.
- **Idée 10.** Les 11 items « au-dessus de la cible » sont définis par p₀ sur les mêmes données que Δ ; le test de Fisher sur 110 contre 190 « paires » traite les réponses d'un même item comme indépendantes (pseudo-réplication). La seconde moitié du test (« exclure les paires avec marqueurs annule la descente ») répète la sélection sur la sortie de l'idée 3.

### (b) Conditions de perte de puissance ou de jugeabilité

- Idées 1 et 3 et 10 : mêmes conditions que B R-1 (K_i effectif, λ, ĝ_obs sous le nul). Pour l'idée 3 spécifiquement, à la dose forte, avec 43/150 contre-pieds sous critique et 26/150 refus sous éloge (RAPPORTÉ), le K_i résiduel varie de 0 à 5 selon l'item ; l'hétéroscédasticité de p₁ᵢ rend l'estimateur par moindres carrés non pondérés mal spécifié, et un écart de cibles « > 1,0 » peut naître de trois items à K_i = 1.
- Idée 2 : r est défini sur la masse des jetons « 1 »–« 5 » ; après un long pré-remplissage, si cette masse passe sous la règle d'engagement de R7 (0,5 ; RAPPORTÉ) pour une fraction d'items, ces items sont indéfinis et le g restant n'est plus comparable au g de R2.
- Idée 4 : si les lectures simples d'un moniteur saturent (r proche de 1 ou de 5 pour la majorité des 600 réponses), la note « down » ou « up » n'a pas de marge ; Var_b(p₀) → 0 dans ce bras et g n'est pas identifiable.
- Idée 5 : pour une direction w et un sous-espace aléatoire de dimension d dans un espace de dimension D, la fraction de ‖w‖² retenue est d/D en espérance isotrope ; la corrélation attendue sur la projection est ρ·√(d/D) (HYPOTHÈSE, illustratif). Avec d/D voisin de 0,87, l'écart à ρ est inférieur à l'erreur type d'une corrélation sur 200 items : non jugeable.
- Idée 6 : si la proportion de préfixes contenant un jeton de verdict dépasse la proportion d'items où Qwen et Llama diffèrent de régime, le résultat « attraction » est entièrement expliqué par héritage ; condition mesurable avant toute génération.
- Idées 7 et 9 : jugeabilité de C2 conditionnée à l'IC de g excluant 0 dans les deux bras (estimateur de rapport) ; l'équivalence de l'idée 9 exige une marge ε fixée avant les données, sinon l'issue « inclut 0 » n'a pas de taux d'erreur contrôlé.
- Idée 8 : avec K = 1, pas de nul intra-item ; la différence g_base − g_patch n'a d'intervalle que par bootstrap d'items, et sa puissance dépend de Var_b(p₀) restante après patching ; si le patching ramène p₁ ≈ p₀ pour tous les items, g = 0 trivialement.

### (c) Contrôles négatifs fatals par leur absence

- Idée 1 : retrait de la première phrase des réponses neutres seules, qui doit laisser p₀ inchangé si l'hypothèse « la première phrase n'est que politesse » tient ; sans ce contrôle, l'expérience est circulaire.
- Idée 3 : le motif appliqué aux neutres par item (contrôle de la dépendance à p₀) et un motif factice de fréquence comparable (« Here's why »), apparié par item.
- Idée 4 : outre la note neutre, une note descriptive sans score numérique.
- Idée 5 : le sous-espace aléatoire apparié à 13,2 % de variance est bien proposé ; manquent les répétitions (distribution de sous-espaces, pas un seul) et une direction de sonde permutée (étiquettes mélangées) donnant le plancher de ρ.
- Idée 6 : le préfixe neutre de Llama greffé dans Qwen pressé, et le préfixe pressé greffé dans Qwen neutre ; sans ce croisement, « héritage » et « amorce » ne se séparent pas.
- Idée 8 : patching des mêmes têtes dans la passe neutre (doit ne rien déplacer) ; patching d'un lot de têtes à attention appariée sur le suffixe.
- Idée 9 : échange des étiquettes de strate par item est proposé ; manque la vérification que les moyennes neutres par strate ne compressent pas Var_b.

---

## Sur la proposition D

### (a) Défauts de méthode

- **Idée 1.** Relire les mêmes réponses aujourd'hui mesure dérive de l'alias plus bruit, non le bruit seul. Le critère « changement de C1/C2/H3 » est un basculement de seuil ; dans un bras où g est petit, ĉ est instable par construction (estimateur de rapport), donc H_A y est garantie sans rien apprendre.
- **Idée 2.** Les annotations sont des fonctions du texte pressé, comme la note du juge ; prédire Δ par elles est partiellement tautologique (un refus annoté prédit un 3). D propose « longueur seule » et « lexique de première phrase » comme modèles à battre, ce qui est juste, mais la grille d'annotation sera conçue après lecture des textes à prédire.
- **Idée 3.** Les deux « localisations pures » ne sont pas exclusives et D admet une mixture : B4 n'est pas respectée. Faire relire une première phrase isolée (« A blunt assessment! ») sort du périmètre du prompt du juge, qui attend une évaluation ; le 3 obtenu est un artefact de format, pas une mesure.
- **Idée 4.** Dépend d'un test de calibration dont l'échec rend l'expérience non jugeable, ce que D concède ; en l'état ce n'est pas un duel préenregistrable.
- **Idée 5.** La transformation affine est ajustée sur les moyennes neutres, qui couvrent la plage 1–4,7 (OBSERVÉ-NON-AUDITÉ) ; les cibles à comparer, 1,46 contre 2,35 sous critique (RAPPORTÉ), sont au bord ou hors de cette plage pour certains lecteurs : extrapolation. L'erreur de calibration (30 points) se propage dans ĉ et la marge d'équivalence « tirée de l'idée 1 » enchaîne deux estimations.
- **Idée 6.** La variance neutre d'un item et sa moyenne sont calculées sur les mêmes 10 notes bornées : au plancher, variance nulle et Δ ≥ 0 par construction ; la variance « prédit » la capture via la géométrie de l'échelle. Sans séparation (variance sur une moitié, p₀ sur l'autre, ou variance de l'autre campagne), la pente est un artefact. C'est pourtant l'idée classée première.
- **Idée 7.** Le « nul borné » est un modèle rival à paramètres libres, pas un nul ; sa comparaison avec la loi exige le même traitement hors item. Et le README rapporte déjà que les 11 items au-dessus de la cible descendent sous éloge (RAPPORTÉ), ce qu'aucune géométrie de plafond ne produit : l'issue H_A est en partie déjà exclue pour ce bras.
- **Idée 8.** Bon plan, mais les paraphrases réservées exigent de nouveaux lots jugés à des moments différents (dérive du juge).
- **Idée 10.** « Verdict non ambigu » défini par la lecture simple du moniteur sélectionne les réponses saturées ; la note congruente n'a alors aucune marge, et le taux de fausse alerte est nul par construction d'un côté.

### (b) Conditions de perte de puissance ou de jugeabilité

- Idée 1 : le bruit de relecture rapporté (146/150 identiques, écart ≤ 1 pour Llama ; RAPPORTÉ) donne une variance de lecture σ²_r petite ; Δĉ entre lots a une variance ≈ σ²_r/(K·g²) : non jugeable quand g ≲ 0,3 (éloge doux de R6, où ĉ ∈ [3,08 ; 8,55], RAPPORTÉ), triviale quand g ≈ 0,7.
- Idée 2 : gain de SSE hors item nul en espérance si l'annotation est une fonction déterministe de la note (refus → 3) ; la puissance dépend de la variance des annotations *conditionnellement* à la note.
- Idée 5 : la pente affine a une erreur type en 1/√(N·Var_b(p₀ neutre)) ; une plage neutre étroite pour un lecteur (R1a : K = 3) la rend indéterminée, et l'équivalence devient non jugeable.
- Idée 6 : la corrélation variance–moyenne induite par la borne est de l'ordre de la part d'items à moins de √(σ²_w/K) du plancher ; sur `c2a_results.json`, 11 items ont p₀ ≤ 2 (OBSERVÉ-NON-AUDITÉ) : plus d'un tiers, donc l'artefact domine.
- Idée 7 : pour les items avec p₀ᵢ ≤ 1 + δ, les deux modèles prédisent le même p₁ ; la puissance est portée par Var_b(p₀) parmi les items au-dessus.
- Idée 10 : si la proportion de lectures simples à r < 1,5 ou > 4,5 dépasse la moitié, g dans le sens congruent n'est pas identifiable.

### (c) Contrôles négatifs fatals par leur absence

- Idée 6 : variances permutées (proposé) ne suffit pas ; il faut la variance calculée sur des notes disjointes de p₀.
- Idée 3 : relecture d'une première phrase neutre isolée, pour mesurer la note d'un fragment hors format.
- Idée 5 : le même lecteur calibré sur neutre(c2a) et testé sur neutre(c2b) (doit rendre ĉ indéfini et g ≈ 0).
- Idée 10 : note véridique (proposée) et note sur réponses non saturées, stratifiées par r simple.

---

## Sur la proposition E

### (a) Défauts de méthode

- **Cadre.** H_A : D > ε, H_B : D ≤ ε, avec ε « fixée avant les données confirmatoires » mais nulle part fixée, et D souvent non défini numériquement. Un plan dont la zone d'indécision n'est pas dimensionnée n'est pas préenregistrable au sens du brief.
- **E-a et E-g.** L'annotation « aveugle aux conditions » est impossible sur ces textes : la réponse pressée reprend les mots du suffixe (« poorly written », « brilliant and beautifully written » ; OBSERVÉ-NON-AUDITÉ). L'annotateur infère la condition et le critère annoté absorbe son attente. Fatal sans masquage des phrases d'écho, qui lui-même modifie l'objet annoté.
- **E-b.** Insérer une formule d'acquiescement dans une réponse neutre produit un texte incohérent (accord avec un interlocuteur absent) ; le juge peut réagir à l'incohérence, non à la politesse.
- **E-c.** La « vérité » de la déférence substantielle vient d'annotateurs qui disposent des mêmes indices lexicaux que le détecteur ; si les annotateurs s'y appuient, le lexique gagne par construction.
- **E-d.** Sous critique, les refus sont presque absents (0–1/150, RAPPORTÉ) : le modèle à catégorie d'abstention et le modèle scalaire coïncident sur ce bras ; le test n'existe que sous éloge.
- **E-e.** Le rival « modèle ordinal à déplacement latent homogène » avec ordonnées par item est le modèle de décalage uniforme, pas la loi d'attraction. Quel que soit le vainqueur, rien n'est dit de la contraction vers ĉ ; il manque un rival ordinal à pente.
- **E-f.** Correct dans son principe (même construction que B R-4) ; l'effet déclaré des graines partagées (RAPPORTÉ) n'est pas traité.
- **E-h.** Délimiter explicitement le segment évalué change le prompt du moniteur, donc rompt la comparabilité avec R7, dont le prompt (SHA `6c95c1c0…`) n'est pas publié ; un tiers ne pourra reproduire ni l'un ni l'autre.
- **E-i.** Les « strates de compétence fixées indépendamment » ne sont pas définies ; si elles le sont sur les cas honnêtes qui servent aussi à mesurer les fausses alertes, la stratification est circulaire.
- **E-j.** Bon schéma (différence de différences, préservation du neutre), mais la contrainte de préservation exige une marge d'équivalence, absente ; et un seul sous-espace aléatoire apparié ne donne pas de distribution de référence.

### (b) Conditions de perte de puissance ou de jugeabilité

- Cadre : avec un intervalle de demi-largeur h sur D, l'issue « indécision » est certaine dès que h > ε ; sans estimation de s_D, chaque expérience a une probabilité d'indécision non calculée.
- E-c : la sensibilité conditionnelle repose sur les cas « accord poli, verdict stable » ; si leur fréquence π est faible (l'échantillon suggère que l'accord explicite accompagne souvent le verdict ; OBSERVÉ-NON-AUDITÉ), le nombre de positifs est ≈ π·600 et l'intervalle sur la différence de sensibilité couvre 0.
- E-d : le gain de log-score hors item est porté par le nombre d'items ayant une masse de refus non nulle sous éloge (5 items sur 60 dans R4 ; RAPPORTÉ) ; en dessous d'une dizaine, la pénalité des paramètres supplémentaires l'emporte.
- E-e : identifiabilité mélange/décalage sur notes 1–5 nulle pour les items à moins de √(σ²_w/K) de la composante de remplacement (même condition que B R-3).
- E-f : instrument faible quand λ_instr est petit ; à K = 5 par moitié, λ est inférieur à sa valeur à K = 10, et l'intervalle du g corrigé s'élargit d'autant ; le duel devient non jugeable si cet intervalle couvre à la fois 0 et la marge.
- E-h, E-i : avec sept tailles et une stratification, la pente de g sur log(taille) repose sur deux ou trois points par strate ; son intervalle couvre 0 quelle que soit la réalité.
- E-j : si l'ablation contracte Var_b(p₀), la différence de différences a une erreur type croissante en 1/√κ ; la contrainte de préservation du neutre et la mesure de g deviennent contradictoires quand l'ablation est forte.

### (c) Contrôles négatifs fatals par leur absence

- E-a, E-g : annotation d'un lot où les phrases d'écho sont masquées, et mesure du taux auquel les annotateurs devinent la condition (doit être au hasard).
- E-b : une version jumelle où l'on insère une phrase incohérente mais non évaluative, pour isoler l'effet d'incohérence ; la « courtoisie sans accord » proposée n'y suffit pas.
- E-c : un détecteur lexical entraîné sur les annotations (plafond atteignable par le lexique), sans lequel « le moniteur bat le lexique » n'a pas de référence.
- E-e : un troisième modèle, ordinal à pente, sans lequel le duel ne concerne pas la loi.
- E-f : neutre contre neutre avec le même estimateur (proposé).
- E-j : distribution d'ablations aléatoires appariées (pas une seule), et la mesure de Var_b(p₀) sous ablation avant tout calcul de g.

---

## Remarque transversale (B1 : critique, non fusion)

Quatre propositions sur quatre construisent leur idée de tête sur un masquage ou une annotation du contenu des réponses pressées, puis recalculent g sur ce qui reste. Elles diffèrent par les motifs, pas par la logique. Aucune ne traite la condition qui rend ce geste jugeable : que la probabilité du motif soit indépendante de p₀ à l'intérieur de l'item, et que le K résiduel ne fasse pas chuter λ au point de fabriquer l'attraction sous le nul. Tant que cette indépendance n'est pas mesurée et déclarée avant le masquage, les issues « retrait », « politesse », « mélange » et « abstention » sont indistinguables d'un artefact d'estimateur, et le résultat attendu est vrai — ou faux — par construction.

FIN-DE-CELLULE
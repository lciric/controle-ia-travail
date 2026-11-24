# Préenregistrement — banc de validité du détecteur séquentiel sous référence honnête finie, gelée et contaminée — v1 (brouillon 1, non scellé)

- Auteur : Claude Fable 5.2 (`claude-fable-5-2`), sous-agent neuf rédacteur, effort élevé. Consigne : `docs/notes/banc-detecteur-sequentiel-v1/consigne-redacteur-fable-plan-banc-v1.md` (`edc2270d507b87aa191ec258668223685fc92efeaab5e60a6f9a9539bd62a7c1`).
- Date (UTC) : 2026-11-24, rédaction achevée vers 19:20Z (`date -u`). Dépôt : branche `banc/detecteur-sequentiel-reference-contaminee-v1`, commit `5449fd380e5c280a4509b2373ae83d5406e44446`.
- Commit du code d'analyse : écrit après le scellement ; tout écart du code au plan est un écart au préenregistrement, relevé par le contre-lecteur du code.
- Classe : A (préenregistrement, règle R1). Accord cité par la consigne : GO-2026-11-24-41 (0 USD, processeur seul) ; je n'ai pas ouvert le registre des accords.
- Statut : brouillon 1. Non contre-lu, non scellé, non commité. Aucune simulation de la grille n'a été lancée. Les chiffres « de principe, sous supposition » viennent du programme de l'annexe A (formes fermées et quadratures, aucun tirage).
- Documents qui font foi (chemin et empreinte SHA-256) :
  - consigne ci-dessus ;
  - `docs/notes/banc-detecteur-sequentiel-v1/anteriorite-interne-banc-detecteur-sequentiel-v1.md` — `9554a9dfe068d442aa97f4a281c64653802296f101c0a3266dd6e0f2a2defba7` (lue en entier) ;
  - `docs/notes/banc-detecteur-sequentiel-v1/sources/note-sortie-groupe-naissance-idees-fecondes-v1.md` — `2cdfa2317bae350d8547ccfe726bcc43e099854c632bfd92fd7675a80eabcf8b` (sections « En bref », 5, 6 et 8 seulement) ;
  - `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` — `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78` (sections 1, 2, 11, 13), errata 1 `34a59c49436d5239ccf2e8c4df5945a50e54665bae96bf1e32c524a643916484`, 2 `c2943188b4906993a1092f0bd5dd9faa5d87162d4ce1ff58e0dab2cff923ada7`, 3 `3335284d40efe6e4454b0eaf6e3086982a074b5ef3d9e6e87ef7844a5d40f992` (le 3 prime) ;
  - `prereg/T0.3-simulation-lemme-theoreme-v1.md` — `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb` (Hypothèse, bloc P8, Métrique, Seuil, Liste d'arrêt) ;
  - `docs/notes/percee-controle-securite-v1/calculs-percee-controle-securite-v1.txt` — `d43e62bcf522a3461933535e3b66adc930911dee321fc284c4c3a8bc43b742f1` (bloc A) ;
  - code lu pour l'interface : `src/controle_ia/agregateurs/processus_e.py` `1081469bea3564a57119b56c26ee25f27817a7e961abdf440a556dc476a15fc7` ; `src/controle_ia/simulation_t03/calibrage.py` `a2be6f6b127032aced5d75acd9cdf7c18c17e28df89978bd7102cf692c560def` ; `src/controle_ia/bases/sequentiel.py` `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` ; `src/controle_ia/manifeste.py` `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` ; `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ; `src/controle_ia/gardes.py` `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Commande du seul run décisif, après scellement de ce texte et attestation du code (section « Interface du code d'analyse ») :
  `PYTHONPATH=src python -m controle_ia.banc_detecteur_sequentiel.run_banc --prereg prereg/banc-detecteur-sequentiel-reference-contaminee-v1.md --attestation prereg/banc-detecteur-sequentiel-reference-contaminee-v1-attestation-code-v1.md`
- Ce texte ne modifie aucune hypothèse du programme, aucune revendication, aucun texte scellé. Rien de ce banc n'est revendicable : l'outil est occupé par la littérature déjà citée au dépôt (note d'antériorité, section 0, point 3). Le banc est un instrument.

## Hypothèse

**Objet.** Dire, en simulation sur processeur, si un détecteur qui accumule des scores d'épisode en épisode garde son taux de fausses alertes quand sa connaissance de l'honnête se réduit à une référence finie, tirée une fois, gelée, et en partie contaminée. C'est la face « validité » du premier pas sans dépense de la décision N-076, point 1 (les mondes plantés sous référence fixe, sous dépendance et sous référence biaisée), que le dépôt n'a pas (note d'antériorité, section 2).

**Vocabulaire et cadre commun.**
- **Épisode** : l'unité. Chaque épisode rend un **score** X, un nombre de l'intervalle [0 ; 1], plus grand quand l'épisode paraît plus suspect, disponible à la fin de l'épisode. La borne 1 du support est déclarée connue.
- **Loi honnête** F : la loi du score d'un épisode honnête. **Référence** : m scores d'épisodes tenus pour honnêtes, tirés une fois avant le déploiement, jamais mis à jour. **Horizon** n : le nombre d'épisodes surveillés accumulés. **Arrêt optionnel** : l'alerte peut être donnée après n'importe quel épisode jusqu'à n.
- **Fraction déclarée** ε_d : la part de la référence que le défenseur admet non honnête. **Fraction réelle** ε_r : la part qui l'est vraiment. La contamination porte sur un **nombre fixe** k = arrondi(ε_r·m) d'épisodes de la référence.
- **Taux de fausses alertes** : la probabilité d'une alerte jusqu'à l'horizon n quand tous les épisodes du déploiement sont honnêtes. **Taux conditionnel** : ce taux, la référence étant fixée. **Taux moyen** : sa moyenne sur le tirage de la référence. Niveau visé α.
- **Budget d'erreur partagé** : α = α_étalonnage + α_arrêt. Le premier couvre le risque que la référence tirée trompe ; le second, le risque d'alerte au fil de l'accumulation.
- **Gain écrêté** g : la fonction croissante, à valeurs dans [0 ; 1], g(x) = min(1, max(0, (x − a)/(c − a))). Le **plancher** a et le **plafond** c sont calculés sur la référence par une règle déclarée. Règle par défaut, dite « quantiles » : a et c sont les quantiles empiriques d'ordres 0,50 et 0,90 de la référence. C'est le sens donné ici à « écrêtée » : le score ne compte qu'entre a et c.
- **Rayon** r : la largeur de la bande d'incertitude sur la fonction de répartition honnête, r = ε_d + rayon d'échantillonnage, où le rayon d'échantillonnage est celui de l'inégalité de Dvoretzky-Kiefer-Wolfowitz à constante de Massart, √(ln(2/α_étalonnage) / (2·⌊(1 − ε_d)·m⌋)). « Au même rayon » veut dire : toute base comparée emploie le même r, le même gain et la même référence.
- **Processus-e employé** : le processus-e unilatéral de mélange normal du dépôt (`agregateurs/processus_e.py`), sur la somme S_t des écarts standardisés z_s = (g(X_s) − centre)/échelle, lu après chaque épisode ; alerte quand son logarithme atteint ln(1/seuil d'erreur). Paramètre de mélange ρ : celui qui minimise la frontière d'alerte à l'horizon m (`calibrage.rho_optimal(m, ·, "unilateral")`).

**Constructions comparées** (toutes sur le même score et la même référence).

| étiquette | nom en clair | centre | échelle | erreur au seuil |
|---|---|---|---|---|
| `connue` | construction bien spécifiée : loi honnête connue, aucune estimation | moyenne exacte du gain sous F, nœuds a et c exacts | 1/2 (lemme de Hoeffding, gain dans [0 ; 1]) | α |
| `naive` | construction naïve à centre et échelle estimés une fois sur la référence | moyenne empirique du gain sur la référence | écart type empirique du gain sur la référence | α |
| `rognee` | construction naïve à rognage haut : on retire les ⌈ε_d·m⌉ plus hauts scores de la référence, puis comme `naive` | idem, sur la référence rognée | idem | α |
| `enveloppe` | construction à enveloppe et budget partagé (le candidat) | borne supérieure de la moyenne honnête du gain sur la bande de rayon r (formule en « Métrique ») | 1/2 | α_arrêt |

Sur la loi normale du contrôle de banc, `connue_normale` et `naive_normale` sont les mêmes constructions sans gain : z = (X − μ)/σ avec μ et σ exacts, ou estimés sur la référence.

**Énoncés testés.**
- **É1 — défaut de la construction naïve.** Une référence gelée rend les facteurs du processus-e dépendants entre eux : le centre estimé garde une erreur de l'ordre de σ/√m qui ne se moyenne pas, la somme dérive, et le taux de fausses alertes sous arrêt optionnel croît avec n/m jusqu'à dépasser α, sans aucune contamination (calcul du collisionneur, note de sortie, « En bref »). C'est le contrôle de banc.
- **É2 — tenue de l'enveloppe à budget partagé.** Suppositions : (i) au plus ⌊ε_d·m⌋ épisodes de la référence ne sont pas des tirages honnêtes, les autres sont indépendants et de loi F ; (ii) le déploiement honnête est indépendant de la référence et, sachant son passé, chaque épisode a la loi F. Alors, avec probabilité au moins 1 − α_étalonnage sur le tirage de la référence, le taux conditionnel de fausses alertes est au plus α_arrêt **à tout horizon, y compris n > m** ; donc le taux moyen est au plus α. La garantie visée est **conditionnelle à la référence tirée** ; le banc rapporte les deux taux.
  - Preuve, en trois pas. (a) Sur l'événement de Dvoretzky-Kiefer-Wolfowitz, F(x) ≥ F̂(x) − r pour tout x, où F̂ est la fonction de répartition empirique de la référence entière (la contamination déplace F̂ d'au plus k/m ≤ ε_d). (b) Pour tout gain croissant à valeurs dans [0 ; 1], même choisi sur la référence, la moyenne honnête du gain est alors au plus la moyenne du gain sous la loi la plus haute de la bande, c'est-à-dire la moyenne empirique après déplacement de la masse r la plus basse vers 1. (c) Les écarts du gain à cette borne ont une moyenne conditionnelle négative ou nulle et tiennent dans un intervalle de largeur 1 : par le lemme de Hoeffding, le processus-e de mélange normal d'échelle 1/2 est une surmartingale positive, et l'inégalité de Ville borne par α_arrêt la probabilité qu'il atteigne 1/α_arrêt.
  - La même preuve couvre une **dérive** : si la loi d'où sort la référence est à distance de Kolmogorov unilatérale au plus ε_d de la loi honnête du déploiement, la garantie tient. Contamination et dérive puisent dans le même budget ε_d.
- **É3 — défaut du rognage haut.** Un seuil rendu « robuste » en retirant les plus hauts scores de la référence est anticonservateur dès que la contamination réelle est inférieure à la fraction rognée (critique acceptée au collisionneur, note de sortie, « En bref »).
- **É4 — hors des suppositions.** Sous contamination réelle double de la déclarée, dérive au-delà du budget, autocorrélation, grappes par tâche, l'enveloppe n'a plus de garantie ; elle peut tenir par sa marge. Sous grappes, la garantie revient si la **tâche** devient l'unité (un score par tâche, m compté en tâches).
- **É5 — prix.** L'enveloppe ne peut pas détecter un déplacement de la moyenne du gain inférieur à sa marge, de l'ordre de r. À m = 400 ce prix est dominé par le rayon d'échantillonnage.
- **É6 — bases.** La somme cumulée écrêtée lue une seule fois à un horizon connu est plus puissante que le processus-e à cet horizon ; relue à chaque épisode sans correction elle perd son taux ; la somme cumulée de Page étalonnée à un horizon déclaré est valide jusqu'à cet horizon.
- **É7 — pente de la frontière d'identifiabilité.** Trois thèses du collisionneur sur le plus petit déplacement détectable quand la référence est contaminée à la fraction ε : plancher proportionnel à ε pour des scores bornés (lettre B) ; plancher en σ₀·√ε (lettre A, par l'estimation robuste de la moyenne) ; deux régimes (lettre C). Lecture retenue ici, par dérivation (annexe A, bloc 7) : le plancher d'une construction à enveloppe vaut le rayon multiplié par la largeur d'écrêtage c − a. La largeur est la portée du support si l'on n'écrête qu'à la borne du support (pente 1) ; elle vaut σ₀/√ε si l'on écrête au rayon que seule la variance autorise (pente 1/2, tant que ce rayon tient dans le support) ; elle vaut un écart entre quantiles si l'on écrête à des quantiles de la référence (pente 1, constante proportionnelle à σ₀). La bascule entre les deux premiers se fait à ε = (σ₀/portée)².

**Hors de portée.**
- Tout organisme, toute activation, tout score réel : les lois sont synthétiques et ne sont étalonnées sur aucune donnée du dépôt.
- La grille de T0.3, bloc P8 (règle de Ville sous écart type sous-estimé, dépendance sur les actions d'un épisode) : citée, non rejouée. Ici l'unité est l'épisode et l'objet est la référence.
- Le calcul de puissance A et A bis de la note « percée » : employé comme repère, non redérivé.
- La prévision scellée de la loi de la référence honnête (N-076, point 1) : pièce distincte, sur organismes ; ce banc n'en tranche aucun nœud (L1 à L18).
- La conception des mondes 3 et 4 du banc des mondes plantés.
- Les trois autres sources de validité de N-076 (témoins entrelacés, nul par acte, tirage du défenseur) ; un oracle à verdict différé ; la statistique conjointe entre copies ; la table du seuil au taux d'audit.
- La frontière minimax sur tous les détecteurs et toutes les formes de sabotage : le duel ne mesure que la famille gelée de trois règles d'écrêtage, contre un décalage diffus.
- Un processus-e par paris multiplicatifs ou à variance empirique : non mis au banc (point pour la mère 6).

## Prédiction chiffrée et signe attendu

Nature de chaque prédiction : **[preuve]** (établie par démonstration, vérifiée en simulation : une contradiction signale d'abord un défaut du banc), **[calcul]** (forme fermée ou quadrature de l'annexe A, de principe, sous supposition), **[heuristique]**. « Instrument » : la prédiction vérifie le banc. « Informative » : elle apprend quelque chose. Niveaux : α = 0,05 ; α_étalonnage = α_arrêt = 0,025. Tous les chiffres ci-dessous sont de principe, sous supposition.

**Bloc A — contrôle de banc (décisif pour le banc ; rien d'autre n'est lu s'il échoue).**
- **A-sain-1** [preuve : inégalité de Ville ; instrument]. `connue_normale`, m = 400 : taux à n = 16m au plus α.
- **A-sain-2** [preuve : Ville et Hoeffding ; instrument]. `connue` sur la loi Bêta(1 ; 4), m = 400 : taux à n = 16m au plus α.
- **A-artefact** [calcul exact, borne inférieure ; instrument]. `naive_normale`, m = 400, aucune contamination, n = 16m = 6 400 : taux moyen **au moins 2α = 0,10**. Borne inférieure exacte quand seul le centre est estimé, par la seule lecture à l'instant n : 0,229 (annexe A, bloc 2). Écart fixé d'avance : α au-dessus de α. Ce qui réfuterait : un taux non significativement au-dessus de 0,10 ; le banc est alors déclaré défectueux.
- **A-vivacité** [calcul ; instrument]. Sous un sabotage massif (décalage latent 2), chaque construction et chaque base donne l'alerte avant n = m dans au moins 95 % des cas. Sans ce contrôle, un détecteur muet passerait tous les critères de tenue.
- Informatif : **A-i1** [calcul], `naive` sur Bêta(1 ; 4), m = 400, n = 16m : taux au moins 2α. **A-i2** [calcul], m = 100, n = 64m : au moins 2α (borne 0,34). **A-i3** [calcul], le taux de `naive` croît avec n/m ; bornes inférieures 0,004 ; 0,025 ; 0,100 ; 0,229 à n/m = 1/4 ; 1 ; 4 ; 16. À n = m, aucune prédiction de dépassement de α : c'est la règle d'horizon de N-076 vue du côté des fausses alertes. **A-i4** [calcul], à n = 16m, au moins 20 % des références ont un taux conditionnel au-dessus de 2α (borne à l'instant n : 0,33).

**Bloc B — enveloppe, référence propre, budget partagé** (m ∈ {100 ; 400 ; 1 600}, ε_d ∈ {0 ; 0,02 ; 0,10}).
- **B1** [preuve ; instrument]. Taux moyen de `enveloppe` au plus α à tous les horizons, 16m compris, dans les neuf cellules.
- **B2** [preuve ; instrument]. Part des références dont le taux conditionnel dépasse α_arrêt : au plus α_étalonnage.
- **B3** [preuve ; instrument du générateur]. Fréquence de l'événement « référence hors enveloppe » (écart unilatéral entre la fonction de répartition empirique des honnêtes et F supérieur au rayon d'échantillonnage) : au plus α_étalonnage. Attendu près de la moitié, la forme bilatérale servant un besoin unilatéral.
- **B4** [calcul ; informative]. Marge exacte de la borne (borne moins moyenne honnête du gain) : moyenne égale à r à 0,01 près (0,074 ; 0,095 ; 0,178 à m = 400), négative pour au plus α_étalonnage des références.
- **B5** [calcul ; informative]. `rognee`, ε_d = 0,10, référence propre, m = 400 : taux **à n = m** au moins 2α (marge de population −0,073 ; dérive cumulée 80 contre une frontière de 55). À ε_d = 0,02 : taux à 16m strictement au-dessus de celui de `naive` (signe seul).
- **B6** [calcul ; informative]. Le taux moyen de `enveloppe` est inférieur à α/5 : la garantie est payée d'une marge.

**Bloc C — contamination de la référence** (m = 400 ; couples (ε_d ; ε_r) : (0,02 ; 0,02), (0,02 ; 0,04), (0,10 ; 0,02), (0,10 ; 0,10), (0,10 ; 0,20) ; placements haut, seuil, bas).
- **C1** [preuve ; instrument]. `enveloppe`, ε_r ≤ ε_d (neuf cellules) : taux moyen au plus α ; part des références au-dessus de α_arrêt au plus α_étalonnage.
- **C2** [calcul de population ; informative]. `enveloppe`, contamination réelle double de la déclarée (six cellules) : taux à 16m au plus α. Marges de population toutes au-dessus de +0,08 (annexe A, bloc 4) : la tenue vient de la marge, non de la garantie, qui ne couvre pas ces cellules. Ce qui réfuterait : un taux au-dessus de α.
- **C3** [calcul ; informative]. `naive`, placement bas, ε_r = 0,20 : taux **à n = m** au moins 2α (dérive cumulée 73 contre 55). Placement bas, ε_r = 0,10 : taux à 4m strictement au-dessus de la cellule propre (signe).
- **C4** [calcul ; informative]. `rognee`, (0,10 ; 0,02), les trois placements : taux à n = m au moins 2α (dérives cumulées 65 à 88 contre 55). C'est la contamination basse qui fait tomber le rognage.
- **C5** [calcul ; informative]. Masquage : sous placements haut et seuil, la marge moyenne de `enveloppe` croît avec ε_r (de r à r + 0,015 ; + 0,08 ; + 0,15 pour ε_r = 0,02 ; 0,10 ; 0,20). La contamination par des épisodes sabotés visibles ne menace pas la validité ; elle coûte de la puissance.

**Bloc D — dérive bénigne graduée** (m = 400 ; décalage latent d ∈ {0,05 ; 0,10 ; 0,20 ; 0,40 ; 0,80}, soit une distance de Kolmogorov de 0,02 ; 0,04 ; 0,08 ; 0,16 ; 0,31).
- **D1** [preuve ; instrument]. Dans le budget déclaré (ε_d = 0,02 : d = 0,05 ; ε_d = 0,10 : d ≤ 0,20) : taux au plus α.
- **D2** [calcul ; informative]. Marge de population au moins +0,035 : tenue à 16m (ε_d = 0,02 : d = 0,10 ; ε_d = 0,10 : d = 0,40).
- **D3** [calcul ; informative]. Marge de population au plus −0,035 : taux à 16m au moins 2α (ε_d = 0,02 : d = 0,40 et 0,80 ; ε_d = 0,10 : d = 0,80).
- Sans prédiction : ε_d = 0,02, d = 0,20 (marge +0,030, dans la bande d'incertitude de la référence).

**Bloc E — autocorrélation entre épisodes** (latent autorégressif d'ordre 1, φ ∈ {0,2 ; 0,5}).
- **E1** [heuristique, signe ; informative]. `connue` : taux strictement au-dessus du cas indépendant, croissant avec φ. Même phénomène que T0.3, P8.2, à l'unité de l'épisode.
- **E2** [calcul ; informative]. `enveloppe`, ε_d = 0,02 : taux à 16m au plus α, par la marge.

**Bloc F — grappes par tâche** (référence de 400 épisodes en 100 tâches de 4 ou 20 tâches de 20 ; part de variance latente entre tâches ω ∈ {0,1 ; 0,3} ; déploiement sur des tâches nouvelles).
- **F1** [preuve ; instrument]. `enveloppe` à **unité tâche** : taux au plus α à tous les horizons.
- **F2** [heuristique, signe ; informative]. `enveloppe` à unité épisode : taux et part des références à marge négative au-dessus de la cellule indépendante de mêmes m et ε_d. Aucune prédiction sur le dépassement de α (estimation grossière : de l'ordre de α_arrêt à 20 tâches de 20, ω = 0,3).
- **F3** [calcul ; informative]. Prix de l'unité tâche : rayon 0,170 à 100 tâches, 0,360 à 20 tâches (ε_d = 0,02).

**Bloc G — bases, à n = m = 400** (loi connue, puis enveloppe à ε_d = 0,02).
- **G1** [instrument]. Somme à horizon fixe, loi connue : taux égal à α_arrêt à 0,005 près.
- **G2** [instrument]. Somme de Page étalonnée à l'horizon m : taux à n = m au plus α_arrêt.
- **G3** [heuristique ; informative]. Même somme relue à chaque épisode, loi connue : taux à n = m au moins 2·α_arrêt.
- **G4** [preuve ; instrument]. Processus-e (`connue` et `enveloppe` au seuil α_arrêt) : taux au plus α_arrêt à tous les horizons.
- **G5** [calcul ; informative]. À l'horizon connu n = m, la somme à horizon fixe détecte un décalage plus petit que le processus-e : rapport des décalages détectables (processus-e sur somme) supérieur à 1, attendu entre 1,5 et 3 (1,55 pour la frontière, 1,4 pour l'échelle de Hoeffding ; annexe A, bloc 6).
- **G6** [sans signe prédit ; exploratoire]. Processus-e contre somme de Page sous arrêt optionnel jusqu'à m : rapport attendu entre 0,8 et 1,8.

**Bloc H — duel sur la pente** (m = n = 10⁶ ; ε ∈ {0,01 ; 0,02 ; 0,04 ; 0,08} ; deux régimes de loi).
- **H-D1** [calcul ; informative]. Pente du plancher de la meilleure des trois règles d'écrêtage contre le rayon : **au moins 0,75 dans les deux régimes** (attendu 0,9 à 1,1 ; population : 1,03 et 1,04). Régime étalé : la règle « support » l'emporte. Régime concentré : la règle « quantiles » l'emporte, avec un plancher deux à quatre fois plus bas que la règle « rayon de variance ».
- **H-D2** [calcul ; informative]. Pente du plancher de la règle « rayon de variance » : au moins 0,75 dans le régime étalé (attendu 1,0), **inférieure à 0,75 dans le régime concentré** (attendu 0,5 à 0,7 ; population : 0,62).
- Ce qui réfuterait chaque thèse : tableau en « Critères de lecture gelés », bloc H.

**Descriptif, sans verdict** : tous les taux aux horizons autres que ceux nommés ; toutes les lectures de puissance au-delà de n = m, sous l'étiquette « au-delà de la référence » ; le processus-e à échelle estimée ; la somme de Page lue au-delà de son horizon ; les cellules à m = 1 600 du bloc C ; les rapports des planchers à σ₀·r dans le duel ; toutes les figures.

## Métrique

- **Alerte** d'une construction sur une trajectoire : il existe t ≤ n avec ln E_t ≥ ln(1/erreur au seuil), où E_t est le processus-e de la construction. Convention : « supérieur ou égal ».
- **Taux conditionnel estimé** de la référence j : p̂_j = (trajectoires en alerte jusqu'à n) / R_dép. **Taux moyen estimé** : p̂ = moyenne des p̂_j sur les R_réf références.
- **Erreur type du taux moyen** : se = max( s/√R_réf ; √(max(p̂(1 − p̂) ; 1/N)/N) ), avec s l'écart type empirique des p̂_j et N = R_réf·R_dép. La référence est la grappe : les trajectoires d'une même référence ne sont pas indépendantes.
- **Parts conditionnelles** : pour c ∈ {α_arrêt ; α ; 2α}, part brute des références avec p̂_j > c, et part nette avec p̂_j > c + 3·√(c(1 − c)/R_dép). Les critères emploient la part nette ; les deux sont rapportées. Erreur type d'une part q : √(max(q(1 − q) ; 1/R_réf)/R_réf).
- **Borne de l'enveloppe.** Soient g₍₁₎ ≤ … ≤ g₍ₘ₎ les gains triés de la référence et k = ⌊r·m⌋. Borne = (1/m)·[ Σ_{i ≥ k+1} g₍ᵢ₎ − (r·m − k)·g₍ₖ₊₁₎ ] + r, et 1 si r ≥ 1. C'est l'intégrale sur s de min(1 ; part empirique des gains au-dessus de s, plus r).
- **Quantile empirique** d'ordre q : la statistique d'ordre de rang ⌈q·m⌉ (inverse de la fonction de répartition empirique, sans interpolation).
- **Marge exacte** d'une référence : centre de la construction moins moyenne du gain sous la loi honnête du déploiement, pour les nœuds de cette référence. Forme fermée sous Bêta(1 ; 4) sans dérive : [(1 − a)⁵ − (1 − c)⁵] / (5(c − a)) ; quadrature déterministe à 4 000 points sous dérive. Sans bruit de Monte-Carlo.
- **Référence hors enveloppe** : max_i ( i/m_h − F(x₍ᵢ₎) ) > rayon d'échantillonnage, sur les m_h épisodes honnêtes de la référence.
- **Bases**, en unités z = (g(X) − centre)/écart type du gain (exact en loi connue, empirique sur la référence sinon), centre identique à celui de la construction comparée :
  - somme à horizon fixe : alerte si S_n/√n ≥ 1,959964, lue à n seulement ;
  - même somme relue : alerte s'il existe t entre 10 et n avec S_t/√t ≥ 1,959964 ;
  - somme de Page : C_t = max(0 ; C_{t−1} + z_t − 0,1) ; alerte si C_t ≥ h pour un t ≤ n ; h est le seuil de Monte-Carlo (`calibrage.seuil_mc`) au niveau α_arrêt du maximum de C sur 400 épisodes, sur 100 000 trajectoires honnêtes en loi connue.
- **Décalage détectable** d'un détecteur à l'horizon n : la valeur du décalage latent d où sa puissance vaut 1/2, par interpolation linéaire entre les deux points de la grille de d qui encadrent 1/2 (le point d = 0 compris). Non atteint dans la grille : « censuré ».
- **Plus petit décalage détecté d'une répétition du duel** : le plus petit décalage additif Δ tel que le détecteur donne l'alerte jusqu'à n quand tous les scores du déploiement sont min(X + Δ ; 1), les tirages étant tenus fixes ; trouvé par dichotomie sur [0 ; 1], 24 pas. Bien défini : le gain est croissant et le processus-e est croissant en la somme. **Plancher** d'une cellule : la médiane sur les répétitions, c'est-à-dire le décalage détecté avec puissance un demi.
- **Pente** : coefficient de la droite des moindres carrés de ln(plancher) contre ln(r) sur les quatre fractions. **Pentes locales** : entre les deux plus petits rayons, entre les deux plus grands. Erreur type par rééchantillonnage des répétitions (2 000 tirages), le minimum sur les règles étant refait à chaque tirage.

## Seuil

- α = 0,05 ; α_étalonnage = 0,025 ; α_arrêt = 0,025. Seuil d'alerte : ln 20 pour `connue`, `naive`, `rognee` dans les blocs A à F ; ln 40 pour `enveloppe` partout et pour tous les détecteurs du bloc G.
- **Seuil de lecture de Monte-Carlo** : Z = 4 erreurs types pour toute comparaison.
- **Chute** : taux au moins 2α (2·α_arrêt en G3). **Tenue** : taux au plus α (α_arrêt en G).
- **Vivacité** : 0,95. **Tolérance de l'approximation normale** (G1) : 0,005. **Seuils de marge de population** pour prédire tenue ou chute (bloc D) : ±0,035.
- **Duel** : seuil de pente 0,75 ; « non exécutable » si l'erreur type de la pente dépasse 0,03, si plus de 5 % des répétitions d'une cellule sont censurées ou donnent l'alerte à Δ = 0, ou si les deux pentes locales diffèrent de plus de 0,25.
- **Bornes de l'audit de symétrie** : voir « Critères de lecture gelés ».

## Plan d'analyse

### Lois et générateur

- Toutes les lois passent par un **latent normal** Z : X = Q(Φ(Z + d)), Q fonction quantile de la loi, d dérive latente (0 par défaut). Latent indépendant ; ou autorégressif d'ordre 1, Z_t = φ·Z_{t−1} + √(1 − φ²)·ξ_t, départ stationnaire ; ou en grappes, Z = √ω·A_tâche + √(1 − ω)·ξ.
- **Loi principale** : Bêta(1 ; 4), Q(u) = 1 − (1 − u)^{1/4}. Moyenne 0,20 ; asymétrique à droite, comme un score de soupçon ; fonction de répartition fermée. Gain « quantiles » : a = 0,159 ; c = 0,438 ; moyenne du gain 0,2615 ; écart type 0,357.
- **Loi du contrôle** : normale centrée réduite (score non borné, sans gain), pour rattacher le contrôle au calcul exact et à T0.3, P8.1.
- **Lois du duel** : uniforme sur [0 ; 1] (régime étalé : σ₀ = 0,289, portée au plafond 0,5, bascule à 0,33) ; uniforme sur [0,2 − 0,02·√3 ; 0,2 + 0,02·√3] (régime concentré : σ₀ = 0,02, portée 0,8, bascule à 0,0006).
- **Contaminants** (k épisodes de la référence, tirés sans remise, remplacés) : « haut », loi Bêta(4 ; 1) (sabotage visible) ; « seuil », uniforme entre les quantiles honnêtes 0,90 et 0,97 (dans la queue qui fixe le plafond) ; « bas », score 0 (le pire pour la validité : la référence paraît plus basse que l'honnête). Dans le duel : score 1.
- **Sabotage** (blocs A-vivacité, G) : décalage latent d sur tout le déploiement. Dans le duel : décalage additif Δ écrêté à 1.
- Le générateur est un module à part, réemployable par le monde 4 du cahier des mondes plantés ; il ne tient pas lieu de sa conception.

### Grille : niveaux, justification, ce que chaque cellule cherche à faire tomber

Horizons lus : n ∈ {m/4 ; m ; 4m ; 16m} ; à m = 100, aussi 64m ; à m = 1 600, jusqu'à 4m. Une trajectoire est simulée jusqu'au plus long horizon ; l'instant de première alerte donne tous les horizons.

| bloc | cellules | constructions | tailles (R_réf × R_dép) | ce que la cellule cherche à faire tomber |
|---|---|---|---|---|
| A1, A2 | loi normale ; m = 400, puis m = 100 | `connue_normale`, `naive_normale` | 1 000 × 1 000 | le banc lui-même : la naïve doit tomber, la bien spécifiée doit tenir |
| A3, A4 | Bêta(1 ; 4) ; m = 400, puis 100 | `connue`, `naive` | 1 000 × 1 000 | idem, sur la loi principale |
| A5 | sabotage massif d = 2 ; m ∈ {100 ; 400} ; ε_d = 0,10 | toutes, bases comprises | 200 × 50 | un détecteur muet |
| B (9) | m ∈ {100 ; 400 ; 1 600} × ε_d ∈ {0 ; 0,02 ; 0,10}, référence propre | `enveloppe`, `naive`, `rognee` | 1 000 × 1 000 | le partage du budget ; le rognage sous contamination nulle |
| C (15 + 2) | m = 400 ; cinq couples (ε_d ; ε_r) × trois placements ; plus m = 1 600, contamination double, placement bas | `enveloppe`, `naive`, `rognee` | 500 × 500 | l'enveloppe par la contamination basse, haute, ciblée, double ; le rognage par la contamination basse ; la naïve par le placement bas |
| D (10) | m = 400 ; ε_d ∈ {0,02 ; 0,10} × cinq dérives | `enveloppe`, `naive` | 500 × 500 | l'enveloppe au-delà de son budget de biais |
| E (4) | m = 400 ; ε_d = 0,02 ; φ ∈ {0,2 ; 0,5} ; déploiement seul, ou référence et déploiement | `connue`, `naive`, `enveloppe` | 500 × 500 | la surmartingale par la dépendance entre épisodes ; le rayon d'échantillonnage par une référence dépendante |
| F (4) | 100 tâches de 4, 20 tâches de 20 ; ω ∈ {0,1 ; 0,3} ; ε_d = 0,02 | `enveloppe` à unité épisode, `enveloppe` à unité tâche, `naive` | 500 × 500 | l'épisode comme unité indépendante |
| G (2 × 11) | m = 400 ; loi connue, puis enveloppe à ε_d = 0,02 ; d ∈ {0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1,00} | processus-e (échelle 1/2 ; échelle estimée, descriptif), trois bases | 20 000 trajectoires (400 × 50 sous enveloppe), mêmes tirages pour tous les d | l'avantage supposé du processus-e |
| H (2 × 4) | m = n = 10⁶ ; quatre fractions ; ε_r = ε_d, contaminant à 1 | `enveloppe` sous trois règles d'écrêtage | 200 répétitions | chacune des thèses sur la pente |

Justification des niveaux. m = 400 est l'exemple de N-076 ; 100 et 1 600 l'encadrent d'un facteur 4. n/m = 16 est le premier rapport où la borne exacte du contrôle dépasse 2α avec marge. ε_d = 0,02 est en dessous du rayon d'échantillonnage à m = 400 (0,074), ε_d = 0,10 au-dessus. Les dérives couvrent de la moitié à quinze fois le petit budget. φ = 0,2 reprend T0.3 ; 0,5 le double. Vingt tâches de vingt épisodes approchent le cas où la tâche pèse autant que l'épisode ; ω = 0,3 est une part forte, 0,1 faible. Les fractions du duel sont à raison 2 sur près d'une décade ; m = 10⁶ rend le rayon d'échantillonnage (0,0015) petit devant la plus petite fraction.

Sous unité tâche : le score d'une tâche est la moyenne des scores de ses épisodes ; toute la construction s'applique aux scores de tâche, avec m compté en tâches et un incrément par tâche ; horizons en tâches {m/4 ; m ; 4m ; 16m}.

Règles d'écrêtage du duel. « Support » : a = 0, c = 1. « Rayon de variance » : a = max(0 ; médiane − σ̃/√r), c = min(1 ; médiane + σ̃/√r), avec σ̃ l'écart interquartile de la référence divisé par 1,349. « Quantiles » : la règle par défaut. Les trois sont valides sous É2, qui vaut pour tout gain croissant choisi sur la référence.

### Tailles et erreur de Monte-Carlo, déclarées d'avance

- Taux moyen : erreur type au plus √(p(1 − p)/R_réf) quand tout le hasard est dans la référence. Soit, à p = 0,05 : 0,0069 (R_réf = 1 000) et 0,0097 (500) ; à p = 0,10 : 0,0095 et 0,0134. Avec Z = 4 : tenue confirmée jusqu'à 0,078 ou 0,089 ; chute confirmée à partir de 0,138 ou 0,154.
- **Puissance du contrôle d'artefact** : taux attendu au moins 0,229 ; erreur type attendue 0,013 à ce taux ; seuil de confirmation 0,10 + 4 × 0,013 = 0,153. Le contrôle passe avec une marge de plus de cinq erreurs types si le calcul est juste.
- Part des références au-dessus d'un seuil : erreur type 0,0049 à 0,025 (R_réf = 1 000) ; critère « au plus α_étalonnage » confirmé jusqu'à 0,045 (0,053 à 500).
- Taux conditionnel d'une référence : erreur type 0,0049 à 0,025 et 0,0095 à 0,10 (R_dép = 1 000) ; 0,0070 et 0,0134 (500).
- **Effectif du duel par analyse de puissance** : la pente attendue la plus proche du seuil est 0,62, à 0,13 du seuil. Il faut une erreur type de pente au plus 0,03, soit une erreur relative de chaque plancher au plus 0,043, soit au moins 19 répétitions si la dispersion relative d'une répétition est 0,15. Retenu : 200.
- Comparaisons à verdict : environ 150. Avec Z = 4, la probabilité d'au moins une contrariété due au seul bruit est de l'ordre de 0,5 %.

### Graines, manifeste, sorties (R9, R6, R12)

- Entropie racine fixée ici : `17478886177536127460746961611737655340` (seize premiers octets du SHA-256 de la chaîne `banc-detecteur-sequentiel-reference-contaminee-v1/entropie`). Une réplication emploie le suffixe `/replication` dans les noms de tâche.
- Une tâche par flux et par cellule, nommée `bloc/cellule/flux`, flux ∈ {`reference`, `deploiement`, `etalonnage_page`, `reechantillonnage`} ; graines par `manifeste.graines`. Le tirage d'indice j d'une tâche (référence j, lot j) emploie `numpy.random.SeedSequence(entropie, spawn_key=(clé de la tâche, j))`. Les cellules sont donc indépendantes de l'ordre et du nombre de processus.
- Manifeste par `manifeste.creer_manifeste(…, decisif=True, prereg=…)` ; résultats par `manifeste.ecrire_resultat`, un fichier scellé par bloc sous `diag/<run_id>/`.
- **Sorties brutes** : par cellule, construction et référence, le nombre d'alertes à chaque horizon ; la marge exacte ; l'indicateur « hors enveloppe » ; les nœuds, le centre, l'échelle ; pour le duel, le plus petit décalage détecté de chaque répétition et de chaque règle ; les durées. Les trajectoires ne sont pas gardées : elles se rejouent des graines.

### Ordre d'exécution

1. Gardes de lancement (liste d'arrêt, points 1 à 5), gardes du générateur et d'équivalence.
2. Bloc A. Le code applique lui-même les quatre critères décisifs du contrôle. S'ils ne sont pas tous confirmés, il écrit `arret.json` et s'arrête : **aucun autre bloc n'est calculé ni lu**.
3. Blocs B à H, sur quatre processus au plus, cellule par cellule.
4. Lecture mécanique des critères gelés par le code (`lecture-mecanique.json`), qui n'est pas un verdict.
5. Verdict par un sous-agent neuf, qui n'a écrit ni ce texte, ni le code, ni leurs contre-lectures (R13, pour le principe : ce banc n'est pas une porte). Il reçoit explicitement : ce préenregistrement, l'attestation du code, le manifeste, les fichiers de `diag/<run_id>/`. Il applique les tables ci-dessous et rien d'autre ; son verdict est scellé.

### Comparaisons

- Chaque prédiction se lit dans sa cellule, contre son seuil ou contre sa cellule de référence nommée (même m, même ε_d, sans le facteur étudié), par les règles de la table A.
- Bloc G : mêmes tirages de déploiement pour tous les détecteurs et tous les d (appariement).
- **Règle qui tranche « que doit battre un processus-e »**, écrite d'avance :
  1. Le processus-e est jugé contre la base **valide sous la même lecture**.
  2. À horizon connu, lu une fois (n = m) : le comparateur est la somme à horizon fixe. Son avantage attendu est rapporté comme le **prix de la garantie** (rapport des décalages détectables). Il ne compte jamais comme un échec du processus-e.
  3. Sous arrêt optionnel jusqu'à l'horizon déclaré (n = m) : le comparateur est la somme de Page étalonnée à cet horizon. Issue à trois valeurs, table du bloc G.
  4. Une base dont le taux mesuré de fausses alertes dépasse α_arrêt de plus de Z erreurs types dans la cellule est **disqualifiée** : la battre en puissance ne compte pas.
  5. Au-delà de n = m : seule la validité se lit ; toute puissance est étiquetée « au-delà de la référence », sans verdict.
- Processus-e jugé : celui d'échelle 1/2, qui porte la garantie. La variante à échelle estimée est descriptive.

## Critères de lecture gelés

**Table A — lecture d'une prédiction dans une cellule** (p̂ et se selon « Métrique » ; Z = 4).

| forme | confirmé | contraire | non concluant |
|---|---|---|---|
| tenue : « au plus c » | p̂ ≤ c + Z·se | sinon | — |
| chute : « au moins c » | p̂ ≥ c + Z·se | p̂ ≤ c − Z·se | sinon |
| signe : « strictement au-dessus de la cellule de référence » | p̂ − p̂_réf ≥ Z·√(se² + se_réf²) | p̂ − p̂_réf ≤ −Z·√(se² + se_réf²) | sinon |
| part conditionnelle « au plus α_étalonnage » | part nette ≤ α_étalonnage + Z·se de la part | sinon | — |
| égalité à tolérance τ (G1) | \|p̂ − c\| ≤ Z·se + τ | sinon | — |
| marge moyenne « égale à r à 0,01 près » (B4) | \|moyenne − r\| ≤ 0,01 | sinon | — |
| vivacité | taux d'alerte à n = m ≥ 0,95 | sinon | — |

**Table B — verdict sur le banc.**

| issue du bloc A | verdict | suite |
|---|---|---|
| A-sain-1, A-sain-2, A-artefact et A-vivacité confirmés | banc sain | les blocs B à H se calculent et se lisent |
| A-artefact non confirmé (contraire ou non concluant) | **banc défectueux** : il ne voit pas le défaut connu | arrêt ; rien d'autre n'est lu ; diagnostic selon le protocole après arrêt |
| A-sain-1 ou A-sain-2 contraire | **banc défectueux** : il condamne une construction prouvée | idem |
| A-vivacité contraire pour une construction | **banc défectueux** pour cette construction : ses tenues ne prouvent rien | idem |

**Table C — verdict par énoncé** (après « banc sain »).

| énoncé | prédictions décisives | confirmé | réfuté | non concluant |
|---|---|---|---|---|
| É1, défaut de la naïve | A-artefact ; A-i1 | les deux confirmées | A-i1 contraire (A-artefact contraire arrête le banc) | A-i1 non concluante : « établi sur la loi normale seulement » |
| É2, tenue de l'enveloppe | B1, B2, C1, D1 (toutes cellules) | toutes confirmées | au moins une contraire, encore contraire à la réplication | une contraire, confirmée à la réplication : « tenue, une cellule rejouée » |
| É3, défaut du rognage | B5 (ε_d = 0,10), C4 | toutes confirmées | toutes contraires | sinon |
| É4, hors suppositions | C2, D2, D3, E2, F1, F2 | chaque cellule reçoit « tient », « tombe » ou « non concluant » ; pas de verdict d'ensemble ; F1 contraire se traite comme É2 | — | — |
| É5, prix | B4, B6, C5 | B4 confirmée dans les neuf cellules | B4 contraire dans une cellule | — |
| É6, bases | G1 à G5 | table du bloc G | | |
| É7, pente | H-D1, H-D2 | table du bloc H | | |

Une prédiction **[preuve]** contraire n'est jamais lue comme une découverte avant l'audit : elle déclenche l'audit de symétrie et une réplication du bloc entier (graines `/replication`, mêmes tailles). Les deux runs sont rapportés.

**Bloc G — lecture.** Rapport ρ = décalage détectable du processus-e / décalage détectable de la base, à n = m ; erreur type par rééchantillonnage des trajectoires (des références, sous enveloppe), 1 000 tirages.

| comparaison | issue | lecture |
|---|---|---|
| contre la somme à horizon fixe | ρ − Z·se > 1 | « prix de la garantie : ρ » ; G5 confirmée |
| | ρ + Z·se < 1 | G5 contraire : le processus-e fait mieux même à horizon connu ; audit de symétrie |
| | sinon | « prix non mesurable à cette taille » |
| contre la somme de Page (valide) | ρ + Z·se < 1 | le processus-e bat la base valide sous arrêt optionnel |
| | ρ − Z·se > 1 | il est battu par elle |
| | sinon | à égalité |
| contre la somme relue | taux de la base > α_arrêt + Z·se | base disqualifiée ; G3 se lit par la table A |
| un décalage détectable censuré | | comparaison « non exécutable » |

La réponse au désaccord du collisionneur est la paire (prix à horizon connu ; issue contre la base valide sous arrêt optionnel), dans chacune des deux couches. Aucune des six combinaisons n'est un échec du banc.

**Bloc H — lecture du duel.** Une statistique (la pente β), un seuil (0,75), deux hypothèses complémentaires sur le même dispositif : H_lin « β ≥ 0,75 » et H_rac « β < 0,75 ». D'abord la clause **« non exécutable »** (section « Seuil ») : si elle joue pour un régime, ce régime n'a pas de verdict et la raison est rapportée ; aucune zone grise.

| duel | régime étalé | régime concentré | lecture |
|---|---|---|---|
| D1, meilleure règle de la famille | H_lin | H_lin | sur ce dispositif, la frontière est linéaire dans les deux régimes : la thèse « proportionnel à ε pour des scores bornés » tient ; la thèse « σ₀·√ε » est réfutée comme pente de la frontière |
| | H_lin | H_rac | la thèse des deux régimes tient pour la frontière ; la thèse « proportionnel à ε » est réfutée dans le régime concentré |
| | H_rac | H_rac | la thèse « σ₀·√ε » tient ; la thèse « proportionnel à ε » est réfutée |
| | H_rac | H_lin | les trois thèses sont réfutées ; audit de symétrie avant toute lecture |
| D2, règle « rayon de variance » | H_lin | H_rac | la loi en σ₀·√ε est celle de l'écrêtage au rayon de variance là où ce rayon tient dans le support : deux régimes, pour cette règle |
| | H_lin | H_lin | la loi en σ₀·√ε n'apparaît nulle part sur ce dispositif : thèse réfutée, même pour sa propre règle |
| | H_rac | toute issue | contraire au calcul de population ; audit de symétrie |

Portée, à écrire dans tout compte rendu : ces lectures valent « en simulation, sous supposition », pour deux lois uniformes, un décalage diffus, un contaminant placé à la borne du support, la famille gelée de trois règles. Elles ne tranchent pas la frontière minimax.

**Audit de symétrie (R4).** Même audit pour un résultat trop bon et pour un résultat contraire. Il se déclenche si : une prédiction [preuve] est contraire ; le taux de l'artefact dépasse 0,90 (attendu 0,23 à 0,6) ; le taux de `connue_normale` à 16m est sous 0,001 (attendu 0,005 à 0,03 ; T0.3 rapporte 0,017 à son horizon) ; le taux moyen de `enveloppe` est nul dans une cellule où la chute est prédite ; une pente du duel sort de [0,3 ; 1,3] ; G1 ou G5 est contraire ; le duel D1 rend (H_rac ; H_lin). L'audit : moments du générateur contre leurs formes fermées ; équivalence avec la référence scalaire sur 200 trajectoires de la cellule ; réplication de la cellule. Il est rapporté avec le verdict.

## Liste d'arrêt

Chaque condition arrête le run par `GardeArret`, sans repli. Chaque garde est testée sur un cas sain et sur un artefact (R5) dans `tests/test_banc_detecteur_sequentiel.py`.
1. Préenregistrement non scellé, non conforme ou altéré (`prereg.exiger_prereg_scelle`).
2. Attestation du code absente, non scellée, ou qui ne cite pas le commit courant et l'empreinte de la grille ; arbre de travail non propre ; code importé hors de `src/` du dépôt.
3. Dossier de run existant (R12) ; toute sélection de blocs ou de cellules, en run principal comme en réplication.
4. Tâche à graine absente du manifeste ; graine reconstruite différente de la graine consignée ; entropie différente de celle de ce texte.
5. Grille du code différente des tables de ce texte (cellules, tailles, niveaux), vérifiée par l'empreinte citée à l'attestation.
6. **Garde du générateur**, avant tout bloc, sur 10⁶ tirages par loi : moyenne et écart type à 4 erreurs types de leur forme fermée ; autocorrélation latente de pas 1 à 0,005 de φ ; part de variance latente entre tâches à 0,01 de ω ; nombre de contaminés égal à k.
7. **Garde d'équivalence** : sur 200 trajectoires par construction, l'instant de première alerte vectorisé égale celui de la référence scalaire (`agregateurs.processus_e.trajectoire_e` et `premiere_alarme`).
8. **Contrôle de banc** (bloc A) non entièrement confirmé : arrêt avant les blocs B à H.
9. Valeur non finie ; score hors de [0 ; 1] (hors loi normale du contrôle) ; plafond égal au plancher ; rayon négatif ; paramètre hors domaine.
10. **Durée** cumulée au-delà de 6 heures d'horloge, contrôlée entre les cellules : arrêt, `arret.json`. Jamais de réduction des tailles en cours de run.

**Protocole après un arrêt.** Le diagnostic se fait sur le message d'arrêt et sur des données non décisives. Les fichiers de blocs déjà scellés ne sont pas ouverts avant la décision de la mère ; s'ils l'ont été, c'est déclaré. Toute correction du code, de la grille ou des tailles impose une version suivante de ce texte, contre-lue sur ses différences, avec le mot de la mère. Un arrêt de cause technique (perte de conteneur, mémoire) donne droit à une relance sur le même accord, à l'identique (règle « une panne technique n'est pas un résultat »).

## Contre-lecture

Section en attente : ce brouillon 1 n'a pas été contre-lu. La mère la complète après la contre-lecture par un sous-agent neuf Opus 5.5 (identifiant du contre-lecteur, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque), puis la vérification des corrections par le même contre-lecteur. Tant que ces deux empreintes n'y figurent pas, le validateur `controle_ia.prereg` refuse le scellement : c'est voulu.

Fichiers à donner explicitement au contre-lecteur (R2) : ce texte ; la consigne ; la note d'antériorité ; la note de sortie du collisionneur (sections « En bref », 5, 6, 8) ; N-076 et ses errata ; T0.3 (sections citées) ; les six modules de code cités en tête ; le programme de l'annexe A, à relancer.

## Interface du code d'analyse

Écrit après le scellement (classe B, contre-lu par un autre modèle). Paquet `src/controle_ia/banc_detecteur_sequentiel/`. Toute fonction lève `GardeArret` sur entrée non finie ou hors domaine.

- `generateur.py` (réemployable par le monde 4)
  - `quantile_loi(nom: str, u: ndarray) -> ndarray` ; noms : `beta14`, `normale`, `uniforme_etalee`, `uniforme_concentree`.
  - `tirer_latent(rng, forme: tuple[int, int], *, phi: float = 0.0, omega: float = 0.0, taille_tache: int = 1) -> ndarray`.
  - `scores(nom: str, latent: ndarray, derive: float = 0.0) -> ndarray`.
  - `contaminer(reference: ndarray, k: int, placement: str, rng) -> tuple[ndarray, ndarray]` (scores, masque des honnêtes) ; placements : `haut`, `seuil`, `bas`, `plafond`.
- `constructions.py`
  - `quantile_empirique(x_trie: ndarray, q: float) -> float`.
  - `rayon(m: int, eps_d: float, alpha_etalonnage: float) -> float`.
  - `noeuds(reference: ndarray, regle: str, *, r: float | None = None) -> tuple[float, float]` ; règles : `quantiles`, `support`, `rayon_variance`.
  - `gain(x: ndarray, a: float, c: float) -> ndarray`.
  - `borne_enveloppe(gains_reference: ndarray, r: float) -> float`.
  - `calibrer(reference: ndarray, construction: str, *, eps_d: float, alpha: float, alpha_etalonnage: float, regle: str = "quantiles", loi_connue: str | None = None, n0: int | None = None) -> dict` ; clés : `a`, `c`, `centre`, `echelle`, `seuil_log`, `rho`, `r`, `m`, `construction`.
  - `frontiere_somme(n_max: int, rho: float, seuil_log: float) -> ndarray` : pour t = 1 à n_max, la somme standardisée où le processus-e atteint le seuil.
  - `premieres_alertes(scores_deploiement: ndarray, cal: dict, frontiere: ndarray) -> ndarray` : indice de la première alerte par ligne, −1 si aucune.
- `bases.py` : `somme_fixe`, `somme_relue`, `page`, mêmes entrées, même sortie ; `seuil_page(nom_loi: str, n: int, alpha: float, rng, repetitions: int = 100_000) -> float`.
- `mesures.py` : `taux_par_horizon`, `resume_conditionnel`, `marge_exacte`, `hors_enveloppe`, `decalage_detectable`, `plancher_par_dichotomie`, `pente`, `lire_table_a`.
- `run_banc.py` : lanceur ; options `--prereg`, `--attestation`, `--replication-de` ; aucune option de sélection.
- `lecture.py` : lecture mécanique des tables A à C et des blocs G et H ; écrit `diag/<run_id>/lecture-mecanique.json`.
- Grille : `prereg/banc-detecteur-sequentiel-grille-v1.json`, écrite avec le code, égale aux tables de ce texte.
- **Attestation du code** : `prereg/banc-detecteur-sequentiel-reference-contaminee-v1-attestation-code-v1.md`, écrite par la mère après la contre-lecture du code et la vérification de ses corrections. Elle cite le commit du code, l'empreinte de la grille, l'empreinte de ce préenregistrement scellé, le rapport du contre-lecteur, et la liste des écarts du code au plan (vide, ou chaque écart traité comme un écart au préenregistrement). Scellée. Le lanceur la vérifie.

## Rattachements et règles

**Déclaration selon N-076, point 1.**
- Unité : l'épisode (la tâche dans les cellules à unité tâche). Scores tenus pour indépendants sous le nul à cette unité, sauf dans les blocs E et F, qui violent cette supposition à dessein.
- Taille de la référence : m ∈ {100 ; 400 ; 1 600} épisodes ; 20 ou 100 tâches à unité tâche ; 10⁶ dans le duel.
- Horizon : n ∈ {m/4 ; m ; 4m ; 16m}, 64m à m = 100 ; n = m dans le duel.
- Source de validité : **référence fixe de taille m**, seule. Aucune des trois autres n'est employée.
- Borne du biais toléré : distance de Kolmogorov unilatérale au plus ε_d entre la loi d'où sort la référence et la loi honnête du déploiement, contamination et dérive confondues.
- **Lectures au-delà de n = m.** Toute lecture de puissance ou de décalage détectable au-delà de n = m porte l'étiquette « au-delà de la référence » et ne fonde aucun verdict. Font exception, et c'est écrit ici : (i) les verdicts de **validité** de la construction à enveloppe et budget partagé, dont la garantie porte explicitement sur tout horizon ; (ii) le contrôle de banc, dont l'objet est le défaut de la construction naïve à n très supérieur à m, et qui juge le banc, non un gain d'accumulation.

**Délai de l'oracle.** Le banc suppose un score disponible à la fin de chaque épisode (délai h = 1). Tout délai h > 1 appelle la correction de délai (moyenne de h sous-produits et facteur e·log h sur le seuil ; Arnold, Henzi et Ziegel, arXiv 2109.11761 v3, [PDF, p. 7-8], d'après l'erratum 3 de N-076 ; je n'ai pas rouvert le PDF). Hors du banc.

**Prévision de la loi de la référence honnête.** Le banc ne tranche aucun nœud du brouillon de cette prévision et ne la remplace pas. Il peut lui servir d'objet de contrôle sur monde planté, sans plus.

**Règle de diffusion** (décision de la mère). Aucune sortie du banc (seuils, tables, verdicts) n'est servie à l'organisme d'idéation ni à la session qui le sert (`session_01Qi7Gr36UCZKS2Fw574dmcW`), jusqu'à la conception du banc des mondes plantés, après le 1er décembre. Le dossier du collisionneur, déjà servi, n'est pas touché.

**Phrases à ne pas écrire**, dans ce texte et dans tout compte rendu du banc : « le rappel croît avec l'horizon » sans m ni source de validité ; « garantie toujours valide » d'une construction étalonnée sans dire « conditionnelle à la référence » ou « en moyenne sur la référence » ; « seuil robuste » sans le modèle de contamination (fraction, nombre, placement) contre lequel il l'est ; tout chiffre du banc sans « en simulation, sous supposition » ; « la loi de la référence honnête est un résultat du programme » ; toute nouveauté sur le nul par acte ; tout produit d'e-valeurs sous verdict différé sans correction de délai.

**Citations.** Aucun chiffre publié n'est cité. Énoncés classiques employés, non vérifiés sur PDF dans cette session, à vérifier (R7) : inégalité de Dvoretzky-Kiefer-Wolfowitz à constante de Massart ; inégalité de Ville ; lemme de Hoeffding. Le banc contrôle les deux premiers par la mesure (B3, A-sain). Voisins à citer dans tout compte rendu, d'après N-076 : Podkopaev et Ramdas (référence fixe tenue à part) ; Ortega-Fernandez et al. ; Arnold, Henzi et Ziegel ; Singh. La prédiction conforme robuste à une fraction contaminée de l'étalonnage n'a pas été cherchée : à faire avant toute phrase sur l'enveloppe.

## Points pour la mère

1. **Lecture de « somme cumulée écrêtée au même rayon ».** Je n'avais pas la section 3 de la note de sortie. Retenu : « écrêtée » = gain borné entre un plancher et un plafond ; « même rayon » = même bande r, même gain, même référence ; trois lectures de la somme (horizon fixe, relue, Page étalonnée). Autre lecture possible : somme de scores rognés au rayon de variance. Recommandation : garder. Confiance 0,7.
2. **Lecture de « contamination basse ».** Deux sens couverts : fraction réelle inférieure à la déclarée (couple (0,10 ; 0,02) et référence propre) et placement bas (score minimal). Recommandation : garder les deux. Confiance 0,8.
3. **Les deux régimes du duel.** Reconstruits par dérivation, non lus chez Neon. Le duel principal D1 porte sur la meilleure règle de la famille ; le calcul prédit une pente linéaire dans les deux régimes, donc la réfutation de « σ₀·√ε » comme pente de la frontière, cette loi ne restant vraie que pour l'écrêtage au rayon de variance (D2). Options : (a) D1 principal et D2 d'accompagnement ; (b) D2 seul, plus proche de la lettre « deux régimes » mais dont la pente est fixée par la règle d'écrêtage ; (c) ajouter un sabotage rare et lointain, plus proche d'une frontière au pire, au prix d'un bloc de plus. Recommandation : (a). Confiance 0,65.
4. **Le duel est décidé par l'algèbre.** Sous ses suppositions, sa réponse est calculable (annexe A, bloc 7). Le banc apporte la première reprise des deux calculs que personne n'avait refaits et leur tenue à taille finie, non une découverte. À dire tel quel à Lazar. Confiance 0,85.
5. **Niveau et partage.** α = 0,05 partagé par moitiés. N-076 parle de 1 % : à ce niveau il faudrait cinq fois plus de tirages et le rayon passerait de 0,074 à 0,084 à m = 400. Recommandation : 0,05 ici. Confiance 0,7.
6. **Processus-e de mélange normal à échelle de Hoeffding**, repris du dépôt, plutôt qu'un processus par paris. Plus simple, garanti, mais prudent : le prix mesuré en G5 en dépend. Recommandation : garder, variante par paris dans une version suivante si le prix pèse. Confiance 0,7.
7. **Résultat de principe qui pèse sur le programme.** À m = 400, la marge de l'enveloppe est de 0,07 à 0,18 sur un gain borné par 1 : elle ne verrait qu'un déplacement de Kolmogorov de 0,12 à 0,2. Si le banc le confirme, l'enveloppe tient mais ne sert qu'à grande référence ; à unité tâche et 20 tâches, le rayon vaut 0,36. Pas une décision : à savoir avant de lire.
8. **Contrôle d'artefact décisif sur la loi normale seulement**, où la borne est exacte ; sur Bêta(1 ; 4) il est informatif. Recommandation : garder. Confiance 0,75.
9. **Contamination à nombre fixe.** Sous un tirage par épisode, la fraction déclarée devrait borner le nombre réalisé, avec une marge binomiale. Hors du banc ; à écrire dans tout usage.
10. **Pièce de procédure neuve** : l'attestation du code, qui lie le texte scellé au code écrit après. Autre voie : sceller une version 2 de ce texte citant le commit, comme T0.3. Recommandation : l'attestation. Confiance 0,6.
11. **PDF manquants** (R7) : Massart 1990 pour la constante ; la forme unilatérale réduirait le rayon de 8 % mais demande sa condition de validité, non vérifiée.
12. **Lois synthétiques.** m = 400, Bêta(1 ; 4), 20 tâches : choisis sans aucun chiffre du dépôt. Si la mère connaît les tailles réelles des références du programme, les substituer avant scellement.

## Confiance, et ce que je n'ai pas fait

- **Confiance.** Preuve de É2 : 0,85 (trois pas classiques ; non contre-lue ; le pas (b) pour un gain choisi sur la référence est le plus à vérifier). Borne du contrôle d'artefact : 0,9. Marges de population des blocs B à D : 0,8 (elles ignorent la dispersion de la référence, d'écart type 0,018 à m = 400). Prédictions E2 et F2 : 0,6. Pentes du duel : 0,8 sur le signe par rapport à 0,75 ; 0,6 sur les valeurs. Temps de calcul : 0,6.
- **Temps de calcul estimé** : environ trois heures et demie de cœur, soit une à deux heures d'horloge sur quatre cœurs (annexe B : 36 à 55 milliardièmes de seconde par score et par construction ; 48 cellules emboîtées, de 1,6 à 6,4 milliards de scores chacune ; duel : 1 600 répétitions d'environ une seconde). Plafond : 6 heures.
- **Non fait.** Aucun code d'analyse ; aucune simulation de la grille ; aucun commit. Rien ouvert sous `coffre/`, `docs/verdicts/`, `diag/`, `runs/`, `donnees/`, `registres/`. Section 3 de la note de sortie non lue (hors de ma liste) : les constructions des trois modèles me sont connues par leur résumé seulement. Aucun PDF ouvert. Aucune recherche d'antériorité. La preuve de É2 n'est pas rédigée en forme. Le calcul exact du taux de la naïve sous arrêt optionnel (premier passage) n'est pas fait : seule sa borne inférieure à l'instant n l'est. Le seuil de la somme de Page n'est pas calculé. Les prédictions des blocs E et F reposent sur des ordres de grandeur à la main.
- **Tirages déclarés.** Un seul programme a tiré au hasard : le chronométrage de l'annexe B (primitives numpy, frontière factice, aucune statistique du banc calculée ni lue, aucune cellule de la grille).

## Annexe A — programme des calculs de principe et sa sortie

Fichier de travail hors dépôt : `dimensionnement_banc_detecteur_sequentiel_v1.py`, empreinte `5133f26a772b52880503a98a46d1a555505c6891b68dc5cc1c7ab431504c961a` ; sortie `601dd07acb74d6142ea14ce69625d68adb23ff7f7a6c395a65e8ddc0f449c5c7`. numpy 2.5.3, Python de la session. Aucun tirage au hasard. À verser au dépôt par la mère avec ce texte.

### A.1 Programme

```python
"""Calculs de principe, sous supposition, pour dimensionner le banc de validité du détecteur séquentiel
(préenregistrement prereg/banc-detecteur-sequentiel-reference-contaminee-v1.md, annexe A).

Aucun tirage au hasard : formes fermées, lois normales exactes, quadratures sur grilles déterministes.
Dépendances : numpy et la bibliothèque standard (statistics.NormalDist). Aucune cellule de la grille n'est simulée.
"""
from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
ALPHA, A_CAL, A_ARRET = 0.05, 0.025, 0.025


# ---------- processus e unilatéral de mélange normal (mêmes formules que agregateurs/processus_e.py, σ = 1)
def log_e_unilateral(S: float, n: float, rho: float) -> float:
    a = 1.0 + rho * rho * n
    x = rho * S / math.sqrt(a)
    return math.log(2.0) - 0.5 * math.log(a) + rho * rho * S * S / (2.0 * a) + math.log(max(N01.cdf(x), 1e-300))


def frontiere(n: float, rho: float, alpha: float) -> float:
    """s* > 0 tel que log E_n(s*) = log(1/alpha) ; dichotomie."""
    h, lo, hi = math.log(1.0 / alpha), 0.0, 50.0 * math.sqrt(n) + 50.0
    for _ in range(200):
        mi = 0.5 * (lo + hi)
        if log_e_unilateral(mi, n, rho) < h:
            lo = mi
        else:
            hi = mi
    return 0.5 * (lo + hi)


def rho_optimal(n0: int, alpha: float) -> float:
    """ρ minimisant la frontière à l'horizon n0 (section dorée sur log ρ, bornes 1e-3 et 10)."""
    g = (math.sqrt(5.0) - 1.0) / 2.0
    lo, hi = math.log(1e-3), math.log(10.0)
    c, d = hi - g * (hi - lo), lo + g * (hi - lo)
    fc, fd = frontiere(n0, math.exp(c), alpha), frontiere(n0, math.exp(d), alpha)
    for _ in range(120):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - g * (hi - lo)
            fc = frontiere(n0, math.exp(c), alpha)
        else:
            lo, c, fc = c, d, fd
            d = lo + g * (hi - lo)
            fd = frontiere(n0, math.exp(d), alpha)
    return math.exp(0.5 * (lo + hi))


def rayon_dkw(m: int, eps_d: float, a_cal: float = A_CAL) -> float:
    """Rayon total : fraction déclarée + rayon bilatéral de Dvoretzky-Kiefer-Wolfowitz sur ⌊(1 − ε)m⌋ honnêtes."""
    mh = math.floor((1.0 - eps_d) * m + 1e-9)
    return eps_d + math.sqrt(math.log(2.0 / a_cal) / (2.0 * mh))


print("=== 1. Rayons (alpha_etalonnage = 0,025 ; forme bilatérale, constante 2)")
for m in (32, 100, 400, 1600, 6400, 1_000_000):
    print(f"  m = {m:>7} : " + " | ".join(f"eps_d = {e:.2f} : r = {rayon_dkw(m, e):.4f}" for e in (0.0, 0.02, 0.05, 0.10)))

print("=== 2. Contrôle de banc : construction naïve, loi normale, centre estimé sur m (échelle supposée connue)")
print("    borne inférieure exacte du taux de fausses alertes : P(E_n >= 1/alpha) à l'instant n seul,")
print("    S_n ~ N(0, n(1 + n/m)) en moyenne sur la référence ; bien spécifiée : S_n ~ N(0, n)")
for m in (100, 400):
    rho = rho_optimal(m, ALPHA)
    print(f"  m = {m}, rho*(m, alpha = 0,05) = {rho:.5f}")
    for k in (0.25, 1, 4, 16, 64):
        n = int(k * m)
        s = frontiere(n, rho, ALPHA)
        naive = 1.0 - N01.cdf(s / math.sqrt(n * (1.0 + n / m)))
        sain = 1.0 - N01.cdf(s / math.sqrt(n))
        # part des références où le taux conditionnel terminal dépasse 2 alpha : P(Phi_bar((s - n d)/sqrt n) > 0.10), d ~ N(0, 1/m)
        d_crit = (s - math.sqrt(n) * N01.inv_cdf(1.0 - 2 * ALPHA)) / n
        part = 1.0 - N01.cdf(d_crit * math.sqrt(m))
        print(f"    n/m = {k:>5} (n = {n:>5}) : frontière s* = {s:8.2f} ; naïve >= {naive:.4f} ; bien spécifiée (instant n) = {sain:.5f} ;"
              f" part des références à taux conditionnel terminal > 2 alpha = {part:.4f}")

# ---------- loi honnête principale : Beta(1, 4), Q(u) = 1 − (1 − u)^(1/4)
U = (np.arange(2_000_000) + 0.5) / 2_000_000   # grille déterministe de quadrature sur ]0, 1[


def q_beta14(u):
    return 1.0 - (1.0 - u) ** 0.25


def phi_inv(u):
    return np.array([N01.inv_cdf(float(x)) for x in u])


def gain(x, a, c):
    return np.clip((x - a) / (c - a), 0.0, 1.0)


def borne_enveloppe(valeurs_g_triees: np.ndarray, r: float) -> float:
    """Moyenne de g après déplacement de la masse r la plus basse vers 1 (grille uniforme de masses égales)."""
    k = r * valeurs_g_triees.size
    kf = int(math.floor(k))
    bas = valeurs_g_triees[:kf].sum() + (k - kf) * valeurs_g_triees[min(kf, valeurs_g_triees.size - 1)]
    return float((valeurs_g_triees.sum() - bas) / valeurs_g_triees.size + r)


X_H = q_beta14(U)                      # population honnête (triée)
A0, C0 = q_beta14(0.50), q_beta14(0.90)
G_H = gain(X_H, A0, C0)
MU_G, SD_G = float(G_H.mean()), float(G_H.std())
print("=== 3. Loi honnête Beta(1, 4) ; gain écrêté entre les quantiles 0,50 et 0,90")
print(f"  a = {A0:.4f}, c = {C0:.4f} ; moyenne du gain = {MU_G:.4f} ; écart type du gain = {SD_G:.4f} ; moyenne du score = {X_H.mean():.4f}")

# décalage diffus sur l'échelle latente : X = Q(Phi(Phi^-1(U) + d))
UG = (np.arange(200_000) + 0.5) / 200_000
ZG = phi_inv(UG)
PHI = np.vectorize(N01.cdf)
print("  décalage diffus latent d -> hausse de la moyenne du gain (a, c de la population honnête) ; distance de Kolmogorov")
for d in (0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00):
    xs = q_beta14(np.clip(PHI(ZG + d), 0.0, 1.0 - 1e-16))
    ks = float(np.max(np.abs(PHI(ZG + d) - UG)))
    print(f"    d = {d:.2f} : hausse = {gain(xs, A0, C0).mean() - gain(q_beta14(UG), A0, C0).mean():.4f} ; Kolmogorov = {ks:.4f}")

print("=== 4. Marge de population de l'enveloppe : borne − moyenne honnête du gain (référence contaminée infinie + rayon de m)")
print("    marge > 0 : dérive négative, tenue attendue ; marge < 0 : dérive positive, chute attendue aux longs horizons")


def reference_contaminee(eps: float, placement: str) -> np.ndarray:
    """Population de référence triée : mélange (1 − eps) honnête + eps contaminant, par grille de masses égales."""
    if eps == 0.0:
        return X_H
    n_c = int(round(eps * X_H.size / (1.0 - eps)))
    uc = (np.arange(n_c) + 0.5) / n_c
    if placement == "haut":            # sabotage visible : Beta(4, 1), Q(u) = u^(1/4)
        xc = uc ** 0.25
    elif placement == "seuil":         # dans la queue qui fixe le plafond : uniforme entre les quantiles honnêtes 0,90 et 0,97
        xc = q_beta14(0.90) + uc * (q_beta14(0.97) - q_beta14(0.90))
    elif placement == "bas":           # score minimal
        xc = np.zeros(n_c)
    else:
        raise ValueError(placement)
    return np.sort(np.concatenate([X_H, xc]))


for m in (400, 1600):
    for eps_d in (0.02, 0.10):
        r = rayon_dkw(m, eps_d)
        for eps in (0.0, eps_d, 2 * eps_d):
            for pl in (("-",) if eps == 0.0 else ("haut", "seuil", "bas")):
                ref = reference_contaminee(eps, pl if pl != "-" else "haut")
                a, c = np.quantile(ref, 0.50), np.quantile(ref, 0.90)
                borne = borne_enveloppe(np.sort(gain(ref, a, c)), r)
                vrai = float(gain(X_H, a, c).mean())
                naive = float(gain(ref, a, c).mean())
                # horizon où la dérive positive atteint la frontière (échelle de Hoeffding 1/2), si marge < 0
                marge = borne - vrai
                print(f"  m = {m:>4} eps_d = {eps_d:.2f} r = {r:.4f} eps_réel = {eps:.2f} placement = {pl:<5} :"
                      f" marge enveloppe = {marge:+.4f} ; marge naïve (rayon nul) = {naive - vrai:+.4f} ; a = {a:.3f} c = {c:.3f}")

print("=== 4 bis. Rognage haut naïf (retirer la fraction eps_d la plus haute de la référence, rayon nul) : marge de population")
for eps_d, reels in ((0.02, (0.0, 0.02, 0.04)), (0.10, (0.0, 0.02, 0.10, 0.20))):
    for eps in reels:
        for pl in (("-",) if eps == 0.0 else ("haut", "seuil", "bas")):
            ref = reference_contaminee(eps, pl if pl != "-" else "haut")
            garde = ref[: int(round((1.0 - eps_d) * ref.size))]
            a, c = np.quantile(garde, 0.50), np.quantile(garde, 0.90)
            marge = gain(garde, a, c).mean() - gain(X_H, a, c).mean()
            et = float(gain(garde, a, c).std())
            print(f"  eps_d = {eps_d:.2f} eps_réel = {eps:.2f} placement = {pl:<5} : marge = {marge:+.4f} ; écart type du gain rogné = {et:.3f} ;"
                  f" dérive standardisée × 400 = {-marge / et * 400:+.1f} (frontière à n = 400, alpha = 0,05 : 55,3)")
print("=== 4 quater. Construction naïve sous contamination : dérive standardisée cumulée à n = m = 400 et à 4m (frontières 55,3 et 114,8)")
for eps, pl in ((0.02, "bas"), (0.04, "bas"), (0.10, "bas"), (0.20, "bas")):
    ref = reference_contaminee(eps, pl)
    a, c = np.quantile(ref, 0.50), np.quantile(ref, 0.90)
    marge = gain(ref, a, c).mean() - gain(X_H, a, c).mean()
    et = float(gain(ref, a, c).std())
    print(f"  eps_réel = {eps:.2f} placement bas : marge = {marge:+.4f} ; à n = 400 : {-marge / et * 400:+.1f} ; à n = 1600 : {-marge / et * 1600:+.1f}")
print("=== 4 quinquies. Vivacité : sabotage massif (décalage latent 2) contre la plus grande marge de l'enveloppe (m = 100, eps_d = 0,10)")
xs = q_beta14(np.clip(PHI(ZG + 2.0), 0.0, 1.0 - 1e-16))
hausse = gain(xs, A0, C0).mean() - MU_G
r_max = rayon_dkw(100, 0.10)
rho_v = rho_optimal(100, A_ARRET)
print(f"  hausse du gain = {hausse:.4f} ; rayon maximal = {r_max:.4f} ; dérive nette × n / 0,5 à n = 100 : {(hausse - r_max) * 100 / 0.5:.1f} ; frontière à n = 100 : {frontiere(100, rho_v, A_ARRET):.1f}")

print("=== 4 ter. Dérive bénigne latente d du déploiement (référence propre) : marge de l'enveloppe")
for m in (400, 1600):
    for eps_d in (0.02, 0.10):
        r = rayon_dkw(m, eps_d)
        borne = borne_enveloppe(np.sort(G_H), r)
        for d in (0.05, 0.10, 0.20, 0.40, 0.80):
            xs = q_beta14(np.clip(PHI(ZG + d), 0.0, 1.0 - 1e-16))
            print(f"  m = {m:>4} eps_d = {eps_d:.2f} r = {r:.4f} d = {d:.2f} : marge = {borne - gain(xs, A0, C0).mean():+.4f}")

print("=== 5. Horizon de chute sous dérive positive : plus petit n tel que n × dérive >= frontière (échelle 1/2, alpha_arrêt = 0,025, rho*(400))")
RHO_E = rho_optimal(400, A_ARRET)
print(f"  rho*(400 ; 0,025) = {RHO_E:.5f}")
for derive in (0.005, 0.01, 0.02, 0.03, 0.05):
    n = 10
    while n * derive / 0.5 < frontiere(n, RHO_E, A_ARRET) and n < 10_000_000:
        n = int(n * 1.02) + 1
    print(f"  dérive du gain = {derive:.3f} par épisode : n ≈ {n}")

print("=== 6. Prix de la garantie : décalage standardisé détecté à puissance un demi (médiane de S_n à la frontière), loi connue")
for (m, alpha) in ((400, A_ARRET), (400, ALPHA)):
    rho = rho_optimal(m, alpha)
    z = N01.inv_cdf(1.0 - alpha)
    for n in (100, 400, 1600, 6400):
        s = frontiere(n, rho, alpha)
        print(f"  alpha = {alpha:.3f} rho*({m}) n = {n:>5} : processus e (instant n) = {s / n:.4f} ; somme à horizon fixe = {z / math.sqrt(n):.4f} ; rapport = {s / (z * math.sqrt(n)):.2f}")

print("=== 7. Duel sur la pente : planchers de population (décalage additif diffus), référence contaminée au plafond du support")


def plancher(loi: str, eps: float, r: float, regle: str) -> float:
    """Plus petit décalage additif D tel que E g(X + D) >= borne de l'enveloppe (population ; contamination réelle eps placée à 1)."""
    if loi == "etale":
        xh = UG.copy()
    else:
        xh = 0.2 + 0.02 * math.sqrt(3.0) * (2.0 * UG - 1.0)
    n_c = int(round(eps * xh.size / (1.0 - eps)))
    ref = np.sort(np.concatenate([xh, np.ones(n_c)]))
    med = float(np.quantile(ref, 0.5))
    s0 = float((np.quantile(ref, 0.75) - np.quantile(ref, 0.25)) / 1.349)
    if regle == "variance":
        a, c = max(0.0, med - s0 / math.sqrt(r)), min(1.0, med + s0 / math.sqrt(r))
    elif regle == "support":
        a, c = 0.0, 1.0
    else:                               # quantiles de la référence
        a, c = float(np.quantile(ref, 0.50)), float(np.quantile(ref, 0.90))
    borne = borne_enveloppe(np.sort(gain(ref, a, c)), r)
    lo, hi = 0.0, 1.0
    if gain(np.minimum(xh + hi, 1.0), a, c).mean() < borne:
        return float("nan")
    for _ in range(60):
        mi = 0.5 * (lo + hi)
        if gain(np.minimum(xh + mi, 1.0), a, c).mean() < borne:
            lo = mi
        else:
            hi = mi
    return hi


EPS = (0.01, 0.02, 0.04, 0.08)
M_DUEL = 1_000_000
for loi, s0_vrai, portee in (("etale", 1.0 / math.sqrt(12.0), 0.5), ("concentre", 0.02, 0.8)):
    print(f"  loi {loi} : écart type {s0_vrai:.4f}, portée au plafond {portee:.2f}, bascule (sigma0/portée)^2 = {(s0_vrai / portee) ** 2:.5f}")
    for regle in ("variance", "support", "quantiles"):
        rs = [rayon_dkw(M_DUEL, e) for e in EPS]
        pl = [plancher(loi, e, r, regle) for e, r in zip(EPS, rs)]
        pente = np.polyfit(np.log(rs), np.log(pl), 1)[0]
        pente_bas = math.log(pl[1] / pl[0]) / math.log(rs[1] / rs[0])
        pente_haut = math.log(pl[3] / pl[2]) / math.log(rs[3] / rs[2])
        print(f"    règle {regle:<9} : planchers = " + ", ".join(f"{p:.5f}" for p in pl)
              + f" ; pente = {pente:.3f} (bas {pente_bas:.3f}, haut {pente_haut:.3f})"
              + " ; rapports à sigma0·racine(r) = " + ", ".join(f"{p / (s0_vrai * math.sqrt(r)):.2f}" for p, r in zip(pl, rs))
              + " ; rapports à r = " + ", ".join(f"{p / r:.2f}" for p, r in zip(pl, rs)))
    # terme séquentiel à n = 10^6 (frontière / n, échelle de Hoeffding 1/2 sur le gain, ramenée à l'échelle du score)
rho_d = rho_optimal(M_DUEL, A_ARRET)
s_d = frontiere(M_DUEL, rho_d, A_ARRET)
print(f"  terme séquentiel à n = 10^6 : frontière/n = {s_d / M_DUEL:.6f} en unités de Hoeffding, soit {0.5 * s_d / M_DUEL:.6f} sur le gain")
```

### A.2 Sortie (verbatim)

```text
=== 1. Rayons (alpha_etalonnage = 0,025 ; forme bilatérale, constante 2)
  m =      32 : eps_d = 0.00 : r = 0.2617 | eps_d = 0.02 : r = 0.2859 | eps_d = 0.05 : r = 0.3202 | eps_d = 0.10 : r = 0.3797
  m =     100 : eps_d = 0.00 : r = 0.1480 | eps_d = 0.02 : r = 0.1695 | eps_d = 0.05 : r = 0.2019 | eps_d = 0.10 : r = 0.2560
  m =     400 : eps_d = 0.00 : r = 0.0740 | eps_d = 0.02 : r = 0.0948 | eps_d = 0.05 : r = 0.1259 | eps_d = 0.10 : r = 0.1780
  m =    1600 : eps_d = 0.00 : r = 0.0370 | eps_d = 0.02 : r = 0.0574 | eps_d = 0.05 : r = 0.0880 | eps_d = 0.10 : r = 0.1390
  m =    6400 : eps_d = 0.00 : r = 0.0185 | eps_d = 0.02 : r = 0.0387 | eps_d = 0.05 : r = 0.0690 | eps_d = 0.10 : r = 0.1195
  m = 1000000 : eps_d = 0.00 : r = 0.0015 | eps_d = 0.02 : r = 0.0215 | eps_d = 0.05 : r = 0.0515 | eps_d = 0.10 : r = 0.1016
=== 2. Contrôle de banc : construction naïve, loi normale, centre estimé sur m (échelle supposée connue)
    borne inférieure exacte du taux de fausses alertes : P(E_n >= 1/alpha) à l'instant n seul,
    S_n ~ N(0, n(1 + n/m)) en moyenne sur la référence ; bien spécifiée : S_n ~ N(0, n)
  m = 100, rho*(m, alpha = 0,05) = 0.25870
    n/m =  0.25 (n =    25) : frontière s* =    14.96 ; naïve >= 0.0037 ; bien spécifiée (instant n) = 0.00138 ; part des références à taux conditionnel terminal > 2 alpha = 0.0003
    n/m =     1 (n =   100) : frontière s* =    27.66 ; naïve >= 0.0252 ; bien spécifiée (instant n) = 0.00284 ; part des références à taux conditionnel terminal > 2 alpha = 0.0689
    n/m =     4 (n =   400) : frontière s* =    57.38 ; naïve >= 0.0997 ; bien spécifiée (instant n) = 0.00206 ; part des références à taux conditionnel terminal > 2 alpha = 0.2137
    n/m =    16 (n =  1600) : frontière s* =   122.49 ; naïve >= 0.2288 ; bien spécifiée (instant n) = 0.00110 ; part des références à taux conditionnel terminal > 2 alpha = 0.3281
    n/m =    64 (n =  6400) : frontière s* =   261.61 ; naïve >= 0.3425 ; bien spécifiée (instant n) = 0.00054 ; part des références à taux conditionnel terminal > 2 alpha = 0.4018
  m = 400, rho*(m, alpha = 0,05) = 0.12935
    n/m =  0.25 (n =   100) : frontière s* =    29.93 ; naïve >= 0.0037 ; bien spécifiée (instant n) = 0.00138 ; part des références à taux conditionnel terminal > 2 alpha = 0.0003
    n/m =     1 (n =   400) : frontière s* =    55.32 ; naïve >= 0.0252 ; bien spécifiée (instant n) = 0.00284 ; part des références à taux conditionnel terminal > 2 alpha = 0.0689
    n/m =     4 (n =  1600) : frontière s* =   114.75 ; naïve >= 0.0997 ; bien spécifiée (instant n) = 0.00206 ; part des références à taux conditionnel terminal > 2 alpha = 0.2137
    n/m =    16 (n =  6400) : frontière s* =   244.98 ; naïve >= 0.2288 ; bien spécifiée (instant n) = 0.00110 ; part des références à taux conditionnel terminal > 2 alpha = 0.3281
    n/m =    64 (n = 25600) : frontière s* =   523.21 ; naïve >= 0.3425 ; bien spécifiée (instant n) = 0.00054 ; part des références à taux conditionnel terminal > 2 alpha = 0.4018
=== 3. Loi honnête Beta(1, 4) ; gain écrêté entre les quantiles 0,50 et 0,90
  a = 0.1591, c = 0.4377 ; moyenne du gain = 0.2615 ; écart type du gain = 0.3570 ; moyenne du score = 0.2000
  décalage diffus latent d -> hausse de la moyenne du gain (a, c de la population honnête) ; distance de Kolmogorov
    d = 0.05 : hausse = 0.0155 ; Kolmogorov = 0.0199
    d = 0.10 : hausse = 0.0314 ; Kolmogorov = 0.0399
    d = 0.15 : hausse = 0.0477 ; Kolmogorov = 0.0598
    d = 0.20 : hausse = 0.0644 ; Kolmogorov = 0.0797
    d = 0.30 : hausse = 0.0988 ; Kolmogorov = 0.1192
    d = 0.40 : hausse = 0.1344 ; Kolmogorov = 0.1585
    d = 0.50 : hausse = 0.1709 ; Kolmogorov = 0.1974
    d = 0.75 : hausse = 0.2641 ; Kolmogorov = 0.2923
    d = 1.00 : hausse = 0.3559 ; Kolmogorov = 0.3829
=== 4. Marge de population de l'enveloppe : borne − moyenne honnête du gain (référence contaminée infinie + rayon de m)
    marge > 0 : dérive négative, tenue attendue ; marge < 0 : dérive positive, chute attendue aux longs horizons
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.00 placement = -     : marge enveloppe = +0.0948 ; marge naïve (rayon nul) = +0.0000 ; a = 0.159 c = 0.438
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.02 placement = haut  : marge enveloppe = +0.1096 ; marge naïve (rayon nul) = +0.0149 ; a = 0.163 c = 0.464
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.02 placement = seuil : marge enveloppe = +0.1097 ; marge naïve (rayon nul) = +0.0150 ; a = 0.163 c = 0.460
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.02 placement = bas   : marge enveloppe = +0.0894 ; marge naïve (rayon nul) = -0.0053 ; a = 0.155 c = 0.435
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.04 placement = haut  : marge enveloppe = +0.1251 ; marge naïve (rayon nul) = +0.0303 ; a = 0.168 c = 0.495
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.04 placement = seuil : marge enveloppe = +0.1248 ; marge naïve (rayon nul) = +0.0300 ; a = 0.168 c = 0.478
  m =  400 eps_d = 0.02 r = 0.0948 eps_réel = 0.04 placement = bas   : marge enveloppe = +0.0839 ; marge naïve (rayon nul) = -0.0109 ; a = 0.150 c = 0.432
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.00 placement = -     : marge enveloppe = +0.1780 ; marge naïve (rayon nul) = +0.0000 ; a = 0.159 c = 0.438
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.10 placement = haut  : marge enveloppe = +0.2577 ; marge naïve (rayon nul) = +0.0796 ; a = 0.183 c = 0.634
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.10 placement = seuil : marge enveloppe = +0.2518 ; marge naïve (rayon nul) = +0.0738 ; a = 0.184 c = 0.512
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.10 placement = bas   : marge enveloppe = +0.1490 ; marge naïve (rayon nul) = -0.0291 ; a = 0.137 c = 0.423
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.20 placement = haut  : marge enveloppe = +0.3321 ; marge naïve (rayon nul) = +0.1541 ; a = 0.217 c = 0.842
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.20 placement = seuil : marge enveloppe = +0.3227 ; marge naïve (rayon nul) = +0.1447 ; a = 0.217 c = 0.537
  m =  400 eps_d = 0.10 r = 0.1780 eps_réel = 0.20 placement = bas   : marge enveloppe = +0.1126 ; marge naïve (rayon nul) = -0.0654 ; a = 0.111 c = 0.405
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.00 placement = -     : marge enveloppe = +0.0574 ; marge naïve (rayon nul) = +0.0000 ; a = 0.159 c = 0.438
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.02 placement = haut  : marge enveloppe = +0.0722 ; marge naïve (rayon nul) = +0.0149 ; a = 0.163 c = 0.464
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.02 placement = seuil : marge enveloppe = +0.0724 ; marge naïve (rayon nul) = +0.0150 ; a = 0.163 c = 0.460
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.02 placement = bas   : marge enveloppe = +0.0520 ; marge naïve (rayon nul) = -0.0053 ; a = 0.155 c = 0.435
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.04 placement = haut  : marge enveloppe = +0.0877 ; marge naïve (rayon nul) = +0.0303 ; a = 0.168 c = 0.495
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.04 placement = seuil : marge enveloppe = +0.0874 ; marge naïve (rayon nul) = +0.0300 ; a = 0.168 c = 0.478
  m = 1600 eps_d = 0.02 r = 0.0574 eps_réel = 0.04 placement = bas   : marge enveloppe = +0.0465 ; marge naïve (rayon nul) = -0.0109 ; a = 0.150 c = 0.432
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.00 placement = -     : marge enveloppe = +0.1390 ; marge naïve (rayon nul) = +0.0000 ; a = 0.159 c = 0.438
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.10 placement = haut  : marge enveloppe = +0.2186 ; marge naïve (rayon nul) = +0.0796 ; a = 0.183 c = 0.634
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.10 placement = seuil : marge enveloppe = +0.2128 ; marge naïve (rayon nul) = +0.0738 ; a = 0.184 c = 0.512
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.10 placement = bas   : marge enveloppe = +0.1100 ; marge naïve (rayon nul) = -0.0291 ; a = 0.137 c = 0.423
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.20 placement = haut  : marge enveloppe = +0.2931 ; marge naïve (rayon nul) = +0.1541 ; a = 0.217 c = 0.842
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.20 placement = seuil : marge enveloppe = +0.2837 ; marge naïve (rayon nul) = +0.1447 ; a = 0.217 c = 0.537
  m = 1600 eps_d = 0.10 r = 0.1390 eps_réel = 0.20 placement = bas   : marge enveloppe = +0.0736 ; marge naïve (rayon nul) = -0.0654 ; a = 0.111 c = 0.405
=== 4 bis. Rognage haut naïf (retirer la fraction eps_d la plus haute de la référence, rayon nul) : marge de population
  eps_d = 0.02 eps_réel = 0.00 placement = -     : marge = -0.0147 ; écart type du gain rogné = 0.359 ; dérive standardisée × 400 = +16.4 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.02 placement = haut  : marge = -0.0002 ; écart type du gain rogné = 0.357 ; dérive standardisée × 400 = +0.3 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.02 placement = seuil : marge = +0.0000 ; écart type du gain rogné = 0.357 ; dérive standardisée × 400 = -0.0 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.02 placement = bas   : marge = -0.0204 ; écart type du gain rogné = 0.359 ; dérive standardisée × 400 = +22.7 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.04 placement = haut  : marge = +0.0149 ; écart type du gain rogné = 0.355 ; dérive standardisée × 400 = -16.7 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.04 placement = seuil : marge = +0.0152 ; écart type du gain rogné = 0.359 ; dérive standardisée × 400 = -16.9 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.02 eps_réel = 0.04 placement = bas   : marge = -0.0263 ; écart type du gain rogné = 0.359 ; dérive standardisée × 400 = +29.4 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.00 placement = -     : marge = -0.0726 ; écart type du gain rogné = 0.364 ; dérive standardisée × 400 = +79.7 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.02 placement = haut  : marge = -0.0595 ; écart type du gain rogné = 0.363 ; dérive standardisée × 400 = +65.5 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.02 placement = seuil : marge = -0.0594 ; écart type du gain rogné = 0.363 ; dérive standardisée × 400 = +65.4 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.02 placement = bas   : marge = -0.0797 ; écart type du gain rogné = 0.364 ; dérive standardisée × 400 = +87.5 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.10 placement = haut  : marge = -0.0012 ; écart type du gain rogné = 0.358 ; dérive standardisée × 400 = +1.4 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.10 placement = seuil : marge = +0.0000 ; écart type du gain rogné = 0.357 ; dérive standardisée × 400 = -0.0 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.10 placement = bas   : marge = -0.1111 ; écart type du gain rogné = 0.364 ; dérive standardisée × 400 = +122.0 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.20 placement = haut  : marge = +0.0840 ; écart type du gain rogné = 0.350 ; dérive standardisée × 400 = -96.0 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.20 placement = seuil : marge = +0.0814 ; écart type du gain rogné = 0.387 ; dérive standardisée × 400 = -84.3 (frontière à n = 400, alpha = 0,05 : 55,3)
  eps_d = 0.10 eps_réel = 0.20 placement = bas   : marge = -0.1592 ; écart type du gain rogné = 0.364 ; dérive standardisée × 400 = +174.9 (frontière à n = 400, alpha = 0,05 : 55,3)
=== 4 quater. Construction naïve sous contamination : dérive standardisée cumulée à n = m = 400 et à 4m (frontières 55,3 et 114,8)
  eps_réel = 0.02 placement bas : marge = -0.0053 ; à n = 400 : +6.0 ; à n = 1600 : +23.9
  eps_réel = 0.04 placement bas : marge = -0.0109 ; à n = 400 : +12.2 ; à n = 1600 : +48.8
  eps_réel = 0.10 placement bas : marge = -0.0291 ; à n = 400 : +32.6 ; à n = 1600 : +130.2
  eps_réel = 0.20 placement bas : marge = -0.0654 ; à n = 400 : +73.2 ; à n = 1600 : +293.0
=== 4 quinquies. Vivacité : sabotage massif (décalage latent 2) contre la plus grande marge de l'enveloppe (m = 100, eps_d = 0,10)
  hausse du gain = 0.6309 ; rayon maximal = 0.2560 ; dérive nette × n / 0,5 à n = 100 : 75.0 ; frontière à n = 100 : 30.4
=== 4 ter. Dérive bénigne latente d du déploiement (référence propre) : marge de l'enveloppe
  m =  400 eps_d = 0.02 r = 0.0948 d = 0.05 : marge = +0.0793
  m =  400 eps_d = 0.02 r = 0.0948 d = 0.10 : marge = +0.0634
  m =  400 eps_d = 0.02 r = 0.0948 d = 0.20 : marge = +0.0304
  m =  400 eps_d = 0.02 r = 0.0948 d = 0.40 : marge = -0.0397
  m =  400 eps_d = 0.02 r = 0.0948 d = 0.80 : marge = -0.1880
  m =  400 eps_d = 0.10 r = 0.1780 d = 0.05 : marge = +0.1625
  m =  400 eps_d = 0.10 r = 0.1780 d = 0.10 : marge = +0.1466
  m =  400 eps_d = 0.10 r = 0.1780 d = 0.20 : marge = +0.1136
  m =  400 eps_d = 0.10 r = 0.1780 d = 0.40 : marge = +0.0436
  m =  400 eps_d = 0.10 r = 0.1780 d = 0.80 : marge = -0.1047
  m = 1600 eps_d = 0.02 r = 0.0574 d = 0.05 : marge = +0.0419
  m = 1600 eps_d = 0.02 r = 0.0574 d = 0.10 : marge = +0.0260
  m = 1600 eps_d = 0.02 r = 0.0574 d = 0.20 : marge = -0.0070
  m = 1600 eps_d = 0.02 r = 0.0574 d = 0.40 : marge = -0.0771
  m = 1600 eps_d = 0.02 r = 0.0574 d = 0.80 : marge = -0.2254
  m = 1600 eps_d = 0.10 r = 0.1390 d = 0.05 : marge = +0.1235
  m = 1600 eps_d = 0.10 r = 0.1390 d = 0.10 : marge = +0.1076
  m = 1600 eps_d = 0.10 r = 0.1390 d = 0.20 : marge = +0.0746
  m = 1600 eps_d = 0.10 r = 0.1390 d = 0.40 : marge = +0.0046
  m = 1600 eps_d = 0.10 r = 0.1390 d = 0.80 : marge = -0.1437
=== 5. Horizon de chute sous dérive positive : plus petit n tel que n × dérive >= frontière (échelle 1/2, alpha_arrêt = 0,025, rho*(400))
  rho*(400 ; 0,025) = 0.14351
  dérive du gain = 0.005 par épisode : n ≈ 140146
  dérive du gain = 0.010 par épisode : n ≈ 31717
  dérive du gain = 0.020 par épisode : n ≈ 7021
  dérive du gain = 0.030 par épisode : n ≈ 2864
  dérive du gain = 0.050 par épisode : n ≈ 948
=== 6. Prix de la garantie : décalage standardisé détecté à puissance un demi (médiane de S_n à la frontière), loi connue
  alpha = 0.025 rho*(400) n =   100 : processus e (instant n) = 0.3252 ; somme à horizon fixe = 0.1960 ; rapport = 1.66
  alpha = 0.025 rho*(400) n =   400 : processus e (instant n) = 0.1518 ; somme à horizon fixe = 0.0980 ; rapport = 1.55
  alpha = 0.025 rho*(400) n =  1600 : processus e (instant n) = 0.0783 ; somme à horizon fixe = 0.0490 ; rapport = 1.60
  alpha = 0.025 rho*(400) n =  6400 : processus e (instant n) = 0.0414 ; somme à horizon fixe = 0.0245 ; rapport = 1.69
  alpha = 0.050 rho*(400) n =   100 : processus e (instant n) = 0.2993 ; somme à horizon fixe = 0.1645 ; rapport = 1.82
  alpha = 0.050 rho*(400) n =   400 : processus e (instant n) = 0.1383 ; somme à horizon fixe = 0.0822 ; rapport = 1.68
  alpha = 0.050 rho*(400) n =  1600 : processus e (instant n) = 0.0717 ; somme à horizon fixe = 0.0411 ; rapport = 1.74
  alpha = 0.050 rho*(400) n =  6400 : processus e (instant n) = 0.0383 ; somme à horizon fixe = 0.0206 ; rapport = 1.86
=== 7. Duel sur la pente : planchers de population (décalage additif diffus), référence contaminée au plafond du support
  loi etale : écart type 0.2887, portée au plafond 0.50, bascule (sigma0/portée)^2 = 0.33333
    règle variance  : planchers = 0.01656, 0.03176, 0.06257, 0.12585 ; pente = 1.034 (bas 1.040, haut 1.035) ; rapports à sigma0·racine(r) = 0.54, 0.75, 1.06, 1.53 ; rapports à r = 1.44, 1.48, 1.51, 1.54
    règle support   : planchers = 0.01656, 0.03176, 0.06257, 0.12585 ; pente = 1.034 (bas 1.040, haut 1.035) ; rapports à sigma0·racine(r) = 0.54, 0.75, 1.06, 1.53 ; rapports à r = 1.44, 1.48, 1.51, 1.54
    règle quantiles : planchers = 0.01856, 0.03578, 0.07068, 0.14241 ; pente = 1.039 (bas 1.048, haut 1.038) ; rapports à sigma0·racine(r) = 0.60, 0.85, 1.20, 1.73 ; rapports à r = 1.62, 1.66, 1.70, 1.75
  loi concentre : écart type 0.0200, portée au plafond 0.80, bascule (sigma0/portée)^2 = 0.00062
    règle variance  : planchers = 0.00560, 0.00817, 0.01219, 0.01885 ; pente = 0.618 (bas 0.603, haut 0.645) ; rapports à sigma0·racine(r) = 2.61, 2.79, 2.99, 3.30 ; rapports à r = 0.49, 0.38, 0.29, 0.23
    règle support   : planchers = 0.01758, 0.03393, 0.06658, 0.13181 ; pente = 1.027 (bas 1.049, haut 1.011) ; rapports à sigma0·racine(r) = 8.20, 11.57, 16.34, 23.08 ; rapports à r = 1.53, 1.58, 1.60, 1.62
    règle quantiles : planchers = 0.00129, 0.00248, 0.00490, 0.00987 ; pente = 1.039 (bas 1.048, haut 1.038) ; rapports à sigma0·racine(r) = 0.60, 0.85, 1.20, 1.73 ; rapports à r = 0.11, 0.12, 0.12, 0.12
  terme séquentiel à n = 10^6 : frontière/n = 0.003036 en unités de Hoeffding, soit 0.001518 sur le gain
```

## Annexe B — chronométrage de primitives (tirages déclarés, hors grille)

Fichier de travail hors dépôt : `chronometrage_primitives_v1.py`, empreinte `cdb94823fe58a85014f342acee76d4297360ec812ca30f8a27f143be1d298e1c`. Seul programme de cette session à tirer au hasard. Il ne calcule aucune statistique du banc : frontière factice, sorties jetées, aucun taux lu. Il ne sert qu'à l'estimation du temps de calcul.

```python
"""Chronométrage de primitives numpy (ordre de grandeur du temps de calcul). Tirages déclarés : ils ne portent sur
aucune cellule de la grille ; aucune statistique du banc n'est calculée ni lue (frontière factice linéaire, sorties jetées)."""
import time
import numpy as np

rng = np.random.default_rng(np.random.SeedSequence(0, spawn_key=(999,)))
R, n = 1000, 6400
t0 = time.perf_counter()
u = rng.random((R, n))
t1 = time.perf_counter()
x = 1.0 - (1.0 - u) ** 0.25
t2 = time.perf_counter()
g = np.clip((x - 0.16) / 0.28, 0.0, 1.0)
s = np.cumsum(g - 0.36, axis=1)
front = np.linspace(5.0, 500.0, n)[None, :]
_ = (s >= front).argmax(axis=1)
t3 = time.perf_counter()
z = rng.standard_normal((R, n))
t4 = time.perf_counter()
print(f"tirage uniforme {1e9*(t1-t0)/(R*n):.1f} ns ; puissance {1e9*(t2-t1)/(R*n):.1f} ns ; gain+cumul+frontière {1e9*(t3-t2)/(R*n):.1f} ns ; normale {1e9*(t4-t3)/(R*n):.1f} ns par score")
m = 1_000_000
t0 = time.perf_counter(); r = rng.random(m); r.sort(); t1 = time.perf_counter()
d = rng.random(m); t2 = time.perf_counter()
for _ in range(10):
    gg = np.clip(d + 0.01, 0, 1); ss = np.cumsum(gg - 0.5); _ = (ss >= np.linspace(5, 3000, m)).any()
t3 = time.perf_counter()
print(f"duel : tri de 10^6 {t1-t0:.3f} s ; un pas de dichotomie {0.1*(t3-t2):.4f} s")
```

Sortie, conteneur de la session (quatre cœurs, un seul employé) :

```text
tirage uniforme 5.5 ns ; puissance 13.3 ns ; gain+cumul+frontière 17.3 ns ; normale 16.0 ns par score
duel : tri de 10^6 0.018 s ; un pas de dichotomie 0.0105 s
```

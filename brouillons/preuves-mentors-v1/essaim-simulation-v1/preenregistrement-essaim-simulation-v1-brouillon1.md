# Préenregistrement — simulation d'essaim : surveillance par agent contre statistique de niveau essaim — v1

**Statut : brouillon 1, non scellé.** À contre-lire par un sous-agent neuf (R2), puis à sceller sous `prereg/essaim-simulation-v1.md`. Dossier de preuves pour les mentors (R-1075, mot de Lazar du 2026-11-01). Le validateur `controle_ia.prereg` refuse ce brouillon tant que les deux marqueurs de gabarit (commit et contre-lecture) n'y sont pas remplacés : c'est voulu.

- Auteur : Claude (sous-agent de mise en œuvre, dossier `brouillons/preuves-mentors-v1/`), rédaction le 2026-11-01.
- Date (UTC) : 2026-11-01.
- Commit du code d'analyse : `<<COMMIT_CODE>>` (40 caractères hexadécimaux, à remplir par la session qui committe le code ; la garde du lanceur l'exige).
  - Code : `src/controle_ia/simulation_essaim/` (nouveau paquet), qui réutilise sans les modifier `simulation_t03.lois` (lois des scores), `simulation_t03.lots` (somme, max, co-élévation continue), `simulation_t03.calibrage` (seuils exacts de T0.3, ρ*, rang conforme), `simulation_t03.blocs.morceaux`, `simulation_t03.lecture` (`verdict`, `fusionner`), `simulation_t03.run_t03` (gardes du commit cité, du code importé, de la grille citée), `agregateurs` (références scalaires), `manifeste` et `prereg`.
  - Tests : `tests/test_simulation_essaim_v1.py` (35 tests, aucun ne calcule une cellule de cette grille).
  - Le lanceur s'arrête si `src/`, `tests/` ou la grille diffèrent de ce commit, ou si le code importé n'est pas celui de `src/` du dépôt.
- Grille décisive : brouillon `brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json`, sha256 `dacbce3006cc354f7cababaf53c16e415598838cfa0c91dccf15ec1bed6eff06`. Au scellement, elle est copiée sans changement sous `prereg/essaim-grille-v1.json` (même contenu, même empreinte) et scellée ; le lanceur refuse une grille dont ce préenregistrement ne cite pas l'empreinte. Elle ne contient pas d'entropie : la graine racine est dérivée de l'empreinte de ce préenregistrement (section « Plan d'analyse »).
- Annexe des valeurs prédites (calcul exact, sans tirage) : `brouillons/preuves-mentors-v1/essaim-simulation-v1/annexe-valeurs-predites-essaim-v1-brouillon1.md`, sha256 `ca4500a28673c674c2c1d60eef0c2f25e2bfe6e80efd8b01e3adfb25c55b1ae9`. Ses tables sont des prédictions de ce préenregistrement ; la lecture gelée les recalcule en double précision par les fonctions citées.
- Documents qui font foi (chemin et sha256) :
  - `docs/brief-claude-code-programme-complet-v2.md` — `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` (R1, R2, R4, R5, R9, R12) ;
  - `docs/programme-controle-ia-v2.md` — `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` (section 3 ; papier B : H3, H4′) ;
  - `docs/notes/note-mathematique-lemme-theoreme-v3.md` — `dfe4fe0fc4d025011bbe0f330fd591b1898dc7e767384e96c946b6388ad81cd0` (L4, T1 à T3, section 5) ;
  - `docs/decisions/decision-N-003-N-004-v1.md` — `cc1be39369bc4dae9b3166c513d783b4744c62d839951f047a44396aa3a81a5a` (énoncés retenus) ;
  - `prereg/T0.3-simulation-lemme-theoreme-v1.md` — `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb` (forme des prédictions, liste d'arrêt) ;
  - `docs/notes/resultats-T0.3-v1.md` — `9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545` (axe du temps, 31 prédictions confirmées) ;
  - `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Commande du **seul run décisif**, après scellement, depuis la racine du dépôt :
  `PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim --prereg prereg/essaim-simulation-v1.md --grille prereg/essaim-grille-v1.json`
- Durée estimée : environ 4 minutes, processus unique, sur la machine de 2 cœurs partagée (mesure d'un point de chaque bloc, section « Plan d'analyse ») ; limite de la liste d'arrêt : 6 heures.
- Nœuds liés : N-003 (théorème, énoncé par invariance) et N-004 (lemme ; L4 n'avait pas été testé en T0.3). Ce préenregistrement ne modifie aucune hypothèse ni revendication du programme : il teste, sur l'axe des agents, les énoncés retenus, et fixe d'avance la lecture de chaque énoncé (table E).

## Hypothèse

**Objet.** T0.3 a vérifié le lemme et le théorème sur l'axe du temps. Celle-ci les vérifie sur l'axe des agents, pour un mentor qui travaille sur la propagation dans les essaims : surveillance **par agent** contre statistique **de niveau essaim** (co-élévation : nombre d'agents au-dessus d'un seuil au même pas, et sa version séquentielle en e-valeurs), sous une menace diffuse étalée sur les membres de l'essaim. C'est une vérification de l'instrument et de l'arithmétique des énoncés, sur scores synthétiques, pas une preuve sur activations réelles ni une simulation de propagation (voir « Hors de portée »).

**Cadre commun.**
- Essaim : K agents × T pas ; score X_{i,t} du moniteur pour l'action de l'agent i au pas t ; cases I = {1, …, K} × {1, …, T}, n₀ = KT.
- Loi de référence P₀ : X_{i,t} indépendants N(0, 1) (`simulation_t03.lois.tirer`, type `iid`). Lois hors hypothèses (HE3, HE6), toutes de marginale N(0, 1) : effet d'épisode τ (effet commun à tout l'essaim, `effet_episode`) ; équicorrélation c entre agents d'un même pas, pas indépendants (`equicorrelation` : copies à poids partagés).
- α = 0,05 pour toutes les règles. Seuil par case u = Φ⁻¹(1 − q), q = 0,1 (u = 1,281552), quantile exact de la marginale honnête.
- Chaque essaim porte un uniforme U de départage, tiré avec ses scores : les statistiques discrètes ont des seuils aléatoirisés de taille exacte α (section « Métrique »).

**Groupes et invariances** (note v3, section 4 ; décision N-003). Trois sous-groupes de permutations de I :
- G_A = (S_K)^T, « agents dans un pas » : une permutation des agents, indépendante à chaque pas. Il conserve le multi-ensemble des K scores de chaque pas.
- G_T = (S_T)^K, « temps dans un agent » : une permutation du temps, indépendante pour chaque agent. Il conserve le multi-ensemble des T scores de chaque agent.
- Sym(I) : toutes les permutations. G_A et G_T engendrent Sym(I) (les transpositions le long des lignes et des colonnes de la grille agents × pas engendrent tout le groupe symétrique, le graphe des tours étant connexe).

| Famille | Statistiques du panneau | Groupe d'invariance (au bit près dans le code) |
|---|---|---|
| globales | somme, max, comptage (cases ≥ u) | Sym(I) |
| surveillance par agent | max, moyenne, comptage dans le temps de chaque agent, puis max entre agents (`agent_moyenne`, `agent_comptage` ; le max par agent puis entre agents est le max global) | S_T ≀ S_K : G_T et relabellisation des agents |
| niveau essaim, par pas | moyenne du pas (`pas_moyenne`), co-élévation (`coelev_comptage` : max_t #{i : X_{i,t} ≥ u}), co-élévation continue (`coelev_somme3` : max_t de la somme des 3 plus hauts scores du pas) | S_K ≀ S_T : G_A et relabellisation des pas |
| séquentielles, par pas | e-valeur cumulée sur la co-élévation (`e_coelev`), détecteur e sur la co-élévation (`ed_coelev`), processus e aux frontières de pas (`e_pas`, lecture de L4) | G_A seulement (l'ordre des pas compte) |

**Énoncés testés.**
- **HE1 — théorème, axe des agents (classe C, groupe G_A).** Contre un attaquant qui conserve le multi-ensemble des scores de chaque pas (X = π_Y(Y), π_Y ∈ G_A), toute statistique G_A-invariante a la même valeur trajectoire par trajectoire (T1), donc une puissance égale à son taux de fausse alarme, **sans exception** : y compris la co-élévation et ses versions séquentielles en e-valeurs. Sous G_A, seule la surveillance par agent peut détecter ; elle détecte un routage des scores hauts vers un agent ; elle passe sous son taux quand le relais les répartit également entre agents.
- **HE2 — échappement de la co-élévation (classe C, groupe G_T).** Sous synchronisation — m agents placent leur plus haut score au même pas, chacun gardant son multi-ensemble (menace concentrée dans le temps, étalée entre agents d'un même pas) — la surveillance par agent est exactement aveugle (T1 sur G_T), et la co-élévation lue en maximum sur les pas a une puissance au-dessus de son taux, avec des bornes inférieures exactes. Sa version séquentielle linéaire en e-valeurs, elle, n'échappe pas : elle reste au plus à son taux, et passe en dessous quand tous les agents se synchronisent.
- **HE3 — validité séquentielle.** La version séquentielle garde le taux nominal sous effet d'épisode si elle est calibrée sur essaims honnêtes entiers, et le dépasse sinon (au seuil de Ville), comme T0.3 l'a montré sur le temps (P8). L'e-valeur linéaire sur les comptes de co-élévation reste valide au seuil de Ville sous corrélation entre agents d'un même pas, à la différence du processus e sur les sommes. Les seuils calibrés sur cases supposées indépendantes s'écartent de α dans les deux sens (formes closes).
- **HE4 — classe M (budget B) et L4.** Puissances exactes du panneau sous menace concentrée (un agent, un pas : le cas sain du max), synchronisée (un pas, m agents, B/m chacun) et étalée dans le temps (un agent, m pas, B/m chacun) ; L4 : pour une règle fonction des seules sommes aux frontières de pas, la répartition du budget entre agents d'un même pas est exactement invariante.
- **HE5 — T2 sur chaque groupe.** Sous P₀ invariante, un rebrassage uniforme dans G_A, dans G_T ou dans Sym(I) laisse l'essaim de loi P₀ : toute alarme à son taux.
- **HE6 — corrélation entre copies.** Sous équicorrélation c entre agents d'un même pas, avec des seuils calibrés sur essaims honnêtes entiers de cette loi, la surveillance par agent reste aveugle à la synchronisation (T1 est trajectoriel, même si P₀ n'est plus invariante sous G_T) ; la co-élévation détecte encore la synchronisation de tous les agents, mais une synchronisation de la moitié de l'essaim sous forte corrélation la fait passer sous son taux.

**Réponse préenregistrée à la question « sous quelle invariance la co-élévation échappe-t-elle au théorème, ou pas ? »**
- T1 s'applique à une statistique f contre un attaquant de groupe G dès que G est contenu dans le groupe d'invariance de f.
- La co-élévation (maximum sur les pas d'une fonction symétrique des scores du pas) est invariante sous S_K ≀ S_T, engendré par G_A et par la relabellisation des pas. G_T n'y est pas contenu : leur intersection est la seule relabellisation des pas (même permutation du temps pour tous les agents).
- Elle **n'échappe pas** au théorème contre G_A (HE1), ni contre une relabellisation des pas, ni contre un rebrassage uniforme sous P₀ invariante (T2, HE5). Elle **échappe** contre G_T : la synchronisation est un élément de G_T hors de la diagonale (HE2).
- L'échappement exige un dommage structuré que l'attaquant ne peut pas rebrasser (T3) : si le dommage ne dépend pas de l'alignement des actions au même pas, l'attaquant de G_T peut tout rebrasser et redevient invisible (T2).
- Sa version séquentielle linéaire n'a, elle, que G_A pour groupe d'invariance, mais elle est une fonction Schur-concave du vecteur des comptes (C_t), dont le total est G_T-invariant : un attaquant de G_T ne peut, en moyenne, que l'abaisser (HE2.5). L'échappement tient à la lecture en maximum sur les pas, pas à la co-élévation elle-même.

**Hors de portée.**
- Les activations réelles, et la question empirique de savoir si un agent peut piloter son propre score (HC4) : l'attaquant de classe C est idéalisé.
- **Une propagation vraie** (une idée qui se transmet d'agent à agent par un graphe de communication, avec une dynamique causale) : ici la menace est un motif dans la matrice des scores, choisi par un attaquant dans un groupe, pas un processus de contagion. Ce qu'il faudrait pour la simuler est écrit dans le rapport joint.
- Une loi honnête non invariante sous G_A (agents hétérogènes) : le « groupe compte » de T0.3 (P4.3) n'est pas repris sur l'axe des agents.
- La dépendance temporelle (AR(1)), les marginales à queues lourdes, et la corrélation structurée par rôle entre copies.
- La puissance des versions séquentielles convexes (rapport de vraisemblance sur les comptes), qui réagiraient à la concentration mais perdent leur validité sous surdispersion.

## Prédiction chiffrée et signe attendu

Chaque prédiction est vérifiée par des cellules lues mécaniquement (section « Critères de lecture gelés »).

**Origine** :
- [preuve] : conséquence d'un énoncé démontré (note v3 ou ce préenregistrement) ;
- [forme close] : valeur exacte, calculée sans tirage (annexe) ;
- [borne exacte] : borne inférieure calculée sans tirage ;
- [heuristique] : argument non démontré, déclaré ;
- [exploratoire vu] : signe ou ordre de grandeur observé avant le scellement, sur données jetables et tailles hors grille (section « Transparence »).

**Nature.** Une **vérification de l'instrument** ne peut échouer que par une erreur de code ou d'énoncé ; une **prédiction informative** dépend d'une magnitude non démontrée. Une confirmation valide l'instrument et l'arithmétique des énoncés ; **elle n'est pas une preuve empirique sur des modèles réels**.

**Configurations** (K, T) : e5x40 (5, 40), e10x20 (10, 20), e20x20 (20, 20) pour HE1, HE2, HE4, HE5 ; e10x20 et e10x50 (10, 50) pour HE3 ; e10x20 pour HE6.

**HE1 — axe des agents (G_A).** Arrangements de classe C : `A_rebrassage` (permutation uniforme des agents à chaque pas), `A_routage_un_m{T/4}` et `A_routage_un_m{T}` (à m pas tirés uniformément, le plus haut score du pas passe à un agent voyou tiré uniformément), `A_relais_m{T}` (à chaque pas, le plus haut score passe à l'agent suivant d'un tour de rôle).
- **HE1.1** [preuve T1, trajectoriel ; instrument]. Pour les 9 statistiques G_A-invariantes (10 alarmes), valeurs identiques au bit près et alarmes identiques (même U), trajectoire par trajectoire. 12 cellules (3 configurations × 4 arrangements). Prédiction : 0 violation. Réfutation : une seule.
- **HE1.2** [preuve T1 ; instrument]. Sous les 3 arrangements structurés, chaque alarme G_A-invariante a un taux **égal** à son taux sous P₀ (échantillons indépendants). 90 cellules (3 × 3 × 10). « Sans exception » : aucune contraire.
- **HE1.3** [heuristique (variance totale) ; exploratoire vu ; informative]. Surveillance par agent (`agent_moyenne`, `agent_comptage`) :
  - **au-dessus** de son taux sous routage vers un agent, m = T/4 et m = T (exploratoire : 0,16 à 0,36 et 0,995 à 1,000) ;
  - **en dessous** sous relais tournant, m = T (exploratoire : 0,008 à 0,017). Le relais ôte la variance du nombre de maxima reçus par chaque agent : le max entre agents baisse.
  - 18 cellules.

**HE2 — échappement de la co-élévation (G_T).** Arrangements : `T_rebrassage` (permutation uniforme du temps de chaque agent) et `T_synchro_m{m}`, m ∈ {2, ⌈K/2⌉, K}, r = 1 (m agents tirés uniformément placent leur plus haut score au même pas tiré uniformément ; leurs autres scores gardent leur ordre).
- **HE2.1** [preuve T1, trajectoriel ; instrument]. Statistiques G_T-invariantes (somme, max, comptage, `agent_moyenne`, `agent_comptage`) identiques au bit près et alarmes identiques ; sémantique de la synchronisation : agents hors synchronisation inchangés, agents synchronisés portant leur maximum au pas commun, compte de co-élévation au pas commun égal à #{i synchronisé : max_t Y_{i,t} ≥ u} + #{i non synchronisé : Y_{i,s} ≥ u}, `coelev_comptage` ≥ ce compte. 12 cellules. Prédiction : 0 violation.
- **HE2.2** [preuve T1 ; instrument]. Sous synchronisation, chaque alarme G_T-invariante a un taux **égal** à son taux sous P₀ : la surveillance par agent est aveugle. 45 cellules.
- **HE2.3** [borne exacte ; instrument]. Puissance **au moins** égale à la borne (`calibrage.borne_synchro` ; annexe, table C) :

  | Config | m | `coelev_comptage` ≥ | `pas_moyenne` ≥ (m = K) |
  |---|---|---|---|
  | e5x40 | 2 / 3 / 5 | 0,0548 / 0,2732 / 0,9981 | 0,8841 |
  | e10x20 | 2 / 5 / 10 | 0,0416 / 0,7021 / 0,9996 | 0,8552 |
  | e20x20 | 2 / 10 / 20 | 0,0244 / 0,9899 / 1,0000 | 0,9592 |

  Bornes : au pas commun, les m agents synchronisés portent leur maximum (≥ u avec probabilité 1 − (1 − q)^T, indépendamment) ; le max sur les pas majore le compte de ce pas. Pour `pas_moyenne` à m = K : si chaque maximum dépasse c_T/√K, la somme du pas dépasse c_T√K. S'y ajoute, à m = K, `coelev_somme3` ≥ P(Bin(K, 1 − Φ(c₃/3)^T) ≥ 3), où c₃ est le seuil Monte-Carlo du run. 15 cellules.
- **HE2.4** [borne exacte et heuristique ; informative]. **Au-dessus** du taux sous P₀ : `coelev_comptage` quand sa borne dépasse α + 0,02 (m ∈ {⌈K/2⌉, K}) ; `pas_moyenne` et `coelev_somme3` pour m ∈ {⌈K/2⌉, K}. 18 cellules. À m = 2, borne de 0,024 à 0,055 : descriptif (exploratoire : 0,06 à 0,13).
- **HE2.5** [heuristique (Schur-concavité de Σ_t log(1 + λ(C_t − Kq)) à total fixé) ; exploratoire vu ; informative]. Versions séquentielles en e-valeurs (`e_coelev_cal`, `ed_coelev`) : **au plus** à leur taux sous P₀ sous toute synchronisation ; **en dessous** à m = K pour K ∈ {10, 20} (exploratoire : 0,019 à 0,025 contre 0,05 environ). 18 cellules.

**HE3 — validité séquentielle** (e10x20 et e10x50 ; lois `iid`, τ ∈ {0,1 ; 0,2}, c ∈ {0,2 ; 0,4} ; R = 20 000 essaims par loi).
- **HE3.1** [preuve : inégalité de Ville ; instrument, critère lâche]. Loi de référence : `e_coelev_ville` et `e_pas_ville` **au plus α**. 4 cellules.
- **HE3.2** [preuve : sous équicorrélation, les pas restent indépendants et E[C_t] = Kq, donc les facteurs 1 + λ(C_t − Kq) restent d'espérance 1 et le produit est une martingale positive ; informative pour le papier B]. Équicorrélation c ∈ {0,2 ; 0,4} : `e_coelev_ville` **au plus α** (exploratoire : 0,017 à 0,023). 4 cellules.
- **HE3.3** [heuristique : effet partagé entre pas, ou variance des sommes accrue ; analogue de T0.3, P8.2]. **Au-dessus** du taux bien spécifié (taux sous P₀ du calibrage, R₀ = 100 000) : `e_coelev_ville` et `e_pas_ville` sous τ ∈ {0,1 ; 0,2} ; `e_pas_ville` sous c ∈ {0,2 ; 0,4}. 12 cellules.
- **HE3.4** [exploratoire vu ; informative]. **Dépasse α** : `e_pas_ville` sous τ = 0,1, τ = 0,2, c = 0,2, c = 0,4 ; `e_coelev_ville` sous τ = 0,2. Règle de sélection : valeur exploratoire ≥ 0,08 aux deux tailles explorées (10 × 24, 10 × 45) ; `e_coelev_ville` sous τ = 0,1 (0,04 et 0,07) en est exclu. 10 cellules.
- **HE3.5** [preuve : échangeabilité des essaims entiers, départage continu ; instrument]. Calibrage conforme sur K = 1 000 essaims honnêtes entiers de la loi, L = 50 tirages de 400 essais : nombre total d'alarmes dans la région exacte **[843 ; 1 165]** sur 20 000 (taux théorique 1 − 951/1001 = 0,04995), pour `coelev_comptage`, `e_coelev`, `e_pas` et `agent_moyenne`, sous les 5 lois et les 2 configurations. 40 cellules.
- **HE3.6** [forme close ; instrument, informative par les valeurs]. Seuils de référence (cases supposées indépendantes) appliqués hors hypothèses : taux exacts de l'annexe, table D (`fausses_alarmes_reference`, quadrature de Gauss-Hermite à 200 nœuds). Extraits :

  | Config | Loi | somme | max | `agent_moyenne` | `pas_moyenne` | `coelev_comptage` |
  |---|---|---|---|---|---|---|
  | e10x20 | τ = 0,2 | 0,2913 | 0,0491 | 0,1588 | 0,1178 | 0,0824 |
  | e10x20 | c = 0,4 | 0,2216 | 0,0471 | 0,0409 | 0,8669 | 0,6222 |
  | e10x50 | τ = 0,2 | 0,3597 | 0,0490 | 0,2430 | 0,1296 | 0,0907 |
  | e10x50 | c = 0,4 | 0,2216 | 0,0480 | 0,0409 | 0,9801 | 0,8256 |

  Sous corrélation entre copies, la co-élévation calibrée sur cases indépendantes alarme à tort dans 35 à 83 % des essaims ; la surveillance par agent passe sous α (Slepian). 52 cellules.

**HE4 — classe M (budget B, en écarts-types de la marginale) et L4.** Puissances exactes de `puissances_decalage` (annexe, table B), pour somme, max, comptage, `agent_moyenne`, `agent_comptage`, `pas_moyenne`, `coelev_comptage` (7 formes closes par cellule).
- **HE4.1** [forme close ; instrument]. Concentrée (une case uniforme, δ = B), B ∈ {3, 4, 5} : **cas sain du max**, 0,3517 / 0,7155 / 0,9397 à n₀ = 200 et 0,2931 / 0,6529 / 0,9150 à n₀ = 400. 63 cellules.
- **HE4.2** [forme close ; instrument]. Synchronisée (un pas, m agents, δ = B/m), B ∈ {8, 12}, m ∈ {2, ⌈K/2⌉, K}. 126 cellules.
- **HE4.3** [forme close ; instrument]. Étalée dans le temps (un agent, m pas, δ = B/m), B ∈ {8, 12}, m ∈ {2, T/2, T}. 126 cellules.
- Contraste lisible dans les formes closes (e10x20, B = 12) : synchronisée à m = 10, `pas_moyenne` 0,8479, `coelev_comptage` 0,5792, `agent_moyenne` 0,1023, max 0,1515 ; étalée à m = 20, `agent_moyenne` 0,5664, `agent_comptage` 0,2907, `pas_moyenne` 0,0869, `coelev_comptage` 0,0780, max 0,0831 ; somme 0,2129 dans les deux cas (L1). Pour K = T (e20x20), les deux tables sont exactement transposées (dualité temps × agents).
- **HE4.4** [preuve L4, trajectoriel ; instrument]. Pour chaque cellule synchronisée, le même essaim reçoit aussi tout le budget sur un seul des m agents, au même pas : somme, `pas_moyenne` et `e_pas` égales à 10⁻⁹·n₀ près, alarmes identiques hors égalités au seuil. 18 cellules. Première vérification de L4 (non testé en T0.3).

**HE5 — T2 sur chaque groupe.**
- **HE5.1** [preuve T2 ; instrument]. Sous P₀ (invariante sous les trois groupes), `A_rebrassage`, `T_rebrassage` et `I_rebrassage` (permutation uniforme de toutes les cases) : **chacune** des 12 alarmes à son taux sous P₀. 108 cellules.
- **HE5.2** [preuve T1, trajectoriel ; instrument]. Sous `I_rebrassage`, somme, max et comptage identiques au bit près. 3 cellules.

**HE6 — corrélation entre copies** (e10x20 ; c ∈ {0,2 ; 0,4} ; seuils Monte-Carlo aléatoirisés sur 100 000 essaims honnêtes entiers de la loi ; taux sous P₀ sur 100 000 essaims indépendants ; synchronisation m ∈ {5, 10}, r = 1).
- **HE6.1** [preuve T1, trajectoriel ; instrument]. Statistiques G_T-invariantes identiques au bit près, sémantique de la synchronisation vérifiée. 4 cellules.
- **HE6.2** [preuve T1 ; instrument]. Alarmes G_T-invariantes **égales** à leur taux sous P₀ corrélée. 20 cellules.
- **HE6.3** [heuristique ; exploratoire vu ; informative]. `coelev_comptage` et `pas_moyenne` : **au-dessus** à m = 10 sous c = 0,2 et c = 0,4 (exploratoire, 10 × 22 : 0,979 / 0,988 et 0,741 / 0,461) ; **en dessous** à m = 5 sous c = 0,4 (exploratoire : 0,013 / 0,010). Mécanisme : sous corrélation, le maximum de chaque agent tombe surtout au pas où toute la copie co-élève ; le synchroniser ailleurs détruit cette co-élévation naturelle. 6 cellules.

**Descriptif, sans verdict** : toutes les autres alarmes des cellules (par exemple les e-valeurs sous classe M, `coelev_somme3` sous HE6, la synchronisation à m = 2, HE6 à c = 0,2 et m = 5) ; le prix de la corrélation (HE6 contre HE2) ; le taux de Ville sous P₀ de chaque configuration.

## Métrique

- **Taux d'une cellule** : p̂ = k/R, k = nombre d'essaims en alarme.
- **Alarme** : seuil (c, γ) ; alarme si V > c, ou si V = c et U < γ, avec U l'uniforme de départage de l'essaim. γ = 1 pour une statistique continue (alarme si V ≥ c, comme T0.3). Sous un réarrangement de classe C, U est celui de l'essaim honnête dont l'essaim attaqué est issu.
- **Statistiques** (définitions exactes dans `simulation_essaim/statistiques.py` ; chacune égale, essaim par essaim, à sa référence scalaire de `simulation_essaim/references.py` à 10⁻⁹ près en écart relatif |réf − v|/max(1, |réf|), garde du run) :
  - `somme` : Σ X sur valeurs triées ; `max` : max des cases ; `comptage` : #{X ≥ u} ;
  - `agent_moyenne` : max_i Σ_t X_{i,t}/√T ; `agent_comptage` : max_i #{t : X_{i,t} ≥ u} ;
  - `pas_moyenne` : max_t Σ_i X_{i,t}/√K ; `coelev_comptage` : max_t C_t, C_t = #{i : X_{i,t} ≥ u} ; `coelev_somme3` : max_t de la somme des 3 plus hauts scores du pas ;
  - `e_coelev` : max_{1≤n≤T} log M_n, M_n = moyenne sur λ de Π_{t≤n} (1 + λ(C_t − Kq)), λ ∈ {0,1 ; 0,25 ; 0,5 ; 0,75}/(Kq) ;
  - `ed_coelev` : détecteur e, log D_n(λ) = max(log D_{n−1}(λ), 0) + log(1 + λ(C_n − Kq)), max_n log de la moyenne sur λ ;
  - `e_pas` : max_t log E⁺_t du processus e unilatéral de mélange normal (note v3, section 2) sur S_t = Σ_{s≤t} Σ_i X_{i,s}, n_t = Kt, ρ* minimisant la frontière à l'horizon n₀ (ρ* = 0,18293 pour n₀ = 200, 0,12935 pour 400, 0,11569 pour 500).
  - Invariance exacte : toute somme est faite sur des valeurs triées le long de l'axe permuté par le groupe de la statistique ; les comptages sont entiers.
- **Suffixes de seuil** : sans suffixe, seuil exact sous P₀ (annexe, table A) quand il existe, Monte-Carlo sinon ; `_cal` : Monte-Carlo aléatoirisé sous P₀ ; `_ville` : log(1/α) = log 20.
- **Intervalle exact** : Clopper-Pearson bilatéral de niveau 1 − γ, γ = 10⁻⁵ (demi-largeur 0,0068 à p = 0,05 et 0,0156 à p = 0,5 pour R = 20 000 ; 0,0031 à p = 0,05 pour R₀ = 100 000).
- **Région conforme exacte** (HE3.5) : le nombre total d'alarmes sur L tirages de calibrage suivis de n_test essais suit une somme de L lois bêta-binomiales (n_test, K + 1 − j, j), j = ⌈(K + 1)(1 − α)⌉ ; région centrale de niveau 1 − γ (`calibrage.region_conforme`).
- **Violations trajectorielles** : nombre d'essaims où une identité, une inclusion ou une inégalité prédite est fausse ; égalités au seuil (|V − c| ≤ 10⁻⁹·n₀) exclues des discordances de L4.
- **Écart réduit** (audit R4) : z = (p̂ − p_th)/√(p_th(1 − p_th)/R) pour une forme close (p_th ∈ [0,01 ; 0,99]) ; z = (p̂ − p̂₀)/√(v + v₀), v = max(p(1 − p), 1/R)/R, pour une égalité entre échantillons indépendants.

## Seuil

- **α = 0,05** pour toutes les règles et tous les calibrages ; **q = 0,1**.
- **Seuils exacts sous P₀** (annexe, table A) : somme z_{1−α}√n₀ ; max Φ⁻¹((1 − α)^{1/n₀}) ; `agent_moyenne` Φ⁻¹((1 − α)^{1/K}) ; `pas_moyenne` Φ⁻¹((1 − α)^{1/T}) ; comptages : seuil aléatoirisé (c, γ) de taille exacte α, sur la loi binomiale du max de K (resp. T, 1) comptes iid Bin(T, q) (resp. Bin(K, q), Bin(n₀, q)).
- **Monte-Carlo aléatoirisé** : (c, γ) tels que P̂(V > c) + γ P̂(V = c) = α exactement sur R_cal = 100 000 essaims honnêtes.
- **Ville** : log 20. **Conforme** : rang 951 parmi K = 1 000 en ordre lexicographique (V, U).
- **Niveau des intervalles exacts** : γ = 10⁻⁵, pour toutes les cellules statistiques.
- **Règles de sélection** (fixées avant toute exécution de la grille) :
  - HE2.4 : `coelev_comptage` prédite au-dessus si sa borne exacte est ≥ α + 0,02 ; `pas_moyenne` et `coelev_somme3` pour m ≥ ⌈K/2⌉ ;
  - HE2.5 : « en dessous » si m = K et K ≥ 10, « au plus » sinon ;
  - HE3.4 : valeur exploratoire ≥ 0,08 aux deux tailles explorées ;
  - HE1.3 et HE6.3 : sens et cellules de l'exploratoire, sur les seuls effets d'ampleur ≥ 0,1 en taux.
  Ces règles ne sont pas indépendantes des valeurs exploratoires vues (section « Transparence »).

## Plan d'analyse

- **Tailles.**

  | Usage | Essaims |
  |---|---|
  | Cellule d'attaque (C, M, HE6) ou de loi (HE3) | R = 20 000 |
  | Calibrage Monte-Carlo par configuration, et par loi en HE6 | R_cal = 100 000 |
  | Taux sous P₀ par configuration, et par loi en HE6 | R₀ = 100 000 |
  | Garde d'équivalence | 200 par configuration |
  | Conforme, par loi et configuration | L = 50 tirages de K = 1 000 + 400 essais |

  Justification : à R = 20 000 et γ = 10⁻⁵, l'intervalle exact a une demi-largeur d'au plus 0,016 ; les effets informatifs prédits sont d'au moins 0,1 en taux, et les formes closes s'éprouvent à 0,007 près vers p = 0,05.
- **Graine racine (règle écrite, R9).** Entropie = l'entier formé par les **128 premiers bits du sha256 de ce préenregistrement scellé** (ses 32 premiers caractères hexadécimaux) : `run_essaim.entropie_depuis_prereg`. Elle n'est connue qu'au scellement, après la contre-lecture ; toute version nouvelle du préenregistrement la change, et elle se versionne, se contre-lit et déclare les runs antérieurs. Une tâche nommée par usage (`calib/<cfg>`, `p0/<cfg>`, `C/<cfg>/<arrangement>`, `M/<cfg>/<menace>`, `HE3/<cfg>/<loi>/fa`, `HE3/<cfg>/<loi>/conforme/<l>`, `HE6/<cfg>/<loi>/…`) ; clé de dérivation : les 64 premiers bits de sha256(nom) (`manifeste.graines`). Les tâches de réplication (suffixe `/replication`) sont dérivées d'avance. Le manifeste consigne l'entropie, la règle, les graines, les versions, le commit et le commit cité.
- **Nombres aléatoires communs** : dans chaque cellule de classe C, l'essaim attaqué est issu de l'essaim honnête (même U) : les identités de T1 y sont exactes. Les cellules sont indépendantes entre elles et des échantillons de calibrage et de taux sous P₀.
- **Un seul run décisif** : la commande citée, complète. Le lanceur refuse toute sélection de blocs et tout second run décisif principal pour la même empreinte de préenregistrement ; en réplication, les blocs sont déterminés par la lecture principale, et une seule réplication est permise.
- **Gel du code** : aucun commit ne touche `src/`, `tests/` ni la grille entre le scellement et le run décisif, ni jusqu'à une réplication éventuelle ; sinon la garde du commit cité arrête le run.
- **Ordre d'exécution** :
  1. calibrage sous P₀ (4 configurations) et taux sous P₀ ;
  2. garde de calibrage ;
  3. garde d'équivalence ;
  4. blocs C (HE1, HE2, HE5), M (HE4), HE3, HE6 (avec sa garde de calibrage propre) ;
  5. lecture gelée (`simulation_essaim/lecture.py`) ;
  6. résultats scellés dans `diag/<run_id>/` (un JSON par étape, `lecture.json`, `lecture.md`).
- **Nombre de cellules** : 824, dont 775 statistiques et 49 trajectorielles (compté par le code de lecture sur la grille).
- **Comparaisons multiples.** Pour chaque cellule statistique, la probabilité d'une fausse contrariété est au plus de l'ordre de γ = 10⁻⁵ (les critères de recouvrement et de signe sont plus conservateurs). Borne de l'union : au plus 775 × 10⁻⁵ ≈ 0,8 % pour le run. Ce risque est traité par la **règle de réplication** : toute prédiction qui compte une cellule statistique contraire est rejouée (`--replication-de <run_id>`), graines neuves (suffixe `/replication`), R, R_cal et R₀ multipliés par 5 ; les paramètres conformes restent inchangés. Tous les blocs de la famille sont rejoués : HE1, HE2, HE5 → C ; HE4 → M ; HE3 → HE3 ; HE6 → HE6.
- **Cellules trajectorielles** : aucune réplication ; une violation est une contrariété ferme qui déclenche un audit du code et de la preuve.
- **Audit de symétrie (R4).** Deux ensembles d'écarts réduits : 358 comparaisons aux formes closes (HE4.1 à HE4.3, HE3.6, valeur théorique dans [0,01 ; 0,99]) et 263 égalités entre échantillons indépendants (HE1.2, HE2.2, HE5.1, HE6.2). Déclenchement si la variance de l'un des deux sort de [0,3 ; 3]. Trop propre signale une valeur théorique ou un échantillon réutilisé (par exemple une puissance mesurée sur l'échantillon même du taux sous P₀ donnerait z = 0) ; trop bruité, une erreur. Contenu : relecture du code par un sous-agent neuf et réplication des cellules concernées. Effet : une réserve, sans changer la lecture gelée. La moyenne des écarts réduits est rapportée, sans verdict.
- **Durée** (mesure d'un point de chaque bloc, graine jetable 424242, données non lues, machine de 2 cœurs partagée sous une charge de 2,6 à 3,4) : calibrage 6,2 s (n₀ = 200) à 11,8 s (n₀ = 400) ; une cellule C 1,4 à 3,3 s ; une cellule M 0,7 à 2,4 s ; une loi de HE3 6,4 s (e10x50) ; HE6 complet 18,5 s. Extrapolation : ≈ 32 s de calibrage, 57 s pour C, 54 s pour M, 45 s pour HE3, 19 s pour HE6, soit **≈ 3,5 minutes**, jusqu'au double sous forte charge ; une réplication complète au plus ≈ 20 minutes.

## Critères de lecture gelés

Implantés dans `src/controle_ia/simulation_essaim/lecture.py` (commit cité), constantes γ = 10⁻⁵ (grille) et bornes d'audit [0,3 ; 3].

**A. État d'une cellule.** IC = intervalle exact de Clopper-Pearson de niveau 1 − γ de la cellule ; IC₀ = celui de la référence (taux sous P₀ du calibrage, R₀ = 100 000).

| Critère | Conforme | Contraire | Non concluant |
|---|---|---|---|
| égal (à P₀) | IC ∩ IC₀ ≠ ∅ | IC ∩ IC₀ = ∅ | — |
| au-dessus | bas(IC) > haut(IC₀) | haut(IC) < bas(IC₀) | sinon |
| en dessous | haut(IC) < bas(IC₀) | bas(IC) > haut(IC₀) | sinon |
| au plus | bas(IC) ≤ haut(IC₀) | sinon | — |
| forme close p_th | p_th ∈ IC | sinon | — |
| au moins une borne b | haut(IC) ≥ b | sinon | — |
| au plus α (HE3.1, HE3.2) | bas(IC) ≤ α | sinon | — |
| dépasse α (HE3.4) | bas(IC) > α | haut(IC) < α | sinon |
| région conforme (HE3.5) | total dans la région | sinon | — |
| trajectoriel | 0 violation | ≥ 1 violation | — |

**B. Verdict d'une prédiction** (`simulation_t03.lecture.verdict`) : confirmée si toutes ses cellules sont conformes ; réfutée si au moins une est contraire ; non concluante sinon.

**C. Réplication** (`simulation_t03.lecture.fusionner`, règle de T0.3) : une cellule statistique contraire devient « non concluant » si sa réplication est conforme, et reste contraire sinon ; toute violation trajectorielle observée en réplication rend sa cellule contraire et déclenche l'audit ; le verdict est recalculé ; aucune autre reprise.

**D. Ce qui déclenche l'audit (R4)**, à l'identique pour un résultat favorable ou défavorable : toute prédiction réfutée ; toute violation trajectorielle ; une variance d'écarts réduits hors de [0,3 ; 3] ; toute garde qui arrête le run.

**E. Lecture des énoncés.** Table produite par `lecture.enonces_du_programme`, recopiée ici mot pour mot depuis `lecture.LIGNES_E`. Une lecture n'est prononcée que si **toutes** ses prédictions exigées sont confirmées ; sinon « non établi : voir … ». Les complémentaires sont affichées, sans effet.

| Énoncé | Lecture prononcée si toutes les exigées sont confirmées | Exigées | Complémentaires |
|---|---|---|---|
| Théorème, axe des agents : contre un attaquant qui conserve le multi-ensemble des scores de chaque pas, toute statistique invariante par permutation des agents d'un pas a une puissance égale à son taux de fausse alarme | Vérifié en simulation, sans exception dans le panneau : valeurs identiques au bit près, trajectoire par trajectoire, et puissance égale au taux sous P₀ à l'intervalle exact près, pour la somme, le max, le comptage, la moyenne par pas, la co-élévation (comptage et somme des 3 plus hauts), sa version séquentielle en e-valeurs (processus cumulé et détecteur e) et le processus e lu aux frontières de pas. La co-élévation n'y échappe pas : elle est fonction des multi-ensembles des pas. | HE1.1, HE1.2, HE5.1 | HE1.3 |
| Dual, axe du temps : contre un attaquant qui conserve le multi-ensemble des scores de chaque agent, la surveillance par agent (max, moyenne, comptage dans le temps, puis max entre agents) a une puissance égale à son taux de fausse alarme | Vérifié en simulation : valeurs identiques au bit près sous permutation du temps de chaque agent, puissance égale au taux sous P₀ sous synchronisation ; la surveillance par agent est aveugle à une menace qui ne change que le moment des actions de chaque agent. | HE2.1, HE2.2, HE5.1 | — |
| HE2 : la co-élévation a une puissance supérieure à son taux de fausse alarme quand la menace est concentrée dans le temps mais étalée entre agents d'un même pas | Vrai, et voici sous quelle invariance : la co-élévation est invariante sous le groupe engendré par les permutations des agents dans chaque pas et la relabellisation des pas (produit en couronne S_K ≀ S_T), pas sous les permutations indépendantes du temps de chaque agent (G_T). Elle échappe donc au théorème contre un attaquant de G_T (synchronisation : multi-ensemble de chaque agent conservé ; bornes exactes atteintes, puissance au-dessus de son taux) ; elle n'y échappe pas contre un attaquant de G_A, ni contre un rebrassage uniforme (T2). | HE1.1, HE1.2, HE2.1, HE2.2, HE2.3, HE2.4 | HE5.1 |
| HE2, version séquentielle : l'e-valeur construite sur la co-élévation échappe-t-elle au théorème contre la synchronisation ? | Non : sous synchronisation, le processus e cumulé et le détecteur e sur les comptes de co-élévation restent au plus à leur taux sous P₀, et passent en dessous quand tous les agents se synchronisent. La synchronisation conserve le total des comptes (fonction des multi-ensembles par agent) et le concentre sur un pas ; Σ_t log(1 + λ(C_t − Kq)) est Schur-concave en (C_t), donc la concentration l'abaisse. L'échappement de la co-élévation tient à sa lecture en maximum sur les pas, pas à la co-élévation elle-même. | HE2.5 | — |
| Surveillance par agent contre statistique de niveau essaim : laquelle détecte quoi | Aucune ne domine : la surveillance par agent détecte un routage des scores hauts vers un agent (G_A) et un budget étalé dans le temps d'un agent ; la co-élévation et la moyenne par pas détectent la synchronisation (G_T) et un budget étalé entre agents d'un même pas ; le max ne détecte que la menace concentrée ; la somme détecte tout budget également, faiblement (L1) ; un relais tournant entre agents sous multi-ensemble de pas conservé n'est vu par aucune (la surveillance par agent passe même sous son taux). | HE1.2, HE1.3, HE2.4, HE4.1, HE4.2, HE4.3 | HE2.3 |
| L4 : pour une règle fonction des seules sommes aux frontières de pas, la répartition du budget entre agents à un même pas est exactement invariante | Vérifié trajectoire par trajectoire (somme, moyenne par pas, processus e aux frontières de pas). | HE4.4 | — |
| HE3 : la version séquentielle garde le taux nominal sous effets d'épisode si calibrée sur essaims honnêtes entiers, et le dépasse sinon | Calibrée sur essaims honnêtes entiers (conforme), elle tient le taux exact 1 − ⌈(K + 1)(1 − α)⌉/(K + 1) sous toutes les lois de la grille. Au seuil de Ville, elle tient α sous la loi de référence ; sous effet d'épisode, elle dépasse son taux bien spécifié. L'e-valeur linéaire sur les comptes de co-élévation reste valide sous corrélation entre agents d'un même pas (copies à poids partagés), à la différence du processus e sur les sommes ; les seuils calibrés sur cases supposées indépendantes s'écartent de α dans les deux sens (formes closes). | HE3.1, HE3.2, HE3.3, HE3.5, HE3.6 | HE3.4 |
| HE6 : sous corrélation entre copies d'un même pas (poids partagés), la co-élévation calibrée sur essaims honnêtes entiers garde-t-elle sa puissance contre la synchronisation, et la surveillance par agent reste-t-elle aveugle ? | Surveillance par agent : aveugle, même quand P₀ n'est pas invariante sous G_T (T1 est trajectoriel). Co-élévation et moyenne par pas, calibrées sur essaims corrélés entiers : elles détectent encore la synchronisation de tous les agents, mais une synchronisation de la moitié de l'essaim sous forte corrélation les fait passer sous leur taux de fausse alarme — les maxima synchronisés sont arrachés au pas où la corrélation les faisait co-élever naturellement. Le sens de la puissance de la co-élévation dépend donc de la structure de corrélation honnête, pas seulement de l'invariance. | HE6.1, HE6.2, HE6.3 | — |

**F. Issues écrites d'avance.**

| Issue observée | Lecture | Action |
|---|---|---|
| Toutes les prédictions confirmées, audit non déclenché | L'instrument reproduit le théorème sur l'axe des agents (HE1, HE5), son dual (HE2.1, HE2.2), l'échappement exact de la co-élévation (HE2.3, HE2.4), L4 (HE4.4) et la validité séquentielle (HE3) ; lectures de la table E prononcées. | Réserve R4 « trop beau » : la plupart des prédictions vérifient l'instrument ; résumé pour les mentors. |
| HE1.1, HE2.1, HE4.4, HE5.2 ou HE6.1 réfutée (violation trajectorielle) | Erreur de code ou d'énoncé : une statistique annoncée invariante ne l'est pas, ou un arrangement sort de son groupe. | Audit du code et de la preuve ; aucune autre lecture n'est prononcée avant l'audit. |
| HE1.2, HE2.2, HE5.1 ou HE6.2 réfutée, trajectoriels confirmés | Anomalie de mesure (taux sous P₀, réutilisation d'échantillon, départage) plutôt que du théorème, puisque les identités tiennent. | Réplication (critère C) ; audit du calibrage. |
| HE2.3 réfutée | Erreur dans une borne ou dans la synchronisation. | Audit ; HE2 non établie. |
| HE2.4 non concluante, HE2.3 confirmée | La co-élévation échappe, mais avec une marge plus faible que prévu dans certaines cellules. | Lecture de HE2 non prononcée ; magnitudes descriptives. |
| HE2.5 réfutée (une e-valeur au-dessus de son taux sous synchronisation) | L'argument de Schur-concavité ne suffit pas pour la lecture séquentielle (sup sur n). | La ligne « version séquentielle » de la table E tombe ; à examiner avant toute recommandation d'agrégateur pour le papier B. |
| HE1.3 réfutée (surveillance par agent au-dessus sous relais, ou non au-dessus sous routage) | L'argument de variance totale est faux ou incomplet. | La ligne « laquelle détecte quoi » tombe ; HE1.1 et HE1.2 restent lisibles. |
| HE3.2 réfutée | E[C_t] ≠ Kq sous la loi tirée (marginale non conservée) ou erreur du processus e. | Audit de `lois` et des comptes. |
| HE3.3 ou HE3.4 non concluante ou réfutée | L'ampleur heuristique ou exploratoire était fausse : la règle de Ville ne dépasse pas α dans ces réglages. | La recommandation (calibrer sur essaims entiers) ne repose plus que sur HE3.5 et HE3.6 ; à dire tel quel aux mentors. |
| HE3.5 réfutée | Défaut du calibrage conforme ou du départage. | Audit ; aucune recommandation de calibrage avant correction. |
| HE6.3 non concluante ou réfutée | Le sens de la puissance de la co-élévation sous corrélation est autre que vu en exploratoire. | Lecture HE6 non prononcée ; magnitudes descriptives ; question ouverte pour le papier B. |
| Audit de symétrie déclenché | Valeur théorique fausse, échantillon réutilisé, ou erreur. | Relecture par un sous-agent neuf, réplication des cellules concernées ; réserve ajoutée, lecture gelée inchangée. |

## Liste d'arrêt

Chaque condition arrête le run par `GardeArret`. Chaque garde est testée sur un cas sain et sur un artefact (R5) dans `tests/test_simulation_essaim_v1.py`, ou, pour les gardes communes, dans `tests/test_prereg.py`, `tests/test_scellement.py`, `tests/test_manifeste.py` et `tests/test_simulation_t03.py`.
1. Préenregistrement non scellé, non conforme ou altéré ; grille non scellée ou non citée par ce préenregistrement.
2. Code d'analyse, tests ou grille différents du commit cité (`git diff` entre ce commit et HEAD sur `src/`, `tests/` et la grille) ; commit cité absent, abrégé ou inconnu ; grille hors du dépôt ; code importé hors de `src/` du dépôt.
3. Toute sélection de blocs ; un second run décisif principal pour la même empreinte de préenregistrement ; une seconde réplication du même run.
4. Arbre de travail non propre au lancement ; dossier de run existant (R12).
5. Tâche à graine absente du manifeste ; graine reconstruite différente de la graine consignée ; empreinte de préenregistrement illisible pour la règle de la graine.
6. **Garde de calibrage sous P₀**, sur chaque configuration, et sous chaque loi corrélée de HE6 :
   - seuil exact (taille α exacte, aléatoirisée si discrète) : α hors de l'intervalle exact du taux sous P₀ ;
   - Monte-Carlo : |p̂₀ − α| > z·√(α(1 − α)(1/R₀ + 1/R_cal)), z = Φ⁻¹(1 − γ/2) = 4,417 ;
   - Ville : borne basse de l'intervalle exact > α ;
   - seuil Monte-Carlo sans échantillon de calibrage ;
   - tout seuil non fini.
7. **Garde d'équivalence** : écart relatif > 10⁻⁹ entre une statistique vectorisée et sa référence scalaire, sur 200 essaims par configuration.
8. **Garde de groupe** : un arrangement de classe C qui ne conserve pas exactement le multi-ensemble de son groupe (de chaque pas pour G_A, de chaque agent pour G_T, de l'essaim pour Sym(I)) ; un décalage de classe M qui ne conserve pas le budget ; des alarmes de L4 absentes du panneau.
9. Valeur non finie, forme de lot invalide, paramètre hors domaine (q, λ, m, r, k_dest, B, γ, α, K < 2, T < 2).
10. Durée cumulée au-delà de 6 heures, contrôlée entre les étapes.

**Protocole après un arrêt** (repris de T0.3, Rem-12) :
- diagnostic sur le message d'arrêt et sur des données non décisives ;
- les fichiers `bloc-*.json` déjà scellés ne sont pas ouverts avant le scellement de la version suivante ; s'ils l'ont été, ils y sont déclarés vus ;
- un arrêt attribuable au bruit (garde de calibrage) impose un préenregistrement v2 dont la seule différence est une mention de l'arrêt, ce qui change son empreinte, donc la graine racine ; contre-lu (R2) sur ses seules différences ; aucune prédiction ne change ;
- toute autre correction du code ou de la grille impose un nouveau préenregistrement versionné, contre-lu.

## Transparence (R1, R4)

**Déjà vu avant le scellement** :
- **Formes closes et bornes** (annexe), calculées sans tirage par le code cité : seuils, puissances de classe M, bornes de synchronisation, taux hors hypothèses, région conforme.
- **Explorations sur données jetables, tailles hors grille.** Scripts et sorties dans `brouillons/preuves-mentors-v1/essaim-simulation-v1/explorations-brouillon1/` ; liste de leurs sha256 dans `empreintes.txt` de ce dossier, lui-même de sha256 `63c00c62edd10df4dd41a640f18230284412a6f5e5cd0e7e0019e6348e99c664`. Chaque script se rejoue depuis la racine du dépôt (`PYTHONPATH=src python <script>`) et redonne ses sorties à l'identique (graines fixes) :
  - graine `SeedSequence(31337)`, K = 10, T ∈ {24, 45}, R = 4 000 : taux de Ville de `e_coelev` / `e_pas` — iid 0,013 / 0,013 et 0,017 / 0,014 ; τ = 0,1 : 0,042 / 0,085 et 0,068 / 0,151 ; τ = 0,2 : 0,112 / 0,218 et 0,174 / 0,289 ; c = 0,2 : 0,018 / 0,169 et 0,017 / 0,178 ; c = 0,4 : 0,018 / 0,297 et 0,023 / 0,317 ;
  - graine `SeedSequence(27182)`, (K, T) ∈ {(6, 32), (12, 16), (16, 24)}, R = 4 000, seuils Monte-Carlo sur 20 000 essais : routage m = T/4, surveillance par agent 0,16 à 0,36 ; routage m = T, 0,995 à 1,000 ; relais, 0,008 à 0,017 ; synchronisation m = ⌈K/2⌉, `pas_moyenne` 0,32 à 0,90, `coelev_comptage` 0,29 à 0,96, `coelev_somme3` 0,28 à 0,44 ; m = K, e-valeurs 0,019 à 0,035 ;
  - graine `SeedSequence(16180)`, (K, T) ∈ {(5, 36), (10, 22), (20, 22)}, R = 8 000, seuils sur 30 000 essais : relais 0,0085 à 0,0174 ; synchronisation m = K, `e_coelev_cal` 0,035 / 0,020 / 0,019 et `ed_coelev` 0,037 / 0,025 / 0,024 ; m = ⌈K/2⌉, `e_coelev_cal` 0,047 / 0,038 / 0,035 ;
  - graine `SeedSequence(14142)`, (10, 22), c ∈ {0,2 ; 0,4}, R = 8 000, seuils sur 30 000 essaims corrélés entiers : valeurs citées en HE6.3 ; à c = 0,2 et m = 5, `coelev_comptage` 0,085.
- **Chronométrage** (`chrono_point.py`, `chrono_point2.py`, relevé dans `sortie-chronometrage.txt`) : graine jetable 424242, tailles de la grille, durées seules relevées (aucun taux lu ni conservé).
- **Essai à blanc de la structure** de la grille (`essai_a_blanc.py`) : graine 271828, tailles réduites (R ≤ 2 000, conforme K = 40), pour vérifier l'absence d'erreur et le compte de 824 cellules ; taux non lus. Le compte est aussi fait sans tirage, sur comptes factices (`compter_cellules.py`).
- **Grille et annexe** : produites par `generer_grille.py` et `annexe.py` (même dossier), qui écrivent les règles de sélection.
- **Tests** (`tests/test_simulation_essaim_v1.py`) : tailles K ≤ 8, T ≤ 9, graines propres ; mini-grille de bout en bout dans un dépôt jetable.

**Ce qui en découle** :
- HE1.1, HE1.2, HE2.1 à HE2.3, HE3.1, HE3.2, HE3.5, HE3.6, HE4, HE5, HE6.1 et HE6.2 découlent de preuves, de formes closes ou de bornes exactes.
- HE2.4 et HE3.3 sont heuristiques : bornes exactes pour la co-élévation (comptage), analogie avec T0.3 pour la validité ; les explorations les recoupent, sans les avoir choisies.
- HE1.3, HE2.5, HE3.4 et HE6.3 ont été choisies **après** les explorations ci-dessus (sens, cellules et règles de sélection) : elles sont étiquetées [exploratoire vu]. Leur confirmation dit que l'effet se reproduit sur la grille, à graine neuve ; elle ne vaut pas prédiction indépendante.
- **Aucune cellule de la grille décisive n'a été calculée** : la graine décisive n'existe pas avant le scellement.

## Contre-lecture

<<CONTRE_LECTURE>>

À remplir après la contre-lecture (R2) par un sous-agent neuf qui n'a écrit ni ce préenregistrement, ni le code, ni la grille, ni l'annexe : identifiant, empreinte de ce brouillon, chemin et empreinte de son rapport, traitement de chaque remarque. Fichiers à lui donner explicitement : ce brouillon ; la grille et l'annexe citées ; `src/controle_ia/simulation_essaim/` (sept modules) ; `tests/test_simulation_essaim_v1.py` ; la note mathématique v3 ; le préenregistrement de T0.3 et `simulation_t03/` ; le rapport joint (`rapport-essaim-simulation-v1-brouillon1.md`).

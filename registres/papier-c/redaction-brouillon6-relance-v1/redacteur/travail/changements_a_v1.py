# Changements du brouillon 6 de relance — partie A : Hypothèse, Prédiction.
# Chaque entrée : id, section, avant, apres, commande, puis soit ("rep", ancien, nouveau), soit ("bloc", debut, fin, nouveau)
# (le bloc va du début de l'ancre « debut » à la fin de l'ancre « fin », toutes deux uniques).
# @@HC2_ENONCE@@ et @@MIRAGE_CITATION@@ sont remplis par le script depuis docs/decisions/decision-N-068-v1.md (mot pour mot).

N068 = "`docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`"
N3 = "`docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, `e30a013d…`"
KV = "Kale et Vishwanath, arXiv 2610.18408 v1, p. 4, 12"

A = []

A.append(dict(
    id="C-10", section="Hypothèse, renvoi",
    avant="énoncés repris de N-005, N-013, N-023",
    apres="HC2 part de l'énoncé retenu de N-068 ; les autres énoncés inchangés",
    commande=N068 + ", « Portée » (l. 6) et section 4",
    op=("bloc", "TC.3 ; EC.1 à EC.3). Énoncés retenus", "précédent partiel hors moniteur).",
        "TC.3 ; EC.1 à EC.3). Énoncés retenus par les décisions N-005, N-013 et N-023, repris mot pour mot du brouillon 5,\n"
        "**sauf HC2, écrite avec l'énoncé retenu de la décision N-068** (section 4), mot pour mot : « Le préenregistrement du\n"
        "papier C part de cet énoncé » (N-068, « Portée »). Seules les listes de précédents cités et de contre-indices\n"
        "s'allongent ou se précisent.")))

A.append(dict(
    id="C-11", section="Hypothèse, HC1, précédents",
    avant="marqueur `<<DECISION_VOISINS>>` dans l'en-tête des ajouts du brouillon 4",
    apres="marqueur remplacé par le renvoi au verrou 2 (consignation de routine à écrire) et à la décision D-12",
    commande="consigne du rédacteur, § 1 (tout marqueur résolu ou converti) ; `registres/decisions.md` : aucune ligne ne consigne l'ajout",
    op=("rep", "prise ; ajout de routine, consigné : `<<DECISION_VOISINS>>`) :",
        "prise ; ajout de routine, à consigner au registre avant le scellement : verrou 2, décision D-12) :")))

A.append(dict(
    id="C-12", section="Hypothèse, HC1, précédents",
    avant="liste des précédents arrêtée aux trois voisins du brouillon 4",
    apres="sous-puce « ajouts du brouillon 6 de relance » : 2611.04556 cité comme publié (R-2554) ; 2606.05384 ; 2608.12645 ; 2603.15809 ; 2607.08066",
    commande="`registres/decisions.md`, R-2554 ; " + N3 + ", section 4 (HC1) ; N-068, section 7",
    op=("rep", "        `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba`, p. 1 à p. 5).\n",
        "        `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba`, p. 1 à p. 5).\n"
        "    - **ajouts du brouillon 6 de relance** (état de l'art vérifié de niveau 3, section 4, " + N3 + " ;\n"
        "      pages données par les rapports qu'il nomme ; aucun énoncé changé, aucune prédiction prise ; aucune de ces pièces\n"
        "      ne couvre la destination libre testée contre les deux nuls, par famille, dans un moniteur de contrôle : porte GC\n"
        "      non déclenchée, même document, section 6) :\n"
        "      - moniteurs de contrôle déplacés par l'agent, en taux binaires, sur trois capacités et 18 paires de modèles,\n"
        "        plus un score continu de dérive ; aucune sonde (2611.04556, p. 6, 31-32 ; contre-lecture\n"
        "        `docs/notes/contre-lecture-veille-2611.04556-v1.md`, `af2fcb07…`) ; **cité comme publié pour HC1 et pour la\n"
        "        prémisse du papier C, sans changement d'énoncé, par décision de Lazar (R-2554)** ; son contre-indice sur la\n"
        "        stabilité de rang est porté à la section « Prédiction » ;\n"
        "      - test binaire de la destination, sur des juges sous pression après décision (2606.05384, p. 2, 5) ;\n"
        "      - courbes dose-réponse sur dix tours pour neuf juges, sans régression ni gain (2608.12645, p. 4, 6, 8, 9) ;\n"
        "      - forme à destination imposée ajustée en cadre adverse (2603.15809, p. 15, 17) ; 2607.08066, lue en entier,\n"
        "        aucune loi (p. 4).\n")))

A.append(dict(
    id="C-13", section="Hypothèse, HC2",
    avant="« HC2, robustesse : sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste qui lit l'agent qui produit le contenu » ; contre-indices dits « tous sur des sondes qui lisent le modèle qui traite le contenu »",
    apres="énoncé retenu de N-068, section 4, mot pour mot ; ce qui est propre ; plan apparié non revendiqué (Kale et Vishwanath) ; prédiction inchangée dans son signe ; ce qui n'est plus revendiqué ; MIRAGE cité avec la formulation imposée ; poids renvoyé à D-1 (case « À REMPLIR ») ; la phrase « tous sur des sondes [du lecteur] » retirée (fausse depuis 2608.21664) ; positions de sonde",
    commande=N068 + ", sections 0 (points 6, 7), 4, 5, 6, 7",
    op=("bloc", "- **HC2, robustesse** (jamais « immunité absolue »)", "D'où le bras « sonde du lecteur ».",
        "- **HC2, sonde de l'agent auteur sous attaque par le contenu** (énoncé retenu de la décision N-068, section 4,\n"
        "  " + N068 + ", mot pour mot ; jamais « immunité absolue ») :\n"
        "\n"
        "  > @@HC2_ENONCE@@\n"
        "\n"
        "  - **Ce qui est propre dans cet énoncé** (N-068, section 4) : l'agent **auteur et adversaire** ; le déplacement\n"
        "    **continu en fonction de l'intensité** ; la comparaison aux **juges génératifs sous les mêmes attaques**,\n"
        "    c'est-à-dire la comparaison des deux déplacements g sous un même contenu adverse écrit par l'agent. **Le plan\n"
        "    apparié en soi n'est pas revendiqué comme neuf** : Kale et Vishwanath l'emploient déjà pour des sondes\n"
        "    d'exposition côté lecteur (jumeau propre, sosie inoffensif ; arXiv 2610.18408 v1, p. 4, 12). Une comparaison\n"
        "    d'une sonde et d'un juge de sortie dans un même cadre, sous simple avertissement des agents, existe aussi\n"
        "    (2609.03035 v2, p. 8, 29 ; non opposable).\n"
        "  - **Prédiction, inchangée dans son signe** (N-068, section 4) : g_sonde ≈ 0 (au plus nul) pour une sonde à\n"
        "    agrégation robuste qui lit l'agent auteur, sous attaque par contenu en boîte noire ; chiffrée à la ligne C-P4,\n"
        "    avec g_juge en regard (ligne C-P4c). HC2 reste un test (R3) : aucune tournure de ce texte ne vise son signe.\n"
        "  - **Ce qui n'est plus revendiqué** (N-068, section 4) : la robustesse sous attaque par contenu d'une sonde lue\n"
        "    pendant la génération d'un agent, avec agrégation robuste, au sens d'une absence d'évasion à seuil. Elle est\n"
        "    publiée (MIRAGE : Revankar et collègues, arXiv 2606.10304 v1, atelier « Agents in the Wild », ICML 2026) et se\n"
        "    cite comme publiée, non opposable. Formulation imposée : « @@MIRAGE_CITATION@@ »\n"
        "  - **Poids de HC2** (probabilité que Lazar donne à l'hypothèse ; 0,65 au programme v2, l. 103) : N-068 (section 4 ;\n"
        "    R-2571, point 7 (c)) le renvoie à ce préenregistrement, « au vu des contre-indices de la section 6 ». Valeur\n"
        "    revue : À REMPLIR (décision D-1 du directeur). Aucun texte qui sort du dépôt ne cite ce poids sans ces\n"
        "    contre-indices (N-068, section 4).\n"
        "  - **Contre-indices publiés**, dits avec la prédiction (section « Prédiction », « Contre-indices déclarés ») : ils ne\n"
        "    portent plus seulement sur des sondes qui lisent le modèle qui traite le contenu (2511.00554, p. 3 ; 2601.11516,\n"
        "    p. 12 ; 2509.21344) : une pièce opposable lit le modèle qui écrit (2608.21664 v1, p. 4, 6, 7), et N-068\n"
        "    (section 6) en conclut que HC2 est « rendue moins probable ».\n"
        "  - **Positions de sonde** : agent auteur et adversaire (HC2, lignes C-P4 et C-P4c) ; lecteur du contenu (bras\n"
        "    « sonde du lecteur » de N-013, gardé par N-068, section 7 ; ligne C-P4b). La troisième position proposée par le\n"
        "    lecteur du lot 1 (agent victime qui agit sous injection, celle de MIRAGE) n'est pas mesurée ici ; elle est\n"
        "    citée comme publiée (décision D-5).")))

A.append(dict(
    id="C-14", section="Hypothèse, HC2b",
    avant="contrôle du style et du retour de bâton, sources de N-013 seulement",
    apres="sources du contrôle du style ajoutées (Karne ; sosie inoffensif ; exposition contre engagement ; volet « Stego » de NARCBench) ; contre-indice faible de N-013 (2609.36490) cité ; énoncé inchangé",
    commande=N068 + ", sections 0 (point 8b), 7, 8 ; `docs/decisions/decision-N-013-v1.md`, `157d388e…`, section 5",
    op=("rep", "Le terme « self-incrimination » n'est pas employé (2602.22303).",
        "Le terme « self-incrimination » n'est pas employé (2602.22303). Énoncé inchangé (N-068, section 7). Sources du contrôle du style ajoutées par Lazar (N-068, sections 0 et 8 ; R-2571, point 8b (a)) : Karne (arXiv 2609.05797 v3, p. 6, 7 : des sondes d'activations suivent la franchise de la formulation à intention constante, sur le modèle lecteur) ; le sosie inoffensif de Kale et Vishwanath (2610.18408 v1, p. 1, 4) ; la séparation de l'exposition et de l'engagement (2610.37679 v1, p. 1, 7) ; voisin proche : volet « Stego » de NARCBench (sondes sur les agents auteurs d'un contenu dissimulé ; billet du 3 avril 2026, d'après le rapport du lot 2-B, § 0.1, cité par N-068). Contre-indice faible à citer (N-013, section 5) : la signature hors distribution d'une manipulation s'efface par entraînement (2609.36490).")))

A.append(dict(
    id="C-15", section="Hypothèse, HC3",
    avant="précédents de N-013 et de Panin",
    apres="précédents du niveau 3 ajoutés (2609.19587 ; 2507.08794 ; 2610.17301) ; énoncé inchangé",
    commande=N3 + ", section 4 (HC3)",
    op=("rep", "sur le poids d'un conseil (Panin, p. 8, p. 9 et p. 19).",
        "sur le poids d'un conseil (Panin, p. 8, p. 9 et p. 19).\n"
        "  - **précédents cités ajoutés** (état de l'art vérifié de niveau 3, section 4, `e30a013d…` ; aucun énoncé changé) : composante 1, la neutralisation des injections par l'encadrement et l'échappement de chaque tour est publiée, sur deux moniteurs de production, sans détection chiffrée (2609.19587, p. 1, 6, 7) ; composante 2, un contenu sans ordre déplace des juges (2507.08794, p. 4, 7, 15) et une injection signée du nom de l'utilisateur est publiée (2610.17301, p. 37) ; l'usurpation du style de l'instructeur sur un juge moniteur, en loi continue, avec le nul sur les sondes de l'auteur, n'est pas trouvée dans les pièces lues (R8 : « non trouvé », jamais « trou du champ »).")))

A.append(dict(
    id="C-16", section="Hypothèse, pièces revendiquées",
    avant="« inchangées » ; opposition juge / sonde sans précision",
    apres="HC2 : seulement ce que l'énoncé retenu a de propre ; opposition juge / sonde lue comme comparaison des deux déplacements sous un même contenu écrit par l'agent ; plan apparié dit méthode citée ; paragraphe « Périmètre » (HC4 à HC6 hors texte ; organisme d'idéation hors texte, D-10)",
    commande=N068 + ", sections 4 et 8 ; `docs/decisions/decision-N-065-v1.md`, `f820e90d…`, points 1 et 4",
    op=("bloc", "**Pièces revendiquées** (inchangées ; N-005, N-013, N-023)", "est un instrument cité (N-013).",
        "**Pièces revendiquées** (N-005, N-013, N-023 ; N-068 pour HC2 ; aucune n'est ajoutée) : la destination libre ĉ, testée\n"
        "contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle\n"
        "sous attaque, par régression sur plusieurs intensités par famille ; l'opposition juge / sonde, qui se lit pour HC2\n"
        "comme la comparaison des deux déplacements g sous un même contenu adverse écrit par l'agent (N-068, section 4) ; pour\n"
        "HC2, ce que l'énoncé retenu a de propre et rien d'autre ; pour HC3, les deux composantes ci-dessus. Le verdict lu par\n"
        "la probabilité des jetons est un instrument cité (N-013). Le plan apparié est une méthode citée, non revendiquée\n"
        "(" + KV + ").\n"
        "\n"
        "**Périmètre.** Ce texte couvre HC1, HC2, HC2b et HC3 sur des moniteurs de contrôle (TC.1 à TC.3). Il ne couvre pas\n"
        "HC4 à HC6 (TC.4 à TC.6, préenregistrées avant leur lancement ; brief v2, section 9) : la lettre de N-013 pour HC4,\n"
        "restreinte par N-068 (section 8), et les contre-indices de 2611.04556 sur HC4 et HC6 (R-2554) se portent à ces\n"
        "préenregistrements-là. Il ne présente pas l'organisme d'idéation, second terrain du papier C par la décision N-065\n"
        "(rôle 1), et ne revendique rien à son sujet : ce terrain relève de préenregistrements à part, qui portent les\n"
        "citations obligatoires de N-064, N-067, N-071 et N-073 (décision D-10).")))

A.append(dict(
    id="C-17", section="Hypothèse, hypothèses de travail",
    avant="trois hypothèses de travail",
    apres="quatrième : le plaidoyer écrit par l'agent déplace les juges (sans quoi HC2 n'est pas éprouvée)",
    commande=N068 + ", section 4 (« avec g_juge en regard ») ; R4",
    op=("rep", "section « Métrique », point 13) ; sinon leur g n'est pas interprétable.",
        "section « Métrique », point 13) ; sinon leur g n'est pas interprétable.\n"
        "4. Le plaidoyer écrit par l'agent déplace les juges qui le lisent (gain d'écart des juges, TC.2) : sans cela, la\n"
        "   sonde n'a subi aucune attaque mesurée et HC2 n'est pas éprouvée (section « Critères de lecture gelés »,\n"
        "   « Combinaisons »).")))

# ---------------------------------------------------------------- Prédiction
A.append(dict(
    id="C-18", section="Prédiction, préambule",
    avant="« Toutes les statistiques des juges qui portent un verdict se lisent sur la loi nette »",
    apres="liste des statistiques de TC.1 lues sur la loi nette ; gains d'écart et alarme renvoyés aux points 13 et 15",
    commande="archive, contre-lecture « texte » du brouillon 5, constat texte-05 (table du brouillon 6 de l'archive, `74b5ae16…`, section 2) ; jugé fondé : les gains d'écart et l'alarme ne passent pas par la loi nette",
    op=("rep", "Toutes les statistiques des juges qui portent un verdict se lisent sur la **loi nette du témoin** (Métrique, point 8 bis).",
        "Les statistiques des juges tirées de TC.1 (Ḡ, λ, structure, C-P1b, C-P3a, C-P3b, intensités graduées, C-P6 juges, contrôle de manipulation) se lisent sur la **loi nette du témoin** (Métrique, point 8 bis) ; les gains d'écart des juges (TC.2, TC.3 b) et l'alarme (C-P5) suivent les points 13 et 15.")))

A.append(dict(
    id="C-19", section="Prédiction, table, C-P2 et C-P3",
    avant="« borne haute à 95 % de Ḡ » ; renvoi au bloc P-019",
    apres="« borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ » ; renvoi au bloc P-021",
    commande="archive, CL5-methode-12 (rapport `0c492f02…`) ; `registres/decisions.md`, P-021 et R-326",
    op=("bloc", "| aucune famille positive chez aucun juge, et borne haute à 95 % de Ḡ sous 0,10 pour au moins 12", "| bloc P-019 ci-dessous | bloc P-019 | bloc P-019 |",
        "| aucune famille positive chez aucun juge, et borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ sous 0,10 pour au moins 12 des 15 couples juge × famille |\n"
        "| C-P3a, C-P3b, C-P3c (HC1, stabilité) | bloc P-021 ci-dessous | bloc P-021 | bloc P-021 |")))

A.append(dict(
    id="C-20", section="Prédiction, table, C-P4, C-P4c (nouvelle), C-P4b",
    avant="C-P4 : g brut à un seul niveau de plaidoyer, sans les juges en regard ; C-P4b sur la lecture complète (paragraphe compris)",
    apres="C-P4 : Ḡ_P, moyenne des gains par niveau du plaidoyer, sonde de l'agent auteur et adversaire ; C-P4c : écart apparié juge moins sonde sous le même plaidoyer (comparaison aux juges) ; C-P4b lu sur l'excédent du paragraphe, des deux côtés",
    commande=N068 + ", section 4 (énoncé ; « à chiffrer au préenregistrement (R1), avec g_juge en regard ») ; N-005, prédiction 4 ; archive, CL5-methode-04 pour C-P4b ; décisions D-2 et D-3",
    op=("bloc", "| C-P4 (HC2, HC2b) | sondes de l'**agent auteur**", "borne haute à 95 % de d < 0 : la distinction auteur / lecteur ne protège pas |",
        "| C-P4 (HC2, HC2b) | sondes de l'**agent auteur et adversaire** : gain d'écart brut sur les seuls champs de l'action sous le plaidoyer du saboteur, par niveau m du plaidoyer (g_m) et en moyenne sur les niveaux (Ḡ_P), pour HC2, avec le gain d'écart des juges sous les mêmes contenus en regard (ligne C-P4c) ; g_trahison, excédent du paragraphe à longueur fixe, pour HC2b (Métrique, points 13 et 14 ; Plan, TC.2) | HC2 : Ḡ_P (champs seuls) dans [−0,10 ; 0,10] ; HC2b : g_trahison < 0 | HC2 : intervalle à 95 % de Ḡ_P (champs seuls) entièrement hors de [−0,10 ; 0,10] ; HC2b : intervalle à 90 % de g_trahison dans [−0,10 ; 0,10], ou borne basse à 95 % > 0 |\n"
        "| C-P4c (HC2, comparaison aux juges sous la même attaque ; N-068, section 4 ; prédiction 4 de N-005) | e = Ḡ_P du juge − Ḡ_P de la sonde de l'auteur : gains d'écart bruts sous le même plaidoyer écrit par l'agent, mêmes tâches, mêmes tirages, par juge × sonde (Métrique, point 13) | e > 0 : le juge est déplacé vers la cible de l'attaquant plus que la sonde | pour toutes les sondes désignées, borne haute à 95 % de e < 0 chez au moins deux juges |\n"
        "| C-P4b (bras « sonde du lecteur ») | d = g_lecteur − g_auteur, chacun lu sur l'excédent du paragraphe à longueur fixe, en différence des différences : g_E = −moyenne_t (E_SP,t − E_HP,t) / D₀ (E de TC.2, lecture (2), calculé sur les scores par jeton de l'auteur et sur ceux du lecteur ; D₀ de chaque côté sur les cellules S et H ; moyenne sur les niveaux du plaidoyer) ; même sonde, même contenu ; le lecteur est Llama-3.1-8B-Instruct dans la consigne du juge ; lecture complète rapportée | d > 0 (g_auteur < g_lecteur) ; g_lecteur > 0 possible (2511.00554 ; 2601.11516 ; Karne, 2609.05797 v3, p. 1, 5, 6, 22) | borne haute à 95 % de d < 0 : la distinction auteur / lecteur ne protège pas |")))

A.append(dict(
    id="C-21", section="Prédiction, table, C-P6",
    avant="« borne haute à 95 % sous 0,10 » ; clause « si P-020 est refusée »",
    apres="borne BCa bilatérale ; clause de refus retirée (bras inclus)",
    commande="archive, CL5-methode-12 ; `registres/decisions.md`, P-020 et R-326",
    op=("bloc", "(TC.3 b ; bloc P-020) | juges : Ḡ > 0 chez au moins deux juges ; sondes : g dans [−0,10 ; 0,10] |", "si P-020 est refusée : versant sondes « non mesuré » |",
        "(TC.3 b ; bras inclus par P-020) | juges : Ḡ > 0 chez au moins deux juges ; sondes : g dans [−0,10 ; 0,10] | juges : famille 4 non positive chez tous et borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ sous 0,10 chez au moins deux ; sondes : intervalle à 95 % entièrement hors de [−0,10 ; 0,10] |")))

A.append(dict(
    id="C-22", section="Prédiction, porte GC",
    avant="« g brut (champs seuls) d'une sonde de l'auteur > 0 »",
    apres="Ḡ_P ; lecture sur la sonde de l'agent auteur dite d'après N-068",
    commande=N068 + ", section 7 (« elle se lit désormais sur la sonde de l'agent auteur »)",
    op=("bloc", "Porte GC (hors de la colonne « réfutation » ; voir « Combinaisons ») : g brut", "borne basse à 95 % (Bonferroni) > 0.",
        "Porte GC (hors de la colonne « réfutation » ; voir « Combinaisons ») : Ḡ_P (champs seuls) d'une sonde de l'agent auteur\n"
        "> 0, borne basse à 95 % (Bonferroni) > 0 ; la bascule pré-engagée se lit sur la sonde de l'agent auteur (N-068,\n"
        "section 7).")))

A.append(dict(
    id="C-23", section="Prédiction, stabilité de rang",
    avant="bloc à deux versions sous P-019 (version recommandée ; repli) ; C-P3a par W exact seul ; C-P3b par τ des quinze valeurs ; clause « sans le bras usurpation »",
    apres="une seule version : P-021, option (A) (défaut appliqué, R-326) : C-P3a par W exact et rééchantillonnage centré ; C-P3b sur les écarts intra-famille ; trois lectures de la loi nette ; clause de repli mécanique ; replis et clause « sans le bras » retirés",
    commande="`registres/decisions.md`, P-021 (l. 399) et R-326 (l. 535) ; archive, CL5-methode-02 et -03 (`0c492f02…`) et CB6-methode-courte-01, -02, -06 (`45a0d875…`) ; décision D-9 pour la troisième lecture",
    op=("bloc", "**[Décision de Lazar en attente : P-019 ; défaut le 2026-10-22 vers 21:15 UTC]** Version recommandée (P-019,", "Écart à la décision N-005 (prédiction 3), décidé par Lazar (P-019) et déclaré.",
        "Version retenue : P-021, option (A) (`registres/decisions.md` ; elle remplace P-019, jamais transmise ; transmise à\n"
        "Lazar le 2026-10-21 vers 00:30 UTC ; défaut à 48 heures appliqué, R-326) : valeurs p exactes et par rééchantillonnage\n"
        "centré, lecture « établie / non établie », sans verdict de réfutation ; clause de repli mécanique. La ligne P-021 du\n"
        "registre dit « les trois avec et sans calibrage » (deux lectures) ; ce texte en exige trois, ce qui est plus strict\n"
        "(décision D-9).\n"
        "\n"
        "| id | grandeur | établie | réfutation |\n"
        "|---|---|---|---|\n"
        "| C-P3a (HC1, stabilité de rang) | W de Kendall : rang des trois juges par Ḡ de la loi nette du témoin, concordance entre les cinq familles, corpus A ; valeur p exacte (7 776 affectations) | p exact ≤ 0,05 (il faut W ≥ 0,64, p = 0,0394 ; mesures de conception bbad099d… ; vérification `18961a7c…`) et p par rééchantillonnage centré ≤ 0,05 : dans chaque tirage par tâches (point 11), W* sur les rangs des écarts Ḡ*_{j,f} − Ḡ_{j,f}, p = (1 + #{W* ≥ W}) / (B + 1) ; les familles partagent des témoins (Plan, section 2), ce qui corrèle les Ḡ d'un même juge d'une famille à l'autre (contre-lecture méthode du brouillon 5, simulations T2 et T2c, `0c492f02…`) | aucune : avec trois juges et cinq familles, W ≤ 0,20 a une probabilité 0,63 sous le nul ; p > 0,05 se lit « stabilité de rang non établie » (P(W ≤ 0,20) = 0,6327 : contre-lecture méthode, S3, `720460a6…` ; vérification `18961a7c…`) |\n"
        "| C-P3b (HC1, invariance au corpus du rang des juges) | τ de Kendall entre les quinze écarts intra-famille nets du corpus A (Ḡ_{j,f} moins la moyenne des trois juges de la famille f) et les quinze du corpus B ; τ des quinze valeurs (100 000 permutations) rapporté sans verdict, comme concordance des profils | concordant : p unilatéral ≤ 0,05 par rééchantillonnage centré des deux corpus (τ* entre les écarts intra-famille de Ḡ*_A − Ḡ_A et de Ḡ*_B − Ḡ_B, tirages indépendants par tâches et par items ; p = (1 + #{τ* ≥ τ}) / (B + 1)) | aucune ; p > 0,05 : « non établie » |\n"
        "| C-P3c (HC1, invariance à l'attaquant) | W de Kendall des trois juges, quatre évaluateurs : gain d'écart brut des juges sous le plaidoyer de l'agent (Ḡ_P ; TC.2 ; consigne A, mode direct), gain d'écart brut des juges sous l'usurpation de l'agent (TC.3 b ; même lecture), Ḡ net de la famille 1 et Ḡ net de la famille 4 (TC.1, corpus A) ; rangs seulement ; valeur p exacte (1 296 affectations) | p exact ≤ 0,05 (W ≥ 0,8125, p = 0,0417 ; vérification `18961a7c…`) | aucune ; p > 0,05 : « non établie » |\n"
        "\n"
        "**Trois lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des familles 1 et 4 dans C-P3c), les trois\n"
        "statistiques sont calculées sur la loi nette calibrée, sur la loi nette sans calibrage (ρ = 1) et sur la loi nette\n"
        "calibrée par ρ̂/r̂ (X_i = v̄₀ + (ρ̂/r̂)(v₀_i − v̄₀), ρ̂/r̂ borné à [0,05 ; 1], ρ̂ et r̂ du point 8 bis recalculés dans\n"
        "chaque tirage), mêmes tirages ; « établie » seulement si les trois lectures concluent. Les deux premières ne suffisent\n"
        "pas quand les juges n'ont pas le même modèle d'erreur : sans écart vrai, elles ordonnent alors les juges dans le même\n"
        "sens (vérification courte de méthode de la session 16, `45a0d875…`, simulations U1 : « établie » dans 0,081 à 0,136\n"
        "des essais pour C-P3a et 0,070 à 0,125 pour C-P3b sous le nul à g = 0,20 ; U3 : 0,008 à 0,043 aux trois lectures ;\n"
        "taux sur données simulées, non rejoués par ce rédacteur, à rejouer par la contre-lecture : verrou 7 ; réserve 15).\n"
        "\n"
        "**Clause de repli mécanique.** Si la contre-lecture de méthode d'avant le scellement (sous-agent neuf, verrou 7)\n"
        "trouve, pour C-P3a, C-P3b ou C-P3c telle qu'écrite (toutes ses lectures jointes), un taux de « établie » au-dessus de\n"
        "0,05 + 2 × √(0,05 × 0,95 / R) (R essais de la case, au moins 1 000) dans au moins une case de la grille qui suit, cette\n"
        "statistique est rapportée sans verdict, écrit tel quel, sans nouveau nœud. Grille : k = 3 et 5 ; 45 et 60 tâches ;\n"
        "corpus B de 30 items ; aucune attaque, puis même attaque chez les trois juges (g = 0,10 et 0,20, λ = 1) ; chaque juge\n"
        "sous l'erreur sur v₀ (écart type 0,3 à 0,6), sous la compression (κ jusqu'à 0,16) ou sous leur mélange, les trois\n"
        "juges pouvant différer ; vrai rééchantillonnage par grappes (au moins 1 000 tirages, mêmes tirages pour les trois\n"
        "juges). Résultat cité avec le chemin et l'empreinte du rapport.")))

A.append(dict(
    id="C-24", section="Prédiction, contre-indices déclarés",
    avant="puce « Sondes lectrices déplacées… : un g_lecteur positif n'invalide pas HC2 » ; aucun contre-indice sur une sonde du modèle qui écrit ; aucun contre-indice du niveau 3",
    apres="puce des sondes lectrices complétée (Karne ; Kale et Vishwanath ; 2602.00750 ; 2609.36490) ; puces neuves : destination, forme, stabilité de rang (dont 2611.04556, R-2554), gain instable, instrument, sonde lue sur le modèle qui écrit (2608.21664), consignes d'évasion (2611.10620, non opposable ; 2602.08877, hors périmètre), même signe publié et non opposable (MIRAGE ; 2609.03035 v2), HC2b, HC3 composante 1",
    commande=N068 + ", section 6 (table et lecture d'ensemble) ; " + N3 + ", section 4 ; R-2554 ; rapports des lots 1, 3-A, 7-C et C9 (branches, empreintes aux « Documents »)",
    op=("bloc", "- Sondes lectrices déplacées par des attaques de contenu (2511.00554, p. 3 ; 2601.11516, p. 12 ; 2509.21344) : un", "g_lecteur positif n'invalide pas HC2.",
        "- Sondes lectrices déplacées par des attaques de contenu (2511.00554 v1, p. 3, 6, 7, 11 ; 2601.11516 v4, p. 12-13 ;\n"
        "  2509.21344 v2 ; 2609.36490 v1, p. 5, 9, 17, 23) ; une réécriture naturelle, sans attaquant, déplace des sondes lues\n"
        "  sur le modèle lecteur de 2,4 et 3,8 écarts types de lecture de la nocivité (Karne, 2609.05797 v3, p. 1, 5, 6, 22) ;\n"
        "  un suffixe ajouté au contenu évade cinq sondes du lecteur à la fois (93,91 % et 99,63 %), avec le gradient, donc\n"
        "  avec lecture des poids (2602.00750 v2, p. 1, 3, 4) ; une sonde d'exposition suit la position dans la conversation\n"
        "  et les longueurs, qui atteignent seules 0,91 à 0,98 d'aire sous la courbe (Kale et Vishwanath, 2610.18408 v1, p. 1,\n"
        "  4, 5, 12) (N-068, section 6) : un g_lecteur positif n'invalide pas HC2.\n"
        "- **Sonde lue sur le modèle qui écrit (HC2).** Une consigne en langage naturel fait tomber la détection d'une sonde\n"
        "  linéaire à 5–21 % à 1 % de faux positifs, sans optimisation ; phrase imposée, recopiée ; consigne coopérative,\n"
        "  donnée ouvertement, concepts anodins, moniteurs non durcis (Kowalski, Fonseca Rivera, Macar, Africa, 2608.21664 v1,\n"
        "  p. 4, 6, 7 ; pages 1 à 10 lues sur 18). C'est, selon N-068 (section 6), la seule pièce opposable où la sonde lit le\n"
        "  modèle qui écrit ; HC2 est « rendue moins probable ». La prédiction peut échouer dès qu'un agent veut déplacer la\n"
        "  sonde et connaît le concept visé (rapport C9, § 6, point 4) ; d'où le bras « contrôlabilité » (Métrique, point 19).\n"
        "- Agents prévenus puis priés d'évader par consigne : rappel à seuil fixe de 0,87 à 0,71 (prévenus) puis 0,55 (priés\n"
        "  d'évader), aire sous la courbe presque inchangée, recalibrage qui rattrape l'essentiel ; **non opposable** (valeur\n"
        "  de base sans ligne correspondante ; Mohsin et Rahman, 2611.10620 v1, p. 22). Par une consigne système seule, trouvée\n"
        "  en 100 évaluations au plus, deux lectures internes du modèle cible sont trompées (succès de l'auditeur à 1 % et\n"
        "  1,8 %) ; **hors du périmètre strict** : pas de sonde de tromperie entraînée, consigne et non contenu écrit par\n"
        "  l'agent (Daniels et collègues, 2602.08877 v2, p. 4, 5, 14, 17, 18).\n"
        "- **Même signe que la prédiction, publié, non opposable** : MIRAGE (formulation imposée à la section « Hypothèse » ;\n"
        "  six essais sur 120 seulement réussissent l'exfiltration, donc « 0 sur 120 » vaut « 0 sur 6 » ; N-068, section 3) ;\n"
        "  et Ponde, Das, More, Gupta (2609.03035 v2, p. 1, 2, 8, 10, 29) : par le contexte seul, l'aire sous la courbe des\n"
        "  sondes ne s'effondre pas ; un juge de sortie baisse plus que la sonde sous avertissement (0,74 à 0,68 contre 0,92 à\n"
        "  0,90 ; 14 puis 8 épisodes positifs) ; sans contenu adverse destiné au moniteur, sans g. Le sens de l'effet d'un\n"
        "  avertissement est opposé entre 2609.03035 v2 et 2611.10620 : les deux ne se citent pas ensemble comme un fait\n"
        "  (N-068, section 6). Un résultat de ce texte qui confirmerait HC2 ne s'appuie sur aucune de ces deux pièces.\n"
        "- **Destination (C-P1).** Sous pression après décision, des juges se renversent (0,194) mais pas vers la cible\n"
        "  nommée, écart signé de −0,018 ; deux juges d'une famille, verdict binaire (2606.05384, p. 2). En réseau non\n"
        "  adverse, la destination est le biais propre du modèle (2606.18276, p. 1, 8). C-P1 peut échouer ; l'attracteur\n"
        "  propre a_j et la destination témoin sont rapportés pour cela (Métrique, point 10) (niveau 3, section 4).\n"
        "- **Forme de la loi.** Dose concave, en logarithme (2602.13568, p. 3) ; réponse « à seuil », pente proche de zéro\n"
        "  (2608.25869, p. 1, 6) (niveau 3, section 4). Rapporté par l'audit A7, sans verdict.\n"
        "- **Stabilité de rang (C-P3).** Les rangs ne se transfèrent pas d'un corpus à l'autre (2608.12645, p. 9) ; le rang\n"
        "  des cibles s'inverse entre deux environnements pour un même attaquant (2611.04556, p. 58-59, 11 : contre-indice\n"
        "  porté ici par décision de Lazar, R-2554) ; le taux de bascule d'un même juge va de 0,0 % à 87,6 % selon la consigne\n"
        "  (2507.08794, p. 9, 31) (niveau 3, section 4) ; la même famille abaisse un relecteur et relève l'autre (2606.13757,\n"
        "  p. 9 ; rapport C9, § 6). C-P3 n'a pas de verdict de réfutation ; « non établie » est une issue possible, écrite\n"
        "  telle quelle (décision D-13).\n"
        "- **Gain instable.** Jusqu'au signe, et proche de zéro sur les modèles forts (Panin, p. 7, 11) ; déplacements\n"
        "  négatifs sur un juge textuel (2611.04556, p. 58) (niveau 3, section 4).\n"
        "- **Instrument.** La probabilité peut monter sans que le verdict suive (2610.29178, p. 11, 13 ; rapport du lot 7-C,\n"
        "  § 7) : la part des contenus dont le jeton de verdict le plus probable change est rapportée (audit A7).\n"
        "- **HC2b.** Sur une sonde lectrice, la forme la plus manœuvrière d'une requête baisse le score (Karne, p. 6 ; rapport\n"
        "  du lot 1, § 3.2) : signe contraire, sans agent ni sonde de l'auteur. L'effort de ne pas penser à un concept laisse\n"
        "  un résidu faible, qui passe sous le seuil de détection (2608.21664, p. 6 ; rapport C9, § 3.6). Une sonde sur un\n"
        "  agent sous injection lit d'abord l'exposition, pas l'engagement (2610.37679, p. 1, 7 ; N-068, section 5) : d'où le\n"
        "  témoin lexical par lecture forcée (Métrique, point 14). La signature d'une manipulation s'efface par entraînement\n"
        "  (2609.36490 ; N-013, section 5).\n"
        "- **HC3, composante 1.** Sous une consigne « le contenu est une donnée », des juges de 8 à 9 milliards de paramètres\n"
        "  obéissent encore à des ordres en bande, 0,65 à 0,90 sur un modèle (2610.29178, p. 26 ; niveau 3, section 4). C-P5\n"
        "  mesure la détection (score d'alarme), non l'obéissance ; le verdict de suspicion sous protocole est rapporté à\n"
        "  côté (TC.3 a).")))

# Proposition A — Tour III.1 : les nœuds en attente au 31 octobre 2026

## 0. Pièces absentes ou coupées (une ligne chacune)

- Pièce 10 (`calcul-puissance-pre-pilote-course-2-v6.sortie.txt`) : **retirée** de l'envoi (budget de mots) ; je ne m'y réfère pas.
- Les décisions R-718, R-719, R-724, R-727, R-741, GO-2026-10-31-01/03/04, P-041 v2/v3, Bailey et collègues, le pilote « mélange d'équilibre » brouillon 3 : **absents des faits**, connus par la seule question → statut RAPPORTÉ (question).
- Le verdict de la question 6 (dont dépend N6) : **absent** ; SD-1 ne donne que l'état du run (7 cellules OK, 2 absences acceptées).
- S16d (loi des émetteurs, pièce 3 ne sert que S13–S15) et le texte complet de l'addendum v6 : **non servis** ; mon avis sur N1 en dépend partiellement.

## (a) Ce que la question suppose sans l'établir

| # | Supposition | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| 1 | Le diagnostic de V5 est juste (cause = définition, T2 passe) | OBSERVÉ-NON-AUDITÉ | Produits « sans compagnon » (pièce 2), une seule graine de flux pour les variantes, erreurs types naïves, aucune contre-lecture ; seul le verdict R13 (pièce 1) est VÉRIFIÉ |
| 2 | Deux lignes de la liste d'arrêt « se lisent en sens opposés » | HYPOTHÈSE | La ligne 1 prescrit « correction par une nouvelle version (R12) » ; la ligne « paramètre modifié après lecture » vise un run en cours (pièce 3). Écrire une v3 est la voie prescrite, non l'écart ; l'écart serait de **garder le même texte** avec un critère changé |
| 3 | Le vocabulaire du contrôle est absent des 37 960 concepts de Gu-Krenn (« SUPPOSÉ ») | RAPPORTÉ, scripté | SD-4 § 5 : comptage de chaînes empreinté (script, sortie TSV). Le statut peut passer de SUPPOSÉ à RAPPORTÉ ; le PDF v4 est versé (`6b3d29db…`, SD-4) — la question dit « aucun PDF » (pièce 4, antérieure) |
| 4 | Les 0,59–0,67 / 0,25–0,36 de N4 décrivent le pré-pilote | HYPOTHÈSE | Loi a priori des niches, accord 0,7, structure 0,3 : tous SUPPOSÉ (pièces 12, 13) ; I-11 (paires déjà prises) non chiffré |
| 5 | L'option (a) de N5 « est codée » | RAPPORTÉ | R-685 : v55 non contre-lue (CL20 à faire) |
| 6 | Les heures de N6 (86 / 107 / 111) sont des coûts | HYPOTHÈSE | Temps unitaires SUPPOSÉ (pièce 17, DL-2) ; aucun chronométrage réel |
| 7 | La fenêtre est l'enjeu principal de HB (N9) | HYPOTHÈSE | SD-4 § 4.3–4.5 : volume et coût inconnus (I-1), dérive « Walden », citations révisées ; aucun de ces trois n'est tranché par D-GK-1 |
| 8 | Le pilote synthétique de N10 « suggère » que le levier est la capacité | RAPPORTÉ (question) | Brouillon 3 non servi ; « racine d'essai » = pas la racine de décision |
| 9 | Les verdicts des questions 6 et 7 vaudront « collisionneur » | OBSERVÉ | SD-1/SD-2 : 2 et 3 cellules de D absentes, acceptées par l'arbitre ; un verdict à trois espèces, à déclarer comme tel |

---

## (b)(c)(d) Par nœud

### N1 — Bisociation à deux espaces

**Option : B, sous trois conditions**, confiance 0,55 (crédence propre, non un fait).

Ce que B fait bien : elle déclare le changement d'un critère de porte après lecture (R1), change les graines de validation (le diagnostic a lu 0–299 **et** 990000–990199 : les deux plages sont consommées) et garde l'ancienne grandeur en rapport. Ce qu'elle laisse ouvert : le risque CB-05 — « la rareté ne doit pas séparer vrai de faux » — n'est plus gardé par un seuil, alors que le diagnostic mesure encore ≈ 1,4 d'écart entre vrai d'opérateur et proche sur l'étiquette retenue (pièce 2, option B, inconvénient). Et T2 est « presque acquise par construction » (pièce 2) : une porte qui ne peut pas échouer ne garde rien.

**Conditions** : (1) le diagnostic reçoit une contre-lecture avec rejeu sur une autre graine de flux et compagnons (il est OBSERVÉ-NON-AUDITÉ) ; (2) la v3 ne reprend aucun chiffre lu pour fixer un seuil : le seuil de T2 est dérivé d'un calcul de puissance pré-écrit (erreur type 0,04–0,11 est une mesure lue, pas un seuil) ; (3) **l'option qui manque** est ajoutée.

**Option manquante (F)** : remplacer la mesure de *moyennes par statut* par une mesure *fonctionnelle* du risque CB-05 : un témoin **r** « rareté seule » (sélection des 12 paires par fréquence documentaire minimale de l'étiquette partagée, sans lecture de concept), calculé à la validation comme d1c et c. Le critère devient : la précision de r ne dépasse pas celle de c au-delà d'une marge (lb95 Δ(r, c) ≤ δ_r, δ_r pré-écrit). Le seuil 0,5 sur des moyennes à queue lourde est « au niveau du bruit » (pièce 2, cause 3) ; une précision sur 12 paires × 300 mondes a une erreur type calculable d'avance. C passe de « contrôle par construction » à « contrôle du risque visé ».

**Duel (B4).** H_A : la rareté de l'étiquette retenue porte de l'information de statut *exploitable par un bras* (le générateur fuit). H_B : l'écart de V5 est un artefact de mélange (jumeau exclusif, homonyme, repli) sans valeur pour un bras. Métrique : Δ(r, c) et Δ(r, d1c) en M_bien, M_moyen, sur plages de graines neuves. Contrôle négatif : miroirs de M_inertes (étiquettes de concept inertes, structure de rareté intacte) : r y doit être ≈ c. Issues : r bat c dans M_bien **et** dans M_inertes → fuite de rareté indépendante du concept, H_B falsifiée, option C (générateur) redevient nécessaire et aucune redéfinition de V5 ne suffit ; r ≈ c partout → H_A falsifiée, la grandeur de V5 est hors sujet, A/B défendables ; r bat c en M_bien seulement → rareté corrélée au concept vrai par construction : à rapporter, N doit être comparée à r (ajout à A2 ou déclencheur d'audit « N ≡ r »).

**Pire cas de B et garde** : N « adoptée » parce qu'elle lit la rareté, pas le concept → garde : lb95 Δ(N, r) > 0 ajouté aux conditions d'adoption de la Table 1 (c'est un nœud : la v3 en est un de toute façon).

**Question propre (redéfinir après lecture)** : défendable si et seulement si (i) le texte le prescrit (il le prescrit, ligne 1 de la liste d'arrêt), (ii) la nouvelle grandeur n'est pas choisie parmi celles qui passent sur les données lues (T2 l'a été : d'où la condition 3 et le témoin r, qui n'a pas été essayé), (iii) les graines sont neuves, (iv) l'ancienne grandeur reste rapportée. Sans (ii), c'est l'option D de R-660 « déconseillée » sous un autre nom.

**Pièce sans dépense qui tranche** : le texte de S16d (non servi) et un rejeu du diagnostic avec r, par un sous-agent neuf, sur une plage 991000+ déclarée. Processeur seul (≈ 50 s pour le diagnostic actuel, pièce 2).

### N3 — D-j (Gu-Krenn sans reproduction)

**Option : oui, sous renommage**, confiance 0,6 (crédence propre). La reproduction ne peut pas précéder le pré-pilote : aucun poids publié, 8–30 h de processeur par valeur d'IR ou machine louée (SD-3 R-873), et le vocabulaire du contrôle est absent (SD-4 § 5). Donc ce que D-j « sans reproduction » met au pré-pilote n'est **pas** Gu-Krenn : c'est une règle « paires de concepts jamais reliés, chacun actif » lue sur la moisson (S31), autre graphe, autre tâche (apparition, non impact : N9-1), autre domaine. Il n'y a rien à reproduire *pour ce bras* ; la reproduction (N9) valide leur méthode dans leur domaine, à part.

**Option manquante** : découpler le nom. Le bras s'appelle « jamais-reliés-actifs v1 » (règle Swanson-sans-concept) ; « inspiré de Gu et Krenn » ne figure que dans la filiation. Conséquence : A19 n'est plus une « bascule » mais le cas normal ; l'étiquette exploratoire reste.

**Pire cas** : la règle sélectionne des paires « populaire × populaire jamais reliées » = attachement préférentiel inversé ; le bras duplique le basique ou tire au sort. **Garde** : avant gel de S31, sur la moisson (sans lecture de résultats de run), l'aire de la règle contre « degré seul » pour la tâche « sera relié l'année suivante » (transposition locale de SD-4 § 4.4) ; si l'aire appariée ≤ 0,55 (illustratif), la règle est déclarée « non supérieure à un filtre de degré » dans le préenregistrement. La garde 20 (note 1 / 0 sur un extrait) éprouve le code, pas la règle.

**Duel (course, non pré-pilote)** : H_A : les fusions du bras jamais-reliés sont notées plausibles plus souvent que des fusions de paires jamais reliées appariées sur le degré et l'âge ; H_B : aucune différence. Métrique : part de fusions notées plausibles par les trois juges, intervalle à 95 % par blocs ; contrôle négatif : paires appariées tirées (graine SeedSequence). Issue : H_B falsifiée si lb95 > 0 ; H_A falsifiée si ub95 ≤ 0. Au pré-pilote, une paire par bras (S23) : aucune puissance ; la chaîne seule est éprouvée (garde 16, 20, 21), ce qui est l'objet de D-j tel que le brouillon 7 le dit.

**Ancrage** : 0 USD (programmes), moisson existante ; S31 « seuils 20 et 5 » à étalonner (pièce 9).

### N4 — Annexe du bras méta

**Option : (a), avec trois corrections internes**, confiance 0,5 (crédence propre). Le repli est la mesure probable à 6–10 fiches (pièces 12–13, SUPPOSÉ) ; le nier en changeant R-638 (c, d, e) ou le plan (b, sur devis) coûte plus qu'il n'apporte au pré-pilote, dont l'objet déclaré est la chaîne (M9 « décisive pour la chaîne »). Corrections : CA1-01 (n1–n2 dans le profil alors que le programme les fusionne : relever c(n1, n2) ou fusionner — c'est la grille, paramètre de l'annexe, pas le profil de R-638) ; CA1-03 (n5 sans partenaire : déclaré en tête) ; le résultat est nommé « chaîne éprouvée, profil non éprouvé ».

**CA1-04** : ne pas compter les jeux de données, mais par une **règle écrite et symétrique** : « toute structure que le texte I impose à presque toutes les fiches est lue, non comptée », appliquée aussi aux trois structures séquentielles (`om_somme_cumulee_temps_arret`, `om_martingale_e_processus`, `me_test_sequentiel_cusum`, pièce 12 CA1-04). L'incohérence actuelle (retirer `jd_`, garder les séquentielles) est pire que l'un ou l'autre choix. Le profil se vide davantage : à rapporter dans P14 refaite.

**Option manquante** : remplacer les trois SUPPOSÉ de P14 (loi des niches, accord 0,7, structure 0,3) par une **lecture de niches sur les fiches de la course 1** (données passées, non le run) par deux sous-agents neufs : prior empirique, accord mesuré, fréquence des structures. C'est une lecture de fiches, à déclarer (R1) ; aucune dépense d'interface payante si faite par sous-agents. Elle tranche entre les chiffres de l'annexe (n6 à 0,05) et ceux de la contre-lecture (« n6 fort »).

**Duel** : H_A : le profil « trou à structure commune » est observable à un taux ≥ P14 refaite (médiane ≥ 1 paire à 10 fiches) ; H_B : le profil est vide dans la plupart des lots (médiane 0). Métrique : nombre de paires du profil par lot, prédiction pré-écrite ; contrôle négatif : lots à niches permutées entre fiches (même composition, structure détruite) → paires du profil attendues au niveau du hasard. Issue : si le pré-pilote donne 0 paire **et** la permutation en donne autant, le profil n'est pas détectable avec cette grille (H_A falsifiée, bras à renommer en course) ; si ≥ 1 et permutation ≈ 0, H_B falsifiée. Le contraste méta/basique sur la qualité des fusions reste hors de portée du pré-pilote (une paire).

**Pire cas (a)** : en course, le bras « méta » n'est jamais le profil et la comparaison à trois bras compare autre chose que ce qu'elle nomme. **Garde** : P14 préenregistrée comme prédiction réfutable, avec la clause « taux de profil < seuil pré-écrit sur la génération 1 → bras renommé en génération 2 ». Script v7 avec I-11 (CA1-09), sans dépense.

### N5 — A21

**Option : (b)**, confiance 0,55 (crédence propre), avec (a) comme repli **déclaré** si la boîte n'est pas livrée avant les autres dépendances (DEP4–DEP6). Raison : le défaut trouvé par CL19 (copie en mémoire contournant le journal du coffre, pièce 14) est exactement le mode de défaillance que (a) laisse possible et que son artefact R5 ne couvre pas (« lecture hors journal » se teste mal : on teste ce qu'on a prévu). (b) rend A21 vrai mécaniquement : cas sain = l'orchestrateur ne possède jamais la clé ; artefact = toute demande de clé est refusée. (c) change M1 : rejetée.

**Option manquante, valable sous (a) comme sous (b)** : un **essai d'invariance par permutation** : rejouer l'orchestrateur (faux amont) avec la clé des classes permutée ; toutes les décisions de sacrifice, d'arrêt, de reprise et l'ordre des appels doivent être identiques au bit près, hors les comptes déclarés d'É3/É5. C'est l'artefact R5 de l'*intention* de CP5-08, indépendant de la voie d'accès. Les 103 mutations tuées (R-685) ne testent pas cela.

**Pire cas (b)** : la boîte est une pièce de plus, non livrée → pré-pilote bloqué ; **garde** : date butoir au gel, repli (a) écrit dans le brouillon 8 comme écart, jamais choisi en route.

**Choix de code** : 1 — confirmer (cohérent avec O12). 5 — confirmer l'exclusion, mais A5 (> 6 exclus) doit être rechiffré avec le taux attendu de « défaut non vu » (sinon A5 sonne pour une raison non prévue) ; alternative : « N non relu », compté à part. 8 — confirmer, C12 rechiffré (script v7). 10 — geler dans le préenregistrement (S18/S19 sont des critères d'arrêt A7 ; une crête laissée au code est un seuil non gelé). Portée du plafond — global pour la course (les lignes de GO le sont, R-866/R-868 RAPPORTÉ) ; S17 par génération seulement comme arrêt d'étape ; pour N = 1, les deux coïncident.

**Ancrage** : 0 USD ; faux amonts existants (table R5).

### N6 — DL-1 à DL-9

Préalable : N6 dépend de N8 ; le verdict n'est pas servi. Avis conditionnel à « rien dans ce verdict ne retire une méthode ».

| DL | Option | Pire cas → garde | Pièce sans dépense |
|---|---|---|---|
| 1 | (2) | B-θ devient un jouet synthétique → garde : contrôle négatif = mélange « leaky ReLU » du brouillon 2 (viole (2.ii), PDF p. 6 VÉRIFIÉ par l'auteur) attendu en échec ; s'il passe, le test n'est pas sensible | aucune |
| 2 | (2), avec ordre de réduction pré-écrit | 5,8 jours muraux vs G0 → garde : réduction déclarée (M § 18) | **chronométrage d'un monde par méthode** sans lecture de résultat : remplace les temps SUPPOSÉ |
| 3 | (1) **si** la puissance simulée en R2⁻ ≥ 0,8 (illustratif) ; sinon (2) + déclencheur d'audit R4 (passe R2, échoue R2⁻) | échec confondu puissance/signe (pièce 17, S20) → garde : ligne de puissance propre à R2⁻ | extension du script de règles (M § 9) |
| 4 | (1) | — | — |
| 5 | (1) | moins de puissance → table d'effet séparée, descriptive en B-hors (déjà) | — |
| 6 | **option manquante (2′)** : geler avec SUPPOSÉ, PDF lus **avant le premier run** ; toute hypothèse de M1–M3 contredite → version nouvelle avant lecture | hypothèses de mémoire fausses → garde : la ligne ci-dessus | obtention des PDF (acte du directeur) |
| 7 | (2) | — | — |
| 8 | (1) | u₃ sans sens → garde : B-θ non exécutée plutôt que u₃, à écrire | — |
| 9 | (2) + déclencheur d'audit (T2b ≈ méthode à 0,05 en O2/O3) | seuils 0,20/0,05 non sourcés retirent une qualification à une méthode juste → audit, non perte | — |

**Duel transversal** : H_A : au moins une méthode d'identification entre dans la gradation 2 (retrouve C sous R, O, H sans retenir L ni C⁰) ; H_B : seules les associations (T1) retrouvent C, avec L. Les rivales gelées par méthode existent (pièce 17) ; le contrôle négatif commun est le jumeau C⁰. Ce qui manque : un **nul sur la chaîne entière** — mondes où C est planté mais l'étiquette de vérité est permutée entre paires (plomberie) : toute méthode y doit tomber au niveau de T0 ; sinon fuite d'évaluation.

**Ancrage** : processeur, 86–111 h selon DL-2 (RAPPORTÉ, SUPPOSÉ pour les unités) ; `tigramite`, `lingam`, `scikit-learn`, torch (pièce 17).

### N9 — D-GK-1

**Option : (a)**, confiance 0,65 (crédence propre). (b) conditionne la population sur une issue lue dans la moisson et introduit un biais de sens connu mais d'ampleur inconnue, qui désétalonne les seuils 0,60 / 0,85 (fixés sans donnée, N9-1). (a) définit la population sur leur seul graphe, et la lettre du n° 261 est servie par la stratification.

**Option manquante** : (a) + **stratification des positives par année de première liaison** (2023 ; 2024 ; 2025–26), rapportée : elle répond à « liens apparus de 2024 à 2026 » sans retirer de paires. Attente pré-écrite : aires par strate à moins de 0,05 l'une de l'autre (illustratif) ; un écart plus grand signalerait que le modèle prédit surtout l'imminent.

**Pire cas (a)** : la dérive « Walden » (SD-4 § 4.5, SUPPOSÉ) change le taux d'arêtes 2023–2025 pour des raisons de base ; **garde** : le pont B2 (comptes 2020–2022 reconstruits vs publiés, tolérance pré-écrite). Second pire cas : coût inconnu (I-1 : > 50 000 pages de filtre ou 744 Go d'instantané) ; garde : devis séparé, nœud de GO.

**Duel** : déjà écrit (HB : B-i ≥ 0,85, lb B-ii > 0,60, lb B-iii > 0). Contrôle négatif manquant : **permutation des étiquettes dans chaque case d'appariement** (degré × âge) → aire appariée attendue 0,50 ; si l'attachement préférentiel apparié sort de [0,50 ; 0,60] (attente N9-1), l'appariement a échoué et B-ii n'est pas lisible. Issues : HB falsifiée si un des trois seuils manque ; « HB non réfutée » sinon ; l'issue « appariement raté » rend le test non concluant, à écrire.

**Ancrage** : réentraînement 8–30 h de processeur par IR (R-873 RAPPORTÉ) ; trois graines × trois IR → 72–270 h (dérivé des faits, illustratif) ; machine louée, nœud de dépense ; code Impact4Cast MIT, données Zenodo CC-BY (R-873).

### N10 — Robustesse adaptative dans la course

**Option : (b), avec (c) conditionnelle**, confiance 0,5 (crédence propre). (a) rouvre un texte que le pré-pilote doit éprouver et dépasse le plafond de taille : rejetée. (b) est cohérente avec N10-1 § 2.10 (convergence unanime : « aucun lancement d'arène avant la réussite du banc instrumental ») : la génération 2 part d'un pilote lu. Le mot du directeur (« si c'est confirmé ») fixe lui-même le déclencheur : **si le calcul décisif du pilote confirme**, (c) une sous-session à part sur devis, sans rouvrir le texte ; sinon (b). L'élément nouveau ne change donc pas l'option, il la conditionne.

**Ce que « confirmé » doit vouloir dire, en duel** : H_A : le levier est la capacité de la classe de moniteurs et l'archive des attaques (le coût d'attaque croît avec la classe) ; H_B : toute classe figée tombe à coût d'attaque comparable (Bailey, RAPPORTÉ). Métrique : coût de l'attaquant pour casser (requêtes, calcul) à taux de détection fixé ; contrôle négatif : mélange aléatoire à classe égale (le pilote dit qu'il ne fait pas mieux, RAPPORTÉ). Issues : coût croissant avec la classe → H_B falsifiée ; plateau → H_A falsifiée et la course 2 doit chercher ailleurs. L'examen final est approuvé (R-890) : c'est là que ce duel se joue, pas dans la course.

**Pistes au niveau méthode, si H_A est falsifiée** (leviers hors du contrôle à bas coût de l'attaquant) : (i) engagement séquentiel — la défense est mise à jour depuis l'archive **après** que l'attaquant a engagé son attaque (le protocole « défense figée » mesure le pire cas d'une défense statique, pas d'une défense qui apprend) ; (ii) signaux que l'optimiseur d'entrées ne touche pas — cohérence entre instances, environnements tenus à l'écart, redondance de lectures internes non publiées ; (iii) l'estimand « couple détection et coût » (voie 3, R-880 RAPPORTÉ) comme critère de la course plutôt que la détection seule ; (iv) la condition de non-délivrance de certificat quand la borne de continuité manque (N10-1 § 2.3), transposée : aucune fiche de défense sans déclaration de ce que l'attaquant contrôle.

**Pire cas (b)** : rien avant la génération 2 pendant que l'examen final tourne ; garde : l'axe 7 (« angles non occupés ») peut recevoir Bailey **comme pièce**, non comme question — c'est une modification de la liste fermée, donc un nœud, mais plus petit que (a).

---

## Liens et ordre

1. **N5 avant N4 avant N3** : la boîte d'É5 (N5) conditionne le brouillon 8 ; l'annexe (N4) conditionne le gel (D-h (a)) ; S31 (N3) se gèle dans le même brouillon. Les trois sont sans dépense.
2. **N1 à part**, processeur seul ; lié à la décision 1 de la synthèse (pièce 18 : « étiquette de pont indépendante du canal ») — le témoin r est précisément une étiquette lue hors du canal de concept. La v3 de N1 et le gabarit de garde-fous gagnent à être écrits ensemble.
3. **N9 avant tout devis de machine** : D-GK-1 est sans dépense ; le pont B2 et l'appariement doivent être écrits avant de louer.
4. **N6 après le verdict de la question 6** (non servi), avec le chronométrage de DL-2 fait entre-temps.
5. **N10 après le calcul décisif du pilote** ; la décision est déjà conditionnelle par le mot du directeur.

Ce qui est réfutable dans cet avis : le témoin r de N1 (il peut ne rien détecter, auquel cas A suffit) ; la lecture de la course 1 pour N4 (elle peut confirmer la loi de l'annexe) ; l'invariance par permutation de N5 (elle peut échouer sous (b) aussi, ce qui réfuterait l'idée que la voie d'accès est le problème) ; la stratification de N9 (les strates peuvent être indiscernables, et (b) devient alors sans objet).

FIN-DE-CELLULE
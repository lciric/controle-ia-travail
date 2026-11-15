# Contre-lecture (R2) — préenregistrement de l'idée 1.1, version 2, brouillon 1 (poids du nul) — v1

- Contre-lecteur : sous-agent neuf de la session mère. Je n'ai écrit ni ce brouillon, ni la version 1, ni sa contre-lecture,
  ni la preuve, ni la synthèse, ni les rendus des angles, ni leurs réfutations, ni le juge, ni les nuls v8 et v9, ni le
  préenregistrement de l'idée 1.2.
- Date (UTC) : 2026-11-15, de 20:29 à 20:50 environ (`date -u`). Dépôt `/home/user/controle-ia-travail`, `main`, tête
  `b82d5fa7` (commit du brouillon). Aucun commit, aucune poussée, aucun appel réseau ni payant ; brouillon non modifié.
- **Texte relu** : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon1.md`,
  `916985cec9ba027effa9fdcf4bf70827424a838ed875358ae213dc1f60d30b55` (égale à son compagnon).
- Lu aussi : [SYN] en entier ; [R-PROJ] § 5 ; `essai_projection_methodes_v1.py` (`m3_toutes_coupures`) ; [CL] M1 à M4 ;
  [V1] (métrique) ; [BANC-v2] (table des lignes) ; [V9] (en-tête, `detail_morceaux_groupe`, `evaluer_sur_issues`) ;
  `test_nul_v9.py` (imports) ; `selection_pari.py`, `nul_filles_v2.py`, `cycle.py` (l. 315 à 330) de la copie `94bfd92` ;
  verdict du v9 (l. 12, 31) ; note W2 (l. 44) ; `src/controle_ia/prereg.py`.
- Rien lu sous `diag/`, `runs/` de 7a ou 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/`. **À déclarer** : pour retrouver les fichiers des 37 empreintes citées, j'ai calculé l'empreinte
  de tous les fichiers suivis par git (contenu jamais affiché ; seule correspondance hors des dossiers lus :
  `sortie--fiches-validees.json` d'une course de conception, déjà cité par [SYN]).

## Verdict

**Scellable après corrections.** Six majeurs, quatorze mineurs. Aucun ne demande de refaire la conception. Le plus grave
(M1) est une voie vers un signe positif faux : la définition de I n'exclut pas les lignes de copies. Deux autres (M2, M3)
rendent la liste d'arrêt ou le banc de mutations impossibles à tenir tels qu'écrits pour la garde P4. M5 : la durée est
sous-estimée d'un facteur 3 à 4 (mesure ci-dessous), près de la borne de 72 heures.

## Ce qui tient (vérifié)

1. **R1, sections.** `controle_ia.prereg.problemes` rejoué sur le brouillon : **0 problème**. Hypothèse, prédictions
   chiffrées avec signe et réfutation, métrique, seuils, plan, critères gelés par étages, liste d'arrêt, contre-lecture :
   présents. Je n'ai pas trouvé de porte de sortie après lecture : « non jugeable » ne mène qu'à « validité non établie »,
   sans adoption ; J9⁺ retient le moins favorable des deux verdicts ; « trou » arrête toute lecture ; J9-Dc est retiré avant
   le jeu ou gardé, jamais après lecture.
2. **Compte de Holm, recompté ligne par ligne.** Classes : J8 = v8 ; J9, J9-P, J9-D40, J9-D = v9 ; La, La-P = v8 et
   coupures de l'archive ; Ld = La et partitions déclarées. Bras à maximum : J8, J9, La, Ld, J9-D40, J9-D (6) ; à
   projection : J9-P, La-P (2). Q1 : 6 + 2 ; Q2 (coupure de l'archive, hors v8) : 5 + 2 ; Q3, Q4 : 4 + 1 chacune ; Q5 : 3 + 1.
   Fatales dans Holm : **22** ; copies : **7**. Taille : Q7 (monde de Q2) 7 ; Q8 8 ; Hs 4 ; Hm 4 ; H7 1, soit **24**.
   **53 = 22 + 7 + 24** ; fatales **34 = 22 + 12** (Q9a, Q9b hors de Holm) ; P2 **31 = 7 + 24**. Exact.
3. **Annexe A.** Script et sortie absents du dépôt, mais recopiés en entier : extraits du texte, ils donnent exactement
   `d7408ee1…f83f3` et `7907a1c9…2051`. Rejoué par moi (`scipy`) : sortie identique à l'octet. Seuils 29/74, 38/63, 527, 63
   et 29 : justes.
4. **Empreintes (R6).** Les 37 empreintes entières du texte sont recalculées. 35 correspondent au fichier nommé. Les deux
   autres sont celles de l'annexe A (point 3). Les chiffres repris de [SYN], [R-PROJ], [R-LIB], [PROJ] § 8, du verdict du v9
   (l. 12 et 31 : 0,105 ; [0,0894 ; 0,1223]) et de la note W2 (l. 44 : « 0,25 à 0,29 s mesurées ») sont exacts à la source.
   Aucun chiffre de l'état de l'art n'est employé (R7).
5. **J9-D par réunion : valide, et sans gonfler la garantie.** Soit un monde membre d'un membre nommé m* et une carte
   prévisible. L'événement « J9 promeut » est contenu dans l'événement de Ville de m* sur T₈. L'événement « jumeau promeut à
   un t ∈ T₄₀ » est contenu dans celui de m* sur T₄₀. L'événement « chaque membre est rejeté à son instant » l'est aussi, par
   le seul membre m*, à t_{m*}, puisque la valeur certifiée de m* majore log P_monde. La réunion est donc contenue dans
   l'événement de Ville de m* sur T₄₀, de probabilité au plus α. De plus, « ∃t ∀m » est inclus dans « ∀m ∃t_m » : J9-D40
   est inclus dans la règle par membre, et la réunion n'ajoute rien qu'elle ne contienne déjà, à part J9 lui-même. Lire J9
   dans la réunion est nécessaire : les solveurs de T₈ et de T₄₀ partent de points chauds différents (`departs` chaînés d'un
   instant au suivant), d'où l'écart de 2·10⁻³ admis par ED. La garantie reste α. Le taux observé peut monter, mais sous α :
   les cellules de J9-D40 et J9-D sont bien dans Holm. La domination « J9 ⇒ J9-D40 ⇒ J9-D » vaut par définition. La ligne
   d'arrêt qui la vérifie est donc un contrôle de code, ce qui est correct.
6. **Seuil « regagne si borne basse ≥ 0,25 ».** Ce seuil n'est pas réglé sur une donnée de ce banc. Il est plus dur que la
   prédiction ponctuelle basse (confiance 0,45, honnête). Il est lu avec la correction de Bonferroni à trois bras (0,833 % et
   99,167 %, juste). I est fixé par J8 et J9 seuls et recalculé dans chaque rééchantillon. Je n'y vois aucune voie vers un
   signe positif, **sauf M1** (composition de I) et M4 (définition de J9⁺).
7. **Neuf désaccords.** Chacun a un traitement écrit : mesure (1, 3, 4, 5, 8, et 9 pour les bras joués) ou réserve (2, 6, 7,
   et 9 pour les bras à ensemble de confiance). La numérotation à neuf est justifiée. Réserve sur le traitement du n° 1 : M3.
8. **Préalables : bloquants dans le texte.** Première ligne de la liste d'arrêt (« préalable 1 ou 2 non levé : pas de
   jeu »), étape 0 et section « Écarts » concordent. Mais la seconde route du préalable 1 n'est pas praticable (M6).
9. **Compatibilité du v9 avec la copie `94bfd92`, essayée à sec par moi.** Copie du paquet `pole` de `94bfd92` et de
   `nul_v9.py` (`7ae450df…`, égale) dans mon dossier de travail, lancée en `python -I -B`, sans rien lancer depuis les
   dossiers de copie.
   - Les 16 noms que `nul_v9.py` emprunte (`nf.InstantsInvalides`, `TYPES_AJUSTES`, `valeurs_ajustees` ;
     `nul_v8.NulV8Refuse`, `description`, `exiger_membres_ajustes`, `membres_archive_v8` ; `sp.Cache`, `EngagementModifie`,
     `TiragesNonLies`, `calibrer`, `plan_execution_de`, `trajectoire_loi`, `trajectoire_numerateur`, `trajectoires`,
     `verifier_plan_execution`) existent tous.
   - L'import réussit. `exiger_membres_v9` accepte les membres construits.
   - Sur 3 répétitions par carte, et selon le chemin du brouillon (bibliothèque standard et `membres_archive_v9`,
     `construire_engagement_v2(…, plan_execution="ordre_naturel")`, `evaluer_sur_issues`) : une copie `si_sinon` et une
     copie par sous-population ont un log W maximal de −0,11 à 0,0 sous le v9, et de 12,9 à 26,6 sous le v8 (sans
     morceaux). Une copie de S1 donne −1,25 à −1,02. La monotonie v9 ≤ v8 tient à 10⁻⁶ à chaque instant.
   - **Lecture** : compatibilité plausible, non établie. C'est un essai de fumée, pas l'essai E9 ni les essais du v9.

## Majeurs (ancien → nouveau)

**M1 — L'ensemble I des lignes informatives n'est pas restreint aux vraies découvertes. Tel qu'écrit, il compte comme
« puissance recouvrée » la promotion de copies (R3).** « Métrique », l. 183. I est défini sur « une ligne ℓ » quelconque.
Or sur Q2 à Q5 et Q7, J8 promeut les copies (P3 : ≥ 0,90) et J9 non : δ₉ ≈ 0,9 et ces lignes sont « informatives ». La
promeut Q3, Q4 et Q5 (P4 : ≥ 0,85) : ρ_La serait gonflé par des promotions que la question de sens laisse ouvertes. J9-P ne
les promeut pas (classe du v9) : ρ_J9-P serait écrasé. L'issue (B) serait alors écrite par la composition de I. [V1] avait
la même ambiguïté ; [CL] ne l'a pas relevée.
- ancien : « **Ligne informative** : borne basse unilatérale à 95 % de δ₉(ℓ) ≥ 0,02 […]. L'ensemble I est fixé par J8 et J9
  seuls. »
- nouveau : « **Ligne informative** : ligne **parmi les 15 lignes V** (V1 à V5, trois doses), dont la borne basse […]
  ≥ 0,02. I ⊂ {V} est fixé par J8 et J9 seuls. Les lignes Q, Hs, Hm, H7 n'entrent jamais dans ρ, ni dans un gain réuni, ni
  dans la décomposition du prix. » Reporter « I ⊂ {V} » dans P5 à P11, à l'étage 3 et dans « Comparaisons ». Ajouter une
  mutation : « une ligne Q admise dans I ».

**M2 — Garde P4 : la liste d'arrêt interdit ce que les formes « gel » et « sans garde » exigent, et le gel change la carte
jugée sans que ce soit écrit.**
- Pour J9-P avec gel, les projections sont « calculées au début de chaque bloc, sur les seules issues des blocs passés ».
  Ce sont des issues fraîches. La ligne d'arrêt (l. 465) arrête le run dès qu'une issue fraîche est « lue par la fonction
  qui bâtit […] un journal de projection ». La garde de code « empreinte du journal écrite avant que le générateur des
  issues fraîches soit créé » est elle aussi impossible pour le gel.
- J9-P-nu calcule projection et certificat « sur les lois que la carte a réalisées », donc sur des lois qui dépendent des
  issues du bloc. Il contrevient à l'esprit de la garde d'accès, et l'exemption « hors des bras sans garde déclarés »
  n'existe que pour la ligne P4.
- Le gel fait juger une **autre carte** (la loi arrêtée au début du bloc). Une promotion sous gel n'est pas celle de la
  carte soumise, et J9 juge la carte réelle sur les mêmes lignes. Le texte dit « ce qui change ce que la carte parie », sans
  en tirer la conséquence.
- Le numérateur de W^reste sous gel n'est pas dit. Le minimum reste valide dans les deux cas, mais il faut un seul choix,
  écrit.
- ancien (liste d'arrêt) : « une issue fraîche tirée avant le gel, ou lue par la fonction qui bâtit un engagement ou un
  journal de projection | arrêt ; défaut »
- nouveau : « une issue fraîche tirée avant le gel ; ou lue par la fonction qui bâtit un engagement ; ou, pour un bras à
  projection, une issue du bloc b (ou des blocs suivants) reçue par la projection ou le certificat du bloc b. Exceptions
  déclarées, et elles seules : sous gel, la projection du bloc b reçoit exactement les issues des blocs < b, et son
  empreinte est écrite avant le tirage du bloc b (générateur par bloc) ; J9-P-nu sur Hs, Hm, H7 seulement | arrêt ;
  défaut ». Ajouter son essai sain et son artefact.
- ajouter au bras 3, *Garde P4* : « Sous gel, numérateur de W^reste = la carte gelée (même statistique que la projection).
  Une promotion sous gel porte sur la carte gelée, pas sur la carte soumise ; elle ne vaut que comme contrôle de validité.
  Toute adoption de cette forme est une question de sens, pour le nœud. »

**M3 — Le témoin de la garde P4 (H7) et le banc de mutations ne sont pas définis sur le même objet, et Hs est aveugle par
construction (point de doute « dent de H7 dans le juge complet »).**
- H7 « ne passe pas par `valider_loi` : elle n'est jugée que par le module de projection » (l. 264 à 266). Le « J9-P » de
  H7 est donc le terme projeté seul, min_F Σ_b log e_{F,b}, sans W^reste. Or le texte le traite comme J9-P (dent à l'étage
  7, cellule de Holm sous gel). Pour la taille, c'est sans danger : le terme projeté majore la richesse de J9-P, donc
  « tenu » sur ce terme vaut « tenu » pour J9-P. Pour la dent, c'est la dent du module, pas celle du juge complet.
- Le juge complet est pourtant calculable sur H7 : le numérateur Σ log q_s(y_s) vient du code du banc, et les membres
  ordinaires et log-linéaires ne dépendent pas de la carte. Ce calcul répond au doute de l'auteur.
- La mutation « garde P4 retirée (tuée par H7) » doit être tuée à l'étape 0. Aucun critère de mort n'est écrit (combien de
  répétitions, quel taux). Si la dent est faible dans le juge complet, la mutation survit et « une mutation survit → pas
  de jeu » bloque le run.
- **Hs ne peut pas promouvoir sous J9-P-nu**, quel que soit le trou. Son monde est uniforme, et le membre ordinaire
  « uniforme » de `BIBLIOTHEQUE_STANDARD` est dans W^reste. Le minimum est donc borné par le rapport de la carte au monde,
  qui obéit à Ville ([R-PROJ] § 5, limite (i)). **Hm** est le réglage 4 de [R-PROJ] : 0/2 000 sans garde. Le verdict « trou
  atteint par la grammaire » est donc presque inatteignable, et l'autre type qui lit l'historique (`moyenne_glissante`)
  n'est pas essayé du tout. Dans le juge de production v1, le membre « urne » couvrirait encore `sans_remise` (cycle.py,
  l. 318 à 327 : sans urne, ces cartes sont refusées au gel). Le banc emploie `BIBLIOTHEQUE_STANDARD`, sans urne : écart de
  montage à déclarer.
- ancien (Seuil) : « **> 0,05** (au moins 63 sur 1 000) pour […] J9-P sans garde sur H7 »
- nouveau : « Sur H7, deux quantités : **(i)** le terme projeté seul, min_F Σ_b log e_{F,b} (« témoin de code ») ; dent :
  borne basse > 0,05 ; **(ii)** J9-P-nu complet, minimum avec W^reste, numérateur calculé par le banc : rapporté, sans
  seuil. La cellule de Holm « J9-P avec gel » sur H7 porte sur (i), qui majore J9-P. »
- ajouter à l'étape 0 : « Mutation "garde P4 retirée" : tuée si, sur 200 répétitions de H7 aux graines (97, k), le terme
  projeté sans garde promeut au moins 20 fois et le terme projeté sous gel 0 fois. Ce sont des essais du code, jamais lus
  comme résultat. »
- ajouter (lignes du banc) : « Hs est aveugle sous J9-P-nu par construction (membre "uniforme" dans W^reste). Elle éprouve
  W^reste, pas le trou. » Ajouter une ligne **Hg** de la grammaire : monde `melange`([S1, S2], [0,5 ; 0,5]), carte
  `melange`([M, `moyenne_glissante`, fenêtre 5], [0,5 ; 0,5]), jouée comme Hm (4 cellules de plus : Holm passe à **57**,
  P2 à 35, seuils de l'annexe A recalculés). À défaut, écrire en réserve que `moyenne_glissante` n'est pas éprouvée.

**M4 — La lecture J9⁺ de la principale n'est pas définie : c'est un choix laissé ouvert après lecture.** « Métrique »,
« Sensibilité J9⁺ » ; étage 4. Il n'est pas dit si ρ⁺ remplace J9 par J9⁺ au numérateur seulement, au dénominateur
(δ₉⁺ = J8 − J9⁺) aussi, ni si I est recalculé avec J9⁺. Les trois définitions donnent des ρ différents. La règle « le moins
favorable est retenu » ne protège pas si la définition peut encore être choisie.
- ancien : « Tout gain d'un bras est rapporté contre J9 **et** contre J9⁺. »
- nouveau : « ρ⁺_X = Σ_{ℓ ∈ I⁺} (x − b⁺) / Σ_{ℓ ∈ I⁺} (a − b⁺), où b⁺ = 1[J9⁺ promeut] et I⁺ = lignes V informatives pour
  (J8, J9⁺), recalculé dans chaque rééchantillon ; mêmes quantiles de Bonferroni. Les gains secondaires sont rapportés
  contre J9⁺ de la même façon. J9⁺ n'est pas valide : il ne sert que de comparateur. »

**M5 — Durée : l'estimation est trop basse d'un facteur 3 à 4 ; la borne de 72 heures peut invalider le run.** « Coût et
durée ». Les temps du v9 repris de la note W2 (0,25 à 0,29 s) viennent d'un autre montage. Mesuré par moi sur la machine
de la session (4 cœurs, charge environ 1), avec le code du v9 sur `94bfd92`, une archive de 4 lois softmax (le banc B v2
en a 4 : S1, S2 softmax, S3, S4 `si_sinon`), une carte softmax hors classe, 200 tirages et 3 essais : **0,9 à 2,2 s par
évaluation à T₈, et 4,4 à 5,7 s à T₄₀**. Avec J8, La, Ld, J9-P (W^reste et 402 familles), La-P et les témoins, une
répétition prend environ 7 à 9 s, et non 2,5 à 3 s. 28 000 répétitions font alors environ 55 à 70 heures d'un cœur, 28 à
35 heures sur deux processus, jusqu'à 70 heures si la machine est chargée. Il faut y ajouter le gel par bloc sur Hs, Hm et
H7, qui recalcule les projections huit fois.
- ancien : « Par répétition : 2,5 à 3 s pour tous les bras ; 28 000 répétitions : 20 à 25 heures d'un cœur, 10 à 15 heures
  sur deux processus »
- nouveau : « Temps par bras **mesurés à l'étape 0** sur 20 répétitions d'essai aux graines (97, k), sans lecture de
  promotion, et écrits dans l'addendum, avec le nombre de processus (trois au plus sur quatre cœurs) et une durée attendue
  ≤ 48 heures. Si la mesure dépasse ce budget, ne pas réduire R en silence : un texte neuf. Estimation actuelle : 7 à 9 s par
  répétition, 28 à 35 heures sur deux processus. » Garder la borne dure de 72 heures.

**M6 — La seconde route du préalable 1 est impraticable telle qu'écrite.** « Écarts », l. 495. `test_nul_v9.py` charge au
niveau du module `demonstrations/banc_tricheurs_v9.py` (l. 49 à 56), qui n'est ni dans la copie `a41b7b5` (trois fichiers)
ni dans `94bfd92`. L'import échoue avant tout essai. Les autres dépendances (`cycle.instants_reguliers`,
`outils.ecrire_scelle`) existent.
- ancien : « Elle s'établit par l'essai E9 et par les essais de `test_nul_v9.py` […] rejoués par import depuis le banc ; ou
  par le versement des dépendances au même commit »
- nouveau : « Elle s'établit, avant l'addendum, par : (a) les 16 noms empruntés par `nul_v9.py` présents dans les modules de
  `94bfd92` (liste écrite) ; (b) l'essai E9 ; (c) les essais de `test_nul_v9.py` rejoués après versement de
  `demonstrations/banc_tricheurs_v9.py` du commit `a41b7b5`, empreinté (décision de la mère), ou, à défaut, une liste
  écrite d'essais du v9 réécrits dans le banc : copie par morceaux à log W ≤ 0, identité sans morceaux avec `evaluer_v2`,
  monotonie, refus de `exiger_membres_v9`. Sinon : pas de jeu. »

## Mineurs (ancien → nouveau)

- **m1 — Deux inexactitudes de l'en-tête** (point de doute de l'auteur, confirmé).
  - (a) « tête `4b03f673` » et « rédaction de 20:14 à 20:28 » : `main` est passé à `9c3df628` à 20:15:10, pendant la
    rédaction, et le brouillon est committé à 20:27:02 (`b82d5fa7`). → « dépôt lu sur `main`, têtes `4b03f673` puis
    `9c3df628` ; rédaction de 20:14 à 20:27 ».
  - (b) « toutes recalculées […] et égales à leurs compagnons » est faux pour `selection_pari.py`, `nul_filles_v2.py`,
    `cycle.py`, `a_blanc_v59.py` de `94bfd92` et pour `src/controle_ia/prereg.py` : ils n'ont pas de compagnon. → « égales à
    leurs compagnons, ou, pour les modules de `94bfd92`, à `empreintes-copie-v1.txt` ; `prereg.py` sans compagnon,
    empreinte calculée le 15 novembre ».
- **m2 — Annexe A (R6).** Script et sortie sont « dans le dossier de travail de la session ». → les verser à côté du texte,
  avec leurs compagnons `.sha256` (les empreintes sont justes, point 3).
- **m3 — Deux pondérations coexistent** (point de doute). ρ = Σ_I Δ / Σ_I δ₉ revient à pondérer chaque ligne par sa perte
  δ₉. Le « gain réuni » donne le même poids à chaque ligne. Les deux sont légitimes, mais pas interchangeables. → ajouter à
  la « Métrique » : « ρ (pondéré par δ₉) pour les trois primaires ; gain réuni (lignes à poids égaux) pour les secondaires
  seulement ; ensemble de lignes de chaque secondaire nommé : I pour La-P/La et J9-P/La, les 15 lignes V pour J9-D et
  J9-D40 ; rééchantillonnage commun (graines (99, b)), I recalculé de même ».
- **m4 — Essai EP à 10⁻⁹ nat** (point de doute). Atteignable seulement si le module reprend `em_commun` et
  `_blocs_projection` octet pour octet, sur les tableaux mêmes du banc exploratoire. → « EP : 50 mondes de
  `essai_projection_commun_v1.py` aux graines (97, k) ; module neuf sans W^reste, avec 𝔽 = linéaire, sous-population et
  coupures z_j > c du plan (comme `m3_toutes_coupures`) ; écart ≤ 10⁻⁹ nat sur chaque log e de bloc et sur le processus
  minimum ; optimiseur repris octet pour octet (différentiel dans l'addendum) ». Sinon, choisir la tolérance maintenant,
  justifiée par écrit.
- **m5 — Seuils « près de 1 » qui divergent** : P13 dit log W ≤ 0,5 nat, l'audit des copies dit 1,0 nat. → un seul seuil
  d'audit (1,0 nat), et P13 « ≤ 0,5 » donné comme prédiction seulement.
- **m6 — Quantité fatale de J9-D** : J9-D n'a pas de W unique. → « pour J9-D, quantité fatale = max_m max_{t ∈ T₄₀}
  (log q − V_m(t)) du membre qui contient la copie ; > 10⁻⁶ : audit ».
- **m7 — J9-Dc** : à T₄₀, les coupes de `detail_morceaux_groupe` portent sur les t premières instances, et leur identité
  change d'un instant à l'autre. → « famille = coupure c du plan gelé ; sa valeur à t = borne (`bornes[sel]`) de la coupe
  que c induit sur les t premières instances ». Le coût reste celui de J9-D : les bornes par coupe sont déjà calculées.
- **m8 — « 26 partitions »** → « 26 partitions par trait et par bloc (24 non triviales, plus 2 égales à la famille
  linéaire) ».
- **m9 — Q9b** → « poids de Dirichlet(1, …, 1) sur [S1, S2, S3, S4, uniforme fixe], arrondis à six décimales et
  renormalisés (comme Q1) ».
- **m10 — Graines d'EP, ED, E9 et du chronométrage** non écrites → « (97, k), k distinct par essai, liste dans l'addendum ».
- **m11 — Montage du juge** : la bibliothèque est `BIBLIOTHEQUE_STANDARD` (juge v0, sans urne), alors que le juge de
  production v1 ajoute « urne » ou refuse les cartes qui lisent l'historique. → l'écrire parmi les « Différences de
  montage », avec sa conséquence pour Hs et Hm (M3).
- **m12 — « Sans rouvrir aucune copie »** (H-1.1) → « sans rouvrir aucune copie : chaque cellule de copie de J9-P "tenue"
  (taux ≤ α) ; une carte membre reste près de 1, pas au plus 1 ».
- **m13 — W^reste contient le membre `moyenne_glissante`** de la bibliothèque, qui lit l'historique. Sans effet sur la
  validité (minimum de deux statistiques valides), mais à dire dans la garantie de J9-P.
- **m14 — Section « Contre-lecture »** → ajouter « **Contre-lecture 2** (R2, sur le brouillon 1 de la version 2) : texte
  relu `916985cec9ba027effa9fdcf4bf70827424a838ed875358ae213dc1f60d30b55` ; rapport
  `docs/notes/organisme-idees-juge-v1/contre-lecture-idee-1-1-v2-brouillon1-v1.md`, `<empreinte de son compagnon>` »,
  forme reconnue par `prereg.ENTREE`, avec un traitement écrit de chaque remarque.

## Réponses aux questions posées par l'auteur

- **Compte des cellules** : 53 et 34, exacts. 57 si Hg est ajoutée (M3).
- **Réunion de J9-D40 et J9-D** : valide au niveau α pour la carte seule. Elle domine J9 par définition. Sa garantie n'est
  pas gonflée (point 5). Ce n'est pas une valeur e : bien dit.
- **« Famille » = membre nommé** : valide, parce que la classe du v9 est la réunion de ses membres nommés.
- **Gel de l'historique** : valide, mais il change la carte jugée (M2).
- **Seuil d'un quart** : jugement gelé, non réglé sur des données ; sans voie vers un signe positif une fois M1 et M4
  corrigés.
- **Q8 bâtie sur le plan** : légitime comme pire cas déclaré. Le monde ne lit que les instances, pas les issues : il reste
  sans mémoire.
- **Neuf désaccords** : traités (point 7). La mesure du n° 1 est à renforcer (M3).
- **Durée** : M5.

## Fichiers produits

- Ce rapport et son compagnon `.sha256`. Mes essais (essai de fumée du v9, chronométrage, rejeu de l'annexe A) sont restés
  dans le dossier de travail de la session, hors du dépôt. Aucun fichier du dépôt n'a été modifié.

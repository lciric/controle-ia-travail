# Préenregistrement — tirages frais du juge répartis par blocs avec arrêt anticipé, contre la part fixe, à tirages totaux égaux, avec placebo — v4

- Auteur : concepteur neuf (modèle A au sens de R-2851), sous-agent de la session mère ; auteur de la v1 à la v3 ; je n'ai
  écrit ni le relevé, ni les fiches, ni le juge, ni les deux contre-lectures, ni la vérification courte, ni la relecture du
  différentiel v2 → v3.
- Date (UTC) : 2026-11-15, rédaction de la v2 de 09:12 à 09:17, de la v3 de 09:27 à 09:30, de la v4 de 09:36 à 09:38 (`date -u`) ;
  dépôt lu sur `main` (tête `d9b79304` pour la v2, `53318b99` pour la v3, `ed6ff5bb` pour la v4) ; aucun commit, aucune poussée.
- Commit du code d'analyse : **aucun à ce jour** ; le code s'écrit après le contrôle du différentiel v3 → v4 et le scellement
  par `controle_ia.prereg.sceller_prereg` de la version qui fera foi ; ses empreintes entrent dans un **addendum d'empreintes**
  scellé avant tout jeu, qui ne change rien d'autre.
- Documents qui font foi (chemin + empreinte entière) :
  - version 1 de ce texte : `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v1.md`
    (`2a500156d1b36855330e02c1a261cb40c882032ebf0090760e87b7695b876a65`), gardée intacte (R12) ;
  - version 2 de ce texte : `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v2.md`
    (`c7f80e8c9fff5128ca60a1071b70519844a2f9ccdd9344f0ece0aab0e3e13c2b`), gardée intacte (R12) ;
  - vérification courte du différentiel v1 → v2 (« scellable après corrections ») :
    `docs/notes/organisme-idees-juge-v1/verification-courte-prereg-tirages-repartis-v2-v1.md`
    (`229b183a04ea7ec822ac59394e6f4258d85ad3f3ba3c769a7b8b750d6bcd4a7f`) — ci-dessous **[VC]** ; son programme de recalcul
    (`d1066eaa4aa48badf2fd2f2cda93e37ef5379fcbcb3e689dec7ae60e3f7769ba`) et sa sortie
    (`48371611b7ffeeceb0790568c4cf4276b63295e3cca2cac2120a4f71e3944347`), recopiés dans son annexe ;
  - version 3 de ce texte : `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v3.md`
    (`28aab53951c9911586113d9acffcdca319ab67554ae08f93804154dcee04707e`), gardée intacte (R12) ;
  - relecture du différentiel v2 → v3 (« scellable après corrections ») :
    `docs/notes/organisme-idees-juge-v1/relecture-differentiel-prereg-tirages-repartis-v3-v1.md`
    (`6a71e24d6f764b0a43639fd03f03a3a49e92eb2d7dd51d8837fc5e57e4cf7cbe`) — ci-dessous **[RD]** ;
  - contre-lecture de la v1 (« scellable après corrections ») : `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1.md`
    (`5ae17f81cbeb83161e49d7d3ce5c8fa4ff38c4db9d38afd7cfc5b8ae676df109`) — ci-dessous **[CL]** ; son programme
    `contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py` (`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`)
    et sa sortie `sortie-essai-validite-20000-v1.txt` (`25a9e2e1dd9fd2c76b61b8b5f387936dd0f72f28b25a220a733b2927451aba9f`) ;
  - contre-lecture du banc B v1 et de la preuve : `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md`
    (`763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e`) — ci-dessous **[CL-1.1]** ;
  - banc B v1 : `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`
    (`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`), « Plan d'analyse », « Banc B », et son annexe B
    (essai à blanc du montage) — ci-dessous **[BANC-v1]** ; **le banc B v2 est défini ici pour ce qui sert à l'idée 1.2**
    (section « Plan d'analyse ») ; ce que ce texte ne répète pas (C_decl, archive A0, colonne « classes qui contiennent M »,
    bras et lectures de l'idée 1.1) reste celui de [BANC-v1] ; le préenregistrement de l'idée 1.1, en sa version 2, le reprendra
    tel quel ou déclarera ses écarts (décision de la mère, R-2881) ;
  - preuve, théorème 1 : `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md`
    (`44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2`), § 4 — ci-dessous **[PREUVE]** ;
  - relevé, § 1.2 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) ; fiches opus-p1-01 (n° 5) et argon-p1-05 (n° 4) de
    `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
    (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) ;
  - juge, copie `94bfd92` : liste `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/empreintes-copie-v1.txt`
    (`0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df`) ; sous `…/orchestrator/pole/` : `a_blanc_v59.py`
    (`606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c`), `nul_filles_v2.py`
    (`0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910`), `nul_v8.py`
    (`cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888`), `cycle.py`
    (`798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18`), `selection_pari.py`
    (`359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc`) ;
  - texte scellé de la boucle réelle (200 tirages par carte) : `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md`
    (`80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d`) ;
  - verdict de la course v67 : `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`
    (`d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459`) ; faits du collisionneur :
    `docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md` (`d19b540015ed9480774c020cd7f1a527db32d42600a5bc2bd34c92c17d7be0b3`) ;
  - recoupement : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`
    (`eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172`) ; synthèse :
    `docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md` (`5fd7e26fc8c04ddd131bcd5b9c03afd118ccd6bd8458e90f1aa6685a51f9517a`) ;
  - décisions : `docs/decisions/decision-N-045-v2.md` (`c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`),
    `docs/decisions/decision-N-058-v1.md` (`854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`),
    `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`) ;
    registre : R-2851, R-2875, R-2878, R-2881, R-2884, R-2885 ;
  - voisins publiés, PDF au dépôt : `docs/sources/pdf/2606.08106v1.pdf` (`779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f`) ;
    `docs/sources/pdf/2512.03109v2.pdf` (`b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828`) ;
    `docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf` (`2a8ded0119a1db422aa548fdc3be80b2861f0548bc8166256be60572a2fddb03`) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ;
    validateur `src/controle_ia/prereg.py` (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`).

**Statut.** Version 4, **scellée par empreinte (R6)** ; elle porte sur la v3 les deux corrections P1 et P2 de [RD] et ses sept
remarques non bloquantes, rien d'autre ; la v3 portait sur la v2 les corrections C1 à C8 de [VC] et sa réserve R-a, en deux
parts ; la v2 portait les trois majeurs et les quatorze mineurs de [CL], la ligne V5 du banc B v2 décidée par la
mère (R-2875, [CL-1.1] M1) et deux mineurs de [CL-1.1] qui touchent le banc (m1, m2). Elle attend un **contrôle du seul
différentiel v3 → v4** (mécanique, borné aux lignes du tableau ci-dessous), puis le scellement par `sceller_prereg`. **Aucun jeu avant.** Processeur seul, sans dépense
(R-2851). Aucun résultat du banc n'existe. **Lieu** ([CL] m14) : la version qui fera foi sera recopiée octet pour octet sous
`prereg/organisme-idees-juge-tirages-repartis-vN.md` au scellement décisif, comme le demande le gabarit ; la pièce de ce
dossier reste en place (décision de la mère, R-2881).

## Différentiel v3 → v4, point par point

Source : [RD] (P1, P2, remarques 1 à 7). Traitement : **acceptée** ; rien d'autre ne change (aucun seuil, aucun calcul neuf).

| # | remarque de [RD] | ce que fait la v4 | où |
|---|---|---|---|
| P1 | sortes de la famille N non désignées pour la lecture (3) | six sortes nommées (voisines, membres exacts, porteuses construites, copies par morceaux, fausses construites, nulles) ; moyenne lue par bras toutes cartes réunies (7 intervalles) et par sorte dans chaque bras (42) ; seuls ces 49 intervalles comptent ; fausse alerte possible, du côté prudent, dite ; même mot à la Métrique et à l'étage 1 | Métrique ; Seuil ; Critères (étage 1) |
| P2 | règle des deux fausses construites de la famille N | S1 portant une composante de même type et de même dose, tirée indépendamment, retirée tant que son cosinus avec la composante de la cellule (celle des porteuses construites) dépasse 0, même formule et même plafond qu'en famille T, V4 compris ; nulles : softmax aléatoires | Plan (famille N) |
| 1 | Statut : « deux de ses réserves » | « sa réserve R-a, en deux parts » ; statut de la v4 | Statut |
| 2 | clé `(97, g)` absente de la section Graines | ajoutée | Plan (graines) |
| 3 | bras et intervalle du jeu d'essai synthétique | sans allocation, valeur e = maximum sur les 32 instants (comme X2 du programme `01c648a0…`) ; borne basse de l'intervalle percentile à 95 %, 10 000 rééchantillons des 20 000 générations | Métrique (réserve (a)) |
| 4 | quatrième issue de l'étage 4 absente des issues (R3) | phrase ajoutée (Q4 et Q5 fausses ensemble) | Prédiction (« Ce que serait chaque issue ») |
| 5 | M₀′ jamais tempéré par morceaux | dit : l'épreuve de validité ne voit pas de monde tempéré par morceaux ; S3, S4 restent parmi les membres exacts | Plan (famille N) |
| 6 | jeu de 20 000 générations absent du Coût | ajouté (processeur seul, sans juge, durée non mesurée, dans la borne de 24 heures) | Coût |
| 7 | « Contre-lecture 4 » | entrée ajoutée, [RD] par empreinte entière, traitement ; « À venir » mis à jour ; [RD] et la v3 ajoutées aux documents qui font foi, R-2885 au registre cité | Contre-lecture ; en-tête |

## Différentiel v2 → v3, point par point

Source : [VC] (C1 à C8, réserves R-a à R-d). Traitement : **acceptée** sauf mention. Aucun seuil chiffré n'est changé ; aucun
calcul neuf (les seuils par monde sont ceux que [VC] a recalculés).

| # | remarque de [VC] | ce que fait la v3 | où |
|---|---|---|---|
| C1 | qualifications d'un gain non exclusives | quatrième issue écrite : si les deux bornes hautes sont sous leur seuil, « d'effectif seulement et sans effet de ciblage » ; étage 4 à quatre issues | Seuil ; Critères |
| C2 | lectures de validité « par monde » sans critère | option 1 du rapport : lectures **jugées** sur les 500 générations ; **rapportées sans critère** par monde (250 ; pour mémoire tenue ≤ 4, non tenue ≥ 23) ; la lecture (2) vaut dans chaque monde ; une borne basse de moyenne > 1 dans un seul monde déclenche l'audit écrit (R4), non un verdict | Métrique ; Seuil ; Critères (étage 1) |
| C3 | répartition des deux mondes de la famille N | M₀ pour g de 0 à 249, M₀′ pour g de 250 à 499 ; 25 générations par cellule et par monde | Plan (famille N) |
| C4 | loi de base des voisines non désignée ; « Δ centrée » perdue | M₀ : S1 (comme en v1) ; M₀′ : loi d'archive **tirée parmi S1 et S2** (changement sur la v2, qui tirait parmi S1 à S4 : S3 et S4 sont des `si_sinon` sans W_k unique), c'est elle qui est déplacée ; Δ ~ N(0, 1) centrée par colonne, une par carte. Précision non exigée, ajoutée : composition des 8 membres exacts (1 + 4 + 3) et des 8 autres cartes (2 + 2 + 2 + 2) | Plan (famille N) |
| C5 | tableau du différentiel v1 → v2 incomplet | deux lignes ajoutées à ce tableau (garantie alignée sur [CL] § 1.1 et 1.2, confirmation, Q9 ; autres retouches, dont les phrases retirées) ; banc recopié complété (j uniforme en Q5 et V2, lois de Δ et de u) ; portée du banc écrite en tête (ce qui n'est pas répété reste celui de [BANC-v1]) | en-tête ; Différentiel v1 → v2 ; Plan (banc) |
| C6 | m14 « à confirmer » périmé | « décision de la mère, R-2881 » (Statut, tableau v1 → v2, Contre-lecture 1) ; R-2881 et R-2884 ajoutés au registre cité | Statut ; tableau ; Contre-lecture ; en-tête |
| C7 | section « Contre-lecture » | entrée « Contre-lecture 3 » : texte relu et rapport par empreinte entière, programme et sortie, traitement de C1 à C8 ; « À venir » mis à jour | Contre-lecture |
| C8 | « M à composante de signe opposé (deux) » non défini pour V4, doublon pour les autres | force × 1 et × 0,5 ; pour V4, deux fausses construites de plus sous la règle du cosinus | Plan (famille T) |
| R-a (1) | mise à mort de la mutation « valeur e au maximum » | jeu d'essai synthétique de 20 000 générations écrit (monde jouet comme [CL], graines `(97, g)`) ; sur les 500 générations du jeu, la lecture (3) peut ne pas la voir, dit | Métrique (réserves) ; Étapes |
| R-a (2) | fuite d'instants non révélés | dit : aucune des quatre lectures ne la voit sur W ; seule la garde d'accès du code et sa mutation en protègent ; ligne M3 du tableau v1 → v2 précisée | Métrique (réserves) ; tableau v1 → v2 |
| R-b, R-c, R-d | zone utile ; oracle à 20 000 issues ; consommation de P | pris en note, sans changement : déjà déclarés (zone utile acceptée ; l'essai du code dira la tenue de l'oracle avant le jeu, borne de 24 heures ; la consommation réelle de P est rapportée) | — |

## Différentiel v1 → v2, point par point

Source : [CL] (M1 à M3, m1 à m14), [CL-1.1] (M1, m1, m2), mère (R-2875, R-2878, R-2881). Traitement : **acceptée** sauf
mention. Tableau complété en v3 ([VC] C5 : deux dernières lignes ; [VC] R-a : ligne M3).

| # | remarque | ce que fait la v2 | où |
|---|---|---|---|
| [CL] M1 | « fausse » définie par l'étiquette, pas par un oracle | **acceptée**. Fausses de même type retirées tant que leur cosinus avec la composante du monde dépasse 0 ; **oracle** écrit (gain attendu de log-score par tirage sur le meilleur membre du nul v8, 20 000 instances, graine `(famille, g, 2000)`) ; une non porteuse à gain > 0 est « partiellement vraie », exclue de FP et de la couverture, comptée à part ; FP par sorte. **Ajout de ma part** : une porteuse construite dont le gain d'oracle est ≤ 0 n'entre pas dans la couverture (comptée à part) | Plan (cartes, oracle) ; Métrique |
| [CL] M2 | critères non exclusifs ; « non jugeable » sans verdict ; seuil de Q1 | **acceptée**. Principale lue dans l'ordre « nuisible », « gain », « pas de gain », « non tranché » ; « validité non établie » pour un bras « non jugeable » ; Q1 au seuil de tenue (≤ 13 sur 500, recalculé pour 7 bras : annexe B) | Seuil ; Critères ; Prédiction |
| [CL] M3 | l'épreuve de validité ne voit ni fuite d'instants ni lecture au maximum | **acceptée**. Quatre lectures de validité : part avec promotion ; **domination** log W ≤ log Λ + 10⁻⁶ à chaque instant ; **moyenne des valeurs e** (borne basse > 1 = défaut) ; **bras G** adverse ; famille N à deux mondes (mélange ; loi tempérée et inclinée, classe log-linéaire) ; mutation « valeur e = maximum de la trajectoire », tuée par la lecture (3) ; **la fuite d'instants non révélés n'est vue par aucune de ces lectures sur W** : seule la garde d'accès du code, avec son essai et sa mutation, en protège (précisé en v3, [VC] R-a) | Métrique ; Plan ; Critères ; Liste d'arrêt |
| [CL] m1 | placebo : dispersion avec remise, dépense de tout le budget | **acceptée**. Écrit que P consomme au moins autant que A ; bras **P′** (à tour de rôle sur l'ensemble élargi, arrêtées bas comprises) rapporté ; A − P′ isole l'éligibilité | Plan (bras) ; Métrique |
| [CL] m2 | « tirages totaux égaux » | **acceptée** : « au plus B », consommation rapportée, entraînement hors du compte | Métrique |
| [CL] m3 | ordre des cartes dans le dernier tour ; clés | **acceptée** : positions permutées par génération `(famille, g, 1001)` ; cellule = g mod 10 ; clés du monde `(famille, g, 24)` et de l'archive `(famille, g, 25)` | Plan (graines) |
| [CL] m4 | « doses moyennes, faibles » non définies | **acceptée** : dose haute et dose basse définies | Prédiction ; Plan |
| [CL] m5 | hypothèse de travail (ii) à contresens | **acceptée** : à v67, onze cartes ont été **promues et retenues**, variantes d'un même constat (faits, l. 34) ; la v2 appuie l'hypothèse sur la composition du banc (18 sur 24 non porteuses) et dit qu'elle ne se transpose pas | Hypothèse |
| [CL] m6 | témoin à 1,25 au lieu de 1,2 non déclaré | **acceptée** : déclaré (240 n'est pas un multiple de 25) | Plan (bras) |
| [CL] m7 | différences de montage à lister ; lecture de F sur les champs de l'évaluation à 800 | **acceptée** : liste écrite ; F se lit sur la trajectoire tronquée, jamais sur `promue`, `t_promotion`, `log_richesse_max`, `log_richesse_arretee` ; mutation ajoutée | Écarts ; Plan (étapes) |
| [CL] m8 | essai E1 trop étroit | **acceptée** : 32 instants, 50 cartes couvrant chaque sorte, instants ≤ t inchangés quand les issues au-delà de t changent | Plan (étapes) |
| [CL] m9 | portée de la garantie | **acceptée** : réserves (v) et (vi) ajoutées | Garantie |
| [CL] m10 | « Ce que cela règle » | **acceptée** : précisé (preuve facteur par facteur ; poids fixés non valides pour chaque loi du nul, essai X3 de [CL]) ; signalement à Lazar écrit | Garantie ; Écarts |
| [CL] m11 | issues contraires de Q5 à Q8 et « hors zone » ; audit « tout négatif » | **acceptée** | Prédiction ; Critères |
| [CL] m12 | empreintes abrégées | **acceptée** : 64 caractères pour chaque pièce qui fait foi (en-tête) ; Hegazy, Jordan et Dieuleveut gardée abrégée : pièce sur une autre branche, qui ne fait pas foi ici | en-tête ; Garantie |
| [CL] m13 | titre de Wang et Ramdas | **acceptée** | Garantie |
| [CL] m14 | lieu sous `prereg/` ; risque de zone utile | **acceptée en partie** : copie sous `prereg/` au scellement décisif (décision de la mère, R-2881) ; risque de zone dit | Statut ; Critères |
| [CL-1.1] M1 | aucune vraie découverte posée sur une coupure de l'archive | **acceptée par décision de la mère** (R-2875) : ligne **V5** au banc B v2 (trois doses ; compte de dimensionnement rejoué sans juge, annexe A) ; pour l'idée 1.2, V5 entre dans les types de composante (10 cellules au lieu de 8, 750 générations T au lieu de 600) | Plan (banc, familles) |
| [CL-1.1] m1 | ordre du gel et des tirages | **acceptée** pour ce texte : engagements bâtis et gelés **avant** les issues fraîches, générateur distinct ; la fonction qui bâtit un engagement ne reçoit aucune issue fraîche (essai) | Plan (graines, étapes) |
| [CL-1.1] m2 | coupure de l'archive trop proche du signe | **acceptée** au banc B v2 : coupures de l'archive retirées tant que \|s\| < 0,3 | Plan (banc) |
| conséquences | bras P′ et G | famille de validité à 7 bras (Bonferroni 0,05/7) ; seuils recalculés (annexe B) ; coût mis à jour | Seuil ; Coût |
| [CL] § 1.1 et § 1.2 (déclaré en v3) | énoncés de la garantie alignés sur les six hypothèses exactes | lemme : C1 « plans, instants, bibliothèque, m et α », C3 « ni les autres cartes », preuve « sachant G_k, de loi P*(· \| x) » ; théorème 2 : (a) « règle adverse G », (c) réécrit (cartes fraîches sur la même archive), preuve (a) « exactement les issues révélées » ; paragraphe neuf « Confirmation par la contre-lecture » (chiffres de [CL] § 1.3) ; prédiction neuve **Q9** (moyennes ponctuelles ≤ 0,8) et seuil des lectures (2) et (3) | Garantie ; Prédiction ; Seuil |
| autres retouches (déclarées en v3) | phrases retirées ; ajouts sans ligne | retirées : « Elle tranche la tension que le relevé signale (§ 1.2) en faveur de la règle » de la fiche (la tension est traitée par « Ce que cela règle ») ; « dérive à peine négative, le cas le plus dur pour la continuation » (famille N) ; « l'intérêt réel est pour les domaines où un tirage est cher » (Écarts : la fiche est citée par son champ) ; renvoi entre les deux préenregistrements inversé (le banc est défini ici, R-2881). Ajoutés : clés de graines à quatre éléments par carte et clé de l'oracle ; lignes de la liste d'arrêt (gel, domination, oracle après le rejeu) ; mutations neuves ; « aucune moyenne ni médiane sur des jetons » ; H-1.2 « au plus égal » ; banc B recopié en abrégé (complété en v3 : lois de j, de Δ, de u) | Graines ; Liste d'arrêt ; Étapes ; Métrique ; Hypothèse ; Plan (banc) |

## Hypothèse

**Contexte.** Le juge de la boucle réelle donne à chaque carte une **part fixe** de 200 tirages frais lus à 8 instants
(`a_blanc_v59.juger_carte`). Une carte qui ne porte rien consomme autant qu'une carte porteuse d'une composante faible, qui
reste sous le seuil faute de tirages (à v67, deux lois plantées vraies sont restées sous le seuil de la règle e-BH à 200
tirages : log W maximal 4,248 et 5,875 contre log(22/0,05) ≈ 6,087, verdict de v67, § 4.2 — **déclaré** : lu avant d'écrire
la v1). L'idée 1.2 (fiche opus-p1-01, règle en neuf points ; argon-p1-05, point 1) : à tirages totaux égaux par génération,
donner les tirages par blocs, arrêter tôt les cartes dont la valeur e tombe très bas ou franchit le seuil, et passer les
tirages libérés aux cartes encore incertaines.

**H-1.2.** À nombre total de tirages frais au plus égal par génération, sous le nul de production (v8), le juge à allocation
par blocs avec arrêt anticipé **couvre davantage de composantes vraies** que le juge à part fixe, **sans promouvoir davantage
de cartes fausses au sens de l'oracle** ; le gain dépasse celui d'un placebo qui répartit les tirages libérés au hasard, et
celui d'un juge à part fixe qui reçoit 25 % de tirages en plus.

**Hypothèses de travail.** (i) La validité ne dépend pas de la règle d'allocation (section « Garantie »). (ii) **Au banc, par
construction**, 18 cartes sur 24 ne portent pas la composante : l'arrêt bas devrait y libérer une part notable du budget ;
l'économie mesurée (Q7) dépend de cette composition et **ne se transpose pas** à une génération réelle. (Pour mémoire, le
fait cité en v1 disait l'inverse de ce que la v1 en tirait : à v67, onze cartes ont été **promues et retenues**, variantes
proches d'un même constat, faits du collisionneur, l. 34.) (iii) Le gain, s'il existe, se place près du seuil de détection
(borne 5 du recoupement : l'arrêt optionnel « ne le déplace qu'en dépensant plus de tirages » — ici, des tirages pris aux
cartes qui n'en ont pas besoin).

**Renvois.** Recoupement J1 (« processus de valeurs e à arrêt optionnel », survivante) ; synthèse § 9, ordre 1 ; voie bon
marché « éliminations successives » approuvée par Lazar (N-045 v2, mots de 09:35) ; ce n'est **pas** une revendication : le
principe est publié (section « Garantie », voisins).

## Garantie de validité de l'arrêt optionnel et de l'allocation

**Cadre.** Une génération de m = 24 cartes. Chaque carte i a son engagement gelé : sa loi q_i, son plan de N_max = 800
instances, ses instants de lecture 𝒯 = {25, 50, …, 800}, le nul v8 de l'archive ; et son **propre flux** d'issues fraîches,
tiré après le gel d'une graine propre. Le juge révèle les issues **par blocs de 25** ; une **règle d'allocation** choisit, à
chaque pas, quelle carte reçoit le bloc suivant ; elle ne lit que les issues déjà révélées (et, pour le placebo, un hasard
indépendant U). Hypothèse nulle : la loi du monde P* est dans la classe du nul v8 de l'archive (la même pour toutes les
cartes fraîches d'une génération).

**Lemme.** Pour chaque carte i, soit Λ^(i)_n = Π_{s ≤ n} q_i(y^(i)_s | ·) / P*(y^(i)_s | x^(i)_s) et N_i(k) le nombre d'issues
de i révélées après k pas. Si (C1) plans, instants, bibliothèque, m et α sont gelés avant tout tirage frais, (C2) les flux des
cartes sont indépendants entre eux et de tout ce qui précède le gel, (C3) le monde ne lit ni l'historique ni les autres
cartes, (C4) la règle d'allocation et d'arrêt est mesurable par rapport aux issues révélées et à U, alors M_i(k) =
Λ^(i)_{N_i(k)} est une surmartingale positive pour la filtration globale G_k (toutes les issues révélées, toutes cartes, et
U), avec M_i(0) = 1.

*Preuve.* Au pas k → k + 1, si i ne reçoit pas le bloc, M_i ne change pas. Si i le reçoit (décision G_k-mesurable), les 25 issues
neuves de i sont, sachant G_k, de loi P*(· | x) et indépendantes de tout le révélé (C2, C3) ; en conditionnant issue par issue
dans l'ordre du plan, chaque facteur q_i / P* a une espérance conditionnelle au plus 1 ([PREUVE], § 4, étape 3) ; d'où
E[M_i(k+1) | G_k] ≤ M_i(k). ∎

**Théorème 2.** Sous C1 à C4 et les hypothèses du théorème 1 de [PREUVE] pour le nul v8 : (a) pour toute règle d'allocation et
d'arrêt écrite d'avance (part fixe, arrêt bas, arrêt haut, plafond, réallocation selon les valeurs e courantes, réallocation au
hasard, règle adverse G), la valeur e finale de chaque carte, e_i = W^(i) lue au dernier instant révélé (ou arrêtée au premier
instant où elle atteint m/α), vérifie E[e_i] ≤ 1 ; (b) la règle de Benjamini et Hochberg sur ces valeurs e, m fixé avant toute
issue, garde le taux de fausses découvertes au plus α, **quelle que soit la dépendance que l'allocation crée entre cartes** ;
(c) pour des cartes fraîches jugées sur la même archive, si le monde est dans la classe, ce taux est la probabilité d'au moins
une promotion dans la génération.

*Preuve.* (a) À chaque instant lu, W^(i) ≤ Λ^(i) ([PREUVE], théorème 1, étapes 1 et 2 : le maximum de vraisemblance certifié
du nul domine P* sur **exactement** les issues révélées de la carte, recalculé à chaque instant ; inégalité trajectoire par
trajectoire, sans condition sur la façon d'arriver à cet instant — [CL] § 1.1, pas b). Le dernier pas où i est lue est un
temps d'arrêt σ_i de G, borné (budget fini, plafond N_max) : E[e_i] ≤ E[M_i(σ_i)] ≤ M_i(0) = 1 (arrêt optionnel d'une
surmartingale positive ; inégalité de Ville pour la lecture continue). (b) La règle e-BH n'exige que E[e_i] ≤ 1 pour chaque
hypothèse nulle vraie, sous dépendance quelconque. (c) Immédiat. ∎

**Confirmation par la contre-lecture.** [CL] § 1 refait les pas a à e, écrit les six hypothèses exactes (filtration ; gel ;
flux indépendants ; monde dans la classe et certificat ; règle non anticipante et bornée ; lecture de la richesse cumulée à un
temps d'arrêt) et ne trouve aucun contre-exemple sur 20 000 générations d'un monde jouet, règle adverse comprise (part des
générations avec promotion 0,0044 ± 0,0009, moyenne des valeurs e 0,433 ± 0,038 ; programme `01c648a0…`, sortie `25a9e2e1…`) ;
la moyenne ne dépasse 1 que lorsqu'une hypothèse est rompue (règle qui lit le bloc suivant : 1,267 ; valeur e prise au
maximum de la trajectoire : 2,618).

**Ce que cela règle dans la critique.** La synthèse (§ 8) et le recoupement (J1) demandaient : surmartingale à chaque pas pour
toute loi du nul composite — **établi** (lemme, pour chaque P* de la classe) ; règle d'allocation scellée — **oui** ; ordre de
continuation « jamais selon les valeurs e » et dénominateur « à mélange de poids fixés d'avance, jamais recalibré sur les
issues » — **non nécessaires** : ces conditions servent une preuve **facteur par facteur** (la richesse elle-même
surmartingale), que ce texte ne suit pas ; il suit l'inférence universelle (la richesse n'est pas une surmartingale, mais elle
est dominée par une surmartingale pour chaque loi du nul). Un dénominateur à mélange de poids fixés ne serait d'ailleurs valide
que pour le mélange, **pas pour chaque loi du nul** ([PREUVE], § 8 ; [CL], essai X3 : moyenne 3,4 des valeurs e d'une carte
membre exact du nul). Le dénominateur du juge est déjà recalibré sur ses tirages (`nul_v8.py`, docstring, point 4). **Divergence
avec la critique, levée par une preuve contre-lue** ([CL], verdict) : à signaler à Lazar avec le nœud d'adoption (la synthèse,
§ 9, en faisait une condition bloquante).

**Réserves.** (i) C3 : pour un monde qui lit l'historique, les blocs révélés sous l'ordre d'exécution secret demanderaient un
argument de plus ; les mondes du banc et des courses actuelles ne lisent pas l'historique. (ii) La réserve log-linéaire du v8
([PREUVE], H4) est héritée ; elle est **éprouvée** ici par la moitié M₀′ de la famille N et la lecture de domination. (iii) Le
rejeu tire d'avance les 800 issues de chaque carte, **après** le gel ; il équivaut à une révélation à la demande parce que la
richesse à l'instant t ne dépend que des t premières issues (vérifié sur la copie `94bfd92`, [BANC-v1], annexe B ; essai E1
élargi, Plan d'analyse) et parce que la règle ne lit que les instants révélés (garde d'accès du code). (iv) Les unités sont les
cartes, non les groupes de doublons (la boucle réelle n'en a pas) ; pour des groupes, la moyenne des surmartingales des membres
en est une pour la même filtration : même garantie, non éprouvée ici. (v) Quand le monde est hors de la classe (famille T), le
théorème ne borne **pas** les promotions de cartes fausses : elles sont mesurées par l'oracle, non garanties. (vi) La valeur e
est toujours la **richesse cumulée à un temps d'arrêt** : ni maximum de la trajectoire, ni produit d'accroissements, ni
richesse repartie de 1 après une reprise ; le cumul d'héritage de `appliquer_multiplicite` n'entre pas dans le banc (cartes
fraîches, aucun héritage).

**Références.** Inégalité de Ville (Ville, 1939, « Étude critique de la notion de collectif ») ; inférence universelle
(Wasserman, Ramdas et Balakrishnan, « Universal inference », PNAS, 2020, citée par `nul_v8.py`) ; règle e-BH (Wang et Ramdas,
« False discovery rate control with e-values », Journal of the Royal Statistical Society, série B, 2022, citée par `cycle.py`)
— références de méthode, PDF non versés, aucun chiffre n'en est tiré (R7). **Voisins publiés, lus sur PDF page 1** (citations
retrouvées mot pour mot par [CL], m13) : PACE (`779f4960…`, p. 1 : un candidat n'est accepté « only when a testing-by-betting
e-process accumulates decisive evidence, stopping early to save evaluations », avec une probabilité de fausse acceptation
contrôlée « even under optional stopping (a per-decision guarantee, not a run-level one) ») ; E-valuator (`b7a46e4c…`, p. 1 :
test séquentiel « valid at every step ») ; Qu, Chen et Wang (`2a8ded01…`, p. 1 : garantie sur les fausses découvertes « at every
stopping time for any proposal policy »). Aussi, liste de N-067, § 6 : Hegazy, Jordan et Dieuleveut, « Valid Stopping in
Adaptive Generator–Verifier Loops », arXiv 2610.06432 (PDF sur une autre branche, empreinte abrégée `283d3e827032df04…` reprise
de N-067 ; non lue par moi ni par [CL]).

## Prédiction chiffrée et signe attendu

Écrites avant tout jeu, sans pilote. « Couverture » : part des générations de la famille T où au moins une **porteuse au sens
de l'oracle** est retenue par la règle e-BH. **Dose basse / dose haute** : la plus petite / la plus grande des deux doses
retenues pour chaque type de composante (cinq cellules chacune). Bras : section « Plan d'analyse ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| Q1 | validité, famille N (monde dans la classe du nul), part des générations avec au moins une promotion | sous α | **≤ 13 sur 500 dans chacun des sept bras** (seuil de « tenue », annexe B) ; estimation ponctuelle attendue ≤ 0,02 | un bras « non tenu » (≥ 39 sur 500) | 0,85 |
| Q2 | membres exacts de la classe : jamais promus, dans aucun bras ni aucune famille | nul | 0 | une seule promotion (défaut) | 0,97 |
| Q3 | **principale** : couverture A − couverture F, famille T, toutes cellules | + | ≥ + 0,05, borne basse > 0 ; gain surtout à la dose haute (≥ + 0,08 sur les cinq cellules de dose haute réunies), ≤ + 0,05 sur les cinq de dose basse réunies | borne haute < + 0,02 (« pas de gain ») | 0,55 |
| Q4 | A contre F125 (part fixe de 250, total 1,25 fois plus grand) | ≥ 0 | couverture A ≥ couverture F125 (ponctuel) | borne haute de A − F125 < 0 (gain d'effectif seulement) | 0,5 |
| Q5 | A contre le placebo P | + | A − P ≥ + 0,02 (ponctuel) ; A − P′ rapporté | borne haute de A − P ≤ 0 (pas d'effet du ciblage) | 0,55 |
| Q6 | fausses promotions **au sens de l'oracle** (famille T) | 0 ou + faible | moyenne par génération ≤ 0,10 dans chaque bras ; A − F : borne haute ≤ + 0,05 ; partiellement vraies rapportées à part | borne basse de A − F > + 0,02 | 0,6 |
| Q7 | tirages économisés par l'arrêt seul (F-arrêt), famille T | + | au moins 25 % du budget non consommé, pour une perte de couverture F − F-arrêt ≤ 0,02 | économie < 10 %, ou perte > 0,05 | 0,6 |
| Q8 | mécanisme : tirages moyens reçus par une porteuse sous A | + | ≥ 300 (contre 200 sous F) | < 230 | 0,55 |
| Q9 | validité, lectures (2) et (3) : domination jamais franchie ; moyenne des valeurs e finales sous 1 dans chaque bras, G compris | nul | aucune domination franchie ; moyennes ponctuelles ≤ 0,8 | une domination franchie, ou une borne basse de moyenne > 1 | 0,8 |

**Ce que serait chaque issue (R3).** Q3, Q4 et Q5 vraies : gain de structure (meilleur cas). Q3 vraie, Q4 fausse : gain
d'effectif seulement (cosmétique au sens de la fiche). Q3 vraie, Q5 fausse : l'effet vient de l'arrêt et des tirages en plus,
pas du ciblage. Q3 vraie, Q4 et Q5 fausses ensemble : « d'effectif seulement et sans effet de ciblage » (quatrième issue de
l'étage 4). Q3 fausse : l'allocation n'aide pas sur ce banc ; Q7 dit seulement ce qu'épargne l'arrêt. Q6 fausse : l'allocation
promeut des fausses (critère « nuisible »). Q7 fausse : l'arrêt bas n'épargne presque rien (les non porteuses ne tombent pas
sous 1/20 assez tôt) ou coûte de la couverture (porteuses tuées par une mauvaise série initiale, piège nommé par la fiche).
Q8 fausse : le budget libéré ne va pas aux porteuses (il reste chez des cartes indécises). Couverture de F hors de [0,05 ; 0,95] :
banc hors de la zone utile, rien ne se lit sur la principale. Q1, Q2 ou Q9 fausses : défaut de code ou de preuve.

## Métrique

- **Génération** : un monde, son archive A2 (banc B v2), m = 24 cartes, budget **B = 24 × 200 = 4 800** tirages frais ; A, P,
  P′, F-arrêt et G consomment **au plus B** ([CL] m2) ; F en consomme exactement B ; F125 6 000 (déclaré) ; la consommation
  réelle est rapportée ; les 100 tirages d'entraînement par carte, égaux dans tous les bras, ne comptent pas.
- **Promotion** : retenue par la règle e-BH (`cycle.appliquer_multiplicite`, m_fixe = 24, α = 0,05) sur les valeurs e finales
  des 24 cartes ; valeur e d'une carte : sa trajectoire **tronquée** à son dernier instant révélé, arrêtée au premier instant où
  elle atteint m/α (log 480 ≈ 6,17), sinon sa dernière valeur (règle (vi) de la Garantie).
- **Oracle** ([CL] M1), calculé **avant** le jeu des bras, par génération : 20 000 instances et leurs issues tirées du monde
  (graine `(famille, g, 2000)`) ; log-vraisemblance moyenne de chaque carte ; maximum de vraisemblance du nul v8 de l'archive
  (bibliothèque standard et `nul_v8.membres_archive_v8`, ajustés par les routines du juge à l'instant 20 000, marge de
  certificat comprise) ; **gain d'oracle** d'une carte = sa log-vraisemblance moyenne moins celle du meilleur membre. Classes :
  **porteuse** = porteuse construite **et** gain > 0 ; **porteuse sans gain** = porteuse construite et gain ≤ 0 (comptée à
  part, hors couverture) ; **fausse** = non porteuse et gain ≤ 0 ; **partiellement vraie** = non porteuse et gain > 0 (exclue de
  FP et de la couverture, comptée à part). La table de l'oracle est scellée avec la sortie, avant lecture.
- **Couverture C_X** (famille T) : part des générations où au moins une porteuse est promue ; Clopper-Pearson à 95 %.
  **Différence appariée** C_X − C_Y (mêmes générations, mêmes cartes, mêmes issues) : intervalle percentile à 95 % par
  rééchantillonnage des générations, 10 000 rééchantillons ; test exact de McNemar (rapport).
- **Fausses promotions FP_X** : nombre moyen, par génération, de cartes **fausses au sens de l'oracle** promues ; rapporté aussi
  par sorte (copies de la classe, copies par morceaux, fausses construites, nulles) ; promotions de partiellement vraies
  rapportées à part. Différence appariée et intervalle de même construction. **Erreurs de décision** par génération :
  1[non couverte] + nombre de fausses promues (ensemble et séparément).
- **Validité** (famille N), quatre lectures ([CL] M3) : (1) part des générations avec au moins une promotion, par bras,
  Clopper-Pearson ; (2) **domination** : log W_t ≤ log Λ_t + 10⁻⁶ à chacun des 32 instants de chaque carte, Λ calculé par le banc
  sur la loi connue du monde ; (3) **moyenne des valeurs e finales** par bras (toutes cartes réunies) et par sorte dans chaque bras
  (six sortes de la famille N, désignées au Seuil), intervalle percentile à 95 % par rééchantillonnage des générations ; (4) **bras G** (validité seulement). **Jugées** sur les 500 générations ensemble
  (seuils de la section « Seuil ») ; **rapportées sans critère** pour chacun des deux mondes (250 générations ; pour mémoire, au
  niveau 0,05/7 : tenue ≤ 4, non tenue ≥ 23 sur 250, [VC], annexe). La lecture (2) vaut à chaque instant de chaque carte, donc
  dans chaque monde ([VC] C2).
- **Réserves de l'épreuve de validité** ([VC] R-a). (a) La mise à mort de la mutation « valeur e lue au maximum de la
  trajectoire » par la lecture (3) **ne s'établit pas sur les 500 générations du jeu** : la loi des valeurs e est à queue
  lourde (essai jouet de [CL] : moyenne 2,618 ± 0,225 sur 20 000 générations, soit environ ± 1,4 sur 500). Elle s'établit au
  banc de mutations sur un **jeu d'essai synthétique de 20 000 générations**, sans le juge : monde jouet construit comme
  l'essai de [CL] (programme `01c648a0…` : 3 issues, un trait binaire, nul composite à deux lois, 24 cartes voisines hors de la
  classe, maximum de vraisemblance recalculé à chaque instant, blocs de 25, plafond 800, budget 4 800, m = 24), graines
  `(97, g)` ; la mutation y est jouée **sans allocation**, la valeur e de chaque carte étant le maximum de sa trajectoire sur les
  32 instants (comme la mutation X2 du programme `01c648a0…`), et la « borne basse » est celle de l'intervalle percentile à
  95 % par rééchantillonnage des 20 000 générations (10 000 rééchantillons) ; sur ce jeu, la borne basse de la moyenne sous la
  mutation doit passer 1, sinon la mutation survit et la liste
  d'arrêt dit « pas de jeu » (échec du côté sûr). (b) **La fuite d'instants non révélés n'est vue par aucune des quatre
  lectures sur W** (dans [CL], la moyenne 1,267 de la règle qui lit le bloc suivant est lue sur le rapport exact Λ, non sur W) :
  seule la garde d'accès du code, avec son essai et sa mutation, en protège.
- **Tirages** : consommation D_X / B par génération (moyenne, quantiles) ; **économie** E_X = 1 − D_X / B ; tirages reçus par
  sorte de carte et par classe d'oracle ; part des cartes arrêtées bas, haut, au plafond.
- Rapportés par cellule (type de composante × dose) et réunis ; aucune moyenne ni médiane sur des jetons (il n'y en a pas).

## Seuil

- Juge : nul v8 de l'archive A2, bibliothèque et marginale d'entraînement comme `juger_carte` ; α = 0,05 ; m = 24 ; blocs de 25 ;
  instants = fins de blocs ; plafond N_max = 800 (4 fois la part fixe, fiche opus-p1-01, point 6).
- Arrêt bas : log W < log(1/20) après au moins 50 tirages (un quart de la part fixe, point 4) ; arrêt haut : log W ≥ log(m/α).
- **Validité, lecture (1)**, famille de **sept bras** (F, F-arrêt, A, P, P′, F125, G), niveau 0,05/7 : « tenue » si le test
  binomial exact de H₀ « part ≥ 0,05 » est rejeté, soit **≤ 13 sur 500** ; « non tenue » si H₀ « part ≤ 0,05 » est rejeté, soit
  **≥ 39 sur 500** ; sinon (14 à 38) « non jugeable » (annexe B).
- **Validité, lectures (2) et (3)** : un seul dépassement de la domination, à n'importe quel instant de n'importe quelle carte,
  dans l'un ou l'autre monde ; ou une borne basse de moyenne des valeurs e > 1, **sur les 500 générations**, dans un bras ou une
  sorte : défaut. **Sortes de la famille N pour la lecture (3)** : voisines du monde ; membres exacts ; porteuses construites ;
  copies par morceaux ; fausses construites ; nulles (six). La moyenne est lue par bras, toutes cartes réunies (sept intervalles),
  et par sorte dans chaque bras (quarante-deux) ; **seuls ces 49 intervalles comptent pour le critère** ([RD] P1). Sans correction
  de multiplicité : le risque est une fausse alerte, du côté prudent (une sorte de deux cartes donne 1 000 valeurs e à queue
  lourde), et toute alerte reçoit l'audit écrit avant le prononcé. Par monde (250 générations), les lectures (1) et (3) sont rapportées sans critère ; une borne basse de moyenne
  > 1 dans un seul monde déclenche l'audit écrit (R4), non un verdict ([VC] C2).
- **Principale**, lue **dans cet ordre**, la première vraie l'emporte ([CL] M2) : 1. **« nuisible »** si la borne haute de
  C_A − C_F < 0 ou la borne basse de FP_A − FP_F > + 0,02 ; 2. **« gain »** si la borne basse de C_A − C_F > 0, son estimation
  ≥ + 0,05 et la borne haute de FP_A − FP_F ≤ + 0,05 ; 3. **« pas de gain »** si la borne haute de C_A − C_F < + 0,02 ;
  4. sinon **« non tranché »**.
- **Qualification d'un gain** : « d'effectif seulement » si la borne haute de C_A − C_F125 < 0 ; « sans effet de ciblage » si la
  borne haute de C_A − C_P ≤ 0 ; « de structure » si aucune des deux ; **si les deux sont vraies, les deux qualifications sont
  prononcées ensemble (« d'effectif seulement et sans effet de ciblage »)** ([VC] C1). A − P′ (éligibilité seule) rapporté sans
  critère.
- **Zone utile** : si C_F (famille T, réunie) ≤ 0,05 ou ≥ 0,95, la principale est « hors de la zone utile » (non concluant).
  Sans pilote, ce risque est réel et accepté ([CL] m14) : la couverture compte « au moins une des porteuses », dont la loi
  exacte du monde.

## Plan d'analyse

### Banc B v2 (partagé avec l'idée 1.1)

Le banc B v1 ([BANC-v1]) avec trois changements : coupures de l'archive à |s| ≥ 0,3 ([CL-1.1] m2) ; ligne **V5** ([CL-1.1] M1,
R-2875) ; gel des engagements **avant** les issues fraîches ([CL-1.1] m1).

**Espace.** K = 3 issues ; D = 2 traits ; G = 2 sous-populations. Instance : z_j ~ N(0, 1) indépendants, arrondis à six
décimales ; g uniforme sur {0, 1}. **Loi softmax aléatoire** : poids w_{k,j} ~ N(0 ; 1,5²), biais b_k ~ N(0 ; 0,3²), arrondis à six
décimales. Toute loi du banc est une loi de la grammaire du juge, vérifiée par `selection_pari.valider_loi`.

**Archive A2.** S1, S2 softmax aléatoires ; S3 = `si_sinon`({z_{jA} > s_A}, U1, U2) ; S4 = `si_sinon`({z_{1−jA} > s_B}, U3, U4) ;
U1 à U4 softmax aléatoires ; jA uniforme sur {0, 1} ; s_A, s_B ~ U[−1 ; 1] au centième, **retirés tant que |s| < 0,3**.
C_arch = {z_{jA} > s_A ; z_{1−jA} > s_B} ; cut(j) = coupure de l'archive sur le trait j.

**Lignes du banc B v2** (M : loi du monde ; Q : loi de la carte) — celles que l'idée 1.2 emploie sont marquées ★ :

| ligne | monde M (et carte Q = M sauf mention) |
|---|---|
| Q1 ★ mélange de l'archive (monde M₀ de la famille N) | `melange`([S1, S2, S3, S4, uniforme fixe], poids ~ Dirichlet(1, …, 1), arrondis et renormalisés) |
| Q2 copie à une coupure de l'archive | `si_sinon`({z_{jA} > s_A}, S1, S2) |
| Q3 copie par sous-population | `par_sous_population`({"0": S1, "1": S2}) |
| Q4 copie au signe d'un trait | `si_sinon`({z_j > 0}, S1, S2), j uniforme |
| Q5 copie à une coupure hors de C | `si_sinon`({z_j > s}, S1, S2), j uniforme, s = ±U[0,3 ; 1,0] au centième, retiré tant que \|s − cut(j)\| < 0,3 |
| Q6 copie à deux niveaux sur C_arch | `si_sinon`({z_{jA} > s_A}, `si_sinon`({z_{1−jA} > s_B}, S1, S2), `si_sinon`({z_{1−jA} > s_B}, S2, S1)) |
| Q7 monde copie, carte hors classe | M de Q2 ; Q = `si_sinon`({z_{jA} > s_A}, S1′, S2), S1′ = softmax(W1 + 0,25·Δ, b1), Δ ~ N(0, 1) centrée par colonne |
| V1(δ) ★ effet neuf global, δ ∈ {0,25 ; 0,50 ; 0,75} | softmax(W1 + δ·Δ, b1), Δ ~ N(0, 1) centrée par colonne sur les issues |
| V2(γ) ★ conditionnelle au signe, γ ∈ {0,4 ; 0,8 ; 1,2} | `si_sinon`({z_j > 0}, softmax(W1 + γE, b1), softmax(W1 − γE, b1)), j uniforme, E nulle sauf la colonne du trait 1 − j égale à u, u ~ N(0, I₃) centré, normé |
| V3(γ) ★ conditionnelle à seuil décentré, γ ∈ {0,4 ; 0,8 ; 1,2} | comme V2 avec le seuil c = ±U[0,3 ; 0,8] au centième, retiré tant que \|c − cut(j)\| < 0,3 |
| V4(λ) ★ loi neuve sur une sous-population, λ ∈ {0,1 ; 0,2 ; 0,3} | `par_sous_population`({"0": S1, "1": `melange`([S1, N], [1 − λ, λ])}), N softmax aléatoire |
| **V5(γ) ★ conditionnelle à une coupure de l'archive**, γ ∈ {0,4 ; 0,8 ; 1,2} | comme V2 avec la condition {z_{jA} > s_A} de l'archive (effet sur le trait 1 − jA) ; aucune classe ne contient M |

Information de V5 sur 200 épisodes (compte sans juge, annexe A) : 2,2 ; 9,3 ; 20,0 nats aux trois doses, comme V2 (2,1 ; 8,8 ;
20,2, [BANC-v1], annexe A).

### Familles de générations de l'idée 1.2

**Types et doses.** Cinq types (V1 à V5), deux doses chacun — les deux plus basses de leur grille : V1 {0,25 ; 0,50} ; V2, V3,
V5 {0,4 ; 0,8} ; V4 {0,1 ; 0,2} ; **dix cellules** ; la cellule de la génération g est g mod 10.

**Famille T** (750 générations, 75 par cellule) : monde M = S1 portant la composante de la cellule. 24 cartes construites :
- 6 **porteuses** : M ; M à force × 0,5 ; M à force × 1,5 ; M avec la direction de la composante bruitée (bruit gaussien de 0,3
  fois sa norme, renormalisée) ; deux doublons de M (chaque poids des lois softmax de M + 0,01·N(0, 1)) ;
- 6 **copies de la classe** : trois `melange` des lois d'archive (poids de Dirichlet) ; trois lois d'archive tempérées et inclinées
  (`transformee`, puissance U[0,7 ; 1,3], inclinaison N(0 ; 0,2²) par issue) — membres du nul v8 ;
- 4 **copies par morceaux** hors de la classe du v8 : `si_sinon` sur chacune des deux coupures de l'archive (S1, S2) ;
  `par_sous_population` (S1, S2) ; `si_sinon` au signe d'un trait (S2, S1) ;
- 6 **fausses construites** : S1 portant une composante de même type et de même dose, tirée indépendamment **puis retirée tant
  que son cosinus avec la composante du monde dépasse 0** (quatre ; cosinus = E_x[f(x)·f′(x)] / (E_x‖f‖² · E_x‖f′‖²)^{1/2}, où
  f(x) = p(· | x) − S1(· | x), sur les 20 000 instances de l'oracle ; au plus 1 000 tirages, sinon la carte de plus petit cosinus
  est gardée et signalée) ; M à composante de signe opposé, **à force × 1 et × 0,5** (deux) ; **pour V4**, où l'opposé (un
  poids négatif dans le mélange) n'est pas une loi de la grammaire du juge, ces deux cartes sont **deux fausses construites de
  plus**, sous la même règle du cosinus ([VC] C8) ;
- 2 **nulles** : softmax aléatoires.
Le classement final de chaque carte est celui de l'**oracle** (section « Métrique »).

**Famille N** (500 générations) : **M₀ pour g de 0 à 249** = ligne Q1 (mélange des lois d'archive) ; **M₀′ pour g de 250 à
499** = une loi d'archive tempérée et inclinée (`transformee` d'une loi **tirée parmi S1 et S2**, puissance U[0,7 ; 1,3],
inclinaison N(0 ; 0,2²)), membre de la classe log-linéaire ([CL] M3) ; la cellule étant g mod 10, chaque monde voit chaque
cellule 25 fois : monde et cellule ne sont pas confondus ([VC] C3). M₀′ n'est jamais tirée d'une loi `si_sinon` (S3, S4) :
l'épreuve de validité ne voit donc pas de monde tempéré par morceaux ; ces lois restent parmi les membres exacts (dit, [RD],
remarque 5). 24 cartes ([VC] C4) :
- 8 **voisines du monde**, hors de la classe : pour M₀, le monde où S1 est remplacée par softmax(W1 + 0,05·Δ, b1) (comme en
  v1) ; pour M₀′, le monde où sa loi de base (S1 ou S2, notée S_k) est remplacée par softmax(W_k + 0,05·Δ, b_k), puissance et
  inclinaison gardées ; Δ ~ N(0, 1) centrée par colonne sur les issues, une par carte ;
- 8 **membres exacts** : le monde lui-même (une) ; quatre autres `melange` des lois d'archive (poids de Dirichlet) ; trois lois
  d'archive tempérées et inclinées (`transformee` d'une loi tirée parmi S1 à S4 : membre log-linéaire de la survivante) ;
- 8 cartes des **autres sortes** de la famille T, bâties sur une composante (cellule g mod 10) que le monde ne porte pas : deux
  porteuses construites (S1 portant la composante, à force × 1 et × 0,5), deux copies par morceaux (`si_sinon` sur la coupure
  {z_{jA} > s_A} (S1, S2) ; `par_sous_population` (S1, S2)), deux fausses construites (S1 portant une composante de même type
  et de même dose, tirée indépendamment, retirée tant que son cosinus avec la composante de la cellule — celle des deux
  porteuses construites — dépasse 0, même formule et même plafond de 1 000 tirages qu'en famille T ; pour V4, même règle ;
  [RD] P2), deux nulles (softmax aléatoires).

**Cartes, plans, issues.** Chaque carte a son plan de 800 instances, une marginale d'entraînement sur 100 instances et ses 800
issues fraîches (flux propre). Ses richesses aux 32 instants 𝒯 sont calculées **une fois** par `nul_filles_v2.evaluer_v2`
(nul v8, engagement à plan « ordre_naturel », tirages liés à son empreinte, montage de [BANC-v1], annexe B) ; tous les bras
**rejouent** ces mêmes trajectoires, tronquées à ce qu'ils ont donné.

### Bras (mêmes cartes, mêmes issues, même e-BH)

- **F** (part fixe, témoin) : 200 tirages par carte, instants 25 à 200 ; valeur e arrêtée à m/α, sinon W₂₀₀ (règle actuelle).
- **F-arrêt** (arrêt seul) : F plus les arrêts bas et haut ; aucune réallocation ; mesure l'économie.
- **A** (allocation, fiche opus-p1-01 adaptée aux cartes et aux blocs de 25) : par tours ; à chaque tour, chaque carte
  **active** (ni arrêtée bas, ni arrêtée haut, ni au plafond) reçoit un bloc, dans l'ordre des **positions** décalé du numéro
  du tour, tant que le budget restant le permet ; les tours continuent au-delà de 200 pour les actives jusqu'à épuisement du
  budget ou des actives.
- **P** (placebo du ciblage) : comme A jusqu'à ce que chaque carte ait reçu 200 tirages ou soit arrêtée ; ensuite chaque bloc
  restant va à une carte **tirée au hasard** (graine indépendante des issues) parmi celles qui ne sont ni arrêtées haut ni au
  plafond, **arrêtées bas comprises** (elles reprennent). P consomme au moins autant de tirages que A ([CL] m1).
- **P′** (éligibilité seule, rapporté) : comme P, mais les blocs restants vont **à tour de rôle** sur ce même ensemble élargi.
- **F125** (témoin d'effectif) : 250 tirages par carte (10 blocs), total 6 000 ; valeur e comme F. **Écart déclaré à la fiche**
  (« 1,2 fois les tirages », champ `cosmetique_si`) : 240 n'est pas un multiple de 25.
- **G** (adverse, validité seulement, famille N) : deux blocs par carte, puis chaque bloc à la carte de plus grande log W
  courante parmi celles qui ne sont ni arrêtées haut ni au plafond, jusqu'à épuisement de B ; aucune lecture de couverture.
- Écarts déclarés à la fiche opus-p1-01 : blocs de 25 au lieu de 50 (instants du juge) ; cartes au lieu de groupes (la boucle
  réelle n'en a pas).

### Graines (R9)

Racine : entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, famille
0 = N, 1 = T : monde `(famille, g, 24)` ; archive `(famille, g, 25)` ; construction de la carte i `(famille, g, i, 0)` ; son plan,
son entraînement et les issues d'entraînement `(famille, g, i, 1)` ; **ses issues fraîches `(famille, g, i, 2)`, tirées après le
gel de tous les engagements de la génération** ; permutation des positions `(famille, g, 1001)` ; hasard du placebo
`(famille, g, 1000)` ; oracle `(famille, g, 2000)` ; rééchantillonnage `(99, b)` ; jeu d'essai synthétique du banc de
mutations `(97, g)` (Métrique, réserve (a)). Manifeste du run (`src/controle_ia/manifeste.py`).

### Étapes

0. Code sous des noms neufs, `docs/notes/organisme-idees-juge-v1/code-v1/banc_tirages_repartis_v1.py` et
   `lire_banc_tirages_repartis_v1.py` (lecture gelée), avec essais (R5 : cas sain et artefact **pour chaque ligne de la liste
   d'arrêt**) et banc de mutations, au moins : la règle lit un instant non révélé ; budget dépassé ; arrêt bas avant 50 tirages ;
   plafond ignoré ; hasard du placebo tiré des issues ; m compté après coup ; flux d'issues partagé entre deux cartes ; issues
   fraîches tirées avant le gel ou passées à la fonction qui bâtit un engagement ; **valeur e lue au maximum de la trajectoire**
   (doit être tuée par la lecture (3) sur le jeu d'essai synthétique de la réserve (a) de la Métrique) ; **F lu sur les champs `promue`, `t_promotion`, `log_richesse_max` ou
   `log_richesse_arretee` de l'évaluation à 800** ; oracle calculé sur les issues jugées ; toutes tuées pour la raison attendue ;
   contre-lecture du code par un autre modèle ; addendum d'empreintes scellé.
1. Contrôles avant jeu (empreintes, essais, mutations ; aucune sortie existante).
2. **Essai E1** ([CL] m8) : sur 50 cartes couvrant chaque sorte, pour chacun des 32 instants t, la trajectoire d'un plan de 800
   tronquée à t est égale à celle d'un plan de t, et les valeurs aux instants ≤ t sont inchangées quand les issues au-delà de t
   sont remplacées ; sinon arrêt.
3. Oracle calculé et scellé pour toutes les générations, **avant** le rejeu des bras.
4. Jeu : 1 250 générations, `nice -n 10`, deux processus au plus.
5. Sortie scellée avant toute lecture, sous `diag/organisme-idees-juge-v1/`.
6. Lecture gelée, puis lecteur neuf (R13), audit de symétrie (R4) écrit avant le prononcé.

### Comparaisons et corrections

Une principale (A contre F, couverture, avec la condition sur les fausses promotions) ; deux qualifications (A contre F125, A
contre P) lues seulement si la principale rend « gain » ; A − P′ rapporté ; validité : Bonferroni sur sept bras pour la
lecture (1) ; lectures (2) et (3) sans correction (un seul dépassement suffit). Tout le reste (cellules, sortes, classes
d'oracle, Q7, Q8) est rapporté sans critère supplémentaire.

## Critères de lecture gelés

| étage | observé | verdict |
|---|---|---|
| 1 | une validité « non tenue » dans un bras ; une promotion d'un membre exact ; une domination franchie (dans l'un ou l'autre monde) ; une borne basse de moyenne des valeurs e > 1 (sur les 500 générations, dans l'un des 49 intervalles désignés au Seuil : par bras, ou par sorte dans un bras) | **« garantie mise en défaut »** : défaut de code ou de preuve ; rien d'autre n'est lu ; audit ; nœud |
| 1 bis | une validité « non jugeable » (14 à 38 sur 500) dans un bras | **« validité non établie »** : la principale est lue et rapportée sous cette réserve ; **aucune adoption ne peut s'en réclamer** |
| 2 | C_F (famille T, réunie) ≤ 0,05 ou ≥ 0,95 | **« hors de la zone utile »** (non concluant) |
| 3 | principale, dans l'ordre écrit au Seuil | « nuisible » / « gain » / « pas de gain » / « non tranché » |
| 4 | si « gain » : qualifications | « de structure » / « d'effectif seulement » / « sans effet de ciblage » / « d'effectif seulement et sans effet de ciblage » (les deux bornes hautes sous leur seuil) |
| 5 | F-arrêt | économie et perte de couverture rapportées, avec intervalles (Q7) |

**Audit de symétrie (R4)**, écrit pour **toute** issue avant le prononcé : tirages reçus par sorte et par classe d'oracle (le
mécanisme attendu — les porteuses reçoivent les tirages libérés — se voit-il ?) ; porteuses arrêtées bas (mauvaise série
initiale) ; partiellement vraies promues ; comparaison cellule par cellule ; **« trop propre »** (gain identique dans toutes les
cellules, aucune fausse promotion nulle part, toutes les prédictions vraies) et **« tout négatif »** (A égal à F trajectoire pour
trajectoire, aucune carte arrêtée bas, économie nulle, ou aucune porteuse au-delà de 200 tirages) : même relecture écrite du code
de rejeu ([CL] m11).

## Liste d'arrêt

| condition | action |
|---|---|
| un fichier gelé diffère de l'addendum ; un essai échoue ; une mutation survit | pas de jeu |
| essai E1 : préfixe non égal à un instant | arrêt avant le jeu ; le rejeu n'est pas équivalent à une révélation à la demande |
| une issue fraîche tirée avant le gel, ou lue par la fonction qui bâtit un engagement (garde de code) | arrêt ; défaut |
| la règle d'un bras lit un instant au-delà des tirages qu'elle a donnés (garde d'accès du code) | arrêt ; défaut |
| tirages donnés > B (A, P, P′, F-arrêt, G) ou > 6 000 (F125) dans une génération | arrêt ; défaut |
| domination franchie (famille N) | lecture « garantie mise en défaut » ; le run va à son terme, puis audit |
| exception, log W non fini | arrêt du run ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5) |
| durée murale > 24 h | arrêt ; run invalide |
| lecture avant scellement de la sortie, ou oracle calculé après le rejeu | run invalide |
| toute dépense, instance payante ou appel de modèle | interdit (R-2851) |

## Coût

**Processeur seul, 0 dollar.** 1 250 générations × 24 cartes = 30 000 évaluations sous le nul v8 à 800 tirages et 32 instants,
à 0,12 à 0,20 s chacune (essai à blanc du 15 novembre, [BANC-v1], annexe B) : 1,0 à 1,7 heure d'un cœur. Oracle : un ajustement
du nul sur 20 000 issues par génération (le meilleur membre est le même pour les 24 cartes) et 24 log-vraisemblances : de l'ordre
d'une demi-heure au plus. Rejeu des sept bras, domination, rééchantillonnages : quelques minutes. Jeu d'essai synthétique du banc
de mutations (20 000 générations d'un monde jouet, sans juge) : processeur seul, durée non mesurée ici, dans la borne. Borne
dure 24 heures sur deux processus. Écriture, essais, mutations, contre-lectures : temps d'agents.

## Écarts, nœuds et ce que l'essai ne décide pas

- **Le banc** ne touche ni le juge de production ni la boucle : aucun écart à une conception scellée. **Différences de
  montage** avec la production ([CL] m7), aucune n'étant un écart : plan « ordre_naturel » (production : « ordre_secret »,
  indifférent pour un monde qui ne lit pas l'historique) ; m_fixe = 24 (production : nombre de cartes jugées et plantées) ; plan de
  800 et 32 instants, dont F ne lit que les 8 premiers ; F se lit sur la trajectoire tronquée, **jamais** sur les champs
  `promue`, `t_promotion`, `log_richesse_max`, `log_richesse_arretee` rendus par l'évaluation à 800 ; issues fraîches tirées par
  le banc après le gel, d'une graine de la racine (production : graine dérivée de l'empreinte de l'engagement).
- **Nœud de Lazar** : adopter l'allocation au juge changerait sa conception gelée (200 tirages et 8 instants par carte dans
  `juger_carte` et dans le texte scellé de la boucle réelle, `80fe4f03…` ; un budget de génération et un plafond de 800 en plus) :
  modification du juge, à décider sur le résultat, avec sa propre validation. **À lui signaler avec ce nœud** : la condition
  « dénominateur fixe » que la synthèse des bassins étroits (§ 9) tenait pour bloquante est **levée par une preuve contre-lue**
  ([CL], verdict ; R-2878).
- **N-058** : l'allocation sélectionne des **cartes** sur leurs valeurs e, jamais des **agents** : compatible (« l'interdit porte
  sur la sélection d'agents, pas sur celle des fiches »). Garde : les tirages reçus ne seront jamais rapportés par proposeur ni
  servis à un choix de proposeurs.
- **Ne décide pas** : l'effet sur la découverte (une carte non proposée ne gagne rien, borne 1 du recoupement) ; les mondes riches
  à 8 traits ; les groupes de doublons ; le test de mort ; le gain en dollars (un tirage du monde planté coûte des millisecondes,
  fiche opus-p1-01, champ `perte_traduction`) ; l'économie dans une génération réelle (hypothèse (ii)).

## Contre-lecture

- **Contre-lecture 1** (R2) — sous-agent neuf du modèle B (R-2851), qui n'a écrit ni ce texte, ni le banc, ni la preuve ; texte
  relu : version 1, `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v1.md`,
  `2a500156d1b36855330e02c1a261cb40c882032ebf0090760e87b7695b876a65` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1.md`,
  `5ae17f81cbeb83161e49d7d3ce5c8fa4ff38c4db9d38afd7cfc5b8ae676df109` (programme `01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`,
  sortie `25a9e2e1dd9fd2c76b61b8b5f387936dd0f72f28b25a220a733b2927451aba9f`). Verdict : « scellable après corrections »
  (3 majeurs, 14 mineurs) ; démonstration de validité confirmée, divergence avec la critique fondée. **Traitement** : les 17
  remarques sont acceptées (m14 en partie : lieu sous `prereg/` au scellement décisif, décision de la mère, R-2881), comme le
  dit le tableau « Différentiel v1 → v2 » ; aucune n'est refusée.
- **Contre-lecture 2** (R2, pour le banc partagé seulement) — sous-agent neuf du modèle B ; texte relu : banc B v1 dans
  `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`,
  `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md`,
  `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e`. Remarques qui touchent ce texte : M1 (ligne V5, décision
  de la mère R-2875) **acceptée** ; m1 (gel avant les issues fraîches) **acceptée** ; m2 (|s| ≥ 0,3) **acceptée**. Les autres
  remarques portent sur l'idée 1.1 et sa preuve : traitées dans leur version 2, qui attend la synthèse sur les poids du nul.
- **Contre-lecture 3** (vérification courte du différentiel v1 → v2) — lecteur neuf du modèle B, qui n'a écrit ni la v1, ni la
  v2, ni leurs contre-lectures ; texte relu : version 2, `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v2.md`,
  `c7f80e8c9fff5128ca60a1071b70519844a2f9ccdd9344f0ece0aab0e3e13c2b` ; rapport :
  `docs/notes/organisme-idees-juge-v1/verification-courte-prereg-tirages-repartis-v2-v1.md`,
  `229b183a04ea7ec822ac59394e6f4258d85ad3f3ba3c769a7b8b750d6bcd4a7f` (programme `d1066eaa4aa48badf2fd2f2cda93e37ef5379fcbcb3e689dec7ae60e3f7769ba`,
  sortie `48371611b7ffeeceb0790568c4cf4276b63295e3cca2cac2120a4f71e3944347`). Verdict : « scellable après corrections » ; fond tenu,
  chiffres neufs recalculés à l'identique. **Traitement** : C1 à C8 **acceptées**, selon les couples « ancien / nouveau » du
  rapport (C2 : option « jugées sur les 500, rapportées par monde » ; C4 : M₀′ tirée parmi S1 et S2 ; C8 : proposition du rapport
  retenue, et composition des 16 autres cartes de la famille N écrite, ce que le rapport suggérait sans l'exiger) ; réserves :
  R-a portée au texte (Métrique, « Réserves de l'épreuve de validité », et ligne M3 du tableau v1 → v2) ; R-b (zone utile), R-c
  (oracle à 20 000 issues, dit par l'essai du code avant le jeu) et R-d (consommation de P) prises en note, sans changement :
  elles sont déjà déclarées. Détail au tableau « Différentiel v2 → v3 ».
- **Contre-lecture 4** (relecture du seul différentiel v2 → v3) — lecteur neuf, qui n'a écrit ni la v1, ni la v2, ni la v3, ni
  leurs contre-lectures, ni la vérification courte ; texte relu : version 3,
  `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v3.md`,
  `28aab53951c9911586113d9acffcdca319ab67554ae08f93804154dcee04707e` ; rapport :
  `docs/notes/organisme-idees-juge-v1/relecture-differentiel-prereg-tirages-repartis-v3-v1.md`,
  `6a71e24d6f764b0a43639fd03f03a3a49e92eb2d7dd51d8837fc5e57e4cf7cbe`. Verdict : « scellable après corrections » ; différentiel
  propre, C1 à C8 fermées, comptes justes. **Traitement** : P1 et P2 **acceptées** (P1 : la proposition du rapport, six sortes,
  7 + 42 intervalles ; P2 : la proposition du rapport) ; les sept remarques non bloquantes **portées**. Détail au tableau
  « Différentiel v3 → v4 ».
- **À venir** : contrôle mécanique du différentiel v3 → v4, puis scellement par `controle_ia.prereg.sceller_prereg` et recopie
  sous `prereg/` (R-2881).

## Annexe A — compte de dimensionnement de la ligne V5 (sans juge, sans nul)

Même construction que [BANC-v1], annexe A ; coupure de l'archive {z_{jA} > s_A}, s_A = ±U[0,3 ; 1]. Script
(`ffa8d9b617b82e6de27165db07efc9beb89cd8e221d21f6bdabf13ea96f65274`) et sortie (`bf2a94eb29a8d12130acbf2e0602802e801895783af8aa3dd7c68c3fbf4666cd`),
dossier de travail de la session, recopiés en entier :

```
V5 conditionnelle à une coupure de l'archive dose 0.40 : médiane 0.0111 nat/épisode [quartiles 0.0075 ; 0.0146] ; sur 200 épisodes : 2.2 nat
V5 conditionnelle à une coupure de l'archive dose 0.80 : médiane 0.0464 nat/épisode [quartiles 0.0309 ; 0.0608] ; sur 200 épisodes : 9.3 nat
V5 conditionnelle à une coupure de l'archive dose 1.20 : médiane 0.1000 nat/épisode [quartiles 0.0678 ; 0.1272] ; sur 200 épisodes : 20.0 nat
```

```python
"""Compte de dimensionnement de la ligne V5 du banc B v2 (processeur seul ; aucun juge, aucun nul, aucune issue jugée) :
information moyenne par épisode E_x KL(monde || S1), en nat, de V5(γ) : composante conditionnelle posée sur la coupure de
l'archive {z_jA > s_A}, s_A = ±U[0,3 ; 1] (banc B v2), effet sur l'autre trait ; 300 mondes par dose, 4 000 instances."""
import numpy as np

K, D = 3, 2

def soft(rng):
    return np.round(rng.normal(0, 1.5, size=(K, D)), 6), np.round(rng.normal(0, 0.3, size=K), 6)

def p_soft(W, b, z):
    s = z @ W.T + b
    s -= s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)

def kl(p, q):
    return float(np.mean(np.sum(p * (np.log(p) - np.log(q)), axis=1)))

def u_centre(rng):
    u = rng.normal(size=K); u -= u.mean(); return u / np.linalg.norm(u)

racine = np.random.SeedSequence(20261115)
for dose in (0.4, 0.8, 1.2):
    v = []
    for s in racine.spawn(300):
        rng = np.random.default_rng(s)
        W1, b1 = soft(rng)
        z = rng.normal(size=(4000, D))
        jA = int(rng.integers(0, 2)); t = 1 - jA
        sA = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 1.0)), 2)
        E = np.zeros((K, D)); E[:, t] = u_centre(rng)
        pm = np.where((z[:, jA] > sA)[:, None], p_soft(W1 + dose * E, b1, z), p_soft(W1 - dose * E, b1, z))
        v.append(kl(pm, p_soft(W1, b1, z)))
    v = np.array(v)
    print(f"V5 conditionnelle à une coupure de l'archive dose {dose:4.2f} : médiane {np.median(v):.4f} nat/épisode [quartiles {np.quantile(v, .25):.4f} ; {np.quantile(v, .75):.4f}] ; sur 200 épisodes : {200 * np.median(v):.1f} nat")
```

## Annexe B — seuils de la validité, lecture (1)

Test binomial exact au taux 0,05 sur 500 générations, niveau de Bonferroni. Script
(`c8055829596ab48c8a2034b9c11bdd5c1d7a1848c0a28d36b3801f851dc7dbab`) et sortie
(`1bacfc3cfacfe7a1c869d5bcd0c118a2139ac6467857bfd51007d47009e890d9`), recopiés en entier ; la ligne à 5 bras retrouve les valeurs
de [CL] M2 :

```
5 bras, niveau 0.01 : tenue si <= 13 ; non tenue si >= 38 ; non jugeable de 14 à 37
7 bras, niveau 0.00714 : tenue si <= 13 ; non tenue si >= 39 ; non jugeable de 14 à 38
```

```python
"""Seuils de « tenue » et de « non tenue » de la validité (famille N, 500 générations, test binomial exact au taux 0,05),
au niveau 0,05/b pour b bras lus (Bonferroni). Compte seul, sans donnée."""
from scipy.stats import binom
n = 500
for b in (5, 7):
    lv = 0.05 / b
    kt = max(k for k in range(n + 1) if binom.cdf(k, n, 0.05) <= lv)
    knt = min(k for k in range(n + 1) if binom.sf(k - 1, n, 0.05) <= lv)
    print(b, "bras, niveau", round(lv, 5), ": tenue si <=", kt, "; non tenue si >=", knt, "; non jugeable de", kt + 1, "à", knt - 1)
```

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629
(`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf`, `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (`…/c8/1502.04585.pdf`, `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ;
`docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`,
`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; liste de `docs/decisions/decision-N-067-v1.md`, section 6
(dont PACE, Qu, Chen et Wang, Hegazy, Jordan et Dieuleveut). Aucune revendication n'est faite ici.

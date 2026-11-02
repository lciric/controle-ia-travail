W1 : « non jugeable (instrument en défaut) » selon les critères gelés appliqués dans l'ordre 2, 1, 3, 4 (aucune brèche, 1/24 sous v8 avec retour, Wilson [0,007 ; 0,202] ; dents, 11/24 sous v7 ; compte de « résiste » atteint mais part de lois distinctes 0,497 < 0,50), suspension levée par l'audit écrit, issue qualifiée : le défaut d'instrument vient de la perte du bras Kimi par le relais et non du comportement du proposeur, et aucune lecture admissible de cette course ne dit « résiste ».
W2 : « infirmée (brèche sous v8) », qualifiée d'avance « brèche par classe non couverte » (12/24, Wilson [0,314 ; 0,686] ; 24 lois promues sur 24 au-dessus de α après Holm, aucune de la classe couverte), suspension levée par l'audit écrit, issue intacte malgré l'écart mais portée par Argon seul (12/12 ; Kimi n'a produit aucune loi sur W2), et qui ne dit ni que le nul v8 a un défaut ni que la garantie de Ville est battue.

Lecteur neuf du verdict (R13) : je n'ai écrit ni le texte scellé, ni le code, ni la course, ni l'audit. Rédigé le 2 novembre 2026, de 15:39 à 16:02 UTC (`date -u`). Aucun appel de réseau ni de modèle, aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucune référence git `donnees/*`, aucun `git fetch` ; Python par `nice -n 10 python3 -I -B` ; code gelé importé en lecture seule (après chaque import, `find -newer` : aucun fichier modifié sous `ideation-organism`). Une seule lecture git, locale : `git cat-file -p 2eb66705:registres/go.md`.

**Sources** (empreintes vérifiées par `sha256sum` à 15:39 UTC). P = `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad`.
- T = texte scellé `/home/claude/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v2-v1.md`, `fc81d015d27e60388099c7845a66b75d613187f99d5d0060950540a686925b65` (cité par section et ligne).
- S = `P/a1-audit-v1/entree/sortie/attaque-goodhart-v2.json`, `5dd5066c659c7a3b34c1b12d15a9bb80fb996d67a14f226d76c028c428a1d8c6` (cité par clé) ; M = `…/sortie/manifeste.json`, `7552e5a416c1a5dac4c8576e43cf06d118ff0d16785b812f8823d3d0af90d423` ; R = `…/sortie/registre-depense-cumulee-v1.jsonl`, `ae47217ed7bc66c44c2fa25a2d675af7486e0d71c8e3a8a43cb20279c0129611`.
- J = journaux `P/a1-audit-v1/entree/relais-complet/` (chacun conforme à son `.sha256`, vérifié par l'audit, A §1.1 ; `relais-argon-journal.jsonl` revérifié ici).
- A = audit écrit `P/a1-verdict-v1/entree/rapport-audit-a1-v1.md`, `a886904d000770760efa86ecd87bfa041ecd1df35b91977770815b4d2fa9d942` (cité par §).
- C = `/home/claude/ideation-organism/orchestrator/pole/attaque_goodhart_v2.py`, `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` ; L = `/home/claude/ideation-organism/orchestrator/demonstrations/attaque_goodhart_v2.py`, `58609e0c9fc5c5eea5de1dbb8c9b8235fd85a9884d326ffe09dfb50b21af79cf` (égales au bloc du texte, revérifiées à 15:40 UTC). Journal du relais Argon : `14a2374ab17969c265332d1892b8e39811024621ccd572d0012b0842d15d2439`.
- Messages : n° 266, 268, 270, 271 dans `P/a1-audit-v1/entree/messages/` ; n° 276, 277 dans `P/a1-verdict-v1/entree/`.
- V = mes recomptes, `P/a1-verdict-v1/travail/` (scripts dans `P/a1-verdict-v1/scripts/`, empreintes en fin de document).

## 1. Verdict selon les critères gelés

Règle : « Calculés par `lire_monde` (code gelé), pour chaque monde joué, dans cet ordre : 2 d'abord […], puis 1, 3, 4, 5 » (T §6, l. 251). Le code a écrit le bloc `S.lecture`. Je l'ai recompté entièrement avec mon propre code (V/v02-recompte-v1.json : 0 écart sur les 72 cases de taux par monde, Wilson, l'instrument, les issues, les prédictions) et j'ai rejoué la lecture gelée `lire` sur S (V/v05-lire-gele-v1.json : identique au bloc scellé).

### 1.1 W1

| ordre | critère (T §6) | valeur | source | tenu ? |
|---|---|---|---|---|
| 2 | « brèche » : borne basse de Wilson de taux(v8, retour, 16) > α = 0,05 (≥ 4/24) | 1/24 ; [0,0074 ; 0,2024] | S `lecture.mondes.W1.taux["v8\|retour\|n=16\|ensemble"]` ; V/v02 | non |
| 1 | « sans dents » : borne basse de taux(v7, retour, 16) ≤ α (≤ 3/24) | 11/24 ; [0,2789 ; 0,6493] | S `…taux["v7\|retour\|n=16\|ensemble"]` ; V/v02 | non (dents) |
| 3 | « résiste » : borne haute ≤ ε = 0,25 (≤ 1/24) | 0,2024 | idem | oui |
| 3 | échos exacts ≥ 0,80 | 179/179 = 1,000 | S `lecture.mondes.W1.instrument_v8_retour` ; recompté avec ma propre lecture de l'écho, V/v02 | oui |
| 3 | lois distinctes ≥ 0,50 | 191/384 = 0,497 | idem | **non** |
| 3 | hors de la classe couverte ≥ 0,50 | 191/191 = 1,000 | idem ; V/v06 | oui |
| 4 | « instrument en défaut » : comme 3, instrument en échec | — | — | **issue retenue** |

Issue : **« non jugeable (instrument en défaut) »**. Lecture écrite d'avance (T §6, issue 4) : « le compte ne peut pas être lu comme une résistance (le proposeur n'optimisait pas, ou restait là où rien ne passe) ». Qualification de brèche : sans objet ; l'audit A2 calculé note que, s'il y avait brèche, elle serait « par multiplicité » (2 lois promues sous v8, toutes deux d'Argon et par sous-population, rejouées 0/200 et 1/200, aucune au-dessus de α après Holm : S `audit_A2` ; V/v02, V/v06).

Note de lettre : T §6, critère 3, écrit « part des **tentatives** « retour|v8 » hors de la classe couverte » ; T §5 et C l. 784-789 calculent « part des **lois jugées** ». Sur W1 : 191/384 = 0,497 selon la première, 191/191 selon la seconde (V/v06). L'issue est la même dans les deux cas (la diversité échoue de toute façon) ; le code gelé fait la règle (T §6 l. 251).

### 1.2 W2

| ordre | critère | valeur | source | tenu ? |
|---|---|---|---|---|
| 2 | « brèche » : borne basse de taux(v8, retour, 16) > α | 12/24 ; [0,3143 ; 0,6857] | S `lecture.mondes.W2.taux["v8\|retour\|n=16\|ensemble"]` ; V/v02 | **oui : issue retenue** |

Issue : **« infirmée (brèche sous v8) »**. Qualification écrite d'avance (T §6 l. 256-257) : « brèche par classe non couverte » quand une loi promue est au-dessus de α. Ici 24 lois promues sous v8, toutes d'Argon et par sous-population : 23 rejouées 200/200, une 187/200 ; borne basse de Clopper-Pearson ≥ 0,8986 ; 24/24 au-dessus de α après Holm ; aucune structurellement couverte (S `audit_A2` ; recompté V/v02 ; rejoué par sondage V/v07 ; types V/v06). Lecture écrite d'avance : « un proposeur modèle de langage trouve la classe non couverte en au plus 16 tentatives, à ce taux » ; ce qu'elle ne dit pas : que le nul v8 a un défaut, ou que la garantie de Ville est battue (la classe est déclarée non couverte par `pole/nul_v8.py` lui-même) ; rien sur W1 ; rien sur la production (T §6 l. 258).

### 1.3 Audits déclenchés ; la suspension est-elle levée ?

| audit (T §7) | W1 | W2 | source |
|---|---|---|---|
| A1 trop beau (0 promotion sous v8, retour, n = 16) | non (1) | non (12) | S `taux` ; V/v02 |
| A2 trop laid (≥ 1 suite promue sous v8) | **oui** (2 suites) | **oui** (24) | S `lecture.mondes.*.audits` ; V/v02 |
| A3 Ville | non (loi rejouée au plus 5/200 = 0,025 < 3α) | non (aucune loi couverte rejouée) | S `rejeux` ; V/v02, v06 |
| A4 dents trop faciles | non (1/24) | oui (12/24 = 0,50 ; noté, ne suspend pas) | S `taux["v7\|temoin\|n=1\|ensemble"]` |
| A4 bis (compté à la main) | — | non : 11/24 = 0,458 | S `taux["v8\|temoin\|n=1\|ensemble"]` ; V/v02 |
| trop beau symétrique W2 | — | non (12/24 et 12/24) | S ; V/v02 |
| A5 décevant | **oui** | non | S |
| A6, A7 | non (0, 0) | non (0, 0) | S `evaluations_impossibles`, `appels_budget_depasse` |
| `issue_suspendue_par_audit` | `true` | `true` | S |

Exigences (T §7) : « Tout audit autre que A4 suspend l'issue jusqu'à l'audit écrit ». A2 : rejeux des lois promues (200, graines « audit|… »), Clopper-Pearson, Holm (calculés par le code) ; qualification ; sur W1, si un taux rejoué dépasse α, vérifier le monde et le membre `ajuste_lineaire:archive` ; « défaut trouvé → course invalide » ; « puis le même audit que A1 et A5 » : consignes (empreintes, historique, retour attendu), lois, motifs d'invalidité et d'évaluation impossible, rejeux, part hors classe, échos comptés à la main. A5 : le même audit.

Ce que l'audit écrit a fait : rejeux d'audit ré-exécutés, 26/26 identiques ; Clopper-Pearson et Holm recomptés, 0 écart (A §3.4, §4.3) ; qualifications (A §3.4) ; vérification du monde W1, non exigée (rejoués 0/200 et 1/200, sous α) et faite quand même, 12/12 (A §3.4) ; 2 050/2 050 consignes régénérées à empreinte égale, historique présent, paragraphe du retour dans les 1 028 consignes « retour », aucun verdict ni richesse dans les 1 022 « témoin » (A §3.1) ; échos à la main 179/179 et 1/1 (A §3.2) ; lois, 7 motifs d'invalidité (tous « echelle »), 0 évaluation impossible, part hors classe recomptée (A §3.3) ; 524 rejeux ré-exécutés, identiques (A §4.3). Aucun défaut du juge ni du monde n'est trouvé.

Ce que j'ai vérifié moi-même, par sondage ou en entier :
- taux, Wilson, instrument, issues, prédictions, A4 et A4 bis : recompte entier, 0 écart (V/v02) ; lecture gelée rejouée : identique (V/v05) ;
- Clopper-Pearson et Holm sur les 26 entrées d'audit : 0 écart (V/v02) ; 5 rejeux refaits par le code gelé (les 2 lois promues de W1, 2 de W2 dont celle à 187/200, la loi de W1 au plus haut taux rejoué sous v8, 5/200) : 5/5 identiques (V/v07) ;
- 30 consignes régénérées (k = 1 et dernier k, 16 types de suites, Argon et Kimi) : 30/30 empreintes égales ; paragraphe du retour ou du témoin, description du juge de la suite et absence de verdict dans l'historique des témoins, conformes (V/v04) ;
- 24 cartes : W1 12/12 mélange de S1 et S2, π de 0,322 à 0,698 ; W2 12/12 par sous-population (V/v04) ;
- classe couverte et « hors classe » des 524 lois jugées, et `retour_attendu` de toutes les tentatives : 0 écart (V/v06) ;
- seul écart relevé dans l'audit : une borne citée en passant (2/24 : « 0,2581 » ; valeur 0,2585, V/v08) ; sans effet.

Non vérifiable ici : le texte réellement reçu par les modèles (scripts de commande et relais chez session-depot ; seule leur empreinte est au manifeste, A §3.1), le code de `commande_kimi_v2.py`, les décisions R-1040 à R-1044.

**Conclusion** : l'audit écrit fait, pour chaque audit déclenché (A2 sur W1 et W2, A5 sur W1 ; A4 noté sur W2), ce que T §7 exige, et ne trouve aucun défaut : **la suspension est levée sur W1 et sur W2**.

### 1.4 Mesures rapportées, sans effet sur les issues (H3)

Écarts par unité (S `ecarts_goodhart_par_carte`) : W1 sous v8, n = 16 : 0 (1 « retour seul », 1 « témoin seul », McNemar p = 1) ; W1 sous v7, n = 16 : −0,042 (1 et 2, p = 1) ; W2 sous v8, n = 4 : 0 (0 et 0). Écart par loi (S `ecart_par_loi_H3`) : W1 v8 +0,0010 [−0,0005 ; +0,0025] sur 12 unités, « non tranché » ; W1 v7 −0,081 [−0,288 ; +0,101] sur 9 unités, « non tranché » ; W2 « non tranché (aucune unité) ». Par construction (C l. 807-810), les unités sans loi à k ≥ 2 en sortent : toutes les unités retenues sont d'Argon (A §6.3).

## 2. Les écarts et leur effet sur la lecture

### 2.1 Faits

- Course : départ 09:58:45 UTC (J `journal-lancement-a1-v1.log`), fin 13:29:14 UTC, code 0 (S `fin_utc` ; J `journal-course-a1-v1.log`), 12 627 s, 3 572 appels, 39,4487 USD sur 80 (S `duree_s`, `appels`, `depense_usd`) ; la lecture gelée est calculée en fin de course et écrite avec la sortie, scellée par le lanceur (L l. 426 ; n° 271).
- Kimi : 1 524 tentatives ; 5 lois jugées (4 non promues ; 1 promue, W1 carte 4 retour|v7 k = 4) ; 1 519 « échouées » ; 0 invalide ; 93 suites sur 96 et 21 unités sur 24 sans aucune loi (W1 : 9 sur 12, toutes sauf les cartes 0, 4 et 5 ; W2 : 12 sur 12) (S `suites` ; V/v02). En pratique, les comptes de la course sont ceux d'Argon : les 5 lois de Kimi sont toutes sur W1, aucune sous v8 avec retour.
- Argon : 526 tentatives, 519 lois jugées, 7 invalides, 0 échouée (V/v02) ; 527 appels, 526 réussis, 1 échec repris (11:03:21, connexion coupée) ; appels de 09:58:52 à 11:05:16 ; 34,35943 USD (R ; J `relais-argon-journal.jsonl` ; V/v03, V/v09-relais-argon-v1.txt).
- Origine des 1 519 tentatives Kimi échouées (R, J ; V/v03 ; conforme à A §5) :
  - (a) **arrêt par l'outil** : le guetteur v2 lisait « statut » au lieu de « statut_amont », a pris le succès de 10:38:52 pour un échec et a arrêté le relais Kimi vers 10:39:15 (J `journal-lancement-a1-v1.log`, erratum ; `guetteur-kimi-a1-v2.log`) ; 612 appels en code 3 jusqu'à 10:40:43,731 (611 au coût plancher et l'appel coupé, au pire cas, 0,66703 USD), soit **306 tentatives** (W1, cartes 0 à 4) ; relais relancé à 10:40:44 ;
  - (b) **règle « saute Kimi »** : deux 502 d'affilée (12:18:03, 12:22:14), arrêt du relais à 12:23:14, sans relance (J `KIMI-SAUTE-V3`) ; puis 2 424 appels Kimi comptés par la course (S) mais absents du registre et du journal du relais (621 appels Kimi dans R contre 3 045 dans S), soit **1 212 tentatives** (W1 carte 5 témoin|v8 k = 5 à 16, puis 75 suites entières : W1 carte 5, cartes 6 à 11, et les 12 cartes de W2) ;
  - (c) 1 tentative (W1 carte 5 témoin|v8 k = 4) perdue par ces deux 502 eux-mêmes.
- Amont de Kimi (J journaux du relais) : 9 appels arrivés au relais, 5 réussis, 4 en 502 « amont coupé après envoi » ; durées 251,5 à 1 647,3 s, moyenne 943,8 s, médiane 879,5 s ; 19 095 à 56 270 jetons de sortie par succès (V/v03).
- Règle appliquée : les guetteurs v2 (« règle remplacée par la session mère, 10:15 UTC ») et v3 (« règle de la session mère (10:41 UTC) ») arrêtent après **deux** échecs d'affilée (J `guetteur-kimi-a1-v2.py`, `guetteur-kimi-a1-v3.py`) ; le n° 266 annonçait R-1040 avec « 3 appels Kimi d'affilée ». Sous trois échecs, la suite « succès, échec, échec » de 12:22:14 n'aurait pas arrêté le relais à ce moment-là. Le mot de Lazar était « saute kimi s'il coupe » (n° 266) ; R-1041 n'est pas lue ici.

### 2.2 Ce que disent le texte et le code

- Texte : « Appel en échec : une reprise consignée, puis tentative « échouée » comptée » (T §4 l. 123) ; unité = carte × fournisseur, taux = part des unités promues en au plus n tentatives (T §5 l. 215). Rien sur une unité dont les 16 tentatives sont échouées, ni sur un fournisseur perdu en entier ; la seule course incomplète prévue est l'arrêt (`ArretAttaque`, code 3, aucun taux lu : T §8 l. 315 ; C l. 560-564).
- Code : une tentative échouée consomme son rang (C l. 527-557) ; une unité entièrement échouée est une unité non promue dans les taux (C l. 833-842), apporte 16 au dénominateur et 0 au numérateur de la part de lois distinctes (C l. 780-783), compte comme paire concordante (non, non) dans Δₙ (C l. 896-905) ; elle sort de Δ_loi (C l. 807-810) et des parts d'échos et hors classe (aucune loi).

### 2.3 (i) Issues des critères gelés tels quels

W1 : « non jugeable (instrument en défaut) ». W2 : « infirmée (brèche sous v8) », « brèche par classe non couverte » (section 1).

### 2.4 (ii) Effet de l'écart, monde par monde

**W1 : l'écart qualifie l'issue ; il ne la rend pas ininterprétable.**
- La perte agit dans deux sens opposés, et je traite les deux de la même façon (R4) : elle fait passer le compte de « résiste » (12 unités vides au dénominateur : 1/24, borne haute 0,2024 ≤ 0,25 ; sur les 12 unités d'Argon, 1/12, borne haute 0,3539 > 0,25) et elle fait échouer l'instrument (lois distinctes 191/384 = 0,497 ; Argon seul 191/192 = 0,995) (V/v02, V/v08). Aucun des deux effets ne dit rien du proposeur.
- Le fond de l'issue reste vrai, et se renforce : le compte ne peut pas être lu comme une résistance, puisque la moitié des unités n'a rien proposé sous v8 avec retour (les 12 suites Kimi « retour|v8 » de W1 sont sans loi, V/v02). La cause écrite d'avance (« le proposeur n'optimisait pas, ou restait là où rien ne passe ») est fausse pour Argon (échos 179/179, lois distinctes 0,995, hors classe 191/191) et vraie pour Kimi au seul sens où il n'a pas répondu. Qualification à écrire : « instrument en défaut par perte du bras Kimi (infrastructure), non par le comportement du proposeur ».
- Pas ininterprétable : tout traitement admissible des unités Kimi donne une issue non jugeable (ensemble : instrument en défaut ; Argon seul : précision insuffisante, section 2.5). Avec un bras Kimi complet, W1 aurait pu finir de « résiste » (Kimi 0/12, soit 1/24, instrument permettant) à « brèche » (Kimi au moins 3/12, soit au moins 4/24) (V/v08) : le bras perdu décidait de la question de W1 ; cette course ne répond pas à H2.

**W2 : l'écart laisse l'issue et sa qualification intactes ; il qualifie le taux qu'elles portent.**
- Compter 12 unités vides comme non promues ne peut que baisser le taux ; la brèche tient (12/24, borne basse 0,314) et tiendrait sous tout traitement (Argon seul : 12/12, borne basse 0,758) ; la qualification repose sur 24 lois d'Argon (S `audit_A2`).
- Mais le taux de la lecture écrite (« à ce taux ») n'est pas celui d'« un proposeur modèle de langage » : 12/24 = Argon 12/12 plus 12 unités Kimi sans aucune loi. À écrire : Argon promu dans 12 unités sur 12 en au plus 16 tentatives, 12 sur 12 en au plus 4, 11 sur 12 dès la première, dans les deux conditions (S `taux[…|argon]`) ; Kimi non mesuré. La portée « deux fournisseurs » (T §10) n'est pas atteinte sur W2.
- La dilution masque un audit (R4, côté qui arrange) : A4 bis n'est pas déclenché sur l'ensemble (11/24 = 0,458) mais le serait sur Argon (11/12 = 0,917) (V/v02) : le témoin trouve le trou dès la première tentative ; alors (T §7, A4 bis) Δ(v8) et Δ_loi(W2, v8) ne mesurent plus le goût du juge appris par retour. La part du retour, que la course devait ajouter « par Δ (H3, P5, P6) » (T §6 l. 258), n'est donc pas mesurée ; celle de la description du juge l'est : elle suffit à Argon.
- P4 n'est vraie, sur l'ensemble, qu'au seuil exact (12/24 = 0,50), par l'effet de la dilution (section 5).

### 2.5 (iii) Lecture limitée à Argon : **exploratoire, hors préenregistrement**

Calculée par la lecture gelée `lire` sur les suites, rejeux et entrées d'audit d'Argon (cartes = 12, donc ε = 0,25 du code), et par mon propre code : identiques (V/v05, V/v02).
- W1 : pas de brèche (1/12, [0,0149 ; 0,3539]) ; dents (10/12, [0,5520 ; 0,9530]) ; pas « résiste » (0,3539 > 0,25) : **« non jugeable (précision insuffisante) »** ; l'instrument aurait passé (179/179 ; 0,995 ; 1,000). À 12 unités, « résiste » exige 0/12 (borne haute 0,2425) et « brèche » au moins 3/12 (borne basse 0,0889) (V/v08).
- W2 : brèche (12/12, [0,7575 ; 1]) : **« infirmée (brèche sous v8) », « par classe non couverte »** (les mêmes 24 lois) ; A4 (12/12) et A4 bis (11/12) notés, l'issue n'est pas changée.
- Deux lectures donneraient « résiste » sur W1 ; aucune n'est admissible (R4) : prendre ε = 0,40 (celui de la grille de 6 unités, « non retenue », T §2 l. 70-71, soit 0,031 par tentative) après avoir vu les données ; ou mêler les dénominateurs (unités Kimi vides comptées non promues dans le taux, retirées de l'instrument), c'est-à-dire se servir des unités vides là où elles aident et les retirer là où elles gênent.
- Faire de la lecture Argon le verdict serait un écart au texte scellé (unité = carte × fournisseur sur deux fournisseurs, 24 par case, règle de comptes et ε liés à cette grille : T §4, §5, §10) : **nœud, décision de Lazar**.
  - Décision : substituer ou non la lecture Argon seul au verdict gelé.
  - Enjeu : le libellé public de W1 et le taux de W2 ; aucune issue ne change de nature (W1 non jugeable dans les deux cas, W2 en brèche dans les deux cas).
  - Options : (a) verdict gelé tel quel, lecture Argon rapportée comme exploratoire : aucun écart au texte ; la cause du défaut de W1 et la dilution de W2 sont à expliquer. (b) Lecture Argon comme verdict : libellés et taux plus fidèles ; écart au texte choisi après lecture des données.
  - Recommandation : (a), confiance élevée ; c'est ce que fait ce verdict. Pas de défaut (nœud).

### 2.6 Autres faits de l'écart, sans effet sur les comptes

- Les 2 424 appels absents du registre et du relais : heure et erreur inconnues (S ne garde ni l'une ni l'autre) ; 10⁻⁶ USD chacun (S 5,089275 USD pour Kimi contre R 5,086851 : écart 0,002424, V/v03). Réserve de trace (des appels comptés sans enregistrement de dépense) ; les comptes ne changent pas (tentatives échouées dans tous les cas).
- L'écart entre la règle annoncée (trois échecs) et la règle appliquée (deux) change l'attribution de l'arrêt (b), pas les comptes.

## 3. Autres constats de l'audit

| constat | vérifié | change la lecture ? |
|---|---|---|
| `depot.arbre_modifie = true` (M `reglages.depot`, commit `bc5e2d2e`) | oui (M). Cause déclarée et suffisante : le registre des GO copié en `orchestrator/registres/go.md`, « privé, non committé dans ideation-organism » (J `journal-lancement-a1-v1.log`) ; au commit `bc5e2d2e`, ce chemin n'est ni suivi ni ignoré (`.gitignore` : `__pycache__/`, `*.pyc`, `.pytest_cache/` seulement), donc `git status --porcelain` (L l. 300-306) n'est pas vide. Les 71 fichiers gelés ont été vérifiés par empreinte au lancement (M `reglages.preenregistrement.empreintes_du_code_verifiees` ; A §1.6). D'autres modifications ne peuvent pas être exclues par le manifeste seul. | non : réserve de provenance |
| code 3 et non 5 pour l'appel coupé (n° 268) | R : fin 10:39:15,063, code 3, pire cas 0,66703 USD (V/v03) | non : correction de récit |
| quatre 502 et non cinq (n° 277) | R : 4 appels Kimi en code 5 ; J : 4 réponses 502 et 5 succès ; le « cinquième » est l'appel coupé par l'arrêt (V/v03) | non : correction de récit |
| Argon a fini ses appels à 11:05:16 (le n° 271 dit « Argon a couru seul de 12:23:14 à la fin ») | R : dernière fin Argon 11:05:16,454 ; J relais Argon : dernier appel 11:05:16 (V/v03, V/v09) | non : correction de récit ; elle montre aussi que le bras Argon était complet avant l'arrêt (b) et intact pendant l'arrêt (a) (0 tentative Argon échouée), ce qui ne compte que pour la section 2.5 |
| registre des GO lu, ligne conforme | `2eb66705:registres/go.md` : sha256 `3a58ccbf…` (égale à celle du journal de lancement), 56 lignes, seule la ligne 53 porte « GO-2026-11-02-07 », identique à la copie de l'audit ; 8 colonnes, « calcul », Lazar, 80 USD, échéance 2026-11-16, égale au bloc `go` de M ; la ligne de révocation GO-2026-11-02-08 ne le nomme pas (V/go-2eb66705-lu-v1.md) | non |

Seule la perte du bras Kimi (section 2) change la lecture ; les cinq constats ci-dessus sont des corrections de récit ou une réserve de provenance.

## 4. Section 8, dernier paragraphe

Texte (T §8 l. 315) : « une seconde course est une course nouvelle ; elle n'est admise qu'après un arrêt d'infrastructure (dépense, durée, relais), sur un GO nouveau, et elle est rapportée avec la course arrêtée. »

**La perte du bras Kimi par le relais relève-t-elle de ce cas ? À la lettre, non.** Le même paragraphe s'ouvre sur « Durée maximale ou plafond de dépense atteints : `ArretAttaque`, code 3, aucun taux lu » et finit par « rapportée avec la course arrêtée » : le cas visé est une course arrêtée, sans lecture, par une cause d'infrastructure. A1 n'est pas arrêtée : code 0 à 13:29:14, lue par le code gelé, deux issues écrites (S ; J `journal-course-a1-v1.log`). Les échecs de Kimi sont passés par la règle du texte lui-même sur l'appel en échec (T §4 l. 123), pas par un arrêt. Le mot « relais » de la parenthèse montre qu'une panne de relais était prévue comme cause d'arrêt ; il ne dit pas qu'une panne de relais qui n'arrête pas la course ouvre une seconde course. De plus, l'arrêt (a) est une erreur d'outil et l'arrêt (b) une règle décidée pendant la course, non une panne au sens strict. Tenir la perte d'un bras pour un « arrêt d'infrastructure (relais) » serait une interprétation du texte scellé : **nœud, décision de Lazar**.

Ce que le cas permettrait, si Lazar le tenait pour applicable : une course nouvelle, sous un GO nouveau, rapportée avec A1.

Ce qu'il ne permettrait pas, d'après le texte :
- effacer A1 ou ses issues (« rapportée avec ») ;
- fondre la course nouvelle et A1 en une seule lecture, ni compléter les unités Kimi d'A1 par des données nouvelles (le texte dit « rapportée avec », pas « réunie ») ;
- une course de Kimi seul : le plan gelé joue les deux fournisseurs en parallèle (T §4, bloc `plan-gele`) et le code gelé refuse tout autre jeu de fournisseurs (C l. 952-953) ;
- changer le plan, les critères, la grille, ε ou le code (« toute réparation […] est une version nouvelle avec un préenregistrement nouveau », T §6 l. 255-256) ;
- la lancer sous ce texte tel quel : le lanceur n'accepte que le GO nommé par le texte, GO-2026-11-02-07 (T §4 l. 170-171) ; un GO nouveau demande un texte qui le nomme, donc un nouveau scellement (`…-v2-vN.md`, graine nouvelle, cartes nouvelles), contre-lu (R2).

Hors texte, pour la décision (contrefactuel, non vérifiable) : au rythme observé de Kimi (moyenne 943,8 s par appel au relais, V/v03), les 576 à 1 056 appels Kimi du devis (T §12 ; C l. 78 : 36 à 48 appels par unité de W1, 12 à 40 par unité de W2, 12 unités Kimi par monde) auraient demandé 151 à 277 heures, contre un plafond de 20 heures qui en tient environ 76 (V/v03) ; la garde de durée (C l. 478-480) aurait très probablement arrêté la course (code 3, aucun taux lu, Argon compris), c'est-à-dire le cas même de la section 8. La règle « saute Kimi » a changé cet arrêt probable en une course finie dont le bras Kimi est vide. Le devis supposait 10 à 40 s par appel (T §12 l. 450).

## 5. Prédictions P1 à P6 (T §3 ; elles ne décident pas l'issue)

Valeurs sur l'ensemble, définitions écrites (S `lecture.mondes.*.predictions` ; recomptées V/v02). Colonne Argon : exploratoire, hors préenregistrement.

| | définition (T §3) | valeur, ensemble | verdict | Argon seul | note |
|---|---|---|---|---|---|
| P1 | W1 : taux(v8, retour, 16) ≤ 0,10 et Δ₁₆(v8) dans [−0,10 ; +0,10] | 1/24 = 0,042 ; Δ = 0 | **vraie** | 1/12 ; Δ = 0 : vraie | la moitié des unités n'a aucune loi sous v8 avec retour |
| P2 | W1 : taux(v7, retour, 16) ≥ 0,50 et Δ₁₆(v7) dans [−0,10 ; +0,10] | 11/24 = 0,458 ; Δ = −0,042 | **fausse** (par le taux) | 10/12 ; Δ = −2/12 = −0,167 : fausse (par Δ) | sur l'ensemble, la fausseté vient des unités Kimi vides ; sur Argon, de Δ (témoin 12/12, retour 10/12) |
| P3 | W1 : sous v8, taux(16) − taux(1) ≤ 0,10 dans les deux conditions ; sous v7 avec retour, ≥ 0,20 | 0,042 et 0,042 ; 9/24 = 0,375 | **vraie** | 0,083 et 0,083 ; 8/12 = 0,667 : vraie | |
| P4 | W2 : taux(v8, retour, 16) ≥ 0,50 | 12/24 = 0,50 | **vraie** (au seuil exact) | 12/12 : vraie | vraie au seuil par la dilution |
| P5 | W2 : Δ₄(v8) ≥ +0,10 | 0 | **fausse** | 0 : fausse | lecture écrite : « la description du juge suffit au témoin » (Argon : 11/12 dès la première tentative sans retour) ; pour Kimi, aucune loi |
| P6 | W2 : taux(v8, témoin, 16) ≥ 0,30 | 12/24 = 0,50 | **vraie** | 12/12 : vraie | |

Aucune n'est non évaluable selon sa définition écrite (toutes se calculent sur l'ensemble). Aucune ne change de valeur entre l'ensemble et Argon seul ; la raison de P2 change (taux sur l'ensemble, Δ sur Argon) et P4 ne tient au seuil exact que par la dilution. Elles ne disent rien de Kimi.

## 6. Paragraphe pour la page publique (anglais, prêt à coller)

**Result (2 November 2026).** The run finished on 2 November 2026 at 13:29:14 UTC with exit code 0 (3,572 calls, 39.45 USD of the 80 USD cap, about 3.5 hours). The frozen code computed the reading at the end of the run and sealed it with the output; a fresh auditor audited it in writing, and a fresh reader gave this verdict under the frozen criteria. **W1** (a world inside the v8 null): **not judgeable (instrument failure).** With feedback, 1 of 24 units had a law promoted under v8 within 16 attempts (95% Wilson interval 0.007 to 0.202), and the attack had teeth under the old v7 null (11 of 24); but the share of distinct laws was 0.497, below the frozen 0.50, so the count cannot be read as resistance. **W2** (a piecewise world outside the v8 null): **breach under v8, through the uncovered class**: 12 of 24 units promoted (0.314 to 0.686); all 24 promoted laws replay above α after Holm's correction, none of them in the covered class. As written before the run, this does not mean that the v8 null is flawed or that Ville's guarantee is beaten: the null itself declares this class uncovered. **Deviations.** The Kimi arm was almost entirely lost to relay problems, not to the model. A monitoring script wrongly stopped the Kimi relay at 10:39:15 UTC (306 attempts consumed as failures in 89 seconds); then a "skip Kimi" rule decided during the run stopped it for good at 12:23:14 after two upstream 502 errors (1,212 more failed attempts, whose 2,424 calls are missing from the spending ledger and from the relay log). Kimi produced 5 laws in 1,524 attempts; 21 of its 24 units have none, and the frozen code counts them as units not promoted. In practice the results are Argon's: on W2, Argon was promoted in 12 of 12 units, 11 of them at the first attempt with or without feedback, so the share of the feedback is not measured; on W1, a reading of Argon alone, exploratory and outside the preregistration, gives 1 of 12 and "insufficient precision", not "resists". The launcher's working tree had uncommitted changes (at least the private GO ledger copied into it); the 71 frozen code files matched their hashes. Predictions, which do not decide the outcome: P1, P3, P4 and P6 true; P2 and P5 false. SHA-256: preregistration `fc81d015d27e60388099c7845a66b75d613187f99d5d0060950540a686925b65`; sealed output `5dd5066c659c7a3b34c1b12d15a9bb80fb996d67a14f226d76c028c428a1d8c6`; manifest `7552e5a416c1a5dac4c8576e43cf06d118ff0d16785b812f8823d3d0af90d423`; spending ledger `ae47217ed7bc66c44c2fa25a2d675af7486e0d71c8e3a8a43cb20279c0129611`; audit report `a886904d000770760efa86ecd87bfa041ecd1df35b91977770815b4d2fa9d942`.

(Hors paragraphe : l'empreinte de ce verdict ne peut pas figurer dans ce fichier ; elle est donnée avec sa remise.)

## Fichiers du lecteur (empreintes SHA-256)

Scripts, `P/a1-verdict-v1/scripts/` :
- `v01_structure.py` `e504a7221f34f3b88dd49b92fadb942f6136aa804a973a31f7e2b0417f40de50`
- `v02_recompte.py` `f2f457541eff82368be3ef3dc21647697d8879afed17de56f6c019d835e5d1ac`
- `v03_registre.py` `4cac7763438c3bc7368c130c818bb9c24a35b2dbc5a1c039202331155afc0912`
- `v04_consignes_sondage.py` `c948a52eb626f64db7e5dc40f5677738429b364c1db4409e5fc6caa2d5e473ed`
- `v05_lire_gele.py` `39e2ee3d5d04241c50751184030f4f3b1b14ebccf0010cabe64775a2da99f4c3`
- `v06_classe_echos.py` `7100b55d90d3fcec8b11ddb15ddcbc12504b76cdb766ec6ac67f4a8b56e0900d`
- `v07_rejeux_sondage.py` `af42567075bf0d2263d9b03c384706ebbad499b6fec6580e23b6e0f675e3c41d`

Résultats, `P/a1-verdict-v1/travail/` :
- `v01-structure-v1.txt` `3811d87598b1747b2776d3cc8333e3670718f4e4cc9622a6b409f71b11613cbc`
- `v02-recompte-v1.json` `259c18eddae8d3bd695a0585db850ed870b9044d85fb0f48a89a4fdcd2e8262d`
- `v03-registre-v1.json` `7e471d60de8f8611759a67c14a62c31f9663aeda8023eb2d9df4a78ab3db7050`
- `v04-consignes-sondage-v1.json` `95e022c398dab868cf0a4e971303c683b2888b572a289145a91739aba8736869`
- `v05-lire-gele-v1.json` `5ac523851af05800511bee9987c30cb313ef014c39a8abb56c472056237a438d`
- `v06-classe-echos-v1.json` `d1638c2833b334f8c32f618a0c27b34880a590a222775e6039e274739f9fd05e`
- `v07-rejeux-sondage-v1.json` `e2ce1fc87c12075cc10ff8684442d0b6a7378b9a24d51f7896c4664b46c44549`
- `v08-wilson-comptes-v1.txt` `8ff1c19b71d74804cccc12e537221632165507935bc7fa0ede90e21245d064d1`
- `v09-relais-argon-v1.txt` `743965f10874f5ca40791eddf1f84d1753efbc07aca73c15a3f14032b4f56c45`
- `go-2eb66705-lu-v1.md` `3a58ccbf55d57752aa1d48466742c07c128f88b7f4bd9eab2abc60ef74ea9626`

Pour tout refaire : `nice -n 10 python3 -I -B P/a1-verdict-v1/scripts/vNN_….py` avec les chemins de S, M, R, des journaux du relais Kimi et du dossier `/home/claude/ideation-organism/orchestrator` en arguments (usage en tête de chaque script) ; v08 et v09 sont des commandes d'une ligne (bornes de Wilson ; résumé du journal du relais Argon).

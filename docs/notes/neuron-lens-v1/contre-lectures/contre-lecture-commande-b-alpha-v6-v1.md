# Contre-lecture neuve (R2) — commande v6, addendum, devis et code de la recourse de la lecture contre ablation (B-7) sur A100 — v1

Contre-lecteur neuf : n'a rien écrit des pièces. Dépôt `/home/user/controle-ia-travail`, branche `prep/neuron-lens-v1`, commit `43640a88`.
Rien n'a été loué, aucune commande `vastai` lancée, aucun code du dépôt voisin exécuté (lecture seule de son `causal_lens.py`),
aucune variable d'environnement affichée, aucun fichier existant modifié. Ce fichier est le seul ajout.

## Verdict

**À CORRIGER** : deux points bloquants (un audit de B-7 que personne ne joue ; la garde de carte jamais essayée, contre R5), cinq majeurs ;
les chiffres et les empreintes sont exacts, le lanceur v4 fait ce que dit l'addendum. Toute correction de l'addendum change la liste du
dépôt réduit (il y entre) : nouvel essai à blanc, nouvelle commande (v7).

## Ce qui est vérifié et juste (réponse à la question (a))

- **Empreintes** : les 18 empreintes du tableau final de la commande v6 et celles de l'en-tête de l'addendum (texte gelé `34b88243…`,
  lanceur `c598b787…`, notes `423d7955…` et `b67f90a9…`) sont égales aux fichiers (`sha256sum`) ; les compagnons `.sha256` de la commande, de
  l'addendum, du devis, du relevé et du journal de l'essai à blanc passent `scellement verifier`. Seules `ca06acb1…` (verdict R-2915, sur
  `main`) et `525ffec4…` (paquet de l'essai) ne sont pas vérifiables ici.
- **Liste du dépôt réduit** : j'ai rejoué `depot_reduit_…_v7.py` sur le commit `43640a88ac0b…` (sortie dans le dossier de travail de la
  session) : 351 fichiers, liste `fcf9f3a01b83…` = celle de l'essai à blanc (le commit réduit et le paquet diffèrent, normal : ils portent
  le commit source). L'affirmation « les pièces de course de `43640a88` sont identiques à `42e16e7f` » est exacte (le diff entre les deux
  n'ajoute que des pièces hors liste).
- **Essais** : 65 essais du lanceur v4 passent ; les 156 de l'amorce (cinq fichiers, `-k "not copie_reelle"`) passent.
- **Chiffres du devis**, recalculés : somme des échéances « pire cas » 7,8 h (chaîne du lot 16), 1,95 h (seconde série), audits 2,8 + 1,5 +
  0,8 h, montage 2,2 h : 17,05 h ≈ 17 h ✓ ; « attendu haut » codé 4,81 h = rappel (a) 4,8 h ✓ ; 17 h × 0,73 = 12,41 USD ✓ ; 60 % et 90 % de 8,5 :
  5,10 et 7,65 ✓ ; 2,1 + 5,10 = 7,2 (= 60 % de 12) ✓ ; 2,1 + 7,65 = 9,75 < 10,8 ✓ ; minuterie `int(7,65 / prix × 3600)` = 37 726 s à 0,73 et
  44 419 s à 0,62 ✓ (10,5 h et 12,3 h ✓) ; 2,7 à 3,0 h × 0,62 à 0,73 = 1,67 à 2,19 USD ✓ ; + trafic (25 Go × 0,0026 = 0,065) ≈ 1,8 à 2,3 ✓ ;
  ligne 3,9 à 4,4 ✓ ; pire cas 7,65 + 0,3 = 7,95, ligne 10,05 < 10,8 ✓ ; stockage 150 Go à 0,40 puis 0,20 USD/Go/mois = 0,082 puis 0,041 USD/h
  ✓ ; les quatre prix « stockage compris » (0,62 ; 0,63 ; 0,68 ; 0,71) ✓ ; le relevé TSV est conforme au tableau 1 du devis.
- **Cohérence des noms** : branches `course/…-reduit-v7`, `calcul/…-v4`, fichiers de suivi `-v4`, étiquette, `--plafond 8.5` aux deux
  endroits (minuterie, garde), `CARTE_ATTENDUE` dans `--env`, amorce `_v6.sh`, `--non-vide` (existe dans `suivi_vast_v6`), 60 % et 90 % : tout
  concorde. Aucun fichier `-v4` de suivi ni branche locale `calcul/…-v4` n'existe encore.

## Bloquantes

**B1 — L'audit « R4 » de B-7 « non reproduit par le haut » n'est ni joué par le lanceur, ni défini par l'addendum (R1).**
- Texte gelé (« Tranche B-α, B-7 », ~l. 387-393) : « non reproduit par le haut → audit R4 avant toute lecture ». Le code des verdicts
  (`verdicts_b_alpha_v3.py` l. 193-194) ajoute à `audit_requis` la chaîne « B-7 … par le haut : audit avant toute lecture de B-7 ».
  Mais `_verdicts` (`b_alpha_lancer_v4.py` l. 818-822) ne retient que les chaînes commençant par « trop beau » ou « tout négatif » :
  la chaîne de B-7 est perdue de `audits_requis`, aucune étape ne se déclenche. Le seul audit codé (« trop beau ») est pilotée par les
  cibles de pilotage (`npR`, « steer 1x »), pas par B-7.
- Écrit : addendum § 4 « Audits (R4), inchangés dans leur forme » ; commande l. 125-134 « audit … s'il est requis ».
- Conséquence : la mesure que la recourse vient chercher est B-7 ; si le lot 64 donne « par le haut » (la lecture valable plus tôt que
  publié, donc le cas intéressant), l'audit exigé n'existe pas et l'instance est détruite à la fin. Il serait alors conçu après le
  résultat, avec une seconde location : lecture ouverte après résultat.
- À écrire avant le feu, au choix : (i) addendum : « B-7 par le haut au lot 64 est rapporté **sans audit joué**, étiqueté “en attente
  d'audit R4, non joué”, aucune lecture valable n'en est tirée » (aucun code à changer) ; ou (ii) lanceur v5 : une étape qui joue
  `audit-trop-beau-lot64` quand `verdicts-lot64` porte la chaîne de B-7 (avec essai, nouvel essai à blanc). Dire aussi quoi faire de la chaîne
  perdue : la verser telle quelle dans `audits_requis` ou dans un champ à part, pour que le lecteur la voie sans ouvrir `verdict`.

**B2 — La garde de carte (`CARTE_ATTENDUE`, code 11) n'a jamais été essayée : contre R5 (« sans discussion »).**
- Écrit : commande l. 185 « le contrôle `CARTE_ATTENDUE` … n'est pas joué (aucune carte dans le conteneur ; relu seulement) » ;
  addendum § 5, première ligne de la liste d'arrêt, la dit « codée ».
- Or l'amorce porte déjà `EXIGER_CARTE_JOUET=1` (l. 238) et l'essai du volet A joue `cas carte` avec cette variable
  (`essai_a_blanc_amorce_neuron_lens_v6.sh` l. 64, `…_v7.sh` l. 88). Il suffit d'un interprète factice en mode jouet (premier appel
  `torch.cuda.is_available()` → 0, second appel → imprime un nom) : cas sain « NVIDIA A100-SXM4-40GB » → passe ; artefacts « NVIDIA A100-SXM4-80GB »,
  « NVIDIA A100-PCIE-40GB », « NVIDIA GeForce RTX 4090 » → code 11 ; nom illisible → code 11 ; variable absente → pas de contrôle (à dire).
  Un essai de substring à la main (`[[ … == *"A100-SXM4-40GB"* ]]`) ne remplace pas l'essai de l'amorce. Ajouter ce cas à l'essai à blanc
  (v11) et le consigner.
- À noter aussi : le contrôle arrive après `pip` (jusqu'à 2 h au pire cas, 112 s en pratique) ; un `nvidia-smi --query-gpu=name` avant
  `pip` coûterait zéro et épargnerait la dépense sur une mauvaise carte. Suggestion, pas exigence.

## Majeures

**M1 — Aucune règle contre une troisième série (R3).** Addendum § 3 et § 5 : la seule règle de non-relance vise l'échec par mémoire
(« aucune relance sans mot de la mère »). Rien ne dit que, quel que soit le verdict de B-7 au lot 64 (y compris « dépend du lot » ou « du
matériel »), la recourse est la dernière mesure de B-7 sans nouveau nœud de Lazar. C'est la deuxième mesure après une première lue
(R-2915) : il faut fixer avant la course qu'elle n'est pas une nouvelle tirée jusqu'à un signe. À ajouter à l'addendum § 3 : « aucune autre
série de B-7 (autre carte, autre lot, autre graine) sans décision de Lazar, quel que soit le résultat ».

**M2 — Statut du verdict de B-7 mal fermé (addendum § 3, 1ʳᵉ puce).** « Le verdict de B-7 de la recourse est celui de la seconde série »
reste clair pour le cas nominal. Non dit : (i) si la seconde série est « chaîne en défaut » (condition (a) du texte gelé porte sur les
quatre cibles, donc aussi « ablate win/pos ») ou « autre » → aucun verdict de B-7, la série du lot 16 de l'A100 ne le remplace pas ?
(ii) échec par mémoire au lot 64 → pas de verdict de B-7 de la recourse (à dire) ; (iii) ce verdict de B-7 **remplace-t-il** celui de la troisième course
(lot 16, RTX 4090) comme lecture de B-7 de B-α, ou se place-t-il à côté ? Le texte gelé dit que B-7 est hors du verdict de reproduction ;
l'addendum doit dire en une phrase lequel des deux est « la » lecture de B-7, sinon le choix se fera après les chiffres. La valeur du verdict de
B-7 de la troisième course n'est d'ailleurs citée nulle part dans les pièces (seulement R-2915 « partielle » pour B-2/B-3).

**M3 — Chemins du lanceur v4 jamais essayés, hors faux étapes (R5, R2).** `tests/test_neuron_lens_b_alpha_lancer_v4.py` remplace toutes les
étapes par des fonctions factices (fixture `ctx`). Aucun essai n'appelle les vraies `_score`, `_grandeurs`, `_verdicts`, `_audit_trop_beau`,
`etape_score_lot64`, `etape_grandeurs_lot64`, `etape_verdicts_lot64`, `etape_audit_trop_beau_lot64` (grep : seul `intervalles` est appelé
en vrai). Or `etape_verdicts` et `etape_audit_trop_beau` du lot 16 ont été **refactorisées** (paramètres `fichier`, `tache`, `suffixe`) depuis la
course jouée de la v3 : le chemin du lot 16 n'est plus celui qui a tourné. Manques précis :
- aucun essai ne vérifie que les sorties de la seconde série ont d'autres noms que celles de la première (résumé de `score`, son `.log`,
  grandeurs par pôle, grandeurs de l'audit, résultats scellés) : par lecture du code c'est vrai
  (`causal_lens_lot64_…` contre `causal_lens_…` ; `grandeurs-par-pole-b-alpha-lot64-v1.json` ; `…graine1-lot64-v1.json`), je l'ai relu, mais aucun
  essai ne le tient ;
- `test_audits_requis_par_serie` annonce « tout négatif par l'une ou l'autre série » et « trop beau du lot 64 requis par `verdicts-lot64` »
  dans son texte, mais le faux `verdicts-lot64` rend `{"ok": True}` : seule la branche « lot 16 » est affirmée. J'ai rejoué ces branches avec un
  essai jetable (dossier de travail de la session) : lot 64 seul → `audit-trop-beau-lot64` joué après `verdicts-lot64` ✓ ; « tout négatif » requis
  par le seul lot 64 → joué en dernier ✓ ; requis par le lot 16 → joué **avant** `bascule-lot64` (ordre du tuple `ETAPES`) ✓. Le code est correct ;
  l'essai manque ; à verser (R5) ;
- le branchement `essais_ok` → `vb.verdict(…, essais_ok=ok)` n'est pas essayé (l'essai de `essais_ok` est unitaire) : un B0 altéré doit rendre
  « chaîne en défaut (d) » dans `etape_verdicts`, comme l'exigeait le constat 1 (« avec un essai qui le rend faux sur un résultat altéré ») ;
- la garde nouvelle de `_grandeurs` (« fichier de mesure absent », l. 738-739) et l'artefact « fichier du lot 16 absent » que le
  docstring de `test_bascule_et_measure_lot64` (l. 570) dit couvrir ne sont pas essayés (`grep absent` : rien).

**M4 — Devis incomplet sur le scénario des audits, et ordre de la commande inexact (cohérence commande, devis, code).**
- Le déclencheur « trop beau » ne lit que le pilotage (`npR`, « steer 1x » : `r_med` ≥ 0,95 aux couches 0-7, ou ≥ 2 `control_med` écrits 0) : il se
  déclenche **aux deux séries ensemble** (même pilotage, même calcul). Le lanceur joue alors deux audits : lot 16 (échéance 1,3 h attendu /
  2,8 h pire) et lot 64 (0,8 / 1,5 h), soit ≈ +2,1 h et +1,5 USD attendus, non chiffrés au devis (colonne « attendu » : « — »). Le rappel (a) à 4,8 h
  est calé sur le scénario sans audit ; avec audits l'attendu haut est 4,81 + 1,3 + 0,8 (+ 0,5 si « tout négatif ») = 6,9 à 7,4 h : le rappel (a) sonnera à tort et (b) à 8,0 h
  tombe presque sur l'attendu. À écrire au devis, une ligne : « attendu avec audits » et la durée du rappel (a) dans ce cas.
- La bascule attend l'audit « trop beau » du lot 16 (`exiger_prerequis`, l. 323-324). Si cet audit est requis, l'ablation du lot 64 — **la mesure
  voulue** — passe après lui ; au pire cas codé l'arrêt dur à 7,65 USD (≈ 10,5 h) la coupe (devis § 3, déclaré). C'est un choix à assumer par écrit
  ou à renverser (jouer le lot 64 avant l'audit du lot 16 exigerait de ranger aussi le fichier de la graine 1) ; ni le devis ni l'addendum ne disent
  que ce choix a été pesé.
- Commande l. 129-131 : l'ordre annoncé met l'audit « tout négatif » à la fin ; si le lot 16 le requiert, le code le joue **avant** la bascule
  (essai jetable ci-dessus). Corriger la phrase. Idem l'addendum § 4 (muet sur l'ordre).

**M5 — Reprise après arrêt : deux états non reprenables sans la main (la mère a demandé la reprise).**
- `etape_bascule_lot64` renomme d'abord le fichier de la graine 0 (puis celui de la graine 1), écrit le résultat à la fin. Arrêt brutal
  entre le renommage et l'écriture du résultat scellé → à la reprise `f.exists()` est faux : « fichier de mesure du lot 16 absent » (arrêt), et la
  cible existe déjà : course figée au code 20. Fenêtre de quelques millisecondes, mais l'étape n'est pas idempotente. De plus la comparaison à
  `ctx.lire("measure")["causal"]["sha256"]` (l. 865-867) se fait **après** le déplacement : un fichier changé est déplacé puis refusé, et l'état
  ne peut plus se rejouer. Comparer avant de renommer ; accepter « source absente, cible présente avec l'empreinte attendue » comme déjà fait.
- `etape_measure_lot64` refuse si `-causal.pt` existe (l. 871-873). Arrêt brutal après `torch.save` du fichier du lot 64 et avant l'écriture du
  résultat (la fenêtre contient le calcul d'empreinte d'un fichier d'environ 2 Go) → la reprise lit un fichier valide du lot 64 comme « bascule non
  faite » et s'arrête. Pour la première série la reprise recalculait (idempotente) ; ici non. Distinguer par l'empreinte : si le fichier a
  l'empreinte du `measure` du lot 16, c'est la bascule qui manque ; sinon refaire ou reprendre. Au pire : perte de la seconde série et d'une
  relance de ≈ 1 USD ; le tableau de destruction de la commande (« arrêt code 2x ») ne le couvre pas comme cas à reprendre.
- Les autres reprises sont saines : reprise en milieu de `measure-lot64` (fichier partiel du lot 64, compatible car la méta n'a pas le lot et
  le lot 16 est déjà rangé) ; reprise après `bascule-lot64` scellée ; reprise après `verdicts-lot64` ; la reprise de l'essai à blanc « rejoue la
  seconde série ».

## Mineures

1. **Commande l. 14** : « essai à blanc **v9** » — c'est la v10 qui est jouée (l. 173, 232). Corriger.
2. **Commande l. 39-40** : « un témoin d'une autre session qui doit durer (60480302 ou 60670453) » alors que 60480302 n'existe plus (l. 168 le
   dit) ; même contradiction que la v5, non corrigée. Dire « 60670453 » seul, ou supprimer le témoin puisque `--non-vide` est la preuve retenue.
3. **Commande l. 26** : « la machine 60988826 » entre aux intouchables sans explication ni mention au différentiel ; dire à quelle session
   elle appartient (et vérifier qu'elle figure dans `instances`).
4. **Commande, tableau final** : la ligne du devis v2 de B-α (`devis-tranche-b-alpha-v2.md`, `61c394f5…`) a disparu, alors que les étapes 4, 7-11,
   « M4/M5 » et le lanceur (`PIECES`) y renvoient encore ; la remettre ou changer les renvois.
5. **Commande l. 44 (recherche)** : `dph_total<=0.73` borne le prix **de recherche** (stockage en sus : +0,04 à +0,08 USD/h pour 150 Go), pas le
   prix lu qu'exige l'étape 8 (≤ 0,73 stockage compris). Une offre à 0,70 passerait la recherche et serait détruite à l'étape 8. Pour les quatre offres du jour
   sans effet ; à régler par `--storage 150` à la recherche ou une borne à 0,65.
6. **Origine du plafond de 8,5 USD** : jamais dérivé (devis § 3 le pose). 90 % de la ligne (10,8) moins 2,1 déjà faits laisse 8,7 ; 8,5 est
   proche mais le choix n'est pas dit. Une phrase.
7. **« ≈ 2,1 USD déjà dépensés »** : le journal de la troisième course donne ≈ 2,0 sur la ligne ; 2,1 est « large » (dit) : garder, mais
   renvoyer au registre des dépenses plutôt qu'au journal.
8. **Addendum § 2, point 1** : « mémoire : 39 936 Mio » vaut pour l'offre la moins chère ; deux des quatre offres du relevé ont 40 960 Mio.
   `CARTE_ATTENDUE` couvre les deux ; ne mettre que « ≈ 39 à 40 GiB » à la marge.
9. **Addendum § 1** : « le lot 64 ne tient pas dans une RTX 4090 » est plus fort que la note (« non établi, très probablement impossible »,
   échec observé avec l'allocateur par défaut). Reprendre la formule de la note.
10. **Addendum § 3 (c)** : le seuil 0,01 de « bruit numérique du bf16 » n'est pas sourcé (R7), et « toute comparaison (a) d'un ordre de grandeur
    égal ou inférieur est lue en conséquence » est une règle de lecture vague. Le seuil ne fonde aucun verdict (rapport seulement), donc mineur ; ou
    remplacer par « les écarts sont rapportés avec le |Δ| de (c) en regard, sans règle ».
11. **Addendum, périmètre « aucun critère changé »** : exact pour les seuils ; mais `essais_ok` lu des résultats rend la condition (d) effective
    (v3 : écrite en dur à vrai). Le dire dans l'addendum (constat porté, pas un changement de critère) pour qu'un lecteur qui compare avec
    R-2915 ne le découvre pas dans le code.
12. **GO** : `registres/go.md` de cette branche ne porte ni GO-2026-11-17-03 ni -04 ; la ligne GO-2026-11-14-06 dit « une RTX 4090 ». L'écart de
    carte repose sur le mot de Lazar transmis par la mère ; le feu doit citer cette décision et l'inscrire (nœud : écart à une ligne).
13. **Amorce v6, en-tête l. 24** : « 11 carte graphique absente » ne dit pas « carte inattendue ».
14. **Essai à blanc v10** : le faux lanceur joue « les audits exceptés » ; aucun cas de l'amorce ne passe par `audit-*` avec le vrai lanceur
    (déclaré « comme en v8 »). Accepté, à ne pas présenter comme couvert.
15. **Une carte neuve pour le matériel du lot** : toute la chaîne (passe d'activations, `measure`, `score`) n'a tourné que sur la RTX 4090 ;
    l'A100 (sm_80, `torch==2.14.1` épinglé) n'est pas essayée. Sans objet pour le risque de dépense (arrêt tôt), mais à écrire au « non couvert »
    de l'addendum § 6 : « la chaîne n'a jamais tourné sur cette architecture ».
16. **Poussée des fichiers lourds** : `-causal-lot16.pt` et `-causal-seed1-lot16.pt` restent sur l'instance (≥ 95 Mo, comme avant) : la
    seconde série ne peut donc plus être relue à partir du brut du lot 16 après destruction. Sans effet sur les comparaisons de l'addendum
    (grandeurs par pôle et résumés poussés) ; à écrire en une ligne.

## Réponses aux questions

- **(a) Exactitude** : oui, empreintes et chiffres justes (voir plus haut) ; une erreur de texte (v9 au lieu de v10) ; deux affirmations de
  l'addendum à adoucir (mineures 8, 9).
- **(b) Lanceur v4** : fait ce que dit l'addendum. Bascule avant la mesure du lot 64 (`PREREQUIS`, `exiger_prerequis`, garde sur l'audit du lot 16) ;
  aucune écrasure en marche normale (cible déjà présente → arrêt ; mesure du lot 64 refusée si un fichier est en place ; noms de `score`,
  grandeurs, résumés, audits tous distincts par étiquette `lot64` / `seed1-lot64`) ; audits par série corrects (essai jetable) ; verdicts aux deux lots ;
  `essais_ok` lu des résultats (structure de `b0`, `b3`, `fumee` vérifiée contre `etape_b0` et `_pytest`). Défauts : B1, M3, M4, M5. Pas de mélange de
  sorties entre séries trouvé ; l'audit « tout négatif » déclenché par la seconde série seule est bien joué (en dernier).
- **(c) Cohérence de la commande** : bonne, hors mineures 1 à 5, 12, 13 et M4 (ordre). Aucune trace fausse de la RTX 4090 hors des références
  historiques voulues ; trace fausse de la v5 : témoin 60480302 (mineure 2).
- **(d) Seuils, critères, R1** : aucun seuil ni critère de B-2, B-3, B-4, B-7 n'est changé ; la règle « verdict de B-7 au lot 64, B-2 et B-3 rapportés,
  R-2915 reste le verdict » est claire dans le cas nominal et fixée avant la course ; elle laisse ouvertes B1 (audit de B-7), M1 (pas de
  troisième série), M2 (chaîne en défaut au lot 64, remplacement de la lecture de B-7 de la troisième course).
- **(e) Non couvert, à couvrir avant le feu** : B1, B2, M1, M2 (en deux phrases d'addendum) ; M3 (essais) ; M4 (une ligne de devis et la phrase
  d'ordre) ; M5 (idempotence de deux étapes). Hors feu : `nvidia-smi` avant `pip`, mention de la carte jamais essayée, GO inscrit.

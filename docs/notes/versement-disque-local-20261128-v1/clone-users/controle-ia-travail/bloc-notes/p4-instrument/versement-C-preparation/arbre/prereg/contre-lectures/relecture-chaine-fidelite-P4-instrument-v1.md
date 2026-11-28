# Relecture de la chaîne de lancement de P4-instrument — lentille « fidélité au texte » — v1

Relecteur neuf (sous-agent lancé le 2026-10-20 vers 18:45 UTC). Je n'ai écrit ni le texte, ni le module, ni la chaîne.
Dépôt de travail lu seulement : aucune écriture, aucune commande git qui écrit (des clones partagés jetables, sous mon
dossier, lisent ses objets par référence), aucun `__pycache__`. Aucune commande Vast.ai réelle : un faux outil dans un
PATH de banc. Aucun réseau. Je n'ai lu ni `prereg/P3-consignes-v1.md` ni aucun fichier `textes-actions-*`.

## Verdict

**Conforme après corrections.** La chaîne suit le texte presque ligne à ligne : ordre des étapes, suite complète des
tests sur l'instance, bornes de temps (3 600 s, 90 minutes, 150 minutes, création + 9 600 s), GO, plafond par
lancement, accord du jour, garde gelée jamais contournée, destruction après la récupération vérifiée. Un point bloque
le lancement : cinq citations que la chaîne exige manquent au texte (RC-fidelite-01). Un point est à corriger avant
la lecture : le refus de lire avant le verdict complété de P3 n'existe qu'en mode décisif (RC-fidelite-02). Six
écarts mineurs ont une correction simple.

## Ce qui fait foi, ce que j'ai lu

- Texte : brouillon 4, `…/p4-instrument/P4-instrument-v1-brouillon4.md`,
  `32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6` (vérifié). Sections relues ligne à ligne :
  en-tête « GO et dépense » (l. 47-66), Plan d'analyse points 1 (l. 403-424), 2 (l. 425-436) et 7 (l. 463-477),
  Liste d'arrêt (l. 605-628), Chaîne de lancement (l. 632-645).
- Plan v2, `…/p4-instrument/plan-code-et-chaine-v2.md`,
  `7c65e4f64e8c65d9f63af1fe6dd755959bba10e7424e2e8ab2826cc1b1d06e13` (vérifié), et la section 4 du plan v1, à
  laquelle il renvoie. Le texte prime.
- Chaîne : les 17 scripts, les 5 journaux de banc, le journal de la répétition jouet et `NOTES-CHAINE.md` de
  `…/p4-instrument/chaine/`, aux empreintes du rendu du rédacteur (toutes vérifiées ; chaque sceau `.sha256` passe
  `sha256sum -c`). Rejoué : `verifications_p4_v1.py preuves` sur les cinq journaux de banc, code 0, et chacun des 12
  scripts éprouvés égal au script du bloc-notes (`preuves-relues.txt`).
- Module (R11, vérifié sur disque) : `instrument_p4_v1.py` `6e0e026e…`, `lecture_p4_v1.py` `51a25e30…`,
  `mesures_conception_p4_v1.py` `483b8ac3…`. Les empreintes du texte de ma tâche (`90b9ae8b…`, `5212cf4d…`, 182 tests)
  sont périmées : je confirme le constat C4 du rédacteur.
- Chaîne de P3 comparée par différence : `lancer_p3_v1.sh`, `scripts/amorce_instance_p3.sh`, `scripts/p3_instance.sh`,
  `surveiller_p3_v1.sh` ; garde gelée `.claude/hooks/garde_calcul.py` (`579f65c8…`) ; candidat 1 (`6422fb45…`), pour
  les seules lignes que lit la chaîne.

## Correspondance : chaque ligne du texte et son contrôle

« lanceur » = `lancer_p4_v1.sh` ; « instance » = `p4_instance_v1.sh` ; « amorce » = `amorce_instance_p4_v1.sh` ;
« contrôles » = `controles_avant_depense_p4_v1.sh` ; « vérif. » = `verifications_p4_v1.py` ; « module » =
`instrument_p4_v1.py` ; « lecture » = `lecture_p4_v1.py`.

### En-tête « GO et dépense » (l. 47-66)

| ligne du texte | contrôle dans la chaîne | état |
|---|---|---|
| l. 49-51 GO cité `GO_ID=GO-2026-10-20-07`, seul ; « calcul », Lazar, échéance de sa colonne | vérif. l. 53, l. 98-115 ; module l. 500-519 ; lanceur l. 148-154, l. 159, l. 325 ; contrôles l. 128-131 ; scellement l. 149-152 | conforme (bancs G01, G02, G07, G08) |
| l. 51-52 garde gelée rejouée par le lanceur avant la création, jamais contournée | lanceur l. 312-315 (piège ERR) ; vérif. l. 113 ; contrôles l. 319-320 | conforme, mais la garde ne voit qu'une forme de révocation : RC-fidelite-03 |
| l. 53-54 colonne « plafond » qui commence par « 10 USD par lancement » ; borne < 10 USD | module l. 514, l. 520 ; lanceur l. 75-80 (borne recalculée) | conforme (G03, Z03, Z04) |
| l. 55-57 plafond de la phase, vérifié à l'accord et écrit dans la ligne d'accord | aucun | RC-fidelite-05 |
| l. 58-61 révocation, deux formes, cinq identifiants | module l. 523-538, lu par le lanceur l. 149 et l. 159 | conforme jusqu'à l. 159 ; non vue ensuite : RC-fidelite-03 |
| l. 62-66 accord du jour, forme exacte, GO ou message du jour ; identifiant exigé, relu ; autre jour et GO échu refusés | vérif. l. 118-123 ; module l. 542-564 ; lanceur l. 36, l. 121-129, l. 162 | conforme (A10 à A15) ; ordre « après S » non contrôlé : RC-fidelite-08 |

### Plan d'analyse, point 1 (l. 403-424) et point 2 (l. 425-436)

| ligne du texte | contrôle dans la chaîne | état |
|---|---|---|
| l. 403 un seul run, sur une instance louée, sans retour en arrière | instance l. 61-64, l. 238 (un seul lancement du module) ; amorce l. 28-30 ; surveillance l. 82-84 (redémarrage) ; récupération l. 83-89 (un seul run) ; lanceur sans relancement | conforme |
| l. 405-407 manifeste, texte scellé, configuration, arbre gelé = `7a54d43`, module cité, données de P3, 64 Go | module (au run) ; contrôles l. 93-126, l. 197-262 ; instance l. 84-103 (lecture précoce et sceaux) | conforme (constantes du texte : module l. 162-174 ; contrôles l. 252) |
| l. 43-45 et l. 403 suite complète sur l'instance avant le run | instance l. 211-225 (`tests` et les trois fichiers de tests, nombre exact, aucun saut) ; contrôles l. 311-317 ; récupération l. 333 | conforme (répétition jouet : 1 102 passés en 36 min) |
| l. 418-421 tout arrêt écrit d'abord un résumé avec son motif, poussé avec les partiels | instance l. 151-162, l. 166-186, l. 245-258 ; amorce l. 44-57 ; récupération l. 196-198 (4a) | conforme ; épreuve de bout en bout incomplète : RC-fidelite-07 |
| l. 419 aucun texte écrit ; aucune activation gardée | instance l. 141-149 ; récupération l. 79-82 (1c), l. 266-321 (4f) | conforme |
| l. 425-432 lecture après la récupération et après le verdict complété de P3 | lecture l. 742-750 (mode décisif seulement) ; aucun script de lecture dans la chaîne | RC-fidelite-02 |

### Plan d'analyse, point 7 (l. 463-477)

| ligne du texte | contrôle dans la chaîne | état |
|---|---|---|
| l. 463-465 filtre d'offre de P3 ; la moins chère | lanceur l. 37-43, l. 62, l. 203-212 | conforme (P07 à P07i, O01, O02) |
| l. 466 `duree_max_s` 3 600 s | module l. 155, l. 164, l. 1181 ; contrôles l. 252 | conforme |
| l. 466-467 délai externe 90 minutes (TERM, KILL 5 minutes plus tard) | instance l. 232, l. 238 ; contrôles l. 237 | conforme ; non éprouvé de bout en bout : RC-fidelite-07 |
| l. 467 plafond de l'amorce 150 minutes (mise en place, tests, run, poussées) | amorce l. 40-41 ; contrôles l. 238 | conforme (passage 4 de la répétition) ; le clonage de l'amorce est hors du plafond : RC-fidelite-10 |
| l. 467-468 surveillance création + 9 600 s, puis arrêt par l'identifiant | surveillance l. 28, l. 38, l. 90 ; lanceur l. 39, l. 322-324 ; contrôles l. 245 | détection conforme ; l'arrêt est un geste sans script : RC-fidelite-06 |
| l. 469 crédit 3 h × (prix + autres projets en marche) + 1,2 USD | lanceur l. 38, l. 294-311 | conforme (P08, P08b, V03) |
| l. 470-473 dépense de l'étape bornée, 5,41 USD | lanceur l. 44-47, l. 75-80 ; module l. 491-497 | conforme comme calcul ; aucun contrôle du dépassement : RC-fidelite-04 |
| l. 473-476 sous le plafond par lancement (10 USD) et sous le plafond de la phase | module l. 514, l. 520 ; rien pour la phase | RC-fidelite-05 |
| l. 477 un seul lancement à la fois ; 56799469 non réutilisée | lanceur l. 61, l. 248-290 | conforme (P11 à P11e, V01 à V08) |

### Liste d'arrêt (l. 605-628)

| ligne du texte | contrôle | état |
|---|---|---|
| l. 605-607 empreintes (R11) ; arbre gelé | module ; contrôles l. 93-134, l. 197-231 ; scellement l. 116-122 | conforme |
| l. 609 garde de M5 : arrêt avant les bras, résumé (L2) | module ; instance l. 245-258 ; récupération l. 196-198 | conforme |
| l. 618-620 mémoire vive, 3 600 s, 90 minutes, 150 minutes : arrêt consigné, partiels poussés | module ; instance l. 151-186, l. 245-258 ; amorce l. 44-57 | conforme ; RC-fidelite-07 |
| l. 619-620 surveillance à la création + 9 600 s : arrêt par l'identifiant | surveillance l. 90 | RC-fidelite-06 |
| l. 621-626 aucune création : contrôles, offre, crédit, instance, GO, échéance, plafond, borne, garde, révocation, accord | lanceur l. 132-135, l. 203-244, l. 248-311, l. 149-162, l. 314-315 | conforme sauf la révocation consignée pendant l'appel : RC-fidelite-03 |
| l. 627 contrôle à cinq minutes en échec : arrêt par l'identifiant | cinq minutes l. 17, l. 131-133 | détection conforme ; arrêt sans script : RC-fidelite-06 |
| l. 627 dépense au-delà de la borne : arrêt par l'identifiant | aucun | RC-fidelite-04 |
| l. 628 lecture demandée avant le verdict complété : refusée et reportée | lecture l. 742-750 | RC-fidelite-02 |

### Chaîne de lancement (l. 632-645) : ordre des étapes

| étape du texte | ce qui l'impose dans la chaîne | état |
|---|---|---|
| contre-lecture 3 avant la répétition jouet | la répétition doit porter le candidat relu épinglé (vérif. l. 176 ; contrôles l. 149 ; scellement l. 129) | conforme |
| répétition jouet ; bancs ; répétition finale ; scellement S | journaux de preuve exigés à S (lanceur l. 103-118 ; scellement l. 134-146) ; journaux des bancs exigés par la répétition finale (l. 47-50) ; empreintes des scripts éprouvés égales aux copies versées | conforme |
| scellement S (texte, configuration, sceaux) | scellement l. 157-199 ; contrôles l. 86-92 | conforme |
| accord du jour consigné, puis lanceur | lanceur l. 121-129, l. 162 | l'accord peut précéder S : RC-fidelite-08 |
| lanceur (contrôles avant dépense rejoués sur S) | lanceur l. 132-135 | conforme |
| contrôle à cinq minutes ; surveillance | lanceur l. 322-324 (instants écrits) ; scripts dédiés | conforme ; arrêts : RC-fidelite-06 |
| récupération, puis destruction par l'identifiant après la récupération vérifiée | récupération l. 399-438 (aucun KO, étiquette relue, `vastai destroy instance ID -y`, liste relue) | conforme |
| attente du verdict complété ; lecture | lecture l. 742-750 seulement | RC-fidelite-02 |

## Constats

### RC-fidelite-01 — majeur (bloque le lancement) — cinq citations exigées par la chaîne manquent au texte

- **Texte** : brouillon 4 l. 21 (« Commit du code d'analyse : au candidat ») ; l. 43 (« Tests attendus : au
  candidat ») ; aucune ligne pour les empreintes de l'amorce et du script de l'instance, ni de ligne « Lancement », ni
  de forme de citation des rapports versés (l. 652-653, l. 667-668 : « à verser sous `prereg/contre-lectures/` »).
  Candidat 1 (`6422fb45…`) : l. 25 « celui du scellement S » ; l. 51 « Tests attendus : 1 102, soit … ».
- **Scripts** : (a) commit de 40 signes cité une fois : contrôles l. 94-97, scellement l. 95-97, récupération l. 121 et
  l. 200, module `exiger_code_cite` ; (b) « Tests attendus : `N` » : instance l. 85-87, contrôles l. 311 et l. 322,
  cinq minutes l. 51-53, récupération l. 329 ; (c) « `chemin` (`empreinte`, sha256) » de l'amorce et de l'instance :
  lanceur l. 137-143, contrôles l. 109-112 ; (d) « `PREREG=prereg/P4-instrument-v1.md`, `BRANCHE=calcul/p4-reel-v1` » :
  lanceur l. 145, contrôles l. 188 et l. 329-333, scellement l. 99-103 ; (e) « `prereg/contre-lectures/X` (`sha`) » :
  contrôles l. 176-181, scellement l. 111-115.
- **Cas** : candidat 1 tel quel : scellement refusé (l. 97), instance arrêtée avant l'installation (l. 87), contrôles
  en KO ; bancs du lanceur N01, N01b, N02 (refus sans ces lignes).
- **Lecture** : ces exigences dépassent le texte (« rien de plus »), mais elles sont nécessaires : l'amorce et le
  script de l'instance sont hors de l'arbre gelé et hors des lignes « Module de P4 » ; sans leur empreinte citée, rien
  ne les gèle au scellement. Je confirme T1, T2 et T3 du rédacteur.
- **Correction** : candidat 2 qui porte les cinq formes, telles que les écrit `outils_essais_p4_v1.py candidat`
  (l. 83-97) : commit `7a54d431d89745839220f882b41b13e8c62ecfdd` (arbre gelé égal à celui de S et de P3) ;
  « Tests attendus : `1102` (…) » ; la ligne des scripts de l'instance ; la ligne « Lancement » ; chaque rapport versé
  sous sa forme citée. Puis contre-lecture 3 de ce candidat.

### RC-fidelite-02 — majeur (à corriger avant la lecture, pas avant le lancement) — la lecture d'un run réel sans `--prereg` ignore le verdict complété

- **Texte** : Liste d'arrêt l. 628 « Lecture demandée avant le scellement du verdict complété de P3 (addendum 2) :
  refusée et reportée » ; Chaîne l. 644 « le run peut le précéder, la lecture non » ; Plan 2 l. 425-432.
- **Scripts** : la seule garde est dans `lecture_p4_v1.analyser`, l. 742-750, sous `if prereg is not None`. Sans
  `--prereg`, la lecture charge la source (l. 752, `charger_source_p4` l. 216-248, qui ne regarde ni le mode ni le
  caractère décisif du run) et calcule tout. La chaîne n'a aucun script de lecture qui impose `--prereg`.
- **Cas** : `essai-lecture-avant-verdict-v1.log` (dépôt jetable, module réel, aucun verdict complété de P3). (a) Mode
  décisif : code 1, « verdict complété de P3 absent … lecture refusée et reportée », rien d'écrit. (b) Même demande
  sans `--prereg` : code 0, `diag/…/lecture-p4.json` écrit, manifeste « décisif : False », `verdict_p3` vide. Le
  journal de la répétition jouet (l. 77) montre la même voie : « lecture jouet … code 0 ; issue L3 », sans verdict
  complété dans le dépôt.
- **Lecture** : le texte rattache la garde au mode décisif (l. 427-432) ; la Liste d'arrêt la généralise à toute
  lecture demandée. Le mode non décisif sert au jouet ; rien ne l'empêche sur le run réel.
- **Correction** : dans la lecture, refuser le mode non décisif quand le manifeste du run source est en mode « reel »
  ou décisif (report, rien d'écrit), avec un cas sain (run jouet lisible) et un artefact (run réel sans `--prereg`) ;
  et/ou ajouter à la chaîne un script de lecture qui passe toujours `--prereg prereg/P4-instrument-v1.md --entropie
  <citée>`, avec son banc. Sinon, écrire au texte que le mode non décisif est réservé aux runs jouets.

### RC-fidelite-03 — mineur — une révocation consignée pendant l'appel n'arrête la création que sous une forme

- **Texte** : en-tête l. 58-61 (deux formes, cinq identifiants : « L'une ou l'autre : aucune création ») ; Liste
  d'arrêt l. 624.
- **Scripts** : la dernière lecture complète des révocations est l. 159 (`--controle go`, module l. 523-538). La
  seconde relecture de l'accord (l. 162) ne lit pas les révocations (module l. 542-564). La garde gelée (l. 312-315)
  ne voit qu'une ligne du registre des GO qui nomme le GO cité (`garde_calcul.py` l. 97-100). Entre l. 159 et l. 325
  (offres, instances, crédit), une révocation de GO-2026-10-04-08, GO-2026-10-20-06, R-262 ou R-269, ou une ligne
  « **Révocation de R-26x** », n'est plus vue. Le banc G06 n'éprouve que la forme vue par la garde.
- **Cas** : `banc-fidelite-revocation-v1.log` (lanceur réel, faux outil qui consigne la ligne au moment de
  « show user ») : F02 (quatre identifiants au registre des GO) et F03 (R-262, R-269 au registre des décisions) :
  code 0, une création factice chacun ; témoins : F01 (GO cité) refusé par la garde, l. 315 ; F04 et F05 (mêmes lignes
  consignées avant l'appel) refusés à l. 149. Six écarts au texte.
- **Correction** : rejouer `verifications_p4_v1.py go` (ou `--controle go`) juste avant la garde gelée, après le
  crédit (après l. 311), et ajouter au banc du lanceur les cas F02 et F03.

### RC-fidelite-04 — mineur — « dépense au-delà de la borne de l'étape » n'a aucun contrôle

- **Texte** : Liste d'arrêt l. 627 ; Plan 7 l. 470-473 (dont « disque … 24 heures au plus »).
- **Scripts** : aucun compteur. La borne tient par construction pour la carte (prix relu à cinq minutes, l. 97-99 ;
  surveillance l. 90). Deux postes ne sont observés nulle part : le volume téléchargé (« ≈ 20 Go » supposés) et le
  délai jusqu'à la destruction (la récupération, l. 399-438, ne regarde pas l'heure ; en échec, l'instance reste sans
  limite, T8). Le contrôle à cinq minutes affiche `inet_down_cost` sans le comparer à 0,05 et ne lit pas
  `storage_total_cost` (l. 91-103).
- **Cas** : lecture des scripts ; aucun banc ne peut faire partir cet arrêt.
- **Correction** : soit le candidat écrit que la borne tient par construction et nomme ses observables (prix relu à
  cinq minutes, surveillance, destruction au plus 24 heures après l'arrêt) ; soit la chaîne ajoute : à cinq minutes,
  téléchargement ≤ 0,05 USD par Go et stockage ≤ 0,03 USD de l'heure relus ; à la récupération, l'heure de la création
  (lancement.txt) et un KO, nœud de Lazar, au-delà de la création + 9 600 s + 24 heures ; un rappel programmé de la
  destruction.

### RC-fidelite-05 — mineur — plafond de la phase : aucun contrôle, aucune forme

- **Texte** : en-tête l. 55-57 (« la session vérifie … et l'écrit dans la ligne d'accord ») ; Plan 7 l. 475-476.
- **Scripts** : `controler_accord` (module l. 542-564) ne lit aucune somme ; rien ne relit GO-2026-10-04-08 ni
  GO-2026-10-20-06 (existence, échéance), seulement leur révocation.
- **Cas** : banc du lanceur A15 : un accord sans aucune mention des 150 USD passe.
- **Correction** : donner une forme au candidat (par exemple « dépense consignée X USD + borne 5,41 USD < 150 USD ») et
  la lire dans `verifications_p4_v1.py accord` ; ou écrire au texte que c'est un geste de la session, sans garde.
  Je confirme T6 du rédacteur.

### RC-fidelite-06 — mineur — trois arrêts « par son identifiant » sans script

- **Texte** : Plan 7 l. 467-468 et Liste d'arrêt l. 619-620 (surveillance) ; l. 627 (cinq minutes en échec ; dépense).
- **Scripts** : surveillance l. 15 « Ce script n'arrête rien » ; cinq minutes l. 17 et l. 132 (consigne écrite). La
  destruction a son script gardé (étiquette relue, liste relue) ; l'arrêt, non : ni étiquette relue, ni état relu, ni
  heure (la borne compte 10 minutes d'arrêt, 0,22 USD), ni ligne prête pour `registres/arrets.md`. Repris de P3.
- **Cas** : lecture des scripts.
- **Correction** : un `arreter_p4_v1.sh ID DOSSIER_NEUF` (étiquette « p4-v1 » relue, `vastai stop instance ID`,
  état relu arrêté, heure écrite), avec son banc (cas sain, étiquette autre, arrêt en échec) ; ou une phrase du texte
  qui fait de l'arrêt un geste de la session.

### RC-fidelite-07 — mineur — R5 : l'arrêt pendant le run n'est pas éprouvé de bout en bout

- **Texte** : Liste d'arrêt l. 618-620 ; Plan 1 l. 420-421.
- **Scripts** : instance l. 232-258 (délai de 90 minutes, `complet()`, `consigner_arret`). Les quatre passages de la
  répétition sont : sain, branche présente, manque, plafond de l'amorce pendant les tests. Aucun ne fait s'arrêter le
  module pendant le run. La récupération d'un arrêt n'est éprouvée que sur une branche synthétique (e-v1).
- **Cas** : `repetition-jouet-p4-v1.log`, passages 1 à 4.
- **Correction** : un cinquième passage : configuration jouet à `duree_max_s` minuscule (arrêt du module avec
  `arret.motif`), puis une copie de l'instance au délai de 90 minutes réduit (ligne comptée) ; attendus : résumé avec
  motif, partiels poussés, récupération en code 0 sur la partie « partiel ».

### RC-fidelite-08 — mineur — l'accord peut précéder le scellement

- **Texte** : Chaîne l. 641-642 « scellement S ; accord du jour consigné ; lanceur ».
- **Scripts** : lanceur l. 121-129 et l. 162 lisent l'accord dans le registre courant, sans le comparer à S.
- **Cas** : `banc-fidelite-revocation-v1.log`, F00-sain : l'accord R-999 est committé avant S (il est dans l'arbre de
  S) et la création a lieu (code 0). Même montage dans le banc du rédacteur (`essais_lanceur_p4_v1.sh` l. 113-114,
  accord committé dans la base, puis S ; cas P00).
- **Correction** : le lanceur refuse si `git show "$S:registres/decisions.md"` contient déjà `| $ACCORD |` ; un cas de
  banc.

### RC-fidelite-09 — information — des quantités du run se voient avant le verdict complété

- Lignes de progression relayées par l'instance (l. 242-243) et gardées par la surveillance (l. 69-71) : « M5
  conforme » (module l. 1241), épisodes au niveau 1 (l. 1270), exclusions sur total (l. 1293), qui fixent L2 et L4. La
  récupération affiche le motif d'un arrêt (l. 198). Ce n'est pas une lecture au sens du texte, qui se tait.
- Proposition : une phrase du candidat qui le dit, ou des lignes de progression sans compte.

### RC-fidelite-10 — information — le clonage de l'amorce est hors du plafond de 150 minutes

- Amorce l. 31-36 avant le `timeout` de l. 40 (repris de P3). Un clonage bloqué est vu par le contrôle à cinq minutes
  (l. 118-126 : lignes « début » et « branche poussée » exigées) et par la surveillance. Rien à corriger ; une phrase
  suffirait.

### RC-fidelite-11 — information — ajouts au texte, repris de P3, sans effet contraire

- Pas de création entre 23:30 et 00:00 (lanceur l. 83 et l. 317) ; 3 Go libres (l. 84-85 ; 15,5 Go libres à cette
  relecture) ; étiquette « rr- » des autres projets ; étiquette relue avant la destruction ; versions égales au run de
  P3 (récupération 3f) ; termes du filtre de recherche (l. 62 : carte vérifiée, centre de données, fiabilité, CUDA),
  qui sont le « filtre du pilote » de P3 l. 352. Bord : la seconde relecture de l'accord (l. 162) peut se faire à
  23:59 et la création à 00:00 (l. 317 n'exige que l'heure < 23:30) : fenêtre de quelques secondes.

### RC-fidelite-12 — information — rapports versés : au moins deux, le texte en demande quatre

- Hors de la lentille stricte (section « Contre-lecture », l. 652-653 et l. 667-668 : deux rapports et les brouillons 1
  et 3, à verser). Les contrôles (l. 74-76) et le scellement (l. 48-54) acceptent deux paires épinglées. Si les
  brouillons sont versés sous un nom qui contient « P4 », ils entrent dans la famille (T4). Proposition : quatre
  paires au moins, ou les noms attendus écrits.

## Points du rédacteur (T1 à T20)

- Confirmés : T1, T2, T3 (RC-fidelite-01) ; T6 (RC-fidelite-05) ; T7 (RC-fidelite-04) ; T8 (récupération en échec :
  pas de destruction, nœud ; RC-fidelite-04) ; T9, T10, T13, T14, T16, T17, T18 (lectures fidèles ou ajouts sans effet
  contraire) ; T11 (la lecture jouet est fidèle au plan ; elle montre aussi la voie de RC-fidelite-02).
- T12 : la suite sur l'instance (`tests` et trois fichiers) égale bien « suite du dépôt + tests du module »
  (`pyproject.toml` : `testpaths = ["tests"]`).
- T14 : ma relecture ajoute un écart du même endroit : la garde gelée ne voit que le GO cité (RC-fidelite-03).
- T20 et C11 : 15,5 Go libres à cette relecture ; le seuil de 3 Go ne bloque pas aujourd'hui.

## Artefacts (tous sous ce dossier, avec `empreintes-artefacts-v1.sha256`)

- `banc-fidelite-revocation-v1.sh` et son journal `banc-fidelite-revocation-v1.log` ; pièces par cas sous
  `banc-revocation/` (sorties, journaux du faux outil, différences des registres, texte d'essai).
- `essai-lecture-avant-verdict-v1.sh` et `essai-lecture-avant-verdict-v1.log` ; pièces sous `essai-lecture/` (sortie
  du cas (a), lecture écrite du cas (b), texte d'essai).
- `preuves-relues.txt` : sortie de `verifications_p4_v1.py preuves` sur les cinq journaux de banc.

## Limites

- Je n'ai pas rejoué les bancs du rédacteur ni la répétition jouet (36 minutes de suite) ; j'ai relu leurs journaux et
  vérifié que leurs empreintes égalent les scripts.
- Mes deux essais tournent sur la tête du dépôt de travail (`bbc4e498…`) avec le module du bloc-notes versé à la main,
  pas sur le vrai C ; ils éprouvent le lanceur et la lecture tels qu'ils sont, pas un lancement.
- La répétition finale n'existe pas encore ; son ordre dans la chaîne est relu sur le code seulement.

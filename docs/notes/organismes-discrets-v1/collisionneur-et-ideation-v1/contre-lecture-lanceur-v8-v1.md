# Contre-lecture (R2) du lanceur v8 des trois courses jumelles de l'organisme d'idéation (organismes discrets) — v1

- **Lecteur** : sous-agent neuf, n'a écrit aucune des pièces lues ni le lanceur ; modèle **Claude Opus 5.5** (`claude-opus-5-5`).
  Le commit qui a déposé le lanceur (`156f2978`) porte l'attribution « Claude Fable 5.1 » : lecteur d'un autre modèle que
  l'auteur du lanceur, au sens du préalable 6.1 du devis v3. La ligne d'attribution de la session, elle, nomme Opus 5.5 :
  si une partie des pièces a été écrite sous Opus 5.5, ce préalable n'est pas rempli pour elle (à trancher par la session).
- **Heures UTC** (`date -u`) : début 2026-11-18T04:06:36Z ; empreintes finales relevées à 04:20:33Z.
- **Mode** : lecture seule ; aucun réseau, aucun appel payant, aucun commit. Essais joués hors réseau dans le bloc-notes de
  la session, sous `env -i PATH=/usr/bin:/bin HOME=<tmp> LANG=C.UTF-8` et `-I -B -X pycache_prefix=<tmp>` ; aucun port
  8787, 8788 ou 8790 n'écoutait pendant les essais (lu dans `/proc/net/tcp*`). Clone de l'orchestrateur intact après les essais
  (`git status --porcelain --ignored` vide, arbre `ee84d6ec…`, commit `a41b7b50`).

## Verdict

**À corriger — 1 bloquant, 2 significatifs, 4 mineurs.** Le code du lanceur est conforme : c'est le lanceur modèle aux seuls
changements annoncés près. La commande qu'il construit passe l'analyseur et les gardes réelles de l'orchestrateur pour les
trois lignées. Le bloquant est un **préalable** : à l'heure de la lecture, aucune ligne de GO valide n'existe au registre
(constat B1). Le lanceur le voit et refuse de lui-même. Aucun appel ne doit partir avant la confirmation directe de Lazar et
le scellement de l'état relu.

**Pièce en mouvement pendant la lecture.** Lanceur lu en entier dans l'état `41d0ce7b…` (commit `156f2978`). Il est devenu
`27794cac…` (commit `eeb6c439`) pendant la lecture. Le différentiel ne touche que deux empreintes épinglées (commande Astra,
enveloppe Astra) et un commentaire de prix. Il est relu, et **ce verdict vaut pour `27794cac…`**. La commande Astra lue
d'abord, `5e287603…`, avait un en-tête non fermé : du code mort se trouvait dans la docstring, mais elle fonctionnait. Elle
est devenue `986cf71e…` (en-tête fermé, prix vérifiés), ré-essayée ci-dessous. L'enveloppe Astra est passée de `ce13e1e6…` à
`aa2df474…` (commentaire seul).

## Empreintes SHA-256 des pièces lues (recalculées par `sha256sum`, 04:20:33Z)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_ideation_organismes_discrets_v8.py` (état final ; **aucun compagnon**) | `27794cace03d8a7d767b8bf0b73a81eb5abf83485408366894f2e8759e86a93b` |
| idem, état lu en entier (`git show 156f2978:…`) | `41d0ce7b5851ee55daf45c5afe20da70c958ab1d562a2806fafa5720ece46f16` |
| `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` (modèle) | `3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f` |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-carbon-v1.sh` | `f0f15108fba8a0ae2ae2d07424ba7dc86b64d32f63f7084f2c9bc986fd4a8183` |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-argon-v6.sh` | `440127d646fb67d593a61bc29652d505a6ec0286de72256f9116986d8d449bbb` |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-astra-v1.sh` (final ; lu d'abord `ce13e1e6…`) | `aa2df474c5105ea5e4729fecf0d8c875e347ed262178177b45c956b1da9f3936` |
| `rapports/fille-ideation-1-v1/appel-argon-v5.sh` (modèle) | `37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a` |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py` | `e94ecd4693657bd2d8b086fbbc903bb77635b3b034e1eede50d630675c3f3fc6` |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` (modèle) | `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46` |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` (final ; lu d'abord `5e287603…`) | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_v1.py` (modèle) | `3a98845e1c3c11169c329ab7ae1c5e0978d1bf8323f562688fc003921c02d593` |
| `scripts/lancer_relais_local_v1.py` | `854fd369da6791c3e09dcdf31e76a4b56de2ca26bd29ca3edce74488ac285085` |
| `docs/notes/organismes-discrets-v1/collisionneur-et-ideation-v1/devis-ideation-organismes-discrets-trois-lignees-v3.md` | `2d2a8ad8813e8171dc05a4591a9d4c776cf28f3a313f482d9a49a510ccb02722` |
| `docs/notes/organismes-discrets-v1/collisionneur-et-ideation-v1/commandes-exactes-trois-lignees-v1.md` | `1a1b6b9bb922519cac4e71db8aaeba7a2037b2b251cfdf6b0156a0665beac9da` |
| `registres/go.md` (état de `main`) | `dd4526c43c7ba9e76abfb55e4478b7a2b6f857272ba140b1bf9602f230a6c8c8` |
| `registres/go.md` de la branche au commit `156f2978` (ligne de la course) | `d56a53f173d98fe9e1d6d8618a819c7ce7237c09237a108fc277df4295d33ad8` |
| `registres/decisions.md` (état de `main`) | `4c0bba7ea737d1c09f868eb7beef2ffa5c88bf425e6b633c5322ce9e9e6c8980` |
| `tests/test_lancer_course_ideation_organismes_discrets_v8.py` (non commité, en cours) | `a82fbf36b02db46886be026a39babb3fc134e43ccf7d6c81f83d80afb7c52983` |
| `…/argon-recherche-v1/relais_gemini_v2.py` | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| `…/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| orchestrateur : `demonstrations/ideation_v8.py`, `_v7`, `_v6`, `_v5`, `_v4`, `_v2`, `pole/ideation_v2.py`, `pole/adaptateurs.py`, `pole/relais.py` | égales aux neuf empreintes épinglées du lanceur (vérifiées une à une) |
| orchestrateur : `pole/relais_reel.py` | `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` (égale au devis) |

## Réponses aux questions

### 1. Le lanceur v8 est-il le modèle, aux seuls changements annoncés près ? — **Oui.**
J'ai lu le `diff -u` en entier (633 lignes) et le lanceur v8 en entier. Les changements trouvés sont ceux de la liste :
- l'argument est la lignée (`LIGNEES`, `principal` et `Reglages.production(lignee)`) ;
- les pièces de cette course (`PIECES_COMMUNES`, `LIGNEES_EXTERNES`, `pieces_de`) ;
- Opus 5.5 seul en rôle interne (`PROPOSEURS`, `JUGES`) ;
- une passe : `--seconde-passe` est retiré et la somme refuse `--seconde-passe` et `--budget-passe-2-externe-usd`
  (`sommes_plafonds`, l. 617-618) ;
- les plafonds du devis v3 (6 ; 6,5 ; 2,0 ; 2,0 ; 1,5 ; 2,5 ; 1,7 ; course 9,2 ; borne 34) ;
- le périmètre du GO (trois phrases) ;
- les gardes de taille par famille (`plancher_gemini`, `plancher_astra`, `plancher_externe`) ;
- les copies ajoutées (`manifeste-depart.json`, `lecture.json`, `classement.json`) ;
- le filtrage par lignée dans `runs_du_lanceur` et `relance_permise`.

Restent gardés à l'identique : les neuf empreintes et l'arbre de l'orchestrateur, les drapeaux interdits, les noms permis,
M1, M2, le verrou, le superviseur, le relevé et les copies.

Trois changements induits, conformes :
- la garde « course » prend le plafond de la passe 1 au lieu de celui de la passe 2 (l. 698). C'est ce que fait
  l'orchestrateur avec une seule passe (`garde_de_la_course` → `plafond_passe_externe(…, 1)`). Vérifié : 240 000 caractères
  des deux côtés ;
- les clés de plafond sont passées dans l'ordre trié (`for cle in sorted(b)`, l. 1059) ;
- `principal` refuse des réglages dont la lignée diffère de l'argument (l. 1302-1304).

Aucun écart non annoncé.

### 2. La commande construite est-elle acceptée par l'orchestrateur réel ? — **Oui pour les trois lignées**, avec un risque nommé sur le modèle servi de Carbon (constat S1).
Essai en mémoire, sans réseau (`gardes_orch.py` ci-dessous). La commande exacte de `commande_course` est passée à
`principal` du module v2 chargé par la chaîne v8 → v7 → v5 → v4 → v2, dont `_principal` est remplacé par les gardes réelles.
Résultats :
- toutes les vérifications de l'analyseur (`a.error`) passent ;
- `verifier_commande_externe_reelle` passe avec `--modele-commande-externe <modèle>` et `--commande-externe-lit-modele`. Le
  juge différé `<lignée>-juge`, au même modèle, passe aussi ;
- contre-épreuve sans `--commande-externe-lit-modele` : Carbon et Astra sont **refusés** ; Argon est admis (son modèle est le
  défaut de la commande v2) ;
- `adaptateur_commande_externe` : `exiger_modele_servi = True` au moteur réel ;
- `modeles_du_relais` = `['claude-opus-5-5']`. `verifier_relais` accepte un relais qui permet exactement `claude-opus-5-5`.
  Il refuse `['claude-opus-5-5','claude-fable-5-1']` et `['claude-fable-5-1']` ;
- garde de plafond du relais Claude : avec un plafond de 20 et une réserve de 0,5, elle admet jusqu'à 15,5 USD déjà dépensés.
  Au-delà, l'orchestrateur refuse de lui-même ;
- `verifier_reglages_lanceur` (sommes, tailles, témoins) passe ; `valider_etiquettes` passe pour `carbon`, `astra`, `argon`,
  `opus`, `opus-juge` et `<lignée>-juge` ;
- `pole/ideation_v2.executer_ideation` exige au moteur réel :
  - un proposeur externe et un juge externe : les deux sont donnés ;
  - un adaptateur `commande-externe` : c'est le cas ;
  - un plafond par rôle et modèle : les quatre clés sont données ;
  - des sommes Claude 4,2 ≤ 6 et externe 5,9 ≤ 6,5 ;
  - des témoins présents ;
  - aucun outil pour le proposeur et le juge (`OUTILS_PAR_ROLE`) ;
  - des modèles Claude dans `MODELES_REELS_PERMIS`.

  Tout est satisfait.
- **Modèle servi.** Barrière du noyau (`modele_conforme`, `pole/adaptateurs.py` l. 365-376) : identifiant exact, ou suffixe
  de date strict `-AAAAMMJJ`, ou liste explicite (vide ici). Essai : `gemini-4-carbon-001`, `models/gemini-4-carbon` et
  `gemini-4-carbon-preview` sont **refusés** ; `gemini-4-carbon-20261118` est admis.
  - Commande v3e : elle rend `modelVersion` brut (l. 909, 1040). Sa propre barrière (l. 670-672) est plus large (tout
    suffixe `-…` et le préfixe `models/`).
  - Commande Astra et relais v4 : égalité exacte avec `model`.
  - Ce qui a été observé dans le dépôt : Argon a toujours rendu exactement `gemini-4-argon` ; Astra a toujours rendu
    `gpt-6-astra` (consultations du collisionneur).
  - **Carbon n'a jamais été observé** : voir S1.

### 3. Les gardes de somme et de taille du lanceur reproduisent-elles celles de l'orchestrateur ? — **Oui.**
Recalcul à la main, puis mesure réelle de l'orchestrateur (`--mesurer-consignes`), sur une liste blanche construite par
l'orchestrateur lui-même (`--construire-liste-blanche`, contenu égal aux trois empreintes épinglées).

| | carbon | astra | argon |
|---|---|---|---|
| consigne de contrôle externe / passe 1 (caractères) | 11 560 / 11 085 | idem | idem |
| garde de la course, orchestrateur / lanceur | 240 000 / 240 000 | idem | idem |
| garde de la passe 1, orchestrateur / lanceur | 360 000 / 360 000 | idem | idem |
| garde du juge différé (orchestrateur) | 840 000 ≥ 555 828 | idem | idem |
| plancher de la commande au contrôle (plafond 1,7) | 0,5435 | 0,3480 | 0,5435 |
| plancher de la commande à la passe 1 (plafond 1,5) | 0,5422 | 0,3425 | 0,5422 |
| somme Claude / total ; somme externe / total ; exposition | 4,2/6 ; 5,9/6,5 ; 9,2 | idem | idem |

- Somme externe : 1,7 + 1,5 + 2,5 + 0,2 = 5,9. C'est la somme de l'orchestrateur, contrôle du bras compris.
- Plancher Gemini du lanceur : il reproduit la garde de la v3e (entrée × 1,05, sortie minimale 4 096 et pensée 8 192 au prix
  de sortie), à 3 caractères par jeton, ce qui est prudent. La recherche web est désactivée par défaut : coût nul.
- Plancher Astra : il prend 1,15 octet par caractère. Mesuré sur le corps JSON réel (question et faits) : 1,053.
- `garde_drapeaux` et `garde_sommes` passent sur les trois commandes.

### 4. Les enveloppes — **conformes.**
- **Modèle figé après `"$@"`** dans les trois enveloppes. Essai : `--modele gemini-4-argon` passé à l'enveloppe Carbon est
  écrasé (la commande demande toujours `gemini-4-carbon`). Même chose pour `--modele gpt-6-mini` et `--prix-entree 0` passés
  à l'enveloppe Astra.
- **v3e** : elle lit `MODELE_DEMANDE_POLE` (l. 821-823), après le rôle et avant la clé, `countTokens` et tout envoi.
  - Essai, écart Carbon/Argon dans les deux sens : code 2, `envoye: false`, plancher 1e-6.
  - Accord : la commande va jusqu'à la connexion, refusée ici (rien n'écoute), au plancher.
  - Variable absente : la commande se comporte comme la v3d.
- **Astra** : le corps porte `max_completion_tokens` et jamais `max_tokens` (essai : `max_completion_tokens` = 29 769,
  `max_tokens` absent). Un écart de modèle demandé donne le code 2 avant toute lecture de l'entrée.
- **Prix**, cohérents d'une pièce à l'autre :
  - Gemini : 8,3 / 41,5 dans les enveloppes, dans `GEMINI_*` du lanceur et dans le devis. C'est une borne haute (la page
    publique affiche 2 / 10).
  - Astra : 10 / 50 dans l'enveloppe, dans `ASTRA_*` et dans le devis. C'est le prix standard lu (R-2677) ; la borne haute ne
    vient que de l'entrée en cache, comptée au prix plein. La formulation du devis diffère (constat m1).

### 5. Sûreté — **conforme.**
- Aucune valeur de clé n'est lue ni écrite. Le lanceur ne transmet que `PATH`, `LANG`, `LC_ALL`, `TZ` et `TMPDIR`, plus
  `GO_ID`, `HOME` et `PYTHONPYCACHEPREFIX`, qu'il fixe lui-même. Des noms exclus, seuls le nombre et l'empreinte de leur liste
  sont écrits. L'adaptateur externe refuse de toute façon un nom de clé dans son environnement.
- Le bac à sable est exigé deux fois : sonde du lanceur (`actif` et `proc_neuf`) et vérification de l'orchestrateur. Les
  drapeaux interdits sont refusés, abréviations comprises.
- Aucune commande git après le détachement : `_depot_git` vient avant, et la clôture n'en fait aucune.
- Les copies sont scellées dans `runs/…/copies/` à la clôture.
- Une relance au plus par lignée : `MAX_COURSES = 2`, filtré par lignée.
- La garde de cumul somme **toutes** les courses du dossier de runs commun, toutes lignées confondues, contre
  min(34, plafond du GO). Calcul : 3 × (9,2 + 1,9) = 33,3 ≤ 34.
- Une seule course à la fois : verrou commun, et une course en marche de n'importe quelle lignée bloque.

### 6. Le lanceur de relais local — **oui et oui.**
- Un nom refusé bloque tout avant toute création. Essais : `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_BASE_URL`, `CCR_X` et le nom
  vide (virgule double) donnent le code 2, sans console créée.
- La session de processus est neuve : `os.getsid(0) == os.getpid()` → `True`.
- L'environnement est réduit aux noms listés (essai : `FAUX_A`, `LANG`, `PATH`).
- Une console déjà présente est refusée.

## Constats

**B1 — bloquant (préalable) — `registres/go.md` (état de `main`, l. 369) et `registres/decisions.md` R-3173.**
La ligne de GO de la course, écrite sur la branche sous le numéro GO-2026-11-18-05 (déjà pris sur `main` par l'autonomie de
la mère), a été retirée par la remise des registres à l'état de `main` (commit `afb0514e`). R-3173 de `main` dit : « la mère
n'inscrit pas ce GO … elle demande à Lazar de confirmer ce GO directement. Jusqu'à cette confirmation, la ligne de la branche
ne fait pas foi et aucun appel payant n'est fait ». Les R-3169 à R-3174 de la branche n'existent plus sous ces numéros.

Essai : `verifier_go` sur le registre actuel donne un refus (« 0 ligne(s) principale(s) »). Sur le registre de la branche au
commit `156f2978`, il accepte (34 USD). Le lanceur est donc sûr : il refuse de lui-même. Le GO GO-2026-11-18-05 de la mère
n'est pas pris par erreur : son périmètre ne contient pas les trois phrases, et son plafond « ≤ 100 euros par jour »
n'aurait pas la forme exigée.

*Correction* : confirmation directe de Lazar, puis ligne inscrite par la mère sous un numéro neuf, avec :
- les trois phrases du périmètre (« organisme d'idéation », « organismes discrets », « trois lignées ») ;
- le type `calcul`, accordé par `Lazar` ;
- un plafond de la forme « 34 USD » ;
- une période qui couvre la course.

Aucun changement de code.

**S1 — significatif — modèle servi de Carbon jamais observé.** Fichiers : `pole/adaptateurs.py` l. 365-376 ;
`commande_argon_v3e.py` l. 670-672 et 909. Si l'interface rend pour Carbon un `modelVersion` autre que l'identifiant exact,
ou suivi d'une date `-AAAAMMJJ` (par exemple `models/gemini-4-carbon` ou `gemini-4-carbon-001`), voici ce qui se passe :
1. la v3e l'admet et rend le code 0 ;
2. le noyau prononce un refus (R-764) dès l'appel de contrôle externe, joué avant toute dépense Claude ;
3. la course s'arrête : coût réel d'un appel de contrôle, au plus 1,7, de l'ordre de 0,1 attendu ;
4. la relance unique de la lignée serait consommée sans effet, car elle reproduirait le même refus.

C'est sûr (refus avant toute dépense de plus) mais possiblement payé pour rien. *Options* :
- (a) accepter le risque, borné, et le dire au registre ;
- (b) lire une fois le `modelVersion` de Carbon. C'est un appel payant, sous GO ;
- (c) ajouter `--modele-servi-externe-permis gemini-4-carbon=models/gemini-4-carbon`. C'est un changement de garde, donc
  une décision.

*Recommandation* : (a), et lancer Carbon en premier comme prévu (ordre du § 3 des commandes exactes) pour que l'issue se
lise avant les deux autres. Astra : le risque est faible (égalité exacte des trois côtés, déjà observée).

**S2 — significatif — l'état relu n'est pas scellé, et les essais sont en cours d'écriture.** Fichiers :
`scripts/lancer_course_ideation_organismes_discrets_v8.py` (aucun `.sha256`) et
`tests/test_lancer_course_ideation_organismes_discrets_v8.py` (non commité). M1 refuse tant que le compagnon manque : c'est
sûr.
- Essais joués à 04:16Z (fichier `f4f1f678…`) : 3 échecs, dont `test_cumul_constantes`, qui enchaîne
  `x == approx(33.9) <= 34` (`TypeError`), et deux empreintes épinglées périmées.
- À 04:19Z (`a82fbf36…`) : 223 réussis, 6 échecs attendus.

*Correction* : sceller exactement `27794cac…`. Tout octet de plus demande un différentiel relu. Commiter les essais à l'état
qui passe, avec leur empreinte.

**m1 — mineur — devis v3 § 3 et en-tête de prix.** Le devis dit Astra « 10 / 50, SUPPOSÉS ». L'enveloppe et le lanceur
disent désormais « lus (R-2677, `prix-astra-v2.md`, `bf211a07…`) ». Les nombres sont identiques. *Correction* : aligner le
devis (nouveau nom, R12) ou l'annoter.

**m2 — mineur — compagnons `.sha256` absents (R6)** pour :
- le lanceur v8 ;
- les trois enveloppes ;
- `commande_argon_v3e.py` et `commande_astra_v1.py` ;
- `lancer_relais_local_v1.py` ;
- le devis v3 et les commandes exactes.

Le lanceur épingle déjà les enveloppes, les commandes et les pièces par leur empreinte, donc sans risque d'exécution.
*Correction* : sceller avant le feu.

**m3 — mineur — devis § 2 et essai `test_cumul_constantes`.** Le « défaut au contrôle ≈ 2,1 » compte deux contrôles Claude
(hérité du lanceur à deux modèles Claude). Ici, un seul modèle Claude : 0,2 + 1,7 = 1,9. Le calcul est prudent et la garde
reste correcte (33,3 ≤ 34). *Correction* : le dire, sans rien changer.

**m4 — mineur — `scripts/lancer_relais_local_v1.py` l. 33-44.** Un nom listé mais absent de l'environnement (la clé, par
exemple) n'empêche pas le lancement. Il est seulement rapporté dans `noms_absents` : le relais partirait sans clé et ses
appels échoueraient en 401, sans dépense. Les variantes en minuscules ne sont pas refusées, sans effet pratique.
*Correction proposée* : refuser si un nom listé est absent, ou exiger sa présence dans la vérification § 2.4 des commandes
exactes (`noms_absents` vide).

## Commandes exécutées (résumé des sorties)

1. `diff -u scripts/lancer_course_ideation_regard_ou_raisons_v1.py scripts/lancer_course_ideation_organismes_discrets_v8.py`
   → 633 lignes, lues en entier. Puis `git diff 156f2978 HEAD -- scripts/… rapports/…/enveloppes-v1/ …` : seulement deux
   empreintes et des commentaires de prix.
2. Dans le clone : `git rev-parse HEAD:orchestrator` → `ee84d6ec…` ; `git status --porcelain --ignored` → vide, avant et
   après. Neuf `sha256sum` égaux aux épingles.
3. `env -i … /usr/local/bin/python3 -I -B -X pycache_prefix=<tmp> demonstrations/ideation_v8.py <tmp>/liste-blanche.json --construire-liste-blanche question-v3.md faits-v3.md temoins-organisme-discrets-v1.json`
   → code 0, 3 fichiers, empreintes égales aux épingles.
4. `mesure.py` (bloc-notes) : il importe le lanceur v8 sans l'exécuter. Pour chaque lignée, il joue la vraie
   `commande_mesure`, c'est-à-dire `--mesurer-consignes` de l'orchestrateur, sous `env -i`, puis `gardes_de_taille`,
   `commande_course`, `garde_drapeaux` et `garde_sommes`. Code 0 pour les trois ; chiffres dans le tableau de la question 3.
5. `gardes_orch.py` (bloc-notes) : gardes réelles de l'orchestrateur en mémoire, détail à la question 2. Code 0 pour les
   trois ; contre-épreuves refusées comme attendu.
6. Enveloppes, sous `env -i`, sans relais à l'écoute : neuf cas, puis trois de plus sur la commande Astra finale. Écarts de
   modèle : code 2, rien envoyé. Accords : connexion refusée, plancher. Modèle et prix figés.
7. `lancer_relais_local_v1.py` : sept cas. Noms refusés : code 2, sans console. Session neuve : `True`. Console existante :
   refusée.
8. `pytest -q -p no:cacheprovider` (environnement virtuel du dépôt, `-I -B`, cache et racine dans le bloc-notes) :
   - essais des commandes v3e et Astra, du lanceur de relais et du lanceur modèle : 304 réussis, 6 échecs attendus ;
   - essais du lanceur v8 : 3 échecs à 04:16Z, puis 223 réussis et 6 échecs attendus à 04:19Z (constat S2).
9. `verifier_go` du lanceur sur le registre actuel → refus (0 ligne). Sur le registre de la branche au commit `156f2978` →
   accepté, 34 USD (constat B1).
10. Mesure du rapport octets/caractère du corps JSON d'Astra sur la question et les faits : 1,053 (borne du lanceur : 1,15).

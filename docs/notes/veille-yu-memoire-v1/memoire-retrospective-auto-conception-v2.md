# Mémoire rétrospective de la conception de l'auto-conception de l'organisme d'idéation — v2

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`), modèle Fable 5.2 (`claude-fable-5-2`), le 19 novembre 2026 ; lecture commencée à 06:59:14Z (`date -u`). Ce lecteur n'a écrit aucune des pièces lues.
- **Version 2** : la version 1 (`memoire-retrospective-auto-conception-v1.md`, `d117d45e95e911124e276177d07897e26e89022819ab2c46a4774b8eba8a23be`) reste en place, intacte (R12). Cette version porte les corrections de la contre-lecture d'un lecteur d'un autre modèle, Opus 5.5 (`contre-lecture-lecture-yu-v1.md`, `97ac990c4fd450c3cd1cc3775db1bcf73f0ade242564f7ce94a5c392b723bb9f`, erreurs 7 à 9 et son point 9), revérifiées par ce lecteur sur les lignes citées des devis v2b et v2f : classements de A2, D1 et D2 corrigés ; compte donné aux deux tolérances ; A1 et E2 marquées contestables. Le contre-lecteur a rouvert les quatorze prédictions à la source : toutes sont écrites avant leur résultat, toutes les citations sont exactes ; il n'a pas ouvert les manifestes de fin.
- **Ce que c'est** : la mémoire que l'organisme aurait tenue si, pendant les deux tentatives de sa course d'auto-conception (18 et 19 novembre 2026), il avait rangé ses essais par problème récurrent, avec la justification, la prédiction écrite avant le résultat, le résultat et la provenance — le format de Yu et al. (2026, arXiv 2611.18856v1, p. 3-4 et annexe D.3 p. 22). Elle est reconstruite après coup, depuis les registres seuls.
- **Ce que ce n'est pas** : une mesure de la qualité des conceptions. Les deux courses se sont closes « non mesurées » pour cause technique ; aucune carte de conception n'a été classée. La mémoire ci-dessous porte donc sur la conduite de la course (commandes, réglages, devis), pas sur des idées de conception.
- **Aucune réponse de modèle n'a été lue.** Rien sous `/home/user/sorties-course-auto-conception-*`, rien sous `/tmp/pole-sessions-*`, aucun journal de relais, aucun journal de sortie du lanceur. Des manifestes de fin, seuls les champs techniques (codes, comptes, coûts, heures) ont été lus par un filtre qui écarte tout champ de texte.

## Sources lues

| pièce | où | empreinte ou repère |
|---|---|---|
| registre des décisions | `registres/decisions.md` (arbre de travail) | lignes R-3271, R-3273, R-3274, R-3278, R-3342, R-3360, R-3398, R-3399, R-3446, R-3502, R-3504, R-3554, R-3584, R-3610, R-3613, R-3616 |
| journaux provisoires du compte organisme, versions 39 à 63 | branche `lot/compte-organisme-v1`, commit `e1068e3715e5c43ba52b0934179778709b432a53` (19 novembre, 06:35:17Z), dossier `registres-provisoires/` | lignes PO-101 à PO-183 qui touchent l'auto-conception, Carbon, Astra, les témoins |
| diagnostic technique des erreurs de Carbon et d'Astra | même commit, `docs/notes/organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md` | `510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec` (vérifiée) |
| préenregistrement v2 de la course | même commit, `…/course-v2/preenregistrement-course-auto-conception-v2.md` | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` (vérifiée) ; lignes de titres et section « Prédiction chiffrée » |
| devis v2b et v2f, additif v2f | même commit, `…/devis-course-auto-conception-v2b.md`, `…/course-v3/devis-course-auto-conception-v2f.md`, `…/course-v3/additif-preenregistrement-course-auto-conception-v2f.md` | `b2319472…`, `7a8ef9d4…`, `3199e80e…` (vérifiées par recalcul) ; lignes chiffrées seulement |
| manifestes de fin des deux courses | même commit, `runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json` et `runs/20261119-001004-course-auto-conception-v6/manifeste-lanceur-fin.json` | champs techniques seulement |

## Règle de classement (écrite par ce lecteur, après coup — réserve 1)

- Une prédiction n'entre que si elle est écrite à une ligne datée **avant** le résultat qui la tranche. Un réglage, une règle d'arrêt ou une réserve ne sont pas des prédictions.
- « Juste » : une borne annoncée est tenue, ou un montant annoncé est atteint à la tolérance près. « Fausse » : le contraire est observé. « Non vérifiable » : ce qui devait la trancher n'a pas été joué, ou a été arrêté avant. **Une attente jamais jouée est non vérifiable, même si un raisonnement ou une documentation la contredit** (la version 1 dérogeait à cette règle pour A2).
- **Deux tolérances, toutes deux écrites** : ± 20 % et ± 10 %. Aucune n'existait avant les résultats ; elles sont de ce lecteur. Le compte **change** de l'une à l'autre (D2, à − 10,4 %) ; la version 1 disait le contraire, à tort.
- Un devis se compare à la **même étape** que le résultat : les deux courses n'ont joué que l'étape « proposition », et les deux devis donnent la part de cette étape. La version 1 comparait le coût de la proposition au devis de la course entière (D1) et déclarait D2 non vérifiable ; c'était asymétrique.
- Deux entrées sont **contestables comme prédictions** (A1, E2) : elles sont gardées au compte et marquées ; le compte est aussi donné sans elles.

## La mémoire, rangée par problème récurrent

### Problème A — le proposeur Carbon, appelé par lot, ne rend pas de proposition exploitable ; l'étape « proposition » est alors « non mesurée » et l'unique tentative est consommée

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance (modèle, banc, course) | prédiction juste ? |
|---|---|---|---|---|---|---|
| A | A1 — 18 novembre, 17:19Z, lanceur v4, commande par lot aux réglages par défaut (budget de pensée 8 192 jetons, délai 1 500 s) | Carbon n'est déclaré qu'après une épreuve réelle de sa commande (R-3273) ; cette épreuve est une autre course, à deux lots courts (R-3274) | « La commande Gemini par lot et le relais v4 sont donc éprouvés de bout en bout (utile au compte de l'organisme, R-3273) » — R-3274, 18 novembre 08:58:17Z | 5 propositions jouées sur 11, 1 réussie, 4 en erreur ; course close code 2, étape « non mesurée (technique) », 44,780492 USD (PO-149, PO-150 ; manifeste de fin v4 : `prop-carbon` 5 appels) | proposeur `gemini-4-carbon` par lot ; course d'auto-conception v4 ; catalogue de matière v3 | **fausse — contestable comme prédiction** : la phrase est le constat d'une épreuve faite (deux lots courts), non une prédiction de la course ; elle n'est fausse que lue comme « la commande marchera dans la course », lecture qui a fondé la déclaration de Carbon (R-3273, R-3278) |
| A | (même tentative A1) | — | Sur l'issue de la course elle-même : « Prédiction chiffrée et signe attendu — Aucune » (préenregistrement v2, section du même nom) | — | — | pas de prédiction écrite |
| A | A2 — 18 novembre, 21:29Z, correction proposée par le diagnostic (jamais lancée ; lanceur v5, additif v2e) : budget de pensée 32 768, sortie maximale 16 384, délai relevé | trois erreurs = pensée de 17 454 à 20 696 jetons au-delà de la provision de 8 192 ; le seul lot sans pensée est le seul réussi (diagnostic, § 2-3) | « Carbon : `--provision-pensee-jetons 32768`, `--max-sortie-jetons 16384` (sorties observées ≈ 3 400 jetons), ce qui garde le pire cas d'un appel sous le plafond de 3 USD » — diagnostic, § 6, 18 novembre 21:29:57Z | **jamais jouée** (lanceur v5 et additif v2e jamais lancés en réel, PO-166). Ce que la citation affirme est un calcul de coût (2,38 USD), que rien n'a démenti. À part : l'attente implicite que les réponses tiendraient dans 16 384 jetons est contredite par la documentation du fournisseur — la sortie maximale compte la pensée (PO-161, 22:11:28Z) ; « chaque réponse de Carbon aurait été coupée […] il est désormais établi » (additif v2f, ligne 15) | lecture de documentation ; aucune course | **non vérifiable** (jamais jouée ; attente implicite réfutée par la documentation) |
| A | A3 — 19 novembre, 00:10Z, lanceur v6, additif v2f : sortie maximale 32 768, budget de pensée 28 672, délai de lot 1 620 s | la sortie doit couvrir la pensée la plus forte observée (20 696) plus la réponse (≈ 3 500) ; provision ≥ 1,385 fois cette pensée (additif v2f, ligne 19) | « la pensée de 28 672 au plus laisse au moins 4 096 jetons de réponse dans 32 768 » — devis v2f, § 2, écrit le 18 novembre vers 22:50Z (PO-166, 22:53:07Z) | aux trois lots : 32 765 jetons de pensée, 3 jetons de réponse ; 3 erreurs consécutives, 6 propositions non jouées ; code 2, 42,360849 USD (PO-177, PO-178 ; manifeste de fin v6 : `prop-carbon` 3 appels) | proposeur `gemini-4-carbon` par lot ; course d'auto-conception v6 ; même matière | **fausse** (énoncé conditionnel dont la prémisse, une pensée d'au plus 28 672 jetons, est démentie ; prémisse déjà mise en doute par le diagnostic, § 3) |
| A | A4 — 19 novembre, 06:35Z, lanceur v7 en développement : Carbon par la commande synchrone qui sert Argon, éprouvée d'abord par un appel réel sur le plus grand lot ; plafond par appel 3 → 6 USD, plafond de course 90 → 120 USD | « en mode lot, le budget de pensée n'est pas tenu ; Carbon remplit la place qu'on lui donne » (PO-178, leçon tirée après coup) ; la commande synchrone a rendu 11 sur 11 pour Argon (PO-181) | « Carbon peut penser et répondre » sous un plafond par appel de 6 USD — PO-182, 19 novembre 06:35:16Z | pas encore joué à l'heure de cette note | — | **non vérifiable** (en attente) |

### Problème B — la même commande sert la course d'affinage des idées des mentors

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance | prédiction juste ? |
|---|---|---|---|---|---|---|
| B | B1 — 18 novembre, 19:31Z : affinage v7 suspendu | même composition, même commande de Carbon par lot, tentative unique | « le même échec est probable tant que la cause des erreurs de Carbon n'est pas établie » — PO-151, 19:31:33Z (repris R-3398) | l'affinage n'a jamais été joué (R-3584, PO-179) | — | **non vérifiable** |

### Problème C — l'épreuve réelle des témoins du juge, préalable à la course, n'aboutit pas pour cause technique

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance | prédiction juste ? |
|---|---|---|---|---|---|---|
| C | C1 — 18 novembre, 14:00Z, programme d'épreuve v2 | épreuve hors ligne réussie (R-3271) | pas de prédiction écrite | arrêt avant tout appel : erreur de chemin levée par la garde de l'orchestrateur ; 0 USD (PO-114) | juges `claude-opus-5-5` et `gemini-4-argon` ; 11 témoins plantés | pas de prédiction écrite |
| C | C2 — 18 novembre, 16:11Z, programme v3 (correctif v2c) | garde neuve sur les 33 dossiers d'appel ; contre-lecture « Scellable. », 241 essais passés (PO-127, PO-130) | pas de prédiction écrite | « échouée » pour causes techniques : bac à sable absent du conteneur ; relais d'Argon plafonné à 15 appels quand 22 sont nécessaires ; 0,132289 USD (PO-131) | mêmes juges | pas de prédiction écrite sur l'issue ; l'estimation de coût du devis v2b (1,13 USD) valait déjà pour cette tentative, arrêtée avant la fin : non vérifiable ici, comptée une seule fois, en C3 |
| C | C3 — 18 novembre, 17:07Z, programme v4 (correctif v2d) | sonde du bac et contrôle de la borne d'appels avant tout appel (PO-133) | coût : « Épreuve des témoins inchangée (estimation 1,13 USD, haut 3,39, plafond 5) » — devis v2b, ligne 33, écrit avant 13:44Z (PO-105) | « réussie », 11 verdicts par juge ; 1,204591 USD (PO-139) | mêmes juges | **juste** (coût, + 6,6 %) |
| C | C4 — 19 novembre, 00:04Z, programme v6 | inchangé | coût : épreuve 1,20 USD — additif v2f, ligne 29, 18 novembre vers 22:50Z | « réussie » ; 1,177995 USD (PO-174) | mêmes juges | **juste** (coût, − 1,8 %) |

Fait à garder : l'absence du bac à sable était **écrite au journal** à 13:44:26Z (PO-103 : « `bwrap` et `socat` absents ») ; l'épreuve C2 a échoué sur cette cause à 16:11Z (PO-131, qui renvoie lui-même à PO-103). L'information existait, datée, dans le journal ; elle n'était rangée sous aucun problème et n'a pas été servie à l'auteur du correctif.

### Problème D — le coût réel s'écarte du devis

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance | prédiction juste ? |
|---|---|---|---|---|---|---|
| D | D1 — devis v2b, 18 novembre (avant 13:44Z) | jetons estimés par espèce, prix du jour | part des proposeurs, soit l'étape « proposition » : **28,32 USD** estimés pour 55 appels, 53,31 au haut (devis v2b, ligne 11 ; la course entière y est estimée à 39,62). Par rôle, d'après le champ `ecart_au_devis_v1` du manifeste de fin v4 (et non d'après la ligne 11 du devis) : Fable 6,9751, Opus 2,7896, Argon 5,7893, Astra 6,9751 | 44,780492 USD pour l'étape « proposition », arrêtée à 49 appels sur 55 : **+ 58 %** sur l'estimation de cette étape ; la valeur haute de 53,31 est tenue. Par rôle : Fable 17,514014 (× 2,5), Opus 7,275471 (× 2,6), Argon 4,214434 (× 0,73), Astra 7,30824 (× 1,05) (manifeste de fin v4) | course v4 | **fausse** aux deux tolérances (sous-estimation de 58 % ; plafond de 90 USD tenu) |
| D | D2 — devis v2f, 18 novembre vers 22:50Z, base : coûts réels de la course v4 | — | étape « proposition » : **47,26 USD** estimés (devis v2f, ligne 11 : « course (proposition 47,26 ; aiguillage 3,41 ; juges 7,89) | 58,55 USD ») ; course entière 58,55 ; parts attendues Claude ≈ 35, Google ≈ 17,6, OpenAI ≈ 7,4 (PO-167) | 42,360849 USD pour l'étape « proposition » : **− 10,4 %** sur l'estimation de cette étape ; Claude 24,716609, Google 12,84088, OpenAI 4,80336 (PO-177 ; manifeste de fin v6). L'observé ne compte que 3 appels de Carbon sur 11 et 47 appels de proposeurs sur 55 : il est tiré vers le bas par l'échec de Carbon. L'estimation de la course entière reste intranchée (aiguillage et juges non joués) | course v6 | **juste à ± 20 %, fausse à ± 10 %** ; biaisée par l'échec de Carbon |
| D | D3 — 18 novembre, 18:09Z | appels d'Astra payés par une seconde clé créditée de 30 USD | « part d'Astra au pire ≈ 16,5 USD, sous 30 » — PO-144, 18:09:13Z | Astra 7,30824 USD (PO-150) | course v4 | **juste** (borne tenue) |
| D | D4 — 18 novembre, 22:11Z | clé Claude « Rigaud » | « reste net ≈ 91,7, juste au-dessus de 90 ; aucune marge si un solde réel est plus bas que nos comptes » — PO-164, 22:11:28Z | relevé au départ : reste net ≈ 90,76 USD ; départ accepté par le lanceur (PO-174, PO-175) | course v6 | **juste** |
| D | D5 — 18 novembre, 22:11Z | même clé, réserves non levées | « reste net 73,7 < 90 → code 3 certain » — PO-163, 22:11:28Z | jamais joué dans cet état : les réserves ont été levées (PO-164, R-3479) | — | **non vérifiable** |

Fait à garder : le manifeste de fin de la course v6 compare encore le coût réel à l'estimation de 39,6167 USD du devis v2b (`ecart_au_devis_v1.devis_estimation_usd`), non aux 58,55 USD du devis v2f qui la régissait.

### Problème E — un appel d'Astra coupé par le réseau suffit à rendre l'étape non mesurée

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance | prédiction juste ? |
|---|---|---|---|---|---|---|
| E | E1 — course v4 | — | pas de prédiction écrite | 1 erreur sur 11 (réponse 502 du relais, connexion coupée, 18:41:35Z) (PO-147, PO-149) | proposeur de la lignée Astra ; course v4 | pas de prédiction écrite |
| E | E2 — course v6 : aucune reprise ajoutée, « aléa accepté » (PO-166), contre la recommandation du diagnostic (une reprise unique déclarée) | dix autres appels sans incident | « Lecture : aléa de connexion, non reproductible par ce diagnostic » — diagnostic, § 4, 21:29:57Z | Astra 11 sur 11 (PO-177) | course v6 | **juste, indice faible — contestable comme prédiction** : c'est une lecture de diagnostic ; une seule course sans coupure ne la tranche pas |

### Problème F — durée et survie du lanceur

| problème récurrent | tentative (date, version) | justification | prédiction (verbatim, source) | résultat observé (source) | provenance | prédiction juste ? |
|---|---|---|---|---|---|---|
| F | F1 — course v4, lanceur porté par une commande d'arrière-plan coupée par l'outil à deux heures | — | pas de prédiction : une réserve (« sa survie à cette coupure n'est pas établie », PO-141) | parade trouvée par une épreuve sans dépense ; lanceur vivant jusqu'à la fin (PO-145, PO-148) | course v4 | pas de prédiction écrite |
| F | F2 — course v6, lanceur détaché de l'outil | — | « durée attendue 2 à 4 h » — R-3554, 19 novembre 00:10:06Z | 1 h 41 min (00:10:05Z à 01:51:10Z, manifeste de fin v6), course arrêtée après l'étape « proposition » | course v6 | **non vérifiable** (course arrêtée tôt) |

## Compte

Quatorze prédictions écrites avant leur résultat, à une ligne datée (ordre des dates et citations confirmés par la contre-lecture).

| tolérance sur les montants | justes | fausses | non vérifiables |
|---|---|---|---|
| **± 20 %** | **6** : C3, C4, D2 (part « proposition »), D3, D4, E2 | **3** : A1, A3, D1 | **5** : A2, A4, B1, D5, F2 |
| **± 10 %** | **5** : C3, C4, D3, D4, E2 | **4** : A1, A3, D1, D2 | **5** : A2, A4, B1, D5, F2 |

- Parmi les neuf tranchées : 6 justes et 3 fausses à ± 20 % ; 5 justes et 4 fausses à ± 10 %.
- **A1 et E2 sont contestables comme prédictions** (un constat d'épreuve ; une lecture de diagnostic). Sans elles, il reste douze prédictions : 5 justes, 2 fausses, 5 non vérifiables à ± 20 % ; 4 justes, 3 fausses, 5 non vérifiables à ± 10 %.
- **Sur le problème A : deux prédictions tranchées, deux fausses** (A1, contestable ; A3). A2 et A4 ne sont pas tranchées. La version 1 écrivait « trois sur trois » ; c'était faux.
- Le compte de la version 1 (5 justes, 4 fausses, 5 non vérifiables) se retrouve par hasard à ± 10 %, mais par d'autres classements : A2 y était fausse et D2 non vérifiable.

Cinq tentatives ou issues sans aucune prédiction écrite : l'issue de la course elle-même (préenregistrement : « Aucune »), C1, C2 (sur l'issue), E1, F1.

## Ce que le compte dit, et ce qu'il ne dit pas

1. **Les prédictions justes portent toutes sur de la comptabilité** (coûts, bornes, reste d'une clé — D4 est une arithmétique de nos propres comptes plus qu'une prédiction) ou sur un aléa. **Sur le problème qui a bloqué les deux courses (A), aucune prédiction n'a été juste : deux tranchées, deux fausses, deux intranchées.** Ce constat qualitatif tient aux deux tolérances et avec ou sans A1 et E2 ; les chiffres, eux, bougent d'une unité selon la tolérance. Les deux tentatives ont coûté 87,141341 USD de courses (PO-179) sans une mesure.
2. **La leçon qui manquait était écrite avant la seconde tentative.** Le diagnostic notait à 21:29Z : « Le budget de pensée demandé n'est pas tenu par le fournisseur en mode lot (fait observé) » (§ 3). La correction A3 a pourtant reposé sur un budget de pensée plus grand, supposé tenu (« la pensée de 28 672 au plus »). Une mémoire rangée par problème aurait mis la justification de A3 en face du fait observé en A1 ; c'est l'usage que Yu et al. décrivent (p. 4 ; cas P8 p. 28-29). Ce lecteur ne peut pas dire qu'elle aurait empêché l'échec : c'est une lecture après coup, sur un seul cas.
3. **L'épreuve qui a justifié A1 n'était pas du même régime** : deux lots finis en ≈ 4 min 30 (R-3274), quand la course a servi des entrées de 28 791 à 40 986 jetons et provoqué 17 000 à 21 000 jetons de pensée (diagnostic, § 2). La provenance (quelle entrée, quel régime) aurait dû voyager avec l'affirmation « éprouvée ».
4. **Quatorze prédictions sur deux courses ne mesurent rien de général.** Les prédictions ne sont pas indépendantes (A2 et A3 sont deux essais de la même idée), la règle de classement est écrite après coup, et celui qui classe sait l'issue. C'est un état des lieux, non une calibration.

## Réserves

1. La règle de classement et les deux tolérances (± 20 %, ± 10 %) sont de ce lecteur, écrites après les résultats ; le compte dépend de la tolérance.
2. Les heures de fin diffèrent d'une minute entre le registre (01:52:07Z, R-3584) et le manifeste de fin v6 (01:51:10Z) ; le manifeste est retenu pour la durée.
3. Le devis v2b n'est pas daté à la ligne ; il précède PO-105 (13:44:26Z), qui le cite par son empreinte.
4. Les lignes R-3360, R-3398, R-3399, R-3446, R-3554, R-3584 du registre des décisions sont des messages du compte organisme rapportés par la mère (« donnée ») ; elles concordent avec les lignes PO- du journal du compte, lues à la source.
5. Aucune réponse de modèle, aucune carte, aucun journal de relais n'a été ouvert : ce que les proposeurs ont rendu est hors de cette mémoire.
6. Les faits tirés des seuls manifestes de fin (« `prop-carbon` 5 appels » et « 3 appels », coûts par rôle, comparaison du manifeste v6 au devis v2b, heure de fin 01:51:10Z) n'ont pas été revérifiés par la contre-lecture, qui n'a pas ouvert ces manifestes ; ils reposent sur la lecture de ce lecteur seul.
7. Le classement de D2 est le plus fragile du tableau : « juste » à ± 20 % seulement parce que l'échec de Carbon a réduit la dépense de l'étape.

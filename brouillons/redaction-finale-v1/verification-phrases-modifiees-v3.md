# Vérification des phrases modifiées par le directeur (dix réponses Pivotal) — v3

- **Vérificateur neuf** (sous-agent) : je n'ai écrit ni les réponses de Lazar Ciric au formulaire Pivotal, ni leurs registres, ni aucune de leurs vérifications. Travail du 3 novembre 2026, de 16:29:25 à 16:42:51 en temps universel coordonné (UTC ; heures relevées par `date -u`), puis écriture de ce fichier.
- **Consigne** : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-phrases-modifiees-v3.md`, empreinte SHA-256 (fonction de hachage) `e3f2784e6cae935137fa21e0846d62908dda8566468953ca3cb6387998f5827a`, égale à l'annonce, vérifiée avant lecture.
- **Fichier vérifié** : `brouillons/redaction-finale-v1/phrases-modifiees-v3.md`, `bc1b2248e09870faffcb37f92c8bc4dd69ef96dda1d9f54383d81fe49c1ba4cc`, égale à l'annonce et à son compagnon. Son titre dit « — v2 », son nom dit v3 : sans effet sur le fond. 13 phrases « + », numérotées ici de 1 à 13 dans l'ordre du fichier, et une suppression sans remplacement (Colognese et Ward, question 1, variante courte).
- **Complétude** : comparaison mot à mot (`git diff --no-index --word-diff`) de chacun des dix couples de versions nommés dans les en-têtes. Hors notes de version situées sous `---`, aucun changement que le fichier ne déclare.
- **Versions finales lues pour le contexte** (empreintes recalculées, chacune égale au préfixe de son en-tête et à son compagnon) :

| réponse | version précédente | version finale | sha256 de la finale |
|---|---|---|---|
| Kirchner, question 1 | `kirchner-q1/reponse-v2.md` `da5ce1e8…fbc5` | `kirchner-q1/reponse-v3.md` | `3592a009f8f64f092b851cb3a4530518ab280e17cd771cf4c8c58ce85179fac6` |
| Kirchner, question 2 | `kirchner-q2/reponse-v2.md` `c23fb113…3f52` | `kirchner-q2/reponse-v3.md` | `4611a645a85a67a569035bc376a966b2a749d0b45c42e0e0acbeed4d1cb1bc04` |
| Heimersheim, question 2 | `heimersheim-q2/reponse-v2.md` `a0154404…980e` | `heimersheim-q2/reponse-v3.md` | `b05579770ea3fc5b11d1417b94412b39c7926f1219f134e22bc148d7d049c1a6` |
| Ibrahim, question 1 | `ibrahim-q1/reponse-v3.md` `4dcba66e…b679` | `ibrahim-q1/reponse-v4.md` | `a1646baa39fc11412b1319fab163942a1208faad3d2f49e040fcccbd80bfccc2` |
| Ibrahim, question 1, variante de repli | `ibrahim-q1/reponse-variante-survie-v2.md` `d2598285…5349` | `ibrahim-q1/reponse-variante-survie-v3.md` | `00ee589dcff230e95c30343ee385de84a795f919d0a10c758ecceebad694f112` |
| Ibrahim, question 2 | `ibrahim-q2/reponse-v2.md` `a075396f…a0d4` | `ibrahim-q2/reponse-v3.md` | `1aece077780d6ebe65bc526273a4c4e8220cac68d423a47f09e9e78c85c6a95c` |
| Scheurer | `scheurer/reponse-v2.md` `d9f3bc73…98e3` | `scheurer/reponse-v3.md` | `d4eb67c554039359ad9d0c7f1cc1e95966add303103fe664ce772a74468960bc` |
| Colognese et Ward, question 2 | `colognese-ward-q2/reponse-v2.md` `06bb673a…5b59` | `colognese-ward-q2/reponse-v3.md` | `faa023216c873577cbe98d86007bf19678c92767ec15d3fe5e44e3d810452bb7` |
| Colognese et Ward, question 1, variante courte | `colognese-ward-q1/reponse-v3.md` `5e25e472…c3a8` | `colognese-ward-q1/reponse-variante-courte-v1.md` | `1d380d5e35ff912d613f0dbcd032917b2c84fff5ccc2295efd1163c150fc55bc` |
| Feng et Jang | `jang-feng/reponse-v2.md` `c29f6437…e4e5` | `jang-feng/reponse-v3.md` | `05f3e8c7cdc158fda78d4fbc34b19eaa2a3971ff56fb5c9733d1039a57f52c8a` |

- **Questions** (texte exact) : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` (égale à son compagnon) ; lignes 20 à 24 (Heimersheim 2, « Max. 150 words »), 28-29 (Kirchner 1), 73 (Kirchner 2), 81-82 (Feng et Jang), 108-109 (Scheurer), 135-136 (Ibrahim 1), 148 (Ibrahim 2), 163-164 (Colognese et Ward 1, « max 200 words »), 174 (Colognese et Ward 2).
- **Méthode** : chaque fait des phrases « + » relu par moi à sa source.
  - Dépôts publics : clones frais aux commits épinglés, lus par `git show`, `git ls-tree` et `git cat-file` ; aucun `git fetch` ; aucun code des dépôts exécuté. Les trois têtes locales sont égales à `origin/main`, et les trois branches distantes sont toujours à `146b2a4`, `b3ecaec` et `faff48b` (`git ls-remote`, 16:31 UTC, qui ne rapatrie rien).
  - Visibilité publique : pages `blob/` servies à un visiteur non connecté (outil de lecture du web, WebFetch ; métadonnée « repository_public: true ») et interface de programmation de GitHub (`gh api`, lecture seule).
  - Papier et billet des mentors : lecture web par WebFetch, outil qui passe par un petit modèle et rend des citations courtes. C'est le niveau « transcription » au sens de la règle gelée R7 : suffisant pour un formulaire, non opposable dans un papier.
  - Vérifications antérieures : servies de carte, non de preuve.
- **Incidents** :
  - WebFetch refuse les adresses GitHub en `tree/` (« robots_disallowed », fichier `robots.txt` de GitHub) : `…/sycophancy-construct-validity/tree/146b2a4` et `…/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses` n'ont pas été lues telles quelles. Je les ai contrôlées par la page `blob/` au même commit, servie publiquement, et, pour `ideation-organism`, par `gh api` (dépôt « public », dossier listé à `faff48b`).
  - `gh api` répond 403 pour `sycophancy-construct-validity` et `sycophancy-psychophysical-law` (« GitHub access to this repository is not enabled for this session ») ; je n'ai pas appelé `add_repo`.
  - Aucun outil ne m'a demandé d'approbation ; aucun appel n'a été refusé par l'environnement.
  - Seul code écrit : `/tmp/verif-pm-v3/compte.py` (sha256 `a7e7441233ffecb11572ae1d7be157a722f7fe18d8acfdd7f36a65482d2a8192`), compte de mots, hors du dépôt, lancé par `python3 -I` sur les seules réponses.
- **Sigles des phrases anglaises citées**, développés une fois : RL, apprentissage par renforcement ; CI, intervalle de confiance ; LLM, grand modèle de langue. R1, R2, R4, R6, R7, R9, P3 et T0.3 sont des étiquettes de suites des dépôts publics ; W1 et W2, les deux mondes jouets de l'attaque.
- **Légende des verdicts** : exact ; inexact (ce qui est juste est dit) ; non vérifiable ; non publié présenté comme publié ; plus fort que sa source ; « hors champ » = phrase sans fait (plan, raisonnement), comptée à part.

## Sources (sigles des tableaux)

| sigle | source et emplacement | sha256 | état |
|---|---|---|---|
| [A] | `resultats/attaque-goodhart-v2/README.md` de `lciric/ideation-organism`, commit `faff48b` (clone `/home/claude/ideation-organism`) | `84d6e77b3b2c6dc6b79640eb48ccce07d4258c70a5943756c49af000ca0609bc` | public |
| [PA] | `orchestrator/prereg/preenregistrement-attaque-goodhart-v2-v1.md`, même commit (égal à l'empreinte du préenregistrement publiée sur [A] l. 7) | `fc81d015d27e60388099c7845a66b75d613187f99d5d0060950540a686925b65` | public, scellé |
| [VA1] | `brouillons/a1-lecture-v1/verdict-a1-v1.md` (verdict du lecteur neuf ; empreinte publiée sur [A] l. 7 et 9, texte privé) | `795e5e992d65bce3096d78f1cd4c36c95cdfc00cdeb40f6259278275e92d3909` | interne |
| [T03] | `resultats/controle-simulation-defenses/README.md`, commit `faff48b` | `04ce0afcedb95478103fb76c15680f185e8614c0f0ed08616162d848270d8ba0` | public |
| [R1p] | `resultats/controle-r1-blanche-noire/README.md`, commit `faff48b` | `6c2dffc8777cf7fbba82ea6e6617dbb76b4d5e877290a87cfebf79be5a140a46` | public |
| [CV] | `README.md` de `lciric/sycophancy-construct-validity`, commit `146b2a4` (clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity`) | `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` | public |
| [PL] | `README.md` de `lciric/sycophancy-psychophysical-law`, commit `b3ecaec` (clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`) | `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` | public |
| [ST] | `STATUS.md`, même commit | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` | public |
| [R9a] | `preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md`, même commit | `81abd962afe1ba8f99840a8b54262b1820184e5a767139712d1e5898d28ce36e` | public |
| [R1a] | `results/R1a/README.md`, même commit | `adce975d8cd9edd0de14d9b730fc2bd6a7bad2f1c4f6deedb8499465c10a0736` | public |
| [R1b] | `results/R1b/README.md`, même commit | `8200f92765ac4b8167e6ac4d289db177bcb6ce36d0a95686c51605c8b8bfaaa6` | public |
| [R2] | `results/R2/README.md`, même commit | `fdae23cafe9a033fbdf9a4b798d79c38f379e8df71f4b6c6d00282e45a42a36d` | public |
| [R4] | `results/R4/README.md`, même commit | `2664d85cb9d3e33523d352daf2d2054729d2d71e42c7b6daf5ad92bcffe4f781` | public |
| [R6] | `results/R6/README.md`, même commit | `27ad89efb844830dea387d2c0a24b5a27e68165d9953b14928b69e287dd2eca9` | public |
| [R6d] | `results/R6/R6_llama_sensitivity-norefusals_dose_output.txt`, même commit | `987287cc4e6d58eea6ae2ec0533be22eff847a67ec8b70c626d2b9a9a5162b6f` | public |
| [R6f] | `results/R6/R6_llama_strong_sensitivity-norefusals_output_items16_K5.txt`, même commit | `a94d13e005ab433bd31ac04695730f7b0e0e1d4186eb5ea4fc2182a85137effc` | public |
| [R7] | `results/R7/README.md`, même commit | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` | public |
| [R7a] | `preregistrations/2026-11-02_addendum_R7_monitor_deference.md`, même commit | `4cc54a84f3960294b00f7222f28af890529a586926faae0d52aefb5e27160974` | public |
| [CW] | Colognese et Ward, « Character training can mitigate reward hacking, but can also make it harder to detect », 28 septembre 2026, `https://www.lesswrong.com/posts/2maYXkEgnfJHPAkxh/` ; lecture web du §3.3 et de la note 1 (« Corrections (14th Oct 2026) ») | — | public, transcription |
| [2507] | Ibrahim, Hafner, Rocher, « Training language models to be warm and empathetic makes them less reliable and more sycophantic », arXiv 2507.21919v2, `https://arxiv.org/pdf/2507.21919v2`, deux lectures web ciblées | — | public, transcription |
| [F] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` (corrections de la lectrice indépendante) | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` | interne |
| [VPM2] | `brouillons/redaction-finale-v1/verification-phrases-modifiees-v2.md` | `c3d3e7f9daee5c26f2fc4304b4adb2fcfd68c3a20ba713b0760d63ce0e462101` | interne |
| [VI3] | `brouillons/redaction-finale-v1/verification-phrases-modifiees-ibrahim-q1-v3.md` | `c1c00ea7db46c27cf6e1a7646f6bef75f6512cf35150ac421a6acbd6eb625aea` | interne |
| [CF] | `brouillons/redaction-finale-v1/coherence-finale-v1.md` | `ec0b04c3e627fdb6a7125035531e7e373efa87a20ab3893f602ab8ddce2ed595` | interne |
| [RC] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` | `cf1edec99be3ecd54a2d09b1c6c1c3931de6ca1a03e47cbbccde58e03f65b395` | interne |
| [RI] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` (ne couvre pas SocioT Warmth : d'où [2507]) | `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` | interne |

Les empreintes des sources internes sont égales à leurs compagnons `.sha256`. Les fichiers `verification-chiffres-v1.md` et `lecture-mentor-v1.md` de chaque réponse n'ont pas été ouverts : chaque fait des 13 phrases a été relu à sa source primaire. Les lignes « programme non publié » de `recoupement-v1.md` sont sans objet : aucune phrase « + » ne cite « < 1 % », et ρ = 0,684 y est lié à sa page publique.

## 1. Kirchner, question 1 (`kirchner-q1/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 1 | « They barely got the chance: 11 of the 12 promotions came at the first attempt, before any verdict existed. » | [A] l. 7 (« on W2, Argon was promoted in 12 of 12 units, 11 of them at the first attempt with or without feedback, so the share of the feedback is not measured ») ; [VA1] l. 109 (« 12 sur 12 en au plus 4, 11 sur 12 dès la première, dans les deux conditions ») : dans le bras avec verdicts, une promotion sur 12 est venue à la 2e, 3e ou 4e tentative, donc après au moins un verdict ; [PA] l. 109-111 (chaque suite « retour » ne voit que « l'historique des tentatives précédentes » de sa carte ; la première tentative n'a donc aucun verdict) | **exact** : « barely » rend la seule promotion venue après un verdict. La phrase suivante (« So the hole was coverage… ») reste juste : le témoin sans verdict promeut aussi 12 sur 12, dont 11 dès la première |

Contradictions internes : aucune (« all 12 of its runs, with or without verdicts » : 12 par condition). Liens : aucun dans la phrase.

## 2. Kirchner, question 2 (`kirchner-q2/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 2 | « In my preregistered simulation (synthetic scores), a shift shared by an episode's scores pushed Ville's always-valid alarm rule, nominally 5% (under 2% with independent scores), to 21–35% false alarms at the largest shifts; a threshold calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). » | [T03] l. 3 (simulation préenregistrée) ; l. 16 (aucune attaque ; alarme quand le processus d'e-valeurs atteint 1/α, α = 0,05) ; **l. 20** (« well specified (Gaussian scores; 1 × 200, 1 × 1000 and 5 × 40) \| 0.017 to 0.019 \| 333, 387 and 337 of 20,000 ») ; **l. 55** (« honest reference law: independent N(0, 1) ») ; l. 21-22 (τ = 0,2, le plus grand décalage de la grille : 0,21 et 0,35) ; l. 30 (K = 1 000 épisodes honnêtes entiers, « drawn from the same law as the test », 0,046 à 0,055) ; l. 32 (« always-valid aggregators ») ; l. 34 (« a shift shared by all the scores of an episode », chaque score restant N(0, 1)). Lien : dossier présent à `faff48b` (`git cat-file` : `tree` ; `gh api` : `README.md` et `pieces` listés ; dépôt « public ») ; page `blob/faff48b/resultats/controle-simulation-defenses/README.md` servie publiquement, ligne « well specified » lue | **exact**. Nuance : « independent » vaut ici « indépendants et de la loi supposée », le cas bien spécifié. La cellule « σ underestimated by 20 % » (l. 25), à scores indépendants mais écart type mal estimé, donne 0,066. La phrase oppose dépendance et indépendance à marges identiques (l. 34) : juste |

Contradictions internes : aucune. L'incise lève la tension avec la question 1 (seuil de Ville sur tirages neufs), relevée en M10 par [CF].

## 3. Heimersheim, question 2 (`heimersheim-q2/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 3 | « In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it, at the doses I tried (github.com/lciric/sycophancy-construct-validity/tree/146b2a4). » | [CV] l. 3 (« no single-direction intervention and no head ablation reduced the judged rate ») ; l. 21 (méthodes de rang 1, « no clean reduction », sorties non gardées) ; l. 70 (« ρ = 0.684 on raw activations » ; « treat them as training fit ») ; l. 115 (« ρ may also be training fit ») ; [F] §2 (« Épingle aussi ρ à `146b2a4` ») et §3 (ρ et sa réserve : justes). Lien : commit présent dans le clone, tête de `origin/main` ; page `blob/146b2a4/README.md` servie publiquement (« repository_public: true », commit `146b2a450f50…`, ρ et la phrase présents) | **exact**. « at the doses I tried » restreint sans ajouter de fait : le README ne donne aucune dose. L'adresse `tree/` elle-même n'a pas pu être lue par l'outil web (`robots.txt`) ; le commit est public, et GitHub résout ce préfixe, comme le montre la page `blob/146b2a4` |
| 4 | « I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9, github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md; not yet run). » | [R9a] l. 3 (« Written: 2 November 2026, evening, before any forward pass of R9 ») ; l. 16 (directions = moyenne des différences d'activation, avec la phrase de pression moins sans elle) ; l. 9, 20, 23-24 (F1, F2 : l'instrument de Ferreira da Silva et Heimersheim) ; l. 25 (F3 : la rotation vers chaque direction baisse ou monte la note attendue ; « reported, not in the outcome ») ; [ST] l. 27 (« R9, preregistered the same evening ») ; l. 29 (archivé dans v2026.11.5, 10.5281/zenodo.23909891, 06:49 UTC ; « R9 has not run ») ; aucun dossier `results/R9` à `b3ecaec` ; branche distante inchangée à 16:31 UTC. Lien : fichier présent (`81abd962…`) ; page servie publiquement (« repository_public: true », commit `b3ecaecc…`, ligne « Written: » lue) | **exact**. F3 est préenregistrée comme mesure rapportée, hors issue : « preregistered both measurements » tient. « not yet run » est à revoir juste avant 23:00 UTC ([ST] l. 31 : R9 attend l'archivage de R9-bis et un budget signé) |

Contradictions internes : aucune. Comptes de mots : voir la section « Comptes ».

## 4. Ibrahim, question 1, réponse principale (`ibrahim-q1/reponse-v4.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 5 | « If RL erased one and kept the other, one score would misreport survival. » | — ; antécédent : « two effects, lost accuracy and validated false beliefs » (phrase précédente, vérifiée exacte par [VI3] n° 2) | **hors champ** (raisonnement). Correction facultative de [VI3] §4 appliquée : « benchmark » n'avait plus d'antécédent |
| 6 | « My own judge already scores refusals as neutral opinions (next answer). » | [PL] l. 9 (le juge note « the polarity of its verdict from 1 (negative) to 5 (positive) » : 3 en est le milieu) ; [R4] l. 36 (9 refus sur 900, tous sous éloge, « the judge rated each of them 3 ») et l. 38 ; [R6] l. 55 (« the judge rates such refusals near the middle of the scale »). Renvoi : la réponse suivante du formulaire (l. 148) est Ibrahim 2, dont la v3 dit « the judge rates refusals near 3, near the praise destination, so they can mimic attraction » | **exact** (glose). Nuances : tous les refus ne sont pas notés 3 (campagne 1 : 82 sur 85 selon l'appariement de [VI3] §0, non refait ici) ; la grille du juge n'est pas publiée (empreinte `6c95c1c0…`, [R6] l. 15), donc « neutral » lit le milieu de l'échelle de polarité, sans la citer |

Contradictions internes : aucune ; « So I would score refusals and hedges apart » suit. Liens : aucun dans les deux phrases.

## 5. Ibrahim, question 1, variante de repli (`ibrahim-q1/reponse-variante-survie-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 7 | « Before RL and at intervals, I measure warmth (SocioT Warmth, as you did), your false-belief and sad-user conditions, plus a correct-belief control, on held-out non-math factual questions. » | [2507] p. 2-3 (« We measured this using SocioT Warmth, a validated metric that computes log-likelihood ratios … using GPT-2 [30] ») ; p. 9 (« We then evaluated the resulting outputs using SocioT Warmth, a previously validated warmth metric ») ; référence [30] : Cheng, Yu, Jurafsky, « HumT DumT », congrès de l'Association for Computational Linguistics, 2025. Croyance fausse : p. 5 et 9, tableau C3 p. 16 ; tristesse : p. 4, annexe C.1 p. 15. Le papier n'a aucune condition de croyance correcte : ce témoin est de Lazar, et la phrase ne l'attribue pas à la mentore | **exact** (transcription). « as you did » attribue l'usage de la mesure, non sa paternité, comme le voulait [VI3] §4 |

Contradictions internes : aucune.

## 6. Ibrahim, question 2 (`ibrahim-q2/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 8 | « Under criticism the gain stayed flat; under praise it grew, as predicted; but both destinations moved, and at the strongest wording neither arm shifted on average (refusals included). » | [R6] l. 33 (H1 : g(fort) − g(doux) = −0,029 [−0,220 ; 0,197] sous critique, +0,521 [0,285 ; 0,764] sous éloge ; « H1 needs both arms ») ; l. 34 (H2 faux dans les deux bras : ĉ(fort) − ĉ(doux) = +0,500 [0,149 ; 0,803] et −1,537 [−6,185 ; −0,632]) ; l. 29-30 (dose forte, 30 items : −0,147 [−0,487 ; 0,193] et −0,100 [−0,493 ; 0,293]) ; l. 43 (« the mean shift is zero in both arms ») ; [R6f] l. 2-3 (sans les 14 items à refus : −0,587 [−1,000 ; −0,225] et −0,688 [−1,175 ; −0,237]) ; [F] §4 (réserve obligatoire) | **exact**. L'incise borne le dernier constat à l'analyse préenregistrée, qui garde les refus ; correction n° 2 de [VPM2] appliquée mot pour mot |
| 9 | « Two Qwen judges (7B, 72B) recover the law from the same responses; the model's own 1–5 rating shows it, barely under praise. » | [R1a] l. 5 et 19 (Qwen2.5-7B-Instruct, réponses publiées de la campagne 1 ; C1 et C2 tiennent, issue A) ; [R1b] l. 5 et 18 (Qwen2.5-72B-Instruct, les 1 200 réponses ; issue A) ; [R2] l. 11-12 (critique g = 0,625 [0,569 ; 0,680] ; éloge g = 0,137 [0,029 ; 0,242]) ; l. 14 (« C1 (attraction) holds; C2 (two destinations) holds », issue A) ; l. 18 (« Under praise the rating barely moves ») ; l. 31 (« Two destinations are therefore not robustly established in the model's own rating » ; le verdict préenregistré reste celui de la course) | **exact**. Nuance : « shows it » s'appuie sur l'issue préenregistrée A ; que les deux destinations ne soient pas robustes (perdues sous une autre implémentation) n'est dit qu'à travers « barely under praise » |
| 10 | « Dropping them changes neither outcome, though both destination shifts then become undetectable. » | [R4] l. 41, 47 et 49 (variante (c), sans les cinq items à refus : C1 à C4 tiennent, issue A) ; [R6] l. 59-60 (sans les 14 items à refus : « The outcome is still C ») ; [R6d] l. 5 (critique : ĉ(fort) − ĉ(doux) = +0,170 [−0,488 ; 0,714]) ; l. 6 (éloge : −2,339 [−13,918 ; 9,101]) ; l. 7 (« H2_per_arm={'critical': True, 'praise': None} ») ; l. 8 (issue C) | **exact** ; correction facultative n° 5 de [VPM2] appliquée |

Contradictions internes : aucune. Les n° 8 et 10 se tiennent : « both destinations moved » et « neither arm shifted » valent avec les refus. Sans eux, les destinations ne bougent plus de façon détectable (n° 10), et les deux bras baissent à la dose forte, ce que l'incise du n° 8 laisse entendre sans le dire. Liens : aucun dans les trois phrases.

## 7. Scheurer (`scheurer/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 11 | « I predicted a size trend under both notes; it appeared only under the negative one: at standard intensity, the deference gain (0 means no attraction) shifts −0.19 (95% CI −0.24 to −0.11) per tenfold increase in parameters, items resampled, not models. » | [R7a] l. 33 (M3 : à l'intensité standard, l'intervalle de la pente de g sur log10(taille) exclut 0 « in both arms » ; signe non prédit) ; l. 36 (issue A = M1 et M3) ; [R7] l. 5 (« not the predicted A » ; « falls by 0.19 per decade of parameters (95 % CI [−0.24, −0.11]) ») ; l. 11 (« with a shared item bootstrap ») ; l. 16 (« attraction = the interval lies above 0 ») ; l. 32 (−0,190 [−0,241 ; −0,114]) ; l. 38 (« The trend exists under the down note only ») | **exact**. Les deux réserves de [VPM2] n° 50 sont levées : g = 0 donne Δ = 0 pour tout item, donc aucune attraction ; « shifts −0.19 » n'a plus de double négation. Accord avec la phrase suivante : le 72 milliards a un gain presque nul, mais ses lectures bougent ([R7] l. 45, régime de décalage) |

Contradictions internes : aucune. Liens : aucun dans la phrase.

## 8. Colognese et Ward, question 2 (`colognese-ward-q2/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 12 | « Yet silent hacks were caught 16% of the time overall, against 91% for genuine reasoning and roughly 50–65% for motivated reasoning. » | [CW] §3.3 (« Silent hacks, where the reasoning never mentions the hack, were caught only 16% of the time (n = 1,955; 95% CI 15–18%) » ; « 91% for genuine reasoning (bands 1 and 2; n = 6,649; 95% CI 90–92%) ») ; note 1, « Corrections (14th Oct 2026) » : « roughly 50–65%, not 52% », estimation qui « rests on fewer than 250 rollouts » ; « Silent hacks are still caught about 16% of the time, against about 91% for genuine reasoning » ; [RC] F1 (16 % et 91 %, « même ordre après correction ») | **exact** (transcription). Nuance : après correction, les auteurs écrivent « about 16% » et « about 91% » ; la phrase garde les chiffres du §3.3, que la note confirme |

Contradictions internes : aucune (« The 16-versus-91 gap » suit). Liens : aucun dans la phrase.

## 9. Colognese et Ward, question 1, variante courte (`colognese-ward-q1/reponse-variante-courte-v1.md`)

Aucune phrase « + » : une phrase retirée (« I would test a learned note: … »). Le texte restant se lit sans renvoi orphelin, répond encore aux deux volets de la question (l. 164) et n'a aucune contradiction. Le plan retiré reste détaillé en question 2 : la répétition M11 de [CF] est levée. Comptes de mots : voir la section suivante.

## 10. Feng et Jang (`jang-feng/reponse-v3.md`)

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 13 | « My comparison of probes with black-box judges on these actions is preregistered; its full run will be posted, null or not. » | [R1p] l. 3 (« The result, whatever its sign, will be posted on this page ») ; l. 7 (« On the 2,400 scored actions of the programme's first test on real activations … do probes … detect the saboteur's actions better than small black-box LLM judges (3 and 8 billion parameters) and a simple cost rule ») ; l. 11-17 (trois analyses scellées avant les données, empreintes publiques, textes rendus publics avec le résultat) ; l. 21-23 (rejeu arrêté par sa garde de fidélité ; « a single rerun of R1 on the complete table » ; « the result is posted here, null or not ») | **exact** : aucune trace de lecture interne. Réserve : « these actions » renvoie aux 2 400 actions de P3, au paragraphe précédent. Placé juste après le test de transfert proposé (« next to black-box judges »), il peut se lire « ce test-là est préenregistré », ce qui serait faux |

Contradictions internes : aucune. Le retrait de l'étiquette « R1 » ôte la confusion avec le R1 de `sycophancy-psychophysical-law`, lié dans la même réponse (M6 de [CF]). Liens : aucun dans la phrase.

## Liens et résultats internes

- **Liens des phrases « + »** (n° 2, 3, 4) : tous vers des pages publiques existantes.
  - Dépôt cloné, commit présent, fichier ou dossier présent à ce commit.
  - Branche distante au même commit à 16:31 UTC.
  - Visibilité publique : page `blob/` servie à un visiteur non connecté pour les trois commits ; `gh api` en plus pour `ideation-organism`.
  - Les deux liens de Heimersheim Q2 n'ont pas `https://` : sans effet si le champ est en texte brut.
- **Résultats internes du programme de contrôle : aucune trace** dans les 13 phrases « + », ni dans le reste des dix versions finales.
  - Recherche, insensible à la casse : « v9 », « v8 », « 0.105 », « fatal », « overnight », « partial », « inconclusive », « G0 », « G1 », « gate », « internal », « private », « unpublished », « validation », « banc-tricheurs », « rerun », « replay », « GO_ », « USD », « $ ».
  - Seules occurrences, toutes hors des phrases « + » ou bénignes :
    - la validation v8 publique du 1er novembre (Kirchner 1, phrase inchangée) ;
    - « A clean rerun of the attack is preregistered » (Kirchner 1, inchangée) : le préenregistrement est public, au commit `4848ad9`, ancêtre de `faff48b` ;
    - « replay » (Kirchner 2), un plan ;
    - « private » (Scheurer), le corpus du plan ;
    - « about $3 of GPU » (Scheurer), [R7] l. 12 ;
    - « privately told » (Feng et Jang), le dispositif de P3.
  - Aucun nombre non public du D36 original (68 %, 1 %), aucun « < 1 % » ; ρ = 0,684 n'apparaît que dans Heimersheim Q2, avec sa réserve et son lien public, jamais fusionné avec le « 1 % ».
- **Clone local à surveiller** : `/home/claude/ideation-organism` porte toujours deux éléments non suivis, `resultats/banc-tricheurs-v9-validation-v1/` (résultats internes du nul v9) et `orchestrator/prereg/couples-contre-lecture-juges-idees-v2-v3.json`. Je ne les ai pas ouverts. Rien n'est commité ni poussé, mais un ajout large les publierait.

## Comptes de mots (hors verdict)

Texte situé au-dessus de la ligne `---`, compté par mon script selon quatre découpages : blancs ; blancs, tirets et barres obliques ; suites de caractères de mot (`\w+`) ; suites alphanumériques. Mes comptes par blancs sont égaux à ceux des notes du directeur pour les dix versions finales.

| réponse | limite | blancs | blancs, tirets, barres | `\w+` | alphanumérique |
|---|---|---|---|---|---|
| Heimersheim Q2, v2 (liens racine) | **150** | 133 | 147 | 150 | 149 |
| **Heimersheim Q2, v3 (liens épinglés)** | **150** | 133 | **155** | **159** | **164** |
| Colognese et Ward Q1, v3 | **200** | 198 | 215 | 225 | 225 |
| **Colognese et Ward Q1, variante courte** | **200** | 179 | 194 | **203** | **203** |
| Kirchner Q1 v3 | aucune | 423 | 444 | 451 | 451 |
| Kirchner Q2 v3 | aucune | 451 | 471 | 497 | 497 |
| Ibrahim Q1 v4 | aucune (visée 450) | 434 | 453 | 463 | 469 |
| Ibrahim Q1, variante v3 | aucune (visée 450) | 459 | 489 | 509 | 514 |
| Ibrahim Q2 v3 | aucune (visée 300) | 299 | 313 | 323 | 319 |
| Scheurer v3 | aucune (visée 500) | 500 | 535 | 560 | 560 |
| Colognese et Ward Q2 v3 | aucune (visée 300) | 299 | 308 | 316 | 316 |
| Feng et Jang v3 | aucune | 507 | 568 | 597 | 595 |

- **Heimersheim Q2** : « sans mot de plus » ne vaut que pour un compteur qui découpe sur les blancs. Les liens épinglés ajoutent 8 à 15 unités pour tout compteur qui découpe aussi sur les barres, les tirets ou la ponctuation ; la v3 passe alors au-dessus de 150 (155 à 164), alors que la v2 était à la limite (147 à 150).
- **Variante courte de Colognese et Ward Q1** : sous 200 par blancs (179) et par blancs, tirets et barres (194), mais 203 pour un compteur alphanumérique, comme la note du directeur le dit déjà.

## Corrections minimales

**Obligatoires : aucune.** Aucune phrase inexacte, aucune plus forte que sa source, aucun résultat non publié présenté comme publié, aucun lien mort, aucune trace interne.

Facultatives, une ligne chacune :
1. n° 13 (Feng et Jang) — « on these actions is preregistered » → « on P3's actions is preregistered » ; raison : l'antécédent est au paragraphe précédent, et la phrase peut se lire comme un préenregistrement du test de transfert ; source : [R1p] l. 7 ; compte : 0 mot par blancs.
2. Heimersheim Q2 (n° 3 et 4, liens) — aucun changement de texte ; avant l'envoi, coller la v3 dans le champ du site et lire son compteur. S'il dépasse 150, il découpe sur la ponctuation : revenir aux liens racine de la v2 (147 à 150, encore à la limite) ou retirer une quinzaine de mots ; source : formulaire l. 24 ; section « Comptes ».
3. Colognese et Ward Q1, variante courte — aucun changement de texte ; même essai dans le champ (limite 200, l. 164) : 203 si le compteur est alphanumérique.
4. n° 4 (Heimersheim Q2) — « not yet run » : à relire sur `STATUS.md` juste avant 23:00 UTC ; si R9 a démarré, « running » ; source : [ST] l. 29, 31 et 54.

## Décompte par verdict (13 phrases « + »)

| verdict | nombre | phrases |
|---|---|---|
| exact | 12 | 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13 |
| inexact | 0 | — |
| non vérifiable | 0 | — |
| non publié présenté comme publié | 0 | — |
| plus fort que sa source | 0 | — |
| hors champ (raisonnement) | 1 | 5 |

- **54 affirmations vérifiées, toutes exactes.** Par phrase, de 1 à 13 : 3, 8, 4, 7, 0, 2, 4, 6, 5, 3, 6, 3, 3.
- **Dont au niveau « transcription »** (lecture web, non opposable dans un papier) : n° 7 et 12.
- **Nuances**, sans effet sur le verdict : n° 2 (« independent » = cas bien spécifié) ; n° 3 (adresse `tree/` non lisible par l'outil, commit public) ; n° 4 (statut à revoir avant l'envoi) ; n° 6 (refus pas tous notés 3 ; grille du juge non publiée) ; n° 9 (deux destinations non robustes dans la note propre) ; n° 12 (« about » dans la correction) ; n° 13 (antécédent de « these actions »).
- **Autres contrôles** : contradictions avec une autre phrase de la même réponse, 0 ; liens des phrases « + », 3 sur 3 publics ; traces de résultats internes, 0.
- **Symétrie** (règle gelée R4 du dépôt, à ne pas confondre avec la suite R4). Un relevé sans inexactitude est « propre » : j'ai donc repris à la source primaire, par des questions distinctes, les points les plus exposés :
  - la conception des suites de l'attaque (la première tentative voit-elle un verdict ?) ;
  - la loi honnête de référence et la cellule à écart type sous-estimé de T0.3 ;
  - la section de robustesse de R2 ;
  - les deux sorties de R6 sans refus ;
  - les notes des refus ;
  - la note 1 et le §3.3 du billet ;
  - SocioT Warmth et les conditions du papier ;
  - la page de R1 ;
  - la visibilité des trois liens.

  Il en sort les nuances ci-dessus, aucune erreur.

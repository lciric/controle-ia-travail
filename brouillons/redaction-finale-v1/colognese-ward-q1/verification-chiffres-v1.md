# Vérification des chiffres — réponse à la question 1 de Paul Colognese et Francis Rhys Ward — v1

Vérificateur neuf : je n'ai écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Travail du 3 novembre 2026, de 12:50 à 13:00 UTC environ (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-chiffres-colognese-ward-q1-v1.md`, sha256 `2d1e0504aeebff3fe83d6d1b7d90e4f51d0eb2656318cc416802bd5ff941298b` (vérifiée avant de commencer).

**Fichiers vérifiés** (empreintes égales à celles de la consigne, recalculées avant lecture) :
- réponse : `brouillons/redaction-finale-v1/colognese-ward-q1/reponse-v1.md`, `dc7d6ac9cb48ecbcecbfc895188aebd0fd10fae9afc0a601b0b06535ff910188` (lignes 1 à 7 ; 196 mots par `wc -w`, limite 200) ;
- registre du rédacteur : `…/registre-affirmations-v1.md`, `7a4d40e03bce0e27dfc5d5095e14ba160183800b0d68091602176a49f0c27fa1`.
- Question (texte exact) : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (`57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`), ligne 164 : « Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words) * » ; mentors ligne 163.

## Sources (abréviations)

Clone public frais `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, tête `b3ecaec`, lu sans exécuter aucun code du dépôt (lectures de fichiers, `git show`, `git ls-tree`). `SHA256SUMS` du dépôt : `cc3ed4030bfdb340c14078a42d04fed5bb8417d5d1420bd56f0ebf8c41e2aee7` ; chaque empreinte ci-dessous y est égale à la ligne indiquée.

| abréviation | fichier | sha256 | ligne de `SHA256SUMS` |
|---|---|---|---|
| [R7] | `results/R7/README.md` (identique à `9f5bf6a`, `e5e960b`, `b3ecaec`) | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` | 218 |
| [ADD] | `preregistrations/2026-11-02_addendum_R7_monitor_deference.md` | `4cc54a84f3960294b00f7222f28af890529a586926faae0d52aefb5e27160974` | 34 |
| [SORTIE] | `results/R7/R7_monitor_output.txt` (où l'issue se décide) | `fb15a4edff4632bd0f3f2c7acd089d8d8d16349f86089015884f5d595c99858e` | 217 |
| [DESC] | `results/R7/R7_descriptive.json` | `6be670114cd509bbfc9bf7bc2cfc1cefa0bfe80242596a8f414c4280990427d8` | 214 |
| [72-douce] | `results/R7/R7_72B_mild_output_items30_K20.txt` | `e4e059480b04530374c32b012e8299813cd72d00b3f566769945db639afd4c76` | 198 |
| [72-std] | `results/R7/R7_72B_standard_output_items30_K20.txt` | `87ad14ba179905873387e5c90a0a63d47c40fe10ad7b556420ee5a4cb4f4a9dd` | 201 |
| [72-forte] | `results/R7/R7_72B_strong_output_items30_K20.txt` | `304fe1f9ba940b6c7d13ff3356306b8b8ce6ff106f974aab2d2f6ba4303c9d72` | 204 |
| [1.5-forte] | `results/R7/R7_1.5B_strong_output_items30_K20.txt` | `124ee833895f7231d4da403b44b188ac22be5701815c3a49347e99aefb647f09` | 168 |
| [3-forte] | `results/R7/R7_3B_strong_output_items30_K20.txt` | `ee4d702914e1cb87fb950eaa7810f3dd32c89eb028a114666f6980ca3fab1cc6` | 195 |
| [32-forte] | `results/R7/R7_32B_strong_output_items30_K20.txt` | `ba61410ad0348b044380561648b7aac06644dad6763c44b2649ec403b0a14516` | 186 |
| [LISEZ] | `README.md` du dépôt | `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` | 5 |
| [ÉTAT] | `STATUS.md` | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` | 6 |
| [BILLET] | billet des mentors, LessWrong `2maYXkEgnfJHPAkxh`, « Character training can mitigate reward hacking, but can also make it harder to detect », Paul Colognese et Francis Rhys Ward, 28 septembre 2026 : relu par moi en `WebFetch` le 3 novembre vers 12:52 UTC ; concordant avec [RAPPORT] `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` (`cf1edec99be3ecd54a2d09b1c6c1c3931de6ca1a03e47cbbccde58e03f65b395`) et [RECOUP] `…/recoupement-v1.md` (`bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a`) | — | — |
| [FABLE] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` (`4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96`), §7 (b) : phrase R7 vérifiée par la lectrice, concordante avec les n° 15 à 18 et 28 à 30 ; ses autres corrections (ρ, « < 1 % », D36, R6) ne touchent pas cette réponse | — | — |

Commits du clone (heure de l'auteur, convertie en UTC) : `d748e23` « Preregister R7 », 2 novembre 14:55 ; `9d2a280` (version v2026.11.4), 18:12 ; `ad64b72` « DOI of v2026.11.4; R7 running », 18:38 ; `9f5bf6a` « R7 results », 20:56 ; `e5e960b`, 21:12.

## Tableau

| n° | phrase (mots exacts de la réponse) | source et emplacement | verdict |
|---|---|---|---|
| 1 | « I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. » | [ADD] l. 3 (auteur Lazar Ciric), l. 10 (la question : un gain vers une destination fixée par une note dans ce que lit le moniteur, et sa dépendance à la taille), l. 15 (la note dans la même case que la réponse, « so that the monitor reads it as part of the content it judges »), l. 33 (signe de la tendance de taille non prédit) | **exact** — « whether size protects » est posé en question, conforme à l. 33 ; exécution par des agents sous ses règles (formulaire l. 158) |
| 2 | « Seven Qwen2.5-Instruct monitors » | [R7] l. 8 ; [SORTIE] l. 1 | **exact** |
| 3 | « (0.5B–72B) » | [R7] l. 8 (0,5 ; 1,5 ; 3 ; 7 ; 14 ; 32 ; 72 milliards) | **exact** |
| 4 | « scored 600 » | [R7] l. 9 (les 600 réponses sans pression publiées de la campagne 1, items 0 à 29, k = 0 à 9, deux bras) ; [ADD] l. 16 | **exact** |
| 5 | « Llama-3.1-8B-Instruct assessments » | [LISEZ] l. 9 (« Llama-3.1-8B-Instruct is asked for its assessment of a text ») et l. 75 | **exact** |
| 6 | « plain and with a note appended claiming a negative or positive verdict » | [R7] l. 9 ; [ADD] l. 15 et tableau des notes l. 17 à 23 | **exact** |
| 7 | « at three intensities (claim, request, order naming the score) » | [R7] l. 9 ; [ADD] l. 21 à 25 (affirmation attribuée à l'auteur ; affirmation avec demande ; « You must score it 1 / 5 ») | **exact** — l'addendum déclare que les intensités diffèrent aussi de nature et de longueur (l. 25) |
| 8 | « Preregistered » | [ADD] ; [R7] l. 3 | **exact** |
| 9 | « archived before any reading » | [R7] l. 3 (Zenodo 10.5281/zenodo.23892810, 2 novembre 2026, 18:30 UTC) ; [ÉTAT] l. 25 (lancé de 19:37 à 21:02 heure de Paris, soit 18:37 à 20:02 UTC) ; commit `ad64b72` « R7 running » à 18:38 UTC | **exact** sur déclaration publique et chronologie publique cohérente. Limite : la notice Zenodo n'a pu être ouverte (zenodo.org refusé par le mandataire de la session, doi.org hors liste de `WebFetch`) ; les heures de lecture sont déclarées, le dépôt de transport est privé ; [ÉTAT] l. 42 signale une horloge en avance sur une machine |
| 10 | « analysed with my sycophancy law » | [R7] l. 11 (la loi d'attraction de `analyse_runs.py`, lectures nues en référence, lectures avec note en pression) ; [LISEZ] l. 5 (auteur) | **exact** |
| 11 | « item means close a fraction g of their distance to a destination » | [LISEZ] l. 9 à 11 (Δ = p₁ − p₀ = g·(ĉ − p₀), moyennes par item) | **exact** |
| 12 | « I predicted every size would defer » | [ADD] l. 31 (M1 : à l'intensité standard, g > 0 dans les deux bras à toutes les tailles) et l. 36 (A = M1 et M3) ; [R7] l. 5 (« not the predicted A ») | **exact** — l'issue A demandait aussi M3, également fausse ([R7] l. 38) |
| 13 | « wrong, outcome C » | [SORTIE] l. 11 et 12 (M1 = False ; « outcome: C ») ; [R7] l. 5 | **exact** |
| 14 | « published as such » | [LISEZ] l. 100 (« Outcome C, reported as such ») ; page [R7] publique au commit lié (n° 32) | **exact** |
| 15 | « At standard intensity, two sizes deferred both ways » | [R7] l. 23, 25 et 36 (7B et 32B) ; [SORTIE] l. 5 et 7 | **exact** |
| 16 | « four one way » | [R7] l. 20 à 22 et 24 (0.5B et 1.5B note négative seule ; 3B et 14B note positive seule) | **exact** — pour 0.5B, la destination n'est pas nettement du côté de la note (exception de M2, [R7] l. 37) ; la réponse suit la colonne « defers » de la page |
| 17 | « the 72B neither » | [R7] l. 26 ; [SORTIE] l. 8 (g = −0,070 [−0,162 ; 0,058] et −0,059 [−0,106 ; 0,001]) | **exact** |
| 18 | « Yet the 72B was pushed, not captured » | [R7] l. 45 ; régime « offset » aux trois intensités ([72-douce], [72-std], [72-forte] l. 5) ; sous la note négative, g = 0,036, −0,070, −0,045 | **exact** — réserve de force : lecture « descriptive, not preregistered » ([R7] l. 43), non signalée dans la réponse (voir corrections). Sous l'ordre de noter 5, le 72B est poussé plus fort (g = 0,393 [0,072 ; 0,673], 81 % de lectures à 5 contre 7 % sans note : [72-forte] l. 3, [DESC]) sans être capté ; la réponse n'en dit rien de faux |
| 19 | « under the order to score 1 » | [ADD] l. 23 (« You must score it 1. ») | **exact** |
| 20 | « 62% of its readings were at 1 » | [DESC] 72B `down_strong_argmax1` = 0,625 ; [R7] l. 45 (« 62 % ») | **exact** tel que publié — valeur exacte 62,5 % (375 sur 600) ; un arrondi au plus proche donnerait 63 % ; « at 1 » = note la plus probable égale à 1 ([DESC], champ « what ») |
| 21 | « against 22% plain » | [DESC] 72B `plain_argmax1` = 0,2217 ; [R7] l. 45 | **exact** |
| 22 | « That order captured 1.5B, 3B and 32B almost completely. » | [R7] l. 44 ; [1.5-forte] g = 0,992 [0,986 ; 0,996] ; [3-forte] g = 0,878 [0,828 ; 0,933] ; [32-forte] g = 0,997 [0,994 ; 1,000] ; [DESC] parts à 1 : 1,0 ; 0,983 ; 1,0 | **exact** — même réserve de force que le n° 18 ([R7] l. 43) |
| 23 | « my monitors scored verdicts, not misbehaviour » | [R7] l. 9 (consigne du juge de la campagne 1) ; [LISEZ] l. 9 (polarité du verdict, de 1 à 5) | **exact** |
| 24 | « without reasoning » | [R7] l. 10 ; [ADD] l. 26 (premier jeton de l'assistant, une seule passe avant) | **exact** |
| 25 | « your anti-cheating seed 1 » (le billet est le leur ; le caractère et la graine existent sous ces noms) | [BILLET] en-tête (auteurs Paul Colognese et Francis Rhys Ward, 28 septembre 2026) ; graines du caractère « anti-cheating » numérotées 1, 2, 3 ; [RAPPORT] l. 15 | **exact** |
| 26 | « 's comment presenting the hack as harmless » | [BILLET] Summary : « 89% added a comment to its answer that presents the hack as harmless », rapporté à la graine anti-triche 1 ; §3.3 : « Its hacks were primarily simple test overrides, often accompanied by a misleading comment » (triche dominante « check = lambda f: None ») ; [RAPPORT] l. 35 et F1 l. 65 ; [RECOUP] n° 208, l. 300 | **exact** — niveau transcription (`WebFetch` rend des citations courtes par un modèle intermédiaire), trois lectures concordantes ; aucun chiffre du billet dans la réponse. « learned note » : commentaire produit par le modèle entraîné, non planté ; qualification cohérente avec le billet |
| 27 | « And more model families » (prémisse : une seule famille de moniteurs dans R7) | [ADD] l. 10 (« one monitor family ») ; [R7] l. 8 | **exact** |
| 28 | « my size trend in g (−0.19 per tenfold size » | [SORTIE] l. 9 (pente par décade, note négative, intensité standard : −0,190) ; [R7] l. 32 | **exact** |
| 29 | « [−0.24, −0.11] » | [SORTIE] l. 9 ([−0,241 ; −0,114]) | **exact** |
| 30 | « standard negative note) » | [SORTIE] l. 9 (« trend critical … standard ») ; [ADD] l. 28 (bras critique = note négative) | **exact** — la réponse ne prétend pas M3 (fausse) ; note positive : −0,019 [−0,098 ; 0,063] ([R7] l. 33) |
| 31 | « bootstraps items, not models » | [ADD] l. 29 (un seul tirage avec remise des items, partagé par tous les moniteurs, B = 10 000) ; [R7] l. 11 | **exact** |
| 32 | lien « https://github.com/lciric/sycophancy-psychophysical-law/tree/e5e960b/results/R7 » | clone : commit `e5e960b` présent (`e5e960b497473c4ecd6a502b0e0dc237604d066d`, 2 novembre 2026 22:12:14 +0100) ; `results/R7` à ce commit : 68 fichiers, liste `git ls-tree -r` de sha256 `e92c3a4655756987acafed54685ef291eaf9ca9b2c687759444509d7936cb89b`, identique à `9f5bf6a` et `b3ecaec` ; [LISEZ] l. 104 (v2026.11.5 = `e5e960b`, Zenodo 10.5281/zenodo.23909891) ; `raw.githubusercontent.com` au commit complet, sans identifiants : code 200, `results/R7/README.md` et `R7_descriptive.json` d'empreintes égales au clone (copies dans `/tmp/verif-cw-q1-raw-n7w3Sg/`) | **exact** (public, présent) — limite : la page `github.com/…/tree/e5e960b/…` elle-même n'a pas été ouverte (refus du mandataire de la session : « GitHub access to this repository is not enabled for this session ») ; la résolution de l'empreinte abrégée par GitHub n'est pas testée ici |

Hors décompte (plans, au conditionnel) : « I would put notes beside known hacks, so deference reads as missed detections at a fixed false-alarm rate. » ; « I would test a learned note: delete … and re-score. » ; « And more model families » (le souhait ; sa prémisse est le n° 27).

## Corrections minimales

**Aucune correction d'exactitude n'est requise.** Deux précisions, au choix de Lazar :
1. *Recommandée (force du résultat)* : « Yet the 72B was pushed, not captured: » → « Yet, descriptively, the 72B was pushed, not captured: » ; raison : les parts de lectures à 1 (62 %, 22 %) et la « capture » sous l'ordre (n° 18 à 22) viennent de la section « Reading (descriptive, not preregistered) », alors que la phrase qui précède dit « Preregistered » ; source [R7] l. 43 à 45, [DESC] ; coût : +1 mot (197).
2. *Facultative (arrondi)* : « 62% » → « 62.5% » ; raison : valeur exacte 0,625, qu'un lecteur qui recalcule arrondirait à 63 % ; source [DESC] 72B `down_strong_argmax1` ; coût : 0 mot. La page publique écrit « 62 % » : la réponse actuelle lui est fidèle.

Hors de la réponse, à signaler à Fable (pages publiques ; la réponse ne les reprend pas) :
- [R7] l. 46, « the size trend is strongest where the note is an order » : la pente est −0,190 [−0,241 ; −0,114] à l'intensité standard (une demande) et −0,164 [−0,237 ; −0,065] sous l'ordre (forte) ; la tendance est la plus marquée à l'intensité standard ([SORTIE] l. 9 ; [R7] l. 32).
- [LISEZ] l. 100, « g ≈ 0 at every intensity » pour le 72B « in either direction » : faux sous l'ordre de noter 5 (g = 0,393 [0,072 ; 0,673], [72-forte] l. 3) ; déjà relevé par le rédacteur (registre l. 65).

## Décompte

- 32 lignes : **32 exactes**, **0 inexacte**, **0 non vérifiable**, **0 non publiée présentée comme publiée**.
- Réserves : n° 9 (horodatage Zenodo non consulté, déclaration publique seulement) ; n° 18 et 22 (lecture descriptive non signalée, correction 1) ; n° 20 (62,5 % arrondi à 62 %, correction 2) ; n° 26 (niveau transcription) ; n° 32 (page github.com non ouverte, contenu public vérifié par `raw.githubusercontent.com`).
- Le registre du rédacteur (20 lignes, 18 publiques et vérifiées, 2 propositions) est confirmé ligne à ligne ; aucune de ses sources n'a d'empreinte différente.

## Méthode et écarts

- Aucun code des dépôts exécuté ; aucune écriture hors de ce fichier et de deux dossiers temporaires sous `/tmp/` (copies publiques téléchargées, dont une tentative Zenodo vide) ; aucun `git fetch` ; rien sous `donnees/` ni `/home/claude/coffre-*`.
- `WebFetch` (billet des mentors) passe par un modèle intermédiaire ; il est explicitement prévu par la consigne pour les sources primaires.
- Écart mineur : deux lectures JSON en une ligne (`python3 -I -c`, lecture seule de [DESC] et tentative Zenodo) ont été lancées sans `nice -n 10` ; sans effet sur les résultats.

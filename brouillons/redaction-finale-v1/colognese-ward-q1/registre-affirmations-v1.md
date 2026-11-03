# Registre des affirmations — réponse à la question 1 de Paul Colognese et Francis Rhys Ward — v1

Rédacteur neuf (aucune version antérieure des réponses de Lazar écrite par moi). Travail du 3 novembre 2026, de 12:23 à 12:50 UTC environ (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-colognese-ward-q1-v1.md`, sha256 `e3f0b3152addd42b5ee0c2ac8327a0d65baa7a9aa8f1eaef847ca190f2403c71` (vérifiée avant de commencer, égale à son compagnon).

Réponse enregistrée : `brouillons/redaction-finale-v1/colognese-ward-q1/reponse-v1.md`, sha256 `dc7d6ac9cb48ecbcecbfc895188aebd0fd10fae9afc0a601b0b06535ff910188` (lignes 1 à 7 ; 196 mots comptés par espaces).

## Forces

- **publique et vérifiée** : relue par moi sur un fichier public (clone frais en lecture seule) dont l'empreinte est égale à celle que le dépôt publie dans `SHA256SUMS`, ou sur la page des mentors relue par deux lecteurs neufs ;
- **interne vérifiée** : fichier daté du dépôt privé, chemin et sha256 (aucune dans cette réponse) ;
- **non vérifiée** : interdite dans la réponse (aucune) ;
- **proposition** : ce que Lazar ferait ; écrit au conditionnel (« I would »), ce n'est ni un résultat ni un travail fait.

## Sources (abréviations)

Clone public : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, tête `b3ecaec` (3 novembre 2026, 11:35 heure de Paris). Aucun code du dépôt n'a été exécuté ; seules des lectures de fichiers et d'objets git (`git show`, `git ls-tree`).

| abréviation | fichier | sha256 | ligne de `SHA256SUMS` |
|---|---|---|---|
| [R7-L] | `results/R7/README.md` (identique à `9f5bf6a`, `e5e960b` et `b3ecaec`) | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` | 218 |
| [R7-P] | `preregistrations/2026-11-02_addendum_R7_monitor_deference.md` | `4cc54a84f3960294b00f7222f28af890529a586926faae0d52aefb5e27160974` | 34 |
| [R7-S] | `results/R7/R7_monitor_output.txt` (sortie de l'analyse gelée, où l'issue se décide) | `fb15a4edff4632bd0f3f2c7acd089d8d8d16349f86089015884f5d595c99858e` | 217 |
| [R7-D] | `results/R7/R7_descriptive.json` | `6be670114cd509bbfc9bf7bc2cfc1cefa0bfe80242596a8f414c4280990427d8` | 214 |
| [72-std] | `results/R7/R7_72B_standard_output_items30_K20.txt` | `87ad14ba179905873387e5c90a0a63d47c40fe10ad7b556420ee5a4cb4f4a9dd` | 201 |
| [72-fort] | `results/R7/R7_72B_strong_output_items30_K20.txt` | `304fe1f9ba940b6c7d13ff3356306b8b8ce6ff106f974aab2d2f6ba4303c9d72` | 204 |
| [1.5-fort] | `results/R7/R7_1.5B_strong_output_items30_K20.txt` | `124ee833895f7231d4da403b44b188ac22be5701815c3a49347e99aefb647f09` | 168 |
| [3-fort] | `results/R7/R7_3B_strong_output_items30_K20.txt` | `ee4d702914e1cb87fb950eaa7810f3dd32c89eb028a114666f6980ca3fab1cc6` | 195 |
| [32-fort] | `results/R7/R7_32B_strong_output_items30_K20.txt` | `ba61410ad0348b044380561648b7aac06644dad6763c44b2649ec403b0a14516` | 186 |
| [L] | `README.md` du dépôt | `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` | 5 |
| [ÉTAT] | `STATUS.md` | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` | 6 |
| [BILLET] | billet des mentors, LessWrong `2maYXkEgnfJHPAkxh` (28 septembre 2026, corrigé le 14 octobre), lu par deux lecteurs neufs : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` (`cf1edec99be3ecd54a2d09b1c6c1c3931de6ca1a03e47cbbccde58e03f65b395`) et `…/recoupement-v1.md` (`bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a`) ; repris par `brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md` (`7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2`) | — | — |

## Affirmations, phrase par phrase

| n° | mots exacts de la réponse | source et emplacement | force | remarque |
|---|---|---|---|---|
| 1 | « I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. » | [R7-P] §7, l. 10 (la question : un gain vers une destination fixée par une note dans ce que lit le moniteur, et sa dépendance à la taille) ; §8, l. 15 (la note suit la réponse dans la même case, « so that the monitor reads it as part of the content it judges ») | publique et vérifiée | « I » : l'addendum a Lazar pour auteur (l. 3) ; l'exécution est faite par des agents sous ses règles, comme le dit sa réponse générale (formulaire l. 158) |
| 2 | « Seven Qwen2.5-Instruct monitors (0.5B–72B) » | [R7-L] l. 8 ; [R7-S] l. 1 | publique et vérifiée | |
| 3 | « scored 600 Llama-3.1-8B-Instruct assessments » | [R7-L] l. 9 (les 600 réponses publiées sans pression de la campagne 1) ; [R7-P] l. 16 ; [L] l. 9 (Llama-3.1-8B-Instruct donne son évaluation d'un texte) et l. 75 | publique et vérifiée | |
| 4 | « plain and with a note appended claiming a negative or positive verdict » | [R7-L] l. 9 ; [R7-P] l. 15 et tableau des notes l. 17 à 23 | publique et vérifiée | |
| 5 | « at three intensities (claim, request, order naming the score) » | [R7-L] l. 9 ; [R7-P] l. 25 (affirmation attribuée à l'auteur ; affirmation avec demande ; ordre qui nomme la note) | publique et vérifiée | l'addendum déclare que les trois intensités diffèrent aussi de nature et de longueur (confusion déclarée) ; non repris faute de place |
| 6 | « Preregistered, archived before any reading » | [R7-L] l. 3 (Zenodo 10.5281/zenodo.23892810, 2 novembre 2026, 18:30 UTC) ; [ÉTAT] l. 25 (archivé à 18:30 UTC ; lectures de 19:37 à 21:02, heure de Paris) | publique et vérifiée | vérifiée sur le dépôt ; l'horodatage de Zenodo lui-même n'a pas été consulté (pas de `WebFetch` hors faits des mentors) |
| 7 | « analysed with my sycophancy law: item means close a fraction g of their distance to a destination. » | [R7-L] l. 11 (la loi d'attraction de `analyse_runs.py`, lectures nues comme référence, lectures avec note comme pression) ; [L] l. 9 à 11 (Δ = g·(ĉ − p₀), moyennes par item) | publique et vérifiée | « my » : [L] l. 5 (auteur Lazar Ciric) |
| 8 | « I predicted every size would defer: wrong, outcome C, published as such. » | [R7-L] l. 5 (« Outcome: C, not the predicted A ») ; [R7-P] l. 31 (M1 : déférence à toutes les tailles, intensité standard, dans les deux sens) et l. 36 (A = M1 et M3 ; C = non M1) ; [R7-S] l. 12 | publique et vérifiée | l'issue A prédite comprenait aussi une tendance de taille (M3, signe non prédit) ; la phrase nomme la partie dont l'échec fait l'issue C |
| 9 | « At standard intensity, two sizes deferred both ways, four one way, the 72B neither. » | [R7-L] l. 36 (ligne M1 : 7B et 32B dans les deux sens ; quatre dans un seul ; le 72B dans aucun) et tableau l. 18 à 26 | publique et vérifiée | |
| 10 | « Yet the 72B was pushed, not captured » | [R7-L] l. 45 (« The 72B is not captured, but it is pushed ») ; [72-std] (régime « offset » dans les deux sens) | publique et vérifiée | voir plus bas : sous l'ordre positif, le 72B montre une attraction partielle (g = 0,393) ; la réponse ne dit rien de ce bras |
| 11 | « under the order to score 1, 62% of its readings were at 1, against 22% plain. » | [R7-L] l. 45 ; [R7-D] 72B : `down_strong_argmax1` = 0,625 ; `plain_argmax1` = 0,2217 | publique et vérifiée | « at 1 » = note la plus probable à 1 ; 0,625 arrondi à 62 % comme le fait la page publique |
| 12 | « That order captured 1.5B, 3B and 32B almost completely. » | [R7-L] l. 44 (g de 0,88 à 1,00 ; 98 à 100 % des lectures à 1) ; [1.5-fort] g = 0,992 ; [3-fort] g = 0,878 ; [32-fort] g = 0,997 ; [R7-D] parts à 1 : 1,0 ; 0,983 ; 1,0 | publique et vérifiée | |
| 13 | « my monitors scored verdicts, not misbehaviour » | [R7-L] l. 9 (la consigne du juge de la campagne 1) ; [L] l. 9 (le juge note la polarité du verdict, de 1 à 5) | publique et vérifiée | |
| 14 | « without reasoning » | [R7-L] l. 10 (r = Σ k·p(k) sur les jetons « 1 » à « 5 », premier jeton de l'assistant, une seule passe avant) | publique et vérifiée | |
| 15 | « I would put notes beside known hacks, so deference reads as missed detections at a fixed false-alarm rate. » | — | proposition | niveau méthode : la note est décrite par sa classe et son rôle de mesure ; aucun mode d'emploi |
| 16 | « your anti-cheating seed 1's comment presenting the hack as harmless » | [BILLET] Summary (« 89% added a comment to its answer that presents the hack as harmless ») et §3.3 ; rapport l. 35 et F1 l. 65 ; recoupement n° 208, l. 300 (« exact ») ; pièce mentor l. 58 | publique et vérifiée | lecture par `WebFetch` (citations de 125 caractères au plus) : niveau transcription, mais deux lecteurs neufs concordent ; aucun chiffre du billet n'est repris dans la réponse |
| 17 | « delete [it] … and re-score » | — | proposition | une intervention sur leurs transcriptions, pas une comparaison entre réponses avec et sans commentaire (qui serait confondue) |
| 18 | « my size trend in g (−0.19 per tenfold size [−0.24, −0.11], standard negative note) » | [R7-L] l. 32 ; [R7-S] l. 9 (pente par décade à l'intensité standard : −0,190 [−0,241 ; −0,114]) | publique et vérifiée | à l'intensité forte : −0,164 [−0,237 ; −0,065] ; à la douce : −0,004 [−0,034 ; 0,031] ; sous la note positive, aucune pente décelable |
| 19 | « bootstraps items, not models » | [R7-P] l. 29 (intervalle percentile d'un seul tirage avec remise des items, partagé par tous les moniteurs, B = 10 000) ; [R7-L] l. 11 | publique et vérifiée | sept points de contrôle d'une seule famille : l'intervalle ne contient pas la variation d'un modèle à l'autre |
| 20 | « https://github.com/lciric/sycophancy-psychophysical-law/tree/e5e960b/results/R7 » | `e5e960b` présent dans le clone public (2 novembre 2026, 22:12 heure de Paris) ; arbre `results/R7` identique à `b3ecaec` (liste `git ls-tree -r` de même sha256, `e92c3a4655756987acafed54685ef291eaf9ca9b2c687759444509d7936cb89b`, 68 fichiers) ; [L] l. 104 (version v2026.11.5 = commit `e5e960b`, Zenodo 10.5281/zenodo.23909891) | publique et vérifiée | lien épinglé au commit archivé ; la page github.com elle-même n'a pas été ouverte |

## Décompte

- 20 lignes : **18 publiques et vérifiées**, **0 interne vérifiée**, **0 non vérifiée**, **2 propositions** (n° 15 et 17).
- Aucun chiffre du billet des mentors ; aucun fait interne du programme de contrôle ; aucun résultat non concluant ou non publié.

## Écartés de la réponse, et pourquoi

- **« g ≈ 0 at every intensity » pour le 72B** ([L] l. 100) : faux pour l'ordre positif, où le 72B donne g = 0,393 [0,072 ; 0,673] dans le bras « praise » ([72-fort], régime « offset » quand même, faute d'attraction dans les deux bras). [R7-L] l. 45 est exact (« under the down note ») ; la réponse ne parle que de l'intensité standard et de l'ordre de noter 1.
- **ρ = 0,684, « < 1 % », « 68 % », D36** : hors de la piste ; et ρ et le bras « 1 % » sont deux objets distincts (lectrice indépendante, `brouillons/canal-fable-v1/fable_2026-11-03_n001.md`, `4b9bd5c9…`).
- **« your project B »** : page des mentors jamais lue par un lecteur (rapport l. 26, l. 50).
- **R8** (étapes du post-entraînement de Tülu 3) : démarré le 3 novembre à 08:01 UTC ([ÉTAT] l. 29), aucun `results/R8/` dans le clone ; hors de la piste.
- **Comparaison avec leur article sur la détection du sabotage** (moniteurs « manipulés » par des agents qui rationalisent) : lue par un seul lecteur (rapport F9), nom anglais exact de leurs moniteurs non vérifié ; non nécessaire.

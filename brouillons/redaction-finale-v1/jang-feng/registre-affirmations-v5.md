# Registre des affirmations — réponse v5 à Shi Feng et Eyon Jang

Rédacteur neuf, 3 novembre 2026 (heures UTC par `date -u` : début 17:44, réponse écrite 17:54).
Réponse : `brouillons/redaction-finale-v1/jang-feng/reponse-v5.md`. Le sha256 de la réponse seule (texte au-dessus du trait) est écrit dans son pied : `cd4e97591d51c6410c2d43a5238cba9427e4a91eb5fc9b8430df49e05f0e9856`.

Forces : **publique et vérifiée** (lue par moi sur la source primaire, sauf mention) ; **publique, transcription** (lue sur la page arXiv par questions ciblées à un petit modèle : vérifiée, mais non opposable dans un papier au sens de R7) ; **interne vérifiée** (aucune ici) ; **plan ou prédiction** (travail non fait, dit comme tel dans la réponse) ; **opinion** (pas un fait) ; **non vérifiée** : aucune dans la réponse.

## Sources et empreintes

| abréviation | source | empreinte ou version |
|---|---|---|
| [TAY] | Taylor et al., « Auditing Games for Sandbagging », arXiv 2512.07810 v1, `docs/sources/pdf/2512.07810v1.pdf` ; pages = index du PDF | sha256 `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` (vérifiée contre son `.sha256`) |
| [JANG-H] | Jang et al., « Exploration Hacking », arXiv 2604.28182 v1, `https://arxiv.org/html/2604.28182v1`, lu par moi par `WebFetch` (deux questions ciblées, plus la fin de la page à partir du caractère 100 000) | page HTML de 118 306 caractères ; pas de PDF empreinté |
| [PIECE] | `brouillons/ideation-mentors-soir-v1/piece-jang-feng-v1.md` | sha256 `1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774` |
| [RAPP] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-jang-feng-v1.md` | sha256 `1c8a4ff27c6ed9103b012899d0758adbe6b99ef8de9bf0937b11edc4ffde686b` |
| [RECOUP] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` | sha256 `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [P3] | page publique `lciric/ideation-organism`, `resultats/controle-p3-premier-test/README.md`, au commit `7c7b688` (ancêtre de `faff48b` = dernier `origin/main` connu localement ; contenu identique aux deux commits) | sha256 du fichier `2485d5095094c2dc7f761cbe972172c88291305c6da1df50b58c0c3c1272bf88` |
| [A1] | page publique `lciric/ideation-organism`, `resultats/attaque-goodhart-v2/README.md`, au commit `7c7b688` (identique à `66dbcf1`, déjà vérifié public par le recoupement, et à `faff48b`) | sha256 `84d6e77b3b2c6dc6b79640eb48ccce07d4258c70a5943756c49af000ca0609bc` |
| [DOSSIER] | `brouillons/ideation-mentors-soir-v1/dossier-piste-jang-feng-v1.md` (fiche JF-28) | sha256 `eb5e51d5fd4c4aef17cc0e400c1628c39e76b4c553c7396091c6ff92bd859bb8` |

## Affirmations, dans l'ordre de la réponse

| n° | affirmation (mots de la réponse) | source et emplacement | force |
|---|---|---|---|
| 1 | « White-box access is best at getting a hidden capability back, and least proven at telling why it was hidden. » | thèse ; appuyée par les n° 3 à 10 | opinion |
| 2 | « (Taylor et al., arXiv 2512.07810) » | [TAY] p. 1 : liste d'auteurs, sans Feng ni Jang | publique et vérifiée |
| 3 | « imitating a weaker model beat black-box detection » | [TAY] p. 1, résumé : « Black-box approaches were defeated by effective imitation of a weaker model » | publique et vérifiée |
| 4 | « training on a single correct demonstration elicited full performance from the (password-locked) sandbaggers » | [TAY] p. 1, résumé : « consistently elicited full performance … using only a single correct demonstration » ; p. 8 : « Sandbagging model organisms were password-locked » ; réserve des auteurs p. 26 | publique et vérifiée |
| 5 | « Eyon's exploration-hacking paper (arXiv 2604.28182, §4.2), fine-tuning took WMDP-with-tools accuracy from 80.0% to 98.0% in 10 steps » | [PIECE] § 1.2 (Jang premier auteur, [revérifié] ; 80,0 % → 98,0 % en 10 pas, § 4.2, [revérifié]) ; [RAPP] fait 7 ; [RECOUP] n° 128 et 143. Pas de score de départ prêté à l'organisme distillé (objection du lecteur A sur JF-28) | publique, transcription (recoupée par deux lecteurs) |
| 6 | « For capability evaluations, that alone justifies white-box access. » | conséquence des n° 4 et 5 | opinion |
| 7 | « Noise, short fine-tuning and demonstrations can lift unexpressed capability, withheld on purpose or never elicited. » | bruit : [TAY] p. 72, fig. 35 (n° 9) ; entraînement : [TAY] p. 19 (n° 10) | publique et vérifiée (« can » : capacité montrée, pas règle générale) |
| 8 | « call the role of under-elicitation in fuzzing "unclear from our experiments and likely requires follow-up" (p. 13) » | [TAY] p. 13 : « Fuzzing results were more ambiguous than we hoped, possibly due to tracking under-elicitation though this is unclear from our experiments and likely requires follow-up » ; citation de 8 mots | publique et vérifiée |
| 9 | « their post-hoc appendix points the way: noise uplift tracked how under-elicited a model was, locked or unlocked alike (r = 0.74, Fig. 35) » | [TAY] p. 72, annexe C.16, fig. 35 : corrélation entre ξ et la perte de performance par rapport au modèle de base, « similar slopes », « Overall across both conditions, the correlation was r = 0.74 » ; « post-hoc » : p. 4 (« only explored after the game in unblinded conditions ») | publique et vérifiée |
| 10 | « Training also lifted a benign model and the benign reference by 10 points (§6.4.1). » | [TAY] p. 19 : Baobab (bénin) +10 points sur GPQA Diamond CoT ; « benign reference model (Llama-3.1-8B-Instruct) » +10 points sur BBH Other | publique et vérifiée |
| 11 | « the noise control is the same organism with its trigger removed, whose accuracy "steadily declines" (§4.1) » | [JANG-H] § 4.1 « Detection », paragraphe « White-box techniques » : « evaluate each perturbed adapter on BigCodeBench with trigger present (treatment) and absent (control) » ; « As σ increases, control accuracy steadily declines ». Deux questions indépendantes concordent. Non lu : la fin des annexes, dont la figure 37 (organisme WMDP). La phrase dit ce qu'est le témoin, pas ce qui manque. | publique, transcription |
| 12 | « That shows the lock is conditional. » | [JANG-H] § 4.1 : « weight noising similarly reveals the locking mechanism » ; légende de la fig. 7 : « Weight noising detects exploration hacking on BigCodeBench » | publique, transcription (paraphrase) |
| 13 | « But an auditor rarely knows the trigger: the comparison that decides is a model never locked that starts at the same score. » | raisonnement ; cœur de JF-28 ([DOSSIER]) | opinion |
| 14 | « The improvement ratio ξ used in the auditing game is a maximum over noise levels and seeds » | [TAY] p. 71, annexe C.15 : ξ = max sur σ et graines de l'exactitude, divisé par l'exactitude moyenne sans bruit | publique et vérifiée |
| 15 | « a maximum can only grow as draws are added, so a model hiding nothing can score above 1 » | propriété du maximum (le maximum d'un ensemble plus grand est au moins aussi grand) ; « can » : dès que l'exactitude varie d'une graine à l'autre | vrai par construction (raisonnement) |
| 16 | « Its null is a benign model run through the same grid, not 1.0. » | conséquence du n° 15 ; [TAY] p. 22 dit la méthode « difficult to properly calibrate » (on ne leur prête pas d'avoir pris 1,0 pour nul) | opinion (méthode) |
| 17 | « my first preregistered test on real activations (Llama-3.1-8B-Instruct, 2,400 actions) » | [P3] titre ; « 2,400 scored actions » ; préenregistrement scellé avant les données | publique et vérifiée |
| 18 | « the deception probe's interval cleared chance (lower bound 0.53) but not the 0.95 quantile of 200 covariance-matched random probes (0.57) » | [P3], tableau : intervalle à 97,5 % [0,5313 ; 0,6183], quantile 0,95 du plancher 0,5717 ; plancher de 200 sondes aléatoires tirées de N(0, Σ) ; « cleared chance » = arithmétique (0,5313 > 0,5), lecture que les règles gelées ne font pas, donnée seulement pour montrer pourquoi le nul apparié compte | publique et vérifiée |
| 19 | « not detected at this power, and the null does not exclude AUCs below 0.63 » | [P3], issue (« not detected at this power ») et réserve 2 (aire minimale détectable 0,6315), que le verdict exige partout où le nul est cité | publique et vérifiée |
| 20 | « with n tries at α = 0.05, the chance of a false promotion is bounded only by 1 − (1 − α)ⁿ, 0.56 at n = 16 » | [A1] l. 17 : « with n attempts and a stop at the first promotion, the bound is 1 − (1 − α)ⁿ (0.05, 0.185 and 0.560 for n = 1, 4 and 16) » | publique et vérifiée |
| 21 | « both Qwen3-14B recipes of Eyon's paper » | [PIECE] § 1.2 (verrouillage par renforcement § 3.1, distillation par affinage supervisé § 3.2) ; [RECOUP] n° 143 (exact) | publique, transcription |
| 22 | « five never-locked controls fine-tuned on degraded demonstrations to the same starting score (within 2 points), through the same σ grid and seeds, comparing whole accuracy-versus-σ curves at equal σ » | plan de JF-28 ([DOSSIER] : 5 paires, ± 2 points, courbe entière à amplitude égale) ; « What I would run » | plan (non fait) |
| 23 | « since a control merely more fragile to noise would fake a gap » | JF-28, « ce qui rendrait le résultat trompeur » | raisonnement |
| 24 | « My prediction: ξ(organism) − ξ(control) near +0.01, inside ±0.05, both above 1.05. » | JF-28, résultat attendu (+0,01 [−0,04 ; +0,05], les deux au-dessus de 1,05, « supposé ») | prédiction (non faite) |
| 25 | « If the gap reaches 0.10 with a 95% interval excluding zero across the five pairs, noise reads the lock and I am wrong; between 0.05 and 0.10, unresolved. » | JF-28, mesure qui tue ; zone grise ajoutée d'après l'objection du lecteur A | plan (mesure qui tue) |
| 26 | « If the controls stay below 1.02, 1.0 is an adequate null and my second point falls. » | seuil choisi par moi, cohérent avec la prédiction de JF-28 (témoin au-dessus de 1,05) | plan (mesure qui tue de l'argument B) |
| 27 | « Whether this changes between RL locking and SFT distillation is your stream's etiology direction. » | [PIECE] § 1.1 (direction 1 du flux Feng–Jang, hiver 2027) ; [RAPP] tableau n° 14 (exact) | publique, transcription |
| 28 | « So white-box perturbation is a strong elicitation tool and, so far, an unvalidated detector of intent: evidence only against a matched benign control. » | conclusion des n° 3 à 20 | opinion |

## Liens de la réponse
- `https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md` : [P3]. Publication du commit `7c7b688` vérifiée localement seulement (contenu dans `origin/main` = `faff48b`, sans appel réseau).
- `https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/attaque-goodhart-v2/README.md` : [A1].

## Faits internes
Aucun. Rien de non publié n'entre dans la réponse : ni le nul v9, ni les nombres de D36 original, ni ρ.

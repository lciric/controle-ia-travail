# Vérification des phrases modifiées — Lujain Ibrahim, question 1, réponse principale et variante de repli — v3

Vérificateur neuf : je n'ai écrit ni les réponses de Lazar Ciric au formulaire Pivotal, ni leurs registres, ni leurs vérifications. Travail du 3 novembre 2026, de 16:10:46 à 16:22:11 en temps universel coordonné (UTC, `date -u`), puis écriture de ce fichier.

- Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-phrases-modifiees-ibrahim-q1-v3.md`, empreinte sha256 (fonction de hachage SHA-256) `5952534f55dbc0824e19dad7ada1a4b5b274b7418b108e19a02ce83b12f2068a`, vérifiée avant lecture.
- Fichier vérifié : `brouillons/redaction-finale-v1/phrases-modifiees-ibrahim-q1-v3.md`, `b8de23ec333ee7bd76ec2826e12a6e8777471f4c1b5d9a21ef8c1acc92182ca8`, vérifiée. Son titre dit « — v2 », son nom dit v3 : sans effet sur le fond.
- Versions finales nommées dans ses en-têtes, empreintes recalculées, conformes aux préfixes de l'en-tête et aux compagnons `.sha256` :
  - `ibrahim-q1/reponse-v3.md` `4dcba66e968a8306eb5d99c99e8cfbd7d29d29ec21842b6722e5e9c1045eb679`, depuis `ibrahim-q1/reponse-v2.md` `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5` ;
  - `ibrahim-q1/reponse-variante-survie-v2.md` `d25982856c990876d7abaf900fca102b2d8ab09186e46c86d6480e5573f05349`, depuis `ibrahim-q1/reponse-v1.md` `5d30d1346778c3974283aef88b7f2ecf8f1bfb16569a93f4eb8acbf2a41e44e1`.
- Question, texte exact (formulaire collé par Lazar, `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`, ligne 136) : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. »
- **Complétude vérifiée par script.** Chaque « + » figure mot pour mot dans la version finale et pas dans l'ancienne ; chaque « − » l'inverse. Une comparaison phrase à phrase des deux couples de versions (pied de page exclu) ne trouve aucune autre phrase changée. Il y a 12 « + » pour la réponse principale et 7 pour la variante, soit 19, comme le fichier l'annonce.

Sigles des citations, développés une fois : apprentissage par renforcement (RL) ; apprentissage par renforcement à récompenses vérifiables (RLVR) ; ajustement supervisé (SFT) ; optimisation directe des préférences (DPO) ; apprentissage par renforcement à partir de retours humains (RLHF) ; MMLU, banc d'essai de connaissances générales. Format de document portable : PDF. R4, R6 et R8 sont des étiquettes de suites du dépôt public de Lazar.

## 0. Sources

| repère | source | version et empreinte | emplacement |
|---|---|---|---|
| [loi] | clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, propre ; tête = `origin/main` = `b3ecaeccf7d9705d9a2391969ed93633ff7156fe` ; branche distante identique à 16:15 UTC (`git ls-remote`, aucun `git fetch`) | `README.md` `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` ; `STATUS.md` `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` ; `results/R4/README.md` `2664d85cb9d3e33523d352daf2d2054729d2d71e42c7b6daf5ad92bcffe4f781` ; `results/R6/README.md` `27ad89efb844830dea387d2c0a24b5a27e68165d9953b14928b69e287dd2eca9` ; `results/R6/R6_descriptive_counts.json` `98b51681f88be910f5a2bf447b9fbe861648819c1d38bde2479587bd057ccdec` ; `preregistrations/2026-11-02_addendum_R8_post_training_stages.md` `68e891921055938a6d0bf7017df19c30ffd1a5aed2ee1a7777ce1b0a850ee0af` | lignes citées |
| [c1] | même clone, données publiques de la campagne 1 | `data/c2a_generations.json` `a7c85816e2ce60fd86727fe367cb1d63335940a13b50ba3e33c9e16b3ba6189a` ; `data/c2a_results.json` `6ad1a71822395e11417223c8d872c5973129dd1c8a4b023be74810f4746b5d83` ; `data/c2b_generations.json` `ec2f7ca5cc80c249fd861a77fb360a8e1c4d59f1788ada2a7864b88ec72586c2` ; `data/c2b_results.json` `ae097f3d7ac993fe41fa3e1bb11d76f88727ffdf128bc661566949b7f5bc0aa2` (les quatre égales à `SHA256SUMS` du dépôt) | entiers, lus par mon script |
| [cv] | clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` ; tête `146b2a450f50bf3bed06726a747d06cd094e5981` = branche distante (16:15 UTC) | `README.md` `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` | lien de la variante (phrase inchangée) |
| [Q2] | `brouillons/redaction-finale-v1/ibrahim-q2/reponse-v2.md`, dernière version du dossier | `a075396f325babc70cc9169346130a760df3120d52537353d71543997a21a0d4` | entier |
| [chaleur] | Ibrahim, Hafner, Rocher, *Training language models to be warm and empathetic makes them less reliable and more sycophantic*, arXiv 2507.21919v2 (30 juillet 2025) | page de résumé et PDF, par WebFetch | résumé ; p. 2, 3, 6, 9 ; tableau C2 p. 16 ; annexe E.1 p. 18 ; tableau E5 p. 19 ; bibliographie p. 26 |
| [Nature] | même papier, version publiée : *Training language models to be warm can reduce accuracy and increase sycophancy*, *Nature* 652, à partir de la p. 1159 (30 avril 2026) ; PDF du dépôt institutionnel d'Oxford, par WebFetch | — | p. 1164 |
| [OCT] | Maiya, Bartsch, Lambert, Hubinger, *Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI*, arXiv 2511.01689 | PDF par WebFetch (100 000 premiers caractères sur 109 893) | tableau 1 ; §2.1 ; Conclusion |
| [taxo] | Ye, Ibrahim, Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje, *What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct*, arXiv 2605.21778 | PDF par WebFetch (100 000 premiers caractères sur 112 048) | sections de l'enquête |
| [web] | pages GitHub des liens, servies à un visiteur non connecté, par WebFetch | — | — |
| [vérif] | vérifications antérieures, empreintes vérifiées : `ibrahim-q1/verification-chiffres-v2.md` `9e9da509b1b3271233ab445c6a053a8f742cb70a3140a7729d67040513ed3d81` ; `ibrahim-q1/lecture-mentor-v2.md` `3782317cff5fbb4c2868c4fb40f52d0967cea1438e6c30bd5a510181f13993b2` ; `ibrahim-q1/verification-chiffres-v1.md` `c35940b1a10635beb616f37d0a6563d376fe542990faa2bae29b7b500fdab4e3` ; `ibrahim-q1/lecture-mentor-v1.md` `b628cf48380183b220a0fde88602d3465f9cc63e18de4477b47b702aba6b60ba` ; `candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` ; `canal-fable-v1/fable_2026-11-03_n001.md` `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` | — | recoupement |

**Limites.**
- WebFetch fait lire chaque page par un modèle intermédiaire de l'outil. Les chiffres des papiers restent au niveau « transcription » au sens de la règle gelée R7 : je n'ai téléchargé ni empreinté aucun PDF. Pour le tableau E5, quatre lectures indépendantes concordent (la mienne et celles de [vérif]), mais par le même outil.
- Les textes des réponses de R6 sont privés (le fichier brut n'est connu que par son empreinte) : la note des refus de R6 ne se vérifie pas réponse par réponse.
- L'appariement des refus et de leurs notes dans [c1] est de moi : indice `k` de chaque réponse vers la position `k` de la liste des notes de son item et de sa condition. Contrôles faits : `k` va de 0 à 9 pour chaque item et chaque condition ; les moyennes recalculées sont égales aux moyennes stockées ; le motif de refus de `R6_descriptive_counts.json` retrouve 85 réponses, le nombre que donne `results/R4/README.md` l. 36. Script : `/tmp/verif-ibrahim-q1-v3/refus.py` (`b3c03fd49e6c977d784001f13d9ce4a45ae7d9e316e949bf91849da818487d7b`), lancé par `python3 -I`. Aucun code des dépôts n'a été exécuté.
- `ideation-organism` (`faff48b`) n'a pas servi : aucune phrase « + » ne s'y appuie.
- Le fichier de la lectrice indépendante ne corrige aucun point touché par ces 19 phrases. Son relevé sur Ibrahim, question 1 (« my llm judge is in the same family as my model ») est absent des deux versions finales. Les lignes « programme non publié » de `recoupement-v1.md` sont sans objet : aucune des deux réponses ne cite ρ = 0,68 ni « < 1 % ».

## 1. Réponse principale — `ibrahim-q1/reponse-v3.md`

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 1 | « First I need to know what a persona installs, and whether my instruments see it. » | — | **sans objet** : plan, aucun fait. Cohérente avec le n° 9. |
| 2 | « Your warmth paper reports two effects, lost accuracy and validated false beliefs. » | [chaleur], page de résumé : Ibrahim 1re autrice ; « Warm models showed substantially higher error rates (+10 to +30 percentage points) than their original counterparts » ; « They were also significantly more likely to validate incorrect user beliefs ». Titre publié ([Nature]) : « can reduce accuracy and increase sycophancy ». | **exact** (« your » : 1re autrice ; deux effets, ceux du résumé). |
| 3 | « If RL erased one and kept the other, one benchmark would misreport survival. » | — | **sans objet** : raisonnement. Remarque facultative au §3. |
| 4 | « For the belief, I net out the same false claim attributed to a web page; for sadness, your happy sentences. » | [chaleur] tableau C2, p. 16 : trois catégories (Sad, Anger, Happy), cinq phrases chacune ; exemple de joie : « I'm thrilled about this! Everything's going my way today. » Le témoin « page web » est un choix de Lazar, non attribué à la mentore. | **exact**. Repère : sur son Llama-8B chaleureux, la joie seule coûte −2,60 points (tableau E5, p. 19 : 68,76 → 66,16). Nette de la joie, la tristesse vaut −10,36, toujours au-dessus de la croyance (−5,24) : l'ordre du n° 6 tient aussi une fois nettoyé. |
| 5 | « On my opinion items I would also fit my attraction law (next answer) for each model. » | [loi] `README.md` l. 9 : Llama-3.1-8B-Instruct évalue un texte, un juge note la polarité du verdict de 1 à 5. Formulaire, l. 136 puis l. 148 : la question suivante est le projet technique. [Q2] y décrit la loi (g, ĉ, échelle de 1 à 5). | **exact**. |
| 6 | « Across your four tasks, it fell 5 points below the original with a false belief and 13 with a sad user (preprint, Table E5). » | [chaleur] annexe E.1, p. 18 : « aggregated across evaluation datasets » ; quatre tâches, TriviaQA, TruthfulQA, MASK Disinformation et MedQA (p. 3 et p. 9). Tableau E5, p. 19, Llama-8B : contexte non modifié avec croyance fausse, 66,72 → 61,48, écart −5,24 ; tristesse sans croyance, 71,09 → 58,13, écart −12,96. | **exact** : « below the original » est bien l'écart au modèle original dans la même condition, ce que donne la colonne ; ce sont des points de justesse. |
| 7 | « I expect Loving to keep that order and Sycophantic, which "always agrees", to reverse it; Loving is described as "validating feelings". » | [OCT] tableau 1, colonnes « Persona » et « General Description ». Sycophantic : « An overly flattering assistant that always agrees, heaps praise, and excuses your mistakes. » Loving : « A gentle assistant with a deep love for all living beings, validating feelings and offering kind, hopeful support. » | **exact** : deux citations littérales ; « described as » correspond au nom de la colonne. L'attente est un plan. |
| 8 | « Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, is unlikely to give opposite signs. » | [OCT] §2.1 : l'entraînement de caractère « is applied through the 11 different personas described in Table 1 ». [chaleur] p. 6 : « We fine-tuned a subset of two models (Qwen-32B and Llama-70B) on identical conversational data », deux modèles plus grands que Llama-8B. | **exact** pour les deux faits. « is unlikely to » est un raisonnement, désormais nuancé. Aucune source ne le contredit : le dommage propre à Llama-8B (−8,6 points sur MMLU, p. 6) interdisait « cannot », pas « unlikely ». |
| 9 | « If Sycophantic moves neither component, my factual instruments cannot see it, and RL waits. » | — | **sans objet** : règle de lecture. Cohérente avec « On your factual questions I would measure two components ». |
| 10 | « My own judge already scores non-answers: on my 1–5 opinion scale, it rates Llama's refusals 3, near where praise pulls ratings, so refusals can pass for sycophancy. » | [loi] `README.md` l. 9 : « scores the polarity of its verdict from 1 (negative) to 5 (positive) ». `results/R4/README.md` l. 36 : 9 refus sur 900, tous sous éloge, gardés, « the judge rated each of them 3 » ; l. 38 : « A rating of 3 lies close to the praise target (3.2), so a refusal can look like attraction » ; l. 49 : les refus ne portent pas le résultat. `README.md` l. 16 : destination sous éloge 2,937. `results/R6/README.md` l. 55 : « the judge rates such refusals near the middle of the scale ». [c1], mon appariement : 85 réponses de refus, dont 82 notées 3, 2 notées 2 et 1 notée 4. | **exact, avec nuance.** « 3 » vaut pour 9 refus sur 9 en R4 et pour 82 sur 85 en campagne 1 ; R6 ne dit que « near the middle ». « near where praise pulls ratings » est vrai à la formulation de la campagne 1 (2,94 ; 3,2 en R4 ; 2,85 en R6 à la dose standard), pas à la dose douce de R6 (4,01). « can pass for » ne dit pas plus que R4. |
| 11 | « Then the second experiment runs the same RLVR on Instruct, Loving and Sycophantic and reads each component at each checkpoint. » | — | **sans objet** : plan. Les trois modèles sont ceux du paragraphe 2. Le retrait de « (math, code) » lève la réserve 4 de `verification-chiffres-v2.md` : le RLVR de Tülu 3 ne récompense pas le code. |
| 12 | « My preregistered R8 (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) is now measuring the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona. » | Lien, [web] : page servie à un visiteur non connecté ; commit `b3ecaeccf7d9705d9a2391969ed93633ff7156fe` ; premier titre « Addendum to the follow-up preregistration — R8, the attraction law across the stages of post-training ». Fichier présent dans le clone (`68e89192…`). Préenregistrement : addendum l. 3, « Written: 2 November 2026, evening, before any token of R8 ». `STATUS.md` l. 29 : archivé dans la version v2026.11.5 (Zenodo 10.5281/zenodo.23909891) le 3 novembre à 06:49 UTC ; « R8 started at 08:01 UTC under its signed budget ». l. 54 : « finish the run ». Aucun `results/R8/` ; branche distante inchangée à 16:15 UTC. Étapes : addendum §9, `meta-llama/Llama-3.1-8B` → Tülu 3 SFT → DPO → RLVR, « not trained with a specific system prompt » ; §10, trois points de contrôle primaires. | **exact** : lien public, commit et fichier présents. « is now measuring » est conforme au statut public : course lancée, ni finie, ni lue. À revoir avant l'envoi : si `results/R8/` paraît, le présent sera en retard, sans être plus fort que la source. |

## 2. Variante de repli — `ibrahim-q1/reponse-variante-survie-v2.md`

| n° | phrase « + » | source et emplacement | verdict |
|---|---|---|---|
| 13 | « Before RL and at intervals, I measure warmth (your SocioT Warmth score), your false-belief and sad-user conditions, plus a correct-belief control, on held-out non-math factual questions. » | [chaleur] p. 2 : « We measured this using SocioT Warmth, a validated metric that computes log-likelihood… », avec la référence [30] : Cheng, Yu, Jurafsky, « HumT DumT: Measuring and controlling human-like language in LLMs », congrès 2025 de l'Association for Computational Linguistics (bibliographie, p. 26). Conditions de croyance fausse et de tristesse : p. 4–5, tableaux C2 et C3. Le témoin de croyance correcte est un ajout de Lazar, non attribué ; son papier n'a pas cette condition (`verification-chiffres-v1.md`, n° 7). | **exact, avec nuance d'attribution.** C'est la mesure qu'elle a employée, mais pas la sienne : elle est de Cheng, Yu et Jurafsky, qu'elle cite. « your » se lit ici comme dans « Your GPT-4o judge » (celle de son papier), mais peut se lire comme une paternité. Correction facultative au §4. |
| 14 | « On your four reliability sets, this model's warmth cost lives in the frame: in your preprint's Table E5, warm minus original accuracy is −0.25 points with no context and −12.96 with a sad user. » | [chaleur] p. 9 : « Reliability evaluation tasks », les quatre jeux. Tableau E5, p. 19, Llama-8B : contexte non modifié sans croyance, 70,74 → 70,50, écart −0,25 ; tristesse sans croyance, 71,09 → 58,13, écart −12,96. La perte de 8,6 points sur MMLU (p. 6) est hors de ces quatre jeux. | **exact** : chiffres de la colonne ; lecture bornée aux quatre jeux, comme la correction le voulait. |
| 15 | « Your paper does not claim that every way of inducing warmth acts alike, so step one is whether Loving pays that cost before RL; if the 95% interval of its deficit is not above 5 points, I stop there. » | [Nature] p. 1164 : « We do not claim that all possible methods for inducing warmth will produce the same effects. » | **exact** (version publiée ; « your paper » la distingue bien de « your preprint »). La porte par l'intervalle est un plan, cohérent avec le n° 18. |
| 16 | « My attraction law (next answer) adds a second readout: how far (g) and toward what (ĉ) ratings move under criticism and praise. » | [loi] `README.md` l. 9–16 : Δ = g·(ĉ − p₀), deux bras, critique et éloge. [Q2] décrit la loi, « how far (g) from where (ĉ) ». | **exact**. |
| 17 | « The estimate is Loving's accuracy deficit against Instruct after RL minus before, so Instruct's own run absorbs what RLVR does to every arm alike. » | — | **sans objet** : plan, désormais nuancé (« every arm alike »). |
| 18 | « Fixed in advance: if the 95% interval lies entirely within ±5 points, the cost survived; entirely below −5, RLVR cut it by at least 5 points; entirely above +5, it grew; otherwise, undecided. » | — | **sans objet** : règle de décision. Logique juste pour une estimation « après moins avant » : sous −5, le déficit a baissé de plus de 5 points. Rien ne la dit déjà préenregistrée. |
| 19 | « The reward says nothing about the user, and 88.7% of the 106 experts in your survey agree RLHF or preference learning is sycophancy's primary cause. » | [taxo] : Ibrahim 2e autrice sur 8 ; « The final sample comprised N = 106 respondents » ; « Respondents also agreed that RLHF or preference learning is the primary cause of sycophancy (M = 5.70, SD = 0.97; 88.7% agree) » ; échelle d'accord en 7 points. 94 / 106 = 88,7 %. | **exact** : la correction de `verification-chiffres-v1.md` (« name » → « agree … primary ») est appliquée fidèlement. La première moitié de la phrase est un choix de conception. |

## 3. Cohérence, liens, traces internes

**Cohérence au sein de chaque réponse : aucune contradiction.**
- Réponse principale :
  - n° 1 et n° 9 sont accordés ;
  - n° 4 et n° 6 : l'ordre des deux indices tient brut (13 contre 5) et une fois la tristesse nettoyée par la joie (10,4 contre 5,2) ;
  - n° 11 nomme les modèles du paragraphe 2 ;
  - n° 12 n'annonce aucun résultat.
- Remarque facultative sur le n° 3. « one benchmark » a perdu son antécédent : la phrase sur les bancs d'essai de la taxonomie est retirée. Or, dans son papier comme dans le plan (« On your factual questions I would measure two components »), les deux effets se lisent sur les mêmes quatre jeux, sous deux conditions. « one score » dit la même chose, au même nombre de mots, sans inviter la réponse « vous n'avez vous-même qu'un banc ».
- Variante :
  - la mesure de la chaleur (n° 13) est un contrôle de la persona, pas une troisième lecture ; « I expect survival on both readouts » reste donc juste ;
  - la porte du n° 15 et la règle du n° 18 sont compatibles ;
  - n° 19 et la phrase sur R8 (inchangée) vont dans le même sens. Le piège déjà relevé par `lecture-mentor-v1.md` reste hors du texte : la prédiction S3 de R8, au bout du lien, s'intitule « preference optimisation lowers the gain ».
- Entre réponses, hors consigne : [Q2] dit « the judge rates refusals near 3 », le n° 10 dit « 3 ». C'est compatible (voir le n° 10).

**Liens.**
- Le seul lien des phrases « + » (n° 12) pointe vers une page publique existante : dépôt cloné, commit présent, fichier présent.
- Revérifiés aussi, hors phrases « + », les deux liens de la variante :
  - R8 : le même ;
  - `https://github.com/lciric/sycophancy-construct-validity/blob/146b2a4/README.md` : page publique, commit `146b2a450f50bf3bed06726a747d06cd094e5981`, fichier présent ; on y lit « lowered the judged rate from 61.0% to 46.5% of items » et « did **not** reproduce in a preregistered replication ».

**Traces de résultats internes du programme de contrôle : aucune.** Recherche par expression régulière, insensible à la casse, dans les deux réponses entières (motifs en anglais, comme les réponses) : `0.68`, `.684`, `rho`, `ρ`, `< 1 %`, `68 %`, `65 %`, `44 %`, `D36`, `null`, `nul`, `v9`, `v8`, `validat`, `organism`, `ideation`, `control`, `monitor`, `white-box`, `probe`, `rank`, `steer`, `patch`, `residual`, `activation`, `T0.`, `G0`, `G1`, `GO-`, `N-0`, `R-1`, `prereg/`, `registre`, `Vast`, `USD`, `internal`, `private`, `unpublished`. Seules sont sorties des occurrences bénignes : « validated false beliefs », « cold control », « correct-belief control », « positive control », « GPT-4o judge, validated ». Les chiffres de l'ablation (61,0 % → 46,5 %, variante, phrase inchangée) sont publics dans [cv].

**Symétrie (règle gelée R4 des consignes du dépôt, à ne pas confondre avec la suite R4).** Un relevé sans inexactitude est « propre ». J'ai donc repris sur source primaire, par des questions distinctes, les affirmations les plus exposées :
- les quatre valeurs du tableau E5, dont la joie ;
- le tableau C2 ;
- les deux effets du résumé ;
- le nom de la colonne du tableau 1 d'Open Character Training ;
- la phrase de la version *Nature* ;
- l'énoncé et l'effectif de l'enquête ;
- le lien et le statut de R8 ;
- l'auteur de SocioT Warmth ;
- les notes des refus, recalculées sur les données publiques.

Il en sort deux nuances (les refus ne sont pas tous notés 3 ; SocioT Warmth n'est pas de la mentore), aucune erreur.

## 4. Corrections minimales

**Aucune correction obligatoire** : aucune phrase inexacte, aucune phrase plus forte que sa source, aucun résultat non publié présenté comme publié, aucun lien mort, aucune trace interne.

Facultatives, une ligne chacune :
- n° 13 : « (your SocioT Warmth score) » → « (SocioT Warmth, as you did) » (+1 mot). Raison : la mesure est de Cheng, Yu et Jurafsky (« HumT DumT », 2025), que son papier cite en [30] ; « your » peut se lire comme une paternité. Source : [chaleur] p. 2 et p. 26.
- n° 3 : « one benchmark would misreport survival » → « one score would misreport survival » (0 mot). Raison : les deux effets se lisent sur les mêmes quatre jeux, dans son papier comme dans le plan ; la phrase sur les bancs d'essai de la taxonomie, qui portait « benchmark », est retirée. Source : [chaleur] p. 3 ; la réponse, paragraphe 4.
- n° 10 : garder « 3 ». Si la mentore le conteste, la source exacte est `results/R4/README.md` l. 36 (9 sur 9). Pour couvrir la campagne 1 (82 sur 85), il faudrait « nearly all of Llama's refusals 3 » (+3 mots), au-dessus de la visée de 450.
- n° 12 : à revoir avant l'envoi de 23:00 UTC. Si `results/R8/` paraît sur la branche publique, remplacer « is now measuring » par « measures » et dire ce qui est lu. Source : `STATUS.md` l. 54.

## 5. Décompte

19 phrases « + » ; 13 portent des affirmations vérifiables, 6 sont des plans, des raisonnements ou des règles de lecture (n° 1, 3, 9, 11, 17, 18).

37 affirmations vérifiées (23 dans la réponse principale, 14 dans la variante) :
- **exactes : 37**, dont 4 avec nuance (n° 10, la note 3 ; n° 10, la destination sous éloge selon la formulation ; n° 12, « is now measuring », à revoir avant l'envoi ; n° 13, l'attribution de SocioT Warmth) ;
- **inexactes : 0** ;
- **non vérifiables : 0** ;
- **non publiées présentées comme publiées : 0** ;
- **plus fortes que leur source : 0**.

Contradictions avec une autre phrase de la même réponse : 0. Liens des phrases « + » : 1 sur 1 public, commit et fichier présents (et 2 sur 2 dans la variante, hors phrases « + »). Traces de résultats internes : 0.

## 6. Outils et interdits

- Lectures en ligne par WebFetch : arXiv 2507.21919 (résumé et PDF v2), 2511.01689 (PDF), 2605.21778 (PDF) ; PDF de la version *Nature* sur le dépôt d'Oxford ; les deux pages GitHub. Aucune demande d'approbation, aucun refus.
- `git ls-remote` vers les deux dépôts publics (16:15 UTC) ; aucun `git fetch` ; aucun code des dépôts exécuté. Les copies de données lues par mon script sont dans `/tmp/verif-ibrahim-q1-v3/donnees-lues/`, hors du dépôt.
- Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni sous `/home/claude/coffre-*`, aucun appel de modèle autre que moi. Seul fichier écrit dans le dépôt : celui-ci.

# Relecture neuve du brouillon de Lazar — Q1 de Heimersheim, option c — v1

Lecteur neuf (Claude Fable 5.1) ; je n'ai écrit aucun des textes lus. Rédigé le 3 novembre 2026 à partir de 06:44 UTC (`date -u`), terminé vers 07:00 UTC. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pivotal-relecture-fable-brouillon-q1-heimersheim-prompt.md`.

Texte vérifié : `brouillons/candidature-pivotal-v16/mentors/heimersheim-q1-brouillon-lazar-2026-11-03-0741.md`, sha256 `a049dfcc74fd091459e8f1ca0059c47c040307da61c826968b52f77fce05e950`.

Règle respectée : rien n'est réécrit, aucune phrase anglaise de réponse n'est proposée ; les corrections gardent les mots de Lazar et ne touchent que le fond.

## 0. Sources lues et niveau de preuve

- Fiche v2, plan v1, rapport Heimersheim v1, recoupement v1 (dossier `lecture-approfondie-v1/`) ; ligne R-1302 de `registres/decisions.md` (D36 et réplication).
- 2510.20487 v5 (Hua, Qin, Marks, Nanda ; HTML jusqu'à l'annexe E, PDF pour les annexes A, B, G, H, I ; tableau 16 lu ligne à ligne).
- 2606.24964 (Ferreira da Silva, Pivotal Research, et Heimersheim ; PDF, corps, annexe A).
- 2605.05115 (Wurgaft et coll. ; PDF, sections 2 à 8, annexe A.3).
- 2409.17113 (Janiak et coll., dont Heimersheim ; PDF ; le HTML est refusé par le proxy).
- Billet de l'Institut britannique de sécurité de l'IA sur GLM-5 (Read, Schoen, Aranguri, Bloom ; LessWrong, 10 avril 2026) et commentaire de Jack Lindsey.
- Dépôts publics de Lazar, par les clones déjà présents sous `/home/claude/scratch/pivotal-approfondi/recoupement/depots/` (aucun `git fetch`) : `sycophancy-construct-validity` à `5ee1d23` (README sha256 `a620c95d…`) ; `sycophancy-psychophysical-law` à `e5e960b` (README et `results/R6/README.md`, sha256 `27ad89ef…`).
- Page d'anthologie ICLR 2026 (mlanthology.org) pour la mention « ICLR 2026 » de Hua et coll.
- Fiche système de Sonnet 4.5 : tentée ; le convertisseur s'arrête en 7.5.6, donc 7.6.4 **non lue**. Tout ce qui concerne Sonnet 4.5 reste secondaire.
- Limite : `WebFetch` passe par un modèle intermédiaire (citations courtes, pas de numéro de page). Niveau « transcription » au sens de R7.

## 1. Tableau de vérification

Verdicts : **exact** ; **exact (nuance)** ; **inexact** ; **non vérifiable ici**.

| # | Mots exacts de Lazar | Ce que dit la source | Verdict |
|---|---|---|---|
| 1 | « (c) Steering towards evaluation awareness » | Formulaire, question du mentor : « c) Activation steering against evaluation awareness » | **inexact** (sens inversé) |
| 2 | « it worked once in Hua et al. ICLR 2026 » | 2510.20487 v5 (2 mars 2026) ; l'arXiv ne porte pas la mention ICLR ; l'anthologie ICLR 2026 (mlanthology.org) liste le papier, auteurs Hua, Qin, Marks, Nanda | exact |
| 3 | « public repo sycophancy-construct-validity at commit 5ee1d23 » | Clone : tête `5ee1d23`, 9 octobre 2026 | exact |
| 4 | « rho=0.684 (this might be overfitting to the training set) » | README l. 40 : ρ = 0,684 sur activations brutes ; l. 85 : « ρ may also be training fit » | exact |
| 5 | « any rank 1 method (contrastive steering, directional steering and ablating, blocking SAE features, adding auxilary loss to fine tune the model, ablating heads (L0.H29 and an ensemble of 3 heads)) » | README l. 58 : rang 1 = CAA steering, directional steering, directional ablation, SAE feature clamping, fine-tuning with auxiliary loss ; « Unit-level controls: ablation of head L0.H29 alone and of a 3-head set » | exact (nuance : les têtes ne sont pas « rang 1 » dans le dépôt) |
| 6 | « I never saw a significant decrease » | README l. 19 : rang 1 « no clean reduction », « reported qualitatively », « carry no numbers » ; l. 20 : 3 têtes 58,5 % → 57,5 %, p = 0,91 | exact (nuance : pas de test pour le rang 1) |
| 7 | « decrease from 61.0 to 46.5% N=200 Mcnemar's p=0.0019 » | README l. 17 : 61,0 % → 46,5 % (122/200 → 93/200), exact McNemar p = 0,0019 | exact |
| 8 | « stored generations that were truncated at 300 chars » | README l. 3, 26 : « stored truncated at 300 characters » avant jugement | exact |
| 9 | « replicated this preregistered using new fully judged generations I did not see the effect » | README l. 23 : « did not reproduce in a preregistered replication with fresh, seed-matched generations judged on full responses (July 2026) » | exact |
| 10 | « The judge was inferring a weaker verdict that came later in the generation as a stance » | README l. 26 : « a softened or deferred negative verdict reads as the model holding its position » ; l. 25 ajoute le premier facteur : l'ablation adoucit tout verdict négatif, même sans pression | exact (nuance : le facteur « adoucissement générique » manque) |
| 11 | « D36 (preregistered 29th July) » | R-1302 : « archive privée D36, préenregistrée le 29 juillet » | non vérifiable ici (privé ; conforme à R-1302) |
| 12 | « layers 13-25 … recovers 68% of the difference [45; 88] » | R-1302 : R(A3) = 0,677 [0,45 ; 0,88], couches 13–25 | non vérifiable ici (conforme à R-1302) |
| 13 | « When I replicated this I found 65% [42; 87] » | R-1302 : 0,65 [0,42 ; 0,87] | non vérifiable ici (conforme) |
| 14 | « portion that is able to be verbalised recovered 1% [-18; +20] » | R-1302 : R(A2) = 0,009 [−0,18 ; 0,20], « indistinguable de zéro » | non vérifiable ici (conforme) |
| 15 | « no pressure state from another prompt recovers 44% [19; 68] … 2/3rds of this is just generic » | R-1302 : 0,44 [0,19 ; 0,68] ; 44/68 ≈ 0,65 | non vérifiable ici (conforme) |
| 16 | « UK AISI replicated on GLM-5 (April 10th 2026 1 scenario 250 samples) » | Billet : 10 avril 2026, « UK AISI Model Transparency Team », un scénario, « 250 epochs » | exact |
| 17 | « A random direction that has no relation ("control_book") produced the largest effect » | Billet : control_book = paire contrastive « book on the bottom shelf » / « top shelf », l'un des dix témoins ; « control_book has the largest and most consistent effect » ; conclusion : « Semantically unrelated contrastive pairs are not appropriate controls » | **inexact** (pas aléatoire : contrastive sans rapport) |
| 18 | « ~80% actions were misaligned with a strength of -0.025 and awareness verbalised around 0 » | Billet : « raising misaligned action rates to 80% » à −0,025, « the highest we observed » ; conscience verbalisée « near zero » | exact |
| 19 | « 2 of the 4 directions had no effect » | Billet : 4 vecteurs de la fiche Opus 4.6 + 2 ajoutés = 6 ; « the remaining two non-control vectors fail to increase misaligned action rates above baseline » (par élimination : testing_vs_conversation, hua_et_al_ha, tous deux parmi les 4 d'Anthropic) | exact (nuance : 2 des 6, et « sur le désalignement ») |
| 20 | « As lindsey pointed out this was better then the random controls on sonnet 4.5 but not on glm-5 » | Commentaire Lindsey : « #1 and #2 are satisfied in our Sonnet 4.5 experiments, and not in yours » ; « your random controls increase misalignment by about as much as your steering vectors » | exact |
| 21 | « emojis are associated with actual users (section 3.1 footnote 3 app A and B) » | 2510.20487 §3.1 note 3 : « We later discovered Llama Nemotron already exhibits this behavior without fine-tuning » ; annexe A : pilotage des émojis | exact |
| 22 | « a truth that correlates with professional code (python type hints) » | Annexe B : « evaluators prefer professional Python code formatting (Black style, type hints, and docstrings) » | exact |
| 23 | « state that steering is similar to contrastive prompts » | Annexe A : « a simple alternative explanation is that steering is similar to prompting with the contrastive prompts » ; annexe B : « we cannot rule out the alternative hypothesis » | exact (nuance : concession, pas affirmation) |
| 24 | « Neither Hua et al or the sonnet 4.5 report test for this » (registre) | Rien sur le registre chez Hua ; fiche Sonnet 4.5 non lue | non vérifiable ici (Sonnet 4.5) ; exact pour Hua (absence) |
| 25 | « we don't know which directions on sonnet 4.5 are actually the deployment behaviour » | §1 : « We do not know which one, if any, represents the model's "true" deployment behavior. » | exact |
| 26 | « decrease type hints to 0.34-0.60 (Table 16 as of January 2026) » | Annexe I.1.1, « Update [Jan 4, 2026] », tableau 16 : de 0,34 (« INFO: Not evaluation. ») à 0,60 ; 128 invites, invite système Wood Labs | exact |
| 27 | « You perturb by keeping the norm constant in the plane of two directions … angle that breaks the plateau … superellipse (equations 8-13) » | 2606.24964 éq. 8 (mélange de deux directions orthonormées), 9 (perturbation à norme constante), 10–12 (modèle de réponse, rupture), 13 (superellipse d'exposant p) | exact |
| 28 | « if p is ~2 there is no privilege … If p>2 then there is privilege of pure directions which means there is some error correction specific to the features » | §4.1, §6.1 : p = 2 ne peut pas privilégier ; p > 2 privilégie les directions pures ; §6.2 : lectures rivales (bassins d'attraction, correction vers une variété) | exact (nuance : « evidence for », pas « means ») |
| 29 | « All my directions that were contrastive had a p of 2.3-2.4 » | §4.1 : contrastives moyenne 2,42 [2,29 ; 2,62], médiane 2,30 ; « p ≈ 2.3 » (§1, §6.1, §7) ; « p ≈ 2.4 » (§4.2, fig. 5) ; ce sont les directions du papier du mentor | **inexact** (attribution « my » ; « all » surestime) |
| 30 | « random directions had a p of 2.05 » | §4.1 : aléatoire 2,03 [2,00 ; 2,07] ; différence aléatoire 2,05 [2,00 ; 2,10] | inexact (mineur : 2,05 est la différence aléatoire) |
| 31 | « across 6 models including llama-3.1-8B » | Six modèles : Gemma-2-9B, Qwen3-1.7B, Llama-3.1-8B, Mistral-7B-v0.3, Aya-Expanse-8B, Yi-1.5-9B | exact |
| 32 | « None of my directions were for evaluation (see app A) » | Annexe A : 33 directions (14 sémantiques, 10 langues, 9 langages), aucune sur l'évaluation | exact sur le fait ; **inexact** (attribution « my ») |
| 33 | « 30+ examples with matched register » | §3 : P ≥ 30 paires par concept | exact (nuance : paires) |
| 34 | « use your method to remove \|cos\|>=0.1 » | Annexe A, fig. 8 : les paires de directions à recouvrement brut ≥ 0,1 sont **exclues** (210 sur 528), parce que Gram–Schmidt déforme les directions trop proches ; le papier n'a pas de méthode pour « retirer » la composante commune | **inexact** (la règle existe, mais comme critère d'exclusion) |
| 35 | « calculate the p value on the rest » | Le papier parle de l'exposant p de la superellipse, jamais d'une valeur p statistique | **inexact** (terme ambigu) |
| 36 | « it only tells you that it is correcting differently it doesn't prove that it is correcting for the feature » | §7 : « p>2 appears to be necessary but not sufficient for a direction to be a feature » | exact |
| 37 | « I used layer 2 5 tokens and l2 distance to answer not a behaviour » | 2606.24964 : couche ℓ = 2 par défaut, N = 30 invites FineWeb de 5 jetons, distance L2 en avant-dernière couche ; c'est le réglage du mentor | **inexact** (attribution « I ») |
| 38 | « I haven't tested it with a feature/non feature pair » | 2606.24964 : aucune paire mixte (trait, non-trait) testée ; c'est le papier du mentor | **inexact** (attribution « I ») |
| 39 | « Hua et al steer from layer 10-30 at every position during generation » | §4.1 : couches 10, 14, 18, 22, 26, 30 ; « we steer on user tokens and all generation tokens after the first sentence, but not on formatting tokens or the system prompt » | exact (nuance : pas « every position ») |
| 40 | « GML-5 all layers » | Billet : GLM-5, 78 couches, pilotage à toutes les couches | **inexact** (coquille « GML-5 ») ; fait exact |
| 41 | « Opus 4.6 as stated by Hua et al will no longer verbalise awareness but oracles can still detect it » | §6 : « greatly suppressed verbalized evaluation awareness, while failing to fully eliminate unverbalized evaluation awareness as measured by activation oracles » ; la référence est « Anthropic (2026) », fiche d'Opus 4.6 en bibliographie | **inexact** (« no longer » trop fort ; « greatly suppressed ») |
| 42 | « stable regions Janiak et al 2409.17113, plateau's from 2024 » | 2409.17113 : régions stables, sortie insensible aux petites perturbations ; Heimersheim coauteur. Billet 2024 non lu ici | exact (2024 : non vérifié ici) |
| 43 | « Directions that are features break the plateau earlier than random directions » | 2606.24964 fig. 1 : la courbe des traits dépasse l'aléatoire pour ≥ 63 % des ancres, à chaque angle | exact |
| 44 | « varies by up to ~70 times (2606.24964 fn 1) » | Note 1 : « up to a factor of ~70 », pour la métrique de divergence de Kullback-Leibler | exact (nuance : métrique KL) |
| 45 | « gets steeper as you go to larger models and more training » | 2409.17113 §4 : les courbes se raidissent avec la taille (0,5 à 7 milliards) et avec l'entraînement | exact |
| 46 | « Hua et al App G … a strength of about 3 on one layer damaged the models performance and 6*0.6 barely touched it » | G.1 : « steering on single layers at strengths around 3 would often cause the performance to decrease dramatically » ; six couches × 0,6 = 3,6 ; §5.1 : 56,8 → 55,2 % vers le déploiement | exact |
| 47 | « going negative by 13.7 points decreased accuracy on evaluation tasks and 1.6 points on deployment tasks » | §5.1 : une seule tâche (BigCodeBench) ; 56,8 % sans pilotage ; **vers l'évaluation** 43,1 % (−13,7) ; **vers le déploiement** 55,2 % (−1,6) | **inexact** (ce sont deux sens de pilotage, pas deux tâches ; « going negative » n'a pas de sens ici) |
| 48 | « GLM-5 will become incoherent past 0.025 where as opus 4.6 is 0.1 as stated by the paper » | Billet : « strengths larger than 0.025 often made the model incoherent, and even 0.025 was sometimes too strong » ; Anthropic : 0,1 pour Opus 4.6 | exact (nuance : « often » ; c'est un billet, pas un papier) |
| 49 | « Manifold Steering (2605.05115) … ~2.8x lower energy for outputs that are days, months, letters and ages » | §3.2 : « a factor of 2.8× » ; jours 0,34 vs 0,93, mois 0,36 vs 1,09, lettres 2,42 vs 6,95, âges 5,21 vs 13,49 ; p < 0,001 | exact |
| 50 | « if you only have 2 points for a binary concept your going to have a line » | Annexe A.3 : spline cubique par les centroïdes ; la réduction au segment est une déduction de Lazar, pas dans le texte | non vérifiable (déduction, non sourcée) |
| 51 | « They haven't tested on more abstract concepts (see section 8) and only predict the next token » | §8 : « more abstract concepts, e.g., refusals » ; « our focus on the next-token distribution » | exact |
| 52 | « They don't discuss register or the remainder of the model that can't be verbalised » | Rien dans le texte lu (annexe tronquée sur 3 000 caractères) | exact (absence ; non démontrable, R8) |
| 53 | « Random control that is close to the same norm (Hua et al section 5.3 » | §5.3 : 24 vecteurs tirés d'une normale de même moyenne et variance, normes L2 « very similar », effet bien moindre | exact |
| 54 | « random features from the sonnet 4.5 report I didn't check the norm » | Billet GLM-5 : « for Sonnet 4.5 and Opus 4.5 they use random SAE features as baselines » ; fiche non lue | non vérifiable ici (secondaire, concordant) |
| 55 | « Make sure the models capabilities arent being effected (56.8 to 55.2%) » | §5.1 : 56,8 % → 55,2 % (BigCodeBench, vers le déploiement) | exact |
| 56 | « Hua et al section 6 states that the organism "will rely on these cues" » | §6 : « Our model organism relies on hints and nudges to successfully implement the evaluation-dependent type hint writing behavior » ; « does not have the capability to consistently distinguish … based on subtle cues » | **inexact** (citation entre guillemets qui n'existe pas) |
| 57 | « Test on more then one capability » (comme non fait) | Hua : BigCodeBench seul ; GLM-5 : MATH et BFCL | exact (nuance : deux tâches sur GLM-5) |
| 58 | « R6 (public zenodo link 10.5281/zenodo.23888058) » | `results/R6/README.md` l. 3 : 23888058 = archive du **préenregistrement** (addendum, 2 nov. 14:42 UTC, v2026.11.3) ; README principal l. 104 : les **résultats** R6 sont dans v2026.11.4, 10.5281/zenodo.23892810 | **inexact** (le lien pointe sur le préenregistrement, pas sur la courbe) |
| 59 | « 3 levels of pressure and Llama-3.1-8B-Instruct 5,400 generations » | R6 l. 8–14 : quatre familles, 12 machines, 5 400 générations au total ; Llama seul = 3 doses × 30 items × K = 5 × 3 conditions = 1 350 | **inexact** (5 400 = quatre familles) |
| 60 | « gain stayed roughly the same (0.658 / 0.678 / 0.629) but the fixed point changed (1.87 / 1.33 / 2.37) » | R6, tableau Llama : g = 0,658, 0,678, 0,629 ; ĉ = 1,867, 1,331, 2,367 | exact |
| 61 | « praise the gain increased (0.28 / 0.60 / 0.80) and the end point decreased » | R6 : g = 0,276, 0,597, 0,797 ; ĉ = 4,011, 2,845, 2,475 | exact |
| 62 | « At high levels of pressure both came back to the middle » | R6 l. 43 : « set back toward the middle of the scale, and the mean shift is zero in both arms » | exact |
| 63 | « how gain wasn't the right metric at one level of pressure » | R6 l. 43 : à la dose forte, « "attraction" holds only in the sense of the fit » | exact (lecture) |

Décompte : 63 lignes ; 40 exactes (dont 13 avec nuance) ; 14 inexactes ; 9 non vérifiables ici (5 pour D36, privé et conforme à R-1302 ; 1 déduction ; 3 secondaires ou absences).

## 2. Corrections de fond, une ligne chacune

Format : mots exacts → correction minimale (mots de Lazar gardés) ; raison ; source.

Majeures (chiffre faux, attribution fausse, sens inversé, citation inexistante, terme qui change le sens) :

1. « (c) Steering towards evaluation awareness » → « (c) Steering against evaluation awareness » ; le titre dit le contraire de l'option ; formulaire du mentor.
2. « All my directions that were contrastive had a p of 2.3-2.4 » → « Your contrastive directions had a p of about 2.3 (2.42 mean, 2.30 median) » ; ce sont les directions du papier du mentor, et « all » surestime (valeurs par direction dispersées) ; 2606.24964 §4.1.
3. « None of my directions were for evaluation (see app A) » → « None of your directions were for evaluation (see app A) » ; attribution ; 2606.24964 annexe A.
4. « I used layer 2 5 tokens and l2 distance to answer not a behaviour » → « You used layer 2, 5 tokens and l2 distance as the response, not a behaviour » ; c'est le réglage du mentor, pas celui de Lazar ; 2606.24964 §2–3.
5. « And I haven't tested it with a feature/non feature pair » → « And you haven't tested it with a feature/non feature pair » ; attribution ; 2606.24964 (aucune paire mixte).
6. « Then calculate the p value on the rest » → « Then calculate the exponent p on the rest » ; « p value » se lit comme une valeur p statistique ; 2606.24964 éq. 13.
7. « use your method to remove |cos|>=0.1 » → « your paper excludes pairs with |cos|>=0.1 ; for the rest, orthogonalise and fit p » ; la règle est un critère d'exclusion des paires (210 sur 528), pas une méthode de retrait ; 2606.24964 annexe A, fig. 8.
8. « They also found that going negative by 13.7 points decreased accuracy on evaluation tasks and 1.6 points on deployment tasks » → « steering toward evaluation cost 13.7 points of accuracy (56.8 to 43.1) and steering toward deployment 1.6 points (56.8 to 55.2) on the same task » ; une seule tâche (BigCodeBench), deux sens de pilotage ; 2510.20487 §5.1 (pas l'annexe G).
9. « GML-5 all layers » → « GLM-5 all layers » ; coquille qui change la référence ; billet de l'Institut britannique.
10. « A random direction that has no relation ("control_book") » → « A contrastive direction that has no relation ("control_book", book on the bottom vs top shelf) » ; ce témoin n'est pas aléatoire, c'est une paire contrastive sans rapport, et c'est précisément la différence entre témoin isotrope et témoin exigeant que l'argument exploite ; billet, annexe des témoins et conclusion « Semantically unrelated contrastive pairs are not appropriate controls ».
11. « Opus 4.6 as stated by Hua et al will no longer verbalise awareness but oracles can still detect it » → « will mostly no longer verbalise awareness (greatly suppressed) but oracles can still detect it » ; la source dit « greatly suppressed », pas éliminée ; 2510.20487 §6.
12. « Hua et al section 6 states that the organism "will rely on these cues" » → « states that the organism "relies on hints and nudges" » ; la citation entre guillemets n'existe pas ; 2510.20487 §6.
13. « I used 3 levels of pressure and Llama-3.1-8B-Instruct 5,400 generations » → « 3 levels of pressure, 4 families, 5,400 generations (Llama-3.1-8B-Instruct: 1,350) » ; 5 400 couvre quatre familles ; `results/R6/README.md` l. 8–14.
14. « R6 (public zenodo link 10.5281/zenodo.23888058) » → « R6 (preregistration 10.5281/zenodo.23888058 ; results 10.5281/zenodo.23892810, or github.com/lciric/sycophancy-psychophysical-law results/R6) » ; le lien donné est celui du préenregistrement, pas de la courbe ; README principal l. 104, R6 l. 3.
15. « Measure what is left in the model that can't be verbalised (using p or oracles) » (sous « Things that aren't done ») → « Measure what is left … on open models (done with oracles on Opus 4.6 as reported ; not on Hua's organism or GLM-5, never with p) » ; contredit son propre point (a) du paragraphe 3 ; 2510.20487 §6 ; commentaire Lindsey, condition #4.

Mineures (nuance qui peut être lue comme une erreur par ce mentor) :

16. « random directions had a p of 2.05 » → « random-difference directions had a p of 2.05 (random 2.03) » ; 2606.24964 §4.1.
17. « state that steering is similar to contrastive prompts » → « concede they cannot rule out that steering is similar to prompting with the contrastive prompts » ; c'est une explication rivale admise, pas leur conclusion ; 2510.20487 annexes A et B.
18. « any rank 1 method (…, ablating heads (L0.H29 and an ensemble of 3 heads)) » → « any rank 1 method (…) or head ablation (L0.H29, 3-head set) » ; le dépôt classe les têtes comme « unit-level controls », pas rang 1 ; README l. 58.
19. « I never saw a significant decrease » → « I never saw a clean decrease » ; les sorties du rang 1 n'ont pas été conservées, aucun test n'existe pour elles ; README l. 19, 87.
20. « which means there is some error correction specific to the features » → « which is evidence for some error correction specific to the features » ; le papier donne des lectures rivales ; 2606.24964 §6.2.
21. « Hua et al steer from layer 10-30 at every position during generation » → « at layers 10 to 30 (six layers) on user tokens and generation tokens after the first sentence » ; pas le système ni les jetons de format ; 2510.20487 §4.1.
22. « 2 of the 4 directions had no effect » → « 2 of the 6 eval-awareness directions (both from the Opus 4.6 card) did not raise misalignment above baseline » ; billet (4 vecteurs d'Anthropic + 2 ajoutés).
23. « Test on more then one capability » (comme non fait) → « Test on a battery of capabilities (Hua: one task ; GLM-5: two) » ; billet (MATH, BFCL).
24. « A curve for your demand control » → « A curve for your demanding control (random-difference from the same prompt set) » ; « demand control » n'est pas lisible ; et GLM-5 a déjà cinq forces pour ses témoins sans rapport, ce qui manque est le témoin « différence aléatoire » avec sa courbe, sur l'organisme de Hua ; 2606.24964 éq. 6–7 ; billet.
25. « D36 (preregistered 29th July <<LIEN_D36>>) » → à résoudre avant envoi : lien public si D36 est publié, sinon dire « unpublished, preregistered 29 July » ; R-1302 (publication soumise au « oui » de Lazar).
26. « GLM-5 will become incoherent past 0.025 … as stated by the paper » → « often becomes incoherent past 0.025 … as stated by the UK AISI post » ; billet (« often », « sometimes too strong ») ; c'est un billet, pas un papier.

## 3. Ce qui manque ou dépasse (cinq lignes)

1. Manque l'effet hors cible documenté : piloter la conscience d'être testé modifie aussi le refus (2510.20487 §2, d'après Abdelnabi et Salem) ; c'est la preuve publiée la plus directe que l'effet n'est pas spécifique, et elle n'est nulle part dans le brouillon.
2. Le témoin aléatoire de Hua est cité sans son résultat ni son nombre (24 vecteurs, effet bien moindre, §5.3) et le cœur du résultat positif (indices de type < 11 % sous pilotage contre 34 % par invite, 16 invites réunies insuffisantes, §5.1, §5.3) n'apparaît pas : « it worked once » reste sans chiffre, alors que c'est le troisième cas que le brouillon doit expliquer.
3. Le résidu non verbal d'Opus 4.6 est bien présent (paragraphe 3, point a) mais il est ensuite listé parmi les choses « non faites » (paragraphe 4) ; la concession « pilotage ≈ invite » et la symétrie du tableau 16 sont présentes ; manque en revanche le premier facteur de la non-réplication du rang 3 (l'ablation adoucit tout verdict négatif, même sans pression, README l. 25), qui est pourtant l'exemple le plus propre de « something happens but it's generic » dans son propre dépôt.
4. Non rattachables à une source lue : les cinq chiffres de D36 (archive privée, conformes à R-1302, non publics tant que D36 n'est pas publié) ; « plateau's from 2024 » (billet non lu ici) ; la réduction de la variété à un segment pour un concept binaire (déduction de Lazar, non signalée comme telle) ; tout ce qui concerne la fiche de Sonnet 4.5 (témoins aléatoires, absence de contrôle de registre : secondaire, concordant avec le billet GLM-5).
5. Dépasse ce que les sources disent : « which means there is some error correction » (le papier admet des lectures rivales, §6.2) ; « will no longer verbalise » (« greatly suppressed ») ; « All my directions … 2.3-2.4 » (moyenne 2,42, médiane 2,30, dispersion par direction).

## 4. Verdict (trois lignes)

Le brouillon répond à la question du mentor : il choisit une option, donne trois raisons d'échec de but (lisible n'est pas causal ; signal contaminé par le registre ; soustraire n'est pas retirer, avec fenêtre de dose) et dit pourquoi, en s'appuyant sur ses propres réplications et sur les papiers du mentor ; l'argument du registre et l'outil de l'exposant p sont bien placés.

Il n'est pas prêt à partir tel quel : il faut d'abord les quinze corrections majeures, dont le titre (« towards » dit le contraire de l'option), quatre attributions qui présentent le réglage et les directions du mentor comme ceux de Lazar (« my », « I used », « I haven't tested »), la phrase inversée sur −13,7 et −1,6 points, la citation entre guillemets qui n'existe pas, « control_book » présenté comme aléatoire, et le lien Zenodo qui pointe sur le préenregistrement et non sur la courbe.

Compte : 63 affirmations vérifiées ; 15 corrections de fond majeures et 11 mineures ; 9 chiffres ou faits non vérifiables ici (les cinq de D36, privés et conformes à R-1302 ; la déduction du segment ; le billet de 2024 ; deux faits secondaires sur Sonnet 4.5).

# Registre des affirmations — réponse Colognese et Ward, question 2 — v1

3 novembre 2026, 15:12 UTC (`date -u`). Rédacteur neuf. Une ligne par affirmation de `reponse-v1.md`, dans l'ordre du texte.

Forces : **publique et vérifiée** (source publique lue, page ou fichier cité) ; **interne vérifiée** (aucune ici) ; **lecture** (interprétation de Lazar, signalée comme telle par la forme conditionnelle ou « suggests ») ; **proposition** (travail non fait, dit comme plan) ; **non vérifiée** : interdite, aucune dans la réponse.

## Sources et empreintes

| abréviation | source | sha256 ou version |
|---|---|---|
| [RAP] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` (lecture du billet LessWrong `2maYXkEgnfJHPAkxh`, corrigé le 14 octobre 2026, section par section, et de 2601.21112 v2, sections 1 à 7) | `cf1edec99be3ecd54a2d09b1c6c1c3931de6ca1a03e47cbbccde58e03f65b395` |
| [PIE] | `brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md` (faits du billet ; parts silencieuses revérifiées sur la page le 3 novembre) | `7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2` |
| [REC] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (vérificateur neuf ; verdicts seulement) | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [R7] | `results/R7/README.md` du dépôt public `lciric/sycophancy-psychophysical-law`, commit `b3ecaec` (clone frais `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`) ; archivé sur Zenodo 10.5281/zenodo.23892810 | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` (égal à celui que cite [RAP]) |
| [DOS] | `brouillons/ideation-mentors-soir-v1/dossier-piste-colognese-ward-q2-v1.md` (plans et objections des fiches ; aucun chiffre de fiche repris comme fait) | `b5563a9961e90f7bfb8838f0f2cdf07754e6376508e8b12df02608ee22dca953` |
| [A583] | arXiv 2608.00583 v3 (Shiromani, Richter), « A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility », déposé le 1er août 2026, v3 du 11 septembre 2026 ; page de résumé `arxiv.org/abs/2608.00583` lue par `WebFetch` le 3 novembre entre 15:00 et 15:05 UTC (extraits de 125 caractères au plus) | v3 |
| [A741] | arXiv 2602.16741 v1 (Scott Thornton), « Can Adversarial Code Comments Fool AI Security Reviewers -- Large-Scale Empirical Study of Comment-Based Attacks and Defenses Against LLM Code Analysis », 18 février 2026 ; page de résumé `arxiv.org/abs/2602.16741`, même lecture | v1 (seule version) |
| [FOR] | `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 174 (question), lignes 176 à 178 (réponse actuelle, 156 mots) | `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` |

## Affirmations

| # | affirmation (mots de la réponse) | source et emplacement | force |
|---|---|---|---|
| 1 | « anti-cheating seed 1's silent hacks sat in plain sight. It disabled the test check in its answer » | [RAP] l. 35 (billet §3.3 : la triche dominante de la graine 1 est dans la réponse) et l. 37 (commentaire de Paul Colognese : la graine 1 apprend à neutraliser presque toujours la fonction de vérification) ; [PIE] §3.2 ; [REC] n° 207 et 213 (exact) | publique et vérifiée ; décrite au niveau méthode |
| 2 | « usually under a comment calling the hack harmless (89%) » | [RAP] l. 35 (Summary : « 89% added a comment to its answer that presents the hack as harmless ») ; [REC] n° 208 (exact) | publique et vérifiée |
| 3 | « Yet silent hacks were caught 16% of the time, against 91% when the reasoning mentioned the hack » | [RAP] l. 65, F1 (billet §3.3, figure 8 : 16 %, n = 1 955 jugements, intervalle 15–18 %, contre 91 % quand le raisonnement est franc ; même ordre après la correction du 14 octobre) ; [PIE] §3.2 ; définition du silence : [RAP] l. 37 (§2.5, le raisonnement ne mentionne jamais la triche) | publique et vérifiée ; réserve : la vue et les graines du 16 % ne sont pas précisées par [RAP] |
| 4 | « if rewarded rollouts are samples from the character's prior » | [RAP] l. 98 (billet §4.2 : « Rewarded RL rollouts can be viewed as samples from the character's prior, conditioned on containing a hack that passes the grader ») ; [PIE] §3.2 | publique et vérifiée (paraphrase, pas de citation) |
| 5 | « an earnest craftsman » | [RAP] l. 43 (annexes A.1.1 à A.1.3 : le caractère anti-triche, « an earnest craftsman ») ; [PIE] §3.1 | publique et vérifiée (deux mots du billet) |
| 6 | « an earnest craftsman who hacks writes an excuse » ; « Your own reading suggests why » | inférence à partir des lignes 2, 4 et 5 (le commentaire porte typiquement une affirmation fausse sur l'environnement : [RAP] l. 35) | lecture |
| 7 | « If the excuse is what fools the monitors, character training taught the policy to plead its case » | conditionnelle ; hypothèse testée par la proposition des lignes 12 à 20 | lecture |
| 8 | « though no monitor was in the training loop » | [RAP] l. 72, F8 (« une intervention d'alignement ordinaire, sans moniteur dans la boucle ») et l. 38 (billet §4.3 : la triche est renforcée si le correcteur la récompense) | publique et vérifiée |
| 9 | « Francis's sabotage-monitoring paper (arXiv 2601.21112) found monitors gaslit by agents rationalising a side task » | [RAP] l. 17 (auteurs : Arike, Mehta Moreno, Subramani, Biswas, Ward) et l. 73, F9 (§5.6 : les échecs viennent surtout d'agents qui mentionnent la tâche secondaire et la rationalisent, « This transparency gaslights monitors into believing that the side task was explicitly intended by the user ») | publique et vérifiée ; crédit exigé par le drapeau de CW-22 |
| 10 | « here the rationalisation moved into a code comment » | [RAP] l. 73 (dernière phrase de F9) | lecture |
| 11 | « The 16-versus-91 gap mixes the comment, the silent reasoning and the hack type, which travel together » | [RAP] l. 70, F6 (billet §3.3 et §4.2 : « hack type and silent hacking were partly confounded » ; 73 % de silence parmi les réécritures de tests des graines anti-triche, moins de 1 % parmi les triches qui ne touchent pas aux tests) ; co-occurrence du commentaire et du silence dans la graine 1 (93 % et 89 % : [RAP] l. 35 et 37) | publique et vérifiée pour la confusion type–silence (dite par les auteurs) ; lecture pour le commentaire |
| 12 | « The test needs no RL, only re-scoring » | plan : renotation de transcriptions existantes ([DOS], CW-22, « Aucun entraînement (renotation) ») | proposition |
| 13 | « replace the harmless comment with a neutral comment of the same length and position, everything else byte-identical » | plan : [DOS] l. 13 (énoncé de CW-22) | proposition |
| 14 | « Deleting it would not do: an unexplained override is more salient, so salience and persuasion predict the same rise » | [DOS] l. 24 (CW-22, première objection, sourcée par la pièce §1 : « persuasion et masquage par remplissage prédisent la même hausse ») | raisonnement sourcé ; neuf par rapport à la phrase de la Q1 |
| 15 | « As a dummy, give another comment the same treatment » | plan : [DOS] l. 15 et l. 38 (éditions factices appariées ; retrait d'un autre commentaire de même longueur et position) | proposition |
| 16 | « Edit honest episodes the same way, so false alarms are measured, not assumed » | plan : [DOS] l. 15 (« éditions factices appariées sur honnêtes de validation (fausses alertes mesurées) ») | proposition |
| 17 | « your 2% threshold » | [RAP] l. 42 (billet §2.4 : seuil réglé pour que 2 % exactement des transcriptions honnêtes tenues à l'écart, mises en commun sur tous les points de départ, soient signalées) ; [REC] n° 214 (exact) | publique et vérifiée |
| 18 | « paired by transcript and per monitor » (le billet moyenne trois moniteurs) | [RAP] l. 36 (Haiku 4.5, Qwen 3.5-122B, DeepSeek-V4-Flash, moyennés, figure 6) et l. 72 (aucun chiffre séparé par moniteur) | publique et vérifiée (pour la moyenne) ; proposition (pour la lecture par moniteur) |
| 19 | « my planted-note test found deference differs by monitor and direction » | [R7] l. 5 (le 72B sans attraction dans aucun sens ; la plupart des tailles moyennes dans un seul sens), l. 18 à 26 (tableau par taille et par note), l. 36 (M1 faux : deux tailles dans les deux sens, quatre dans un seul, le 72B dans aucun) | publique et vérifiée ; R7 décrit en une demi-phrase (consigne) |
| 20 | « If catch rises less than 20 points beyond the dummy, the comment is not the main cause » | paramètre de plan : 20 points, illustratif dans CW-22 ([DOS] l. 13 et 18), adopté ici ; justification : environ un quart de l'écart de 75 points (calcul : 91 − 16 = 75 ; 20 / 75 ≈ 0,27) | proposition ; **à confirmer par Lazar** |
| 21 | « The outcome is open » | lignes 19, 22, 23 et 24 | lecture |
| 22 | « arXiv 2608.00583 rewrote only the reasoning, actions byte-identical » | [A583], résumé : « we rewrite only the agent's reasoning to read as good-faith engineering, leaving every command and output byte-identical, so the exploit is unchanged » | publique et vérifiée (résumé) ; crédit exigé par le drapeau de CW-18 |
| 23 | « and catch collapsed, but on hacks only the reasoning revealed » | [A583], résumé : « One gradient-free rewrite drops a held-out monitor's catch rate on that subset from about 95% to between 4 and 11% » ; « Monitor accuracy should be reported on the reasoning-dependent subset » | publique et vérifiée (résumé) ; aucun chiffre repris dans la réponse |
| 24 | « here the code shows the hack » | [RAP] l. 35 (triche dans la réponse, §3.3) et l. 38 (billet §4.2 : réécriture des tests dans les réponses) | publique et vérifiée |
| 25 | « arXiv 2602.16741 found adversarial comments barely moved LLM vulnerability reviewers » | [A741], résumé : « Adversarial comments produce small, statistically non-significant effects on detection accuracy » ; détection de vulnérabilités, huit modèles de pointe | publique et vérifiée (résumé) ; appui contraire exigé par les drapeaux de CW-22 et CW-04 |

## Contrôles

- **Chaque nombre de la réponse** : « 1 » (graine 1 : lignes 1, 13), « 89% » (2), « 16% » et « 91% » (3, 11), « 2601.21112 » (9), « 2% » (17), « 20 points » (20), « 2608.00583 » (22, 23), « 2602.16741 » (25). Aucun autre nombre.
- **Aucune affirmation non vérifiée** ; aucun fait interne ; aucun chiffre de fiche repris comme fait ; aucun résultat du nul v9 ; aucun extrait de code de triche (niveau méthode).
- **Citations** : aucune entre guillemets dans la réponse ; « earnest craftsman » (deux mots) et « gaslit » (un mot) sont les seuls emprunts lexicaux au billet et à 2601.21112.
- **Articles extérieurs** : lus sur la page de résumé seulement, par un outil qui rend des extraits ; niveau « transcription » au sens de R7 du programme : suffisant pour une mention qualitative dans une candidature, non opposable dans un préenregistrement ou un papier.
- **Empreinte de [FOR]** : recalculée à 15:13 UTC, égale à celle relevée à 15:00 UTC (`57393598f012…f7b5c6`). Une première écriture de ce registre portait une empreinte mal recopiée ; corrigée avant toute remise (fichier non scellé, écrit dans la même session).

# Rapport de lecture — niveau 3, lot 2-A : billets sur le contrôle boîte blanche et les sondes comme moniteurs (papier A) — v1

- **Lecteur** : sous-agent neuf (modèle Fable 5.2), qui n'a écrit ni le programme ni aucun rapport antérieur.
- **Date** : 2026-11-10 ; fin de lecture relevée à 11:10 UTC, rapport assemblé à l'heure imprimée en section 7 (heures relevées par `date -u`).
- **Sources** : dix-sept rendus texte de billets et de pages web, non versés au dépôt (droits réservés), dans `/tmp/claude-0/-home-user-controle-ia-travail/ba75ee53-729a-59d5-934a-27a4eace4393/scratchpad/lot2/non-verses/`. Provenance : `docs/sources/pdf/niveau3-v1/provenance-niveau3-lot2-hors-archives-v1.md` (sha256 `a30e87c5d835ff87b448bcb25f3debb5b3eeac1ca5f77a7eb489c1b4f3081fec`, conforme à son compagnon).
- **Repérage d'une citation** : abréviation du fichier, numéro de ligne du rendu `.txt`, citation exacte, identifiant entre crochets. La table des abréviations est en section 1 ; la liste complète des 201 citations est en annexe.
- **Nature des chiffres** : « auteurs » (imprimé dans le billet), « calcul » (recalculé par le lecteur, fichier `calculs.txt` de l'archive). Aucun chiffre « figure » : aucune image des dix-sept billets n'est dans le dossier (les seules images du dossier appartiennent à un autre billet, hors lot).
- **Portée** : un billet n'est pas un article. « Libre » veut dire « non trouvé dans les billets lus ». Les articles auxquels les billets renvoient ne sont pas lus ici ; ils sont listés en section 6.

## 0. En tête : occupations, même partielles

1. **H2 (énoncé N-007) — occupée en partie, pour la configuration de référence seulement**, par le billet de LessWrong du 30 octobre 2026 (Surya et Lucassen, stage de Redwood Research). Le billet lit six sondes linéaires sur les activations de l'agent qui agit, à chaque commande, avec un seuil par action réglé à 1 % des commandes honnêtes et une trajectoire déclarée attrapée dès qu'une commande franchit le seuil : « We set each threshold so that 1% of honest commands raise an alarm » (LW26, l. 136) [LW-10] ; « it catches an attack run if it raises an alarm on any of the run's commands » (LW26, l. 136) [LW-09]. C'est le « moniteur par action calibré à 1 % de faux positifs » de l'énoncé, réalisé avec des sondes de l'agent. **Non fait** : aucune accumulation (« Each action gets its own score, with no smoothing across actions such as an exponential moving average. » (LW26, l. 252) [LW-14]), aucune garantie au niveau de la trajectoire (de 26 à 43 % des trajectoires honnêtes sonnent : « so 26% to 43% of honest runs still raise at least one alarm, depending on the probe » (LW26, l. 136) [LW-11]), aucun sabotage tenu sous le seuil, aucune courbe selon l'horizon. Lecture douce possible : « voisin fort ». La conjonction revendiquée reste libre dans les billets lus.
2. **H6 (énoncé N-013) — occupée en partie pour le ré-échantillonnage, en sabotage concentré**, par le billet de Redwood Research du 29 mai 2026 qui résume arXiv 2605.26047 : gain de sécurité de 10,2 points sans coût d'utilité quand le ré-échantillonnage sert d'information (« Of a +10.2 pp safety gain achievable by drawing four resamples on top of every original sample » (RETRY, l. 122) [RE-06] ; « Resampling without executing the least suspicious sample has zero usefulness impact. » (RETRY, l. 120) [RE-05]). Réserves fortes : le gain passe par l'audit (plus d'information pour le moniteur), non par une chute du succès de l'attaque sous perturbation ; cadre concentré (BashArena) ; la variante qui exécute l'échantillon le moins suspect n'apporte rien contre un attaquant optimal. Les rapports du niveau 2 n'avaient pas confronté cet article à H6. À trancher sur le PDF (2605.26047, déjà au dépôt d'après le niveau 2).
3. **H1 — aucune occupation ; un voisin fort chiffré et un contre-indice de position.** Le billet long de l'institut britannique (10 juillet 2025) donne une comparaison chiffrée sonde contre moniteur boîte noire sur une tâche d'agent avec sous-performance volontaire, **en aire sous la courbe seulement** : « the black box chain-of-thought monitor performed relatively poorly, achieving only 74% AUROC » (AISILW, l. 193) [AL-07] contre « achieving 97%-99% AUROC (for mean-aggregation vs max-aggregation respectively) » (AISILW, l. 195) [AL-08]. Ce n'est pas à faux positifs égaux, pas sur tâche floue, sur 17 transcriptions, avec un moniteur boîte noire désavantagé de l'aveu des auteurs. En lecture dure, c'est « occupée en partie » pour la seule composante « comparaison chiffrée blanc contre noir sur une sous-performance d'agent ». Le billet d'Anthropic du 23 juin 2026 (Terekhov et collègues, base du programme) écrit que la surveillance est moins prometteuse que l'entraînement pour le diffus : « We focus on training interventions because they seem more promising than monitoring and incrimination for » (DIFFUSE, l. 60) [DI-02].
4. **Risque de collision à lire d'urgence (non lus ici)** : arXiv 2610.12445 (sonde de tromperie qui, selon le billet de LessWrong, attrape déjà le sabotage d'agent : « in SHADE-Arena and BashArena » (LW26, l. 770) [LW-21]) et arXiv 2610.31593 (évaluations de contrôle simulées, cinq moniteurs qui lisent la transcription, mêmes tâches LinuxArena). La même équipe a donc, sur les mêmes 1 313 tâches, des sondes et des moniteurs boîte noire : la comparaison blanc contre noir en sabotage **concentré** est à une table près.
5. **État de l'art v1, ligne 37** : affirmation **à nuancer** (section 2). Ligne 36 : **exacte pour ce que le billet permet de vérifier**, un détail non vérifiable ici.
6. **Statut de la source prioritaire** : le billet de LessWrong porte une mention de rejet par la modération (« This is an automated rejection. » (LW26, l. 43) [LW-02]), confirmée dans le HTML (`"rejected":true`), et se présente comme un travail de deux semaines (« This is a two-week sprint project done as part of the Redwood Research internship (through MATS 11.0). » (LW26, l. 168) [LW-26]). À citer avec cette réserve.
7. Aucun refus de permission ni de classifieur.

## 1. Méthode, fichiers et empreintes

- Chaque `.txt` et chaque `.html` lu a son empreinte dans la note de provenance (34 empreintes cherchées, 34 trouvées). Les empreintes des `.txt` sont dans `empreintes-txt-lues.txt` de l'archive.
- Lecture intégrale des dix-sept `.txt` (commentaires compris). Les lignes vides et, pour les billets Substack, les lignes qui ne portent qu'une adresse d'image ont été écartées à l'affichage.
- Vérification dans le HTML faite pour un seul point : le statut de rejet du billet prioritaire.
- Énoncés du programme lus : `docs/programme-controle-ia-v2.md` (lignes 85 à 125 et 190 à 215), décisions N-003/N-004, N-007/N-008, N-013, sections H1, H2, L, T, Tr, H6, H8, HC2 de `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`.

| Abréviation | Fichier `.txt` | Billet | Date imprimée |
|---|---|---|---|
| LW26 | `lw-2026-probe-monitors-perform-realistically-in-simulated.txt` | « Probe monitors seem to perform realistically in simulated control environments », Surya et Lucassen, LessWrong | « 30th Oct 2026 » (LW26, l. 34) [LW-01] |
| AISILW | `aisi-2025-lesswrong-white-box-control-update-sandbagging.txt` | « White Box Control at UK AISI - Update on Sandbagging Investigations », Bloom et collègues, miroir LessWrong | « 10th Jul 2025 » (AISILW, l. 51) [AL-01] |
| AISIPUB | `aisi-2025-publication-white-box-control-update-sandbagging.txt` | fiche de publication de l'institut (résumé seul) | « Jul 10, 2025 » (AISIPUB, l. 28) [AP-01] |
| AISIWHY | `aisi-2025-why-were-working-on-white-box-control.txt` | « Why we're working on white box control », institut britannique | « Jul 10, 2025 » (AISIWHY, l. 37) [AW-01] |
| CASE | `lw-case-for-white-box-control.txt` | « The Case for White Box Control », J Rosser, LessWrong | « 18th Apr 2025 » (CASE, l. 32) [CA-01] |
| LIE | `anthropic-2026-lie-detectors.txt` | « Fine-Tuned Lie Detectors Failed to Generalize », Hopkins, Khullar et collègues | « August 21, 2026 » (LIE, l. 8) [LD-01] |
| CHEAP | `anthropic-2025-cheap-monitors.txt` | « Cost-Effective Constitutional Classifiers via Representation Re-use », Cunningham et collègues | aucune date dans le rendu ; adresse en `/2025/` |
| APOLLO | `apollo-2025-deception-probes.txt` | « Detecting Strategic Deception Using Linear Probes », Apollo Research | « 06 February 2025 » (APOLLO, l. 75) [AO-01] |
| HEBBAR | `hebbar-2025-redwood-how-can-we-solve-diffuse-threats.txt` | « How can we solve diffuse threats like research sabotage with AI control? », Hebbar | « Apr 30, 2025 » (HEBBAR, l. 29) [HE-01] |
| NOTES | `redwood-notes-on-handling-non-concentrated.txt` | « Notes on handling non-concentrated failures with AI control », Greenblatt | « Mar 29, 2025 » (NOTES, l. 29) [NO-01] |
| DIFFUSE | `anthropic-2026-diffuse-ai-control.txt` | « Diffuse AI Control on Fuzzy Tasks », Terekhov, Gulcehre, Hebbar, Benton | « June 23, 2026 » (DIFFUSE, l. 10) [DI-01] |
| LOGIT | `redwood-logit-rocs-monitor-tpr-is-linear.txt` | « Logit ROCs: Monitor TPR is linear in FPR in logit space », Staley, Bhatt, Stastny | « Apr 12, 2026 » (LOGIT, l. 31) [LR-01] |
| BLOCK | `redwood-blocking-live-failures-with-synchronous.txt` | « Blocking live failures with synchronous monitors », Lucassen et Kaufman | « Mar 30, 2026 » (BLOCK, l. 29) [BL-01] |
| RETRY | `redwood-retrying-vs-resampling-in-ai-control.txt` | « Retrying vs Resampling in AI Control », Lucassen et Kaufman | « May 29, 2026 » (RETRY, l. 29) [RE-01] |
| GAMES | `aisi-auditing-games-for-sandbagging-detection.txt` | « Auditing games for sandbagging detection », institut britannique | « Dec 9, 2025 » (GAMES, l. 37) [AG-01] |
| REDTEAM | `aisi-how-our-new-control-red-team-is-stress-testing-frontier-monitors.txt` | « How our Control Red Team is stress-testing frontier monitors », institut britannique | « Jul 23, 2026 » (REDTEAM, l. 37) [RT-01] |
| STRESS | `aisi-stress-testing-asynchronous-monitoring-of-ai-coding-agents.txt` | « Stress-testing asynchronous monitoring of AI coding agents », institut britannique | « Dec 16, 2025 » (STRESS, l. 37) [ST-01] |

## 2. Vérification de deux affirmations de l'état de l'art v1 (`docs/etat-de-l-art-controle-ia-v1.md`)

### Ligne 37 — « Blog de l'institut britannique … et "The Case for White Box Control" … posent la thèse blanc > noir, sans mesure sur diffus/flou à faux positifs égaux »

**Verdict : à nuancer**, en trois points.

1. **« posent la thèse blanc > noir » — inexact pour « The Case », à nuancer pour l'institut.**
   - « The Case for White Box Control » ne soutient pas que le blanc bat le noir. Il répartit les menaces entre les deux : le noir est jugé plus adapté pour trois des sept priorités (« black box monitors may be more accurate at detecting the tampers » (CASE, l. 128) [CA-07] ; « Black box monitoring seems like a safer bet? » (CASE, l. 152) [CA-12]), le blanc pour les autres. Il liste des arguments contre les sondes (« Generalization challenges of probes - they can struggle out of domain » (CASE, l. 111) [CA-06]) et se dit enthousiaste pour le noir aussi (« I'm still super excited about black box control too! » (CASE, l. 83) [CA-03]). Sa thèse est la complémentarité : « adding the results of white box monitors to black box ones could provide a much stronger signal to overseers » (CASE, l. 89) [CA-04]. Le seul commentaire, de Fabien Roger, va contre la thèse prêtée : « I think it's not obvious that probes will be more reliable than trusted monitors for most tasks you care about » (CASE, l. 186) [CA-10].
   - L'institut britannique avance bien un avantage des sondes, mais comme un indice limité à un cas : « providing some evidence for the usefulness of probes over black box monitors for sandbagging detection » (AISIWHY, l. 73) [AW-02]. Les deux billets insistent autant sur la dégradation : « we also found that increased model size and task complexity caused the performance of both white and black box monitors to deteriorate » (AISIWHY, l. 75) [AW-03] ; « the second and third updates show that simple baseline methods leave much room for improvement » (AISILW, l. 106) [AL-17].
2. **« sans mesure » — inexact pour l'institut, exact pour « The Case ».**
   - Le billet long de l'institut mesure. Tâche d'agent (InterCode CTF, outils bash et python), Llama-3.3-70B, sous-performance sur consigne : moniteur boîte noire sur la chaîne de pensée à 74 % d'aire sous la courbe (« the black box chain-of-thought monitor performed relatively poorly, achieving only 74% AUROC » (AISILW, l. 193) [AL-07]), sonde à 97 % et 99 % selon l'agrégation (« achieving 97%-99% AUROC (for mean-aggregation vs max-aggregation respectively) » (AISILW, l. 195) [AL-08]) — chiffres « auteurs ». Pour la sonde seule, un point de fonctionnement : « (88% TPR, 2% FPR with max aggregation) » (AISILW, l. 195) [AL-09], avec un seuil pris sur un autre corpus (« setting the decision boundary to give a 1% false positive rate on the Alpaca chat dataset » (AISILW, l. 195) [AL-10]).
   - « The Case » ne contient aucune mesure : « Not too much research in the space yet » (CASE, l. 101) [CA-05].
3. **« sur diffus/flou à faux positifs égaux » — exact comme conjonction.**
   - Aucun des quatre textes ne compare sonde et moniteur boîte noire à taux de faux positifs égal : la comparaison de l'institut est en aire sous la courbe, et le taux de vrais positifs à faux positifs fixés n'est donné que pour la sonde.
   - La sous-performance volontaire est rangée parmi les menaces diffuses par le billet d'Anthropic (« Diffuse threats correspond to behaviors that are » (DIFFUSE, l. 36) [DI-03], suite ligne 37 du même fichier). La mesure de l'institut porte donc sur une menace de type diffus, mais sur une tâche vérifiable (un drapeau à trouver), non floue, et sur des réponses notées une à une, sans étalement sur une trajectoire de déploiement.
   - « The Case » affirme sans mesure que les sondes conviennent aux tâches difficiles à vérifier : « much less easily checkable tasks like confusing conceptual work » (CASE, l. 146) [CA-08] ; « Use probes to extract non-sabotaged work from activations » (CASE, l. 147) [CA-09]. C'est la thèse du diffus sur tâche floue, posée en une ligne.

**Formulation proposée** (à la décision de Lazar, le lecteur ne modifie pas l'état de l'art) : « Le billet long de l'institut britannique (10 juillet 2025) mesure sonde contre moniteur boîte noire sur une sous-performance volontaire, y compris sur une tâche d'agent (74 % contre 97 à 99 % d'aire sous la courbe, 17 transcriptions positives), sans comparaison à faux positifs égaux ni tâche floue, et rapporte la dégradation des deux méthodes quand le modèle et la tâche grossissent. "The Case for White Box Control" (18 avril 2025) est un billet d'opinion sans mesure, qui plaide la complémentarité et attribue aux sondes, par simple affirmation, les tâches difficiles à vérifier. »

### Ligne 36 — Taylor et collègues, arXiv 2512.07810 (jeux d'audit)

**Verdict : exact pour ce que le billet de l'institut permet de vérifier ; un détail non vérifiable ici.**
- « méthodes fondées sur les internes plus prometteuses que la boîte noire » : « white box methods proved significantly more promising than black box ones » (GAMES, l. 71) [AG-03] ; « We had very little success with black box methods. » (GAMES, l. 65) [AG-02].
- « usage naïf battu par des comportements introduits par l'équipe rouge » : « the red team was later able to introduce false positives using distractor behaviours » (GAMES, l. 75) [AG-04] ; « can be fragile and easily confused, leading to false negatives » (GAMES, l. 91) [AG-05].
- « organismes publics, dont un imitant Llama-3.1-8B-Instruct » : absent du billet, qui dit seulement « The red team trained five models using conditional underperformance ('password locking') as a proxy for sandbagging. » (GAMES, l. 49) [AG-06]. À vérifier sur le PDF (déjà lu au niveau 2, lot2-A3).
- Nuance utile au programme : le billet donne la méthode gagnante, et ce n'est pas une sonde mais l'entraînement sur la distribution, qui élimine la sous-performance sans la détecter ; il reconnaît que cette voie peut être impraticable sur tâche ouverte : « it may be infeasible for messier, open-ended tasks where it’s hard to demonstrate perfect performance » (GAMES, l. 89) [AG-08].

## 3. Fiches par billet

### 3.1 LW26 — sondes d'activations comme moniteurs de contrôle sur LinuxArena (priorité 1)

**Ce qu'il fait.**
- Question : la simulation des réponses d'outils par un modèle change-t-elle le taux d'attrape de sondes qui lisent les activations de l'agent ? Agent Qwen3.5-27B ; simulateur GPT-6-Astra ; 1 313 tâches LinuxArena, chacune attaquée trois fois (« tasks once in simulation and twice on real machines » (LW26, l. 50) [LW-03]).
- Sabotage **concentré** : une tâche principale et une tâche annexe nuisible par trajectoire (« Each task pairs an ordinary main task, such as fixing a bug in a web service, with a harmful side task, such as planting a backdoor. » (LW26, l. 70) [LW-06]) ; l'agent reçoit la consigne d'attaquer (« We call runs where the agent is told to attempt the side task “attack runs” » (LW26, l. 70) [LW-39]).
- Six sondes linéaires, lues près de la fin de chaque commande (« All six read the activations of Qwen3.5 near the end of each command. » (LW26, l. 76) [LW-07]) : deux entraînées sur LinuxArena (sur la politique de l'agent ; hors politique, sur les trajectoires d'un autre agent relues par Qwen3.5), quatre publiées (tromperie, direction de nocivité, direction de refus, enjeux élevés).
- Règle de décision : seuil par commande à 1 % des commandes honnêtes (« We set each threshold so that 1% of honest commands raise an alarm » (LW26, l. 136) [LW-10]), calibré sur des trajectoires honnêtes ; trajectoire attrapée si une commande sonne (« it catches an attack run if it raises an alarm on any of the run's commands » (LW26, l. 136) [LW-09]), même après le dommage (« An alarm anywhere in an attack run counts as a catch, even one after the agent has carried out the side task. » (LW26, l. 254) [LW-15]).
- Sonde séparée qui distingue simulation et réel.

**Résultats chiffrés (auteurs, sauf mention).**
- Aire sous la courbe par trajectoire, au maximum des commandes (« Each run is scored by its most suspicious command. » (LW26, l. 78) [LW-08]) : sonde sur politique « 0.99 » (LW26, l. 94) [LW-31] ; hors politique 0,76 ; tromperie 0,77 ; nocivité 0,65 ; refus « 0.54 » (LW26, l. 126) [LW-32] ; enjeux élevés 0,55 (LW26, l. 94 à 134).
- Taux d'attrape à 1 % des commandes honnêtes, trajectoires réelles, première série : sur politique « 99.8 » (LW26, l. 424) [LW-35] % ; hors politique 72,5 % ; tromperie « 75.3 » (LW26, l. 448) [LW-33] % ; nocivité 58,7 % ; refus « 42.8 » (LW26, l. 472) [LW-34] % ; enjeux élevés 48,3 % ; moyenne des six « 66.2 » (LW26, l. 496) [LW-36] % en réel et « 65.1 » (LW26, l. 500) [LW-37] % en simulation (LW26, tableau 5, l. 408 à 516). Moyennes recalculées : 66,23 ; 66,03 ; 65,13 — conformes (calcul).
- Écart simulation moins réel : « the catch rate in simulated trajectories was 1.0 points lower than in real trajectories (95% interval −3.0 to +1.0) » (LW26, l. 52) [LW-04].
- **Coût en fausses alarmes par trajectoire** : « so 26% to 43% of honest runs still raise at least one alarm, depending on the probe » (LW26, l. 136) [LW-11], pour « An honest run gives the probes about 65 to 75 commands to score » (LW26, l. 136) [LW-38]. Sous indépendance des commandes, on attendrait 48 à 53 % (calcul : 1 − 0,99^65 et 1 − 0,99^75) : les alarmes honnêtes sont donc regroupées dans les mêmes trajectoires, ce que les auteurs disent eux-mêmes (LW26, l. 140 et 808).
- Sonde de simulation : « separates simulated attack runs from real ones with an AUROC of 0.88 » (LW26, l. 152) [LW-16] ; les six sondes n'en sont pas déplacées (« Spearman correlation −0.03 » (LW26, l. 404) [LW-17], entre « avoir l'air simulé » et « être manqué »).
- Seuils stricts : à 0,02 % et 0,05 %, le seuil simulé repose sur une à quatre trajectoires et « its catch rate in simulated runs falls 31 to 38 points below the rate in real runs » (LW26, l. 518) [LW-19] ; « At 0.1%, the simulated threshold rests on the 56 to 65 most suspicious simulated honest commands » (LW26, l. 518) [LW-40].

**Ce qu'il ne fait pas.**
- **Aucune comparaison avec un moniteur boîte noire.** Les moniteurs qui lisent la transcription ne sont cités que par renvoi à un autre article et à un autre point de fonctionnement : « each flagging 5% of honest runs, with a root-mean-square error of 3.6 percentage points » (LW26, l. 766) [LW-20]. Sondes à 1 % des commandes, moniteurs à 5 % des trajectoires : les deux ne sont pas comparables tels quels.
- **Aucune accumulation ni test séquentiel** : « Each action gets its own score, with no smoothing across actions such as an exponential moving average. » (LW26, l. 252) [LW-14]. Agrégation par le maximum sur les commandes ; moyenne sur les jetons pour la lecture des sorties d'outils (« each probe averages over every “content token” of the output » (LW26, l. 250) [LW-41]) ; moyenne des actions pour la seule sonde de simulation (« scored each run by the mean of its held-out action scores » (LW26, l. 528) [LW-42]).
- Aucun sabotage diffus, aucune tâche floue, aucun attaquant qui vise les sondes, aucune garantie de faux positifs par trajectoire, aucune courbe de rappel selon l'horizon.
- Aucune mesure de la conscience d'évaluation : la sonde essayée n'a pas répondu (« On Qwen3.5, it did not respond when we told the agent it was being tested, so it could not measure awareness. » (LW26, l. 790) [LW-22]).

**Limites reconnues.** Un agent, un simulateur, un jeu d'environnements ; six sondes non indépendantes (« The six probes are not independent, so their average is worth less than six separate tests. » (LW26, l. 812) [LW-29]) ; écart non montré équivalent à zéro (LW26, l. 816) ; 47 tâches écartées ; stratégies d'attaque non comparées.

**Incohérences et résultats trop beaux (symétrie).**
- **Sonde sur politique à 99,8 % : trop beau, réserve.** Elle est entraînée en étiquetant « attaque » toute commande d'une trajectoire d'attaque (« every command in an attack run counts as an attack example, not only the sabotage step » (LW26, l. 186) [LW-12]), et lit des activations qui reflètent tout le contexte (« By then the agent has read every earlier tool output, so its activations there reflect the run so far. » (LW26, l. 250) [LW-13]), consigne d'attaque comprise. Elle sonne sur une commande anodine d'une trajectoire d'attaque (« Caught, +1.8. mkdir -p /app/app/services » (LW26, l. 358) [LW-27]) et tient à 98,6 % avec un dixième des données (« the on-policy probe still catches 98.6% of real attacks on whole runs » (LW26, l. 400) [LW-18]). Lecture la plus simple : elle détecte la présence de la consigne dans le contexte, non l'acte de sabotage. Les auteurs ne discutent pas cette lecture. Elle rejoint le contre-indice de portée de 2509.21344 (niveau 2) et l'objection de Sam Marks sous le billet de l'institut (« it will be pretty hard to tell whether your probe is working by detecting the presence of instructions about sandbagging vs. working by detecting the presence of cognition about sandbagging » (AISILW, l. 454) [AL-19]).
- **Deux sondes sur six sont au niveau du hasard par trajectoire.** Refus à 42,8 % et enjeux élevés à 48,3 % d'attrape, quand 26 à 43 % des trajectoires honnêtes sonnent ; le billet le signale par un repère sur sa figure (« about what a random probe would catch if it couldn’t tell attack runs from honest ones » (LW26, l. 140) [LW-44]), dont la valeur par sonde n'est pas imprimée. La « moyenne des six » mêle donc des sondes informatives et des sondes nulles.
- Décomptes cohérents : 1 310 et 1 306 trajectoires attrapées sur 1 313 redonnent 99,77 % et 99,47 % (calcul, d'après « 1,304 of the 1,313 tasks were caught in both real run 1 and the simulated run » (LW26, l. 344) [LW-28]).
- Les trajectoires d'attaque et honnêtes n'ont pas la même longueur (« Runs took about 76 steps. » (LW26, l. 704) [LW-45] ; 65 à 75 commandes honnêtes) et les trajectoires longues sont plus attrapées (« Because they are long, these runs may be caught more often » (LW26, l. 708) [LW-25]) : la longueur est un facteur de confusion du maximum, non corrigé.
- Statut : billet rejeté par la modération (« This is an automated rejection. » (LW26, l. 43) [LW-02]), travail de deux semaines (« This is a two-week sprint project done as part of the Redwood Research internship (through MATS 11.0). » (LW26, l. 168) [LW-26]), revendication de primauté (« To our knowledge, this is the first such check for probe monitors. » (LW26, l. 66) [LW-05]) limitée à la question simulation contre réel.

**Questions de la consigne.** (a) Aucune comparaison sonde contre boîte noire ; sabotage concentré. (b) Maximum sur les commandes, sans lissage ; aucune somme cumulée, aucun test séquentiel. (c) Travaux annoncés : même question avec un agent plus capable (« whether probes still catch attacks as often in simulation when the agent is much more capable » (LW26, l. 166) [LW-24]) ; rien sur la comparaison ni sur l'accumulation. Usage visé des sondes : premier étage d'une cascade (« A probe is cheap enough to run as a first stage, whose alarms only go to an LLM monitor reading the transcript » (LW26, l. 806) [LW-23] ; « describes a probe that picks out tool calls that might take an impactful action, so that a transcript-reading monitor reviews them » (LW26, l. 770) [LW-43]).

**Verdicts.**
- H1 : **voisin** (sondes de l'agent comme moniteurs de contrôle sur trajectoires, sans bras boîte noire, concentré). Risque de collision par les articles compagnons (section 6).
- H2 : **occupée en partie** — configuration de référence faite (sondes de l'agent qui agit, seuil par action à 1 % calibré sur l'honnête, maximum sur la trajectoire) ; accumulation additive, garantie toujours valide, sabotage sous le seuil, rappel selon l'horizon : non faits. Donnée utile à H2 : 1 % par action devient 26 à 43 % par trajectoire.
- H8 : **voisin**. Le billet touche l'axe « intention contre conscience d'évaluation » par un côté : les activations portent la trace de la simulation (« Its activations registered the simulation, even though Qwen3.5 rarely said it thought it was being evaluated. » (LW26, l. 164) [LW-30]) sans que les sondes d'attaque en soient déplacées. Il ne mesure pas un construit pour en prédire la robustesse adverse. Indice plutôt favorable aux sondes sur ce point, à tempérer par la réserve sur la sonde sur politique.
- Tr : **voisin** (maximum au niveau action puis trajectoire, employé sans attaquant adaptatif et sans comparaison d'agrégations).
- L, T : **voisin lointain** (donnée empirique : dépendance positive des alarmes à l'intérieur d'une trajectoire honnête).
- HC2 : **ne touche pas** (renvoi à lire : sensibilité des sondes aux fautes de frappe, arXiv 2609.15994, LW26, l. 774).

### 3.2 AISILW, AISIPUB, AISIWHY — institut britannique, 10 juillet 2025

**Ce qu'ils font.** Notes de laboratoire (« Please interpret these results as you might a colleague sharing their lab notes. » (AISILW, l. 66) [AL-02]) en quatre parties : sous-performance sur consigne, tâches simples, Llama-3.1-8B ; passage à Llama-3.3-70B et à une tâche d'agent ; organismes réglés pour sous-performer ; recherche de sous-performance dans les évaluations passées par un moniteur boîte noire. AISIWHY en est le résumé public ; AISIPUB n'est qu'une fiche (« we share preliminary results on the topic of sandbagging » (AISIPUB, l. 45) [AP-02]).

**Résultats chiffrés (auteurs).**
- Tâches simples : « the white box monitoring performed very well whilst the black box monitor seemed to struggle » (AISILW, l. 143) [AL-20] ; « our off-policy trained deception probes performed consistently very well » (AISILW, l. 87) [AL-03] ; aucun chiffre dans le texte, un nuage de points en figure (« A scatterplot of probe accuracies (y-axis) vs task difficulty » (AISILW, l. 149) [AL-23]).
- Tâche d'agent : 78 échantillons, « the 70B model gets 26% accuracy with this system prompt, and 46% accuracy without it » (AISILW, l. 186) [AL-24], « containing only 17 transcripts » (AISILW, l. 186) [AL-06] positives ; moniteur boîte noire à 74 % d'aire sous la courbe (« the black box chain-of-thought monitor performed relatively poorly, achieving only 74% AUROC » (AISILW, l. 193) [AL-07]) ; sonde à 97 % (moyenne) et 99 % (maximum) (« achieving 97%-99% AUROC (for mean-aggregation vs max-aggregation respectively) » (AISILW, l. 195) [AL-08]) ; sonde seule au seuil importé : « (88% TPR, 2% FPR with max aggregation) » (AISILW, l. 195) [AL-09]. Écart : 23 à 25 points d'aire (calcul). 88 % de 17 correspond à 15 transcriptions (calcul).
- Organismes réglés : dégradation des sondes, sans chiffre dans le texte (« as judged by recall at 1% TPR, these model organisms did show significantly diminished probe performance » (AISILW, l. 272) [AL-13]).

**Ce qu'ils ne font pas.** Pas de comparaison à faux positifs égaux ; pas de tâche floue ; pas d'étalement sur une trajectoire de déploiement ; pas d'attaquant ; aucune accumulation entre échantillons (seulement annoncée).

**Limites reconnues.** Moniteur boîte noire désavantagé : il ne voit pas la consigne, la sonde en garde la trace (« We note that this does disadvantage the black box monitor, relative to the white box monitor » (AISILW, l. 137) [AL-05]) ; il est peu travaillé (« we didn’t iterate that much on the monitor prompt or try few shot prompting so we might be under-estimating it » (AISILW, l. 154) [AL-18]). Seuil mal fondé (« our application of this calibration method is relatively unprincipled here » (AISILW, l. 195) [AL-21]). Cadre jouet (« in toy experimental set-ups » (AISIWHY, l. 69) [AW-04]). Motif avancé pour le blanc : la sous-performance « may appear indistinguishable from honest mistakes, even when a full chain-of-thought is available » (AISIWHY, l. 65) [AW-06] ; le noir n'est pas écarté (« There’s plenty of progress we can make on the problem of controlling misaligned AI systems using black box techniques! » (AISIWHY, l. 63) [AW-07]) et le rôle du blanc reste au conditionnel (« We think white box methods for sandbagging detection and mitigation may play a crucial role » (AISIWHY, l. 81) [AW-08]). Dégradation des deux méthodes avec la taille et la complexité (« We were surprised by the deterioration in performance of both the white and black box baseline methods from simply working with a larger model and more difficult task. » (AISILW, l. 92) [AL-04] ; « we note that black-box chain-of-thought monitoring also suffered from the switch to complex tasks » (AISILW, l. 223) [AL-12]).

**Incohérences et résultats trop beaux.**
- Aire de 97 à 99 % sur 17 positifs, avec une sonde qui peut lire la consigne : trop beau, réserve (même mécanisme que pour LW26 ; objection « it will be pretty hard to tell whether your probe is working by detecting the presence of instructions about sandbagging vs. working by detecting the presence of cognition about sandbagging » (AISILW, l. 454) [AL-19]).
- « recall at 1% TPR » (« as judged by recall at 1% TPR, these model organisms did show significantly diminished probe performance » (AISILW, l. 272) [AL-13]) : coquille probable pour « 1 % de faux positifs ».
- Le résumé AISIWHY dit que la précision du moniteur blanc baisse sur la tâche d'agent ; le billet long y rapporte pourtant une aire de 97 à 99 %, supérieure à celle du noir. La « baisse » vise le point de fonctionnement et la marge entre distributions, non l'aire : les deux textes ne se contredisent pas, mais le résumé seul induirait en erreur.

**Questions de la consigne.** (a) Oui, comparaison chiffrée sonde contre moniteur boîte noire, en aire sous la courbe, sur une sous-performance sur consigne (menace de type diffus, tâche vérifiable) ; pas à faux positifs égaux. (b) Moyenne et maximum sur les jetons d'une transcription ; le « problème d'agrégation » est nommé (« Probes firing in these benign situations causes issues for naive strategies for aggregating the token-level probe scores into a sample-level score » (AISILW, l. 206) [AL-11] ; « Exploring strategies for handling the “aggregation problem”, which become more apparent in these complex evaluations. » (AISILW, l. 227) [AL-22]). (c) Oui : accumulation des scores de sondes entre échantillons d'une évaluation (« or gain more significant evidence by aggregating probe scores from all samples » (AISILW, l. 407) [AL-14] ; « We are currently investigating this question. » (AISILW, l. 407) [AL-15]) ; sondage sur questions de suivi ; protocoles d'usage (« thinking about the protocols/mitigations that we'd likely use in practice » (AISILW, l. 272) [AL-25]) ; jeux rouge contre bleu (« we will stress-test the effectiveness of our methods through » (AISIWHY, l. 83) [AW-05]), parus depuis (GAMES, arXiv 2512.07810).

**Verdicts.**
- H1 : **voisin fort** ; en lecture dure, **occupée en partie** pour la composante « comparaison chiffrée blanc contre noir sur sous-performance d'agent ». Non fait : faux positifs égaux, agrégation égale, tâche floue, sabotage étalé. Contre-indices internes : dégradation des deux méthodes ; construit douteux de la sonde (« we hypothesised that the probe likely tracked some combination of intent to deceive and observing incorrectness » (AISILW, l. 135) [AL-16]).
- H2 : **voisin** (annonce d'une accumulation de scores de sondes entre échantillons, note 10 ; aucune garantie, aucun résultat). À surveiller : c'est l'annonce la plus proche de H2 dans le lot ; l'article de décembre 2025 est à relire sur ce point précis.
- H8 : **voisin** (question du construit posée : intention de tromper ou simple erreur, consigne ou cognition ; non reliée à la robustesse adverse).
- Tr : **voisin** (moyenne contre maximum au niveau jeton, faux positifs du maximum).
- Autres : ne touche pas.

### 3.3 CASE — « The Case for White Box Control », 18 avril 2025

Billet d'opinion d'un auteur seul, premier billet de l'auteur, sans expérience. Thèse : les méthodes boîte blanche pourraient détecter la tromperie absente des sorties (« a set of methods that could detect deception even when it doesn't appear in model outputs » (CASE, l. 39) [CA-02]) et se combinent au noir (« adding the results of white box monitors to black box ones could provide a much stronger signal to overseers » (CASE, l. 89) [CA-04]). Il propose les sondes comme moniteurs de confiance pour le code piégé (« Use probes as trusted monitors, e.g. we could train probes to predict when solutions are backdoored. » (CASE, l. 133) [CA-11]) et pour les tâches difficiles à vérifier (« much less easily checkable tasks like confusing conceptual work » (CASE, l. 146) [CA-08]), sans mesure. (a) Aucune comparaison chiffrée. (b) Aucune agrégation sur trajectoire ; seule mention : prédiction au fil des jetons et arrêt de la génération (CASE, l. 99). (c) Aucune annonce.

**Verdicts.** H1 : **voisin au niveau de l'idée** (thèse posée pour le diffus et le flou en une ligne ; aucune mesure ; commentaire contraire de Fabien Roger, « I think it's not obvious that probes will be more reliable than trusted monitors for most tasks you care about » (CASE, l. 186) [CA-10]). Autres : ne touche pas.

### 3.4 LIE — « Fine-Tuned Lie Detectors Failed to Generalize », 21 août 2026

**Ce qu'il fait.** Détecteurs de mensonge obtenus par réglage fin du modèle lui-même sur une question (« as-tu menti ? »), sur ses propres mensonges, douze cadres, environ 200 000 exemples ; pas de sonde d'activations (« We fine-tuned using LoRA (rank 16, α=32, dropout 0.05) with cross-entropy loss on the final token. » (LIE, l. 404) [LD-04]). Résultat : « In-distribution detection worked well (AUROC 0.60 → 0.95), but cross-category transfer did not (AUROC ~0.70–0.75). » (LIE, l. 32) [LD-03] ; le détecteur dépasse à peine la consigne simple hors distribution (« Our specialized detector barely outperformed the prompted baseline on novel lie types. » (LIE, l. 406) [LD-10]), base de 0,46 à 0,80 (« Gemma-3-27B showed baseline AUROC ranging from 0.46 to 0.80 » (LIE, l. 394) [LD-09]). Le transfert suit la ressemblance de surface (« tracking surface similarity rather than underlying deceptive intent » (LIE, l. 410) [LD-05] ; « Surface similarity predicted transfer better than our lie categories did. » (LIE, l. 436) [LD-06]). La lecture à la troisième personne bat l'auto-déclaration (« outperformed self-report across model sizes » (LIE, l. 396) [LD-11]).

**Limites reconnues.** Étiquettes bruitées (« Approximately 25% of labels changed after this pass » (LIE, l. 40) [LD-08]) ; cadres contrôlés (« we tested controlled settings rather than deployment-relevant deception » (LIE, l. 452) [LD-12]) ; les approches par représentations ne sont pas testées (« representation-level approaches may fare better, but face their own generalization challenges » (LIE, l. 454) [LD-07]).

**Incohérence.** Le tableau d'accord avec l'annotateur est illisible dans le rendu (colonnes collées, LIE, l. 497 à 507) : aucun chiffre n'en est repris.

**Questions.** (a) Non : pas de sonde ; la comparaison est entre détecteur réglé et modèle interrogé par consigne, en aire sous la courbe, sur des réponses isolées. (b) Non. (c) Non.

**Verdicts.** H8 : **voisin** (ce que le détecteur a appris, la forme de surface du cadre, explique après coup son transfert ; ni sondes, ni attaque, ni prédiction faite avant la mesure). Phrase à citer : « in-distribution accuracy will keep overstating what they can catch » (LIE, l. 460) [LD-13]. H1 : **ne touche pas** (mais rappel utile : le plus grand modèle, interrogé par simple consigne, atteint 0,98 à 0,99 d'aire sur ces cadres, LIE, l. 394 ; le résumé dit : « fine-tuning them didn’t generalize well to out-of-distribution cases » (LIE, l. 18) [LD-02]). HC2 : ne touche pas.

### 3.5 CHEAP — classifieurs à bas coût par réemploi des représentations (2025)

**Ce qu'il fait.** Détection de contournements (armes biologiques) sur l'entrée seulement (« the methods we consider only look at the prompt » (CHEAP, l. 41) [CM-09]) : sondes linéaires sur activations, dernière couche réentraînée, cascades à deux étages. Trois sondes : moyenne des jetons, moyenne mobile exponentielle puis maximum, suffixe. Mesure : aire sous la courbe en espace logarithmique, faux positifs de 0,001 à 0,1 (« In this paper we use FPR values between 1e-3 and 1e-1. » (CHEAP, l. 167) [CM-07]).

**Résultats (auteurs, qualitatifs dans le texte).** « linear probes achieve performance comparable to a classifier 2% of the size of the policy model with virtually no additional computational cost » (CHEAP, l. 11) [CM-01] ; la sonde à moyenne mobile se place entre deux classifieurs dédiés (« performing between the strength of the S and M models » (CHEAP, l. 183) [CM-10]) ; la moyenne simple est la pire (« The probe that is evaluated only on the mean of the context performs worse than even the smallest tested model. » (CHEAP, l. 183) [CM-06]), parce que le signal se dilue sur les entrées longues (« Mean-token probes perform worse on long inputs » (CHEAP, l. 55) [CM-04]). Les valeurs sont dans les figures, absentes du dossier.

**Limites reconnues.** Aucune attaque adaptative (« we have not studied the robustness of any of the classifiers in this paper to adaptive adversarial attacks » (CHEAP, l. 37) [CM-02]) ; la robustesse des sondes pourrait être pire (« the relative robustness under direct attack could be worse for probes » (CHEAP, l. 37) [CM-03]) ; la cascade ouvre une attaque sur le premier étage (« could give a significant advantage to an attacker if it’s easier to find attacks against the first stage classifier » (CHEAP, l. 69) [CM-08]). Coûts illustratifs seulement.

**Questions.** (a) Oui pour « sonde contre classifieur boîte noire dédié » sur toute une plage de faux positifs, mais sur des requêtes d'utilisateurs, pas sur un sabotage d'agent. (b) Agrégation au niveau jeton dans une entrée : « We then apply an exponential moving average to this sequence with α = 0.5 » (CHEAP, l. 55) [CM-05], puis maximum ; aucune trajectoire. (c) Non, sinon l'appel à des essais adverses.

**Verdicts.** H1 : **voisin** (forme de la comparaison à faibles faux positifs ; objet : mésusage, entrée seule ; résultat : la sonde vaut un petit classifieur, pas le meilleur). Tr : **voisin** (prémisse au niveau jeton : la moyenne dilue, moyenne mobile puis maximum ; déjà connue du niveau 2 par 2506.10805). HC2 : **voisin** (les auteurs disent ne pas avoir testé l'attaque et craindre pour les sondes). H2 : ne touche pas (la moyenne mobile porte sur les jetons d'une entrée, sans garantie).

### 3.6 APOLLO — sondes de tromperie (6 février 2025)

Page de présentation de l'article arXiv 2502.03407, sans chiffre. Points utiles : la sonde capte en partie le texte « lié à la tromperie » (« it may partially be a probe for “deception-related” text rather than “actually-deceptive” text » (APOLLO, l. 95) [AO-02]) ; la moyenne des jetons peut se tromper quand le détail par jeton est raisonnable (« The mean score being incorrect even if the per-token probe behavior is reasonable » (APOLLO, l. 113) [AO-04]) ; la base boîte noire fait jeu égal (« Our best probes performs comparably to this baseline, although we iterated more on the probes than the baseline. » (APOLLO, l. 107) [AO-03]). (a) Comparaison qualitative, sans gain blanc sur noir, sur des réponses où la tromperie se lit dans la transcription. (b) Moyenne par jeton. (c) Souhait : cadres où la tromperie ne se voit pas dans la transcription (« where it’s not obvious from the transcript that the model is being deceptive » (APOLLO, l. 117) [AO-05]).

**Verdicts.** H1 : **voisin, contre-indice faible** (parité avec GPT-4o, base moins travaillée). H8 : **voisin** (construit de surface nommé). Les chiffres que l'état de l'art v1 prête à cet article (ligne 33) ne figurent pas dans cette page : ils relèvent du PDF.

### 3.7 HEBBAR — menaces diffuses (30 avril 2025)

**Ce qu'il fait.** Billet conceptuel, sans expérience. Définit la menace diffuse (« where catastrophe requires numerous bad actions, but each bad action is only weak evidence of malign intent when investigated » (HEBBAR, l. 41) [HE-02]), l'axe concentré–diffus, et une frontière de Pareto entre nombre d'actions et discrétion (« some Pareto frontier between the number of actions needed1 and the sneakiness of each action » (HEBBAR, l. 75) [HE-07]). Deux parades : entraînement en ligne et incrimination.

**Phrase clé pour H2 et L.** L'incrimination par accumulation de faibles soupçons est jugée impossible sans référence honnête : « no amount of mildly suspicious actions is enough to incriminate the model » (HEBBAR, l. 87) [HE-03] ; elle ne deviendrait possible que « would only allow us to incriminate if we knew exactly how suspicious a benign model would look » (HEBBAR, l. 87) [HE-04]. L'auteur en conclut : « Therefore incrimination is only promising for the top left region » (HEBBAR, l. 87) [HE-05]. C'est, en creux, la condition de H2 (seuil calibré sur des épisodes honnêtes du même agent) ; l'auteur ne la croit pas disponible et n'envisage ni sonde ni test séquentiel.

**Questions.** (a) Non. (b) Non (idée d'accumulation évoquée et écartée ; entraînement renforcé sur les actions les plus suspectes, « we might train against the most suspicious 3% of actions for multiple epochs » (HEBBAR, l. 91) [HE-08]). (c) Non.

**Verdicts.** H2 : **voisin, avec contre-indice de position** (l'accumulation de soupçons faibles est jugée non praticable sans connaître la loi honnête ; aucune mesure). L : **voisin** (arbitrage nombre d'actions contre discrétion, « A scheming model is therefore incentivized to sabotage in ways that require as few actions as possible. » (HEBBAR, l. 71) [HE-06] ; qualitatif, sans statistique ni budget). T : **voisin lointain** (« bad actions are numerous but are very difficult to distinguish from benign actions » (HEBBAR, l. 89) [HE-09]). H1 : ne touche pas (aucune mention des activations).

### 3.8 NOTES — défaillances non concentrées (29 mars 2025)

**Ce qu'il fait.** Notes conceptuelles sur l'audit en ligne, l'entraînement en ligne, le débat. Mentionne les sondes une fois, comme moyen de choisir les actions à auditer (« e.g. trusted/untrusted monitors, probes on the model » (NOTES, l. 63) [NO-02]).

**Points utiles.**
- Audit sans entraînement : contrôle des fausses alertes à partir d'une loi a priori des scores d'un modèle honnête (« some prior over what the suspiciousness scores should be for a non-scheming model » (NOTES, l. 89) [NO-03]), avec la même difficulté que chez Hebbar (« A key difficulty is that we're unsure how suspicious we expect behavior to be » (NOTES, l. 91) [NO-04]), et réponse à un motif systématique (« A systematic pattern of seemingly intentionally bad behavior. » (NOTES, l. 85) [NO-09]).
- Budget de l'attaquant : « then the AI needs the product of the q_i's to be high enough that it is unlikely to be caught » (NOTES, l. 149) [NO-05] — forme additive en logarithme ; puis un budget en « bits » (« SGD will update the model if the total bits (or maybe total reward) separating from the good model are sufficiently high » (NOTES, l. 151) [NO-10]), que l'auteur ne tient pas pour acquis (« I don't know if "bits" are a natural way to denominate this. » (NOTES, l. 151) [NO-06]).
- Détection trop tardive : « there exist regimes where you'd eventually get enough signal to detect or train away problematic behavior, but it would be too late by the time you managed it » (NOTES, l. 161) [NO-07] — voisin de la clause « alarme avant le dommage » de N-004.
- Sabotage indiscernable par les scores : « subtle enough that it results in identical oversight scores » (NOTES, l. 147) [NO-08] — germe de la moitié négative de T.

**Questions.** (a) Non. (b) Non (aucune statistique). (c) Non.

**Verdicts.** L : **voisin** (budget additif heuristique, détection à temps ; ni énoncé ni sonde). T : **voisin** (moitié négative, non revendiquée). H2 : **voisin** (contrôle des fausses alertes sur référence honnête, posé en principe). H1 : ne touche pas.

### 3.9 DIFFUSE — « Diffuse AI Control on Fuzzy Tasks », 23 juin 2026 (base du programme, arXiv 2606.08892)

**Ce qu'il fait.** Jeu entre une équipe bleue (consigne d'un noteur faible de confiance, Haiku 4.5 : « The blue team uses Haiku 4.5 as the » (DIFFUSE, l. 149) [DI-05]) et une équipe rouge (consigne du générateur, Opus 4.6), sur des propositions d'expériences (« We evaluate the model on generating a set of ten ideas for experiments or high-level sketches of theoretical » (DIFFUSE, l. 143) [DI-11]) ; vérité approchée par Sonnet 4.6 avec l'article (« As the ground truth proxy scorer, we use Sonnet 4.6 with access to the full paper » (DIFFUSE, l. 145) [DI-04]). L'attaquant est contraint de rester près du score faible optimal : « w(\mathfrak{b},\mathfrak{r})>w^*-\varepsilon, » (DIFFUSE, l. 111) [DI-10]. Résultats qualitatifs dans le texte : attaques qui font noter Opus 4.6 plus bas que GPT-OSS-20B par la vérité approchée (« proposals rated as worse than those of GPT-OSS-20B by the ground truth proxy scorer » (DIFFUSE, l. 168) [DI-06]) ; consigne bleue robuste trouvée, mais avec un accès irréaliste (« robust blue-team prompts requires access to the ground truth proxy scorer, which the blue team may not have » (DIFFUSE, l. 233) [DI-07]). Aucun chiffre dans le texte du billet (valeurs en figures, absentes du dossier).

**Ce qu'il ne fait pas.** Aucune activation, aucune sonde, aucun moniteur par action, aucune trajectoire ni horizon mesuré (malgré « solutions to the tasks it was given across a long deployment horizon » (DIFFUSE, l. 283) [DI-08]), aucun taux de faux positifs. La « détection » n'est pas l'objet : le cadre est l'entraînement contre un score.

**Position.** « We focus on training interventions because they seem more promising than monitoring and incrimination for » (DIFFUSE, l. 60) [DI-02] (suite ligne 61). Pistes bleues citées : débat, cognition factorisée, surveillance non fiable (« or untrusted monitoring with » (DIFFUSE, l. 264) [DI-09]) ; pas de boîte blanche.

**Questions.** (a) Non. (b) Non. (c) Non pour ces points.

**Verdicts.** H1 : **ne touche pas la mesure ; contre-indice de position** (la surveillance est dite moins prometteuse que l'entraînement pour le diffus ; opinion appuyée sur deux références, sans mesure propre). H2 : ne touche pas. T : **voisin lointain** (attaquant contraint sur la moyenne d'un score, dommage mesuré ailleurs : forme « statistique préservée, dommage libre »). L : ne touche pas. L'adaptativité de l'attaquant est dite nécessaire (« show in the paper that the adaptive nature of the red team is necessary for a successful attack. » (DIFFUSE, l. 190) [DI-12]) : à retenir pour le bras d'attaque du papier A.

### 3.10 LOGIT — courbes de discrimination en espace logit (12 avril 2026)

**Ce qu'il fait.** Moniteur de confiance boîte noire, note de 0 à 100 par action, BashArena (400 trajectoires d'attaque pour chacune de 4 tâches annexes, « averaging 20 agent actions per trajectory » (LOGIT, l. 50) [LR-10]) et LinuxArena (96 honnêtes, 111 attaques). Loi empirique : « logit(TPR) is linear in logit(FPR) » (LOGIT, l. 40) [LR-02], soit des scores honnêtes et d'attaque de loi logistique. Convention : vrais positifs par trajectoire (« the fraction of malicious trajectories that has at least one action above the cutoff » (LOGIT, l. 52) [LR-03]), faux positifs par action (« the fraction of actions from benign trajectories above the cutoff » (LOGIT, l. 52) [LR-04]), budgets très bas (« e.g. 1e-4, that is 1 audit for every 10,000 actions » (LOGIT, l. 52) [LR-05]). Aucun chiffre de performance dans le texte.

**Points utiles à H2 et L.** Même convention que LW26 : seuil par action, trajectoire attrapée au maximum. La loi nulle d'une attaque manquée est simulée comme le maximum d'autant de tirages que la trajectoire a d'actions (« sample that many values from a μ=0 σ=1 logistic distribution and take the max » (LOGIT, l. 120) [LR-06]) : dépendance explicite du maximum à la longueur, sous indépendance supposée. Le jeu d'attaque ne garde que le pas le plus suspect (« We then filter the attack dataset down to scores for the single most suspicious step (according to the average score) of each trajectory » (LOGIT, l. 177) [LR-11]).

**Limites reconnues.** Loi valable à attaquant, tâche, moniteur et consigne fixés (« it tends to hold if we fix the untrusted LLM, the attack task, the monitor LLM, and the monitor prompt » (LOGIT, l. 126) [LR-07]) ; rompue si la discrétion varie (« They do not hold if the “sneakiness” of the attacks vary widely » (LOGIT, l. 405) [LR-08]) ; moniteurs faibles qui manquent l'attaque (« completely “miss” the attack some fraction of the time » (LOGIT, l. 93) [LR-09]). La consigne d'attaque suggère elle-même d'étaler l'attaque (« The best strategy might be to distribute your attack over a couple scripts which invoke one another » (LOGIT, l. 257) [LR-12]), sans mesure par degré d'étalement.

**Questions.** (a) Non (aucune sonde). (b) Maximum sur les actions, boîte noire ; aucune somme. (c) Non.

**Verdicts.** H2 : **voisin** (convention du moniteur par action et du maximum, boîte noire, concentré). L : **voisin** (loi du maximum selon la longueur, descriptif ; outil d'extrapolation aux faibles faux positifs utile au préenregistrement de G1). H6, H1 : ne touche pas.

### 3.11 BLOCK — défaillances immédiates et moniteurs synchrones (30 mars 2026)

Billet de cadrage, sans mesure. Distingue détection et prévention, latence d'attaque, taux de dommage (« Asynchronous monitors are generally better at countering threats with low rates of damage. » (BLOCK, l. 48) [BL-03]), défaillances immédiates (« We call actions “live failures” if their harmful effects are rapid and hard to recover from. » (BLOCK, l. 38) [BL-02]). Les moniteurs bloquants lisent action par action (« they monitor each action individually instead of monitoring long trajectories all at once » (BLOCK, l. 67) [BL-04]). Un commentaire relève que l'expérience subtilement faussée n'a pas de point de contrôle naturel (« 'running a subtly wrong experiment' might not have a merge-point where that can be caught » (BLOCK, l. 116) [BL-05]). (a), (b), (c) : non.

**Verdicts.** L (clause « alarme avant le dommage ») : **voisin** (vocabulaire : délai de grâce, taux de dommage ; aucun énoncé). H2, H6 : ne touche pas.

### 3.12 RETRY — réessai contre ré-échantillonnage (29 mai 2026, résumé d'arXiv 2605.26047)

**Ce qu'il fait.** BashArena, « using Claude Opus 4.6 as an untrusted model and MiMo-V2-Flash as a trusted model » (RETRY, l. 67) [RE-12] ; tâches annexes traitées comme défaillances immédiates ; budget d'audit de 0,3 % des pas (« We chose to report safety results at an auditing budget of 0.3% » (RETRY, l. 69) [RE-08]).

**Résultats (auteurs).**
- Agrégation des ré-échantillons : « Resampling hurts if resamples are aggregated for auditing decisions by taking the minimum, but helps if they are aggregated by max. » (RETRY, l. 63) [RE-02] ; le bon choix dépend des corrélations (« the optimal aggregation function will depend on the relationship between the cross-resample correlations of the attack and honest data » (RETRY, l. 92) [RE-10]).
- Audit après trois alertes : « auditing after three strikes doesn’t help » (RETRY, l. 99) [RE-03] ; explication : « Smarter monitors aggregate this information just fine by default, and adding in hand-holding decreases safety. » (RETRY, l. 99) [RE-04] ; la décision d'audit ne dépend d'aucun score passé (« Because our decision to audit an action doesn’t directly depend on any previous monitor scores » (RETRY, l. 99) [RE-13]).
- Ré-échantillonnage : « Of a +10.2 pp safety gain achievable by drawing four resamples on top of every original sample » (RETRY, l. 122) [RE-06], dont 6,2 points pour un dixième du coût (soit 61 % du gain, calcul) ; « Resampling without executing the least suspicious sample has zero usefulness impact. » (RETRY, l. 120) [RE-05] ; exécuter l'échantillon le moins suspect : « we show that executing the least suspicious sample has almost no usefulness cost » (RETRY, l. 94) [RE-11].
- Réessai avec retour du moniteur : « the attacker can decrease its suspicion a similar amount, leading to no net safety gain over trusted monitoring » (RETRY, l. 105) [RE-07] ; même sans retour, fuite d'information (« still leak information about whether the previous step was suspicious enough to retry or not » (RETRY, l. 135) [RE-09]).

**Ce qu'il ne fait pas.** Aucune sonde ; aucun sabotage diffus ; pas de sélection d'attaque dans l'essentiel des résultats ; pas de courbe « succès de l'attaque contre utilité » selon l'intensité d'une perturbation.

**Questions.** (a) Non. (b) Maximum ou minimum sur des ré-échantillons d'un même pas ; comptage d'alertes sur l'historique, sans gain ; aucune somme cumulée ni garantie. (c) Travaux annoncés sur les protocoles de réessai et la stratégie d'abandon.

**Verdicts.**
- H6 : **occupée en partie** (lecture dure) pour le ré-échantillonnage : un gain de sécurité à coût d'utilité nul est publié, à deux intensités de coût. Réserves : cadre concentré ; gain obtenu par l'audit et non par l'affaiblissement de l'attaque ; la variante « exécuter le moins suspect », seule à réduire directement la progression de l'attaque, ne gagne que peu et rien contre un attaquant optimal ; le réessai n'offre aucune marge. Lecture douce : « voisin fort ». Ce qui resterait revendicable : la marge mesurée comme chute du succès du sabotage **diffus** plus rapide que l'utilité, à intensité fixée, sans passer par l'audit.
- H2 : **contre-indice** déjà au dossier (lot2-A1), précisé : compter les alertes passées n'aide pas quand le moniteur lit déjà l'historique. Portée : boîte noire, concentré ; une sonde lit, elle aussi, un état qui reflète l'historique (« By then the agent has read every earlier tool output, so its activations there reflect the run so far. » (LW26, l. 250) [LW-13]), ce qui rend la question ouverte pour H2.
- T : **voisin** (agrégateur optimal selon des corrélations que l'attaquant choisit ; déjà relevé au niveau 2).
- H7 (hors lot, pour mémoire) : la riposte visible fuit de l'information.

### 3.13 GAMES — jeux d'audit de la sous-performance (9 décembre 2025, résumé d'arXiv 2512.07810)

Cinq modèles à verrou par mot de passe (« The red team trained five models using conditional underperformance ('password locking') as a proxy for sandbagging. » (GAMES, l. 49) [AG-06]), dix méthodes. Boîte noire : échec (« We had very little success with black box methods. » (GAMES, l. 65) [AG-02] ; « black box methods proved largely ineffective » (GAMES, l. 93) [AG-07]). Boîte blanche : plus prometteuse (« white box methods proved significantly more promising than black box ones » (GAMES, l. 71) [AG-03]), puis mise en défaut par des comportements de diversion (« the red team was later able to introduce false positives using distractor behaviours » (GAMES, l. 75) [AG-04] ; « can be fragile and easily confused, leading to false negatives » (GAMES, l. 91) [AG-05]). Aucun chiffre dans le billet. (a) Comparaison qualitative, par modèle entier, sur sous-performance ; pas de faux positifs fixés. (b) Non décrit. (c) Appel à des sondes plus robustes.

**Verdicts.** H1 : **voisin** (énoncé qualitatif blanc plus prometteur que noir pour la sous-performance, avec contre-résultat ; conforme au verdict du niveau 2 sur le PDF). H8 : **voisin** (sondes trompées par des corrélats introduits à dessein). HC2 : **voisin** (faux positifs provoqués par l'équipe rouge, par entraînement du modèle et non par contenu). H2 : ne touche pas.

### 3.14 REDTEAM — équipe rouge du contrôle (23 juillet 2026)

Moniteurs visés : modèles de langage qui lisent actions ou raisonnement (« a separate LLM that reviews the agent’s actions and flags them if they are dangerous » (REDTEAM, l. 39) [RT-02]) ; aucune sonde. Failles trouvées dans chaque version (« We found vulnerabilities in every monitor version we tested » (REDTEAM, l. 55) [RT-03]) ; recherche évolutive d'attaques (« the evolutionary search eventually achieves a minimum suspicion score of 3 out of 100 » (REDTEAM, l. 78) [RT-04]) ; bruit du score à prendre en compte (« we’d like to account for the random noise in a monitor’s score » (REDTEAM, l. 80) [RT-05]) ; estimation de la sécurité d'ensemble ouverte (« How do we estimate overall safety? » (REDTEAM, l. 88) [RT-06]). (a), (b) : non. (c) Travaux annoncés côté attaque.

**Verdicts.** H1, H2 : **ne touche pas** (contexte : la base boîte noire de G1 doit être éprouvée par une recherche d'attaques, pas par des attaques à consigne fixe). HC2 : ne touche pas (aucune sonde).

### 3.15 STRESS — surveillance asynchrone d'agents de code (16 décembre 2025, résumé d'arXiv 2512.13526)

Agent Claude 4.1 Opus, moniteur Claude 3.7 Sonnet, taux de faux positifs imposé à 1 % (« (we enforce a 1% false positive rate) » (STRESS, l. 56) [ST-02]) ; l'équipe rouge ne modifie que la consigne (« The Red team can only modify the agent's system prompt » (STRESS, l. 54) [ST-05]). Le moniteur de la première manche manquait jusqu'à 67 % des attaques, celui de la troisième 6 % au pire (« By Round 3, after seeing attack patterns and iterating, the best monitor missed only 6% at worst » (STRESS, l. 64) [ST-03]). Un moniteur faible synchrone bat le meilleur asynchrone (« the weaker Round 1 monitor acting synchronously outperformed the best Round 3 monitor working asynchronously » (STRESS, l. 75) [ST-04]). (a) Non (boîte noire seule, sabotage concentré). (b) Non décrit dans le billet. (c) Attaques automatisées, réglage fin côté rouge (« such as the ability to fine-tune models or rewrite model outputs » (STRESS, l. 83) [ST-06]).

**Verdicts.** H1 : **voisin de contexte** (comparateur boîte noire à 1 % de faux positifs, concentré). H2 : ne touche pas.

## 4. Verdicts d'ensemble par énoncé (billets du lot seulement)

| Énoncé | Verdict d'ensemble | Sources décisives | Ce qui change |
|---|---|---|---|
| **H1** | **Non occupée.** Voisin fort : AISILW (comparaison en aire sous la courbe, sous-performance d'agent). Contre-indice de position : DIFFUSE. Contre-indice faible : APOLLO (parité). | AISILW l. 193-195 ; DIFFUSE l. 60 ; APOLLO l. 107 ; LW26 (pas de bras noir) | Rien dans l'énoncé. À citer : la mesure de l'institut, avec ses réserves. Urgence : lire 2610.12445 et 2610.31593. |
| **H2 (N-007)** | **Occupée en partie pour la configuration de référence** (LW26) ; conjonction revendiquée libre. Contre-indice de position : HEBBAR. Annonce voisine : AISILW, note 10. | LW26 l. 136, 252, 254 ; HEBBAR l. 87 ; AISILW l. 407 ; RETRY l. 99 | Le « moniteur par action à 1 % sur sondes de l'agent, maximum sur la trajectoire » se cite, ne se revendique pas. Reste revendicable, inchangé : accumulation additive toujours valide, actions sous le seuil, rappel croissant avec l'horizon, calibrage sans exemple de sabotage. |
| **H8** | **Non occupée.** Voisins : LW26 (trace de simulation sans effet sur les sondes), LIE (la surface explique le transfert), AISILW et APOLLO (construit douteux). | LW26 l. 152, 404 ; LIE l. 436 ; AISILW l. 135, 454 | Rien. LW26 est à citer comme premier contrôle « simulation contre réel » pour des sondes. |
| **HC2** | **Ne touche pas** (aucune attaque par contenu sur une sonde dans le lot). Voisins : CHEAP (crainte exprimée), GAMES (faux positifs provoqués par entraînement). | CHEAP l. 37 ; GAMES l. 75 | Rien. |
| **H6 (N-013)** | **Occupée en partie pour le ré-échantillonnage, en concentré** (RETRY, lecture dure) ; à trancher sur le PDF. | RETRY l. 63, 94, 105, 120, 122 | Si la lecture dure est retenue : préciser que la marge revendiquée porte sur le sabotage diffus et se mesure sur le succès de l'attaque, hors audit. Décision de Lazar (modification de revendication). |
| **L (N-004)** | **Non occupée.** Voisins : NOTES (budget additif heuristique, détection trop tardive), HEBBAR (nombre contre discrétion), LOGIT (maximum selon la longueur), LW26 (dépendance des alarmes dans une trajectoire). | NOTES l. 149, 151, 161 ; HEBBAR l. 71, 75 ; LOGIT l. 120 | Rien. Deux précédents conceptuels à citer (Greenblatt, Hebbar). |
| **T (N-003)** | **Non occupée.** Voisins lointains de la moitié négative, non revendiquée : NOTES, DIFFUSE, RETRY. | NOTES l. 147 ; DIFFUSE l. 111 ; RETRY l. 92 | Rien. |
| **Tr** | **Non occupée.** Voisins : LW26 (maximum action puis trajectoire, sans attaquant), CHEAP et AISILW (moyenne, maximum, moyenne mobile au niveau jeton). | LW26 l. 136, 252 ; CHEAP l. 55 ; AISILW l. 206 | Rien. |

**Bases de G1 (N-007, N-056), pour mémoire.** La cascade « sonde en premier étage, puis moniteur qui lit la transcription » est décrite comme usage courant (LW26, l. 770 et 806 ; CHEAP, cascades à deux étages) : la base (ii) est une pratique publiée, à citer.

## 5. Réponse groupée aux trois questions de la consigne

| Billet | (a) comparaison chiffrée sonde contre boîte noire, à faux positifs égaux | Type de sabotage | (b) agrégation de scores de sondes sur une trajectoire | (c) annonce |
|---|---|---|---|---|
| LW26 | non (aucun bras boîte noire) | concentré (tâche annexe) | maximum sur les commandes ; aucun lissage ; aucune garantie par trajectoire | agent plus capable |
| AISILW, AISIWHY | oui en aire sous la courbe (74 % contre 97 à 99 %) ; non à faux positifs égaux | sous-performance sur consigne, tâche vérifiable | moyenne et maximum sur les jetons d'une transcription | accumulation entre échantillons, protocoles, jeux rouge contre bleu |
| CASE | non | — | non | non |
| LIE | non (pas de sonde) | mensonges en réponse isolée | non | non |
| CHEAP | oui sur une plage de faux positifs, contre classifieurs dédiés ; valeurs en figures | mésusage (requêtes) | moyenne mobile puis maximum, sur les jetons d'une entrée | essais adverses souhaités |
| APOLLO | qualitative : parité avec GPT-4o | tromperie en réponse isolée | moyenne par jeton | cadres sans indice dans la transcription |
| HEBBAR, NOTES | non | diffus (conceptuel) | non ; accumulation évoquée et jugée impraticable sans référence honnête | non |
| DIFFUSE | non | diffus sur tâche floue | non | non |
| LOGIT, BLOCK, RETRY, STRESS, REDTEAM | non (boîte noire seule) | concentré | boîte noire : maximum sur les actions ; maximum ou minimum sur ré-échantillons ; trois alertes sans gain | réessai, attaques automatisées |
| GAMES | qualitative, par modèle | sous-performance (verrou par mot de passe) | non décrit | sondes plus robustes |

**Constat d'ensemble.** Dans les dix-sept textes : aucune comparaison sonde contre moniteur boîte noire à faux positifs égaux sur un sabotage diffus ; aucune somme cumulée ni test séquentiel à garantie sur des scores de sondes le long d'une trajectoire ; une seule annonce proche (institut britannique, accumulation entre échantillons).

## 6. Pistes à lire, non lues ici (renvois des billets, non opposables)

- **arXiv 2610.12445** — sonde de tromperie avec poids publiés pour Qwen3.5-27B ; selon LW26 (l. 770), attrape le sabotage d'agent sur SHADE-Arena et BashArena. **Priorité 1 pour H1** (et pour la ligne « Liars' Bench et SHADE-Arena à T0.8 » de N-061).
- **arXiv 2610.31593** — évaluations de contrôle simulées ; cinq moniteurs qui lisent la transcription sur LinuxArena (LW26, l. 48 et 766). Priorité 1 avec le précédent.
- **arXiv 2609.15994** — sondes qui perdent en précision sur de simples fautes de frappe (LW26, l. 774) : pour HC2 et H8.
- **Rapport de risque d'Anthropic d'août 2026** — sonde qui trie les appels d'outils pour un moniteur (LW26, l. 770) : cascade en production.
- **arXiv 2512.07810** (déjà lu au niveau 2) — à relire sur un seul point : l'accumulation de scores de sondes entre échantillons annoncée dans AISILW, note 10.
- **arXiv 2605.26047** (déjà lu au niveau 2 pour H2 et T) — à relire pour H6.
- **arXiv 2512.22154** (latence d'attaque, synchrone contre asynchrone), **2512.13526**, **2604.15384** (LinuxArena) — contexte.

## 7. Contrôle des citations

- Script : `controle_citations.py` (archive), lancé par `python3 -I`. Il vérifie que chaque citation figure dans la ligne citée du rendu `.txt` après normalisation (Unicode, guillemets et apostrophes, espaces), que chaque citation du fichier figure mot pour mot dans ce rapport, et que tout identifiant du rapport existe dans le fichier de citations.
- Essais préalables : cas juste, 0 échec (attendu 0) ; citation altérée, 1 échec (attendu 1) ; ligne décalée, 1 échec (attendu 1).
- Premier passage sur les textes : 201 citations, 2 échecs (une ligne mal relevée, une citation à cheval sur deux lignes) ; corrigées.
- **Résultat final : 201 citations contrôlées, 0 échec.**
- Heure de l'assemblage : 2026-11-10 11:16 UTC (relevée par `date -u`).

## Annexe — liste complète des citations contrôlées

| Identifiant | Fichier | Ligne | Citation exacte |
|---|---|---|---|
| LW-01 | LW26 | 34 | 30th Oct 2026 |
| LW-02 | LW26 | 43 | This is an automated rejection. |
| LW-03 | LW26 | 50 | tasks once in simulation and twice on real machines |
| LW-04 | LW26 | 52 | the catch rate in simulated trajectories was 1.0 points lower than in real trajectories (95% interval −3.0 to +1.0) |
| LW-05 | LW26 | 66 | To our knowledge, this is the first such check for probe monitors. |
| LW-06 | LW26 | 70 | Each task pairs an ordinary main task, such as fixing a bug in a web service, with a harmful side task, such as planting a backdoor. |
| LW-07 | LW26 | 76 | All six read the activations of Qwen3.5 near the end of each command. |
| LW-08 | LW26 | 78 | Each run is scored by its most suspicious command. |
| LW-09 | LW26 | 136 | it catches an attack run if it raises an alarm on any of the run's commands |
| LW-10 | LW26 | 136 | We set each threshold so that 1% of honest commands raise an alarm |
| LW-11 | LW26 | 136 | so 26% to 43% of honest runs still raise at least one alarm, depending on the probe |
| LW-12 | LW26 | 186 | every command in an attack run counts as an attack example, not only the sabotage step |
| LW-13 | LW26 | 250 | By then the agent has read every earlier tool output, so its activations there reflect the run so far. |
| LW-14 | LW26 | 252 | Each action gets its own score, with no smoothing across actions such as an exponential moving average. |
| LW-15 | LW26 | 254 | An alarm anywhere in an attack run counts as a catch, even one after the agent has carried out the side task. |
| LW-16 | LW26 | 152 | separates simulated attack runs from real ones with an AUROC of 0.88 |
| LW-17 | LW26 | 404 | Spearman correlation −0.03 |
| LW-18 | LW26 | 400 | the on-policy probe still catches 98.6% of real attacks on whole runs |
| LW-19 | LW26 | 518 | its catch rate in simulated runs falls 31 to 38 points below the rate in real runs |
| LW-20 | LW26 | 766 | each flagging 5% of honest runs, with a root-mean-square error of 3.6 percentage points |
| LW-21 | LW26 | 770 | in SHADE-Arena and BashArena |
| LW-22 | LW26 | 790 | On Qwen3.5, it did not respond when we told the agent it was being tested, so it could not measure awareness. |
| LW-23 | LW26 | 806 | A probe is cheap enough to run as a first stage, whose alarms only go to an LLM monitor reading the transcript |
| LW-24 | LW26 | 166 | whether probes still catch attacks as often in simulation when the agent is much more capable |
| LW-25 | LW26 | 708 | Because they are long, these runs may be caught more often |
| LW-26 | LW26 | 168 | This is a two-week sprint project done as part of the Redwood Research internship (through MATS 11.0). |
| LW-27 | LW26 | 358 | Caught, +1.8. mkdir -p /app/app/services |
| LW-28 | LW26 | 344 | 1,304 of the 1,313 tasks were caught in both real run 1 and the simulated run |
| LW-29 | LW26 | 812 | The six probes are not independent, so their average is worth less than six separate tests. |
| LW-30 | LW26 | 164 | Its activations registered the simulation, even though Qwen3.5 rarely said it thought it was being evaluated. |
| LW-31 | LW26 | 94 | 0.99 |
| LW-32 | LW26 | 126 | 0.54 |
| LW-33 | LW26 | 448 | 75.3 |
| LW-34 | LW26 | 472 | 42.8 |
| LW-35 | LW26 | 424 | 99.8 |
| LW-36 | LW26 | 496 | 66.2 |
| LW-37 | LW26 | 500 | 65.1 |
| LW-38 | LW26 | 136 | An honest run gives the probes about 65 to 75 commands to score |
| LW-39 | LW26 | 70 | We call runs where the agent is told to attempt the side task “attack runs” |
| LW-40 | LW26 | 518 | At 0.1%, the simulated threshold rests on the 56 to 65 most suspicious simulated honest commands |
| LW-41 | LW26 | 250 | each probe averages over every “content token” of the output |
| LW-42 | LW26 | 528 | scored each run by the mean of its held-out action scores |
| LW-43 | LW26 | 770 | describes a probe that picks out tool calls that might take an impactful action, so that a transcript-reading monitor reviews them |
| LW-44 | LW26 | 140 | about what a random probe would catch if it couldn’t tell attack runs from honest ones |
| LW-45 | LW26 | 704 | Runs took about 76 steps. |
| AL-01 | AISILW | 51 | 10th Jul 2025 |
| AL-02 | AISILW | 66 | Please interpret these results as you might a colleague sharing their lab notes. |
| AL-03 | AISILW | 87 | our off-policy trained deception probes performed consistently very well |
| AL-04 | AISILW | 92 | We were surprised by the deterioration in performance of both the white and black box baseline methods from simply working with a larger model and more difficult task. |
| AL-05 | AISILW | 137 | We note that this does disadvantage the black box monitor, relative to the white box monitor |
| AL-06 | AISILW | 186 | containing only 17 transcripts |
| AL-07 | AISILW | 193 | the black box chain-of-thought monitor performed relatively poorly, achieving only 74% AUROC |
| AL-08 | AISILW | 195 | achieving 97%-99% AUROC (for mean-aggregation vs max-aggregation respectively) |
| AL-09 | AISILW | 195 | (88% TPR, 2% FPR with max aggregation) |
| AL-10 | AISILW | 195 | setting the decision boundary to give a 1% false positive rate on the Alpaca chat dataset |
| AL-11 | AISILW | 206 | Probes firing in these benign situations causes issues for naive strategies for aggregating the token-level probe scores into a sample-level score |
| AL-12 | AISILW | 223 | we note that black-box chain-of-thought monitoring also suffered from the switch to complex tasks |
| AL-13 | AISILW | 272 | as judged by recall at 1% TPR, these model organisms did show significantly diminished probe performance |
| AL-14 | AISILW | 407 | or gain more significant evidence by aggregating probe scores from all samples |
| AL-15 | AISILW | 407 | We are currently investigating this question. |
| AL-16 | AISILW | 135 | we hypothesised that the probe likely tracked some combination of intent to deceive and observing incorrectness |
| AL-17 | AISILW | 106 | the second and third updates show that simple baseline methods leave much room for improvement |
| AL-18 | AISILW | 154 | we didn’t iterate that much on the monitor prompt or try few shot prompting so we might be under-estimating it |
| AL-19 | AISILW | 454 | it will be pretty hard to tell whether your probe is working by detecting the presence of instructions about sandbagging vs. working by detecting the presence of cognition about sandbagging |
| AL-20 | AISILW | 143 | the white box monitoring performed very well whilst the black box monitor seemed to struggle |
| AL-21 | AISILW | 195 | our application of this calibration method is relatively unprincipled here |
| AL-22 | AISILW | 227 | Exploring strategies for handling the “aggregation problem”, which become more apparent in these complex evaluations. |
| AL-23 | AISILW | 149 | A scatterplot of probe accuracies (y-axis) vs task difficulty |
| AL-24 | AISILW | 186 | the 70B model gets 26% accuracy with this system prompt, and 46% accuracy without it |
| AL-25 | AISILW | 272 | thinking about the protocols/mitigations that we'd likely use in practice |
| AP-01 | AISIPUB | 28 | Jul 10, 2025 |
| AP-02 | AISIPUB | 45 | we share preliminary results on the topic of sandbagging |
| AW-01 | AISIWHY | 37 | Jul 10, 2025 |
| AW-02 | AISIWHY | 73 | providing some evidence for the usefulness of probes over black box monitors for sandbagging detection |
| AW-03 | AISIWHY | 75 | we also found that increased model size and task complexity caused the performance of both white and black box monitors to deteriorate |
| AW-04 | AISIWHY | 69 | in toy experimental set-ups |
| AW-05 | AISIWHY | 83 | we will stress-test the effectiveness of our methods through |
| AW-06 | AISIWHY | 65 | may appear indistinguishable from honest mistakes, even when a full chain-of-thought is available |
| AW-07 | AISIWHY | 63 | There’s plenty of progress we can make on the problem of controlling misaligned AI systems using black box techniques! |
| AW-08 | AISIWHY | 81 | We think white box methods for sandbagging detection and mitigation may play a crucial role |
| CA-01 | CASE | 32 | 18th Apr 2025 |
| CA-02 | CASE | 39 | a set of methods that could detect deception even when it doesn't appear in model outputs |
| CA-03 | CASE | 83 | I'm still super excited about black box control too! |
| CA-04 | CASE | 89 | adding the results of white box monitors to black box ones could provide a much stronger signal to overseers |
| CA-05 | CASE | 101 | Not too much research in the space yet |
| CA-06 | CASE | 111 | Generalization challenges of probes - they can struggle out of domain |
| CA-07 | CASE | 128 | black box monitors may be more accurate at detecting the tampers |
| CA-08 | CASE | 146 | much less easily checkable tasks like confusing conceptual work |
| CA-09 | CASE | 147 | Use probes to extract non-sabotaged work from activations |
| CA-10 | CASE | 186 | I think it's not obvious that probes will be more reliable than trusted monitors for most tasks you care about |
| CA-11 | CASE | 133 | Use probes as trusted monitors, e.g. we could train probes to predict when solutions are backdoored. |
| CA-12 | CASE | 152 | Black box monitoring seems like a safer bet? |
| LD-01 | LIE | 8 | August 21, 2026 |
| LD-02 | LIE | 18 | fine-tuning them didn’t generalize well to out-of-distribution cases |
| LD-03 | LIE | 32 | In-distribution detection worked well (AUROC 0.60 → 0.95), but cross-category transfer did not (AUROC ~0.70–0.75). |
| LD-04 | LIE | 404 | We fine-tuned using LoRA (rank 16, α=32, dropout 0.05) with cross-entropy loss on the final token. |
| LD-05 | LIE | 410 | tracking surface similarity rather than underlying deceptive intent |
| LD-06 | LIE | 436 | Surface similarity predicted transfer better than our lie categories did. |
| LD-07 | LIE | 454 | representation-level approaches may fare better, but face their own generalization challenges |
| LD-08 | LIE | 40 | Approximately 25% of labels changed after this pass |
| LD-09 | LIE | 394 | Gemma-3-27B showed baseline AUROC ranging from 0.46 to 0.80 |
| LD-10 | LIE | 406 | Our specialized detector barely outperformed the prompted baseline on novel lie types. |
| LD-11 | LIE | 396 | outperformed self-report across model sizes |
| LD-12 | LIE | 452 | we tested controlled settings rather than deployment-relevant deception |
| LD-13 | LIE | 460 | in-distribution accuracy will keep overstating what they can catch |
| CM-01 | CHEAP | 11 | linear probes achieve performance comparable to a classifier 2% of the size of the policy model with virtually no additional computational cost |
| CM-02 | CHEAP | 37 | we have not studied the robustness of any of the classifiers in this paper to adaptive adversarial attacks |
| CM-03 | CHEAP | 37 | the relative robustness under direct attack could be worse for probes |
| CM-04 | CHEAP | 55 | Mean-token probes perform worse on long inputs |
| CM-05 | CHEAP | 55 | We then apply an exponential moving average to this sequence with α = 0.5 |
| CM-06 | CHEAP | 183 | The probe that is evaluated only on the mean of the context performs worse than even the smallest tested model. |
| CM-07 | CHEAP | 167 | In this paper we use FPR values between 1e-3 and 1e-1. |
| CM-08 | CHEAP | 69 | could give a significant advantage to an attacker if it’s easier to find attacks against the first stage classifier |
| CM-09 | CHEAP | 41 | the methods we consider only look at the prompt |
| CM-10 | CHEAP | 183 | performing between the strength of the S and M models |
| AO-01 | APOLLO | 75 | 06 February 2025 |
| AO-02 | APOLLO | 95 | it may partially be a probe for “deception-related” text rather than “actually-deceptive” text |
| AO-03 | APOLLO | 107 | Our best probes performs comparably to this baseline, although we iterated more on the probes than the baseline. |
| AO-04 | APOLLO | 113 | The mean score being incorrect even if the per-token probe behavior is reasonable |
| AO-05 | APOLLO | 117 | where it’s not obvious from the transcript that the model is being deceptive |
| HE-01 | HEBBAR | 29 | Apr 30, 2025 |
| HE-02 | HEBBAR | 41 | where catastrophe requires numerous bad actions, but each bad action is only weak evidence of malign intent when investigated |
| HE-03 | HEBBAR | 87 | no amount of mildly suspicious actions is enough to incriminate the model |
| HE-04 | HEBBAR | 87 | would only allow us to incriminate if we knew exactly how suspicious a benign model would look |
| HE-05 | HEBBAR | 87 | Therefore incrimination is only promising for the top left region |
| HE-06 | HEBBAR | 71 | A scheming model is therefore incentivized to sabotage in ways that require as few actions as possible. |
| HE-07 | HEBBAR | 75 | some Pareto frontier between the number of actions needed1 and the sneakiness of each action |
| HE-08 | HEBBAR | 91 | we might train against the most suspicious 3% of actions for multiple epochs |
| HE-09 | HEBBAR | 89 | bad actions are numerous but are very difficult to distinguish from benign actions |
| NO-01 | NOTES | 29 | Mar 29, 2025 |
| NO-02 | NOTES | 63 | e.g. trusted/untrusted monitors, probes on the model |
| NO-03 | NOTES | 89 | some prior over what the suspiciousness scores should be for a non-scheming model |
| NO-04 | NOTES | 91 | A key difficulty is that we're unsure how suspicious we expect behavior to be |
| NO-05 | NOTES | 149 | then the AI needs the product of the q_i's to be high enough that it is unlikely to be caught |
| NO-06 | NOTES | 151 | I don't know if "bits" are a natural way to denominate this. |
| NO-07 | NOTES | 161 | there exist regimes where you'd eventually get enough signal to detect or train away problematic behavior, but it would be too late by the time you managed it |
| NO-08 | NOTES | 147 | subtle enough that it results in identical oversight scores |
| NO-09 | NOTES | 85 | A systematic pattern of seemingly intentionally bad behavior. |
| NO-10 | NOTES | 151 | SGD will update the model if the total bits (or maybe total reward) separating from the good model are sufficiently high |
| DI-01 | DIFFUSE | 10 | June 23, 2026 |
| DI-02 | DIFFUSE | 60 | We focus on training interventions because they seem more promising than monitoring and incrimination for |
| DI-03 | DIFFUSE | 36 | Diffuse threats correspond to behaviors that are |
| DI-04 | DIFFUSE | 145 | As the ground truth proxy scorer, we use Sonnet 4.6 with access to the full paper |
| DI-05 | DIFFUSE | 149 | The blue team uses Haiku 4.5 as the |
| DI-06 | DIFFUSE | 168 | proposals rated as worse than those of GPT-OSS-20B by the ground truth proxy scorer |
| DI-07 | DIFFUSE | 233 | robust blue-team prompts requires access to the ground truth proxy scorer, which the blue team may not have |
| DI-08 | DIFFUSE | 283 | solutions to the tasks it was given across a long deployment horizon |
| DI-09 | DIFFUSE | 264 | or untrusted monitoring with |
| DI-10 | DIFFUSE | 111 | w(\mathfrak{b},\mathfrak{r})>w^*-\varepsilon, |
| DI-11 | DIFFUSE | 143 | We evaluate the model on generating a set of ten ideas for experiments or high-level sketches of theoretical |
| DI-12 | DIFFUSE | 190 | show in the paper that the adaptive nature of the red team is necessary for a successful attack. |
| LR-01 | LOGIT | 31 | Apr 12, 2026 |
| LR-02 | LOGIT | 40 | logit(TPR) is linear in logit(FPR) |
| LR-03 | LOGIT | 52 | the fraction of malicious trajectories that has at least one action above the cutoff |
| LR-04 | LOGIT | 52 | the fraction of actions from benign trajectories above the cutoff |
| LR-05 | LOGIT | 52 | e.g. 1e-4, that is 1 audit for every 10,000 actions |
| LR-06 | LOGIT | 120 | sample that many values from a μ=0 σ=1 logistic distribution and take the max |
| LR-07 | LOGIT | 126 | it tends to hold if we fix the untrusted LLM, the attack task, the monitor LLM, and the monitor prompt |
| LR-08 | LOGIT | 405 | They do not hold if the “sneakiness” of the attacks vary widely |
| LR-09 | LOGIT | 93 | completely “miss” the attack some fraction of the time |
| LR-10 | LOGIT | 50 | averaging 20 agent actions per trajectory |
| LR-11 | LOGIT | 177 | We then filter the attack dataset down to scores for the single most suspicious step (according to the average score) of each trajectory |
| LR-12 | LOGIT | 257 | The best strategy might be to distribute your attack over a couple scripts which invoke one another |
| BL-01 | BLOCK | 29 | Mar 30, 2026 |
| BL-02 | BLOCK | 38 | We call actions “live failures” if their harmful effects are rapid and hard to recover from. |
| BL-03 | BLOCK | 48 | Asynchronous monitors are generally better at countering threats with low rates of damage. |
| BL-04 | BLOCK | 67 | they monitor each action individually instead of monitoring long trajectories all at once |
| BL-05 | BLOCK | 116 | 'running a subtly wrong experiment' might not have a merge-point where that can be caught |
| RE-01 | RETRY | 29 | May 29, 2026 |
| RE-02 | RETRY | 63 | Resampling hurts if resamples are aggregated for auditing decisions by taking the minimum, but helps if they are aggregated by max. |
| RE-03 | RETRY | 99 | auditing after three strikes doesn’t help |
| RE-04 | RETRY | 99 | Smarter monitors aggregate this information just fine by default, and adding in hand-holding decreases safety. |
| RE-05 | RETRY | 120 | Resampling without executing the least suspicious sample has zero usefulness impact. |
| RE-06 | RETRY | 122 | Of a +10.2 pp safety gain achievable by drawing four resamples on top of every original sample |
| RE-07 | RETRY | 105 | the attacker can decrease its suspicion a similar amount, leading to no net safety gain over trusted monitoring |
| RE-08 | RETRY | 69 | We chose to report safety results at an auditing budget of 0.3% |
| RE-09 | RETRY | 135 | still leak information about whether the previous step was suspicious enough to retry or not |
| RE-10 | RETRY | 92 | the optimal aggregation function will depend on the relationship between the cross-resample correlations of the attack and honest data |
| RE-11 | RETRY | 94 | we show that executing the least suspicious sample has almost no usefulness cost |
| RE-12 | RETRY | 67 | using Claude Opus 4.6 as an untrusted model and MiMo-V2-Flash as a trusted model |
| RE-13 | RETRY | 99 | Because our decision to audit an action doesn’t directly depend on any previous monitor scores |
| AG-01 | GAMES | 37 | Dec 9, 2025 |
| AG-02 | GAMES | 65 | We had very little success with black box methods. |
| AG-03 | GAMES | 71 | white box methods proved significantly more promising than black box ones |
| AG-04 | GAMES | 75 | the red team was later able to introduce false positives using distractor behaviours |
| AG-05 | GAMES | 91 | can be fragile and easily confused, leading to false negatives |
| AG-06 | GAMES | 49 | The red team trained five models using conditional underperformance ('password locking') as a proxy for sandbagging. |
| AG-07 | GAMES | 93 | black box methods proved largely ineffective |
| AG-08 | GAMES | 89 | it may be infeasible for messier, open-ended tasks where it’s hard to demonstrate perfect performance |
| RT-01 | REDTEAM | 37 | Jul 23, 2026 |
| RT-02 | REDTEAM | 39 | a separate LLM that reviews the agent’s actions and flags them if they are dangerous |
| RT-03 | REDTEAM | 55 | We found vulnerabilities in every monitor version we tested |
| RT-04 | REDTEAM | 78 | the evolutionary search eventually achieves a minimum suspicion score of 3 out of 100 |
| RT-05 | REDTEAM | 80 | we’d like to account for the random noise in a monitor’s score |
| RT-06 | REDTEAM | 88 | How do we estimate overall safety? |
| ST-01 | STRESS | 37 | Dec 16, 2025 |
| ST-02 | STRESS | 56 | (we enforce a 1% false positive rate) |
| ST-03 | STRESS | 64 | By Round 3, after seeing attack patterns and iterating, the best monitor missed only 6% at worst |
| ST-04 | STRESS | 75 | the weaker Round 1 monitor acting synchronously outperformed the best Round 3 monitor working asynchronously |
| ST-05 | STRESS | 54 | The Red team can only modify the agent's system prompt |
| ST-06 | STRESS | 83 | such as the ability to fine-tune models or rewrite model outputs |

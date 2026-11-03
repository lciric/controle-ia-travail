# Lecture comme le mentor — Jan Hendrik Kirchner, question 2 — v1

- Écrit le 3 novembre 2026, de 13:57 à 14:18 UTC (`date -u`), par un lecteur neuf qui n'a écrit aucune version des réponses. Consigne : `prompts-sous-agents/lecteur-mentor-kirchner-q2-v1.md`, sha256 `208ca028be979e49c3e2115269bc43fad934d29245430ecfa70229e2fcfd9c0d`, vérifiée, égale à son compagnon.
- Texte lu : `brouillons/redaction-finale-v1/kirchner-q2/reponse-v1.md`, sha256 `1f1e7982026052f2a1aad024fb61f4066a6e32186ae5d1af86749c1b548e130f`, vérifiée avant lecture. Texte seul, au-dessus de « --- » : sha256 `302eee6870b869ba20fc5c60683bbeb409fa701c2361ad764da9d7f06bacf1de`, égal à celui que déclare le rédacteur.
- Question, ligne 73 de `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (sha256 `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`) : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? » Aucune limite écrite ; visée : 450 mots au plus.

## 0. Sources et limites

| Source | Ce qui a été lu | Limite |
|---|---|---|
| Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner, arXiv 2608.28945, version 3, « Automated Researchers Can Mitigate Well-characterized Alignment Failures », 52 pages. Copie locale `brouillons/ideation-kirchner-q2-v1/sources/arxiv-2608.28945v3.pdf`, sha256 `6686c7bf3c80e319b3da79e12ac7e6ccf78c729a409815255748040cec14aa59`, égale à son compagnon et au fichier téléversé par Lazar (`/mnt/user-data/uploads/50b8c458-2608.28945v3.pdf`). | Texte extrait par `pdftotext` dans un dossier temporaire hors du dépôt. Relus en entier : §1 (p. 2), §2.3 (p. 4), §3.1 (p. 5), §5.1 (p. 7), §5.3 (p. 9), §7 (p. 10), A.3 (p. 21), C.2 (p. 30-31), D.1 à D.3 et figure 19 (p. 35 à 38), F.2 et figure 30 (p. 49-50), G et G.2 (p. 51-52). Recherche de mots sur tout le texte. | Pages : celles du fichier PDF. |
| Même papier en ligne, par `WebFetch` : PDF d'arXiv (§5.1, A.3) et billet du blog d'alignement d'Anthropic (D.3, figure 19). | Questions ciblées. | Concordant avec la version 3 sur chaque point vérifié. Le texte converti du PDF en ligne s'arrête en C.1, celui du blog en E.1. |
| Page publique citée par la réponse : `lciric/ideation-organism`, commit `faff48bfc16821f069e030bf42733be328fa1145` (3 novembre 2026, 10:23:43 UTC), `resultats/controle-simulation-defenses/README.md`. | En entier, par `gh api` en lecture seule (dépôt public vérifié). sha256 de la copie lue : `04ce0afcedb95478103fb76c15680f185e8614c0f0ed08616162d848270d8ba0`. | Pièces jointes en français non lues. |
| `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-kirchner-v1.md` | En entier, pour le contexte. | Écrit pour l'ancienne réponse ; n'avait pu lire ni F ni G. |

Refus d'accès, non contournés : arxiv.org en ligne de commande (le mandataire répond 403, refus de politique) ; version HTML d'arXiv `https://arxiv.org/html/2608.28945` par `WebFetch` (autorisation non accordée à temps). Non lus volontairement, pour rester neuf : `note-piste-v1.md` et `registre-affirmations-v1.md` du rédacteur.

## Verdict

Aucun point bloquant. Sur la version 3, tout ce que la réponse prend au papier du mentor est exact : treize renvois vérifiés, mot pour mot quand ils sont entre guillemets, annexes F.2 et G.2 comprises. Le lien public porte les chiffres cités. 441 mots, sous la visée. Deux points à corriger : la seconde expérience compare la règle d'arrêt à un gagnant que le banc tenu à l'écart a aussi choisi (M13) ; « Ville's rule » n'est défini nulle part, et le papier du mentor n'emploie jamais ce vocabulaire (L1). Le reste est mineur.

## 1. La phrase qu'il contredirait

Aucune phrase de la réponse n'est contredite par son texte. Le tableau donne chaque renvoi vérifié ; la colonne « ce qu'il dirait » ne note que les frottements.

| # | Réponse (mots exacts) | Sa source (version 3, page du PDF) | Ce qu'il dirait | Gravité |
|---|---|---|---|---|
| M1 | « a question your Appendix D.3 leaves open: how much of the automated researchers' climb above the median is selected noise » | D.3, p. 35 : « which leaves open how the audit score varies over the rest of the leaderboard » ; p. 36 : « We pose this as a question rather than a result. » Aucun des mots « noise », « selection », « chance », « luck », « variance », « seed » dans D.3. | « D.3 laisse ouverte la forme du sommet ; le bruit, c'est votre lecture. » La réponse le dit elle-même deux phrases plus loin (« A fourth comes from your Section 5.1 »). | mineur ; au choix : « a question your Appendix D.3 leaves open: » → « a question behind your Appendix D.3: » (−1 mot). |
| M2 | « On Petri, the test nothing is selected on » | §2.3, p. 4 : « Petri, which nothing is selected on, is the test. » | — | exact |
| M3 | « your deception winner scores 5.65 ± 0.61 against 5.42 ± 0.64 for the median method (lower is safer) » | D.3, p. 36 : « the winning method at the 99th percentile scores 5.7, no better than the median method and within its interval (5.42 ± 0.64 against 5.65 ± 0.61) » ; figure 19, p. 38 : « 100 audits per method, error bars are 95% confidence intervals », « lower is safer ». | — (ordre inversé, attribution juste) | exact |
| M4 | « on prompt injection the median already wins 6.2 of the 6.6 points » | D.3, p. 36 : « reaching the median method wins 6.2 of the 6.6 points and everything above it wins 0.4 » (base non entraînée à 8,7 : p. 37). | — | exact |
| M5 | « Your three readings (a ceiling, a floor, log-linear returns) remain unseparated. » | p. 36-37 : « Three readings are consistent with what we measure, and we have not run the experiments that would separate them » ; « A ceiling in the hill-climbing suite », « A floor set by the target models and the compute budget », « Log-linear rather than flat returns ». | — | exact |
| M6 | the AAR's number is « the best of roughly 150 scored methods, so it is biased upwards by taking a maximum over noisy evaluations. » | §5.1 « Main results », p. 7 : « The AAR's number is also the best of roughly 150 scored methods, so it is biased upwards by taking a maximum over noisy evaluations. » | Peut noter que sa phrase vise la comparaison aux idées humaines ; le transfert au sommet du classement reste juste. | exact, mot pour mot |
| M7 | « A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average: one gain, not the best of 150. » | A.3 « Choosing target models », p. 21, critère (iii) : « at least 25 scorable samples, meaning independently graded units the benchmark's scorer returns a verdict on and over which its confidence interval is computed, […] so its score has low enough sampling variance to separate a real gain from noise. On average, each benchmark we select has around 200 test examples. » | — (le seuil est un plancher de 25, 200 la moyenne ; « one gain, not the best of 150 » est une déduction du candidat, juste) | exact |
| M8 | « Your integrity monitor flags "reporting the best of many seeds or evaluation runs" (G.2) » | G.2, p. 52, consigne abrégée du juge du moniteur d'intégrité : « Seed cherry-picking: reporting the best of many seeds or evaluation runs. » | — | exact, mot pour mot |
| M9 | « Retrain each from its code snapshot » | §3.1, p. 5 : « each result is posted to the forum with a code snapshot » ; D.1, p. 35 : « retrain its winner from source ». | Il l'a déjà fait (D.1) : faisable chez lui. | exact |
| M10 | « 120 training runs, about 60 H200-hours of training, 4,000 audits » | §3.1, p. 5 : « an H200 GPU and roughly 30 minutes of training » ; D.3 : 100 audits par méthode. 2 défaillances × 20 méthodes × 3 graines = 120 ; × 0,5 heure = 60 heures ; 2 × 20 × 100 = 4 000. | — | exact |
| M11 | « all items of a submission share one trained model, yet your intervals are computed over items » | A.3, p. 21 (citée en M7) ; une méthode, un entraînement (§3.1). Ses intervalles des figures 7 et 12 et de F.2 portent sur des courses ou des défaillances, pas sur une soumission. | Rien dans ce contexte. | exact ; mineur : « your intervals » → « your A.3 intervals » (+1 mot) ancre la phrase dans son texte. |
| M12 | « your F.2: about 0.8 of the final score comes in a run's first quarter » | F.2, p. 49 : « the score reaches about 0.8 of its final value in the first quarter of the run » ; moyenne sur les dix courses ; score = meilleur score atteint jusque-là, divisé par sa valeur finale ; avancement = rang de la méthode divisé par la longueur de la course. | « C'est une moyenne sur dix courses. » Le pari l'applique à chaque course (« within each climb's first half ») : acceptable pour un pari. | fidèle |
| M13 | « then audit its pick and your winner 400 times each. Second number: their Petri gap. » ; plus loin : « your winner safer than the rule's pick by 0.5 points or more (stopping early costs safety) » | §2.3, p. 4 : « we take the leading methods on the leaderboard and pick the one that scores highest on the held-out benchmark. The held-out benchmark is therefore a validation set for that choice » ; C.2, p. 31 : « the seven methods the AAR ships, one per alignment failure, chosen from the top three on that leaderboard by held-out generalization ». | « Mon gagnant n'est pas le maximum du classement : il passe par le banc tenu à l'écart. Sans la même étape pour votre règle, l'écart de Petri mesure cette étape, pas l'arrêt précoce. » Le biais joue contre le pari du candidat, mais la lecture « stopping early costs safety » serait confondue. | **à corriger** : « then audit its pick and your winner » → « then audit its pick (same held-out tie-break) and your winner » (+3 mots). |

## 2. Affirmations plus fortes que leur preuve

Aucun « shows », « proves », « always » ni « never » dans le texte (recherche par script). Restent :

- **A1, mineur.** « a threshold calibrated on 1,000 whole honest episodes held 4.6–5.5% ». Exact (page publique : « 0.046 to 0.055 in all 17 settings »), mais la même page dit les épisodes de calibrage « drawn from the same law as the test », et que la tenue sous un écart entre calibrage et emploi « is not tested in T0.3 » (contrôle d'instrument). La réponse transpose à un seuil calibré sur les relances de 40 méthodes choisies, puis appliqué à toutes les soumissions : c'est l'échangeabilité qui porte. Correction : « held 4.6–5.5% » → « held 4.6–5.5% (exchangeable episodes) » (+2 mots).
- **A2, rien à changer.** « 21–35% false alarms at the strongest settings » : la page dit que 0,21 à 0,35 sont les trois réglages d'effet d'épisode les plus forts (les plus faibles donnent 0,034 à 0,107) et que ces cellules ont été choisies après des courses exploratoires (pas de prédiction à l'aveugle). « at the strongest settings » est la réserve honnête ; « preregistered » est exact.
- **A3, rien à changer.** « where methods may differ by less than the noise, a leaderboard does that by design » : « may » protège. Ses pages en donnent l'indice (D.3 : gagnant dans l'intervalle de la médiane sur Petri ; §5.3, p. 9 : « each condition is a single run, so we read the result as suggestive »), pas la mesure sur la suite grimpée, que l'expérience 1 fournit justement.
- « the best of N noisy scores rises with N » : vrai en espérance pour des bruits indépendants.

## 3. Ce que la question demande et qui manque

Les trois demandes sont couvertes : le problème et pourquoi il est sous-estimé (paragraphes 1 et 2), la première expérience (3 et 4), le résultat qui ferait changer d'avis (5).

- **Q1, à corriger** : la comparaison non appariée de la seconde expérience (M13).
- **Q2, mineur** : le seuil de 0,5 point porte-t-il sur les estimations ponctuelles ou sur un intervalle ? Avec 400 audits de chaque côté, la demi-largeur à 95 % d'un écart vaut environ 0,44 point (déduit des ± 0,61 et ± 0,64 de D.3 à 100 audits : écart-type par audit de 3,1 à 3,3). Sur les estimations ponctuelles, le seuil se déclenche à tort environ 1,3 % du temps si l'écart vrai est nul, 19 % s'il vaut 0,3. « Fixed in advance » appelle la précision : « by 0.5 points or more » → « by 0.5 points or more (point estimates) » (+2 mots).
- **Q3, mineur** : « give it 100 Petri audits » : sur lequel des trois modèles réentraînés ? Le total de 4 000 dit 100 par méthode : « 100 Petri audits across its seeds » (+2 mots).
- **Q4, mineur** : la partie temporelle du pari (« crowned within each climb's first half ») n'a pas de résultat contraire annoncé.
- **Q5, mineur** : l'enjeu d'alignement au-delà de son papier (une boucle de recherche automatisée certifie un gain de sécurité par un maximum dont le biais croît avec le nombre de soumissions) n'est dit qu'en creux, par « grows with throughput ». Le mentor le verra ; un second lecteur, moins.
- **Q6, facultatif** : rescorer aussi sur le banc tenu à l'écart dans l'expérience 1 dirait si la marge qui survit se généralise ; c'est son propre ensemble de validation (§2.3).

## 4. Ce qui le perdrait

- **L1, à corriger** : « Ville's rule, nominally 5% ». Jamais défini ; le papier ne contient ni « Ville », ni « e-value », ni « e-process », ni « martingale », ni « anytime » (zéro occurrence sur le texte de la version 3). Correction : « Ville's rule, nominally 5%, » → « Ville's always-valid alarm rule, nominally 5%, » (+2 mots).
- **L2, mineur** : « e-value rule » : même famille, mais la phrase dit ce que fait la règle ; suffit une fois L1 corrigé.
- **L3, mineur** : « a shift shared by an episode's scores » : « episode » est l'unité du candidat ; le mentor doit la traduire en « submission » : « an episode's (your submission's) scores » (+2 mots).
- **L4, mineur** : « at the strongest settings » : les plus forts de quoi ? « at the strongest shared shifts » (+1 mot).
- **L5, mineur** : « one gain, not the best of 150 » : trop serré, se relit. « sized for one gain, not the best of 150 » (+2 mots), ou laisser.
- **L6, mineur** : la phrase de 36 mots « I would replay each logged climb […] 400 times each. » est dense ; « counting every submission » (la règle paie chaque tentative) en est le passage le plus dur.
- Rien d'autre : « AAR » est son propre terme, « H200 » un nom de produit ; chaque nombre a son unité ; le « ± » suit la convention de sa figure 19. Le lien a sa raison (vérifier le chiffre propre au candidat), page en anglais, épinglée à un commit, qui dit ses limites : à garder. Sans enjeu : le message du commit `faff48b` porte sur une autre pièce (« Ideation LLM judges v2, draft 3 (not sealed, not counter-read) ») ; la page elle-même dit la simulation exécutée une seule fois le 4 octobre, préenregistrement scellé.

## 5. Ce qui le retiendrait — à ne pas couper

- **La justesse** : treize renvois vérifiés, trois citations mot pour mot de son texte (§5.1, A.3, G.2), jusque dans les annexes F et G, qu'on lit rarement. Il verra que le candidat a lu tout le papier.
- **La quatrième lecture** : D.3 écrit « We pose this as a question rather than a result » et « we have not run the experiments that would separate them » ; la réponse tire la lecture manquante de son propre §5.1 et propose l'expérience qui la départage.
- **La phrase sur G.2** : son moniteur range « reporting the best of many seeds or evaluation runs » dans la triche ; un classement le fait par construction quand les écarts sont sous le bruit. Courte, vérifiable, cohérente avec son §1, p. 2 (« re-submitting an unchanged method in the hope that scorer variance produces a higher (noisy) score »).
- **La faisabilité chez lui** : instantanés de code (§3.1), réentraînement depuis la source (D.1), 100 audits par méthode (D.3), 30 minutes par H200 (§3.1) ; 60 heures de H200 en tout.
- **Deux nombres annoncés** et deux seuils qui feraient changer d'avis, fixés d'avance.
- **L'unité d'analyse** (tous les items d'une soumission partagent un modèle) : absente de son papier, appuyée sur la simulation préenregistrée du candidat, publique, épinglée, qui dit ses propres limites.

## 6. Compte de mots

| Mesure (texte seul, au-dessus de « --- ») | Valeur |
|---|---|
| `str.split()` (Python) | 441 |
| `wc -w`, locale C.UTF-8 | 441 |
| `wc -w`, locale POSIX (ne compte pas les deux « ± » isolés) | 439 |
| `\w+`, pire cas (décimaux et lien coupés) | 484 |
| Signes | 2 671 |
| Par paragraphe | 127, 50, 76, 105, 83 |

Concorde avec le compte déclaré dans le fichier. Limite écrite : aucune (ligne 73). Visée de 450 : respectée, marge de 9 mots. Les deux corrections à corriger coûtent +5 (446). Les mineures coûtent ensemble +12 et ne tiennent pas toutes sous 450 ; priorité suggérée L3, Q2, A1 (+6, soit 452), à compenser par « about 60 H200-hours of training » → « about 60 H200-hours » (−2) : 450. Seul le texte au-dessus de « --- » se colle dans le formulaire.

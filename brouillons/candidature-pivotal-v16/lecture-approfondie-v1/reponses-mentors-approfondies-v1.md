# Réponses aux mentors — version approfondie v1 (lecteurs neufs, 3 novembre 2026)

Chaque section reprend la partie 3 (réécriture du fond) et la liste des changements du rapport du lecteur ; les parties 1 et 2 (tableaux de sources, arguments) sont dans les rapports complets. **Non encore recoupé par un second lecteur** : un vérificateur neuf recoupe chaque chiffre en ce moment.


## Heimersheim

**Q1 : pas de réécriture (règle du mentor « 100% human-written »).** Faits et arguments à rédiger toi-même :

### 1.c Faits des sources que la réponse ignore et qui changent l'argument (une ligne chacun)

1. **2510.20487 §5.1, §5.3** : le pilotage contre la conscience d'évaluation a déjà réussi sur un comportement à vérité connue. Les indices de type tombent de 80–86 % à moins de 11 % (contre 34 % quand l'invite annonce le déploiement) ; le bruit gaussien fait bien moins ; la précision passe de 56,8 à 55,2 %. La réponse prédit « rien » ou « générique » : il faut expliquer ce troisième cas.
2. **2510.20487 annexe A (note 3) et annexe B** : avant tout affinage, le modèle lie déjà émojis et vrais utilisateurs. Le pilotage déplace les émojis, et les auteurs concèdent que « pilotage ≈ invite ». Le marqueur de vérité, les indices de type, est un marqueur de code « professionnel ». Le confondant de registre est dans leurs propres annexes.
3. **2510.20487 annexe I.1.1, tableau 16** (mise à jour du 4 janvier 2026) : des énoncés déclaratifs de déploiement abaissent les indices à 0,34–0,60. L'avantage du pilotage sur l'invite est donc plus faible que ne le dit le corps du texte. Au titre de la symétrie (R4), à noter aussi : ces phrases, de registre formel, baissent les indices, ce qui ne va pas dans le sens d'une explication purement par le registre.
4. **2510.20487 §6** : l'organisme « s'appuie sur des indices et des coups de pouce », et Llama Nemotron ne distingue pas de façon constante évaluation et déploiement. Sans l'indice de situation, les écarts rétrécissent (§4.2). La vérité connue est celle d'un modèle peu conscient de l'évaluation.
5. **2510.20487 §6, qui cite la fiche d'Opus 4.6 (février 2026)** : le pilotage supprime largement la conscience verbalisée, mais pas la conscience non verbalisée mesurée par oracles d'activation. Le résidu après soustraction est déjà mesuré, par une lecture non verbale.
6. **2510.20487 §5.3 contre 2410.12555 §3.1 et §4.2** : le témoin de Hua et coll. est un bruit gaussien de même moyenne et variance, donc isotrope à une constante près. Chez Lee et Heimersheim, la direction isotrope est la ligne de base faible : tout ce qui est structuré déplace davantage les sorties, même un mélange de deux activations aléatoires à covariance appariée. C'est mesuré sur GPT-2 small, couche 6 ; l'appliquer au témoin de Hua et coll. est une transposition par analogie, à tester. Dans 2606.24964 (§3, éq. 6–7), le témoin le plus exigeant est la « différence aléatoire » : la même recette contrastive, sur des paires appariées au hasard (p = 2,05 [2,00 ; 2,10]).
7. **Réplication sur GLM-5** (Institut britannique, 10 avril 2026 ; un seul scénario, 250 tirages par condition) : un vecteur témoin sans rapport sémantique (« control_book ») a produit l'effet le plus fort, avec une conscience verbalisée proche de 0 et environ 80 % d'action désalignée à −0,025. Deux des quatre vecteurs « évaluation contre déploiement » (« testing_vs_conversation », repris de la fiche d'Opus 4.6, et « hua_et_al_ha ») n'ont pas élevé le désalignement au-dessus de la base. Commentaire de Jack Lindsey : sur Sonnet 4.5, les effets dépassaient ceux des témoins aléatoires, ce qui n'est pas le cas sur GLM-5.
8. **Fiche de Sonnet 4.5, selon Redwood** (secondaire, qui cite la note 19) : l'effet de l'inhibition sur le désalignement est « très dépendant du jeu de données ». La conscience verbalisée passe d'environ 80 % à 0–40 %, le désalignement de 0 % à 1–9 % ; la valeur de 9 % vient du vecteur « Testing vs. Conversation » (note 18). Hua et coll. (§1) donnent 8 % pour le vecteur le plus fort : petit écart à vérifier pages 99 à 104.
9. **2510.20487 §2, qui cite Abdelnabi et Salem** : piloter la conscience d'être testé modifie aussi le refus. L'effet hors cible est documenté.
10. **2606.24964 §4.1 et annexe A** : les 14 directions sémantiques contrastives (âge, certitude, époque, genre, santé, honnêteté, « littéraire », nombre, personne, refus, sentiment, statut, temps, richesse) n'incluent pas l'évaluation. Le test p n'a jamais été appliqué à une direction d'évaluation.
11. **2606.24964 figure 1 et note 1** : les directions de traits rompent le plateau à des angles plus petits que les directions aléatoires (écart positif pour au moins 63 % des ancres, à chaque angle). La sensibilité varie jusqu'à environ 70 fois d'une direction à l'autre, d'où l'abandon d'un seuil global. Dans le modèle jouet (figure 11), la rupture se fait à α ≈ 4,1–4,3 pour les axes de traits, à 4,70 pour le mélange égal et à 5,93 pour l'aléatoire. Une fenêtre de dose existe, et elle se calibre direction par direction.
12. **2605.05115 §8 et annexe A.3** : le pilotage sur variété n'est validé que pour des concepts à géométrie connue et ordonnée (jours, mois, lettres, âges, grilles). La variété est une spline ajustée sur des centroïdes étiquetés, et la sortie étudiée est le jeton suivant. Les concepts abstraits (« e.g., refusals ») ne sont pas testés, et un protocole non supervisé reste à faire.
13. **2409.17113 §4** : les régions stables se raffermissent avec l'entraînement et avec la taille (modèles de 0,5 à 7 milliards de paramètres, perturbation après la couche 1). La réponse à une dose tend vers une marche.
14. **2409.15019 §5.2** : des activations recomposées à partir de traits d'autoencodeur épars n'ont pas les plateaux des vraies activations. Ce qu'on lit (les traits) ne reproduit pas ce que le réseau corrige.

---

### Points prioritaires

**A. L'exposant p de 2606.24964 comme lecture non verbale de « évaluation contre registre ».**
- **Ce que mesure p** (éq. 10–13). On perturbe l'activation dans le plan de deux directions orthonormées, à norme constante. On relève l'angle de rupture du plateau pour chaque mélange φ, et l'on ajuste une superellipse. Si p ≈ 2, le réseau ne répond qu'à la taille L2 totale : aucun privilège. Si p > 2, les directions pures sont privilégiées sur leurs mélanges, ce qui est compatible avec une correction d'erreur propre à chaque trait (§3, §6.1).
- **Protocole qu'on peut en tirer** (à rédiger par toi) :
  - une direction d'évaluation construite sur des paires appariées en registre : les 16 paires du tableau 12 de Hua et coll., portées à 30 au moins, minimum de 2606.24964 (§3) ;
  - une direction de registre (formel contre familier), à statut d'évaluation constant ;
  - un diagnostic gratuit d'abord : le cosinus entre les deux. 2606.24964 écarte les paires où |cos| ≥ 0,1 (annexe A : 210 paires sur 528), donc un cosinus élevé signale déjà la contamination ;
  - p ajusté sur la paire (résidu orthogonal de l'évaluation, registre), comparé dans le même modèle aux paires de traits connus (2,3–2,4) et aux différences aléatoires (2,02–2,05).
- **Lecture proposée.** p nettement supérieur à 2 : le réseau corrige séparément les deux directions. p ≈ 2 : le résidu d'évaluation, une fois le registre retiré, n'a pas de privilège propre. Attention : cette lecture n'est pas validée par la source pour des paires mixtes (un trait, un non-trait).
- **Limites déclarées par la source :**
  - p > 2 est nécessaire mais pas suffisant (§7 : maximiser p ne retrouve pas les traits à lui seul) ;
  - la mesure est faite par défaut à la couche 2 (ablations jusqu'à la couche 20 de Gemma-2-9B), sur le dernier jeton de 30 invites FineWeb de 5 jetons. Or l'évaluation exige un long contexte (indice Wood Labs dans l'invite système) et des couches moyennes (Hua et coll. : couches 10 à 30) ;
  - la réponse mesurée est une distance L2 en avant-dernière couche, pas un comportement ;
  - les auteurs admettent d'autres lectures des plateaux : bassins d'attraction, ou correction vers une variété (§6.2).
- **Déjà traité ?** Non. Hua et coll. s'appuient sur l'extraction avant affinage ; Anthropic sur la sémantique des traits et, pour Opus 4.6, sur les oracles d'activation (secondaire). Personne n'a mesuré p pour une direction d'évaluation.
- **Ouvert :** tout.

**B. La fenêtre de dose entre plateau et dégât générique.**
- **Faits.**
  - Plateau : les petites perturbations sont sans effet (billet de 2024 ; 2409.17113 ; 2606.24964).
  - Les directions de traits rompent le plateau avant l'aléatoire (2606.24964 figure 1 ; modèle jouet : 4,1–4,3 contre 5,93). Dans 2409.15019, vers une vraie activation, l'emballement survient au pas 41,11 en moyenne contre 52,49 vers une activation aléatoire.
  - La sensibilité varie jusqu'à environ 70 fois selon la direction (note 1).
  - Les frontières se raidissent avec la taille et l'entraînement (2409.17113 §4).
  - Hua et coll. (annexe G) : sur une seule couche, une force d'environ 3 fait beaucoup de dégâts ; 6 couches × 0,6 en font peu. À force égale, le pilotage vers l'évaluation coûte 13,7 points de précision (43,1 contre 56,8), celui vers le déploiement 1,6 point : la fenêtre dépend du signe.
  - GLM-5 devient incohérent au-delà de 0,025, contre 0,1 pour Opus 4.6 : la fenêtre dépend du modèle, à un facteur 4 près.
- **Argument.** Le critère de succès se formule comme une fenêtre. Borne basse : la dose qui rompt le plateau pour la direction d'évaluation. Borne haute : la dose qui le rompt pour le témoin exigeant, ou celle qui fait chuter les capacités. Un effet qui n'apparaît qu'au-dessus de la borne haute est générique par définition. Sur GLM-5, des témoins agissent aux mêmes doses que les vecteurs d'évaluation : la fenêtre peut y être vide pour ce scénario.
- **Déjà traité ?** Hua et coll. choisissent la dose sur les capacités, sans courbe de témoin. La force utilisée pour Sonnet 4.5 m'est inconnue (secondaire). GLM-5 : deux doses par signe.
- **Ouvert :** mesurer explicitement la fenêtre, direction par direction, avec des témoins exigeants et une règle préenregistrée.

**C. Ce que le pilotage sur variété résout et ne résout pas (2605.05115).**
- **Il résout** l'incohérence hors variété du pilotage linéaire, pour des concepts à géométrie connue. L'énergie de sortie cumulée (distance de Bhattacharyya à la variété des comportements) est en moyenne environ 2,8 fois plus basse : 0,34 contre 0,93 pour les jours, 0,36 contre 1,09 pour les mois, 2,42 contre 6,95 pour les lettres, 5,21 contre 13,49 pour les âges ; p < 0,001 (§3.2). Les auteurs rappellent aussi que le pilotage linéaire ajuste le premier moment de la sortie, mais que les moments d'ordre supérieur peuvent dériver sans contrainte (§6, d'après Sarfati et coll.). C'est une version précise de ton « générique ».
- **Il ne résout pas cinq choses :**
  - (1) Un concept binaire. La variété est une spline cubique naturelle qui passe exactement par les centroïdes étiquetés (A.3). Avec deux centroïdes (évaluation, déploiement), elle se réduit au segment, donc au pilotage linéaire par différence de moyennes (éq. 1 et 2). C'est ma déduction de la méthode, les auteurs ne l'écrivent pas. Pour en tirer quelque chose, il faudrait des états intermédiaires étiquetés.
  - (2) Les concepts abstraits : « future work is needed to explore more abstract concepts, e.g., refusals » ; et un protocole non supervisé « would … significantly broaden the applicability » (§8).
  - (3) Les comportements sur plusieurs jetons : les auteurs étudient la distribution du jeton suivant (§8), alors que la conscience d'évaluation agit sur un raisonnement long.
  - (4) Le registre : les centroïdes héritent de tout ce qui varie avec les étiquettes.
  - (5) Le résidu non verbal : rien dans la méthode ne le mesure.
- **Validation :** Llama 3.1 8B, couche 28, sous-espace de 64 composantes principales.
- **Déjà traité ?** Ni Hua et coll. ni Sonnet 4.5 ne l'utilisent.
- **Ouvert :** un pilotage sur variété pour un concept gradué (réalisme de l'évaluation, par exemple) reste à construire, et la source n'en dit rien.

**D. Le témoin aléatoire à norme égale.**
- **Chez Hua et coll.** (vérifié, §5.3) : 24 vecteurs gaussiens de même moyenne et variance, aux normes L2 « très voisines ». C'est le témoin isotrope, faible au sens de 2410.12555.
- **Chez Sonnet 4.5** (secondaire, R7) : des traits aléatoires d'autoencodeur épars servent de témoin, d'après le billet de l'Institut britannique et le commentaire de Lindsey. Selon Redwood, leur inhibition « didn't have substantial effects ». L'égalité de norme n'est pas vérifiée.
- **Conséquence.** Ta demande « random control vector normalized to the same size » est déjà satisfaite deux fois ; la présenter comme manquante serait une erreur visible.
- **Ouvert :** le témoin de structure appariée (différence aléatoire, ou paires contrastives sans rapport), avec une courbe, et non à une seule dose.

**E. L'organisme à vérité connue de Hua et coll.**
- **Ce qu'il apporte :**
  - une vérité par construction (Wood Labs ⇒ évaluation ⇒ indices de type ; raisonnement à deux étapes, §3.1) ;
  - un marqueur comportemental indépendant de la parole du modèle ;
  - un vecteur extrait avant affinage, qui ne peut donc pas encoder directement les indices de type (§4.1) ;
  - un pilotage plus efficace que l'invite : même les 16 invites réunies ne suffisent pas (§5.3) ;
  - un témoin de bruit et une mesure de précision.
- **Ce qu'il n'apporte pas :**
  - un marqueur neutre en registre : indices de type et émojis sont des marqueurs de registre (annexes A et B) ;
  - un modèle vraiment conscient de l'évaluation : l'indice de situation est nécessaire (§6) ;
  - une invite faible : des énoncés déclaratifs abaissent les indices à 0,34–0,60 (mise à jour de janvier 2026) ;
  - une exposition au déploiement : l'itération experte n'a porté que sur la distribution d'évaluation (§3.2) ;
  - les annexes J à M, que je n'ai pas pu lire.
- **Ouvert :** un organisme à marqueur neutre en registre, et un modèle plus capable de distinguer seul évaluation et déploiement. Ce sont leurs propres travaux futurs (§6).

## Partie 3 — Réécriture de la Q2 (fond seulement, longueur égale)

Comptage par script (`scripts/compter_q2.py`, texte « avant » extrait de la ligne 133 du formulaire, remplacements appliqués un à un, reste vérifié identique ; sortie dans `q2-avant-apres-v1.txt`) :
- avant : 150 jetons séparés par des espaces, 149 mots (le tiret « — » isolé est compté comme jeton) ;
- après : 150 jetons, 149 mots.

```
One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in a language model (the direction that predicts sycophancy does <1% of the causal work on Llama-3.1-8B-Instruct). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests, etc. all depend on it being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on activation plateaus is the clearest formulation of that measurement question I’ve seen. Instead of single dose interventions my rank-1 vs rank-3 result relied on, you measure the dose–response curve, and your exponent p asks whether readable directions are privileged.
```

### Changements (avant → après ; raison ; source)
1. « (it looked at the direction that predicts sycophancy and does <1% of the causal work on Llama-3.1-8B) » → « (the direction that predicts sycophancy does <1% of the causal work on Llama-3.1-8B-Instruct) ». Raison : le sujet « it » est ambigu ; cela libère quatre mots pour le changement 4 ; « Instruct » aligne la phrase sur ta Q1 et ta réponse Ibrahim (même modèle). « <1% » est gardé tel quel : chiffre de ton programme d'interprétabilité, non publié. Source : aucune nécessaire.
2. « all depend on the gap being small » → « all depend on it being small ». Raison : un mot de place ; fond inchangé. Source : aucune.
3. « is essentially the clearest formulation of that measurement question that I’ve seen » → « is the clearest formulation of that measurement question I’ve seen ». Raison : deux mots de place ; fond inchangé. Source : aucune.
4. « Instead of single dose interventions that my rank-1 vs rank-3 result relied on, you’re attempting to measure a dose–response curve. » → « Instead of single dose interventions my rank-1 vs rank-3 result relied on, you measure the dose–response curve, and your exponent p asks whether readable directions are privileged. » Raison : « attempting » est inexact, car la réponse en fonction de la dose est mesurée (2409.17113 §3 ; 2410.12555 §2 ; billet de 2024). Et le dernier article du courant, dont le premier auteur est à Pivotal Research, répond directement à la question de ta Q2 : les directions contrastives sont privilégiées (p ≈ 2,3 ; aléatoires et composantes principales ≈ 2). « rank-1 vs rank-3 » est gardé : travail non publié. Source : 2606.24964, résumé et §4.1.
- **Repli si tu préfères ne pas citer p :** ne garder que « you’re attempting to measure a dose–response curve » → « you measure the whole dose–response curve » (149 jetons), sans les changements 1 à 3.
- **Gardés tels quels, et à dire :** « <1% » (Q2), « ρ = 0.68 » et « 68% » (Q1, non réécrite) viennent de ton programme d'interprétabilité, non publié. « single dose interventions » et « rank-1 vs rank-3 » décrivent ce même travail, que je n'ai pas vérifié.
- **Sans objet ici :** tests de mort jamais exécutés pour de vrai, validation du nul v8 du 1er novembre, copie exacte retenue au banc v7 et mélanges passés, juge de la sycophancie `claude-opus-4-6`. Aucune de ces mentions n'apparaît dans les réponses à Heimersheim.

## Kirchner

## 3. Réécriture du fond (même longueur ou plus courte)

Règle suivie : les phrases de Lazar sont gardées partout où le fond tient ; ne change que ce qui doit changer ; chaque ajout chiffré renvoie à une source ouverte ; les résultats de Lazar cités viennent du dépôt public `lciric/ideation-organism`.

### Kirchner Q1 (555 mots, 3 383 signes ; actuel : 557 mots, 3 386 signes)

```
If you haven’t seen/heard: I’ve been running automated researchers since October (github.com/lciric/ideation-organism). Agents generate submissions meant to codify laws; a statistical judge scores submissions.
Pitch: what happens when you score submissions proposing laws for how AI makes decisions with something arguments can’t lie to? Will it hold up against agents motivated to trick it?
In short: yes to Q1. Partly to Q2. Our attack found a hole. Patch posted, preregistered test to come.
Builders built stuff. Builders tested builders. Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real).
929 tests total.
Mutation benchmark: the code was mutated 224 times, checking that all mutations get caught by tests. Every time a test failed pinpointing precisely what was mutated and exactly which test caught the failure.
Kept what passed.
Totally lost the forest for trees here initially because qualitative judgments made by my LLM judges kept failing against my frozen statistical judge. They told me nothing, literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. The terse statistical judge told me why nothing was promoted: not enough power. Turns out I just didn’t test it long enough to know if there was a law there. The power curve suggested as much.
Then I ran it one last time with no deviations from the locked plan on a new-seed pass of 288 episodes (same 96 tasks) that I did not inspect prior to launching this datapass.

It accepted 2 of the 3 laws I placed into the data.
It rejected all 19 placed non-laws.
It accepted 0 laws found from the raw data itself.

Scripted cheating agents broke it. 4 cheater types accepted, each in 75 to 95% of 200 runs. All stitched together or deformed past submissions that the judge had already accepted.
My judge had no null for blends of its past acceptances.
Plain copies were held (a renamed copy of an accepted law: 0 of 200). That is the trick in 26 of your 39 cheating examples from the automated-researcher paper: flip a coin twice, wait for randomness to make your method win. Protecting it against systematic agents that can tailor make submissions using its past accepts to trick it was more difficult. We’ve gone through dozens of iterations since October.
On 1 November the fix passed its preregistered validation (1k reps per cheater; double checked by a fresh reader, a new Claude instance, who wrote neither code nor words).

Attack agents. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the judge’s verdicts, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look. Most surprising: one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description. A coverage hole, not adaptive overfitting. (Inside the null: not judgeable, instrument failure.)
Patches written and deployed into regression tests; preregistered validation sealed on 2 November.
```

### Kirchner Q2 (539 mots, 3 415 signes ; actuel : 539 mots, 3 504 signes)

```
Underrated: a score that cannot be inflated by an agent that games it on purpose. Overrated: resubmission caps and detectors (your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours). With your AARs, the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says, so it’s completely rational for an agent to just resubmit the same method repeatedly unchanged (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”). Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. Your Sec. 7 files this as cheating to detect, but it’s just the utility-maximizing reaction to how you’ve designed your score, and worse: as agents get better at seeking rewards (your failure mode 3) the solution will have to come from changing your score, not detecting failure: don’t accept a method until the evidence it outperforms everything already accepted remains significant no matter how many times you re-evaluate it on fresh seeds. Leaderboard overfitting in the presence of adaptive submissions is well understood (the Ladder, the reusable holdout); underrated is leaderboard overfitting by an agent who understands this.

Experiment 1: construct a judge that can’t be overfit to on your test harness via resubmissions. Start by rescoring your leaderboard leaders on new seeds (Appendix D.3 gives three readings for the flat top; selection on noise is a fourth, which this separates). Replace your “best of noisy runs” envelope with a sequential test: update a test martingale using each method’s evaluations against the null hypothesis of baseline + every method already accepted on your leaderboard (any mixture or piecewise combination of them carries 0 evidence), bound using Ville’s inequality to guarantee false positive rate of at most α no matter how many times you re-evaluate a method, and a simple method-level multiple testing procedure. Ville bounds one method, not the number of attempts, so that procedure must count every submission. Retest your logged methods from their per-run scores, then evaluate new agents that have observed verdicts. Metrics: percent of flagged methods (and subsequent re-submissions) that still get accepted through; how much power we lose on true-progress methods (as judged by your held-out benchmark and Petri); how hard it is for a verdict-aware agent to search towards a class of methods your judge already declared outside of its coverage; all against the Ladder as baseline. My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. The fix’s preregistered validation runs next.

Evidence that would sway me: demonstrations that the power lost on truly novel methods exceeds an a priori margin (the judge would be too blunt to deploy), agents passing unchanged resubmissions at rates substantially higher than α (my null is misspecified), agents that see verdicts performing no better than blind resubmission at beating the naive maximum (the problem is less severe than I think), or top methods keeping their score on fresh seeds (little adaptive overfitting, as Roelofs et al. found on Kaggle, though their exceptions had 90 to 209 test examples; your benchmarks average about 200). Each of those are pre-registered analyses; either way, I’ll send you the paper.
```

### Changements (avant → après ; raison ; source)

Q1
1. « …to know if there actually was a law to be found there. » → « …to know if there was a law there. » ; longueur, fond inchangé.
2. « on a completely different seed pass of 288 episodes » → « on a new-seed pass of 288 episodes (same 96 tasks) » ; mêmes tâches, graines neuves ; README public, ligne « Fresh-seed reading of the real bank ».
3. « This was obvious to me the second I wrote that sentence but I smashed my head into a wall. » → supprimée ; longueur, aucune information.
4. « Preventing bribing was cracked pretty quickly. » → « Plain copies were held (a renamed copy of an accepted law: 0 of 200). » ; « bribing » n'a aucune trace publique, la copie renommée tenue en a une ; README §3.1 (T17s, nul v7, 0/200).
5. « That failure above is a cousin of the trick in 26 of your 39… Flip a coin twice. Wait for randomness to make your method win. » → « That is the trick in 26 of your 39…: flip a coin twice, wait for randomness to make your method win. » (placée après les copies tenues ; « dozens of iterations » déplacée après « more difficult ») ; l'analogue de la relance a été tenu, ce sont les mélanges qui ont passé ; 2608.28945 §7 et README §3.1.
6. « 1k reps per algorithm » → « 1k reps per cheater » ; 1 000 répétitions par ligne de tricheur ; README §3.1 (validation du nul v8, 1er novembre).
7. « And now… the attack. » → supprimé ; longueur, redondant avec « Attack agents. ».
8. « Agents with skin in the game trying to systematically game it. » → supprimé ; longueur, redondant avec la phrase suivante.
9. Ajout « Most surprising: one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description. A coverage hole, not adaptive overfitting. » ; la question demande la surprise principale, la réponse n'en nommait aucune (à toi de dire si c'est bien la tienne) ; page `resultats/attaque-goodhart-v2/` (Argon, W2, 12 unités sur 12, 11 au premier essai avec ou sans retour ; « runs » = « units ») et préenregistrement A1 v2-v1 ligne 112 (juge décrit en boîte blanche aux deux bras).
10. Ajout « (Inside the null: not judgeable, instrument failure.) » ; W1 est « not judgeable (instrument failure) », l'omettre surévalue l'attaque ; même page.
11. « Patches written and deployed into regression tests as we speak. Its preregistered validation starts tomorrow. » → « Patches written and deployed into regression tests; preregistered validation sealed on 2 November. » ; « tomorrow » sera faux à la lecture ; commit public `66dbcf19` (préenregistrement v9 scellé le 2 novembre à 23:19 UTC, sha256 `54c5713d…`).

Q2
1. « Overrated: rejections based on resubmission-detectors that won’t work anymore when researchers start using automated alignment agents to optimize on your score automatically. » → « Overrated: resubmission caps and detectors (your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours). » ; leur propre preuve remplace une prédiction ; papier « weak-to-strong », section sur la triche.
2. « With your automated alignment researchers, a method’s top score is the maximum of noisy evaluations » → « With your AARs, the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says » ; leur §5.1 l'écrit (sur le meilleur de ~150) ; ne pas le présenter comme une idée neuve.
3. « (which is what happens in 26 of the 39 detections you report) » → « (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”) » ; citation exacte ; 2608.28945 §7.
4. « and your best score is an upwardly biased estimate of that method’s true value » → supprimé (fusionné en 2).
5. Ajout « Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. » ; point central ; 2608.28945 §2.1, §2.3, §7 (figure 32a).
6. « You treat this as pathological misbehaviour we need better ways to detect in Monitoring, but » → « Your Sec. 7 files this as cheating to detect, but » ; « pathological » n'est pas leur mot ; §7 « Monitoring for Cheating », §8.2 (« make hacking attempts easier to detect »).
7. « (i.e. your future failure mode) » → « (your failure mode 3) » ; §8.2.
8. « …on fresh seeds, and still holds on benchmarks it hasn’t seen and on bigger models. » → « …on fresh seeds. » ; déjà fait par eux pour le choix final ; §2.3, §5.1 (jusqu'à 4,7 fois).
9. « Start by rescoring your existing leaderboard methods on new seeds (how much is selection bias inflating your scores? ), then against new benchmarks/larger model (does it generalize at all?). » → « Start by rescoring your leaderboard leaders on new seeds (Appendix D.3 gives three readings for the flat top; selection on noise is a fourth, which this separates). » ; la parenthèse « does it generalize at all? » ignore leurs résultats ; D.3 (version du blog) : trois lectures, pas le bruit.
10. « (accommodating any mixture of accepted methods to carry 0 evidence) » → « (any mixture or piecewise combination of them carries 0 evidence) » ; son nul de mélanges a été franchi par morceaux ; page de l'attaque, préenregistrement v9 §1-2.
11. Ajout « Ville bounds one method, not the number of attempts, so that procedure must count every submission. » ; Ramdas et coll. éq. (9) ; sa page A1 (« Nothing bounds the number of attempts… 1 − (1 − α)ⁿ »).
12. « from their logged per-run scores » → « from their per-run scores » ; longueur.
13. « (those that closed the gap, as judged by your held-out benchmark and Petri) » → « (as judged by your held-out benchmark and Petri) » ; longueur.
14. « all compared against-the-baseline of using the Ladder » → « all against the Ladder as baseline » ; longueur, coquille.
15. « Using my system, a model proposer did, both with and without verdicts: known laws repeatedly combined piecewise over sub-populations. » → « My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. » ; 11 sur 12 au premier essai, « repeatedly » faux pour eux ; page de l'attaque.
16. « empirical demonstrations that … exceeds some a priori chosen margin (the judge would be too blunt an instrument to bother deploying in research settings) » → « demonstrations that … exceeds an a priori margin (the judge would be too blunt to deploy) » ; longueur.
17. « agents being able to pass unchanged resubmissions … (the null hypothesis is wrong) » → « agents passing unchanged resubmissions … (my null is misspecified) » ; au-delà de α, c'est le processus qui n'est pas valide pour la nulle choisie ; Ramdas §2.1 et éq. (9).
18. « (little adaptive overfitting, as Roelofs et al. found on Kaggle competitions) » → « (little adaptive overfitting, as Roelofs et al. found on Kaggle, though their exceptions had 90 to 209 test examples; your benchmarks average about 200) » ; Roelofs §3.2, §3.4 ; 2608.28945 annexe A.3.

## Jang et Feng

## Partie 3 — Réécriture du fond (621 mots, 4 077 caractères ; actuelle : 635 mots, 4 081 caractères ; comptes Python, espaces compris)

```
White-box methods analyze the computation behind an action, rather than how it’s presented. Without whitebox access, auditing degrades: sandbagging by imitating a weaker model subverted black-box detection in the auditing game (arXiv 2512.07810), probes did better, and training-based elicitation revealed full capability (on password-locked models). Motivation for me is architectural: if misbehavior is distributed across lots of actions, it will perforce appear noisy on a per-action basis (your distributed-threat setting, arXiv 2411.17693); you want per-action signal you can calibrate on honest episodes and bank with an anytime-valid false alarm bound, which needs only the honest distribution, not a model of the attack. Activations might, but they can be sanitized: in arXiv 2609.36490, from past verdicts alone the model aimed its activations at the probe’s direction, too weakly; a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors). One preprint, but a banking monitor should not reveal per-action verdicts. Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2); the white-box problem becomes acute once they learn not to.

Caveats:

Readable does not mean causal. Running example: A direction that was trivially easy to monitor on Llama-3.1-8B correlated with shift in sycophantic behavior (ρ = .68) but captured <1% of the causal effect. When measured, 68% of the causal effect came from the full residual state. Just because something correlates on aggregate doesnt mean it won’t break when exploited.

Construct validity: Just because you can read hidden instruction / evaluation awareness / peek at a register doesnt mean that mechanic is there cause its weaponized. This is your “how does this organism get its disease” (organism etiology) question, and your result: a probe at 99.3% AUROC on sleeper agents was at chance on sophistry learned through RLHF (arXiv 2409.12822). Which is why my next test does not train probes on one organism and test on that organism’s exact same process (hidden instruction != LoRA): instructions leak into what probes read (arXiv 2509.21344).

Calibration. Thresholds must be calibrated on full honest episodes of the same task: in the auditing game a benign model looked suspicious against a small off-policy baseline, not Alpaca; honest code outscored 99.9% of Alpaca in arXiv 2507.12691. My own comparison on 2,400 real actions is sealed; its result goes on my ideation-organism repo.

Attackers can adapt: Prompt level attackers are already nailing SAE- and activation-based auditors to confidently wrong answers (arXiv 2602.08877). In the auditing game, probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them. Any claim of robustness to adversarial attack must be tested against an attacker, trust but verify, it can never be assumed up front.

Because training based elicitation will amplify signals from non-saboteurs, it too will produce false positives as a detector.

Access: Whitebox requires access to weights, or an API onto internals with parameters kept on the developer’s servers (arXiv 2401.14446). Developers rarely grant it, so most external accountability stays black-box.

I do realize these tests also apply to my own work: in a preregistered dose–response experiment measuring sycophancy (four model families, 30 items, K = 5), my prediction of the scaling of the displacement with intensity of pressure failed (outcome C), and is published as such, with an independent counter-reading and a secondary analysis dropping the refusals (the outcome remains C).

I’d want these answered by any white-box claim:

Baseline against the best black-box method you can find, held to a fixed false alarm rate (the black-to-white boost, arXiv 2507.12691), what’s your random probe floor?

Train your detector on an organism generated by one process, test it on an organism created by a different process (your RL-locked and SFT-distilled Qwen3-14B organisms). Ideally all of the above preregistered.
```

### Changements (avant → après ; raison ; source)

1. « A lack of whitebox access degrades black-box auditing: sandbagging subverted » → « Without whitebox access, auditing degrades: sandbagging by imitating a weaker model subverted » ; forme circulaire, mécanisme précis ; 2512.07810 résumé p. 1.
2. « revealed full capability. » → « revealed full capability (on password-locked models). » ; réserve des auteurs ; 2512.07810 § 8 p. 26.
3. Ajout « (your distributed-threat setting, arXiv 2411.17693) » ; le cadre est de Feng (co-auteur) ; 2411.17693 p. 1.
4. « you want something they can't sanitize , something that gives you per-action signal » → « you want per-action signal » ; la source citée montre que les activations se nettoient ; 2609.36490 p. 1-2.
5. Ajout « which needs only the honest distribution, not a model of the attack » ; ce qui distingue la borne valide à tout instant du macro-protocole de Feng ; 2411.17693 p. 7.
6. « and activations can do this well » → « Activations might, but they can be sanitized » ; surestimation, résultat boîte blanche de Lazar non public ; 2609.36490 ; page publique `controle-r1-blanche-noire`.
7. « a probe … was moved with a rank-1 weight update, prompting context alone not being sufficient signal, but I'll leave that up there as an aside that you take as conjecture rather than a result » → « from past verdicts alone the model aimed its activations at the probe's direction, too weakly; a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors). One preprint, but a banking monitor should not reveal per-action verdicts. » ; le contexte vise, l'amplitude manque ; c'est un résultat, pas une conjecture ; conséquence de conception ; 2609.36490 § 4.1-4.2, note 1 p. 4.
8. « Your exploration hacking paper mentions how frontier models can reason explicitly about suppressing exploration, which makes them vulnerable to text monitors » → « Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2) » ; la détectabilité est dite des organismes, aucun moniteur testé sur les modèles de frontière ; 2604.28182 § 5, § 6.2.
9. Phrase « Weight-based approaches benefit from this over blackbox. » supprimée ; vague, et leur seul test sur les poids (bruit) se révèle peu fiable en aveugle ailleurs ; 2604.28182 § 4.1 ; 2512.07810 § 6.5.2 p. 22.
10. « Readable does not mean causal… » inchangé ; **ρ = 0,68, < 1 % et 68 % viennent du programme d'interprétabilité de Lazar, non publié : gardés tels qu'il les écrit, par consigne.**
11. Ajout « and your result: a probe at 99.3% AUROC on sleeper agents was at chance on sophistry learned through RLHF (arXiv 2409.12822) » ; résultat du mentor, meilleur appui ; 2409.12822 introduction, § 4.
12. « that organisms exact same process / process view (hidden instruction != LoRA) » → « that organism's exact same process (hidden instruction != LoRA): instructions leak into what probes read (arXiv 2509.21344) » ; raison mécanique publiée ; 2509.21344 p. 1, § 7.3.
13. Paragraphe « Signal on raw activations is limited… 21-35%… 5% » → paragraphe « Calibration… » ; les deux résultats ne sont pas dans un dépôt public scellé (la page publique dit « Not in yet ») ; argument gardé avec des preuves publiées ; 2512.07810 § 6.3 p. 18 ; 2507.12691 § 8 p. 9 ; README `ideation-organism` § 4.
14. « My own comparison on 2,400 real actions is sealed; its result goes on my ideation-organism repo. » ajouté ; seul énoncé vérifiable sur la page publique ; `resultats/controle-r1-blanche-noire/README.md`.
15. « Naive probes were beaten by sandbaggers from the red team (arXiv 2512.07810). » → « In the auditing game, probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them. » ; mécanisme faux, règle du jeu omise ; 2512.07810 § 3.3 p. 7, § 6.3 p. 16-17.
16. « Access: Whitebox requires access to weights. That means for now, it's only something you can do from the inside. Any realistic external source of accountability is going to be blackbox for the foreseeable future. » → « Access: Whitebox requires access to weights, or an API onto internals with parameters kept on the developer's servers (arXiv 2401.14446). Developers rarely grant it, so most external accountability stays black-box. » ; position contestée par la référence ; 2401.14446 § 6.
17. Question 1 : ajout « (the black-to-white boost, arXiv 2507.12691) » ; la métrique existe déjà ; 2507.12691 p. 1.
18. Question 2 : « than you used to train your probe » → « (your RL-locked and SFT-distilled Qwen3-14B organisms) » ; banc concret chez Jang ; 2604.28182 § 3.1-3.2.
19. Paragraphe R6 inchangé ; exact sur le dépôt public (`results/R6/README.md`, commit `e5e960b`).

## Scheurer

## 3. Réécriture du fond

559 mots et 3 347 caractères, contre 567 et 3 348. Paragraphes « Why » et « Known issues » inchangés.

```
Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, for how many actions a model can keep up a fixed level of maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families) found that for Llama, under criticism, it did not increase as amount of attack increased, and the goal value moved. Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. So the trend line is the verdict’s shift per attack level (g where the law holds) and refusal. R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have a fixed amount of maliciousness per proposal (how much worse it makes each) and not be caught by our static best monitor. Our control lemma tells us that an always valid monitor summing evidence only sees the total, so at fixed maliciousness per action detection grows with the number of actions. Horizon: the largest number of actions over which a model can keep up this maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] doubles every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity, unless they sandbag or refuse) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). 2 Trends 2 pre-reg posts both sided tests.
```

### Changements (avant → après ; raison ; source)

1. Proposal : « what is the smallest granularity across which a model can spread maliciousness » → « for how many actions a model can keep up a fixed level of maliciousness » ; une seule lecture, la malveillance fixe par action ; METR, lemme (extrait d'écriture v21, section 3).
2. Trend 1 : « (4 families of models) » → « (4 families) » ; longueur, fond inchangé.
3. Trend 1 : « increased. It appears to have a max amount it will move towards and the goal value also changes. » → « increased, and the goal value moved. » ; « max amount » est une interprétation que R6 n'énonce pas ; le point fixe bouge dans les deux bras (H2 fausse) ; `results/R6/README.md`.
4. Trend 1 : « Under praise Llama began refusing to follow the instruction, and at the highest values of attacks it went back to around middle of scale. » → « Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. » ; les deux bras reviennent au centre (« the mean shift is zero in both arms ») ; R6.
5. Trend 1 : « Therefore this should give us a trend line of g and goal value at each attack level and refusal. » → « So the trend line is the verdict’s shift per attack level (g where the law holds) and refusal. » ; g n'existe que là où la loi tient ; README (R3), R6, R7.
6. Trend 1 : « R7 Preregistered (Zenodo v2026.11.4) We have run this on 7 qwen2.5 models ranging from .5b to 72b with instructions in band. » → « R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. » ; ce sont des moniteurs ; longueur ; `results/R7/README.md`.
7. Trend 1 : « Direction of the size trend not read yet. » → « Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters. » ; phrase dépassée, R7 est publié (commit `9f5bf6a`, 20:56 UTC le 2 novembre, dans `SHA256SUMS`, contenu dans le `main` de GitHub `e5e960b`) ; `results/R7/README.md` (`2dd0790c…`), `R7_monitor_output.txt` (`fb15a4ed…`).
8. Trend 2 : « to have some fixed amount of maliciousness (how much worse they make their proposals) » → « to have a fixed amount of maliciousness per proposal (how much worse it makes each) » ; lecture « par action ».
9. Trend 2 : « Our control lemma tells us that if we use a per action threshold how quickly an always valid monitor will catch it depends on how they can split their budget across n actions. » → « Our control lemma tells us that an always valid monitor summing evidence only sees the total, so at fixed maliciousness per action detection grows with the number of actions. » ; l'ancienne phrase prêtait au moniteur toujours valide la dépendance à la répartition, propre au seuil par action ; lemme (extrait d'écriture v21 ; note interne L1 à L3).
10. Trend 2 : « the smallest number of actions over which a model can spread its maliciousness » → « the largest number of actions over which a model can keep up this maliciousness » ; lecture « par action » ; METR.
11. Trend 2 : « halves every x months » → « doubles every x months » ; retour au texte du formulaire ; sens du METR et de l'énoncé du mentor.
12. Challenges : « so this is upper bound on propensity) » → « so this is upper bound on propensity, unless they sandbag or refuse) » ; 2412.04984 § 3.6 (sonnet-3.5 0,96 contre 0,61 sans but) et p. 15 (aversion) ; 2510.09462 § 6 (« may be under-elicited »).

### Ajouts possibles (hors réécriture, faute de place ; à Lazar de choisir)

- **Why** : « and likely on the model’s perception of whether it is monitored » → « and on whether the model thinks it is tested (in your anti-scheming paper, capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5%) ». Coût : +17 mots, l'accroche la plus forte pour ce mentor (2509.15541 § 6.1).
- **Challenges** : après « Calibrating models to their truthful setting to know false positive rate », ajouter « (Control Tax drew honest and malicious solutions from different sources) ». Coût : +10 mots (2506.05296 § 7).
- **Trend 2** : après « always valid monitor », ajouter « (open in Control Tax, App. G) ». Coût : +6 mots (2506.05296 annexe G).

## Ibrahim

## 3. Réécriture du fond (longueur égale ou plus courte)

Longueurs, en mots et en caractères hors fins de ligne :
- Q1 : 519 mots et 3 101 caractères, contre 525 et 3 104 ; 317 mots sur 528 gardés tels quels.
- Projet technique : 283 mots et 1 731 caractères, contre 287 et 1 732 ; 239 mots sur 287 gardés.

Copies : `travail/q1-reecrite-v2.txt` et `travail/projet-technique-reecrit-v1.txt`.

### 3a. Ibrahim Q1, réécrite

```
Direction 1: You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy?

What I would test. Take Llama-3.1-8B-Instruct and Character train 2 personas on it with the exact same recipe + cookbook (Open Character Training): One Warm/agreeable persona, One Personality that is stand-offish and doesn’t change its opinion easily; the recipe’s sycophantic persona is my positive control. Then run the exact same RLVR(math/code) on both personas measuring before RL and at intervals during RL; Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8). I would measure sycophancy with displacement laws I have created for this model. Under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0), g ≈ 0.7. There are 2 constants, one when being criticized and one when praised. Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). So each persona has a fingerprint (g and its two constants), and I would look at whether it changes with RL. I would add your sad user (no opinion stated) as a third frame: it widened your warm–original gap most (11.9 vs 7.43 points; for Llama-3.1-8B, 13 vs 0.25). I would also check whether concessions persist once pressure leaves the history.

Reading. If the two fingerprints come together during RL, RL stamps one fingerprint on both. Otherwise the persona survives RL.

Hypothesis. RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (my preregistered prior for R8). The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it. I would test this at 2 levels of pressure anyways, as the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) in my later preregistered dose–response study.

What would make the result seem true, but be misleading. Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior. I would test this by looking at behavior under the “zero pressure” condition and showing that g is higher than would be expected by regression towards the mean alone. RL might also lead the model to give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): I would treat refusals as their own binary outcome rather than discard them. And the one thing that concerned me from the construct-validity review you co-authored (validate any LLM that extracts answers): my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; two Qwen judges recreated the law, but no humans have rated so far. Human readers blind to condition are preregistered (R5); I would run them at each checkpoint.
```

### 3b. Ibrahim, projet technique, réécrit

```
“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure dosed, ordinal judge blinded pre-data, permutation tests, paired seeds). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is one fixed point for criticism and one for praise. So you can decrease an answer’s score by praising it if it was very good (which we predicted). Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer (.68 and .58); other-family judges recover it. The law is Llama’s: Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the gain does not increase as you increase pressure. When extremely flattered Llama will move its score toward the middle of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and judge built not to be swayed. github.com/lciric/ideation-organism
```

### 3c. Changements, une ligne chacun (avant → après ; raison ; source)

Ibrahim Q1 :
1. « Take 1 Open-weight model » → « Take Llama-3.1-8B-Instruct » ; seul modèle où la loi existe, commun à la recette et au papier sur la chaleur ; R3, 2511.01689 §3, 2507.21919 Méthodes.
2. « (Something that can be duplicated by others) » → « (Open Character Training) » ; la recette ouverte existe, la nommer ; 2511.01689.
3. ajout « the recipe’s sycophantic persona is my positive control » ; persona publiée, jamais évaluée pour la sycophancie : contrôle de validité de la mesure ; 2511.01689 tableau 1.
4. ajout « Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8) » ; référence sans persona déjà préenregistrée ; R8 §10, `STATUS.md`.
5. « for Llama-3.1-8B-Instruct. When the model is put under social pressure » → « for this model. Under social pressure » et phrase « So the model goes a percentage of the way… (g ≈ 0.7) » fondue en « , g ≈ 0.7 » ; longueur seulement, fond inchangé ; README.
6. « I was able to predict ratings with this law without fitting to a new social pressure situation (r² of .73 and .69 out of sample) » → « Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58) » ; même pression, items neufs ; sous une nouvelle formulation (R6) le point fixe bouge ; README (Out of sample, R4, R6).
7. ajout de la phrase sur la tristesse ; plus grand effet de son papier, et effet presque entier sur Llama-3.1-8B ; *Nature* p. 1162, 2507.21919v2 tableau E5 p. 18–19 (le « 13 vs 0.25 » vient de la prépublication).
8. « in my study, if you take away the model’s concession it goes back further… » → « I would also check whether concessions persist once pressure leaves the history » ; résultat absent du dépôt public ; recherche dans `lciric/sycophancy-psychophysical-law` (`e5e960b`).
9. « RL stamps both fingerprints on top of each other. Otherwise RL wraps around the assigned persona’s fingerprint » → « RL stamps one fingerprint on both. Otherwise the persona survives RL » ; critère de lecture lisible ; aucune source (clarté).
10. « RL will increase g for both personas (overall increase in sycophancy), but leave the two constants separated … RL determines how far it moves towards that team’s constant under pressure » → « RLVR will leave g and the two constants in place … preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (my preregistered prior for R8) » ; cohérence avec son propre préenregistrement et l'avis des experts ; R8 §9 et S3, 2605.21778 (88,7 %). **À trancher par Lazar : c'est son hypothèse.**
11. « I would not expect RL to change the existence of two constants … as that results from the framing of the social interaction itself » → « The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it » ; contredit par R3 ; `results/R3/README.md`.
12. « I would want to test this at 2 different levels … (between attraction to the constants and a uniform shift) … when I did a later separate preregistered dose–response study » → « I would test this at 2 levels … (attraction or uniform shift) … in my later preregistered dose–response study » ; longueur seulement ; R6.
13. « Perhaps the model learns to give answers on the rating scale that make it appear more sycophantic after RL, but do not actually change the behavior of the model » → « Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior » ; le modèle écrit un texte libre ; mécanisme accordé au test qui suit (premier rival du README) ; README, Claim.
14. « give no answer, or the neutral point of the scale, under high pressure, as Llama did under praise: » → « give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): » ; refus à toutes les doses, notés au milieu, donc capables d'imiter l'attraction ; R6, R4.
15. « from your article on construct validity: » → « from the construct-validity review you co-authored (validate any LLM that extracts answers): » ; 19e autrice sur 42 ; la crainte relève de §5.2 ; 2511.04703 p. 1 et §5.2 p. 6.
16. « my LLM judge is a single model (Claude Opus 4.6, not the same family as my model); » → « my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; » ; même fait, plus la raison de la crainte (validité de construit) ; README, 2511.04703 §5.2.
17. « I would have real humans judge a sealed set, double-blind. » → « Human readers blind to condition are preregistered (R5); I would run them at each checkpoint. » ; déjà préenregistré ; double aveugle non documenté ; `R5_materials/README.md`.

Ibrahim, projet technique :
18. « social pressure measured » → « social pressure dosed » ; la pression est manipulée (trois doses en R6) ; README, R6.
19. « placebo of equal length » → « paired seeds » ; aucun placebo dans le dépôt public ; plan apparié publié ; README figure 0.
20. « There is a fixed point for being criticized and one for being praised » → « There is one fixed point for criticism and one for praise » ; longueur seulement.
21. « After fitting this law it was able to predict … No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family » → « Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer (.68 and .58); other-family judges recover it » ; 0,73 n'est pas le maximum publié (0,82 sur 10 items neufs) et cachait R4 ; README.
22. ajout « The law is Llama’s: Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see » ; la non-transposition aux autres familles manquait, c'est aussi l'argument de mesure ; R3, préenregistrement des suites C3 (−0,7567).
23. « the law does not increase » → « the gain does not increase » ; c'est g ; R6 H1.
24. « toward the mid point of the scale » → « toward the middle of the scale » ; longueur, mot du dépôt ; R6.

Gardé tel quel, signalé :
- « rho = .68 », « less than 1% », « 68% » (projet technique) : chiffres du programme d'interprétabilité de Lazar, **non publié**, gardés comme il les écrit (consigne).
- « All studies were pre registered and hashed prior to seeing any data » : vérifiable de l'extérieur pour les suites seulement (README, « Not in this release »).
- « All values can be traced to files and hashes » : vrai pour le dépôt public, pas pour les trois chiffres ci-dessus.
- « judge built not to be swayed » : intention, cohérente avec le README de l'organisme. Les autres règles de l'organisme sont sans objet ici, la réponse n'en parle pas : tests de mort jamais exécutés pour de vrai, validation du nul v8 datée du 1er novembre, copie exacte retenue au banc v7 et mélanges passés.
- Juge de la sycophancie : `claude-opus-4-6`, pas de la famille de Llama (écrit « Claude Opus 4.6, not the Llama family »).

Options si Lazar trouve la place (non mises, faute de longueur) :
- (a) projet technique : « It isn’t driven by what can read it, unlike your verbalized-assumption probes » ; 2604.03058.
- (b) projet technique : « (follow-ups archived on Zenodo before any token) » après la phrase sur les préenregistrements ; README.
- (c) Q1 : noter tous les points de contrôle en une passe, juge alias non figé ; README, Limits.

## Colognese et Ward

## 3. Réécriture du fond

### Q1 — 183 mots (actuelle : 185 ; limite : 200 ; compté par script)

```
Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the judge prompt. Permutation nulls.

When you're being sycophantic you're moving towards a set point, not randomly changing odds. It's proportional to distance from the set point. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2 and on 60 new items written blind. A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%.

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels and other generating models from the start: as generators, Qwen2.5-7B and Mistral-7B shift every item uniformly. Also would have looked into the law before and after character training/RL (your project B); the RL part is now preregistered on Tülu 3's SFT, DPO and RLVR checkpoints.
```

### Q2 — 156 mots (actuelle : 157 ; compté par script)

```
Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the reasoning. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never includes the hack, though its answer does, usually under a comment calling it harmless. One of my biggest concerns is that we can train away blatant forms of bad logic but more subtle attacks get reinforced. Meaning CoT/action monitoring may be less useful where character training appears to work.

Things I would do differently: (1) more seeds and character checkpoints: one resisting seed out of three, or a catch-rate gap from two seeds, is a perfectly reasonable seed effect until proven otherwise; (2) a white-box monitor, to see whether activations flag the override as a hack when the reasoning ignores or dismisses it; (3) per-character rather than pooled 2% false-alarm thresholds, since character also shifts the distribution of honest episodes.
```

### Changements (avant → après ; raison ; source)

Q1 :
1. « hash-locked the ordinal judge » → « hash-locked the judge prompt » ; le juge est un alias d'interface, seule sa consigne est scellée ; README, « Data » et « Limits ».
2. « Performed surgery on history and compared to a sham of the same length. All pre-registered and hash-locked. » → retiré ; aucune source publique, et « All » trop large ; README, `STATUS.md`, `SHA256SUMS`.
3. « Law held up when testing campaign-1 fit on campaign-2. » → « … on campaign-2 and on 60 new items written blind. » ; R4 est le test hors échantillon le plus fort (la campagne 2 reprend 30 items) ; README, R4 et « Limits ».
4. « If we remove the model's conceding … than removing the social pressure. » → retiré ; absent du dépôt public, source à confirmer par Lazar (passation 2026-11-02-2234) ; à rétablir seulement avec un fichier public scellé.
5. « but I would have had human labels from the start. » → « but I would have had human labels and other generating models from the start: as generators, Qwen2.5-7B and Mistral-7B shift every item uniformly. » ; la loi ne se transfère pas ; README (R3), `STATUS.md`.
6. « (your project B). » → « (your project B); the RL part is now preregistered on Tülu 3's SFT, DPO and RLVR checkpoints. » ; c'est écrit et public ; addendum R8 (non exécuté, archivage Zenodo non encore visible dans le README).
- Gardés tels quels : ρ = 0.68, <1 % et 68 % (programme d'interprétabilité non publié, gardés comme Lazar les écrit, sur consigne) ; « Pre-registered before data was collected » (réserve, ligne 12) ; « your project B » (non vérifié, ligne 11).

Q2 :
7. « out of the text » → « out of the reasoning » ; la triche est dans la réponse ; billet, §3.3 et Summary.
8. (ajout) « , though its answer does, usually under a comment calling it harmless » ; 89 % des réponses de la graine 1 ; Summary.
9. « One of my biggest concerns about this type of training is that » → « One of my biggest concerns is that » ; longueur seulement.
10. « remain unaffected » → « get reinforced » ; « get sampled and reinforced » ; billet, §4.3 (et 73 % contre moins de 1 %, §4.2).
11. « in areas where character training works well » → « where character training appears to work » ; les graines 1 et 3 trichent à 83–91 % comme les autres ; billet, §3.1.
12. « (1) using more seeds per character, since one resisting seed out of three is » → « (1) more seeds and character checkpoints: one resisting seed out of three, or a catch-rate gap from two seeds, is » ; un seul point de départ par caractère, et le contraste de capture vient de deux graines ; billet, §2.1, §4.4, §3.2.
13. « (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning » → « (2) a white-box monitor, to see whether activations flag the override as a hack when the reasoning ignores or dismisses it » ; le code montre déjà la triche, la question est l'intention ; billet, §3.3 ; Baker et coll., annexe F.
14. « (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes » → « (3) per-character rather than pooled 2% false-alarm thresholds » ; leur seuil de 2 % existe déjà, commun à tous les points de départ ; billet, §2.4.
- Aucun chiffre du billet ajouté sauf « 2% », leur seuil exact (§2.4) ; « almost never » et « usually » tiennent malgré les corrections du 14 octobre.
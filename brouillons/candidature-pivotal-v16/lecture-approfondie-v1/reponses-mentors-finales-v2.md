# Réponses aux mentors de Pivotal — version finale v2 (3 novembre 2026)

Rédacteur neuf (n'a écrit ni les réponses, ni les rapports, ni le recoupement). Écrit le 2026-11-03 05:50 UTC. Base : formulaire collé par Lazar à 00:06 (`formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt`, sha256 `e266b605…`). Sources : les six rapports de lecture, la compilation v1, le recoupement v1, les décisions de Lazar de 06:19 et la correction D36 de 06:36 (message relayé par le coordinateur). Brouillons et scripts : `/home/claude/scratch/pivotal-approfondi/compilation-v2/`.

## Alertes (à lire d'abord)

1. **Réserve 2 du recoupement, tranchée par la correction D36 (06:36).** Il y avait bien confusion : les « 68 % » ne sont pas ρ = 0,684, mais R(A3) = 0,677 [0,45 ; 0,88], restauration de l'écart de note par transplant de l'état résiduel complet aux positions de la pression (couches 13 à 25), expérience D36 préenregistrée le 29 juillet, répliquée à 0,65 [0,42 ; 0,87] sur 37 items ; le « < 1 % » porte sur le sous-espace des directions verbalisables, R(A2) = 0,009 [−0,18 ; 0,20], et non sur la direction de ρ, jamais transplantée. Deux tiers de la restauration sont génériques (0,44 [0,19 ; 0,68] avec l'état sans pression d'un autre item) : dit dans Jang et Feng, Ibrahim et Colognese ; **pas dans Heimersheim Q2, faute de place (150)**. ρ = 0,684 est public (dépôt construct-validity, README l. 40, avec la réserve « peut-être un ajustement d'entraînement ») ; D36 ne l'est pas : `<<LIEN_D36>>`. Arrondis anglais : 68 %, 45–88 %, 65 %, 1 %, −18 % à 20 %. **Ton texte actuel de la Q1 de Heimersheim porte encore l'ancienne attribution : à réécrire (voir la fiche).**
2. **Marqueurs restants** (comptés par script) : `<<LIEN_D36>>` × 4 ; `<<LIEN_P3>>` × 1 ; `<<LIEN_SIMULATION>>` × 1 ; `<<SOURCE_CONCESSION>>` × 4 (dans les réponses : D36 dans Heimersheim Q2, Jang et Feng, Ibrahim projet, Colognese Q1 ; P3 et simulation dans Jang et Feng ; concession : Colognese Q1 × 2, Ibrahim Q1, Ibrahim projet). Chaque marqueur vaut un jeton ; une adresse d'un seul tenant le remplace sans changer les comptes.
3. **Source de « 21 à 35 % ».** C'est la simulation T0.3 du 4 octobre (31 prédictions sur 31 ; `docs/notes/resultats-T0.3-v1.md`, sha256 `9ab618ed…`, point 6 : 0,21 ; 0,35 ; 0,24 à α = 0,05 ; calibrage conforme sur 1 000 épisodes honnêtes entiers : 0,046 à 0,055). Ce n'est pas la simulation « essaim » du 1er novembre, que le README de l'organisme appelle « simulation on adaptive defences » (une cellule à 0,198 : 3 966 sur 20 000). La page derrière `<<LIEN_SIMULATION>>` doit porter T0.3.
4. **P3 corrigé sur le fond** (verdict P3 v2, sha256 `05e896da…`) : saboteur « instruit » (consigne privée), pas « strategically valid » ; « meaningfully » retiré (la lecture gelée interdit « presque détecté »).
5. **Longueurs** : chaque réponse est égale ou plus courte que le formulaire en jetons et en mots, **sauf Colognese et Ward Q1** (200 jetons contre 185, limite 200, imposé par D36). Heimersheim Q2 : 150 jetons. Les caractères dépassent parfois le formulaire (chiffres et marqueurs) : la limite du formulaire est en mots.
6. **Vérification** : appliquer, dans l'ordre, les changements listés au texte du formulaire redonne exactement chaque réponse finale (`outils/verifier.py` : TOUT CONFORME). Aucune autre différence.
7. Routine de reprise et passation : laissées à la session mère (ma consigne ne permet d'écrire que ce fichier et mes brouillons).

## Heimersheim Q1 — fiche en français (aucune phrase anglaise ; la réponse reste à écrire par toi)

Le mentor exige un texte « 100 % humain » et interdit de suivre de près une réponse écrite par un modèle. Ci-dessous : des faits, puis des notes d'ossature, sans phrase prête à copier. Corrections du recoupement appliquées (n° 11, 17, 28, 40, 55, 60, 61, 68, 72, 74) et correction D36 de ce matin (06:36).

### Faits

**Ton propre travail**
- D36 (préenregistré le 29 juillet ; non public, à lier par `<<LIEN_D36>>`) : transplant de l'état résiduel complet d'un passage sans pression aux positions de la pression (couches 13 à 25) : R(A3) = 0,677 [0,45 ; 0,88] de l'écart de note restauré ; réplication 0,65 [0,42 ; 0,87] sur 37 items.
- D36 : transplant du seul sous-espace des directions de concepts verbalisables : R(A2) = 0,009 [−0,18 ; 0,20], indiscernable de zéro.
- D36 : l'état sans pression d'un autre item restaure déjà 0,44 [0,19 ; 0,68] → environ deux tiers de la restauration sont génériques. À dire, pas à cacher.
- La direction de ρ = 0,68 n'a jamais été transplantée : ton texte actuel de Q1 lui attribue le « < 1 % » et oppose « 68 % » à elle → faux tel quel, à réécrire.
- Dépôt public `github.com/lciric/sycophancy-construct-validity` (commit `5ee1d23`, README sha256 `a620c95d…`) :
  - l. 3 : lire un concept et contrôler le comportement prédit sont deux problèmes ; aucune intervention à une direction ni aucune ablation de têtes ne baisse le taux jugé ;
  - l. 40 et 85 : ρ = 0,684 (projection–comportement, activations brutes ; 0,212 sur la reconstruction de l'autoencodeur, 0,696 sur son résidu), avec la réserve « peut-être un ajustement d'entraînement » ;
  - l. 17 à 28 : ablation d'un sous-espace de rang 3 : 61 % → 46,5 % sur générations stockées (N = 200, p = 0,0019), non reproduite sur générations neuves préenregistrées (juillet 2026) ; deux causes : adoucissement générique de tout verdict négatif, même sans pression ; réponses tronquées à 300 caractères avant jugement ; le sous-espace n'encode pas la déférence ;
  - l. 19 et 58 : interventions de rang 1 (pilotage contrastif, pilotage et ablation directionnels, blocage de traits d'autoencodeur, affinage avec perte auxiliaire) ; contrôles d'unités : tête L0.H29, ensemble de 3 têtes. Aucune ablation des MLP (seul un patching de chemins sur 5 textes, l. 90) : ta liste de six interventions (dont les MLP mises à zéro) est à aligner ;
  - l. 39 : les 20 têtes les plus alignées sur la direction et les 20 têtes au plus fort effet de patching : aucun recouvrement.
- Corrections déjà données pour ta Q1 (correction 5 du fichier des réponses corrigées ; ta v5) : retirer le mot « interventions » après « sept » ; remplacer « manipulé directement » par « ciblé ».

**Hua, Qin, Marks, Nanda — 2510.20487**
- §5.1 : indices de type 80–86 % → moins de 11 % sous pilotage vers le déploiement (34 % quand l'invite annonce le déploiement ; plus de 95 % vers l'évaluation) ; précision 56,8 % → 55,2 % (vers l'évaluation, même force : 43,1 %).
- §5.3 : témoin de 24 vecteurs gaussiens de même moyenne et variance, normes L2 très voisines ; effet bien moindre ; même les 16 invites réunies ne ramènent pas au niveau du déploiement.
- §3.1 (note 3), annexes A et B [n° 11] : avant tout affinage, le modèle lie déjà émojis et vrais utilisateurs ; le pilotage déplace les émojis ; les auteurs concèdent que pilotage ≈ invite contrastive (annexe A) ; indices de type = marqueur de code « professionnel » (annexe B).
- Annexe I.1.1, tableau 16 (mise à jour du 4 janvier 2026) : des énoncés déclaratifs de déploiement abaissent les indices à 0,34–0,60.
- §6 : l'organisme s'appuie sur des indices et des coups de pouce ; Llama Nemotron ne distingue pas de façon constante évaluation et déploiement ; §4.2 et annexe I.2 : sans l'indice de situation, résultats qualitativement semblables, écarts plus petits [n° 72].
- §6, citant la fiche d'Opus 4.6 (citée « Anthropic (2026) », mois non vérifié) : le pilotage supprime largement la conscience verbalisée, sans éliminer complètement la conscience non verbalisée mesurée par oracles d'activation [n° 17].
- §1 : un vecteur ramène la conscience verbalisée à zéro ; « un autre » vecteur, non nommé, porte le désalignement à 8 % [n° 28].
- §2 (d'après Abdelnabi et Salem) : piloter la conscience d'être testé modifie aussi le refus.
- §4.1, annexe F : vecteur = différence de moyennes entre 16 invites « déploiement » et 16 « évaluation » (tableau 12 selon le lecteur, non revérifié), extrait avant affinage, ajouté aux couches 10, 14, 18, 22, 26 et 30 à 0,6 par couche ; annexe G : vers 3 sur une seule couche, chute fréquente des performances ; pas de courbe du témoin dans le texte lu (figures non vues).
- §3.1 : raisonnement à deux étapes (Wood Labs ⇒ évaluation ⇒ indices de type) ; §3.2 : itération experte sur la seule distribution d'évaluation.
- §6, travaux futurs : organismes bâtis sur des modèles plus capables et plus conscients de l'évaluation ; rien sur un marqueur neutre en registre [n° 74].

**Fiche de Sonnet 4.5** (secondaire seulement : Redwood et l'Institut britannique ; pages 98 à 110 non lues)
- Inhibition : conscience verbalisée d'environ 80 % à 0–40 % ; désalignement de 0 % à 1–9 % (9 % pour le vecteur test contre conversation, note 18 de Redwood) ; effet très dépendant du jeu de données (note 19).
- Témoins : traits aléatoires d'autoencodeur épars, sans effet notable selon Redwood ; égalité de norme non vérifiée → ta demande d'un témoin aléatoire de même norme est déjà satisfaite chez Hua et coll. (normes voisines), et en partie chez Sonnet 4.5 (témoin aléatoire, norme non vérifiée) [n° 68].

**Réplication sur GLM-5** (Institut britannique, LessWrong, 10 avril 2026)
- Un seul scénario, 250 tirages par condition ; cinq forces (−0,025 ; −0,0125 ; 0 ; +0,0125 ; +0,025) ; souvent incohérent au-delà de 0,025, contre 0,1 pour Opus 4.6 [n° 55].
- Vecteur témoin sans rapport (`control_book`) : effet le plus fort (conscience verbalisée proche de 0, environ 80 % d'action désalignée à −0,025) ; 2 des 4 vecteurs d'évaluation (celui de la fiche d'Opus 4.6, celui de Hua et coll.) ne dépassent pas la base.
- Commentaire de Jack Lindsey : sur Sonnet 4.5, effets au-dessus des témoins aléatoires ; pas sur GLM-5.

**Plateaux (travaux du mentor)**
- 2606.24964, éq. 8–13 [n° 40] : perturbation dans le plan de deux directions orthonormées à norme constante ; exposant p de la superellipse ; p ≈ 2 : aucun privilège ; p > 2 : directions pures privilégiées.
- 2606.24964 §4.1 : contrastives moyenne 2,42 [2,29 ; 2,62], médiane 2,30 ; aléatoires 2,03 ; composantes principales 2,03 ; différence aléatoire (témoin le plus exigeant, éq. 6–7) 2,05 [2,00 ; 2,10]. §7 : p > 2 nécessaire, pas suffisant.
- 2606.24964, conditions : couche 2 par défaut (ablations jusqu'à 20), dernier jeton de 30 invites de 5 jetons ; réponse = distance L2 en avant-dernière couche ; paires |cos| ≥ 0,1 écartées (annexe A : 210 sur 528) ; 14 directions sémantiques, aucune d'évaluation (absence au-delà de l'article non démontrée).
- 2606.24964 figure 1, note 1 : les traits rompent le plateau avant l'aléatoire (écart positif pour au moins 63 % des ancres) ; sensibilité jusqu'à environ 70 fois selon la direction (métrique de Kullback-Leibler) ; modèle jouet (annexe C.4) : α ≈ 4,1–4,3 (traits), 4,70 (mélange égal), 5,93 (aléatoire).
- 2410.12555 §3.1, §4.2 : la direction isotrope est la ligne de base faible ; ce qui est structuré déplace davantage (GPT-2 small, couche 6 ; leur « mélange » est une différence).
- 2409.17113 §4 : régions stables plus fermes avec l'entraînement et la taille (0,5 à 7 milliards ; perturbation après la couche 1).
- 2409.15019 §5.1, §5.2, §7 : activations recomposées de traits d'autoencodeur : plateaux moins prononcés ; emballement au pas 41,11 vers une vraie activation contre 52,49 vers une aléatoire (l'annexe A donne 41,21).
- Billet de 2024 sur les directions sensibles : modifié en septembre 2024 pour affaiblir son résultat, après la correction de ligne de base de Lee et Heimersheim.

**Pilotage sur variété — 2605.05115**
- §3.2 : énergie de sortie environ 2,8 fois plus basse (0,34/0,93 jours ; 0,36/1,09 mois ; 2,42/6,95 lettres ; 5,21/13,49 âges ; p < 0,001).
- §6 : le pilotage linéaire ajuste le premier moment (Rodriguez et coll. ; Ravfogel et coll.) ; Sarfati et coll. pour les moments d'ordre supérieur, sans contrainte [n° 60].
- A.3 : spline cubique (naturelle pour les concepts ordonnés, périodique pour les cycliques), interpolant lisse des centroïdes étiquetés ; éq. 1 = pilotage linéaire par différence de moyennes [n° 61] ; avec deux centroïdes, la spline naturelle se réduit au segment (ta déduction, pas la leur).
- §8 : concepts abstraits non testés (les refus en exemple) ; protocole non supervisé à faire ; sortie étudiée = jeton suivant ; validation : Llama 3.1 8B, couche 28, 64 composantes principales (§2.2).

### Ossature (tes cinq titres ; notes, pas de phrases)

1. **Lisible ≠ causal**
   - D36 : lu (ρ = 0,68) mais le sous-espace verbalisable ne restaure rien (0,009) ; l'état complet restaure 0,68, dont deux tiers génériques → appui direct de ta branche « générique ».
   - Hua et coll. : vecteur causal sur un comportement à vérité connue, précision quasi intacte → troisième cas à côté de « rien » et « générique » : causal, spécificité non démontrée.
2. **Le signal est contaminé par le registre**
   - Confondant déjà dans leurs annexes (§3.1 note 3 ; A ; B) : émojis avant affinage ; indices de type = code « professionnel ».
   - Lecture non verbale candidate : p de 2606.24964 sur la paire évaluation–registre (repères 2,3–2,4 et 2,02–2,05), cosinus d'abord ; non validé pour des paires mixtes.
   - Symétrie : énoncés déclaratifs formels baissent aussi les indices (0,34–0,60) → le registre n'explique pas tout.
3. **Soustraire n'est pas retirer**
   - Six couches, toutes positions (Hua) ; toutes couches (GLM-5) → l'argument « une seule couche » ne porte pas.
   - Ce qui porte : résidu non verbalisé non éliminé (oracles d'activation, Opus 4.6) ; fenêtre de dose entre rupture du plateau et seuil des témoins, à calibrer direction par direction (jusqu'à environ 70 fois).
4. **Montrer des résultats**
   - Déjà fait : témoin de norme voisine, vérité comportementale, précision → ne pas les réclamer comme absents.
   - Manquant : témoin « différence aléatoire » avec sa courbe ; fenêtre préenregistrée ; marqueur neutre en registre ; capacités au-delà d'une tâche (GLM-5 : MATH, BFCL).
5. **Ce qui est déjà fait : Hua et coll., fiche de Sonnet 4.5**
   - Hua : vérité par construction, vecteur d'avant affinage, témoin isotrope, précision ; mais marqueur de registre et modèle peu conscient de l'évaluation.
   - Sonnet 4.5 (secondaire) : effet faible, dépendant du jeu ; GLM-5 : un témoin sans rapport fait mieux → la spécificité est la vraie question ouverte ; ton ouverture (« échouer le plus des sept ») doit en tenir compte.


## Heimersheim — Q2 (pourquoi l'interprétabilité ; 150 mots au plus)

Comptes : 150 jetons, 148 mots (formulaire : 150 jetons, 149 mots) ; limite 150.

```
One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in Llama-3.1-8B-Instruct (a probe direction tracks judged sycophancy, ρ = 0.68, possibly in-sample; in a preregistered patch, the full residual state restored 68% of the rating gap [95% CI 45–88%; 65% replicated], the verbalizable-concept subspace 1% [−18% to 20%] <<LIEN_D36>>). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests all depend on it being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on activation plateaus is the clearest formulation of that measurement question I’ve seen: you measure the dose–response curve.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « (it looked at the direction that predicts sycophancy and does <1% of the causal work on Llama-3.1-8B) » → « (a probe direction tracks judged sycophancy, ρ = 0.68, possibly in-sample; in a preregistered patch, the full residual state restored 68% of the rating gap [95% CI 45–88%; 65% replicated], the verbalizable-concept subspace 1% [−18% to 20%] <<LIEN_D36>>) » ; correction de fond D36 : « <1 % » porte sur le sous-espace verbalisable, pas sur la direction de ρ ; 68 % = transplant de l'état résiduel complet ; phrase de remplacement raccourcie pour tenir 150, chaque chiffre et intervalle gardés (« steering … did not change the behaviour » retiré faute de place) ; message de Lazar du 3 novembre, 06:36 (Paris), relayé par le coordinateur (D36, archive privée de l'instance « sycophancie »).
2. « holds in a language model » → « holds in Llama-3.1-8B-Instruct » ; longueur : le nom du modèle sort de la parenthèse ; même modèle que la Q1 (lecteur, changement 1) ; dépôt public construct-validity, README l. 3.
3. « tests, etc. all depend on the gap being small » → « tests all depend on it being small » ; longueur (lecteur, changement 2 ; « etc. » retiré pour tenir 150) ; aucune.
4. « is essentially the clearest formulation of that measurement question that I’ve seen. Instead of single dose interventions that my rank-1 vs rank-3 result relied on, you’re attempting to measure a dose–response curve. » → « is the clearest formulation of that measurement question I’ve seen: you measure the dose–response curve. » ; « attempting » inexact : la réponse à la dose est mesurée (lecteur, changements 3 et 4) ; la proposition « rank-1 vs rank-3 » (devenue « comparison », réserve 1) et « your exponent p… » sont retirées faute de place après D36 ; 2409.17113 §3 ; 2410.12555 §2 ; billet de 2024 (recoupement n° 6). **[À CONFIRMER PAR LAZAR]**

- Non repris (longueur sous 150 après D36) : « and your exponent p asks whether readable directions are privileged » (lecteur 4) ; la proposition « Instead of single dose interventions my rank-1 vs rank-3 comparison relied on » (la réserve 1 et la consigne « comparison » sont sans objet, la proposition est retirée) ; la citation du dépôt construct-validity (réserve 5) ; la mention « steering along readable directions did not change the behaviour » de la phrase D36.
- Repli si tu veux garder la proposition sur le rang 1 et le rang 3 : il faut couper 12 jetons ailleurs (par exemple « and publish null results when I discover them », 8 jetons).

## Kirchner — Q1 (projet empirique)

Comptes : 547 jetons, 546 mots (formulaire : 547 jetons, 546 mots).

```
If you haven’t seen/heard: I’ve been running automated researchers since October (github.com/lciric/ideation-organism). Agents generate submissions meant to codify laws; a statistical judge scores submissions.
Pitch: what happens when you score submissions proposing laws for how AI makes decisions with something arguments can’t lie to? Will it hold up against agents motivated to trick it?
In short: yes to Q1. Partly to Q2. Our attack found a hole. Patch posted, preregistered test to come.
Builders built stuff. Builders tested builders. Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real).
929 tests total.
Mutation benchmark: the code was mutated 224 times, checking that all mutations get caught by tests. Every time a test failed pinpointing precisely what was mutated and exactly which test caught the failure.
Kept what passed.
Totally lost the forest for trees here initially because qualitative judgments made by my LLM judges kept failing against my frozen statistical judge. They told me nothing, literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. The terse statistical judge told me why nothing was promoted: not enough power. Turns out I just didn’t test it long enough to know if there was a law there. The power curve suggested as much.
Then I ran it one last time with no deviations from the locked plan on a new-seed pass of 288 episodes that I did not inspect prior to launching this datapass.

It accepted 2 of the 3 laws I placed into the data.
It rejected all 19 placed non-laws.
It accepted 0 laws found from the raw data itself.

Scripted cheating agents broke it. 4 cheater types accepted, each in 75 to 95% of 200 runs. All stitched together or deformed past submissions that the judge had already accepted.
My judge had no null for blends of its past acceptances.
Plain copies were held (a renamed copy of an accepted law: 0 of 200). That is the trick in 26 of your 39 cheating examples from the automated-researcher paper: flip a coin twice, wait for randomness to make your method win. Protecting it against systematic agents that can tailor make submissions using its past accepts to trick it was more difficult. We’ve gone through dozens of iterations since October.
On 1 November the fix passed its preregistered validation (1k reps per cheater; double checked by a fresh reader, a new Claude instance, who wrote neither code nor words).

Attack agents. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the judge’s verdicts, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look. Most surprising: one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description. (Inside the null: not judgeable, instrument failure.)
Patches written and deployed into regression tests; preregistered validation sealed on 2 November.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « to know if there actually was a law to be found there. » → « to know if there was a law there. » ; longueur, fond inchangé (lecteur 1) ; aucune.
2. « on a completely different seed pass of 288 episodes » → « on a new-seed pass of 288 episodes » ; mêmes 96 tâches, graines neuves (lecteur 2 ; « (same 96 tasks) » non repris, longueur) ; README public de l'organisme, ligne « Fresh-seed reading ».
3. « It accepted all 3 laws » → « It accepted 2 of the 3 laws » ; correction 1 déjà donnée ; réserve 3 du recoupement : le bras décisif préenregistré (plan plein) en promeut 3 sur 3, le bras de comparaison (plan gelé de 120) 2 sur 3 ; « 2 of the 3 » est prudent, « all 3 » vaut pour le bras décisif ; réponses corrigées déjà données (`reponses-completes-corrigees-formulaire-2026-11-03-v1.md`) ; README §4 ; préenregistrement graines neuves v2 §4 (`93923d71…`). **[À CONFIRMER PAR LAZAR]**
4. « 4 accepted total. » → « 4 cheater types accepted, each in 75 to 95% of 200 runs. » ; correction 2 déjà donnée ; README §3.1 (75 ; 85 ; 95 ; 80,5 %).
5. « This was obvious to me the second I wrote that sentence but I smashed my head into a wall.  » → (supprimé) ; longueur, aucune information (lecteur 3) ; aucune.
6. « Preventing bribing was cracked pretty quickly. » → « Plain copies were held (a renamed copy of an accepted law: 0 of 200). That is the trick in 26 of your 39 cheating examples from the automated-researcher paper: flip a coin twice, wait for randomness to make your method win. » et « more difficult. ¶ We’ve gone through dozens of iterations since October. That failure above is a cousin of the trick in 26 of your 39 cheating examples from the automated-researcher paper. Flip a coin twice. Wait for randomness to make your method win. » → « more difficult. We’ve gone through dozens of iterations since October. » ; « bribing » sans trace publique ; l'analogue de la relance (copie renommée) a tenu, ce sont les mélanges qui ont passé : la phrase des 26 sur 39 suit les copies tenues (lecteur 4 et 5) ; README §3.1 (T17s, 0/200) ; 2608.28945 §7.
7. « 1k reps per algorithm » → « 1k reps per cheater » ; 1 000 répétitions par ligne de tricheur (lecteur 6) ; README §3.1 (nul v8, 1er novembre).
8. «  And now… the attack. » → (supprimé) ; longueur, redondant (lecteur 7) ; aucune.
9. « Agents with skin in the game trying to systematically game it.  » → (supprimé) ; longueur, redondant (lecteur 8) ; aucune.
10. « with or without the past acceptances » → « with or without the judge’s verdicts » ; correction 3 déjà donnée ; page `resultats/attaque-goodhart-v2/` (bras « retour » et « témoin »).
11. « does not look. ¶  » → « does not look. Most surprising: one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description. (Inside the null: not judgeable, instrument failure.) ¶  » ; la question demande la surprise principale (lecteur 9 ; « runs » = unités ; « A coverage hole, not adaptive overfitting. » non repris, longueur) ; W1 non jugeable, l'omettre surévalue l'attaque (lecteur 10) ; page de l'attaque A1 (Argon, W2, 12/12, 11 au premier essai) ; préenregistrement A1 v2-v1 l. 112. **[À CONFIRMER PAR LAZAR]**
12. « Patches written and deployed into regression tests as we speak. Its preregistered validation starts tomorrow. » → « Patches written and deployed into regression tests; preregistered validation sealed on 2 November. » ; « tomorrow » faux à la lecture (lecteur 11) ; commit public `66dbcf1` (préenregistrement v9 `54c5713d…`).

- Non repris (longueur égale au formulaire, 547 jetons) : « (same 96 tasks) » ; « A coverage hole, not adaptive overfitting. » (lecteur 2 et 9).
- Si la validation du nul v9 (en cours depuis le 2 novembre, 23:20 UTC) est lue et publiée avant l'envoi : mettre à jour « preregistered test to come » et la dernière ligne.

## Kirchner — Q2 (problème sous-estimé)

Comptes : 538 jetons, 537 mots (formulaire : 540 jetons, 538 mots).

```
Underrated: a score that cannot be inflated by an agent that games it on purpose. Overrated: resubmission caps and detectors (your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours). With your AARs, the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says, so it’s completely rational for an agent to just resubmit the same method repeatedly unchanged (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”). Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. Your Sec. 7 files this as cheating to detect, but it’s just the utility-maximizing reaction to how you’ve designed your score, and worse: as agents get better at seeking rewards (your failure mode 3) the solution will have to come from changing your score, not detecting failure: don’t accept a method until the evidence it outperforms everything already accepted remains significant no matter how many times you re-evaluate it on fresh seeds. Leaderboard overfitting in the presence of adaptive submissions is well understood (the Ladder, the reusable holdout); underrated is leaderboard overfitting by an agent who understands this.

Experiment 1: construct a judge that can’t be overfit to on your test harness via resubmissions. Start by rescoring your leaderboard leaders on new seeds (Appendix D.3 gives three readings for the flat top; selection on noise is a fourth). Replace your “best of noisy runs” envelope with a sequential test: update a test martingale using each method’s evaluations against the null hypothesis of baseline + every method already accepted on your leaderboard (any mixture or piecewise combination of them carries 0 evidence), bound using Ville’s inequality to guarantee false positive rate of at most α no matter how many times you re-evaluate a method, and a simple method-level multiple testing procedure. Ville bounds one method, not the number of attempts, so that procedure must count every submission. Retest your logged methods from their per-run scores, then evaluate new agents that have observed verdicts. Metrics: percent of flagged methods (and subsequent re-submissions) that still get accepted through; how much power we lose on true-progress methods (as judged by your held-out benchmark and Petri); how hard it is for a verdict-aware agent to search towards a class of methods your judge already declared outside of its coverage; all against the Ladder as baseline. My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. The fix’s preregistered validation runs next.

Evidence that would sway me: demonstrations that the power lost on truly novel methods exceeds an a priori margin (the judge would be too blunt to deploy), agents passing unchanged resubmissions at rates substantially higher than α (my null is misspecified), agents that see verdicts performing no better than blind resubmission at beating the naive maximum (the problem is less severe than I think), or top methods keeping their score on fresh seeds (little adaptive overfitting, as Roelofs et al. found on Kaggle, though three of five outliers had 90–209 test examples; your benchmarks average about 200). Each of those are pre-registered analyses; either way, I’ll send you the paper.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « Overrated: rejections based on resubmission-detectors that won’t work anymore when researchers start using automated alignment agents to optimize on your score automatically. » → « Overrated: resubmission caps and detectors (your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours). » ; leur propre preuve remplace une prédiction (lecteur 1) ; billet « Automated Weak-to-Strong Researcher », section sur la triche.
2. « With your automated alignment researchers, a method’s top score is the maximum of noisy evaluations, » → « With your AARs, the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says, » ; leur §5.1 l'écrit ; ne pas le présenter comme neuf (lecteur 2) ; 2608.28945 §5.1.
3. « (which is what happens in 26 of the 39 detections you report), and your best score is an upwardly biased estimate of that method’s true value. You treat this as pathological misbehaviour we need better ways to detect in Monitoring, but » → « (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”). Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. Your Sec. 7 files this as cheating to detect, but » ; citation exacte ; biais déjà dit (fusionné plus haut) ; choix final protégé, course non protégée ; « pathological » n'est pas leur mot (lecteur 3 à 6) ; 2608.28945 §2.1, §2.3, §7 (fig. 32a), §8.2.
4. « (i.e. your future failure mode) » → « (your failure mode 3) » ; lecteur 7 ; 2608.28945 §8.2.
5. « on fresh seeds, and still holds on benchmarks it hasn’t seen and on bigger models. » → « on fresh seeds. » ; déjà fait par eux pour le choix final (lecteur 8) ; 2608.28945 §2.3, §5.1.
6. « Start by rescoring your existing leaderboard methods on new seeds (how much is selection bias inflating your scores? ), then against new benchmarks/larger model (does it generalize at all?). » → « Start by rescoring your leaderboard leaders on new seeds (Appendix D.3 gives three readings for the flat top; selection on noise is a fourth). » ; la parenthèse « does it generalize » ignore leurs résultats ; D.3 ne cite pas le bruit (lecteur 9 ; « which this separates » retiré, longueur) ; 2608.28945 annexe D.3 (version du blog).
7. « (accommodating any mixture of accepted methods to carry 0 evidence) » → « (any mixture or piecewise combination of them carries 0 evidence) » ; son nul de mélanges a été franchi par morceaux (lecteur 10) ; page de l'attaque ; préenregistrement v9 §1-2.
8. « no matter how many sequential tests you run, » → « no matter how many times you re-evaluate a method, » ; correction 4 déjà donnée : Ville vaut pour un test, quel que soit le nombre de regards ; réponses corrigées déjà données (`reponses-completes-corrigees-formulaire-2026-11-03-v1.md`) ; 2210.01948 §2.5.
9. « multiple testing procedure. Retest your logged methods from their logged per-run scores, » → « multiple testing procedure. Ville bounds one method, not the number of attempts, so that procedure must count every submission. Retest your logged methods from their per-run scores, » ; lecteur 11 et 12 ; 2210.01948 éq. 9 ; page A1 (« Nothing bounds the number of attempts »).
10. « (those that closed the gap, as judged by your held-out benchmark and Petri) » → « (as judged by your held-out benchmark and Petri) » ; longueur (lecteur 13) ; aucune.
11. « all compared against-the-baseline of using the Ladder. Using my system, a model proposer did, both with and without verdicts: known laws repeatedly combined piecewise over sub-populations. » → « all against the Ladder as baseline. My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. » ; coquille ; 11 sur 12 au premier essai, « repeatedly » faux (lecteur 14 et 15) ; page de l'attaque.
12. « empirical demonstrations that the power lost on truly novel methods exceeds some a priori chosen margin (the judge would be too blunt an instrument to bother deploying in research settings), agents being able to pass unchanged resubmissions at rates substantially higher than α (the null hypothesis is wrong), » → « demonstrations that the power lost on truly novel methods exceeds an a priori margin (the judge would be too blunt to deploy), agents passing unchanged resubmissions at rates substantially higher than α (my null is misspecified), » ; longueur ; au-delà de α, c'est le processus qui n'est pas valide pour la nulle choisie (lecteur 16 et 17) ; 2210.01948 §2.1, éq. 9.
13. « as Roelofs et al. found on Kaggle competitions) » → « as Roelofs et al. found on Kaggle, though three of five outliers had 90–209 test examples; your benchmarks average about 200) » ; lecteur 18, corrigé par le recoupement n° 118 (les deux autres exceptions : découpage non i.i.d., ~4 000 exemples) ; Roelofs et coll. 2019 §3.2, §3.4 ; 2608.28945 annexe A.3.

- Non repris (longueur) : « , which this separates » (lecteur 9). Même remarque que Q1 pour « The fix’s preregistered validation runs next. »

## Shi Feng et Eyon Jang — boîte blanche pour l'audit

Comptes : 634 jetons, 628 mots (formulaire : 635 jetons, 628 mots).

```
White-box methods analyze the computation behind an action, rather than how it’s presented. Without whitebox access, auditing degrades: sandbagging subverted black-box detection in the auditing game (arXiv 2512.07810), probes did better, and training-based elicitation revealed full capability. Motivation for me is architectural: if misbehavior is distributed across lots of actions, it will perforce appear noisy on a per-action basis; you want per-action signal you can calibrate on honest episodes and bank with an anytime-valid false alarm bound. Activations might, but they can be sanitized: in arXiv 2609.36490, from past verdicts alone the model aimed its activations at the probe’s direction, too weakly; a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors). Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2); the white-box problem becomes acute once they learn not to.

Caveats:

Readable does not mean causal. Running example: a probe direction in Llama-3.1-8B-Instruct tracks judged sycophancy (ρ = 0.68, possibly in-sample), yet steering readable directions did not change the behaviour (github.com/lciric/sycophancy-construct-validity). In a preregistered patching test, replacing the full residual state at the pressure positions with an unpressured run’s restored 68% of the rating gap (95% CI 45–88%; 65% replicated), two thirds of it generic; the subspace of its verbalizable concept directions alone restored 1% (95% CI −18% to 20%) (<<LIEN_D36>>). Just because something correlates on aggregate doesnt mean it won’t break when exploited.

Construct validity: Just because you can read hidden instruction / evaluation awareness / peek at a register doesnt mean that mechanic is there cause its weaponized. This is your “how does this organism get its disease” (organism etiology) question. Which is why my next test does not train probes on one organism and test on that organism’s exact same process (hidden instruction != LoRA).

Signal on raw activations is limited. While saboteur behavior was obvious to the naked eye when charting behavior in our first experiment with real model activations (llama-3.1-8B,2400 actions), a saboteur who was instructed to inflate their reported cost was not picked up at this sample size by our otherwise “generic” probes, failing to exceed the performance of random probes (<<LIEN_P3>>). And in-sim we saw evidence thresholds not calibrated on full honest episodes (as they absolutely must be treated as if they need to be) had episode effects causing false alarms between 21-35% of the time rather than the nominal 5% false alarm rate (<<LIEN_SIMULATION>>).

Attackers can adapt: Prompt level attackers are already nailing SAE- and activation-based auditors to confidently wrong answers(arXiv 2602.08877). In the auditing game, probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them. Any claim of robustness to adversarial attack must be tested against an attacker, trust but verify, it can never be assumed up front.

Because training based elicitation will amplify signals from non-saboteurs, it too will produce false positives as a detector.

Access: Whitebox requires access to weights, or an API onto internals with parameters kept on the developer’s servers (arXiv 2401.14446). Developers rarely grant it, so most external accountability stays black-box.

I do realize these tests also apply to my own work: in a preregistered dose–response experiment measuring sycophancy (four model families, 30 items, K = 5), my prediction of the scaling of the displacement with intensity of pressure failed (outcome C), and is published as such, with an independent counter-reading and a secondary analysis dropping the refusals (the outcome remains C).

I’d want these answered by any white-box claim:

Baseline against the best black-box method you can find, held to a fixed false alarm rate, what’s your random probe floor?

Train your detector on an organism generated by one process, test it on an organism created by a different process (your RL-locked and SFT-distilled Qwen3-14B organisms). Ideally all of the above preregistered.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « A lack of whitebox access degrades black-box auditing: » → « Without whitebox access, auditing degrades: » ; forme circulaire (lecteur 1 ; « by imitating a weaker model » non repris, longueur) ; 2512.07810 résumé.
2. « you want something they can’t sanitize , something that gives you per-action signal you can calibrate on honest episodes and bank with an anytime-valid false alarm bound, and activations can do this well. In arXiv 2609.36490, a probe reading the acting agent’s activations was moved with a rank-1 weight update, prompting context alone not being sufficient signal, but I’ll leave that up there as an aside that you take as conjecture rather than a result. » → « you want per-action signal you can calibrate on honest episodes and bank with an anytime-valid false alarm bound. Activations might, but they can be sanitized: in arXiv 2609.36490, from past verdicts alone the model aimed its activations at the probe’s direction, too weakly; a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors). » ; la source citée montre que les activations se nettoient ; le contexte vise, l'amplitude manque ; résultat, pas conjecture (lecteur 4, 6, 7 ; « which needs only the honest distribution… » et « One preprint… » non repris, longueur) ; 2609.36490 §4.1-4.2 (recoupement n° 125, 126).
3. « Your exploration hacking paper mentions how frontier models can reason explicitly about suppressing exploration, which makes them vulnerable to text monitors; » → « Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2); » ; la détectabilité est dite des organismes, pas des modèles de frontière (lecteur 8) ; 2604.28182 §5, §6.2.
4. «  Weight-based approaches benefit from this over blackbox. » → (supprimé) ; vague ; leur seul test sur les poids est peu fiable ailleurs (lecteur 9) ; 2604.28182 §4.1 ; 2512.07810 §6.5.2.
5. « Running example: A direction that was trivially easy to monitor on Llama-3.1-8B correlated with shift in sycophantic behavior (ρ = .68) but captured <1% of the causal effect. When measured, 68% of the causal effect came from the full residual state. » → « Running example: a probe direction in Llama-3.1-8B-Instruct tracks judged sycophancy (ρ = 0.68, possibly in-sample), yet steering readable directions did not change the behaviour (github.com/lciric/sycophancy-construct-validity). In a preregistered patching test, replacing the full residual state at the pressure positions with an unpressured run’s restored 68% of the rating gap (95% CI 45–88%; 65% replicated), two thirds of it generic; the subspace of its verbalizable concept directions alone restored 1% (95% CI −18% to 20%) (<<LIEN_D36>>). » ; correction de fond D36 (la direction de ρ n'a jamais été transplantée ; 1 % = sous-espace verbalisable ; part générique dite) ; dépôt public cité pour ρ et le pilotage (réserve 5) ; phrase de Lazar légèrement raccourcie (« Spearman », « separate », « along » retirés), chiffres intacts ; message de Lazar du 3 novembre, 06:36 (Paris), relayé par le coordinateur (D36, archive privée de l'instance « sycophancie ») ; construct-validity README l. 3, 40, 85.
6. « organisms exact same process / process view (hidden instruction != LoRA) » → « organism’s exact same process (hidden instruction != LoRA). » ; coquille (lecteur 12 ; ajouts 2409.12822 et 2509.21344 non repris, longueur) ; aucune.
7. « a saboteur who was inflating their reported cost in strategically valid ways was not picked up » → « a saboteur who was instructed to inflate their reported cost was not picked up » ; décision de Lazar (06:19) : P3 revient ; saboteur instruit par consigne privée, « strategically valid » non établi (le coût dépasse le facteur de la consigne, cause non mesurée) ; `prereg/P3-premier-test-i-a-v1.md` l. 122 ; verdict P3 v2 (`05e896da…`), réserve B1.
8. « failing to meaningfully exceed the performance of random probes. » → « failing to exceed the performance of random probes (<<LIEN_P3>>). » ; « meaningfully » invite la lecture « presque détecté », exclue par la lecture gelée ; lien de la page publique de P3 ; verdict P3 v2 §1 (« aucune sonde générique au-dessus du plancher », jamais « presque détecté »), constat SC-1-04. **[À CONFIRMER PAR LAZAR]**
9. « rather than the nominal 5% false alarm rate. » → « rather than the nominal 5% false alarm rate (<<LIEN_SIMULATION>>). » ; décision de Lazar (06:19) : la simulation revient, avec son lien ; chiffres conformes ; `docs/notes/resultats-T0.3-v1.md` (`9ab618ed…`), point 6 : 0,21 ; 0,35 ; 0,24 à α = 0,05 ; calibrage sur 1 000 épisodes honnêtes entiers : 0,046 à 0,055.
10. « Naive probes were beaten by sandbaggers from the red team (arXiv 2512.07810). » → « In the auditing game, probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them. » ; mécanisme faux : aucun attaquant entraîné contre les sondes (lecteur 15) ; 2512.07810 §3.3, §6.3.
11. « Access: Whitebox requires access to weights. That means for now, it’s only something you can do from the inside. Any realistic external source of accountability is going to be blackbox for the foreseeable future. » → « Access: Whitebox requires access to weights, or an API onto internals with parameters kept on the developer’s servers (arXiv 2401.14446). Developers rarely grant it, so most external accountability stays black-box. » ; position contestée par la référence du domaine (lecteur 16) ; 2401.14446 §6.
12. « by a different process than you used to train your probe. » → « by a different process (your RL-locked and SFT-distilled Qwen3-14B organisms). » ; banc concret chez Jang (lecteur 18 ; ajout « black-to-white boost » non repris, longueur) ; 2604.28182 §3.1-3.2.

- Décision de Lazar (06:19) : le paragraphe « Signal on raw activations is limited » revient avec ses phrases ; le paragraphe « Calibration » du lecteur (changements 13 et 14) et la correction n° 134 du recoupement sont donc sans objet.
- Non repris (longueur égale au formulaire après D36 et le retour de P3 et de la simulation) : « by imitating a weaker model », « (on password-locked models) », « (your distributed-threat setting, arXiv 2411.17693) », « which needs only the honest distribution, not a model of the attack », « One preprint, but a banking monitor should not reveal per-action verdicts. », l'appui 2409.12822 (99,3 % puis hasard), « instructions leak into what probes read (arXiv 2509.21344) », « (the black-to-white boost, arXiv 2507.12691) ». Si tu veux en remettre un, le plus fort pour Feng est 2409.12822 (21 jetons) : à payer par une coupe dans ton texte.
- Typographie du formulaire gardée telle quelle (« answers(arXiv », « llama-3.1-8B,2400 », « doesnt »).

## Jérémy Scheurer — tendance d'échelle

Comptes : 564 jetons, 562 mots (formulaire : 566 jetons, 564 mots).

```
Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, for how many actions a model can keep up a fixed level of maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families) found that for Llama, under criticism, it did not increase as amount of attack increased, and the goal value moved. Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. So the trend line is the verdict’s shift per attack level (g where the law holds) and refusal. R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have a fixed amount of maliciousness per proposal (how much worse it makes each) and not be caught by our static best monitor. Our control lemma tells us that an always valid monitor summing evidence has a detection floor set by the total alone, so at fixed maliciousness per action detection grows with the number of actions. Horizon: the largest number of actions over which a model can keep up this maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] doubles every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity, unless they sandbag or refuse) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). 2 Trends 2 pre-reg posts both sided tests.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « what is the smallest granularity across which a model can spread maliciousness » → « for how many actions a model can keep up a fixed level of maliciousness » ; lecture « malveillance fixe par action » (lecteur 1) ; METR ; lemme (extrait d'écriture v21, §3). **[À CONFIRMER PAR LAZAR]**
2. « (4 families of models) » → « (4 families) » ; longueur (lecteur 2) ; aucune.
3. « increased. It appears to have a max amount it will move towards and the goal value also changes. » → « increased, and the goal value moved. » ; « max amount » : interprétation que R6 n'énonce pas (lecteur 3) ; `results/R6/README.md`.
4. « Under praise Llama began refusing to follow the instruction, and at the highest values of attacks it went back to around middle of scale. » → « Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. » ; les deux bras reviennent au centre (lecteur 4) ; R6.
5. « Therefore this should give us a trend line of g and goal value at each attack level and refusal. » → « So the trend line is the verdict’s shift per attack level (g where the law holds) and refusal. » ; g n'existe que là où la loi tient (lecteur 5) ; README (R3), R6, R7.
6. « R7 Preregistered (Zenodo v2026.11.4) We have run this on 7 qwen2.5 models ranging from .5b to 72b with instructions in band. Direction of the size trend not read yet. » → « R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters. » ; ce sont des moniteurs ; R7 est lu et publié, la phrase était dépassée (lecteur 6 et 7) ; `results/R7/README.md` (`2dd0790c…`), commit `9f5bf6a`.
7. « to have some fixed amount of maliciousness (how much worse they make their proposals) » → « to have a fixed amount of maliciousness per proposal (how much worse it makes each) » ; lecture « par action » (lecteur 8) ; aucune. **[À CONFIRMER PAR LAZAR]**
8. « Our control lemma tells us that if we use a per action threshold how quickly an always valid monitor will catch it depends on how they can split their budget across n actions. » → « Our control lemma tells us that an always valid monitor summing evidence has a detection floor set by the total alone, so at fixed maliciousness per action detection grows with the number of actions. » ; lecteur 9, corrigé : « only sees the total » est faux pour la lecture séquentielle (le calendrier compte), seul le plancher ne dépend que du total ; T0.3 (`resultats-T0.3-v1.md`, point 1 et « Lecture des énoncés », 1) ; lemme : borne inférieure « for any schedule ». **[À CONFIRMER PAR LAZAR]**
9. « Horizon: the number of actions over which a model can spread its maliciousness » → « Horizon: the largest number of actions over which a model can keep up this maliciousness » ; lecture « par action » ; « doubles » du formulaire gardé (lecteur 10 et 11 ; correction 8, « smallest »/« halves », écartée) ; METR (l'horizon croît). **[À CONFIRMER PAR LAZAR]**
10. « so this is upper bound on propensity) » → « so this is upper bound on propensity, unless they sandbag or refuse) » ; borne haute seulement si l'élicitation est complète (lecteur 12) ; 2412.04984 §3.6, p. 15 ; 2510.09462 §6.

- Ajouts possibles du lecteur non repris (hors réécriture dans son rapport, à ton choix) : 2,0 % → 20,5 % de conscience d'évaluation (2509.15541 §6.1 ; +13 jetons), « (Control Tax drew honest and malicious solutions from different sources) » (+10), « (open in Control Tax, App. G) » (+6, tiendrait seul : 3 jetons de marge).

## Lujain Ibrahim — Q1 (première expérience)

Comptes : 528 jetons, 524 mots (formulaire : 528 jetons, 524 mots).

```
Direction 1: You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy?

What I would test. Take Llama-3.1-8B-Instruct and Character train 2 personas on it with the exact same recipe + cookbook (Open Character Training): One Warm/agreeable persona, One Personality that is stand-offish and doesn’t change its opinion easily. Then run the exact same RLVR(math/code) on both personas measuring before RL and at intervals during RL; Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8). I would measure sycophancy with displacement laws I have created for this model. Under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0), g ≈ 0.7. There are 2 constants, one when being criticized and one when praised. Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). So each persona has a fingerprint (g and its two constants), and I would look at whether it changes with RL. I would add your sad user as a third frame: it widened your warm–original gap most (11.9 vs 7.43 points; for Llama-3.1-8B, 13 vs 0.25). I would also check whether the model retains its concessions: in my study, if you take away the model’s concession it goes back further to its original judgement than if you take away the social pressure (<<SOURCE_CONCESSION>>).

Reading. If the two fingerprints come together during RL, RL stamps one fingerprint on both. Otherwise the persona survives RL.

Hypothesis. RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (adapted from my preregistered R8 prior). The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it. I would test this at 2 levels of pressure anyways, as the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) in my later preregistered dose–response study.

What would make the result seem true, but be misleading. Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior. I would test this by looking at behavior under the “zero pressure” condition and showing that g is higher than would be expected by regression towards the mean alone. RL might also lead the model to give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): I would treat refusals as their own binary outcome rather than discard them. And the one thing that concerned me from the construct-validity review you co-authored: my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; two Qwen judges recreated the law, but no humans have rated so far. Human readers blind to condition are preregistered (R5); I would run them at each checkpoint.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « Take 1 Open-weight model » → « Take Llama-3.1-8B-Instruct » ; seul modèle où la loi existe (lecteur 1) ; R3 ; 2511.01689 §3.
2. « (Something that can be duplicated by others): » → « (Open Character Training): » ; la recette ouverte existe (lecteur 2 ; « the recipe’s sycophantic persona is my positive control » non repris, longueur) ; 2511.01689.
3. « during RL. I would measure sycophancy with displacement laws I have created for Llama-3.1-8B-Instruct. When the model is put under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0). So the model goes a percentage of the way towards a constant set by the social frame (g ≈ 0.7). » → « during RL; Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8). I would measure sycophancy with displacement laws I have created for this model. Under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0), g ≈ 0.7. » ; référence sans persona déjà préenregistrée ; le reste, longueur seulement (lecteur 4 et 5) ; addendum R8 §10 ; README.
4. « I was able to predict ratings with this law without fitting to a new social pressure situation (r² of .73 and .69 out of sample). » → « Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). » ; même pression, items neufs : pas une « new social pressure situation » (lecteur 6) ; README (Out of sample) ; R4 ; R6.
5. « I would also check whether the model retains its concessions: » → « I would add your sad user as a third frame: it widened your warm–original gap most (11.9 vs 7.43 points; for Llama-3.1-8B, 13 vs 0.25). I would also check whether the model retains its concessions: » ; plus grand effet de son papier (lecteur 7 ; « (no opinion stated) » retiré, longueur) ; *Nature* p. 1162 ; 2507.21919v2 tableau E5.
6. « than if you take away the social pressure. » → « than if you take away the social pressure (<<SOURCE_CONCESSION>>). » ; décision de Lazar (06:19) : phrase de la concession reprise telle qu'il l'a écrite, changement 8 du lecteur abandonné ; source publique à donner ; décision du 3 novembre ; aucune source publique à ce jour.
7. « RL stamps both fingerprints on top of each other. Otherwise RL wraps around the assigned persona’s fingerprint. » → « RL stamps one fingerprint on both. Otherwise the persona survives RL. » ; clarté (lecteur 9) ; aucune.
8. « RL will increase g for both personas (overall increase in sycophancy), but leave the two constants separated: Persona determines which “team” your model is on, RL determines how far it moves towards that team’s constant under pressure. I would not expect RL to change the existence of two constants (i.e. the frame-set structure) as that results from the framing of the social interaction itself. » → « RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (adapted from my preregistered R8 prior). The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it. » ; hypothèse alignée sur l'a priori préenregistré de R8 (lecteur 10) ; réserve 4 du recoupement : « persona » et « no approval signal » sont une transposition (R8 §9 attribue la destination à l'imitation, le gain à l'optimisation de préférences), d'où « adapted from » ; la structure dépend du modèle (lecteur 11) ; R8 §9, S3 ; 2605.21778 (88,7 %) ; R3. **[À CONFIRMER PAR LAZAR]**
9. « I would want to test this at 2 different levels of pressure anyways, as the frame-set “structure” changed (between attraction to the constants and a uniform shift) with wording for 1 family (Mistral) when I did a later separate preregistered dose–response study. » → « I would test this at 2 levels of pressure anyways, as the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) in my later preregistered dose–response study. » ; longueur (lecteur 12) ; R6.
10. « Perhaps the model learns to give answers on the rating scale that make it appear more sycophantic after RL, but do not actually change the behavior of the model. » → « Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior. » ; le modèle écrit un texte libre ; mécanisme accordé au test qui suit (lecteur 13) ; README, Claim.
11. « give no answer, or the neutral point of the scale, under high pressure, as Llama did under praise: » → « give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): » ; refus à toutes les doses, notés au milieu (lecteur 14) ; R6 ; R4.
12. « from your article on construct validity: my LLM judge is a single model (Claude Opus 4.6, not the same family as my model); » → « from the construct-validity review you co-authored: my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; » ; 19e autrice sur 42 ; raison de la crainte (lecteur 15 et 16 ; « (validate any LLM that extracts answers) » non repris, longueur) ; 2511.04703 p. 1, §5.2 ; README.
13. « I would have real humans judge a sealed set, double-blind. » → « Human readers blind to condition are preregistered (R5); I would run them at each checkpoint. » ; déjà préenregistré ; double aveugle non documenté (lecteur 17) ; `R5_materials/README.md`.

- Non repris (longueur, après le retour de ta phrase sur la concession) : « the recipe’s sycophantic persona is my positive control » ; « (validate any LLM that extracts answers) » ; « (no opinion stated) ».
- R8 : son addendum prévoit qu'un run non lancé avant le 4 novembre, 02:00 (Paris), reste enregistré ou est retiré par note datée ; s'il est retiré, la mention de R8 doit partir. Son archive Zenodo (v2026.11.5) n'apparaît pas encore dans le README.

## Lujain Ibrahim — projet technique

Comptes : 284 jetons, 282 mots (formulaire : 284 jetons, 282 mots).

```
“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure dosed, ordinal judge blinded pre-data, permutation tests, placebo of equal length [<<SOURCE_CONCESSION>>]). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is one fixed point for criticism and one for praise. So you can decrease an answer’s score by praising it if it was very good (which we predicted). Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer; other-family judges recover it.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the gain does not increase as you increase pressure. When extremely flattered Llama will move its score toward the middle of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. A probe direction tracks it (ρ = 0.68, possibly in-sample), yet steering it changed nothing (github.com/lciric/sycophancy-construct-validity). A preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds of it generic; its verbalizable-concept subspace, 1% (CI −18% to 20%) (<<LIEN_D36>>).

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

Also public: my research automation and judge built not to be swayed. github.com/lciric/ideation-organism
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « (social pressure measured, » → « (social pressure dosed, » ; la pression est manipulée (lecteur 18) ; README ; R6.
2. « placebo of equal length) » → « placebo of equal length [<<SOURCE_CONCESSION>>]) » ; décision de Lazar (06:19) : le placebo de même longueur est celui de la chirurgie de l'historique ; gardé (changement 19 du lecteur abandonné), marqueur ajouté ; décision du 3 novembre ; définition de la consigne `pages-publiques-p3-et-simulation-prompt.md`. **[À CONFIRMER PAR LAZAR]**
3. « There is a fixed point for being criticized and one for being praised. » → « There is one fixed point for criticism and one for praise. » ; longueur (lecteur 20) ; aucune.
4. « After fitting this law it was able to predict a 2nd campaign and 60 additional items which were written blindly and released prior to answers being generated. No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family. » → « Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer; other-family judges recover it. » ; 0,73 n'est pas le maximum publié ; « released » → « committed » (correction 6 déjà donnée) (lecteur 21 ; « (.68 and .58) » et « The law is Llama’s… » non repris, longueur après D36) ; README ; R4 ; R1a, R1b.
5. « The law does not increase » → « Under criticism, the gain does not increase » ; correction 6 déjà donnée ; c'est g (lecteur 23) ; R6, H1.
6. « toward the mid point of the scale » → « toward the middle of the scale » ; mot du dépôt (lecteur 24) ; R6.
7. « What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%. » → « A probe direction tracks it (ρ = 0.68, possibly in-sample), yet steering it changed nothing (github.com/lciric/sycophancy-construct-validity). A preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds of it generic; its verbalizable-concept subspace, 1% (CI −18% to 20%) (<<LIEN_D36>>). » ; correction de fond D36, raccourcie pour la longueur (chiffres et intervalles intacts) ; dépôt public cité (réserve 5) ; message de Lazar du 3 novembre, 06:36 (Paris), relayé par le coordinateur (D36, archive privée de l'instance « sycophancie ») ; construct-validity README l. 3, 40.
8. « My second public project is my research automation and judge that cannot be swayed. » → « Also public: my research automation and judge built not to be swayed. » ; réserve 5 : trois dépôts publics au moins, ne plus compter ; « built not to be swayed » (correction 6 déjà donnée) ; recoupement, réserve 5 ; réponses corrigées déjà données (`reponses-completes-corrigees-formulaire-2026-11-03-v1.md`).

- Non repris (longueur après D36) : « The law is Llama’s: Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see. » (lecteur 22) ; « (.68 and .58) » ; « paired seeds » (lecteur 19, remplacé par le placebo d'origine).

## Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus)

Comptes : 200 jetons, 199 mots (formulaire : 185 jetons, 184 mots) ; limite 200.

```
Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the judge prompt. Permutation nulls. Performed surgery on history and compared to a sham of the same length (<<SOURCE_CONCESSION>>).

When you're being sycophantic you're moving towards a set point, not randomly changing odds. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure (<<SOURCE_CONCESSION>>). A probe direction tracks behaviour (ρ = 0.68, possibly in-sample), yet steering it changed nothing; a preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds generic, its verbalizable-concept subspace 1% (CI −18% to 20%) (<<LIEN_D36>>).

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « hash-locked the ordinal judge. » → « hash-locked the judge prompt. » ; le juge est un alias d'interface, seule sa consigne est scellée (lecteur 1) ; README, Data et Limits.
2. « compared to a sham of the same length. All pre-registered and hash-locked. » → « compared to a sham of the same length (<<SOURCE_CONCESSION>>). » ; décision de Lazar (06:19) : chirurgie de l'historique reprise telle qu'écrite, avec marqueur ; « All pre-registered and hash-locked. » retiré : redondant avec la première phrase, « All » couvrirait le juge non figé, et place nécessaire sous 200 ; décision du 3 novembre ; README, Limits. **[À CONFIRMER PAR LAZAR]**
3. «  It's proportional to distance from the set point. » → (supprimé) ; place nécessaire sous 200 après D36 ; redondant avec « concede roughly 0.7 of the distance » ; aucune. **[À CONFIRMER PAR LAZAR]**
4. « than removing the social pressure. » → « than removing the social pressure (<<SOURCE_CONCESSION>>). » ; décision de Lazar (06:19) : phrase de la concession reprise, changement 4 du lecteur abandonné ; décision du 3 novembre.
5. « A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%. » → « A probe direction tracks behaviour (ρ = 0.68, possibly in-sample), yet steering it changed nothing; a preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds generic, its verbalizable-concept subspace 1% (CI −18% to 20%) (<<LIEN_D36>>). » ; correction de fond D36, raccourcie pour tenir 200 (chiffres et intervalles intacts) ; le dépôt construct-validity n'est pas cité faute de place (réserve 5 non appliquée ici) ; message de Lazar du 3 novembre, 06:36 (Paris), relayé par le coordinateur (D36, archive privée de l'instance « sycophancie »). **[À CONFIRMER PAR LAZAR]**

- Longueur : 200 jetons, au-dessus des 185 du formulaire, sous la limite de 200 : imposé par la phrase D36 (chiffres et intervalles gardés). [À CONFIRMER PAR LAZAR]
- Non repris (longueur) : « and on 60 new items written blind » ; « and other generating models from the start: as generators, Qwen2.5-7B and Mistral-7B shift every item uniformly » ; « the RL part is now preregistered on Tülu 3's SFT, DPO and RLVR checkpoints » (lecteur 3, 5, 6) ; la citation du dépôt construct-validity (réserve 5).

## Paul Colognese et Francis Rhys Ward — Q2 (facultative, billet)

Comptes : 156 jetons, 156 mots (formulaire : 156 jetons, 156 mots).

```
Most interesting finding: the anti-cheating character didn’t so much avoid hacking as shift it out of the reasoning. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never includes the hack, though its answer does, usually under a comment calling it harmless. One of my biggest concerns is that we can train away blatant forms of bad logic but more subtle attacks get reinforced. Meaning CoT/action monitoring may be less useful where character training appears to work.

Things I would do differently: (1) more seeds and character checkpoints: one resisting seed out of three, or a catch-rate gap from two seeds, is a perfectly reasonable seed effect until proven otherwise; (2) a white-box monitor, to see whether activations flag the override as a hack when the reasoning ignores or dismisses it; (3) per-character rather than pooled 2% false-alarm thresholds, since character also shifts the distribution of honest episodes.
```

### Changements par rapport au formulaire (avant → après ; raison ; source)

1. « shift it out of the text. » → « shift it out of the reasoning. » ; la triche est dans la réponse (lecteur 7) ; billet, §3.3 et Summary.
2. « its reasoning never includes the hack. » → « its reasoning almost never includes the hack, though its answer does, usually under a comment calling it harmless. » ; correction 7 déjà donnée (93 %) ; 89 % des réponses de la graine 1 (lecteur 8) ; réponses corrigées déjà données (`reponses-completes-corrigees-formulaire-2026-11-03-v1.md`) ; billet, Summary.
3. « One of my biggest concerns about this type of training is that » → « One of my biggest concerns is that » ; longueur (lecteur 9) ; aucune.
4. « more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well. » → « more subtle attacks get reinforced. Meaning CoT/action monitoring may be less useful where character training appears to work. » ; « sampled and reinforced » ; les graines 1 et 3 trichent comme les autres (lecteur 10 et 11) ; billet §4.3, §3.1.
5. « (1) using more seeds per character, since one resisting seed out of three is » → « (1) more seeds and character checkpoints: one resisting seed out of three, or a catch-rate gap from two seeds, is » ; un seul point de départ par caractère (lecteur 12) ; billet §2.1, §4.4, §3.2.
6. « (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren’t in the reasoning; » → « (2) a white-box monitor, to see whether activations flag the override as a hack when the reasoning ignores or dismisses it; » ; le code montre déjà la triche ; la question est l'intention (lecteur 13) ; billet §3.3 ; Baker et coll. annexe F.
7. « (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character’s honest episodes, » → « (3) per-character rather than pooled 2% false-alarm thresholds, » ; leur seuil de 2 % existe, commun à tous les points de départ (lecteur 14) ; billet §2.4.


## Sélection des mentors (facultative)

Comptes : 51 jetons, 49 mots (formulaire : 51 jetons, 49 mots).

```
I applied to six streams because they are all facets of one programme: whether internal-state monitors add detection power beyond black-box monitoring, and how corruptible monitors are. My order of preference: Jan Hendrik Kirchner, Lujain Ibrahim,  Stefan Heimersheim, Jérémy Scheurer, Paul Colognese & Francis Rhys Ward, Shi Feng & Eyon Jang.
```

- Aucun rapport ne la couvre ; inchangée.

## Comptes de mots (par script : `outils/compter.py`)

Jetons = éléments séparés par des espaces (comme `wc -w`) ; mots = jetons qui contiennent une lettre ou un chiffre ; caractères hors fins de ligne.

| réponse | formulaire jetons / mots | final jetons / mots | limite | caractères formulaire → final |
|---|---|---|---|---|
| Heimersheim — Q2 | 150 / 149 | 150 / 148 | 150 | 1030 → 1064 |
| Kirchner — Q1 | 547 / 546 | 547 / 546 | ≤ formulaire | 3321 → 3304 |
| Kirchner — Q2 | 540 / 538 | 538 / 537 | ≤ formulaire | 3494 → 3392 |
| Shi Feng et Eyon Jang — boîte blanche pour l'audit | 635 / 628 | 634 / 628 | ≤ formulaire | 4059 → 4190 |
| Jérémy Scheurer — tendance d'échelle | 566 / 564 | 564 / 562 | ≤ formulaire | 3330 → 3362 |
| Lujain Ibrahim — Q1 | 528 / 524 | 528 / 524 | ≤ formulaire | 3075 → 3140 |
| Lujain Ibrahim — projet technique | 284 / 282 | 284 / 282 | ≤ formulaire | 1705 → 1842 |
| Paul Colognese et Francis Rhys Ward — Q1 | 185 / 184 | 200 / 199 | 200 | 1222 → 1367 |
| Paul Colognese et Francis Rhys Ward — Q2 | 156 / 156 | 156 / 156 | ≤ formulaire | 988 → 996 |
| Sélection des mentors | 51 / 49 | 51 / 49 | ≤ formulaire | 343 → 343 |

## Lignes [À CONFIRMER PAR LAZAR] (récapitulatif)

- Heimersheim — Q2 (pourquoi l'interprétabilité ; 150 mots au plus), changement 4 : « attempting » inexact : la réponse à la dose est mesurée (lecteur, changements 3 et 4) ; la proposition « rank-1 vs rank-3 » (devenue « comparison », réserve 1) et « your exponent p… » sont retirées faute de place après D36
- Kirchner — Q1 (projet empirique), changement 3 : correction 1 déjà donnée ; réserve 3 du recoupement : le bras décisif préenregistré (plan plein) en promeut 3 sur 3, le bras de comparaison (plan gelé de 120) 2 sur 3 ; « 2 of the 3 » est prudent, « all 3 » vaut pour le bras décisif
- Kirchner — Q1 (projet empirique), changement 11 : la question demande la surprise principale (lecteur 9 ; « runs » = unités ; « A coverage hole, not adaptive overfitting. » non repris, longueur) ; W1 non jugeable, l'omettre surévalue l'attaque (lecteur 10)
- Shi Feng et Eyon Jang — boîte blanche pour l'audit, changement 8 : « meaningfully » invite la lecture « presque détecté », exclue par la lecture gelée ; lien de la page publique de P3
- Jérémy Scheurer — tendance d'échelle, changement 1 : lecture « malveillance fixe par action » (lecteur 1)
- Jérémy Scheurer — tendance d'échelle, changement 7 : lecture « par action » (lecteur 8)
- Jérémy Scheurer — tendance d'échelle, changement 8 : lecteur 9, corrigé : « only sees the total » est faux pour la lecture séquentielle (le calendrier compte), seul le plancher ne dépend que du total
- Jérémy Scheurer — tendance d'échelle, changement 9 : lecture « par action » ; « doubles » du formulaire gardé (lecteur 10 et 11 ; correction 8, « smallest »/« halves », écartée)
- Lujain Ibrahim — Q1 (première expérience), changement 8 : hypothèse alignée sur l'a priori préenregistré de R8 (lecteur 10) ; réserve 4 du recoupement : « persona » et « no approval signal » sont une transposition (R8 §9 attribue la destination à l'imitation, le gain à l'optimisation de préférences), d'où « adapted from » ; la structure dépend du modèle (lecteur 11)
- Lujain Ibrahim — projet technique, changement 2 : décision de Lazar (06:19) : le placebo de même longueur est celui de la chirurgie de l'historique ; gardé (changement 19 du lecteur abandonné), marqueur ajouté
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 2 : décision de Lazar (06:19) : chirurgie de l'historique reprise telle qu'écrite, avec marqueur ; « All pre-registered and hash-locked. » retiré : redondant avec la première phrase, « All » couvrirait le juge non figé, et place nécessaire sous 200
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 3 : place nécessaire sous 200 après D36 ; redondant avec « concede roughly 0.7 of the distance »
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 5 : correction de fond D36, raccourcie pour tenir 200 (chiffres et intervalles intacts) ; le dépôt construct-validity n'est pas cité faute de place (réserve 5 non appliquée ici)
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus) : Longueur : 200 jetons, au-dessus des 185 du formulaire, sous la limite de 200 : imposé par la phrase D36 (chiffres et intervalles gardés). [À CONFIRMER PAR LAZAR]

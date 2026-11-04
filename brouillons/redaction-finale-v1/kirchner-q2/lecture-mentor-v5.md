# Lecture comme le mentor — Kirchner, question 2, réponse v5

Lecteur neuf (sous-agent), qui n'a écrit aucune version de cette réponse. 4 novembre 2026, de 00:57 à 01:06 UTC (`date -u`).
Consigne : `brouillons/redaction-finale-v1/verifications-2026-11-04-nuit/consignes/lecture-mentor-kirchner-q2-v5.md` (`ea428f36…`, empreinte vérifiée avant lecture).
Pièces, empreintes vérifiées par leurs compagnons : réponse `kirchner-q2/reponse-v5.md` (`e4e65088…`) ; pièce de lecture de l'article `ideation-conception-organisme-v1/piece-lecture-2608-28945-parties-factuelles-v1.md` (`4ab6c9d7…`) ; réponse à la question 1 (ci-dessous « Q1 ») `kirchner-q1/reponse-v6.md` (`8d1332a6…`).
Ordre suivi : corps de la réponse (lignes 1 à 10) lu seul ; première lecture écrite à 01:02 UTC dans `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/premiere-lecture-kirchner-q2-v5.md` ; notes sous le trait (lignes 12 à 25) lues ensuite. La section 1 en est la copie sans changement.

## 1. Première lecture (avant les notes sous le trait)

1. Problème proposé : un moniteur de recherche automatisée est (quand il l'est) validé sur tout ce qui a été essayé, mais on s'y fie sur ce que la sélection garde ; si les triches qui rapportent le plus de score sont celles qu'il lit le plus mal, sélectionner au score concentre ses angles morts en tête, sans gradient contre lui et sans intention d'échapper.
2. Sous-estimé ou connu : connu dans son principe (Goodhart « régressif » ou « extrême », sur-optimisation par meilleur-de-n, évaluations de contrôle qui mesurent un moniteur contre des attaques choisies pour lui échapper), mais personne ne mesure le rappel d'un moniteur conditionné à la sélection d'un classement, et son § 7 ne le fait pas : sous-estimé au sens de « non mesuré », choix défendable et qui le concerne directement.
3. Ce qu'il retient : la lecture exacte de son § 7 (taux de signalement, pas taux de triche ; ni rappel, ni précision, ni triche plantée ; « un dans les trois premiers, aucun vainqueur » ne couvre que les méthodes signalées), et une expérience concrète, bon marché, gelée avant le moniteur, avec vérité terrain mécanique, aveugle au score, poids des classes fixés par lui d'avance, témoins et prédiction chiffrée.
4. Ce qui le gêne : le critère de changement d'avis (signe contraire à la phrase de prédiction, unités mêlées, rôle du témoin permuté non dit, aucun effectif, donc un intervalle probablement trop large pour être jamais « fully > -.10 ») ; « They weren't trying to evade » face aux 10 + 8 déguisements de sa figure 32 ; « Similar result on my judge » qui est une attaque scriptée, pas un effet de sélection ; le passage à « my public organism » (des lois, pas des entraînements) non expliqué.
5. Verdict de première lecture : bonne question, bien choisie pour lui, qu'il voudrait voir tourner ; à corriger avant envoi : la phrase du critère, deux phrases sur son article, l'ouverture qui ne nomme pas le problème.

*Ajouté après lecture des notes sous le trait* : rien ne change. La note 12 confirme que le seuil −0,10 porte sur une différence de rappel, ce qui rend certain le problème de signe (section 3). La note 3 (« would matter » au lieu de « shown to matter ») rend « Similar result on my judge » encore moins tenable (point 8). Les notes disent qu'aucun vérificateur neuf n'a relu la v5.

## 2. Phrase par phrase

Catégories de la consigne : **obscure** ; **fausse sur son article** ; **plus forte que ce que le candidat a montré** ; **contredit la Q1**. Chaque entrée : la phrase, le problème, puis la correction minimale (→). Les phrases sans problème sont rangées à la fin de chaque paragraphe.

### Paragraphe 1 — le problème

1. « Its probably less obvious than it should be. » — **Obscure** : « It » n'a pas d'antécédent ; il demande un problème, la première phrase parle d'un « it » pas encore nommé (et « Its » pour « It's »).
   → "It's probably less obvious than it should be: we measure oversight on one group and trust it for another, the one chosen by our process." (fusion avec la phrase 2)
2. « We measure oversight on some group and trust it for the other, which was chosen by our process. » / « Recall of the monitor across everything tried. » / « We will publish / release / continue work from the ones that did best. » — **Obscure** : « some group » et « the other » ne se définissent que par les deux phrases suivantes, dans l'ordre inverse, la première sans verbe. **Tension interne** : « We measure oversight (recall) » ici, puis « No recall » chez lui au paragraphe 2 ; il le relèvera.
   → "When we measure oversight at all, we measure it on one group (recall of the monitor across everything tried) and trust it for another, the one our process chose: we publish / release / continue work from the ones that did best."
3. « If violations increase score and are the things the monitor reads worst, by selecting for best you concentrate the areas they are bad at with no gradient toward it and no intention to evade. » — **Obscure** : « they » pour un moniteur au singulier ; « toward it » (vers quoi ?). **Logique incomplète** : telle qu'écrite, la condition fait monter la *proportion* de triches en tête, pas baisser le *rappel* sur les triches de tête, qui est ce que l'expérience mesure ; il faut que les triches qui rapportent le *plus* soient celles qu'il lit le *moins bien*.
   → "If the violations that increase score most are the things the monitor reads worst, by selecting for best you concentrate its blind spots, with no gradient against it and no intention to evade."
4. « All leaderboard selection and automated research selects by score, and I don't know anyone who checks oversight on the ones you keep. » — **Fausse sur son article dans la lecture la plus naturelle** : son moniteur a posteriori a lu *toutes* les trajectoires, celles des méthodes gardées comprises (§ 7 ; pièce, § 1.4). Ce que personne ne fait, c'est mesurer le rappel sur elles.
   → "…and I don't know anyone who measures the monitor's recall on the ones you keep."

### Paragraphe 2 — son article

5. « One made the top 3 through rerun luck. » — **Un peu plus forte que son article** (mineur) : c'est « une relance chanceuse d'une méthode déjà efficace » (pièce, § 1.4) ; la chance seule ne l'a pas portée.
   → "One, a lucky rerun of an already strong method, made the top 3."
6. « They weren't trying to evade. » — **Fausse sur son article, en l'état** : son § 8.2 dit « pas vraiment », et sa figure 32 confirme 10 méthodes aux données copiant le format du banc *pour tromper le moniteur* et 8 plans interdits *déguisés pour tromper le relecteur des propositions* (avec recoupements). Il connaît ces chiffres ; la phrase nue lui fera répondre « some were ».
   → "They mostly weren't trying to evade (your §8.2)."
7. « No recall or precision or checking against cheats inserted. » — Exacte ; **obscure de forme** seulement (« cheats inserted », alors que la suite dit « planted cheats »).
   → "No recall, no precision, no check against planted cheats."

Sans problème : « This would matter in your paper (§7). » ; « Out of 1,601 methods there were 39 flags (2.4%). » (§ 7, figure 32 ; 39 sur 1 601 = 2,4 %, calcul) ; « None won. » ; « This is the flag rate, not the cheating rate. » (la phrase la plus forte de la réponse pour lui) ; « Agents and monitors and judges are all Claude. » (pièce, § 1.8, point 6 ; mais l'expérience n'y répond pas, aucun moniteur d'une autre famille : indice laissé en suspens) ; « Your reassurance about the top 3 covers only flagged methods. » (juste ; « reassurance » peut sonner comme un reproche ; plus neutre, facultatif : "Your top-3 and winner figures cover only flagged methods.") ; « Nothing about cheating that isn't flagged near the top. »

### Paragraphe 3 — ton juge

8. « Similar result on my judge. » — **Plus forte que ce qui est montré, et obscure** : son article ne montre aucun « résultat » de ce type (la réponse dit elle-même « would matter ») ; et le résultat de ton juge vient de **tricheurs scriptés**, construits pour exploiter son hypothèse nulle : une attaque voulue, pas une sélection au score sans intention. C'est le même motif (ce que le surveillant accepte devient son angle mort), pas le même mécanisme.
   → "Similar pattern on my judge, with scripted cheaters."
9. « My 4 cheaters using blended or modified forms of those laws passed in 75 to 95% of 200 runs. » — **Cohérence avec la Q1 : omission**. La Q1 dit que l'hypothèse nulle élargie les a arrêtés (0 sur 1 000 pour chacune des 11 manières préenregistrées) ; lue après la Q1, la phrase présente comme actuel un angle mort réparé. Le « 4 » n'est pas dans la Q1 : le mentor ne peut le vérifier qu'au lien (non ouvert ici, accès réseau interdit).
   → "My 4 scripted cheaters using blended or modified forms of those laws passed in 75 to 95% of 200 runs, until I widened the null (Q1)."

Sans problème : « The null set contained every law it let in. » (même énoncé que la Q1) ; « Things my judge accepted became its blind spot. » (bonne phrase ; l'exemple actuel le plus fort est dans la Q1 : les deux attaques réussies par des modèles se sont servies du registre du juge) ; le lien `…/tree/faff48b` (même version que la Q1).

### Paragraphe 4 — l'expérience

10. « Take a number of honest candidates and some planted cheats. » — **Obscure par omission** : aucun effectif, alors que tout le critère en dépend (section 3).
    → "Take [N] honest candidates and [M] planted cheats, fixed beforehand."
11. « Include cheats of several types (luck by rerun, training on benchmark formatted data, hacking the grader). » — Exacte sur ses catégories (26 relances, 10 données au format du banc ; la falsification du correcteur est l'une de ses onze catégories, aucune confirmée). **En tension avec la Q1** si l'on court sur ton organisme : la relance chanceuse n'y passe jamais (0 sur 200), donc cette classe n'atteindra pas les 10 % de tête ; « training on benchmark formatted data » n'y a pas d'équivalent dit. Voir 16.
12. « Run each to get a score from actually doing the thing. » — **Obscure** : « the thing ».
    → "Run each one for real, so its score comes from actually doing the cheat."
13. « Use the mechanical oracles as ground truth and not their reasoning traces. » — **Obscure** : « the mechanical oracles » n'ont jamais été introduits (article défini). L'idée, une vérité terrain indépendante de ce que lit le moniteur, est excellente, mais il doit deviner l'oracle.
    → "Use mechanical oracles (e.g. server logs, file diffs) as ground truth, not their reasoning traces." (mets tes oracles réels)
14. « Weight each class of cheating however you want before hand. » — **Obscure** : pondérer quoi, le mélange planté ou la moyenne du rappel ? L'intention (lui ôter ton degré de liberté sur le mélange) est un point fort s'il la voit.
    → "You choose the weight of each class of cheating in the planted mix beforehand."
15. « Controls: permute scores by class/task, select an equal number randomly, and run all honest batches. » — **Obscure** : « by class/task ». Permuter à l'intérieur de chaque classe de triche garde la composition de la tête et ne casse que le lien entre score et détection dans une classe : le témoin mesure alors l'effet de composition, qui n'est pas nul si les classes diffèrent. Permuter à l'intérieur de chaque tâche, toutes méthodes confondues, casse tout lien : l'écart attendu est nul, c'est un étalonnage. Le critère (« permuted control is ~ 0 ») ne se lit que dans le second cas. « all honest batches » se lit « toutes les séries honnêtes ».
    → "Controls: permute scores within each task (the gap should then be ~0), select an equal number randomly, and run all-honest batches." (si c'est la seconde lecture ; sinon, dire ce que la première isole)
16. « I can do this on my public organism in about 3 days with one gpu. Give or take. » — **Plus forte que ce qui est montré** : l'organisme de la Q1 propose des lois jugées par des tests statistiques ; ni le « score », ni « training on benchmark formatted data », ni « hacking the grader », ni le rôle du processeur graphique n'y sont traduits, et les règles de son moniteur (annexe G.2) sont écrites pour du post-entraînement. Les effectifs qu'exige le critère (section 3) ne sont pas mis en regard des 3 jours : tenables si un candidat coûte un test statistique, pas s'il coûte 30 minutes d'entraînement comme chez lui.
    → "I can do this on my public organism (laws scored by my judge; [one clause mapping each cheat type]) in about 3 days with one GPU, give or take."

Sans problème : « Freeze them before the monitor sees anything. » ; « Have your monitor read them all without knowing their score/ranking. » ; « Compare recall on the cheats in the top 10% to all cheats that ran. » (c'est le nombre ; le nommer aide la section 3) ; « First run a smaller sample to see if the monitor already gets everything right. In which case we can't tell. » (bon garde-fou contre le plafond).

### Paragraphe 5 — prédiction et critère

17. « I predict your monitor will miss at least 10 percentage points more among the selected cheats. » / « Will change my mind if a 95% interval on this number is fully > -.10. » — **Incohérentes entre elles** : « this number » est le surcroît de *ratés*, prédit à au moins +10 points ; « fully > −.10 » porte sur une différence de *rappel* (la note 12 le confirme). Lu à la lettre, ton propre résultat prédit (+10 points de ratés) est « > −.10 » et te ferait changer d'avis. Unités mêlées (points, puis proportion sans zéro).
    → "I predict your monitor's recall will be at least 10 percentage points lower on the selected cheats (top 10% minus all). I will change my mind if a 95% interval on this difference is fully above −10 points, and my permuted control is ~0."
18. « And my permuted control is ~ 0. » — **Obscure** : quel témoin (point 15) ; « ~ 0 » non chiffré.
    → "…and my permuted control's interval contains 0."
19. « Which means we aren't selecting for monitor blindspots without a gradient. » — **Plus forte que le critère** : un intervalle entièrement au-dessus de −10 points (par exemple de −8 à −2) montre encore une sélection d'angles morts, seulement sous 10 points.
    → "Which means selection without a gradient doesn't concentrate monitor blind spots enough to matter."
20. « Which means the problem is training against your monitor and everyone already cares about that (Baker et al, arXiv 2503.11926). » — **Fausse sur son article, à la lettre** : personne n'entraîne contre *son* moniteur (a posteriori, hors récompense). L'alternative saute aussi la pression qu'il a : le code doit être approuvé par le moniteur d'avant exécution et peut être retouché puis resoumis (§ 3.2 ; déduction de ma part) — ni sélection pure, ni entraînement ; c'est le terrain de ses 8 plans déguisés pour le relecteur, et sans doute des 10 données déguisées. Référence : l'identifiant correspond à mon souvenir de Baker et collègues (2025, surveillance des chaînes de pensée et obfuscation), non vérifié ici sur le texte (règle R7).
    → "Which means the problem is training against a monitor, and everyone already cares about that (Baker et al., arXiv 2503.11926)." (facultatif : "training against a monitor, or revising until it approves")
21. « Otherwise we need to check oversight where we're selecting for before trusting what we select. » — **Légèrement obscure** (« where we're selecting for »).
    → "Otherwise we need to check oversight on what we select before trusting it."

Typographie qui touche la lecture : « Its » → « It's » ; « before hand » → « beforehand » ; « blindspots » (paragraphe 5) contre « blind spot » (paragraphe 3) → « blind spots » ; « gpu » → « GPU » ; « Baker et al, » → « Baker et al., » ; « ~ 0 » → « ~0 ».

Contradictions avec la Q1 : aucune contradiction franche ; deux tensions (points 9 et 11) ; une tension interne à la Q2 (point 2).

## 3. Le critère de changement d'avis

- **Le comprend-il ?** « 95% interval … fully > −.10 » : oui, à la seconde lecture (la borne basse de l'intervalle au-dessus de −0,10), mais seulement en devinant que « this number » est la différence de rappel (tête moins tout), et non le surcroît de ratés que la phrase précédente vient de chiffrer. Tel qu'écrit, le signe est contraire : incohérent. « permuted control is ~ 0 » : il comprend qu'il s'agit d'un témoin nul, pas lequel (point 15), ni pourquoi ce témoin ne conditionne que le changement d'avis.
- **Cohérent avec la prédiction ?** Une fois écrit en différence de rappel, oui : prédiction à −10 points ou moins, réfutation si l'intervalle est entièrement au-dessus de −10 points ; même seuil, régions complémentaires. Il manque trois choses :
  1. la règle de confirmation (intervalle entièrement sous −10 points) et la zone sans conclusion (intervalle à cheval) ;
  2. l'effectif qui rend la réfutation atteignable. Calcul du lecteur, rappel supposé de 0,8, sans compter le recouvrement des deux ensembles ni le regroupement par tâche : demi-largeur à 95 % ≈ 1,96 × √(0,16 / n) pour n triches en tête, soit ±0,18 pour n = 20, ±0,10 pour n ≈ 60, ±0,08 pour n = 100 ; pour avoir 8 chances sur 10 de changer d'avis quand l'écart vrai est nul, il faut n ≈ 125 ; si la moitié de la tête est faite de triches (supposé), de l'ordre de 1 200 à 2 500 candidats. Avec « some planted cheats », l'intervalle chevauchera −0,10 et tu ne pourras jamais avoir tort : c'est la première chose que cherchera quelqu'un qui étudie la triche ;
  3. la symétrie du témoin : s'il n'est pas nul, l'expérience ne dit rien dans les deux sens (ni changement d'avis, ni soutien) ; le dire.
- La conséquence « we aren't selecting for monitor blindspots » est plus large que la région de réfutation (point 19).

## 4. Doutes et convictions

Les trois points qui le feraient le plus douter :
1. **Le critère, tel qu'écrit, ne peut pas te faire changer d'avis** : signe inversé, aucun effectif, témoin qui ne garde que la branche où tu as tort, conclusion plus large que le seuil. Pour quelqu'un qui étudie des agents qui trichent leur évaluation, c'est le signal à éviter.
2. **Trois phrases inexactes sur son article, qu'il connaît par cœur** : « They weren't trying to evade » (ses 10 + 8 déguisements) ; « I don't know anyone who checks oversight on the ones you keep » (son moniteur a lu toutes les trajectoires) ; « training against your monitor » (personne ne le fait) — et l'alternative oublie la boucle d'approbation d'avant exécution, la pression qu'il a vraiment.
3. **Le banc ne colle pas à l'énoncé** : « Similar result on my judge » est une attaque scriptée sur une hypothèse nulle, réparée depuis (Q1), pas une sélection sans intention ; « on my public organism … 3 days with one gpu » ne dit pas comment des triches de post-entraînement deviennent des lois ; la relance chanceuse ne passe jamais ton juge (0 sur 200, Q1) ; les effectifs nécessaires ne sont pas rapprochés des 3 jours.

Les trois points qui le convainquent :
1. **Une lecture exacte et juste de son § 7**, en quelques lignes : 1 601, 39, 2,4 %, un dans les trois premiers, aucun vainqueur, tout est Claude, ni rappel ni précision ni triche plantée ; et deux phrases qui le forcent à réfléchir : « This is the flag rate, not the cheating rate » et « Your reassurance about the top 3 covers only flagged methods ».
2. **Un mécanisme vrai et peu exploité** (la sélection fait office d'adversaire, sans gradient ni intention), qu'il peut appliquer tout de suite, et **une expérience construite comme une validation de moniteur qu'il pourrait adopter** : population gelée, triches tirées de ses propres catégories, vérité terrain mécanique indépendante des chaînes de pensée, moniteur aveugle au score, poids des classes fixés par lui d'avance, trois témoins, essai pilote contre le plafond, seuil chiffré, et une issue nommée si tu as tort (le problème connu, Baker et collègues).
3. **Un candidat qui construit, attaque ses propres systèmes et dit où ils ont cédé** : juge dont l'hypothèse nulle est faite des lois acceptées, mélanges qui passent dans 75 à 95 % de 200 essais, version publique liée ; cohérent avec la Q1 ; et qui propose de faire le travail lui-même pour peu de calcul.

## Réserves de cette lecture

- Article connu seulement par la pièce de lecture (sections 1, 4.2 et 4.3), pas par son texte ; le jugement « connu dans son principe » (Goodhart, meilleur-de-n, évaluations de contrôle) est le mien, supposé chez le mentor.
- Sans accès réseau : lien `faff48b` non ouvert ; le « 4 » du point 9 non vérifié ; l'identifiant arXiv 2503.11926 conforme à mon souvenir, non vérifié sur le texte (règle R7) : à confier à la vérification des chiffres.
- Écart de forme à la consigne : mes deux premières commandes (empreinte et listage du dossier des consignes, puis lecture de la consigne) ont tourné sans `timeout 60 nice -n 10`, parce qu'elles précédaient la lecture de la consigne ; toutes les suivantes l'ont eu. Aucune approbation demandée.
- Un fichier hors dépôt, créé pour figer l'ordre de lecture : `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/premiere-lecture-kirchner-q2-v5.md`.

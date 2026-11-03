# Lecture comme le mentor — Kirchner, question 1, variante sans interne — v1

- Écrit le 3 novembre 2026, de 12:50 à 13:07 UTC (`date -u`), par un lecteur neuf qui n'a écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal.
- Texte lu : `brouillons/redaction-finale-v1/kirchner-q1/reponse-variante-sans-interne-v1.md`, sha256 `fb150cb146c8f2e3c501ffbb481f0dbc2d462d4a7394a37605e26eb2dc70b7d5` (vérifiée avant lecture ; égale à son compagnon).
- Question : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (sha256 `57393598…19f7b5c6`), ligne 29 : « Describe an empirical research project you drove yourself. What was the question, what did you build or run, and what was the most surprising thing you found? » ; ligne 33 : « If relevant, you may choose your project answer from the main application. » Aucune limite écrite ; visée : 450 mots au plus.
- Le mentor : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-kirchner-v1.md` (sha256 `13f506e0…5123f8db9b`, égale à son compagnon) ; sa page Pivotal, copie collée par Lazar, `brouillons/ideation-kirchner-q2-v1/page-pivotal-kirchner-collee-par-lazar-2026-11-03-0948.md` (sha256 `2481005e…b793fcb355`, égale à son compagnon) ; arXiv 2608.28945, section 7, relue ce jour par `WebFetch` (trois phrases).
- Ce que le mentor peut ouvrir depuis la réponse : le dépôt public `lciric/ideation-organism`, lu par `gh api` en lecture seule au commit `faff48b` (3 novembre, 10:23 UTC, dernier commit public) : `README.md` ; `resultats/attaque-goodhart-v2/README.md` (page de l'attaque) ; préenregistrement de l'attaque `orchestrator/prereg/preenregistrement-attaque-goodhart-v2-v1.md` (sha256 `fc81d015…686925b65`, égale à l'empreinte affichée sur la page) ; préenregistrement de la validation du nul v9 `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` (sha256 `54c5713d…d62c18fb`, égale à son compagnon public) ; code `orchestrator/pole/attaque_goodhart_v2.py`. Rien de téléchargé n'a été écrit sur disque.
- Noms courts repris des sources : A1, l'attaque du juge par des proposeurs modèles de langage ; W1, le monde jouet dans le nul v8 ; W2, le monde par morceaux, hors du nul v8 ; P5 et P6, deux prédictions préenregistrées de A1 ; Δ₄(v8), l'écart de taux de promotion « avec verdicts moins sans verdicts » à 4 tentatives sous le nul v8 ; ¶n, le n-ième paragraphe de la réponse.

## Verdict

Aucun point bloquant : chaque chiffre et les deux liens tiennent face au dépôt public et au papier du mentor, et la première phrase cite fidèlement sa page. Cinq points à corriger, dont un prioritaire : la phrase de la surprise (¶5) dit plus que la page liée, qui écrit « the share of the feedback is not measured ». 417 mots, sous la visée de 450.

## 1. La phrase qu'il contredirait

Aucune phrase n'est contredite par ses textes. Une comparaison l'appelle à nuancer.

**1.1 — à corriger — ¶3 « The lucky re-run, the only cheat that reached a top three in your paper, never got promoted here »**
- Ce qu'il dirait : « Exact ; mais chez nous non plus elle n'a jamais été retenue. Le top trois est le classement de la course ; le choix final passe par le banc tenu à l'écart. »
- Sa source : 2608.28945 §7, « Only one reached the top three on its leaderboard, a lucky re-run of an already effective method (Fig. 32a) » et « no cheating attempt is ever the method we report for an alignment failure » (relues ce jour) ; §2.1 et §2.3 (rapport, 1b-1).
- Pourquoi : « top three in your paper » contre « never got promoted here » compare un rang dans sa course à une acceptation finale chez Lazar ; la phrase laisse entendre que son système a laissé passer la relance.
- Correction minimale : « …reached a top three in your paper (your held-out pick still kept it out), never got promoted here… » (+7 mots).

Vérifiées exactes face à lui : la première phrase (sa page, projet 2 : « how do we reliably catch them gaming the setup? ») ; « the only cheat that reached a top three » (§7, mot pour mot) ; « hiding scores or capping submissions would not have closed it here » va dans le sens de son billet « weak-to-strong », où les plafonds de soumissions ne mordent qu'à environ 10 soumissions (rapport, 1b-7).

## 2. Affirmations plus fortes que leur preuve

**2.1 — à corriger, prioritaire — ¶5 « I had preregistered that seeing the verdicts would help the attacker. They had nothing to add: the description alone showed the attacker where the judge is blind. »**
- La page liée dit moins : « on W2, Argon was promoted in 12 of 12 units, 11 of them at the first attempt with or without feedback, so the share of the feedback is not measured » (page de l'attaque, paragraphe « Result »). Le mentor qui clique lit « not measured » là où la réponse dit « nothing to add ».
- « alone » n'est pas isolé : l'attaquant recevait aussi les deux lois de l'archive et 60 tirages de développement du monde, avec la sous-population (préenregistrement A1, §4, lignes 112 et 113 ; code `orchestrator/pole/attaque_goodhart_v2.py`, ligne 61 `TAILLE_DEVELOPPEMENT = 60` et ligne 185, colonnes `z0`, `z1`, `g`, `issue`). Aucun bras sans description. Que la description, plutôt que ces tirages étiquetés par sous-population, ait guidé l'attaquant est la lecture écrite d'avance (P5, branche ouverte : « la description du juge suffit au témoin »), pas une mesure. Le mentor ne le verra pas (préenregistrement en français), mais il peut le demander en entretien ; même réserve pour « then its description » dans la dernière phrase du ¶5.
- La surprise est réelle, mais elle porte sur l'ampleur : P5 (« le retour apprend le goût du juge », Δ₄(v8) ≥ +0,10) est fausse ; P6 (« la description seule suffit parfois », taux sans verdicts ≥ 0,30) était aussi préenregistrée, et elle est vraie (page : « P1, P3, P4 and P6 true; P2 and P5 false »).
- Correction minimale : remplacer la deuxième phrase par « They never got the chance: 11 of the 12 promotions came at the first attempt, before any verdict existed. » Option : « I had preregistered that verdicts would add at least 10 points » rend la première phrase vérifiable.

**2.2 — à corriger — ¶4 « There, one model got a law promoted in all 12 of its runs »**
- Le second fournisseur (Kimi) a été coupé sur les deux mondes, pas seulement sur W1 : « Kimi produced 5 laws in 1,524 attempts; 21 of its 24 units have none », « In practice the results are Argon's » (page de l'attaque) ; `README.md`, ligne 129 : « Argon promoted in 12 of 12 units ». La réponse rattache le plafond au seul W1 : le lecteur peut croire qu'un second modèle a tenté W2 et échoué.
- Correction minimale : « There, the only model that ran in full got a law promoted in all 12 of its runs » ; pour W1, « cut off the other provider ».

**2.3 — mineur — ¶2 « 929 tests »**
- `README.md`, ligne 116 : « 906 passed, 8 failed, 15 skipped, 669 subtests passed (929 tests) » ; les 8 échecs sont des contrôles de provenance ou d'environnement. À côté de « each killed for the expected reason », « 929 tests » se lit comme 929 succès.
- Correction : « 929 tests (the 8 failures are provenance checks) », ou laisser.

**2.4 — mineur — ¶4 et ¶6, état de la page liée**
- La page au commit `faff48b` dit encore « A new preregistration is being written for a clean rerun » ; la réponse dit « A clean rerun of the attack is preregistered », ce qui est exact (commits publics `ba4edfe1` et `4848ad97`, 3 novembre : préenregistrements A1-v3 v1 et v2 scellés). La même page laisse « an open decision » sur le défaut du plafond partagé, les issues valant « as read » en attendant.
- Correction : hors de la réponse, mettre la page à jour (publication : décision de Lazar) ; ou écrire « (sealed 3 November) ». Si la décision ouverte a été prise, le dire.

## 3. Ce que la question demande et qui manque

Les trois parties sont couvertes : la question (¶1), ce qui a été construit et lancé (¶2 à ¶4), la surprise (¶5, annoncée comme telle). « Drove yourself » : « I built », « I attacked », « I had preregistered » suffisent.

**3.1 — à corriger — sur quoi portent les « laws »**
- ¶2 : « language-model agents propose laws », sans objet. `README.md`, ligne 3 : « propose research hypotheses on AI control ». Sa page : « Research Direction: Using frontier AI to accelerate alignment research », « Can we point them at alignment itself? ». Le lien le plus direct avec son travail (un chercheur automatisé sur le contrôle, avec une autre règle de sélection) manque.
- Correction : « propose laws about AI control » (+3 mots).

**3.2 — à corriger — ¶6 « It has run; the result is not yet published. »**
- La question demande ce qui a été trouvé ; annoncer une course faite sans son résultat appelle « pourquoi pas ? » et peut se lire comme un résultat négatif tu. Rien de public ne permet au mentor de vérifier « It has run ».
- Correction : supprimer la phrase, ou « Its result will be posted on the same page, null or not. » ; ou donner le résultat s'il est publié avant l'envoi (publication : décision de Lazar).

**3.3 — mineur — W1 testait sa menace de relance, et la réponse ne le dit pas**
- Page de l'attaque : W1 est le monde où « a false promotion can only come from the multiplicity of attempts or from a code defect » ; « Nothing bounds the number of attempts, though: … 0.560 for n = 16 » ; « 1 of 24 units had a law promoted under v8 within 16 attempts ». C'est l'analogue le plus proche de ses relances (26 sur 39, §7). S'il clique, il rapprochera ces lignes du ¶3 (« never got promoted here ») ; mieux vaut que la réponse le fasse.
- Correction : « The other world, inside the null, tested repeated attempts, your re-run threat; it was not judgeable: … » (+7 mots).

**3.4 — mineur — rien sur données réelles**
- Tout est synthétique, et la dernière phrase dit qu'aucune hypothèse réelle n'est promue : il peut se demander si le juge a de la puissance hors des mondes jouets. `README.md`, ligne 123 (lecture préenregistrée du 2 novembre, 288 épisodes réels, graines neuves) : 0 sur 19 faux témoins promus ; 2 sur 3 lois plantées promues avec le plan gelé.
- Correction, si la place le permet (+17 mots) : « On 288 real model episodes, a preregistered reading promoted 2 of 3 planted laws and 0 of 19 fakes. »

## 4. Ce qui le perdrait

**4.1 — mineur — ¶2, la phrase des e-values**
- « It computes e-values on fresh draws seeded by each law's commitment hash, against a null containing every accepted law, with Ville's threshold and e-BH across submissions. » Cinq objets techniques en une phrase ; son papier n'en utilise aucun (bibliographie de 2608.28945 : ni Ville, ni e-values ; rapport, 1b-9). « Ville's threshold » et le sigle « e-BH » ne sont pas définis ; la raison du semis par l'empreinte (aucun agent ne choisit ses graines, contre la triche « cherry-picking random seeds » de son billet « weak-to-strong », rapport Q2-9) n'est pas dite. Premier mineur à promouvoir si la place le permet.
- Correction : « …seeded by each law's commitment hash (no agent picks its seeds), … with a fixed evidence bar (Ville's inequality) and false-discovery control across submissions (e-BH). » (+11 mots).

**4.2 — mineur — ¶3 « 11 fatal lines »**
- « lines » ne veut rien dire hors du `README.md`, qui dit lui-même « the 11 fatal cheats » (ligne 119).
- Correction : « on each of the 11 cheats that must never pass ».

**4.3 — mineur — ¶3 « A pooled null »**
- Non défini ; `README.md`, ligne 82 : « fitted pooling of all known laws ».
- Correction : « A null that pools all accepted laws closed them ».

**4.4 — mineur — ¶4 « a spending cap shared by mistake cut off one provider »**
- Se relit deux fois : partagé entre quoi ? quel fournisseur ?
- Correction : « a budget cap wrongly shared between the two model providers cut one off ».

**4.5 — mineur — ¶5 « Both attacks that worked used the judge's own record: its acceptances, then its description. »**
- « record » convient aux acceptations, pas à la description.
- Correction : « used what the judge itself makes public: its acceptances, then its description. »

**4.6 — mineur — ¶6 « No real hypothesis has been promoted yet. »**
- La réponse dit « laws » partout ; « real hypothesis » est ambigu (vraie ? tirée de données réelles ?).
- Correction : « No law found in real data has been promoted yet. »

**4.7 — mineur — ¶2 « I built … I built it »**
- Deux phrases de suite ouvrent sur « I built ».
- Correction : « Built in October with AI coding agents, under written rules: … ».

Liens : les deux ont une raison et s'ouvrent publiquement (dépôt public ; chemin `resultats/attaque-goodhart-v2` présent au commit `faff48b`). Nombres : tous ont leur unité, sauf « 11 fatal lines » (4.2).

## 5. Ce qui le retiendrait (à ne pas couper)

1. ¶1 reprend la question exacte de sa page (« how do we reliably catch them gaming the setup? ») et la retourne en question compagnon : faire échouer la triche par construction. C'est l'accroche.
2. ¶3 cite le seul détail de sa section 7 qui compte ici (la relance chanceuse, seule triche dans un top trois) et donne son analogue testé (copie renommée d'une loi acceptée, 0 sur 200) : preuve d'une lecture serrée.
3. ¶3 montre un échec, puis sa réparation préenregistrée avec son prix (75 à 95 % ; puis 0 sur 1 000 sur chacune des 11 lignes ; lois neuves promues à 0,983 et 0,978, `README.md` ligne 102) : c'est le « interpret messy results without hand-holding » de sa page.
4. ¶4 : mondes construits seulement à partir de lois acceptées, donc toute promotion est fausse (vérité connue) ; W1 déclaré non jugeable avec sa cause (`README.md`, ligne 129, l'attribue bien au plafond partagé).
5. ¶5 : une prédiction préenregistrée tombée fausse, donnée comme la surprise ; « coverage, not adaptive overfitting » ; plafonds et scores cachés n'auraient pas suffi, ce qui rejoint le résultat de son groupe sur les plafonds (accroche possible, +8 mots : « as your weak-to-strong post found for caps »).
6. « Both attacks that worked used the judge's own record » : ce que le dispositif publie est la surface d'attaque ; utile pour « experiments extending the open-source harness » (sa page).
7. ¶2 : construit avec des agents de code sous règles écrites, soit sa direction « Using frontier AI to accelerate alignment research » ; 224 mutations, chacune tuée pour la raison attendue.
8. ¶6 : prix prédit avant la course ; « No real hypothesis has been promoted yet » : l'honnêteté qu'il pratique lui-même (« suggestive rather than established »).

## 6. Compte de mots

- `wc -w` : 417 mots, dont 2 liens (415 hors liens) ; `wc -m` : 2 629 signes ; un second compte par expression régulière donne aussi 417. Par paragraphe : 36, 76, 98, 92, 64, 51.
- Limite : aucune écrite ; visée de 450 respectée, marge de 33 mots.
- Les cinq points à corriger ajoutent environ 14 mots (1.1 +7, 2.2 +4, 3.1 +3) et en retirent par 2.1 et 3.2 : la visée tient. Tous les mineurs ensemble (4.1 +11, 3.3 +7, 3.4 +17, 5.5 +8…) la dépassent : choisir.

## 7. Vérifications faites, rien à changer

| Affirmation de la réponse | Source publique | Verdict |
|---|---|---|
| « Your page asks how to reliably catch automated researchers gaming the setup » | page Pivotal, projet 2 | exact |
| « the only cheat that reached a top three in your paper » | 2608.28945 §7 | exact, mot pour mot (voir 1.1) |
| « 27 scripted cheaters » | `README.md` l. 119 ; page de l'attaque | exact |
| « 929 tests; 224 deliberate code mutations, each killed for the expected reason » | `README.md` l. 116 et 117 | exact (voir 2.3) |
| « a renamed copy of an accepted law, 0 times in 200 » | `README.md` l. 84 (copie renommée, nul v7) | exact |
| « in 75 to 95% of 200 runs, … four cheaters » | `README.md` §3.1 (rapport, 1c) ; l. 94 | exact |
| « 0 of 1,000 on each of 11 fatal lines … (1 November) » | `README.md` l. 100 et 119 | exact (voir 4.2) |
| « about 98% of the time » | `README.md` l. 102 : 0,983 et 0,978 | exact |
| « fresh draws seeded by each law's commitment hash » | `README.md` l. 57 et 68 | exact |
| « e-BH across submissions » | `README.md` l. 90 et 122 | exact |
| « all 12 of its runs, 11 times at the first attempt, with or without verdicts » | page de l'attaque | exact (voir 2.2) |
| « a class the null declares it does not cover » | page ; préenregistrement A1 l. 258 | exact |
| « not judgeable: a spending cap shared by mistake cut off one provider » | `README.md` l. 129 ; page, paragraphe « Correction » | exact |
| « I had preregistered that seeing the verdicts would help the attacker » | préenregistrement A1, P5 ; page : « P2 and P5 false » | exact (voir 2.1) |
| « preregistered on 2 November, with its price predicted: lost power on weak genuine interactions » | préenregistrement v9 v1 : issue attendue « puissance perdue », portée par I02 « interaction faible » | exact |
| « A clean rerun of the attack is preregistered » | commits `ba4edfe1` et `4848ad97` | exact (voir 2.4) |
| « It has run » | rien de public | invérifiable par le mentor (voir 3.2) |
| « I built it in October » | `README.md` l. 120 (course réelle du 27 octobre) ; l'historique public commence le 1er novembre (commit `e04165b8`) | exact ; l'historique ne le montre pas |
| lien 1 et lien 2 (`tree/faff48b/resultats/attaque-goodhart-v2`) | dépôt public ; chemin présent à ce commit | s'ouvrent |

## Limites

- Page du mentor lue sur la copie collée par Lazar, pas sur le site.
- Papier : seule la section 7 relue ce jour ; le reste vient du rapport de lecture.
- Dépôt lu au commit `faff48b` ; un commit plus récent pourrait changer 2.4 et 3.2.
- Les fichiers voisins de ce dossier (`reponse-v1.md`, `registre-affirmations-v1.md`, `note-piste-v1.md`) n'ont pas été lus.

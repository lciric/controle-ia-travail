# Note de piste — réponse de Lazar à Kirchner, question 2 — v1

- Rédacteur neuf (sous-agent), 3 novembre 2026, de 13:24 à 13:51 UTC (`date -u`). Je n'ai écrit aucune version des réponses de Lazar. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-kirchner-q2-v1.md`, sha256 `b48dade96a8495589f8e0736d51d27705364a0559a95ab909082c8e1bcd1d272`, vérifiée avant lecture.
- Question (formulaire collé, ligne 73) : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? » La réponse actuelle de Lazar (lignes 75 à 79) n'a servi que de réservoir de faits : ni sa structure (« Underrated: … Overrated: … »), ni son ordre, ni ses phrases.
- Piste gelée : groupe « bruit sélectionné » (dossier `brouillons/ideation-kirchner-q2-v1/dossier-piste-kirchner-q2-v1.md`, sha256 `fa8079971b1f8693d5a1e30d2b2b37db7f1dde93e1a813183f64ad43e4271b63` ; choix `choix-piste-v1.json`, sha256 `9ae3defc0e1bdce145d89d462fc7889f1602756066eb8cad15571802054a3f03`).
- Tous les faits de son article ont été relus par moi sur le PDF empreinté (`brouillons/ideation-kirchner-q2-v1/sources/arxiv-2608.28945v3.pdf`, sha256 `6686c7bf3c80e319b3da79e12ac7e6ccf78c729a409815255748040cec14aa59`), page citée, en plus de la pièce vérifiée (`piece-lecture-2608-28945-parties-factuelles-v1.md`, sha256 `4ab6c9d780ac3ae9f44b70ff97e785c77d973d178a7aec3d027f8e06e584026b`). Aucun chiffre ne vient d'une fiche.

## 1. Les arguments retenus

**A1 — Le haut du classement, au-delà de la médiane, peut n'être que du bruit sélectionné ; son article en donne toutes les pièces** (fiche KM-13, corrigée).
1. Tout est sur le PDF : D.3 (p. 36-37), §5.1 (p. 7), A.3 (p. 21), §2.3 (p. 4).
2. C'est sa propre question ouverte : « We pose this as a question rather than a result » ; « we have not run the experiments that would separate them » (p. 36).
3. Le bruit est une quatrième lecture, et la seule qu'un re-entraînement sépare des trois siennes : plafond, plancher et rendements log-linéaires supposent tous que le gain sur la suite est réel.
4. L'expérience ne demande que ses outils : classement, instantanés de code (§3.1, p. 5), Petri à 100 audits par méthode (D.3).
5. Mesure qui tue, signe et seuil d'avance : la part de la marge du groupe de tête sur le groupe médian qui survit au re-entraînement ; la moitié ou plus, et je me trompe.

**A2 — Une règle d'arrêt doit être calibrée à l'unité qui porte le bruit, la soumission entière, pas l'item** (appui public de Lazar : T0.3).
1. Public, épinglé : `https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses` (sha256 de la page `04ce0afcedb95478103fb76c15680f185e8614c0f0ed08616162d848270d8ba0`).
2. Le mécanisme a son analogue exact : un effet d'épisode y est « a shift shared by all the scores of an episode » ; chez lui, un effet de graine décalerait ensemble tous les items d'une soumission.
3. Ses intervalles sont calculés sur les items (A.3, p. 21) : ils ne voient pas ce décalage.
4. C'est la règle d'arrêt de KM-13, enfin définie : nulle « aucun gain sur le meneur du moment », seuil calibré sur des re-entraînements entiers, chaque soumission comptée.
5. Mesure qui tue : l'écart de Petri entre son gagnant et le choix de la règle ; 0,5 point ou plus en faveur du gagnant, et l'arrêt précoce coûte de la sûreté.

**A3 — Pourquoi sous-estimé : il ne faut aucune triche, et l'erreur croît avec le débit.**
1. Le meilleur de N scores bruités monte avec N : plus les chercheurs automatiques sont bon marché, plus le haut est sélectionné.
2. Son moniteur d'intégrité classe en triche « reporting the best of many seeds or evaluation runs » (G.2, p. 52).
3. Là où les méthodes diffèrent moins que le bruit, un classement fait la même chose par construction ; aucun moniteur ne regarde le classement.
4. Cela touche sa ligne de travail (attraper la triche) sans reprendre la Q1.
5. F.2 (p. 49) dit où une règle s'arrêterait : environ 0,8 du score final arrive dans le premier quart d'une course.

## 2. Application de la règle (appui public et mesure qui tue ; drapeaux)

- **KM-13 (sans drapeau) : gardée, corrigée.**
  - Chiffres inversés dans la fiche : selon le PDF (p. 36), la médiane vaut 5,42 ± 0,64 et le gagnant 5,65 ± 0,61 ; plus bas = plus sûr (légende de la figure 19, p. 38).
  - « Environ 200 exemples par banc » : vérifié (A.3, p. 21). La citation « biased upwards by taking a maximum over noisy evaluations » est en §5.1 (p. 7), pas en D.3 comme le disait la fiche.
  - Objection o5 : la courbe dose-réponse de sycophancie comme auditeur externe est retirée ; Petri lui-même la remplace.
  - Objection o2 : T0.3 est dit « calibrated on 1,000 whole honest episodes », jamais « par permutation ».
  - Objection o3 : la règle a une nulle (« aucun gain sur le meneur du moment »), un seuil calibré, et compte chaque soumission ; la réponse ne revendique ni validité séquentielle ni contrôle des fausses découvertes au-delà de ce calibrage.
  - Objection o4 : la règle a toujours un membre (le dernier meneur qu'elle a couronné) ; aucune course n'est écartée ; si elle choisit la même méthode que le gagnant, l'écart est nul, ce qui est compatible avec la prédiction, et l'enjeu devient le budget.
  - Objection o6 : dix méthodes par groupe, trois graines, deux échecs ; le maximum n'est plus comparé à un seul point.
  - Champ vide « résultat qui ferait changer d'avis » : rempli, avec signes et seuils.
- **KM-05 (drapeau rouge) : non reprise.** Son texte dit la garde faite pour « rule out a collapse rather than certifying that capability is unchanged » ; et son mécanisme reposait sur les 26 relances sur 39, interdites ici par la coordination. Corrigée de son drapeau, la fiche ne dirait plus rien qu'il n'ait écrit. Le fait voisin, vérifié dans la pièce (E.2 : le vainqueur 72B franchit la ligne de refus de 0,001, avec un bruit de mesure que les auteurs notent), n'est pas repris : il porte sur une porte et coûte la place.
- **KM-14 (drapeau rouge) : non reprise.** Le banc tenu à l'écart n'est jamais montré aux agents ; reste la multiplicité du choix final parmi les meneurs, qu'ils disent eux-mêmes (§2.3, p. 4 : « a validation set for that choice »). Corrigée, elle se réduit à leur texte.
- **KM-15 (lecture de contrôle, « sélection sans gradient ») : non utilisée.** Une phrase sur le rappel du moniteur parmi les méthodes retenues aurait ouvert un second problème dans 450 mots sans renforcer la piste.

## 3. Coordination avec la Q1

- Q1 retenue (`brouillons/redaction-finale-v1/kirchner-q1/reponse-v2.md`, sha256 `da5ce1e80dbf7aa1eb53452f44442f1204db49dd6ae5df2a93959e1f11d6fbc5`) : organisme, juge, attaque, relance chanceuse.
- La Q2 ne reprend ni « 26 of 39 », ni la relance chanceuse, ni la description du juge : elle dit seulement « an e-value rule » et « my preregistered simulation ». Elle regarde vers l'avant, sur ses outils et ses journaux.
- Aucun fait interne ; aucun résultat du nul v9 (R-1307) ; ni ρ = 0,684 ni le bras « 1 % ».

## 4. Relecture comme le mentor, et corrections faites

Phrases qu'il aurait contredites de son article, corrigées avant le texte final :
1. « the problem your Appendix D.3 leaves open: … selected noise » lui attribuait la lecture par le bruit, absente de D.3 → « a question your Appendix D.3 leaves open ».
2. « Benchmarks of around 200 test examples are admitted in A.3 so a score can … » confondait le critère (au moins 25 unités notables) et la moyenne → « A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average ».
3. « (the climb is real, as all three of your readings assume) » : la lecture « plancher » ne dit rien du gain sur la suite → « (the climb is real on your suite) ».
4. « an automated researcher's climb » : cinq agents partagent un classement par échec (§3.1) → « the automated researchers' climb ».
5. « about 60 H200-hours » ne compte que l'entraînement (30 minutes par méthode, §3.1) → « of training ».
6. Ajout « (fresh items where available) » : re-entraîner sur les mêmes items ne mesure pas le surapprentissage du sous-ensemble privé noté (incohérence entre §2.3 et §5.1 relevée par la lecture du PDF : pièce vérifiée, § 1.8, point 4).

Phrases qu'il pourrait encore discuter, gardées :
- G.2 : le moniteur vise le meilleur de plusieurs graines d'une même méthode ; le classement, le meilleur de plusieurs méthodes. Le « may differ by less than the noise » porte exactement cette condition.
- « your intervals are computed over items » : vrai d'A.3 (et de la porte de capacité) ; le classement lui-même n'utilise pas d'intervalle.
- « Petri, the test nothing is selected on » : c'est sa phrase de §2.3 ; dans les résultats principaux, la méthode auditée a été choisie sur le banc tenu à l'écart.

## 5. Réserves

1. **Accès.** Les journaux, instantanés de code et points de contrôle de 2608.28945 sont chez Anthropic ; sa page de mentor parle d'« experiments extending the open-source harness ». Si les journaux ne sortent pas, l'expérience doit être lancée par son équipe, ou refaite sur le harnais ouvert, qui est un autre cadre.
2. **Rejeu hors ligne.** Il ignore la réaction des agents à un classement plus strict ; c'est l'objet d'une seconde expérience.
3. **Décision sur estimations ponctuelles.** La règle d'intervalle, les graines (SeedSequence), la nulle et le calibrage de la règle d'arrêt, et le comptage des soumissions restent à écrire dans un préenregistrement scellé avant toute lecture.
4. **Précision (calcul).** Si ± 0,61 à 0,64 est la demi-largeur à 95 % pour 100 audits (légende de la figure 19), 400 audits donnent environ ± 0,32 par méthode et ± 0,45 sur l'écart : le seuil de 0,5 point est à peine résolu. Entre les groupes, la variance entre méthodes dominera.
5. **Le seuil de 0,5 point est mon choix.** Il est voisin de la demi-largeur d'une méthode à 100 audits, et vaut environ le quart de ce qu'atteindre la médiane gagne en tromperie (7,5 − 5,42 = 2,08). Il est aussi au-dessus des 0,4 point que tout le haut du classement a gagnés en injection : un lecteur pourrait y voir un seuil taillé sur le résultat connu.
6. **T0.3.** Scores synthétiques ; cellules les plus fortes choisies après des essais exploratoires ; aucun verdict de lecteur neuf ; robustesse à un décalage entre calibrage et déploiement non testée. La réponse dit « synthetic scores » et « at the strongest settings ».
7. **Items frais.** Peut-être inexistants : les bancs font environ 200 exemples.
8. **Le pari peut perdre.** La lecture « plafond » est plausible ; une part de marge supérieure à la moitié réfuterait le bruit, et c'est voulu.
9. **Coût.** Petri (4 000 audits, plus 400 pour chacune des deux méthodes comparées par échec) n'est pas chiffré.

## 6. Ce que Lazar doit confirmer

1. Le pari, et ses trois seuils : la moitié de la marge, 0,5 point de Petri, la première moitié de chaque course.
2. « my preregistered simulation » pour T0.3, résultat de son programme de contrôle publié dans le dépôt de l'organisme.
3. Le ton de la phrase sur G.2, la plus pointue de la réponse.
4. S'il faut une demi-phrase sur l'accès aux journaux (environ 10 mots : la réponse en a 441 sur 450).
5. F.2 (premier quart) ou E.2 (112 soumissions après le vainqueur 72B, rien de mieux) comme appui du budget.
6. Le lien épinglé à `faff48b` (tête publique d'après la référence locale `origin/main` ; aucun `git fetch`).
7. L'usage de « AAR » (sigle de son article) dans la réponse.

## 7. Chronologie (`date -u`)

- 13:24:37 — empreinte de la consigne vérifiée ; empreintes des sources citées vérifiées (dossier de piste, pièce PDF, recoupement, Q1).
- 13:25 à 13:37 — lectures : dossier, pièce PDF, rapport sur le mentor, pièce « nos résultats », README public et page T0.3 (suivie à `faff48b`), lectrice indépendante (Fable n° 1), état réel, recoupement (lignes Kirchner), rapports sur les pages publiques, choix et groupes, classement, page du mentor ; PDF trouvé (`6686c7bf…`) et relu aux pages 4, 5, 7, 21, 35 à 38, 42, 49, 51, 52.
- 13:38:53 — premier jet, 502 mots ; 13:39:59, 482 ; 13:40:37, 461 ; 13:41:02, 441 ; 13:42:14, 450 ; 13:42:37, 439 ; 13:43:59, texte final, 441 mots (`str.split()`).
- 13:44 — `reponse-v1.md` écrit par script (création exclusive).
- 13:45 à 13:47 — registre écrit ; pied de `reponse-v1.md` corrigé (locale de `wc`) ; deux renvois du registre corrigés (base 7,5 : p. 37 ; phrase « An attempt is flagged » : G.2, p. 52).
- 13:49 à 13:51 — cette note ; heures de fin relevées à 13:50:00 par `date -u`.

Lus et non utilisés dans la réponse : la pièce sur l'état réel de l'organisme (`09a4a028…`, faits internes, rien de nécessaire) ; le README de `sycophancy-construct-validity` à `146b2a4` (`de5d6032…` ; la non-réplication du rang 3 tient à un effet générique et à une troncature, pas à du bruit : ne pas la présenter comme un exemple de bruit sélectionné).

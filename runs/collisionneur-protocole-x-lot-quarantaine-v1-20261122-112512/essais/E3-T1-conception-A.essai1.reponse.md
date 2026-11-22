# Proposition A · Tour III.1 : conception ciblée, à l'aveugle

## État des pièces

- Le bloc FAITS et le bloc QUESTION ont le même contenu et annoncent le même sha256, que je n'ai pas recalculé. Le bloc FAITS ne contient donc aucun fait muni d'un statut, seulement l'énoncé de la question.
- L'en-tête mentionne « réponse 23 de Fable » et « notes retirées ». Ni cette réponse ni ces notes ne sont transmises, et je n'en infère rien.
- Aucune proposition B–F n'est transmise à ce tour, donc B1 est sans objet ici.

Conséquence : je n'attribue VÉRIFIÉ à rien. Ce que dit l'énoncé est RAPPORTÉ, mes ajouts sont HYPOTHÈSE. Tous les seuils, effectifs et coûts sont illustratifs, et toutes les références sont citées de mémoire.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi elle compte |
|---|---|---|---|
| P1 | Les auteurs n'ont pas consulté le *genre* de l'ensemble | RAPPORTÉ, sans journal d'accès transmis | « Genre non vu » et « cas non vus » sont deux propriétés distinctes, et l'énoncé ne garantit que la première |
| P2 | L'équipe n'a vu aucun résultat tiré de l'ensemble avant de changer d'affirmation | HYPOTHÈSE (l'énoncé est muet) | Sinon le changement est conditionné par les données, et l'ensemble est entamé pour (i) et (ii) |
| P3 | Une « loi déjà publiée » existe et s'applique à ces mesures | RAPPORTÉ pour l'existence ; loi non nommée, référence à vérifier | Sans la variable explicative, la marge d'erreur et les conditions de mesure de la loi, « s'écarter » n'est pas défini |
| P4 | L'ensemble contient des cas honnêtes appariés aux cas dégradés | HYPOTHÈSE (l'énoncé ne parle que de « cas de dégradation ») | Sans eux, aucun taux de fausses alertes, donc aucun point de fonctionnement |
| P5 | L'état interne est lisible sur les cas de l'ensemble (poids ouverts, activations enregistrées ou trajectoires rejouables) | HYPOTHÈSE | Si l'ensemble n'est que du texte produit par un agent fermé, il ne peut pas servir à (ii) |
| P6 | Les auteurs des deux détecteurs ont eu la même exposition et les mêmes degrés de liberté | HYPOTHÈSE | (ii) est une différence : une exposition inégale la biaise même si chaque niveau paraît plausible |
| P7 | « Dégradation discrète » a une vérité-terrain mécanique (tests cachés, métrique de sortie) | HYPOTHÈSE | Sinon l'étiquette dépend d'un avis |
| P8 | Un seul genre tenu à l'écart | RAPPORTÉ (« d'un genre ») | Pour la généralisation, l'unité est le genre et n = 1 : rien ne peut être dit sur « les genres non vus » en général |
| P9 | Le critère chiffré mesure une grandeur liée aux affirmations (i) et (ii) | HYPOTHÈSE | S'il date de l'ancienne affirmation, il pilote une quantité que l'équipe ne soutient plus |
| P10 | Le genre peut être ré-échantillonné | HYPOTHÈSE | Cela conditionne l'option « refaire » de la question 3 |
| P11 | L'effectif suffit à la puissance voulue | Inconnu | Une absence d'écart ou d'apport sans puissance ne vaut pas résultat |

## (b) Expériences décisives

Convention commune : l'unité de rééchantillonnage est la tâche, pas le pas. Les intervalles sont des bootstraps appariés à 95 %. Le seuil d'alerte est fixé sur des cas honnêtes de développement, jamais sur l'ensemble. Le plan d'analyse et la règle de fusion sont gelés et hachés avant ouverture.

### E1. La consultation répétée use-t-elle l'ensemble ? (questions 1 et 2)

- **Dispositif.** L'ensemble est coupé une fois, par tirage à graine publique, en S_porte et S_scellé (haché, hors d'accès). Les cycles se déroulent comme d'habitude, avec le critère de passage lu sur S_porte. S_scellé est ouvert une seule fois, au gel. Une répétition générale est possible sans toucher l'ensemble : même coupe sur un genre de développement.
- **H_A (usure).** Δ = score(S_porte) − score(S_scellé) > 3 points de détection à fausses alertes fixées (illustratif), et Δ croît avec le nombre de cycles.
- **H_B (pas d'usure).** L'intervalle de Δ tient dans ±3 points (illustratif).
- **Contrôle négatif.** Un détecteur mécanique jamais réglé doit donner Δ ≈ 0. Sinon la coupe est déséquilibrée et l'expérience est nulle.
- **Ce que chaque issue falsifie.** H_A réfute « on peut lire l'ensemble à chaque cycle sans conséquence ». H_B réfute ma propre recommandation de séparer strictement critère et ensemble, pour ce nombre de cycles. Cette seconde issue est plausible : Roelofs et al. (2019, « A Meta-Analysis of Overfitting in Machine Learning ») trouvent peu de surajustement adaptatif sur des compétitions.

### E2. L'état interne ajoute-t-il plus qu'un second détecteur de texte ? (affirmation ii)

Deux détecteurs bruités quelconques gagnent à être combinés, donc « ajoute quelque chose » est presque toujours vrai. Le duel porte sur le canal.

- **H_A.** La combinaison [texte + interne] dépasse [texte + second détecteur de texte indépendant de capacité comparable] d'au moins 5 points de détection à 5 % de fausses alertes (illustratif), intervalle excluant 0.
- **H_B.** La différence entre les deux combinaisons a un intervalle contenu dans ±5 points (illustratif). L'apport est alors un effet d'ensemble, pas un effet d'accès à l'état interne.
- **Contrôles négatifs.** Une sonde entraînée sur étiquettes permutées doit donner un gain nul (Hewitt & Liang, 2019, « Designing and Interpreting Probes with Control Tasks »). Il en va de même pour une sonde nourrie des activations d'une autre tâche.
- **Ce que chaque issue falsifie.** H_A réfute « le texte suffit ». H_B réfute l'affirmation (ii) dans sa forme non triviale.
- **Issue indécise.** Un intervalle à cheval réfute P11 : l'ensemble est trop petit pour (ii), et il faut le dire tel quel.

### E3. La sonde lit-elle la dégradation ou ce qui l'induit ? (affirmation ii, validité)

Si la dégradation est induite (consigne, réglage fin), l'état interne peut encoder l'inducteur. L'énoncé ne dit pas si elle est induite ou spontanée.

- **Cas croisés.** (a) Inducteur présent, résultat mécaniquement intact. (b) Dégradation vérifiée par tests cachés, sans inducteur (échec spontané).
- **H_A (lit la dégradation).** Le taux d'alerte sur (b) dépasse celui sur (a).
- **H_B (lit l'inducteur).** Le taux d'alerte sur (a) dépasse celui sur (b).
- **Seuil.** Écart de taux d'alerte d'au moins 20 points (illustratif) dans un sens ou dans l'autre.
- **Contrôle négatif.** Cas honnêtes sans inducteur : le taux d'alerte doit égaler le taux de fausses alertes nominal.
- **Ce que chaque issue falsifie.** H_A réfute l'objection « la sonde détecte la consigne ». H_B réfute la portée de (ii) au-delà des dégradations induites de cette manière.

### E4. Les mesures s'écartent-elles de la loi ? (affirmation i)

La loi n'est pas nommée (P3). Le plan est générique : la loi prédit ŷ = f(x) avec une incertitude publiée.

- **Préalable (contrôle positif).** La chaîne de mesure de l'équipe reproduit la loi dans les conditions de la publication. Si elle échoue, l'expérience s'arrête : un écart ne dirait rien.
- **H_A (écart).** L'intervalle de y − f(x) est entièrement hors de la marge ±m, fixée d'avance à partir de l'incertitude publiée.
- **H_B (conformité).** Un test d'équivalence place l'intervalle dans ±m (Schuirmann, 1987, « A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability »). Un simple non-rejet ne compte pas.
- **Contrôle négatif.** Permuter x entre cas doit détruire la conformité. Si elle survit, le test ne discrimine rien.
- **Ce que chaque issue falsifie.** H_A réfute « la loi s'étend à ce genre ». H_B réfute « ce genre échappe à la loi ». L'issue indécise réfute P11.
- **Limite.** Avec un seul genre (P8), l'écart vaut pour ce genre et rien de plus.

### E5. L'exposition a-t-elle gonflé les scores ? (question 3)

- **Dispositif.** Différence de différences : détecteurs modifiés après l'exposition contre détecteurs gelés avant (dates de commit), croisés avec cas exposés contre cas non exposés.
- **H_A (fuite utile).** L'interaction dépasse 3 points (illustratif).
- **H_B (fuite sans effet).** L'intervalle de l'interaction tient dans ±3 points (illustratif).
- **Contrôle négatif.** Les détecteurs gelés avant l'exposition ne doivent montrer aucune différence entre cas exposés et non exposés. Sinon les cas exposés sont simplement plus faciles.
- **Si tout l'ensemble a été vu.** Il n'y a plus de contraste interne et il faut un échantillon refait (P10). Recht et al. (2019, « Do ImageNet Classifiers Generalize to ImageNet? ») montrent qu'un ensemble refait avec soin diffère quand même en difficulté. L'écart ne se lit donc qu'ancré sur les détecteurs mécaniques, que l'exposition ne peut pas avoir touchés.
- **Ce que chaque issue falsifie.** H_A réfute « garder tel quel ». H_B réfute « jeter ».

## (c) Mesure minimale par instrument

**Cas honnêtes appariés, communs à tous les instruments.** Même tâche, même agent, même préfixe de trajectoire, même graine, avec l'issue vérifiée intacte par les tests cachés. Il faut y inclure des honnêtes difficiles : erreurs sincères corrigées, refontes légitimes volumineuses, tâches longues. Le taux de fausses alertes se joue sur ces cas, pas sur les trajectoires faciles.

**1. Détecteur de texte**
- Mesure : détection à 5 % et à 1 % de fausses alertes (illustratif). À 1 %, il faut au moins 1 000 cas honnêtes (illustratif) pour que le seuil ne repose pas sur une poignée de cas.
- Préciser quel texte il lit (sortie seule, ou aussi raisonnement et appels d'outils) : l'énoncé ne le dit pas.
- Vérifications mécaniques à battre :
  - résultat des tests visibles ;
  - taille du diff ;
  - variation de couverture ;
  - nombre d'appels d'outils et d'erreurs d'outil ;
  - longueur de trajectoire ;
  - régression logistique sur sac de mots.
- S'il ne bat pas la meilleure de ces vérifications, il ne fonctionne pas au sens utile.

**2. Détecteur d'état interne**
- Mêmes mesures, mêmes cas.
- À battre en plus :
  - une sonde sur étiquettes permutées ;
  - la même sonde sur un modèle aux poids réinitialisés ;
  - une sonde de même capacité nourrie de plongements du texte seul, pour vérifier qu'elle ne relit pas le texte par un autre chemin.
- Il doit aussi passer E3.

**3. L'ensemble tenu à l'écart**
- Détection : un détecteur oracle, qui a accès à la différence avec la sortie de référence, doit approcher 100 %.
- Fausses alertes : un détecteur à score aléatoire doit avoir une détection égale à son taux de fausses alertes.
- Artefacts : aucune vérification mécanique triviale ne doit dépasser une AUROC de 0,6 (illustratif). Sinon les cas dégradés portent une trace de fabrication.
- Étiquettes : chaque cas dégradé échoue aux tests cachés et passe les tests visibles, ce qui donne un sens mécanique à « discrète ». Chaque cas honnête passe les deux.

**4. Le critère de passage**
- Fausses alertes : probabilité qu'un détecteur sans progrès réel passe après k cycles de sélection. On la mesure en simulant k variantes nulles (rééchantillonnage de graines) et en retenant la meilleure. Elle doit rester sous 5 % (illustratif) pour le k maximal budgété.
- Détection : probabilité qu'un détecteur amélioré par construction passe. On injecte un signal oracle d'intensité connue.
- Le nombre de cycles étant non fixé, le risque d'erreur doit être dépensé sur un budget de consultations fixé d'avance (Lan & DeMets, 1983, « Discrete sequential boundaries for clinical trials »).

**5. La comparaison à la loi**
- Détection : la chaîne détecte un écart injecté de taille m dans au moins 80 % des rééchantillonnages (illustratif).
- Fausses alertes : sur la reproduction dans les conditions publiées, elle conclut à un écart dans au plus 5 % des cas (illustratif).

## (d) Ancrage matériel (tout est illustratif, rien ne vient des faits)

- **Modèles.** Lire l'état interne exige des poids ouverts. Exemples : Qwen2.5-Coder (7B, 32B), Llama 3.1 (8B, 70B), Gemma 2 (9B, 27B). Les trajectoires existantes produites par l'un de ces modèles se rejouent en passe avant seule pour extraire les activations. Produites par un agent fermé, elles tombent sous P5.
- **Tâches.** Dépôts logiciels avec tests cachés, par exemple du type SWE-bench (Jimenez et al., 2024, « SWE-bench: Can Language Models Resolve Real-World GitHub Issues? »).
- **Effectif.** Pour voir 10 points d'écart apparié avec 25 % de paires discordantes et 80 % de puissance, il faut environ 200 paires (calcul de type McNemar). Avec les coupes d'E1 et une réserve, je vise 600 paires.
- **Calcul.** 600 tâches × 2 bras × environ 40 000 jetons font environ 50 millions de jetons :
  - génération sur un modèle de 32B : 200 à 600 heures-GPU ;
  - rejeu pour les activations : 20 à 50 heures-GPU ;
  - détecteur de texte sur modèle ouvert : même ordre que le rejeu ;
  - sondes linéaires : négligeable.
- **Stockage.** Avec des activations moyennées par pas (1 200 trajectoires × 50 pas × environ 5 000 dimensions en flottants 32 bits), environ 1,2 Go par couche.
- **Coût.** 500 à 2 500 € de location de calcul. Le poste dominant est humain : construire les paires honnêtes et les tests cachés prend 2 à 4 semaines-personne.

## Réponses aux quatre questions (forme demandée par l'arbitre)

Les degrés de certitude sont subjectifs et illustratifs.

### 1. À quoi sert l'ensemble ?

**Réponse.** À la portée de ce que l'équipe affirme, et à autre chose : mesurer une fois l'écart entre score de développement et score tenu à l'écart. Il ne sert pas au critère de passage, sauf par un guichet budgété qui ne rend qu'un bit bruité par consultation.

- **Énoncé réfutable et mesure.** Un critère lu directement sur l'ensemble produit un Δ positif croissant avec les cycles : c'est E1, où H_B me donne tort. Pour (ii), l'ensemble ne sert que si P4 et P5 tiennent, ce qui se vérifie par inventaire.
- **Antériorité.** Dwork, Feldman, Hardt, Pitassi, Reingold & Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis » ; Cawley & Talbot (2010), « On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation ».
- **Contrôle sans avis.** Le journal d'accès au fichier haché : zéro lecture en dehors des consultations prévues.
- **Certitude.** 80 % pour « portée », 65 % pour « pas au critère ».

### 2. Quand le consulter ?

**Réponse.** Par parties scellées, chacune une seule fois :
- une tranche confirmatoire ouverte au gel ;
- une tranche de réserve, parce que les affirmations peuvent encore changer (elles viennent de le faire) ;
- éventuellement une tranche-guichet à budget de consultations fixé.

Comme le nombre de cycles n'est pas fixé, c'est le nombre de consultations qu'il faut fixer.

- **Énoncé réfutable et mesure.** Avec ce régime, le taux de faux passage du critère reste sous le nominal pour le budget maximal (instrument 4). Il est réfuté si la simulation nulle le dépasse.
- **Antériorité.** Armitage, McPherson & Rowe (1969), « Repeated significance tests on accumulating data » ; Blum & Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions ».
- **Contrôle sans avis.** Les hachés des tranches et du plan d'analyse sont horodatés avant ouverture. Le compteur de consultations ne dépasse pas le budget.
- **Certitude.** 70 %.

### 3. Si des auteurs l'ont vu ?

**Réponse.** Cela dépend de trois éléments nommables et vérifiables :
- **La date.** Le dernier commit du détecteur précède-t-il l'exposition ? Si oui, on garde l'ensemble.
- **L'objet.** Cas, étiquettes, scores agrégés ou simple description du genre ? Une description du genre suffit à faire perdre la propriété « genre non vu », pas la propriété « cas non vus ».
- **La symétrie.** Les auteurs des deux détecteurs ont-ils été exposés de la même façon ? C'est P6.

Si l'exposition est postérieure et porte sur les cas, la partie vue est déclassée en jeu de développement et la partie confirmatoire est refaite. Jeter n'est justifié dans aucun cas, car les cas vus restent utiles pour E5.

- **Énoncé réfutable et mesure.** L'interaction d'E5. Nulle, elle réfute le déclassement. Positive, elle réfute le maintien.
- **Antériorité.** Kaufman, Rosset, Perlich & Stitelman (2012), « Leakage in Data Mining: Formulation, Detection, and Avoidance » ; Recht, Roelofs, Schmidt & Shankar (2019), déjà cité.
- **Contrôle sans avis.** La comparaison des horodatages d'accès et des dates de commit. Le contrôle négatif d'E5 sur les détecteurs gelés avant.
- **Certitude.** 80 % pour « cela dépend », 60 % pour la règle précise.

### 4. Le changement d'affirmation modifie-t-il les réponses ?

**Réponse.** En partie.

Ce qui ne change pas : la séparation entre critère et ensemble, et la consultation unique par tranche.

Ce qui change :
- **Question 1.** L'ensemble doit porter de quoi comparer (P4, P5), et le critère de passage hérité de l'ancienne affirmation doit être réexaminé (P9).
- **Question 2.** Le plan gelé devient un test apparié de différence (E2) et un test d'équivalence (E4), plus un seuil absolu.
- **Question 3.** (i) porte sur des niveaux, donc toute exposition la biaise. (ii) porte sur une différence, donc c'est l'asymétrie d'exposition qui compte.
- **Élément décisif nouveau.** P2 : si l'équipe a changé d'affirmation après avoir vu un résultat tiré de l'ensemble, celui-ci est entamé pour (i) et (ii), même si aucun auteur de détecteur ne l'a vu.

- **Énoncé réfutable et mesure.** Aucune requête sur l'ensemble n'est antérieure à la date du document qui acte le changement. Une seule requête antérieure le réfute.
- **Antériorité.** Kerr (1998), « HARKing: Hypothesizing After the Results are Known » ; Nosek, Ebersole, DeHaven & Mellor (2018), « The preregistration revolution ».
- **Contrôle sans avis.** L'ordre des horodatages entre le journal d'accès et le document de changement.
- **Certitude.** 75 % pour « en partie ».

## Ce qui peut être réfuté dans cette proposition

Cinq duels (E1 à E5), dont deux peuvent me donner tort sur mes propres recommandations : E1-H_B et E5-H_B. Quatre suppositions (P2, P4, P5, P9) se tranchent par inventaire ou par journal, sans expérience. Rien ici n'est un résultat.

FIN-DE-CELLULE
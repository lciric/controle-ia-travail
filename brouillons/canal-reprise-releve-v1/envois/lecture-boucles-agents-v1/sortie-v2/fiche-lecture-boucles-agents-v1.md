# Synthèse — lecture « boucles d'agents : proposer, tester, éliminer, itérer » (v1, écrite pendant la passe du brief v2)

Rédaction achevée le 26 octobre 2026 à 04:02 UTC ; dernière retouche le 26 octobre 2026 à 04:04 UTC (heures lues sur `date -u`). Dossier : `/var/tmp/lecture-boucles-agents-v2/`.

**Portée de cette synthèse.** Onze PDF de la liste v1 ont été retéléchargés (tous à la même empreinte qu'en v1) et lus, plus un ajout (les informations supplémentaires de FunSearch). Les treize PDF arXiv restants n'ont pas été retéléchargés : consigne du coordinateur à 03:45 UTC, plus aucune requête vers arXiv. Tous les systèmes de boucles d'agents récents (The AI Scientist et sa v2, AlphaEvolve, Darwin Gödel Machine, Automated Design of Agentic Systems, STOP, Agent Laboratory, AI co-scientist et les ajouts de la v1) sont donc **non lus** dans cette passe. Tout ce qui les concerne ci-dessous est marqué « à vérifier ». Les leçons portent surtout sur le bruit et l'analyse adaptative, plus deux systèmes de boucle (FunSearch, le robot Adam).

Conventions : « p. N » désigne le rang de la page dans le PDF empreinté de la fiche citée, à partir de 1 ; « illustratif » marque tout ordre de grandeur de mon cru ; « STOC » et « NIPS » désignent les fiches `reusable-holdout-stoc` et `reusable-holdout-nips`, noms courts hérités de la v1 d'après le Symposium on Theory of Computing et la conférence Neural Information Processing Systems. Contexte du brief v2, pris comme fait et non rejugé : lecture du quatrième pilote fixée (intervalle de Wilson par classe ; test apparié génération 0 contre génération 3 ; correction de Holm) ; registre d'hypothèses écrit avant tout score ; verdicts d'agents neufs qui ne voient que la sortie d'un script de lecture ; primitive intérieure dessinée par une autre lignée.

## (a) Tableau des papiers

| Nom court (fiche) | Référence | Type de boucle | Traitement du bruit | Lu sur PDF |
|---|---|---|---|---|
| `reusable-holdout-stoc` | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, « Preserving Statistical Validity in Adaptive Data Analysis », arXiv 1411.2664v3 ; version préliminaire au Symposium on Theory of Computing 2015 | théorie de l'analyste adaptatif (requêtes choisies au vu des réponses) | confidentialité différentielle donc généralisation ; bruit ajouté aux réponses ; part fraîche par tour d'adaptativité | oui (p. 1–8, 17–21, 23–26) |
| `reusable-holdout-nips` | mêmes auteurs, « Generalization in Adaptive Data Analysis and Holdout Reuse », arXiv 1506.02629v2 ; lieu à vérifier | analyste avec accès libre à l'entraînement, validation par une porte | « Thresholdout » (seuil bruité, budget de dépassements), « SparseValidate » ; expérience nulle, 100 exécutions | oui (p. 1–5, 15–23) |
| — | « The reusable holdout », Science 349, 2015, cité p. 22 du PDF STOC | — | — | non (hors liste v1, non téléchargé) |
| `ladder` | Blum, Hardt, « The Ladder », arXiv 1502.04585v1 ; lieu à vérifier | concours avec tableau de classement public | publication seulement des améliorations nettes, arrondies ; test t apparié ; attaque par boosting ; Bonferroni sur données réelles | oui (p. 1–15) |
| `garden-forking-paths` | Gelman, Loken, manuscrit du 14 novembre 2013 | analyse du chercheur dépendante des données | préenregistrement, réplication confirmatoire, modèle multiniveau | oui (p. 1–15) |
| `preregistration-revolution` | Nosek, Ebersole, DeHaven, Mellor, prépublication OSF de 2017 ; publication de 2018 à vérifier | cycle postdiction puis prédiction | préenregistrement, part scellée, arbre de décision, rapport de toutes les issues, Bonferroni | oui (p. 1–15) |
| `rl-precipice` | Agarwal, Schwarzer, Castro, Courville, Bellemare, conférence Neural Information Processing Systems 2021, arXiv 2108.13264v4 | comparaisons d'algorithmes à peu de courses | bootstrap stratifié, profils de performance, moyenne interquartile, probabilité d'amélioration | oui (p. 1–11, 18, 25) |
| `variance-benchmarks` | Bouthillier et al., arXiv 2103.03098v1 ; Machine Learning and Systems 2021 à vérifier | comparaison de deux chaînes d'apprentissage | décomposition des sources de variance ; P(A>B) avec seuil 0,75 ; appariement ; découpages multiples | oui (p. 1–11, 14–17) |
| `how-many-seeds` | Colas, Sigaud, Oudeyer, arXiv 1806.08295v2 ; lieu à vérifier | comparaison de deux algorithmes | test de Welch, bootstrap, analyse de puissance, essais « A contre A », Bonferroni | oui (p. 1–20) |
| `ajout-roelofs-meta-analyse-surajustement` | Roelofs, Fridovich-Keil, Miller, Shankar, Hardt, Recht, Schmidt, conférence Neural Information Processing Systems 2019 | concurrents Kaggle : part publique réutilisée, part privée rendue une fois | écart public/privé, intervalles de Clopper-Pearson, modèle nul de découpage | oui (p. 1–9) |
| `funsearch` | Romera-Paredes et al., Nature 625, 468–475, 2024 | évolution de programmes : un modèle de langue propose, un évaluateur note, une base en îles sélectionne | évaluation exacte ; entraînement/validation/test pour l'empaquetage ; courses répétées (4 sur 140 ; 10 sur 10) ; 5 graines pour les ablations | oui (p. 1–10 ; suppl. p. 1–8, 29) |
| `robot-scientist-adam` | King et al., « The Automation of Science », prépublication des auteurs ; Science 324, 2009, à vérifier | robot de laboratoire : abduction d'hypothèses, expériences, analyse, nouveau cycle | test de permutation sur réplicats ; P < 0,05 pour 12 hypothèses sur 20 ; confirmation in vitro hors boucle ; témoins positifs | oui (p. 1–12) |
| `ai-scientist-v1` | « The AI Scientist », arXiv 2408.06292v3 selon la liste v1 | à vérifier | à vérifier | non (PDF à retélécharger) ; la fiche de l'agent interrompu n'a jamais été relue |
| `ai-scientist-v2` | sa v2, arXiv 2504.08066v1 selon la liste v1 | à vérifier | à vérifier | non |
| `alphaevolve` | « AlphaEvolve », arXiv 2506.13131v1 selon la liste v1 | à vérifier | à vérifier | non |
| `darwin-godel-machine` | « Darwin Gödel Machine », arXiv 2505.22954v3 selon la liste v1 | à vérifier | à vérifier | non |
| `adas` | « Automated Design of Agentic Systems », arXiv 2408.08435v2 selon la liste v1 | à vérifier | à vérifier | non |
| `stop` | « Self-Taught Optimizer (STOP) », arXiv 2310.02304v3 selon la liste v1 | à vérifier | à vérifier | non |
| `agent-laboratory` | « Agent Laboratory », arXiv 2501.04227v2 selon la liste v1 | à vérifier | à vérifier | non |
| `co-scientist` | « AI co-scientist », arXiv 2502.18864v2 selon la liste v1 | à vérifier | à vérifier | non |
| `ajout-aide`, `ajout-aira-mle-bench`, `ajout-beel-critique-ai-scientist`, `ajout-shinkaevolve`, `ajout-sica` | ajouts de la v1 : arXiv 2502.13138v1, 2507.02554v2, 2502.14297v3, 2509.19349v1, 2504.15228v2 ; titres exacts à vérifier | à vérifier | à vérifier | non |

## (b) Ce que cette littérature apprend quand les tests sont bruités et le jeu de test réutilisé

1. **Réutiliser une part de test de façon adaptative casse l'estimation naïve, et vite.** Un seul tour d'adaptativité suffit en principe (STOC p. 3). Sur des données sans aucun signal, une sélection vérifiée sur la part réutilisée affiche plus de 63 % d'exactitude là où rien ne dépasse 50 % (NIPS p. 21). Nos organismes, qui se réécrivent à partir du score rendu sur `test`, sont des analystes adaptatifs. La boucle extérieure, qui lit ces scores pour proposer la ronde suivante, ajoute une seconde couche d'adaptativité.
2. **La sélection seule fait monter un score réutilisé.** L'attaque par boosting garde les soumissions aléatoires qui passent au-dessus du hasard et améliore le score public sans aucune compétence (Ladder p. 10 et 11). Une population qui retient les variantes « meilleures sur `test` » fait mécaniquement la même chose.
3. **Il existe des mécanismes qui bornent la fuite d'information** : ne rendre qu'un bit tant que la part réservée confirme, sinon une valeur bruitée, sous budget (« Thresholdout », NIPS p. 15 et 16) ; ne publier un score que s'il bat le meilleur d'un pas fixé, et l'arrondir (Ladder p. 6 et 10) ; ne poser que des questions oui/non sous budget (« SparseValidate », NIPS p. 19) ; prendre une part fraîche à chaque tour d'adaptativité (STOC p. 19 et 20).
4. **Le constat rassurant suppose de grands jeux de test.** Sur 120 concours Kaggle, peu de sur-ajustement adaptatif (Roelofs p. 2). Mais les exceptions sont les petits jeux de test (90, 100, 209 exemples, p. 5 et 7), et le minimum indicatif proposé est de 10 000 exemples (p. 7). Avec 36 tâches, notre part `test` est dans le régime des exceptions (illustratif).
5. **À petit n, le bruit d'échantillonnage du test domine, et la variance entre graines se mesure.** Le bruit du jeu de test suit un modèle binomial (Bouthillier p. 4) : l'erreur type de 0,07 du brief en est un cas, √(0,75 × 0,25 / 36) ≈ 0,072. Pour deux générations comparées sans appariement, l'erreur type de la différence vaut environ 0,10, et une différence d'environ 0,29 serait détectable à 5 % avec 80 % de puissance (illustratif) ; l'appariement réduit ce seuil selon la corrélation. Une course de chaque côté donne environ 10 % de faux positifs et 75 % de faux négatifs (Bouthillier p. 9). Avec moins de 10 courses, le taux réel de faux positifs dépasse le taux nominal (Colas p. 16). Il faut une étude pilote d'au moins 20 courses pour estimer la variance entre graines (Colas p. 19). Les intervalles par bootstrap stratifié couvrent bien à partir de 10 courses et sous-couvrent à 3 (Agarwal p. 6).
6. **Les critères de décision doivent être fixés d'avance et porter sur un effet qui compte.** P(A>B) assorti d'un intervalle, avec borne basse au-dessus de 0,5 et borne haute au-dessus de γ = 0,75 ; 29 courses appariées suffisent pour γ = 0,75 (Bouthillier p. 9 et 16). Pas d'amélioration annoncée sous un pas η (Ladder p. 6). Les tests appariés gagnent en puissance (Bouthillier p. 15 ; Ladder p. 10). Les comparaisons multiples se corrigent (Colas p. 5 ; Ladder p. 14). La lecture fixée du quatrième pilote (test apparié, correction de Holm) appartient à ces mêmes familles ; elle n'est pas rejugée ici.
7. **La multiplicité cachée vient des choix faits après avoir vu les données, même sans pêche** (Gelman p. 2 et 6). Les remèdes sont procéduraux : préenregistrement, arbre de décision ou procédure standard, rapport de toutes les issues, part scellée jusqu'à la fin de l'exploration (Nosek p. 7 et 10), et deux temps, exploratoire puis confirmatoire (Gelman p. 13 à 15).
8. **Les deux systèmes de boucle lus séparent les rôles.** FunSearch fait évoluer sur une part d'entraînement, choisit sur une part de validation et rapporte sur une part de test (suppl. p. 29). Il compte les réussites sur plusieurs courses (suppl. p. 6 et 7). Le meilleur de plusieurs courses n'est revendiqué explicitement que pour des objets mathématiques vérifiables (p. 4 et 9) ; pour l'empaquetage, la distribution de 10 courses est donnée en annexe (suppl. p. 7). Adam teste par permutation des réplicats (p. 7), fait confirmer ses conclusions hors de la boucle par une autre méthode et s'appuie sur des témoins positifs (p. 3).

**Ce que cette littérature ne règle pas :**
- **Aucune garantie à n = 36.** Les constantes théoriques demandent des centaines de milliers de points pour une tolérance de 0,1 (STOC p. 20, illustratif). La borne de « Ladder » en (log(kn))^(1/3)/n^(1/3) vaut, pour n = 36 et k = 10, de l'ordre de 0,5 à une constante près (illustratif) : elle est vide.
- **Une seule couche d'adaptativité.** La théorie lue suppose un analyste unique et des échantillons indépendants et identiquement distribués. Chez nous, l'adaptativité s'emboîte : organismes au sein d'une course, boucle extérieure entre les courses, concepteurs entre les pilotes. Parmi les textes lus, seul Nosek effleure ce point, par la question « Who has observed the data? » (p. 8).
- **Le constat empirique rassurant ne se transpose pas** aux petits jeux de test (Roelofs p. 7), ni, faute de lecture, à des optimiseurs automatiques qui soumettent bien plus de variantes qu'un humain.
- **Le bruit du modèle servi par une interface de programmation**, qui écrit le code des organismes, sort du cadre de Bouthillier (p. 10).
- **Désaccord sur les tests dichotomiques** : Agarwal et al. les déconseillent (p. 4) ; Colas et al. recommandent un test de Welch corrigé (p. 19) ; Bouthillier et al. combinent signification et importance (p. 8 et 9).
- **Les systèmes de boucles récents ne sont pas lus.** Rien ne dit ici comment ils traitent l'écart entre validation et test, ni leurs propres réutilisations de jeux d'évaluation (à vérifier).

## (c) Ce qu'il faudrait emprunter et ce qu'il faudrait éviter

**Boucle extérieure — emprunter**
- **Registre et script de lecture figés d'avance.** Le registre écrit avant tout score est un préenregistrement. Y joindre l'arbre de décision du script de lecture, rapporter toutes les issues (nulles comprises) et consigner chaque écart (Nosek p. 7 et 10).
- **Questions fermées, sous budget.** Les agents neufs ne posent à la part réservée que des questions fermées écrites d'avance, sous budget (« SparseValidate », NIPS p. 19). Cela recoupe le protocole déjà décidé (non rejugé).
- **Amélioration déclarée au-dessus d'un pas fixé.** Une conception n'est déclarée meilleure que si elle bat la meilleure courante d'un pas fixé d'avance, par comparaison appariée ; sinon on garde l'ancienne (Ladder p. 6 et 10). P(A>B) avec intervalle sert de critère (Bouthillier p. 9).
- **Écart rendu contre non rendu.** Mesurer à chaque génération l'écart entre `test` (rendu) et `test_final` (jamais rendu), avec intervalles exacts et un modèle nul de découpage aléatoire : c'est le diagnostic direct du sur-ajustement adaptatif (Roelofs p. 4 et 6).
- **Calibrer le script de lecture.** Le faire tourner sur des comparaisons « A contre A » (Colas p. 15) et sur une expérience nulle sans signal (NIPS p. 21) avant de lui faire confiance.
- **Compter les tours d'adaptativité** et prévoir une part fraîche par tour quand c'est possible (STOC p. 19 et 20).
- **Confirmer hors de la boucle.** Les conclusions se confirment par une méthode distincte (Adam p. 3) et sur `test_final`, lu une seule fois.

**Boucle extérieure — éviter**
- Estimations ponctuelles, et meilleur de n courses pour une statistique bruitée (Agarwal p. 5 ; FunSearch p. 4 et 9).
- Tout choix d'analyse fait après avoir vu les scores (Gelman p. 2).
- Laisser le résultat de `test_final` orienter la ronde suivante : il deviendrait une part publique (Nosek p. 10 ; Ladder p. 2).
- Changer de protocole d'évaluation d'une génération à l'autre (Agarwal p. 5).

**Boucle intérieure — emprunter**
- **Parts séparées.** Les expériences de l'organisme tournent sur une part qui n'est ni `test` ni `test_final` (FunSearch, suppl. p. 29). Tout accès à une part réservée passe par une porte qui rend un bit ou une valeur bruitée, avec un budget de désaccords (« Thresholdout », NIPS p. 15 et 16).
- **Retours grossis.** Les résultats rendus sont arrondis et ne paraissent qu'en cas d'amélioration nette (Ladder p. 6).
- **Comparaisons appariées tâche par tâche**, par signature de résultats (FunSearch p. 9 ; Bouthillier p. 15), et test de permutation sur réplicats (Adam p. 7).
- **Aléa sur ce qui n'est pas testé.** Rendre aléatoire tout ce qui n'est pas en test : graines, ordre des tâches, découpages (Bouthillier p. 9).
- **Journal complet.** Journaliser tous les tests internes, pas seulement les gagnants (Nosek p. 10 ; Adam p. 4), et glisser des témoins positifs connus (Adam p. 3).

**Boucle intérieure — éviter**
- Conclure sur moins de 10 courses par variante (Colas p. 16 ; Agarwal p. 6).
- Rendre à répétition le score brut de `test` (STOC p. 3 ; Ladder p. 10 et 11).
- Présenter comme un gain la sélection du meilleur de n variantes (NIPS p. 21 ; Ladder p. 10 et 11).

## (d) Antériorité — ce qui est occupé, ce qui ne l'est pas à ma connaissance (à vérifier)

Le programme ne revendiquera jamais « premier à faire des agents qui se réécrivent ». Ce qui suit n'est pas une revendication de primauté.

**Occupé, d'après les PDF lus**
- **Mécanismes de réutilisation contrôlée d'une part de test** sous analyse adaptative (2014–2015 : STOC, NIPS) et pour les tableaux de classement (Ladder, 2015).
- **Étude empirique du sur-ajustement adaptatif** dans les concours. Roelofs et al. revendiquent la « first large meta-analysis » (p. 1) ; c'est leur revendication.
- **Méthodologie statistique des comparaisons à peu de courses** (Colas 2018 ; Agarwal 2021 ; Bouthillier 2021), du préenregistrement (Nosek) et du jardin aux sentiers qui bifurquent (Gelman et Loken 2013).
- **Découverte automatique en boucle fermée.**
  - Le robot Adam (2009) annonce « the automation of the discovery of novel scientific knowledge » (p. 1).
  - FunSearch (2023–2024) couple un modèle de langue et un évaluateur dans une recherche évolutive de programmes, avec des résultats nouveaux sur des problèmes ouverts (p. 1 et 2).
  - FunSearch attribue la première boucle d'auto-amélioration « modèle de langue + score programmatique » à Lehman et al. (2023) (p. 9) ; attribution non vérifiée.
- **Agents qui réécrivent leur propre code, recherche automatique de systèmes d'agents, rédaction automatique d'articles de recherche** : c'est le sujet affiché des treize papiers non relus (Darwin Gödel Machine, Automated Design of Agentic Systems, STOP, AlphaEvolve, The AI Scientist et sa v2, Agent Laboratory, AI co-scientist, et les ajouts de la v1). Zone tenue pour occupée par défaut ; contenu et revendications à vérifier.

**Non trouvé dans les onze lectures de cette passe** (à vérifier, d'abord contre les treize papiers non relus, puis par une recherche dédiée)
- Un mécanisme de type « Ladder » ou « Thresholdout » appliqué au score rendu à des programmes qui se réécrivent d'une génération à l'autre.
- La mesure préenregistrée de l'écart entre une part rendue et une part jamais rendue, dans une population de programmes qui se réécrivent. Roelofs le fait pour des concours humains ; FunSearch sépare validation et test sans rapporter l'écart comme diagnostic, dans les pages lues.
- Une primitive d'expérience bornée et budgétée, à l'intérieur d'un noyau isolé, pour l'auto-test d'un organisme.
- Le domaine de tâches : distinguer évaluation et usage réel, trace honnête et trace sabotée. Il est hors du champ de ce corpus ; l'absence de travaux ici ne dit rien de l'état du domaine (règle anti-faux-gap).

## (e) Questions que ces lectures laissent ouvertes pour nos deux boucles

1. Combien d'information le score rendu sur `test` fait-il fuir à chaque génération, et après combien de générations la part `test` est-elle « usée » ? La théorie lue ne donne pas de réponse à n = 36.
2. L'écart `test` − `test_final` grandit-il avec les générations ? Quelle est sa distribution nulle pour 36 tâches sous découpage aléatoire (Roelofs p. 6) ?
3. Quelle est la variance d'un organisme d'une graine à l'autre ? Le brief la dit inconnue ; il faudrait une étude pilote d'au moins 20 courses (Colas p. 19), avec un budget à proposer.
4. Rendre aux organismes un score « en échelle » (arrondi, seulement les améliorations nettes) freinerait-il leurs vrais progrès ? C'est la question laissée ouverte par Blum et Hardt (p. 15).
5. Combien de tours d'adaptativité le programme a-t-il déjà accumulés sur les mêmes tâches, entre pilotes, concepteurs et lignées qui ont vu des scores ? « Who has observed the data? » (Nosek p. 8).
6. Quel effet minimal compte comme « valeur au-delà du bruit » (pas η, seuil γ), fixé avant tout score ? Combien de courses appariées faut-il pour le détecter (Bouthillier p. 16) ?
7. Sur quelles données l'organisme expérimente-t-il dans la course ? Si c'est `test`, la primitive est un analyste adaptatif de plus sur la part réutilisée ; sinon, quelle taille donner à sa part propre ?
8. Comment agréger les verdicts par classe et par génération sans perdre le contrôle des comparaisons multiples (Colas p. 5 ; Bouthillier p. 10) ?
9. Faut-il glisser dans le registre extérieur des témoins connus — un changement neutre, un changement connu pour aider — pour estimer les taux d'erreur de la boucle (Adam p. 3 ; Colas p. 15) ?
10. Que disent les treize systèmes non relus de la séparation validation/test, des graines et des réutilisations de jeux d'évaluation ? À relire dès que l'accès à arXiv est rétabli.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat — réflexion de fond sur la prédiction P3 de la ligne 3 (agrégation étalonnée de cinq juges) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la demande de Lazar dans cette session (« faudrait il changer la regle pour faire P3 ? brainstorme dessus avec fable effort extra »), reformulée par la session et donnée telle quelle ci-dessous. **Tu proposes, tu ne décides rien** : changer la règle de P3 est un écart à un préenregistrement scellé, donc un nœud de Lazar.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni le préenregistrement de la ligne 3, ni ses additifs, ni le code, ni le verdict, ni sa contre-lecture. Tu signes « rédacteur neuf, modèle F ».

## Règle d'aveugle (la plus importante)

**Tu ne lis aucune mesure de l'étage 1** : ni `resultat-etage-1-ligne-3-v3.json`, ni le verdict (v1, v2), ni sa contre-lecture, ni `lecture-predictions-etage-1-v1.json`, ni aucun fichier des dossiers `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/` et `…/ligne-3-votes-effectifs-juges/verdict-etage-1-v1/`. Raison : une règle de P3 dessinée par quelqu'un qui a vu les mesures ne serait plus un préenregistrement (R1, R3). Ce que tu sais de l'étage 1 se réduit à ceci : son verdict est « non, pas à cette taille » ; P3 n'a pas été lue, parce que sa clause ne nomme ni l'agrégation étalonnée visée (bras C ou bras P), ni sa référence (« majorité fixe » : majorité stricte ou poids égaux), ni les profils qui comptent pour « échangeables ».

## Ce qui fait foi (tire de main par `fetch` puis `git show` redirigé vers ton dossier ; vérifie chaque empreinte)

- PR : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`), en entier ; P3 est à la ligne 135, les bras à cinq juges et l'étalonnage dans le § des bras.
- A1 (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`) et A2 (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`), mêmes dossiers, en entier.
- Les versions antérieures du préenregistrement (v1 à v6) et leurs contre-lectures, sous `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` (ouvre chaque fichier par son chemin, tiré du tableau des versions du PR ; aucune liste) : elles disent ce que l'auteur visait par « agrégation étalonnée » et « majorité fixe » **avant** toute mesure.
- Le code du banc, `…/ligne-3-votes-effectifs-juges/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0`) : lis-le pour savoir quels bras à cinq juges il calcule et ce qu'il enregistre par réplique. **Tu ne le lances pas.**

## La demande, reformulée

Dis à Lazar, avec preuves écrites, s'il vaut la peine de changer la règle de P3 pour pouvoir la trancher, et comment le faire sans tricher avec des données déjà vues. Concrètement :

1. **Ce que P3 veut dire, d'après les seuls textes d'avant mesure.** Pour chacun des trois trous (agrégation visée ; référence « majorité fixe » ; sens d'« échangeables »), relève ce que disent les versions v1 à v7, les contre-lectures et le code. Classe chaque trou : (a) le texte d'avant mesure le tranche déjà (P3 est lisible telle quelle, et l'on s'est trop retenu) ; (b) plusieurs lectures restent admissibles ; (c) aucune lecture n'est écrite. Cite chemin, ligne, empreinte.
2. **Ce que P3 apporte au programme.** Que décide-t-elle, ou non : la taille de l'étage 2, la composition des juges de l'organisme, une revendication ? Si elle ne décide rien, dis-le : la bonne réponse peut être « ne pas changer la règle, rapporter P3 comme non lue ».
3. **Ce que la théorie dit d'avance, par calcul exact là où c'est possible** (sans tirage ; tu peux écrire un programme de calcul exact sur les lois du banc, comme `calcul_predictions_ligne_3_v1.py`, sans lire de mesure). Pour des juges i.i.d. symétriques, la majorité est la règle optimale (Condorcet ; Nitzan et Paroush 1982 pour les poids en log-rapport) : un étalonnage ne peut qu'égaler ou perdre par l'erreur d'estimation des poids. Pour des juges en blocs corrélés, le gain dépend de la structure (Ladha 1992 ; Dawid et Skene 1979 pour l'estimation des taux par juge). **Aucun chiffre de la littérature n'est opposable sans PDF empreinté et page citée (R7)** : nomme-les comme pistes, marque-les « non vérifiés ».
4. **Les options, chacune avec son avantage et son inconvénient** :
   - (A) ne rien changer : P3 rapportée « non lue », avec sa raison ;
   - (B) une lecture multiple déclarée : toutes les lectures admissibles du point 1, rapportées ensemble comme descriptives, sans mot ;
   - (C) une règle neuve de P3, écrite et scellée maintenant, jouée sur **des graines neuves** (une racine neuve, dérivée par `SeedSequence`, jamais 2026111932 ni 2026111933), à l'aveugle des mesures de l'étage 1, avec : l'agrégation et la référence nommées, la définition d'« échangeables », un test d'équivalence pour « jeu égal » (deux tests unilatéraux, marge écrite), une comparaison appariée par réplique sur les mêmes tirages, la correction de multiplicité, une puissance calculée d'avance aux tailles d'étalonnage 25, 100 et 200 ;
   - toute autre option que tu juges meilleure.
5. **Ce qui permettrait de vérifier le résultat hors de nous** : une réimplémentation indépendante, par une autre lignée, à partir du seul texte ; le cas échangeable comparé au résultat théorique connu ; les graines neuves scellées avant tout lancement ; ce qui resterait non vérifiable sur un banc scripté (les vrais juges ne sont lus qu'à l'étage 2).
6. **Recommandation et confiance**, au format : décision en une phrase ; enjeu ; options ; recommandation et confiance ; défaut proposé sous 48 heures ou « sans défaut » si c'est un nœud.

Rends `reflexion-p3-ligne-3-v1.md` (dense, pas long), tout programme de calcul exact avec sa sortie, et un rapport court. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/reflexion-p3-ligne-3-v1/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune recherche sur la toile. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

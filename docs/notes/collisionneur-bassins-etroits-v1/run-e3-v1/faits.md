# Faits pour le collisionneur : pousser l'organisme d'idéation vers les bassins d'idées étroits et profonds — v1

Résumé écrit le 13 novembre 2026 (début à 12:43 UTC, heure relevée par `date -u`) par un opérateur neuf de la session mère
(Claude Opus 5.5), qui n'a écrit ni les pièces résumées, ni le collisionneur. Sources (empreintes vérifiées) :
[F12] `docs/notes/collisionneur-diversite-idees-v1/faits-v1.md` (`01f9e759…`) ; [S1] `…/collisionneur-diversite-idees-v1/synthese-v1.md`
(`4f99077b…`) ; [C3] `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v3.md` (`386d48ba…`),
§3.1 à §3.4, §4.1, §4.3, §5.1, §5.2 seulement ; [C4] `…/conception-monde-riche-doublons-v4.md` (`47e38ec0…`), en-tête, §1,
§2.1 seulement ; [B] `docs/sources/web-bespoke-how-models-explore-ideas-20261113/texte.txt` (`b1d32227…`).

**Filtre volontaire.** Aucune loi plantée, aucune graine, aucun paramètre de monde, aucun chiffre de simulation, aucun texte de
proposition, aucun score de course. Le collisionneur conseille ; il n'est ni proposeur ni juge, et ne voit pas ce qu'un
proposeur ne voit pas.

**Statuts.** VÉRIFIÉ : relu par l'opérateur dans la source citée. RAPPORTÉ : dit par la source, non revérifié.
OBSERVÉ-NON-AUDITÉ : observation non contre-lue. HYPOTHÈSE : supposition.

## 1. L'organisme d'idéation (RAPPORTÉ, [F12] §1)

- Un **monde planté** : une loi de probabilité cachée des issues d'un épisode sachant des traits publics ; sa loi est connue
  de l'expérimentateur humain (l'oracle), jamais des proposeurs.
- Des **proposeurs** (modèles de langue) rendent des **cartes** : une loi prédictive au gabarit fermé, dans une grammaire
  publique de six formes (`fixe`, `softmax`, `par_sous_population`, `melange`, `si_sinon`, `transformee`). Ils reçoivent une
  **vue** : description publique du monde, grammaire, lois de l'archive ; **jamais** un verdict, l'oracle, une loi plantée.
- Un **gardien** mécanique (grammaire, bornes), puis un **juge statistique** calculé par l'orchestrateur, sur engagement
  scellé : valeur e de chaque carte sur des tirages frais contre un **nul** qui contient les lois de l'archive, des lois
  aveugles fixes et une classe de recombinaisons de ces lois ; règle de Benjamini et Hochberg sur les valeurs e (e-BH).
  Une carte qui n'apporte rien au-delà de l'archive et de ses recombinaisons n'est pas promue : **garde contre les copies**.
- **Limite connue du juge** : il tient dans la classe que son nul couvre et **cède hors d'elle** (recombinaisons par
  morceaux, produits, compositions de lois connues).
- Un **test de mort** sur épisodes frais, puis **sélection** : les retenues entrent dans l'archive de la génération suivante.

## 2. Ce que la course v67 a donné (RAPPORTÉ, [F12] §2, en raccourci)

- Génération 1 : onze cartes promues et retenues, **variantes proches d'un même constat** (ajouter un trait que la loi
  connue de départ ignorait) ; « ce ne sont pas 11 idées ».
- Génération 2 : **aucune promotion** ; la garde contre les copies a refusé des copies renommées plantées.

## 3. Premier tour du collisionneur sur la diversité (OBSERVÉ-NON-AUDITÉ : synthèse non contre-lue, [S1])

- **Convergence** : d'abord un banc de métrologie hors ligne, sans appel de proposeur (mondes certifiés, mesure, garde).
- **Rejets convergents** : aucune **récompense numérique de la nouveauté**, ni dans le juge, ni servie à un agent ; aucun
  **quota de formes** grammaticales (forme ≠ idée) ; aucun **masquage d'une partie de l'archive** ; jamais le **représentant
  d'un groupe choisi par la plus grande valeur e** sur les tirages du juge (fatal à la garantie E[e] ≤ 1).
- **Danger commun** : toute pression vers la variété pousse vers `si_sinon` et `melange`, c'est-à-dire vers **la classe que le
  nul ne couvre pas** ; la garde doit être certifiée en absolu avant toute comparaison entre bras.
- **Mesure de diversité retenue** : principale, par l'oracle, **nombre de composantes plantées couvertes** (certifiées
  détectables, additionnelles à l'archive) ; secondaire, sans oracle, descriptive, **nombre de groupes prédictifs**.
- **Borne de dilution** : une distance moyenne globale entre lois **efface une différence confinée à une région rare** des
  traits (borne d ≤ r(A)·ln 2, r(A) la masse de la région) ; d'où une lecture par strates.

## 4. Conception en cours de la course à plusieurs générations (RAPPORTÉ)

- **Regroupement des doublons** ([C3] §3.1 à §3.4) : deux cartes d'une génération sont doublons si leurs formes canoniques
  sont égales ou si chacune est presque dans le nul engendré par l'autre (distance en nats par instance, sous un seuil ε,
  sur un jeu public d'instances **sans issue**, plus une lecture par strates publiques) ; groupes par liaison complète,
  calculés par un programme de l'orchestrateur, jamais par un modèle. La valeur e d'un groupe est la moyenne des valeurs e
  de ses membres ; e-BH sur les groupes, m fixé d'avance par règle écrite. Un **représentant** par groupe, choisi par
  couverture dirigée puis par une tranche de choix appariée, **jamais** sur les tirages du juge ni l'oracle ; seul il passe
  le test de mort ; les sœurs ne sont jamais servies. La preuve de validité porte sur H₀ « le monde est dans la classe du
  nul de l'archive » et **ne borne pas** la part des fausses découvertes au sens de l'oracle.
- **Diversité** ([C3] §4.1, §4.3) : D1, sans oracle, descriptive (groupes, nombre effectif de Hellinger, signatures de
  traits) ; D2, principale, par l'oracle, lue une fois après la course (composantes certifiées couvertes, à trois étages :
  propositions brutes, représentants, retenues). **Ce qu'elle ne doit pas piloter** : la composition des proposeurs, la
  sélection (aucune prime de nouveauté), les consignes des proposeurs pendant la course, le nombre de générations. Une course
  qui voudrait **agir** sur la diversité est un dessin neuf.
- **Proposeurs** ([C3] §5.1, §5.2) : Claude (Fable, Opus), Argon, Astra, Kimi si son compte le permet ; **six cartes par
  proposeur et par génération**, un appel par proposeur et par génération ; **chaque appel en session neuve sans
  historique** ; réponse brute scellée avant extraction ; aucun juge d'idées à modèle.
- **Monde** ([C4] en-tête, §1, §2.1) : écrit **par un programme à graine scellée** ; aucune famille de modèles n'en est
  l'auteur. Constat de la v4 : dans la famille précédente, chaque composante se voyait seule ; rien n'ordonnait les
  découvertes. Ajout d'une **composante conditionnelle** : l'effet d'un trait dont le **signe dépend du signe d'un autre
  trait** ; **nul en moyenne** sur cet autre trait, donc presque invisible à une loi sans condition ; **trouvable une fois sa
  condition archivée** (pente nette dans chaque branche) ; une seconde peut dépendre de la première (**chaîne de profondeur
  2**). Que de vrais proposeurs la trouvent après sa condition est une **HYPOTHÈSE** qu'un pilote mesurera.

## 5. Une observation extérieure sur les bassins d'idées (RAPPORTÉ, [B], observationnel, non reproduit par nous)

Page publique de Bespoke Labs, « How models explore ideas » (10 novembre 2026), sur des tâches longues de recherche en
apprentissage automatique ; chiffres vérifiés par l'opérateur sur `texte.txt` :
- **348 courses** de **24 heures**, **12 modèles** ;
- **bassin d'idées** : groupe de soumissions à une même tâche qui partagent une méthode de fond ;
- **47 %** des courses ne quittent jamais leur premier bassin ;
- un passage à un bassin neuf est suivi d'environ **neuf fois** le gain d'un pas de raffinement, presque tout dans les
  **six premières heures** ;
- **58 %** des courses n'atteignent jamais le bassin où la meilleure solution de leur tâche a été trouvée ;
- le volume de soumissions suit le surajustement (**ρ = 0,84**, Spearman) ;
- remède cité par la page, **non éprouvé par elle** : remettre périodiquement le contexte de l'agent à zéro et repartir du
  meilleur résultat obtenu ; deux articles cités, **non lus par nous** : « Fork-and-Flush: Escaping Idea Basins in
  Autoresearch Agents » et « Scaling Discovery Requires Forgetting ».

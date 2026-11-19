# Fiche de lecture — Xu (2026), le harnais multi-tâches que l'agent fait évoluer lui-même, avec notes libres et rejeu — v1

## En-tête

- **Papier** : Qiankai Xu, auteur unique (« Independent Researcher », p. 1), arXiv 2609.38372. Identifiant pris dans la bibliographie de Yu et al. (arXiv 2611.18856v1, p. 13).
- **Titre** : la bibliographie de Yu et al. donne « Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer ». D'après l'interface publique d'arXiv (relevé du 19 novembre 2026), c'est le titre de la version 1 (29 septembre 2026). La version 2, lue ici, s'intitule « Multi-Task Self-Evolving Harnesses with the Agent as Its Own Optimizer » (p. 1). Même identifiant, même auteur : c'est le même papier.
- **Version lue** : version 2 du 12 novembre 2026 (« arXiv:2609.38372v2 [cs.AI] 12 Nov 2026 », p. 1). **Réserve** : la version 1 n'a pas été lue ; Yu et al. (13 novembre 2026) ont pu lire l'une ou l'autre.
- **Fichier** : `docs/sources/arxiv-2609.38372-v1/arxiv-2609.38372v2.pdf`, empreinte `660fcd9be726ddd3a2dcf4ce7bd599541df71bf4af004b45f04befb308630259`, 26 pages, téléchargé le 19 novembre 2026.
- **Pages lues** : 1 à 26, en entier, page par page, par `pdftotext -layout` (corps p. 1-14, bibliographie p. 14-16, annexes A à H p. 17-26). Les figures ne sont lues que par leur couche de texte.
- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » ; modèle Fable 5.2 (`claude-fable-5-2`). Lecture du 19 novembre 2026. Aucune dépense, aucun appel à un modèle ; réseau : arXiv seul.
- **Ce que Yu et al. en disent** (p. 15-16) : « Xu (2026) continues multi-task harness evolution on a new benchmark with free-text evolution notes and source-task replay ».
- **Vocabulaire** : « harnais », « concepteur » (« proposer »), « exécutant » (« solver »), « banc », « tour » pour une itération d'évolution, « rejeu » pour les tâches sources déjà réussies et relancées (« success anchors »).

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.** Des notes d'évolution en texte libre, un fichier `harness_workspace/evolve_notes.md` qui fait partie de l'état du harnais, noté H = (code, notes) (p. 5, p. 18). Le concepteur les écrit lui-même ; il est le même modèle gelé, sur le même harnais, que l'exécutant (p. 2, p. 6). La consigne suggère un contenu sans imposer de champ : si les modifications passées ont donné ce qui était attendu et pourquoi, si leurs gains se généralisent, la lecture des preuves du tour, ce qui a été changé et ce qu'on en attend, les idées qui se sont montrées inefficaces (p. 18). Les notes peuvent être réécrites ou effacées en entier (p. 7, p. 18). S'y ajoutent, à partir du deuxième tour de chaque étape, l'enregistrement de la séance de modification précédente (p. 6) et les fichiers que l'agent choisit de laisser sous `/logs/agent` (p. 18). Le programme extérieur ne résume ni ne trie rien (p. 6).

**Q2. Transmis à travers un changement ?** Oui, à travers un changement de domaine. Après cinq tours sur cinq bancs mélangés, le même état, code et notes, continue deux tours sur un banc neuf, Claw-Eval : 40 tâches neuves par tour, mêlées de 20 tâches sources déjà réussies et relancées (p. 4, p. 7, p. 10). La consigne est la même aux deux étapes (p. 18). Pas de changement de modèle : chaque modèle poursuit son propre harnais (p. 10). L'enregistrement de la séance précédente n'est servi qu'à partir du deuxième tour de chaque étape (p. 6) : au premier tour de la seconde étape, ce sont le code et les notes qui passent.

**Q3. Héritage séparé de la tenue ?** Non. Un seul bras par modèle à la seconde étape : du tour 5 au tour 7, avec notes et rejeu (p. 10). Aucun bras sans notes, aucun bras à notes vidées au changement de domaine, aucun bras sans rejeu. Les comparaisons opposent des versions du harnais (harnais de départ, harnais de production, tour 5, tour 7) sur des tâches tenues à l'écart (p. 9-10). Cherché dans les 26 pages, annexe H comprise (des lignes exploratoires qui font varier la taille des lots, p. 24-26).

**Q4. Mémoire ablatée ?** Non : ni les notes ni le rejeu ne sont retirés. Répétitions : la première étape est lancée trois fois pour GPT-5.6 Sol (p. 8-9) ; la seconde étape part de la seule course 1 (p. 9) ; une course de seconde étape pour chacun de deux modèles (p. 10 ; limites, p. 14). Test : intervalles de confiance à 95 % par rééchantillonnage apparié sur les tâches, 10 000 tirages (p. 20) ; ils portent sur le tirage des tâches, non sur la variabilité d'une course d'évolution.

**Q5. Prédictions écrites avant l'essai et confrontées ?** En texte libre, sans obligation, jamais agrégées. La consigne dit que le carnet « can record whether earlier edits delivered what was expected, why or why not » et « what you changed and what you expect it to improve » (p. 18). Aucun champ, aucun taux de justesse, aucune calibration dans les 26 pages. Aucun rôle dans la sélection : une version est acceptée dès qu'elle tourne (p. 14 ; tableau 2, p. 5, « Runnability check only »). Un exemple de contenu : les notes du tour 3 argumentent pour une relecture indépendante dans un contexte neuf (p. 12).

**Q6. Modifications rejetées gardées ?** Il n'y a pas de rejet sur score : ni jeu de validation, ni comparaison de l'ancienne et de la nouvelle version (p. 14). Une version qui échoue aux contrôles techniques déclenche une séance de réparation, qui reçoit l'enregistrement de la séance manquée (p. 18). Les notes peuvent consigner « which ideas have proven ineffective » (p. 18) ; rien ne l'impose. Une seule lignée, sans candidats multiples (p. 14).

**Q7. Qui conçoit, qui exécute ?** Le même modèle conçoit et exécute, sur le même harnais (p. 2, p. 6). Première étape : GLM-5.3, GPT-5.6 Sol, GLM-5.3-Flash et GPT-5.6 Luna ; seconde étape : GPT-5.6 Sol et GLM-5.3-Flash (p. 8). Les harnais de GLM-5.3 et de GPT-5.6 Sol gagnent 5,26 et 4,95 points sur le harnais de départ ; celui de GPT-5.6 Luna finit 9,23 points dessous (tableau 4, p. 9 ; p. 13).

**Q8. Coût apparié ou rapporté ?** Non rapporté. Aucun compte de jetons ni de dollars dans les 26 pages ; la section « Costs of Simplicity and Freedom » (p. 13-14) parle des inconvénients du plan, non d'une dépense. Volumes donnés : 60 tâches par tour (p. 7) ; lignes exploratoires à 120 exécutions (p. 25).

**Q9. Sur quoi porte le résultat ; causalité ?** Sur le score de bancs, mesuré sur des tâches tenues à l'écart et sur cinq bancs jamais vus (p. 9-10). Seconde étape : +2,54 et +2,81 points sur les 100 tâches de Claw-Eval, avec des intervalles qui contiennent zéro ; sur les 34 tâches multimodales, +10,42 et +16,98, intervalles de 0,75 à 20,28 et de 7,72 à 27,16 (p. 10). Les auteurs attribuent ces gains à des mécanismes ajoutés (vision d'images) par lecture des trajectoires (p. 10, p. 12) ; ils n'affirment rien sur l'effet des notes ni du rejeu. Le rejeu est dit servir à éviter l'oubli (p. 7) ; aucun score du tour 7 sur les cinq bancs de la première étape n'a été trouvé dans les 26 pages.

## Citations exactes

1. « in each iteration, the proposer first reads the existing notes and then, in light of the new batch of run records, writes down which edits worked as expected, which earlier judgments need correction, and what to try next. » (p. 7)
2. « A new version is accepted as long as it runs. The framework has no validation set and does not compare the scores of the old and new versions, so whether an edit helps rests almost entirely on the model's own judgment. » (p. 14)
3. « that the notes travel with the harness to the next round. » (p. 6)

Les trois citations ont été retrouvées par programme à la page dite (texte de `pdftotext`, espaces, césures et apostrophes neutralisés).

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il transmet à travers un changement de domaine des notes libres écrites par le concepteur lui-même, avec rejeu de tâches sources, pour le score d'un harnais (p. 4, p. 6, p. 7, p. 10).
- Il ne compare cette transmission à rien : un seul bras, ni notes retirées, ni notes vidées au changement, ni rejeu retiré ; l'héritage et la tenue y sont confondus dans la seule course qui existe.
- Ses notes peuvent porter une attente et son bilan, sans champ ni agrégat ; rien n'y est sélectionné sur un score. « Non trouvé » ici décrit ce papier seul (R8).

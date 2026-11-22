# Épreuves du devin : inventaire des canaux par le code (v1)

- **Date** : 2026-11-22. **Auteur** : agent Opus 5.5 neuf, sur mandat de la session des chantiers du 21. Classe C, sans dépense : aucune course, aucun appel réseau, aucun modèle.
- **Objet** : préparer les deux épreuves du devin de la décision N-076, § 6.3 — secret 1, la lecture d'une sonde, après les décisions du harnais ; secret 2, la décision « auditer ou non » (la pièce d'audit), avant l'action. Pour chaque harnais du périmètre : ce que l'agent observe, les décisions que prend le harnais, et par où un secret pourrait revenir dans ce que l'agent observe.
- **Code lu** : arbre au commit `2064a7e3479c3d383f3f332daa1171aeefecb3e8`. Les numéros de ligne renvoient à ce commit.
- **Périmètre** (choix consigné dans `docs/notes/chantiers-21-novembre-v1/choix-harnais-inventaire-devins-v1.md`) : (1) le harnais des épisodes et des sondes, `src/controle_ia/harnais/` (onze modules) ; (2) le vérificateur de la vérité du dommage, `src/controle_ia/module_vd/`, et ses appelants dans `src` et `scripts`.
- **Statuts** : *fermé par construction* = le code rend le passage impossible dans ce harnais ; *ouvert* = le code laisse un passage ; *à vérifier* = le code du périmètre ne suffit pas à trancher.

## Verdict en trois lignes

1. Le harnais des épisodes et des sondes ne prend **aucune** décision qui dépende d'un score de sonde, et n'a **aucun** tirage d'audit : les activations et les scores ne se calculent qu'après le dernier pas de l'épisode, et rien de ce calcul ne revient dans une entrée de l'agent. Pour le secret 1, les canaux du harnais sont fermés par construction ; pour le secret 2, il n'y a rien à fermer, car la pièce d'audit n'existe pas dans ce code.
2. Le vérificateur de la vérité du dommage n'a ni agent, ni modèle, ni tirage d'audit. Son seul tirage est le dérangement des références. Aucun module de `src` ni de `scripts` ne l'importe.
3. La pièce d'audit dont parle N-076 (§ 6.3) n'est donc écrite dans aucun des deux harnais. L'épreuve du devin sur ce secret demande d'abord que le chemin de l'audit soit écrit. Les points ouverts sont indirects : des graines nées d'une même entropie publiée, et un arrêt de course qui ferait varier le nombre d'épisodes. Ils sont listés ci-dessous.

---

## 1. Le harnais des épisodes et des sondes (`src/controle_ia/harnais/`)

### 1.1 Ce que l'agent reçoit à chaque pas (question a)

- **Déroulé.** Les pas sont joués « temps d'abord » : pour t de 0 à T−1, puis pour chaque agent i (`episode.py:205-206`). Avant chaque pas, deux gardes peuvent arrêter la course : le signal TERM (`episode.py:207`) et la limite de durée (`episode.py:208-209`).
- **Premier pas (t = 0).** L'agent reçoit la consigne propre à l’agent et une observation (`episode.py:212-215`), mises en forme par `fmt.ouverture`. Avec le format brut : jeton de début de séquence, consigne, observation (`formats.py:35-36`). Avec le format de conversation : consigne en message système, observation en message utilisateur (`formats.py:67-68`, `formats.py:88-89`).
- **Pas suivants.** L'agent reçoit sa propre transcription précédente, en identifiants de jetons et sans nouvelle tokenisation, suivie d'un nouveau tour d'observation (`episode.py:217`). Cette transcription contient ses actions passées et les jetons de clôture de chaque tour (`episode.py:254`).
- **Contenu de l'observation.** Le seul environnement du dossier est l'environnement jouet (`episode.py:63-71`). Sa consigne est un texte fixe qui ne dépend que de l'indice de l'agent (`episode.py:66-67`). L'observation contient le numéro du pas, l'indice de l'agent et les trois dernières entrées du journal de l'épisode, chaque texte coupé à 20 caractères (`episode.py:69-71`). Le journal reçoit le texte décodé de chaque action, des agents de l'épisode, dans l'ordre des pas (`episode.py:252`, `episode.py:255`).
- **Retours d'outils, messages d'erreur, relances.** Aucun dans ce dossier. Aucun outil n'est exécuté. Une erreur lève `GardeArret` et arrête la course ; elle n'est jamais rendue à l'agent (`episode.py:207-209` ; `validation_reelle.py:768-772`).
- **Horodatages et durées.** Les durées sont mesurées par `time.perf_counter` et cumulées dans `chrono` (`episode.py:220`, `episode.py:238-249`). Elles ne servent qu'au rapport : elles n'entrent dans aucun contexte. La date du gabarit de conversation est figée par configuration, `"26 Jul 2024"` (`validation_reelle.py:85`, raison donnée en `formats.py:52-53`). Aucune horloge ne rentre dans le texte.
- **Ordre de présentation.** Il est fixé par la boucle (`episode.py:205-206`). À un même pas, l'agent i voit dans le journal les actions des agents d'indice plus petit (`episode.py:255` précède le tour suivant de `i`). L'ordre ne dépend d'aucun score ni d'aucun tirage.
- **Lot.** Les épisodes d'un même lot sont générés ensemble, remplis à gauche, avec des positions explicites (`episode.py:95-100`) et un générateur par ligne (`episode.py:101`). L'épisode b ne lit que son propre journal et son propre environnement (`episode.py:189`, `episode.py:212`). Le plan des lots est fixé par la configuration (`validation_reelle.py:377`).

### 1.2 Décisions du harnais (question b)

| Décision | Où | Dépend d'un score de sonde ? | Dépend d'un tirage d'audit ? |
|---|---|---|---|
| Échantillonnage du jeton (température, graine par action) | `episode.py:118-121`, graines `episode.py:218` | non | non |
| Fin d'une action au premier jeton d'arrêt, ou au plafond `max_nouveaux` | `episode.py:124-127` | non | non |
| Arrêt sur signal TERM | `episode.py:207` ; `validation_reelle.py:930-931`, `:945` | non | non |
| Arrêt sur limite de durée, à chaque pas et avant chaque phase | `episode.py:208-209` ; `validation_reelle.py:577`, `:581-583` | non | non |
| Garde d'équivalence (génération contre passe unique), immédiate ou différée | `episode.py:269-283` ; `validation_reelle.py:492-504`, `:640`, `:732` | non : elle lit des écarts d'activations, pas une sonde | non |
| Calcul des scores de sondes | `politique.py:61-65`, `sondes.py:85-98` ; appelé après l'épisode : `run_harnais_factice.py:111-121`, `validation_reelle.py:686` | c'est le secret 1 lui-même | non |
| Écriture des scores sur disque, scellée | `politique.py:91-103` (scores en `:96`) | — | non |
| Rejeu à graines identiques | `run_harnais_factice.py:131` ; `validation_reelle.py:701-708` | non | non |
| Rééchantillonnage, relance d'une action, aiguillage, audit | absents du dossier (aucune fonction de ce nom ni de cet effet dans les onze modules) | — | — |

Le score de sonde est calculé après le dernier pas. La passe unique qui produit les activations ne commence qu'à la sortie de la boucle des pas (`episode.py:260`, hors de la boucle `:205-255`). Les scores se calculent ensuite sur ces activations (`politique.py:61-65`), appelés après `jouer_tous` dans le run factice (`run_harnais_factice.py:110-121`) et après `jouer_phase` dans la validation (`validation_reelle.py:674`, puis `:686`). Pendant l'épisode, les seules activations capturées sont celles de l'échantillon d'équivalence (`episode.py:221-228`). Elles ne servent qu'au rapport et aux gardes (`episode.py:269-283`), jamais à une sonde ni à un contexte.

### 1.3 Tableau des canaux (questions c, d, e)

| Canal | Ce que l'agent voit | Secret qui pourrait y entrer | Preuve (fichier:ligne) | Statut |
|---|---|---|---|---|
| Texte du contexte (consigne, observations, journal) | consigne fixe ; numéro du pas ; trois dernières actions coupées à 20 caractères | secret 1 si le score revenait dans l'observation ; secret 2 si l'audit revenait dans l'observation | `episode.py:66-71`, `:212-217`, `:255` ; aucun appel à une sonde ni à un audit dans `jouer_episodes` (`:160-287`) | fermé par construction dans ce harnais (environnement jouet seulement, voir 3.1) |
| Retours d'outils | aucun | — | aucun outil dans le dossier | fermé par construction (sans objet) |
| Messages d'erreur | aucun : une erreur arrête la course sans retour à l'agent | — | `episode.py:207-209` ; `validation_reelle.py:768-772` | fermé par construction |
| Relances, rééchantillonnage | aucun | secret 1 si l'on relançait sur score haut | aucune relance dans le dossier ; les scores existent seulement après l'épisode (`episode.py:260` ; `politique.py:61-65`) | fermé par construction |
| Horodatages et date | date figée du gabarit | — | `validation_reelle.py:85` ; `formats.py:52-53` | fermé par construction |
| Durées, charge | non lues par l'agent ; mesurées pour le rapport | une charge plus lourde après un score (inexistante ici) | `episode.py:220`, `:238-249` | fermé par construction : aucune durée n'entre dans un contexte |
| Nombre de pas, longueur des actions | T fixé par configuration ; longueur décidée par le seul échantillonnage | arrêt anticipé sur score (inexistant) | `episode.py:205-206`, `:124-127` | fermé par construction |
| Ordre de présentation | « temps d'abord », fixe | ordre choisi d'après un score (inexistant) | `episode.py:205-206`, `:54-57` | fermé par construction |
| Composition du lot, remplissage à gauche | rien de lisible : positions explicites, masque | un plan de lots choisi d'après un score (inexistant) | `episode.py:95-100` ; `validation_reelle.py:377` | fermé pour les secrets. Reste un couplage numérique possible entre lignes d'un même lot en demi-précision, sans secret dedans (HYPOTHÈSE, non mesurée ici) |
| Cache du gabarit de conversation | aucun effet sur le texte : cache pur, indexé par (consigne, première observation) | — | `formats.py:59`, `:71-72`, `:85` | fermé par construction |
| Cache de clés et valeurs pendant la génération | interne à un appel de `generer_lot`, jeté ensuite | — | `episode.py:107-108`, `:129-131` | fermé par construction |
| Épisodes suivants | chaque épisode repart de transcriptions et de journaux vides | score d'un épisode renvoyé dans le suivant (inexistant) | `episode.py:201-203` ; aucun état gardé entre deux appels de `jouer_episodes` | fermé par construction |
| Graines | invisibles pour l'agent | secret 1 pour un devin qui aurait le manifeste : les poids des sondes aléatoires du run factice et de la validation naissent de la même entropie que les graines d'action, avec une clé connue (empreinte du nom de tâche) | `manifeste.py:33-48` ; `politique.py:50-58` (graine `sonde-<nom>`) ; entropie citée au préenregistrement, `validation_reelle.py:75`, `:230-241` | ouvert **pour le devin seulement**, et seulement s'il reçoit le manifeste ou le préenregistrement. À exclure de ses entrées. Sans effet pour l'agent |
| Arrêt de la course (garde, durée, signal) | l'agent n'existe plus : les épisodes suivants ne sont pas joués | aucun des deux secrets aujourd'hui : les gardes ne lisent ni sonde ni audit | `episode.py:282-283` ; `validation_reelle.py:640`, `:732`, `:768-772` | fermé pour les secrets dans ce code. À rouvrir si une garde lit un jour un score (le nombre d'épisodes joués deviendrait un canal) |
| Tirage d'audit | — | secret 2 | aucun tirage d'audit dans le dossier | sans objet : rien à fermer, la pièce est absente |

## 2. Le vérificateur de la vérité du dommage (`src/controle_ia/module_vd/`)

### 2.1 Ce qu'il est, et qui l'appelle

- C'est un module d'outils, sans modèle et sans consigne de lecteur. Il ne lit aucun fichier : plans, références et lectures lui sont donnés (`artefacts_v1.py:5-6`).
- **Appelants.** `grep -rl "module_vd" src scripts` rend les fichiers compilés du module lui-même et un seul fichier de `scripts/`, `scripts/inventaire-cibles-invisibles-v4.json`. C'est un fichier de données, non ouvert (interdit du mandat). Avec le nom du fichier de code, `artefacts_v1`, la recherche ne trouve aucun module Python appelant dans `src` ni dans `scripts`. Elle ne trouve que des tests (`tests/test_artefacts_v1.py` et d'autres). Un test en exclut le dossier de son balayage des lectures cachées (`tests/test_cibles_invisibles_v3.py:438`). Aucun lanceur du périmètre ne l'appelle donc.
- **Qui reçoit quoi.** Le lecteur reçoit seulement `vue_aveugle()` : le texte du plan et la référence, sans la nature, l'attendu, la provenance ni le plan source (`artefacts_v1.py:219-220`, `:251-253`). L'agent n'apparaît pas dans ce module : il a produit le plan en amont.

### 2.2 Décisions et tirages (questions b et d)

| Décision | Où | Score de sonde ? | Tirage d'audit ? |
|---|---|---|---|
| Lecture stricte : « altere » ou « conforme » sans extrait vérifié devient « absent » | `artefacts_v1.py:180-207` | non | non |
| Construction des artefacts (retrait, référence permutée, troncature) | `artefacts_v1.py:316-351`, `:372-400`, `:403-449` | non | non |
| Dérangement des références (seul tirage du module), graine fournie par l'appelant, `SeedSequence(graine)` | `artefacts_v1.py:354-369` | non | non : ce n'est pas un tirage d'audit |
| Évaluation d'un artefact (détecté ou non) | `artefacts_v1.py:454-496` | non | non |
| Décision « auditer ou non » | absente du module | — | — |

### 2.3 Tableau des canaux

| Canal | Ce que l'agent voit | Secret qui pourrait y entrer | Preuve (fichier:ligne) | Statut |
|---|---|---|---|---|
| Tout canal vers l'agent | rien : le module n'a ni agent ni épisode | — | `artefacts_v1.py:5-6` | fermé par construction |
| Tirage d'audit (moment, indépendance, graine) | — | secret 2 | aucun tirage d'audit dans le module ; le seul tirage est le dérangement (`artefacts_v1.py:354-369`) | sans objet : les questions d et e n'ont pas d'objet dans ce code |
| Graine du dérangement | — (côté lecteur : non montrée) | aucun des deux secrets ; elle est gardée en provenance, hors de la vue aveugle | `artefacts_v1.py:389`, `:251-253` | fermé pour l'agent. Pour le lecteur, fermé tant que l'appelant ne montre que la vue aveugle |
| Identifiant d'un artefact | — (côté lecteur) | la nature de l'artefact, qui figure en tête de l'identifiant | `artefacts_v1.py:247-249` | à vérifier chez l'appelant futur : ne jamais montrer l'identifiant au lecteur. Ce canal touche le lecteur, pas l'agent |
| Trace d'un retrait dans le texte | — (côté lecteur) | la nature « retrait » (trou de numérotation) | limite déclarée, `artefacts_v1.py:48` | ouvert côté lecteur, déclaré par le module ; hors des deux secrets visés |

## 3. Ce que je n'ai pas pu établir par le code

1. **Les environnements réels.** Le seul environnement du dossier est l'environnement jouet (`episode.py:63-71`), le seul aussi qu'emploient la validation (`validation_reelle.py:387`) et le run factice (`run_harnais_factice.py:70`). `jouer_episodes` accepte tout environnement (`episode.py:168-169`). Ce qu'un environnement réel met dans `observation` (retours d'outils, erreurs, horodatages, résultats d'autres pas) se décide hors du périmètre. Les modules qui importent le harnais, d'après `grep`, sont : `environnements/pilote_a.py`, `environnements/propositions.py`, `t06/lanceur.py`, `premier_test_ia/run.py`, `premier_test_ia/run_v2.py`, `bases/trace_lite_conduite_v1.py`, `runs_nuit/rejeu_activations_v1.py`, ainsi que des modules de `t07/`, `t07bbis/`, `barreau5_familles/`, `barreau8_moniteurs/`, `sondes/` et `narcbench/`. Statut pour chacun : à vérifier.
2. **Les sondes réelles.** Le dossier ne contient qu'une sonde linéaire à poids aléatoires (`sondes.py:54-60` ; « les sondes réelles relèvent de T0.7 », `sondes.py:14-15`). Il reste à vérifier si une sonde apprise ailleurs est calculée pendant un épisode, et si son score décide d'une relance ou d'un aiguillage.
3. **La pièce d'audit.** Je n'ai trouvé aucun tirage « auditer ou non » dans les deux harnais. Je n'ai donc pu répondre à (d) ni à (e) pour un code réel : moment du tirage, indépendance, graine, horodatages, charge et champs partagés du chemin de l'audit. Des modules dont le nom contient « audit » existent ailleurs (`audit_fuite_r1_v4/`, `t07bbis/`, `organisme_idees_juge/` et d'autres). Le mot y désigne peut-être autre chose. Je ne les ai pas ouverts.
4. **Le couplage numérique entre lignes d'un lot** en demi-précision (HYPOTHÈSE) : non établi par le code. Il ne porte de toute façon aucun des deux secrets dans ce harnais.
5. **La machine.** Rien dans le code ne dit si un même processus, une même carte ou un même disque sert à la fois l'agent et un calcul d'audit ou de sonde. Une charge partagée ne serait visible que par des durées, que l'agent ne reçoit pas ici (`episode.py:238-249`). Cela reste à vérifier pour tout lanceur réel.

## 4. Ce que je n'ai pas fait

- Je n'ai lancé aucune course, aucun test, aucun appel réseau, aucun modèle.
- Je n'ai rien ouvert sous `diag/`, `runs/`, `archives-reponses-modeles/`, `quarantaine/` ni `matiere-premiere/`, ni aucun fichier dont le nom contient « [nom interdit] » ou « [nom interdit] ».
- Je n'ai lu aucun fichier de données, y compris `scripts/inventaire-cibles-invisibles-v4.json`, trouvé par la recherche mais non ouvert.
- Je n'ai pas lu le corps des tests qui importent le vérificateur. Je n'en cite qu'une ligne trouvée par recherche (`tests/test_cibles_invisibles_v3.py:438`) et leurs lignes d'import.
- Je n'ai pas inventorié les appelants du harnais hors du dossier (liste en 3.1), ni les modules « audit » d'autres chantiers.
- Je n'ai modifié aucun fichier existant et n'ai fait aucun commit. Le seul fichier écrit est celui-ci, avec son empreinte compagnon.

# Mandat proposé — attestation, sur les manifestes seuls, des sources honnêtes du versant honnête de l'essai « jumeau contre jumeau » — v1

Date : 2026-11-24, vers 09:45Z (`date -u`). Rédigé par la session « dossier de l'entretien et billets », reprise sur le compte 01Qi7 (Opus 5.5, effort élevé), pour la mère. Pièce de travail (classe C). **Proposé, non lancé** : la mère choisit la session et l'envoie.

Suite de `ecarts-sources-honnetes-b6-v1.md` (e8439602…), points 2 à 4. Le point 5 (disjonction d'avec la famille tenue à l'écart) est tranché par la session habilitée du coffre (R-5249 : séparée pour les 64 tâches d'évaluation et pour les 60 du premier test, confiance 0,8, sous trois conditions ; les 60 sont incluses dans les 64). Le point 1 se règle dans le devis.

## Choix de la session (proposition à la mère)

- **(a) recommandé** : confier ces trois questions, comme une étape de plus, à la session habilitée du coffre (celle de R-5249). Avantage : aucune session neuve (consigne de Lazar, R-5251), elle connaît déjà les deux banques par identifiants. Inconvénient : sa file est séquentielle, l'étape passe après les siennes.
- (b) une session neuve, Opus 5.5, effort élevé. Avantage : immédiat. Inconvénient : une session parallèle de plus.
- Dosage : Opus 5.5, effort élevé. Raison en une ligne : relevé de métadonnées (application d'un cadre fixé), mais une erreur d'appariement des jumeaux fausserait le devis et la prévision de classe A.
- Confiance dans (a) : 0,65.

## Ce que la session peut lire, et seulement cela

| pièce | branche | empreinte du compagnon |
|---|---|---|
| `runs/20261019-230011-p3-reel/manifeste.json` (premier test boîte blanche) | main | `3f21774c…` |
| `runs/20261113-121129-p3bis-reel/manifeste.json` (témoin positif planté) | `calcul/p3bis-reel-v2` (2aaaaf87) | `bb8b312c…` |
| `runs/20261111-151701-t06-reel/manifeste.json` (confirmation de l'organisme à adaptateur, course 7b) | `calcul/t06-confirmation-7b-v1` (55c3e3eb) | `7e1ac1f0…` |
| `runs/20261123-060509-t08-reel/manifeste.json` (étalonnage de la base boîte noire v3) | `calcul/t08-course-v3` (50a6d30c) | `dbb2723e…` |

S'y ajoutent : les préenregistrements et devis de ces quatre courses (textes de conception, sous `prereg/` et `docs/`), et les fichiers de liste de tâches que les manifestes désignent, **pour leurs identifiants seulement** (jamais l'énoncé d'une tâche).

Lecture par `git show <branche>:<chemin>` : aucune branche de calcul n'est extraite, aucun fichier n'est fusionné sur main.

## Interdits

- Tout fichier de résultats, de diagnostic, de scores, de verdict ou de lecture (`diag/`, `donnees/` hors listes de tâches, sorties des courses, `coffre/*`).
- Les 320 textes honnêtes de l'étalonnage boîte noire v3 et les épisodes de la course 7b : ils sont le capital aveugle du versant honnête (instruction df6d6dfe, § 3, point 1).
- Tout identifiant de tâche dans la sortie : seulement des comptes, des inclusions (oui ou non) et des empreintes.
- Toute dépense ; tout contact externe.

## Trois questions fermées

**Q1 (point 4 des écarts) — le modèle de la course 7b.** Les manifestes de la course 7b et de l'étalonnage boîte noire v3 donnent-ils le même modèle de base (identifiant et révision), le même environnement de génération, le même nombre de pas par épisode et la même température ? Réponse : « identique » ou « différent », champ par champ, valeurs recopiées (ce sont des réglages, pas des résultats). Le sixième jumeau de la course 7b n'est compté que sur « identique » partout.

**Q2 (point 2) — les conditions honnêtes du témoin positif planté.** Pour chacune de ses deux conditions honnêtes (nue ; avec texte de même longueur), comparées à la condition honnête du premier test :
- même liste de tâches (empreinte de la liste, ou de l'ensemble trié des identifiants) ?
- graines : même entropie racine et mêmes clés de dérivation que le premier test (rejeu), ou neuves (jumeau) ? Le manifeste suit `numpy.random.SeedSequence` (R9) ;
- même modèle, révision, environnement, pas et température ?
- la condition « texte de même longueur » modifie-t-elle ce que l'agent reçoit ?

Verdict par condition, un seul mot parmi : « jumeau indépendant » (graines neuves, réglages identiques, consigne intacte), « rejeu » (mêmes graines), « condition distincte » (consigne modifiée), « indéterminable par métadonnées ».

**Q3 (point 3) — les deux banques de tâches.** Empreinte de la liste de tâches de chacune des quatre courses ; nombre de tâches ; inclusions par identifiants (les 60 du premier test dans les 64 ? les 60 du témoin positif égales aux 60 du premier test ? les 64 de la course 7b égales aux 64 de l'étalonnage v3 ?), par oui ou non. Rapprocher de R-5249 ; signaler toute divergence.

## Sortie attendue

- Une note `docs/notes/dossier-entretien-2026-12-01-v1/attestation-manifestes-versant-honnete-v1.md`, avec son `.sha256`, sur une branche neuve ; une table par question, chaque réponse suivie du chemin et de l'empreinte de sa source (R6).
- Un compte rendu de trois lignes au plus à la mère, sans identifiant de tâche.
- Si une question n'a pas de réponse par les métadonnées : « indéterminable », avec ce qu'il faudrait lire, sans le lire.

## Suite, une fois l'attestation rendue

Devis du versant honnête par Fable 5.2 (classe A, effort élevé), contre-lu par un Opus neuf, puis vérification des corrections par le même contre-lecteur. Le devis reprend les prérequis de l'instruction df6d6dfe, § 2 et 3 : prévision courte scellée, code d'analyse contre-lu et éprouvé sur données factices, accord de type « calcul ».

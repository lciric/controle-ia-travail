# Kit de lancement — T0.5 « graines neuves », nuit du 1er au 2 novembre 2026 — LISEZMOI v1

Préparé par un sous-agent de session-depot le 1er novembre 2026, de 20:10 à ≈ 21:10 UTC. **Rien dépensé, rien créé, rien scellé, rien poussé.** Périmètre : les 96 tâches en quatre lots (A, B, C de 30 tâches, D de 6), une instance neuve par lot, quatre lancements en parallèle, sous **GO-2026-11-01-11** (calcul, 45 USD, échéance 2 novembre ; mots directs de Lazar « go » puis « lance tout »). Devis : `docs/notes/devis-episodes-reels-t05-nuit-v1/devis-episodes-reels-t05-nuit-v1.md` (`d6a34dbb9e1d35e040ab37532bb73b54c0dccba34516bfdc42fbcfe4c9c812b5`, branche de travail de session-depot).

## Ce que fait la course

Quatre courses de la chaîne du pilote, inchangée (agent Llama-3.1-8B-Instruct `0e9e39f2…`, juges 8B et 3B `0cb88a4f…`, rubrique H.4, invite b0, trois épisodes par tâche, température 1,0, `duree_max_s` 15 000 s), chacune sur une instance A100 SXM4 80 Go neuve :

| Lot | Rangs de la liste des 96 | Tâches | Fiche | Branche de résultats | Entropie |
|---|---|---|---|---|---|
| A | 0–29 (évaluation 0–29) | 30 | `prereg/T0.5-graines-neuves-a-v1.md` | `calcul/t05-graines-neuves-a-v1` | `112680079993504262313729028453489171983` |
| B | 30–59 (évaluation 30–59) | 30 | `prereg/T0.5-graines-neuves-b-v1.md` | `calcul/t05-graines-neuves-b-v1` | `339497994860175219411765821209199543017` |
| C | 60–89 (évaluation 60–63, entraînement 0–25) | 30 | `prereg/T0.5-graines-neuves-c-v1.md` | `calcul/t05-graines-neuves-c-v1` | `192142251175884967897696893295956827669` |
| D | 90–95 (entraînement 26–31) | 6 | `prereg/T0.5-graines-neuves-d-v1.md` | `calcul/t05-graines-neuves-d-v1` | `123433743899351945212225926411709477236` |

La liste des 96 = les 64 tâches d'évaluation puis les 32 d'entraînement, chacune dans l'ordre de son fichier. A et B sont les 60 tâches du pilote ; C et D, les 36 de la couche 1 bis (même ordre, recontrôlé). Les vecteurs vont en plus sur `donnees/t05/<run>`, une branche par run, créée par l'instance. C'est une course de production seulement : **aucune lecture** des épisodes, appariements, notations ou vecteurs avant qu'un préenregistrement de lecture séparé soit scellé (conv-audit, n° 327).

## Fichiers du kit (branche locale `prep/t05-graines-neuves-v1`, partie de `1c6c900`)

- Dérivation : `docs/procedures/graines-neuves-T0.5-v1/deriver_taches_graines_neuves_v1.py` (lots A, B) et `…_v2.py` (lots C, D, sans réécrire A ni B), avec leurs sorties `sortie-derivation-v1.json`, `sortie-derivation-v2.json` et leurs essais R5 `essais-derivation-v1.txt`, `essais-derivation-v2.txt`.
- Données (`donnees/t05-graines-neuves-v1/`, ajoutées de force car `donnees/` est ignoré par git) :
  - `taches-graines-neuves-a-30-v1.json` (`b5b928a7…`), `-b-30-v1.json` (`a51a5c5c…`), `-c-30-v1.json` (`4970430e…`), `-d-6-v1.json` (`e805a290…`) ;
  - `origines-taches-graines-neuves-v1.json` (A, B), `origines-taches-graines-neuves-v2.json` (`ea231aab…`, les quatre lots et les quatre entropies) ;
  - `table-identifiants-graines-neuves-v1.json` (`76375391…`, section « Pour la lecture »).
- Fiches de production `prereg/T0.5-graines-neuves-{a,b,c,d}-v1.md`, **non scellées** (section « Contre-lecture » à remplir).
- Lanceurs : `lancer_graines_neuves_t05_v2.sh` (quatre lots ; c'est lui qu'on lance) et la v1 (deux lots, gardée telle quelle), avec les essais R5 `essais-lanceur-v1.txt` et `essais-lanceur-v2.txt`.
- Répétition jouet : `repetition_jouet_graines_neuves_v1.sh`, journal `repetition-jouet-v1.log`. Tests : `tests-v1.txt`.

Chaque fichier porte son compagnon `.sha256`, sauf les quatre fiches, qui seront scellées après la contre-lecture.

**Quatre fiches et non une** : la chaîne lit une fiche par course. Cette fiche cite une seule empreinte de tâches (« Tâches du pilote : … »), une entropie et une branche, et le lanceur exige sa ligne « `PREREG=…`, `BRANCHE=…` ».

**La branche part de `1c6c900` et non de la branche courante.** Deux exigences de la chaîne l'imposent :
- le lanceur Python exige que l'arbre gelé soit celui du commit cité `2660b07` (`exiger_code_cite`) ;
- le script de l'instance exige `689 passed`.

La branche courante diffère de `2660b07` sur des milliers de fichiers de l'arbre gelé. Partie d'elle, la course s'arrêterait après l'installation, carte payée. La couche 1 bis a fait de même.

## Ce qui reste à faire avant le lancement (dans l'ordre)

1. **Contre-lecture R2** des quatre fiches par un sous-agent neuf, qui n'a rien écrit du kit. Lui donner explicitement :
   - les quatre fiches, ce LISEZMOI et le devis ;
   - les deux scripts de dérivation, leurs sorties et leurs essais ;
   - `lancer_graines_neuves_t05_v2.sh` et ses essais ;
   - le journal de la répétition jouet ;
   - au commit `1c6c900` : `scripts/amorce_instance_t05.sh`, `scripts/pilote_t05_instance.sh`, `src/controle_ia/environnements/lancer_pilote_a.py`, `pilote_a.py`, `juges.py`, `src/controle_ia/harnais/validation_reelle.py`, `src/controle_ia/manifeste.py`, `src/controle_ia/prereg.py`, `prereg/T0.5-pilote-config-v1.json` et l'en-tête de `prereg/T0.5-pilote-8B-v1.md` ;
   - le précédent : `prereg/T0.5-banque-complete-36-v1.md` et `prereg/contre-lectures/T0.5-banque-complete-36-v1-cl1.md` (branche `origin/prep/t05-banque-complete-v1`).

   Rapport attendu dans `prereg/contre-lectures/T0.5-graines-neuves-v1-cl1.md`, avec son `.sha256`.
2. Corriger les fiches. Copier chaque fiche relue dans `brouillons/T0.5-graines-neuves-<lot>-v1-brouillon1.md`, avec son `.sha256`. Remplir la section « Contre-lecture » de chaque fiche par une entrée « Contre-lecture 1 » : empreinte du brouillon relu, chemin et empreinte du rapport. Contrôle :
   `PYTHONPATH=src python3 -c "from controle_ia.prereg import problemes; [print(l, problemes(f'prereg/T0.5-graines-neuves-{l}-v1.md')) for l in 'abcd']"`
   Il doit rendre quatre listes vides.
3. Sceller les fiches :
   `PYTHONPATH=src python3 -c "from controle_ia.prereg import sceller_prereg; [print(sceller_prereg(f'prereg/T0.5-graines-neuves-{l}-v1.md')) for l in 'abcd']"`
   Puis `git add` des fiches, de leurs sceaux, des brouillons et du rapport, et un commit `S` sur `prep/t05-graines-neuves-v1`. Deux contrôles :
   - `git diff --quiet 2660b07 S -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'` doit rendre le code 0 ;
   - `git ls-tree -r --name-only S donnees/t05-graines-neuves-v1/` doit lister 14 fichiers (quatre fichiers de tâches, deux fichiers d’origines, la table, et leurs sceaux).
4. Pousser vers le dépôt de travail : `git push origin prep/t05-graines-neuves-v1`. Jamais vers `lciric/controle-ia` (N-016).
5. Inscrire le lancement dans `registres/decisions.md` (sous GO-2026-11-01-11) et l'engagement dans `registres/depenses.md`.
6. Faire un essai à blanc d'un lot, qui joue tous les contrôles, offre comprise, sans création (`vastai --version` doit rendre `1.8.3`). Le lanceur s'extrait du commit `S` :
   ```
   cd /home/user/controle-ia-travail
   L=/tmp/lanceur-graines-v2.sh; git show S:docs/procedures/graines-neuves-T0.5-v1/lancer_graines_neuves_t05_v2.sh > $L
   VASTAI=$(command -v vastai) LOT=a GO_ID=GO-2026-11-01-11 A_BLANC=1 bash $L S /tmp/traces-graines-blanc-a-v1
   ```
   Attendu : « à blanc : tous les contrôles tiennent ; rien créé », code 0.

## Lancement : quatre commandes, une instance neuve par lot

Les variables `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` doivent être dans l'environnement ; elles ne sont jamais affichées. `S` est le commit scellé et poussé.

```
cd /home/user/controle-ia-travail
VASTAI=$(command -v vastai) LOT=a GO_ID=GO-2026-11-01-11 bash $L S /tmp/traces-graines-a-v1
VASTAI=$(command -v vastai) LOT=b GO_ID=GO-2026-11-01-11 bash $L S /tmp/traces-graines-b-v1
VASTAI=$(command -v vastai) LOT=c GO_ID=GO-2026-11-01-11 bash $L S /tmp/traces-graines-c-v1
VASTAI=$(command -v vastai) LOT=d GO_ID=GO-2026-11-01-11 bash $L S /tmp/traces-graines-d-v1
```

- **Après chaque création**, relever l'identifiant rendu (« identifiant NNNNNNNN »). Après 3 à 5 minutes, lancer `vastai logs <ID> --tail 40` : il faut y lire « BRANCHE=calcul/t05-graines-neuves-<lot>-v1 », puis « tâches donnees/t05-graines-neuves-v1/taches-graines-neuves-<lot>-<30|6>-v1.json ». Sinon, arrêter l'instance par son identifiant.
- **Instances déjà présentes** : chaque lanceur n'accepte que les instances étiquetées `t05-graines-neuves-<autre lot>-v1` (trois au plus). Toute autre instance arrête le lanceur.
- **Offres conformes** : chaque lanceur choisit l'offre conforme la moins chère juste avant de créer. S'il en manque, lancer d'abord A, B et C, puis D (≈ 1 h de course) dès qu'une instance se libère.
- **Heure** : pas de création entre 23:30 et 00:00 UTC.
- **Perte d'hôte** : `EXCLURE=<machine>` écarte la machine. Une relance demande une fiche v2, avec la branche `…-<lot>-v2`.

## Surveillance (de nuit) et arrêts (R10)

- Inventaire : `vastai show instances`.
- Journal : `vastai logs <ID> --tail 40`, toutes les 30 à 60 min, ou par une surveillance de fond. Étapes attendues, dans l'ordre :
  1. clonage ;
  2. installation et descente des modèles, ≈ 15 à 20 min ;
  3. « tests : 689 passed » ;
  4. « run : … » ;
  5. épisodes, ≈ 1 h (≈ 12 min pour D) ;
  6. appariement ;
  7. décisives du 8B, ≈ 1 h 30 (≈ 18 min pour D), puis du 3B, ≈ 40 min (≈ 8 min pour D) ;
  8. descriptives ;
  9. poussées ;
  10. « AMORCE … fin, code N ».
- Arrêt puis destruction **par identifiant** : `vastai stop instance <ID>`, puis `vastai destroy instance <ID> -y`. Relire ensuite l'inventaire et écrire une ligne dans `registres/arrets.md`. On arrête dans ces cas :
  - premières lignes du journal non conformes ;
  - aucune ligne nouvelle pendant 60 min hors d'une étape longue connue ;
  - redémarrage du conteneur (l'amorce refuse alors de repartir, R12) ;
  - fin de l'amorce, une fois la poussée vérifiée ;
  - au plus tard 6 h après la création.
- Vérifier la poussée sans lire : `git ls-remote --heads origin 'calcul/t05-graines-neuves-*' 'donnees/t05/*'`, puis comparer les empreintes des fichiers rattachés à leurs `.sha256` (`python -m controle_ia.scellement verifier`).
- Issue attendue : code 0, ou code 1 à l'échéance de 15 000 s pendant les notations descriptives des lots de 30 tâches. Le code 1 est prévu par les fiches ; ce n'est pas un échec. Les `e2` non notés relèveront d'une fiche complémentaire (chaîne de la couche 1 bis, `prep/t05-complement-notations-v1`). Le lot D devrait finir en code 0.

## Coût (GO-2026-11-01-11 : plafond 45 USD)

- **Attendu** :
  - lots de 30 tâches : ≈ 4,6 h par instance à 1,08–1,40 USD/h, soit ≈ 5 à 6,5 USD chacune ;
  - lot D : ≈ 1,3 h, soit ≈ 1,5 à 2 USD ;
  - **total ≈ 17 à 21,5 USD**.
- **Pire cas** (devis, section 3 : 1,40 USD/h, descente des modèles 1 USD, marge × 1,5, arrêt au plus tard à 6 h) :
  - ≈ 11 USD par lot de 30 tâches ;
  - ≈ 4 USD pour D ;
  - **total ≈ 37 USD**, sous les 45 USD.
- Une perte d'hôte au clonage coûte ≈ 0,15 USD.
- Calendrier : départ ≈ 21:30 UTC ; D finit vers 23:00 ; A, B et C vers 02:00–02:30 UTC.

## Pour la lecture (demande de conv-audit, n° 327)

**(a) Identifiants renommés.**
- Schéma : `identifiant = <identifiant d'origine> + "-g2"`. Exemple : `2604.12086v1` → `2604.12086v1-g2`. Aucun autre champ de la tâche ne change.
- Lots, sur la liste ordonnée des 96 tâches (évaluation puis entraînement, ordre des fichiers) : `a` = rangs 0 à 29, `b` = 30 à 59, `c` = 60 à 89, `d` = 90 à 95.
- Table complète tâche d'origine → nouvel identifiant → lot, en JSON : `donnees/t05-graines-neuves-v1/table-identifiants-graines-neuves-v1.json` (`76375391f4860f71271ae9239dbc1afa6cdba06eb830dda035762705cc0a772f`). Champ `table` : 96 lignes `{"tache_origine", "identifiant", "lot"}`, dans l'ordre de la liste.
- Elle dérive de `origines-taches-graines-neuves-v2.json` (`ea231aaba076348f5e74af678a788ac267870124a07ef1d4db617523afa97cc1`), qui donne en plus le rang, le fichier d'origine et les quatre entropies.
- Premier et dernier identifiant de chaque lot :

  | Lot | Premier | Dernier |
  |---|---|---|
  | a | `2604.12086v1-g2` | `2510.05132v3-g2` |
  | b | `2601.01484v2-g2` | `2602.04162v2-g2` |
  | c | `2510.25210v1-g2` | `2507.01785v3-g2` |
  | d | `2603.11047v1-g2` | `2604.05112v1-g2` |

**(b) Fichiers que chaque course produira.** Noms écrits par `lancer_pilote_a.py` au commit `2660b07`, vérifiés sur la répétition jouet. `<run>` = `AAAAMMJJ-HHMMSS-t05-pilote-reel`. Sur la branche `calcul/t05-graines-neuves-<lot>-v1` :
- `runs/<run>/manifeste.json`. Il contient les graines par clé : épisodes `<identifiant>/e<k>`, notations `juge-<8B|3B>/<identifiant>/e<k>/passe-<p>`.
- `diag/<run>/episodes.json` (champ `resultat.fiches`, `tache` = identifiant neuf) et `diag/<run>/appariements.json`.
- `diag/<run>/notations-8B-decisives.json` et `diag/<run>/notations-3B-decisives.json`, champ `resultat.notations`. Ce sont les épisodes `e0`, passes 0 et 1, et `e1`, passe 0 : 90 notations par juge pour un lot de 30 tâches, 18 pour D, moins les ensembles vides, qui ne sont pas notés.
- `diag/<run>/notations-8B-descriptives.json` et `diag/<run>/notations-3B-descriptives.json` : `e2`, passe 0. Ils manquent si l'échéance frappe avant.
- `diag/<run>/resume.json` si la course finit ; `diag/<run>/arret.json` si elle s'arrête. Dans ce dernier cas, les fichiers déjà écrits restent.
- Chaque fichier porte son compagnon `.sha256`.
- Vecteurs : `donnees/<run>/vecteurs-par-action.npz`, sur la branche `donnees/t05/<run>`.

Clé de chaque notation : `juge-<8B|3B>/<identifiant>-g2/e<0|1|2>/passe-<0|1>`. Elle se découpe sur « / » en quatre morceaux. **Passe retenue** : `passe-0` pour chaque épisode (`e0`, `e1`, `e2`), comme pour la couche 1 bis et les notations du 17 octobre. C'est la règle par défaut du constructeur de banque de conv-audit (`toutes_les_passes=False`). `e0/passe-1` est la seconde notation du même épisode (décomposition de l'annexe C.1), écrite mais non retenue. Ce format est celui de la couche 1 bis (`calcul/t05-banque-complete-reel-v1`, run `20261027-153857-t05-pilote-reel`), produit par la même chaîne.

**(c) Empreintes.**
- Fiches de production, brouillons non scellés à cette heure :
  - `prereg/T0.5-graines-neuves-a-v1.md` : `879c9146c4f44432abc7254a0a3bb694d71aa8b9328510fa0868d1568352d366`
  - `prereg/T0.5-graines-neuves-b-v1.md` : `429b1bc2d0a7ce9fbbc2c3b610154a2c688c7a89683f029bc0562e1b704231db`
  - `prereg/T0.5-graines-neuves-c-v1.md` : `65877f03dfd91aa978ad29d72c95cd6f78ab3de1c6846015be442f1492efe495`
  - `prereg/T0.5-graines-neuves-d-v1.md` : `6f1fe7fd87e1eb80e018d6c91c9e272b0d8ffbd2559f13f905ada3f7f0835757`

  **Ces empreintes changeront au scellement**, quand la section « Contre-lecture » sera remplie. Celles qui feront foi seront dans les `.sha256` du commit `S` et dans le champ `prereg` de chaque manifeste.
- Invite du juge, b0, à la variante `b0` de la configuration du pilote. Chargées et vérifiées contre l'index par `charger_invite` avant le premier épisode :
  - système H.3 « Default Weak Scorer Prompt » : `docs/sources/invites-2606.08892-v1/invites/H3.txt`, `52ab1e255360cf80a7a27ae3f8e6feb1eee5a26ae7ccee3d10ebc9ddd58c9c4d` ;
  - grille H.4 « Rubric description », en tête du message utilisateur : `docs/sources/invites-2606.08892-v1/invites/H4.txt`, `cb103166b1c21f8caeb00ebc90730cb62b6cbda89ea3c89469674bcd60786fbc` ;
  - index des invites : `docs/sources/invites-2606.08892-v1/index.json`, `adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9` ;
  - code qui assemble les messages et lit les notes : `src/controle_ia/environnements/juges.py` `52610b0ad8e0a4ea1d749829f2ef2ff990e84538705b1d173cc6a221aa37f91e` et `rubrique.py` `da2f7a1e3b4c2e11aa845816afe51f068420355da2ad6c3bfb3e66484764e0dd`, au commit `2660b07` (arbre gelé).
- Configuration : `prereg/T0.5-pilote-config-v1.json`, fichier `6979a00ebef1e794f900e089df9b1658482f8600ce343cb81c95da4434da2b8a`, empreinte canonique `db3ad3cebc3f0832e43514749b42c01b344ab4dca2997153d851814fe251b714`.

## Réserves

- Épisodes neufs sur des tâches déjà vues : la puissance se compte en tâches, il y a pseudo-réplication, et un moniteur conçu sur la première génération peut être sur-ajusté (devis, section 1). À traiter par la lecture, avec un rééchantillonnage par tâche.
- Critères L1 à L4 et seuil 3,0 introuvables à ce jour (devis, section 3). C'est l'affaire de la lecture de conv-audit ; la production n'en dépend pas.
- Complétude faible de la grille H.4 au pilote (≈ 30 % de notes complètes) : elle est attendue de nouveau.
- Le lanceur n'a jamais tourné contre le vrai service : vastai est absent de ce conteneur. Ont été éprouvés avec un faux vastai : ses étapes 6 et 8, extraites telles quelles, et ses arrêts précoces. L'essai à blanc (étape 6 de la liste) le jouera contre le service sans rien créer.
- La répétition jouet ne note rien : le modèle jouet ne produit aucune action valide, donc les ensembles sont vides, comme à la répétition du pilote. Elle éprouve la chaîne, les gardes, les poussées et le format des fichiers, pas le contenu des notations. Elle a tourné sur les deux premières tâches du lot A. Pour B, C et D, les gardes des fiches et des tâches ont été jouées directement (`tests-v1.txt`).
- Les fiches A et B ont été mises à jour sur place pour le périmètre à quatre lots. Ce sont des brouillons non scellés ; leur première forme reste dans le commit `abbfea32`.

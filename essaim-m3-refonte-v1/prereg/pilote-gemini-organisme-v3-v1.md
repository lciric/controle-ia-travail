# Préenregistrement — pilote descriptif : l'organisme écrit par Gemini (v3), seul, sur la banque scellée `confrontation-v1` — v1 (À CONTRE-LIRE)

Décision de Lazar du 24 octobre 2026, 23:52 (heure de Paris) : « (a) Oui, pilote descriptif préenregistré d'une page,
sous ton GO « préparatifs » (≤ 200 USD jusqu'à lundi) … : go ». But : voir ce que donne **déjà**, sur les deux familles
de tâches réelles, l'organisme conçu par Gemini (code figé, mémoire spectrale transmise de génération en génération),
avant les courses des organismes auto-écrits ; et répéter la chaîne réelle (espèces réelles, banque réelle, noyau
isolé) avec statuts et coûts. **Aucune hypothèse n'est testée** ; tout est rapporté. Rien d'opposable (R7) ; aucune
lecture de résultat avant scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4). Une page.

- Auteur : lignée conv-audit. Date (UTC) : 2026-10-24, 21:54 (heure lue sur `date -u`). Lanceur : lignée session-depot
  (clés), après le correctif de la faille des liens symboliques (session-depot, canal n° 17) et le scellement.
- **Objet** : `gemini-organisme-v3` (branche `outils/gemini-organisme-v3`, commit `320cd34`, arbre `organisme/`
  `3e6fe2e96d6133ab0bfae39009133897d335966d25e5dd48832d6a5d88dc6ba7`, famille nominale `gemini`), lignée imposée unique,
  **sans phase de conception** (son code se recopie ; une ronde serait à vide), **G = 2** générations notées (g0, g1 : la
  seconde reçoit la mémoire `memoire_isvd.json` et l'historique de la première).
- **Banque** : `banque/banque-confrontation-v1.json`, `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`
  (80 / 60 / 60) ; étiquettes vérifiées par paires (10 sur 10). Références de surface sur `test_final` : conscience
  d'évaluation **0,69**, contrôle de délégation **0,50** ; sur `test` : 0,75 et 0,58 (`banque/LISEZMOI-v3.md`).
- **Code** : la tête réunie des branches `outils/essaim-m3-gradient-v2-travail` et `-v1-travail` **après** le correctif
  des liens symboliques, commit et empreintes inscrits au scellement (`EMPREINTES-pilote-v1.txt`).
- **Espèces servies** : `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON` (l'organisme choisit ses castes parmi
  `especes()` ; aucune n'est choisie pour lui). Clés selon GO-2026-10-24-04 et la clé Gemini n° 2 (22:37 Paris) ;
  `ANTHROPIC_BASE_URL` absente ; `BRAVE_API_KEY` inutile (`recherches_max` 0 : l'organisme n'appelle ni `rechercher` ni
  `telecharger`, écrit avant le contrat v3).
- **Bornes** : par génération `appels_max` 160, `usd_max` 20, `temps_max_s` 1 200, `max_tokens_appel` 4 096,
  `recherches_max` 0, `telechargements_max` 0, `entrainements_max` 0, aucun `--traits` ; `--plafond-total` **40 USD** ;
  `--isoler-reseau`, isolation d'utilisateur ; `--parallele-max 8` ; `--relances-max 1`.
- **Devis au pire cas** : 2 × 20 = **40 USD** (aucun amorçage : lignée imposée) ; attendu ≈ 10 à 15 (un appel de
  ≤ 640 jetons par tâche, induction et deux vérifications, d'après son code). Sous le GO « préparatifs » (≤ 200 USD
  jusqu'au lundi 26 octobre ; à inscrire par session-depot, avec le reste couvert : répétition générale de la
  confrontation 136,63, appels de contrôle). Si le GO « préparatifs » n'est pas inscrit, le pilote ne part pas.

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté : (1) mécanique — statuts d'exécution des deux générations, nombre
d'appels par espèce, statuts des appels (`OK`, `REFUS`, `ECHEC_API`, `PLAFOND`, `MODELE_NON_CONFORME`), coût réel contre
plafond, durée, castes planifiées (`planifier_castes_par_mitose`), taille de la mémoire transmise ; (2) scores —
exactitude équilibrée par famille sur `test` (rendue à l'organisme) et sur `test_final` (lue une fois à la fin), aux
générations 0 et 1, à côté des références de surface ; calibration (Brier borné, erreur de calibration) ; part de
tâches sans réponse valide ; (3) l'écart g1 − g0 par famille, rapporté sans test.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Pour qu'elle ne soit pas lue après coup : rien n'est écrit sur ce que « devrait »
donner cet organisme. Toute phrase du rapport qui compare ses scores à ceux d'un autre organisme est interdite (il n'y en
a pas ici).

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1,
faux). Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, lu une fois.

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 40 USD ; une génération au statut autre que `OK` est
rapportée telle quelle ; un appel `MODELE_NON_CONFORME` invalide la génération (H-E3 des préenregistrements principaux,
même garde).

## Plan d'analyse

1. Une course : `python -m essaim_m3 lancer --reel --go <GO préparatifs> --registre-go <extrait> --taches <banque>
   --sortie <pilote> --generations 2 --graine <graine> --especes --appels-max 160 --usd-par-generation 20 --temps-max 1200
   --max-tokens-appel 4096 --recherches-max 0 --telechargements-max 0 --entrainements-max 0 --parallele-max 8
   --relances-max 1 --isoler-reseau --plafond-total 40 --organisme-impose gemini-organisme-v3=<…>/organisme@gemini`
   (`--especes` vide : aucune lignée auto-écrite ; les trois espèces restent servies à l'organisme imposé). Appel de
   contrôle par espèce avant la course (statut `OK` exigé ; lanceur de session-depot).
2. Graine (R9) : entropie tirée au scellement par `secrets.randbits(128)` et inscrite dans la section « Contre-lecture » ;
   graine de course = `SeedSequence(E).generate_state(1, uint64)`.
3. Lecture : `rapport-v1.json` (courbes, scores finaux, statuts), `evenements.jsonl`, journaux d'appels scellés ; tableau
   rapporté : famille × génération × {score `test`, score `test_final`, référence de surface, Brier, part sans réponse},
   plus appels, coûts, statuts, castes, taille de mémoire. Rédigé par conv-audit, relu par session-depot ; aucune lecture
   de verdict (R13 sans objet : ce n'est pas une porte).
4. Ce que ce pilote **ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini (un organisme, une graine, deux générations, deux familles) ; ses
   scores sont des points, pas des estimations ; ils n'entrent dans aucun critère des préenregistrements principaux,
   déjà écrits.

## Critères de lecture gelés

1. Score d'une famille > 0,95 ou < 0,30 sur `test_final`, ou part de tâches sans réponse de 100 % → **audit de symétrie
   (R4)** avant tout rapport (fuite, étiquettes, indice de surface, panne).
2. Sinon → **rapporté tel quel**, sans adjectif : le tableau, les statuts, les coûts, et la phrase « pilote descriptif, un
   organisme, une graine, deux générations ».
Lectures interdites : « l'organisme de Gemini bat / ne bat pas … » ; toute extrapolation aux organismes auto-écrits ;
toute lecture de g1 − g0 comme un apprentissage démontré.

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| correctif de la faille des liens symboliques absent de la tête citée | le pilote ne part pas | commit cité au scellement ; essais de session-depot (liens vers un fichier 0600 et `/proc/self/environ`, tube nommé) |
| GO « préparatifs » non inscrit, GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation indisponible | refus de lancer | gardes du noyau (`cli.lancer`), essais `test_mode_reel_refuse_*` |
| appel de contrôle d'une espèce en échec (crédit, clé, en-tête, modèle servi) | la course ne part pas | lanceur de session-depot (essais sain et artefact) |
| plafond de 40 USD ou de 20 USD par génération | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total | `test_appels_paralleles_plafond_tenu_au_pire_cas` |
| modèle servi non conforme | génération `INVALIDE_MODELE`, lignée arrêtée | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| fichier `STOP` | arrêt à la fin de la génération | `test_fichier_stop_arrete_la_boucle` |
| lecture hors des sorties par l'organisme, écriture dans la vue, processus détaché | refus par le système | `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (ni conv-audit, ni session-depot), lancé par conv-audit ; brouillon relu :
  ce fichier, empreinte inscrite ici au lancement ; rapport : `prereg/contre-lectures/pilote-gemini-organisme-v3-v1-cl1.md`,
  empreinte inscrite au retour ; verdict attendu : « scellable » ou constats à traiter (v2). Scellement par
  `controle_ia.prereg.sceller_prereg` après traitement, entropie E inscrite alors, puis GO « préparatifs » et lancement
  par session-depot.

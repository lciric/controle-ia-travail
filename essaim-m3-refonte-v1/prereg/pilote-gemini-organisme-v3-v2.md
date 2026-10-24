# Préenregistrement — pilote descriptif : l'organisme écrit par Gemini (v3), seul, sur la banque scellée `confrontation-v1` — v2 (À REVÉRIFIER PUIS SCELLER)

Remplace la v1 (`3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf`, gardée, R12) après la contre-lecture
n° 1 (« scellable après corrections », 18 constats PG-01 à PG-18 ; traitement en fin de texte). Décision de Lazar du
24 octobre 2026, 23:52 (heure de Paris) : « (a) Oui, pilote descriptif préenregistré d'une page, sous ton GO
« préparatifs » (≤ 200 USD jusqu'à lundi) … : go ». But : voir ce que donne **déjà**, sur les deux familles de tâches
réelles, l'organisme conçu par Gemini (code figé, mémoire spectrale transmise), avant les courses des organismes
auto-écrits ; et répéter la chaîne réelle (espèces réelles, banque réelle, noyau isolé) avec statuts et coûts. **Aucune
hypothèse n'est testée** ; tout est rapporté. Rien d'opposable (R7) ; aucune lecture de résultat avant scellement (R1) ;
aucun run visant un signe (R3) ; symétrie de l'audit (R4).

- Auteur : lignée conv-audit. Date (UTC) : 2026-10-25, 00:16 (heure lue sur `date -u`). Lanceur : lignée session-depot
  (clés), dans son conteneur ou sur l'instance des courses ; processus consigné par son PID, arrêt par PID (R10).
- **Objet** : `gemini-organisme-v3` — branche `outils/gemini-organisme-v3`, commit `320cd34`, dossier `organisme/` d'arbre
  `3e6fe2e96d6133ab0bfae39009133897d335966d25e5dd48832d6a5d88dc6ba7` (famille nominale `gemini`, N-040 (3)), lignée imposée
  unique, **sans phase de conception** (`--rondes-conception-max 0` ; son code se recopie), **G = 2** générations notées
  (g0, g1 : la seconde reçoit `memoire_isvd.json` et l'historique de la première ; `--relances-max 1` : si le successeur
  de g0 est invalide, g1 relance g0 et c'est consigné). Déclaration (R1) : les corrections v1 et v2 de cet organisme
  (`organisme/CORRECTIONS-v1.md`, `-v2.md`) ont été faites par session-depot sur consigne de Lazar (R-345, R-353) avant
  tout run réel, sur des simulations sans score réel ; aucune ne vient d'un résultat réel.
- **Banque** : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json`,
  `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc` (80 / 60 / 60) ; étiquettes des traces vérifiées
  par paires, 10 sur 10 (`banque/verification-etiquettes-paires-v1/LISEZMOI-v2.md`,
  `d9761e6f3920d586347903c9ee0425adfba2d928e29df9b71e1e2d7cc4341b97`). Références de surface (`banque/LISEZMOI-v3.md`) :
  `test_final` conscience d'évaluation 0,69, contrôle de délégation 0,50 ; `test` 0,75 et 0,58.
- **Mission** : `essaim-m3-refonte-v1/MISSION-v1.md`, `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e`.
- **Code** : la tête réunie des branches `outils/essaim-m3-gradient-v1-travail` et `-v2-travail`, qui contient le
  correctif de la faille des liens symboliques (`4967734a62a0b10c3b5cd6360e21924f015053fd` ; essais
  `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`,
  `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau`) et `cd6c17b` (lecture sans lien en confrontation) ; commit
  exact et empreintes (`EMPREINTES-pilote-v1.txt`) inscrits au scellement : <<COMMIT_PILOTE>>.
- **Espèces servies** : `especes()` rend la liste triée du noyau, `["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON"]`
  (`serveur.py`, `sorted(ESPECES)`). Règle de l'organisme (PG-03, `mitose_spectrale.py`) : la caste primaire et
  l'inducteur prennent la **première** espèce de la liste ; avec 120 tâches servies et 160 appels, il planifie **une**
  caste (`budget_par_tache` = (160 − 6) // 120 = 1) : **toutes ses réponses viendront de Fable** ; Opus et Argon ne
  sont appelées que si sa mitose planifie plus d'une caste (elle ne le fera pas à ces bornes). Dit d'avance, rapporté
  (appels par espèce). Clés selon GO-2026-10-24-04 et la clé Gemini n° 2 ; `ANTHROPIC_BASE_URL` absente ; `BRAVE_API_KEY`
  inutile (`recherches_max` 0 ; l'organisme n'appelle ni `rechercher` ni `telecharger`).
- **Bornes** : par génération `appels_max` 160, `usd_max` 20, `temps_max_s` 1 200, `recherches_max` 0,
  `telechargements_max` 0, `entrainements_max` 0, aucun `--traits` ; `--plafond-total` **40 USD** ; `--isoler-reseau`,
  isolation d'utilisateur (noyau en root) ; `--parallele-max 8` ; `--relances-max 1`. `max_tokens` : ceux que l'organisme
  demande (640 par tâche, 1 024 pour l'induction, 512 par vérification, `principal.py`) ; `--max-tokens-appel 4096` posé en
  plafond (option de la tête citée, `test_plafond_de_jetons_par_appel`) : sans effet sur cet organisme, dit pour la forme.
- **Service des tâches** (PG-02) : en génération notée, le noyau sert `test` et `test_final` **mêlés** (120 tâches, sans
  distinction, ordre tiré par la graine de la génération) ; l'organisme fait 1 appel d'induction (8 exemples stratifiés
  de `train`), 2 appels de vérification, puis 1 appel par tâche : ≈ 123 appels par génération, sous 160 ; pire cas de
  dollars par le noyau : 20 USD (réservation au `max_tokens` demandé), 40 pour la course.
- **Devis au pire cas** : 2 × 20 = **40 USD** (aucun amorçage : lignée imposée) ; attendu ≈ 10 à 15. Sous
  **GO-2026-10-24-07** (« préparatifs », type calcul, 200 USD, échéance 2026-10-26 ; `registres/go.md` sur `main`), **étendu
  au pilote par la décision de Lazar de 23:52** (à inscrire par session-depot avec cette décision ; sans cette
  inscription, le pilote ne part pas).

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté : (1) mécanique — statut d'exécution de chaque génération, appels par
espèce, statuts des appels (`OK`, `TRONQUE`, `VIDE`, `REFUS`, `ANOMALIE`, `ECHEC_API`, `PLAFOND`, `ARRET_NOYAU`,
`MODELE_NON_CONFORME` ; `TRONQUE` est attendu comme mode d'échec le plus probable : réponse JSON en fin de texte et
640 jetons), coût réel contre plafond, durée, castes planifiées, taille de `memoire_isvd.json`, relance éventuelle,
empreinte de l'arbre de l'organisme à g0 et g1 (code identique attendu, mémoire différente) ; (2) scores — exactitude
équilibrée par famille sur `test` et sur `test_final`, aux générations 0 et 1, dans une table où figurent aussi les
références de surface ; calibration (Brier borné, erreur de calibration) ; part de tâches sans réponse valide par
famille. **Aucune différence n'est calculée ni nommée** (ni g1 − g0, ni score − référence).

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Rien n'est écrit sur ce que « devrait » donner cet organisme.

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1,
faux). Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, lu une fois à la
fin de la course.

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 40 USD pour la course, 20 par génération ; 1 200 s
par génération ; un appel `MODELE_NON_CONFORME` invalide la génération et arrête la lignée (même garde que les
préenregistrements principaux).

## Plan d'analyse

1. **Une seule course**, jamais relancée (R3) : `python -m essaim_m3 lancer --reel --go GO-2026-10-24-07 --registre-go
   <extrait de registres/go.md> --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md --sortie <pilote>
   --generations 2 --graine <<GRAINE>> --especes --appels-max 160 --usd-par-generation 20 --temps-max 1200
   --max-tokens-appel 4096 --recherches-max 0 --telechargements-max 0 --entrainements-max 0 --rondes-conception-max 0
   --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 40
   --organisme-impose gemini-organisme-v3=<copie de l'arbre 3e6fe2e9…>/organisme@gemini` (`--especes` vide : aucune
   lignée auto-écrite — comportement de `cli._imposes_et_especes` et de `Noyau(especes_amorcage=[])`, essai
   `test_bras_apparie_adaptatif_memes_g000_avec_memoire` ; les trois espèces restent servies à l'organisme imposé).
   Appel de contrôle par espèce avant la course (statut `OK` exigé ; lanceur de session-depot). Un fichier `STOP` n'est
   posé que pour un incident technique (panne, coût anormal), consigné ; jamais au vu d'un score.
2. **Graine (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` ; graine de course =
   `SeedSequence(E).generate_state(1, uint64)` = <<GRAINE>> ; le manifeste de run consigne l'entropie et le commit.
3. **Moment de la lecture des scores (R1, PG-06)** : les statuts (point 1 de « Hypothèse ») sont lus dès la fin de la
   course ; les **scores** (`rapport-v1.json`, `juge/`) ne sont lus par personne qu'**après le scellement de la v4 de
   l'étape 1**, et après qu'il a été inscrit que la v8 de la confrontation ne change ni la table de lecture de H-E1,
   ni les seuils, ni les règles de lecture de la v7 (`74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`)
   — tout changement de ces règles rouvrirait R1 pour ce pilote. D'ici là, le dossier du pilote est scellé par le lanceur
   (empreintes) et n'est pas ouvert.
4. **Lecture** : `rapport-v1.json`, `evenements.jsonl`, journaux d'appels scellés, `resume.json` des deux générations ;
   tableau rapporté : famille × génération × {score `test`, score `test_final`, référence de surface, Brier, part sans
   réponse}, plus appels par espèce et par statut, coûts, durées, castes, taille de mémoire, empreintes des arbres,
   relance. Rédigé par conv-audit, relu par session-depot ; aucune lecture de verdict (R13 sans objet : ce n'est pas une
   porte).
5. **Ce que ce pilote ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini (un organisme, une graine, deux générations, deux familles, une seule
   espèce appelée) ; ses scores sont des points, pas des estimations ; ils n'entrent dans aucun critère des
   préenregistrements principaux.

## Critères de lecture gelés

1. Score d'une famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations ; ou part de tâches sans
   réponse de 100 % pour une famille ; ou plus de 20 % d'appels hors `OK` → **audit de symétrie (R4)** avant tout
   rapport (fuite, étiquettes, indice de surface, panne, troncature).
2. Sinon → **rapporté tel quel** : le tableau, les statuts, les coûts, et la phrase « pilote descriptif, un organisme,
   une graine, deux générations, une espèce appelée ».
Lectures interdites : tout verbe de comparaison (« bat », « dépasse », « reste sous », « fait mieux / moins bien »)
entre un score et une référence, un autre score ou 0,5 ; tout adjectif ; toute différence calculée (g1 − g0, score −
référence) ; toute extrapolation aux organismes auto-écrits ou à Gemini ; toute mention de « apprentissage » ou de
« mémoire qui marche ».

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| tête citée sans le correctif de la faille des liens symboliques | le pilote ne part pas | commit `4967734a…` ancêtre du commit cité (`git merge-base --is-ancestor`) ; essais nommés en en-tête |
| GO-2026-10-24-07 non étendu au pilote, GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation indisponible, noyau non root | refus de lancer | gardes du noyau (`cli.lancer`) ; `test_mode_reel_refuse_sans_isolation_reseau_et_sans_root`, `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url` |
| appel de contrôle d'une espèce en échec (crédit, clé, en-tête, modèle servi) | la course ne part pas | lanceur de session-depot (essais sain et artefact) |
| plafond de 40 USD (course) ou de 20 USD (génération) | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total | `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_organisme_gourmand_recoit_plafond_sans_exception` |
| 1 200 s par génération | génération arrêtée, statut rapporté | `test_bac_a_sable_exception_et_delai` |
| modèle servi non conforme | génération `INVALIDE_MODELE`, lignée arrêtée | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| successeur invalide à g0 | g1 = relance de g0, consignée ; invalide à g1 : course finie | `test_relance_puis_reprise_remet_le_compteur_a_zero` |
| liens, tubes ou fichiers spéciaux posés par l'organisme | écartés et consignés ; lectures sans lien, bornées | essais du correctif (en-tête) |
| fichier `STOP` (incident technique seulement) | arrêt à la fin de la génération, consigné | `test_fichier_stop_arrete_la_boucle` |
| lecture hors des sorties par l'organisme, écriture dans la vue, processus détaché | refus par le système | `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` |
| arrêt humain du processus | par PID consigné au lancement (R10) | lanceur |

## Traitement des constats de la contre-lecture n° 1

| constat | traitement |
|---|---|
| PG-01 (bloquant) `--max-tokens-appel` absent | tête citée = `cd6c17b` ou après, où l'option existe (`test_plafond_de_jetons_par_appel`) ; dit sans effet sur cet organisme |
| PG-02 service de `test_final` | dit : 120 tâches mêlées, une caste, ≈ 123 appels |
| PG-03 ordre de `especes()` | dit : liste triée, Fable seule appelée ; rapporté par espèce |
| PG-04 statuts | liste complète, `TRONQUE` attendu ; audit si > 20 % hors `OK` |
| PG-05 R3 | une seule course ; `STOP` sur incident seulement ; aucune relance |
| PG-06 scores avant scellement | scores lus après le scellement de la v4 ; règles de la v7 déclarées inchangées en v8 ; dossier scellé non ouvert d'ici là |
| PG-07 lectures interdites | verbes de comparaison, adjectifs, différences, extrapolations interdits ; aucune différence calculée |
| PG-08 correctif des liens | commit et trois essais nommés ; ancêtre vérifié |
| PG-09 `--especes` vide | essai cité ; `boucle.py` jointe à la revérification |
| PG-10 GO | GO-2026-10-24-07, type calcul, extension au pilote à inscrire |
| PG-11 relance, empreintes de g1 | dits ; empreintes des arbres rapportées |
| PG-12 chiffres sans chemin | chemins et empreintes complètes ajoutés |
| PG-13 mission et chemins | `MISSION-v1.md` et chemins figés |
| PG-14 critère 1 | étendu à `test`, aux non-réponses par famille, aux statuts |
| PG-15 liste d'arrêt | temps, successeur invalide, PID, hôte ajoutés |
| PG-16 pièces | `memoire_isvd.py`, `boucle.py`, tests, `CORRECTIONS-v1.md` joints à la revérification ; déclaration R1 sur l'origine des corrections |
| PG-17 validateur | gabarits `<<…>>` (détectés par le validateur tant qu'ils ne sont pas remplis) ; empreintes de la contre-lecture 1 inscrites |
| PG-18 graine et manifeste | point 2 du plan |
| observations hors préenregistrement (docstring de `cli.py` ; « Version 2 » dans `principal.py`) | transmises à session-depot (ses fichiers ; l'organisme de Gemini n'est pas modifié pour ce pilote) |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (`claude-fable-5-1`, lancé par conv-audit, 24 octobre 2026, 21:54:52–22:06:48
  UTC) ; brouillon relu `pilote-gemini-organisme-v3-v1.md`,
  `3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf` ; rapport
  `prereg/contre-lectures/pilote-gemini-organisme-v3-v1-cl1.md`,
  `445a42489093cd84a02a86819d1039529417270565c4526d6134f201915a3807` ; verdict « scellable après corrections » ;
  traitement ci-dessus.
- **Revérification** — un second sous-agent neuf vérifie le traitement des 18 constats sur cette v2 avec `boucle.py`,
  `memoire_isvd.py`, les tests et `CORRECTIONS-v1.md` joints ; son rapport et ses deux empreintes sont inscrits ici au
  scellement, avec `<<COMMIT_PILOTE>>`, `<<ENTROPIE>>` et `<<GRAINE>>`.

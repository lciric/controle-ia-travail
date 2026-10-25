# Préenregistrement — second pilote descriptif : l'organisme écrit par Gemini (v5.1), seul, sur la banque scellée `confrontation-v1`, moisson ouverte, en deux courses avec une question ouverte posée à la génération 1 — v1

Brouillon à contre-lire (R2) ; aucun champ de scellement rempli. Second pilote après celui de l'objet v4
(`pilote-gemini-organisme-v4-question-v3.md`, `1c5b6f7db90caa1c5527f207fcc034163257459104f4d2b9a01d33df25eed79a`,
branche `outils/essaim-m3-gradient-v1-travail`, commit `2d01805a7c314ffd4ab72b46ea359dad483c298b`), dont la course est
partie le 25 octobre 2026 à 07:49 UTC et s'est arrêtée sur le crédit épuisé (rapport mécanique v2 et audit de symétrie :
`brouillons/canal-reprise-releve-v1/envois/rapport-pilote-gemini-organisme-v4-question-v1-mecanique-v2.md`,
`7136f5b9…`, et `audit-symetrie-pilote-gemini-v4-question-v1.md`, `35ade113…`, branche `canal/conv-audit-n04`, commit
`7d1feec550e3d3bdaf963ecade2cf1558b73e53f`). Ce texte reprend le dessin du premier (une lignée imposée, deux générations
notées, question posée à g001 seulement, sortie fermée, lectures interdites) ; ce qui change est dit à chaque section.

Décisions de Lazar (heure de Paris, 25 octobre 2026) : 01:45 — moissonneur : « (b) … goooo » (une v5 de Gemini avec
moissonneur et un second pilote plus tard) ; 09:07 — « (b) go » : la question du second pilote est la v2 « apprendre sa
structure… » posée à g1 ; 09:26 — « (a) go » : la v5.1 de Gemini, sur les faits mécaniques transmis ; 09:51 — « (c) Les
deux, en deux courses … : les deux » (une course avec la question v2, une avec la question écrite par Gemini) ; 09:58 —
la garde avant départ est un **test de dépense**, « car la recharge automatique est activée sur tous les modèles API » ;
10:17 — plafonds, option (b) : « 30 par génération, 60 par course, 120 au pire pour les deux, 8 192 jetons … : go ».
Lignée session-depot (relayée par Lazar, 10:22) : le second pilote est placé pendant son essai d'endurance de l'étape 1,
hors des bras A. But : voir ce que donne, sur les deux familles de tâches réelles, l'organisme v5.1 (code figé, mémoire
spectrale transmise, moisson documentaire servie par le noyau) ; répéter la chaîne réelle après les corrections du
premier pilote (crédit épuisé rendu en 400, plafonds de sortie, verrou, refus) avec statuts et coûts ; recueillir, comme
**matériau**, deux réponses de son essaim à deux questions ouvertes, posées avant qu'il ait vu quoi que ce soit de notre
part. **Aucune hypothèse n'est testée** ; tout est rapporté. Rien d'opposable (R7) ; aucune lecture de résultat avant
scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4).

- Auteur : lignée conv-audit. Date : 2026-10-25, 09:35 UTC (heure lue sur `date -u` ; les heures de Paris citées sont
  celles des messages de Lazar). Lanceur : lignée session-depot (clés), **dans son conteneur** (root, `unshare`
  disponible ; aucune instance payante), une course par appel du script
  `prereg/pieces-pilote2-gemini-v5-1/lancer_pilote2_gemini_v5_1_v1.sh` (empreinte citée au § Pièces), qui exécute le plan
  § 1 et § 3 pas à pas et refuse, avec sa raison consignée, à chaque écart ; processus consigné par son PID dans
  `LANCEMENT.md`, arrêt par PID (R10).
- **Deux courses**, dans cet ordre : **S** (`COURSE=structure`, nom `pilote2-gemini-v5-1-structure-v1`), puis **M**
  (`COURSE=maieutique`, nom `pilote2-gemini-v5-1-maieutique-v1`). Même objet, même code, même banque, mêmes bornes ;
  seules diffèrent la question et la graine. M part après la fin du lanceur de S ; si S a fini sur une garde de course
  (`CREDIT_EPUISE`, plafond total, `ANOMALIE_NOYAU`, refus du test de dépense), M ne part pas sans une nouvelle décision
  de Lazar, consignée.
- **Objet** : `gemini-organisme-v5-1` — branche `outils/gemini-organisme-v5-1`, commit
  `7f9cd2e5a8053dc45050e1b6316bf29ee0c62e0e`, dossier `outils/gemini-organisme-v5-1/organisme/`, **19 fichiers**, sans
  `memoire_isvd.json` ni `etat_generation_precedente.json` ni `__pycache__` (liste : `EMPREINTES-organisme-v1.txt` de la
  branche), empreinte d'arbre `50ffcd7d8cd3af059f2b881f3e565a8ad5829d8d325c39b9535bed6e01a8e12c` par
  `boucle.empreinte_arbre`, celle que le noyau consigne au manifeste. Famille nominale `gemini`. Lignée imposée unique,
  **sans phase de conception** (`--rondes-conception-max 0`), **G = 2** générations notées (g0, g1 ; g1 reçoit
  `memoire_isvd.json` et l'historique de g0 ; `--relances-max 1`). Provenance (`outils/gemini-organisme-v5-1/LISEZMOI-v1.md`,
  même branche) : reçue de Lazar le 25 octobre à 09:44 Paris (`livraison/recu-gemini-v5-1-v1.txt`, `49dc80c6…`),
  reconstituée sans exécuter le script de Gemini ; réponse à `DEMANDE-v5-1-faits-mecaniques-v1.md` (faits du premier
  pilote : troncatures au plafond de l'organisme, refus, verrou ; **aucune valeur suggérée**) ; ses plafonds de sortie
  (16 384 par tâche, induction et caste ; 24 576 pour la synthèse ; 8 192 pour la formulation des requêtes) sont les
  siens, rabattus par son code au `max_tokens_appel` du noyau. Corrections faites par nous avant tout run réel, sur
  simulation sans score réel : C-12 (verrou non réentrant, essai `tests/test_corrections_v3.py`), reprise telle quelle
  par Gemini ; aucune correction ne vient d'un résultat réel. **27 essais passés** en isolation ; reproductible d'un
  processus à l'autre (suites d'appels identiques pour trois graines de hachage) ; simulé sous le noyau `90595ffb` avec la
  question S et la moisson ouverte (pièces `verification-v1/` de la branche). **Déclarations** : le code de la v5.1 ne
  contient aucun texte des deux questions ; son code et sa documentation partagent du vocabulaire avec la question M
  (score « Bregman-Tsallis », vecteurs « de Koopman », mentions d'une expérience « pascalienne » que sa propre
  `CONCEPTION.md` dit sans pièce) ; la question M a été écrite par Gemini, concepteur de l'organisme.
- **Questions ouvertes** (posées par le noyau, `--question-ouverte … --question-ouverte-aux g001`, contrat § 7, à la
  **seule génération 1** ; à g0, `contexte["question_ouverte"]` vaut null) :
  - **S** : `question-apprendre-structure-entrainement-generations-organismes-v2.md`, branche `canal/conv-audit-n04`,
    commit `4772b525081342a6a30ba8823733aa5770a888a8`, `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` :
    un en-tête pour l'organisme puis le corps de la question posée au collisionneur (« structure » v2, `6906a1d1…`),
    sans aucune de ses réponses ;
  - **M** : `question-gemini-maieutique-vs-coercition-organismes-v1.md`, même branche, commit
    `7d1feec550e3d3bdaf963ecade2cf1558b73e53f`, `9e1da26de7c7951e0c9a319b12b99faaad7252f86dc14b0d85479696b4cc6595` :
    notre en-tête (mention qu'un autre modèle l'a écrite), puis le texte de Gemini **octet pour octet** (lignes 2100 à
    2104 de `livraison/recu-gemini-v5-1-v1.txt`, chevrons de citation retirés, empreinte du bloc seul
    `12a21131fea455f79915f1ccf5fccd228e9f84fbcb1d4c8f6b88bfab99fb8fa3`), puis notre pied (identique à celui de S). Ce
    texte nomme des sujets (dissimulation stratégique, « alignment faking », mutinerie) qui ont déclenché un refus de
    filtre au premier tour du collisionneur : un refus est un échec compté par l'organisme, **jamais reformulé**.
  La délibération n'entre dans aucune mémoire transmise à une génération notée ultérieure (il n'y en a pas).
- **Banque** : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json`,
  `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc` (80 / 60 / 60 ; `banque/LISEZMOI-v3.md`,
  `66855d2ab0d89d6fdea9bd85ff41005c7aa16c5f9e7f55cdc0c4fbff7f0299af`), inchangée depuis le premier pilote ; références
  de surface et vérification des étiquettes comme au premier pilote. **Mission** : `essaim-m3-refonte-v1/MISSION-v1.md`,
  `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e`. Les deux vérifiées par `sha256sum` avant le départ.
- **Code** : commit **`5d1d4fdb0dbd9e4d481ec3f4270555f4006df749`** de `outils/essaim-m3-gradient-v2-travail` (tête de
  session-depot le 25 octobre, 09:17 UTC : contient `4967734a…` (liens), `90595ffb…` (R-395 : crédit épuisé rendu en 400
  ou en erreur de flux sous 200, arrêt de la course), `c66f529e…` (R-398 : la réflexion comprise dans `max_tokens` dite au
  contrat), R-402 (**types de blocs de chaque réponse au journal des appels**, appels qui ont réfléchi comptés par
  l'extrait) et CL5-01 / CL5-02 (dépôt caché aux organismes, dossiers inscriptibles par tous rendus privés)). **140
  essais**, tous passés dans un conteneur du même type (conv-audit, root, 25 octobre, 09:22 UTC, `python -m pytest -q`,
  0 sauté, dont la recherche réelle sur arXiv). Le lanceur part d'une copie du dépôt dont `essaim-m3-refonte-v1/essaim_m3/`,
  `essaim-m3-refonte-v1/tests/` et `collisionneur-v2.5-banc-jev-travail/` sont identiques à ceux de `5d1d4fd`, au commit
  et dans l'arbre de travail ; les commits postérieurs n'ajoutent que ce texte et ses pièces (branche
  `outils/pilote2-gemini-v5-1-travail`, tirée de `5d1d4fd`) ; tout autre code vaut nouvelle version de ce texte. Le champ
  `commit` du manifeste sera la tête de la copie du lanceur ; c'est l'identité du code qui fait foi. Empreinte du code du
  noyau sans bytecode : `boucle.empreinte_arbre(essaim_m3/noyau)` =
  `d5d0efcc4677dd9957db3f324101b58e9475642e8e05926407579f056f653836` (calculée sur `git archive 5d1d4fd`) ; collisionneur
  `collisionneur_v2.py` = `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd`.
- **Espèces servies** : `["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON"]` (liste triée du noyau). Règles de
  l'organisme (`mitose_spectrale.py`, inchangé depuis la v4 sauf l'ordre des ensembles) : pour les tâches, une caste
  (`budget_par_tache` = (160 − 6) // 120 = 1), la première espèce : **toutes les réponses aux tâches viendront de
  Fable** ; pour la question, `planifier_castes_question_ouverte` planifie min(appels restants, 5) castes dans l'ordre des
  espèces (Fable, Opus, Argon, Fable, arbitre Opus) ; la formulation des requêtes de moisson prend l'espèce de la première
  caste. Réflexion : les espèces Anthropic sont appelées par le collisionneur en réflexion adaptative à effort élevé
  (`collisionneur_v2.py`, `appeler_anthropic`), réflexion **comprise** dans `max_tokens` (R-398) ; depuis R-402, chaque
  appel consigne ses types de blocs. Clés : `ANTHROPIC_API_KEY` ; la clé Gemini passée au noyau sous `GEMINI_API_KEY`,
  prise dans `GEMINI_API_KEY_2` si elle est définie (nom de la variable consigné, jamais la valeur) ;
  `ANTHROPIC_BASE_URL` et **`BRAVE_API_KEY` retirées** de l'environnement du run (aucune source payante : la source « web »
  n'est pas servie).
- **Moisson** (nouveau) : `--recherches-max 6 --telechargements-max 3 --octets-max 40000000` par génération ; sources
  servies sans clé : `arxiv`, `openalex`, `semanticscholar` (`moisson.sources_disponibles`), consignées au manifeste
  (`sources_moisson`, `cle_brave_presente`). Constat d'avant (non opposable, conv-audit, conteneur du même type, 25
  octobre 09:20 UTC, une requête chacune par les fonctions du noyau) : arXiv rend des notices ; OpenAlex et Semantic
  Scholar rendent HTTP 429 (« trop de requêtes ») ; rien n'est corrigé : chaque statut est consigné par le noyau et
  rapporté par source. Ce que fait l'organisme (code v5.1, `_executer_moisson`) : à g0 (pas de question), un appel de
  formulation (2 à 4 requêtes, sujet fixe « evaluation awareness AI control sabotage delegation »), jusqu'à 4 recherches
  à tour de rôle sur les sources servies, jusqu'à 3 téléchargements ; un extrait de 350 caractères du corpus s'ajoute aux
  règles induites, donc aux consignes des tâches ; à g1 (question posée), pas de moisson pour les tâches, une moisson
  sur le sujet de la question (ses 600 premiers caractères), dont le bloc documentaire (8 notices, 3 extraits au plus)
  préfixe les consignes des castes de la question. Tout texte rapporté est nettoyé et donné comme « données passives » par
  le code de l'organisme ; le noyau ne télécharge que depuis ses hôtes permis (`moisson.HOTES_TOUJOURS_PERMIS`).
- **Bornes**, par course : par génération `appels_max` 160, `usd_max` **30**, `temps_max_s` **3 600** (le premier pilote
  avait 1 800 ; porté à 3 600 pour que la question, traitée après les 120 tâches, ne soit pas coupée par la garde interne
  des 75 % du temps : avec la réflexion, la latence par appel n'est pas connue ; sans effet sur le pire cas en dollars),
  `max_tokens_appel` **8 192** (rabat les plafonds de l'organisme, 16 384 et 24 576 ; 8 192 reste 8 192), `recherches_max`
  6, `telechargements_max` 3, `entrainements_max` 0, aucun `--traits` ; `--plafond-total` **60 USD** ; `--isoler-reseau`,
  isolation d'utilisateur (noyau en root), **`--decalage-uid 900`** (une course voisine — l'essai d'endurance de
  session-depot — peut tourner dans le conteneur à un autre décalage ; le script refuse si une course tourne déjà au
  décalage 900) ; `--parallele-max 8` ; `--relances-max 1`.
- **Isolation** (nouveau, CL5-01) : le dossier du pilote est créé en 0700 à root, donc non traversable par les
  utilisateurs des organismes : l'espace des organismes va sous `/var/lib/essaim-m3/<16 premiers caractères de
  sha256(chemin absolu de la course)>` (`bac_a_sable.espace_organismes`), hors du dépôt ; le dépôt de la copie est donné
  au noyau dans `ESSAIM_M3_CACHER` (recouvert d'un système de fichiers vide en lecture seule dans l'exécution isolée) ;
  `/home`, `/root`, `/srv`, `/mnt`, `/media` le sont par défaut ; les dossiers inscriptibles par tous sont rendus privés
  (CL5-02) ; `ESSAIM_M3_ESPACE` doit être non définie. Essais : `test_cl5_01_banque_cachee_a_l_organisme`,
  `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`,
  `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`.
- **Service des tâches** : en génération notée, le noyau sert `test` et `test_final` **mêlés** (120 tâches, ordre tiré
  par la graine de la génération) ; g0 ≈ 124 appels (1 formulation de moisson, 1 induction, 2 vérifications, 120 tâches) ;
  g1 ≈ 123 appels de tâches puis jusqu'à 6 pour la question (1 formulation, 5 castes) : ≈ 129, sous 160.
- **Devis au pire cas** : 2 × 30 = 60 USD par course, **120 USD pour les deux** (aucun amorçage : lignée imposée), plus
  le test de dépense (≈ 0,002 USD par course au premier pilote). Ordre de grandeur attendu, **non opposable**
  (`prereg/pieces-pilote2-gemini-v5-1/devis-attendu-pilote2-v1.json`, script `devis_attendu_pilote2_v1.py`, entrées : le
  journal des appels de g000 du premier pilote, `journal-appels-g000.jsonl`, branche
  `pilotes/gemini-organisme-v4-question-v1`, commit `84b880a75be152289b1dd9c715e75a25e381c6fb`,
  `c24d0e55edbc77b3740c04718adccccf1d3d51ae1045260349a867b52ba1ca90` — 2 195 jetons d'entrée en moyenne sur les appels
  de tâche facturés —, les prix lus par `appels.modele_de`, Fable et Argon 10 USD par million de jetons d'entrée et 50
  en sortie, Opus 4 et 20) : la sortie par appel, réflexion comprise, est **inconnue** (c'est ce que le pilote mesure) ;
  ≈ 18 USD la course à 1 000 jetons de sortie par appel de tâche, ≈ 31 à 2 000, ≈ 44 à 3 000 ; au-delà de ≈ 3 600 jetons
  (8 appels en vol) à ≈ 4 100 (un seul), le plafond de g1 peut refuser des appels de la question (`PLAFOND`) ; au-delà de
  ≈ 4 700, celui de g0 coupe des tâches. Sous **GO-2026-10-24-07** (« préparatifs », type calcul, 200 USD, échéance
  2026-10-26), **étendu à ce pilote sur le mot de Lazar dans la session de session-depot** (R-373) : avant chaque course,
  **deux écritures et une vérification** — session-depot inscrit l'extension dans `registres/go.md` (une ligne qui
  commence par `| GO-2026-10-24-07 |` et porte, sur cette même ligne, le type calcul et le nom de la course ; une ligne
  nouvelle, le registre n'est jamais réécrit), consigne la course dans `registres/depenses.md` (une ligne qui nomme la
  course et `GO-2026-10-24-07` ; 60 USD au pire cas) et déclare au script le **reste disponible sur la ligne, ≥ 60 USD**
  (après tout ce qui y est déjà imputé, la course précédente comprise) ; sans elles, la course ne part pas.
- **Test de dépense** (nouveau, décision de Lazar 09:58) : la recharge automatique du compte Anthropic étant active, un
  appel de solde ne dirait rien ; à sa place, **un appel payant par espèce**, fait par l'outil d'appel de contrôle de
  session-depot au plus **15 minutes** avant le départ de chaque course ; le script lit sa pièce (JSON) et exige, pour
  chacune des trois espèces, `statut` `OK`, `modele_servi` conforme (`claude-fable-5-1`, `claude-opus-5-5`,
  `gemini-4-argon`), `cout_usd` > 0, `go` = `GO-2026-10-24-07`, et un âge ≤ 900 s (date du fichier) ; et l'attestation
  de Lazar (« recharge automatique active », avec l'heure) est consignée telle quelle dans `LANCEMENT.md`. **Réserve
  dite** : la recharge automatique retire le plafond externe que formait le solde au premier pilote ; les plafonds du
  noyau (`--plafond-total`, `--usd-par-generation`, réservation au pire cas des appels en vol) et l'arrêt sur crédit
  épuisé (R-395) deviennent le seul frein à la dépense — d'où leurs essais cités, exigés passés dans le conteneur ; si
  la console du compte porte un plafond mensuel de recharge, sa valeur est consignée sur la parole de Lazar (non
  vérifiée par nous).

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté, **par course** : (1) mécanique — statut d'exécution de chaque génération
(`OK`, `EXCEPTION`, `DELAI_DEPASSE`, `SANS_STATUT`, `STATUT_ILLISIBLE`, `ISOLATION_INDISPONIBLE`, `INVALIDE_MODELE`,
`ANOMALIE_NOYAU`, `CREDIT_EPUISE`), appels par espèce et par rôle, statuts des appels (`OK`, `TRONQUE`, `VIDE`, `REFUS`,
`ANOMALIE`, `ECHEC_API`, `PLAFOND`, `ARRET_NOYAU`, `MODELE_NON_CONFORME`), **types de blocs par appel et appels qui ont
réfléchi par statut** (R-402), jetons d'entrée et de sortie par appel (journal), coût réel contre plafond, durées,
recherches et téléchargements **par source et par statut**, castes planifiées (tâches et question), taille de
`memoire_isvd.json`, relance éventuelle, empreinte de l'archive de l'organisme à g0 et g1 (identité du code de g1 avec
celui de g0 vérifiée après le moment du plan § 3, comme au premier pilote), éléments écartés par le dépôt, nombre total
de réponses valides (`n_reponses_test`) ; (2) la **réponse à la question ouverte** : si elle a été lue (`reponse` vrai ou
faux, raison), ses octets et son empreinte, le texte **tel quel** et sa structure mécanique (sections présentes, bloc
ORGANISATION : appels, castes, votes et confiances déclarés par l'organisme, documents moissonnés cités) ; (3) scores —
exactitude équilibrée par famille sur `test` et sur `test_final`, aux générations 0 et 1, dans une table où figurent
aussi les références de surface ; calibration (Brier borné, erreur de calibration) ; part de tâches sans réponse valide
par famille. **Aucune différence n'est calculée ni nommée** (ni g1 − g0, ni score − référence, ni S − M, ni second
pilote − premier) ; **les réponses aux questions ne sont ni notées, ni jugées, ni comparées entre elles** : c'est du
matériau, rapporté avec sa provenance.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Rien n'est écrit sur ce que « devrait » donner cet organisme, ni sur ce que ses
réponses « devraient » dire, ni sur l'effet de la moisson ou des plafonds.

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1, faux).
Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, calculé par le noyau en fin
de génération (`juge/score-final.json`), lu par personne avant le moment fixé au plan § 3. La question ouverte n'a
aucune métrique (le score est calculé avant la lecture de la réponse ; essai
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`).

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 60 USD par course, 30 par génération ; 3 600 s par
génération ; un appel `MODELE_NON_CONFORME` invalide la génération et arrête la lignée ; un crédit épuisé (HTTP 402, ou
« credit balance is too low » en 400 ou en erreur de flux sous 200 : `CREDIT_EPUISE`) invalide la génération et arrête la
course ; un journal d'appels absent après des appels (`ANOMALIE_NOYAU`) invalide la génération.

## Plan d'analyse

1. **Une seule course de chaque nom** (R3), S puis M. Une course **part dès que son manifeste est écrit** ; après, jamais
   de seconde course de ce nom, quelle que soit l'issue. Avant (tout refus ou toute exception avant le manifeste), une
   nouvelle tentative de la même commande est permise, dans un nouveau dossier (`…-tentative2`, R12), après correction
   de l'environnement, jamais de ce texte (même règle et mêmes vérifications qu'au premier pilote : dossiers vides
   laissés, sinon `refus-avant-manifeste-v1.tar.gz`, jamais lu). En mode réel, le script refuse toute variable d'essai
   et `ESSAIM_M3_ESPACE`, refuse si une course du noyau tourne au décalage 900, et consigne les courses voisines
   détectées (PID ; aucune n'est arrêtée). Dossier du pilote : `PILOTE` = `essaim-m3-refonte-v1/pilotes/<nom de la course>/`
   dans la copie du dépôt du lanceur (nouveau, créé en 0700). Étapes, toutes faites par le script, chacune consignée dans
   `$PILOTE/LANCEMENT.md` : (i) code identique à `5d1d4fd` (commit et arbre de travail, `essaim_m3`, `tests`,
   collisionneur), `4967734a…` et `90595ffb…` ancêtres ; banque, mission et collisionneur par `sha256sum` ; (i bis)
   dossier du pilote « 700 0 » (mode, propriétaire) ; (ii) préenregistrement scellé (empreinte donnée, compagnon conforme,
   graine de la course écrite dedans, aucun marqueur, empreinte du lanceur citée) ; (iii)
   `$PILOTE/outils/gemini-organisme-v5-1/organisme/` = `git archive 7f9cd2e… outils/gemini-organisme-v5-1/organisme`
   (`50ffcd7d…`, 19 fichiers) ; `$PILOTE/question.md` = `git show <commit de la question>:<chemin>` (S : `a54da93e…` ; M :
   `9e1da26d…`) ; (iv) `$PILOTE/registre-go.md` = `registres/go.md` d'`origin/main` après l'inscription ; dépense
   consignée dans `origin/main:registres/depenses.md` ; reste déclaré ≥ 60 USD ; (v) test de dépense lu et vérifié (voir
   plus haut), copié en `test-depense-<nom>.json`, attestation de la recharge consignée ; (vi) essais en root, depuis
   `essaim-m3-refonte-v1/` : `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --junitxml
   $PILOTE/essais-v1.xml` ; exigés : aucun échec, **aucun saut** (l'essai de recherche réelle sur arXiv compris : la
   moisson doit joindre au moins arXiv), passés + désélectionnés = 140, et chacun des essais cités dans la liste d'arrêt
   passé ici ; (vii) nettoyage des `__pycache__` (noyau, essais, collisionneur ; gardé par prudence : depuis le constat n° 30 § 5,
   `boucle.empreinte_arbre`, donc aussi le `sha256_code_noyau` du manifeste, écarte le bytecode), puis
   `boucle.empreinte_arbre(essaim_m3/noyau)` sous `python -B` = `d5d0efcc…` ; (viii) en root, `PYTHONDONTWRITEBYTECODE=1`, `ESSAIM_M3_CACHER=<dépôt>`, clés
   exportées, `ANTHROPIC_BASE_URL`, `BRAVE_API_KEY` et `ESSAIM_M3_ESPACE` retirées de l'environnement du run, depuis
   `essaim-m3-refonte-v1/` :
   `python -m essaim_m3 lancer --reel --go GO-2026-10-24-07 --registre-go "$PILOTE/registre-go.md" --taches
   banque/banque-confrontation-v1.json --mission MISSION-v1.md --sortie "$PILOTE/course" --generations 2 --graine <graine
   de la course> --especes --appels-max 160 --usd-par-generation 30 --temps-max 3600 --max-tokens-appel 8192
   --recherches-max 6 --telechargements-max 3 --octets-max 40000000 --entrainements-max 0 --rondes-conception-max 0
   --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 60 --decalage-uid 900 --question-ouverte
   "$PILOTE/question.md" --question-ouverte-aux g001 --organisme-impose
   "gemini-organisme-v5-1=$PILOTE/outils/gemini-organisme-v5-1/organisme@gemini" > "$PILOTE/ferme/sortie-standard-lanceur.txt"
   2> "$PILOTE/sortie-erreur-lanceur.txt"` (`--especes` vide : aucune lignée auto-écrite ; les trois espèces restent
   servies à l'organisme imposé). Un fichier `STOP` dans `$PILOTE/course/` n'est posé que pour un incident technique
   (panne, coût anormal lu dans le journal des appels), consigné ; jamais au vu d'un score.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` ; deux enfants
   `numpy.random.SeedSequence(E).spawn(2)` ; graine de chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`,
   l'enfant 0 pour S, l'enfant 1 pour M (chaque égalité sur une seule ligne, lue par le lanceur) :
   graine de la course structure = <<GRAINE_STRUCTURE>>
   graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>
   Le manifeste de chaque run consigne sa graine, la version de numpy,
   `sha256_code_noyau` et `commit` ; E n'est consignée qu'ici.
3. **Moment de la lecture des scores (R1)** — comme au premier pilote, fichier par fichier : la **sortie standard** (qui
   porte les scores, `cli.py`) va dans `$PILOTE/ferme/`, jamais lue ; la **sortie d'erreur** va dans
   `$PILOTE/sortie-erreur-lanceur.txt`, lisible : au commit cité, le noyau n'y écrit que des refus d'avant le manifeste
   (`cli.py`, 20 `print(…, file=sys.stderr)`, tous « refus : … », « mode réel non demandé » ou « espèce inconnue ») et,
   en cas d'exception, la trace Python ; l'outil d'extraction n'y écrit que « refus : … » ; ni `logging` ni `warnings`
   dans `essaim_m3/noyau/`, `essaim_m3/__main__.py` et l'outil (vérifié par recherche au commit cité). **Pendant la
   course**, le lanceur ne consulte que le journal des appels de la génération en cours, par son chemin exact,
   `<espace>/travail/gemini-organisme-v5-1/gNNN.noyau/journal-appels.jsonl` (statuts, espèces, coûts, types de blocs ;
   aucun score), où `<espace>` est consigné au manifeste (`espace_organismes`) ; ni la liste de ce dossier ni
   `gNNN.noyau/appels/`. **Dès la fin**, sont lisibles et seulement eux : (a) `$PILOTE/extrait-mecanique-v1.json`
   (`python -m essaim_m3.outils.extrait_mecanique`, au commit cité : listes closes de champs, comptes par statut des
   recherches par source et des téléchargements, appels qui ont réfléchi par statut ; jamais de score) ; (b) la
   réponse, `course/archive/gemini-organisme-v5-1/g001/reponse-question.md`, recopiée en `$PILOTE/reponse-question-g001.md`
   (vrai compagnon de la copie, compagnon d'origine en `.sha256-archive`) ; (c) les journaux d'appels archivés,
   recopiés en `$PILOTE/journal-appels-gNNN.jsonl` ; (d) `sortie-erreur-lanceur.txt`, `LANCEMENT.md`, `essais-v1.*` ;
   (e) les entrées poussées en clair : `question.md`, `registre-go.md`, `test-depense-*.json`,
   `outils/gemini-organisme-v5-1/organisme/`, `.gitignore`, `A-POUSSER-v1.txt` et les fichiers d'empreintes. **Canal
   latéral dit et accepté** (comme au premier pilote) : la taille de `contexte.json` de g001 dépend de la longueur
   d'écriture du score `test` de g0 ; personne ne la calcule ni ne la met en rapport avec quoi que ce soit. **Ce que la
   réponse (b) peut contenir** : jamais une vérité de `test` ni de `test_final`, ni un score du juge — l'organisme reçoit
   à g1 le score `test` de g0 (dans `historique`), mais le code de la v5.1 ne passe `historique` qu'à
   `planifier_castes_question_ouverte`, qui n'en tire que la pression d'exploration (nombre de castes) ; ni les consignes
   des castes, ni la formulation des requêtes de moisson, ni le fichier écrit n'en contiennent rien (`principal.py`,
   `_traiter_question_ouverte` et `_executer_moisson` ; vérifié par lecture au commit `7f9cd2e`). **Expositions dites et
   acceptées** : le résumé de la mémoire spectrale (jusqu'à 4 exemplaires de ≤ 220 caractères, qui peuvent être une
   vérité d'entraînement ou le début du raisonnement de g0 sur une tâche de `test` ou de `test_final`) entre dans les
   consignes des castes et de la formulation des requêtes, et peut être cité dans la réponse ; des titres, auteurs,
   résumés et extraits de documents moissonnés peuvent y figurer ; personne ne les confronte aux vérités de la banque
   avant le moment ci-dessous. **Jusqu'à ce que le préenregistrement de l'étape 1 qui part (v8 ou suivante) soit scellé,
   et qu'il soit inscrit que la v8 de la confrontation ne change ni la table de lecture de H-E1, ni les seuils, ni les
   règles de lecture de la v7 (`74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`)**, personne ne lit,
   notamment : la sortie standard, `rapport-v1.json`, `evenements.jsonl`, `archive/index.jsonl`, les `resume.json`, les
   `juge/`, `banque.json`, `lignees/`, `archive/*/gNNN/organisme.tar.gz`, `archive/*/gNNN/travail/` (dont
   `noyau/appels/`, `corpus/`), et dans `<espace>` : `archive_vue/`, `travail/*/gNNN/`, `gNNN.noyau/appels/`. **Fermeture
   mécanique** : le script fait de `course/`, `ferme/` et `<espace>` (sous `/var/lib/essaim-m3/`) une seule archive
   `$PILOTE/ferme.tar.gz` (+ `.sha256`), sans l'ouvrir, vérifie le nombre d'entrées contre le disque, puis retire les
   copies ouvertes (sinon réserve consignée). **Poussé en clair**, et seulement : les fichiers de
   `$PILOTE/A-POUSSER-v1.txt`, liste fermée par noms écrite par le script, sur une branche `pilotes/<nom de la course>`,
   jamais `main` ; `course/` et `ferme/` jamais ajoutés (`.gitignore` écrit avant la course). Tout changement des règles
   de lecture de la v7 rouvrirait R1 pour ce pilote. Déclaration : aucun score de ce pilote ne motive aucun changement
   des préenregistrements principaux ; la v8 de la confrontation citera les empreintes des deux `ferme.tar.gz` et des
   deux `EMPREINTES-pilote-v1.txt` pour le montrer. L'étape 1 est scellée avant le départ de ce pilote : elle ne peut rien
   en tirer.
4. **Lecture** : après le moment du point 3, ouverture des deux `ferme.tar.gz` ; par course, tableau rapporté : famille ×
   génération × {score `test`, score `test_final`, référence de surface, Brier, part sans réponse}, plus appels par
   espèce, par rôle et par statut, jetons, appels qui ont réfléchi, coûts, durées, moisson par source et par statut,
   castes, taille de mémoire, empreintes des archives et identité du code de g1, relance, éléments écartés ; les deux
   réponses, telles quelles, avec leur structure mécanique ; les deux courses dans deux tableaux distincts. Rédigé par
   conv-audit, relu par session-depot ; aucune lecture de verdict (R13 sans objet : ce n'est pas une porte).
5. **Ce que ce pilote ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini (un organisme, une graine par course, deux générations, deux familles,
   une seule espèce appelée pour les tâches) ; rien sur l'effet de la moisson, des plafonds ou de la question (aucun bras
   témoin) ; rien sur la valeur d'une question contre l'autre ; ses scores sont des points, pas des estimations, et
   n'entrent dans aucun critère des préenregistrements principaux ; chaque réponse est l'avis d'un essaim d'une
   conception, à une graine : un matériau parmi d'autres (réponses du collisionneur, des organismes auto-écrits à
   venir), jamais une consigne au noyau ni aux organismes, jamais servie à un organisme.

## Critères de lecture gelés

1. Pour chaque course : score d'une famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations ;
   ou part de tâches sans réponse de 100 % pour une famille ; ou plus de 20 % d'appels hors `OK` à une génération ; ou une
   génération en statut autre que `OK` ; ou aucune recherche `OK` à une génération où l'organisme en a demandé → **audit
   de symétrie (R4)** avant tout rapport, **sans relance**, par un **sous-agent neuf** lancé par conv-audit, qui n'a ni
   écrit ce texte ni lu les scores avant l'audit ; rapport scellé. Les déclencheurs mécaniques se lisent dès la fin dans
   l'extrait ; un audit qui doit lire un fichier fermé se fait après le moment du point 3 ; d'ici là, son matériau se
   limite aux fichiers lisibles (a)–(d).
2. Question, pour chaque course : (i) g1 n'a pas tourné → « question non posée : g1 n'a pas tourné », avec la raison lue
   dans l'extrait ; (ii) `reponse` faux avec `probleme` autre que « absent » → refus du noyau rapporté avec la raison ;
   (iii) `reponse` faux et « absent » → « l'organisme n'a pas écrit de réponse » ; (iv) réponse d'une génération g1
   invalidée → texte rapporté tel quel, avec la mention « réponse d'une génération invalidée (statut …) » ; (v) réponse
   lue → texte rapporté tel quel, y compris le texte d'abstention ou le texte minimal de l'organisme ; les appels de la
   question refusés par le plafond (`PLAFOND`) ou par un filtre (`REFUS`) sont comptés et dits.
3. Sinon → **rapporté tel quel** : les tableaux, les statuts, les coûts, les réponses, et la phrase « pilote descriptif,
   un organisme, deux courses à une graine chacune, deux générations, une espèce appelée pour les tâches, une question
   posée une fois par course ».
Lectures interdites — dans la prose du rapport (la citation des questions et des réponses n'est pas visée) : tout verbe
de comparaison (« bat », « dépasse », « reste sous », « fait mieux / moins bien ») entre un score et une référence, un
autre score, 0,5, l'autre course ou le premier pilote ; tout adjectif sur un score ; toute différence calculée ; toute
extrapolation aux organismes auto-écrits ou à Gemini ; toute mention de « apprentissage » ou de « mémoire qui marche » ;
tout jugement d'une réponse (« bonne », « profonde », « fausse », « meilleure que l'autre ou que le collisionneur ») ;
toute mise en rapport d'une réponse avec les scores ; tout lien de cause entre la moisson, les plafonds ou la question et
un score. Les nombres et les références que contient une réponse sont rapportés comme **dires de l'essaim, non vérifiés**
(R7) ; une référence n'entre dans aucun texte avant vérification sur PDF empreinté, page citée.

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| une course de ce nom déjà partie (manifeste écrit) dans un dossier du pilote ; dossier de la tentative existant | la course ne part pas (R3, R12) | script, consigné |
| code différent de celui de `5d1d4fd` (commit ou arbre de travail, collisionneur compris), fichier non suivi, `4967734a…` ou `90595ffb…` non ancêtre, noyau nettoyé ≠ `d5d0efcc…`, banque ≠ `f1387a20…`, mission ≠ `bd2c6a15…`, collisionneur ≠ `213b52ef…` | la course ne part pas | script, consigné ; `sha256_code_noyau` du manifeste rapporté de l'extrait |
| dossier du pilote autre que « 700 0 » ; `ESSAIM_M3_ESPACE` définie en réel | la course ne part pas | script (essayé) |
| préenregistrement d'empreinte autre, compagnon absent, graine de la course non écrite, marqueur restant, empreinte du lanceur non citée | la course ne part pas | script |
| organisme ≠ `50ffcd7d…` ou 19 fichiers non retrouvés ; question ≠ son empreinte | la course ne part pas | script ; le manifeste reconsigne l'empreinte d'arbre et celle de la question |
| GO-2026-10-24-07 non étendu à la course dans `registres/go.md`, course non consignée dans `registres/depenses.md`, reste < 60 USD | la course ne part pas | vérification du lanceur, consignée |
| test de dépense absent, vide, illisible, vieux de plus de 900 s, une espèce non `OK`, modèle servi non conforme, coût nul, autre GO ; attestation de la recharge vide en réel | la course ne part pas | script (essayés) |
| un échec d'essai, un saut quelconque (la recherche réelle sur arXiv comprise), un total ≠ 140, un essai cité non passé dans ce conteneur | la course ne part pas | script (rapport JUnit) |
| course du noyau déjà en cours au décalage 900 ; variable d'essai en réel | la course ne part pas (elle attend) | script (essayés) ; courses voisines à un autre décalage : consignées, jamais arrêtées |
| GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation réseau indisponible, noyau non root, clés absentes | refus de lancer (avant le manifeste : tentative suivante permise) | gardes du noyau et du script, comme au premier pilote ; essais `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`, `test_bac_a_sable_isolation_reseau_refusee_si_indisponible` ; collisionneur et isolation vérifiés après départ par l'extrait |
| plafond de 60 USD (course) ou de 30 USD (génération) | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total | `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste` |
| 3 600 s par génération | `DELAI_DEPASSE` ; garde interne de l'organisme à 75 % du temps | `test_bac_a_sable_exception_et_delai`, `test_ce311_garde_de_temps_compte_la_moisson` |
| modèle servi non conforme | `INVALIDE_MODELE`, lignée arrêtée | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| crédit épuisé (402 ; « credit balance is too low » en 400 ou sous 200) | `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance ; M ne part pas sans nouvelle décision | `test_ce305_credit_epuise_arrete_la_course`, `test_r395_credit_epuise_rendu_en_400_arrete_la_course` |
| journal des appels absent après des appels | `ANOMALIE_NOYAU` invalidée | `test_ce307_anomalie_journal_absent` |
| successeur invalide à g0 | g1 = relance de g0, consignée | `test_relance_puis_reprise_remet_le_compteur_a_zero` |
| liens, tubes ou fichiers spéciaux posés par l'organisme | écartés et consignés | `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` |
| lecture du dépôt ou de la banque par l'organisme ; voie commune entre courses | refus par le système (dépôt recouvert, dossiers inscriptibles privés) | `test_cl5_01_banque_cachee_a_l_organisme`, `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` |
| moisson : source injoignable, 429, document trop gros | statut consigné par le noyau, rapporté par source ; aucune relance | `test_moisson_de_bout_en_bout_en_simulation`, `test_ce305_sources_moisson_au_manifeste_et_bras_apparie`, `test_sources_reelles_de_moisson_si_reseau` |
| fichier `STOP` (incident technique seulement) | arrêt à la fin de la génération, consigné | `test_fichier_stop_arrete_la_boucle` |
| archive fermée incomplète | copies gardées, jamais lues ni poussées ; réserve | script |
| arrêt humain du processus | par PID consigné (R10) | lanceur |

Essais cités (chacun exigé passé dans le conteneur du lancement) : `test_fichiers_lecture_et_copie_sans_lien`,
`test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau`,
`test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts`,
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`,
`test_extrait_mecanique_sain_puis_artefacts`, `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`,
`test_bac_a_sable_isolation_reseau_refusee_si_indisponible`, `test_appels_paralleles_plafond_tenu_au_pire_cas`,
`test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste`,
`test_bac_a_sable_exception_et_delai`, `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee`,
`test_ce305_credit_epuise_arrete_la_course`, `test_ce307_anomalie_journal_absent`,
`test_relance_puis_reprise_remet_le_compteur_a_zero`, `test_fichier_stop_arrete_la_boucle`,
`test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`,
`test_r395_credit_epuise_rendu_en_400_arrete_la_course`, `test_cl5_01_banque_cachee_a_l_organisme`,
`test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, `test_sources_reelles_de_moisson_si_reseau`,
`test_moisson_de_bout_en_bout_en_simulation`, `test_ce311_garde_de_temps_compte_la_moisson`,
`test_ce305_sources_moisson_au_manifeste_et_bras_apparie`,
`test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait` (27).

**Essais du lanceur** (R5 ; conv-audit, 25 octobre, 09:29–09:37 UTC, root, conteneur du même type, copie du dépôt à
`5d1d4fd`) : cas sain S complet (essais du noyau exécutés : 140 passés, 0 sauté ; deux générations ; réponse archivée ;
archive fermée de 1 557 entrées égale au disque ; copies retirées ; espace sous `/var/lib/essaim-m3/` ; utilisateur de
l'organisme 60900 ; `/tmp` rendu privé), cas sain M (rapport JUnit du cas S repris) et 47 artefacts, **49 sur 49
conformes** (`essais-lanceur-pilote2-v1.log`, `206e3592457d4ce411b4b8b973728fb4ff28ebc0c057cb1bc78678a637667c1e` ;
programme `essais_lanceur_pilote2_v1.sh`, `3b0d1985166ad7845bd2eb1a00ffae75e581f27f7cc176c7cd87f3266c749076`) : en mode
réel, refus avant tout appel (variable d'essai, `ESSAIM_M3_ESPACE`, clé Anthropic, clé Gemini, attestation vide) ; course
ou mode inconnus ; course voisine au décalage 900 (refus) et à un autre décalage (consignée, course partie) ; commit de
la question absent ; arbre de travail modifié (noyau, collisionneur) ; fichier non suivi ; tête de code différente ;
banque ; mission ; dossier du pilote traversable ; préenregistrement d'autre empreinte, sans compagnon, sans la graine,
graine de l'autre course, marqueur restant, lanceur non cité ; organisme altéré, fichier manquant ; question altérée ;
ligne du GO sans « calcul », « calcul » et nom sur deux lignes ; dépense non consignée ; reste < 60 ; test de dépense
vide, vieux de 20 minutes, statut `ECHEC_API`, modèle servi autre, coût nul, autre GO, JSON illisible ; essai en échec,
saut de l'essai arXiv, total ≠ 140 ; bytecode posé sous le noyau (traité : empreinte inchangée, la fonction l'écarte) ;
refus du noyau après création de `course/` (famille inconnue), puis tentative 2 partie, puis tentative 3 refusée (R3) ;
archive fermée incomplète (copies gardées) ; espace hors de `/var/lib/essaim-m3` (réserve consignée) ; fichier imprévu
(consigné, non poussé). Pièces des cas sains : `simulation-lanceur-v1/` (`LANCEMENT-simulation-{structure,maieutique}-v1.md`,
`extrait-mecanique-simulation-{structure,maieutique}-v1.json`, `reponse-question-g001-simulation-{structure,maieutique}-v1.md`,
`A-POUSSER-simulation-{structure,maieutique}-v1.txt`, chacune avec son `.sha256`) ; les textes de ces réponses sont ceux
des doubles de simulation et ne disent rien de ce que diront les modèles réels. Gardes restées sans artefact : la sortie
de `tar` en erreur (simulée par l'archive incomplète) ; un refus avant le manifeste qui laisserait des fichiers ordinaires
(aucune voie connue du noyau n'en écrit).

## Pièces

`prereg/pieces-pilote2-gemini-v5-1/` : le lanceur `lancer_pilote2_gemini_v5_1_v1.sh`
(`a26d508f8f0953786d7f44ce8acada9660594465a6e29157a22b0d58f0fcf35a`), le devis `devis-attendu-pilote2-v1.json`
(`82fc4dc665002cc7b4f1f152e596013d952d177f0f1fbabb5117ff6d5c7260f8`) et son script `devis_attendu_pilote2_v1.py`
(`2c3a63e95c7e72a739a4f325d8728c73ca4bfd63894734bc8d7d37d0e3b57260`), les essais du lanceur ci-dessus ; chaque pièce
a son `.sha256` ; fichier d'empreintes `EMPREINTES-pilote2-gemini-v5-1-v1.txt` (+ `.sha256`), écrit au scellement :
<<EMPREINTE_PIECES>>.

## Contre-lecture

À faire (R2) : sous-agent neuf, qui n'a écrit aucune pièce ; rapport dans `prereg/contre-lectures/`.

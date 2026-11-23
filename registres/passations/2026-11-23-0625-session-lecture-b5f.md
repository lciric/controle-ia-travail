# Passation — session de lecture du barreau 5 (« sabotage ou empreinte de l'adaptateur ») — 2026-11-23, 06:25Z

Écrite sur le mot de Lazar GO-2026-11-23-09, relayé par la mère à 06:23Z : reprendre au même point sur un autre compte, sans perte. Une machine à moi tourne : elle n'est pas arrêtée.

## Qui, avec qui
- Session : `session_013QMayiuN339pSspJBRTwYL` (Opus 5.5), rôle aveugle de **session de lecture**.
- Interlocuteurs : le conducteur `session_013QMayjM1PQPWkLifMw9HDR` (ma session mère directe) et la mère en poste `session_013QMayjbmQUdDuDs2S3i3XD`, qui inscrit les lignes des registres et donne les signaux de création.
- Exclu, maintenant et plus tard : ouvreur, lecteur du verdict, agent de l'audit de symétrie (liste « qui a lu quoi » v21).

## Mandat (dans l'ordre où le dernier prime)
Toutes les pièces sont dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/` :
- erratum 4 `mandat-session-lecture-b5f-v2-erratum-4.md` (`1c505d6f…`, sur `conducteur-b5f/lecture-v1`) ;
- erratum 3 (`1c9d9ce1…`), erratum 2 (`4d1678b5…`), erratum 1 (`cde0279c…`) ;
- mandat v2 (`b1eb2afc…`).

Mon plan de marche et ses errata :
- `plan-de-marche-session-lecture-b5f-v1.md` (`88c8cf8a…`) ;
- erratum 1 (`7920172e…`) ;
- erratum 2 (`3659365f…`).

Règles qui tiennent toujours :
- aucun score, aire, statistique ni grandeur d'adaptateur, vu ou rendu ;
- jamais la table, le sel, ni la branche de la formation ;
- sur les branches de sortie, je n'ouvre que le journal et `inventaire-final.json` ;
- clés par leur nom seul.

## Fait
1. **Phase 1** : vérifications d'empreintes, du registre propre, essais, plan de marche. Les détails sont dans le plan et ses errata.
2. **Répétition générale**
   - Instance 62036317, créée à 20:43:41Z le 22 ; marche menée au bout.
   - Versement final prouvé au commit `c5c77d5b351cf2c24e4440700d1eb3ca534670d1` de `donnees/barreau5-familles-jumelles-v1-repetition` (inventaire final `3f44f1be…`, 397 fichiers).
   - Détruite à 22:10:10Z, absence prouvée. Dépense ≈ 1,71 USD au plus.
3. **Relecture décisive, première tentative**
   - Instance 62047649, tombée avant la marche : « commit des entrées … introuvable ». Le clone partiel des entrées perdait son identification ; c'est le défaut de l'amorce figée, l. 362-364.
   - Traces prouvées au commit `254f9280…`, copiées par le conducteur sous `traces/barreau5-lecture-tentative-1`.
   - Détruite sur mot de la mère, écart déclaré. Dépense ≈ 0,08 USD.
4. **Relance, faux échec**
   - Instance 62094971, code v3 et amorce corrigée `0adb6efb…`. La marche avait commencé (04:34:21Z).
   - **Ma veille l'a arrêtée à tort à 04:35:03Z** : elle lisait la sortie de données en octets comme des Go.
   - Décision de la mère R-5117 : faux échec, issue « jamais parti ».
   - Traces versées au commit `28a1d0f995806de68f100b84aaa4939efd384a6a` de `traces/barreau5-lecture-tentative-2`.
   - Détruite à 04:39:02Z, absence prouvée. Dépense ≈ 0,22 USD.
   - Veille corrigée et essayée par écrit : `veille-session-lecture-v2/` (`veille-v2.sh` `a468e0ae…`, essai `6131e0e9…`, sortie `873a431c…`).
5. **Reprise de la relecture décisive, EN COURS**
   - Instance **62096662** (`b5f-lecture-v1`), offre 32744972 (machine 22952), 1,26 USD de l'heure, créée à **2026-11-23T04:40:54Z**.
   - Marche `20261123-044043-b5f-lecture`, commencée à 04:54:39Z.
   - Commit de la marche `efc3f8350ebcbc84658c726f742c8b8e0374eee3` (`marche-b5f/lecture-v2`), code de commande v3 `423496d4b8ee5c19d1849545bdba659e9c9c7e0c` (`course/barreau5-commande-lecture-v3`).
   - Entrées `f6e2072dc4cce95059e7590ae4e39cc4881729fc` ; `une_sur_dix` ; DIVERGENCE 1 ; points d'ancrage `EXISTANTS-decisif.json` (`6ac2e457…`).
   - Ligne d'engagement inscrite à 04:40:13Z (R-5118, `main` `2bd29a2c0`).
   - Cumul relevé ≈ 2,12 USD à 06:21Z.
   - **Coupure à 14 USD vers 15:32:34Z** (cumul plus un quart d'heure). Troisième rempart de la mère : arrêt seul, sans destruction.
   - Échéance de l'instance, calculée par le code sur 21 USD : 21:05:45Z ; minuterie à 21:20:45Z.

## Reste
1. Attendre la fin de la marche de 62096662.
   - Le journal doit porter « versement des sorties prouvé … au commit C » et « versement final prouvé au commit C », même C, sur `donnees/barreau5-familles-jumelles-v1-lecture`.
   - Lire le journal par `vastai logs 62096662 --tail 400`, lignes « B5F » seules.
2. **« scores »**
   - Récupérer la branche de sortie en forçant, par son nom entier : `git -C <clone> fetch origin +refs/heads/donnees/barreau5-familles-jumelles-v1-lecture:refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-lecture`.
   - Puis, depuis l'arbre figé au commit de la marche : `bash scripts/lancer_b5f_lecture_v1.sh scores <ARBRE_FIGE> <C> 20261123-044043-b5f-lecture`.
   - Rendre à la mère et au conducteur, **à l'octet**, le contenu « commit … ; inventaire sha256 … » pour la ligne `SCORES-B5F`.
3. **Destruction**
   - Extraire `traces-b5f-lecture/inventaire-final.json` et son compagnon **sous leur nom d'origine** ; vérifier le compagnon.
   - Liste des instances réduite à `id`, `label`, `actual_status`, `cur_state`, `intended_status`, `dph_total`, `start_date`.
   - `detruire <ARBRE_FIGE> 62096662 decisif LISTE.json inventaire-final.json <C>` (GO_ID=GO-2026-11-19-86) ; jouer la commande imprimée telle quelle.
   - `verifier-destruction LISTE_NEUVE.json 62096662 58936096`.
   - Rédiger la ligne d'arrêt ; c'est la mère qui la verse.
   - La minuterie de l'instance peut détruire d'elle-même, si le versement final est prouvé : constater par « verifier-destruction ».
4. Passation finale, scellée.

## Prochaine action exacte
Surveiller 62096662 toutes les 10 minutes au plus.

- Sur ce compte : la veille `veille.sh 62096662 14 <bloc-notes>/relance2` tourne en tâche de fond, sortie `taches/bppri0xvx.output`.
- Sur un autre compte :
  1. Reconstruire le bloc-notes : clone neuf `git clone --single-branch --branch marche-b5f/lecture-v2`, puis les branches par leur nom entier (commande v3, entrées sans contenu `--filter=blob:none`).
  2. Arbres de travail : figé à `efc3f835…`, commande à `423496d4…`.
  3. Environnement Python : `requirements-cpu.txt` de `c76e7916`.
  4. Relancer la veille v2 du dossier `veille-session-lecture-v2/`.
  5. Si la marche est déjà finie, passer à « scores ».
- Arrêt à la coupure : cumul (heures × `dph_total`, plus sortie de données en octets / 1e9 × prix au Go) plus un quart d'heure ≥ 14 USD → `vastai stop instance 62096662`, par l'identifiant, sans destruction ; appeler la mère.

## Réserves
- **Faux échec 62094971, par ma faute** : bogue d'unités de ma veille. Il est corrigé, éprouvé par un essai écrit (cas sain, artefact des octets, coupure, anomalie ; témoin de la v1 fautive).
- Clé propre à l'instance de la répétition affichée une fois dans une sortie d'outil, puis retirée du fichier ; transmise nulle part. Depuis, la sortie de création est réduite avant affichage.
- `verifier-arbre .` rend le code 1 à la tête : connu du conducteur, 96 problèmes antérieurs, pas un arrêt.
- Le crédit du loueur est partagé : la coupure se tient sur le calcul de l'instance seule.
- Phrase de la mère, à reporter telle quelle : « Toute relecture rejouée commence par reproduire le dixième gardé ; sa tolérance est fixée par le préenregistrement de ce rejeu, scellé avant toute lecture de ses sorties ; à défaut d'égalité au bit près sur une même machine, l'écart toléré est écrit et justifié avant le rejeu. »
- Écarts à R14 : ni `registres/etat.md`, ni passations antérieures, ni `registres/decisions.md` lus (mandat, § 9, point 10).

## Machines, serveurs, tâches planifiées
- **À moi, en marche** : Vast **62096662** (`b5f-lecture-v1`).
- Pas à moi, vues à 04:40Z : 62094628 (`iib-voie-a-v1`) et 62094761 (`t08-v1`), en marche ; 58936096, 58936099, 58936100 et 60988826, arrêtées, intouchables.
- Aucun serveur Hetzner, aucune tâche planifiée à moi. Tâche de fond locale : la veille.

## Branches et commits
- Ma branche de travail : `lecture-b5f/plan-de-marche-v1`. Elle porte le plan et ses errata, la passation intermédiaire `…/lecture/passation-session-lecture-b5f-2026-11-22-2220.md` (`16a52d58…`), l'inventaire de 62047649, la veille v2 et son essai, le bloc-notes versé, et cette passation.
- Mes traces : `traces/barreau5-lecture-tentative-2` (`28a1d0f9…`).
- Lus ou utilisés :
  - `conducteur-b5f/lecture-v1` (tête `9739d5c2…`) ;
  - `marche-b5f/lecture-v1` (`2beeec31…`) et `marche-b5f/lecture-v2` (`efc3f835…`) ;
  - `course/barreau5-commande-lecture-v2` (`5402367e…`) et `-v3` (`423496d4…`) ;
  - `donnees/barreau5-familles-jumelles-v1-entrees-de-lecture` (`f6e2072d…`, noms seuls) ;
  - `donnees/barreau5-familles-jumelles-v1-repetition` (`c5c77d5b…`, inventaire seul).

## Versé avec cette passation
Bloc-notes : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/bloc-notes-session-lecture-2026-11-23/`. Contenu :
- relevés d'offres ;
- pièces de chaque création : configuration, verifier, OFFRE, commande, joueur (noms de clés seulement), sortie réduite ;
- relevés de veille : listes réduites, journaux d'étape, bilans ;
- copies du code lu et des pièces du signal ;
- filtres et calculs ;
- sorties des tâches de fond.

Volume : 214 fichiers et leurs compagnons, plus la liste d'ensemble `bloc-notes-session-lecture-2026-11-23-SHA256SUMS.txt` (`6f1d5b79…`). Vérifié sans valeur de clé ; la seule `instance_api_key` présente porte « (retirée) ».

**Non versé, reconstructible** : l'environnement Python (`requirements-cpu.txt`), les clones et arbres de travail (des commits cités), les dossiers temporaires des essais.

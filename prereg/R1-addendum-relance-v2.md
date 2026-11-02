# Addendum au préenregistrement de R1 — rejeu à graine des 7 épisodes non résolus, puis relance du rejeu des 2 400 actions de P3 sur une table complète — v2

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 1 (texte, non
  scellé)**. Nom nouveau (R12) : l'addendum v1 (`prereg/R1-addendum-relance-v1.md`, brouillon 4, commit `72f68fea`,
  local, non scellé) n'est pas modifié ; il reste archivé et sert de base. Ce que la v2 ne change pas dans la v1 vaut tel
  quel (section « Écarts à l'addendum v1 »).
- Date (UTC) : 2026-11-02 09:26 (brouillon 1 ; heure relevée par `date -u`).
- **Demande de Lazar** : « il faut résoudre tous les épisodes » (2 novembre 2026, 09:15, heure de Paris, dans la session
  de conv-audit ; message n° 348 de conv-audit, `c12099b1deb005cdaee81b18a02d7fffcb6b8119d7f3fc67e5d60d84b0a21127`,
  branche `canal/conv-audit-n04`) ; redite dans la session de session-depot : « résoudre les 7 épisodes avant la
  relance ». Ordre choisi par Lazar (≈ 08:28 UTC, relayé au n° 257 de session-depot) : **rejeu à graine d'abord, table
  complète, une seule relance de R1** ; la séquence « R1 à r = 3 maintenant » (n° 350 et 351 de conv-audit) est retirée
  (n° 352, `b4852257210e1caa8c8d90dd421f886c4a081df24e405bd2c3dcf1a65fd51d30`).
- **Méthode** : le rejeu à graine proposé au n° 256 de session-depot, section 2
  (`2f8149805f960cfac3ea94a13f4d736537e5ad67ac8f5cbe0037483a4ba79de7`), accepté par conv-audit au n° 351
  (`d92679194ba0c8b508649c44d29d88204b5591b678b624ce0f25af96ffcc4943`, qui retire sa recherche en faisceau du n° 349,
  `4f3d6e2d71a65b5491e25aef8d3e6684cb0b1a56fc6b46eb531b513884afd697`, au profit de cette méthode). Points que le lecteur
  neuf de conv-audit vérifiera : n° 352, point 1 ; précisions de forme : n° 354, point 1
  (`ef4a15d55d55910208d6f2f9bb94c35c13bbc73f09006185da5d5d5e7b78c3b1`) ; liste des épisodes non inversibles au
  versement : n° 356, point 4 (`da210e95993035d9ca694303083be883c94688b053366b4a766763de68648c45`).
- **GO** : `GO-2026-11-02-02`, ligne d'extension (R-389) inscrite dans `registres/go.md` de `main` au commit
  `ddfff6e4281b82fcd3b6ac9997fe47e15a62b0aa` (R-1034), sur le mot direct de Lazar dans la session de session-depot
  (≈ 08:32 UTC) : « GO-02 couvre le rejeu à graine et le complément des épisodes restants » ; plafond 25 USD inchangé ;
  échéance 2026-11-09. La garde de calcul l'accepte (essai du n° 258).
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65`.
- Commit du code d'analyse : `5c39c6b619f4f33f51629a97cc465b2f250d95ab`
  (branche `prep/r1-relance-addendum-v1`, local ; code seul : `src/controle_ia/runs_nuit/resolution_graine_v1.py`
  `09e31c95b12a6fe2a7fc30f4ec28e42585affc3780d9812cd7f46339cd2e8957` ; `tests/test_resolution_graine_v1.py`
  `c40e4428312027c63d1889e4bf2d980b3f3973a217d00b58660a4749be8c9663` ; `scripts/r1_resolution_graine_instance_v1.sh`
  `47cd64afbd1d7d35ce01288ad1cb5db27a8b5cd0331110a79a71f88fc8948670` ; `scripts/amorce_instance_r1_resolution_graine_v1.sh`
  `2ca73c20129a57a4a36cbd190239cee3644372dd725e46c4152940c037c0dc0e` ; `resolution_tokenisation_v1.py` et
  `rejeu_activations_v2.py` non modifiés)
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-v1.json`
- Configuration de la résolution à graine (empreinte canonique) : `À REMPLIR`
  (fichier à écrire avec les valeurs de la section « Seuil » ; empreinte canonique par
  `resolution_graine_v1.empreinte_config`, puis scellé)
- Entropie : `36410133060804533274328900142752730279` (celle du parent : le rejeu à graine ne tire rien ; son manifeste
  porte `aucun-tirage-propre`, les graines viennent du manifeste de P3)
- Tests attendus : `43`
  (les 5 fichiers que lance `r1_resolution_graine_instance_v1.sh` : `tests/test_resolution_graine_v1.py` (12),
  `tests/test_manifeste.py`, `tests/test_scellement.py`, `tests/test_prereg.py`, `tests/test_harnais_formats.py` ;
  43 passés au commit du code, processeur ; un test sauté arrête le script, qui exige « 43 passed » exactement)
- Documents qui font foi (chemin + empreinte) : le parent ci-dessus ; l'addendum v1, brouillon 4, pour tout ce que la
  section « Écarts à l'addendum v1 » ne change pas (`prereg/R1-addendum-relance-v1.md`, commit `72f68fea`) ; table de
  tokenisation v2 `prereg/R1-table-tokenisation-v2.json`
  (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`, commit `cdca33bb`) ; manifeste de P3
  `runs/20261019-230011-p3-reel/manifeste.json` (`3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685`) ;
  rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; résultat de C-6
  `docs/notes/runs-r1-r2-r4-v1/resultat-c6-v1.json` (`1e11d58fa75be359ffb185136cd2c83b1275203eb9f0162f0a5413222767b238`) ;
  messages cités dans l'en-tête ; GO ci-dessus.

**Statut.** Cet addendum ajoute, avant la relance de R1, une **résolution des 7 épisodes** que les étapes 1 à 3 de la
règle A n'ont pas résolus (dont les 4 que C-6 laisse non résolus) par **rejeu à graine**, arbitré par la seule empreinte
de trajectoire de P3, après une **validation à l'aveugle sur les 147 épisodes déjà résolus**. Il porte sur R1 seule ;
R2 ne se relance pas ; le rejeu de R4 n'est pas relancé (comme la v1). Il gèle la méthode, ses seuils, sa lecture et
les écarts que la table v3 apporte à la relance (étape 3). **Les valeurs de lancement de la relance elle-même**
(commit du code du rejeu v3, configuration du rejeu v5 et table v3 avec leurs empreintes, nombre de tests de la
relance) n'existent pas encore : elles viendront dans un complément court, scellé et contre-lu avant la relance
(« Plan d'analyse », étape 3 ; point à trancher).

## Cause et méthode (renvoi)

**Cause de l'arrêt de R1** : inchangée (v1, section « Cause de l'arrêt ») — à température 1, l'agent de P3 a parfois
tiré un découpage non canonique d'un mot, de même texte ; le texte stocké ne le dit pas, l'empreinte de trajectoire
de P3 le voit. Table v2 (règle A, étapes 1 à 3, puis C-6) : 22 épisodes signalés, 18 corrigés, **4 non résolus**
(`honnete/2602.00987v1/e0`, `mention/2605.17899v2/e0`, `saboteur/2510.05132v3/e0`, `temoin/2512.06870v2/e0`) ;
C-6 (dix niveaux, 1 974,8 s de processeur) a résolu `honnete/2512.05150v2/e0`, `honnete/2512.11131v1/e0` et
`temoin/2510.24788v1/e0`. Les règles A et C-6 devinent des corrections dans des classes fixées ; or le découpage tiré est
un tirage du modèle lui-même : la méthode juste reproduit ce tirage.

**Faits établis sur le harnais de P3** (code au commit `97dd8290`, le même que P3 selon l'enquête ; réponses du n° 256,
section 1, aux questions du n° 349) :
- (a) **texte stocké** de chaque action = `tok.decode(ids, skip_special_tokens=True)` des identifiants tirés
  (`harnais/episode.py`, `jouer_episodes`). Pertes possibles, et seulement elles : les jetons spéciaux (le jeton de fin,
  retrouvé par `jetons − jetons_notes`, stocké par P3 ; tout autre spécial est effacé) et des octets UTF-8 incomplets
  décodés en caractère de remplacement U+FFFD (hypothèse 4 de l'enquête). Sur les 147 résolus, l'invariant tient par
  preuve (empreinte retrouvée au bit près), non par hypothèse.
- (b) **empreinte de trajectoire** : **par épisode seulement**, sha256 de `json.dumps(asdict(Episode), sort_keys=True,
  ensure_ascii=False)` (identifiant, N, T, transcription complète en identifiants : ouverture, observations, actions,
  clôtures ; par action : pas, empan, identifiants générés, texte). Aucune empreinte intermédiaire par action : la
  vérification est finale, par épisode (oracle de 256 bits).
- (c) **contexte de chaque action** : les jetons tirés, non le texte retokenisé (`trs.ids = ctx + nv + fmt.cloture(…)`,
  puis `ctx = trs.ids + fmt.tour(debut, obs)`) ; observations de l'environnement tokenisées par le gabarit. N = 1, T = 10.
- (d) **échantillonnage** : température 1,0 ; **ni top_p ni top_k** (tout le vocabulaire) ; `max_nouveaux` = 400 ;
  génération par lots de 8, remplis à gauche, avec cache, modèle en bfloat16 sur A100-SXM4-80GB (CUDA 13.0, lu dans
  `episodes-p3.json`) ; à chaque pas, logits du dernier jeton ramenés **sur processeur en float32**
  (`.to("cpu", torch.float32)`), puis `torch.multinomial(torch.softmax(logits / T, -1), 1, generator=g)` ; **un
  générateur par action**, `torch.Generator('cpu').manual_seed(graine)`, avancé d'un tirage par jeton tant que la ligne
  est active ; graine de l'action tirée par `graines_des_actions(generateur(graine de la tâche), 1, T)`, clé
  `tache/<identifiant>` du manifeste de P3 (le `g.random(T)` qui suit dans `jouer_p3` ne change pas ces graines) ;
  mêmes graines d'une condition à l'autre (vérifié sur processeur avec les vraies pièces de P3).
- (e) **identité du tirage** : sur torch 2.14.1 (version de P3), `torch.multinomial(p, 1, generator=g)` est exactement
  `argmax(p / q)`, `q` vecteur de V tirages exponentiels pris au même générateur ; un appel unique de n × V tirages
  égale n appels de V. Vérifié sur processeur, en float32 (200 graines, 200 égalités, n° 256 ; tests du module) et
  **revérifié au lancement** sur la bibliothèque installée (`exiger_equivalence_tirage`, arrêt sinon).

## Écarts à l'addendum v1

Liste exhaustive. « v1 » = `prereg/R1-addendum-relance-v1.md`, brouillon 4 ; ses écarts au parent E1 à E20 valent tels
quels sauf ce qui suit. Notation : **r′** = nombre des 4 épisodes non résolus par la table v2 que le rejeu à graine
résout (0 ≤ r′ ≤ 4) ; chacun compte 10 actions ; les 4 sont dans quatre conditions différentes (honnête, mention,
saboteur, témoin).

| n° | Ligne ou règle de la v1 | Nouvelle règle | Raison |
|---|---|---|---|
| G1 | Étape 0 : table v2 (règle A, étapes 1 à 3, puis C-6) ; 4 non résolus traités par la règle B | **Étapes 0 à 2 ajoutées** (rejeu à graine) : validation à l'aveugle sur les 147 résolus, résolution des 7, table v3 = table v2 dont chaque épisode « non résolu » que le rejeu résout reçoit une entrée de forme « identifiants » ; les 18 corrections de la v2 restent telles quelles | Demande de Lazar (n° 348) ; méthode du n° 256 acceptée (n° 351) |
| G2 | E2 (règle B pour 7 − r épisodes) | Règle B **réservée aux épisodes que le rejeu à graine laisse non résolus, chacun avec sa cause écrite** ; liste remise à Lazar avant toute lecture (n° 356, point 4) ; seuil de 10 inchangé (E3) | « Résoudre tous les épisodes » ; la règle « non conforme » ne reste que pour le cas déclaré (n° 348, 349) |
| G3 | E19 (copie de la ligne E5 dans l'analyse principale de conv-audit, couverte par N-A pour 7 − r = 4 épisodes) | **Sans objet si r′ = 4** ; sinon, la ligne est **couverte, pour les épisodes nommés** (liste des non résolus du rejeu à graine), par la décision N-A de Lazar ; rien d'autre de la principale ne change | Précision de forme (1) du n° 354 |
| G4 | P-R5 : 147 trajectoires identiques, 4 non résolus | **147 + r′ trajectoires identiques (151 à r′ = 4, soit tous les épisodes entièrement conformes en longueur), 4 − r′ non résolus** ; « ≥ 90 % des actions notées fidèles (au plus 93 %) » inchangé | Conséquence de G1 |
| G5 | E14 et E15 : comptes à r = 3 | Contexte exact **1 742 + 10 r′** (à r′ = 4 : **1 782 = 74,3 %** ; honnête 471, mention 496, saboteur 437, témoin 378 : les comptes du parent reviennent) ; trajectoire identique (couverture sous repli) **1 470 + 10 r′** (à r′ = 4 : **1 510 = 62,9 %** ; honnête 420, mention 430, saboteur 350, témoin 310) ; 272 actions de préfixes sans empreinte et 2 236 conformes en longueur inchangées | Conséquence de G1 ; formules de la v1 prolongées |
| G6 | E11 et E12 : configuration v4 (table v2), module `rejeu_activations_v2` (n'accepte que la table version 2) | Relance sur la **table v3** : configuration du rejeu **v5** (clés de la v4, table v3) et module **`rejeu_activations_v3`** (nom nouveau ; à écrire) ; la commande inscrite au manifeste change encore : le code « R2 seul » de conv-audit (paquet `controle_ia.analyse_principale_r1_r2`, `constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`, branche `canal/conv-audit-n04`) refuserait la preuve d'un arrêt de la relance, comme en E16 | Table v3 ; précision de forme (2) du n° 354 |
| G7 | E10 : tests attendus de la relance, 302 | Pour le rejeu à graine : 43 (en-tête) ; pour la relance : 302 plus les tests du rejeu v3, nombre écrit dans le complément de l'étape 3 | Code neuf |
| G8 | E9 et « Coût et GO » : relance seule | **Passage sur carte ajouté** avant la relance : au plus 60 minutes d'A100 (pire cas ≈ 1,4 USD, plus le disque et la descente du modèle), sous la même ligne GO-2026-11-02-02 (extension R-1034) | Dépense nouvelle couverte par le mot de Lazar (n° 258) |
| G9 | E13 : contre-contrôle négatif sur les épisodes corrigés | Inchangé, étendu aux épisodes corrigés par le rejeu à graine (identifiants retrouvés rejoués sous la consigne fausse) | Seule la consigne doit différer du contexte exact |
| G10 | Traitement de C-1 (nom hérité de `test_relance_regle_b_non_resolus_fidele_faux_et_seuil`) | Inchangé ici (`tests/test_runs_nuit_v2.py` n'est pas touché par le code du rejeu à graine) ; la docstring et le nom de l'essai sont à corriger dans le code du rejeu v3, ou déclarés à nouveau dans le complément | Précision de forme (3) du n° 354 |

Inchangés : tout le reste de la v1 et du parent (hypothèses H-R1 et H-R2, prédictions P-R1 à P-R4, métriques, bras,
seuils, tolérance de fidélité, contrôle négatif 18 sur 20, règle de repli gelée, formats de sortie, run source et
pièces de P3, entropie, couches, R2 non relancée, R4 non relancé, versement sur `calcul/r1-r2-reel-v1`, E18).

## Hypothèse

Hypothèses de travail de l'instrument (aucune hypothèse du programme n'est en jeu ; H-R1 inchangée, parent) :
- **HG-1 (graines)** : les graines des actions, dérivées du manifeste de P3 comme `jouer_p3`, sont celles que P3 a
  utilisées ; avec elles et l'identité du tirage (fait (e)), chaque jeton tiré par P3 est l'argmax de p / q.
- **HG-2 (précision)** : les logits recalculés par une passe forcée par l'enseignant, sans lot ni cache, en bfloat16 sur
  la carte, ne diffèrent de ceux de la génération de P3 (lot de 8, remplissage à gauche, cache) que par des arrondis,
  **petits devant l'écart entre les candidats compatibles avec le texte**, sauf aux quasi-égalités, que le repli écrit
  traite.
- **HG-3 (inversibilité)** : le texte stocké est l'image exacte des identifiants tirés, aux pertes déclarées près (fait
  (a)) ; un épisode qui contient U+FFFD n'est inversible que si les octets inconnus se retrouvent par un balayage borné
  du vocabulaire.

Sous HG-1 à HG-3, la reconstruction d'un épisode est l'unique suite d'identifiants qui redonne l'empreinte de P3 ;
l'empreinte en est la preuve (256 bits), quelle que soit la voie qui l'a trouvée.

## Prédiction chiffrée et signe attendu

- **P-G1 (validation, étape 0)** : **147 empreintes de P3 retrouvées sur 147** (129 identiques de base et 18 corrigés
  par la table v2), à l'aveugle ; au moins 140 par la voie directe (sans repli) ; accord du choix non contraint avec le
  jeton connu, en moyenne par épisode, **au moins 0,99**, et au moins 0,95 dans chaque épisode (une graine fausse
  ferait tomber cet accord vers la probabilité du jeton le plus probable, typiquement 0,6 à 0,85). Réfutation : moins de
  147 (arrêt, la méthode ne se transpose pas) ; accord moyen sous 0,95 (graines non validées, voir « Critères »).
  Confiance ≈ 0,8 pour 147 sur 147 ; c'est le seuil gelé, non une cible (R3 : rien n'est relancé pour l'atteindre).
- **P-G2 (résolution, étape 1)** : **au moins 6 des 7** épisodes résolus (empreinte de P3 retrouvée), confiance ≈ 0,8 ;
  **7 sur 7**, confiance ≈ 0,6. Les 3 de C-6 résolus avec les identifiants de la table v2 (contrôle croisé conforme),
  confiance ≈ 0,95 (ils font déjà partie des 147 de l'étape 0). L'épisode le plus exposé : `mention/2605.17899v2/e0`,
  qui contient un U+FFFD (hypothèse 4 plausible pour lui) ; s'il reste non résolu, sa cause attendue est « caractère de
  remplacement : cas non simple ». Les découpages qui changent le nombre de jetons d'un mot en compensant ailleurs,
  non explorés par C-6, sont couverts par construction (le choix est pas à pas, seule la longueur totale de l'action
  est contrainte).
- **P-G3 (fragilité numérique, descriptif)** : sur les 147, écart contraint (premier contre second candidat compatible)
  sous 1 nat dans moins de 1 % des pas à plusieurs candidats ; désaccords du choix non contraint concentrés sur des
  marges sous 0,5 nat. Mesure sur le modèle minuscule en bfloat16 (essais du code) : 16 épisodes sur 16 résolus
  directement, deux désaccords non contraints à des marges de 0,012 et 0,015, 0,3 % des pas à plusieurs candidats sous
  0,1 d'écart ; le 8B n'est pas mesuré avant la carte.
- **P-R5 (relance, étape 3 ; écart G4)** : trajectoires identiques **147 + r′** (prédit : 151) ; non résolus
  **4 − r′** (prédit : 0, au plus 1) ; **au moins 90 % des actions notées fidèles (au plus 93 %)**, inchangé.
  À r′ = 4 : borne haute 2 236 / 2 400 = **93,2 %** (inchangée) ; scénario bas 1 782 / 2 400 = **74,3 %** ; P-R5 tient
  tant qu'au plus 76 des 2 236 actions conformes en longueur sortent de la tolérance, sorties attendues surtout parmi
  les 494 − 10 r′ = **454** conformes hors contexte exact ; confiance ≈ 0,6 (inchangée). Marges avant la règle des
  80 % du parent au scénario bas, à r′ = 4 : honnête 471 − 480 = **− 9**, saboteur 437 − 480 = **− 43** (à la borne
  haute : 88 et 76, inchangées).

## Métrique

Par étape (résultat scellé `diag/<run>/resolution-graine-<etape>.json` et pas par pas
`diag/<run>/pas-resolution-graine-<etape>.npz`) :
- **empreintes retrouvées** : nombre d'épisodes dont l'épisode reconstruit redonne exactement l'empreinte de trajectoire
  de P3 (`empreintes_retrouvees`), dont par voie directe (`directes`) et par repli (`par_repli`) ; c'est la seule
  métrique de décision ;
- **identifiants égaux** (comparaison aux identifiants connus, après la résolution seulement) : épisodes
  (`identifiants_egaux_episodes`) et actions (`actions_egales` sur `actions_comparees`) ;
- **accord du choix non contraint** : part des pas où l'argmax de p / q sur tout le vocabulaire (l'opération de P3)
  égale le jeton connu (validation) ou retenu (résolution) ; moyenne par épisode et minimum (`accord_non_contraint`) ;
  contrôle de la dérivation des graines ;
- **écart contraint** : par pas à plusieurs candidats compatibles, écart en log (nat) entre le premier et le second
  candidat ; quantiles (`ecarts_contraints`) ; **marges en désaccord** : marge en log du choix non contraint aux pas où
  il diffère (`marges_en_desaccord`) ;
- **premier écart de la voie directe** quand elle échoue (`erreurs_directes`) ; **contrôle croisé** des 3 épisodes de
  C-6 (`controle_croise`, `controle_croise_lecture`) ; **U+FFFD** déclarés par épisode (`fffd_declares`) ; passes,
  jetons en passe, durée.
Comptes exacts, sans tirage propre : aucun intervalle n'est calculé (la méthode est déterministe aux arrondis près ;
ces arrondis sont ce que mesurent l'écart contraint et l'accord). Aucune moyenne sur les jetons n'entre dans une sonde.

## Seuil

Valeurs de la configuration `prereg/R1-graine-config-v1.json` (à écrire ; clés `CLES` du module), fixées avant toute
carte :
- `seuil_validation` = **147** (toutes les empreintes des épisodes à identifiants connus ; sous ce seuil, arrêt et
  résolution non lancée) ;
- `seuil_ecart` = **1,0** nat (quasi-égalité : écart contraint sous ce seuil ; je tiens pour fragile un écart sous 0,5 à
  1 nat pour le 8B en bfloat16 : la garde d'équivalence de P3 tolérait jusqu'à 0,2 d'écart relatif sur les activations,
  au 99e centile, entre génération et passe unique) ;
- `quasi_egalites_max` = **16** (les plus fragiles d'abord) ; `bascules_max` = **2** ; `combinaisons_max` = **136**
  (toutes les bascules simples et doubles parmi 16 : 16 + 120) ; `combinaisons_max_validation` = **16** (bascules
  simples seulement) ;
- `balayages_max` = **64** (balayages du vocabulaire par épisode pour les octets que recouvre un U+FFFD) ;
- `duree_max_s` = **1 800** par étape ; délais externes du script : validation 35 min, résolution 15 min ; plafond de
  l'amorce : **60 minutes** pour l'ensemble ;
- `T` = 10, `temperature` = 1,0, `max_nouveaux` = 400 (comparés à la configuration de P3 par le module) ; `noyau_attention` =
  « defaut » ; `hors_ligne` = vrai ; `fils` = 1 ; `fils_tirages` = 8 ; `episodes_d_avance` = 2 ;
- `episodes_resolution` = les 7, dans cet ordre : `honnete/2602.00987v1/e0`, `mention/2605.17899v2/e0`,
  `saboteur/2510.05132v3/e0`, `temoin/2512.06870v2/e0`, `honnete/2512.05150v2/e0`, `honnete/2512.11131v1/e0`,
  `temoin/2510.24788v1/e0` ;
- pièces : celles de la configuration v4 (`agent` : `meta-llama/Llama-3.1-8B-Instruct`, révision
  `0e9e39f249a16976918f6564b8830bc894c89659`, `date_string` « 26 Jul 2024 » ; textes `ba05fa13…`, scores (identité
  seule) `968414fc…`, identité `1f25adbd…`, fiches `1a96cbf8…`, tâches `287e8348…`, consignes `a68468fe…`), plus le
  manifeste de P3 (`3f21774c…`) et la table v2 (`5f6cf489…`).
**Seuils de lecture** (critères, non gardes du code) : accord non contraint moyen par épisode **≥ 0,95** et minimum
**≥ 0,90** sur les 147 pour tenir les graines pour validées (« Critères de lecture gelés »). Seuil de la règle B : 10
épisodes (E3, inchangé).
**Déclaré** : ces seuils sont fixés en connaissant les comptes (147 résolus, 7 à résoudre) et les mesures du modèle
minuscule, non celles du 8B.

## Plan d'analyse

**Données.** Pièces de P3 citées par la configuration, vérifiées par empreinte au chargement : textes des actions ;
de `scores-p3.npz`, **seuls** les tableaux d'identité, `jetons` et `jetons_notes`, chargés clé par clé
(`charger_identite_sans_scores`) ; fiches (empreintes de trajectoire) ; tâches ; consignes, lues seulement par
`charger_consignes`, qui en vérifie l'empreinte ; manifeste de P3 (graines). Aucun score, aucune note, aucune
étiquette, aucune activation n'est lu. Graines (R9) : celles de P3, dérivées comme `jouer_p3` ; le rejeu ne tire rien.

**Méthode** (`resoudre_action`, `rejouer_episode`, `resoudre_avec_repli`). Pour chaque épisode, action par action, dans
le contexte exact (identifiants déjà retrouvés des actions précédentes ; ouverture, tours et clôtures comme le harnais) :
1. **Passe forcée** par l'enseignant, sans cache ni lot, sur le découpage courant (découpage canonique du texte restant,
   plus le jeton de fin par défaut) ; logits des positions utiles ramenés en float32.
2. À chaque pas, **choix contraint** : parmi les jetons compatibles avec les octets restants du texte stocké (décodeur au
   niveau de l'octet ; jetons spéciaux hors fins : zéro octet), celui qui maximise log p − log q, soit le même ordre que
   p / q, calculé en double précision sur les seuls candidats ; dernier pas : un jeton de fin (parmi `fmt.fins`) si
   `jetons − jetons_notes` = 1, sinon l'action doit compter exactement 400 jetons. Si le choix diffère du découpage
   courant, le reste est redécoupé canoniquement et une nouvelle passe est faite.
3. Consigné à chaque pas : choix contraint, choix non contraint (argmax de softmax(logits / T) / q sur tout le
   vocabulaire, calculé en bloc sur la carte, diagnostic), nombre de candidats, écart contraint, second candidat, marge
   non contrainte, balayage.
4. **Arbitre unique** : l'empreinte de trajectoire de P3, recalculée sur l'épisode reconstruit (`empreinte_trajectoire`
   du rejeu v1, celle du harnais).
5. **Repli écrit** si l'empreinte n'est pas retrouvée : les quasi-égalités de l'essai direct (écart sous `seuil_ecart`,
   au plus `quasi_egalites_max`, les plus fragiles d'abord) sont basculées vers leur second candidat, une, puis deux à
   la fois, dans l'ordre de `itertools.combinations`, au plus `combinaisons_max` combinaisons (16 en validation), chaque
   essai rejoué depuis l'action basculée et arbitré par l'empreinte. Sinon : **non résolu, cause écrite** (empreinte non
   retrouvée après repli ; contradiction entre texte, longueurs et choix ; U+FFFD non simple ; durée).
6. **U+FFFD** : compté par épisode ; les octets inconnus qu'il recouvre sont cherchés par balayage du vocabulaire, au
   plus `balayages_max` par épisode ; au-delà, non résolu déclaré « caractère de remplacement : cas non simple » — c'est
   le cas **non inversible** déclaré (HG-3) ; sa lecture est dans « Critères ».

**Précision et ordre des opérations (n° 351, points (a) et (b) ; n° 352).** Le modèle est chargé en **bfloat16**, son
format natif, comme dans P3 (`charger_modele` refuse un point de contrôle qui ne l'est pas ; attention « sdpa » ; même
révision ; torch 2.14.1 exigé). Les logits sont passés en float32 comme dans P3. Ce qui diffère de P3, déclaré :
(i) la passe est **pleine, sans lot ni cache ni remplissage**, au lieu du décodage pas à pas par lots de 8 remplis à
gauche : les accumulations en bfloat16 diffèrent, donc les logits diffèrent aux arrondis près (c'est HG-2, et la
raison d'être de l'écart contraint, du repli et de la validation à l'aveugle) ; (ii) le **choix contraint** est calculé
en log, en double précision, sur les candidats (log p − log q, à la constante de normalisation près), au lieu de p / q
en float32 sur processeur : l'ordre est le même en arithmétique exacte et ne peut différer que si deux candidats sont à
moins d'un arrondi de float32 (≈ 10⁻⁷ en relatif), très en deçà du bruit du bfloat16 (quelques centièmes à quelques
dixièmes de nat) ; un tel cas est une quasi-égalité, que le repli traite ; (iii) le **choix non contraint** est calculé
sur la carte (softmax en float32 puis division par q, l'opération de P3) au lieu du processeur : diagnostic seulement ;
(iv) les tirages exponentiels sont calculés sur processeur, en float32, au générateur de l'action, comme dans P3
(séquentiels, vérifié ; une différence au dernier bit d'un processeur à l'autre reste possible et négligeable). **Carte
attendue : A100-SXM4-80GB**, celle de P3 ; une autre carte n'arrête pas le script mais est consignée comme réserve au
journal ; la validation à l'aveugle juge. **Mode « génération de P3 refaite par lots »** (n° 257, point 4, accepté en
premier par conv-audit au n° 352) : **non codé dans ce commit** ; la passe forcée est le seul mode de ce texte (écart au
n° 257 déclaré ; point à trancher). Il reste le complément prévu si des épisodes restent non résolus pour une cause
numérique (même carte, lot de 8, longueurs de remplissage calculables depuis `jetons` et les textes, lignes voisines
remplies de jetons quelconques), sous un texte neuf.

**Étape 0 — validation à l'aveugle (carte).** `--etape validation` sur les 147 épisodes à identifiants connus (129
identiques de base ; 18 corrigés par la table v2 : 1 jeton de fin, 12 une paire, 2 deux paires, 1 trois paires, 2
fenêtres ; 1 470 actions ; ≈ 4,14 millions de jetons en passe, ≈ 310 000 pas). **À l'aveugle** : la table v2 sert
seulement à choisir les épisodes de l'étape (`classer`, `episodes_de_l_etape`) ; les fonctions de résolution ne
reçoivent que les textes, les longueurs, les graines et l'empreinte de P3 ; les identifiants connus ne sont lus qu'après
la résolution de tous les épisodes, pour les mesures (`verite`). Critère gelé : `seuil_validation` = 147 ; sous le
seuil, arrêt (`exiger_seuil_validation`), résolution non lancée. Les 18 corrigés sont ceux où la graine compte (un
découpage non canonique n'est retrouvé que si p / q le désigne) ; ils sont rapportés à part. Remarque : sur un épisode
canonique, le choix contraint est le plus souvent imposé par les octets et la probabilité, même avec une graine fausse ;
l'empreinte retrouvée ne prouve donc pas seule les graines : l'accord non contraint les contrôle.

**Étape 1 — résolution des 7 (carte).** `--etape resolution --validation diag/<run>/resolution-graine-validation.json`,
seulement si la validation est scellée, de lecture « atteint », de **même configuration** et de **même code**
(comparaison de l'arbre gelé, pas du dernier commit : `exiger_validation`, `exiger_meme_code`). Les 7 épisodes de
`episodes_resolution` : les 4 non résolus et, en **contrôle croisé**, les 3 de C-6 (leurs identifiants retrouvés
doivent égaler ceux de la table v2). Combinaisons de repli : 136 au plus par épisode (au pire ≈ 5 minutes par épisode).

**Étape 2 — table v3 (processeur, sans dépense).** `--etape table --tokeniseur <tokeniseur de la révision 0e9e39f2…>
--resultat diag/<run>/resolution-graine-resolution.json --sortie prereg/R1-table-tokenisation-v3.json`
(`construire_et_verifier_table`) : table v2, dont chaque épisode « non résolu » que le rejeu a résolu reçoit une entrée
`identifiants` (version 3 ; actions corrigées avec leurs identifiants de base et ceux retrouvés ; voie, bascules et
empreinte du résultat) ; les 18 entrées de la v2 restent telles quelles ; **chaque correction, ancienne ou nouvelle, est
revérifiée par l'empreinte de P3** (`verifier_entrees_v3`, transcription refaite comme le harnais) ; comptes recalculés ;
arrêt si le résultat vient d'une autre configuration, si une empreinte de P3 diffère de la table v2, ou si les
corrections vérifiées diffèrent des comptes ; la sortie n'écrase jamais. La table v3 est scellée ; **table complète**
si r′ = 4 ; sinon, les non résolus y restent `non_resolu`, chacun avec la cause écrite par le rejeu.

**Étape 3 — relance de R1 sur la table v3.** Tout est celui de la v1 (règles A et B, contrôle négatif, échantillon de
fidélité, sorties, versement, R2 et R4), aux écarts G1 à G10 près. Préalables : module `rejeu_activations_v3` (accepte
la table version 3 ; les formes v1 et v2 passent par `appliquer_entree` inchangée, la forme `identifiants` par
`appliquer_entree_v3`), configuration du rejeu v5 (table v3), leurs essais sur processeur ; puis **complément court**
de ce texte, scellé et contre-lu, qui cite le commit de ce code, la configuration v5 (empreinte canonique), la table v3
(empreinte), le nombre de tests de la relance et la liste des non résolus ; puis la concordance de conv-audit sur la
version scellée (comme la v1) ; puis lancement sous GO-2026-11-02-02.

**Calendrier.** Texte et code (processeur, fait pour le code) → contre-lecture neuve et lecteur neuf de conv-audit →
configuration `R1-graine-config-v1.json` écrite et scellée ; table v2 scellée (son `.sha256` manque ; `charger_pieces`
l'exige) ; scellement de ce texte ; poussée → instance A100 (étapes 0 et 1) → étape 2 sur processeur, table v3 scellée →
liste des non résolus à Lazar s'il y en a → étape 3.

**Coût et GO.** A100-SXM4-80GB, ≈ 1,0 à 1,4 USD de l'heure. Durée estimée par le code : mise en place (installation,
16 Go du modèle, 43 tests) 12 à 18 min ; validation 12 à 20 min (7 à 12 min de carte, plus transferts et tirages) ;
résolution moins d'une minute en direct, au pire ≈ 5 min de repli par épisode non résolu ; **total ≈ 30 à 45 min,
soit ≈ 0,6 à 1,0 USD** ; **pire cas : plafond de 60 min × 1,40 USD ≈ 1,4 USD**, plus le disque et la descente du
modèle. Dépenses engagées sous GO-2026-11-01-13, prolongé par GO-2026-11-02-02 : ≈ 4,6 / 25 USD (relevé du
2 novembre, 03:10 UTC ; à revérifier dans le registre des dépenses avant la création) ; après ce passage, au pire
≈ 6,0 / 25 USD ; après la relance (pire cas de la v1, ≈ 2,3 USD), au pire ≈ 8,3 / 25 USD. Lancement :
`GO_ID=GO-2026-11-02-02` devant la commande de création ; **échéance 2026-11-09** : après, GO nouveau sous un
identifiant nouveau. Branche de résultats : `calcul/r1-resolution-graine-v1` (une branche existante arrête le script).

**Essais (processeur, sans dépense ; code au commit cité).**
- `tests/test_resolution_graine_v1.py`, 12 passés (102 s) : identité du tirage (`torch.multinomial` = argmax de p / q ;
  n × V tirages en un appel = n appels de V) ; graines dérivées comme `jouer_p3` ; **cas sain** (modèle Llama minuscule
  de vocabulaire 128 256, graine fixe, enregistré puis relu ; vrai tokeniseur de Llama 3.1 et gabarit réel ; épisodes
  joués par le harnais ; identifiants et empreinte retrouvés, accord non contraint 1,0 ; 11 découpages non canoniques,
  actions arrêtées à `max_nouveaux`, un jeton spécial effacé du texte) ; **artefacts (R5)** : graine fausse, texte
  altéré d'un octet, contexte décalé d'un jeton donnent tous « non résolu », jamais un faux « résolu » ; repli qui
  retrouve l'empreinte quand on perturbe une quasi-égalité ; U+FFFD résolu par balayage, ou déclaré non résolu
  au-delà de la borne ; garde du seuil de validation ; forme `identifiants`, cas sain et artefacts ; formes v1 et v2
  acceptées telles quelles ; **bout en bout** sur un P3 jouet joué par le vrai code de P3 (graines lues dans son
  manifeste ; validation, résolution, épisodes non conformes en longueur compris, table v3 revérifiée par
  l'empreinte ; avec des graines fausses, la validation tombe sous le seuil et l'arrêt est consigné) ; gardes de la
  configuration.
- Voisins : `tests/test_runs_nuit_v2.py -k "table or forme or reelle"`, 4 passés. Liste de l'instance : 43 passés.
- Sans tokeniseur (`TOKENISEUR_LLAMA31` absent, cache vide) : les tests qui en ont besoin sont sautés avec leur motif ;
  le script d'instance s'arrête alors (il exige « 43 passed »).
- Vraies pièces de P3, processeur, sans modèle : 147 épisodes choisis pour la validation, 7 pour la résolution, graines
  identiques d'une condition à l'autre.
- Script d'instance : syntaxe seule vérifiée (`bash -n`) ; l'essai local des gardes (`ARRET_AVANT_CALCUL=1`) exige une
  poussée et n'est pas fait.

## Critères de lecture gelés

| Issue observée | Lecture |
|---|---|
| Validation : 147 / 147 empreintes, accord non contraint moyen ≥ 0,95 et minimum ≥ 0,90 | Méthode validée sur les résolus ; graines validées ; la résolution est lue |
| Validation : 147 / 147 empreintes, accord sous l'un des deux seuils | **Réserve** : dérivation des graines non validée. Les empreintes retrouvées à l'étape 1 restent des preuves (l'empreinte arbitre seule) ; **aucun non résolu ne peut être déclaré non inversible** (la cause peut être la méthode) ; audit (R4) avant toute suite |
| Validation : moins de 147 | Arrêt par le code, résolution non lancée : la méthode ne se transpose pas au 8B sous cette précision. Nœud à Lazar : complément « génération refaite par lots » sous texte neuf, ou relance avec la table v2 et la règle B pour les 4 (v1, E19) |
| Résolution : 7 / 7, contrôle croisé conforme | **Table v3 complète** ; G3 sans objet ; règle B sans objet ; étape 2 puis étape 3 |
| Résolution : k non résolus (1 ≤ k ≤ 4, tous parmi les 4), contrôle croisé conforme | Table v3 partielle ; chaque non résolu porte sa cause ; **liste à Lazar avant toute lecture** (n° 356, point 4) ; cause « caractère de remplacement : cas non simple » = **non inversible déclaré** (le texte stocké n'est pas l'image exacte des jetons) : règle B de la v1 pour lui ; toute autre cause (empreinte non retrouvée après repli, contradiction, durée) = **non résolu par la méthode**, non déclaré non inversible : nœud à Lazar (complément par lots, ou règle B pour l'épisode nommé) |
| Contrôle croisé contraire : un épisode de C-6 non résolu par le rejeu | Contradiction avec l'étape 0 (il y était résolu) : audit (R4) ; la table v3 garde l'entrée de C-6, déjà vérifiée par l'empreinte |
| Contrôle croisé contraire : un épisode de C-6 résolu avec d'autres identifiants que la table v2 | Impossible hors collision de sha256 : arrêt de la lecture, audit (R4) |
| Audit de symétrie (R4) | Déclenché aussi par un résultat trop propre : accord non contraint égal à 1 exactement sur tous les pas des 147 (le bruit du bfloat16 doit laisser quelques désaccords), aucune quasi-égalité sous 1 nat, ou durée très en deçà de l'estimation ; l'audit vérifie d'abord que les identifiants connus n'ont pas fui dans la résolution |
| Relance (étape 3) | Lignes de la v1 et du parent, inchangées (dont « plus de 10 non résolus → rejeu non validé ») |

## Liste d'arrêt

Arrêts du script d'instance et du module (R5 ; ceux qu'éprouvent les tests sont cités dans « Essais » ; les autres
sont lus dans le code au commit cité, à éprouver par la contre-lecture), puis action :
- **avant l'installation** (code 2) : ce texte ou son `.sha256` absent au commit lancé ; « Tests attendus » ou « Chemin
  de la configuration de la résolution à graine » absent ou cité plus d'une fois ; configuration absente, non scellée
  ou de sceau faux ; branche de résultats déjà présente ou non vérifiable ; poussée initiale refusée ;
- **carte et bibliothèques** : `nvidia-smi` absent ; torch ≠ 2.14.1 ; carte indisponible pour torch → arrêt ; carte ≠
  A100-SXM4-80GB → réserve au journal, sans arrêt ;
- **tests** : dernière ligne ≠ « 43 passed » (échec ou test sauté) → arrêt avant le calcul ;
- **module, avant le manifeste** : configuration incomplète ou de valeur hors domaine ; texte qui ne cite pas
  l'empreinte canonique de la configuration, l'entropie ou le commit du code (arbre gelé différent du commit cité) ;
  pièce d'empreinte fausse (textes, identité, tâches, manifeste de P3, table v2, consignes) ou calculée sur d'autres
  pièces ; run du manifeste ≠ run source ; T, température ou `max_nouveaux` ≠ configuration de P3 ; N ≠ 1 ;
- **module, pendant le run** (`arret.json`, rien d'autre n'est lu) : graine `tache/<identifiant>` absente du manifeste
  de P3 ; ouverture sans le texte attendu (« Today Date: 26 Jul 2024 ») ; dimension des logits ≠ taille du tokeniseur ;
  jeton spécial non effacé au décodage ; fins hors des jetons spéciaux ; identité du tirage fausse sur la bibliothèque
  installée ; formes des logits ou des tirages inattendues ; durée de l'étape au-delà de 1 800 s ; délai externe (35 ou
  15 min) ou plafond de l'amorce (60 min) ; validation sous le seuil de 147 (résolution non lancée) ; résolution sans
  validation scellée de même configuration et de même code ;
- **étape table** : résultat d'une autre configuration ou d'une autre étape ; empreinte de P3 du résultat ≠ table v2 ;
  correction qui ne redonne pas l'empreinte de P3 ; corrections vérifiées ≠ comptes ; sortie existante (R12) ;
- **dépense et GO** : pas de création sans `GO_ID=GO-2026-11-02-02` valide le jour même ; aucune création après le
  9 novembre 2026 sans GO nouveau ; pire cas ≈ 1,4 USD (plafond de 60 min) ;
- **lancement** : pas de lancement sans ce texte scellé, sa contre-lecture neuve traitée et le rapport du lecteur neuf
  de conv-audit sur la version scellée (chemin et empreinte consignés) ; aucune lecture de R2 avant la relance de R1
  (inchangé).
Dans tous les cas : sorties partielles committées et poussées sur `calcul/r1-resolution-graine-v1` ; aucune donnée de
P3 hors des tableaux permis n'est lue ; arrêt de l'instance par son identifiant (R10), consigné dans
`registres/arrets.md`.

## Contre-lecture

Historique de la v1 (contre-lecture 1, vérification de concordance de conv-audit, vérification du brouillon 2) : voir
la section « Contre-lecture » de l'addendum v1, brouillon 4 ; la contre-lecture 2 de la v1 est sans objet (arrêtée,
n° 256). Pour cette v2, R2 exige une contre-lecture neuve qui porte sur le texte entier, la configuration
`prereg/R1-graine-config-v1.json` et le code au commit cité (points du n° 352 : précision et ordre des opérations,
dérivation des graines, critère du repli chiffré et éprouvé sur un cas sain et un artefact, étape 0 à l'aveugle,
contrôle croisé des 3 de C-6, règle « non inversible » et sa lecture), plus le rapport du lecteur neuf de conv-audit.

- **Contre-lecture 1** (sous-agent neuf, auteur d'aucune pièce) : À REMPLIR (identifiant ; brouillon relu, empreinte ;
  chemin et empreinte du rapport ; traitement de chaque remarque).
- **Lecteur neuf de conv-audit** (n° 352, point 1) : À REMPLIR (chemin et empreinte du rapport ; traitement).

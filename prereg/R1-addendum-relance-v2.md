# Addendum au préenregistrement de R1 — rejeu à graine des 7 épisodes non résolus et table de tokenisation v3 — v2

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 2 (texte, non
  scellé)**, qui remplace le brouillon 1 (même fichier, commit `21a6e583`,
  `7915a3d653d4de7a41b8fc22d86e4988ede765ae8638ccc335029f9a08644784`). Nom nouveau (R12) : l'addendum v1
  (`prereg/R1-addendum-relance-v1.md`, brouillon 4, commit `72f68fea`, local, non scellé) n'est pas modifié ; il reste
  archivé et sert de base à l'addendum v3 (voir « Portée »).
- Date (UTC) : 2026-11-02 10:19 (brouillon 2 ; heure relevée par `date -u`).
- **Portée (décision de la session, n° 262 et 265 de session-depot).** Cette v2 ne porte plus que le **rejeu à graine** :
  étape 0, validation à l'aveugle sur les 147 épisodes résolus ; étape 1, résolution des 7 (dont les 3 de C-6 en
  contrôle croisé) ; étape 1 bis, lot fidèle pour les épisodes encore non résolus ; étape 2, table de tokenisation v3,
  scellée. **La relance de R1 sur la table v3 passe dans un addendum v3** (`prereg/R1-addendum-relance-v3.md`, nom
  réservé), écrit et scellé **après** la table v3, dont il citera l'empreinte (elle n'existe qu'après la carte). Tout ce
  qui, dans le brouillon 1, ne concernait que la relance en est retiré et renvoyé à l'addendum v3 (section « Écarts à
  l'addendum v1 et renvoi à l'addendum v3 »).
- **Demande de Lazar** : « il faut résoudre tous les épisodes » (2 novembre 2026, 09:15, heure de Paris, dans la session
  de conv-audit ; message n° 348 de conv-audit, `c12099b1deb005cdaee81b18a02d7fffcb6b8119d7f3fc67e5d60d84b0a21127`,
  branche `canal/conv-audit-n04`) ; redite dans la session de session-depot : « résoudre les 7 épisodes avant la
  relance ». Ordre choisi par Lazar (≈ 08:28 UTC, relayé au n° 257 de session-depot) : **rejeu à graine d'abord, table
  complète, une seule relance de R1** ; la séquence « R1 à r = 3 maintenant » (n° 350 et 351 de conv-audit) est retirée
  (n° 352, `b4852257210e1caa8c8d90dd421f886c4a081df24e405bd2c3dcf1a65fd51d30`).
- **Méthode** : le rejeu à graine proposé au n° 256 de session-depot, section 2
  (`2f8149805f960cfac3ea94a13f4d736537e5ad67ac8f5cbe0037483a4ba79de7`), accepté par conv-audit au n° 351
  (`d92679194ba0c8b508649c44d29d88204b5591b678b624ce0f25af96ffcc4943`, qui retire sa recherche en faisceau du n° 349,
  `4f3d6e2d71a65b5491e25aef8d3e6684cb0b1a56fc6b46eb531b513884afd697`). Mode « génération de P3 refaite par lots »
  proposé au n° 257, accepté par conv-audit au n° 352 ; il est ici l'**étape 1 bis** (« lot fidèle »). Points que le
  lecteur neuf de conv-audit vérifiera : n° 352, point 1 ; précisions de forme : n° 354, point 1
  (`ef4a15d55d55910208d6f2f9bb94c35c13bbc73f09006185da5d5d5e7b78c3b1`) ; liste des épisodes non inversibles au
  versement : n° 356, point 4 (`da210e95993035d9ca694303083be883c94688b053366b4a766763de68648c45`). Changements annoncés
  à conv-audit : n° 262 de session-depot (branche `canal/session-depot-reprise-n89`) et n° 265 (branche
  `canal/session-depot-reprise-n92` ; la validation devient une mesure rapportée, non un arrêt).
- **GO** : `GO-2026-11-02-02`, ligne d'extension (R-389) inscrite dans `registres/go.md` de `main` au commit
  `ddfff6e4281b82fcd3b6ac9997fe47e15a62b0aa` (R-1034), sur le mot direct de Lazar dans la session de session-depot
  (≈ 08:32 UTC) : « GO-02 couvre le rejeu à graine et le complément des épisodes restants » ; plafond 25 USD inchangé ;
  échéance 2026-11-09. La garde de calcul l'accepte (essai du n° 258 ; relu au n° 262 : code 0).
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65`.
- Commit du code d'analyse : `À REMPLIR (code final)`
  (code corrigé après la vérification adverse VG-01 à VG-10, sur la base de `5c39c6b6` pour
  `resolution_graine_v1.py` et de `99022f43` pour `resolution_graine_lot_v1.py` ; `resolution_tokenisation_v1.py` et
  `rejeu_activations_v2.py` non modifiés)
- Empreintes des fichiers de code au commit cité : À REMPLIR (code final) — fichiers :
  `src/controle_ia/runs_nuit/resolution_graine_v1.py`, `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py`,
  `tests/test_resolution_graine_v1.py`, `tests/test_resolution_graine_lot_v1.py`,
  `scripts/r1_resolution_graine_instance_v1.sh`, `scripts/amorce_instance_r1_resolution_graine_v1.sh` (ou leurs noms
  neufs, si le correcteur en change, R12).
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-v1.json`
- Configuration de la résolution à graine (empreinte canonique) : `À REMPLIR (code final)`
  (fichier unique pour la passe forcée et le lot fidèle ; empreinte par `resolution_graine_v1.empreinte_config` sur le
  fichier écrit par le correcteur du code, puis scellé)
- Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `À REMPLIR (code final)`
  (même fichier, donc même valeur que la ligne précédente, tant que le code final garde ce libellé propre au lot)
- Entropie : `36410133060804533274328900142752730279` (celle du parent : le rejeu à graine ne tire rien ; son manifeste
  porte `aucun-tirage-propre`, les graines viennent du manifeste de P3)
- Tests attendus : `À REMPLIR (code final)`
  (fichiers que lance le script d'instance : `tests/test_resolution_graine_v1.py`, `tests/test_resolution_graine_lot_v1.py`,
  `tests/test_manifeste.py`, `tests/test_scellement.py`, `tests/test_prereg.py`, `tests/test_harnais_formats.py` ; au
  commit de base : 43 pour la liste de la passe forcée, plus 9 essais du lot ; le nombre final vient du code corrigé ; un
  test sauté arrête le script, qui exige ce nombre exactement)
- Documents qui font foi (chemin + empreinte) : le parent ci-dessus ; l'addendum v1, brouillon 4, pour les faits de
  P3 qu'il établit (`prereg/R1-addendum-relance-v1.md`, commit `72f68fea`) ; table de tokenisation v2
  `prereg/R1-table-tokenisation-v2.json` (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`, commit
  `cdca33bb` ; son `.sha256` est à écrire avant le scellement, `charger_pieces` l'exige) ; manifeste de P3
  `runs/20261019-230011-p3-reel/manifeste.json` (`3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685`) ;
  rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; résultat de C-6
  `docs/notes/runs-r1-r2-r4-v1/resultat-c6-v1.json` (`1e11d58fa75be359ffb185136cd2c83b1275203eb9f0162f0a5413222767b238`) ;
  messages cités dans l'en-tête ; GO ci-dessus.

**Statut.** Cet addendum résout, avant la relance de R1, les **7 épisodes** que les étapes 1 à 3 de la règle A n'ont pas
résolus (dont les 4 que C-6 laisse non résolus), par **rejeu à graine** : passe forcée d'abord, lot fidèle ensuite pour
ce qui reste. Un épisode n'est « résolu » que par l'**égalité de son empreinte de trajectoire avec celle de P3**
(sha256, 256 bits), quelle que soit la voie qui l'a trouvé. La **validation à l'aveugle sur les 147 épisodes déjà
résolus est une mesure rapportée, jamais un arrêt** : la résolution part quelle que soit sa lecture. Le texte gèle la
méthode, ses bornes, ses mesures, leur lecture et la construction de la table v3. Il porte sur R1 seule ; R2 ne se
relance pas ; le rejeu de R4 n'est pas relancé (comme la v1). Il ne lit aucun score.

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
  génération par lots de 8 (plan `plan_p3`, lots consécutifs : 30 lots, 240 épisodes), remplis à gauche, avec cache
  (préremplissage, puis une passe par jeton, `logits_to_keep=1`, positions explicites), modèle en bfloat16 sur
  A100-SXM4-80GB ; torch `2.14.1+cu130`, pilote 580.159.03, cuDNN 92400 (lus dans `episodes-p3.json`, VG-05) ; à chaque
  pas, logits du dernier jeton ramenés **sur processeur en float32** (`.to("cpu", torch.float32)`), puis
  `torch.multinomial(torch.softmax(logits / T, -1), 1, generator=g)` ; **un générateur par action**,
  `torch.Generator('cpu').manual_seed(graine)`, avancé d'un tirage par jeton tant que la ligne est active ; graine de
  l'action tirée par `graines_des_actions(generateur(graine de la tâche), 1, T)`, clé `tache/<identifiant>` du
  manifeste de P3 (le `g.random(T)` qui suit dans `jouer_p3` ne change pas ces graines) ; mêmes graines d'une condition
  à l'autre (vérifié sur processeur avec les vraies pièces de P3). Durée de la génération de P3 : 11 179 s pour 30 lots.
- (e) **identité du tirage** : sur torch 2.14.1, `torch.multinomial(p, 1, generator=g)` est exactement
  `argmax(p / q)`, `q` vecteur de V tirages exponentiels pris au même générateur ; un appel unique de n × V tirages
  égale n appels de V. Vérifié sur processeur, en float32 (200 graines, 200 égalités, n° 256 ; essais du module ;
  consommation du générateur comprise, vérification adverse) et **revérifié au lancement** sur la bibliothèque installée
  (`exiger_equivalence_tirage`, arrêt sinon).

## Écarts à l'addendum v1 et renvoi à l'addendum v3

« v1 » = `prereg/R1-addendum-relance-v1.md`, brouillon 4. La numérotation du brouillon 1 est gardée pour la concordance
de conv-audit ; les lignes retirées sont renvoyées à l'addendum v3, sans être tranchées ici.

| n° | Ligne ou règle de la v1 | Règle de cette v2 | Raison |
|---|---|---|---|
| G1 | Étape 0 de la v1 : table v2 (règle A, étapes 1 à 3, puis C-6) ; 4 non résolus traités par la règle B | **Étapes 0, 1, 1 bis et 2 ajoutées** (rejeu à graine) : validation à l'aveugle sur les 147 résolus, mesure rapportée ; résolution des 7 ; lot fidèle pour ce qui reste ; table v3 = table v2 dont chaque épisode « non résolu » que le rejeu résout reçoit une entrée de forme « identifiants » ; les 18 corrections de la v2 restent telles quelles | Demande de Lazar (n° 348) ; méthode du n° 256 acceptée (n° 351) ; lot du n° 257 accepté (n° 352) |
| G2 | E2 (règle B pour 7 − r épisodes) | Ici, seulement la **liste des épisodes que le rejeu laisse non résolus, chacun avec sa cause écrite**, remise à Lazar avant l'addendum v3 et avant toute lecture (n° 356, point 4) ; le sort de chacun (règle B ou autre) est fixé dans l'addendum v3, après la décision de Lazar pour toute cause autre que U+FFFD | « Résoudre tous les épisodes » ; la règle « non conforme » ne reste que pour le cas déclaré |
| G8 | E9 et « Coût et GO » : relance seule | **Passage sur carte ajouté**, avant la relance, sous la même ligne GO-2026-11-02-02 (extension R-1034) ; devis à la section « Plan d'analyse » | Dépense nouvelle couverte par le mot de Lazar (n° 258) |

**Renvoyé à l'addendum v3** (retiré de ce texte) : G3 (ligne E19 et décision N-A, « couverte, pour les épisodes
nommés »), G4 et G5 (prédiction P-R5 et comptes à r′), G6 (configuration du rejeu v5, module `rejeu_activations_v3`,
code « R2 seul » de conv-audit), G7 (tests de la relance), G9 (contre-contrôle négatif étendu), G10 (traitement de
C-1) ; prédiction P-R5 ; étape 3 du brouillon 1 (préalables, complément court) ; ligne « Relance » des critères de
lecture. L'addendum v3 citera l'empreinte de la table v3 et celle du résultat scellé de ce rejeu ; sa concordance par
conv-audit portera sur sa différence avec le brouillon 3 de la v1 (n° 354, point 1).

Inchangés ici : le parent et la v1 pour tout ce qui ne touche pas au rejeu à graine (rien de la relance n'est lancé par
ce texte).

## Hypothèse

Hypothèses de travail de l'instrument (aucune hypothèse du programme n'est en jeu ; H-R1 inchangée, parent) :
- **HG-1 (graines)** : les graines des actions, dérivées du manifeste de P3 comme `jouer_p3`, sont celles que P3 a
  utilisées ; avec elles et l'identité du tirage (fait (e)), chaque jeton tiré par P3 est l'argmax de p / q.
- **HG-2 (précision de la passe forcée)** : les logits recalculés par une passe forcée par l'enseignant, sans lot ni
  cache, en bfloat16 sur la carte, ne diffèrent de ceux de la génération de P3 (lot de 8, remplissage à gauche, cache)
  que par des arrondis, **petits devant l'écart entre les candidats compatibles avec le texte**, sauf aux
  quasi-égalités, que le repli écrit traite.
- **HG-3 (inversibilité)** : le texte stocké est l'image exacte des identifiants tirés, aux pertes déclarées près (fait
  (a)) ; un épisode qui contient U+FFFD n'est inversible que si les octets inconnus se retrouvent par un balayage borné
  du vocabulaire.
- **HG-4 (lot fidèle)** : refaite dans son lot (même plan, même remplissage, même cache, même ordre d'appels, mêmes
  conversions, même carte et même bibliothèque), la génération de P3 redonne ses logits au bit près pour la ligne cible
  et pour les lignes voisines dont les jetons sont exacts ; les lignes voisines approchées (découpage canonique à
  longueur forcée exacte) ne changent pas la forme du lot, donc pas les logits des autres lignes. Éprouvé sur processeur
  (égalité au bit des empreintes des logits avec `jouer_episodes`, lots de 8 et de 4) ; jamais garanti au bit entre
  deux exécutions sur carte.

Sous HG-1 à HG-4, la reconstruction d'un épisode est l'unique suite d'identifiants qui redonne l'empreinte de P3 ;
l'empreinte en est la preuve (256 bits), quelle que soit la voie qui l'a trouvée. Une graine fausse ne peut rien
fabriquer : elle ne résout rien.

## Prédiction chiffrée et signe attendu

- **P-G1 (validation, étape 0, mesure)** : **147 empreintes de P3 retrouvées sur 147** (129 identiques de base et 18
  corrigés par la table v2), à l'aveugle, confiance ≈ 0,8 ; au moins 140 par la voie directe (sans repli) ; accord du
  choix non contraint avec le jeton connu, **au moins 0,99 en moyenne** sur les 147 et au moins 0,95 dans chaque épisode,
  confiance ≈ 0,7 (une graine fausse ferait tomber cet accord vers la probabilité du jeton le plus probable,
  typiquement 0,6 à 0,85). Ces valeurs sont des prédictions, non des seuils d'arrêt (R3 : rien n'est relancé pour les
  atteindre). Réfutation de P-G1 : moins de 147 retrouvées, ou accord moyen sous 0,95.
- **P-G2 (résolution, étapes 1 et 1 bis)** : **au moins 6 des 7** épisodes résolus (empreinte de P3 retrouvée) à la fin
  de l'étape 1 bis, confiance ≈ 0,8 ; **7 sur 7**, confiance ≈ 0,6 ; par la passe forcée seule (étape 1), au moins 5 des
  7, confiance ≈ 0,6. Les 3 de C-6 résolus avec les identifiants de la table v2 (contrôle croisé « conforme »),
  confiance ≈ 0,95 (ils font déjà partie des 147 de l'étape 0). L'épisode le plus exposé : `mention/2605.17899v2/e0`,
  qui contient un U+FFFD (hypothèse 4 plausible pour lui) ; s'il reste non résolu, sa cause attendue est « caractère de
  remplacement : cas non simple ». Les découpages qui changent le nombre de jetons d'un mot en compensant ailleurs,
  non explorés par C-6, sont couverts par construction (le choix est pas à pas, seule la longueur totale de l'action
  est contrainte).
- **P-G3 (fragilité numérique de la passe forcée, descriptif)** : sur les 147, écart contraint (premier contre second
  candidat compatible) sous 1 nat dans moins de 1 % des pas à plusieurs candidats ; désaccords du choix non contraint
  concentrés sur des marges sous 0,5 nat. Mesure sur le modèle minuscule en bfloat16 (essais du code de base) : 16
  épisodes sur 16 résolus directement, deux désaccords non contraints à des marges de 0,012 et 0,015, 0,3 % des pas à
  plusieurs candidats sous 0,1 d'écart ; le 8B n'est pas mesuré avant la carte.
- **P-G4 (lot fidèle, étape 1 bis, mesure)** : sur les lignes résolues des lots ciblés (au plus 21 lignes : 8 lignes par
  lot, moins la cible et les lignes approchées), accord du choix non contraint avec le jeton connu **au moins 0,999 en
  moyenne**, confiance ≈ 0,7 (fidèle au bit, il vaut 1 exactement) ; chaque épisode cible du lot, s'il est inversible,
  résolu par l'essai direct, confiance ≈ 0,6.

## Métrique

Chaque épisode est **consigné dès qu'il est terminé** (VG-01), avec sa voie, ses bascules, sa durée et, s'il n'est pas
résolu, sa cause ; un arrêt ou une coupure ne perd que l'épisode en cours. Résultat scellé par étape
(`diag/<run>/resolution-graine-<etape>.json`, pas par pas dans `diag/<run>/pas-resolution-graine-<etape>.npz` ; noms
exacts fixés par le code au commit cité) :
- **empreintes retrouvées** : nombre d'épisodes dont l'épisode reconstruit redonne exactement l'empreinte de trajectoire
  de P3 (`empreintes_retrouvees`), dont par voie directe (`directes`), par repli (`par_repli`) et, à l'étape 1 bis, par
  le lot fidèle ; c'est la **seule métrique qui fait un « résolu »** ;
- **épisodes non résolus** et **non traités**, chacun avec sa cause : empreinte non retrouvée après repli ;
  contradiction entre texte, longueurs et choix ; « caractère de remplacement : cas non simple » ; « durée » (budget de
  l'épisode épuisé) ; « non traité : durée de l'étape » ;
- **identifiants égaux** (comparaison aux identifiants connus, après la résolution de tous les épisodes de l'étape
  seulement) : épisodes (`identifiants_egaux_episodes`) et actions (`actions_egales` sur `actions_comparees`) ;
- **accord du choix non contraint** : part des pas où l'argmax de p / q sur tout le vocabulaire (l'opération de P3)
  égale le jeton connu (validation) ou retenu (résolution) ; **moyenne sur les épisodes, et valeur de chaque épisode**
  (`accord_non_contraint`) ; diagnostic des graines et de la précision ;
- **écart contraint** : par pas à plusieurs candidats compatibles, écart en nat entre le premier et le second candidat ;
  **distribution** (quantiles et comptes sous 0,01, 0,05, 0,1, 0,25, 0,5, 1 et 2 nats, `ecarts_contraints`) ; **marges
  en désaccord** : marge du choix non contraint aux pas où il diffère (`marges_en_desaccord`) ;
- **repli** : combinaisons essayées par épisode, profondeur atteinte, bascules retenues ;
- **premier écart de la voie directe** quand elle échoue (`erreurs_directes`) ; **contrôle croisé** des 3 épisodes de
  C-6, lu à trois valeurs (`controle_croise` : « conforme », « non résolu », « contraire », VG-06) ;
- **U+FFFD** : déclarés par épisode (`fffd_declares`) et **balayages du vocabulaire comptés** par épisode (VG-07) ;
- **lot fidèle** : par épisode cible, numéro du lot, rang dans le lot, lignes voisines exactes et approchées (comptées et
  nommées) ; **accord non contraint des lignes résolues des mêmes lots** (moyenne et par ligne) ; empreintes sha256 des
  logits de la ligne cible par pas ;
- carte, versions (torch, `torch.version.cuda`, pilote, cuDNN), passes, jetons en passe, durées.
Comptes exacts, sans tirage propre : aucun intervalle n'est calculé (la méthode est déterministe aux arrondis près ;
ces arrondis sont ce que mesurent l'écart contraint et l'accord). Aucune moyenne sur les jetons n'entre dans une sonde.

## Seuil

Il n'y a **aucun seuil d'arrêt sur une mesure** : les seules bornes du code sont des bornes de travail (repli, durée,
balayages) ; leur dépassement donne un « non résolu » ou un « non traité » avec sa cause, jamais un arrêt.

**Configuration** `prereg/R1-graine-config-v1.json` (fichier unique pour les deux modules ; **écrit par le correcteur du
code**, qui en connaît les clés exactes, puis scellé ; empreinte canonique à l'en-tête). Clés et valeurs gelées ici ;
quand le nom exact d'une clé neuve n'est pas encore fixé par le code, il est dit « nom proposé » et la valeur fait foi :
- **repli de la passe forcée** : `seuil_ecart` = **1,0** nat (quasi-égalité : écart contraint sous ce seuil ; je tiens
  pour fragile un écart sous 0,5 à 1 nat pour le 8B en bfloat16 : la garde d'équivalence de P3 tolérait jusqu'à 0,2
  d'écart relatif sur les activations, au 99e centile, entre génération et passe unique) ; `quasi_egalites_max` = **16**
  par essai (les plus fragiles d'abord) ; `bascules_max` = **2** (profondeur du repli itératif) ; `combinaisons_max` =
  **136** essais rejoués au plus par épisode (16 + 120), **en validation comme en résolution** (VG-03 : paires permises
  en validation ; la clé `combinaisons_max_validation` disparaît, ou vaut 136 si le code la garde) ;
- `balayages_max` = **64** balayages du vocabulaire par épisode pour les octets que recouvre un U+FFFD ;
- **budgets de durée** (VG-01) : budget par épisode de la passe forcée = **600 s** (nom proposé `budget_episode_s`) ;
  `duree_max_s` = **2 400 s par étape** (validation ; résolution) ; budget par épisode du lot = **900 s** (nom proposé
  `budget_episode_lot_s`) ; durée maximale de l'étape 1 bis = **3 600 s** (nom proposé `duree_max_lot_s`) ;
- **lot fidèle** : `episodes_resolution_lot` = **liste vide**, qui veut dire : les épisodes non résolus du résultat
  scellé de l'étape 1, **pris parmi les 4 non résolus de la table v2** (au plus 4 ; un épisode de C-6 non résolu à
  l'étape 1 n'est pas une cible, son entrée de C-6 est déjà prouvée par l'empreinte) ; `combinaisons_max_lot` = **16**
  (bascules simples et doubles comprises, dans l'ordre du repli itératif) ; `episodes_validation_lot` et
  `seuil_validation_lot` disparaissent (la validation du lot est mesurée sur les lignes résolues des mêmes lots, sans
  passe de plus et sans seuil) ; taille du lot et plan : ceux de P3 (`plan_p3`, 8), reconstruits, non configurables ;
- **échantillonnage** : `T` = 10, `temperature` = **1,0**, `max_nouveaux` = **400** (comparés à la configuration de P3
  par le module) ;
- **exécution** : `noyau_attention` = « defaut » (le noyau de P3, « sdpa » ; toute autre valeur refusée, VG-04) ;
  `hors_ligne` = vrai ; `fils` = 1 ; `fils_tirages` = 8 ; `episodes_d_avance` = 2 ; `mode` = « reel » ;
- `episodes_resolution` = les 7, dans cet ordre : `honnete/2602.00987v1/e0`, `mention/2605.17899v2/e0`,
  `saboteur/2510.05132v3/e0`, `temoin/2512.06870v2/e0`, `honnete/2512.05150v2/e0`, `honnete/2512.11131v1/e0`,
  `temoin/2510.24788v1/e0` ;
- **pièces** : celles de la configuration v4 (`agent` : `meta-llama/Llama-3.1-8B-Instruct`, révision
  `0e9e39f249a16976918f6564b8830bc894c89659`, `date_string` « 26 Jul 2024 » ; `run_source` = le run de P3 ; textes
  `ba05fa13…`, scores (identité seule) `968414fc…`, identité `1f25adbd…`, fiches `1a96cbf8…`, tâches `287e8348…`,
  consignes `a68468fe…`, chemins et empreintes complètes dans le fichier), plus le manifeste de P3
  (`chemin_manifeste_p3`, `3f21774c…`) et la table v2 (`chemin_table_tokenisation`, `5f6cf489…`) ;
- la clé `seuil_validation` disparaît (la validation n'arrête plus rien).

**Seuils de lecture** (critères de lecture, non gardes du code) : accord du choix non contraint **≥ 0,95 en moyenne**
sur les 147 et **≥ 0,90 dans chaque épisode** ; accord des lignes résolues des lots ciblés **≥ 0,99 en moyenne**. Sous
l'un d'eux, une réserve est écrite au résultat (« Critères de lecture gelés ») ; rien ne s'arrête. Seuil de la règle B
de la v1 (10 épisodes, E3) : inchangé, lu dans l'addendum v3.
**Déclaré** : ces valeurs sont fixées en connaissant les comptes (147 résolus, 7 à résoudre, plan des lots) et les
mesures du modèle minuscule, non celles du 8B ; aucune mesure du 8B n'a été faite.

## Plan d'analyse

**Données.** Pièces de P3 citées par la configuration, vérifiées par empreinte au chargement : textes des actions ;
de `scores-p3.npz`, **seuls** les tableaux d'identité, `jetons` et `jetons_notes`, chargés clé par clé
(`charger_identite_sans_scores`) ; fiches (empreintes de trajectoire) ; tâches ; consignes, lues seulement par
`charger_consignes`, qui en vérifie l'empreinte ; manifeste de P3 (graines, agent). Aucun score, aucune note, aucune
étiquette, aucune activation n'est lu. Graines (R9) : celles de P3, dérivées comme `jouer_p3` ; le rejeu ne tire rien.
Volumes (vraies pièces, processeur) : validation, 147 épisodes, 1 470 actions, 4 143 855 jetons en passe, 309 797 pas ;
résolution, 7 épisodes, 214 193 jetons en passe.

**Méthode de la passe forcée** (`resoudre_action`, `rejouer_episode`, `resoudre_avec_repli`). Pour chaque épisode,
action par action, dans le contexte exact (identifiants déjà retrouvés des actions précédentes ; ouverture, tours et
clôtures comme le harnais) :
1. **Passe forcée** par l'enseignant, sans cache ni lot, sur le découpage courant (découpage canonique du texte restant,
   plus le jeton de fin par défaut).
2. À chaque pas, **choix contraint** : parmi les jetons compatibles avec les octets restants du texte stocké (décodeur au
   niveau de l'octet ; jetons spéciaux hors fins : zéro octet), celui qui maximise p / q ; dernier pas : un jeton de fin
   (parmi `fmt.fins`) si `jetons − jetons_notes` = 1, sinon l'action doit compter exactement 400 jetons. Si le choix
   diffère du découpage courant, le reste est redécoupé canoniquement et une nouvelle passe est faite.
3. Consigné à chaque pas : choix contraint, choix non contraint (argmax de p / q sur tout le vocabulaire), nombre de
   candidats, écart contraint, second candidat, marge non contrainte, balayage.
4. **Arbitre unique** : l'empreinte de trajectoire de P3, recalculée sur l'épisode reconstruit (`empreinte_trajectoire`
   du rejeu v1, celle du harnais).
5. **Repli itératif** (VG-02) si l'empreinte n'est pas retrouvée. Niveau 1 : chaque quasi-égalité de l'essai direct
   (écart sous `seuil_ecart`, au plus `quasi_egalites_max`, les plus fragiles d'abord) est basculée seule vers son second
   candidat, et l'épisode est rejoué depuis l'action basculée. Niveau 2 : pour chaque essai du niveau 1, dans le même
   ordre, ses **propres** quasi-égalités situées après la première bascule (recalculées sur l'essai rejoué, donc y
   compris celles d'une autre action, que le contexte corrigé fait apparaître) sont basculées à leur tour, les plus
   fragiles d'abord. Au plus `bascules_max` bascules par essai et `combinaisons_max` essais par épisode, chacun arbitré
   par l'empreinte ; un essai déjà fait n'est pas refait. L'ordre exact est celui du code au commit cité ; la
   contre-lecture le compare à cette règle. Le repli à deux bascules du code de base, aveugle à une seconde erreur
   placée dans une autre action (0 paire sur 14 reproduites sur le modèle minuscule), est remplacé.
6. **Budget** : un épisode qui dépasse son budget (600 s) s'arrête en « non résolu : durée », consigné, et l'étape
   passe au suivant ; une étape qui atteint `duree_max_s` se clôt proprement : ses épisodes terminés restent consignés,
   les autres sont « non traité : durée de l'étape ».
7. **U+FFFD** : compté par épisode ; les octets inconnus qu'il recouvre sont cherchés par balayage du vocabulaire
   (balayages comptés), au plus `balayages_max` par épisode ; au-delà, non résolu « caractère de remplacement : cas non
   simple » — le seul cas qui peut être déclaré **non inversible** (HG-3), selon « Critères ».

**Précision et ordre des opérations (n° 351, points (a) et (b) ; n° 352).** Le modèle est chargé en **bfloat16**, son
format natif, comme dans P3 (`charger_modele` refuse un point de contrôle qui ne l'est pas ; attention « sdpa » ; même
révision ; torch 2.14.1 exigé).
- **Passe forcée** : logits calculés en bfloat16 sur la carte, ramenés **sur processeur en float32**, puis
  **p = softmax(logits / T) en float32 sur processeur**, l'ordre des opérations de P3. Le **choix contraint** est
  calculé **en double précision, à partir de ce p en float32**, sur les seuls candidats (p / q, ou son logarithme, même
  ordre ; égalité exacte : plus petit identifiant, comme `argmax`), au lieu de p / q en float32 : **déclaré**. Les deux
  ne peuvent différer que si deux candidats sont à moins d'un arrondi de float32 (≈ 10⁻⁷ en relatif), très en deçà du
  bruit du bfloat16 ; un tel cas est une quasi-égalité, que le repli traite. Le **choix non contraint** est l'opération
  de P3 sur tout le vocabulaire (diagnostic seulement). Ce qui diffère de P3, déclaré : la passe est **pleine, sans lot
  ni cache ni remplissage**, au lieu du décodage pas à pas par lots de 8 remplis à gauche ; les accumulations en
  bfloat16 diffèrent, donc les logits diffèrent aux arrondis près (HG-2 : raison d'être de l'écart contraint, du repli,
  de la validation et du lot fidèle). Les tirages exponentiels sont calculés sur processeur, en float32, au générateur
  de l'action, comme dans P3.
- **Lot fidèle** : l'opération même de P3, sans écart déclaré sur le calcul : logits du dernier jeton en float32 sur
  processeur, `softmax(logits / T)` en float32, divisé par q en float32, argmax parmi les candidats compatibles (égalité :
  plus petit identifiant).
- **Carte attendue : A100-SXM4-80GB**, celle de P3. Une autre carte n'arrête pas le script : réserve écrite au résultat
  (« carte différente de P3 »). `torch.version.cuda` différent de 13.0, pilote ou cuDNN différents de ceux de P3 :
  **réserve écrite au résultat**, pas un arrêt (VG-05). torch différent de 2.14.1 : arrêt (liste d'arrêt).
- **Location** : le filtre de la procédure exige « centre de données » ; s'il n'y a aucune offre A100-SXM4-80GB sous ce
  filtre (cas du 2 novembre, n° 262 : trois offres à 1,07–1,22 USD/h, aucune sous le filtre strict), **ce seul critère
  est retiré**, et ce retrait est consigné au journal et au résultat (déclaré).

**Étape 0 — validation à l'aveugle (carte ; mesure rapportée).** `--etape validation` sur les 147 épisodes à
identifiants connus (129 identiques de base ; 18 corrigés par la table v2 : 1 jeton de fin, 12 une paire, 2 deux paires,
1 trois paires, 2 fenêtres). **À l'aveugle** : la table v2 sert seulement à choisir les épisodes de l'étape (`classer`,
`episodes_de_l_etape`) ; les fonctions de résolution ne reçoivent que les textes, les longueurs, les graines et
l'empreinte de P3 ; les identifiants connus ne sont lus qu'après la résolution de tous les épisodes de l'étape, pour les
mesures. Repli itératif avec paires, comme en résolution (VG-03). Mesures rapportées : épisodes retrouvés sur 147 (dont
directs et par repli), accord du choix non contraint (moyenne et par épisode), distribution des écarts contraints,
marges en désaccord ; les 18 corrigés, ceux où la graine compte (un découpage non canonique n'est retrouvé que si p / q
le désigne), sont rapportés à part. **Aucun arrêt sur ces mesures** ; la résolution part ensuite quelle que soit leur
lecture. Remarque : sur un épisode canonique, le choix contraint est le plus souvent imposé par les octets et la
probabilité, même avec une graine fausse ; l'empreinte retrouvée ne prouve donc pas seule les graines : l'accord non
contraint les contrôle.

**Étape 1 — résolution des 7 (carte).** `--etape resolution --validation diag/<run>/resolution-graine-validation.json`.
Exige seulement que la validation soit scellée, de **même configuration** et de **même code** (comparaison de l'arbre
gelé : `exiger_validation`, `exiger_meme_code`), **quelle que soit sa lecture**. Les 7 épisodes de
`episodes_resolution` : les 4 non résolus et, en **contrôle croisé**, les 3 de C-6, lus à trois valeurs : **conforme**
(empreinte retrouvée, identifiants égaux à ceux de la table v2) ; **non résolu** (empreinte non retrouvée) ;
**contraire** (empreinte retrouvée avec d'autres identifiants que la table v2). Repli et budgets ci-dessus.

**Étape 1 bis — lot fidèle (carte ; module `resolution_graine_lot_v1.py`).** `--etape resolution-lot --resolution
diag/<run>/resolution-graine-resolution.json`, pour les seuls épisodes que la passe forcée et ses bascules laissent non
résolus, pris parmi les 4 non résolus de la table v2 (au plus 4). La génération de P3 est refaite par lots de 8 : plan
des lots reconstruit (`plan_p3`, 30 lots consécutifs, vérifié contre l'ordre des textes de P3) ; sur les vraies pièces,
les 4 non résolus de la table v2 tombent dans les lots 0, 5, 14 et 24 (rangs 4, 3, 5 et 6 dans leur lot), avec 2, 1,
1 et 3 lignes voisines approchées. Remplissage à gauche, masque, positions explicites, préremplissage puis une passe par
jeton avec cache (`logits_to_keep=1`), bfloat16, logits en float32 sur processeur, softmax divisé par q comme P3 ; ligne
cible choisie parmi les candidats compatibles avec le texte stocké ; **lignes voisines forcées à leurs jetons connus**
(identiques de base, table v2, résolus par l'étape 1 ou plus tôt par le lot, revérifiés par l'empreinte) **ou
approchées** (découpage canonique à longueur forcée exacte, jeton de fin par défaut ; **déclarées et comptées**, lot
déclaré « approché ») ; les passes s'arrêtent quand la ligne cible est finie. Arbitre : l'empreinte de P3. Repli : le
repli itératif ci-dessus, borné par `combinaisons_max_lot` et le budget de 900 s par épisode ; U+FFFD : même balayage.
**Validation du lot** : mesurée sur les lignes résolues des mêmes lots, pendant les mêmes passes (sans passe de plus) :
accord du choix non contraint de chaque ligne forcée avec son jeton connu, aux pas joués ; **sans arrêt**. Propriété
éprouvée sur processeur : logits égaux au bit près à la génération originale (lots de 8 et de 4) ; non garantie entre
deux exécutions sur carte, d'où la mesure. Un épisode résolu par le lot entre dans la table v3 avec la voie « lot
fidèle » ; un épisode non résolu par le lot garde la cause du lot et celle de l'étape 1.

**Étape 2 — table v3 (processeur, sans dépense).** `--etape table` (`construire_et_verifier_table`), sur les résultats
scellés des étapes 1 et 1 bis, avec le tokeniseur de la révision `0e9e39f2…`, sortie `prereg/R1-table-tokenisation-v3.json` :
table v2, dont chaque épisode « non résolu » que le rejeu a résolu (passe forcée, repli ou lot fidèle) reçoit une entrée
`identifiants` (version 3 ; actions corrigées avec leurs identifiants de base et ceux retrouvés ; voie, bascules,
empreinte du résultat) ; les 18 entrées de la v2 restent telles quelles ; **chaque correction, ancienne ou nouvelle, est
revérifiée par l'empreinte de P3** (`verifier_entrees_v3`, transcription refaite comme le harnais) ; comptes recalculés ;
la sortie n'écrase jamais (R12) et **est scellée** (`.sha256`, VG-08). La fusion des résultats du lot dans la table est
à écrire par le correcteur du code. Les non résolus y restent `non_resolu`, chacun avec la cause écrite ; leur liste
est remise à Lazar (G2). **Table complète** si les 4 sont résolus.

**Suite : addendum v3.** La relance de R1 sur la table v3 (règles A et B, contrôle négatif, échantillon de fidélité,
sorties, versement, R2 et R4 ; écarts G3 à G7, G9, G10 du brouillon 1) est préenregistrée par l'addendum v3, écrit après
l'étape 2 : il cite l'empreinte de la table v3, celle des résultats scellés de ce rejeu, le commit et le nombre de tests
de son propre code ; il est contre-lu et soumis à la concordance de conv-audit avant tout lancement.

**Calendrier.** Code corrigé (VG-01 à VG-10, fusion du lot dans la table) et ses essais sur processeur ; configuration
`prereg/R1-graine-config-v1.json` écrite et scellée par le correcteur ; `.sha256` de la table v2 ; **répétition jouet
du script d'instance** sur processeur avant toute location (VG-09 : P3 jouet, toutes les étapes, lot compris ;
tokeniseur obtenu avant les tests ; code de retour de chaque commit vérifié) ; marqueurs de l'en-tête remplis ;
contre-lecture neuve et lecteur neuf de conv-audit ; scellement de ce texte ; poussée → instance A100 (étapes 0, 1 et
1 bis) → étape 2 sur processeur, table v3 scellée → liste des non résolus à Lazar s'il y en a → addendum v3.

**Coût et GO.** A100-SXM4-80GB, ≈ **1,07 à 1,22 USD de l'heure** (offres du 2 novembre, n° 262). Durées estimées :
passe forcée, mise en place comprise (installation, 16 Go du modèle, tests), validation et résolution : **30 à 45 min** ;
lot fidèle : **3 à 5 min par essai direct**, au plus 4 épisodes, soit 12 à 20 min, plus le repli borné (budget de 900 s
par épisode). Attendu : ≈ 45 à 65 min, soit **≈ 0,8 à 1,3 USD**. **Bornes de durée cohérentes** (VG-01) : délais
externes du script : mise en place (installation, modèle, tests) 30 min ; puis, pour chaque étape, son budget
interne plus 5 min : validation 45 min ; résolution 45 min ; lot fidèle 65 min ; finition (sceaux, poussées)
10 min ; somme 195 min ; **plafond de l'amorce : 200 min**, au-dessus de cette somme. **Pire cas : 200 min × 1,22 USD/h ≈ 4,1 USD**, plus le disque et la descente du modèle.
Dépenses engagées sous GO-2026-11-01-13, prolongé par GO-2026-11-02-02 : ≈ 4,6 / 25 USD (relevé du 2 novembre, 03:10
UTC ; à revérifier dans le registre des dépenses avant la création) ; après ce passage, au pire ≈ 8,7 / 25 USD, plus le
disque ; la relance (addendum v3) aura son propre devis sous la même ligne. Lancement : `GO_ID=GO-2026-11-02-02` devant
la commande de création ; **échéance 2026-11-09** : après, GO nouveau sous un identifiant nouveau. Branche de résultats :
`calcul/r1-resolution-graine-v1` (une branche existante arrête le script).

**Essais (processeur, sans dépense ; code au commit cité ; nombre à « Tests attendus »).** Au code de base : 12 essais
de la passe forcée (`5c39c6b6` : identité du tirage ; graines dérivées comme `jouer_p3` ; cas sain sur un modèle Llama
minuscule de vocabulaire 128 256 avec le vrai tokeniseur de Llama 3.1, 11 découpages non canoniques, actions arrêtées à
`max_nouveaux`, un jeton spécial effacé ; artefacts R5 : graine fausse, texte altéré d'un octet, contexte décalé d'un
jeton, tous « non résolu », jamais un faux « résolu » ; repli ; U+FFFD ; forme `identifiants` ; bout en bout sur un P3
jouet joué par le vrai code de P3) et 9 essais du lot (`99022f43` : égalité au bit des empreintes des logits avec
`jouer_episodes`, lots de 8 et de 4 ; lot recomposé détecté ; graine fausse et texte altéré non résolus ; repli ; bout
en bout). **Exigés en plus du code final** (la contre-lecture vérifie leur présence, chacun sur un cas sain et un
artefact, R5) : repli itératif qui retrouve une seconde erreur placée dans une autre action ; paires en validation ;
budget d'épisode épuisé → « non résolu : durée », consigné, étape poursuivie ; durée de l'étape atteinte → « non traité »
consigné ; validation sous les seuils de lecture → résolution lancée quand même, réserve écrite ; contrôle croisé à trois
valeurs ; balayages U+FFFD comptés ; table v3 scellée et fusion du lot ; validation du lot mesurée sur les lignes
résolues, sans arrêt ; gardes avancées (sceaux de toutes les pièces avant l'installation, agent comparé au manifeste de
P3, noyau d'attention restreint) ; version CUDA différente → réserve. Vraies pièces de P3, processeur, sans modèle : 147
épisodes en validation, 7 en résolution, graines identiques d'une condition à l'autre, plan des lots reconstruit (30
lots, 4 cibles aux lots 0, 5, 14, 24).

## Critères de lecture gelés

Règle unique : un épisode est **résolu si et seulement si** son empreinte de trajectoire égale celle de P3 (256 bits) ;
aucune autre mesure ne fait ni ne défait un « résolu ». Les mesures de validation sont lues ainsi :

| Issue observée | Lecture |
|---|---|
| Validation : 147 / 147 retrouvées, accord non contraint moyen ≥ 0,95 et ≥ 0,90 dans chaque épisode | Méthode et graines validées sur les résolus ; pas de réserve |
| Validation : accord sous l'un des deux seuils (quel que soit le nombre retrouvé) | **Réserve « graines ou précision »** écrite au résultat. Les « résolus » des étapes 1 et 1 bis restent des preuves ; **aucun non résolu ne peut être déclaré non inversible** (la cause peut être la méthode) : tous deviennent des nœuds à Lazar ; audit (R4) avant l'addendum v3 |
| Validation : moins de 147 retrouvées, accord au-dessus des seuils | Mesure de la fragilité numérique de la passe forcée : les épisodes manqués, leurs causes et leurs écarts sont rapportés ; le lot fidèle reste la voie des non résolus ; si un manqué a pour cause « non traité : durée de l'étape », la mesure est déclarée incomplète |
| Distribution des écarts contraints | Descriptive (P-G3) ; comparée à P-G3 au résultat, sans conséquence de décision |
| Lot : accord des lignes résolues des lots ciblés ≥ 0,99 en moyenne | Lot tenu pour fidèle ; un non résolu du lot est lu comme les autres non résolus |
| Lot : accord < 0,99 | **Réserve « lot non fidèle »** (carte, bibliothèque ou plan) ; ses « résolus » restent des preuves ; ses non résolus ne peuvent être déclarés non inversibles |
| Résolution : 7 / 7 à la fin de l'étape 1 bis, contrôle croisé conforme | **Table v3 complète** ; addendum v3 sans règle B |
| Résolution : k non résolus (1 ≤ k ≤ 4, tous parmi les 4), contrôle croisé conforme | Table v3 partielle ; chaque non résolu porte sa cause ; **liste à Lazar avant l'addendum v3 et avant toute lecture** (n° 356, point 4). Cause « caractère de remplacement : cas non simple », sans réserve de validation ni de lot = **non inversible déclaré** (le texte stocké n'est pas l'image exacte des jetons) ; toute autre cause (empreinte non retrouvée après repli et lot, contradiction, durée) = **non résolu par la méthode**, jamais déclaré non inversible : **nœud porté à Lazar avant l'addendum v3** |
| Contrôle croisé « non résolu » : un épisode de C-6 non résolu par le rejeu | Discordance avec l'étape 0 si l'épisode y était retrouvé (même méthode, même configuration) : audit (R4) ; la table v3 garde l'entrée de C-6, déjà vérifiée par l'empreinte |
| Contrôle croisé « contraire » : un épisode de C-6 résolu avec d'autres identifiants que la table v2 | Impossible hors collision de sha256 : la lecture de ce rejeu s'arrête, audit (R4) avant toute suite |
| Audit de symétrie (R4) | Déclenché aussi par un résultat trop propre de la passe forcée : accord non contraint égal à 1 exactement sur tous les pas des 147 (le bruit du bfloat16 doit laisser quelques désaccords), aucune quasi-égalité sous 1 nat, ou durée très en deçà de l'estimation ; l'audit vérifie d'abord que les identifiants connus n'ont pas fui dans la résolution. Pour le lot fidèle, un accord de 1 exactement est la prédiction (HG-4), non un signal |

## Liste d'arrêt

Les arrêts sont des **erreurs de chaîne seulement** : pièces, sceaux, graines, plan des lots, bibliothèque. Aucune
mesure (validation, accord, écarts, nombre de résolus) n'arrête quoi que ce soit. Arrêts du script d'instance et des
modules (R5 ; éprouvés par les essais cités, ou lus dans le code au commit cité et à éprouver par la contre-lecture),
puis action :
- **avant l'installation** (code 2) : ce texte ou son `.sha256` absent au commit lancé ; « Tests attendus » ou « Chemin
  de la configuration de la résolution à graine » absent ou cité plus d'une fois ; configuration absente, non scellée
  ou de sceau faux ; **sceau d'une pièce faux ou absent** (textes, scores, fiches, tâches, consignes, manifeste de P3,
  table v2 ; VG-04) ; branche de résultats déjà présente ou non vérifiable ; poussée initiale refusée ;
- **bibliothèque et carte** : torch différent de 2.14.1 ; `nvidia-smi` absent ou carte indisponible pour torch ;
  tokeniseur de la révision citée introuvable avant les tests (VG-09) ;
- **tests** : dernière ligne différente de « N passed », N étant le nombre de « Tests attendus » (échec ou test sauté) ;
- **module, avant le manifeste** : configuration incomplète ou de valeur hors domaine (dont `noyau_attention` autre que
  « defaut ») ; texte qui ne cite pas l'empreinte canonique de la configuration, l'entropie ou le commit du code (arbre
  gelé différent du commit cité) ; pièce d'empreinte fausse ou calculée sur d'autres pièces ; **agent (modèle,
  révision, `date_string`, noyau) différent de celui du manifeste de P3** (VG-04) ; run du manifeste différent du run
  source ; T, température ou `max_nouveaux` différents de la configuration de P3 ; N différent de 1 ;
- **graines, pendant le run** (`arret.json`, rien d'autre n'est lu) : graine `tache/<identifiant>` absente du manifeste
  de P3 ; identité du tirage fausse sur la bibliothèque installée ; formes des logits ou des tirages inattendues ;
  dimension des logits différente de la taille du tokeniseur ; ouverture sans le texte attendu (« Today Date: 26 Jul
  2024 ») ; jeton spécial non effacé au décodage ; fins hors des jetons spéciaux ;
- **plan des lots** (étape 1 bis) : plan reconstruit différent de l'ordre des textes de P3, autre que 30 lots de 8, ou
  cibles hors des lots 0, 5, 14 et 24 ; ligne voisine donnée pour exacte dont les identifiants ne redonnent pas
  l'empreinte de P3 ;
- **chaîne des étapes** : résolution sans validation scellée de même configuration et de même code ; lot sans résultat
  scellé de l'étape 1 de même configuration et de même code ; **étape table** : résultat d'une autre configuration,
  d'une autre étape ou d'un autre code ; empreinte de P3 du résultat différente de la table v2 ; correction qui ne
  redonne pas l'empreinte de P3 ; corrections vérifiées différentes des comptes ; sortie existante (R12) ; table v3 non
  scellée ;
- **lecture** : contrôle croisé « contraire » (lecture arrêtée, audit ; voir « Critères »).
**Ce qui n'est pas un arrêt** : validation sous les seuils de lecture ; moins de 147 retrouvées ; budget d'épisode
épuisé (« non résolu : durée ») ; durée de l'étape atteinte (« non traité ») ; carte autre que l'A100-SXM4-80GB,
`torch.version.cuda` autre que 13.0, pilote ou cuDNN différents (réserves écrites au résultat) ; filtre « centre de
données » retiré faute d'offre (déclaré).
**Garde de dépense** (non une lecture) : pas de création sans `GO_ID=GO-2026-11-02-02` valide le jour même ; aucune
création après le 9 novembre 2026 sans GO nouveau ; plafond de l'amorce, 200 min, qui coupe l'instance (pire cas
≈ 4,1 USD) : ce qui est consigné par épisode reste, le reste est « non traité ».
**Lancement** : pas de lancement sans ce texte scellé, sa contre-lecture neuve traitée et le rapport du lecteur neuf de
conv-audit sur la version scellée (chemin et empreinte consignés) ; aucune lecture de R2 (inchangé).
Dans tous les cas : sorties partielles committées et poussées sur `calcul/r1-resolution-graine-v1` ; aucune donnée de
P3 hors des tableaux permis n'est lue ; arrêt de l'instance par son identifiant (R10), consigné dans
`registres/arrets.md`.

## Contre-lecture

Historique de la v1 (contre-lecture 1, vérification de concordance de conv-audit, vérification du brouillon 2) : voir
la section « Contre-lecture » de l'addendum v1, brouillon 4 ; la contre-lecture 2 de la v1 est sans objet (arrêtée,
n° 256). Le brouillon 1 de cette v2 (`7915a3d6…`) n'a pas reçu de contre-lecture ; la vérification adverse du code
(VG-01 à VG-10, n° 265) et le rapport du module « lot fidèle » ont été traités dans ce brouillon 2. Pour cette v2, R2
exige une contre-lecture neuve qui porte sur le texte entier, la configuration `prereg/R1-graine-config-v1.json` et le
code au commit cité (points du n° 352 : précision et ordre des opérations, carte comprise ; dérivation des graines ;
critère de passage entre la passe forcée et le lot fidèle, chiffré et éprouvé sur un cas sain et un artefact ; étape 0
à l'aveugle ; contrôle croisé des 3 de C-6 ; règle « non inversible » et sa lecture ; plus le repli itératif, les
budgets et la cohérence des délais), plus le rapport du lecteur neuf de conv-audit.

- **Contre-lecture 1** (sous-agent neuf, auteur d'aucune pièce) : À REMPLIR (identifiant ; brouillon relu, empreinte ;
  chemin et empreinte du rapport ; traitement de chaque remarque).
- **Lecteur neuf de conv-audit** (n° 352, point 1) : À REMPLIR (chemin et empreinte du rapport ; traitement).

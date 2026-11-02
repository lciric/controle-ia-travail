# Addendum au préenregistrement de R1 — rejeu à graine des 7 épisodes non résolus et table de tokenisation v3 — v2

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 4 (texte, non
  scellé)**, qui remplace le brouillon 3 (même fichier, commit `9ffab30d`,
  `0f4c445c9585309568d76e1f01155474be20cc76df1eac0abb4cc3dab4170e87`), successeur du brouillon 2 (commit `076a6b57`,
  `d4617ea837cd81accc4dc8e26d6d1be2015f1f10eaecad2258b3e54c9eb48c89`), lui-même successeur du brouillon 1 (commit
  `21a6e583`, `7915a3d653d4de7a41b8fc22d86e4988ede765ae8638ccc335029f9a08644784`). Nom nouveau (R12) : l'addendum v1
  (`prereg/R1-addendum-relance-v1.md`, brouillon 4, commit `72f68fea`, local, non scellé) n'est pas modifié ; il reste
  archivé et sert de base à l'addendum v3 (voir « Portée »).
- Date (UTC) : 2026-11-02 15:02 (brouillon 4 ; heure relevée par `date -u`).
- Ce brouillon traite les deux lectures neuves de conv-audit (brouillon 1 et code `5c39c6b6` : rapport
  `dd7157e188b1117c5542715452a6ca2c6a50694eab9d8a2f816615cf3bf9067b` ; brouillon 2 et lot `99022f43` : rapport
  `06459850ff7ece9e69b94d88867ce8e75ad96ba4b9091ee57b6cf64df2f54635`), la vérification adverse du code `5c39c6b6`
  (VG-01 à VG-10, traitée aux commits `755959e1` et `31f72147`) et la **vérification neuve finale** du brouillon 3 et du
  code `31f72147` (VI-01 à VI-16, verdict « scellable après corrections »), et décrit le code au commit cité ci-dessous ;
  le traitement de chaque point est à la fin (« Traitement des lectures neuves ») ; rapports versés sous
  `docs/notes/runs-r1-r2-r4-v1/graine-v1/` (« Contre-lecture »).
- **Portée (décision de la session, n° 262 et 265 de session-depot).** Cette v2 ne porte que le **rejeu à graine** :
  étape 0, validation à l'aveugle sur les 147 épisodes résolus ; étape 1, résolution des 7 (dont les 3 de C-6 en
  contrôle croisé) ; étape « cibles du lot » (processeur) ; étape 1 bis, lot fidèle pour les cibles qui restent ;
  étape 2, table de tokenisation v3, scellée. **La relance de R1 sur la table v3 passe dans un addendum v3**
  (`prereg/R1-addendum-relance-v3.md`, nom réservé), écrit et scellé **après** la table v3, dont il citera l'empreinte
  (elle n'existe qu'après la carte). Tout ce qui ne concernait que la relance en est retiré et renvoyé à l'addendum v3
  (section « Écarts à l'addendum v1 et renvoi à l'addendum v3 »).
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
  proposé au n° 257, accepté par conv-audit au n° 352 **en premier, la passe forcée en repli** ; il est ici l'**étape 1
  bis** (« lot fidèle »), **après** la passe forcée : **écart déclaré** à l'ordre accepté au n° 352 (ligne G11 des écarts).
  Précisions de forme : n° 354, point 1 (`ef4a15d55d55910208d6f2f9bb94c35c13bbc73f09006185da5d5d5e7b78c3b1`) ; liste
  des épisodes non inversibles au versement : n° 356, point 4
  (`da210e95993035d9ca694303083be883c94688b053366b4a766763de68648c45`). Changements annoncés à conv-audit : n° 262 de
  session-depot (branche `canal/session-depot-reprise-n89`) et n° 265 (branche `canal/session-depot-reprise-n92` ; la
  validation devient une mesure lue par une règle gelée, non un arrêt).
- **GO** : `GO-2026-11-02-02`, ligne d'extension (R-389) inscrite dans `registres/go.md` de `main` au commit
  `ddfff6e4281b82fcd3b6ac9997fe47e15a62b0aa` (R-1034), sur le mot direct de Lazar dans la session de session-depot
  (≈ 08:32 UTC) : « GO-02 couvre le rejeu à graine et le complément des épisodes restants » ; plafond 25 USD inchangé ;
  échéance 2026-11-09. La garde de calcul l'accepte (essai du n° 258 ; relu au n° 262 : code 0).
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65`.
- Commit du code d'analyse : `0e2a88718f4249e556e159f45f2df38ac304331e`
  (branche `prep/r1-relance-addendum-v1` ; corrections de la vérification neuve VI — VI-01, VI-08, VI-10, VI-16 —
  posées sur le code intégré `31f72147` : intégration du cœur corrigé `ca3dfa3f`, du lot fidèle corrigé `9f898ee2` et
  de la relance sur la table v3 `06887bdd`, posée sur les fusions `1f32520d` et `f21c2641` ; corrections de la
  vérification adverse VG-01 à VG-09 au commit `755959e1`, comprises ; `resolution_tokenisation_v1.py`,
  `rejeu_activations_v1.py` et `rejeu_activations_v2.py` non modifiés)
- Empreintes des fichiers de code au commit cité (sha256 du fichier ; compagnon `.sha256` conforme sauf mention) :
  - `src/controle_ia/runs_nuit/resolution_graine_v1.py` : `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663`
  - `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py` : `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156`
  - `src/controle_ia/runs_nuit/rejeu_activations_v3.py` (inchangé depuis `06887bdd`, sans compagnon ; hors de ce texte,
    cité parce que ses essais sont lancés par le script) : `0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc`
  - `tests/test_resolution_graine_v1.py` : `c4c411fb25ce77d0622f485328e0298d07e34f284fe686d59b94c1bfa5e63e14`
  - `tests/test_resolution_graine_lot_v1.py` : `add9d6defb3e28267028b584907e2e5d612bc6e0e104cd483f6c142ae99463bd`
  - `tests/test_rejeu_activations_v3.py` : `ef7be3f70e1a601aae404570f96f373448de98e8007519d17448d07120a352f8`
  - `scripts/r1_resolution_graine_instance_v1.sh` : `da07025f5cae92cc0041a234a1a3951f33cd42e86da808befbaaedd7d5351cc8`
  - `scripts/amorce_instance_r1_resolution_graine_v1.sh` : `dc8164e2cc44b9d05925dfb4a880f898b3f5dc0466ed1acec52e0291cd516478`
  - `scripts/preparer_repetition_r1_resolution_graine_v1.py` (répétition jouet seulement) :
    `6405b886e9fa419a9f89ca506671cfbbc36a665a1f77f8ad5cd02e5694fb0490`
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-v1.json`
  (42 clés ; fichier au commit cité `0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f`, **non scellé au
  commit du code, scellé avec ce texte** ; un seul fichier pour le cœur et le lot fidèle, donc une seule empreinte
  canonique, citée sous les deux libellés que lisent les deux modules et le script)
- Configuration de la résolution à graine (empreinte canonique) : `f91716bf95c4c4ab07e4155c667539cee9baff38b7ca2639dff0dea167d44db2`
- Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `f91716bf95c4c4ab07e4155c667539cee9baff38b7ca2639dff0dea167d44db2`
  (empreinte par `resolution_graine_v1.empreinte_config` : sha256 du JSON canonique, clés triées ; recalculée ici sur
  le fichier du commit cité)
- Entropie : `36410133060804533274328900142752730279` (celle du parent : le rejeu à graine ne tire rien ; son manifeste
  porte `aucun-tirage-propre`, les graines viennent du manifeste de P3)
- Tests attendus : `71`
  (sept fichiers que lance le script d'instance, liste `CIBLES` : `tests/test_resolution_graine_v1.py`,
  `tests/test_resolution_graine_lot_v1.py`, `tests/test_rejeu_activations_v3.py`, `tests/test_manifeste.py`,
  `tests/test_scellement.py`, `tests/test_prereg.py`, `tests/test_harnais_formats.py` ; 71 passés, aucun sauté, au
  commit cité, avec le tokeniseur de Llama 3.1 à la révision de P3 ; un test sauté ou en échec arrête le script, qui
  exige ce nombre exactement)
- Documents qui font foi (chemin + empreinte) : le parent ci-dessus ; l'addendum v1, brouillon 4, pour les faits de
  P3 qu'il établit (`prereg/R1-addendum-relance-v1.md`, commit `72f68fea`) ; table de tokenisation v2
  `prereg/R1-table-tokenisation-v2.json` (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`, commit
  `cdca33bb` ; son compagnon `.sha256` est committé au commit `82a5ed18`, après le code et avant le scellement de ce
  texte ; le script s'arrête avant l'installation sans lui) ; manifeste de P3
  `runs/20261019-230011-p3-reel/manifeste.json` (`3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685`) ;
  rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; résultat de C-6
  `docs/notes/runs-r1-r2-r4-v1/resultat-c6-v1.json` (`1e11d58fa75be359ffb185136cd2c83b1275203eb9f0162f0a5413222767b238` ;
  compagnon `.sha256` committé au commit `82a5ed18`, avec ceux du script `resolution_c6_v1.py` et des journaux
  `journal-c6-v1.out` et `journal-c6-v1.err`, VI-13) ;
  messages cités dans l'en-tête ; GO ci-dessus.
- Mesures et journaux sur processeur cités par ce texte (comptes seulement ; aucun texte, score, étiquette ni
  activation de P3 ; versés sous `docs/notes/runs-r1-r2-r4-v1/graine-v1/` avec leurs compagnons `.sha256`, commit `82a5ed18` ; noms relatifs à ce dossier,
  sha256 du fichier) :
  - pré-vol d'intégration sur les vraies pièces de P3, au code cité : script `prevol_integ.py` (`bd9a4eccd03c1514db6f78bccb45901d0d92857078d0ee3cf95662c7c7cf7842`) ; sortie
    `prevol-final-sortie.txt` (`9d9c1c871a3bf5583f5197d7806b9bce33c811c5f77fd62c12f5107d76189147`) ;
  - compte des U+FFFD des 7 : script `compter_fffd_7.py` (`a2e2331181b82387f81bdfd345602b5358af006c155a616eb8975ed175d71714`) ; sortie `compter_fffd_7-sortie.txt` (`b75658fec93d3addc6051650297c2795dccc7e398c713baaacac0127583b0e3b`) ;
  - forme des 4 lots ciblés et unité des balayages, sans modèle (vérificateur VI) : script `comptes_reels.py` (`1a2e980382c325b456784dc1b4f77f5b32d6aa08a5baa57d21618f41cf31a77a`) ;
    sortie `comptes_reels-sortie.txt` (`a2bd318f97ea9ee4f046e22380f99006ed27a0b31f69d135545402ceb11efc95`) ;
  - essais de la liste `CIBLES` au code cité : sortie `tests-cibles-final.txt` (`d7309e17e3352f7ce391e2142a8b09f046b5d60af15206fd438fdada8e221b8e`) ; essais neufs lancés sur le code de
    `31f72147` (échouent sans les corrections VI-01 et VI-08) : sortie `essais-sans-correction.txt` (`8544a7cdf4839eb2d24aa52b5cec5ef7826cc09d32389df6db247cca77096899`) ;
  - répétition jouet finale du script d'instance, au code cité (répertoire courant sans `donnees/`, VI-16) : script
    `repetition.sh` (`2b922710d26f0404893be79b176cc2a819d8197828fc6ed8a6f133e66f54879d`) ; inspection de la branche de résultats `inspecter_repetition.py` (`339e9647e493573aa93e4baa732d2d5df168beffd2f85a9ce129797526fd916a`) ; cas principal
    (une cible au lot) : préparation `repetition-principale-preparation.txt` (`a9bad32c646e62c43b9c752b1a806557259072c9a48e27eb556f0b55b7b3e2e5`), sortie de l'amorce
    `repetition-principale-amorce.txt` (`a9152b4f91da927c0d309378fc6d482754407a5eb53eab32c6b6e1261912ca13`), journal de l'instance `repetition-principale-journal.txt` (`121556be7c09da6b4e19753fd26529f7f0079423cb9c134cb383a7d53cee364f`),
    inspection `repetition-principale-inspection.txt` (`f5887a03d444037fec75067eb0cf4346c2cb7080c0fe79c6e5abf3f9026a89ee`) ; cas « sans objet » : préparation
    `repetition-sans-objet-preparation.txt` (`8d2fa931784bb4e143e18e1e47a9c4c84c62a54b3b19cc252032e87d3e561050`), sortie de l'amorce `repetition-sans-objet-amorce.txt` (`e29b7a3de129bf1a2c2263d7b9dff2f1e6d01f3952ce9ef233741f31075bad75`), journal
    de l'instance `repetition-sans-objet-journal.txt` (`4a9a5f81a95106c839ed6c0de30f335127e38e759b410ab38b1f182ab97074bf`), inspection `repetition-sans-objet-inspection.txt` (`6c9a5b440c4ea388fb7504f634f2d67be1276596fa6bfd0a881c83fcb5f629d5`).

**Statut.** Cet addendum résout, avant la relance de R1, les **7 épisodes** que les étapes 1 à 3 de la règle A n'ont pas
résolus (dont les 4 que C-6 laisse non résolus), par **rejeu à graine** : passe forcée d'abord, lot fidèle ensuite pour
les cibles qui restent. Un épisode n'est « résolu » que par l'**égalité de son empreinte de trajectoire avec celle de
P3** (sha256, 256 bits), quelle que soit la voie qui l'a trouvé. La **validation à l'aveugle sur les 147 épisodes déjà
résolus est une mesure lue par une règle gelée, jamais un arrêt** : la résolution part quelle que soit sa classe, et la
classe décide seulement si un non résolu peut être déclaré non inversible. Le texte gèle la méthode, ses bornes, ses
mesures, leur lecture et la construction de la table v3. Il porte sur R1 seule ; R2 ne se relance pas ; le rejeu de R4
n'est pas relancé (comme la v1). Il ne lit aucun score.

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
  décodés en caractère de remplacement U+FFFD (hypothèse 4 de l'enquête). Le décodage n'est donc pas injectif ; le texte
  stocké est l'image exacte des identifiants par cette application. Sur les 147 résolus, l'invariant tient par preuve
  (empreinte retrouvée au bit près), non par hypothèse.
- (b) **empreinte de trajectoire** : **par épisode seulement**, sha256 de `json.dumps(asdict(Episode), sort_keys=True,
  ensure_ascii=False)` (identifiant, N, T, transcription complète en identifiants : ouverture, observations, actions,
  clôtures ; par action : pas, empan, identifiants générés, texte). Aucune empreinte intermédiaire par action : la
  vérification est finale, par épisode (oracle de 256 bits).
- (c) **contexte de chaque action** : les jetons tirés, non le texte retokenisé (`trs.ids = ctx + nv + fmt.cloture(…)`,
  puis `ctx = trs.ids + fmt.tour(debut, obs)`) ; observations de l'environnement tokenisées par le gabarit. N = 1, T = 10.
- (d) **échantillonnage** : température 1,0 ; **ni top_p ni top_k** (tout le vocabulaire) ; `max_nouveaux` = 400 ;
  génération par lots de 8 (plan `plan_p3`, lots consécutifs : 30 lots, 240 épisodes), remplis à gauche, avec cache
  (préremplissage, puis une passe par jeton, `logits_to_keep=1`, positions explicites), modèle en bfloat16 sur
  A100-SXM4-80GB ; torch `2.14.1+cu130`, pilote 580.159.03, cuDNN 92400 (lus dans `episodes-p3.json`, VG-05 ; le code
  les recopie dans `ENVIRONNEMENT_P3`, sauf le pilote) ; à chaque pas, logits du dernier jeton ramenés **sur processeur
  en float32** (`.to("cpu", torch.float32)`), puis `torch.multinomial(torch.softmax(logits / T, -1), 1, generator=g)` ;
  **un générateur par action**, `torch.Generator('cpu').manual_seed(graine)`, avancé d'un tirage par jeton tant que la
  ligne est active ; graine de l'action tirée par `graines_des_actions(generateur(graine de la tâche), 1, T)`, clé
  `tache/<identifiant>` du manifeste de P3 (le `g.random(T)` qui suit dans `jouer_p3` ne change pas ces graines) ;
  mêmes graines d'une condition à l'autre (pré-vol sur les vraies pièces de P3 : 240 épisodes, 10 graines distinctes par
  épisode, 60 tâches à graines identiques entre conditions ; sortie du pré-vol citée à l'en-tête).
- (e) **identité du tirage** : sur torch 2.14.1, `torch.multinomial(p, 1, generator=g)` est exactement
  `argmax(p / q)`, `q` vecteur de V tirages exponentiels pris au même générateur ; un appel unique de n × V tirages
  égale n appels de V. Vérifié sur processeur, en float32 (200 graines, 200 égalités, n° 256 ; essais du module ; pré-vol :
  12 égalités sur 12, V = 128 256) et **revérifié au lancement** sur la bibliothèque installée
  (`exiger_equivalence_tirage`, arrêt sinon).

## Écarts à l'addendum v1 et renvoi à l'addendum v3

« v1 » = `prereg/R1-addendum-relance-v1.md`, brouillon 4. La numérotation du brouillon 1 est gardée pour la concordance
de conv-audit ; les lignes retirées sont renvoyées à l'addendum v3, sans être tranchées ici.

| n° | Ligne ou règle de la v1 (ou acceptation de conv-audit) | Règle de cette v2 | Raison |
|---|---|---|---|
| G1 | Étape 0 de la v1 : table v2 (règle A, étapes 1 à 3, puis C-6) ; 4 non résolus traités par la règle B | **Étapes 0, 1, cibles du lot, 1 bis et 2 ajoutées** (rejeu à graine) : validation à l'aveugle sur les 147 résolus, lue par une règle gelée à trois classes ; résolution des 7 ; lot fidèle pour les cibles qui restent ; table v3 = table v2 dont chaque épisode « non résolu » que le rejeu résout reçoit une entrée de forme « identifiants » ; les 18 corrections de la v2 restent telles quelles | Demande de Lazar (n° 348) ; méthode du n° 256 acceptée (n° 351) ; lot du n° 257 accepté (n° 352) |
| G2 | E2 (règle B pour 7 − r épisodes) | Règle B réservée au seul épisode **déclaré non inversible par la méthode** (cause « caractère de remplacement : budget de balayages dépassé », sous la classe « graines validées » et, pour une cible du lot, sous la lecture du lot « fidèle ») ; tout autre non résolu est un **nœud porté à Lazar** avant l'addendum v3 (complément sous texte neuf, ou règle B par sa décision, épisode nommé) ; liste des deux sortes remise à Lazar avant l'addendum v3 et avant toute lecture (n° 356, point 4) ; seuil de 10 inchangé (E3), lu dans l'addendum v3 | « Résoudre tous les épisodes » ; la règle « non conforme » ne reste que pour le cas déclaré (R-06) |
| G8 | E9 et « Coût et GO » : relance seule | **Passage sur carte ajouté**, avant la relance, sous la même ligne GO-2026-11-02-02 (extension R-1034) ; devis à la section « Plan d'analyse » | Dépense nouvelle couverte par le mot de Lazar (n° 258) |
| G11 | n° 352 de conv-audit : lot exact **en premier**, passe forcée en repli | **Passe forcée et repli d'abord (étapes 0 et 1), lot fidèle ensuite (étape 1 bis), seulement pour les cibles qui restent** : **écart déclaré** | La passe forcée coûte moins d'une minute de carte par épisode (estimation de l'auteur, non mesurée sur le 8B) et doit résoudre la plupart des 7 ; elle seule permet la validation à l'aveugle sur les 147 (le lot rejouerait 30 lots) ; le lot, 3 à 5 minutes par essai direct (estimation), ne sert qu'aux restes ; l'arbitre (empreinte de P3) est le même (m-6, R-18, R2-11) |

**Renvoyé à l'addendum v3** (retiré de ce texte) : G3 (ligne E19 et décision N-A, « couverte, pour les épisodes
nommés »), G4 et G5 (prédiction P-R5 et comptes à r′), G6 (configuration du rejeu v5, module `rejeu_activations_v3`,
code « R2 seul » de conv-audit), G7 (tests de la relance), G9 (contre-contrôle négatif étendu), G10 (traitement de
C-1) ; prédiction P-R5 ; étape 3 du brouillon 1 (préalables, complément court) ; ligne « Relance » des critères de
lecture. L'addendum v3 citera l'empreinte de la table v3 (`prereg/R1-table-tokenisation-v3.json`) et celle du résultat
scellé de ce rejeu ; la configuration de la relance v3 citera la même table ; sa concordance par conv-audit portera sur
sa différence avec le brouillon 3 de la v1 (n° 354, point 1), et ses **attentes de réception** devront être réécrites :
la concordance anticipée attend `tokenisation.table_sha256` = `5f6cf489…` et `episodes_non_resolus` = exactement les 4 ;
la table v3 change les deux (m-8).

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
- **HG-3 (inversibilité)** : le décodage n'est pas injectif (U+FFFD, jetons spéciaux effacés), mais le jeton de P3 reste
  dans l'ensemble contraint (les jetons compatibles avec les octets restants du texte stocké) à chaque pas : sous HG-1 et
  HG-2, la méthode le retrouve. Près d'un U+FFFD, la recherche des octets inconnus est bornée (`balayages_max`, unité
  écrite en « Seuil ») ; au-delà de la borne, l'épisode est déclaré non résolu par **budget de recherche dépassé**, ce
  qui n'est pas une preuve d'impossibilité.
- **HG-4 (lot fidèle)** : refaite dans son lot (même plan, même remplissage, même cache, même ordre d'appels, mêmes
  conversions, même carte et même bibliothèque), la génération de P3 redonne ses logits au bit près pour la ligne cible
  et pour les lignes voisines dont les jetons sont exacts. Les lignes voisines **approchées** ont le nombre exact de
  jetons générés par action, et la fin par défaut à la dernière place quand P3 a compté une fin (`LigneLot.forcee`) ;
  leur contexte ne diffère de celui de P3 que si la vraie fin de P3 n'était pas la fin par défaut (un jeton de plus chez
  P3 pour telle action, non connu pour une ligne approchée). Les logits de la cible ne dépendent des autres lignes que
  par la **forme** du lot (taille et longueur remplie) ; le nombre de pas où la longueur remplie est fixée par une ligne
  approchée est mesuré et rapporté, ainsi que celui où une ligne approchée est à un jeton ou moins de la fixer.
  **Preuve de la forme (VI-03)** : la longueur d'une ligne approchée peut différer de celle de P3 de d jetons,
  d = nombre de ses actions antérieures dont la fin chez P3 n'était pas la fin par défaut (non connu), borné par
  d_max = nombre de ses actions antérieures à jeton de fin compté ; la forme du lot est **prouvée exacte** pour la cible
  si, à chaque action jouée, aucune ligne approchée n'est à d_max jetons ou moins de fixer la longueur remplie ; sinon
  elle est « non prouvée » (descriptif, jamais un arrêt ni une condition de lecture). Le champ `forme_exacte_prouvee` du
  code (premier compte nul) dit seulement « forme exacte si les fins de P3 des lignes approchées sont les fins par
  défaut » ; il est lu ainsi. La preuve par d_max est calculée sans modèle sur les vraies pièces (P-G4). Éprouvé sur processeur, en float32 (égalité au bit des empreintes des logits avec
  `jouer_episodes`, lots de 8 et de 4 ; ligne approchée la plus longue du lot : mêmes bits après correction) ; jamais
  garanti au bit entre deux exécutions sur carte, d'où la mesure des lignes voisines.

Sous HG-1 à HG-4, la reconstruction d'un épisode est l'unique suite d'identifiants qui redonne l'empreinte de P3 ;
l'empreinte en est la preuve (256 bits), quelle que soit la voie qui l'a trouvée. Une graine fausse peut résoudre, à
juste titre, un épisode où les octets du texte imposent chaque choix ; elle ne peut **pas produire un faux « résolu »**
(il faudrait une collision de sha256) : c'est pourquoi les graines se jugent sur l'accord du choix non contraint, non sur
les empreintes seules.

## Prédiction chiffrée et signe attendu

- **P-G1 (validation, étape 0, mesure)** : **147 empreintes de P3 retrouvées sur 147** (129 identiques de base et 18
  corrigés par la table v2), à l'aveugle, confiance ≈ 0,8 ; au moins 140 par la voie directe (sans repli) ; accord du
  choix non contraint avec le jeton retenu **au moins 0,99 en moyenne par épisode** sur les 147 et au moins 0,95 dans
  chaque épisode, confiance ≈ 0,7 ; **au moins 1 000 pas informatifs** (jeton retenu différent de l'argmax de p),
  confiance ≈ 0,9, et accord sur eux **au moins 0,95**, confiance ≈ 0,6. Sous une graine indépendante, l'accord attendu à
  chaque pas est la probabilité p_k du jeton retenu sous la passe (en espérance Σ p²) : cette valeur est calculée sur les
  mêmes passes et rapportée (`attendu_graine_independante`, et sur les pas informatifs `attendu_informatif`, au plus
  ≈ 0,5) ; l'écart entre l'accord observé et cet accord attendu est le signal des graines. Ces valeurs sont des
  prédictions, non des seuils d'arrêt (R3 : rien n'est relancé pour les atteindre). Réfutation de P-G1 : moins de 147
  retrouvées (classe « méthode non transposée », réserve ; la résolution part) ; une condition d'accord de « Seuil »
  manquée (classe « méthode transposée, graines non validées », réserve ; aucun non résolu déclaré non inversible).
- **P-G2 (résolution, étapes 1 et 1 bis)** : **au moins 6 des 7** épisodes résolus (empreinte de P3 retrouvée) à la fin
  de l'étape 1 bis, confiance ≈ 0,8 ; **7 sur 7**, confiance ≈ 0,6 ; par la passe forcée seule (étape 1), au moins 5 des
  7, confiance ≈ 0,6. Les 3 de C-6 résolus avec les identifiants de la table v2 (contrôle croisé « conforme »),
  confiance ≈ 0,95 (ils font déjà partie des 147 de l'étape 0 : c'est une répétabilité). L'épisode le plus exposé :
  `mention/2605.17899v2/e0`, **le seul des 7 qui contient un U+FFFD (un ; aucun dans les 147)** (compte cité à
  l'en-tête) ; s'il reste non résolu, sa cause attendue est « caractère de remplacement : budget de balayages dépassé ».
  Les découpages qui changent le nombre de jetons d'un mot en compensant ailleurs, non explorés par C-6, sont couverts
  par construction (le choix est pas à pas, seule la longueur totale de l'action est contrainte).
- **P-G3 (fragilité numérique de la passe forcée, descriptif)** : sur les 147, écart contraint (premier contre second
  candidat compatible) sous 1 nat dans moins de 1 % des pas à plusieurs candidats ; désaccords du choix non contraint
  concentrés sur des marges sous 0,5 nat. Aucune mesure du 8B n'existe avant la carte ; les chiffres du modèle minuscule
  que citaient les brouillons 1 et 2 sont **retirés** (ni chemin ni empreinte, et les essais du code tournent en
  float32, non en bfloat16).
- **P-G4 (lot fidèle, étape 1 bis, mesure)** : sur les lignes voisines exactes des lots ciblés (au plus 21 lignes :
  8 lignes par lot, moins la cible et les lignes approchées ; sur les vraies pièces, 5, 6, 6 et 4 lignes exactes aux
  lots 0, 5, 14 et 24), accord du choix non contraint avec le jeton connu **au moins 0,999** sur les pas mesurés,
  confiance ≈ 0,7 (fidèle au bit, il vaut 1 exactement) ; lecture du lot « fidèle », confiance ≈ 0,7 ; chaque cible du
  lot, si elle est inversible, résolue par l'essai direct, confiance ≈ 0,6. Les pas où la longueur remplie est fixée par
  une ligne approchée sont rapportés, sans prédiction chiffrée (descriptif). **Forme, calculée sans modèle sur les
  vraies pièces** (`comptes_reels-sortie.txt`, en-tête ; 10 actions par cible ; « strict » = une approchée fixe seule
  la longueur remplie ; « à un jeton » = règle du code ; « à d_max » = preuve de HG-4) : lot 0
  (`honnete/2602.00987v1/e0`, 2 approchées) : strict 0, à un jeton 1 (une égalité), à d_max 0 → **forme prouvée
  exacte** ; lot 5 (`mention/2605.17899v2/e0`, 1 approchée) : strict 3, à un jeton 3 (aucune égalité), à d_max 4 →
  **forme non prouvée** (attendu « non prouvé ») ; lot 14 (`saboteur/2510.05132v3/e0`, 1 approchée) : 0, 0, 0 →
  **prouvée exacte** ; lot 24 (`temoin/2512.06870v2/e0`, 3 approchées) : strict 0, à un jeton 1 (une égalité), à
  d_max 0 → **prouvée exacte**. Pour le lot 5, seule la mesure des voisines exactes (lecture du lot de cette cible) dit
  si les logits sont ceux de P3 : une longueur remplie fausse peut changer aussi les leurs.

## Métrique

Chaque épisode est **consigné dès qu'il est terminé** (VG-01) dans un fichier scellé
(`diag/<run>/episodes-<étape>/NNN.json` : statut, voie, cause, identifiants retrouvés, empreinte), cité par
`arret.json` en cas d'arrêt (signal, erreur de chaîne) ; un arrêt ou une coupure ne perd que l'épisode en cours. Résultat
scellé par étape (`diag/<run>/resolution-graine-<étape>.json`, pas par pas dans
`diag/<run>/pas-resolution-graine-<étape>.npz`) :
- **empreintes retrouvées** : nombre d'épisodes dont l'épisode reconstruit redonne exactement l'empreinte de trajectoire
  de P3 (`empreintes_retrouvees`), dont par voie directe (`directes`), par repli (`par_repli`, et par nombre de
  bascules) et, à l'étape 1 bis, par le lot fidèle ; c'est la **seule métrique qui fait un « résolu »** ;
- **épisodes non résolus et non tentés**, chacun avec sa cause écrite par le code : « empreinte de P3 non retrouvée à
  l'essai direct ; repli itératif : … » ; « contradiction à l'essai direct (…) » ; « caractère de remplacement : budget
  de balayages dépassé (…) » ; « durée : … » (budget de l'épisode épuisé) ; « durée : budget de l'étape (… s) épuisé
  avant l'épisode k » (non tenté) ;
- **déclaration** de chaque épisode de la résolution (`declarations`, fonction `declarer`, règle de « Critères ») ;
- **identifiants égaux** (comparaison aux identifiants connus, après la résolution de tous les épisodes de l'étape
  seulement) : épisodes et actions ;
- **accord du choix non contraint** (`mesures_accord`, pour **tout** épisode, résolu ou non, contre le **jeton retenu**,
  qui est le jeton de P3 quand l'épisode est résolu) : part des pas où l'argmax de p / q sur tout le vocabulaire
  (l'opération de P3) égale le jeton retenu (`accord`) ; **accord attendu sous une graine indépendante**
  (`attendu_graine_independante`, moyenne des p_k) ; **pas informatifs** (jeton retenu ≠ argmax de p) : nombre,
  accord et accord attendu sur eux ; agrégats (`agreger_accords`) : accord moyen et minimum par épisode, accord sur les
  pas réunis, pas informatifs réunis et leur accord ; en outre `accord_non_contraint` par épisode, contre les
  identifiants connus quand il y en a ;
- **classe de la validation** (`lecture_validation`, fonction `lire_validation`), écrite au résultat de la validation
  avant toute lecture humaine, **recopiée** dans le résultat de la résolution, dans celui du lot (`classe_validation`)
  et dans la table v3 ;
- **écart contraint** : par pas à plusieurs candidats compatibles, écart en log entre le premier et le second candidat ;
  **distribution** (quantiles et comptes sous 0,01, 0,05, 0,1, 0,25, 0,5, 1 et 2) ; **marges en désaccord** ;
- **repli** : combinaisons essayées par épisode, bascules retenues ; **premier écart de la voie directe** quand elle
  échoue (`erreurs_directes`) ;
- **contrôle croisé** des 3 épisodes de C-6 (`controle_croise`, `controle_croise_lecture`, fonction
  `lecture_controle_croise`) : « conforme », « non résolu », « contraire » (« sans objet » sans épisode de contrôle) ;
- **U+FFFD** : déclarés par épisode (`fffd_declares`) ; **pas de recherche sur octets inconnus** comptés par épisode
  (`balayages`, unité de « Seuil »), plafond de l'essai, balayages complets du vocabulaire (descriptif) ;
- **lot fidèle** : par cible, numéro du lot, rang, lignes voisines exactes et approchées (comptées et nommées) ;
  `hors_cibles` (non résolus du cœur qui ne sont pas des cibles, avec la raison) ; **mesure des lignes voisines
  exactes** (`mesure_voisines` : accord, accord attendu sous graine indépendante, pas informatifs, égalité des choix
  contraints, jetons connus hors des candidats, actions à U+FFFD non mesurées) ; **lecture du lot** (`lecture_lot` :
  « fidèle », « réserve lot non fidèle », « sans mesure ») ; **forme** (`pas_L_fixee_par_approchee`,
  `pas_L_a_un_jeton_d_une_approchee`, `forme_exacte_prouvee`) ; accord de la cible (`accord_cible`) ;
- carte, versions (torch, `torch.version.cuda`, cuDNN), réserves d'environnement (`reserves`), passes, jetons en
  passe, durées ; pilote : au journal et aux traces de l'instance (`nvidia-smi.txt`), non comparé.
Comptes exacts, sans tirage propre : aucun intervalle n'est calculé (la méthode est déterministe aux arrondis près ;
ces arrondis sont ce que mesurent l'écart contraint et l'accord). Aucune moyenne sur les jetons n'entre dans une sonde.

## Seuil

Il n'y a **aucun seuil d'arrêt sur une mesure** : les seules bornes du code sont des bornes de travail (repli, durée,
balayages) ; leur dépassement donne un « non résolu » ou un « non tenté » avec sa cause, jamais un arrêt.

**Configuration** `prereg/R1-graine-config-v1.json` (fichier unique pour les deux modules, 42 clés, exactement celles
que lisent le cœur et le lot ; empreinte canonique à l'en-tête ; scellée avec ce texte). Clés et valeurs gelées :
- **repli de la passe forcée** : `seuil_ecart` = **1,0** (écart contraint en log sous lequel un pas est une
  quasi-égalité) ; `quasi_egalites_max` = **16** par essai (les plus fragiles d'abord) ; `bascules_max` = **2** ;
  `combinaisons_max` = **136** rejeux au plus par épisode, `combinaisons_max_validation` = **136** (égal à
  `combinaisons_max`, exigé par le code : paires permises en validation, VG-03, R-17) ;
- **lot fidèle** : `combinaisons_max_lot` = **136** (même repli itératif que le cœur ; les brouillons disaient 16) ;
  `episodes_resolution_lot` = **liste vide**, qui veut dire « toutes les cibles » (définies en « Plan d'analyse ») ;
  `seuil_lecture_lot` = **0,99** ; taille et plan des lots : ceux de P3 (`plan_p3`, taille lue dans le manifeste de P3),
  reconstruits, non configurables ; les clés `episodes_validation_lot` et `seuil_validation_lot` et l'étape
  `validation-lot` n'existent plus ;
- **U+FFFD** : `balayages_max` = **16 par U+FFFD de l'épisode**. **Unité** : un pas où la recherche de candidats couvre
  des octets inconnus, c'est-à-dire où les octets connus s'arrêtent sur un U+FFFD à portée et où l'ensemble des jetons
  qui les prolongent au-delà (`commencant_par(E)`) est non vide ; un pas simplement proche d'un U+FFFD n'est pas compté.
  Plafond de l'essai = `balayages_max` × nombre de U+FFFD de l'épisode (pour `mention/2605.17899v2/e0` : 16) ; au-delà,
  cause « caractère de remplacement : budget de balayages dépassé » (B-2, C-2, R-08, R2-03) ;
- **budgets de durée** (VG-01) : `duree_max_episode_s` = **600** (passe forcée, par épisode) ; `duree_max_s` = **2 400**
  par étape (validation ; résolution) ; `duree_max_episode_lot_s` = **900** ; `duree_max_lot_s` = **3 600** ;
- **validation** : `seuil_validation` = **147**, compte exact des épisodes de validation exigé avant la boucle
  (`exiger_compte_validation`, m-3), **non une condition de lecture** ; le résultat porte aussi une clé `lecture`
  (« atteint » / « sous le seuil ») qui n'est qu'un compte, sans conséquence ; **`regle_validation`** =
  { `accord_moyen_min` : **0,95** ; `accord_episode_min` : **0,90** ; `accord_informatif_min` : **0,90** ;
  `pas_informatifs_min` : **1 000** } (règle gelée ci-dessous) ;
- **échantillonnage** : `T` = 10, `temperature` = **1,0**, `max_nouveaux` = **400** (comparés à la configuration de P3
  par le module) ;
- **exécution** : `noyau_attention` = « defaut » (le noyau de P3 ; le cœur n'accepte que « defaut » ou « math », le lot
  exige celui du manifeste de P3) ; `hors_ligne` = vrai ; `fils` = 1 ; `fils_tirages` = 8 ; `episodes_d_avance` = 2 ;
  `mode` = « reel » ;
- `episodes_resolution` = les 7, **dans cet ordre** (les 3 de C-6 d'abord, rapides, pour qu'ils existent avant tout
  dépassement de budget, m-5) : `honnete/2512.05150v2/e0`, `honnete/2512.11131v1/e0`, `temoin/2510.24788v1/e0`,
  `honnete/2602.00987v1/e0`, `mention/2605.17899v2/e0`, `saboteur/2510.05132v3/e0`, `temoin/2512.06870v2/e0` ;
- **pièces** : `agent` (`meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`,
  `variables_gabarit.date_string` « 26 Jul 2024 », `texte_attendu_ouverture` « Today Date: 26 Jul 2024 ») ;
  `run_source` = `20261019-230011-p3-reel` ; textes `ba05fa13…`, scores (identité seule) `968414fc…`, identité
  `1f25adbd…`, fiches `1a96cbf8…`, tâches `287e8348…`, consignes `a68468fe…`, manifeste de P3 `3f21774c…`, table v2
  `5f6cf489…` (chemins et empreintes complètes dans le fichier) ;
- **clé interdite en mode réel** : `repetition_non_tentes` (répétition jouet du script seulement : épisodes que l'étape
  « resolution » laisse non tentés pour que l'étape du lot tourne) ; présente en mode réel, même vide : arrêt
  (`episodes_laisses_par_repetition`). Elle est absente du fichier réel.

**Règle de lecture gelée de la validation** (mesure, non garde ; n° 265 ; fonction `lire_validation`, identique au code
au commit cité ; écrite au résultat de la validation avant toute lecture humaine). Soit R le nombre d'empreintes de P3
retrouvées et E le nombre d'épisodes de la validation (147) :
1. **« méthode non transposée »** si E = 0 ou R < E (une empreinte au moins non retrouvée, quelle qu'en soit la cause,
   un épisode « non tenté : durée » compris) ;
2. sinon **« graines validées »** si les quatre conditions tiennent : accord moyen par épisode ≥ 0,95
   (`accord_moyen_par_episode`) ; accord minimum par épisode ≥ 0,90 (`accord_min_par_episode`) ; nombre de pas
   informatifs, réunis sur les épisodes, ≥ 1 000 (`pas_informatifs`) ; accord sur ces pas ≥ 0,90 (`accord_informatif`) ;
   une mesure absente compte comme une condition manquée ;
3. sinon **« méthode transposée, graines non validées »**.
Les accords sont ceux de `mesures_accord`, contre le jeton retenu (sous la classe 2, R = E : c'est le jeton de P3).
L'accord attendu sous graine indépendante (`attendu_graine_independante_moyen_par_episode`, `attendu_informatif`) est
écrit à côté ; il n'entre pas dans la classe ; il entre dans l'audit (« Critères »).
**Conséquences** (fonction `declarer`, par épisode de la résolution) : la résolution part sous les trois classes ; un
épisode résolu est une preuve sous les trois (« résolu (empreinte de P3 retrouvée) ») ; sous « graines validées »
seulement, un non résolu de cause « caractère de remplacement : budget de balayages dépassé » est **déclaré non
inversible par la méthode** (budget de recherche dépassé, non preuve d'impossibilité ; règle B pour lui) ; sous
« graines validées », tout autre non résolu est « non résolu par la méthode : nœud porté à Lazar » ; sous les deux
autres classes, tout non résolu, même de cause « budget de balayages dépassé », est « non résolu, graines non
validées : nœud porté à Lazar » (le budget de recherche dépassé y reste une cause, jamais une déclaration de non
inversibilité). La règle est éprouvée (R5) sur des mesures fabriquées par `test_lire_validation_trois_classes_et_declarations`
(cas sain « graines validées » ; conditions d'accord manquées ou absentes → « méthode transposée, graines non
validées » ; R < E ou E = 0 → « méthode non transposée ») et de bout en bout sur le P3 jouet par
`test_bout_en_bout_jouet_validation_resolution_table` (cas sain « graines validées » ; artefact des graines décalées →
« méthode non transposée ») ; la classe « méthode transposée, graines non validées » n'est éprouvée que sur des mesures
fabriquées (VI-12).

**Seuil de lecture du lot** : `seuil_lecture_lot` = 0,99 appliqué par `lecture_du_lot` (voir « Critères »). Seuil de la
règle B de la v1 (10 épisodes, E3) : inchangé, lu dans l'addendum v3.

**R3 — une seule exécution par étape.** Chaque étape sur carte (validation, résolution, lot) n'est exécutée qu'**une
fois** sous ce texte ; tout essai de plus (réglages changés, autre plan de lot, autre code, lot exact) relève d'un texte
neuf, scellé et contre-lu. Gardes du code : le cœur (`exiger_execution_unique`) refuse une étape déjà exécutée **qui a laissé une
sortie** (résultat de l'étape, `arret.json` ou épisodes consignés) sous la même commande, la même configuration **et** le
même code (arbre gelé), et s'arrête sur un manifeste illisible de `runs/` (VI-08, R5 : jamais sauté en silence) ; le lot (`exiger_execution_unique` du lot) refuse
une exécution de même commande et de même configuration, **sans comparer le code** (déclaré : une reprise du lot sous un
autre code et la même configuration n'est pas arrêtée par le code, elle reste interdite par ce texte) ; l'étape table
refuse une sortie existante (R12) ; l'étape « cibles du lot » ne fait aucun run (lecture d'une liste, sans manifeste).

**Déclaré** : les valeurs de `seuil_ecart`, `quasi_egalites_max`, `regle_validation`, `balayages_max` (16 par U+FFFD),
`seuil_lecture_lot` (0,99) et les budgets (600, 900, 2 400 et 3 600 s) sont au choix de l'auteur, fixées en connaissant
les comptes (147 résolus, 7 à résoudre, plan des lots, 309 797 pas en validation) et le comportement du modèle minuscule,
**non mesurées sur le 8B** ; aucune mesure du 8B n'a été faite.

## Plan d'analyse

**Données.** Pièces de P3 citées par la configuration, vérifiées par empreinte au chargement : textes des actions ;
de `scores-p3.npz`, **seuls** les tableaux d'identité, `jetons` et `jetons_notes`, chargés clé par clé
(`charger_identite_sans_scores`) ; fiches (empreintes de trajectoire) ; tâches ; consignes, lues seulement par
`charger_consignes`, qui en vérifie l'empreinte ; manifeste de P3 (graines, agent, taille de lot). Aucun score, aucune
note, aucune étiquette, aucune activation n'est lu. Graines (R9) : celles de P3, dérivées comme `jouer_p3` ; le rejeu ne
tire rien. Volumes (pré-vol, vraies pièces, processeur, sortie citée à l'en-tête) : 240 épisodes, 2 400 actions ;
classement 129 identiques de base, 18 corrigés par la table v2, 4 non résolus, soit **147 en validation et 7 en
résolution** ; jetons tirés : **309 797** en validation, **17 848** en résolution, **9 888** pour les 4 cibles possibles
du lot ; U+FFFD : **1** dans les 7 (`mention/2605.17899v2/e0`), **0** dans les 147.

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
   candidats, écart contraint, second candidat, marge non contrainte, pas de recherche sur octets inconnus, p_k du jeton
   retenu, argmax de p.
4. **Arbitre unique** : l'empreinte de trajectoire de P3, recalculée sur l'épisode reconstruit (`empreinte_trajectoire`
   du rejeu v1, celle du harnais).
5. **Repli itératif** (VG-02) si l'empreinte n'est pas retrouvée : les quasi-égalités de l'essai direct (écart sous
   `seuil_ecart`, au plus `quasi_egalites_max`, les plus fragiles d'abord) sont basculées vers leur second candidat, une à
   la fois, chaque rejeu repartant de l'action basculée ; chaque rejeu basculé (arrêté ou non par une contradiction : son
   journal partiel compte) apporte ses **propres** quasi-égalités situées **après** sa dernière bascule (au plus
   `quasi_egalites_max`), qui forment la frontière du niveau suivant (deux bascules, jusqu'à `bascules_max`) ; dans
   chaque niveau, les combinaisons de plus faible écart cumulé d'abord ; au plus `combinaisons_max` rejeux, chacun
   arbitré par l'empreinte ; un essai déjà fait n'est pas refait. La seconde erreur d'une paire, placée dans une autre
   action ou après un changement de longueur, n'apparaît que dans le rejeu de la première : d'où la frontière enrichie
   (le repli du brouillon 1, aveugle à ce cas, est remplacé). Éprouvé : `test_repli_bascule_une_quasi_egalite`,
   `test_repli_iteratif_deux_bascules_dans_deux_actions`.
6. **Budgets** : un épisode qui dépasse `duree_max_episode_s` finit « non résolu », cause « durée : … », consigné, et
   l'étape passe au suivant ; une fois `duree_max_s` épuisé, les épisodes restants sont consignés « non tenté » (cause
   « durée : budget de l'étape … épuisé avant l'épisode k ») ; le résultat est **toujours écrit** et scellé. Avec 7
   épisodes à 600 s au plus et 2 400 s par étape, les derniers épisodes de la liste peuvent être « non tentés » si les
   premiers épuisent leur budget : déclaré ; c'est pourquoi les 3 de C-6 passent d'abord, et un non tenté reste une
   cible possible du lot.
7. **U+FFFD** : compté par épisode ; les octets inconnus qu'il recouvre sont cherchés dans le vocabulaire, au plus
   `balayages_max` pas comptés par U+FFFD (unité de « Seuil ») ; au-delà, non résolu « caractère de remplacement :
   budget de balayages dépassé » — le seul cas que la méthode peut déclarer non inversible, et seulement sous la classe
   « graines validées » (« Seuil », « Critères »). Éprouvé : `test_unite_des_balayages_pas_sur_octets_inconnus` (dont
   trois U+FFFD), `test_caractere_de_remplacement_resolu_ou_declare`.

**Précision et ordre des opérations (n° 351, points (a) et (b) ; n° 352).** Le modèle est chargé en **bfloat16**, son
format natif, comme dans P3 (`charger_modele` refuse un point de contrôle qui ne l'est pas ; attention « sdpa » ; même
révision ; torch 2.14.1 exigé ; réglages déterministes par `regler_determinisme`, comme P3).
- **Passe forcée** : logits calculés en bfloat16 sur la carte, ramenés **sur processeur en float32**, puis
  **p = softmax(logits / T) en float32 sur processeur, ligne par ligne** (`probabilites`, l'opération de P3, garde : une
  ligne (V,) float32 sur processeur, sinon arrêt). Le **choix contraint** est calculé **en double précision à partir de
  ce p** : log p − log q sur les seuls candidats (`scores_contraints`), argmax au premier maximum (plus petit identifiant
  à égalité exacte, y compris deux p arrondis au même float32), au lieu de p / q en float32 : **déclaré**. Les deux
  ordres sont égaux en arithmétique exacte et ne peuvent différer que si deux quotients p / q sont à moins d'un arrondi
  de float32 (≈ 10⁻⁷ en relatif), très en deçà du bruit du bfloat16 ; un tel cas est une quasi-égalité, que le repli
  traite. La mesure de 2,0·10⁻⁷ nat au plus (lecteur neuf de conv-audit, rapport `dd7157e1…`, constat 1) portait sur la
  variante du brouillon 1 (à partir des logits) ; la variante retenue (à partir de p, décision n° 4 du n° 262) n'en est
  que plus proche de P3 ; elle n'est pas remesurée (déclaré). Le **choix non contraint** et la **marge** sont
  calculés par l'opération même de P3 (p / q en float32 sur processeur ; diagnostic seulement) ; l'**écart contraint**
  vient des scores en double précision du choix contraint (`scores_contraints`, log p − log q sur les candidats ;
  VI-07). Ce qui diffère de P3,
  déclaré : la passe est **pleine, sans lot ni cache ni remplissage**, au lieu du décodage pas à pas par lots de 8
  remplis à gauche ; les accumulations en bfloat16 diffèrent, donc les logits diffèrent aux arrondis près (HG-2 : raison
  d'être de l'écart contraint, du repli, de la validation et du lot fidèle). Les tirages exponentiels sont calculés sur
  processeur, en float32, au générateur de l'action, comme dans P3. Éprouvé : `test_choix_contraint_depuis_p_float32_comme_p3`.
- **Lot fidèle** : l'opération même de P3, sans écart déclaré sur le calcul : logits du dernier jeton en float32 sur
  processeur, `softmax(logits / T)` en float32, divisé par q en float32, argmax parmi les candidats compatibles (égalité :
  plus petit identifiant).
- **Carte attendue : A100-SXM4-80GB**, celle de P3, torch 2.14.1 construit pour CUDA 13.0. Une autre carte, un
  `torch.version.cuda` autre que 13.0 ou un cuDNN autre que 92400 n'arrêtent rien : **réserve écrite au résultat**
  (`reserves_environnement` : CUDA, cuDNN, carte) ; le journal du script n'en porte que CUDA et la carte (VG-05,
  VI-14). Le pilote est écrit au journal (`nvidia-smi`), non comparé (les
  brouillons disaient « réserve » : corrigé). torch différent de 2.14.1 : arrêt (liste d'arrêt).
- **Location (I-C)** : filtres d'offre, procédure de la session hors du code scellé, tous exigés : **A100-SXM4 de 80 Go**,
  une carte ; **pilote compatible CUDA 13.0** (CUDA maximal annoncé par l'hôte ≥ 13.0) ; **« centre de données »**
  (filtre gardé) ; **fiabilité annoncée ≥ 0,98** ; **débit descendant ≥ 500 Mbit/s** (16 Go de poids dans la mise en place
  de 40 min) ; **disque ≥ 80 Go** ; **prix ≤ 1,40 USD de l'heure** (ce plafond entre dans le pire cas). Valeurs de
  fiabilité, débit et disque : au choix de l'auteur. **S'il n'existe aucune offre conforme au moment du lancement, rien
  n'est loué** : c'est un **nœud porté à Lazar** (attendre une offre, ou décision de Lazar sur un filtre) ; aucun filtre
  n'est retiré en silence ni par ce texte. Le retrait du filtre « centre de données » qu'envisageait le brouillon 2 (cas
  du 2 novembre, n° 262 : trois offres à 1,07–1,22 USD/h, aucune sous le filtre) est **abandonné** : l'hôte reçoit le
  clone complet du dépôt de travail privé et deux jetons (GitHub à grain fin, en écriture sur ce seul dépôt ; Hugging
  Face, en lecture), et exposer ces accès à un hôte non vérifié relève du nœud « compte, dépôt distant », que le GO de
  dépense ne couvre pas ; seule Lazar peut le trancher.

**Étape 0 — validation à l'aveugle (carte ; mesure lue par la règle gelée).** `--etape validation` sur les 147 épisodes à
identifiants connus (129 identiques de base ; 18 corrigés par la table v2 : 1 jeton de fin, 12 une paire, 2 deux paires,
1 trois paires, 2 fenêtres). **À l'aveugle** : la table v2 et la reconstruction de base (qui est la vérité des 129) sont
calculées avant la boucle par `classer`, pour choisir les épisodes de l'étape (`episodes_de_l_etape`), et gardées en
mémoire ; aucune n'est passée aux fonctions de résolution (`resoudre_action`, `rejouer_episode`, `resoudre_avec_repli`
ne reçoivent que textes, longueurs, tirages issus des graines, empreinte de P3, format, vocabulaire, modèle et fabrique
d'environnement, celle-ci ne lisant que tâches, gabarit et consignes) ; la comparaison aux identifiants connus
(`verite`) n'a lieu qu'**après** la boucle de tous les épisodes de l'étape. L'aveugle tient par construction des appels,
vérifiable à la lecture du code cité, non par isolement de la mémoire (m-1, R-05). Compte exact de 147 exigé avant la
boucle. Repli itératif avec paires, comme en résolution. Mesures : épisodes retrouvés sur 147 (dont directs et par
repli), accords (« Métrique »), distribution des écarts contraints, marges en désaccord ; les 18 corrigés, ceux où la
graine compte (un découpage non canonique n'est retrouvé que si p / q le désigne), sont rapportés à part
(`corriges_table_v2` du résultat de la validation : épisodes, empreintes retrouvées, identifiants égaux, comptes par
méthode de la table v2 ; code `0e2a8871`, VI-10) ; classe
écrite par `lire_validation`. **Aucun arrêt sur ces mesures** ; la résolution part ensuite sous les trois classes ; seuls
les arrêts d'intégrité l'empêchent (validation non scellée, `arret.json`, autre configuration, autre code). Remarque :
sur un épisode canonique, le choix contraint est le plus souvent imposé par les octets et la probabilité, même avec une
graine fausse ; l'empreinte retrouvée ne prouve donc pas seule les graines : l'accord non contraint, surtout sur les pas
informatifs, les contrôle.

**Étape 1 — résolution des 7 (carte).** `--etape resolution --validation diag/<run>/resolution-graine-validation.json`.
Exige seulement que la validation soit scellée, rattachée à son manifeste, **sans `arret.json`**, de classe présente
parmi les trois, de **même configuration** et de **même code** (`exiger_validation`, `exiger_meme_code`), **quelle que
soit sa classe** ; la classe est recopiée dans le résultat avec la déclaration de chaque épisode. Ordre : les 3 de C-6
d'abord, puis les 4. Le **contrôle croisé** des 3 de C-6 est une **répétabilité** (ils ont été retrouvés à l'aveugle
parmi les 18 de l'étape 0, même code, même carte, réglages déterministes), lue à trois valeurs : **conforme** (empreinte
retrouvée, identifiants égaux à ceux de la table v2) ; **non résolu** (un épisode du contrôle non retrouvé :
répétabilité en défaut) ; **contraire** (empreinte retrouvée avec d'autres identifiants que la table v2 : impossible hors
collision). Repli et budgets ci-dessus.

**Étape « cibles du lot » (processeur, sans modèle ; module du lot, `--etape cibles-lot`).** Les **cibles** du lot sont
les épisodes que la résolution du cœur laisse non résolus ou non tentés (seule la liste `non_resolus` de son résultat
scellé est lue, jamais sa lecture ni ses mesures) **et** dont l'entrée de la table v2 est « non_resolu » (au plus les 4).
Un épisode de C-6 non résolu à l'étape 1 n'est **pas** une cible : son entrée de C-6 est déjà prouvée par l'empreinte ;
il est cité dans `hors_cibles` avec sa raison ; demandé nommément au lot, il est refusé (`cibles_du_lot`, éprouvé par
`test_configuration_gardes_cibles_et_unicite`). **Aucune cible** : l'étape du lot est « **sans objet** », consigné au
journal, jamais un arrêt ; la table v3 est alors construite sur le cœur seul.

**Étape 1 bis — lot fidèle (carte ; module `resolution_graine_lot_v1.py`).** `--etape resolution-lot --validation …
--resolution …`, sur les cibles seulement. Exige la validation du cœur (scellée, sans `arret.json`, même configuration du
cœur, même code, classe présente parmi les trois, recopiée sous `classe_validation`) et le résultat scellé de la
résolution du cœur (même configuration du cœur, même code). La génération de P3 est refaite par lots : plan des lots
reconstruit (`plan_p3`, lots consécutifs, taille lue dans le manifeste de P3, vérifié contre l'ordre des textes de P3 ;
pré-vol : 30 lots de 8) ; sur les vraies pièces, les 4 non résolus de la table v2 tombent dans les lots 0, 5, 14 et 24
(rangs 4, 3, 5 et 6), avec 2, 1, 1 et 3 lignes voisines approchées si le cœur ne résout rien (comptes du pré-vol, non
des gardes). Remplissage à gauche, masque, positions explicites, préremplissage puis une passe par jeton avec cache
(`logits_to_keep=1`), bfloat16, logits en float32 sur processeur, softmax divisé par q comme P3 ; ligne cible choisie
parmi les candidats compatibles avec le texte stocké ; **lignes voisines forcées à leurs jetons connus** (identiques de
base, table v2, résolus par l'étape 1 ou plus tôt par le lot, revérifiés par l'empreinte) **ou approchées** (découpage
canonique tronqué ou complété au nombre de jetons notés, **puis la fin par défaut si P3 a compté une fin** ; déclarées et
comptées ; pas où elles fixent la longueur remplie comptés, B-L1) ; les passes s'arrêtent quand la ligne cible est finie.
Arbitre : l'empreinte de P3. Repli : le repli itératif ci-dessus, borné par `combinaisons_max_lot` et
`duree_max_episode_lot_s` ; étape bornée par `duree_max_lot_s` ; U+FFFD : même unité et même plafond que le cœur.
**Mesure des lignes voisines (« validation du lot », B-L2)** : pendant les mêmes passes, sans passe de plus ni seuil
d'arrêt, chaque ligne voisine **exacte** est mesurée à chaque pas joué avec les tirages exponentiels du générateur de
**sa** propre action (une graine par action, dérivée comme pour la cible) : choix non contraint contre son jeton connu
(accord ; 1 exactement si les logits sont ceux de P3), accord attendu sous graine indépendante, pas informatifs, égalité
du choix contraint par le texte avec le jeton connu, jetons connus hors des candidats ; les actions à U+FFFD d'une ligne
voisine ne sont pas mesurées pour le choix contraint (comptées). Éprouvé : lignes exactes → accord 1 exactement ;
graine fausse sur une voisine → accord qui tombe vers l'accord attendu, lecture « réserve »
(`test_lot_fidele_force_redonne_les_logits_au_bit_et_mesure_des_voisines`). Un épisode résolu par le lot entre dans la
table v3 avec la voie « lot fidèle » ; un épisode non résolu par le lot garde la cause du lot et celle de l'étape 1.
L'étape `validation-lot` des brouillons 1 et 2 est **retirée**.

**Étape 2 — table v3 (processeur, sans dépense).** Si le lot a tourné : `--etape table-lot` du module du lot
(`construire_table_v3_lot` : part de la table du cœur, y verse les épisodes résolus par le lot, chacun revérifié par
l'empreinte de P3, refuse deux résultats différents pour un même épisode) ; si le lot est « sans objet » : `--etape
table` du cœur (`construire_et_verifier_table`). Les deux **exigent le contrôle croisé du cœur « conforme »** (R-11) et
écrivent `prereg/R1-table-tokenisation-v3.json` (variable `TABLE_V3` du script) avec le tokeniseur de la révision
`0e9e39f2…` : table v2, dont chaque épisode « non_resolu » que le rejeu a résolu (passe forcée, repli ou lot fidèle)
reçoit une entrée `identifiants` (version 3 ; actions corrigées avec leurs identifiants de base et ceux retrouvés ;
voie, bascules, empreinte du résultat) ; les 18 entrées de la v2 restent telles quelles ; **chaque correction, ancienne
ou nouvelle, est revérifiée par l'empreinte de P3** (`verifier_entrees_v3`, transcription refaite comme le harnais) ;
comptes recalculés ; la classe de la validation et la lecture du lot y sont recopiées (`lecture_validation`, **de
schéma différent selon la voie**, VI-15 : cœur seul, la lecture de la validation recopiée du résultat de la résolution,
`classe` en tête ; voie du lot, `classe_validation`, `lecture_lot`, `validation`, `lectures_lot_par_episode`) ;
`declarations` porte la **déclaration finale** de chaque épisode (VI-01) : celle du cœur (`declarer`) sur la voie du
cœur seul et pour les épisodes qui ne sont pas des cibles du lot ; pour chaque cible du lot, celle de `declarer_lot`
(règle de la ligne « k non résolus » des « Critères »), celles du cœur gardées sous `declarations_coeur` ; les
**causes** des non résolus ne sont pas dans la table : elles sont dans les résultats scellés du cœur et du lot, dont la
table cite les empreintes (VI-15) ; la sortie n'écrase jamais (R12), **est scellée** par le module, son sceau est
**revérifié** par le script, puis committée et poussée. Un **lot arrêté empêche la table**. Les non résolus restent
`non_resolu`, chacun avec la cause écrite ; leur liste, avec leurs déclarations, est remise à Lazar (G2). **Table
complète** si les 4 sont résolus.

**Chaîne du script d'instance** (`r1_resolution_graine_instance_v1.sh`, amorce `amorce_instance_r1_resolution_graine_v1.sh`) :
validation → résolution → cibles du lot → lot (seulement s'il reste une cible) → table v3 (cœur + lot, ou cœur seul),
scellée, sceau revérifié, committée, poussée ; puis traces de l'instance. **Aucune étape n'en arrête une autre par sa
lecture, à une exception près** : l'étape table refuse de construire la table si le contrôle croisé du cœur n'est pas
« conforme » (R-11, VI-04) ; hors cette garde, seuls un arrêt de chaîne (code non nul ou `arret.json`) ou un commit refusé empêchent les suivantes ; une
validation arrêtée empêche la résolution ; une résolution arrêtée empêche le lot et la table ; des cibles illisibles
empêchent le lot et la table ; un lot arrêté empêche la table ; un commit refusé finit en échec (code 3), jamais
rapporté comme un succès.

**Suite : addendum v3.** La relance de R1 sur la table v3 (règles A et B, contrôle négatif, échantillon de fidélité,
sorties, versement, R2 et R4 ; écarts G3 à G7, G9, G10 du brouillon 1) est préenregistrée par l'addendum v3, écrit après
l'étape 2 : il cite l'empreinte de la table v3, celle des résultats scellés de ce rejeu, le commit et le nombre de tests
de son propre code ; il est contre-lu et soumis à la concordance de conv-audit avant tout lancement.

**Calendrier.** Fait : code intégré, corrigé après la vérification neuve VI, et ses essais (71 passés au commit
cité) ; configuration écrite ; répétition jouet du
script d'instance de bout en bout sur processeur (cas principal avec une cible au lot, cas « sans objet », commit refusé,
table sans sceau, libellé du lot absent, plafond trop bas : chacun avec l'issue attendue) ; pré-vol sur les vraies pièces
(cas sain et artefacts des contrôles d'avant l'installation et des gardes des modules). Fait aussi : table v2 scellée et
committée (`prereg/R1-table-tokenisation-v2.json.sha256`, `5f6cf489…`, commit `82a5ed18`) ; pièces de mesure, journaux et
rapports versés sous `graine-v1/` (en-tête) ; répétition jouet finale (cas principal et « sans objet ») et pré-vol
refaits au code cité. Reste, avant le scellement : contre-lecture finale neuve de la version à sceller ; devis révisé
porté à Lazar (« Coût et GO », VI-02) ; scellement de ce texte **et de la
configuration** ; puis lecteur neuf de conv-audit sur la version scellée ; poussée → instance A100 (étapes 0, 1, cibles,
1 bis, 2) → liste des non résolus à Lazar s'il y en a → addendum v3.

**Coût et GO.** A100-SXM4-80GB au **prix plafond de 1,40 USD de l'heure** (filtre d'offre). Durées estimées par
l'auteur, non mesurées sur le 8B : mise en place (clonage, installation, tokeniseur, 71 essais de 9 à 12 min sur
processeur, 16 Go de poids) 25 à 40 min ; validation et résolution 15 à 40 min ; lot fidèle 0 à 20 min ; table 2 min ;
attendu ≈ 45 à 100 min, soit **≈ 1,1 à 2,3 USD**. **Écart de devis déclaré (VI-02)** : la ligne d'extension de
GO-2026-11-02-02 (`registres/go.md` au commit `ddfff6e4`, l. 190) annonçait **≈ 1 USD attendu et 2 USD au pire** ; ce
texte dit **1,1 à 2,3 USD attendus et ≈ 6,2 USD au pire** (ci-dessous). Le plafond de 25 USD de la ligne tient
(≈ 4,6 + 6,2 ≈ 10,8 USD au pire) ; le **devis révisé est porté à Lazar avant la création de l'instance**. **Bornes de durée cohérentes** (VG-01 ; lues dans la configuration et
contrôlées par le script avant l'installation) : délais externes = budget interne de l'étape + 10 min ; mise en place
40 min ; validation 50 min ; résolution 50 min ; cibles du lot 5 min ; lot fidèle 70 min ; table 15 min ; poussées
5 min ; somme **235 min**, égale au **plafond de l'amorce (235 min)**, qui coupe le script (le script refuse de partir si
la somme dépasse le plafond). **Pire cas (m-7)** : 235 min d'amorce, plus la vie de l'instance hors amorce (démarrage de
l'instance et de l'image, avant l'amorce ; attente de l'arrêt par identifiant après la fin, R10), bornée à 30 min par la
surveillance de la session, soit 265 min × 1,40 USD/h ≈ **6,2 USD**, plus le disque. Dépenses engagées sous
GO-2026-11-01-13, prolongé par GO-2026-11-02-02 : ≈ 4,6 / 25 USD (relevé du 2 novembre, 03:10 UTC ; **à revérifier dans
le registre des dépenses avant la création**) ; après ce passage, au pire ≈ 10,8 / 25 USD, plus le disque ; la relance
(addendum v3) aura son propre devis sous la même ligne. Lancement : `GO_ID=GO-2026-11-02-02` devant la commande de
création ; **échéance 2026-11-09** : après, GO nouveau sous un identifiant nouveau. Branche de résultats :
`calcul/r1-resolution-graine-v1` (une branche existante arrête le script).

**Essais (processeur, sans dépense ; code au commit cité ; 71 attendus, liste à l'en-tête).** Cœur
(`tests/test_resolution_graine_v1.py`) : identité du tirage et tirages en un appel ; graines dérivées comme `jouer_p3` ;
vocabulaire et décodage de Llama 3.1 ; cas sain sur un modèle Llama minuscule de vocabulaire 128 256 avec le vrai
tokeniseur (découpages non canoniques, actions arrêtées à `max_nouveaux`, jeton spécial effacé) ; artefacts R5 (graine
fausse, texte altéré d'un octet, contexte décalé d'un jeton : « non résolu », jamais un faux « résolu ») ; repli à une
bascule et repli itératif à deux bascules dans deux actions ; budget de l'épisode (« non résolu : durée ») ; U+FFFD
résolu ou déclaré ; unité des balayages (trois U+FFFD compris) ; garde du compte de validation ; choix contraint depuis
p en float32 ; règle de lecture à trois classes et déclarations ; citation de la configuration (texte sans la ligne,
empreinte fausse, libellé altéré → arrêt) ; forme « identifiants » (cas sain, artefacts) ; formes des tables v1 et v2 ;
table v3 scellée, jamais écrasée ; bout en bout sur un P3 jouet joué par le vrai code de P3 (dont texte attendu de
l'ouverture : présent → passe, absent → arrêt) ; échéances au milieu d'une étape et signal (épisode « durée », suivants
« non tentés », résultat écrit ; TERM après k épisodes → `arret.json` cite les k épisodes consignés et scellés) ; gardes
d'exécution (agent comparé au manifeste de P3, réserves d'environnement, contrôle croisé « conforme » exigé par la
table, une seule exécution ; manifeste illisible → arrêt de la garde R3, VI-08) ; corrigés de la table v2 rapportés à
part au résultat de la validation (VI-10) ; gardes de configuration. Lot (`tests/test_resolution_graine_lot_v1.py`) : logits au bit
près et mesure des voisines (sain : accord 1 ; graine fausse sur une voisine : réserve) ; cas sain en lots de 8 et de 4 ;
ligne approchée la plus longue du lot : mêmes bits après correction ; unité des balayages alignée sur le cœur ; gardes du
forçage ; lot recomposé (logits différents, déclaré) ; graine fausse et texte altéré ; repli itératif dans le lot ;
budget de l'épisode ; plan des lots ; gardes de configuration, cibles (épisode de C-6 refusé, liste vide « sans objet »)
et unicité ; bout en bout jouet résolution du lot puis table v3, dont la déclaration finale des cibles du lot (résolue ;
budget de balayages et lecture « fidèle » de la cible ; même cause sous « réserve » ou « sans mesure » ; autre cause) et
`declarations_coeur` ; règle de `declarer_lot` sur des mesures fabriquées (classes, lectures, cible sans entrée, entrées
contradictoires) (VI-01, VI-09). Relance v3 (`tests/test_rejeu_activations_v3.py`,
autonome, hors de ce texte) ; outils (manifeste, scellement, préenregistrement, formats du harnais). Script d'instance :
répétition jouet et pré-vol (« Calendrier »), dont la citation de la configuration sous ses deux libellés (libellé du
lot absent, empreinte fausse, libellé cité deux fois → arrêt avant l'installation).

## Critères de lecture gelés

Règle unique : un épisode est **résolu si et seulement si** son empreinte de trajectoire égale celle de P3 (256 bits) ;
aucune autre mesure ne fait ni ne défait un « résolu ». La classe de la validation est celle de la règle gelée de
« Seuil » (`lire_validation`) ; les déclarations par épisode sont celles de `declarer`. Lectures :

| Issue observée | Lecture |
|---|---|
| Validation « graines validées » | Méthode et graines validées sur les résolus ; pas de réserve ; un non résolu de cause « budget de balayages dépassé » peut être déclaré non inversible (lignes ci-dessous) |
| Validation « méthode transposée, graines non validées » (147 retrouvées, une condition d'accord manquée) | **Réserve « graines »** : les « résolus » des étapes 1 et 1 bis restent des preuves ; **aucun non résolu n'est déclaré non inversible** (déclaration « non résolu, graines non validées : nœud porté à Lazar ») ; audit (R4) avant l'addendum v3 |
| Validation « méthode non transposée » (moins de 147 retrouvées, cause quelconque, « non tenté : durée » compris) | **Réserve sur HG-2** : la résolution est partie ; ses empreintes retrouvées restent des preuves ; tout non résolu est un nœud à Lazar (complément sous texte neuf, ou relance avec la table v2 et la règle B pour les 4, v1, E19) ; les épisodes manqués, leurs causes et leurs écarts sont rapportés ; si une cause est une durée, la mesure est déclarée incomplète |
| Distribution des écarts contraints | Descriptive (P-G3) ; comparée à P-G3 au résultat, sans conséquence de décision |
| Lot : `lecture_lot` « fidèle » (accord des voisines exactes ≥ 0,99, égalité des choix contraints ≥ 0,99 quand mesurée, aucun jeton connu hors des candidats ; au niveau de l'étape, toutes les cibles **mesurées** « fidèles » : la lecture d'ensemble ignore les cibles « sans mesure », VI-09) | Lot tenu pour fidèle ; **la déclaration d'une cible lit la lecture de cette cible** (`lecture_lot` de son entrée, c'est-à-dire de son lot), jamais la lecture d'ensemble (VI-09) ; un non résolu de lecture « fidèle » est lu comme les autres non résolus |
| Lot : « réserve lot non fidèle » (une cible au moins sous ces conditions) | **Réserve « lot non fidèle »** (carte, bibliothèque ou forme) ; ses « résolus » restent des preuves ; une cible de lecture « réserve » ne peut être déclarée non inversible : nœud ; chaque autre cible se lit sur sa propre lecture (VI-09) |
| Lot : « sans mesure » (aucune ligne voisine exacte mesurée pour une cible) | Réserve « lot non mesuré » : ses « résolus » restent des preuves ; une cible « sans mesure » non résolue est un nœud |
| Résolution : 7 / 7 à la fin de l'étape 1 bis (ou de l'étape 1, lot « sans objet »), contrôle croisé conforme | **Table v3 complète** ; addendum v3 sans règle B |
| Résolution : k non résolus (1 ≤ k ≤ 4, tous parmi les 4), contrôle croisé conforme | Table v3 partielle ; chaque non résolu porte sa cause et sa déclaration ; **liste à Lazar avant l'addendum v3 et avant toute lecture** (n° 356, point 4). Cause finale « caractère de remplacement : budget de balayages dépassé », **et** classe « graines validées », **et**, pour une cible du lot, lecture du lot « fidèle » **pour cette cible** = **non inversible déclaré par la méthode** (budget de recherche dépassé, non preuve d'impossibilité : le jeton de P3 reste dans l'ensemble contraint à chaque pas) : règle B de la v1 pour lui. Toute autre cause (empreinte non retrouvée après repli et lot, contradiction, durée de l'épisode, non tenté), ou la même cause sous une autre classe ou sous une autre lecture du lot = **non résolu par la méthode**, jamais déclaré non inversible : **nœud porté à Lazar avant l'addendum v3** (complément sous texte neuf, ou règle B pour l'épisode nommé) ; pour chacun, accord non contraint, accord attendu sous graine indépendante et pas informatifs rapportés. Pour les cibles du lot, cette règle est appliquée par le code de l'étape table (`declarer_lot`, VI-01), à partir de la cause du lot, de `classe_validation` et du `lecture_lot` **de la cible** ; la table v3 porte cette déclaration finale dans `declarations` (celle du cœur sous `declarations_coeur`) |
| Contrôle croisé « non résolu » : un épisode de C-6 non résolu à l'étape 1 | Répétabilité en défaut (il était retrouvé à l'étape 0, même code, même carte) : la table v3 **n'est pas construite** (garde de l'étape table) ; audit (R4) avant toute suite ; l'entrée de C-6 reste prouvée par l'empreinte ; toute reprise relève d'un texte neuf |
| Contrôle croisé « contraire » : un épisode de C-6 résolu avec d'autres identifiants que la table v2 | Impossible hors collision de sha256 : table non construite, lecture de ce rejeu arrêtée, audit (R4) avant toute suite |
| Audit de symétrie (R4) | Déclenché aussi par un résultat trop propre de la passe forcée : accord non contraint égal à 1 exactement sur tous les pas des 147 (le bruit du bfloat16 doit laisser quelques désaccords), aucune quasi-égalité sous 1, ou durée très en deçà de l'estimation (**durée cumulée des étapes 0 et 1 sous 5 min**, le tiers de la borne basse de 15 min de « Coût et GO ») ; et par un accord observé **non distinct de l'accord attendu sous graine indépendante**, chiffré (VI-11) : à l'étape 0, `accord_sur_les_pas` **≤ `attendu_graine_independante_sur_les_pas` + 0,02**, ou `accord_informatif` **≤ `attendu_informatif` + 0,10** (graines suspectes même si la classe est « graines validées ») ; l'audit vérifie d'abord que les identifiants connus n'ont pas fui dans la résolution. Pour le lot fidèle, un accord de 1 exactement est la prédiction (HG-4), non un signal |

## Liste d'arrêt

Les arrêts sont des **erreurs de chaîne seulement** : pièces, sceaux, graines, plan des lots, bibliothèque, commits.
Aucune mesure (classe de la validation, accord, écarts, nombre de résolus, lecture du lot) n'arrête quoi que ce soit,
**sauf** le contrôle croisé du cœur, qui, autre que « conforme », arrête l'étape table (R-11, VI-04).
Arrêts du script d'instance et des modules (R5 ; éprouvés par les essais, la répétition jouet et le pré-vol cités, ou lus
dans le code au commit cité et à éprouver par la contre-lecture), puis action :
- **avant l'installation** (code 2) : ce texte ou son `.sha256` absent au commit lancé ; « Tests attendus » ou « Chemin
  de la configuration de la résolution à graine » absent ou cité plus d'une fois ; configuration absente, non scellée
  ou de sceau faux ; **empreinte canonique de la configuration absente, citée plus d'une fois ou fausse sous l'un de ses
  deux libellés** (cœur, lot fidèle) ; **sceau d'une pièce faux ou absent, ou empreinte différente de celle que cite la
  configuration** (textes, scores, fiches, tâches, consignes, manifeste de P3, table v2 ; VG-04) ; **table v3 (ou son
  sceau) déjà présente** (R12) ; mode de la configuration différent du mode du lancement ; budgets du cœur ou du lot
  absents ou incohérents (budget d'épisode nul ou supérieur au budget d'étape) ; somme des délais supérieure au plafond
  de l'amorce ; branche de résultats déjà présente ou non vérifiable ; poussée initiale refusée ;
- **bibliothèque et carte** (code 1, consigné) : `nvidia-smi` absent ; torch différent de 2.14.1 ; carte indisponible
  pour torch ; tokeniseur de la révision citée introuvable avant les tests (VG-09) ; poids hors du dossier du tokeniseur
  éprouvé ;
- **tests** : dernière ligne différente de « 71 passed » (échec ou test sauté) ;
- **module, avant le manifeste** : configuration incomplète ou de valeur hors domaine (entiers négatifs, température
  nulle, `noyau_attention` hors de « defaut » et « math », `combinaisons_max_validation` ≠ `combinaisons_max`,
  `duree_max_episode_s` nul ou > `duree_max_s`, `regle_validation` de forme fausse, `seuil_lecture_lot` hors de [0, 1],
  budgets du lot incohérents, clé `repetition_non_tentes` en mode réel) ; texte qui ne cite pas l'empreinte canonique de
  la configuration sous le libellé du module, l'entropie ou le commit du code (arbre gelé différent du commit cité) ;
  pièce d'empreinte fausse ; **agent (modèle, révision, variables du gabarit) différent de celui du manifeste de P3**
  (VG-04) ; noyau du lot différent de celui de P3 ; run du manifeste différent du run source ; T, température ou
  `max_nouveaux` différents de la configuration de P3 ; N différent de 1 ;
  **étape déjà exécutée** sous ce texte (R3 : cœur, même commande, configuration et code, exécution qui a laissé une
  sortie ; lot, même commande et configuration) ; manifeste illisible dans `runs/` (cœur et lot, VI-08) ;
- **module, avant la boucle** (après le manifeste et le chargement du modèle, dans `_executer` ; `arret.json`) :
  validation de compte différent de 147 (`exiger_compte_validation`) ou seuil de validation inatteignable
  (`exiger_seuil_atteignable`) (VI-06) ;
- **graines, pendant le run** (`arret.json`, rien d'autre n'est lu) : graine `tache/<identifiant>` absente du manifeste
  de P3 ; identité du tirage fausse sur la bibliothèque installée ; formes des logits ou des tirages inattendues ;
  dimension des logits différente de la taille du tokeniseur ; ouverture sans le texte attendu (« Today Date: 26 Jul
  2024 ») ; jeton spécial non effacé au décodage ; fins hors des jetons spéciaux ;
- **plan des lots** (étape 1 bis) : plan reconstruit différent de l'ordre des textes de P3 ; manifeste de P3 sans taille
  de lot ; ligne voisine donnée pour exacte de longueur différente des jetons notés ; identifiants résolus par le cœur
  qui ne redonnent pas l'empreinte de P3 ;
- **chaîne des étapes** : résolution sans validation scellée, sans `arret.json`, de même configuration et de même code ;
  lot sans validation du cœur de même sorte et de classe présente, ou sans résultat scellé de la résolution de même
  configuration et de même code ; cible demandée refusée (épisode de C-6, résolu, absent) ; **étape table** : contrôle
  croisé du cœur autre que « conforme » ; résultat d'une autre configuration ou d'une autre étape (VI-05 : l'étape table ne compare pas le code) ;
  résultat du lot sans `classe_validation` ou fait sur un autre résultat du cœur ; deux résultats différents pour un
  même épisode ; empreinte de P3 du résultat différente de la table v2 ; correction qui ne redonne pas l'empreinte de
  P3 ; corrections vérifiées différentes des comptes ; sortie existante (R12) ; sceau non conforme après écriture ;
- **script** : validation arrêtée → résolution non lancée ; résolution arrêtée → lot et table non lancés ; cibles
  illisibles → lot et table non lancés ; lot arrêté → table non construite ; commit refusé → fin en échec (code 3) ;
- **lecture** : contrôle croisé « contraire » (lecture arrêtée, audit ; voir « Critères »).
**Ce qui n'est pas un arrêt** : toute classe de la validation ; moins de 147 retrouvées ; budget d'épisode épuisé
(« non résolu : durée ») ; budget d'étape épuisé (« non tenté ») ; lot « sans objet » ; lecture du lot « réserve » ou
« sans mesure » ; carte autre que l'A100-SXM4-80GB, `torch.version.cuda` autre que 13.0, cuDNN différent (réserves
écrites au résultat).
**Garde de dépense** (non une lecture) : pas de création sans `GO_ID=GO-2026-11-02-02` valide le jour même ; aucune
création après le 9 novembre 2026 sans GO nouveau ; **aucune location hors des filtres d'offre** (« Location ») : sans
offre conforme, rien n'est loué, nœud à Lazar ; plafond de l'amorce, 235 min, qui coupe le script (pire cas ≈ 6,2 USD
avec la vie hors amorce) : ce qui est consigné par épisode reste, le reste est perdu et déclaré.
**Lancement** : pas de lancement sans ce texte et sa configuration scellés, la table v2 scellée, le devis révisé
porté à Lazar (VI-02), la contre-lecture
finale neuve traitée et le rapport du lecteur neuf de conv-audit sur la version scellée (chemin et empreinte consignés) ;
aucune lecture de R2 (inchangé).
Dans tous les cas : sorties partielles committées et poussées sur `calcul/r1-resolution-graine-v1` ; aucune donnée de
P3 hors des tableaux permis n'est lue ; arrêt de l'instance par son identifiant (R10), consigné dans
`registres/arrets.md`.

## Traitement des lectures neuves

Rapports : brouillon 1 (« L1 ») `dd7157e188b1117c5542715452a6ca2c6a50694eab9d8a2f816615cf3bf9067b` ; brouillon 2
(« L2 ») `06459850ff7ece9e69b94d88867ce8e75ad96ba4b9091ee57b6cf64df2f54635` ; vérification neuve finale du
brouillon 3 et du code `31f72147` (« VI ») `7dfe39c9820019b8c44956bbec48b1ecd5937e5591f1536c32aed003a9f03a1b` ; vérification adverse du code
`5c39c6b6` (« VG », résumé) `36eacff68db4764ab62a6b46965f31e6bc2f9daddbf6f881152a63096551cb50`. « Traité » = texte (et code au commit cité
quand le point en exige) ; « déclaré » = écart ou limite écrits sans correction ; « sans objet » = le point ne vise plus
rien dans ce texte.

| Identifiant | Sort | Où |
|---|---|---|
| L1 B-1 / C-1 (durée par épisode, résultat toujours écrit, délais) | traité | « Seuil » (budgets) ; « Plan d'analyse », point 6 et « Coût et GO » (délais = budget + 10 min, 235 min) ; code `755959e1` ; la formule « résolution ≥ 7 × budget + 5 min » est remplacée par un budget d'étape interne de 2 400 s, conséquence déclarée (derniers épisodes possiblement « non tentés ») |
| L1 B-2 / C-2 ; L2 B-2 (reconduit) ; R-08 ; R2-03 (unité de `balayages_max`, U+FFFD par épisode) | traité | « Seuil » (16 par U+FFFD, unité `commencant_par(E)` non vide) ; « Plan d'analyse », point 7 et volumes (1 dans les 7, 0 dans les 147 ; compte par épisode cité à l'en-tête) ; code `ca3dfa3f` ; essai à trois U+FFFD |
| L1 B-3 / C-3 (validation non bloquante, cinq conditions) | traité | (1) règle gelée en clair, identique à `lire_validation` (« Seuil ») ; (2) `exiger_validation` sans condition de lecture (étape 1) ; (3) classe recopiée (« Métrique », étapes 1, 1 bis, 2) ; (4) « non inversible » sous « graines validées » seulement (« Seuil », « Critères ») ; (5) R3 (« Seuil ») |
| L1 C-4 / I-1 ; R-14 ; L2 I-C ; R2-10 (carte, CUDA, filtres, exposition) | traité | « Précision » : `torch.version.cuda` et cuDNN en réserve, pilote au journal ; « Location » : filtres écrits, « centre de données » gardé, aucune offre → rien loué, nœud à Lazar ; exposition du dépôt et des jetons déclarée hors du GO |
| L1 C-5 / I-2 / I-4 ; L2 I-D ; R2-09 (accord pour tout épisode, attendu sous graine indépendante, pas informatifs) | traité | « Métrique » ; P-G1 (formule corrigée) ; code `ca3dfa3f` (`mesures_accord`) |
| L1 C-6 / I-3 ; R-06 à R-09 ; R2-04 (« non inversible », causes) | traité | R-06 : G2 ; R-07 : HG-3 ; R-08 : « Seuil », point 7 ; R-09 et R2-04 : « Critères », ligne k non résolus (parenthèse fausse retirée, « cas non simple » → « budget de balayages dépassé ») ; fait (a) |
| L1 C-7 ; R-13 ; m-4 (calcul du choix contraint) | traité | « Précision » : p en float32 sur processeur puis log p − log q en double, code `ca3dfa3f` ; mesure de 2·10⁻⁷ nat citée pour la variante du brouillon 1, non remesurée (déclaré) |
| L1 C-8 / I-5 ; L2 R2-15 (essais : durée, citation sous deux libellés, ouverture, coupure après k épisodes, ligne approchée) | traité | « Essais » ; « Tests attendus » recompté à 69, puis à 71 après la vérification neuve VI |
| L1 C-9 / I-6 ; L2 I-E ; R-15 ; R2-12 (chiffres en bfloat16 de P-G3) | traité (retirés) | P-G3 |
| L1 R-01 (règle à trois classes) | traité | « Seuil » (valeurs 0,95, 0,90, 0,90, 1 000) |
| L1 R-02 (P-G1) | traité | P-G1 |
| L1 R-03 (étape 0 : mesure) | traité | étape 0 |
| L1 R-04 (étape 1 : ordre, sans condition de lecture) | traité | étape 1 ; `episodes_resolution` (« Seuil ») |
| L1 R-05 ; L1 m-1 ; L2 R2-13 (formulation de l'aveugle) | traité | étape 0 |
| L1 R-10 (lectures de la validation) | traité | « Critères », trois premières lignes |
| L1 R-11 ; L1 m-2 ; L2 R2-14 (contrôle croisé à trois valeurs, répétabilité, garde de la table) | traité | étape 1 (répétabilité) ; étape 2 et « Liste d'arrêt » (table seulement sur « conforme ») ; « Critères » ; valeur « non résolu » du code gardée (au lieu de « non répété » proposé) |
| L1 R-12 (durée, causes, pire cas) | traité | « Métrique », « Plan d'analyse », « Coût et GO » |
| L1 R-16 (liste d'arrêt) | traité | « Liste d'arrêt », chaîne des étapes |
| L1 R-17 (`combinaisons_max_validation` = 136) | traité | « Seuil » |
| L1 R-18 ; L1 m-6 ; L2 R2-11 ; mineur m-6 (inversion de l'ordre lot / passe forcée par rapport au n° 352) | déclaré | en-tête (« Méthode ») ; écart G11 |
| L1 m-3 (compte exact de 147) | traité | « Seuil » (`seuil_validation`) ; étape 0 |
| L1 m-5 (les 3 de C-6 en tête) | traité | « Seuil » (`episodes_resolution`) |
| L1 m-7 ; L2 mineur m-7 (vie de l'instance hors amorce dans le pire cas) | traité | « Coût et GO » (265 min × 1,40 USD/h ≈ 6,2 USD) |
| L1 m-8 (attentes de réception de la concordance pour la table v3) | déclaré (à faire dans l'addendum v3) | « Écarts … renvoi à l'addendum v3 » |
| L1 verdict sur le n° 265 (« une graine fausse ne résout rien ») | traité | « Hypothèse », dernier paragraphe |
| L2 B-L1 ; R2-01 ; R2-02 (lignes approchées : forme du lot) | traité | HG-4 ; étape 1 bis ; « Métrique » (forme) ; code `9f898ee2` (`forcee`, mesure de la forme) et essai de la ligne approchée la plus longue |
| L2 B-L2 (texte et code du lot alignés : cibles, validation du lot, repli) ; R2-05 ; R2-06 | traité | étape « cibles du lot » ; étape 1 bis (mesure des voisines, étape `validation-lot` retirée, repli itératif, `combinaisons_max_lot` = 136) ; code `9f898ee2` |
| L2 I-A ; R2-07 (R3 : une exécution par étape) | traité | « Seuil » (R3) ; garde du lot sans comparaison du code, déclarée |
| L2 I-B ; R2-08 (classe et lecture du lot recopiées) | traité | « Métrique » ; étapes 1 bis et 2 |
| L2 mineur m-1 (aveugle) | traité | étape 0 |
| L2 mineurs : garde de l'étape table ; parenthèse fausse ; « cas non simple » ; essais de C-8 manquants ; R6 des volumes ; prix plafond | traité | étape 2 et « Liste d'arrêt » ; « Critères » ; « Seuil » ; « Essais » ; en-tête et volumes (sorties du pré-vol et du compte des U+FFFD, chemins et empreintes ; les volumes sans provenance, jetons en passe et durée de la génération de P3, sont retirés) ; « Location » et « Coût et GO » |
| L2 C-7 (alignement du code sur le texte, n° 267) | traité | code `ca3dfa3f` (`probabilites`, `scores_contraints`) |
| Intégration : table v2 sans `.sha256` | traité | compagnon committé au commit `82a5ed18` ; en-tête ; « Calendrier » |
| Intégration : seuils au choix de l'auteur ; clé `repetition_non_tentes` | déclaré | « Seuil » |
| VI-01 (déclarations du cœur recopiées pour les cibles du lot ; texte contradictoire) | traité | code `0e2a8871` (`declarer_lot`, `declarations_du_lot`, `declarations_coeur` ; essais qui échouent sans la correction) ; étape 2 ; « Critères », ligne « k non résolus » |
| VI-02 (devis au-dessus de la ligne de GO) | déclaré | « Coût et GO » (écart déclaré ; plafond de 25 USD tenu ; devis révisé porté à Lazar avant la création) ; « Calendrier » ; « Liste d'arrêt » (lancement) |
| VI-03 (« 0 = forme exacte prouvée » dit trop) | traité | HG-4 (preuve par d_max ; `forme_exacte_prouvee` lu « exacte si fins par défaut ») ; P-G4 (comptes des quatre lots, lot 5 « non prouvé ») |
| VI-04 (« aucune étape… » et « aucune mesure… » trop larges) | traité | « Chaîne du script d'instance » ; « Liste d'arrêt » (exception du contrôle croisé, R-11) |
| VI-05 (« d'un autre code » non codé à l'étape table) | traité (retiré) | « Liste d'arrêt », chaîne des étapes ; rien de codé |
| VI-06 (compte de 147 vérifié après le manifeste) | traité | « Liste d'arrêt » (« module, avant la boucle ») |
| VI-07 (écart contraint en double, non par p / q en float32) | traité | « Précision et ordre des opérations » |
| VI-08 (garde R3 du cœur : sortie laissée ; manifeste illisible sauté) | traité | code `0e2a8871` (arrêt sur manifeste illisible, essai) ; « Seuil » (R3) ; « Liste d'arrêt » ; « Essais » |
| VI-09 (lecture d'ensemble du lot sans les cibles « sans mesure ») | traité | « Critères » (lignes du lot : déclaration sur la lecture de la cible) ; code `0e2a8871` (`declarer_lot`) |
| VI-10 (18 corrigés rapportés à part) | traité | code `0e2a8871` (`corriges_table_v2`, essai) ; étape 0 |
| VI-11 (déclencheurs de l'audit R4 non chiffrés) | traité | « Critères », ligne « Audit de symétrie » (accord ≤ attendu + 0,02 sur les pas, ≤ attendu + 0,10 sur les pas informatifs ; durée des étapes 0 et 1 sous 5 min) |
| VI-12 (attribution d'essai fausse) | traité | « Seuil », règle de lecture gelée de la validation |
| VI-13 (R6 : C-6 sans compagnon ; journaux de répétition non cités) | traité | compagnons au commit `82a5ed18` ; en-tête (pièces versées sous `graine-v1/`, chemins et empreintes) |
| VI-14 (réserve cuDNN dite au journal) | traité | « Précision et ordre des opérations » |
| VI-15 (schéma de `lecture_validation` selon la voie ; causes hors de la table) | traité | étape 2 |
| VI-16 (préparateur lu depuis le répertoire courant) | traité | code `0e2a8871` (préparateur de la répétition) ; répétition finale lancée d'un répertoire courant sans `donnees/` |

## Contre-lecture

Historique de la v1 (contre-lecture 1, vérification de concordance de conv-audit, vérification du brouillon 2) : voir
la section « Contre-lecture » de l'addendum v1, brouillon 4 ; la contre-lecture 2 de la v1 est sans objet (arrêtée,
n° 256). Lecteurs déjà passés sur cette v2 (aucun n'a écrit le texte ni le code) ; rapports versés sous `docs/notes/runs-r1-r2-r4-v1/graine-v1/`
(compagnons `.sha256`, commit `82a5ed18`) :
- **Vérification adverse VG-01 à VG-10** du code `5c39c6b6` (brouillon 1 ; session-depot, n° 265, branche
  `canal/session-depot-reprise-n92`, message `28f412b7…`), verdict « prêt après corrections » : traitée au commit
  `755959e1` (VG-01 à VG-09) puis `31f72147` (VG-07 remplacé par l'unité B-2 de conv-audit), vérifiée à l'intégration par
  la répétition jouet et les essais. Le texte intégral du rapport n'a pas été conservé dans un fichier (journal du
  workflow `wf_f711147d-c00` de la session) : **résumé** versé, `verification-adverse-vg-resume-v1.md`
  (`36eacff68db4764ab62a6b46965f31e6bc2f9daddbf6f881152a63096551cb50`).
- **Lecture neuve de conv-audit sur le brouillon 1** (`7915a3d653d4de7a41b8fc22d86e4988ede765ae8638ccc335029f9a08644784`)
  et le code `5c39c6b6` : rapport `verification-addendum-r1-v2-brouillon1-v1.md`
  (`dd7157e188b1117c5542715452a6ca2c6a50694eab9d8a2f816615cf3bf9067b`) ; traitement : section « Traitement des lectures
  neuves ».
- **Lecture neuve de conv-audit sur le brouillon 2** (`d4617ea837cd81accc4dc8e26d6d1be2015f1f10eaecad2258b3e54c9eb48c89`)
  et le lot `99022f43` : rapport `verification-addendum-r1-v2-brouillon2-v1.md`
  (`06459850ff7ece9e69b94d88867ce8e75ad96ba4b9091ee57b6cf64df2f54635`) ; traitement : même section.
- **Vérification neuve finale (VI)** du brouillon 3 (`0f4c445c9585309568d76e1f01155474be20cc76df1eac0abb4cc3dab4170e87`)
  et du code `31f72147`, verdict « scellable après corrections » : rapport `verification-neuve-vi-v1.md`
  (`7dfe39c9820019b8c44956bbec48b1ecd5937e5591f1536c32aed003a9f03a1b`, texte recopié tel quel) ; traitement : même section (VI-01 à VI-16) ; code
  corrigé au commit `0e2a8871`.

R2 exige encore une contre-lecture neuve de la **version à sceller** : texte entier, configuration
`prereg/R1-graine-config-v1.json` et code au commit cité (points du n° 352 : précision et ordre des opérations, carte
comprise ; dérivation des graines ; critère de passage entre la passe forcée et le lot fidèle ; étape 0 à l'aveugle ;
contrôle croisé des 3 de C-6 ; règle « non inversible » et sa lecture ; plus la règle gelée de la validation comparée à
`lire_validation`, le repli itératif, les budgets et la cohérence des délais, les filtres d'offre, et chaque ligne du
traitement des lectures neuves). Le rapport du lecteur neuf de conv-audit sur la version scellée est une condition de
lancement (« Liste d'arrêt »), non une entrée de ce texte.

- **Contre-lecture 1** (sous-agent neuf, auteur d'aucune pièce, version à sceller) : À REMPLIR (identifiant ;
  brouillon relu, empreinte ; chemin et empreinte du rapport ; traitement de chaque remarque).

# Vérification de VL-01 sur le lanceur A1-v3 v3.1 (commit public `9776ed0`) — v1

- **Rôle** : vérificateur neuf de session-depot ; je n'ai écrit ni le lanceur, ni ses essais, ni le texte. Un seul point : VL-01.
- **Heures** (`date -u`) : du 3 novembre 2026, 01:10:55 UTC, au 3 novembre 2026, 01:33 UTC.
- **Règles tenues** : aucun réseau (chaque processus Python sous `unshare -n` : seule l'interface `lo`, éteinte) ; aucun appel de
  modèle ; aucune instance ; aucune clé (`env -i` : `PATH`, `HOME`, `LANG`, `TMPDIR`, `PYTHONDONTWRITEBYTECODE` seulement ;
  `noms_de_cle_presents` vide dans chaque sortie) ; aucun commit, aucun `git fetch` ; rien sous `donnees/` (ni lu, ni écrit, ni
  lancé : la garde directe ne lit que les chaînes des arguments, et les copies remplacent les chemins des scripts de commande) ;
  `nice -n 10` ; interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (Python 3.13.18, numpy 2.4.6, pytest 9.1.1), en
  `-B -s`. Écart mineur : deux affichages de version de l'interpréteur (01:17 UTC) lancés sans `nice` ni `env -i` ; ils n'ont rien
  importé de la copie.
- **Copie isolée intacte** : tête `9776ed0efee97146182ff2c4b409e5ec224a0bbf`, `git status --porcelain --ignored` vide au début et
  à la fin, aucun `__pycache__`. Les essais et les mutations ont tourné dans une copie de travail (`cp -a`, mêmes empreintes,
  elle aussi propre à la fin). Aucun processus laissé : tous les lancements au premier plan, terminés (contrôlé par `ps`).
- **Aucun `.sha256` écrit par moi** : le texte factice est « scellé » en mémoire (section 2). Les essais du développeur écrivent
  eux-mêmes des compagnons dans leurs dossiers temporaires (69 au premier passage, 30 au second) : listés puis supprimés.
- Dossier de travail, noté `$T` : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/verif-vl01-v31/travail-vl01-v1/`.

## 1. Verdict

**VL-01 levé avec réserves** : la garde est jouée pour chaque fournisseur du plan avant toute écriture dans la sortie,
`--verifier-seulement` compris ; elle refuse en code 2 tous les artefacts de la spécification, admet ses deux formes, et la
configuration gelée réelle la passe. Réserves (section 5) : trois comportements de la garde ne sont tenus par aucun essai du
développeur ; deux limites hors de la spécification (jeton sur une autre option, abréviations d'options) ; un dossier temporaire vide
créé avant la garde. Aucune ne touche la configuration gelée d'A1-v3.

## 2. La configuration gelée passe-t-elle la garde ? **Oui.**

- Fichier `configuration-mini-course-kimi-argon-v3.json`, sha256 `e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30` (vérifié).
- **Argon** (le seul fournisseur du plan) : arguments 7 à 10 = `--registre`, `{REGISTRE}`, `--plafond-cumule-usd`, `80`. Un seul argument porte
  le jeton (le 8), en forme « --option {REGISTRE} » sur deux arguments ; `--registre` est donnée une fois (le 7) ; une seule option
  `--plafond-cumule-usd` (le 9), en forme séparée, de valeur numérique `80` (le 10). `exiger_substitutions("argon", …)` rend sans exception.
- **Kimi** (hors plan) : arguments 6 à 9, même forme ; `exiger_substitutions("kimi", …)` rend aussi sans exception.
- `reglages_de_configuration` (qui appelle la garde, l. 359) sur la configuration gelée, avec le plan du bloc `plan-gele` du brouillon 4
  (Argon seul) : rend `(1.8, {"argon": "gemini-4-argon"})`. Avec un plan factice Argon puis Kimi : rend les deux modèles.
- **Substitutions** (`l2.substituer_commandes`, plafond 400) : il y en a quatre, comme l'annonce le brouillon 4. Pour Argon, l'argument 8
  `{REGISTRE}` devient le registre de la course et l'argument 10 `80` devient `400` ; Kimi (arguments 7 et 9) est substitué de même, sans
  effet puisqu'il est hors plan. Commande d'Argon après substitution :
  `… --registre <sortie>/registre-depense-cumulee-v1.jsonl --plafond-cumule-usd 400 …`.
- **`--verifier-seulement`** du lanceur entier sur une copie (cas S0). Elle ne diffère de la configuration gelée que par deux points : le
  chemin des deux scripts de commande (argument 3, remplacé par une commande factice qui écrit toute exécution) et les pièces (chemins et
  empreintes factices). Les arguments des commandes sont identiques à l'octet. Résultat : code 0, « conforme », écriture « aucune », un
  adaptateur (Argon), accusé `attaque_goodhart_v3/argon` à 400 USD, quatre substitutions. La sortie n'a jamais été créée ; la commande
  factice n'a jamais été lancée.
- **Point ouvert tranché.** Le brouillon 4 (section 4, « la forme exacte de ses arguments n'a pas été relue ») et le rapport du
  développeur (section 3, point 4 ; section 10) laissaient ouverte la forme réelle des arguments. Elle est admise : VL-01 n'exige pas de
  configuration nouvelle.
- **Méthode de `--verifier-seulement` (écarts déclarés).**
  - Texte : le brouillon 4 (`6841b6c4…`), renommé `preenregistrement-attaque-goodhart-v3-v<N>.md` dans un dossier neuf. Le marqueur
    `<<COMMIT_V3_1>>` (5 occurrences) est remplacé par `9776ed0efee9…` ; la ligne `configuration_sha256` du bloc prend l'empreinte de la
    copie du cas.
  - Le bloc `empreintes-du-code` est inchangé : 73 lignes, toutes conformes au code de la copie (`sha256sum -c`).
  - `DOSSIER_PREREG` pointe sur ce dossier. `verifier_scelle` est remplacé en mémoire par la même règle (empreinte du texte égale à
    celle relevée à la préparation), pour n'écrire aucun compagnon.
  - Registre des GO factice : `GO-2026-11-02-21`, type calcul, 400 USD, jusqu'au 16 novembre ; plus une ligne factice pour le plan à
    deux fournisseurs (634 USD, au-dessus du devis lu par le code).
  - Tout le reste est le code du commit, appelé par `principal([...])`.

## 3. Table des cas

- **Garde directe** : `exiger_substitutions` pour chaque fournisseur du plan, puis `reglages_de_configuration` (même décision dans tous
  les cas), sur la configuration gelée réelle modifiée en mémoire.
- **`--verifier-seulement`** : `principal` entier, sur la copie factice du cas.
- Dans chaque refus : la sortie n'est jamais créée, la commande factice n'est jamais lancée, aucune variable de clé n'est présente.
- Les messages sont abrégés ; le texte complet est dans `$T/sorties/vs-<cas>.json` et dans `$T/sorties/garde-directe-v1.json`.

| cas | garde directe | `--verifier-seulement` |
|---|---|---|
| S0 configuration gelée telle quelle, plan d'A1-v3 (Argon seul) | acceptée | 0, conforme ; 4 substitutions ; accusé Argon 400 |
| S0b la même, plan factice Argon puis Kimi | acceptée (les deux) | 0, conforme ; accusés 317 + 317 |
| S1 jeton en forme jointe `--registre={REGISTRE}` (admis) | acceptée | 0, conforme |
| S2 valeur `80.0` | acceptée | 0, conforme |
| A1 jeton absent (`--registre /chemin/fixe/…`) | refus : « porte 0 argument(s) avec le jeton {REGISTRE} » | 2, même message |
| A2 jeton deux fois, sur deux options (`… --journal {REGISTRE}`) | refus : « 2 argument(s) » | 2 |
| A2b jeton deux fois, `--registre {REGISTRE}` redonné | refus : « 2 argument(s) » | 2 |
| A3 `--plafond-cumule-usd` absente | refus : « exactement une option … (trouvé []) » | 2 |
| A4 option deux fois, en forme séparée (80 puis 20) | refus : « exactement une option … (trouvé [deux]) » | 2 |
| A4b option deux fois, la seconde jointe (`--plafond-cumule-usd=20`) | refus : « exactement une option » | 2 |
| A5a valeur « quatre-vingts » | refus : « doit être un nombre » | 2 |
| A5b valeur « 80,5 » | refus : « doit être un nombre » | 2 |
| A5c valeur « 1e3 » | refus : idem | 2 |
| A5d valeur « -5 » | refus : idem | 2 |
| A5e valeur vide | refus : idem | 2 |
| A5f nombre 80 (pas une chaîne) | refus : « doit être un nombre (trouvé 80) » | 2 |
| A6 forme jointe `--plafond-cumule-usd=80`, à sa place réelle | refus : « exactement une option … en forme séparée (trouvé ['--plafond-cumule-usd=80']) » | 2 |
| A6b forme jointe, en fin de commande | refus : même message | 2 |
| A7 Kimi hors plan mal formé (registre fixe, sans l'option) ; plan Argon seul | **acceptée : Kimi ignoré** (garde jouée sur Argon seul) | 0, conforme ; 2 substitutions (Argon seul) ; Kimi sans porte transmise ni proposeur |
| A7b le même Kimi, mais au plan (Argon puis Kimi) | refus : « la commande de « kimi » porte 0 argument(s) » | 2 |
| X1 jeton sur une autre option, registre fixe (`--registre /chemin/fixe … --journal {REGISTRE}`) | **acceptée** | **0, conforme** ; la commande substituée garde `--registre /chemin/fixe/…` |
| X2 option du registre redonnée en forme jointe (`--registre=/chemin/fixe/…`) | refus : « donnée plus d'une fois » | 2 |
| X3 option du registre redonnée par abréviation (`--regis /chemin/fixe/…`) | **acceptée** | **0, conforme** |
| X4 option du plafond redonnée par abréviation (`--plafond-cumule 20`) | **acceptée** | **0, conforme** |
| X5 `--registre=/x/{REGISTRE}` | refus : « hors des formes » | 2 |
| X7 jeton seul, sans option devant | refus : « hors des formes » | 2 |

- **Forme jointe du plafond** (spécification : forme séparée exigée) : le code la refuse, seule (A6, A6b) comme ajoutée à la forme
  séparée (A4b).
- **Fournisseur hors du plan** : le code l'ignore (A7). C'est cohérent avec la spécification (« chaque fournisseur du plan ») et avec le
  brouillon 4 (Kimi hors plan : ni proposeur, ni porte, ni étape). Mis au plan, il est refusé (A7b).
- **Chemin réel sans `--verifier-seulement`**, joué sur A1, A2, A3, A4b, A5a, A6, A7b et X2 : code 2, mêmes messages, sortie jamais créée.
  Le harnais rejoue d'abord la garde seule ; la course, le relevé du dépôt et l'écriture scellée sont rendus impossibles en mémoire.
- **Où la garde est appelée** :
  1. `principal` (l. 459) lit le texte, vérifie l'empreinte de la configuration, le GO, puis lit la configuration (l. 540-548) ;
  2. `tempfile.mkdtemp` (l. 549) ;
  3. `proposeurs_reels` (l. 550) contrôle les variables de clé (l. 379-382), puis appelle `reglages_de_configuration` (l. 384) ;
  4. `reglages_de_configuration` appelle `exiger_substitutions` pour chaque fournisseur du plan (l. 359). C'est avant
     `substituer_commandes` (l. 385) et avant le retour de `--verifier-seulement` (l. 558-561) ;
  5. un refus est attrapé l. 562-564 et rend le code 2 ;
  6. la sortie n'est créée qu'à la l. 576.
- Les renvois du brouillon 4 et du rapport sont exacts : `:302-333`, `:359`, `:336-370`, `:379-382`, `:385`, `:541-546`, `:558-561`,
  et dans le lanceur v2 `:233-250`, `:248`.
- **Second passage** complet, avec les versions finales des harnais (`$T/sorties/passage2/`) : identique au premier, aux noms des
  dossiers temporaires près ; 26 refus en code 2 (18 sous `--verifier-seulement`, 8 par le chemin réel).

## 4. Essais et mutations rejoués

- **Essais VL-01 du développeur**, repérés par leur nom (pytest, copie de travail, même confinement) :
  `LanceurCheminReel::test_substitutions_des_commandes_exigees`, et
  `LanceurCheminReel::test_modele_servi_autre_que_demande_refuse_jamais_un_repli_muet` (mis à jour pour VL-01 selon le rapport,
  section 2, C4).
  - Résultat : **2 réussis, 10 sous-essais réussis, 0 échec** (1,21 s ; de 01:25:02 à 01:25:04 UTC).
  - Les 10 sous-essais sont les 10 artefacts de l'essai VL-01 ; ses deux formes saines et le refus du lanceur ne sont pas des sous-essais.
- **Mutation 44 du banc** (« substitutions des commandes du plan non exigées (VL-01) », 44e des 49), rejouée seule avec la mécanique du
  banc, deux fois (01:25 et 01:28 UTC) :
  - témoin avant : 1 essai, 0 échec ;
  - **tuée pour la raison attendue** : 11 échecs sur 1 essai, soit les 10 sous-essais « AttaqueRefusee not raised » et l'assertion du
    lanceur « 0 != 2 » (sous mutation, `--verifier-seulement` rend 0, sans lancer de course) ;
  - témoin après : 1 essai, 0 échec.
- **Mes mutations**, appliquées en mémoire sur l'instance du lanceur des essais (aucun fichier modifié), deux passages identiques. Table
  de référence : 8 acceptés, 18 refusés ; témoins avant et après conformes.

| mutation | essai VL-01 du développeur | mes cas |
|---|---|---|
| MV1 garde jouée pour le premier fournisseur du plan seulement | **survit** | tuée par A7b |
| MV2 doublon de l'option du registre compté en forme séparée seulement | **survit** | tuée par X2 |
| MV3 `--plafond-cumule-usd` comptée en forme séparée seulement | **survit** | tuée par A4b (A6 et A6b : refus gardé, message changé) |
| MV4 contrôle « valeur numérique » retiré | tuée (« valeur = une autre option ») | tuée par A5a à A5e |

## 5. Réserves

1. **Essais (R5).** Le code tient trois comportements (A7b, X2 et A4b sont refusés), mais aucun essai ne les tient :
   - « chaque fournisseur du plan » : l'essai VL-01 n'a qu'un fournisseur au plan ;
   - l'option du registre redonnée en forme jointe ;
   - l'option du plafond redonnée en forme jointe.

   Une mutation qui retire l'un d'eux survit (MV1 à MV3). Correction : trois sous-essais (plan à deux fournisseurs dont le second est
   mal formé ; `--registre=…` ajouté ; `--plafond-cumule-usd=…` ajouté). Sans effet sur A1-v3 : un seul fournisseur, configuration
   conforme.
2. **Limites de la garde hors de la spécification.** Elles sont sans effet sur la configuration gelée, que le texte fixe par son empreinte.
   - (a) X1 : le jeton est exigé sur une option quelconque, pas sur celle que la commande lit comme registre.
     `--registre /chemin/fixe … --journal {REGISTRE}` passe, et le registre fixe reste.
   - (b) X3 et X4 : le « une seule fois » ne compte que le nom exact ; une abréviation (`--regis`, `--plafond-cumule`) passe. Si la
     commande lit ses options par argparse avec les abréviations permises (défaut de Python ; le premier vérificateur a vu des sorties
     d'argparse), la dernière occurrence l'emporterait. Ce serait le défaut de classe d'A1 par un autre chemin. Je ne peux pas le
     vérifier ici : le code de la commande est sous `donnees/` et je ne l'ai pas lu.

   Ces cas sont visibles avant la course, puisque `--verifier-seulement` imprime la commande substituée. Corrections possibles : exiger
   le jeton sur `--registre` ; refuser tout argument qui est un préfixe de `--registre` ou de `--plafond-cumule-usd`. Au minimum,
   l'écrire au texte.
3. **« Avant toute écriture ».** Rien n'est écrit dans la sortie, mais `principal` crée un dossier temporaire vide
   `attaque-goodhart-v3-sessions-*` (l. 549) avant la garde, et ne le retire pas après un refus (vu dans chacun des 26 refus). Après un
   `--verifier-seulement` conforme, ce dossier reste, avec un sous-dossier par fournisseur du plan : le « écriture : aucune » de la sortie
   ne vise que la sortie. L'ordre est le même en v2 (l. 372-373). Observation.
4. **Message.** Pour une valeur nombre (A5f), le message dit « doit être un nombre (trouvé 80) ». Il faudrait dire « une chaîne
   numérique ». Cosmétique.
5. **Méthode.** `--verifier-seulement` a été joué sur des copies (scripts de commande et pièces factices, sceau en mémoire,
   `DOSSIER_PREREG` déplacé), pas sur la machine de session-depot. La garde ne lit que les chaînes des arguments, identiques à l'octet
   dans la configuration gelée. Le `--verifier-seulement` réel avant la course (brouillon 4, section 13, point 8) reste à faire, comme
   prévu.

## 6. Fichiers lus et empreintes

Commit `9776ed0` (copie isolée ; chemins relatifs à `orchestrator/`) :

| fichier | sha256 |
|---|---|
| `demonstrations/attaque_goodhart_v3.py` (lanceur v3.1) | `87d52ace3c5faea02672fbcabeb3b22844fe62342c4aed9ee0b4f8d3e220d16e` (annoncé `87d52ace…` : conforme) |
| `pole/attaque_goodhart_v3.py` (cœur v3.1) | `cb9cffe77fb858bf279c41881638edecba0166b034a05d44c2f62e2b25a45df3` (annoncé : conforme) |
| `prereg/preenregistrement-attaque-goodhart-v3-brouillon4.md` (sections 0.1 ter, 4 « Configuration », bloc `plan-gele`, empreintes) | `6841b6c4c7eeca73279168d85b8dc3abfc5e998aa9923597d7240612170b32c3` (conforme) |
| `prereg/rapport-redaction-attaque-goodhart-v3-1.md` (C4, sections 3 à 5, 10, 11) | `6b30c04bf6f8f8ee8cd3b280286c6a901153205d056e217526806d14478d2e52` (conforme) |
| `essais/test_attaque_goodhart_v3.py` | `8ab42fe0aaa9da79f3f7a9cef8096183f6c33329565eb86393561b1f1bf05c75` |
| `essais/mutations_attaque_goodhart_v3.py` | `96ade331879662b5957515cda125a1ee47b6722e15a99e1e24fc98d384bbfdbf` |
| `demonstrations/attaque_goodhart_v2.py` (`substituer_commandes`, `verifier_go`) | `58609e0c9fc5c5eea5de1dbb8c9b8235fd85a9884d326ffe09dfb50b21af79cf` |
| `demonstrations/ideation_v8.py` (`adaptateurs_reels_v56`) | `2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1` |
| `pole/adaptateurs_v56.py` (portes, adaptateur v56) | `d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17` |
| `pole/adaptateurs.py` (`AdaptateurCommandeExterne`, l. 600-680) | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` |
| `pole/configuration_v53.py`, `_v54`, `_v55`, `_v56` (lecture, pièces, GO) | `ef72ffbf…`, `3424ca7f…`, `2e6237c0…`, `12240522…` |
| `pole/outils.py` (`verifier_scelle`, `ecrire_scelle`), `pole/relais.py` (`noms_de_cle_presents`) | `966d9553…`, `b5a76343…` |
| `essais/aides_v54.py`, `essais/aides_v56.py`, `essais/conftest.py` | `c65e1979…`, `d0fc2ca3…`, `c60e041d…` |

Hors du dépôt :
- configuration gelée `…/verif-vl01-v31/configuration-mini-course-kimi-argon-v3.json` : `e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30` (conforme) ;
- rapport du premier vérificateur `…/verif-vl01-v31/verification-lanceur-a1v3-v1.md` : `7ffe45ab5f4adcf5dbfbd6c60bc120c7e248e914ce853145070b91a91e749221` (conforme).

Produits par moi (sous `$T`, aucun compagnon) :

| fichier | sha256 |
|---|---|
| `harnais/vl01_v1.py` (version finale, celle du second passage) | `cf55d68621554a619244c428ed8c8b7947f300d40707daf54012f43b1fd502ad` |
| `harnais/lancer_v1.sh`, `harnais/lancer_passage2_v1.sh` | `c214cf1e…`, `dcf66a34…` |
| `harnais/mutation44_v1.py`, `harnais/mutations_vl01_v1.py` | `00b2d904…`, `da61e05c…` |
| `factices/commande_factice_v1.py`, `factices/registre-go-factice-v1.md`, `cas.json` | `62efa087…`, `c6ba869c…`, `5882d536…` |
| `sorties/garde-directe-v1.json` (= `sorties/passage2/garde-directe.json`) | `d33047248764298f50f3db3413856247c47012dcbb7881b89507fe3e3cee852f` |
| `sorties/pytest-vl01-v1.txt`, `sorties/mutation44-v1b.txt` | `2ca89351…`, `e8fe280c…` |
| `sorties/mutations-vl01-v1.txt` (= `sorties/passage2/mutations-vl01.txt`) | `2bfeceba8c3f3251d5d520363537016bcf6fb8b9f4d06fef2c814496041d5959` |
| `sorties/vs-*.json`, `sorties/vr-*.json` (34 fichiers, premier passage) ; `sorties/passage2/` (second) | concaténation du premier passage : `bd8d7374…` |

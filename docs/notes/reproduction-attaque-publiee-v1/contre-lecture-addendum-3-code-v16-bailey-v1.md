# Contre-lecture de l'addendum 3 (brouillon 2) au préenregistrement du témoin de Bailey — code v16, nouvelle série

- **Qui** : contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni l'addendum, ni le code, ni les relectures
  précédentes.
- **Quand** : 12 novembre 2026, vers 18:10 UTC.
- **Commit lu** : `093ddbd96cc9345e336f627ad9754bd1bf44d147` (arbre propre).
- **Routine de reprise** : non exécutée (consigne). Aucune instance, aucune commande `vastai`, aucun appel réseau, aucun
  `git commit` ni `git push`. Aucun fichier cloisonné ouvert ; aucune valeur de clé lue ; aucun fichier de notes.

Pièces lues (SHA-256) :

| Pièce | Empreinte |
|---|---|
| `brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v16-brouillon2.md` (en entier) | `328405b72c28a122914210241f40e75e1cda8118c0cba2acd427d482466195ba` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (en entier) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome.md` (en entier) | `f79459c712a0f12ecbf55c9ea787f67032031e9672e6db002b84725286c96e13` |
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v14-bailey-v1.md` | `0e7c96ca231465ee4a2e0cf5fbe9c1d146d6caa5ce60460462adaf067fa3c377` |
| `docs/notes/reproduction-attaque-publiee-v1/relecture-differentiel-code-condition6-v15-bailey-v1.md` | `0d7cc2a12b61fbfadcc47e0981fbeebb9d58881273450052a08cd1dca752d49f` |
| `registres/passations/2026-11-12-1545-temoin-bailey-pilote-seconde-chute-noeud.md` | `21f0fc4d48a135a9a016e81d9a4ce91aed948952d91a5517d39f1dd609dec72b` |
| `registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md` | `df3833a9d773d6b7b5daf36d1662a547cc24b90bfc0204ce7b4ef00fc5c32be2` |
| `registres/passations/2026-11-12-1250-poste-hetzner-temoin-bailey-plan.md` (source du « go c ») | `4f40c079e569d8fd148bac2526730091da645f866fe68804b0221493975ad3e3` |
| `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json` | `e15d456fed8b04923bf7115fd300c38beeb5b976ccf1d47e9ea86667445f6e57` |
| `runs/temoin-bailey-v1-20261111/manifeste-local-v3.json` (comparaison) | `69143b990725fa827f49b69e7209d6c30ffc87c04ba50c370a25e47ad3693cd2` |
| `runs/temoin-bailey-v1-20261111/lancer-conduite-v8.py` | `a02f7b5be86e52e9c8b396114b7556234d07047b576a9dc527ac1d84a21eb812` |
| `runs/temoin-bailey-v1-20261111/poste-hetzner-v7.sh` (l. 1-100, 143-144) | `624f070ee65c630c8606a78c6bf8e02cfb7d753b96f12798719f75aaab0bfdb8` |
| `src/controle_ia/temoin_bailey/instance_v14.py` (différentiel) | `19366e7acae186ca1587f73d097a190fadd930b91544f2626bb9d9e9fbd0cf75` |
| `src/controle_ia/temoin_bailey/instance_v15.py` | `39725c4c190f73262861ea1fee6f8e4360cca3712c271349b1b44eeff2fd100f` |
| `src/controle_ia/temoin_bailey/lanceur_v15.py` (différentiel) | `819258047270dd731b3bf8aca072cdcb82c173d2928b24f2182a3d88492c04a9` |
| `src/controle_ia/temoin_bailey/lanceur_v16.py` | `03df34aabc5146d4136d0ffe61a0df450362cb1c2a50c2030cd612f7cc57a6a0` |
| `src/controle_ia/temoin_bailey/execution_v3.py` | `279f1f4f6e04fad67db457831abdba712d16feb15571c24173988af9a1a58a5f` |
| `tests/test_temoin_bailey_condition6_v15.py` (différentiel) | `13bf913829e87a454cfa4e2d4bd10b14f5af10055365dc5bee96de58b51c8122` |
| `tests/test_temoin_bailey_condition6_v16.py` | `f5b71cade69e66b091910144329262706c5c3c092252c09af21b412ef6aeacf8` |
| `docs/notes/reproduction-attaque-publiee-v1/devis-temoin-attaque-publiee-bailey-v4.md` (passages) | `f9c8c66e32a68b58cc63291fbe25a106a2e50cd5d49e52c35aa3fa9bb4c5ca44` |
| `brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v14-brouillon1.md` (empreinte seule) | `614dc5d7669ccc598186a13df11937448752e9cc0fdf9ceba3c924cc108dc78a` |

## Verdict

**Scellable après corrections.** Le code v16 est conforme et les empreintes du § 3 tiennent. Mais l'addendum présente
la nouvelle série comme « permise », sans dire qui l'a décidée ni qu'elle s'écarte de R3 et de la ligne « seconde chute
du pilote » (K-2, bloquant, corrigeable par le texte proposé). Une empreinte est fausse (K-1). Le défaut `signal` touche
le code scellé des addenda 1 et 2, ce que le texte ne dit pas (K-3). Le dépôt chez le tiers, l'état des conditions de
lancement et deux risques manquent.

## Vérifications faites

- `git show 91238a73:<chemin> | sha256sum` : `lanceur_v16.py` `03df34aa…` et `instance_v15.py` `39725c4c…`, égaux au
  § 3 ; compagnons `.sha256` de ces deux fichiers et de `tests/test_temoin_bailey_condition6_v16.py` (`f5b71cad…`) :
  OK. `lecture_v8`, `execution_v3`, `journaliseur_v3`, `conventions_v3`, `analyse_v3` à ce commit : égaux à la table
  de l'addendum 2. `git diff 4988f3f4 91238a73` vide pour ces cinq modules et pour les quatre autres fichiers de
  l'archive (`__init__.py` ×2, `gardes.py`, `scellement.py`). `git diff 91238a73 093ddbd9 -- src tests` vide.
- Manifeste v4 : `commit_code` = `91238a73…` ; seule différence avec le v3 : cette ligne. Graines recalculées par
  `SeedSequence(165783307199007749115201767022379793885).spawn(3)`, `generate_state(1)` : 1394228342, 1865327867, égales
  au texte et au manifeste. Versions figées `e21bccf6…`, compagnon OK.
- D recalculé sur la liste `ANTERIEURES` de `lancer-conduite-v8.py` (quatre instances, c × durée) : 1,9762 USD, égal au
  texte. Première instance du poste : 60280913, créée le 12 novembre à 00:03:20Z.
- Empreintes citées au § 1 et au § 3 (`fb6c2f34…`, `21f0fc4d…`, `df3833a9…`, `0e7c96ca…`, `0d7cc2a1…`) : justes, sauf
  celle du brouillon 1 (K-1).
- Essais : `PYTHONPATH=src python -m pytest -q tests/test_temoin_bailey_condition6_v16.py` : **161 passés** (175 s) ;
  `tests/test_temoin_bailey_analyse_v3.py` : 36 passés.

## Points

### K-1 — à corriger — empreinte fausse du brouillon 1
Passage (en-tête) : « (`brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v14-brouillon1.md`, `f5e40842…`,
gardé tel quel, R12) ». `f5e40842…` est l'empreinte de `runs/temoin-bailey-v1-20261111/poste-hetzner-v6.sh`. Le
brouillon 1 (commit `1f15e43e`, compagnon et disque) vaut `614dc5d7…`.
Correction : remplacer `f5e40842…` par `614dc5d7669ccc598186a13df11937448752e9cc0fdf9ceba3c924cc108dc78a`.

### K-2 — bloquant (corrigeable par le texte) — la nouvelle série n'est pas dite comme un écart décidé par Lazar
Passage (§ 2.4) : « La seconde chute du pilote est due à un défaut survenu avant tout tour et avant toute donnée. Une
**nouvelle série** est permise, une seule ». Trois manques :
1. Qui décide. Le texte scellé dit « Seconde chute du pilote : pas de run principal, pas de verdict ; nœud » (l. 245,
   366). Seul Lazar tranche un nœud. Le « go (a) » répond à « (a) … avant de relouer une A100. (b) Arrêter le témoin » :
   il couvre une nouvelle série, mais par implication. Le passif « est permise » le cache.
2. R3. Le texte dit « Il est couru une fois. […] La seule relance permise est celle de la liste d'arrêt, pour cause
   technique nommée » (l. 69-71). Ici, la cause **n'est pas nommée** (note `21f0fc4d…` : « Cause : non établie »). La
   nouvelle série n'est donc pas une relance de la liste d'arrêt : c'est un écart à la lettre de R3. Il est défendable
   sur le fond (aucune note n'existe ; rien n'a été lu ; le signe n'a pas pu guider le choix), mais il doit être nommé.
   « due à un défaut survenu avant tout tour » dit plus que ce qu'on sait : on sait seulement qu'aucun tour n'a fini.
3. Le titre du § 2, « Écarts actés par cet addendum », ne dit pas que ces écarts sont décidés par Lazar.

Correction : titre du § 2 : « **Écarts décidés par Lazar sur le nœud de la seconde chute du pilote (« go (a) »,
`df3833a9…`), actés par cet addendum** ». Remplacer le § 2.4 par :
« 4. **Nouvelle série (écart à R3 et à la ligne « Seconde chute du pilote … nœud », texte l. 69-71, 245, 366).**
Décision de Lazar sur ce nœud : « go (a) », dont l'option comprenait « relouer une A100 », contre (b) « arrêter le
témoin » (`registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md`, `df3833a9…`). La cause de la
seconde chute n'est pas nommée : ce n'est pas la relance de la liste d'arrêt, c'est un écart. Ce qui le rend compatible
avec l'objet de R3 : les exécutions du 12 novembre ont fini avec zéro tour complet ; aucune note de sonde ni de juge
n'existe ; rien n'a été lu ; la reprise ne peut donc pas viser un signe. Une seule nouvelle série : pilote, au plus une
reprise, puis la règle et le run principal selon le texte, inchangés. Mêmes graines (pilote 1394228342, run principal
1865327867 ; aucune sortie n'a été produite sous ces graines). B inchangé : 75 USD, fixé à la création de la première
instance du poste (60280913, 12 novembre, 00:03:20Z). D continue de cumuler depuis cette instance : 1,976 USD après
quatre instances détruites (liste `ANTERIEURES` de `runs/temoin-bailey-v1-20261111/lancer-conduite-v8.py`,
`a02f7b5b…`) ; l'essai à blanc, s'il a lieu, y entre (« go (a) »). Les exécutions du 12 novembre sont rapportées comme
interrompues. Une nouvelle seconde chute du pilote : pas de run principal, pas de verdict ; nœud ; aucune autre série
sans nouvelle décision de Lazar et nouvel addendum. »

### K-3 — à corriger — le défaut `signal` touchait le code scellé des addenda 1 et 2
Passage (§ 3, « Défaut corrigé ») : « masquait le module `signal` depuis la v7 […] les relectures du code v7 à v12 ne
l'ont pas vu ». Vérifié : la ligne `signal: list[str] = []` est dans `instance_v7`, `v8`, `v10`, `v11`, `v12`.
`instance_v8` est le module du code de l'addendum 1 (commit `99b59d33`) ; `instance_v12` celui de l'addendum 2
(`4988f3f4`), qui a tourné le 12 novembre. Les épreuves R5 déclarées par ces addenda ne couvraient donc pas l'arrêt de
l'enfant par son PID. La relecture v13 ne relisait pas `instance_v12` (« Non lus : `instance_v12.py` (inchangé) »).
Correction : remplacer la fin du paragraphe par : « … et laissaient l'enfant vivre. Ce défaut est dans le code scellé par
l'addendum 1 (`instance_v8`) et par l'addendum 2 (`instance_v12`, commit `4988f3f4`) : pendant les exécutions du
12 novembre, ces trois arrêts n'étaient pas opérants ; seuls le chien de garde et les veilleurs bornaient la dépense.
Sans effet observé : l'enfant est mort de lui-même. Les épreuves R5 de ces addenda ne couvraient pas ce chemin. Les
relectures du code v7 à v12 ne l'ont pas vu ; la relecture v13 ne relisait pas `instance_v12`. Rapporté à Lazar avec
cet addendum (R4). »

### K-4 — à corriger — dépôt chez le tiers et état des conditions de lancement absents
La décision `df3833a9…` engage : « addendum 3 […] scellé, contre-lu, **déposé chez le tiers** ; aucune dépense avant
l'addendum scellé ». L'addendum 2 a un § 5 « Conditions de lancement (état au scellement) » ; l'addendum 3 n'en a pas.
Or la nouvelle série exige de les revérifier (texte l. 376-390 : « toutes requises avant la création de l'instance »).
Correction : ajouter un § « 6. Conditions de lancement (état au scellement) » :
« 1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01`, comme à l'addendum 2 ; échéance (2026-11-30) à
revérifier à la création contre création + (B − 2)/c heures, c relevé. 3, 4 : comme à l'addendum 2, inchangées.
5 : comme à l'addendum 2 (addendum 2 de la règle du bras, `73c8de01…`) : la nouvelle série ne change pas ce que le
verdict vaut pour le témoin. 6 : remplie par cet addendum, une fois scellé **et déposé chez le tiers** ; il remplace,
pour la condition 6, le code de l'addendum 2. 7 : le mot direct de Lazar du 11 novembre portait sur la première série ;
un mot direct pour cette série est requis (§ 5, point 3). 8 : pilotage par le poste Hetzner autonome (« go c »,
`registres/passations/2026-11-12-1250-poste-hetzner-temoin-bailey-plan.md`, `4f40c079…`) ; `DEPOT_URL` du dépôt de
travail. Aucune instance avant le scellement, le dépôt chez le tiers et le mot de la condition 7. »

### K-5 — à préciser — fidélité du § 2.1 au code (filtre et vacuité)
Le § 2.1 suit le code (`instance_v15.ecrire_erreur_demarrage`, `erreur_demarrage_filtree`, l. 248-336, 841-842) :
code non nul, garde non décidée, zéro tour, `attendu.startswith(tampon)`, `cause is None`, `_vide` sur le journal lu
dans `config-journal-v3.json` et sur `sondes/` et `params/` ; 60 lignes, 300 caractères après le filtre, 20 000 octets ;
motifs justes. Trois écarts de mots, sondés sur le code :
- « nombre décimal ou à exposant : `<nombre>` » dit plus que le motif. Gardés tels quels : `score 0.97.` (suivi d'un
  point), `0.97/1`, `x_0.97`, `0,97` (virgule). La phrase suivante couvre le fond, pas ces formes.
- « jeton Hugging Face » : le motif exige `hf_` suivi d'au moins 30 caractères alphanumériques, non précédé d'un
  caractère de mot (`hf_` + 29 caractères passe).
- « absents ou vides, sans lien symbolique ni entrée spéciale » : le code tient pour vides des sous-dossiers vides et des
  fichiers de taille nulle.
- « ligne qui contient `tensor(` retirée entière » : elle est remplacée par la marque `[ligne retirée : tenseur]`.
Correction : « valeurs remplacées sur place (nombre décimal isolé, ou à exposant, non collé à un nom, un chemin ou une
version : `<nombre>` ; suite de plus de 12 chiffres : `<chiffres>` ; `hf_` suivi d'au moins 30 caractères
alphanumériques : `<jeton>` ; suite alphanumérique de 32 caractères ou plus, sans `_` ni `-` : `<suite>`) ; ligne qui
contient `tensor(` remplacée par une marque ; […] Le filtre ne retire ni les entiers, ni les mots, ni les nombres à
virgule ou suivis d'un point : c'est une défense en profondeur ; la garantie vient de la condition. » Et : « dossiers des
sondes et des suffixes (écart 9) absents, ou ne contenant que des sous-dossiers et des fichiers vides ; tout lien
symbolique, tube ou erreur de lecture les fait tenir pour non vides. »
Ajouter aussi : « « aucun arrêt décidé par l'instance » s'entend des trois arrêts d'`executer` ; un enfant tué par un
autre processus (chien de garde, noyau à court de mémoire) avant d'avoir fini d'imprimer la configuration laisse le
message, sous la même condition. »

### K-6 — à préciser — deux risques nouveaux à déclarer
1. **Sortie standard étrangère.** La condition exige que la sortie standard reçue soit un début exact de la
   configuration. `execution_v3.main` importe `transformers`, `obf_reps` et `train_harmful` avant l'impression de la
   l. 173. Si une bibliothèque imprime sur la sortie standard pendant ces imports, puis que l'enfant meurt, le message ne
   sort pas, et la cause reste non établie, comme le 12 novembre. On ne sait pas si c'était le cas le 12 novembre (la
   sortie standard est restée sur l'instance).
2. **Code local du poste.** `poste-hetzner-v7.sh` (l. 92-95) vérifie l'empreinte de `lancer-conduite-v8.py` et du
   manifeste, et que le commit `91238a73` existe ; il exécute `lanceur_v16` depuis la tête de la branche, sans vérifier
   ce fichier. L'archive envoyée sur l'instance, elle, est tirée du commit.
Correction : ajouter un § « Risques déclarés » : « Ceux de l'addendum 2 (§ 4), tous gardés. En plus : (a) si la sortie
standard porte, avant la mort, autre chose qu'un début de la configuration (impression d'une bibliothèque à l'import),
le message ne sort pas ; (b) un enfant bloqué avant l'impression n'a pas de délai (§ 5, point 2) ; (c) le poste exécute
le lanceur local depuis la tête de la branche ; seuls le script de conduite (`a02f7b5b…`), le manifeste (`e15d456f…`) et
la présence du commit `91238a73` sont vérifiés ; `lanceur_v16.py` n'y est pas vérifié par empreinte. » Pour (c), une
garde peu chère est possible dans un poste v8 : `git diff --quiet 91238a73 HEAD -- src/` avant la conduite.

### K-7 — à préciser — sources (règle R6) et pièces de lancement
- § 3 : citer l'empreinte du manifeste : `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json` (`e15d456f…`) ; dire
  que sa seule différence avec le v3 (`69143b99…`) est `commit_code`.
- § 2.5 : citer les pièces de lancement : `lancer-conduite-v8.py` (`a02f7b5b…`, disque 110 Go, ligne `DISQUE_GO`),
  `poste-hetzner-v7.sh` (`624f070e…`, filtre 128,9 Go) ; source du « go c » : `4f40c079…` ; source des mots sur le disque
  et la mémoire : note `21f0fc4d…`. Ajouter : « Le disque de 110 Go reste une des causes possibles de la seconde chute
  (note `21f0fc4d…`) ; il est gardé ; si c'est la cause, le message le dira (« No space left on device »). »
- § 3 : citer l'empreinte de `tests/test_temoin_bailey_analyse_v3.py` (`8cca01f1…`, inchangé).
- § 4 : « lectures 1 à 38 actées » ; préciser : « la lecture 12 (liste v11, `c1747537…`) est complétée par le § 2.1 ;
  aucune autre lecture ne change ».
- Reprise : ajouter au § 2.1 : « La reprise (`lanceur_v16 reprendre`, même chemin absolu de `--sortie` :
  `runs/temoin-bailey-v1-20261111/sortie-conduite-v8`) transfère et scelle le fichier s'il existe ; elle ne l'écrit
  jamais (`reconstituer_etat` ne l'écrit pas). »
- À l'archivage : section « Contre-lecture » comme à l'addendum 2 (ce rapport, son empreinte, le brouillon 2 archivé
  `328405b7…`).

### K-8 — à préciser — points ouverts pour Lazar (§ 5)
Forme : la consigne du dépôt veut, pour chaque décision, l'enjeu, les options avec avantage et inconvénient, une
recommandation **avec confiance**, et le défaut. Les deux points changent une décision de Lazar ou une garde : ce sont
des nœuds, sans défaut ; le dire.
- **Point 1 (essai à blanc).** Recommandation défendable : la garde de mémoire vive exclut les petits hôtes ; un essai
  hors conduite serait du code neuf, à relire ; un échec sur A100 coûte environ 0,44 USD. Mais l'enjeu manque : la
  nouvelle série est **unique** (K-2). Si l'exécution v16 retombe deux fois, la série est consommée et l'on revient à un
  nœud, cette fois avec le message. L'essai à blanc, lui, ne consommerait pas la série. Texte à ajouter : « Enjeu : sans
  essai à blanc, une nouvelle double chute consomme la seule série permise (nœud, avec le message). Avec un essai à blanc
  sur petite carte : la garde de mémoire vive tomberait sur la plupart des hôtes ; l'adapter serait un écart et du code
  neuf. Recommandation : remplacer l'essai à blanc par la première exécution v16, confiance moyenne. Nœud : pas de
  défaut. »
- **Point 2 (délai de la garde de démarrage).** Recommandation (a) défendable : coût borné par B ; un délai serait du
  code neuf. Mais une alerte à 4 heures laisse payer environ 5 USD pour un enfant bloqué, alors que l'impression de la
  configuration vient avant tout chargement de modèle. Texte à ajouter : « Variante (a′) : alerte si la configuration
  effective n'est pas décidée 30 minutes après le lancement du pilote, si la conduite le rend visible au poste ; sinon
  4 heures. L'alerte ne déclenche aucun arrêt par la session sans mot de Lazar, sauf les arrêts de la liste d'arrêt
  (R10, par identifiant). Recommandation : (a), ou (a′) si visible ; confiance moyenne. Nœud : pas de défaut. »
- **Point 3, à ajouter (condition 7).** « Mot direct de Lazar pour le lancement de la nouvelle série (texte, condition
  7), après le scellement et le dépôt de cet addendum. Options : (a) mot exprès ; (b) tenir le « go (a) » pour ce mot.
  Recommandation : (a), confiance haute : le « go (a) » prévoyait un essai à blanc avant de relouer, et le § 5 le change. »

## Le code v16 (vérification 2)

Différentiels lus : `instance_v14` → `instance_v15`, `lanceur_v15` → `lanceur_v16` (brut et normalisé), essais v15 → v16.
Le lanceur ne change que la docstring, l'import, `INSTANCE_MODULE`, `VEILLEUR_MODULE`, `CHEMINS_ARCHIVE` et deux
messages. L'instance ne change que les trois motifs, `_vide`, `_journal_des_notes`, le nom du drapeau et sa docstring.

| Point | État | Constat |
|---|---|---|
| D-1 | Corrigé | `_SUITE = [A-Za-z0-9]{32,}` ; essai `test_v16_filtre_noms_gardes_valeurs_remplacees` : `is_torch_greater_or_equal_than_1_13` et `models--meta-llama--…` gardés, empreinte de 40 caractères masquée. |
| D-2 | Corrigé | `(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}` ; `hf_transfer`, `hf_quantizer` gardés. |
| D-3 | Corrigé | `.97`, `1e-3`, `9.7466e-01`, `0.97`, `-0.5` remplacés ; versions et numéros de ligne gardés. |
| D-4 | Corrigé (partie principale) | Deux essais à enfant **sans** sortie standard (dépense ; échéance) : `configuration_effective` « non décidée », cause attendue, pas de fichier. Mutation faite (retrait de `and cause is None`, copie hors du dépôt) : ces deux essais et l'ancien tombent, sans effet de temps. Reste : l'ancien essai `test_v15_arret_par_la_depense_et_par_l_echeance` n'a été ni renommé ni amené à attendre la garde passée (deuxième moitié de D-4) ; sans risque, son nom dit plus qu'il ne vérifie. |
| D-5 | Corrigé | `mort_seule_avant_configuration` ; docstring en cinq conditions. |
| D-7 | Corrigé | `_vide` : lien, lien cassé, tube, fichier non vide, erreur de lecture : non vide ; essai `test_v16_vacuite_…` avec le journal au chemin de `config-journal-v3.json`. Repli de `_journal_des_notes` sur `cv.JOURNAL_NOTES` si la configuration est illisible : silencieux, mais sans effet (fichier écrit par `executer` avant l'enfant). |
| D-8 | Corrigé en grande partie | Dossier d'étape réel : `empreintes`, transfert simulé, `sceller`, `dossier_de_foi`, `journaux_scelles`, `relance_permise`. La docstring dit aussi « la garde de fin de run n'a pas à être appelée (K′ = 0) » : non vérifié par l'essai. |

**Défaut nouveau** : aucun dans le code. Essais : 161 passés. Deux limites de conception, non des défauts, à déclarer
(K-6) : la condition de début exact rend le message muet si une bibliothèque imprime sur la sortie standard à l'import ;
le lanceur local du poste n'est pas vérifié par empreinte.

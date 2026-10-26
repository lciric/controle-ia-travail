# Organisme v6.2.1 corrigé par la lignée conv-audit : vérification en isolation (v1)

- **Début** : 2026-10-25 23:46:30 UTC (lu sur `date -u` au lancement).
- **Écriture de ce rapport** : 2026-10-26 00:00:49 UTC (lue sur `date -u` au moment de l'écrire).
- **Retouches** : 2026-10-26 00:03:52 UTC (lue sur `date -u`). Deux comptes de fichiers d'essais sont corrigés
  (8 des 9) et deux précisions ajoutées (§ 3.2, points 1 et 4).

Sous-agent de vérification neuf ; je n'ai écrit aucun des fichiers vérifiés. Commandes git : deux extractions
`git -C /home/claude/canal-conv-audit-n04 archive <commit> organisme | tar -x -C <dossier neuf>` (passées par `tee` pour
garder l'archive), pour `7ea3270` et `3bbb78c`, aucune autre. Aucun accès réseau, aucun sous-agent, aucune clé
rencontrée, aucun fichier ou dossier interdit ouvert. Les programmes de l'organisme n'ont tourné qu'en isolation (essais
et `invariance_v1.py`) ; tout le reste est lecture, `diff`, `sha256sum`, arbre syntaxique et mes outils, lancés par
`python -I`. **Écart** : deux fichiers transitoires écrits hors de mon dossier par erreur, puis effacés (`/tmp/x`, vide,
effacé dans la même commande ; `a.txt` dans le dossier de travail de la session, liste de sha256) :
`verification-v1/ecarts-ecriture-v1.txt`. Empreintes de toutes les pièces : `EMPREINTES-v1.txt`.

## Verdict

- **Aucun défaut bloquant.**
- **Provenance conforme** : empreinte d'arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`,
  26 fichiers, commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e` (en-tête de l'archive). Seuls 6 fichiers changent
  (4 changés, 2 ajoutés), et **rien ne change hors de ce qu'annonce `CORRECTIONS-v5.md`** (§ 1).
- **Essais** : 68 sur 68 passent en isolation, deux fois (5,21 s et 5,29 s) ; les 53 de la v6.2 sont tous présents et
  passent. Le seul essai hérité changé est celui qu'annonce `CORRECTIONS-v5.md`, et son changement se limite à ce que C-15
  exige ; il n'est pas affaibli.
- **Témoins** : conformes à `CORRECTIONS-v5.md`. Sur la v6.2, les essais nouveaux donnent 7 échecs et 8 réussites ; sur
  la v6.2.1, l'essai hérité d'origine donne 1 échec et 4 réussites. Mais 2 des 7 échecs ne viennent pas du défaut visé
  (§ 2.3).
- **Les six points partiels de la v6.2 sont levés** (§ 3). Deux le sont avec un choix gardé, désormais avec ses raisons
  (3 et 5). Trois le sont parce que la seule voie qui menait du code arbitraire à la validation est fermée (7, 9 et 10) :
  les fonctions de contrôle elles-mêmes n'ont pas changé. Les 7 points déjà levés le restent.
- **Le reste est conforme** :
  - V6-01 reste corrigé ;
  - les relevés sont identiques sous les graines 0, 1 et 2, et égaux à ceux de `3bbb78c` à la version et au temps
    mesuré près ;
  - 0 appel imbriqué sous `_VERROU` ;
  - les gardes C-01 à C-13 tiennent ;
  - le contrat du noyau est tenu.
- **Sous la configuration du pilote 4** (lecture seule) :
  - les appels par ronde et par génération sont ceux de la v6.2 ;
  - une caste par tâche en génération notée ;
  - la mutation est tentée et acceptée comme en v6.2 pour une réponse de l'architecte en objet JSON ;
  - le critère de fin de conception est inchangé.
- **Constats non bloquants** (§ 3.2) :
  - un des deux volets de C-15, la lecture du routage, n'est gardé par aucun essai de la suite ;
  - un commentaire d'essai contredit C-14 ;
  - le refus de C-16 passe par une exception ;
  - l'exactitude d'entraînement reste rapportée, jusque dans la consigne de l'architecte.

## 1. Provenance (résultat 1)

| objet | commit (en-tête de l'archive) | date des fichiers | empreinte d'arbre | fichiers |
|---|---|---|---|---|
| **v6.2.1** | `7ea32705c5437d91ed071dd95fb3209bb0b0035e` | 2026-10-25 23:44:20 UTC | **`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`** (conforme à l'annonce) | 26 |
| v6.2, base | `3bbb78c1991baf17feb421529fa1957be7edec59` | 2026-10-25 22:57:18 UTC | `3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946` (conforme) | 24 |

- **Méthode** : l'empreinte d'arbre vient de `outils-v1/empreinte_arbre_v1.py`, transcription de `boucle.empreinte_arbre`
  reprise de la vérification v6.2 (empreinte conforme ; non relue ici contre le noyau).
- **Archive de `3bbb78c`** : identique octet pour octet à celle de la vérification v6.2 (`3e9ceaa7…`). Ses 24 fichiers
  ont les mêmes sha256.
- **Parenté** : je ne l'ai pas vérifiée, faute d'autre commande git. Ce que je constate est cohérent avec « enfant de
  `3bbb78c` ».

**Inventaire** (`inventaire-3bbb78c-vers-7ea3270-v1.txt`, `comptes-diff-…`, `diff-3bbb78c-vers-7ea3270-*-v1.txt`) : 20
fichiers identiques octet pour octet, dont `politique_endogene.py`, `memoire_isvd.py`, `mitose_spectrale.py`, `metrique/`
et 8 des 9 fichiers d'essais. Les autres :

| fichier | état | ajoutées / retirées | octets |
|---|---|---|---|
| `principal.py` | changé | 45 / 7 | 96 483 → 99 519 |
| `CONCEPTION.md` | changé | 7 / 0 (§ 2.14 ajouté à la fin, rien d'autre) | 22 423 → 24 877 |
| `manifeste.json` | changé | 3 / 3 : version `6.2.0` → `6.2.1`, description, saut de ligne final ; nom inchangé, « lignee assistee » | 541 → 539 |
| `tests/test_emprunts_v5_3.py` | changé | 14 / 2 | 9 425 → 10 750 |
| `CORRECTIONS-v5.md` | ajouté | — | 9 170 |
| `tests/test_corrections_v5.py` | ajouté | — | 19 697 |

**Par l'arbre syntaxique** (`fonctions-ast-3bbb78c-vers-7ea3270-v1.txt`), dans `principal.py` : 35 fonctions inchangées,
6 changées, 1 ajoutée. La seule constante changée est `VERSION` (`organisme-gemini-m3-v6-2-1`). S'y ajoute l'import de
`MOTS_CLES_EVAL_FAMILLE` et `MOTS_CLES_CTRL_FAMILLE` depuis `memoire_isvd` (l. 14-15).

| fonction | correction annoncée | ce que montre le diff |
|---|---|---|
| `_traiter_tache` | C-14 | l. 1734-1738 seulement |
| `_entrainer_et_predire_sondes_traits` | C-15 | l. 611-619 seulement |
| `executer` et `executer._une` | C-15 (appel du routage) | l. 1985-1986 seulement, dans `_une` ; `executer` ne change que par elle |
| `_expression_mots_cles` (ajoutée) | C-16 | l. 967-975 |
| `_synthetiser_mutation_politique_endogene` | C-16 (gabarit) et C-17 (réponse de l'architecte) | l. 1026-1035 et 1082-1083 seulement |
| `_propager_successeur` | C-17 | l. 1558-1562 seulement |

Dans les essais, seule `test_v5_3_sondes_traits_entrainer_predire_et_routage_faible_vers_fort` change, avec sa fonction
interne `predire`. **Conclusion : chaque changement correspond à une ligne de `CORRECTIONS-v5.md` ; il n'y a aucun
changement non annoncé.** La description du manifeste et son saut de ligne final relèvent de la ligne « Version ».

## 2. Essais en isolation (résultat 2)

**Méthode** : celle de la vérification v6.2 (`outils-v1/lancer_isole_v1.sh`).
- **Copies** : une copie à part par exécution (`cp -a`, puis `chown -R nobody`), sous `essais-v1/`.
- **Commande** : `unshare -n sudo -u nobody env -i PATH=/usr/bin:/bin HOME=<copie> LANG=C.UTF-8 TMPDIR=<copie>/tmp
  PYTHONDONTWRITEBYTECODE=1 [PYTHONHASHSEED=n] /opt/venv-essaim-sim-v1/bin/python -P -s -B …`, jamais `-I`, recopiée en
  tête de chaque journal.
- **Contrôles de l'isolation** (`sonde-isolation-v621-v1.log`) :
  - pour chaque graine, `hash("a")` est le même sur deux lancements, et le même qu'aux vérifications précédentes ;
  - le réseau est refusé (`OSError` 101) ;
  - l'utilisateur est l'uid 65534 ;
  - l'interpréteur est Python 3.13.17, avec pytest 9.1.1 ;
  - aucun fichier de `nobody` plus récent que mon début n'existe hors de mon dossier (`/tmp`, `/var/tmp`, `/home`,
    `/root`, `/mnt/user-data`, `/opt/venv…`), sans entrer dans `runs/`, `donnees/` ni `diag/`.

### 2.1. Résultats

| objet | exécution | résultat | journal |
|---|---|---|---|
| v6.2.1 | `-q` | **`68 passed in 5.21s`**, code 0 (5,41 s au mur) | `pytest-v621-v1.log` |
| v6.2.1 | `-v --durations=0`, copie à part | `68 passed in 5.29s`, code 0 | `pytest-v621-detail-v1.log` |
| témoin : `test_corrections_v5.py` (v6.2.1) sur une copie de `3bbb78c` | `-v` | **7 échecs, 8 réussites**, code 1 | `temoin-c5-sur-3bbb78c-v1.log` |
| témoin : `test_emprunts_v5_3.py` d'origine (`3bbb78c`) sur une copie de la v6.2.1 | `-v` | **1 échec, 4 réussites**, code 1 | `temoin-v53-origine-sur-v621-v1.log` |
| v6.2.1 : essai du point 6 lancé seul | `-q` | 1 échec (`ModuleNotFoundError: noyau_client`), comme en v6.2 | `pytest-v621-point06-seul-v1.log` |

- **Les 53 essais de la v6.2 sont tous présents et passent** (`essais-presents-53-v1.txt`, par comparaison au journal
  détaillé de la vérification v6.2).
- **Les 15 nouveaux** : 11 fonctions, dont une paramétrée sur 4 jeux.
- **Durées** : les plus longues sont `test_c06` (1,87 s) et `test_c05` (1,55 s) ; l'essai de V6-01 prend 0,09 s ;
  chaque essai nouveau prend 0,05 s au plus.

### 2.2. L'essai hérité adapté

**C'est bien le seul.** Les 8 autres fichiers d'essais hérités sont identiques octet pour octet. Dans `test_emprunts_v5_3.py`,
l'arbre syntaxique montre que seul cet essai change (et sa fonction interne `predire`) ; les 4 autres essais du fichier
sont inchangés.

**Le changement** (`diff-…test_emprunts_v5_3.py-v1.txt`) :
- **deux tâches d'entraînement ajoutées** (`tr_3`, `tr_4`, l. 77-80) ;
- **le faux `predire`** donne 0,94 à `tr_1` et `tr_3`, 0,06 à `tr_2` et `tr_4` (l. 57-59). `te_clair` et `te_ambigu`
  gardent 0,94 et 0,52, comme avant ;
- **une assertion remplacée** : `set(donnees) == {"tr_1", "tr_2"}` devient « 2 tâches entraînées, 2 tâches de
  validation, disjointes, dont l'union est `{tr_1…tr_4}` » (l. 98-101) ;
- **une assertion ajoutée** : l'exactitude de validation vaut 1,0 (l. 102).

`"viv_1" not in donnees` et les deux assertions de routage (l. 103-104) sont gardés tels quels.

**Limité à ce que C-15 exige** :
- sans pli de validation, la sonde ne vote plus. Il faut donc au moins 4 tâches hors vivier (`principal.py` l. 526) ;
- il faut aussi des probabilités de validation conformes : à 0,52 partout, l'exactitude serait de 0,5, sous le seuil de
  0,65 ;
- la partition entre entraînement et validation est faite par `_selection_stratifiee` ; l'ensemble exact ne peut donc
  plus être écrit d'avance.

**Pas affaibli** :
- l'ancienne égalité disait « toutes les tâches hors vivier, et elles seules, servent » ; la nouvelle dit la même chose
  pour l'entraînement et la validation réunis, et elle est plus stricte d'une assertion ;
- le routage est essayé comme avant, sur les mêmes probabilités de test.

**Comme en v6.2**, l'essai ne distingue pas laquelle des deux exactitudes la garde lit : 0,88 à l'entraînement et 1,0 à
la validation, toutes deux au-dessus de 0,65 (voir § 3.2).

### 2.3. Les témoins : ce qui échoue, et pourquoi

**`test_corrections_v5.py` sur la v6.2** : 7 échecs, comme annoncé.

| essai | cause de l'échec sur la v6.2 | l'artefact visé est-il montré ? |
|---|---|---|
| `test_c14_…sans_terme_redondant` | l'expression est `conf_c1 < seuil_c1 or len(castes) > 1` | oui (l'essai porte sur le texte, le comportement étant le même) |
| `test_c15_moins_de_4_taches…` | `exactitudes_validation` vaut `{conscience-evaluation: 0.99}`, le repli sur l'entraînement | oui |
| `test_c15_prediction_de_validation_non_ok…` | le même repli, à 0,99 | oui |
| `test_c16_mots_cles_une_seule_source…` | **les deux égalités de mots passent sur la v6.2** ; l'échec vient seulement de `AttributeError: _expression_mots_cles` | **non** : la v6.2 écrivait déjà les mêmes mots ; l'essai montre l'égalité, pas l'unicité de la source (celle-ci se lit dans le code, l. 1082-1083) |
| `test_c16_mot_cle_invalide…` | `AttributeError` : la fonction est nouvelle | sans objet |
| `test_c17_code_brut_refuse…` | l'espion de la validation est appelé : `rejet_validation: espion de l'essai` | oui |
| `test_c17_assemblage_refuse…import_ast` | **la v6.2 garde elle aussi le module d'origine** (« assemblage … invalide (RuntimeError) » : il manque au code de l'essai les fonctions requises) ; seul le message diffère | **non** : la garde des l. 1558-1562 est dans le code, mais l'essai ne montre pas que la v6.2 aurait assemblé un tel code. Par le gabarit, elle est d'ailleurs inatteignable (§ 3) |

Les 8 réussites sont celles qu'annonce `CORRECTIONS-v5.md` :
- C-14, délibération et une seule caste ;
- C-15, cas sain ;
- C-17, objet JSON entre accents graves et les 4 jeux de bornes.

**L'essai hérité d'origine sur la v6.2.1** : 1 échec, à l'assertion `te_clair … routage_sonde_accord_precoce is True`.
- Les assertions précédentes passent : 2 tâches, aucun pli, entraînement sur `{tr_1, tr_2}`.
- Faute d'exactitude de validation, la sonde ne vote plus : c'est exactement l'effet de C-15, de bout en bout jusqu'au
  routage.

## 3. Les points 3, 4, 5, 7, 9 et 10 de la vérification v6.2 (résultat 3)

Les lignes sont celles de la v6.2.1. Le critère est celui de la vérification v6.2 : un point est levé quand le fait
décrit n'est plus vrai du code ; un choix gardé sans raisons ne compte pas comme levé.

### 3.1. Verdicts

**Point 3 — arbitrage redondant dès deux castes : levé, avec un choix gardé et ses raisons.**
- **Constat** :
  - l. 1738 : sans sonde, `besoin_arbitrage = len(castes) > 1` ;
  - l. 1740 : `if besoin_arbitrage and len(castes) > 1` ;
  - `besoin_arbitrage` n'est lu nulle part ailleurs.
- **Le comportement est exactement le même**. En v6.2 on avait (A ou B) et B, qui vaut B, et la comparaison des réels
  `conf_c1 < seuil_c1` n'a aucun effet de bord.
- **Le choix gardé**, à savoir que sans sonde toutes les castes recrutées délibèrent, est désormais dit avec ses raisons,
  dans `CORRECTIONS-v5.md` C-14, dans le commentaire des l. 1734-1737 et dans `CONCEPTION.md` § 2.14.1 :
  - c'est le comportement de la v6.2 : je le constate ;
  - le changer changerait les appels et les décisions dès deux castes : je le constate à la lecture ;
  - c'est aussi celui de la v5.3 : non revérifié, la v5.3 étant hors de mes extractions.
- **`seuil_confiance_caste1`** ne sert plus au routage qu'avec une sonde (l. 1724 et 1732).
- **Preuves** :
  - essais `test_c14_*` ;
  - relevés B et D identiques à ceux de `3bbb78c` (§ 4.2).
- **À trancher** : que l'arbitrage sans sonde dépende ou non de la confiance est une question de conception, que Lazar
  tranche.

**Point 4 — repli silencieux sur l'exactitude d'entraînement : levé.**
- **Constat** :
  - l. 611-619 : l'exactitude de validation n'est inscrite que si elle a été calculée ; sinon, aucune valeur n'est
    inscrite et la raison est consignée, que le pli manque ou que la prédiction ne soit pas exploitable (l. 617-619 ;
    `taches_val` est défini dans les deux branches, l. 526-536) ;
  - l. 1986 : le routage ne lit plus que `exactitudes_validation`, sans repli sur `exactitudes` ;
  - une famille absente garde `acc_sonde = 0.0` (l. 1677), sous tout seuil admis (au moins 0,05, l. 1624), et donc ne
    vote pas (l. 1686).
- **Preuves** :
  - essais `test_c15_*`, dont les deux qui portent l'artefact échouent sur la v6.2 ;
  - le témoin d'origine (§ 2.3), qui montre l'absence de vote dans le routage.

**Point 5 — trois jeux de mots-clés : levé, avec une copie gardée et ses raisons.**
- **Une seule source à l'exécution** pour la mémoire et le gabarit : `memoire_isvd.py` l. 81-82, lus l. 87-88, et
  importés par `principal.py` l. 14-15.
- **Le gabarit écrit son expression depuis cette source** : `_expression_mots_cles`, l. 967-975, appelée l. 1082-1083.
- **Même texte qu'en v6.2, octet pour octet** : les modules mutés que les essais écrivent ont les mêmes sha256 sous
  `3bbb78c` et sous `7ea3270` (`11ca1a56…` et `47967ec7…`, `successeurs-mutes-v62-vs-v621-v1.txt`).
- **Ce qui reste** :
  - le module initial `politique_endogene.py`, inchangé, garde sa copie en toutes lettres (l. 38-39) et ses constantes
    (l. 9-10, qui n'y servent pas) ;
  - leur égalité à la source est tenue **par deux essais**, pas par construction : `test_c16_…une_seule_source` pour
    l. 38-39, `test_v6_2_point_05` pour l. 9-10 ;
  - la raison est dite : le module réécrit ne peut importer que `math`.
- **La détection reste faite sur les mots du texte**, choix gardé avec ses raisons : c'est une propriété du texte.

**Point 7 — validation sans borne de temps, coût d'une opération non borné : levé, par la fermeture de la voie.**
- **La voie du code brut est retirée** (l. 1030-1035). Un bloc de code définissant `recompense_interne` est refusé et
  consigné, sans validation ni exécution.
- **Seul le gabarit atteint la validation** :
  - `code_candidat` n'a plus que deux affectations, `None` (l. 1025) et le gabarit (l. 1048) ;
  - la validation n'a qu'un appel, l. 1102 ;
  - `exec` et `compile` ne figurent qu'à `politique_endogene.py` l. 226-227.
- **Le gabarit est borné** :
  - sa forme est fixe ;
  - ses paramètres sont ramenés dans leurs bornes : α dans [1,15 ; 1,85], Brier dans [0,60 ; 0,95], seuil dans
    [0,72 ; 0,85] (l. 1044-1046) ;
  - le nom est réduit à `[A-Za-z0-9_]`, 60 caractères au plus (l. 1043).
- **La validation tient donc en temps borné** : quatre jeux, aux bornes et au-delà, chacun moins de 0,05 s.
- **Mais le validateur lui-même n'a pas changé** (`politique_endogene.py` est identique) : pas de borne de temps, et le
  filtre statique laisse toujours passer les candidats lourds de ma transcription v6.2. Une voie rouverte ramènerait le
  défaut.

**Point 9 — propreté : règle impropre entre les points lus : levé, par la même fermeture.**
- **Seules les règles du gabarit peuvent être validées.** Elles sont propres par construction : un mélange à poids
  positifs de Brier et de la divergence de Bregman de Tsallis normalisée, avec φ(0) = φ(1) = 0 et φ convexe pour α > 1.
- **Elles sont acceptées sur toute la plage** : 120 sur 120 d'après ma transcription v6.2. Celle-ci vaut ici, le
  contrôle et le texte du gabarit étant identiques.
- **Mais le contrôle n'a pas changé** : il accepterait toujours la règle à bonus caché si on la lui donnait.

**Point 10 — ce que la liste blanche ne garantit pas : levé, hors la part inhérente.**
- **Coût** : voir le point 7.
- **Séparateur dans une chaîne** :
  - le gabarit ne peut pas porter `import ast`, son nom étant réduit à `[A-Za-z0-9_]` ;
  - l'assemblage refuse en plus tout code muté qui le porte (l. 1558-1562) : c'est une défense en profondeur,
    inatteignable par le gabarit, et son essai ne la distingue pas de la v6.2 (§ 2.3) ;
  - la coupe se fait donc toujours au vrai séparateur (l. 1565-1567).
- **Reste, comme en v6.2** : le successeur s'importe avec toutes les fonctions intégrées. C'est inhérent, mais son code
  est désormais le gabarit, plus le bloc du vérificateur.

**Les 7 points déjà levés en v6.2 le restent.**
- **1** : `CONCEPTION.md` n'a reçu qu'un ajout. Les relevés B et D gardent les appels, les réponses et la mémoire de
  `3bbb78c`, eux-mêmes égaux à ceux de la v6.1 et de la v5.2.1.
- **2** : le seuil de 0,65 est lu l. 1665 et appliqué l. 1686 ; la marge de 0,10 l'est l. 1689.
- **6** : le paramètre `erreurs` est à la l. 468, `_noter_err` aux l. 470-473, et `executer` le passe l. 1907. L'essai
  reste fragile lancé seul, comme en v6.2.
- **8** : l. 1039-1042, et `_lire_seuil_verifie` l. 1619-1627.
- **11** : 0 marque d'ordre d'octets et 0 caractère de contrôle autre que le saut de ligne, sur les 26 fichiers
  (`c01-octets-7ea3270-v1.txt`).
- **12** : le fichier d'essais est identique.
- **13** : l. 2122-2126.

### 3.2. Effets ou écarts que `CORRECTIONS-v5.md` ne dit pas (non bloquants)

1. **Le volet « routage » de C-15 n'est gardé par aucun essai de la suite.** D'après ma lecture des essais (je ne l'ai pas
   exécuté), si l'on remettait le repli de la l. 1986, tous passeraient encore :
   - `test_c15_*` ne regardent que `exactitudes_validation` et le message, pas les votes ;
   - l'essai adapté a un pli de validation.

   Seul le témoin ponctuel (§ 2.3) le montre.
2. **Commentaire faux dans `test_corrections_v5.py`.** Il dit, l. 76, « C-14 : sans sonde, l'arbitrage n'a lieu que si la
   caste 1 doute ». Or C-14 et l'essai qui suit (l. 114-117) établissent le contraire.
3. **Le refus de C-16 est une exception.** `_expression_mots_cles` refuse par `ValueError`, qui n'est pas rattrapée
   dans `_synthetiser_mutation_politique_endogene`. Si cela arrivait, l'exception remonterait à l'`except` d'`executer`
   (l. 2041, « exécution interrompue »), et le journal dirait `non_declenchee`. C'est inatteignable avec les constantes
   actuelles.
4. **L'exactitude d'entraînement reste rapportée**, sans servir au routage :
   - dans `sondes_traits.exactitudes`, ce que dit `CONCEPTION.md` § 2.14.2 ;
   - mais aussi dans le journal d'ablations de la mémoire, sous `exactitude_sonde_observee` (`principal.py`
     l. 2060-2075, `memoire_isvd.py` l. 162), et dans `exactitude_moyenne_sonde` de `fin_conception.json` (l. 2113) ;
   - or la consigne de l'architecte montre les deux dernières ablations (l. 1007).

   C'était déjà le cas en v6.2.
5. **Une réponse qui porte à la fois un objet JSON et un bloc de code définissant `recompense_interne` est refusée en
   entier** : l'objet JSON n'est pas repris. En v6.2, le bloc de code passait déjà en premier.

## 4. V6-01, reproductibilité, verrous, gardes, contrat (résultat 4)

### 4.1. V6-01 reste corrigé

L'essai en processus neuf passe. Journaux qu'il écrit (`v6-01-et-noms-non-lies-7ea3270-v1.txt`) :
- **génération 1** : mutation acceptée (`validation_stricte_ok`), 0 erreur, 3 appels dont 1 d'architecte ;
- **génération 2**, dans un processus neuf, avec le successeur muté (`NOM_POLITIQUE = bregman_mutee_gen2`) : 0 erreur,
  2 appels, 1 tâche répondue.

C'est ce que donnait la v6.2. **Aucun nom non lié** :
- dans les 45 modules `politique_endogene.py` que les essais écrivent ;
- dans l'original (`8e8b58ea…`) ;
- dans `principal.py`.

### 4.2. Reproductibilité : cas B et D, graines 0, 1 et 2

L'outil est `invariance_v1.py` (`1fe2609c…`, conforme). Journal : `invariance-7ea3270-v1.log`.

| cas | appels | `budget()` / `especes()` | recherches / téléchargements | sha256 des relevés |
|---|---|---|---|---|
| B | 28 | 46 / 1 | 0 / 0 | `c4c492ed…`, identique pour les trois graines |
| D | 29 | 53 / 1 | 2 / 1 | `54c56fdf…` pour les graines 0 et 2, et pour la graine 1 relancée |

- **Graine 1, premier lancement** : il a donné `91cfed25…`. La seule différence est `temps_s` (0,1 → 0,2 s), une mesure
  d'horloge (`diff-journal-D-s0-vers-s1-7ea3270-v1.txt`). Relancé, il redonne `54c56fdf…`. Ce n'est donc pas un effet de
  la graine de hachage.
- **Comparaison aux relevés de `3bbb78c`** (`comparaison-invariance-3bbb78c-vers-7ea3270-v1.txt`,
  `diff-journaux-3bbb78c-vers-7ea3270-v1.txt`) :
  - **mêmes appels**, dans le même ordre ;
  - **mêmes rôles, espèces et plafonds** ;
  - **même empreinte** pour chaque consigne ;
  - **identiques** : `memoire_isvd.json`, `metrique_proposee.json`, `reponses_test.json` et `reponse-question.md` ;
  - **le journal de génération** ne diffère que par `version` et `temps_s` (0,0 → 0,2 en B, 0,0 → 0,1 en D).
  - Les sha256 des relevés diffèrent donc de `139c9036…` et `423c5a3f…` par ces deux champs seulement.

### 4.3. Verrous, gardes, contrat

- **Verrous** (`verrous-7ea3270-v1.txt`) :
  - 0 appel imbriqué, avec l'outil des appels directs comme avec celui des chaînes d'appels internes ;
  - aucun `acquire` ni `release` explicite ;
  - les mêmes six fonctions qu'en v6.2 prennent `_VERROU`, et `_expression_mots_cles` ne le prend pas ;
  - les trois autres modules ne le prennent jamais.
- **Gardes C-01 à C-13** :
  - les 13 essais `test_c01` à `test_c13` passent ;
  - les fonctions qui les portent sont inchangées par l'arbre syntaxique : `_parser_decision_tache`,
    `_extraire_json_candidat`, `_selection_stratifiee`, `_faut_basculer`, `_confiance_finie`,
    `_sanitiser_donnee_externe` et `_bloc_moisson_borne`, ainsi que les constantes d'ouverture et de fermeture (l. 28-29) ;
  - `memoire_isvd.py` et `metrique/` sont identiques ;
  - **C-03** : `_traiter_tache` change par C-14 seulement ; les étiquettes sont toujours lues dans chaque tâche (l. 1644) ;
  - **C-05** : `executer` change par C-15 seulement. Le `try` est l. 1867, l'`except` l. 2041 et le `finally` l. 2043.
    La mutation est appelée dans le `try` (l. 2030), et le `finally` écrit mémoire, métrique, journal et successeur.
- **Contrat du noyau** (`motifs-contrat-3bbb78c-vers-7ea3270-v1.txt`) :
  - les comptes de motifs sont identiques dans chaque fichier, et les mots interdits ne paraissent que dans la liste de
    `politique_endogene.py` ;
  - `exec` et `compile` ne figurent qu'aux l. 226-227 de ce fichier ;
  - les lectures et écritures sont les mêmes, aux lignes décalées, et toutes se font sous `dossier_travail` ;
  - `subprocess` ne sert que dans l'essai de V6-01 (l. 4 et 160).

## 5. Sous la configuration du pilote 4 (résultat 5)

C'est une lecture du code, sans exécution hors des essais. La configuration : 6 rondes de conception au plus à 3 USD,
puis 4 générations notées, `--appels-max 160`, 120 tâches servies, ni trait ni entraînement.

- **Castes par tâche en génération notée : 1.** Dans `mitose_spectrale.py` (identique) :
  - la réserve vaut min(6, max(1, 160 // 4)) = 6 (l. 68) ;
  - `budget_par_tache` vaut (160 − 6) // 120 = 1 (l. 69-70) ;
  - donc `nb_castes_cible` vaut 1 (l. 78).

  Avec une seule caste, il n'y a pas d'arbitrage (l. 1740), et C-14 ne change rien. Même à plusieurs castes, en
  conception par exemple, C-14 est exactement équivalent.
- **Sans traits, `_entrainer_et_predire_sondes_traits` n'est même pas appelée** (l. 1901), et C-15 est sans effet.
- **C-16 écrit des successeurs identiques octet pour octet** (§ 3.1, point 5).
- **Appels par génération notée** : 1 induction, 2 vérifications (`N_VERIFICATIONS`, l. 31) et 120 tâches, soit 123,
  plus 1 appel d'architecte sous stagnation (l. 991-998), soit 124. C'est la même suite qu'en v6.2.
- **Appels par ronde de conception** : 1 induction et 4 vérifications (l. 1932), les tâches selon les castes planifiées
  (même fonction), 1 architecte, et la moisson si elle est ouverte. C'est la même suite qu'en v6.2.
- **Non vérifié** : les « 123 appels en simulation » de `CORRECTIONS-v5.md`. Je n'ai pas lu ces journaux ; le chiffre
  est cohérent avec la lecture.
- **La mutation est tentée comme en v6.2** :
  - en conception à chaque ronde, en génération sous stagnation (l. 997, puis `_peut_appeler` l. 1000) ;
  - la consigne est inchangée et demande « un objet JSON strict sur une ligne » (l. 1008-1011).
- **Elle est acceptée comme en v6.2** pour un objet JSON complet : même gabarit, même validation, mêmes successeurs.
  **Une seule différence** : si l'architecte répondait par un bloc de code définissant `recompense_interne`, la v6.2 le
  validait, et pouvait l'accepter, alors que la v6.2.1 le refuse. Le nombre d'appels ne change pas. Mais le successeur
  garderait sa règle, ce qui changerait, à la ronde suivante, le score interne, et donc la fin de conception.
- **Le critère de fin de conception est inchangé** : l. 2101-2106, même texte que dans `3bbb78c` l. 2063-2068.

## 6. Lignes que cite le préenregistrement du pilote 4 (résultat 6)

Journal : `lignes-preenregistrement-pilote4-3bbb78c-vers-7ea3270-v1.txt`. La correspondance est faite ligne à ligne, par
blocs égaux. **Toutes ces lignes ont le même texte**, à leur nouvelle place :

| citation (`3bbb78c`) | v6.2.1 | texte |
|---|---|---|
| `principal.py` l. 2063-2068, fin de conception | **l. 2101-2106** | identique |
| l. 970-977, mutation et stagnation | **l. 991-998** | identique |
| l. 2005, `finally`, puis l. 2028, mémoire | **l. 2043, puis 2066** (bloc l. 2005-2038 = l. 2043-2076 ; pondération l. 2039 = l. 2077) | identique |
| l. 784, exemple de format | **l. 794** (bloc l. 777-785 = l. 787-795) | identique |
| l. 87-96, requêtes de réserve | **l. 89-98** | identiques |
| `memoire_isvd.py` l. 240-248, 118-121, 129-131 | **mêmes lignes** (fichier identique) | identique |
| `mitose_spectrale.py` l. 75 et 117 | **mêmes lignes** (fichier identique) | identique |

**Une seule précision de comportement** : la mutation de la l. 997 refuse désormais une réponse en code brut (l. 1030-1035).
La pondération reçue par la mémoire (l. 2077) a le même texte qu'en v6.2, tant pour le module initial que pour les modules
du gabarit.

## 7. Réserves de cette vérification

1. **Ce qui repose sur des transcriptions.**
   - **Ma transcription v6.2** : l'acceptation de toute la plage du gabarit et la persistance des candidats lourds et de
     la règle à bonus caché dans les fonctions de contrôle. Elle vaut ici parce que `politique_endogene.py` et le texte
     du gabarit sont identiques, mais je ne l'ai pas relancée.
   - **L'empreinte d'arbre** : transcription reprise de la vérification v6.2.
2. **Ce qui vient de la lecture seule.** Le comportement sous le pilote 4 : je n'ai relu ni le noyau ni la configuration
   du lanceur.
3. **Ce qui n'est pas revérifié** : la parenté des commits et la tête de branche ; la v5.3 citée par C-14 ; les journaux
   de la lignée conv-audit (`/var/tmp/essais-v621-conv-audit-v1/`), que je n'ai pas lus.
4. **Écart d'écriture** : deux fichiers transitoires hors de mon dossier, effacés (en tête).

Je n'ai rien préparé d'autre. La suite est ta décision.

## 8. Contenu de ce dossier

- **Ce rapport et ses empreintes** : `LISEZMOI-v1.md` ; `EMPREINTES-v1.txt` donne le sha256 de chaque pièce. Contrôle :
  `sha256sum -c EMPREINTES-v1.txt` depuis ce dossier.
- **`verification-v1/`** : journaux d'essais, de témoins, d'invariance et d'isolation, relevés, différences,
  inventaires, analyses.
- **`outils-v1/`** :
  - **repris et conformes** : `empreinte_arbre_v1.py`, `comparer_releves_v1.py`, `diff_json_v1.py`,
    `filtre_statique_v62_transcrit_v1.py`, `proprete_regles_v4.py`, `assembler_successeur_v1.py`,
    `noms_non_lies_v1.py`, `fonctions_ast_v1.py`, `verrous_transitifs_v1.py` et `verrous_imbriques_v1.py` ;
  - **nouveaux** : `lancer_isole_v1.sh`, `sonde_isolation_v1.py`, `lire_journaux_v1.py`, `motifs_contrat_v1.py` et
    `lignes_citees_v1.py`.
- **Hors du zip**, empreintes dans `EMPREINTES-v1.txt` :
  - `archives-v1/` : les deux archives ;
  - `extraction-*` : les arbres extraits ;
  - `temoins-v1/` : les deux arbres témoins ;
  - `essais-v1/` : les copies d'essai, propriété de `nobody`.
- **`livrable-verification-v621-poussee-v1.zip`** : `LISEZMOI-v1.md`, `EMPREINTES-v1.txt`, `verification-v1/` et
  `outils-v1/`.

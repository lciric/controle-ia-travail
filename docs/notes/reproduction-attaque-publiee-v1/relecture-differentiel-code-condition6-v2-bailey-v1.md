# Relecture en différentiel du code de la condition 6 (v1 → v2) et de la garde de fin de run (`analyse_v3`) — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les deux rapports
  relus. Date : `date -u` = Tue Nov 10 12:18:23 UTC 2026 (début), 12:27:22 UTC (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `08cc4c63`, arbre de
  travail propre avant ce rapport (`git status`).
- Pièces relues, avec leur empreinte (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), en entier ;
  - `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-code-condition6-bailey-v1.md` (`90af7dea7c87f800d84f5dc380c0b46687429cd613dfeb6aaee0b7e718010c31`), en entier ;
  - `docs/notes/reproduction-attaque-publiee-v1/relecture-differentiel-analyse-v2-bailey-v1.md` (`8895a5a7ad497e7bbb6c566d1c89ea9ac3afdedaa039d8c6bda620d26e679889`), en entier ;
  - `diff -u` v1 → v2 de `src/controle_ia/temoin_bailey/` : `conventions_v2.py` (`5a070219…`), `journaliseur_v2.py`
    (`84396bcd…`), `execution_v2.py` (`05022c4e…`), lus en entier ; `instance_v2.py` (`406451af…`), `lecture_v2.py`
    (`4a64ecb5…`), `lanceur_v2.py` (`848c088f…`), lus en entier (réécritures trop larges pour le seul différentiel) ;
  - `analyse_v2.py` (`5dad0bd0…`) → `analyse_v3.py` (`c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca`) : différentiel, et `validite`, `verdict`, `garde_fin_de_run` en entier ;
  - essais : `tests/test_temoin_bailey_condition6_v2.py` (`d44e29bd…`), en entier ; `tests/test_temoin_bailey_analyse_v3.py`
    (`8cca01f1…`), section « fin de run » en entier, le reste par la liste des essais ;
  - devis v4 (`f9c8c66e…`) : la seule ligne « Mémoire vive de l'hôte » (grep) ; `src/controle_ia/scellement.py` : liste
    des fonctions (grep) ;
  - code public des auteurs, hors dépôt, lecture seule, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` :
    `train_harmful.py` l. 150-185, `evaluate.py` l. 235-250, 550-575, 820-845, `obf_reps/optimize/loss.py`
    l. 130-145, 200-210, 395-405, `obf_reps/logging/__init__.py` l. 40-80, 155-163, `obf_reps/models/hf.py`
    l. 169-175, 535-545, `obf_reps/models/llama3.py` l. 8, `obf_reps/utils.py` l. 124, 220-232, grep des appels
    `logger.log` ; paquet du juge, commit `7a551d5b440ec7b75d4f6f5bb7c1719965b76b47` : `strong_reject/evaluate.py`
    l. 110-140, 425-500.
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`,
  `registres/` en entier (dont `etat.md` et `decisions.md`), tout résultat, note ou seuil de sonde ou de moniteur du
  programme, tout résultat d'attaque contre le juge de l'organisme ; le reste du devis v4 ; les modules v1 hors
  différentiel ; `analyse_v3.py` hors des fonctions nommées (les points D-3 à D-11 n'ont pas été relus point par point :
  hors demande).
- Outils : `sha256sum`, `git`, `diff -u`, `grep`, `sed` ; essais demandés (`TEMOIN_BAILEY_CLONE=… PYTHONPATH=src python -m
  pytest -q tests/test_temoin_bailey_condition6_v2.py tests/test_temoin_bailey_analyse_v3.py`) : **76 passés** ; trois
  sondes du lecteur dans `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v2/` :
  `sonde_conduite.py` (`1454638e…`), `sonde_lecture.py` (`5f690c3d…`), `sonde_mep.py` (`aab172cf…`), qui appellent les
  modules et réemploient les aides de l'essai (`FournisseurFactice`, `fabriquer`, `jouer`) sans rien modifier. Un essai
  d'import de `obf_reps.models.llama3` sur le clone a échoué faute de `joblib` dans l'environnement : B-1 vérifié par
  lecture seulement. Aucune requête réseau, aucun appel à `vastai`, aucune dépense, rien de committé. Rapport non scellé.

Renvois : « I l. n » = `instance_v2.py` ; « La l. n » = `lanceur_v2.py` ; « J l. n » = `journaliseur_v2.py` ;
« Le l. n » = `lecture_v2.py` ; « C l. n » = `conventions_v2.py` ; « X l. n » = `execution_v2.py` ; « A3 l. n » =
`analyse_v3.py` ; « E l. n » = `tests/test_temoin_bailey_condition6_v2.py` ; « texte l. n » = le préenregistrement.

## Verdict

**Conforme après corrections.** La v2 applique pour l'essentiel la contre-lecture `90af7dea` sur l'instance et dans le
journaliseur (B-1, B-2, B-3, B-4, B-7, B-8, A-1, A-2, A-10 corrigés ; essais de bout en bout sur les colonnes réelles),
et la garde de fin de run d'`analyse_v3` corrige D-1 et D-2 avec leurs essais. Mais la pièce neuve, la **conduite**
(`lanceur_v2.Conduite`), contredit la liste d'arrêt en quatre points démontrés (reprise après « sonde orientée »
tombée ; relance jamais lancée sur une erreur technique ; aucune relance après une garde de démarrage ; instance jamais
détruite si un transfert échoue), compte D sans les instances antérieures du poste et laisse vivre l'instance après
l'échéance du GO ; et la **validité calculée sans note** (`lecture_v2.valider`) rend la garde de fin de run en partie
tautologique (K′ « déclaré » tiré du journal même ; aucune empreinte prise sur les fichiers lus). Un écart de rangement
neuf fait sortir de l'instance, dans le journal dit « sans note », la note moyenne de la sonde à chaque pas
(`obf_loss`). Décompte : contre-lecture `90af7dea` : 11 corrigés (deux avec réserve), 14 en partie, 3 non corrigés (dont P-1 renvoyé à
l'addendum) sur 28 points ; essais manquants : 8 corrigés, 4 en partie ; D-1 et D-2 corrigés. Défauts neufs : 7 bloquants,
8 à corriger, 6 à préciser. Corrections exactes en section 4 ; après elles, relire en différentiel la conduite,
`valider` et leurs essais. **L'addendum ne peut pas être scellé avant** ces corrections, cette relecture et le mot de
Lazar sur la lecture de la ligne « B − 2 » (section 3).

## 1. Points des deux rapports

### Contre-lecture `90af7dea`

| Point | État | Lignes v2 | Constat |
|---|---|---|---|
| B-1 import | corrigé | I l. 222-224 | `obf_reps.models.llama3` définit la classe (pub `llama3.py` l. 8) ; `validate_and_create_model_config` existe (pub `utils.py` l. 124). Import non éprouvé : l'essai passe `generer` (E l. 476-477). |
| B-2 sortie d'erreur | corrigé | I l. 369-371 ; E l. 395-401 | fichier propre resté sur l'instance ; avertissement avant la configuration : garde passée. |
| B-3 juge par lots | corrigé | I l. 207-208, 231-249 ; E l. 462-487 | lots de `eval_batch_size` (16) pour la génération et le juge ; garde après le premier appel. |
| B-4 adaptateur | corrigé, réserve | C l. 55-59 ; J l. 91-131 ; I l. 135-143, 175-177 ; La l. 214-236 ; E l. 302-332 | (a) établi le 10 novembre (base `google/gemma-2b`) ; (b) trois téléchargements à révision, `refs/main` posé ; (c) révisions de l'adaptateur et de la base lues dans le cache, type numérique, tokeniseur. Réserve : `peft` n'est exigé nulle part (`versions` peut être vide, N-9) ; la présence d'un tokeniseur dans le dépôt de l'adaptateur n'est pas vérifiée (P-c). |
| B-5 B − 2, transfert avant destruction | **en partie** | I l. 390-401 ; La l. 178-209, 378-387 | séquence arrêt sur l'instance → empreintes → transfert → destruction codée. Mais : un transfert qui lève empêche la destruction (N-4) ; l'arrêt à l'échéance et le secours (+ 1 800 s) laissent l'instance vivre après l'échéance du GO (N-5) ; le veilleur est un fil « démon » du même processus, qui meurt avec lui ; seuil de secours B − 0,5 à faire confirmer (section 3). |
| B-6 ce qui sort | corrigé, réserve | C l. 66-76 ; La l. 255-269, 389-410 ; E l. 548-557 | fichier par fichier, liste fermée, refus d'un chemin hors liste. Réserves : les fichiers d'état (mise en place, contrôle du juge, règle) sortent sans comparaison d'empreinte (La l. 399-405, N-12) ; `obf_loss` sort dans le journal technique (N-7). |
| B-7 ligne « MARK » coupée | corrigé | I l. 276-303 ; E l. 352-368 | tampon de ligne ; décodage après assemblage. |
| B-8 K et graine au manifeste | corrigé | I l. 306-327, 353-357 ; E l. 371-389 | K et graine lus au manifeste par phase ; la graine comparée au texte ; le K du texte observé égale celui du manifeste par l'égalité des empreintes (texte attendu construit sur le K du manifeste). |
| A-1 mémoire vive | **en partie** | I l. 87-99 ; E l. 427-431 | tolérance retirée, mais l'unité est le Gio sans le dire : un hôte de 134 Go décimaux tombe (N-10) ; `/proc/meminfo` d'un conteneur donne la mémoire de l'hôte, pas la limite allouée. |
| A-2 commits des paquets | **en partie** | I l. 116-132, 174 | garde présente ; mais `manifeste.get("git", {})` vide passe, et `strong_reject` = `JUGE_COMMIT_PAQUET` n'est pas exigé (N-9). |
| A-3 journal sans note | **en partie** | J l. 189-198 | notes et technique séparés ; mais `behavior_loss` et `obf_loss`, à chaque pas, vont au journal technique (N-7). |
| A-4 état écrit avant de lever | **en partie** | J l. 175-187, 207-211, 250-251 ; X l. 63-65 | « table », « suffixe au journal », « suite des étiquettes » : corrigés et éprouvés (E l. 262-299). « Dossier neuf » (J l. 151-152) et `TESTING` dans l'enfant (X l. 63-65) n'écrivent que sur la sortie d'erreur, qui reste sur l'instance. |
| A-5 fin de run branchée | **en partie** | Le l. 78-95 | branchée ; mais K′ déclaré = K′ du journal, aucune empreinte prise sur les fichiers lus (N-6). |
| A-6 journal absent | corrigé | Le l. 31-35 ; E l. 231-233 | lève. `instance_v2.empreintes` (I l. 434-437) omet en silence un journal absent ; la garde de fin de run le rattrape (ensemble des noms exigé, A3 l. 429). |
| A-7 manifeste | **en partie** | La l. 133-149, 338-340, 362-363, 372-373 | écrit avant l'instance ; complété **sur l'instance seulement** (pas, longueur, règle), puis détruit avec elle ; à la relance, K et D sont écrasés (R12) ; le manifeste local reste sans B R D c t H K. |
| A-8 conduite | **en partie** | La l. 280-387 | codée, une reprise et une relance au plus ; défauts N-1 à N-5 ; aucun scellement des notes du pilote ni de la première exécution (N-8). |
| A-9 une ligne d'état | **en partie** | I l. 55-57 ; La l. 74-78, 247-252 | seule la ligne `ETAT` est gardée ; la sortie standard entière des commandes distantes (chargement des modèles au contrôle du juge, `pip` à l'amorce) revient pourtant au poste local en mémoire. Aucun texte du modèle n'y est imprimé au commit public (vérifié : pub `hf.py`, `evaluate.py`), d'où « en partie » seulement. |
| A-10 taille stable | corrigé | I l. 330-342, 412 ; E l. 414-424 | |
| A-11 K′ et validité depuis les journaux | **en partie** | Le l. 40-95, 150-153 | K′ calculé ; `mise_en_place`, `controles_juge_tenus`, `pilote_seconde_chute`, `relance`, scellements : toujours reçus de l'appelant ; « sonde orientée » du pilote non lue ; mémoire vive au pic non rapportée. |
| P-1 appariement sur `beh_target` | non corrigé (addendum) | J l. 239 | inchangé ; à déclarer à l'addendum, qui n'existe pas encore. |
| P-2 pas calculés | corrigé | C l. 84-87 ; I l. 159-163 ; E l. 456 | 1 600 retrouvés sur le clone. |
| P-3 échéance, révocation | **en partie** | La l. 109-119 | lecture « 23:59:59 UTC » écrite ; aucune vérification de révocation du GO cité. |
| P-4 rejeu des gardes | non corrigé | Le l. 177-211 | la docstring annonce le rejeu de l'appariement, que le code ne fait pas ; longueur du suffixe et dépense non rejouées ; « lequel fait foi » (empreintes de valeurs ou de fichiers) non dit. Les étiquettes de comportement sont fabriquées, non lues (Le l. 187 ; N-6). |
| P-5 ordre mise en place → juge | **en partie** | La l. 334-344 | imposé par la conduite ; `controle_juge` ne vérifie pas l'état de la mise en place. |
| P-6 t choisi par le code | corrigé | La l. 353-358 | `--pilote` subsiste en ligne de commande (I l. 449), sans effet dans la conduite. |
| P-7 GO vu par la garde | **en partie** | La l. 309-313 | `GO_ID` et ligne de GO relus ; la création passe toujours par `subprocess`, hors de `garde_calcul.py`. |
| P-8 replis silencieux | non corrigé | Le l. 147-148, 153 ; J l. 70-78 | mémoire de carte absente → 0 ; attaques passées de taille ≠ 200 retirées sans mention ; `_memoire` avale toute erreur ; la question « les pertes sont-elles des notes ? » est tranchée sans le dire, dans le mauvais journal (N-7). |
| P-9 jeton d'accès | **en partie** | La l. 55-60, 214-222 | jeton par l'environnement de l'instance, passé en ligne de commande à `vastai` (`--env`), visible dans la table des processus du poste ; l'amorce clone `lciric/controle-ia-travail`, privé, sans aucun accès prévu (N-13). |

Essais manquants de `90af7dea` : (1) dépôt public : **en partie** (cas sain sur le clone et « pas un dépôt »,
E l. 448-459 ; artefacts commit, arbre, fichier suivi modifié absents) ; (2) juge adaptateur : corrigé (E l. 302-332) ;
(3) suffixe absent, longueur : corrigé ; (4) 199 notes, 199 lignes : corrigé (`juge_199`) ; (5) « MARK » coupée,
avertissement : corrigé ; (6) `configuration_attendue` contre un vrai `@hydra.main` : **en partie** (composition sur le
clone, E l. 457-459, pas de comparaison à la sortie d'un `@hydra.main`) ; (7) contrôle du juge : **en partie** (lots
éprouvés, import non) ; (8) fin de run branchée, transfert, veilleur : corrigé (E l. 214-229, 531-557) ; (9) audit : corrigé
(E l. 236-259) ; (10) `lire_jsonl` : corrigé ; (11) exclusion retirée : corrigé (E l. 297-299) ; (12) faux déroulé :
**en partie** (11 et 23 colonnes réelles ; mais ni `behavior_loss`/`obf_loss` à chaque pas, ni `log_table_name`, ni
`concept_dataset_*` : leur absence a caché N-7).

### Relecture `8895a5a7`, garde de fin de run

| Point | État | Lignes | Constat |
|---|---|---|---|
| D-1 étiquettes par tour | corrigé | A3 l. 418-426 ; essais v3 l. 231-247 | fonction du tour exigée (`callable`) ; sain sur `etiquettes_attendues` du paquet à 3 tours ; artefact « étiquettes du tour 0 au tour 1 » tombe. |
| D-2 (a) K′ ≥ 1 | corrigé | A3 l. 414-415 ; essais l. 262-263 | |
| D-2 (b) étiquettes non vides | corrigé | A3 l. 425 ; essais l. 264-267 | |
| D-2 (c) relance explicite, `is True` | corrigé | A3 l. 418-419, 435-438 ; essais l. 252-261 | |
| D-2 (d) clé manquante | corrigé | A3 l. 420-428 ; essais l. 268-271 | `KeyError` → `GardeArret`. |

La garde elle-même est juste. Ce qui la vide en partie est son appel (N-6) : `valider` lui passe comme K′ « déclaré » le
K′ qu'il vient de tirer du même journal, des étiquettes de comportement fabriquées, et des empreintes « transférées »
fournies par l'appelant sans réempreinter les fichiers qu'il lit.

## 2. Défauts neufs de la v2 (sondes du lecteur)

**N-1 (bloquant). La conduite reprend le pilote après la chute de « sonde orientée ».** Texte l. 245-246 et liste d'arrêt
l. 366 : « Sonde orientée tombée au pilote : arrêt, “non interprétable”, pas de run principal. » La l. 346-351 : toute
exécution du pilote qui ne finit pas ses 3 tours déclenche `pilote-reprise`, sans lire l'état des gardes. Sonde S1 : un
pilote qui s'arrête au tour 0 (code de retour 1, aucune ligne « MARK ») → 2 commandes de pilote lancées. `valider`
(Le l. 83-84) ne lit d'ailleurs que les gardes du run qui porte le verdict, jamais celles du pilote.

**N-2 (bloquant). La relance n'a jamais lieu sur une erreur technique, ni après une garde de démarrage.** Liste d'arrêt
l. 371. La l. 367 teste `principal["code"]`, code de sortie de la commande distante ; or `instance_v2.main` rend 0 dès
que `executer` revient (I l. 465-469, 481), quel que soit `code_retour` de l'enfant. Sondes : L6 (enfant en échec,
`code_retour` = 1 → commande distante 0) ; S2 (crash au tour 5 → aucune relance) ; S2b (la relance ne part que si la
commande distante elle-même échoue) ; S3 (`cause_arret` = « garde de démarrage » → aucune relance, alors que le texte en
permet une). Corrigé naïvement (lire `code_retour`), le test relancerait aussi après « sonde orientée » (code non nul,
0 tour), ce que le texte interdit (table des critères, l. 334 et 338 : « non interprétable », toute reprise par version
nouvelle).

**N-3 (bloquant). D ignore les instances antérieures du poste.** Texte l. 252-254 : D « toutes instances comprises » ;
B fixé « à la création de la première instance du poste ». `Conduite` (sonde S5 : aucun champ pour elles) crée un
`Poste` vide (La l. 314) ; `d_avant` vaut 0 à l'instance (garde de dépense, I l. 390 ; J l. 134-136), dans la règle
(I l. 472) et pour le veilleur. Une mise en place refaite sur une nouvelle instance (permise, texte l. 336 et 364)
sous-compte D d'autant.

**N-4 (bloquant). Un transfert qui échoue laisse l'instance vivante.** La l. 378-383 : `_rapatrier` est appelé dans le
`finally` avant `detruire` ; `rapatrier_fichier` (La l. 406-409) et `transferer` lèvent sur un `scp` en échec, sans
rattrapage. Sonde S4 : `FileNotFoundError`, instances détruites : `[]`. Le veilleur, fil démon du même processus,
meurt avec lui : rien ne détruit plus l'instance (R10, liste d'arrêt l. 368-369).

**N-5 (bloquant). Instance vivante après l'échéance du GO.** I l. 392-393 : l'arrêt nominal attend l'échéance elle-même,
puis viennent empreintes, transfert et destruction ; La l. 195 : le secours détruit à l'échéance + 1 800 s (sonde S6 :
1 700 s après l'échéance, `verifier()` rend `None`). Et `verifier_echeance` (La l. 122-124) ne garantit que
`échéance ≥ création + (B − 2)/c`, alors que la v2 laisse la dépense courir jusqu'à B − 0,5 : de la dépense peut tomber
hors de la validité du GO (nœud « dépense sans GO »).

**N-6 (bloquant). Validité : garde de fin de run en partie tautologique.** Texte l. 307-310 : « nombre de tours complets
égal à K, ou au K′ déclaré » ; « empreinte de chaque journal égale à celle prise sur l'instance avant transfert ».
(a) Le l. 86-91 passe à la garde le K′ calculé par `k_prime` sur le même journal. Sonde L1 : règle K = 30, exécution
finie sans interruption déclarée (`etat-execution` : code 0, cause nulle, k = 30), journal de 21 tours → `etat` = None,
lisible comme un run de 21 tours. (b) `valider` ne réempreinte aucun des fichiers qu'il lit. Sonde L2 : journal des
notes modifié après la prise des empreintes → garde de fin de run passée. (c) Les étiquettes
`behavior_evaluation_e_…` sont fabriquées par `tours_journal` (Le l. 54-62) : sonde L3, tour 1 sans aucune trace de
table de comportement → suite « complète ». Même fabrication dans l'audit (Le l. 187).

**N-7 (bloquant). La note de la sonde à chaque pas sort dans le journal « sans note ».** Pub `loss.py` l. 138-143,
204-209, 399-404 : `{"behavior_loss", "obf_loss"}` à chaque pas d'attaque ; `obf_loss` est la moyenne des
prédictions de la sonde courante sur le lot attaqué (`self.obf_metric.predict`). J l. 193-198 les range au journal
technique, que la v2 dit « lisible au pilote sans ouvrir les notes » (sonde L4). Texte l. 239-241 (au pilote, on ne lit
que durées, mémoire, pas, gardes ; notes scellées sans lecture) et l. 316-317 (sortent : notes, durées, empreintes) :
soit c'est une note, et elle doit aller au journal des notes, scellé ; soit ce n'en est pas une, et elle ne doit pas
sortir. Le faux déroulé des essais ne les émet pas (essai manquant 12).

**N-8 (à corriger). Aucun scellement codé.** Texte l. 240-243, 268-270, 308-309. Ni la conduite ni la lecture ne scellent
les notes du pilote ou de la première exécution ; `valider` reçoit `notes_pilote_scellees` et
`notes_premiere_execution_scellees` de l'appelant, sans lien avec `controle_ia.scellement`.

**N-9 (à corriger). Gardes de versions vides passantes.** Sonde M1-M2 : `garde_commits_git({})` et `garde_versions({})`
rendent « passée » ; `peft` (chargement de l'adaptateur) et `strong_reject` au commit `JUGE_COMMIT_PAQUET` ne sont pas
exigés.

**N-10 (à corriger). Mémoire vive en Gio sans le dire.** Sonde L5 : `MemTotal: 131000000 kB` = 124,93 Gio = 134,1 Go
décimaux → « tombée ». Le devis dit « au moins 128 Go » (l. 27) sans unité binaire. La garde n'est pas plus laxiste que le
texte, mais elle peut refuser un hôte conforme, et elle lit l'hôte, pas la limite du conteneur.

**N-11 (à corriger). Manifeste du run perdu ou écrasé.** La l. 338-340, 362-363, 372-373 : les ajouts (pas, longueur,
B R D c t H K) ne vont qu'au manifeste de l'instance, détruit avec elle ; à la relance, `regle_tours` est remplacé
(K et D de la première exécution perdus du manifeste, R12).

**N-12 (à corriger). Fichiers d'état transférés sans empreinte.** La l. 399-405 : `mise-en-place-v2.json`,
`controle-juge-v2.json` (comptes des contrôles du juge, qui décident de la validité) et `regle-tours-v2.json` sortent
sans comparaison ; la liste `transferts` n'est pas conservée (`bilan["transferts"]` ne garde que des longueurs,
La l. 410) : l'appelant de `valider` ne peut pas la lui donner.

**N-13 (à corriger). L'amorce ne peut pas cloner le dépôt de travail.** La l. 222 : `git clone` de
`lciric/controle-ia-travail`, privé (`CLAUDE.md`), sans accès ; l'amorce échoue après la création (dépense engagée). Y
mettre un jeton GitHub sur une machine louée serait pire : copier par `scp` une archive `git archive` du commit,
empreintée.

**N-14 (à corriger). Arrêt pour dépense hors des exécutions.** La garde B − 2 n'existe que dans `executer`
(I l. 390) et dans le journaliseur ; pendant l'amorce, la mise en place et le contrôle du juge, seul le secours
B − 0,5 joue, par destruction sans transfert.

**N-15 (à corriger). `echeance_go` absent → `TypeError`.** I l. 448, 392 : `--echeance-go` non requis ; `time.time() >=
None` lève hors de toute garde (sans effet par la conduite, qui le passe toujours).

À préciser (addendum) :
- **P-a.** Le seuil de secours (0,5 USD) et le délai de secours : voir section 3.
- **P-b.** Ce qui sort, au-delà de la liste du texte : mémoire au pic, configuration de génération du modèle
  (`mise-en-place-v2.json`), comptes des contrôles du juge, horodatages : à déclarer comme « durées et coûts » ou
  « empreintes et états ».
- **P-c.** Le dépôt de l'adaptateur porte-t-il un tokeniseur ? Le paquet du juge charge `AutoTokenizer` sur le nom de
  l'adaptateur (`strong_reject/evaluate.py` l. 475-478) ; à établir avant l'instance, comme la base.
- **P-d.** Quel dossier de transfert fait foi (`transfert-1` ou `transfert-2`) : celui dont les empreintes égalent
  celles de l'instance ; à écrire dans le bilan.
- **P-e.** « Erreur technique nommée » (texte l. 371 : mémoire de carte, mémoire vive, valeur non finie, coupure de
  l'hôte) : la conduite corrigée doit-elle relancer sur tout code non nul, ou seulement sur ces causes ? À trancher par
  une liste écrite.
- **P-f.** La conduite dépend d'une seule session `ssh` de plusieurs jours (La l. 293, 301) : une coupure du poste local
  tue la commande distante (raccrochage) et mène à la destruction. Lancer les exécutions détachées sur l'instance et les
  sonder, ou le déclarer comme risque.

## 3. Écarts au texte scellé (chacun est un nœud tant qu'il n'est pas corrigé ou acté)

1. **Arrêt à B − 2.** Texte l. 368 : « Dépense ≥ B − 2 USD → Arrêt de l'instance par son identifiant (R10) ; run
   tronqué. » La v2 lit : arrêt du run sur l'instance par PID, empreintes, transfert, comparaison, puis destruction par
   identifiant. Cette lecture est la seule qui tienne ensemble les l. 368 (« run tronqué », donc lisible), 307-310
   (empreintes comparées « avant la destruction ») et 264-265 (« lu comme un run interrompu ») : détruire à B − 2 perdrait
   les journaux, et K′ ne serait plus lisible. Je la tiens pour fidèle à l'intention, **mais c'est une lecture d'une ligne
   scellée** : elle doit être écrite à l'addendum et actée par Lazar, comme la v2 le demande elle-même (La l. 10).
2. **Seuil de secours B − 0,5 USD.** Absent du texte ; reste sous B (aucun dépassement du plafond du GO). C'est un
   paramètre d'exécution, pas un critère ; il ne contredit le texte que par N-5 (dépense après l'échéance) et par la
   condition 2, dont l'inégalité suppose l'instance arrêtée à B − 2 (l. 380-381). Acceptable si : (a) Lazar l'acte avec
   la lecture du point 1 ; (b) `verifier_echeance` emploie B − 0,5 au lieu de B − 2 (plus strict que le texte, donc
   permis) ; (c) secours et arrêt nominal sont bornés par l'échéance (correction 5).
3. **Reprise après « sonde orientée » au pilote** (N-1) : contraire aux l. 245-246 et 366.
4. **Relance** (N-2) : contraire à la l. 371 (jamais sur erreur technique, jamais après garde de démarrage).
5. **D** (N-3) : contraire aux l. 249-254.
6. **Garde de fin de run** (N-6) : la comparaison au K ou au K′ déclaré et la comparaison des empreintes « des journaux
   scellés » ne sont pas faites sur ce qui est lu (l. 307-310).
7. **Ce qui sort et lecture du pilote** (N-7) : contraire aux l. 239-241 et 316-317.
8. **Dépense hors de la validité du GO** (N-5) : condition 2 et règle « toute dépense sur GO » du dépôt.

Aucun écart sur les critères de lecture eux-mêmes (`validite`, `verdict`, double calcul) dans ce qui a été relu.

## 4. Corrections exigées (numérotées, avec la correction exacte)

1. **(N-1, N-2, P-e) Conduite, pilote et relance.** `instance_v2.executer` écrit dans `etat-execution-v2.json` et
   dans la ligne `ETAT` la liste des gardes tombées (nom seulement, lue dans `journal/gardes-v2.jsonl` et
   `gardes-lanceur-v2.jsonl`) ; `Conduite` décide sur `code_retour`, `cause_arret` et ces noms, jamais sur le code `ssh` :
   - pilote : si « sonde orientée » est tombée → arrêt, `bilan["arret"] = "non interprétable (sonde orientée au
     pilote) ; pas de run principal"`, aucune reprise ; sinon, si `code_retour != 0` ou `tours_marques != 3` ou
     `cause_arret` ∈ {« garde de démarrage »} → une seule reprise ; `cause_arret` ∈ {« dépense », « échéance du GO »}
     → arrêt, pas de reprise ;
   - run principal : relance si `tours_complets < 20` **et** (`code_retour != 0` **ou** `cause_arret` = « garde de
     démarrage ») **et** « sonde orientée » non tombée **et** `cause_arret` ∉ {« dépense », « échéance du GO »} ; sinon
     pas de relance ; si le K recalculé est < 20, `bilan["arret"] = "relance impossible (K < 20) : pas de verdict ;
     nœud"`.
   Essais : S1, S2, S2b, S3 de ce rapport, plus « sonde orientée au run principal → pas de relance » et « dépense au
   pilote → pas de reprise ».
2. **(N-3) D toutes instances.** `Conduite` prend un champ obligatoire `instances_anterieures: list[dict]` (identifiant,
   c, création, destruction, lus dans `registres/depenses`), le verse au `Poste` avant `creer`, et vérifie que `B`
   égale celui de la première instance du poste ; `d_avant` passé à l'instance en tient compte. Essai : une instance
   antérieure de 5 USD → `d_avant` = 5 et K plus petit.
3. **(N-4) Destruction garantie.** Dans `conduire`, `self._rapatrier(...)` dans son propre `try/except Exception`
   (consigné au bilan), **puis** `detruire` dans tous les cas ; dans `transferer`, un `scp` en échec compte comme un
   écart (essai suivant), jamais comme une exception qui sort. Le veilleur de secours tourne dans un processus séparé
   (ou une tâche planifiée locale) qui survit au processus de conduite, avec l'identifiant de l'instance. Essai : S4 →
   `detruites == ["77"]`.
4. **(N-6) `valider`.** (a) K′ déclaré lu dans `etat-execution-v2.json` : si `code_retour == 0` et `cause_arret` nulle,
   le nombre de tours complets doit égaler le K de la phase (`k` de ce fichier, égal au manifeste) ; sinon K′ = nombre de
   tours complets, et le tour e₀ = K′ doit porter une garde tombée, une absence de « MARK » ou la cause d'arrêt ;
   (b) `valider` empreinte lui-même chaque fichier de `NOMS_JOURNAUX` dans `d` et compare à `empreintes_instance` (lu
   dans `empreintes-instance-v2.json` transféré), au lieu de recevoir `transferts` ; (c) l'étiquette de comportement
   du tour e est lue au journal technique (évènement `pas` de la création de la table, `tour` = e), jamais fabriquée ;
   même lecture dans l'audit. Essais : L1, L2, L3 de ce rapport doivent tomber.
5. **(N-5, section 3) Échéance.** `instance_v2.executer` arrête à `echeance_go − marge_transfert_s` (déclarée, par
   exemple 3 600 s) ; le secours détruit au plus tard à l'échéance (`delai_secours_s ≤ 0`) ; `verifier_echeance` exige
   `échéance ≥ création + (B − marge_secours)/c h + marge_transfert`. Essai : S6 doit rendre une cause.
6. **(N-7) Pertes par pas.** Au journaliseur, `{"behavior_loss","obf_loss"}` vont au journal des notes (scellé), ou ne
   sont que comptées ; jamais au journal technique. Le faux déroulé des essais les émet à chaque pas, avec
   `log_table_name` et `concept_dataset_*` (essai manquant 12). Essai : L4 → absentes du journal technique.
7. **(N-8) Scellement.** Après une comparaison d'empreintes égale, `Conduite` scelle par `controle_ia.scellement.sceller`
   chaque journal transféré du pilote, de la reprise et de la première exécution (compagnon `.sha256`) ; `valider`
   remplace les booléens `notes_pilote_scellees` et `notes_premiere_execution_scellees` par `scellement.verifier` sur
   ces compagnons, et `relance` par l'existence du dossier `principal-relance` transféré.
8. **(N-9, B-4) Versions exigées.** `garde_versions` refuse un dictionnaire vide et exige au moins `torch`,
   `transformers`, `peft`, `hydra-core`, `omegaconf` ; `garde_commits_git` exige
   `git["strong_reject"][1] == cv.JUGE_COMMIT_PAQUET`. Essais M1 et M2 doivent tomber.
9. **(N-10, A-1) Mémoire vive.** Fixer l'unité dans l'addendum (Go décimaux, 128 × 10⁹ octets, ou Gio) et comparer en
   octets ; prendre le minimum de `MemTotal` et de la limite du groupe de contrôle (`/sys/fs/cgroup/memory.max` si
   numérique). Essai : L5 selon l'unité choisie ; limite de groupe sous le minimum → tombée.
10. **(N-11, A-7) Manifeste.** Chaque ajout produit un manifeste local versionné (`manifeste-v2-mise-en-place.json`,
    `…-regle.json`, `…-relance.json`), sans écrasement, transféré et empreinté ; les ajouts sont aussi écrits sur
    l'instance.
11. **(N-12) Fichiers d'état.** `FICHIERS_ETAT` entre dans le calcul de `empreintes` de leur dossier et passe par
    `transferer` (comparaison, un second essai) ; le bilan garde les dictionnaires d'empreintes, pas leur nombre.
12. **(N-13, P-9) Amorce.** Remplacer le `git clone` du dépôt privé par l'envoi d'une archive `git archive <commit>`
    empreintée, vérifiée sur l'instance ; passer le jeton du dépôt de modèles par un fichier envoyé par `scp` (droits
    600), jamais par la ligne de commande de `vastai`.
13. **(N-14) Dépense hors exécution.** `mise-en-place`, `controle-juge` et l'amorce reçoivent `--depense` et
    s'arrêtent à B − 2 comme `executer` ; ou la conduite vérifie `poste.depense() < B − 2` avant chaque commande.
14. **(A-4) États écrits.** « Dossier neuf » (journaliseur) et `TESTING` (exécution) écrivent une ligne dans
    `gardes-lanceur-v2.jsonl` du dossier d'exécution avant de lever.
15. **(P-4, P-8, A-11) Lecture.** Rejouer l'appariement (empreintes `empreinte_cible` du journal des notes contre
    `reponses_attendues`), la longueur du suffixe et la dépense dans l'audit, ou corriger la docstring ; mémoire de carte
    absente → `None` signalé, jamais 0 ; attaques passées de taille ≠ 200 → signalées ; mémoire vive au pic rapportée ;
    `_memoire` écrit l'erreur au lieu de l'avaler.
16. **(N-15) `--echeance-go` requis** pour `executer`.
17. **(Essais manquants 1, 6, 7)** Artefacts commit, arbre et fichier suivi modifié sur un petit dépôt fabriqué ;
    `configuration_attendue` comparée à la sortie d'un `@hydra.main` réel ; import de `Llama3SoftPrompted` dans un
    environnement où les dépendances du clone sont installées.
18. **(Addendum)** Écrire : la lecture de la ligne « B − 2 » et le seuil de secours (section 3, points 1-2), à faire acter
    par Lazar avant le scellement ; P-1 de `90af7dea` ; P-a à P-f ci-dessus.

Après les corrections 1 à 7 : relecture en différentiel courte de `lanceur_v2.Conduite` (ou de sa v3),
`lecture_v2.valider` et de leurs essais, avant l'addendum.

# Contre-lecture du code de la condition de lancement 6 — témoin « attaque publiée reproduite » (Bailey) — v1

- Lecteur : sous-agent neuf (R2), lancé par la session « attaquant informé ». Je n'ai écrit ni le préenregistrement,
  ni le code, ni les essais, ni la contre-lecture précédente. Date : `date -u` = Tue Nov 10 11:57:56 UTC 2026 (début de
  lecture 11:48:59 UTC).
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), lu au début de la tâche.
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit
  `2beefb5a345fbced5921583540cb0ae833b80d52`, arbre de travail propre (vérifié par `git status`).
- Pièces relues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md`
    (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), lu en entier ;
  - liste exigée : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-code-analyse-bailey-v1.md`
    (`151eee65f9c232c5acb325a48e686de2525d897ff7dd2f539bbdda6064ad347d`), en-tête, verdict et section « Ce qui manque
    au code exigé par la condition de lancement 6 » ;
  - `src/controle_ia/temoin_bailey/conventions_v1.py` (`147ba841…`), `journaliseur_v1.py` (`eb3b6037…`),
    `execution_v1.py` (`e6698829…`), `instance_v1.py` (`7a781ad1…`), `lecture_v1.py` (`0de52d58…`),
    `lanceur_v1.py` (`85193c38…`) ;
  - essais : `tests/test_temoin_bailey_condition6_v1.py` (`de296c78…`) ;
  - `analyse_v2.py` (`5dad0bd0…`) pour les seules fonctions appelées ;
  - code public des auteurs, hors dépôt, lecture seule, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` :
    `train_harmful.py`, `evaluate.py` (l. 467-1165), `obf_reps/utils.py`, `obf_reps/logging/__init__.py`,
    `obf_reps/models/__init__.py`, `obf_reps/models/hf.py`, `obf_reps/models/llama3.py`,
    `obf_reps/data/__init__.py`, `obf_reps/optimize/optimizers.py`, `obf_reps/optimize/loss.py`,
    `obf_reps/config.py`, `configs/config.yaml`, `configs/experiment/{default,z-jailbreak,zf-iter-100-mlp}.yaml`,
    les six fichiers du jeu (comptes de lignes) ; paquet du juge, commit `7a551d5b440ec7b75d4f6f5bb7c1719965b76b47` :
    `strong_reject/evaluate.py` (l. 115-140, 432-490) ;
  - en-tête de `registres/go.md` (format des colonnes) et motifs de `.claude/hooks/garde_calcul.py` (grep).
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`,
  `registres/etat.md`, `registres/decisions.md`, tout résultat ou seuil de sonde ou de moniteur du programme, tout
  résultat d'attaque contre le juge de l'organisme, épisodes d'épreuve, items de l'étiqueteur ; le devis v4 hors la
  ligne « Mémoire vive » (grep) ; les essais d'`analyse_v2` hors grep ; la page du modèle du juge (aucun réseau).
- Outils : `sha256sum`, `git`, `grep`, `sed`, lecture de fichiers ; `PYTHONPATH=src python -m pytest -q
  tests/test_temoin_bailey_condition6_v1.py` : **27 passés** ; trois sondes du lecteur dans
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/cl-code-c6/` (hors dépôt, aucun fichier
  du dépôt ni du code public modifié) : (a) comparaison du texte de `configuration_attendue` à la sortie d'un
  `@hydra.main` réel sur les configurations publiques (Hydra 1.3.8, OmegaConf 2.3.1) ; (b) ligne « MARK » coupée entre
  deux lectures ; (c) doublons de la colonne `response` des 200 entrées tenues à l'écart. Aucune requête réseau, aucune
  dépense, rien de committé.

Renvois : « texte l. n » = préenregistrement ; « J l. n » = `journaliseur_v1.py` ; « X l. n » = `execution_v1.py` ;
« I l. n » = `instance_v1.py` ; « L l. n » = `lanceur_v1.py` ; « C l. n » = `conventions_v1.py` ; « Le l. n » =
`lecture_v1.py` ; « E l. n » = essais ; « pub » = code public.

## Verdict

**Conforme après corrections.** L'architecture suit le texte : journaliseur substitué sans toucher au dépôt public,
gardes embarquées au bon moment de la boucle publique, configuration effective comparée par empreinte, arrêts par PID
et par identifiant d'instance, aucune note imprimée. L'ordre réel des appels du code public au journaliseur est
respecté (étiquettes, tables, pas, moment de la sauvegarde du suffixe), et le texte attendu au démarrage est exact
(sonde (a)). Mais **huit défauts bloquants**, dont deux certains (import faux du contrôle du juge ; lignes « MARK »
perdues) et plusieurs pièces de la liste absentes (manifeste, K′, garde de fin de run branchée, scellement, conduite
pilote-reprise-relance). Décompte : **8 bloquants, 11 à corriger, 9 à préciser.** Le code corrigé doit être relu en
différentiel, et une exécution à blanc de bout en bout (petit modèle sur processeur, ou faux modèle) est recommandée
avant l'addendum.

## 1. Points 1 à 8 de la liste

| Point | État | Où, et ce qui manque |
|---|---|---|
| 1. Journaliseur local | **Couvert**, un défaut | J l. 125-291 : notes brutes étiquetées (l. 245-247), notes du juge (l. 225-229), durées `t`, mémoire (l. 74-82), longueur de suffixe, empreintes des textes et des entrées ; figures fermées (l. 195-196) ; attribut `tables` (l. 130) ; rien vers l'extérieur ; refus d'un suffixe au journal (l. 239-240) ; égalités au seul journal scellé, jamais imprimées (l. 248-249). Défaut : pas et mémoire sont écrits dans le même fichier que les notes (A-3). |
| 2. Lanceur | **En partie** | Présents : clone au commit (L l. 185-186), gardes de mise en place (I l. 61-131), graines avant la sonde initiale (X l. 178-179), Hydra hors clone et surcharges `save_*` (X l. 136-146), empreinte des fichiers (I l. 244-251), longueur du suffixe (I l. 107-131), D sur toutes les instances (L l. 117-138), arrêt par PID (I l. 303-309) et par identifiant (L l. 160-169), transfert à deux essais (L l. 211-223). Absents : écriture du **manifeste** (versions, révisions, configuration de génération, B R D c t H K) ; **conduite** pilote → règle → run principal, une seule reprise, une seule relance ; **scellement** des notes du pilote et de la première exécution ; transfert **avant** destruction (B-5) ; périmètre de ce qui sort (B-6). |
| 3. Configuration effective | **En partie** | I l. 198-241, X l. 149-159 : texte attendu exact (sonde (a)), empreinte comparée au début de la sortie, valeurs observées au journal (I l. 217-220). Défauts : sortie d'erreur mêlée à la sortie standard (B-2) ; nombre de tours et graine non comparés au manifeste (B-8). |
| 4. Garde du juge | **En partie** | J l. 95-117, 213-220 ; I l. 148-149, 184-185 ; X l. 164-166. `TESTING` et type numérique couverts. Le cas « adaptateur » n'est pas tenu : révision de l'adaptateur non lue, nom attendu ambigu (B-4). |
| 5. Contrôles du juge | **En partie** | I l. 144-193 : génération publique par lots de 16, graine pilote, positif sur `response`, comptes, arrêt hors seuil. Deux défauts bloquants : import faux (B-1) ; juge appelé sur 200 réponses en un lot (B-3). |
| 6. Conventions | **Couvert** | C l. 9-103 : empreinte des valeurs (float32, ordre C, forme préfixée), étiquettes attendues, noms des journaux, appariement. L'appariement lit `beh_target` au lieu de « l'entrée » : à déclarer (P-1). |
| 7. Code de lecture | **En partie** | Le l. 258-420 : assemblage R_att/R_def/R_std/J (conforme à l'ordre réel, vérifié), double calcul, audit en trois contrôles, intervalles dans l'ordre, grandeurs rapportées. Absents : **détermination de K′** et de l'état de validité (gardes de mise en place, contrôle du juge, sonde orientée, chutes du pilote, fin de run) : `lire` les reçoit de l'extérieur (Le l. 405-410) ; mémoire vive au pic non rapportée ; replis silencieux de `lire_jsonl` (A-6). |
| 8. Addendum scellé | **Absent** | Attendu après corrections et relecture ; rien à relire ici. |

## 2. Écarts entre le code et le texte scellé (chaque écart est un nœud si le code n'est pas corrigé)

Gardes :
- **Mise en place** (texte l. 274-278). Commit, arbre, fichiers suivis, empreintes, graines : conformes (I l. 61-76,
  118). Écarts : mémoire vive acceptée à 97 % du minimum (I l. 88), le texte dit « au moins égale » (A-1) ; commits des
  trois paquets tirés de dépôts tiers non vérifiés (`garde_versions` ne lit qu'un numéro de version ;
  `JUGE_COMMIT_PAQUET`, C l. 52, n'est employé nulle part) (A-2) ; ordre « mise en place puis contrôle du juge puis
  pilote » non imposé par le code (P-5).
- **Démarrage** (texte l. 279-286). Le texte compare « le début exact de la sortie standard » ; le code lit la sortie
  standard **et** la sortie d'erreur fusionnées (I l. 279 `stderr=subprocess.STDOUT`) (B-2). « Nombre de tours égal à
  celui du manifeste » : `garde_k_configuration` (I l. 235-241) compare le texte attendu au `k` de la ligne de commande,
  à partir duquel ce texte est construit : la garde est tautologique ; ni K ni la graine ne sont lus au manifeste (B-8).
- **Juge** (texte l. 287-289). Voir B-4. L'état « tombée » de la garde `TESTING` dans le processus enfant n'est écrit
  que sur la sortie d'erreur, qui reste sur l'instance (X l. 164-166) (A-4).
- **Par tour** (texte l. 290-297). Toutes les grandeurs exigées sont contrôlées (J l. 257-282 ; `garde_par_tour`,
  `garde_suffixe_appris`, `garde_appariement`, `garde_depense`). Trois gardes lèvent sans écrire leur état
  (« table », J l. 190-194 ; « suffixe au journal », J l. 239-240 ; « dossier neuf », J l. 134-136) (A-4).
- **Sonde orientée** (texte l. 305-306) : conforme, au début du tour 0 de chaque exécution (J l. 251-252).
- **Fin de run** (texte l. 307-310) : `analyse_v2.garde_fin_de_run` n'est appelée par aucun module nouveau ; personne
  ne construit la liste des tours (index, ligne MARK, garde tombée, étiquettes) depuis les journaux (A-5).
- **Dépense et échéance** (texte l. 297, 368-369) : mesurées aux trois endroits (journaliseur, surveillance,
  veilleur), au seuil B − 2. Mais le veilleur **détruit l'instance** dès ce seuil (L l. 160-169), sans transfert ;
  le texte exige la comparaison des empreintes des journaux transférés avant la destruction (l. 309-310) et lit le run
  comme tronqué (l. 264-265) (B-5).
- Messages : aucune valeur de note dans les messages (vérifié sur toutes les levées) ; états « passée »/« tombée » :
  conforme là où `_garde` est employée.

Règle du nombre de tours (texte l. 248-266) : calcul conforme (`analyse_v2.nombre_de_tours` ; I l. 329-338) ; t pris
sur les lignes « MARK » des tours 0 et 1. Écarts : la lecture des lignes « MARK » perd une ligne coupée entre deux
lectures du tube (B-7) ; B, R, D, c, t, H, K sont écrits dans `regle-tours-v1.json`, pas au manifeste (A-7) ; le choix
de « la première exécution du pilote qui a fini ses tours 0 et 1 » est laissé à l'opérateur (`--pilote`) (P-6).

Pilote, reprise, relance (texte l. 239-246, 371) : seule la règle « dossiers neufs » est codée (I l. 258-259 ;
J l. 134-136). Le nombre de reprises et de relances, « même graine », « K recalculé sur le budget restant, même B, t du
pilote », et le scellement sans lecture des notes de la première exécution ne sont pas codés (A-8).

Ce qui sort de l'instance (texte l. 316-319) : les journaux nommés (C l. 59-61) ne contiennent ni texte, ni suffixe,
ni sonde, ni configuration (empreinte seule, I l. 217-220) : conforme. Mais `transferer` (L l. 211-223) rapatrie
`distant` en entier par `scp -r` ; si `distant` est le dossier d'exécution, il emporte `params/` (suffixes),
`sondes/`, `hydra/.hydra/config.yaml`, `config-journal-v1.json` et `sortie-standard-instance.log` (configuration
imprimée) (B-6). `FournisseurVast.executer` renvoie au poste local les 4 000 derniers caractères de la sortie des
commandes distantes, sans filtre (L l. 62-66) (A-9).

Arrêts par identifiant (R10) : conformes (PID, I l. 304-308 ; identifiant d'instance, L l. 53, 165). La création
d'instance par `subprocess` depuis Python échappe à la garde `.claude/hooks/garde_calcul.py`, qui ne voit que la ligne
de commande (P-7).

Replis silencieux (R5) : `lire_jsonl` rend `[]` pour un fichier absent (Le l. 251-255) : un journal des gardes absent
se lit comme « aucune garde tombée » (A-6) ; `_memoire` avale toute erreur (J l. 80-81) ; mémoire de carte rapportée
`0` si absente (Le l. 320) ; attaques passées de taille ≠ 200 retirées sans mention (Le l. 312-313) (P-8).

## 3. Défauts de fonctionnement probables sur la vraie instance

Vérifié conforme sur pièces :
- **Ordre des appels** (pub `train_harmful.py` l. 50-168, `evaluate.py` l. 518-840, 1102-1162) : par tour e, ligne
  « Inning e, defender just went » de `metric_evaluation` ; pas d'attaque (`{"loss": …}` une fois par pas,
  `optimizers.py` l. 189 ; `{"behavior_loss","obf_loss"}` de la perte, sans clé `loss`) ; sauvegarde du suffixe
  (l. 117-125) **avant** l'évaluation de l'attaquant ; `create_table("behavior_evaluation_e_attacker_just_went")` ; 200
  lignes de comportement, juge appelé avant chaque lot ; ligne « Inning e, attacker just went » ; réajustement
  (`probe_loss_layer_*`) sauf au dernier tour. Le journaliseur compte les pas entre la ligne du défenseur et la création
  de la table de comportement (J l. 173-174, 184-187, 253-254), lit le fichier du suffixe à la ligne de l'attaquant
  (fichier déjà écrit), et reconstruit la suite [défenseur, comportement, attaquant] attendue (C l. 68-69). Pas
  attendus : 2 époques × 800 lots de 1 = **1 600** par tour (non calculé dans le code : P-2).
- **Assemblage** : à la ligne « defender » du tour e + 1, le suffixe du tour e est encore en place (réinitialisation
  après cette évaluation, pub l. 101-104) et l'attaque e n'est pas reprise du cache (`params_last_train_epoch` = e) :
  R_def(e) lu sur `obfuscated_harmful_scores` est juste (Le l. 276-278).
- **Chemins des fichiers par tour** : `save_*_path / HIDHarmfulConceptDataModule / …pkl` puis `_ade_e` (pub `utils.py`
  l. 422-442, 100-121) = C l. 95-103.
- **Dépliage des paramètres sauvegardés** : `pickle.dump(SoftParams)` (pub l. 124) ; `SoftParams` porte `params`
  (`nn.Parameter`, demi-précision, sur la carte) et `init_params` (pub `models/__init__.py` l. 72-77). Le dépliage a
  lieu dans le processus du code public, où la classe est importable et la carte présente ; `detach().cpu().float()`
  (C l. 88) convient. `reinit` recopie `init_params`, constant : la comparaison « différent de la valeur initiale » est
  bien posée.
- **Texte imprimé au démarrage** : `print(OmegaConf.to_yaml(cfg))` est la première impression de la tâche ; les
  impressions « Created directory structure… » viennent après (pub `utils.py` l. 477) ; sonde (a) : la sortie d'un
  `@hydra.main` réel commence exactement par `configuration_attendue(...)` (Hydra 1.3.8), et le dossier courant n'est
  pas changé (`version_base=None`) : les chemins relatifs du jeu tiennent.
- **Journaliseur substitué** : `utils.py` résout `WAndBLogger` dans son espace de noms à l'appel (l. 396) ; aucun
  `isinstance` sur le journaliseur dans le code public ; `ExperimentConfig` est une classe de données simple.

Défauts probables ou certains :
- **Import faux du contrôle du juge (certain)** : I l. 160 importe `Llama3SoftPrompted` de `obf_reps.models.hf`, qui ne
  la définit pas (0 occurrence) ; elle est dans `obf_reps.models.llama3` (pub `utils.py` l. 70). `ImportError` à la mise
  en place (B-1).
- **Juge sur 200 réponses en un lot (probable)** : `strongreject_finetuned` est appelée directement sur 200 couples
  (I l. 183, 187) ; le décorateur rend la fonction telle quelle (`evaluate.py` l. 130-132) ; elle calcule les logits de
  toutes les positions sur un vocabulaire de modèle de type Gemma (≈ 256 000) pour 200 séquences jusqu'à 512 jetons de
  réponse plus le gabarit : plusieurs dizaines de Go, au-delà d'une carte de 80 Go selon la longueur. Le run public
  l'appelle par lots de 16 (`eval_batch_size`, via `evaluate_behavior`). Le contrôle doit juger comme la boucle (B-3).
- **Juge en adaptateur (probable, non vérifié faute de réseau)** : si `qylu4156/strongreject-15k-v1` est un adaptateur
  (le texte l. 206-207 le laisse ouvert), le chargement par `AutoModelForCausalLM` charge la base, dont le nom et la
  révision remplissent `config._name_or_path` et `config._commit_hash` ; `etat_juge_charge` (J l. 95-108) ne lit alors
  ni le nom ni la révision de l'adaptateur. Hors ligne (`HF_HUB_OFFLINE=1`, L l. 198), le juge est chargé sans révision
  (révision « main ») : un téléchargement par empreinte de commit (L l. 192) n'écrit pas `refs/main` dans le cache, et
  la base n'est pas téléchargée du tout ; `peft` n'est pas listé (B-4).
- **Lignes « MARK » perdues (certain)** : `Surveillance._lignes` découpe chaque morceau lu séparément (I l. 226-232) ;
  sonde (b) : « MARK: Epoch 0 took 12 » puis « .5000 seconds » ne donnent aucune durée. Avec la sortie d'erreur des
  barres de progression dans le même tube, les coupures sont fréquentes : t introuvable au pilote, ou tour non
  « complet », K′ faux (B-7).
- **Sortie d'erreur fusionnée (probable)** : tout avertissement émis à l'import (bibliothèques, `warnings`) avant la
  configuration fait tomber la garde de démarrage sur un cas sain, au pilote puis à la reprise : seconde chute, pas de
  run (B-2).
- **Empreinte d'un fichier en cours d'écriture (possible)** : le sondage toutes les 5 s (I l. 295-297) peut
  empreinter un fichier de sonde ou de suffixe à demi écrit, puis ne plus jamais le relire (clé `vus`) (A-10).
- **Téléchargement du modèle soumis à accès** : `huggingface-cli download` de Llama-3-8B-Instruct (et d'une base de
  juge soumise à accès) demande un jeton ; le script d'amorce n'en dit rien (P-9, condition 8).

## 4. Essais

27 passés. Cas sains présents : demi-précision conforme au texte l. 311-314 (150 nuisibles au plafond avec et sans
suffixe, trois bénignes à τ ; E l. 60-68) ; journal et lecture de bout en bout ; surveillance ; exécution factice ;
règle du GO ; poste et veilleur. Artefacts présents : pas, bénignes constantes, valeur non finie, même suffixe,
suffixe initial, ordre, étiquette, suffixe au journal, sonde orientée, juge (type, nom, `TESTING`, cache vide),
dépense embarquée, dossier neuf (journaliseur et exécution), configuration fausse, dépense et échéance de la
surveillance, mémoire vive, versions, GO.

Manquent (R5 : chaque garde, un cas sain et un artefact) :
1. dépôt public (commit, arbre, fichier suivi modifié) et empreintes publiques : aucun essai (un petit dépôt git
   fabriqué suffit) ;
2. juge : révision différente ; cas sain et artefact **avec adaptateur** (`peft_config`) ;
3. suffixe : fichier du tour absent ; longueur différente de celle du tour 0 ;
4. 199 notes du juge ; table de comportement à 199 lignes ;
5. ligne « MARK » coupée entre deux lectures ; avertissement sur la sortie d'erreur avant la configuration (doit
   passer) ;
6. `configuration_attendue` contre un vrai `@hydra.main` sur un petit arbre de configuration fabriqué (aujourd'hui
   remplacée par un faux, E l. 272-273) ;
7. contrôle du juge : import et découpage en lots (faux modèle, faux juge) ;
8. garde de fin de run branchée sur des journaux réels ; transfert avec écart au premier essai puis égalité, et écart
   persistant ; veilleur qui exécute `run` à l'échéance ;
9. audit : un artefact par contrôle (recalcul différent, suffixe répété, garde tombée dans un tour compté) ;
10. `lire_jsonl` sur fichier absent (doit lever) ;
11. l'essai paramétré exclut « suffixe_au_journal » et « non_fini » du contrôle de l'état écrit (E l. 202-203) : à
    retirer après A-4 ;
12. le faux déroulé (E l. 84-123) omet les journaux réels hors tour (`concept_dataset_*`, `behavior_loss`/`obf_loss`
    à chaque pas, `log_table_name`) et emploie 6 et 8 colonnes au lieu de 11 et 23 : reprendre les colonnes réelles.

## 5. Corrections

**Bloquants**
1. **B-1** I l. 160 : `from obf_reps.models.llama3 import Llama3SoftPrompted` (et, mieux, obtenir la classe comme
   `utils.py` l. 225-227). Essai d'import sur le clone.
2. **B-2** I l. 279 : `stderr=` vers un fichier propre resté sur l'instance (`sortie-erreur-instance.log`) ;
   `Surveillance` ne lit que la sortie standard. Essai : avertissement sur la sortie d'erreur avant la configuration,
   garde passée.
3. **B-3** I l. 183, 187 : juger par lots de `cfg.eval_batch_size` (16), dans l'ordre, comme la boucle — de préférence
   par `JailbreakCircuitBreakersObfusDataModule.evaluate_behavior` ; la garde du juge reste après le premier appel.
4. **B-4** Juge : (a) avant l'instance, établir sur la page du modèle s'il s'agit d'un adaptateur et consigner nom et
   révision de l'adaptateur et de la base ; (b) amorce : télécharger adaptateur **et** base à leurs révisions, installer
   `peft` à version consignée, et faire pointer `refs/main` du cache sur la révision épinglée (le paquet charge sans
   révision) ; (c) `etat_juge_charge` : lire la révision effective de l'adaptateur (chemin résolu dans le cache, dossier
   `snapshots/<révision>`) et celles de la base (`config._commit_hash`), comparer les deux couples au manifeste ;
   essais sain et artefact avec adaptateur.
5. **B-5** L l. 152-169 : au seuil B − 2 ou à l'échéance, le veilleur arrête l'exécution (commande distante qui tue le
   processus par PID), lance `empreintes`, transfère, compare, **puis** détruit par identifiant ; une destruction
   d'office seulement à un second seuil déclaré (par exemple B − 0,5) ou à une heure de garde avant l'échéance. Ce
   second seuil doit tenir dans le texte (« arrêt de l'instance » à B − 2) : à faire confirmer par Lazar s'il est lu
   comme un écart.
6. **B-6** L l. 211-223 : transférer **la seule liste** `NOMS_JOURNAUX` plus `mise-en-place-v1.json`,
   `controle-juge-v1.json`, `regle-tours-v1.json`, `empreintes-instance-v1.json`, fichier par fichier ; jamais un
   dossier ; essai qui échoue si un chemin hors liste est demandé.
7. **B-7** I l. 226-232 : tampon de ligne gardé d'un morceau à l'autre (ne traiter que les lignes terminées, décoder
   après assemblage) ; essai sonde (b).
8. **B-8** I l. 254-276 : `executer` lit K et la graine au manifeste selon la phase (pilote : 3 et
   `graines.pilote` ; run principal : K de la règle et `graines.principal` ; reprise et relance : mêmes valeurs que
   l'exécution reprise), refuse toute autre valeur, et la garde de démarrage compare le nombre de tours du texte
   **observé** à ce K.

**À corriger**
9. **A-1** I l. 88 : retirer la tolérance de 3 % ; comparer `MemTotal` × 1 024 octets à 128 × 10⁹ octets (unité du
   devis à fixer à l'addendum).
10. **A-2** Vérifier à la mise en place le commit de chaque paquet tiré d'un dépôt (`direct_url.json` de sa
    distribution, `vcs_info.commit_id`), dont `strong_reject` = `JUGE_COMMIT_PAQUET`.
11. **A-3** J l. 187, 245-247 : écrire pas, durées et mémoire dans un journal sans note (`couts-v1.jsonl`), seul lu au
    pilote (texte l. 239-241) ; l'ajouter à `NOMS_JOURNAUX`.
12. **A-4** Toute garde écrit son état avant de lever : « table », « suffixe au journal », « dossier neuf », et
    `TESTING` dans l'enfant (X l. 164-166 : écrire dans un fichier de gardes du dossier d'exécution).
13. **A-5** Fonction qui construit la liste des tours (MARK lus, gardes tombées, étiquettes) depuis les journaux et
    appelle `garde_fin_de_run` ; branchée avant `lire`.
14. **A-6** `lire_jsonl` lève pour un journal attendu absent ; `lire` vérifie la présence de chaque nom de
    `NOMS_JOURNAUX`.
15. **A-7** Écrire le manifeste (R9) : graines, versions et commits, révisions du modèle et du juge, configuration de
    génération du modèle (écart 5), longueur du suffixe (écart 10), pas attendus, B R D c t H K, commit du code ; les
    sous-commandes y lisent leurs entrées.
16. **A-8** Conduite codée : mise en place → contrôle du juge → pilote (une reprise au plus) → règle → run principal
    (une relance au plus, K recalculé sur le budget restant, même B, t du pilote) → empreintes → transfert →
    destruction ; compteur d'exécutions écrit ; refus d'une troisième exécution d'une phase.
17. **A-9** L l. 62-66 : les commandes distantes écrivent leur sortie sur l'instance ; seul le code de retour et une
    ligne d'état reviennent.
18. **A-10** I l. 244-251 : n'empreinter qu'un fichier dont la taille est stable entre deux sondages, ou à la fin du
    tour.
19. **A-11** Le l. 405-420 : calculer K′ (tours complets) et l'état de validité depuis les journaux (états de la mise
    en place, contrôle du juge, gardes, chutes du pilote, règle), au lieu de les recevoir ; rapporter la mémoire vive au
    pic.

**À préciser (addendum)**
20. **P-1** Appariement : déclarer que « l'empreinte de l'entrée » est lue sur la réponse de référence (`beh_target`),
    196 valeurs distinctes sur 200 ; les quatre doublons (indices 2 et 78, 13 et 154, 141 et 151, 166 et 199) sont des
    paires identiques (sonde (c)) : leur permutation est sans effet.
21. **P-2** Pas attendus par tour : calculer 1 600 dans le code depuis la configuration (`epochs` × lots), pas à la main.
22. **P-3** Échéance « AAAA-MM-JJ » lue comme 23:59:59 UTC (L l. 98-107) : à confirmer ; vérifier qu'aucune ligne de
    révocation de `registres/go.md` ne vise le GO cité.
23. **P-4** Audit : le rejeu des gardes omet l'appariement, la longueur du suffixe et la dépense ; le troisième contrôle
    lit les empreintes de valeurs du journal, pas les fichiers de `empreintes-fichiers-v1.jsonl` : dire lequel fait foi.
24. **P-5** Le contrôle du juge vérifie que la mise en place est passée (fichier d'état) avant de charger quoi que ce
    soit.
25. **P-6** « Première exécution du pilote qui a fini ses tours 0 et 1 » : choisie par le code, pas par `--pilote`.
26. **P-7** Création d'instance : passer par une ligne de commande `GO_ID=… vastai create instance …` vue par la garde,
    ou appeler `ligne_go`/`verifier_go`/`verifier_echeance` dans `creer` ; `lanceur_v1` n'a pas de point d'entrée.
27. **P-8** Grandeurs rapportées : signaler (et non taire) une attaque passée de taille ≠ 200, une mémoire absente ; les
    pertes par pas écrites au journal sont-elles des « notes » au sens de « ce qui sort » ?
28. **P-9** Accès de compte au dépôt de modèles (jeton) sur l'instance, sans jamais l'imprimer ni l'écrire au journal
    (condition 8).

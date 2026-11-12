# Addendum 4 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — code v17 : script public lancé comme programme principal ; troisième série après une cause établie — brouillon 2

12 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 2 : non contre-lu (R2), non scellé** ; il complète le brouillon 1 (`brouillons/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-brouillon1.md`, gardé tel quel, R12), écrit avant la contre-lecture du code. Le préenregistrement et ses
addenda 1, 2 et 3 restent tels quels (R12) ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet
addendum ne contient aucun résultat : aucune note de sonde ni de juge n'existe (zéro tour complet dans toutes les
exécutions) et aucune n'a été lue.

## 1. Pourquoi
Nouvelle série de l'addendum 3 (conduite v9, code v16 au commit `91238a73`, poste Hetzner v9 175884265, instance
60403564, Oregon) : mise en place (aucune garde tombée) et contrôle du juge tenus ; **pilote (21:11:09Z) et reprise
(21:12:19Z) sortis en code 1 en ≈ 70 s, zéro tour** ; issue de l'addendum 3, § 2.4 : « nouvelle seconde chute du pilote :
pas de run principal, pas de verdict ; nœud ; aucune autre série sans nouvelle décision de Lazar et nouvel addendum ».
Note `registres/passations/2026-11-12-2140-temoin-bailey-serie-2-cause-hydra-noeud.md` (`b70d8fea…`).

Cette fois **le message d'erreur est sorti** (addendum 3, § 2.1) :
`runs/temoin-bailey-v1-20261111/sortie-conduite-v9/pilote/transfert-1/erreur-demarrage-v1.txt` (`33599bfc…`), identique
pour la reprise. Trace : Hydra `run_and_report` → `compose_config` → `load_configuration` →
`ensure_main_config_source_available` → `importlib_resources_config_source.available` → **`NotADirectoryError:
MultiplexedPath only supports directories`**.

**Cause établie** (reproduction sur processeur, sans dépense ; note `b70d8fea…`). `execution_v3` appelait le script public
**par import** (`import train_harmful` ; `train_harmful.main()`), alors que les auteurs le lancent comme programme
(`python train_harmful.py`). Le décorateur public `@hydra.main(version_base=None, config_path="configs",
config_name="config")` (`train_harmful.py` l. 171, commit `9c1f4b1a`) cherche alors la configuration comme ressource d'un
paquet Python `configs`, et non comme dossier voisin du fichier. Le défaut est dans tout le code d'exécution depuis
`execution_v1` ; aucune épreuve antérieure ne lançait `@hydra.main` (l'essai à blanc de l'installation ne faisait
qu'importer le code public). La chute du 12 novembre à 15:33Z (même durée, même absence de journal) a très probablement la
même cause.

Décision de Lazar sur ce nœud, verbatim : « go (a), garde le poste »
(`registres/passations/2026-11-12-2210-decision-lazar-bailey-a-execution-v4-garde-poste.md`, `cb16b95c…`), où (a) était :
« `execution_v4` (appel du script public par `runpy.run_path`, `run_name="__main__"`), essais dont une épreuve réelle de
`@hydra.main`, contre-lecture, addendum 4, nouvelle série », contre (b) « arrêter le témoin ».

## 2. Écarts décidés par Lazar (« go (a), garde le poste », `cb16b95c…`), actés par cet addendum
1. **Lancement du script public (écart d'exécution, sans effet voulu sur le fond).** `execution_v4` lance
   `<clone>/inference_time_experiments/train_harmful.py` comme programme principal :
   `runpy.run_path(<chemin>, run_name="__main__")`, après la pose de `sys.argv = [<chemin>, *surcharges]`. C'est le mode de
   lancement des auteurs. Rien d'autre ne change dans l'exécution : garde `TESTING`, `WANDB_MODE=disabled`, dossier
   courant et `sys.path` (le dossier `inference_time_experiments`), graines (`transformers.set_seed`), journaliseur
   substitué dans `obf_reps.logging` et `obf_reps.utils` avant l'appel (écart 2 du texte ; le script construit son
   journaliseur dans `obf_reps.utils` l. 394-396, module déjà chargé que `runpy` réutilise), surcharges déclarées (écarts
   1, 3, 7, 9), configuration attendue et garde de démarrage.
2. **Troisième série (écart à R3 et à la ligne « Seconde chute du pilote … nœud », texte l. 69-71, 245, 366 ; et à
   l'addendum 3, § 2.4, « aucune autre série sans nouvelle décision de Lazar et nouvel addendum »).** Décision de Lazar :
   « go (a) ». La cause est cette fois **nommée et corrigée** ; l'écart reste un écart (ce n'est pas la relance de la liste
   d'arrêt). Ce qui le rend compatible avec l'objet de R3 : toutes les exécutions du 12 novembre ont fini avec zéro tour
   complet ; aucune note de sonde ni de juge n'existe ; rien n'a été lu ; la reprise ne peut donc pas viser un signe. Une
   seule série : pilote, au plus une reprise, puis la règle et le run principal selon le texte, inchangés. Mêmes graines
   (pilote 1394228342, run principal 1865327867 ; aucune sortie n'a été produite sous ces graines). B inchangé : 75 USD,
   fixé à la création de la première instance du poste (60280913, 12 novembre, 00:03:20Z). D continue de cumuler depuis
   cette instance : **2,778 USD après six instances détruites** (liste `ANTERIEURES` de la conduite v10, qui ajoute
   60403564 à celle de la conduite v9). Les exécutions des séries 1 et 2 sont rapportées comme interrompues. Une nouvelle
   seconde chute du pilote : pas de run principal, pas de verdict ; nœud ; aucune autre série sans nouvelle décision de
   Lazar et nouvel addendum.
3. **Le message d'erreur de l'addendum 3 (§ 2.1 à 2.3) est gardé tel quel**, condition, contenu et portée compris.
4. **Paramètres de lancement** (hors du texte, déclarés) : ceux de l'addendum 3, § 2.5, inchangés (disque 110 Go ; offres
   à 128,9 Go de mémoire allouée au moins ; garde de mémoire vive du texte inchangée ; pilotage par un poste Hetzner
   autonome neuf, v10). Le poste v9 (175884265) reste en marche sur consigne de Lazar ; il ne pilote rien (son script de
   démarrage a fini ; un poste reçoit ses données de démarrage à la création).

## 3. Commit et code
**Commit du code : `8d1c541ef7a3ac99f942e0b2f26567088f2cc503`.** Seuls changent, par rapport à l'addendum 3 :

| Rôle | Module | SHA-256 |
|---|---|---|
| Exécution (enfant) | `execution_v4.py` | `560247ed8cd537ceb4558027de875233ef77da314057f764e8646b2abde65f3f` |
| Lanceur côté instance | `instance_v16.py` | `d9a56e878d091b210d7b96ceded756d24a37f8dea9ef579d489bdf24d524a597` |
| Lanceur local | `lanceur_v17.py` | `acad9644093370b0ab74402eb52f3dff884b7b73284128bc30e035cf7d8ae541` |

`instance_v16` = `instance_v15` dont seuls changent l'import (`configuration_attendue`, `surcharges` depuis
`execution_v4`) et la commande par défaut de l'enfant (`-m controle_ia.temoin_bailey.execution_v4`). `lanceur_v17` =
`lanceur_v16` dont seuls changent le module d'instance, le module des veilleurs et l'archive envoyée sur l'instance
(`execution_v4.py` et `instance_v16.py` au lieu d'`execution_v3.py` et `instance_v15.py`). Les autres modules sont ceux de
l'addendum 3, inchangés à ce commit (`lecture_v8`, `journaliseur_v3`, `conventions_v3`, `analyse_v3`). Le code exécuté est identique à celui du commit `60d06b1f` contre-lu ; le commit `8d1c541e` n'ajoute que les essais complétés (C-2), l'épreuve v2 (C-1) et les empreintes. Manifeste neuf
(R12) : `runs/temoin-bailey-v1-20261111/manifeste-local-v5.json` (`111c6e98…`), écrit par
`lanceur_v17.manifeste_depuis_versions_figees` ; sa seule différence avec le manifeste v4 est `commit_code`.

**Essais (R5)** : `tests/test_temoin_bailey_condition6_v17.py` (``c2b498bb…``) : les 161 essais v16 rejoués sur les
modules v17, plus 8 essais v17 : modules et archive ; aucune chaîne exécutée ne nomme `execution_v3`, `instance_v15` ou
`lanceur_v16` ; commande par défaut de l'enfant ; **épreuve réelle de `@hydra.main`** : un mini-clone synthétique
(`configs/` à deux niveaux comme le code public, `obf_reps.logging`, `obf_reps.utils`, `train_harmful.py` portant le même
décorateur) lancé par `python -m controle_ia.temoin_bailey.execution_v4` dans un processus enfant réel — cas sain : code 0,
sortie standard commençant exactement par `configuration_attendue`, journaliseur substitué vu par le script, dossier de
Hydra hors du clone ; **artefact** : le même mini-clone par `execution_v3` échoue sans rien imprimer, comme les pilotes du
12 novembre ; erreur du script propagée (code non nul, aucun repli) ; garde `TESTING` ; même épreuve avec le vrai dossier
`configs/` du code public quand il est fourni. Résultat : les 8 essais v17 passés (dont l'essai des configurations publiques, fourni ; sauté par défaut), assertions ajoutées après la contre-lecture (C-2 : dossier courant, tête de `sys.path`, module local `evaluate`, graine, `__name__`, `sys.argv[0]`) ; suite complète du dépôt : en cours au moment de la contre-lecture (résultat inscrit avant le scellement).

**Épreuve hors essais, version figée de l'instance** (Hydra 1.3.2, OmegaConf 2.3.0, Python 3.11.18) :
`runs/temoin-bailey-v1-20261111/epreuve-hydra132-execution-v4-v2.py` (`0677c557…`), sortie `…-sortie-v2.txt` (`316910b9…`, en-tête écrit par le script : interpréteur, emplacements de Hydra et d'OmegaConf, commit du clone, empreinte de `configs/`, empreinte des essais) ; la v1 (`17c3544d…`, sortie `7c204bd5…`, en-tête écrit à la main) reste telle quelle : mini-clone synthétique
et mini-clone portant le vrai dossier `configs/` du code public (commit `9c1f4b1a`) ; `execution_v4` : code 0,
configuration au début exact, journaliseur substitué, dossier courant et tête de `sys.path` au dossier `inference_time_experiments`, module local importé, graine 7 reçue, `__name__ == "__main__"` ; `execution_v3` : code 1, rien imprimé.

**Contre-lecture du code (R2)** : `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v17-bailey-v1.md`
(`833429c64a36f7dfc894fde75c6fd1ca38d188be5e7d92875013d0e9b9124fff`), contre-lecteur neuf : **« conforme après corrections »** ; C-1 (à corriger : épreuve hors essais sans empreinte, en-tête écrit à la main) corrigé par l'épreuve v2 et les compagnons `.sha256` ; C-2 (remarque : assertions manquantes) repris dans les essais ; C-3, C-4 (remarques) déclarés au § 5 (c) ; C-5 (remarque : variable `HYDRA_MAIN_MODULE`) déclaré au § 5 (d) ; C-6 (sceller le code) fait. Les effets de `runpy` (`__file__`, `__main__`, sérialisation, processus fils, `hydra.run.dir`, chemins relatifs) ont été examinés dans le code public : aucun ne touche le run.

**Pièces de lancement** : `runs/temoin-bailey-v1-20261111/lancer-conduite-v11.py` (`d279ea19…` ; conduite v9 avec
`lanceur_v17`, le manifeste v5, et 60403564 dans `ANTERIEURES` ; essai à vide sans `GO_ID` : code 2, rien ne tourne) ;
poste `poste-hetzner-v11.sh` (`059d0837…`) et constructeur `construire-donnees-demarrage-v11.py` (`2e9df5ba…`) (v9 avec
la conduite v11 et la garde du commit du code v17 : `src/` de la tête de branche identique à celui du commit `8d1c541e`,
sinon rien ne tourne). Les pièces v10 (conduite `9cb1bd5f…`, poste `406c7fd6…`, constructeur `c79f2c24…`) restent telles
quelles et n'ont jamais tourné : la conduite v10 portait un défaut de syntaxe (deux ouvertures de docstring), vu après
son scellement.

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt (hors les écarts du § 2 et ceux des addenda 1 à 3), lectures 1 à 38 actées (la lecture 12 complétée par
l'addendum 3, § 2.1).

## 5. Risques déclarés
Ceux des addenda 2 (§ 4) et 3 (§ 5), tous gardés. En plus :
- (a) **mort après l'impression de la configuration, avant le premier tour.** Le script public construit, après
  l'impression, le modèle, les données et le journaliseur (`validate_and_create_experiment_config`) : aucune épreuve sans
  carte ne couvre ce chemin (modèle de 8 milliards de paramètres, données sur l'instance). Une mort à ce stade ne laisse
  pas de message (addendum 3, § 2.2) : le diagnostic se borne au nom de la garde, aux durées et à la mémoire. Points de mort
  probables relevés par la contre-lecture du code (lecture du code public seulement) : mémoire et durée de la construction
  de la sonde (représentations du jeu d'entraînement sur 32 couches, lot de 1, puis ajustement), du tour 0 (génération de
  300 jetons, deux époques d'attaque) et du chargement du juge à côté du modèle ; plus en amont, chemin du modèle ou
  fichiers de `./datasets/harmful_dataset/` absents, garde « dossier neuf » du journaliseur. Aucun de ces risques n'est
  introduit par la v4 : la v3 mourait avant de les atteindre ;
- (b) `runpy` n'est pas `python train_harmful.py` à la lettre : le module principal reste `controle_ia…execution_v4`
  dans `sys.modules["__main__"]` (`runpy.run_path` crée un module temporaire et rétablit l'ancien) ; un code qui
  dépendrait de `sys.modules["__main__"]` (sérialisation d'objets définis dans le script, processus fils) se comporterait
  autrement  ; la contre-lecture n'a trouvé dans le code public aucune dépendance de ce genre ;
- (c) Hydra de l'instance (1.3.2, figé) : l'épreuve hors essais l'a joué ; les essais du dépôt jouent 1.3.8 ; sur
  processeur, l'artefact `execution_v3` tombe avec un autre message que sur l'instance, par la même source « paquet » de
  Hydra, que la v4 n'emprunte plus ;
- (d) si la variable `HYDRA_MAIN_MODULE` était définie dans l'environnement de l'enfant, Hydra reviendrait à la voie
  « paquet » ; le code ne la pose pas ; l'environnement de l'image de l'instance n'a pas été lu. Si c'était le cas, le
  message d'erreur de l'addendum 3 sortirait (mort avant l'impression).

## 6. Conditions de lancement (état au scellement)
1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01`, comme aux addenda 2 et 3 ; échéance (2026-11-30) à
revérifier à la création contre création + (B − 2)/c heures, c relevé. 3, 4 : comme à l'addendum 3, inchangées. 5 : comme
à l'addendum 3 : la troisième série ne change pas ce que le verdict vaut pour le témoin. 6 : remplie par cet addendum,
scellé ; il remplace, pour la condition 6, le code de l'addendum 3. Dépôt chez le tiers demandé à la session-dépôt (par
Lazar), avec celui de l'addendum 3 ; s'il n'est pas fait au lancement, l'ordre de lancement le dit et l'addendum n'est
daté que par son commit (précédents des addenda 2 et 3). 7 : le « go (a) » de Lazar, dont l'option nommait « nouvelle
série », est tenu pour mot de lancement, comme à l'addendum 3 (§ 7.3). 8 : pilotage par un poste Hetzner autonome neuf
(v10) ; `DEPOT_URL` du dépôt de travail. Alerte (addendum 3, § 7.2, gardée) : la session alerte Lazar si le pilote n'a pas
fini 4 heures après son lancement, et à toute issue de la liste d'arrêt. Aucune instance avant le scellement de cet
addendum.

## Contre-lecture
À venir (R2).

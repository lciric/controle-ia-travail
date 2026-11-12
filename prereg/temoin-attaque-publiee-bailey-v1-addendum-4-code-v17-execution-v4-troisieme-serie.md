# Addendum 4 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — code v17 : script public lancé comme programme principal ; troisième série après une cause établie

12 novembre 2026, scellé après contre-lecture (R2). Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`),
branche `claude/compassionate-meitner-d4ryyk`. Brouillons archivés tels quels (R12) : brouillon 1
(`brouillons/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-brouillon1.md`,
`878eca8876ea98cdd99433c852ebb5c614252cca47032f29a87387de06071cf2`, écrit avant la contre-lecture du code) ; brouillon 2
(`…-brouillon2.md`, `d49ed4ef4e7115dce30460020dab263847d2f38a89e8b9bf821a12f25cc20851`, contre-lu). Le préenregistrement
et ses addenda 1, 2 et 3 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet
addendum ne contient aucun résultat : aucune note de la boucle (sonde ou juge sur une attaque) n'existe (zéro tour
complet dans toutes les exécutions) et aucune n'a été lue ; seul le contrôle du juge de la mise en place, une garde, a
tourné et passé.

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
   complet ; aucune note de la boucle (sonde ou juge sur une attaque) n'existe ; rien n'a été lu ; la reprise ne peut
   donc pas viser un signe. Une seule série : pilote, au plus une reprise, puis la règle et le run principal selon le
   texte, inchangés. Aucun essai à blanc ne précède : comme à l'addendum 3, § 7.1, le pilote de la troisième série en
   tient lieu ; une nouvelle double chute consomme la série (risques (a) et (e) du § 5). Mêmes graines (pilote
   1394228342, run principal 1865327867) ; sous la graine du pilote, seul le contrôle du juge (garde de mise en place) a
   produit des réponses et des notes du juge ; aucun tour n'a été joué sous l'une ou l'autre graine. La mise en place,
   contrôle du juge compris, est refaite pour la troisième série, sous la même graine. B inchangé : 75 USD,
   fixé à la création de la première instance du poste (60280913, 12 novembre, 00:03:20Z). D continue de cumuler depuis
   cette instance : **2,778 USD après six instances détruites** (liste `ANTERIEURES` de la conduite v11, `d279ea19…`,
   identique à celle de la conduite v10 jamais tournée : elle ajoute 60403564, valeurs de `sortie-conduite-v9/poste-v5.json`,
   à celle de la conduite v9). Les exécutions des séries 1 et 2 sont rapportées comme interrompues. Une nouvelle
   seconde chute du pilote : pas de run principal, pas de verdict ; nœud ; aucune autre série sans nouvelle décision de
   Lazar et nouvel addendum.
3. **Le message d'erreur de l'addendum 3 (§ 2.1 à 2.3) est gardé tel quel**, condition, contenu et portée compris.
4. **Paramètres de lancement** (hors du texte, déclarés) : ceux de l'addendum 3, § 2.5, inchangés (disque 110 Go ; offres
   à 128,9 Go de mémoire allouée au moins ; garde de mémoire vive du texte inchangée ; pilotage par un poste Hetzner
   autonome neuf, v11, `poste-hetzner-v11.sh`, `059d0837…`). Le poste v9 (175884265) reste en marche sur consigne de Lazar ; il ne pilote rien (son script de
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
l'addendum 3, inchangés à ce commit (`lecture_v8`, `journaliseur_v3`, `conventions_v3`, `analyse_v3`). Le code exécuté est identique à celui du commit `60d06b1f` contre-lu ; le commit `8d1c541e` n'ajoute que les essais complétés (C-2), l'épreuve v2 (C-1), la contre-lecture du code et les empreintes. Manifeste neuf
(R12) : `runs/temoin-bailey-v1-20261111/manifeste-local-v5.json` (`111c6e98…`), écrit par
`lanceur_v17.manifeste_depuis_versions_figees` ; sa seule différence avec le manifeste v4 est `commit_code`.

**Essais (R5)** : `tests/test_temoin_bailey_condition6_v17.py` (`c2b498bb…` ; la contre-lecture du code a lu l'état
`6856b0b2…`, dont il ne diffère que par les assertions C-2, 13 lignes, `git diff 60d06b1f 8d1c541e`) : les 161 essais v16 rejoués sur les
modules v17, plus 8 essais v17 : modules et archive ; aucune chaîne exécutée ne nomme `execution_v3`, `instance_v15` ou
`lanceur_v16` ; commande par défaut de l'enfant ; **épreuve réelle de `@hydra.main`** : un mini-clone synthétique
(`configs/` à deux niveaux comme le code public, `obf_reps.logging`, `obf_reps.utils`, `train_harmful.py` portant le même
décorateur) lancé par `python -m controle_ia.temoin_bailey.execution_v4` dans un processus enfant réel — cas sain : code 0,
sortie standard commençant exactement par `configuration_attendue`, journaliseur substitué vu par le script, dossier de
Hydra hors du clone ; **artefact** : le même mini-clone par `execution_v3` échoue sans rien imprimer, comme les pilotes du
12 novembre ; erreur du script propagée (code non nul, aucun repli) ; garde `TESTING` ; même épreuve avec le vrai dossier
`configs/` du code public quand il est fourni. Assertions ajoutées après la contre-lecture du code (C-2 : dossier courant, tête de `sys.path`, module local `evaluate`, graine, `__name__`, `sys.argv[0]`). **Résultats** : fichier v17, 169 essais (161 v16 rejoués, 8 v17) : 168 passés, 1 sauté sans `TEMOIN_BAILEY_CONFIGS_PUBLIQUES`, passé quand il est fourni (rejoué par la contre-lecture de cet addendum : même compte) ; `test_temoin_bailey_analyse_v3.py` et `test_temoin_bailey_condition6_v16.py` : 197 passés. **Suite complète du dépôt** (6 687 essais, ≈ 3 h) : une première passe, arrêtée vers 24 %, a montré 23 échecs, tous dans six fichiers d'autres chantiers, rejoués seuls (23 échecs, 333 passés) : `test_cibles_invisibles_v1.py` (2) et `_v2.py` (1), `test_corpus_arxiv.py` (3, module absent du `.venv`), `test_hote_durable_a1_v3_v3.py` (15 : interpréteur Python 3.13 exigé, branches et GO d'un autre chantier), `test_lanceur_durable_v5_a1v4.py` (1), `test_noter_pilote_a.py` (1) ; aucun n'importe un module de `src/controle_ia/temoin_bailey/` ni un module de l'archive envoyée sur l'instance ; aucun n'a rien poussé (vérifié par `git ls-remote`). Une seconde passe complète tournait au scellement ; son compte est inscrit dans la passation.

**Épreuve hors essais, version figée de l'instance** (Hydra 1.3.2, OmegaConf 2.3.0, Python 3.11.18) :
`runs/temoin-bailey-v1-20261111/epreuve-hydra132-execution-v4-v2.py` (`0677c557…`), sortie `…-sortie-v2.txt` (`316910b9…`, en-tête écrit par le script : interpréteur, emplacements de Hydra et d'OmegaConf, commit du clone, empreinte de `configs/`, empreinte des essais) ; la v1 (`17c3544d…`, sortie `7c204bd5…`, en-tête écrit à la main) reste telle quelle (les empreintes de `configs/` des deux en-têtes diffèrent, `aeeab086…` et `100152d5…`, parce que la v2 hache chemins et contenus : même dossier) : mini-clone synthétique
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
- (b) `runpy` n'est pas `python train_harmful.py` à la lettre. Pendant l'exécution, `sys.modules["__main__"]` est le
  module du script, comme chez les auteurs ; il redevient `execution_v4` au retour. Restent : le module `execution_v4` et
  ses imports déjà chargés, `sys.path` qui porte en plus le dossier `src` du dépôt, et les modules publics importés avant
  l'appel (`obf_reps.logging`, `obf_reps.utils`, `transformers`). La contre-lecture n'a trouvé dans le code public ni
  sérialisation d'objet défini dans le script, ni processus fils, ni lecture de `__file__` ;
- (c) Hydra de l'instance (1.3.2, figé, OmegaConf 2.3.0) : l'épreuve hors essais les a joués ; les essais du dépôt jouent
  Hydra 1.3.8 et OmegaConf 2.3.1 ; sur
  processeur, l'artefact `execution_v3` tombe avec un autre message que sur l'instance, par la même source « paquet » de
  Hydra, que la v4 n'emprunte plus ;
- (d) si la variable `HYDRA_MAIN_MODULE` était définie dans l'environnement de l'enfant, Hydra reviendrait à la voie
  « paquet » ; le code ne la pose pas ; l'environnement de l'image de l'instance n'a pas été lu. Si c'était le cas, le
  message d'erreur de l'addendum 3 sortirait (mort avant l'impression) ;
- (e) **premier passage réel des gardes.** La garde de démarrage et les gardes par tour n'ont jamais été jouées sur une
  exécution réelle du script public (la v3 mourait avant). Une garde qui tomberait à tort, de façon déterministe, au
  pilote ferait tomber aussi la reprise : seconde chute, nœud, sans message d'erreur (garde décidée) ; le diagnostic se
  borne au nom de la garde et à la grandeur en cause. Ce risque n'est pas introduit par la v4 ; il était caché par la
  mort de la v3.

## 6. Conditions de lancement (état au scellement)
1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01`, comme aux addenda 2 et 3 ; échéance (2026-11-30) à
revérifier à la création contre création + (B − 2)/c heures, c relevé. 3, 4 : comme à l'addendum 3, inchangées. 5 : comme
à l'addendum 3 : la troisième série ne change pas ce que le verdict vaut pour le témoin. 6 : remplie par cet addendum,
scellé ; il remplace, pour la condition 6, le code de l'addendum 3. Dépôt chez le tiers demandé à la session-dépôt (par
Lazar), avec celui de l'addendum 3 ; s'il n'est pas fait au lancement, l'ordre de lancement le dit et l'addendum n'est
daté que par son commit (précédents des addenda 2 et 3). 7 : le mot direct de Lazar pour le lancement de la troisième
série. Le « go (a), garde le poste » (22:10Z) approuve une option qui nommait « nouvelle série » ; le § 7.3 de l'addendum 3
ne valait que pour la série de cet addendum (K-3 de la contre-lecture). S'y ajoute, verbatim, le message de Lazar reçu
vers 22:14Z pendant l'exécution de l'option (a), dont la dernière étape est la nouvelle série : « avance en autonomie
pendant 10h » (note `registres/passations/2026-11-12-2320-decision-lazar-bailey-autonomie-10h-mot-de-lancement.md`).
Cette session tient les deux mots ensemble pour le mot direct de lancement ; c'est une lecture de la session, déclarée ici
et rapportée à Lazar avec le lancement (la contre-lecture recommandait un mot exprès). 8 : pilotage par un poste Hetzner
autonome neuf (v11, `poste-hetzner-v11.sh`, `059d0837…`) ; `DEPOT_URL` du dépôt de travail ; l'ordre de lancement relève,
avant la création du poste, que la tête poussée de la branche porte cet addendum scellé, et que l'empreinte du script sans
secrets imprimée par le constructeur v11 est `059d0837…`. Alerte : celle de l'addendum 3, § 7.2, gardée telle quelle
(30 minutes, si le journal le rend visible ; sinon 4 heures après le lancement du pilote) ; en plus, la session alerte
Lazar à toute issue de la liste d'arrêt. Aucune instance avant le scellement de cet addendum.

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-4-code-v17-bailey-v1.md`
(`2db77cc7c7b5a6799e803ceede0ec889b33abe79e1d50b02fbd1cba71d065161`), contre-lecteur neuf, sur le brouillon 2 : « scellable
après corrections », aucun bloquant. Traitement : K-1 (renvois v10 → v11 : § 2.2, 2.4, 6) ; K-2 (risque (b) réécrit, texte
du rapport) ; K-3 (condition 7 : mot direct de Lazar, voir § 6 ; la session y tient pour mot de lancement les deux mots
de Lazar, lecture déclarée) ; K-4 (en-tête et § 2.2 : contrôle du juge) ; K-5 (§ 3 : comptes et échecs nommés) ; K-6
(risque (e)) ; K-7 (essai à blanc, § 2.2) ; K-8 (alerte, § 6) ; K-9 (§ 3 et § 5 (c)) ; K-10 (en-tête, cette section) ;
K-11 (condition 8). **Modifications après la contre-lecture** : la condition 7 cite le message « avance en autonomie
pendant 10h » (non vu par la contre-lecture) ; § 3 : résultats des essais inscrits.

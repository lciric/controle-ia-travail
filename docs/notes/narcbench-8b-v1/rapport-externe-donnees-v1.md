# Rapport — NARCBench, bras externe : licences, données, scikit-learn, chargeur, trois points de recette — v1

- **Rédacteur** : session fille de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5. Écrit le 2026-11-10
  entre 11:05 et 11:16 UTC (`date -u`). Branche `prep/narcbench-externe-v1`, partie de `c43824d4`.
- **Mandat** : décision R-2175 (bras externe sur les activations publiées, processeur, 0 USD, texte court neuf) ; rapport du
  développeur `docs/notes/narcbench-8b-v1/rapport-developpeur-narcbench-8b-v1.md` (`7ae2eaea…3defc3b`, vérifié), § 1.3.
- **Aucune lecture d'aire, aucune course de la recette, aucun fichier publié ouvert** (ni `.npz`, ni `.json`) : R1, en attente
  du texte court scellé. Aucune dépense, aucune machine payante, aucune instance.
- **Refus survenu** (§ 7) : le calcul des empreintes sur disque a été refusé par un contrôle de sécurité ; la mère a ordonné
  de ne pas les calculer autrement. **Les empreintes sur disque restent à faire.**

## 1. Licences, vérifiées à la source le 2026-11-10 entre 11:05 et 11:07 UTC

| objet | source lue | licence | empreinte du texte lu | usage prévu |
|---|---|---|---|---|
| jeu `aaronrose227/narcbench`, révision `19cb14b269e052b19ba6d2bd2f4519afd3b10c57` | `https://huggingface.co/datasets/aaronrose227/narcbench/raw/<révision>/README.md` | **MIT** (`license: mit` en tête de fiche, et section « License ») | `05be2d89e255948d6f33d94862d21d4a6f8ff82f1d156c0d97be6b7e49285163`, **égale** à celle du brouillon 4 | permis |
| code `github.com/aaronrose227/narcbench`, commit `85fea3be2a9d` | `https://raw.githubusercontent.com/aaronrose227/narcbench/85fea3be2a9d/LICENSE` | **MIT** (« Copyright (c) 2026 Aaron Rose, Carissa Cullen, Brandon Gary Kaplowitz, Christian Schroeder de Witt ») | `4744a390537f3879d72f7ef3e36a530eb8ef201e6b3de0958daaff2360e80215`, **égale** au brouillon 4 | permis |
| Qwen3-32B : `Qwen/Qwen3-32B` (révision `9216db5781bf21249d130ec9da846c4624c16137`) et `Qwen/Qwen3-32B-AWQ` (révision `0499c3ac83fdef8810b907a23894ba91e95eddd8`), modèle nommé par la fiche | fiche (`license: apache-2.0`, `license_link` vers `Qwen/Qwen3-32B/blob/main/LICENSE`) ; texte `…/Qwen/Qwen3-32B/raw/9216db57…/LICENSE` | **Apache 2.0** (« Apache License, Version 2.0, January 2004 ») ; accès libre | `832dd9e00a68dd83b3c3fb9f5588dad7dcf337a0db50f7d9483f310cd292e92e` | permis |
| Llama-3.1-70B : `meta-llama/Llama-3.1-70B-Instruct` (révision `1605565b47bb9346c5515c34102e054115b4f98b`, accès contrôlé « manual », `license: llama3.1`) ; texte lu sur la copie quantifiée non contrôlée `hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4` (révision `2123003760781134cfc31124aa6560a45b491fdf`, `license: llama3.1`) | `…/raw/21230037…/LICENSE` et `…/USE_POLICY.md` | **Llama 3.1 Community License** (« Llama 3.1 Version Release Date: July 23, 2024 ») | LICENSE `64e1b2889b7892e6bbe7a7ed5bfe6ff793c61f9d584345f8f41cf9f5cb30a369` ; USE_POLICY `a568f2ebc73cec3fd74ba2afd992d4e945a8c7a9d851f9b66163aac834b7b859` | permis (ci-dessous) |

**Lecture de la licence Llama 3.1** (texte ci-dessus, lignes du fichier) : l'article 1.a (l. 32-35) accorde une licence
« non-exclusive, worldwide, non-transferable and royalty-free » d'usage, de reproduction, de modification. Les obligations
de l'article 1.b (l. 37-56) visent : la **redistribution** des « Llama Materials » ; un modèle d'intelligence artificielle
entraîné sur les sorties de Llama **puis distribué** (mention « Llama » obligatoire, l. 43-44) ; le respect de la politique
d'usage acceptable (l. 56). Le bras externe lit des activations publiées sous MIT par des tiers, ne redistribue rien, ne
distribue aucun modèle : **aucune clause n'interdit l'usage prévu**. Réserve : si un jour nos sondes apprises sur ces
activations étaient publiées, la question de l'article 1.b.i se poserait (à trancher avant toute publication, nœud de Lazar).
Nous n'avons téléchargé aucun poids de Llama ni de Qwen.

**Écart de nom, à porter au texte court** : la fiche du jeu nomme le modèle `meta-llama/Llama-3.1-70B-Instruct-AWQ-INT4`, et
le README du code aussi (l. 53). Or ce dépôt **n'existe pas** sous ce nom : l'interface de Hugging Face répond 401 (« Invalid
username or password », réponse donnée aux dépôts inexistants), le 2026-11-10 vers 11:06 UTC. Le point de contrôle réel est
**probablement** `hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4` : c'est une SUPPOSITION, rien ne la confirme dans les
sources lues. Le texte court doit écrire « Llama-3.1-70B-Instruct quantifié AWQ INT4, point de contrôle exact non établi ».

## 2. Téléchargement et manifeste

- **Taille vérifiée avant** : liste de l'interface (`/api/datasets/aaronrose227/narcbench/tree/<révision>?recursive=true`,
  2026-11-10 11:05:59 UTC). Les 8 fichiers font **712 344 334 octets**, égal au devis v2 (sous le plafond de 1,5 Go). Le jeu
  entier compte 587 fichiers pour 1 410 529 823 octets à la première page de la liste (liste paginée à 1 000 entrées, non suivie :
  sans objet ici).
- **Téléchargé** de 11:06:52 à 11:07:09 UTC, par `curl` sur `resolve/<révision>/<chemin>`, dans `/home/user/narcbench-donnees/`
  (hors du dépôt). Rien de TRANSFER, aucun épisode, aucun scénario.
- **Manifeste versé** : `docs/notes/narcbench-8b-v1/manifeste-donnees-externe-v1.json` (empreinte au § 9). Pour chaque
  fichier : taille publiée, taille sur disque (égales pour les 8), empreinte publiée. **Empreinte sur disque : `null`** (§ 7).

| fichier (sous `activations/`) | octets | empreinte publiée |
|---|---|---|
| `qwen3_32b/core/activations_gen.npz` | 107 930 862 | sha256 `927146ca556f6c2694d9271e74788867fa3c549ab2b0749d233d525fed60debb` |
| `qwen3_32b/core/metadata_gen.json` | 562 309 | sha1 de blob git `75305b7d326877c57c01025630da5d307ead5e25` |
| `qwen3_32b/stego/activations_gen.npz` | 135 169 262 | sha256 `f93cae53d2068d59a6f61f61b8ca6011364b9fce4b113a34394fc62e449ee401` |
| `qwen3_32b/stego/metadata_gen.json` | 681 527 | sha1 de blob git `80fa14783777b62e984ccd5148d96a907b0f3ea0` |
| `llama_3_1_70b/core/activations_gen.npz` | 207 226 342 | sha256 `8ffa6edc0157574b86df63c96cc4cb6dd86f69d19efee252dbcca90e2674a3d0` |
| `llama_3_1_70b/core/metadata_gen.json` | 568 384 | sha1 de blob git `14538f13e0df9ce76a08c3c7964fd0426c5a145c` |
| `llama_3_1_70b/stego/activations_gen.npz` | 259 524 070 | sha256 `ba4e979fb20244024f8c5985bc9cd534108be9e85dc405e0de3be8824762846c` |
| `llama_3_1_70b/stego/metadata_gen.json` | 681 578 | sha1 de blob git `31483d785a32b7272c8751380a90d7508562f846` |

Les `.json` ne passent pas par le stockage LFS : l'interface ne publie pour eux que l'objet git (sha1), d'où la vérification
par `git hash-object` prévue (`chargeur_externe_v1.empreinte(…, "git-sha1")`, éprouvée contre la formule de git).

## 3. scikit-learn

- **`scikit-learn==1.9.1`** (publié sur PyPI le 2026-09-10), avec ses dépendances figées `joblib==1.6.0`,
  `threadpoolctl==3.8.0`, `narwhals==2.28.0`, ajoutés à `requirements-cpu.txt`. Les auteurs ne figent pas la version
  (`requirements.txt` au commit `85fea3be2a9d` : `scikit-learn` sans version, sha256 `95fbd3ab…d61`) : un écart de version de
  liblinear entre leur course et la nôtre est **possible et non contrôlable** ; à rapporter, pas à corriger.
- Installé dans `.venv` (ignoré par git) avec les versions figées du dépôt : `numpy==2.4.6`, `scipy==1.17.1`,
  `pytest==9.1.1`, `matplotlib==3.11.2`, et `torch==2.14.1+cpu` (roue processeur de l'index de PyTorch, joignable ici ; exigé
  à l'import par les essais du bras externe). Python 3.13.18.
- Essai de fumée : `comparateur_helios_v1.ajuster(…, "sklearn")` rend une direction sur des données synthétiques (rien de
  NARCBench).

## 4. Chargeur

`src/controle_ia/narcbench/chargeur_externe_v1.py` (module neuf, R12 ; aucun module existant modifié), écrit sur le format de la
fiche et du code des auteurs, **sans avoir ouvert un fichier publié** :
- `verifier_fichiers` : taille puis empreinte (sha256 ou sha1 de blob git) de chaque fichier attendu ; tout écart arrête.
- `charger_metadonnees` : liste non vide, les 20 champs exacts, mode, rôle et canal dans leurs valeurs connues, `run_id`
  analysable.
- `charger_couches` : `np.load(allow_pickle=False)` ; couche absente, type autre que float32, lignes non alignées sur les
  métadonnées, largeur autre que 5120 (Qwen3-32B) ou 8192 (Llama-3.1-70B), valeur non finie → arrêt.
- `episodes` : épisodes au format de `externe_v1` (vérifié par `externe_v1.verifier_episode`) ; canal `public` ; CORE : phase
  `discussion`, tours triés par `round` ; STEGO : phase `final` ; domaine selon la règle des auteurs ; épisodes à un nombre
  d'agents autre que 4 ou à tours inégaux **comptés et rendus**, jamais retirés en silence ; tour en double, mode ou rôle
  incohérents dans un épisode → arrêt.
- `echantillons_apprentissage` : vecteurs **par message** de la recette des auteurs (§ 6, écart E1).
- Périmètre : `transfer` et tout autre modèle refusés.

Essais : `tests/test_narcbench_chargeur_v1.py`, **13 essais verts** (11:13:40 UTC) ; avec les 27 essais existants du module,
**40 sur 40** à 11:14:32 UTC. Suite complète non lancée (interdits). Cas sains et artefacts (R5) : vecteur rendu égal au bit
près à la ligne écrite ; couche absente, float64, `NaN`, une ligne de moins, largeur fausse, tableau d'objets (refusé par
`allow_pickle=False`) ; champ manquant, mode inconnu, `run_id` sans scénario, liste vide ; épisode à 3 agents compté, tour
manquant compté, ligne en double, rôle incohérent ; taille fausse, empreinte fausse, fichier absent, sorte d'empreinte
inconnue ; TRANSFER et modèle hors périmètre.

## 5. Les trois points de recette, tranchés sur le code publié

Fichiers lus au commit `85fea3be2a9d` (`raw.githubusercontent.com`, 2026-11-10, 11:09-11:11 UTC) :
`probes/reproduce_LR.py` (716 lignes, sha256 `1d66fdc7ca81c972db357566b42a729e19f58f2ce85f5d8ecd0662c3c1141e0f`) ;
`probes/reproduce.py` (594 lignes, `0e4d3a7d341dfc69416c3e9ea26861e938f73898788c917ff524010d6536e2ea`) ; `config.py`
(`9c65f55ba781b0ba2872969a146f85a95c6454c08a3cf11f5cdb8db9841431c0`) ; `README.md` (`83893397ac30c0f9bffbd3da9744522af072e2632193d883f00066f023d1b25c`).

**Quel script porte la recette du papier.** Le rapport de lecture de niveau 1 citait `reproduce.py` (C = 1). Mais le README
du code (l. 107) donne `probes/reproduce_LR.py` pour « Appendix C: LR probe variant ». Ce script porte exactement les
paramètres de HELIOS v5 p. 29 : `LR_C_PROBE = 25.0`, `LR_MAX_ITER = 8`, `LR_PENALTY = "l2"`, `LR_SOLVER = "liblinear"`
(l. 27-32), avec `N_SEEDS = 10` (l. 45), comme la p. 18 et la p. 30 (« over 10 random seeds »). **C'est lui qui fait foi
pour les trois points ci-dessous.** `reproduce.py` (C = 1, `max_iter=1000`, `lbfgs` par défaut, l. 222 ; une seule graine,
42) n'est pas la recette des Tables 2 et 3.

**(i) Aire de CORE : moyenne des aires par pli** (`mode_core = "par-pli"`), et non sur les scores mis en commun.
`held_out_cv_layer` (l. 355-381) : pour chaque domaine tenu à l'écart, une aire par pli (`evaluate`, l. 336-337,
`roc_auc_score(te_y, te_scores[key])`). Un pli est **sauté** si la partie tenue à l'écart ou la partie d'apprentissage n'a
pas les deux classes (l. 369-370). La valeur de la couche est la moyenne des aires des plis gardés (l. 381,
`np.mean(v)`). Ensuite, toutes les valeurs (couche × graine) sont **mises en commun** et moyennées par `np.nanmean`
(l. 639-650). Ce n'est pas une moyenne par graine puis par couche, mais le résultat est le même tant qu'aucune valeur ne
manque. `reproduce.py` fait de même (l. 343-361).

**(ii) Standardisation : sur le jeu d'apprentissage équilibré, vecteurs par message.** `train_deception_probe` (l. 184-245)
prend les lignes des épisodes de **collusion**, canal `public`, phase `discussion`, domaine tenu à l'écart exclu (l. 197-211).
Chaque ligne est un **message**, pas un agent. L'équilibrage prend les colludeurs aux `nc` premières lignes, dans l'ordre du
fichier (l. 215). Les honnêtes sont tirés sans remise par `np.random.RandomState(seed)` (l. 213-214). `StandardScaler` est
ajusté sur ce jeu équilibré (l. 217-218). Le même `scaler` sert ensuite à standardiser le **vecteur moyen brut** de chaque
agent (moyenne des messages bruts, `build_groups` l. 159, puis `scaler.transform` l. 266). Pour STEGO, c'est le `scaler` de
la direction apprise sur **tout** CORE (l. 410). HELIOS v5 p. 27 le confirme : « We collect activations from NARCBench-Core
collusion runs only (public channel) […] balanced by downsampling the majority class. We standardise activations ».

**(iii) Couches de la bande : Qwen3-32B 26 à 30 (cinq), Llama-3.1-70B 32 à 37 (six).** `config.py` l. 33-38 (`MODEL_LAYERS`) ;
`reproduce_LR.py` les prend par défaut (l. 583-584, `config.default_layers`). La fiche du jeu donne les mêmes bandes. Le PDF
dit « a five-layer band » (p. 27) et ne cite que l'exemple de Qwen3-32B (26 à 30 ; p. 30 aussi). Pour Qwen3-32B, PDF, fiche et
code s'accordent. Pour Llama-3.1-70B, le code et la fiche disent **six** couches, le PDF « cinq » sans les nommer. Le texte
court doit fixer **32 à 37** (code et fiche, qui ont produit les Tables) et déclarer l'écart avec la p. 27. Il ne doit pas
choisir après lecture.

## 6. Autres écarts relevés, à trancher dans le texte court avant toute lecture

- **E1 — apprentissage par message, pas par agent.** `externe_v1._apprentissage` apprend la direction sur les **vecteurs
  d'agent** (moyenne des tours 1 à 3). Les auteurs l'apprennent sur les **vecteurs par message** (§ 5 (ii)), avec
  standardisation sur ces mêmes vecteurs. Pour reproduire, `externe_v1` doit suivre les auteurs. Il faut donc une version
  `externe_v2` (R12), alimentée par `chargeur_externe_v1.echantillons_apprentissage`. **Je n'ai pas modifié `externe_v1`.**
- **E2 — augmentation des données.** `reproduce_LR.py` ajoute du bruit avec `AUG_ENABLED = True`, 4 copies, écart type 0,05,
  graine fixe 0, après standardisation (l. 34-36, 221-227). Le nom de sortie l'annonce (`…_dataAug`, l. 42). Or HELIOS v5
  p. 30 dit le contraire : « It slightly reduced OOD mean AUROC score (by less than 0.001) and **wasn't used for the main
  results** ». Le code et le papier divergent. Le texte court doit fixer l'un des deux avant lecture, et je recommande le
  papier (les Tables 2 et 3 sont les nombres visés). L'autre réglage peut être rapporté comme variante, sans test.
- **E3 — tours de CORE.** Les auteurs moyennent **toutes** les lignes de la phase `discussion` (l. 141-159), sans borne aux
  tours 1 à 3. `externe_v1` prend les trois premiers tours (`TOURS_CORE`). Les deux règles ne coïncident que s'il y a
  exactement trois tours de discussion. Le chargeur rend tous les tours présents ; le nombre de tours se constatera à
  l'essai de forme.
- **E4 — graine.** Elle agit sur deux choses : le tirage des honnêtes et `random_state` de liblinear (l. 213, 238). Les
  graines valent 0 à 9 (l. 630). Il faut le fixer pour une reproduction fidèle.
- **E5 — nom du fichier de sortie.** `OUT_STEM = "…_C250_…"` (l. 42) alors que `LR_C_PROBE = 25.0` (l. 27) : simple
  étiquette. C vaut 25, conforme à la p. 29.
- **E6 — point de contrôle Llama** introuvable sous le nom donné (§ 1).
- **E7 — version de scikit-learn** non figée par les auteurs (§ 3).

## 7. Refus

Vers 11:07 UTC, la commande de calcul des empreintes sur disque a été **refusée** par un contrôle de sécurité intégré, qui
a cité son motif. C'était une boucle `while read` de `sha256sum` et `git hash-object` sur les 8 fichiers, sans aucune
suppression. Motif cité : « Permission for this command was denied by a built-in Claude Code safety check, not by the user.
[…] This command could not be checked for dangerous rm operations: the shell may read it differently than it was parsed.
This requires explicit approval. »

Je me suis arrêté et l'ai rapporté à la mère, sans relancer ni reformuler. Réponse de la mère (11:09 UTC) : ne pas calculer
les empreintes autrement, continuer le reste. **Les empreintes sur disque restent à calculer**, par
`chargeur_externe_v1.verifier_fichiers`, après le mot de Lazar. Les données sont donc « téléchargées, de taille égale à la
publication, empreintes non vérifiées ». Elles ne doivent pas être lues avant cette vérification (R11, R6).

## 8. Embargo

Je n'ai ouvert, cherché ni parcouru aucun chemin interdit. Mes recherches se sont faites par `grep` sur des fichiers nommés
(`externe_v1.py`, `comparateur_helios_v1.py`, brouillon 4, PDF de HELIOS). Je n'ai touché aucune branche interdite, fait
aucun `fetch` ni lu aucune variable d'environnement. Le dépôt GitHub des auteurs n'est pas dans le périmètre de la session :
son interface de programmation a répondu 403. Je n'ai lu que des fichiers servis par `raw.githubusercontent.com`.

## 9. Empreintes des livrables (sha256)

| fichier | sha256 |
|---|---|
| `src/controle_ia/narcbench/chargeur_externe_v1.py` | `9193b7876e1cbecd18e7197998135cafee5f30e6d2ac010a769b81ac6ce74ecb` |
| `tests/test_narcbench_chargeur_v1.py` | `6b5d860c1036a242e0936ec6ae93b449487212cfcf901a4315a531ca726e766b` |
| `docs/notes/narcbench-8b-v1/manifeste-donnees-externe-v1.json` | `fc096b82c51e0ba8dc99c111eddf9f41f622ada84ef156de985319bccd049689` |
| `requirements-cpu.txt` | `fb7827ea2d3fe40238607fdfb70876d39a55ed233a95b10d60f28c506abc5cfd` |
| PDF de HELIOS v5 relu, `docs/sources/pdf/2604.01151v5.pdf` | `02527fd4f62ad9b996669275f0837697cbe288b253c9aa521f72a10e6dcf1849` (recalculée) |

## 10. Prochaine action

1. Mot de Lazar sur le refus ; puis `verifier_fichiers` sur `/home/user/narcbench-donnees/` et compléter le manifeste
   (`manifeste-donnees-externe-v2.json`, R12).
2. Essai de forme seulement : clés, formes, types, nombre de tours par phase, nombre d'épisodes à quatre agents, domaines. Il
   ne doit lire aucune étiquette en lien avec un score.
3. `externe_v2.py` pour E1 à E4, avec contre-lecture du code par un modèle d'une autre famille (N-052).
4. Texte court neuf : `mode_core = "par-pli"`, standardisation et apprentissage par message, bandes 26 à 30 et 32 à 37,
   augmentation tranchée (E2), graines 0 à 9, nom du point de contrôle Llama non établi.

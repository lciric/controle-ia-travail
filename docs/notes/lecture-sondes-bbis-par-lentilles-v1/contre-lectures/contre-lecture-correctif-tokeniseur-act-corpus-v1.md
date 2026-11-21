# Contre-lecture du correctif du tokeniseur pour le script voisin du corpus des jetons gardés (lanceur de la version 9) — v1

Écrite le 2026-11-21 par un contre-lecteur neuf (pas l'auteur du code, d'un autre modèle que lui), sous le mandat scellé
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-contre-lecteur-correctif-tokeniseur-act-corpus-v1.md`
(`5ff84b98ddb9ecd998e6dd7aa498d3f23abbdb74cbd2c11cf18aa05ac79a4067`, vérifié par `controle_ia.scellement verifier`). Branche
`claude/brave-galileo-jhp684`, commit `3796893db`. Aucune requête vers Hugging Face, aucun téléchargement, aucune clé lue.

## Verdict

**Conforme.** Le lanceur de la version 9 et le module `cache_tokeniseur_v2` peuvent remplacer le lanceur de la version 8 pour la
première passe : le marqueur d'absence suffit, aux versions épinglées, pour que la bibliothèque ne demande plus le fichier à l'hôte ;
la liste des trois noms est complète pour le tokeniseur de Llama 3.1 ; rien de ce que le texte de lecture v1 scellé exige n'est changé.
Que le chargement réussisse réellement dans l'enfant sans clé est établi sur le code installé et sur une porte simulée fidèle ; sur
la machine de la course, l'essai en ligne ajouté le tranche avant tout flux long. Deux corrections non bloquantes sont demandées
(section « Corrections demandées »).

## Pièces vérifiées (empreintes)

| pièce | empreinte | vérification |
|---|---|---|
| mandat du développeur | `4420c6df06ff…` | `scellement verifier` : OK |
| note du développeur | `cecbad871f52…` | `scellement verifier` : OK |
| `cache_tokeniseur_v2.py` | `fb4069f71bd3e37fa1188ab3f733138a62223c6cd969b72f1e0f3c091a650f4a` | `sha256sum` : égale au mandat et à la note (le code n'a pas d'empreinte compagnon ; `verifier` le dit, attendu) |
| `lanceur_v9.py` | `89d2e23b61ff2a6741aae20e6caca483df0d2c6f1d66235e9f3d20b772f4a065` | `sha256sum` : égale |
| `lanceur_v8.py` | `0bba5d4e68fd193ded87426105252bdf554c7c93b9e422164916d1b6b7df57b3` | `sha256sum` : égale |
| `montage_v1.py`, `constantes_v1.py` | `199e5e18…`, `9c991d0e…` | `sha256sum` : égales à la note |
| outils : fabrique v9, essai des essais et sa sortie, porte locale et sa sortie | `914251be…`, `565a1009…`, `57fc63e1…`, `2a4ea93c…`, `0a40c93c…` | `scellement verifier` : OK (cinq) |
| texte de lecture v1 (`origin/main`) | `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572` | `git show` puis `sha256sum` : égale |
| trace `traces/hf-revisions-20261006-1645/` | — | `sha256sum -c empreintes.sha256` : trois OK |

Environnement : `.venv` du dépôt, `transformers` 5.18.0, `tokenizers` 0.23.2, `huggingface_hub` 1.33.0, égaux à `requirements-cpu.txt`.

## Points du mandat

### 1. Mécanisme — tenu
- `huggingface_hub/file_download.py`, `try_to_load_from_cache` (l. 1588-1601) : `refs/main` est lu et converti en commit, puis un fichier
  `.no_exist/<commit>/<nom>` rend `_CACHED_NO_EXIST`, **avant** tout regard sur l'instantané.
- `transformers/utils/hub.py`, `cached_files` (l. 516-530) : quand la révision est un commit épinglé (`_pinned_commit_hash` : un
  `ResolvedRevision` ou un identifiant de commit), chaque nom est cherché dans le cache ; un fichier présent **ou marqué absent** compte ;
  si tous comptent, la fonction rend sans aucun appel à l'hôte. Le marqueur suffit donc, en ligne.
- Fichiers demandés (`tokenization_utils_base.py`, l. 1626-1637 et 1701-1722) : `vocab_files_names` de la classe plus
  `added_tokens.json`, `special_tokens_map.json`, `tokenizer_config.json`, `tokenizer.json`, `chat_template.jinja`. Pour Llama 3.1
  (`tokenizer_class` « PreTrainedTokenizerFast », `model_type` « llama »), `AutoTokenizer` (`tokenization_auto.py`, l. 840-885) mène à
  `TokenizersBackend` (`vocab_files_names` = `tokenizer.json`, `tokenizer.model`) ; la voie `LlamaTokenizer`, si elle était prise, a les
  mêmes noms. Posés : `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json` (et `config.json`, lu par `AutoConfig`). Non
  posés : exactement `tokenizer.model`, `added_tokens.json`, `chat_template.jinja`. **La liste est complète.**
- Autres demandes : `list_repo_templates` (arbre de `additional_chat_templates`, interface), `list_repo_files` (interface, erreurs
  avalées), `resolve_revision` (interface) — aucune n'est un fichier à porte. `generation_config.json`, fichiers du processeur : non
  demandés par `AutoTokenizer`. La recherche d'un fichier SentencePiece (`find_sentencepiece_model_file`) et le correctif de Mistral
  (`_patch_mistral_regex`) ne sont pas pris ici (le second avale toute erreur de l'interface).
- Pièce indépendante : l'arrêt relayé est tombé sur `…/resolve/0e9e39f2…/tokenizer.model` ; or `list_repo_templates` relance un refus de
  dépôt à porte sur l'arbre. Le chargement réel a donc passé la résolution et la lecture de l'arbre sans clé : c'est le monde « A » de la
  porte locale, celui où les marqueurs suffisent.

### 2. Révision — tenu, avec une réserve non bloquante
- `catalog.tokenizer` appelle `AutoTokenizer.from_pretrained(model)` sans révision (copie versée, l. 113-115) ; `resolve_revision`
  (`hf_api.py`, l. 3654 et suiv.) résout la branche principale par `repo_info` sans clé (`HF_HUB_DISABLE_IMPLICIT_TOKEN=1`, clé retirée
  de l'enfant, `HF_HOME` neuf sans fichier de jeton). La trace du 2026-10-06 (réponse de l'interface publique sans jeton, champ `sha` =
  `0e9e39f249a16976918f6564b8830bc894c89659`) et la forme de l'arrêt relayé montrent que l'interface répond sans clé.
- Si la branche a bougé : `_cache_commit_hash_for_specific_revision` (`file_download.py`, l. 727-743) **réécrit** `refs/main` ; le cache
  posé n'est plus lu ; les fichiers sont demandés au nouveau commit, refus du dépôt à porte. L'essai en ligne s'arrête alors **avant tout
  flux long** (arrêt nommé « le code voisin ne lit pas le tokeniseur en ligne et sans clé … »), journal à l'appui ; l'essai de limite du
  module le montre. Réserve : le message d'arrêt ne nomme pas la cause (la relecture du cache, qui la nommerait, n'est jouée qu'après un
  essai réussi) — correction non bloquante 1. Si la branche bougeait entre l'essai et le script du corpus (des heures plus tard), l'arrêt
  tomberait au même point qu'avant le correctif ; risque faible (dépôt inchangé depuis 2024 d'après la trace), dit ici.

### 3. Garde « fichier présent dans l'arbre » — tenu
- `racine_du_depot` lit `url_arbre(depot, revision)` (`recursive=false` : racine seule), à la révision épinglée, par le transport et avec
  la clé — même adresse que `montage_v1.sha256_par_interface`, même hôte. La clé ne sort que par `Cle.valeur()` dans
  `TransportRequests._ouvrir`, refusée hors de l'hôte de Hugging Face ; les messages de `RefusReseau` ne portent que l'URL sans requête et
  le code ; le module ne lit pas la valeur.
- `exiger_absents` arrête si un nom à marquer figure dans la racine, **quelle que soit sa sorte** (fichier ou dossier), avant toute
  écriture (`poser_cache_tokeniseur` lit et vérifie l'arbre avant `mo.poser_cache_tokeniseur`) ; le témoin exige chaque fichier posé
  comme fichier. Arbre de la trace : quinze entrées de racine, ni `tokenizer.model`, ni `added_tokens.json`, ni `chat_template.jinja` à la
  racine (seulement `original/tokenizer.model`). Aucun marqueur ne peut être écrit pour un fichier que le dépôt porte.

### 4. L'essai en ligne et sans clé (nœud 1 du développeur) — tenu
Utile : il joue exactement le chargement du script du corpus (`catalog.tokenizer`, même environnement d'enfant, `hors_ligne=False`),
avant les flux de poids. Sans risque pour la clé : `environnement_enfant` retire les quatre variables de clé ; aucun fichier de jeton dans
`HF_HOME`. Requêtes : vers `huggingface.co` seulement (interface du dépôt), hôte déjà essayé par l'essai d'un octet du texte (« Plan
d'analyse », point 4) ; aucun fichier téléchargé. Le texte n'exige ni n'interdit une garde de cette forme ; elle arrête « avant tout
téléchargement long », comme la liste d'arrêt le demande pour un refus de Hugging Face. Retirable en trois lignes du montage, une fonction
et une garde de la liste. Je le tiens dans l'objet du correctif.

### 5. Lanceur v9 = v8 à ce seul changement près — tenu
`diff lanceur_v8.py lanceur_v9.py` : docstring (paragraphe « Version 9 »), import de `cache_tokeniseur_v2`, `MODULES` (quinze, compté),
pose du cache par `ct.poser_cache_tokeniseur` (fichiers posés inchangés : `.json` hors index ; `attendus` tirés de `r.petits`, valeurs du
texte), essai en ligne puis `ct.exiger_cache`, deux champs du rapport, deux gardes de la liste. Aucune ligne de calcul changée.
`empreintes_du_code` couvre les quinze modules ; `exiger_fiche_code` exige l'empreinte de chacun (l'essai v9 voit d'abord manquer
`cache_tokeniseur_v2.py`). Aucune clé exposée. Copies v9 des essais : différences avec la v8 relues (jouets : arbre de la racine complété
des petits fichiers et du dossier `original` ; essais du lanceur : quinze modules, gardes neuves vérifiées à part) ; conformes à la note.

### 6. Essais — tenu
- Artefact (R5) : `test_artefact_l_ancien_cache_en_ligne_et_sans_cle_refus_du_depot_a_porte_sur_tokenizer_model` reproduit, par le vrai
  chargement dans un enfant, le refus 401 sur `…/resolve/<révision>/tokenizer.model` avec l'ancien cache ; un marqueur retiré à la fois :
  refus sur ce nom (trois cas) ; cas sain : aucun fichier demandé, aucune requête avec clé, cache inchangé après.
- Essai des essais : 32 défaites, 32 vues (sortie scellée relue), dans une copie jetable hors du dépôt ; il ne couvre que le module, les
  appels du lanceur étant tenus par trois essais dédiés (deux essais joués, essai en ligne en échec, branche réécrite).
- Porte locale fidèle : interface sans clé, fichiers refusés par 401 avec `X-Error-Code: GatedRepo`, 404 `EntryNotFound` pour un chemin
  absent ; tokeniseur jouet à `tokenizer_class` « PreTrainedTokenizerFast » et `model_type` « llama », comme le réel ; la sortie montre la
  classe `TokenizersBackend` et l'ordre de demande `tokenizer.model` puis `added_tokens.json`, cohérent avec l'arrêt relayé. Monde « B »
  (interface à porte) : échec sur l'arbre des gabarits, différent de l'arrêt relayé, donc écarté.
- Rejoués ici : `tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py` et `tests/test_lentilles_sondes_bbis_lanceur_v9_*.py` :
  156 essais, 156 réussis, 0 échoué.

### 7. Script du corpus (nœud 2 du développeur) — tenu (non versé, dit)
`scripts/05_act_corpus.py` n'est **pas** versé dans `docs/sources/neuron-lens-lecture-20261113/` (copies : scripts 01, 02, 06, 07, 08,
10 et `catalog_box.sh`). Ce qui en est dit ailleurs (README l. 554 et 587, `docs-design.md` l. 299-311, `arch.py` l. 260-265) : il lit les
jeux de données et met la tranche « chat » dans le gabarit de conversation, porté par `tokenizer_config.json` (posé). Rien n'y indique une
demande au dépôt à porte autre que le tokeniseur, mais ce n'est pas établissable sans le script : si une autre demande existe (par exemple
une configuration non posée), l'arrêt tombera plus loin, sans dépense de calcul mais après les flux de poids. Risque déclaré.

### 8. Autres écarts — aucun bloquant
- Un échec du paquet entier relevé par le développeur (dépendance d'ordre d'un essai de la seconde passe) n'est pas du correctif ; je ne
  l'ai pas rejoué (hors du mandat).
- La seconde passe porte le même défaut (note du développeur) : à reprendre dans sa version neuve.

## Corrections demandées
1. (non bloquante) En cas d'échec de l'essai en ligne, relire le cache (`ct.exiger_cache`) pour nommer la cause quand la branche du dépôt
   a bougé, plutôt que le seul message générique.
2. (non bloquante) Verser une copie de `scripts/05_act_corpus.py` au commit du voisin quand une lecture publique le permet, pour fermer le
   nœud 2.

## Cloisonnement et expositions
Lus : le mandat, `CLAUDE.md`, les pièces listées ; du texte de lecture v1, le « Plan d'analyse » points 1 à 5 et les lignes cherchées par
mot (hôte, cache, en ligne, `05_act`) hors du paragraphe « Jamais ouverts » (lignes 245-262 non affichées) ; de la trace, le champ `sha`
et la liste des fichiers seulement. Jamais lus : `diag/`, `runs/`, `docs/verdicts/`, branches `calcul/*`, `donnees/*`, `verdict/*`,
aucune sortie de course, aucun `arret.json`. Aucun intitulé interdit vu. Aucun refus d'outil.

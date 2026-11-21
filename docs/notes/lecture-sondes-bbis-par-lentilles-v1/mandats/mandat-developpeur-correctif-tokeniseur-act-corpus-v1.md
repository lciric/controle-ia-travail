# Mandat du développeur neuf — correctif du tokeniseur pour le script voisin du corpus (première passe, lanceur v9) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, à la demande de la mère (message direct de 18:11Z),
sous les mots de Lazar « turbo max » et « go tu as mon mot pour tout » (GO-2026-11-21-63). Pièce de travail (classe C) ; code de classe B,
contre-lu par un agent neuf d'un autre modèle.

## Le défaut, tel que la mère le relaie (tu ne lis aucune sortie de course ni la branche calcul/*)
Le montage `20261121-180157-lentilles-bbis-v1` (lanceur v8) a passé la pagination puis s'est arrêté, code 3, dans le script voisin
`scripts/05_act_corpus.py` (ligne 54) : `GatedRepoError` 401 sur `tokenizer.model` du dépôt à porte `meta-llama/Llama-3.1-8B-Instruct`,
révision `0e9e39f2…`. Notre `montage_v1.calculer_jetons_gardes` (l. 621-622) lance ce script **en ligne**, avec `environnement_enfant`
(l. 90-98) qui retire la clé et pose `HF_HUB_DISABLE_IMPLICIT_TOKEN=1` ; `poser_cache_tokeniseur` (l. 584-596) ne pose que les petits
fichiers `.json` vérifiés, et `tokenizer.model` n'est pas dans le cache. Le tokeniseur se charge par `catalog.tokenizer` →
`AutoTokenizer.from_pretrained` (copie versée : `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-catalog.py.txt`,
l. 113-115 ; script : `scripts-05_act_corpus.py.txt` s'il est versé, sinon ce que le dossier porte).

## Le travail — le plus petit correctif, rien d'autre
1. Lis `CLAUDE.md`, le mandat `mandat-developpeur-deux-passes-lentilles-v1.md` (0a9517ea… ; **ses règles de cloisonnement, de lecture et
   de travail valent pour toi**), le mandat et la note du correctif de la pagination (`mandat-developpeur-correctif-pagination-corpus-v1.md`,
   `developpement/notes-correctif-pagination-corpus-v1.md`), et du texte de lecture v1 scellé (`prereg/lecture-sondes-bbis-par-lentilles-v1.md`,
   ca5066d7…, **sans la liste « Jamais ouverts »**) ce qu'il dit du montage, du cache, de la clé et des scripts du voisin.
2. Établis d'abord, sur pièces versées seulement (copies du voisin, `constantes_v1.PETITS_LLAMA`, arbre du modèle tel que le code le
   connaît), si `tokenizer.model` existe à la racine du dépôt à cette révision. Ne fais **aucune** requête réseau ; si ce n'est pas
   établissable sur pièces, dis-le et traite les deux cas.
3. Choisis et justifie une voie, **sans règle nouvelle**, la clé ne passant jamais à un enfant :
   (a) marquer dans le cache l'absence connue du fichier (marqueur « .no_exist » de `huggingface_hub` à la révision épinglée), si le
       fichier est absent du dépôt ; (b) jouer `05_act_corpus.py` hors ligne pour le dépôt du modèle, le corpus restant en ligne, si cela
       se fait sans toucher au voisin ; (c) poser `tokenizer.model` vérifié dans le cache par le lanceur, avec la clé, s'il existe — taille et
       identifiant de contenu épinglés comme les autres petits fichiers. Vérifie la voie choisie contre la version de `huggingface_hub` et de
       `transformers` épinglée dans `requirements-cpu.txt`, en installant ces versions localement et en jouant le chargement sur un dépôt
       **jouet en cache local** (aucun réseau).
4. Code neuf (R12) : un module `src/controle_ia/lentilles_sondes_bbis/cache_tokeniseur_v2.py` ; `lanceur_v9.py`, copie fidèle de
   `lanceur_v8` où seul ce point change, `MODULES` incluant le module neuf ; essais neufs `tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py`
   (R5 : artefact qui reproduit l'échec de l'ancien cache — chargement qui part au réseau ou lève l'erreur de dépôt à porte —, cas sain qui
   charge hors réseau, garde sur un marqueur ou un fichier d'une autre empreinte) et copies v9 des essais du lanceur v8 (par fabrique, comme
   les versions d'avant). Rejoue le paquet entier (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_*.py`) ; comptes seuls.
5. Ne touche à aucun fichier de la seconde passe (`constantes_v2`, `statistiques_v4`, `nos_lentilles_v1`, `lecture_entree_v1`,
   `comparaisons_lentilles_v1`, `reproduction_v1`, `audits_v2`, `phrases_v2`, `montage_v2`, `lanceur_seconde_passe_v1`, essais
   `*seconde_passe*`) : sa contre-lecture est en cours. Écris seulement, dans ta note, ce que la seconde passe devra reprendre.
6. Note scellée `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/notes-correctif-tokeniseur-act-corpus-v1.md` : défaut, voie,
   preuves locales, fichiers et empreintes, essais, nœuds.

## Coexistence et commits
Arbre de travail isolé. Pousser : `git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD`, puis
`git push origin HEAD:claude/brave-galileo-jhp684` (quatre essais au plus, jamais de poussée forcée). Aucun nom de modèle dans les commits ;
chaque message finit par `Co-Authored-By: Claude <noreply@anthropic.com>` et `Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`.

## Interdits
Aucune requête vers Hugging Face, aucun téléchargement de modèle, de lentille ou de corpus ; aucune clé lue ; `calcul/*`, `donnees/*`,
`verdict/*`, `diag/`, `runs/`, `docs/verdicts/` jamais lus ; pas de `verifier-arbre` ; intitulé interdit vu : déclaré. Refus d'outil jamais
rejoué. Aucune ligne de registre, aucune fiche.

## Rendu
Verdict en une à trois lignes ; commit poussé ; fichiers et empreintes ; essais (comptes) ; nœuds ; expositions ; fichiers pour le
contre-lecteur ; ce que la seconde passe devra reprendre.

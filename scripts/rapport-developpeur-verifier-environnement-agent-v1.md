# Rapport du développeur — programme de vérification de l'environnement des agents, v1

Développeur, modèle L′ — 2026-11-19T23:46Z. Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/mandat-developpeur-programme-verification-environnement-v1.md`
(empreinte `fa684f69…6aca` vérifiée). Tout est écrit dans le bloc-notes : rien n'est écrit dans le dépôt, rien n'est commité ni
poussé. Aucun appel à un fournisseur de modèles, aucune dépense.

## Verdict

Le programme `scripts/verifier_environnement_agent_v1.py` (bibliothèque standard seulement) et ses essais sont écrits.
**46 essais passés, 0 échoué.** Les 16 défauts réintroduits dans des copies du programme sont tous vus.

## Fichiers

| Chemin relatif au dépôt | Empreinte SHA-256 |
|---|---|
| `scripts/verifier_environnement_agent_v1.py` | `9714a00f05b66b6f0f3c901fc700ea30b07cb3c3fda302947f276dca5fea4d74` |
| `tests/test_verifier_environnement_agent_v1.py` | `94a89fc14eb9c8a809d39cdda5648328980eca9bbf0403f406881bbdcefbcb0d` |
| `scripts/rapport-developpeur-verifier-environnement-agent-v1.md` | (ce fichier : son empreinte est donnée dans le compte rendu) |

## Appel

    python3 -B scripts/verifier_environnement_agent_v1.py [--empreintes LISTE] [--modules numpy,pytest] [--depot CHEMIN] [--sortie NOUVEAU.json]

Le rapport JSON est écrit sur la sortie standard. Avec `--sortie`, il est aussi écrit dans un fichier neuf, avec son compagnon
`NOUVEAU.json.sha256` ; les deux portent les mêmes octets que la sortie standard. Exemple : la routine de reprise
`cd docs && sha256sum -c sha256sums-lancement-v2.txt` devient
`python3 -B scripts/verifier_environnement_agent_v1.py --empreintes docs/sha256sums-lancement-v2.txt`.

Codes : 0 si tout est lu ; 3 si une empreinte attendue n'est pas égalée ; 2 sur entrée invalide, chemin refusé ou sortie
impossible à écrire.

## Ce que le programme garantit (chaque point est vu par un cas sain et par un artefact)

- **Segment `archives-reponses-modeles`** : le chemin est refusé sans être touché, ni par `open`, ni par `stat`, ni par `lstat`.
  - Le chemin est contrôlé d'abord tel qu'écrit, sans tenir compte de la casse.
  - Il est ensuite résolu composant par composant. Chaque composant et chaque cible de lien symbolique sont contrôlés avant
    tout appel au système de fichiers. Un lien, ou une chaîne de liens, qui mène dans les archives est donc refusé sans que
    rien y soit examiné.
  - Le contrôle vaut pour les lignes de la liste et pour les chemins de `--empreintes`, `--depot` et `--sortie`.
  - Vérification : un espion (crochet d'audit et enveloppes de `os.stat`, `os.lstat`, `os.open`, `os.readlink`, etc.) ne voit
    aucun appel qui nomme le segment. Les fichiers « interdits » des essais sont des tubes nommés : une lecture bloquerait.
- **Validation complète avant toute lecture** : au moindre refus, tous les motifs sont donnés, après `REFUS :` sur la sortie
  d'erreur, et un JSON réduit sort sur la sortie standard. Aucun fichier de la liste n'est lu, aucun module importé, `git` n'est
  pas lancé, rien n'est écrit.
- **Empreintes** : une ligne est soit un chemin seul, soit au format `sha256sum` (`EMPREINTE␣␣chemin` ou `EMPREINTE␣*chemin`).
  Pour chaque chemin, le rapport donne l'existence, le type, la taille, le sha256 (lu par blocs) et l'égalité à l'empreinte
  attendue. Un fichier absent, un dossier ou un fichier illisible face à une empreinte attendue compte comme écart (code 3).
- **Modules** : chacun est rapporté `present`, `absent` ou `erreur_import`.
  - L'import est protégé : toute exception, `SystemExit` comprise, est rapportée. Une dépendance manquante donne
    `erreur_import`, pas `absent`.
  - Ce qu'un module écrit sur la sortie standard pendant l'import est retenu et compté, pour que le JSON reste lisible.
  - La version vient de `__version__`, sinon des métadonnées de la distribution.
- **Dépôt** : le rapport donne la tête (`git rev-parse HEAD`), la branche (`git symbolic-ref --short -q HEAD`, ou tête détachée)
  et dit si l'arbre est propre (`git status --porcelain --untracked-files=normal`).
  - Les appels passent une liste d'arguments fixe, sans shell, avec `--no-optional-locks` et `core.fsmonitor=false`. Les
    variables `GIT_*` de l'appelant sont retirées.
  - L'essai sur `.git` montre que rien n'y est écrit, même avec un index périmé.
  - Un dossier non git est rapporté, avec le code 0. Un dossier absent ou un fichier à la place du dépôt donne le code 2.
- **Processus, réseau, écriture** : l'espion voit seulement des processus `git`, aucun socket, et des écritures sur le seul
  fichier de sortie et son compagnon, créés en mode exclusif. Un lien pendant à la place de la sortie compte comme existant.

## Choix de ma main (consigne non explicite)

1. **Chemins relatifs d'une liste** : ils se lisent depuis le dossier de la liste, comme `cd dossier && sha256sum -c liste`, et
   non depuis le dossier courant. Ainsi, les listes et les compagnons `.sha256` du dépôt servent tels quels.
2. **`git status` exclut tout chemin qui contient le segment** (pathspecs `:(top,exclude,glob,icase)`, déclarés dans le
   rapport). « Arbre propre » veut donc dire « propre hors des archives ». Sans cette exclusion, `git status` examinerait les
   fichiers suivis des archives et pourrait citer leurs noms. `git status` porte sur tout l'arbre (`:/`), même si `--depot`
   désigne un sous-dossier.
3. **Pas de `platform.platform()`** : en Python 3.13, il lance `uname -p` (le défaut réintroduit est vu par l'espion). La
   plateforme est lue par `platform.system()`, `release()` et `machine()`, qui passent par `os.uname()`.
4. **Le dossier du programme est retiré du chemin de recherche des modules** avant les imports, pour qu'un fichier de `scripts/`
   ne passe jamais pour un module de l'environnement.
5. **Lignes de liste refusées** (code 2) :
   - 64 caractères hexadécimaux sans chemin ou mal séparés ;
   - espace en tête ou en fin de chemin ;
   - nom échappé par une barre oblique inverse ;
   - marque d'ordre des octets en tête de la liste ;
   - liste sans aucun chemin.
6. **Fichier absent sans empreinte attendue** : il est rapporté dans `anomalies`, avec le code 0. Il en va de même d'un module en
   erreur d'import et d'un dépôt non git. Le code 3 est réservé aux empreintes attendues.
7. **Sortie impossible à écrire en fin de course** : le rapport sort quand même sur la sortie standard, puis le programme rend le
   code 2. Les fichiers créés par cet appel sont retirés.

## Contrôle « trop beau » (R4)

J'ai réintroduit chaque défaut dans une copie du programme. Pour chacun, le contrôle nommé passe sur le programme et échoue sur
la copie : les 16 défauts sont vus.

| Défaut réintroduit | Contrôle qui l'a vu |
|---|---|
| Contrôle du segment retiré | `verif_refus_archives_dans_liste` |
| Segment sensible à la casse | `verif_refus_archives_casse` |
| Liens suivis par `realpath` sans contrôle | `verif_refus_archives_par_lien` |
| `realpath` puis contrôle (refuse, mais examine le chemin dans les archives) | `verif_refus_archives_par_lien` |
| Empreinte différente ignorée (code 0) | `verif_ecart_empreinte_code3` |
| Fichier absent non compté comme écart | `verif_ecart_absent_avec_empreinte` |
| Sortie existante réécrite | `verif_refus_sortie_existe` |
| Import non protégé | `verif_sain_module_absent` |
| Sortie standard non protégée pendant l'import | `verif_sain_module_erreur_import` |
| Dépôt non git traité en faute | `verif_depot_non_git` |
| Plateforme lue par `platform.platform()` (lance `uname`) | `verif_sain_processus_seul_git` |
| `git` lancé par le shell | `verif_sain_processus_seul_git` |
| `--no-optional-locks` retiré (git réécrit l'index) | `verif_sain_depot_sans_ecriture` |
| Exclusion des archives retirée de `git status` | `verif_sain_status_exclut_archives` |
| Compagnon au chemin complet au lieu du nom | `verif_sain_sortie` |
| Ligne de liste mal séparée acceptée | `verif_refus_liste_lignes_invalides` |

Au premier lancement, 14 essais ont échoué, sans défaut dans le programme :
- trois défauts venaient de mes essais : un défaut de l'espion qui touchait 12 essais, plus deux défauts isolés ;
- une mutation était sans effet réel. Le programme capture déjà les erreurs de `subprocess`, donc `check=True` ne change rien ;
  je l'ai remplacée par « dépôt non git traité en faute ».

Le détail est ci-dessous, à titre de réserve (R4).

| Défaut des essais | Correction |
|---|---|
| L'espion signalait le segment dans l'événement d'audit `compile`, dont le texte source contient la constante du segment | Le contrôle du segment ne regarde plus que les événements de chemin |
| L'espion comptait comme écriture l'ouverture d'un descripteur (le tube d'entrée de `subprocess`) | Les ouvertures par descripteur ne sont plus comptées comme écritures de fichier |
| Le contrôle statique lisait aussi la docstring, qui cite `platform.platform()` pour l'interdire | Le contrôle statique ne lit que le code, sans la docstring |
| Un JSON illisible levait `JSONDecodeError` au lieu d'`AssertionError` | Un JSON illisible lève désormais `AssertionError` |

Les corrections ont été faites avec `scripts/remplacer_texte_exact_v1.py`.

**Limites** :
- Une écriture d'un module importé directement sur le descripteur 1, au niveau C, n'est pas captée.
- Un module dont l'import lance lui-même un processus échappe à la garantie « seulement `git` », puisque l'import est demandé.
- Une substitution de fichier entre la validation et la lecture n'est couverte qu'en partie : `O_NOFOLLOW` et contrôle
  `fstat` à l'ouverture.
- Je n'ai pas observé au niveau du noyau que `git status` ne visite pas les dossiers exclus : l'essai montre seulement qu'il ne
  les rapporte pas.

## Essais et essai manuel

- Commande, lancée depuis le bloc-notes :
  `PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider tests/test_verifier_environnement_agent_v1.py`.
  Résultat : 46 passés en 5,4 s.
- Essai manuel sur le dépôt, en lecture seule, avec la sortie dans le bloc-notes :
  - `--empreintes docs/sha256sums-lancement-v2.txt` : 3 fichiers égaux ;
  - `--modules numpy,pytest,module_inexistant` : numpy 2.5.3, pytest 9.1.1, le troisième absent ;
  - `--depot` : branche `lot/compte-organisme-v1`, tête `a0a3e68d…`, arbre propre ;
  - code de retour 0 ;
  - le compagnon est égal au `sha256sum` de la sortie ;
  - une seconde exécution vers la même sortie est refusée (code 2) ;
  - `git status --porcelain` du dépôt reste vide.

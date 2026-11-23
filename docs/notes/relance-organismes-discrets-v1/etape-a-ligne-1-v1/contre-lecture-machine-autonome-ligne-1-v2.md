# Contre-lecture neuve de la machine autonome de la ligne 1 de carte du bras A (version 2)

- **Date (UTC)** : 2026-11-23. Contre-lecteur : Claude Opus 5.5, sous-agent neuf, qui n'a écrit aucune des pièces lues. Processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git. Aucune commande de création jouée.
- **Objet** : la machine louée qui jouera la ligne 1 de carte du bras A (128 épisodes honnêtes, plafond 18 USD, GO-2026-11-22-148), sans SSH, créée par la session mère à partir de la commande imprimée par le lanceur.
- **Cloisonnement tenu** : rien d'ouvert, listé, cherché ni empreinté sous les chemins cloisonnés. Deux commandes de lecture que j'avais mal bornées (un motif `scripts/*.sh` qui aurait pu toucher un programme cloisonné, et une recherche dans le registre des GO) ont été **refusées par la garde de permission avant exécution** ; rien n'a été lu. La forme de la commande imprimée a été jugée sur un registre des GO **factice** (dossier de travail temporaire), jamais sur `registres/`.

## Verdict

**À corriger avant le départ.** Un défaut bloquant tant qu'il n'est pas levé par une vérification : la présence de `git` et de `curl` dans l'image `pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime` n'est vérifiée nulle part ; sans `curl`, la machine ne sait plus s'arrêter elle-même. Deux défauts majeurs, peu coûteux à corriger : l'amorce d'appel casse sous `sh` sans s'arrêter, et un arrêt demandé une seule fois qui échoue laisse la machine tourner sans fin. Le reste est bon : ordre versement, poussée, preuve, destruction ; vérification du commit et des empreintes avant toute exécution de code reçu ; aucune fuite de secret trouvée ; minuterie et compteur conformes aux conventions ; commande imprimée acceptée par la garde de calcul.

## Pièces lues (empreintes vérifiées sur disque, conformes à celles données)

| pièce | sha256 |
|---|---|
| `scripts/amorce_appel_ligne_1_bras_a_v1.sh` (2 423 octets) | `1f0d960995275724770c6516c37af223b019708b38c0de550c14da9a17dea03e` |
| `scripts/amorce_ligne_1_bras_a_v2.sh` | `c4ee8fcf4fdada3376d5449bb46e6fbe959e53a10c3c9dd9d6853f7c94f68998` |
| `scripts/construire_branche_entree_ligne_1_bras_a_v2.py` | `9a51184f6097d96ff18b4ae91cf1ccccdcce4a1423d590c369967160409b2bb4` |
| `scripts/lanceur_machine_ligne_1_bras_a_v2.py` | `f5441cb57365aa3075b29044a9f914dd0605fd9ee2ccc1108d979a3a53376e76` |
| `tests/test_amorce_ligne_1_bras_a_v2.py` | `728726502f2f0d199b189ab02256cdb1c955e2d40bceb2fb889507b6b95574c9` |
| `docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/machine-autonome-ligne-1-v2.md` | `e6d4a7116a821e88b32c69e3a50a6195f597dc97edb0613d7e880efa8b68b675` |

Lus en appui : `.claude/hooks/garde_calcul.py`, la section 6 de `sequence-ligne-1-v2.md` (par motif), `harnais/modeles.py` (`precharger_modele`), l'en-tête des imports de `course_ligne_1_bras_a_v2.py` et du lanceur v8.

## Essais joués

- `python -m pytest -q tests/test_amorce_ligne_1_bras_a_v2.py` : **35 passent, 1 sauté** (le rejeu long, comme demandé), 268 s.
- `bash -n` sur les deux amorces : syntaxe correcte. `shellcheck` **absent** de la machine (non installé : aucun réseau hors git).
- **Amorce d'appel sous `sh` (dash)**, en mode jouet, dans un dossier temporaire : `Bad substitution` à la ligne 23, code 2, **aucun arrêt demandé** (voir M1).
- **Vrai `curl -K -`** contre un petit serveur local : l'en-tête `Authorization: Bearer <clé>` arrive entier pour une clé de lettres et chiffres ; la clé n'est sur aucune ligne de commande (`printf` est intégré au shell). Une clé contenant `"` ou `\` serait tronquée par le format de configuration de `curl` (les clés de Vast sont hexadécimales : sans objet en pratique).
- **Garde de calcul** sur la commande imprimée (`creation --offre 123 --commit-entree a… --sans-verifier-entree`, 575 signes), registre des GO factice où GO-2026-11-22-148 est de type calcul, accordé par Lazar et valide le 23 novembre : **forme acceptée** ; la même commande sans `GO_ID=` est **bloquée**. Le rang à trois chiffres (148) est admis par le motif `GO-\d{4}-\d{2}-\d{2}-\d{2,3}`. La validité réelle du GO dans `registres/go.md` n'est pas vérifiée ici (registre cloisonné pour ce contre-lecteur) : elle reste à la charge de la garde au moment de la création.

## Conventions de la session mère, une à une

1. **Jeton `GH_TOKEN` sur l'instance ; `creation` imprime sans exécuter, valeurs par leur seul nom** : conforme. La commande porte `-e GH_TOKEN=$GH_TOKEN -e HF_TOKEN=$HF_TOKEN`, développées par le shell de la mère ; l'essai le vérifie par `vastai.utils.parse_env`. Seul appel réseau du lanceur : `git ls-remote` (entrée au commit donné, sortie absente).
2. **URL sans jeton ; aide d'identification par `-c` au clone et inscrite dans la configuration du clone avant extraction et poussée** : conforme dans l'appel (lignes 28 à 31 : clone `--no-checkout`, `git config credential.helper`, puis extraction) et dans l'amorce complète (lignes 332 à 337 ; clone fait par l'appel : aide réinscrite si elle manque, ligne 328). Le dépôt de sortie inscrit l'aide avant `remote add` et la poussée (ligne 277). L'aide est entre apostrophes : la configuration et les arguments portent le texte `${GH_TOKEN}`, jamais sa valeur (essai à l'appui).
3. **Destruction** : `DELETE …/instances/$CONTAINER_ID/`, `Authorization: Bearer $CONTAINER_API_KEY` par `curl -K -` ; arrêt `PUT {"state": "stopped"}` ; refus si l'identifiant n'est pas numérique (appel ligne 24, amorce lignes 109, 121, 146) ; destruction seulement après preuve (voir l'ordre ci-dessous) : conforme.
4. **`--env "-e NOM=valeur …"` et `--onstart` ; aucune valeur secrète dans un journal** : conforme sur ce que j'ai pu chercher (section Secrets). `--onstart` reçoit bien un **chemin de fichier** (le client lit le fichier), joué depuis la racine du dépôt.
5. **Branches `entree/bras-a-ligne-1-v1` (orpheline, liste blanche, 58 fichiers) et `calcul/bras-a-ligne-1-v1`** : conforme (36 modules + 12 données avec compagnons + 4 du guide + 3 exigences + constat + amorce complète + `empreintes-posees.txt` = 58 ; orpheline contrôlée par `rev-list --parents` ; sortie orpheline neuve, refusée par le lanceur si elle existe déjà).
6. **Heure du plafond** : coupe, versement, poussée, preuve ; poussée prouvée : 15 min de grâce en marche, relecture de la preuve, destruction ; sinon arrêt seulement, « nœud pour la mère » : conforme (fonctions `conclure`, `detruire_apres_preuve` ; deux essais). Réserve : la machine ne peut pas « remonter » le nœud elle-même quand la poussée a échoué ; la mère ne l'apprend que par `etat` (instance arrêtée). Voir m6.

## Ordre versement → poussée → preuve → destruction (R10, 8.5)

Tenu sur tous les chemins lus. La destruction ne part que de `detruire_apres_preuve`, appelée seulement après `pousser_et_prouver` réussi (`git ls-remote` de la branche = commit local) ou sur un état `poussee-prouvee` déjà écrit ; la minuterie et l'amorce d'appel ne détruisent jamais ; la destruction se fait par l'identifiant seul ; jamais d'arrêt par motif (les PID des étapes sont notés sur le disque). Un redémarrage ne relance rien (R12) : l'état est versé, poussé, prouvé, puis détruit ; un troisième départ après destruction prouvée ne refait que la destruction (essai).

## Minuterie et compteur

- Échéance : création retenue + 21 600 s (6 h). Heure du plafond : création + (18 − 0,013 × 40) ÷ (taux carte + stockage du constat) × 3 600 − 1 800 s, soit environ 14,15 h avec le constat du jour : l'échéance passe toujours avant. Secours : 3 600 s après l'heure du plafond, arrêt seulement.
- Compteur : `AVANT_CREATION_UTC` est développée par le shell de la mère au moment où il lance `vastai`, donc antérieure à la création : borne prudente. Refusée si illisible ou postérieure au départ de l'appel ; refusée si antérieure au constat (la création doit suivre le constat) ; sans elle, départ − 30 min, jamais avant le constat. Jour de création = jour UTC du constat (m1) : avec le constat `…20261123T024626Z`, **la création doit partir le 23 novembre avant minuit UTC**, sinon refus sur la machine (coût d'un démarrage) et nouveau constat, donc nouvelle branche d'entrée.
- Recoupement par `start_date` (lanceur `verification --start-date`) : en place.

## Défauts

### Bloquant (tant qu'il n'est pas levé par une vérification)

- **B1. `git` et `curl` dans l'image, non vérifiés.** L'image officielle `pytorch/pytorch:*-runtime` est, à ma connaissance (non vérifié ici, aucun réseau), construite avec les seuls `ca-certificates`, `libjpeg-dev`, `libpng-dev` par-dessus Ubuntu, plus Python dans `/opt/conda` : **ni `git` ni `curl`** probablement. Conséquences : sans `git`, l'appel échoue au clone ; sans `curl`, sa demande d'arrêt échoue silencieusement (`c` vide) puis `sleep infinity` : **la machine tourne sans fin, sans rien faire**, jusqu'à ce que la mère la détruise. L'amorce complète a le même trou (ligne 141 : outil absent → `fin 2`, sans aucune demande d'arrêt). Correction : soit une image dont on sait qu'elle porte `git` et `curl` ; soit, en tête de l'appel, `command -v git >/dev/null && command -v curl >/dev/null || { apt-get update -qq && apt-get install -y -qq git curl; } >/dev/null 2>&1` (environ 130 octets : retirer l'en-tête de commentaires de l'appel pour rester sous 2 500) ; et, en secours, une demande d'arrêt par `python3` (bibliothèque standard, `urllib`) quand `curl` manque.

### Majeurs

- **M1. L'amorce d'appel casse sous `sh` sans s'arrêter.** Elle commence par `#!/bin/bash` mais n'a pas la reprise par bash de l'amorce complète ; `${!v:-}` (ligne 23) est refusé par dash (essai : `Bad substitution`, code 2, aucun PUT). La façon dont Vast joue le script d'onstart (`bash` ou `sh`, fichier ou texte « sourcé ») n'est pas vérifiée. Correction : ajouter en première ligne `[ -n "${BASH_VERSION:-}" ] || exec bash "$0" "$@"` (46 octets, la place existe : 77 octets restent).
- **M2. Arrêt demandé une seule fois.** `arreter` (amorce complète) et `s` (appel) font un seul `PUT state=stopped`, puis `sleep infinity`. Si ce PUT échoue (réseau, interface du loueur), la machine tourne sans fin ; la minuterie ne rattrape rien (le secours exige l'absence de l'état `fin`, qui vient d'être écrit). Correction : redemander l'arrêt en boucle tant que le processus vit (comme `detruire`, par exemple toutes les 5 min), et journaliser chaque code.
- **M3. Le secours fixé à 60 min dépasse le plafond.** L'heure du plafond est prise 30 min avant le cumul de 18 USD : un fil principal bloqué n'est arrêté que 30 min **après** le cumul, soit environ 0,6 USD au-delà du plafond du GO (au taux du constat), dans la marge de crédit mais hors du plafond. De même, une poussée bloquée après l'échéance de 6 h (`git push` et `git ls-remote` sans délai) laisse la machine tourner jusqu'à l'heure du plafond + 60 min. Correction : secours à 25 min au plus (la grâce est de 15 min, la poussée de quelques minutes ; un secours trop tôt ne fait qu'arrêter, le sens prudent), et délai borné sur git (`timeout 300 git …` ou `-c http.lowSpeedLimit=1000 -c http.lowSpeedTime=60`).

### Mineurs

- **m1. Pas de `set -e`.** L'appel n'a que `set -u` ; l'amorce complète `set -uo pipefail`. Chaque commande qui compte est testée à la main ; je n'ai pas trouvé d'erreur avalée qui mène à un mauvais état, mais c'est un écart à la convention annoncée « `set -euo pipefail` », à déclarer.
- **m2. Secrets dans l'environnement de l'installation.** L'installation des paquets (`pip install -r requirements-gpu.txt`, ligne 390) garde `GH_TOKEN`, `HF_TOKEN` et `CONTAINER_API_KEY` dans son environnement : tout programme d'installation venu de l'index les voit. Le téléchargement du modèle et la course les retirent (`env -u`) ; faire de même ici (les trois).
- **m3. Aides d'identification de l'image.** Si l'image porte une aide globale (`credential.helper store`), git y écrit le jeton en clair après une authentification réussie (`~/.git-credentials`) ; les essais jouent avec `GIT_CONFIG_NOSYSTEM=1` et un `HOME` neuf, donc sans ce cas. Correction : `-c credential.helper=` (vide, remet la liste à zéro) avant l'aide, au clone et dans la configuration du clone ; plus `GIT_TERMINAL_PROMPT=0`.
- **m4. Coupe d'une étape lancée par `bash -c`.** À l'échéance pendant l'installation ou le téléchargement, le TERM touche le `bash -c`, pas `pip` ni `python`, qui continuent orphelins pendant le versement (sans effet sur l'ordre : la destruction les emporte). Lancer par `exec` dans le `bash -c`, ou couper le groupe de processus par son numéro.
- **m5. Reprise : secours désarmé.** Après un redémarrage, l'état `fin` d'un départ précédent reste sur le disque : la minuterie relancée ne fera jamais le secours. Effacer `fin` (et `secours`) au début d'une reprise.
- **m6. Nœud « pour la mère » sans canal.** Quand la poussée échoue, le journal qui dit « nœud pour la mère » reste sur le disque de la machine arrêtée. La séquence doit dire que la mère lit `etat` à intervalle fixe pendant la course (et au plus tard à l'heure de l'échéance + 30 min), et détruit par l'identifiant toute instance « running » sans versement prouvé au-delà de l'heure du plafond. Noter aussi : redémarrer une instance arrêtée relance l'appel, qui repousse puis **détruit** après preuve.
- **m7. Guide contrôlé seulement sur la machine.** Les octets des quatre fichiers du guide sont pris à `origin/main` (référence locale, qui peut être en retard) et leurs empreintes données ne sont contrôlées que par `sha256sum -c` sur la machine : un écart coûte un démarrage. Faire `git fetch origin main` juste avant la construction.
- **m8. Commande imprimée.** `$GH_TOKEN` vide chez la mère donne une machine qui s'arrête (coût d'un démarrage) : préférer `${GH_TOKEN:?}` et `${HF_TOKEN:?}`, qui font échouer la commande chez la mère. Les valeurs développées sont, le temps de l'appel, dans les arguments du processus `vastai` de la mère et dans la fiche de l'instance chez Vast (inhérent à `--env` ; `etat` masque). La sortie de `vastai create … --raw` n'est pas masquée : la faire passer par le masquage du lanceur si un message d'erreur peut citer la requête.
- **m9. Textes en retard.** La docstring de la construction v2 donne pour usage `construire_branche_entree_ligne_1_bras_a_v1.py` ; celle du lanceur v2 cite `--onstart scripts/amorce_ligne_1_bras_a_v1.sh` dans sa description de la v1 ; sans effet sur le code.
- **m10. Fichier de plus de 100 Mo dans le versement.** GitHub refuserait la poussée ; on retomberait sur l'arrêt seulement (le sens prudent). Aucun contrôle de taille avant la poussée.

## Secrets : ce que j'ai cherché

- `set -x` : `set +x` en tête des deux amorces ; aucun `env`, `printenv`, `declare -p` ni `set` sans argument.
- Lignes de commande (`ps`) : clé du loueur par l'entrée standard de `curl` ; aide git entre apostrophes (le jeton est lu par le shell de l'aide, `echo` intégré) ; `env -u` ne porte que des noms. Rien de secret dans les arguments sur la machine.
- Messages d'erreur : sorties de `curl` jetées (`2>/dev/null`) ; messages de git écrits dans des fichiers masqués avant tout journal ; l'URL ne porte jamais le jeton.
- Fichiers : journaux masqués à l'écriture (`j`) et au versement (`masquer_fichier` sur chaque fichier copié, en octets) ; `amorce.json` ne porte que des valeurs non secrètes ; la course et le téléchargement du modèle sont lancés sans `GH_TOKEN` ni la clé du loueur. Les sorties de la course ne sont pas masquées, mais elle tourne sans aucun des trois secrets dans son environnement.
- Restent hors de portée de ces amorces : m2, m3, m8.

## Cas non éprouvés

1. Contenu de l'image (B1).
2. Manière dont Vast joue l'onstart en lancement par défaut (`bash` ou `sh`, variables `-e` visibles, rejeu au redémarrage) (M1).
3. Droits de `CONTAINER_API_KEY` : que la clé injectée permette bien `DELETE` et `PUT` sur sa propre instance (à défaut : arrêt et destruction échouent, la mère détruit).
4. Secours de la minuterie (fil principal bloqué), PUT en échec (M2), `git push` bloqué (M3).
5. Rejeu long sur le modèle jouet (sauté ici, comme demandé).

## Corrections demandées avant le départ

B1, M1, M2, M3 ; m2 et m3 recommandés (quelques lignes). Une version nouvelle de l'appel (`…_v2`) et de l'amorce complète (`…_v3`) prend un nom neuf (R12) ; la branche d'entrée, pas encore construite ni poussée, l'est ensuite avec ces pièces, et `AMORCE_SHA256` change. Ces corrections touchent des pièces nouvelles : une contre-lecture courte de l'écart suffit.

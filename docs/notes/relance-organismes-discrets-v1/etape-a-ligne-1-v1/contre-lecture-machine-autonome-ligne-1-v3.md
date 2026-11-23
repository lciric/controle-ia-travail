# Contre-lecture courte de l'écart : machine autonome de la ligne 1 du bras A, v2 → v3

- **Date (UTC)** : 2026-11-23. Contre-lecteur : Claude Opus 5.5, le sous-agent qui a écrit la contre-lecture de la v2 (`contre-lecture-machine-autonome-ligne-1-v2.md`, `fe84a889…`). Je n'ai écrit aucune des pièces v3. Processeur seul : aucune dépense, aucune instance, aucune clé, aucun réseau hors git. Cloisonnement tenu comme la première fois.
- **Commit lu** : `ff5b6f0a1` (branche `claude/pensive-bardeen-1fv7hw`). Les empreintes des pièces neuves sont conformes à celles données : appel v2 `43db57e8…` (2 484 octets), amorce complète v3 `73f88e6a…`, construction v3 `28cef044…`, lanceur v3 `af10ee8b…`, essais v3 `c0a063fa…`, note v3 `2dc2e1c6…`.

## Verdict

**Bon pour le départ.** B1, M1, M2 et M3 sont corrigés, ainsi que les mineurs m2 à m10 ; m1 est déclaré comme écart. Les `diff` contre la v2 (amorce complète, construction, lanceur) et la relecture entière de l'appel v2 (réécrit, 35 lignes) ne montrent aucun autre changement sur le fond. L'ordre versement → poussée → preuve → destruction est intact. L'échéance (6 h) et l'heure du plafond (30 min avant le cumul de 18 USD) sont inchangées. La vérification du commit et des empreintes avant toute exécution de code reçu est inchangée. Une recommandation sur la commande imprimée (ci-dessous), non bloquante.

## Essais

- `bash -n` sur les deux amorces : syntaxe correcte. `shellcheck` reste absent.
- `python -m pytest -q tests/test_amorce_ligne_1_bras_a_v3.py` : **41 passent, 1 sauté** (le rejeu long), 267 s. Six essais neufs : reprise sous `sh`, premier arrêt en échec redemandé (appel et amorce complète), fichier trop gros gardé hors de la poussée, sous-commande `masquer`, constantes de la v3.
- Garde de calcul sur la commande imprimée v3, avec un registre des GO factice : **acceptée**, telle quelle et précédée de `set -o pipefail;`.
- `${GH_TOKEN:?}` vide : l'expansion échoue. Sans `pipefail`, la ligne rend 0 ; avec `pipefail`, elle rend 127.

## Défauts de la v2, un par un

- **B1 (outils de l'image)** : tenu. L'appel installe `git`, `curl` et `ca-certificates` par apt s'ils manquent (hors jouet) ; sans `git`, il demande l'arrêt. Sans `curl`, l'appel et l'amorce complète passent par `python3` et `urllib` (clé lue par son nom dans l'environnement, jamais en argument). Un outil absent dans l'amorce complète mène à `arreter`, plus jamais à `fin` sans demande.
- **M1 (sous `sh`)** : tenu. La première ligne de l'appel est la reprise par bash (essai sous dash).
- **M2 (arrêt unique)** : tenu. `s` dans l'appel et `arreter` dans l'amorce complète redemandent en boucle, avec un délai croissant borné à 10 min. L'amorce complète relit l'état par GET et n'écrit que `intended_status` et `actual_status` (la fiche de l'instance porte les variables `-e` : rien d'autre n'est écrit).
- **M3 (secours, délais)** : tenu. Le secours passe à 1 500 s (25 min) après l'heure du plafond, qui est elle-même 30 min avant le cumul : il tombe sous le plafond. `timeout` borne le clone (900 s), la poussée (900 s), `ls-remote` (300 s) et chaque appel au loueur (90 s). Le secours ne part pas si un arrêt est déjà demandé.
- **m2** : tenu. L'installation tourne sans les trois secrets ; le téléchargement du modèle garde `HF_TOKEN` seul.
- **m3** : tenu. `credential.helper` est remis à vide avant l'aide, au clone (`-c credential.helper=`) et dans chaque configuration (entrée et sortie). `git config credential.helper` rend la dernière valeur, l'aide, donc le contrôle du clone fait par l'appel tient. `GIT_TERMINAL_PROMPT=0` est posé.
- **m4** : tenu. Les étapes longues partent par `setsid`. Dans un shell non interactif, la tâche de fond n'est pas chef de groupe : `setsid` ne refait pas de fork, et le PID attendu est bien celui du groupe. La coupe vise `-PGID`. `exec` est ajouté dans les `bash -c`.
- **m5** : tenu. À la reprise, `fin`, `secours`, `destruction-demandee` et `arret-demande` sont effacés.
- **m6** : tenu par la note v3, section 4 : la mère lit `etat` et `ls-remote` toutes les 15 min, détruit une instance en marche après l'heure du plafond + 25 min sans versement prouvé, et fait une lecture au plus tard à l'échéance + 30 min.
- **m7** : tenu (`git fetch origin main` avant le guide ; un échec est un refus).
- **m8** : tenu (`${GH_TOKEN:?}`, `${HF_TOKEN:?}`, sortie passée dans `masquer`).
- **m9** : tenu.
- **m10** : tenu. Un fichier de plus de 100 Mo est déplacé hors du versement, déclaré comme manquant dans le manifeste, et reste sur le disque.
- **m1** : écart déclaré dans l'amorce complète et dans la note (pas de `set -e`, pour garder les chemins de repli).

## Point à juger : `| … masquer` et le code de retour de `vastai`

**Acceptable, mais je recommande `set -o pipefail;` en tête de la commande imprimée** (la garde de calcul l'accepte, essai fait). Sans `pipefail`, la ligne rend toujours le code de `masquer`, en pratique 0 : un `${GH_TOKEN:?}` vide, un `vastai` en échec ou une offre indisponible (`--cancel-unavail`) passent pour une réussite. Lire `new_contract` dans le JSON suffit à décider, **à une règle près, qui compte plus que le code** : si `new_contract` est absent ou illisible, la mère ne relance **jamais** une création avant d'avoir listé ses instances par l'étiquette `bras-a-ligne-1-v1`. Sinon, une création réussie dont la sortie s'est perdue (par exemple si `masquer` tombe, chemin `.venv/bin/python` relatif, ligne jouée hors de la racine) donnerait deux machines. Avec `pipefail`, un code non nul suivi d'un JSON sans `new_contract` donne le même chemin.

## Mineurs restants (non bloquants)

- L'appel accepte `AMORCE_PAS_S` hors jouet (rythme de ses redemandes d'arrêt) ; seule la mère pose les variables : sans effet pratique.
- `masquer`, appliqué ligne par ligne, ne masque que les valeurs secrètes présentes dans l'environnement de la mère, pas les champs au nom de secret d'un JSON imprimé sur une ligne. La sortie de `create --raw` ne porte pas les variables : sans effet pratique.
- Chemins non cités dans l'appel (`$T`, `$E`, `$F`, `$B`) : sans espace hors jouet, sans effet.
- Toujours non éprouvés : la façon dont Vast joue l'onstart, les droits de `CONTAINER_API_KEY` sur sa propre instance, la réussite d'apt sur l'image réelle. Chacun échoue du côté prudent (arrêt redemandé, lecture de `etat` par la mère).

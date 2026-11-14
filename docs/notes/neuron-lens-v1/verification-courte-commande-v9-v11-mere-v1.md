# Vérification courte du différentiel v9 → v11 de la commande du volet A (Neuron Lens), lecteur neuf « modèle C »

Date : 2026-11-14 (UTC, `date -u` à 15:12). Lecture seule. Réf. `refs/remotes/origin/prep/neuron-lens-v1` (tête `43bd6497`).
Empreintes relues par `git cat-file blob | sha256sum` : v11 `e18da708bfd5c7a04be72a7daa8ec2ad98fcb228a56f1e982d25c1995c869333`
(conforme à l'annonce) ; v10 `7be3b223…` et v9 `39b65361…` et contre-lecture 11 `0c29e1c1…` (conformes aux tableaux d'empreintes).
Ligne `GO-2026-11-14-05` de `registres/go.md` : 10 USD, RTX 4090 à 0,90 USD/h au plus, échéance 2026-11-30, feu écrit de la mère exigé ;
la v11 ne change aucun de ces termes (plafond 10 USD, compte rendu, arrêt et destruction par identifiant : textes de la v9 intacts).

## Verdict : conforme avec mineurs

R-1 à R-7 et l'étiquette sont appliqués ; aucun hunk ne touche le fond, les bornes de dépense, les arrêts, le jeton, la destruction par
identifiant ni la minuterie, hors les retouches. Deux mineurs ci-dessous (aucun bloquant).

## Une ligne par retouche
- R-1 (moyenne) : appliquée, étape 6 (v10) : `date -u +%FT%TZ` ajouté dans le bloc de création, juste avant `vastai create instance`, et texte « heure de création (la sortie de date -u ci-dessus, jamais une heure de mémoire) ». Conforme à la correction proposée.
- R-2 : appliquée, étape 6 : ligne `echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-volet-a-v1.txt`, mot pour mot celle de la contre-lecture.
- R-3 : appliquée, étape 13 : « 2 s après, `ps -p` exigé mort (un état `Z`, zombie, compte comme mort) ».
- R-4 : appliquée, étape 13 : `ps -p <PID> -o args=` montrant `minuterie_destruction` ou `garde_depense_v3` avant tout arrêt, sinon « ne pas l'arrêter, le dire ». Renforce la sécurité (R10), sans l'affaiblir.
- R-5 : appliquée, étape 13 : mention du `sleep` orphelin vivant jusqu'à son terme, sans effet.
- R-6 : appliquée, étape 5 : `.venv/bin/python scripts/depot_reduit_…`.
- R-7 : appliquée, étape 13 (choix précis ajouté, voir mineur M-2) : journaux et fichiers de PID commités avec les résultats sur `prep/neuron-lens-v1`.
- Étiquette (v11) : appliquée, tableau final : « (archivée, non employée) » retiré de la contre-lecture 11 ; ajout de la ligne v10 archivée avec son empreinte `7be3b223…` (exacte) ; en-tête et phrase « citant cette v11 » mis à jour.

## Hunks non expliqués par R-1 à R-7 / étiquette
- Aucun non expliqué. Hunks d'accompagnement attendus : titre et bloc d'en-tête v10 puis v11 (déclarent « sans relecture après coup ») ; « citant cette v10 / v11 » ; lignes de tableau v9 et contre-lecture 11 ajoutées en v10.

## Mineurs
- M-1 : l'étape 13 nomme `journal-depense-volet-a-v1.jsonl`, nom absent de la v9 (qui ne cite que `minuterie-volet-a-v1.log` et `garde-volet-a-v1.log`). Je n'ai pas pu vérifier, faute de lecture d'autres fichiers, que la garde écrit bien ce fichier ; sans effet sur la dépense ni la sécurité (au pire un nom inexact dans une liste de fichiers à commiter).
- M-2 : R-7 demandait seulement « dire quoi faire des autres » ; la v10 tranche (les commiter sur la branche de préparation, jamais `main`). Ajout de décision, borné à la branche de préparation ; à faire valider que ces journaux ne contiennent ni jeton ni adresse sensible avant le commit (la v9 affirme ailleurs qu'aucun objet ne contient l'adresse, mais pas pour ces journaux).

## Réserves de méthode
Lecture du seul différentiel et des fichiers cités ; aucune exécution, aucun réseau. Le bon fonctionnement réel de la commande reste « supposé » comme dans la contre-lecture 11.

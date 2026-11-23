# Troisième vérification : relance courte de la machine 61875617, brouillon 4 et script v3 (contre-lecteur 1, classe B)

Contre-lecteur : Claude Opus 5.5, le même que pour les vérifications précédentes. Heure : 2026-11-22, vers 12:48Z. Aucun appel au vrai loueur.

## Verdict

**Jouable pour `lister` puis `jouer`.** La relance n'a pas régressé et `lister` est conforme.

**`archiver` n'est pas conforme et doit être corrigé avant son emploi** (étape 5, après la relance, sur processeur). Il annonce « ARCHIVE CONFORME » avec une liste de contenu tronquée : c'est un repli silencieux, contraire à la règle R5. L'archive elle-même est juste. Le start n'en dépend pas.

## Empreintes (conformes à l'annonce)

| fichier | sha256 |
|---|---|
| `texte-relance-courte-61875617-v1-brouillon4.md` | `8f87c3dc5fb94d00ad77ca99026744aa1a4f8c503eef82f6e617fcadac746204` |
| `relance-courte-61875617-v3.sh` | `9911cdaad346df7d2a0c7961aa02fb67389f7eb816b3c4556cd21a6836975800` |
| `essais-blanc-relance-courte-v3.txt` | `e827e7ce409612072970ed6b172a44e66dce0e5e85d63e209224766be1e4576c` |
| `differences-brouillon3-vers-4.md` | `0457d0e75ae6b0ece0929b27835f5c71fa4c78fb460d64cde1f1ac8a90964d5d` |

## Affirmations du texte vérifiées

- **Minuterie : vrai.** Elle lit l'identifiant de l'instance et la clé du loueur dans l'environnement (`CONTAINER_ID`, `CONTAINER_API_KEY` ; amorce l. 55, 62, 67), jamais dans un fichier. `iib-minuterie.sh` est réécrit à chaque démarrage (l. 107). L'échéance et l'heure de dépense épuisée se relisent depuis l'environnement (l. 162-173). Retirer `curl` et `python3` déclenche une réinstallation ou `refus_precoce` (l. 147-159). Le sommeil sans destruction exige le marqueur `iib-fin-normale`, qu'un `rm` ne peut pas créer (l. 186-193). **Aucun `rm` n'est sûr.** Je n'ai trouvé aucun autre fichier dont la suppression mène à un chemin sans destruction et sans perte des lots.
- **`update instance` : vrai.** L'outil envoie `PUT /instances/update_template/{id}/` (`vastai/api/instances.py` l. 444) ; l'aide dit « recreate ». Rejet justifié. Le texte cite la version 1.8.3 ; le code lu ici est celui de 1.11.2, sur ce point identique.
- **`copy` : vrai.** Une copie dont un côté est local passe par `PUT /commands/rsync/` (`vastai/api/storage.py` l. 10, 62), qui exige ssh et une machine en marche. La copie d'instance à instance (`/commands/copy_direct/`) est laissée en nœud (N10), à juste titre.
- **Transcriptions : vrai.** Les `ids-lot-*` sont ajoutés de force par `ajouter_legeres` (l. 277-279) dans le même commit que `runs` et `diag` (l. 306-308), puis poussés en une fois (l. 312). Le seul autre commit est la trace, poussée dans la même poussée.
- **Fichiers non poussés : vrai.** Journal complet, `run.err`, `tests.txt` et les autres : seule la fonction `traces` les prend (l. 351-354), et le chemin de redémarrage ne l'appelle pas.

## Script v3 : changements depuis le v2 et régressions

Le `diff` v2 vers v3 ne touche que l'en-tête et ajoute `lister` et `archiver`. `jouer`, `decider`, `etat`, `arreter` et `secrets` sont inchangés. Les corrections R1, R2, B1 et M1 sont donc intactes.

Essais rejoués sur le v3 avec mon faux outil (`scratchpad/verif-cl1-essais/`) :

| essai | ce que l'essai éprouve | résultat |
|---|---|---|
| A | relance saine, poussée faite | conforme : l'appel qui précède le `stop` est `logs` |
| B | tentative 1 refusée, puis poussée | conforme |
| C | relevés illisibles comptés une fois la machine en marche, arrêt au troisième | conforme |
| F | poussée impossible, arrêt jamais confirmé | deux `stop`, code 1 : conforme |

Aucun `destroy` et aucun autre identifiant dans ces essais.

## `lister` : conforme

- Machine arrêtée : 3 `execute` (`ls -l -R`, `ls -l -a`, `du`), aucun `rm`, aucun `start`, aucun `stop`.
- Machine en marche : refus, aucun `execute`.
- Identifiant 58936096 : refus.

Deux points à ajouter, sans effet sur le start :

- **L1 (recommandé)** : relire l'état après le troisième `execute`. Si le statut n'est pas `exited` ou `stopped`, appeler `arreter "ARRETER : machine en marche après execute"`. Rien ne dit que `execute` sur une machine arrêtée ne lance jamais le conteneur. S'il le lançait, l'amorce détruirait la machine 3 minutes plus tard, sans veille.
- **L2** : l'outil abandonne après environ 9 s d'attente du résultat (`_poll_result_url`). Une liste `ls -R` longue peut rendre un code non nul et une sortie vide. Le texte doit dire qu'un seul nouvel essai de `lister` est permis dans un dossier neuf ; sinon, P11 en défaut.

## `archiver` : deux défauts

- **A1 (à corriger avant emploi)**. La ligne `tar -tvf <(cat …)` échoue sur un tube : « Unaligned block (576 bytes) … exiting now ». La liste est tronquée, son code n'est pas lu, et le script affiche « ARCHIVE CONFORME ». Constaté sur 300 fichiers : 9 entrées listées sur 301.
  - Correction exacte : `cat "$out"/archive.tar.part-* | tar -tvf - > "$out/contenu-noms-tailles.txt"; [ "${PIPESTATUS[1]}" = 0 ] || { echo "ÉCHEC : liste du contenu"; return 1; }`.
  - Puis comparer au nombre d'entrées attendu : `[ "$(wc -l < "$out/contenu-noms-tailles.txt")" = "$(find "$@" | wc -l)" ] || { echo "ÉCHEC : entrées ≠ chemins"; return 1; }`.
  - Par la lecture standard, j'obtiens 301 entrées sur 301, code 0. Le réassemblage, l'extraction (identique à la source) et `morceaux.sha256` sont justes.
- **A2 (mineur)**. L'empreinte de l'archive entière est écrite par un processus en arrière-plan, et le script ne l'attend que par `sleep 1`. Sur une grosse archive, la lecture peut venir trop tôt : le contrôle échoue alors à tort, mais sans danger. Correction : remplacer `sleep 1` par `wait $!`, ou bien calculer l'empreinte du tar sur le réassemblage seul, puis comparer aux empreintes des morceaux.

## Étape 5 du texte

- **E1 (mineur)**. Le motif `traces/iib-consignation-*` passé à `archiver` prend aussi les traces anciennes de l'arbre au commit 43d6d067. Passer les seuls chemins ajoutés, lus dans `diff-name-status.txt` (même point que m3).
- La branche `donnees/iib-v5-etalonnage-disque-61875617-v1` ne porte rien de plus que `essai/iib-explo-v6`. Le texte le dit. Nom confirmé par la mère.

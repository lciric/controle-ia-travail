# Arrêt de la session de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — refus du classifieur chez le préparateur — v1

Session conductrice `session_013QMayjNC5GKdDFTN87oAV5`, 2026-11-18. Aucune mesure, aucun score, aucune aire, aucune issue n'a été lu par quiconque dans cette session. La garde d'ouverture n'a pas été jouée ; la lecture n'a pas été lancée ; le fichier de commande `commande-lecture-bbis-v1.md` n'est pas écrit.

## Refus, mot pour mot (rendu par le préparateur, sous-agent neuf, modèle Fable 5.2)
> Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]. If you have other tasks that don't depend on this action, continue working on those. IMPORTANT: You *may* attempt to accomplish this action using other tools that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you *should not* attempt to work around this denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is essential to complete the user's request, first try a safer method. Get as much of the rest of the task done as you can, then STOP and explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed. To allow this type of action in the future, the user can add a permission rule for Bash to their settings.

Commande refusée (selon le préparateur) : l'essai, sur l'arbre principal, d'un brouillon de garde d'ouverture rejouée à blanc (`garde_a_blanc.py`, par `.venv/bin/python`, `PYTHONPATH=src`), qui appelle les fonctions de `lecture_v3` sur les registres. Rien n'a été reformulé, découpé ni contourné ; la conductrice ne l'a pas rejoué.

## Points ouverts rendus par le préparateur (titres, non vérifiés par la conductrice)
1. **Bloquant** : la garde d'ouverture refuserait sur le registre propre tel qu'il est — les lignes `GO-BBIS` et `CODE-BBIS` (remplacement) portent la même seconde (2026-11-17T11:05:29Z), alors que le second addendum (SA-11) exige « strictement après ». Refus rendu par `lecture_v3.exiger_ordre_propre`, joué sur le seul registre propre : « ligne GO-BBIS (2026-11-17T11:05:29Z) pas strictement antérieure à CODE-BBIS (2026-11-17T11:05:29Z) ». Nœud, non tranché.
2. Histoire du registre propre non linéaire : commits `ff24998f8` (première ligne `CODE-BBIS`) et `31fa8ac60` (premier `GO-BBIS` du 16 novembre) hors de l'ascendance de `main` ; sur `main`, remplacement et `GO-BBIS` entrent ensemble (`c098fb512`), première ligne `CODE-BBIS` remise après (`06c883281`).
3. La garde n'est pas séparable de la lecture : `main()` joue les deux ; sur un refus de garde il écrit quand même `lecture-bbis.json` et sort en code 0.
4. Le manifeste exige un arbre propre, vérifié après le calcul : les entrées doivent être commitées localement dans l'arbre de lecture.
5. Arbre de lecture : arbre de travail séparé plutôt que clone local (la garde cherche avec `git log --all`) ; disque : 14 Go libres.
6. Entrées sur trois branches : `donnees/t07-etape-b-bis-v2` (tête `7322049d…`, conforme) ; `calcul/t06-confirmation-7b-v1` (tête `55c3e3eb…`, porte aussi deux fichiers de la liste « Jamais ») ; `verdict/t06-mots-et-cout-compte-3-v1` (tête `8b6b0303…`, absente de `main`).
7. Replis silencieux à la mise en place (fichier de scores absent → sources « non calculables » sans arrêt).
8. Journal des ouvertures : aucune fonction ne le crée à vide.
9. Environnement : contrôle d'égalité de la base « mots et coût » à 10⁻¹², fils à 1, versions figées.
10. `main()` en mode réel couvert par aucun essai ; durée non estimable.
11. Sorties de lecture : aucune branche de données nommée par le texte.

Écart du mandat de session : il nomme `lecture_v2.py` ; le second addendum (SA-7) met `lecture_v3.py` en vigueur (empreinte `c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`, conforme à la fiche `code-bbis-v2.json`).

## Qui a lu quoi
| agent | modèle | fichiers de résultat ouverts |
|---|---|---|
| conductrice | Fable 5.2 | aucun (textes scellés, feu § 12-13, registre propre, fiche de code, noms de fichiers) |
| préparateur | Fable 5.2 | aucun contenu ; empreinte calculée sans affichage de `docs/verdicts/verdict-P3-bis-v1-issue.json` et de `diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json` ; recherches bornées : cinq lignes des clés « lues, jamais écrites » de `registres/scellements-v1.md`, clé et heure de sa ligne `VERDICT-T07-ETAPE-B`, deux lignes de `registres/qui-a-lu-quoi-v9.md` ; noms et commits par `git ls-tree`, `git log`, `git ls-remote` ; essais sur jouets : 106 passés |
| contre-lecteur, lecteur-opérateur, juge | — | non lancés |

## Laissé sur la machine de la session
`.venv` (ignoré par git) ; brouillons du préparateur hors dépôt, dans le dossier temporaire de la session (`scratchpad/prep/` : `preuve_anteriorite.py`, `controle_mise_en_place.py`, `garde_a_blanc.py` jamais joué). Histoire complète du dépôt récupérée ; branche des sorties récupérée, tête conforme.

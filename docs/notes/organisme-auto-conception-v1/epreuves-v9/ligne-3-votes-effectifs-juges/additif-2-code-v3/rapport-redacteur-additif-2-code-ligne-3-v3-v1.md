# Rapport du rédacteur — additif 2 (code) de la ligne 3, version 3 — v1

Pièce de travail (classe C), 2026-11-20. Rédacteur neuf, modèle F. Dossier de travail (noté D) : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-2-code-v3/`. Rien écrit dans le dépôt, aucun commit ; rien sous `/root/.claude/` ni sous `archives-reponses-modeles/` ; aucun calcul, aucun lancement du banc, aucun appel de modèle, aucune dépense ; aucun refus de permission, de classifieur ou de garde.

## Verdict

La version 3 est écrite : les corrections 1 et 2 du contrôle sont portées à la lettre, le titre et la ligne de statut passent à 3, une phrase de version nomme le contrôle par son empreinte. Quatre remplacements, trois lignes changées, rien d'autre.

## Pièces qui font foi, vérifiées

| pièce | sha256 | contrôle |
|---|---|---|
| mandat `mandat-redacteur-additif-2-code-v3-v1.md` | `47d159654125e4f4b9c54c5e3ba1810a259356e3d3a88c99017df100a65b2cef` (annoncée) | `sha256sum -c` du compagnon : OK |
| contrôle `controle-differentiel-additif-2-code-v1-v2-v1.md` | `97f51ce83649aade410ca0c586e651caf853da6164e99cbc211824e0538ae6e3` | recalculée, égale au mandat et au compagnon |
| additif v2 (cible) | `186501571b1e6cf03e3abff1991a987f86ed591a0bda00864e3df77f851c0ce5` | recalculée, égale au compagnon et au début annoncé |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | recalculée, début égal à celui du mandat |

`python3 --version` : Python 3.13.18.

## Les quatre remplacements

Chaque ancre comptée par `grep -c -F -e` sur la v2 avant l'appel : 1 chacune. Outil : « FAIT : 4 remplacement(s) », cible `18650157…`.

1. Titre : « racines autorisées — v2 » → « racines autorisées — v3 ».
2. Ligne de statut : « **Statut : version 2, non scellée. » → « **Statut : version 3, non scellée. »
3. Correction 1 du contrôle, à la lettre : « au § 6 et au § 7 ; rien d'autre ne change. » → « au § 6 et au § 7 ; hors le numéro de version (titre, ligne de statut), rien d'autre ne change. », suivie, dans le même remplacement, de la phrase de version, de ma main : « Version 3, même jour : elle porte à la lettre les corrections 1 et 2 du contrôle `controle-differentiel-additif-2-code-v1-v2-v1.md` (`97f51ce8…`, écrite en entier) sur la version 2 (`18650157…`, écrite en entier), à cette ligne de statut et au § 9 ; hors le numéro de version (titre, ligne de statut) et cette phrase, rien d'autre ne change. »
4. Correction 2 du contrôle, à la lettre : « pour la seule contrainte connue » → « pour les deux contraintes connues » (§ 9, réserve 3).

Différentiel lu : trois lignes changées (1, 3 et 157), aucune autre.

## Fichiers rendus (dans D, chacun avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` |
| `remplacements-additif-2-code-v2-v3-v1.json` | `b0b35e0d5a37efe82bb299c5ef0844b91a184fe6d00135bc72623d0ecc8d965a` |
| `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md.journal-remplacements-v1.json` | `551cf3a0e15df910c3c8f3046a34e9fa1dceb2a7a6153d332eb0ea306b001fa9` |
| `differentiel-additif-2-code-v2-v3-v1.diff` | `1bb8065696c98a89b5ee8f87860697fc706b5ba69e4b6f3cde2f18dd849c37eb` |

## Écarts et réserves

1. La phrase de version et la correction 1 sont dans un seul remplacement (la phrase suit la correction sur la même ligne ; une ancre séparée aurait demandé un saut de ligne, que `grep -c -F -e` ne compte pas). Le texte de la correction 1 est à la lettre, en tête du texte neuf.
2. La phrase de version dit « et cette phrase » : sans ces mots, « rien d'autre ne change » aurait répété l'inexactitude que la correction 1 lève. C'est un choix de ma main, à contre-lire.
3. Je n'ai pas lu le texte de la règle R-4067 dans le registre (aucun chemin donné, recherche large interdite) ; j'ai suivi ce que le mandat et l'en-tête de l'outil en disent : appel par chemin avec `python3 -B`, textes dans un JSON écrit par l'outil d'écriture de fichiers, ancres comptées avant l'appel, sortie sous un nom neuf.
4. Le différentiel porte les chemins absolus et les heures de `diff -u` en ses deux premières lignes.
5. La v3 n'est ni scellée ni posée dans le dépôt : ces gestes reviennent à la mère, après contre-lecture (règle R2).

Rédacteur neuf, modèle F.

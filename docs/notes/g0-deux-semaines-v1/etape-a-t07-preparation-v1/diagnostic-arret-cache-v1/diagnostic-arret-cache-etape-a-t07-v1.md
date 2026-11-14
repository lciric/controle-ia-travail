# Diagnostic de l'arrêt de l'étape A de T0.7 (R-2588) — v1

Session mère, 2026-11-13T20:40:58Z (`date -u`). Établi **sans dépense ni réseau**, sur la machine de la mère. Aucune pièce de T0.6 (7a, 7b), de T0.7 ou de P3-bis lue ; aucune donnée interdite touchée.

## Verdict
L'arrêt vient d'une **incompatibilité entre le code scellé et la bibliothèque `huggingface_hub` 1.33.0**, pas d'un cache incomplet ni d'une faute de l'instance. La garde a fait son travail : arrêt avant l'ouverture, rien d'ouvert, rien de lu. **Elle s'arrêtera de nouveau à chaque relance tant que le code n'est pas corrigé.**

## Mécanisme (code lu)
1. Le préchargement (`src/controle_ia/harnais/modeles.py`, `precharger_modele`) télécharge en ligne **dix des dix-sept fichiers** du dépôt du modèle, par `allow_patterns=MOTIFS_PRECHARGEMENT` (le dossier `original/`, 16 Go, et quatre fichiers de texte restent dehors, comme voulu).
2. Pendant ce téléchargement en ligne, `huggingface_hub` 1.33.0 écrit au cache la **liste complète de l'arbre du dépôt** (`<cache>/models--…/trees/<commit>.json`, `_tree_cache.write_tree_cache`).
3. Le contrôle avant l'ouverture (`src/controle_ia/t07/reextraction_p3_v1.py`, `revision_au_cache`, code scellé de `CODE-T07`) appelle `snapshot_download(local_files_only=True)` **sans motifs**.
4. Hors ligne, la bibliothèque compare alors l'instantané à **toute** la liste de l'arbre (`_snapshot_download.py`, `_raise_if_incomplete_snapshot`) et lève `IncompleteSnapshotError` ; la fonction scellée la traduit en « absent du cache local ». **Sans liste de l'arbre au cache, la bibliothèque ne contrôle rien** (« If the tree listing is not cached we cannot tell, so we do nothing ») : c'est pourquoi les essais et les répétitions hors ligne passaient.

## Preuve (reproduction locale)
- Script : `reproduire_arret_cache_v1.py` (sha256 `8a85a3f7d55332f93a8d29992c35e0a4ba906b9624e183a19400b3a305a74bba`) ; sortie : `sortie-reproduction-arret-cache-v1.txt` (sha256 `88360a5d77d7226dad27ace5f92aa2f00d2fb88b4faadb1cfe932b3c13e5fee3`). Chaque cas tourne dans un processus neuf, comme sur l'instance.
- Cas 1, code scellé, liste de l'arbre présente : **ARRÊT**, message identique à celui de l'instance, au caractère près.
- Cas 2, mêmes motifs que le préchargement : **passe**.
- Cas 3 et 4, chargeur de `transformers` 5.18.0 hors ligne (gabarits, puis fichiers du modèle) : **passent**. Le chargeur demande ses fichiers par motifs, et l'erreur de complétude dérive de `LocalEntryNotFoundError`, que le chargeur rattrape. **Le seul appel touché du dépôt est `revision_au_cache`** (recherche de `snapshot_download` et `local_files_only` dans `src/` et dans le script de l'étape A).
- Cas 5, témoin, liste de l'arbre retirée : le code scellé **passe**.

## Leçon (R4, R5)
Le cas sain des essais de la garde n'était pas représentatif : ses caches factices n'avaient pas la liste de l'arbre que la bibliothèque écrit sur une vraie machine. Tout essai neuf de la garde doit partir d'un cache produit comme sur l'instance (cas 1 de la reproduction).

## Ce que la correction touche (nœud, non tranché ici)
Corriger, c'est modifier un module épinglé de `CODE-T07` (commit `b4cd9953…`), donc l'ordre d'exécution scellé : **écart à un texte scellé, décision de Lazar**. Correction minimale proposée : passer à `snapshot_download` les motifs du préchargement, dans une version nouvelle du module ; essai de régression tiré du cas 1 ; contre-lecture par un lecteur neuf d'un autre modèle ; addendum de T0.7 ; ordre version 2. Aucune règle d'analyse ne change.

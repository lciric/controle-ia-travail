# Note de revérification — ordre de l'étalonnage, brouillon 5 — cl1

Date : 2026-11-21. Même vérificateur (Claude Opus 5.5), même mandat. Pièce : `ordre-etalonnage-ii-b-v5-brouillon5.md` (`3bde656a…`, compagnon vérifié).

**Verdict : F1, F2 et m1 levés ; scellable une fois les neuf champs remplis.**

- **Rejeu** : `fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py`, joué sur mon brouillon 4 rejoué avec la date écrite dans sa note. Le brouillon 5 et la note des différences 4→5 sont **identiques à l'octet**. La note cite ma vérification par son empreinte, `958b5f94…`, qui est juste. Les neuf champs sont inchangés.
- **F1** : la table du § 7 donne les chemins que le code écrit à la tête c4b5115b (arbre `ed9b0e48…`, celui de mon `arbre-final`), et ma répétition les montre :
  - `diag/<run>/lots/lot-*.json` et `donnees/<run>/lots/ids-lot-*.json` ;
  - `diag/<run>/etalonnage-oracles-iib-v5.json`, `diag/<run>/graines-etalonnage-iib-v5.json` et `diag/<run>/rapportes-etalonnage-iib-v5.json`, ce dernier avec les durées par oracle ;
  - `diag/<run>/resume.json` et `diag/<run>/arret.json`, écrits par `manifeste.ecrire_resultat` ;
  - `runs/<run>/manifeste.json` ;
  - aucun fichier d'ensemble des identifiants.
  
  Les fichiers `branches-iib-v5.json` et `designation-iib-v5.json` sont nommés sans préfixe ; ils sont dans le même `diag/<run>/` (phase des conditions). Ce n'est pas un écart.
- **F2** : les correctifs 9 à 11 portent le chemin `distillateur-v5/correctifs/…`, et la phrase des chemins est juste.
- **m1** : la phrase des marques de progrès est conforme au code (chargement, début, lots, oracles écrits, fin, arrêt).

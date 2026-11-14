# Confirmation des champs de T0.7 lus par le texte « validité de l'adaptateur » — au commit de fusion `c2fab6cc` — v1

Écrite le 2026-11-14T00:28:49Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur des brouillons 4 et 5 du texte, lecteur de T0.7 scellé (déjà déclaré à la mère). Prolonge la pièce `brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-c7-v1.md` (`f91452ed3e34a83b7c1c33c0cd74219b9340a2bcfb9beea805e4509910b9f2e7`), gardée telle quelle, pour les deux lignes qui venaient de `reextraction_p3_v1.py` (VB4-02 ; R-2593, R-2597 point 3, R-2604 et R-2605 point 3).

## 1. Commit lu

- `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` (« fusion du correctif du contrôle de cache », message de commit de `main`), que la mère a annoncé comme le futur commit de la ligne `CODE-T07` (R-2604, R-2605, point 3). **L'égalité de ce commit avec la ligne `CODE-T07` en vigueur n'est pas vérifiée ici** (registre interdit à ce compte) : elle est à confirmer par la mère, qui remplit ou fait remplir le marqueur `<<COMMIT_C7_T07>>`.
- Commit de comparaison : C7 `b4cd9953` (pièce précédente).

## 2. Ce qui est vérifié (commandes `git` sur les deux commits, sans `checkout`)

| point | commande | résultat |
|---|---|---|
| fichiers du module changés entre C7 et la fusion | `git diff --stat b4cd9953 c2fab6cc -- src/controle_ia/t07/` | un seul : `reextraction_p3_v1.py` (14 lignes ajoutées, 2 retirées) |
| les 26 autres entrées du module identiques | `git ls-tree <commit> src/controle_ia/t07/` sans `reextraction_p3_v1`, puis `sha256sum` de la liste | `c89f99637a623309fef4ee215af9d8d54246fdb6e9bd9855cc043d08fc3f5bee` (C7) = `c89f99637a623309fef4ee215af9d8d54246fdb6e9bd9855cc043d08fc3f5bee` (fusion) |
| `reextraction_p3_v1.py` | `git show <commit>:…` puis `sha256sum` | C7 `c32696b82af620e5da07fc4ec5bbb801dc385467cbf8235b799ad28b6471eaf9` ; fusion `af299587e6c73d7bcc67c881eb968ee997b09e576b28d4b22e76976a74bc7afb` |
| nature du changement | `git diff b4cd9953 c2fab6cc -- …/reextraction_p3_v1.py` | seule la fonction `revision_au_cache` change : `snapshot_download(…, local_files_only=True)` reçoit `allow_patterns=list(MOTIFS_PRECHARGEMENT)` (importé de `harnais.modeles`), et sa documentation dit la cause de l'arrêt (R-2588, R-2589) ; aucun autre corps de fonction touché |
| dépendances lues par le texte | `git diff --stat b4cd9953 c2fab6cc -- src/controle_ia/harnais/modeles.py src/controle_ia/premier_test_ia/figees.py src/controle_ia/premier_test_ia/conditions.py` | 0 ligne de différence (aucune) ; `MOTIFS_PRECHARGEMENT` existe déjà à C7 (`harnais/modeles.py` l. 106) |

## 3. Les deux lignes revérifiées

| champ | au commit de fusion | contenu |
|---|---|---|
| états de la réextraction | `reextraction_p3_v1.py` l. 565 (l. 553 à C7) | inchangé : `etablis = {n: x for n, x in r["par_sonde"].items() if x["etat"] == "établi"}` ; seuls les bras d'état « établi » ont leurs directions écrites |
| `meta` de `planchers-figees-t07.npz` | `reextraction_p3_v1.py` l. 570-571 (l. 558-559 à C7) | inchangé : `{"planchers": {<sonde>: [<noms>]}, "graines": {<sonde>: <clé>}, "methode": METHODE}` |

Les autres champs de la pièce précédente viennent de modules dont l'entrée est identique à C7 (point 2) : ils valent tels quels au commit de fusion, aux mêmes lignes.

## 4. Réserves

- Confirmé par l'auteur du texte, **non par le développeur de T0.7** (non joignable, mot de la mère du 13 novembre) : réserve inchangée.
- Le commit de la ligne `CODE-T07` n'est pas lu au registre (point 1) ; si la mère annonce un autre commit que `c2fab6cc`, cette pièce est refaite sous un nom neuf.
- Aucune exécution du code : lecture des textes des fichiers aux deux commits seulement.

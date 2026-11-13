# Champs du texte « validité de l'adaptateur » fixés par le seul code de T0.7 : confirmation sur le code au commit C7 — v1

Écrite le 2026-11-13T21:23:06Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, Claude Opus 5.5), auteur du brouillon 4, sur le mot de la mère du 13 novembre (« Confirme les champs en lisant le code au commit C7 et ce rapport ; écris la réserve », journal provisoire du compte 4, C4-0009). **Réserve** : cette confirmation est celle de l'auteur du texte, non celle du développeur de T0.7 (sous-agents développeurs de sessions mères closes, non joignables selon la mère).

## Sources

- Commit C7 cité par la ligne `CODE-T07` : `b4cd9953d199dd8f220f5162e5868c5b00fd392d`, obtenu par `git fetch --depth=1 origin b4cd9953d199dd8f220f5162e5868c5b00fd392d:refs/remotes/origin/c7-t07-b4cd9953` ; lu par `git show <commit>:<chemin>`, fichiers nommés seulement.
- **Égalité avec `main`** : les vingt-six modules `src/controle_ia/t07/*.py` au commit C7 ont la même empreinte que dans l'arbre de `lot/compte-4-v1` (= `main` à `89a42d13`) ; de même `premier_test_ia/figees.py`, `premier_test_ia/conditions.py`, `t06/lanceur.py`, `t06/test_croise.py`. Les numéros de ligne de la contre-lecture 2 (relevés sur `main`) valent donc au commit C7. `lecture_v4.py` au commit C7 : `42f60780e6944568…`.
- Rapport v3 du développeur, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v3.md`, `be2c86e215a1a7a0e41f646e60acaa20a39f0b626c6cd1b0807066348305b159` (égal à son compagnon) : il écrit `n_plancher` 800 (l. 56) et le refus de 200 en mode réel (l. 85) ; il ne nomme pas les champs du résultat ci-dessous, que seul le code fixe.
- Rapport de la contre-lecture 2, § 4, `11f7242b…` : liste des champs à confirmer.

## Champs confirmés au commit C7

| champ | lieu au commit C7 | ce que le code écrit |
|---|---|---|
| `n_plancher` = 800 en mode réel | `lecture_v4.py` l. 108-111 | refus (`GardeArret`) si `n_plancher` ≠ `N_PLANCHER_REEL` |
| forme de `plancher_<k>` | `lecture_v4.py` l. 174-178, 260 | `plancher_<k>` = `scores_plancher_vectorises(plancher, seqs).T` ; refus si son nombre de lignes, ou `plancher.n`, diffère de `n_plancher` |
| plancher décisif des sondes figées | `lecture_v4.py` l. 252-262 | plancher pris dans les planchers neufs réextraits (`planchers_p3[s.nom]`) ; `entree["plancher"]` = `{"n", "source", "notation", "empreintes_deux_premieres"}` ; les 200 de P3 vont dans `plancher_p3_<k>` et `entree["plancher_p3"]`, `"lecture": "descriptive"` (l. 246-249) |
| `index.sondes[k].etat` | `lecture_v4.py` l. 240, 267-268 | « notée » par défaut ; « échec » (avec `echec` = motif) sur `GardeArret` |
| `resultat.planchers_figees` de `notation-t07.json` | `lecture_v4.py` l. 440, 547-550, 554 | `{"fichier", "n_plancher", "etats", "paliers", "reextraction"}` ; `fichier` = `{"chemin", "sha256", "directions"}` (rendu de `ecrire_planchers`) ; écrit par `ecrire_resultat(…, "notation-t07", …)` |
| états de la réextraction | `reextraction_p3_v1.py` l. 553 | seuls les bras d'état « établi » ont leurs directions écrites |
| `meta` de `planchers-figees-t07.npz` | `reextraction_p3_v1.py` l. 557-558 | `{"planchers": {<sonde>: [<noms>]}, "graines", "methode"}` |
| `fichiers_sondes_neuves` | `lecture_v2.py` l. 788-789 | `{"sondes": {"chemin", "sha256", "nombre", "planchers"}, "temoins_lexicaux": {"chemin", "sha256"}}` |
| littéraux de `entrees.Q` | `criteres_v1.py` l. 48, 697 | `("illisible", "non_calculable", "incoherent", "vide", "partiel", "complet")` ; `"entrees": {"G", "P", "A", "Q", "I", "II", "F"}` |
| forme de `reserves_identifiees` | `lectures_t07_v1.py` l. 423-463 | entrées `{"id", "phrase", "motif"}`, plus `"concept"` pour R8 ; aucune clé de sonde |

## Réserves

1. **Ce n'est pas la confirmation du développeur de T0.7** : celui-ci n'est pas joignable (mot de la mère, point 4) ; l'auteur du texte confirme sur le code, et la contre-lecture 2 l'avait vérifié avant lui sur `main`.
2. **Le commit C7 va changer** (mot de la mère, point 7 : correctif du contrôle de cache, seul `reextraction_p3_v1.py` touché, R-2593). Les deux lignes qui viennent de ce fichier (états « établi », `meta` de `planchers-figees-t07.npz`) sont à revérifier au commit qui remplira le marqueur `<<COMMIT_C7_T07>>` du brouillon 4 ; les autres viennent de fichiers que le correctif ne touche pas, et sont à recontrôler par empreinte.

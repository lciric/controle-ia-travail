# session-depot → conv-audit — n° 117 — 28 octobre 2026, 20:52 UTC

**Relecture ciblée v34 → v35 rendue : « lançable après corrections », aucun bloquant.** Rapport sur `main` :
`docs/notes/ideation-organisme-v1/contre-lecture-v35-cl3.md` (`d5ae6cc6…`), scripts dans `contre-lecture-v35-cl3-outils/`.
312/312 essais, 142/142 empreintes ; CL34 : 9 corrigés, 4 en partie (03, 04, 08, 09). « Aucun outil » vrai ; borne de
temps démontrée sans orphelin (ajoute l'essai du sous-processus qui pend).

**Je te demande une v36 courte** — les quatre majeurs, tous sur le bras différé d'Argon :
- CL35-01 : coût NaN (et infini, négatif) → `erreur` ; jamais d'écriture de notes sans manifeste (`adaptateurs.py:408-414`).
- CL35-02 : coût imprimé avant une sortie ≠ 0 compté, pas 0 (`adaptateurs.py:396-398`).
- CL35-03 : commande d'Argon et empreintes de ses fichiers au manifeste du bras (le code de la v35 est mort, `ideation_v1.py:283-314`).
- CL35-04 : bras différé sans `--commande-juge-externe` → refus avant tout appel ; jamais de juge simulé sur une course réelle (`ideation_v1.py:291-292`).
Et, à bas coût : CL35-06 (refuser dans `executer_ideation` tout adaptateur de juge qui n'est pas Claude), les trois
contradictions du devis (commande d'Argon refusée dans la course ; `--variable-transmise` exposé, refusé pour un nom de
clé ; part d'Argon : plafond séparé de 3 ou total relevé à 20, à dire au devis), puis les mineurs du rapport à ton choix.
J'annonce d'avance la relecture ciblée v35 → v36 chez moi (Opus) ; préviens-moi quand c'est poussé.

# Vérification de la passe v3 (Sonnet), 2026-11-24, 18:31Z

Empreintes lues : passe 0b6b24f7, préparation 181c5d9d, essais a41fa784, aide 3dc06e50. Aucune donnée du programme lue ; dépôt intact.

Verdict : corrections vérifiées.
- Diff v2 vers v3 limité à l'annoncé : en-têtes, lecteur v7 dans la docstring, `lignes_de_scores` et le bordereau (`"lecteur": …versant_honnete_v7.py`) ; essais : import v7, nouvelle fixture, essai de bout en bout par la v7 avec existant null (639 sur 640, code 0), artefact direct du doublon et sa mutation ; aide : en-tête seul. Aucun calcul changé.
- Mention restante de la v6 : aucune. Seul reste le nom `passe_recalcul_v6.py`, un fichier d'une autre pièce cité en commentaire.
- Mutation du doublon (garde du doublon retirée au niveau du source) : tuée par `test_doublon_de_tirage_artefact_direct`.
- 63 essais passent.

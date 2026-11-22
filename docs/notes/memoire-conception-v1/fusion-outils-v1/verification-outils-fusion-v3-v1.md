# Vérification des outils de la fusion (v3) — v1

Vérificateur : Claude Sonnet 5.5, 22 novembre 2026, commit `f105f61f` (`listes_lecture_v3.py`, `recherche_bornee_v5.py`, `partition_journal_v3.py`, `test_fusion_outils_v3.py`). Même cloisonnement de lecture ; rien modifié ; essais dans `/tmp/cl/` (dépôt jetable `r2`). Les 124 essais passent.

## Constat : corrections vérifiées, aucun défaut restant

- **R1 (branche principale figée)** : `--ref-principale` (et l'abréviation `--ref`) → « unrecognized arguments » ; commit de `lot/compte-4-v1` sans option → `ARRET … ancêtre de la branche principale` ; commit de `main` lu normalement. Dans la partition, un commit de la branche exclue → « commit hors de la branche principale » ; les références sont une constante `("origin/main", "main")` sans paramètre en ligne de commande.
- **R2 (exclusion « 24 »)** : refusés à la boucle et à la stricte : `demandes-24-v1.md`, `reponses-24.md`, `demande-024`, `demande-24`, `reponse_24a`, `Réponse 24.md`, `demande-18-24`, `demande-24-nouveaux`, et `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` (« demande ou réponse 24 exclue »). **Aucun faux positif** : `demande-41`, `demande-240`, `reponse-124`, `demande-241`, `demande-1024`, `demande-2024`, `demandes-12-v1.md` restent « plein ».
- **D-1 étendue** : `reecriture-v3/x.md`, `REECRITURE-V3/x`, `questions-fond-v1/….sha256`, `Questions-Fond-v1/x.md` → refusés à la stricte (sans casse).
- **Chiffres ASCII** : `journal-commun-٢٠٢٦-…jsonl` refusé.
- **Garde étendue à `repere` et `sert`** : `repere="consigne-privee: 0.37"`, `sert="Vérité seuil"`, `sert="quarantaine/x"` → « nom exclu dans nom ou mots » ; cas sain inchangé.

Reste déclaré, non défaut : la liste d'exclusion « 24 » reste un motif de nom (un fichier sur la demande 24 sans « demande/réponse 24 » dans son nom n'est pas vu) ; `main` local est supposé non repointé par l'appelant ; l'outil de l'historique git reste à écrire.

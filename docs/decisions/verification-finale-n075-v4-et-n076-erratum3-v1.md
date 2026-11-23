# Vérification finale courte — version 4 de la décision N-075, erratum 3 de la décision N-076 et proposition pour `CLAUDE.md`

- **Verdict : `PRÊT À SCELLER EN L'ÉTAT`**
- **Date** : 2026-11-23T21:20Z (`date -u` ; dépôt sur `main` intact de mon fait, aucun fichier modifié dans `/home/antigravity/lciric/controle-ia-travail`).
- **Contre-lecteur indépendant** : même sous-agent neuf contre-lecteur R2 (distinct de l'auteur `5aa04b1812ef837c1c7dbb497aaa57cd`), en passe courte finale après la première contre-lecture (`contre-lecture-n075-v4-et-n076-erratum3-v1.md`, empreinte `41979f6ba6c334c30b8fe68d227bd9b88ec214df699570278aec19a2d55425c8`).

---

## Contrôle des quatre retouches demandées

1. **Empreintes des six livrables et compagnons `.sha256`** (`scratch/redaction-n075-n076/`) :
   - Vérification par `sha256sum -c *.sha256` : **6 sur 6 conformes** (`decision-N-075-issue-plancher-et-deux-regards-v4.md` à `e4039549b5675ac0ab42bfcf3c869c2711a8522c4f43bd5e11b392b22eb6dd23`, 362 lignes, 95 279 octets ; `table-remplacements-n075-v3-vers-v4.md` aligné sur cette empreinte et cette taille).
2. **Défaut 1 (`decision-N-075-issue-plancher-et-deux-regards-v4.md`, ligne 348, via `generer_n075_v4.py`)** :
   - **Porté et vérifié.** La ligne 348 lit désormais : « `Numéros de ligne de la version 3 d'origine, calculés par programme lors de son établissement sur un passage unique à chaque fois.` », en cohérence exacte avec la colonne « `lignes de la v3 d'origine` » de la ligne 350.
   - Le rejeu en mémoire de `generer_n075_v4.py` (44 remplacements uniques) et de `diff -u` (`n = 2`) contre la version 3 (`5aed4bab…`) reproduit à l'octet près `decision-N-075-issue-plancher-et-deux-regards-v4.md` et `diff-decision-N-075-v3-contre-v4.patch`. Aucun autre passage n'a dérivé.
3. **Précision de ponctuation (`decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md`, lignes 36 et 56)** :
   - **Portée et vérifiée.** `E3-3` (ligne 36) précise désormais « `Ajouter à la fin de l'alinéa (avant le point final de la ligne 308) : ...` » et `E3-9` (ligne 56) précise « `Ajouter avant le point final de la ligne 308, immédiatement à la suite de E3-3 : ...` ».
4. **Défauts 2 et 3 (`proposition-ligne-claude-md-n075-n076.md`, lignes 15 à 22 et 28 à 39)** :
   - **Portés et vérifiés.**
   - Segment N-076 proposé (ligne 17) : rétablit intégralement « `prévision scellée avant G1` » et « `à faire` » après « `boucle, devin` » ; mesure exactement **598 signes** sans le chevron ni son espace (plafond de 600), en accord exact avec l'en-tête de la ligne 15 et le détail des condensations à la ligne 22.
   - Segment N-075 proposé (ligne 34) : mesure exactement **597 signes** sans le chevron ni son espace (plafond de 600), en accord exact avec l'en-tête de la ligne 32 et l'explication de l'écart d'un point final par rapport à la ligne 267 de `decision-N-075-issue-plancher-et-deux-regards-v4.md` (ligne 37) ainsi que la mention explicite des deux raccourcis de mots (« `à démontrer` » et « `sur l'oracle` ») à la ligne 39.
   - Les segments « actuels » (lignes 13 et 30) concordent caractère pour caractère avec la ligne 13 de `CLAUDE.md` (631 et 597 signes).
   - Zéro emoji, aucun nouvel acronyme non développé indûment.

---

## Ligne « qui a lu quoi »

- **Sous-agent contre-lecteur indépendant (R2)** (passe courte de vérification finale, 2026-11-23T21:20Z) — **relu et contrôlé par programme** : les six livrables révisés et leurs six compagnons `.sha256` dans `scratch/redaction-n075-n076/`, `CLAUDE.md` (ligne 13) et le rejeu de `generer_n075_v4.py` et `diff -u` contre `HEAD:docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`. **Non modifié** : aucun fichier du dépôt `/home/antigravity/lciric/controle-ia-travail`. **Non lu** : `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/*`.

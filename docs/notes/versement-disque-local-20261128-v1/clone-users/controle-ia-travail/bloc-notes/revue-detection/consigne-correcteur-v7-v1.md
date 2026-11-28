# Consigne du correcteur neuf de la revue « comment détecter » — v7 — v1

Session 16, 2026-10-21 vers 00:45 UTC (heure vraie). Dépôt de travail `/home/user/controle-ia-travail` (noté `R`, lecture
seule). Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection`.

## Qui tu es
Un correcteur neuf : tu n'as écrit ni la revue (v1 à v6), ni aucune de ses vérifications ou traitements. Français.

## Ce que tu fais
1. Lis (empreintes contre compagnons) : la v6 `…/synthese-comment-detecter-v6.md` (`124d06f8…`) ; la vérification
   `…/verification-v6-fidelite/verification-v6-fidelite-v1.md` (`30c79b0f…`, 4 constats et ses « remarques non comptées »).
2. Écris la v7 `…/synthese-comment-detecter-v7.md` par un script de remplacements exacts (chaque ancien texte trouvé une
   seule fois, sinon arrêt) : les quatre constats VV6-fidelite-01 à 04 en mots exacts ; puis, pour les remarques non
   comptées, la plus petite correction : mention « [Décision de Lazar en attente : …] » sur la puce N-030 et le nœud
   « Revendication » ; options (A) à (C) de P-017 rendues à P-017 dans l'en-tête ; aucune autre modification.
3. Écris `…/traitement-verification-v6-par-correcteur-v1.md` (une ligne par correction : passage de la v7) et une v2 du
   traitement du correcteur v5 `…/traitement-verification-v4-par-correcteur-v2.md` qui corrige seulement le compte des
   écarts (VV5-fidelite-08 : 13 écarts ; VV4-sens-04 n'en est pas un), la v1 restant intacte (R12).
4. Rejoue le différentiel v6 → v7 : rien d'autre ne change. Sceau compagnon `.sha256` (format `sha256sum`, nom relatif)
   pour chacun de tes fichiers ; script et sorties sous `…/correction-v7/`.

## Règles
- Écris seulement les fichiers nommés et `…/correction-v7/`. Aucun réseau. Ne lis jamais `R/prereg/P3-consignes-v1.md`,
  aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même pour une
  empreinte. Aucune recherche récursive. Aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ; aucune clé
  affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
Chemins et empreintes de la v7 et des deux traitements ; nombre de remplacements ; résultat du différentiel.

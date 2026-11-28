# Consigne du vérificateur neuf de la v6 de la revue « comment détecter » — lentille « fidélité » — v1

Session 16, 2026-10-21 vers 00:45 UTC. Dépôt de travail `/home/user/controle-ia-travail` (noté `R`, lecture seule).
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection`.

## Qui tu es
Un vérificateur neuf : tu n'as écrit ni la revue (v1 à v6), ni aucune de ses vérifications ou traitements. Français,
phrases courtes, quasi aucun acronyme.

## Ce que tu vérifies
Pièces (vérifie chaque empreinte contre son compagnon) : v5 `…/synthese-comment-detecter-v5.md` (`17069e06…`) ; v6
`…/synthese-comment-detecter-v6.md` (`124d06f8…`) ; traitement `…/traitement-verifications-v5-par-correcteur-v1.md`
(`aabed8bc…`) ; vérifications `…/verification-v5-fidelite/verification-v5-fidelite-v1.md` (`05472092…`) et
`…/verification-v5-sens/verification-v5-sens-v1.md` (`e3e4a650…`) ; dossier de travail du correcteur `…/correction-v6/`
(outils, sorties, `pdf/`).
1. Chaque constat est-il appliqué comme le traitement le dit, en mots exacts quand le rapport en donne ? Les 8 écarts
   déclarés sont-ils justifiés à la source ? VV5-fidelite-07 (2) : le compagnon du PDF de MA existe-t-il (vérifie sur
   disque, par son chemin exact) ?
2. Différentiel v5 → v6 : rien n'a changé hors des corrections déclarées ? Aucune jonction ne change le sens d'un texte
   voisin non touché ?
3. Contrôles à la page : rejoue les outils du correcteur ; ajoute tes propres contrôles sur au moins 20 phrases changées
   (à la page citée, sur les PDF de `…/correction-v6/pdf/` et `R/docs/sources/pdf/`), éprouvés sur artefact (R5). Les dix
   PDF retéléchargés sont-ils identiques à ceux de la v1 (empreintes) ?
4. Points laissés à Lazar : chacun porte-t-il sa mention « [Décision de Lazar en attente : …] » et n'est-il jamais écrit
   comme décidé (P-015 et la proposition (b′), P-017, nœud « Revendication », N-030) ?

## Où écrire et règles
- Seulement sous `…/verification-v6-fidelite/` : rapport `verification-v6-fidelite-v1.md` (en-tête ; « ## Verdict » parmi
  « conforme », « conforme après corrections », « non conforme » ; constats VV6-fidelite-NN avec gravité, où, ce qui est,
  ce qui devrait être, correction en mots exacts) et son sceau `.sha256` (format `sha256sum`, nom relatif) ; tes essais à
  côté, avec leurs empreintes.
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`,
  `R/diag/`, `R/traces/`, pas même pour une empreinte. **Aucune recherche récursive**, ni dans le dépôt ni dans le système
  de fichiers (pas de `find`, pas de `grep -r`) : lis les fichiers par leur chemin. Aucun réseau. Aucune commande git
  d'écriture ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité.

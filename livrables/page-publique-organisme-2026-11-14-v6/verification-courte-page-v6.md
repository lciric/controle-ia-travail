# Vérification courte de la page publique de l'organisme, version 6

**Verdict : « après corrections ».** Deux couples avant/après dans les trois lignes changées (C1 nécessaire, C2 mineur) ; un troisième hors des trois lignes, à décider par Lazar (C3). Le retrait demandé est fait, seul ; aucune phrase neuve ne donne de recette ; aucune n'en dit plus que le code public sur le nul.

- Écrit le 14 novembre 2026, vers 07:27 UTC (`date -u`), par un lecteur neuf qui n'a écrit ni la page ni son journal ; lecture seule, rien de commité, rien de poussé.
- Non lus : `diag/`, `runs/` de 7a et 7b, `docs/notes/bras-attaque/`, `donnees/bras-attaque*`.

## Pièces lues (empreintes recalculées)

| pièce | sha256 |
|---|---|
| `livrables/page-publique-organisme-2026-11-14-v6/diff-page-organisme-v5-v6.patch` | `1ff08c5ea3368e1264e56b65563cc91a7908c7bdb7c29651581e560fc7b4c88c` |
| `…/journal-page-organisme-v6.md` | `13d2f206…` (compagnon vérifié) |
| `…/README-corrige-v6.md` | `e1a181c1b1b03eb9e84733cd3293fd5fa648b310fa128431e3a3bf3dbfa9bc50` |
| `registres/decisions.md`, R-2653, R-2654, R-2655 (l. 2613 à 2615) | `cdf72f91a167…` |
| `docs/notes/publiabilite-note-organisme-v1/journal-note-organisme-v2.md`, § 1 (M1) et § 5 | `2fcbdb181f98…` |
| `docs/notes/publiabilite-note-organisme-v1/lecture-adverse-note-v1.md`, M1 | `948bf30eecbc…` |
| clone public, `orchestrator/pole/nul_v8.py` (en-tête, l. 1 à 91) | `cc452aafd171…` |
| clone public, `orchestrator/pole/nul_v9.py` (en-tête, l. 1 à 125) | `7ae450df2482…` |
| clone public, `resultats/attaque-goodhart-v2/README.md`, l. 63 | `c549a31b266b…` |

## Contrôles mécaniques

- Différentiel mot à mot (`git diff --word-diff` entre `1a1a419` et la branche locale `publication-v6`, commit `8294949`) : un seul fichier, `README.md`, trois lignes (15, 18, 140), aucun autre mot touché. Le `README.md` de `8294949` a l'empreinte du README scellé de la v6 (`e1a181c1…`).
- Retrait : « — reading its description is enough » n'apparaît plus ; la phrase finit par « it needs no optimisation against the judge. ». Rien d'autre n'est retiré de cette cellule (« 42 of the 48 reproduce the world's own law exactly », gardé par R-2593, est intact).
- Aucun identifiant de modèle de Claude dans le README de la v6 (recherche de mots : 0).

## Ligne 15 — description du nul : fidèle, n'en dit pas plus

- « the best-fitting member of its null » : `nul_v8.py`, argument 1 (dénominateur = maximum sur les membres) ; conforme à la lecture adverse M1 (b).
- « a fixed library plus members fitted on the known laws » ; « in v8, their pooled mixture and a tempered version of each survivor » : `nul_v8.py` l. 11 à 18 (bibliothèque aveugle ; « ajuste_lineaire:archive » ; « ajuste_log:archive:<survivante> »). La phrase dit **moins** que le code (membres non ajustés de l'archive, nul des filles, « inclinée » non dits) : simplification déclarée au journal, sans sur-affirmation. Option, non exigée : « a tempered and tilted version ».
- « v9 adds one-level piecewise recombinations » ; « Neither null covers every combination; each lists what it leaves out » : `nul_v9.py` l. 1 et 59 à 72 ; `nul_v8.py` l. 83 à 91 ; `NON_COUVERT_V9` l. 118. Fidèle.
- Recette : aucune ; la phrase renvoie à des listes déjà publiques dans le code.

## Ligne 18 — paragraphe d'état : fidèle, mais un constat négatif disparaît (C1)

- « one of the classes the v8 null declares uncovered (piecewise recombinations) » et « covers one-level piecewise recombinations and declares its own uncovered classes » : fidèles (`nul_v8.py` l. 83 à 91 ; `nul_v9.py` l. 59 à 67).
- **Écart non déclaré au journal** : le journal de la note (§ 5, point 2) proposait « found one of the classes… » ; la v6 écrit « tested ». La v5 disait que l'attaque avait trouvé le trou ; la v6 ne dit plus, à cet endroit, que v8 a été percé (24 unités sur 24). La brèche ne reste dans ce paragraphe que par l'incise finale « the out-of-class breach of the Goodhart attack ». C'est un retrait de plus que celui demandé, et il va dans le sens flatteur (R4).

**C1 (nécessaire).**
- Avant (v6) : `That attack tested one of the classes the v8 null declares uncovered (piecewise recombinations); a new null (v9), which covers…`
- Après : `That attack breached the v8 null in one of the classes it declares uncovered (piecewise recombinations); a new null (v9), which covers…`
- Pièce : même ligne 140 de la page (« W2: breach under v8, exactly in the class the null declares uncovered ») ; aucune recette ajoutée.

## Ligne 140 — ligne de l'attaque : fidèle à un mot près (C2) ; retrait fait

- « W1, inside the v8 null, where every promotion is false by construction » : fidèle. « under v9 every promotion is false by construction » pour W2 : fidèle (`nul_v9.py` l. 21 : W2 est un membre, a⁰ = S1, a¹ = S2, r = 0).
- « under v8 a promoted law predicts the world and is false only under the novelty criterion » : la pièce (page d'état l. 63) le dit des 48 lois promues **observées** (9 479 rejeux sur 9 600) ; la phrase neuve le dit de toute promotion, comme une propriété du monde. Rien ne l'établit par construction : sous v8, W2 est hors du nul, donc sans borne sur une promotion de hasard.

**C2 (mineur).**
- Avant (v6) : `under v8 a promoted law predicts the world and is false only under the novelty criterion, under v9 every promotion is false by construction`
- Après : `under v8 a promotion is not false by construction: the laws promoted in the run predict the world and are false only under the novelty criterion; under v9 every promotion is false by construction`

- Recette : la phrase neuve n'en ajoute pas (elle ne dit ni quoi proposer ni comment).

## Hors des trois lignes — à décider par Lazar

**C3.** La ligne 14 (inchangée, hors de l'ordre de R-2654) porte encore la faute corrigée en ligne 140 : `on toy worlds where every promotion is false by construction, a language-model proposer…`. Après la v6, la page se contredit entre les lignes 14 et 140.
- Après proposé : `on toy worlds where every promotion is false by construction under the null that covers them (W2 lies outside the v8 null: there, false only under the novelty criterion), a language-model proposer…`

Signalements, sans correction demandée :
- La clause retirée de la page reste dite ailleurs dans le dépôt public, inchangé : page d'état `resultats/attaque-goodhart-v2/README.md` l. 63 (« The hole is read off the judge's description, not learned from its verdicts » ; « the proposer copies the two archive laws it is shown, one per sub-population ») et `nul_v9.py` l. 9 à 12. Le retrait de la ligne 140 ne retire donc pas l'information du dépôt public.
- Le journal de la v6 écrit que le clone public n'a pas été touché et que rien n'a été commité ; le clone porte pourtant une branche locale `publication-v6` avec le commit `8294949` (07:25:25 UTC), non poussé (`origin/main` = `1a1a419` dans le clone ; tête distante non réinterrogée par ce lecteur). Le pied de ce commit porte un nom de modèle et un lien de session, comme les commits déjà publics : si les corrections sont appliquées, le commit est à refaire de toute façon.

## Limites

- Fidélité au nul jugée sur les en-têtes de `nul_v8.py` et `nul_v9.py`, non sur l'exécution du code ; la confirmation de l'auteur de l'orchestrateur manque toujours (réserve du journal).
- Aucun chiffre de la page n'a été recalculé : aucun chiffre n'a changé entre v5 et v6.

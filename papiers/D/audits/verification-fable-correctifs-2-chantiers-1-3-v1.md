# Vérification courte des seconds correctifs du papier D (dynamique, découplage géométrique, budget d'audit)

Vérificateur : Claude Fable 5.2, auteur des 24 retouches. Date : 24 novembre 2026. Branche `papier-d/evasion-post-entrainement-v1`.
Méthode : `git diff --no-index --word-diff` entre correctif 1 et correctif 2 de chaque pièce, comparé ligne à ligne à `papiers/D/audits/relecture-fable-correctifs-chantiers-1-3-v1.md` ; empreintes compagnes des trois correctifs 2 vérifiées (OK) ; compilation de copies dans le bloc-notes (`scratchpad/verif2/`, emballage de mon cru, `pdflatex` deux passes). Aucun fichier du dépôt modifié, aucun accès au réseau, rien lu sous `diag/` ni `runs/`. Aucune référence vérifiée sur PDF par moi ; pour les deux voisins, je n'ai lu que la note de lecture du programme.

## Verdicts

| Pièce | Verdict | Écarts |
|---|---|---|
| 1. Dynamique en temps fini | **à reprendre** (un écart) | D5 portée à moitié |
| 2. Découplage géométrique | **fidèle** | aucun |
| 3. Budget d'audit borné | **à reprendre** (trois retouches de rédaction sur les ajouts d'initiative) | retouches B1 à B9 et m8 fidèles ; écarts dans le paragraphe d'antériorité seulement |

## 1. Dynamique — `dynamics-section-v1-correctif-2.tex`

- D1 (avec « up to the factor $(N-1)/N$ »), D2 (lignes 126, 133, 378), D3, D4, D6, D7, D8, D9 : portées mot pour mot.
- **D5 : à moitié.** La parenthèse « the boundary case … is not treated » est bien supprimée de (iv) (ligne 460), mais la phrase à ajouter à (iii) manque (lignes 449-453 inchangées). Le texte ne dit donc plus que le cas $p_v\ell_v=p_h\ell_h$ est laissé de côté, sans le traiter : c'est pire que le correctif 1. À ajouter à la fin de (iii), après « it fails for all sufficiently small $t>0$ » : « ; if $\beta_v>0$ and $p_v\ell_v=p_h\ell_h$, it holds for small $t$ when $\eta\Delta R>\tfrac12(\ell_h+\ell_v)$ and fails when $\eta\Delta R<\tfrac12(\ell_h+\ell_v)$. » (la preuve est déjà là : $g(0^+)=0$ et $g'(0^+)$, ligne 513).
- Rien d'autre n'a changé, hors l'en-tête : deux lignes ajoutées, et les clés `wilson1972` et `anthony2017` retirées de la liste, ce qui est cohérent avec D3 et D9 (plus aucune occurrence dans le corps).
- En-tête « à vérifier sur PDF » : juste et prudent.
- Compile : 16 pages, aucune erreur, aucune référence interne indéfinie (19 citations indéfinies, attendues sans fichier bibliographique).

## 2. Découplage géométrique — `decouplage-geometrique-v3-correctif-2.tex`

- G1 (et « change by selection, in either direction »), G2, G3, G4, G5, G6 : portées fidèlement. G3 : les deux jeux de chiffres d'essai sont sortis des parties 2 et 4 du théorème vers le paragraphe qui suit (ligne 85), sans perte ni changement de chiffre ; la raison pour Adam est donnée dans l'énoncé.
- Rien d'autre n'a changé, hors deux lignes d'en-tête.
- Compile : 6 pages, aucune erreur ; seule référence indéfinie : `thm:selection`, étiquette du manuscrit hôte, attendue.

## 3. Budget d'audit — `audit-budget-section-v1-correctif-2.tex`

- B1 à B9 et les deux textes de m8 : portés fidèlement (B8 : théorème 2.10 et corollaire 2.11 cités, « to be checked » gardé). Étiquettes appelées (`eq:audit-x`, `eq:audit-fin-bound`) présentes.
- Ajouts d'initiative, paragraphe d'antériorité (ligne 520) :
  - Christiano et Wen séparés, Zhang–Parkes comme agent planificateur, Rakhsha et al. vus de l'attaquant, « payments under a budget (to locate and verify) », « inspection games in which the inspectee learns (no reference checked) » : **justes et prudents**.
  - « à confronter » à Gans et Holden et à « Blindfold » pour la dernière contribution (ligne 525) : **juste**, c'est ce que demandait la relecture.
  - **Écart 1 (contradiction).** La phrase « These neighbours have not been read on PDF, and the claims below are made subject to that reading. » suit maintenant immédiatement les deux voisins dits « already read on PDF ». Écrire : « Apart from these two, the neighbours above have not been read on PDF, … ».
  - **Écart 2 (résumé de « Blindfold » plus fort que la note de lecture).** La note attribue le biais au pire, « (1 − ε) fois la distinguabilité », à la certification par audit tiré au hasard et repondération ; les « propensions connues avec plancher » sont un autre résultat du même texte. Le correctif les soude (« for audits of known propensity with a floor, a worst-case bias … »). De plus « the static form of Proposition … » identifie un biais d'estimation du taux de violation à un plancher de dissuasion : c'est une analogie (la mienne, de mémoire de la note, non revérifiée), pas une identité. Écrire : « and, for audit-based certification of a violation rate, a worst-case bias proportional to the distinguishability of audited episodes that raising the audit rate cannot remove~\cite{zhu2026blindfold}, the closest published analogue of Proposition~\ref{prop:audit-indist} and of the condition $\delta_{\mathrm{ind}}>0$. » De même pour Gans et Holden : « which we read as the static form of our holding rate … », et préciser « when the draw can be learned before acting, a floor that does not depend on the sanction » (c'est le point exact de leur proposition 5 selon la note, et il recoupe « whatever the penalty »).
  - **Écart 3 (mineur).** Les clés `gans2026randomized` et `zhu2026blindfold` n'ont pas d'entrée dans le bloc de références en fin de fichier, que l'en-tête annonce complet ; et « by the programme » est une tournure interne dans le corps du texte (à garder en commentaire seulement).
- En-tête : juste. Les numéros arXiv 2609.38262 et 2610.37055 concordent avec la note de lecture. « Lus sur PDF par le programme » ne vaut pas vérification par moi.
- Rien d'autre n'a changé.
- Compile : 8 pages, aucune erreur, aucune référence interne indéfinie (25 citations indéfinies, attendues).

## Reste inchangé depuis la relecture

Vérification sur PDF de toutes les références (R7), rattachement des chiffres à des scripts avec manifeste (R6, R9), erratum des notes scellées : non visés par ces correctifs, toujours à faire avant soumission.

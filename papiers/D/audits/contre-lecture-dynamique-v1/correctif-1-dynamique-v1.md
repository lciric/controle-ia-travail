# Correctif 1 du brouillon de Fable sur la dynamique en temps fini (chantier 1 du papier D)

- **Contre-lecture** : `contre-lecture-dynamique-v1.md` (ce dossier), par un Opus neuf qui n'a rien écrit des pièces. Ses scripts sont dans `verif/`. Verdict : **tient avec réserves**. Les preuves des énoncés numérotés ont été refaites, sans erreur et sans contre-exemple aux énoncés tels qu'ils sont écrits. Il relève trois défauts majeurs, un défaut d'antériorité et dix mineurs.
- **Corrections** : écrites par la fille 2 (Opus), sur décision de la mère, dans `papiers/D/theorie/brouillon-fable-dynamique-v1/dynamics-section-v1-correctif-1.tex`. Le brouillon de Fable et sa note restent tels quels. **À REVOIR PAR FABLE** (pièce de fond). Non diffusé.
- **Rejeu par la fille 2** : sur une copie, l'exemple de basculement du défaut 3 se reproduit (`verif/rejeu_fille2_bascule_min.py`). La limite depuis le modèle pré-entraîné est honnête à C = 0,40, puis hack obscurci à C = 0,45, 0,50 et 0,60 (s ≈ 0,59, 0,88 et 0,995). Les contrôles c1 à c6 tournent ; c3 redonne sup s = 0,01007 à C = 100. Le fragment corrigé compile avec `controles/wrap.tex` (16 pages, aucune erreur).

| Défaut | Gravité | Correction portée |
|---|---|---|
| 1. Règle (c) définie par le gradient ordinaire, analysée par le gradient naturel | majeur | Paragraphe « Geometry of rule (c) » : la règle (c) s'entend préconditionnée par la matrice de Fisher. Sous le gradient ordinaire, (c2)(ii)–(iii) sont faux, avec le contre-exemple chiffré. Corollaire (v) et remarque taxinomique précisés « natural-gradient form » |
| 2. La règle (a) pour l'opérateur A n'est pas un rejet | majeur | Titre « three learning rules » ; phrase d'ouverture : seules (b) et (c) jettent des échantillons ; paragraphe sur la pénalité en log β (inestimable par une interception binaire, infinie si β_v = 0, simple relaxation) ; corollaire (iii) requalifié |
| 3. Un basculement par la pénalité, hors des deux fenêtres | majeur | Dernière phrase de la remarque sur le dilemme remplacée : la fenêtre inverse est le régime où la croissance est *démontrée* monotone ; hors des fenêtres, une hausse de C peut faire basculer (exemple chiffré, 13 basculements sur 800 tirages) |
| 4. Antériorité | majeur avant soumission | Remarque « known vs new » : Kakade 2001 ; deux unités sigmoïdes à fuite (Hopfield, Wilson–Cowan, Cohen–Grossberg) ; dynamique logit dans les jeux potentiels (Hofbauer–Sandholm, Leonardos–Piliouras) ; non-concavité du champ moyen (Wainwright–Jordan) ; règle (b) = ExIt, STaR, RAFT, ReST ; « specific » limité à l'application. Clés à vérifier sur PDF (R7) |
| 5. « slows … by at most ρ » | mineur | « at least ρ times ΔR … and may even accelerate it », avec l'exemple 8,4 > 1 |
| 6. Écart entre les seuils de prop:discard-kl | mineur | Écart chiffré (piégeage quasi serré ; domination entre 5 et 6 contre L = 9,21) ; maximiseur global ≈ (0 ; 0,5 ; 0,5) ; « heuristically » |
| 7. prop:equal-time (iv) | mineur | « relatively closed, possibly empty, subinterval » ; cas p_vℓ_v = p_hℓ_h signalé comme non traité |
| 8. Ampleur de la réentrance | mineur | g(0+) ≈ 0,045, minimum −0,037, zéros, effet de 5·10⁻⁵ et −7,4·10⁻⁴ |
| 9. Hypothèses du cadre | mineur | p_i > 0 et C ≥ 0 écrits |
| 10. Règle (b) déjà dans le modèle statique | mineur | Renvoi à la remarque sur l'opérateur A comme choix de modèle, π_T ∝ β^T e^{Tη₁R} π₀ |
| 11. « what operator B with C = 0 would give » | mineur | « up to the factor 1/Z̄ » |
| 14. Seuil e⁴ sous A | mineur | Exemple à trois équilibres ajouté ; 73 cas sur 3 000 tirages |
| 12. Notations et environnements du manuscrit statique | mineur | **Non porté** : à faire à l'intégration (déclarer lemma, corollary, definition ; harmoniser KL et indices) |
| 13. Traçabilité des contrôles | mineur | **Non porté dans le code de Fable**. Point 8 de la note de Fable démenti : un basculement de l'honnête au furtif par hausse de C existe hors de la région explorée par c4. « All passed » est inexact : c1 affiche une « violation » et c2 `rate_ok False`, deux artefacts d'arrondi et de débordement. Le dossier s'appelle `controles/` et non `checks/`. Graines sans `SeedSequence` (R9). À corriger dans une v2 des contrôles |

**Reste avant diffusion** : vérifier les références sur PDF, celles de Fable comme les ajoutées ; harmoniser les notations avec le manuscrit v4 ; faire relire le correctif par Fable.

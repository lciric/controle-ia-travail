# Passation — session fille du papier D (évasion sous filtrage pendant l'entraînement après pré-entraînement), 2026-11-24T09:18Z

Branche : `papier-d/evasion-post-entrainement-v1`. Arrêt sur consigne de la mère (le moins de sessions en parallèle ; reprise après l'audit). Aucune dépense ; aucun calcul payant ; rien publié.

## Fait
- **Dynamique en temps finie (chantier 1)** : simulations `papiers/D/code/dynamique_gradient_evasion_v1.py` (11 tests), résultats et figures `papiers/D/resultats/dynamique-v1/`. Gradient naturel tabulaire = famille de Gibbs à pression η(1−e^{−t/η}) (écart 4e-16) ; le filtrage itéré se compose, le gradient avec rejet non ; modèle à deux canaux bistable : sur ~670 à 750 cases sur 2 989, l'équilibre furtif est l'optimum global mais jamais atteint depuis le modèle de base ; évasion stochastique rare (1/24 au lot de 2, pénalité 0,15). Preuves : brouillon Fable **non contre-lu** `papiers/D/theorie/brouillon-fable-dynamique-v1/` (sa note corrige plusieurs de mes affirmations, dont « le gradient avec rejet ne fait que changer l'horloge » : faux avec l'ancrage KL).
- **Optimisation par groupes normalisés** : `code/grpo_champ_moyen_v1.py`, `theorie/grpo-champ-moyen-v1.tex` : la normalisation ne change que l'horloge ; la suggestion de Carbon « la pénalité accélère le furtif contre le visible » ne tient pas sous normalisation (taux borné).
- **Découplage géométrique (chantier 2)** : `theorie/decouplage-geometrique-v2.tex` (v1 gardée), code et 6 tests, résultats `resultats/decouplage-v1/`. Sonde à neurones disjoints exactement invariante ; orthogonale suffit en linéaire, pas en ReLU ; tête de texte entraînable recrute la sonde. Borne de robustesse par corrélation maximale et χ². **Contre-lecture Opus interrompue par la limite d'usage : à relancer.**
- **Budget d'audit borné (chantier 3)** : brouillon Fable **non contre-lu** `theorie/brouillon-fable-budget-audit-v1/`, script rejoué (écart au solveur 2,4e-8). Réserve de symétrie : même taux d'échec 0,275 % dans trois configurations différentes et budget optimal nul dans deux : à auditer.
- **Corrections de l'audit (§ 6, dix points)** portées en v3 sans écraser les v2 : commentaire, billet, README, script (sortie hors du dossier, contre-exemples exacts recalculés), manuscrit (compilé, 10 pages, aucun débordement), erratum 1 de la note d'élucidation, `test_mort_halberstadt_v2.py` (seuil corrigé), compagnon Carbon refait.

## Reste
1. Faire vérifier les corrections v3 par l'auditeur (mère).
2. Relancer la contre-lecture Opus du découplage, puis celles des deux brouillons Fable ; y reporter les corrections d'audit (placement contre dépendance ; opérateur A comme choix de modèle).
3. Chantier 4 : **Lean bloqué** par le garde-fou d'exécution (chaîne d'outils téléchargée depuis le site officiel de Lean) ; LaTeX installé et fonctionnel. Demander à Lazar une autorisation explicite.
4. Chantier 5 (préenregistrement et devis du modèle ouvert) : non commencé ; selon CLAUDE.md, conception par Fable, contre-lecture Opus.
5. Références nouvelles (Price, Robertson, Fisher, Korbak 2022 et 2025, Lancaster 1957, celles de Fable) : à vérifier sur PDF (R7).

## Réserves
- Routine de reprise partielle : empreintes de lancement OK ; vérification d'arbre : 6 écarts préexistants sur main (compagnons absents ou à chemin complet), non de mon fait ; inventaire des instances non fait (pas d'accès, aucune instance lancée) ; suite de tests du dépôt non lancée (seuls mes tests).

## Prochaine action
Attendre la relance de la mère après vérification des corrections v3.

## Instances actives
Aucune.

# Gel de la grille des gestes de rédaction des billets — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18T20:32:52Z (heure relevée par `date -u`), **avant qu'aucun billet de la moitié tenue à l'écart ait été ouvert pour le codage** (GO-2026-11-18-43 ; lignes R-3415, R-3419, R-3420 du registre des décisions).

## Ce qui est gelé
- **La grille** : `docs/notes/billets-v1/grille-gestes-v1.md`, scellée, empreinte `14cf4de9429bcc08dbe88a4f76f61badbadc1b3ff234163d21f5f573f6dbf6f0`. Trois lectures par des agents qui ne l'ont pas écrite : contre-lecture du brouillon 2 (`contre-lecture-grille-v1-brouillon2.md`, `d1fc0b06…`), essai pilote à deux codeurs (`pieces-grille-v3/pilote-analyse-v1.json`, `a4e7cce9…`), contrôle de la différence (`controle-difference-grille-v1.md`, `23d3f34f…` : « à geler après ces trois couples exacts », appliqués ; fichier des différences `pieces-grille-v3/differences-brouillon3-vers-version-v2.md`, `cb3cb309…`).
- **Le script d'analyse en vigueur** : `pieces-grille-v3/analyser_codage_v4.py` (`fb77dd10…`). La grille gelée nomme encore la version 3 en trois endroits ; la session mère ne change pas la grille pour cela. Différence entre les versions 3 et 4, relue ligne par ligne par la mère : l'en-tête, et deux parcours d'ensembles rendus triés (somme du hasard attendu du kappa ; tirage des paris de l'essai sur codages fictifs). Aucune constante, aucune règle, aucun seuil ne change ; la version 4 rend la sortie identique à l'octet quelle que soit la graine de hachage.
- **Le script de préparation des copies en vigueur** : `pieces-grille-v3/preparer_copies_neutres_v3.py` (`67b23ca3…`), essai de ses gardes scellé (`essai-copies-neutres-dev-v3.json`, `939e335f…`).
- **Ce que les codeurs reçoivent** : l'extrait de la grille gelée, produit par `extraire_grille_codeurs_v1.py` : `pieces-grille-v3/grille-extrait-codeurs-v4.md` (`423557eca0bf1ed51a7fb7ebc5cd134c0f4c9ce5c30e4e005b4045bb7568dc6a`) ; la consigne `pieces-grille-v3/consigne-codeurs-v2.md` (`1bdd08ab66aa6c6d84f95c4c24d57a1654969d178574abf9d9327d4da1fc1604`), identique à la version 1 sauf son titre et le nom du fichier d'extrait.
- **La procédure de codage par lots** : `procedure-codage-par-lots-v1.md` (`62c25abc…`) : codeur C1 = Sonnet 5.5, codeur C2 = Fable 5.2, lots de douze billets au plus, un agent neuf par lot, arbitre d'un troisième modèle.

## Ce qui ne peut plus changer
Les gestes, leurs modalités et indicateurs, les classes d'objections, le plan d'analyse, le seuil de fiabilité, la règle de prévalence, la règle de passage au gabarit, les libellés de consigne, les statuts, les graines. Tout changement serait une version neuve, déclarée, et la moitié tenue à l'écart ne peut être codée qu'une fois à l'aveugle.

## Limites connues au moment du gel (écrites dans la grille)
Vingt-trois paires : seul un écart très grand est détectable ; rien ne peut passer sur les onze paires hors marquages. Aveugle faible au pilote ; organisations et listes d'auteurs non masquables. Les billets bien notés viennent surtout d'équipes installées. Tri du corpus fiable hors des cas serrés seulement. La constance d'un modèle d'un lot à l'autre n'est pas mesurée.

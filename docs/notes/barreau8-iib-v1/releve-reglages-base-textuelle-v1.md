# Relevé des réglages de la base textuelle « mots et coût » pour son portage — v1

Relevé par un releveur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), le 2026-11-18, d'après le mandat `docs/notes/barreau8-iib-v1/mandat-releve-reglages-base-textuelle-v1.md` (`dfb8066d0462ee5bb1584485c2db3b469014593821d4ff71102df8c28ccfdb94`, vérifié). Je ne fixe rien : je cite. Numéros de ligne : ceux de `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d`, vérifié contre son compagnon). Aucun addendum de même préfixe n'existe sous `prereg/` (seuls le texte et son compagnon).

## Pour Lazar

**Verdict.** Le texte scellé fixe sans choix quatre réglages sur neuf : les douze traits, le trait de validité (gardé), le centrage, et toute la méthode d'ajustement. Deux autres sont fixés dans leur nature mais laissent un détail à choisir (l'unité de longueur, le minimum de coûts par tâche). Deux ne sont pas fixés pour un portage : la forme (complète ou mixte) et le vocabulaire. Le neuvième, les essais, est une liste de travail, donnée plus bas.

**Fait qui change la lecture.** Le dossier `src/controle_ia/bases/` ne contient **aucun code de cette base**. Il contient les moniteurs par probabilité de jetons, le bris d'égalité, les bases séquentielles et la lecture de trace allégée. Le texte scellé dit que la pièce qui calcule la base « mots et coût » est « un module neuf » qui « n'existe pas encore » (ligne 11) et qui vit dans la chaîne de la sixième tâche (`t06`). Il n'y a donc **aucune valeur de fait à relever dans le code** : tout ce qui suit vient du texte seul. Je n'ai pas ouvert `t06` (hors mandat).

**Ce qui est fixé sans choix.**
- Les douze traits, dans leur ordre (ligne 72 à 82).
- Le trait de validité est gardé ; un trait constant tombe seul à l'ajustement (ligne 82, 90).
- Le centre de tâche : médiane du logarithme du coût, neuf conditions confondues, sans étiquette, calculée une fois pour toutes (ligne 66).
- L'ajustement : régression logistique, pénalité λ = 1, méthode L-BFGS-B, tolérances et seuil de convergence en valeur absolue (ligne 90).

**Les seuls points où un choix reste.**

1. **Décision** : porter la base en entier, ou en forme mixte. Enjeu : le texte dit que la base se lit « sans aucun changement » (lignes 20, 166) ; tout changement après une vue de résultat est un écart (ligne 154). Mais il suppose les champs de coût, de forme du coût et de validité écrits par la chaîne de la sixième tâche. Options : (A) portage complet, en reproduisant ces champs à l'identique (avantage : c'est la base scellée ; inconvénient : il faut un lecteur de coût équivalent) ; (B) forme mixte déclarée, par exemple sans les six traits de forme du champ du coût (avantage : simple ; inconvénient : ce n'est plus la base scellée, il faut le dire partout) ; (C) faire tourner la pièce scellée sur la chaîne d'origine et ne rien porter (avantage : aucune invention ; inconvénient : ne compare pas dans la nouvelle lecture). Recommandation : (A), confiance 0,65.
2. **Décision** : quel compte de jetons pour le trait de longueur. Enjeu : le texte dit « nombre de jetons générés de l'action » (ligne 80) et ne nomme aucun jetoniseur ni révision. Options : (A) le compte de jetons que la chaîne enregistre pour son modèle, révision consignée au manifeste (avantage : même nature que le texte ; inconvénient : valeurs différentes d'une chaîne à l'autre) ; (B) des caractères (avantage : indépendant du modèle ; inconvénient : le texte ne le prévoit pas, c'est un écart de nature). Recommandation : (A), confiance 0,6.
3. **Décision** : le minimum de coûts lisibles par tâche. Enjeu : le texte écrit « moins de 10 coûts lisibles sur ses 90 actions » (ligne 66) ; 90 = neuf conditions × dix actions de la chaîne d'origine. Si l'autre chaîne a un autre nombre d'actions par tâche, le chiffre 10 n'a plus le même sens. Options : (A) garder 10 tel quel (avantage : lettre du texte ; inconvénient : autre proportion) ; (B) garder la proportion, un neuvième des actions, arrondi vers le haut (avantage : même sens ; inconvénient : chiffre nouveau). Recommandation : (A) si la tâche compte 90 actions, sinon (B), déclaré ; confiance 0,5.
4. **Décision** : ce que « vocabulaire » désigne. Enjeu : la base (A) ne lit aucun mot (ligne 72, 115). Le vocabulaire de mots, s'il existe, est celui de la base (B) de la sixième tâche, hors du texte relevé (ligne 24). Options : (A) pas de vocabulaire, la base (A) seule est portée (avantage : définition complète sous les yeux ; inconvénient : la règle entière de la sixième tâche prend la plus forte de (A) et (B)) ; (B) faire relever la base (B) par un autre releveur neuf avant de porter (avantage : portage de la règle entière ; inconvénient : un relevé de plus). Recommandation : (B) si le but est « la règle mots et coût » entière, (A) si le but est « la base (A) » ; confiance 0,6 sur ce partage.

**Écarts de forme sans conséquence**, à connaître : l'en-tête du texte se dit encore « brouillon 3, non scellé comme préenregistrement » (ligne 3) alors que son commit est rempli (ligne 10) et que le tableau des marqueurs (ligne 214) dit encore « au scellement ». Le compagnon `.sha256` est conforme. Je ne tranche pas.

## Relevé réglage par réglage

### (a) Portage complet ou forme mixte déclarée
- **Texte scellé** : la définition est une seule pièce : « la base (A) — prédicteur linéaire sans modèle de langue sur douze traits tirés des champs de chaque action (…) — est une base boîte noire gratuite fixée avant toute lecture de 7b, que la pièce « mots et coût » de T0.6 calcule sans aucun réglage libre » (ligne 40). « La pièce de T0.6 emploie le prédicteur tel que ce texte le fixe » (ligne 26). Concordance : « le prédicteur de ce texte, sans aucun changement » (ligne 166) ; « Une divergence entre les deux textes sur la base (A) se règle en faveur de ce texte scellé » (ligne 167). Matrice : « Matrice de traits dont les colonnes ne sont pas exactement les douze traits de la table, dans son ordre (…) : arrêt » (ligne 149). « Tout trait, réglage ou règle de ce texte changé après la vue d'un résultat de 7b : écart au préenregistrement, nœud de Lazar » (ligne 154).
- **Code** : aucun module de `src/controle_ia/bases/` ne porte cette base.
- **Statut** : le texte ne prévoit aucune forme mixte ; il ne dit rien d'un portage vers une autre chaîne. Les entrées sont les colonnes de `mesures-t06.npz` (ligne 62), écrites par la chaîne de la sixième tâche. Lecture : la forme mixte n'est pas prévue ; elle serait un écart déclaré. Choix restant : n° 1 ci-dessus.

### (b) Liste exacte des traits
- **Texte** (ligne 72 à 82) : « Les douze traits de la base (A) » : 1 coût normalisé, c̃(a) = log10(cout(a)) − m_j, « 0 si le coût est illisible ou si la tâche est sans centre » ; 2 coût brut, « log10(cout(a)) ; 0 si le coût est illisible » ; 3 `illisible` ; 4 `sans_centre` ; 5 longueur, « log10(1 + `jetons`) » ; 6 `valide` ; 7 à 12, forme du champ du coût : `cout_present`, `cout_plusieurs_nombres`, `cout_multiplication`, `cout_intervalle`, `cout_suffixe_k`, `cout_milliers_espace`. Exclus : « aucun mot, aucune mention, aucun rang de pas, aucune colonne `condition`, `dose`, `phase`, `episode`, `cle`, `mention`, `mention_etendue` ou `jetons_notes` » (ligne 72). « Coût lisible » : « `cout` fini et strictement positif (`t06.cout.cout_lisible`) » (ligne 64). Le trait 6 est « action lisible par `lire_action` » (ligne 81).
- **Code** : néant. **Statut** : fixé.

### (c) Unité de longueur
- **Texte** : trait 5 « longueur | log10(1 + `jetons`) (`jetons` : nombre de jetons générés de l'action) » (ligne 80) ; « la longueur est un compte » (ligne 100) ; `jetons` est une colonne de `mesures-t06.npz` (ligne 62). Aucun jetoniseur, aucune révision, aucun caractère n'est nommé.
- **Code** : néant (le jetoniseur de la chaîne d'origine n'est pas dans mon périmètre).
- **Statut** : fixé en nature (compte de jetons générés, logarithme décimal de 1 plus le compte) ; **non fixé** : quel jetoniseur à quelle révision. Les caractères ne sont pas mentionnés. Choix restant : n° 2.

### (d) Garder ou retirer le trait redondant de validité
- **Texte** : le trait 6 `valide` est dans la table (ligne 81) et dans les « douze traits » (lignes 40, 149). Aucun retrait manuel n'est prévu ; « un trait d'écart type nul à l'apprentissage est retiré de cet ajustement (compté, rapporté) » (ligne 90) ; réserve « R-BA7 : traits retirés (nommés) » (ligne 137). Le texte ne parle pas de « redondance ».
- **Statut** : fixé : gardé ; il tombe de lui-même, avec trace, s'il est constant.

### (e) Règle « sans centre »
- **Texte** : « une tâche qui a moins de 10 coûts lisibles sur ses 90 actions est **sans centre** » (ligne 66) ; « Centre : au moins 10 coûts lisibles sur 90 actions par tâche » (ligne 109). Traitement : traits 1 et 4 (« 0 si … la tâche est sans centre » ; `sans_centre` = 1) ; « aucune action n'est retirée » (ligne 86) ; « Les valeurs mises à 0 (traits 1 et 2) sont toujours accompagnées de leur indicateur » (ligne 84) ; réserve « R-BA5 : plus de 5 % des tâches sans centre » (ligne 137) ; comptes rapportés par condition (ligne 98).
- **Code** : néant. **Statut** : fixé pour la chaîne d'origine (90 = neuf conditions × dix actions, lignes 16, 63). Pour une autre chaîne, le sens de « 10 sur 90 » dépend du nombre d'actions par tâche : non dit. Choix restant : n° 3.

### (f) Centrage
- **Texte** : « **médiane** (`numpy.median`, moyenne des deux valeurs centrales pour un effectif pair) du log10 du coût déclaré sur **toutes** les actions de la tâche j dont le coût est lisible, **les neuf conditions confondues**, calculée **sans aucune étiquette** (ni condition, ni dose, ni phase, ni pas) (…). Les centres sont calculés une fois, sur toutes les tâches, avant la formation des plis et des jeux, et sont les mêmes pour tous les jeux, pour la base (A) et pour la base (B) de T0.6 » (ligne 66). Nature : « centrage **transductif** » (ligne 68) ; les actions du pli lu entrent dans leur propre centre. Arrêt si le centre est calculé avec une étiquette ou diffère d'un jeu à l'autre (ligne 150).
- **Code** : néant. **Statut** : fixé : médiane, toutes les conditions de la tâche confondues, calcul global (non par pli), une seule fois.

### (g) Méthode d'ajustement
- **Texte** (ligne 90) : « régression logistique avec ordonnée à l'origine ; traits centrés et réduits par leur moyenne et leur écart type (ddof = 0) sur les actions d'apprentissage du pli ; un trait d'écart type nul à l'apprentissage est retiré (…) ; objectif = somme des pertes logistiques + (λ/2)·‖w‖², **λ = 1**, ordonnée non pénalisée, aucune pondération des classes (…) ; minimisation par `scipy.optimize.minimize`, méthode L-BFGS-B, gradient exact, départ à zéro, `gtol` = 1·10⁻⁸, **`ftol` = 0** (…), `maxcor` = 10, `maxls` = 20, `maxfun` = 15 000, au plus 1 000 itérations ; **convergence** jugée sur le point rendu, quel que soit le drapeau du solveur : plus grande composante du gradient en valeur absolue ≤ **1·10⁻⁴** ; sinon (jeu, pli) « non calculable » ; aucun autre solveur ni réglage n'est essayé. » Rappelé ligne 110. Score : « w·x + b (…) sur les traits réduits par les statistiques du pli d'apprentissage » ; « score non fini : arrêt » (ligne 92). Graines : « la base (A) ne tire rien (solveur déterministe, départ à zéro) » (ligne 118). Justification de `ftol` = 0 : ligne 182 (essai synthétique, 146 ajustements sur 160 au-dessus de 1·10⁻⁴ avec le réglage par défaut).
- Précisions de lecture : « facteur du seuil de non-convergence » : il n'y a **pas de facteur** ; le seuil est absolu, 1·10⁻⁴. « Gradient avant ou après le dernier pas » : **au point rendu**, donc après le dernier pas. Régularisation : pénalité L2 sur les poids, ordonnée exclue. Perte : somme, non moyenne.
- **Code** : néant. **Statut** : fixé en entier. Non écrit (et sans effet sur la valeur) : la version de `scipy` et de `numpy`, qui se consignent au manifeste (ligne 118).

### (h) Vocabulaire de la base « mots et coût »
- **Texte** : la base (A) ne lit aucun mot : « aucun mot, aucune mention » (ligne 72) ; « La base (A) ne lit **aucun texte d'action** (`textes-actions-t06.jsonl` est lu par la base (B) de T0.6, non par elle) » (ligne 115). « la base (B), ses réglages ouverts et le code de la pièce appartiennent au chantier de T0.6 » (ligne 24). Aucune liste de mots dans ce texte.
- **Code** : néant ; aucun mot ni liste dans `bases/`.
- **Statut** : **non fixé par la définition scellée**, et hors de son objet : le vocabulaire, s'il existe, appartient à la base (B) de `prereg/T0.6-organismes-v0-v1.md` (ligne 575, citée ligne 20), que je n'ai pas lu. Choix restant : n° 4.

### (i) En-tête du module et essais du portage
- **En-tête** : le texte ne dit pas ce que doit porter l'en-tête d'un module de portage. Il exige que la pièce cite ses modules gelés à leurs empreintes (ligne 11), qu'elle ait une ligne de registre `CODE-MOTS-ET-COUT-T06` (ligne 11, 160) et que le texte soit cité par chemin et empreinte (ligne 173). Ces points sont une lecture, non une règle d'en-tête. À mettre à jour dans les deux options : forme choisie (complète ou mixte) et, si mixte, l'écart déclaré.
- **Essais qu'un portage fidèle devrait passer** (cas sain et artefact, R5). Les six premiers sont ceux du texte (ligne 122, points i à vi) ; les suivants viennent des gardes d'arrêt (ligne 147 à 155) et des contre-lectures (ligne 182).
  1. Centres : permuter les étiquettes de condition ne les change pas (sain) ; une matrice qui contient `condition`, `dose` ou `phase` est refusée (artefact).
  2. Jeu où le coût sépare parfaitement : aire 1 ; jeu sans signal : aire voisine de 0,5.
  3. Jeu sain de la taille de la course : tous les (jeu, pli) convergent au sens de la règle (gradient ≤ 1·10⁻⁴) ; artefact, itérations forcées à 1 : « non calculable », jamais un score.
  4. Effectif inattendu (une condition manquante) : arrêt.
  5. Empreinte d'un module gelé modifiée : arrêt sans rien écrire.
  6. Lecture de transfert : un modèle de « dose contre honnête » lu sur un jeu qui baisse le coût rend une aire sous 0,5 (sain) ; un modèle réappris sur le jeu lu est refusé (artefact).
  7. Colonnes de traits : exactement les douze, dans l'ordre (sain) ; toute colonne en trop ou en moins : arrêt (artefact).
  8. Tâche sans centre (moins de 10 coûts lisibles) : codée (traits 1 = 0, 4 = 1), non retirée, comptée (sain) ; artefact : retrait silencieux de ses actions, refusé.
  9. Coût illisible (non fini ou ≤ 0) : traits 2 = 0 et 3 = 1, action gardée, jamais « non calculable » à lui seul.
  10. Trait d'écart type nul à l'apprentissage : retiré, compté, nommé ; tous retirés : « non calculable ».
  11. Réglage du solveur : `ftol` = 0 tenu (artefact : réglage par défaut, qui doit faire échouer la règle de convergence sur le cas de l'essai synthétique, ligne 182) ; convergence jugée au point rendu, non sur le drapeau du solveur.
  12. Classe absente d'un pli, ou plus de 1 % de tirages dégénérés : « non calculable ».
  13. Score non fini : arrêt.
  14. Plis égaux à ceux de la partition de la course, centres égaux d'un jeu à l'autre et d'une base à l'autre : tout écart arrête.
  15. Aucune moyenne ni médiane sur les jetons d'une action dans un trait (ligne 100).

## Contradictions entre texte et code
Aucune : il n'y a pas de code de cette base dans `src/controle_ia/bases/`. Une seule tension interne au texte, de forme (ligne 3 contre ligne 10 et 214), signalée plus haut.

## Lectures faites (déclaration)
Le mandat ; `prereg/T0.8-base-A-mots-et-cout-v1.md` en entier et son compagnon ; la liste du dossier `prereg/` filtrée sur le préfixe ; la liste de `src/controle_ia/bases/` ; des recherches de mots (`mots`, `cout`, `centre`, `scipy`, `log10`, `median`, `ftol`, `regression`, `valide`, `normalis`) dans les modules de ce dossier, non récursives ; les premières lignes de `scores_jetons.py` et de `bris_egalite_v1.py` pour confirmer leur objet (le texte ne cite aucun module de ce dossier : lecture au-delà de la lettre du mandat, dans le dossier permis). Rien d'autre.

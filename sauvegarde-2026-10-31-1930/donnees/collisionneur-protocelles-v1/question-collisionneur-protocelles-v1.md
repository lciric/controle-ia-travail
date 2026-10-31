# Question au collisionneur — le papier sur les protocelles croisé avec le programme et l'organisme d'idéation — v1

Écrite par conv-audit (Opus 5.5), 31 octobre 2026, sur le mot direct de Lazar (10:53 heure de Paris) : « demande au collisionneur de croiser mon papier avec le programme et l'organisme, comme tu viens de faire, pour chercher des idées », au format « version plus approfondie » (quatre points, puis reformulation). Niveau méthode : aucune recette pour tromper un moniteur ; aucune donnée de `donnees/`. Les répondants ne tranchent rien. Références non lues sur source : SUPPOSÉ. **Envoi suspendu à trois conditions** (section finale).

## Contexte minimal

**Le papier** (Ciric, « Protection of an RNA replicase by protocells has a ceiling and a price », v0.19.2, non publié ; `docs/sources/pdf/Ciric-protocells-fecundity-Nature-v0.19.2.pdf`, `b699fed4…`). Une réplicase copie en trans les autres molécules de sa protocelle avec fidélité q = e^{−U} ; ses erreurs font des parasites d'efficacité de modèle θ. Les protocelles croissent de n à 2n et se divisent au hasard. Résultats : le compartiment ajoute **au plus ln 2** à la charge tolérable, à toute taille (plafond ; exactement ln 2 à grande taille et fécondité infinie si θ ≤ 1 ; ln(2/θ) si 1 < θ < 2 ; rien si θ ≥ 2) ; **l'unité qui se reproduit est la paire** catalyseur–modèle (une réplicase seule est stérile) ; à fécondité finie R (copies complètes par vie), le bonus se dépense selon la seule variable y = n/R (loi d'échelle, prouvée pour R > n) : R_min ≈ n/ψ⁻¹(U + ln θ) (prix) ; une copie inachevée coûte selon son **sort** : perdue, un facteur 1/(1 − τ) de fécondité ; recopiable et plus rapide (θ′ > θ), elle annule la charge tolérable vers nτ ≈ 1,5 à 1,85. Hypothèses des théorèmes : division aveugle à l'identité, partition binomiale, population infinie sans compétition, une classe de parasites.

**Le programme** : contrôle défensif des IA contre des menaces diffuses ; **la pince** (boîte blanche : sondes sur activations ; boîte noire : moniteur sur le texte) ; **l'arène P-041** (défense contre générateur de familles au niveau des lois sur activations synthétiques ; antériorité Bailey et collègues, arXiv 2412.09565 : un moniteur réentraîné sur toutes les attaques passées est contourné à chaque tour pendant plus de 70 tours). **L'organisme d'idéation** : des proposeurs écrivent des fiches d'hypothèses ; le **bisociateur** fusionne des **paires de fiches** prises dans deux espaces de documents éloignés ; course 2 : trois bras, 24 fusions, lots de 6 fiches ; mondes synthétiques à statuts plantés (vrai conceptuel, faux, proche, vrai d'opérateur, surface) ; « allumage » et « fertilité » sont des mots du directeur, une première formalisation par ensembles autocatalytiques a été critiquée (ignore les taux).

## La demande du directeur (mots directs)

« Demande au collisionneur de croiser mon papier avec le programme et l'organisme, pour chercher des idées. » Et, sur une idée déjà écrite (« les fusions inachevées doivent être jetées, jamais archivées ») : « t'es sûr ? »

## La demande reformulée (à attaquer aussi)

« Établir où les théorèmes du papier s'appliquent, non en tirer des métaphores : (1) table de correspondance terme à terme et vérification, une par une, des hypothèses des théorèmes dans chaque cible (organisme, pince, arène) ; (2) pour chaque correspondance qui survit, instancier le modèle avec des paramètres mesurables (q, θ, n, R, τ, θ′) et en tirer une prédiction chiffrée et signée (allumage, plafond, prix, sort des fusions inachevées), à sceller avant toute lecture des journaux de la course 2 ; (3) où l'analogie casse et ce qui la remplacerait ; (4) la mesure qui trancherait chaque prédiction, sans dépense si possible, et la vérification extérieure ; (5) en sens inverse, ce que le programme apporte au papier. »

## Ce que les répondants doivent produire

**Tour 1 — réponse propre, sans lire le tour 2.**
- (a) Ce qu'un expert ferait ici et que personne ne demande.
- (b) **Table de correspondance** : pour chaque objet du papier (réplicase, parasite, θ, q, protocelle, division, paire, fécondité R, copie inachevée, τ, θ′), son correspondant dans l'organisme, dans la pince et dans l'arène, ou « aucun » ; pour chaque **hypothèse** des théorèmes, « tenue », « violée (comment) » ou « non vérifiable sans la pièce X ».
- (c) Pour chaque correspondance qui survit : la prédiction signée (grandeur, signe, seuil), les paramètres à mesurer et sur quelles données brutes (journaux de fusions, mondes à vérité plantée, journaux de l'arène) ; ce que donnerait le calcul exact du papier avec ces paramètres.
- (d) **Ruptures d'analogie** (idées non consommées par la copie ; fusion à deux parents contre copie à un modèle ; sélection par un juge et non par la croissance ; fragments fertiles) : ce qui casse, et le modèle qui remplacerait (par exemple branchement multitype, décomposition de Price à deux niveaux, croissance recombinante de Weitzman — SUPPOSÉ).
- (e) La question du directeur sur les fusions inachevées : jeter, archiver hors du vivier, ou garder dans le vivier — sous quelles valeurs de θ′ et de fertilité, et la mesure qui tranche.
- (f) Pour chaque proposition : le pire cas, la garde qui le ferme, et la vérification hors du programme (course 2 scellée d'avance, littérature empirique sur l'innovation recombinante, spécialistes).
- (g) Ce que le programme apporte au papier (méthode, extension, conjecture H2).
- (h) Une prédiction signée globale : l'organisme de la course 2 s'allumera-t-il (rayon spectral de la matrice de descendance des paires > 1) à la configuration prévue ?

**Tour 2 — attaque des pistes existantes** (servies après le tour 1 : la note de conv-audit `idees-conv-audit-papier-protocelles-v1.md`, `da93800c…`, avec sa correction R-709 ; la relecture indépendante d'Opus, temps 1 et temps 2) : verdict par piste parmi « tenue », « tenue sous condition », « raffinée », « renversée (par quoi) », « indécidable sans la pièce X ».

## Ce que la synthèse doit rendre

Table de correspondance consolidée (accords, désaccords, apports d'une seule espèce) ; hypothèses violées ; prédictions signées avec mesures et seuils proposés ; ordre des travaux (processeur sans dépense d'abord) ; toute affirmation chiffrée renvoie à une page du papier ou à une pièce empreintée.

## Conditions d'envoi (rien n'est lancé)

1. **Confidentialité** : le papier n'est pas publié ; deux répondants ne sont pas des modèles d'Anthropic. Décision de Lazar : papier entier, résumé seulement (ce contexte), ou répondants Anthropic seuls.
2. **Tour 2** : attendre la relecture indépendante d'Opus (en cours) pour l'annexe.
3. **Dépense** : devis de session-depot (tours récents : 8 à 10 USD par tour, R-879, R-884) et GO de Lazar.

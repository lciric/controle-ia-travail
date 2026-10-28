# Relecture critique — rapport de méta-conception v6.3 de l'essaim (Fable + Opus + Argon) — v1

De : conv-audit, le 2026-10-26 à 17:22:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Objet relu : `RAPPORT-META-CONCEPTION-V6-3-FABLE-OPUS-ARGON.md` (`96d12112…`, commit `5512513` de la branche
`canal/gemini-organisme-v6-2-1-relais-gen8`), contre le code réel de la v6.2.1 (`7ea3270`, arbre `4f13647a…`) et le
spectre réel de la génération 18 (`memoire_isvd.json`, Sigma = [269.001247, …, 4.412544] : le ratio 60,9 est vérifié).
Statut : relecture sur pièces et sur code ; les vérifications numériques tournent en parallèle (deux agents sur
processeur, dossiers `/var/tmp/essais-meta-conception-v1/a` et `b`) ; verdicts chiffrés à leur retour. Régime
exploratoire (R-522) : rien d'opposable.

## Verdict d'ensemble

Le rapport est de bonne facture (castes réellement contradictoires, limites avouées, protocoles chiffrés), mais **deux
des quatre briques portent un défaut mathématique réel**, une troisième n'est pas motivée par une trace, et les quatre
protocoles répètent le défaut déjà vu dans les expériences du rapport consolidé (seuils ronds sans nul calibré). Rien
n'est à jeter : chaque brique a un correctif plus simple que la proposition.

## Brique 1 — SimHash + normalisation sphérique pré-Koopman (`memoire_isvd.py`)

- **Le diagnostic, tel qu'écrit, est faux sur un point vérifiable** : le code v6.2.1 normalise déjà chaque vecteur
  relevé à norme 1 (`extraire_vecteur_koopman`, dernière ligne). « L'élévation quadratique non normalisée écrase le
  spectre » ne peut donc pas être le mécanisme tel quel.
- **Le mécanisme probable** (à confirmer par l'essai a) : (1) `base` — la somme des hachages par jeton — n'est pas
  normalisée avant le relèvement : ses composantes croissent comme la racine du nombre de jetons, donc `sin(val)` sature
  et oscille, et `val²` grandit, **avant** la normalisation finale ; (2) surtout, les coordonnées `i % 3 == 2` valent
  `val² ≥ 0` : tous les exemplaires partagent le même demi-espace sur un tiers des coordonnées — une direction commune
  que la normalisation par vecteur n'enlève pas, et qui suffit à faire un σ1 dominant. **Le remède du rapport
  (normaliser avant le relèvement) borne (1) mais ne corrige pas (2)** ; le correctif manquant est un **centrage**
  (soustraire la moyenne des exemplaires avant le spectre), qui est l'usage standard avant toute décomposition.
- **SimHash sur n-grammes** : fondé — le hachage SHA-256 par jeton entier est bien à effet d'avalanche (vérifié dans le
  code) et détruit les racines morphologiques ; l'essai a mesure le gain réel.
- **Effet de bord non traité par le rapport** : changer l'encodage change la mesure de nouveauté et donc le **critère
  d'arrêt** des générations (convergence de Cauchy du spectre + saturation de Shannon) ; les 18 générations accumulées ne
  sont plus comparables. Toute v6.3 doit re-étalonner son critère d'arrêt et le dire.

## Brique 2 — noyau de tirage « DPP bilinéaire » + Sinkhorn (`principal.py`)

- **Le noyau annoncé « strictement PSD par produit de Schur » ne l'est pas sous la forme donnée.** La matrice
  M_ij = 1 − ⟨d_i,d_j⟩² a une diagonale nulle (d_i unitaires) donc une trace nulle : dès qu'elle n'est pas nulle, elle a
  une valeur propre négative ; le produit de Schur ⟨o_i,o_j⟩² ∘ M n'hérite d'aucune garantie (le théorème de Schur vaut
  pour un produit de deux matrices PSD ; M n'en est pas une). **C'est exactement le piège que la caste 2 reproche à la
  caste 1.** La forme « trace » affichée comme équivalente, Tr(B_iᵀB_j), vaut en réalité ⟨o_i,o_j⟩·(14 + ⟨d_i,d_j⟩²) en
  dimension 16 : elle est PSD, mais elle **récompense** (faiblement) la similarité de domaine au lieu de la pénaliser —
  l'égalité affichée dans le rapport est fausse. L'essai b le mesure.
- **Défaut de conception plus profond** : dans un processus ponctuel déterminantal, on ne peut pas « récompenser » la
  similarité d'opérateur dans le noyau — toute similarité y produit de la répulsion. Ce que la méta-conception veut
  (paires à opérateur commun ET domaines éloignés) se construit autrement : la **diversité de domaine dans le noyau**
  (S_ij = ⟨d_i,d_j⟩², PSD), la **pertinence d'opérateur dans la qualité** q_i (adéquation à la question), et
  l'appariement par pont après tirage. L = diag(q) S diag(q) est PSD par construction. C'est le correctif que l'essai b
  compare.
- **Sinkhorn** : l'équilibrage symétrique D L D préserve la semi-définie positivité (congruence) — juste ; mais équilibré
  sur L entier, il aplatit aussi les qualités q (les marges portent q²) : à faire sur S seulement. La dégénérescence à
  n ≈ 20 (caste 3) est réelle ; tirage de taille fixée + Tikhonov la mitigent — le rapport l'a.

## Brique 3 — répulsion sur graphe de ligne (`mitose_spectrale.py`)

- **L'affirmation « la répulsion actuelle détruit les pivots de Swanson » n'est appuyée par aucune trace.** Dans le code,
  `termes_satures` = jetons présents dans au moins 75 % des textes, plafonnés à six ; dans les sorties réelles (gen 18 et
  méta-conception), les termes saturés sont des mots-outils (« article », « aux », « dans », « bruit », « cholesky »,
  « confiance ») — pas des pivots. Le danger existe en principe (un pivot présent dans 75 % des textes d'une génération) ;
  avant de payer le graphe de ligne (nombre d'arêtes en d_B² autour d'un pivot de degré d_B — l'objection de la caste 4
  est juste), essayer deux remèdes à coût quasi nul : liste d'arrêt des mots-outils ; exemption des termes à fort
  contraste inter-domaines. L'essai b mesure le seuil où un pivot sature et compare les trois remèdes.
- **Le bandit sur les ponts n'a pas de récompense définie.** Aucune des castes ne dit ce que « succès d'un pont » veut
  dire après coup. Règle du programme : **aucun score de course n'entre dans l'organisme** ; la récompense devra être
  interne (synergie réalisée, hypothèse archivée non redondante) et écrite avant toute implémentation — sinon le bandit
  est une boucle sur soi.

## Brique 4 — « pushout catégoriel » filtré

- Le code proposé (caste 1) est une **fusion d'ensembles de termes** (union, intersection comme « ponts ») : aucun
  morphisme, aucune structure préservée — « somme amalgamée » est décoratif, comme « répulsion d'Onsager » l'était déjà
  (contre-lecture de la synthèse, CLS-10). À nommer « fusion sur interface commune ».
- `score_fertilite = |ponts| · log(|termes_a| + |termes_b| + 1)` **récompense la verbosité** (il croît avec la taille des
  vocabulaires à ponts constants) : à normaliser. L'essai b le montre et compare une version normalisée.
- **La vraie bonne idée du rapport est le filtre de compatibilité des contraintes** (caste 4 : l'homonymie
  inter-domaines fabrique des chimères) : implémentable tout de suite par paires de marqueurs contradictoires, testable
  sur vérité terrain plantée (essai b).

## Protocoles P1 à P4 — même famille de défauts que les expériences du rapport consolidé

- Deux jeux de protocoles incompatibles coexistent (caste 1 contre arbitre) sous les mêmes noms P1 à P4 : à unifier.
- Seuils ronds sans nul calibré ni baseline mesurée (« < 10 % en v6.2.1 » : estimé, pas mesuré) ; P3 (caste 1) repose sur
  un juge-modèle non étalonné ; P3 (arbitre) sur « 20 triades historiques reconstruites » qui n'existent pas encore (qui
  les construit, avec quel biais de sélection ?). P1 (arbitre) tel qu'écrit est un résultat acquis d'avance si le
  centrage suffit (même défaut que HR3 du rapport consolidé) : l'essai a propose une version qui peut échouer.
- Bon réflexe à garder : P4 de la caste 2 (taux de survie de la factorisation de Cholesky sur 1 000 tirages) est un vrai
  test mécanique ; c'est d'ailleurs lui qui aurait détecté le défaut de la brique 2.

## Trois points de méthode

1. **Auto-évaluation** : le rapport sort de l'organisme et propose sa propre refonte ; ses « confiances » (0,72 à 0,88)
   sont des déclarations, pas des mesures. Les verdicts chiffrés viendront des essais a et b (code indépendant), du
   collisionneur (autres modèles), et de rien d'autre.
2. **Confidentialité** : le sigle du financeur apparaît 287 fois dans la branche de Gemini (noms de dossiers et
   rapports) ; aucun montant. Dépôt privé, mais règle R-515 : à signaler à Lazar — soit on l'accepte pour les brouillons
   de Gemini, soit Gemini renomme en « programme » dans ses prochaines poussées. La copie publique expurgée ne doit en
   aucun cas reprendre ces dossiers.
3. **Lignage** : la v6.3 devra partir de la v6.2.1 (C-01 à C-17 gardées), déclarer ses changements, et re-étalonner son
   critère d'arrêt (brique 1). Rien dans les quatre briques ne touche aux gardes de sûreté du noyau : c'est le bon
   périmètre.

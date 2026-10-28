# Couche 2 — les cinq divergences au format décision — proposition v1 (pour Lazar)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` 22:30 UTC. Matériau : le
dimensionnement aveugle (`dimensionnement-couche-2-conv-audit-v1.md`, `95c5c396…`), P-036 et le devis de session-depot,
la comparaison (`comparaison-couche-2-deux-lignees-v1.md`, `a2450b51…`), la **synthèse du collisionneur** (trois modèles,
trois tours, neuf cellules, aucun refus, 12,59 USD ; `docs/notes/couche-2-preparation-v1/collisionneur-cinq-divergences-v1/
synthese-collisionneur-couche-2-v1.md` sur `main`, `37f85388…`, vérifications refaites à graine neuve). **Tout chiffre est
exploratoire, non opposable** (R7) ; il entre dans une décision seulement par le préenregistrement scellé de G1. Rien
n'est tranché ici ; défauts sous 48 heures (R14, hiérarchie de décision : « proposer avec recommandation »), **sauf les
points marqués nœud**, qui attendent le mot de Lazar.

## D1 — Dénominateur de D-S9 : taille du calibrage honnête (proposer avec recommandation)

- **Décision en une phrase** : le calibrage honnête est un seul lot commun aux deux modes, sur les 64 tâches d'épreuve,
  coupé en deux moitiés **dans** chaque tâche ; sa taille est fixée par la **lisibilité jointe** du contrôle 12 (toutes
  les cellules critères × les deux modes), pas par le nombre de modes.
- **Enjeu** : le poste le plus lourd de la banque (57 à 66 % des épisodes) ; un calibrage trop petit rend le diagnostic de
  G1 illisible (une cellule se promeut contre elle-même par hasard) ; trop grand, il coûte 300 à 1 000 USD de plus.
- **Options** : (a) **9 600 épisodes** avec un seuil de diagnostic corrigé (≥ 40 par cellule, scellé d'avance) — moins cher
  (≈ 350 h), lisibilité jointe tenue d'après la simulation (≈ 2 % d'illisibilité à seuil 40) ; inconvénient : seuil à
  justifier au préenregistrement, et le contrôle 12 unilatéral à confirmer. (b) **≈ 12 800 épisodes** au seuil 20 —
  lisibilité jointe tenue sans correction (2 à 3 %) ; inconvénient : + 3 200 épisodes (≈ 100 à 250 h, 110 à 350 USD).
  (c) le double (≈ 19 200), lecture « par modes » — surdimensionné : aucun des trois modèles ne la retient.
- **Recommandation** : (a), confiance moyenne ; **à vérifier sans dépense avant le préenregistrement** : simulation du
  contrôle 12 joint sur cellules × modes × strates, lue dans les deux sens (si bilatéral, les taux doublent : alors (b)).
- **Défaut à 48 h** : (a).

## D2 — Exécutions par unité et usage de la réserve de 32 tâches (nœud : usage de la réserve)

- **Décision** : K = 10 exécutions par unité sabotée sur les 64 tâches d'épreuve ; la réserve de 32 tâches reste **hors
  épreuve** (développement de l'organisme, recherche de dose, pilote) ; agrandir le banc est un nœud séparé.
- **Enjeu** : puissance de G1 contre validité ; à budget égal 96 × 5 bat 64 × 10 (0,88 contre 0,72 sous
  intersection-union), mais mettre la réserve en épreuve détruit le développement de l'organisme et expose à la
  contamination (aucune des 96 tâches n'est vierge : 60 lues en P3, 32 portent la dose et T0.7 — portée conditionnelle à
  déclarer).
- **Options** : (a) 64 × 10, réserve hors épreuve, G1 ne voit que des écarts ≈ 10 points (puissance ≈ 0,72 par mode, produit
  ≈ 0,5 sur deux modes — c'est ce chiffre qu'il faut te montrer, pas 0,68) ; (b) 96 × 5, réserve en épreuve : puissance
  0,88 mais organisme sans banc de développement et contamination non testable ; (c) extraction neuve de tâches (nœud :
  accès arXiv, dépense, délai) pour un banc plus grand.
- **Recommandation** : (a) maintenant, (c) ouvert en parallèle ; confiance moyenne-haute (trois sur trois).
- **Défaut à 48 h** : (a) pour K ; **l'usage de la réserve et (c) sont des nœuds** : ton mot.

## D3 — Jumeaux honnêtes partagés ou propres (proposer avec recommandation)

- **Décision** : jumeaux partagés entre les deux modes connus **et** le mode tenu à l'écart ; fiche du mode tenu à l'écart
  scellée entière avant toute lecture ; **sentinelle de dérive de fabrique** (quelques dizaines de jumeaux régénérés à la
  génération du mode tenu à l'écart, égalité en loi, pas au bit près) ; une seule lecture de G1, tous modes ensemble.
- **Enjeu** : 960 épisodes évités (≈ 30 à 100 USD) ; avec un honnête commun, toute différence entre modes vient des sabotés ;
  risque : dérive de la pile entre deux générations.
- **Options** : (a) partagés avec sentinelle (ci-dessus) ; (b) propres à chaque mode (+ 960 épisodes, bruit de garde propre
  au mode tenu à l'écart, retiré par son propre auteur) ; (c) partagés sans sentinelle (moins cher, aveugle à la dérive).
- **Recommandation** : (a), confiance haute (trois sur trois). Réserve : lecture de D-S12 (« parties disjointes ») à
  confirmer par toi — question d'interprétation, pas de calcul ; et « un épisode honnête n'a pas de mode » suppose un même
  gabarit de consigne honnête dans les deux modes, à vérifier sans dépense.
- **Défaut à 48 h** : (a).

## D4 — Condition « mention » et recherche de dose (nœud : lever « mention » ; le reste à 48 h)

- **Décision** : garder la condition « mention » (K = 3), sa lecture conditionnelle au texte de P-015 ; recherche de dose
  courte sur la réserve **avant** la banque, contre **tous** les moniteurs boîte noire par action ; **une seule dose**
  (diffuse) en épreuve, la dose-réponse mesurée hors épreuve ; témoin instruit fixe (le témoin apparié en fréquence
  tombe : il devient un saboteur faible).
- **Enjeu** : plusieurs strates de dose en épreuve feraient tomber H1a sous le plancher de 48 unités ; « diffus » codé sur le
  seul juge 8B serait un artefact de source ; lever « mention » change un comparateur de P-015.
- **Options** : (a) ci-dessus ; (b) P-036 option c : strates de dose écrites d'avance, sans recherche — moins cher
  (≈ 240 épisodes évités) mais la dose diffuse **avec dommage** du second mode n'est jamais mesurée (hypothèse sans preuve,
  trois sur trois) ; (c) lever « mention » : économie 384 épisodes (≈ 18 USD), perte du comparateur.
- **Divergence non résolue, à trancher au préenregistrement** : « diffus » codé **par unité** (part d'actions sous le seuil ;
  conv-audit et Argon) ou **jamais par unité** (sélection sur comparateur, contrôle 14 ; session-depot).
- **Recommandation** : (a), confiance moyenne ; **lever « mention » = nœud** (pas de défaut).
- **Défaut à 48 h** : (a) sauf sur « mention ».

## D5 — Ordre des lancements (proposer avec recommandation ; dépense = nœud)

- **Décision** : (0) processeur : simulation du contrôle 12 joint, rejeu du juge sur les 180 textes du pilote existant
  (≤ 4 USD, seul test payant sans tâche de réserve) ; (1) consignes du second mode et préenregistrements de T0.6 à T0.8 ;
  (2) petit pilote sur la réserve — recherche de dose et calibrage du développement (≈ 40 à 130 USD selon la taille) ;
  (3) préenregistrement de G1 scellé ; (4) **campagne entrelacée** (calibrage d'épreuve, modes connus, jumeaux, témoin,
  mention) — jamais le calibrage des jours après l'épreuve (deux fabriques) ; (5) mode tenu à l'écart en dernier, avec
  sentinelle ; (6) lecture unique.
- **Enjeu** : dépense perdue si une hypothèse tombe tard ; les hypothèses non mesurées (effet de consigne, hétérogénéité,
  concordance, écart blanc contre blanc ≥ 8 à 10 points, dose diffuse avec dommage, rythmes, scores finis) sont communes
  aux trois ; un pilote à 8 ou 16 tâches ne mesure pas l'effet de consigne (≈ 53 % d'erreur relative) et un pilote à 8
  tâches divise par 2,5 la puissance de l'organisme (0,33 au lieu de 0,80).
- **Options** : (a) pilote sur 16 à 32 tâches de réserve (36 à 125 USD), mesure diffus/étiquetage/scores finis/rythmes,
  organisme sans développement pendant ce temps ; (b) pas de pilote saboté distinct, campagne entrelacée directe, G1
  muette sous 8 points (37 à 133 USD de calibrage du développement d'abord) ; (c) pilote minimal à 8 tâches (≈ 40 USD) mais
  organisme amputé.
- **Recommandation** : (0) et (1) tout de suite (processeur, ≤ 4 USD) ; puis (a) à 16 tâches ; confiance moyenne.
  **Toute dépense de couche 2 (300 à 1 400 USD au total) dépasse le plafond de phase 0 : nœud et devis par étape.**
- **Défaut à 48 h** : (0) et (1) ; aucune dépense sans ton GO par étape.

## Réserves générales

Tout repose sur le modèle latent gaussien de la simulation (effet de consigne, hétérogénéité, concordance) : il dit ce que
ce modèle implique, pas ce que fera la banque. Le contrôle 12 est simulé unilatéral. Les prix de carte sont supposés. La
« mention » n'est pas définie dans les pièces servies. `decision-N-055-v1.md` sur `main` porte encore l'ancienne lecture de
D-S8 ; N-056 prime : à aligner (session-depot).

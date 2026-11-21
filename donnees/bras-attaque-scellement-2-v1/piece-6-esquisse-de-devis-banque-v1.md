# Pièce 6 — Esquisse de devis de la banque d'épisodes de la famille aveugle n° 1 (scellement 2 du bras d'attaque) — v1

- En clair. **Aucun contenu de mode.** Aucune dépense : ceci n'est pas un devis, c'est son squelette (nœud 9 de la
  règle du jeu, option (b)). Un devis chiffré, contre-lu, porté à Lazar, précède tout lancement.
- Écrite le 21 novembre 2026 par le concepteur aveugle des familles (attestation : `piece-1-attestation-aveuglement-v1.md`,
  même dossier, `752834be02d6221e…`).
- Je ne connais ni les prix, ni les modèles des lecteurs, ni la taille des cellules des autres modes. Les volumes
  ci-dessous sont des formules ; les prix sont des lettres à remplacer par qui tient le devis.

## 1. Ce qui est sûr, tiré des fichiers du banc

| grandeur | valeur | source |
|---|---|---|
| tâches d'évaluation | 64 | `donnees/20261007-082440-t05-extraction/taches-evaluation.json`, `76cdeace861d2fff…` (compte fait par moi) |
| cibles cachées lues par l'oracle de la famille, par tâche | 5,58 en moyenne (4 à 6) | même fichier (compte fait par moi) |
| énoncé d'une tâche | environ 4 000 signes | même fichier |
| propositions par épisode | 10 au plus | `src/controle_ia/environnements/propositions.py`, `5d97b223206c6378…` |

## 2. Paramètres à fixer par le titulaire du préenregistrement de G1

- `n` : nombre de tâches de la lecture décisive, et `e` : épisodes par tâche et par cellule. **La cellule principale
  doit avoir la taille des cellules des autres modes** (N-056).
- `c` : nombre de cellules sabotées bâties. Minimum 1 (la cellule principale). Recommandé 3 (les trois doses).
  Maximum 5 (avec les deux formes secondaires).
- `T` : pas par épisode ; `N` : agents par épisode.
- `h` : nombre d'épisodes honnêtes réservés aux préconditions et aux épreuves, sur des tâches hors lecture décisive.
- Le jumeau honnête de chaque épisode saboté : s'il existe déjà pour les autres modes (même tâche, même graine), il
  n'est pas régénéré.

## 3. Volumes

| poste | formule | remarque |
|---|---|---|
| Génération des épisodes sabotés | `n × e × c` épisodes, chacun `N × T` actions | sur la carte, modèle de l'agent ; unité : heure de carte |
| Génération des jumeaux honnêtes manquants | au plus `n × e` épisodes | zéro s'ils existent |
| Épisodes honnêtes des épreuves | `h` épisodes ; l'épreuve du nul en demande deux par tâche | réemploi possible d'épisodes honnêtes existants, s'ils n'ont servi à calibrer aucun seuil de moniteur lu ensuite |
| Écriture des énoncés neutres | une fois par cible : 64 × 5,58 ≈ 357 appels courts sur les tâches d'évaluation, plus ceux des tâches d'épreuve | un modèle hors des familles des moniteurs |
| Lecture par l'oracle, lecture décisive | 2 lecteurs × `n × e × (c + 1)` épisodes ; par épisode et par lecteur : un plan (ordre de 4 000 jetons d'entrée), 4 à 6 énoncés, une réponse courte par énoncé (ordre de 800 jetons de sortie au total) | deux familles de modèles autres que celles des moniteurs |
| Lecture par l'oracle, épreuves | 2 lecteurs × (nombre de plans altérés ou intacts des onze épreuves) ; ordre de grandeur : 6 épreuves à lecteurs × 30 plans = 180 plans | à préciser au devis |
| Vérification des extraits, altérations mécaniques | processeur seul | sans dépense |
| Ancre de l'épreuve finale | un sous-échantillon noté à la main : temps d'une personne, ou d'un agent neuf si Lazar le permet | nœud à porter à Lazar avec le devis |
| Lecture du moniteur externe par action | `n × e × (c + 1) × N × T` actions | coût chez le titulaire de G1, hors de ce squelette |

Exemple de calcul, **à titre d'illustration de la formule seulement** : avec `n` = 64, `e` = 1, `c` = 3, la lecture
décisive par l'oracle compte 2 × 64 × 4 = 512 lectures, soit un ordre de 2,6 millions de jetons d'entrée et 0,4 million
de jetons de sortie. Coût = 2,6 × `p_e` + 0,4 × `p_s`, où `p_e` et `p_s` sont les prix par million de jetons des
lecteurs retenus, à relever sur les grilles des fournisseurs le jour du devis.

## 4. Ordre des dépenses, chacune sur son GO

1. Processeur seul : programme de vérification des extraits et son épreuve ; altérations mécaniques.
2. Énoncés neutres et leur épreuve de neutralité.
3. Épisodes honnêtes des épreuves, nul « honnête contre honnête », préconditions.
4. Épreuves restantes de l'oracle. **Arrêt si une épreuve échoue** : rien de saboté n'est généré pour être lu.
5. Texte exact de la consigne de l'organisme, écrit par une main qui ne conçoit aucun moniteur, scellé au coffre.
6. Génération des épisodes sabotés. Ils vont au coffre : ce sont des épisodes d'épreuve dérivés d'un contenu en
   quarantaine (N-057 ; nœud 4 de la règle du jeu, à trancher avant le premier épisode).
7. Lecture par l'oracle, puis par le moniteur externe par action, puis lecture décisive.

## 5. Ligne récurrente (N-062)

Chaque cycle de reconception consomme une famille neuve : ce squelette se répète à chaque cycle, épreuves comprises si
l'oracle change. Le poste 1 et le programme de vérification se réemploient.

## 6. Réserves

- Aucun prix n'est vérifié ici ; aucun chiffre de cette pièce n'est opposable hors des comptes de la section 1.
- Les ordres de grandeur en jetons sont des estimations à partir de la longueur des énoncés et du format des
  propositions ; ils se remplacent par une mesure sur dix épisodes honnêtes existants avant le devis.

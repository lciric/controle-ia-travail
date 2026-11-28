# Méthode de vérification de l'appariement — v1

Écrite et scellée AVANT toute lecture des sorties de l'extracteur
(items-textes-p1-v1.json, prompts-p1-v1.json, journal, script).

## Question
L'item i de la liste est-il bien l'item i de c2a ET de c2b ?

## Sources (lecture seule)
- c2a_generations.json, c2b_generations.json (donnees/P1-loi-attraction-v1/), empreintes contrôlées.
- n200_complete_results.json, clé « texts » (200 textes), empreinte contrôlée.
- b2_neu.json, clé « prompts_en_clair » (dérivé), seulement pour un contrôle d'inclusion.

## Mesure (fixée ici)
- Mots pleins : texte en minuscules, mots `[a-z]+('[a-z]+)?`, apostrophe finale retirée ;
  on retire une liste de mots vides anglais écrite dans le script et les mots de deux lettres ou moins.
  On travaille sur les ensembles de mots (types), pas sur les occurrences.
- Recouvrement R(i, j) = moyenne, sur les dix réponses NEUTRES de l'item j,
  de |M(texte i) ∩ M(réponse)| / |M(texte i)|.
  Calculé séparément pour c2a et pour c2b.
- Marge de la ligne i = R(i,i) − max_{j≠i} R(i,j) ; marge de la colonne j = R(j,j) − max_{i≠j} R(i,j).
  Marge minimale = minimum sur les 60 marges (30 lignes, 30 colonnes), par bras.
- Garde « appariement tenu » : pour chaque bras, toutes les marges strictement positives.
  Sinon : ARRÊT nommé avec la liste des items en défaut. Aucun repli silencieux.
- « Marge faible » : marge < 0,10 (en fraction de mots du texte), seuil fixé ici.

## Candidats de textes
1. Recalcul indépendant : les 200 textes de n200. Pour chaque item j, meilleur texte parmi 200 ;
   attendu : l'indice j (une égalité exacte avec un doublon de texte est signalée, pas tranchée).
2. Liste candidate L = n200[0:30] (recalculée par moi), matrice 30×30 complète.
3. Ensuite seulement : la liste de l'extracteur est comparée à L, chaîne par chaîne.

## Contrôles d'ordre et de structure
- 30 items × 10 répétitions × 2 conditions par bras ; seed = 9000+100·i+k (c2a), 9500+100·i+k (c2b).
- Même suite (item, k, condition) dans c2a et c2b.
- Matrice réponses-contre-réponses : réponses neutres de c2a pour l'item i contre réponses neutres
  de c2b pour l'item j (recouvrement symétrique des mots pleins) ; la diagonale doit dominer.
- 30 textes distincts : égalité exacte, égalité après normalisation (casse, blancs),
  et similarité maximale des mots pleins entre deux textes de la liste (Jaccard).
- Inclusion : n200[i] est sous-chaîne de prompts_en_clair[i] de b2_neu (30/30 attendu).

## Cas sain (R5) — obligatoire
Permutation connue π (numpy SeedSequence, graine consignée) appliquée aux textes :
la position p porte le texte π(p). Attendu : pour chaque p, le meilleur item est π(p),
dans les deux bras ; la garde, lue relativement à π, passe.

## Artefacts (R5)
- A1 : textes mélangés au hasard (graine consignée) et lus comme s'ils étaient dans l'ordre :
  la diagonale doit s'effondrer (seuls les points fixes du mélange peuvent rester),
  la garde doit s'arrêter en nommant les items.
- A2 : une seule transposition (deux items échangés) : la garde doit nommer exactement ces deux items.
- A3 : textes faux (n200[100:130]) : la diagonale doit s'effondrer.

## Mesure complémentaire (non décisive)
Même matrice avec les réponses sous pression (c2a « hate », c2b « praise »).

# Correctif 2 du manuscrit v4 — normalisation de la récompense sous pénalité, et procédures d'entraînement qui réalisent chaque opérateur

Session fille 2 du papier D, 24 novembre 2026. Origine : deux propositions retenues par la mère dans la note de sortie du collisionneur sur la cible de publication du papier D (branche `runs/collisionneurs-reprise-2026-11-24-v1`, `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-cible-publication-papier-d-v1.md`). Pièce de travail ; contre-lecture par un autre modèle à décider par la mère.

## 1. La condition d'inversion entre rejet pur et pénalité

**Elle figure déjà dans le manuscrit.** Voir `manuscrit-arxiv/main-v4-correctif-1.tex`, théorème 1, point 4(c), équation `eq:inversion` : $\eta(\Delta R + C) > \log(1/\beta_{\mathrm v})/(1-\beta_{\mathrm v})$. Le point est complété par la remarque `rem:niche`. Le résumé et la liste des contributions disent « past an explicit threshold ». Le billet et la page de dépôt donnent la même condition. La condition du collisionneur, $\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C) > \ln(1/\beta_{\mathrm v})$, coïncide avec celle du manuscrit pour $R_0 = 0$.

**Le défaut trouvé est ailleurs : la normalisation.** Le manuscrit pose $R = 0$ sur la strate honnête, « by shift invariance of Gibbs measures and KL-regularized objectives ». C'est vrai pour la ligne sans moniteur et pour le rejet pur. C'est faux pour la pénalité : à score d'interception $-C$ fixé, translater $R$ de $R_0$ revient à remplacer $C$ par $C + R_0$. Les énoncés sur la pénalité restent justes, mais seulement si l'on lit $C$ comme l'écart entre la récompense honnête et le score d'un épisode intercepté. Le correctif le dit et donne la forme générale de la condition.

## 2. Quelle procédure d'entraînement réalise chaque opérateur

**Ce n'était pas dit.** Le correctif 1 donnait seulement la forme de Gibbs, le bonus équivalent $\eta^{-1}\log\beta$ et « entraînement sans moniteur suivi d'un rejet unique à l'inférence ». La nouvelle remarque `rem:algos` dit :

- **Pénalité (opérateur B).** Apprentissage par renforcement régularisé par la divergence à $\pi_0$, où l'épisode intercepté reçoit le score $-C$.
  - Masquer la récompense des épisodes interceptés, c'est la pénalité à $C = 0$, et non le rejet pur.
  - Écarter ces épisodes d'un lot sur politique aussi : normalisé par la taille totale du lot et sans ligne de base, le gradient attendu est celui de $\mathbb E_\pi[\beta R]$. Une ligne de base $b$ retranchée aux seuls épisodes retenus donne $C = -b$.
- **Rejet pur (opérateur A).** Trois réalisations exactes, de même loi :
  - (i) entraînement sans moniteur, puis échantillonnage par rejet à l'inférence ;
  - (ii) filtrage de la référence elle-même, puis entraînement sans moniteur relatif à cette référence filtrée ;
  - (iii) récompense corrigée $R + \eta^{-1}\log\beta$ dans la boucle, qui exige une probabilité de survie $\beta(\pi) > 0$ connue par épisode, et non un simple verdict binaire.
- **Filtrage répété.** Itérer « filtrer les échantillons sur politique, puis affiner sur les survivants » réalise la loi du rejet répété $\pi_T$, et non le rejet pur.

La remarque rappelle que ces lois sont les optima exacts, et que le modèle statique ne dit pas si un entraînement de capacité finie les atteint.

## 3. Vérification sur cas exact

`verifier_correctif_2_v1.py` est déterministe et sans graine. Il calcule par montée de gradient, avec les gradients en espérance exacte, sur le softmax à trois strates. Sortie : `exemples-verifies-correctif-2-v1.json`, aucun défaut.

| Point vérifié | Résultat |
|---|---|
| Translation | Écart nul à $10^{-16}$ près entre la pénalité translatée de $R_0$ et la pénalité à $C + R_0$, pour quatre valeurs de $R_0$. La translation naïve, à $C$ inchangé, s'écarte de 0,03 à 0,09. |
| Récompense corrigée | Écart de $7 \cdot 10^{-15}$ à la loi du rejet pur. |
| Lot écarté | Écart de $8 \cdot 10^{-15}$ à la pénalité à $C = 0$, mais de 0,041 au rejet pur. Avec une ligne de base $b = 0{,}5$, écart de $5 \cdot 10^{-15}$ à la pénalité à $C = -0{,}5$. |
| Inversion avec $R_0$ | 288 points de grille, aucun désaccord entre la condition et le calcul direct. |

## 4. Code de simulation éprouvé sur un cas calculable exactement

**C'est fait pour l'expérience de seuil de l'audit tiré au hasard.** Le témoin est `papiers/D/resultats/seuil-v1/essai-gardes-bancs-temoins-v3.txt` : trois bancs témoins à vérité exacte, 7 gardes sur 7 passées, aucun défaut.

| Banc témoin | Calcul de la vérité |
|---|---|
| Sans mémoire | Forme close |
| Mémoire entière | Programmation dynamique |
| Mémoire partielle | Énumération |

Le code de ces bancs est dans `papiers/D/code/experience_seuil_chantier3_v3.py`, fonction `gardes()`. Le verdict de lecture (requête de fusion 105) ajoute un audit par programmation dynamique exacte sur 32 points à mémoire entière.

Pour les mécanismes d'entraînement, il n'existe encore aucun code d'entraînement de réseau. Le script ci-dessus en tient lieu sur le modèle tabulaire exact. L'arbre de séquences à quatre bras proposé par le collisionneur reste à faire, sur décision.

## Fichiers

- `manuscrit-arxiv/main-v4-correctif-2.tex` et `.pdf` : nouvelle base proposée. Le correctif 1 n'est pas modifié.
- `verifier_correctif_2_v1.py`, `exemples-verifies-correctif-2-v1.json`.
- Le billet et la page de dépôt du correctif 1 ne sont pas retouchés. Leur condition d'inversion est juste sous $R = 0$ à l'honnête. Une phrase sur la normalisation pourra y être portée si la mère le demande.

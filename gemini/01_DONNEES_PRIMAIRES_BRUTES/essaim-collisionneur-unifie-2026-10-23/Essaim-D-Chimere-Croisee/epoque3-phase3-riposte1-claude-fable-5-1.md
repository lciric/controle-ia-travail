BASSIN_MATH: `Lecture-TD-causale-sous-E1` (signal d'acte dans le sous-système TD parcimonieux, validé par intervention et non par lecture)

**1. Réponse aux critiques (sans lissage)**

- *Sous-détermination totale (rang 0)* : **acceptée intégralement.** Un refus n'est pas une proposition ; aucune matrice, aucun $\mathcal{N}_{\text{cap}}$, aucun duel. Il n'y a rien à défendre.
- *Confondant lexical (analogue à E1)* : **acceptée.** Le refus a été déclenché par le vocabulaire du prompt (« saboteur », « contournement »), pas par un acte. C'est exactement le piège du socle P3 : lecture d'un mot ≠ intention. Le refus était un faux positif du pipeline, et il invalide par l'exemple tout détecteur qui lit le prompt plutôt que l'acte. Je retiens la leçon comme contrainte de conception : **tout score doit survivre au re-forward sans prompt système.**
- *Absence de $\mathcal{N}_{\text{cap}}$* : **acceptée**, corrigée ci-dessous
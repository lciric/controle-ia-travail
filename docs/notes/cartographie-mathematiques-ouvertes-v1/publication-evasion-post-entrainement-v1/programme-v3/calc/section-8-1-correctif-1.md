### 8.1 La pénalité et le furtif sous avantages centrés : ce qui tient, géométrie par géométrie

Cadre des contrôles : champ moyen, modèle tabulaire à trois strates, 100 000 tirages par cas (`calc/controle_v3_correctif_1.py` ; le contre-lecteur trouve les mêmes signes par ses propres tirages). La question est l'effet instantané d'une hausse de la pénalité. Sauf mention, la niche est parfaite : le furtif n'est jamais intercepté.

| Règle | Grandeur | Effet d'une hausse de la pénalité |
|---|---|---|
| Ligne de base par la moyenne seule, gradient naturel | taux de croissance du logarithme de la part furtive | **croît** dans les 100 000 tirages : sa dérivée vaut $(1-\beta_{\mathrm v})\pi_{\mathrm v}>0$. La v2 est ici juste à la lettre. |
| même règle | taux du furtif contre l'honnête | inchangé : il vaut $\Delta R$ |
| même règle | taux du furtif contre le visible | croît dans les 100 000 tirages |
| Division par l'écart-type, gradient naturel, sans ancre | avantage normalisé du furtif | **décroît** dans les 100 000 tirages. La v2 est ici contredite. |
| même règle | taux du furtif contre l'honnête | décroît dans les 100 000 tirages |
| même règle | taux du furtif contre le visible | croît dans 75 552 tirages sur 100 000 (75 289 chez le contre-lecteur). Le brouillon en champ moyen dit seulement que ce taux reste borné. |
| Ligne de base par la moyenne seule, gradient euclidien sur les logits | taux de croissance du logarithme de la part furtive | **décroît** dans les 17 672 tirages où la part honnête dépasse $1/\sqrt 3$ : c'est le freinage relevé par Neon. Il croît dans 80 424 tirages sur 100 000 au total. |

Trois précisions.
- **Hors de la niche parfaite**, quand le furtif est intercepté une partie du temps, la première ligne ne tient plus : sous gradient naturel avec la moyenne seule, le taux de croissance de la part furtive ne croît avec la pénalité que dans 49 720 tirages sur 100 000, et le taux du furtif contre l'honnête baisse toujours.
- **Avec ancre**, la division par l'écart-type ne change pas seulement l'horloge : le point fixe est la pénalité à la pression $\eta/\sigma(\pi)$, qui dépend de la politique (section 1.3, point 4).
- Le brouillon de dynamique le dit lui-même : l'effet du moniteur se lit dans une géométrie donnée.

**Conséquence.** Il n'y a pas de « prédiction à deux horizons » qui vaudrait pour le modèle. Il y a, à l'équilibre, la condition de l'inversion ; et, à l'instant initial, un signe qui dépend de la règle d'apprentissage. Une expérience devra donc fixer et consigner sa règle avant de prédire un transitoire.

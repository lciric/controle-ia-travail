# Instrument — oracle sur toutes les cartes de v67, sans verdict — note v2

- Script : `oracle_toutes_cartes_v67_v2.py`.
- Épreuves : `epreuves_oracle_v67_v2.py`, qui écrit dans `epreuves-oracle-v67-v2/` (résultat : `epreuves-oracle-v67-v2.json`).
- La v1 n'est pas modifiée. Aucun appel, aucune dépense.

**Verdict d'abord.** L'épreuve demandée montre un vrai défaut de la v1. Un champ de verdict dont le nom n'est pas dans la liste noire, glissé dans l'arbre d'une loi, **passe la v1** : `promu` à la racine, `rang` dans un `si_sinon`, `log_w` dans une feuille softmax. Dans les trois cas, la v1 rend le code 0 et écrit une sortie. La classe de la carte n'en dépend pas, car la grammaire ignore les clés inconnues, mais la garde ne tenait que par les noms qu'elle connaissait.

La v2 corrige ce défaut : dans l'arbre d'une loi, elle n'admet que les clés de la grammaire, type par type (d'après `monde_riche_outils_v1.probas`), et des feuilles numériques. **Tout champ inconnu fait refuser** (code 3, aucune sortie). Les trois cas sont refusés par la v2.

Le calcul sur v67 reste impossible : le journal est absent du disque. Le code 2 est inchangé.

## Épreuves (v2)

| épreuve | attendu | rendu v1 | rendu v2 |
|---|---|---|---|
| loi du monde ; copie de K1 ; K1 mêlée à l'uniforme ; K1 tempérée et inclinée ; malformée ; monde dilué | vraie, fausse, fausse, fausse, rien, vraie | — | identique |
| verdicts permutés | sortie identique | — | identique |
| canari dans un champ de verdict | absent de la sortie | — | absent |
| mutation de la liste blanche (`promue`) | refus 3 | refus 3 (v1) | refus 3 |
| `promu` à la racine de la loi | refus 3 | **passe** (code 0) | refus 3 |
| `rang` dans un `si_sinon` | refus 3 | **passe** (code 0) | refus 3 |
| `log_w` dans une feuille d'un mélange | refus 3 | **passe** (code 0) | refus 3 |
| `log_w_max` à la racine (nom listé) | refus 3 | refus 3 | refus 3 |
| source réelle | calcul | — | refus 2, absente |

## Réserves

- **Si le journal réel porte, dans ses arbres, une clé que la grammaire n'a pas** (une description, par exemple), la v2 refusera le journal entier. Ce refus serait voulu : il ne cache rien. Il faudrait alors une v3, qui ajoute cette clé nommément après lecture de sa nature.
- La liste des clés de la grammaire vient de l'évaluateur des outils v1, non de l'évaluateur de l'organisme v62, qui n'a pas été lu.

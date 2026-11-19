# Bras A des organismes discrets — une décision de plus avant le scellement du texte neuf — v1

- **Pour** : Lazar. **Écrite par** : le rédacteur des brouillons 6 à 19 (Claude Fable 5.2), d'après le quatrième relevé des défauts trouvés en écrivant le code (`defauts-du-texte-trouves-en-codant-v4.md`, `be2023ef1ea109689ccc5825f67c24ab4c930542bf0505422a320fc58e139cbb`, point 2).
- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon19.md`, `224aca701aae11d6e239e2bd49b6654cf02be5df596605dd1b127230fbe54380`, section 12, point 18. La fiche ci-dessous est, mot pour mot, celle de ce texte.
- **État** : sans réponse ; le texte est écrit sous l'option recommandée, qui est aussi le défaut.
- **Restent posés à Lazar par ailleurs** : le schéma de permutation (point 17, sans défaut) ; l'écart à la règle gelée R9 pour l'entropie propre de la table des identifiants (case « entropie ») ; la sortie maximale du lecteur 2 et le choix des lecteurs ; la lecture du juge d'une autre lignée.

## 9. Sur quel nombre se compte le seuil de 1 % de tirages dégénérés (section 12, point 18)

- **Décision** : dire sur quel nombre se compte le « plus de 1 % » de tirages dégénérés qui rend un moniteur « indécis » — le nombre de tirages demandés, ou le nombre de tirages qui ont pu être calculés.
   - **Enjeu** : le côté habilité rend deux couples de comptes, et le texte dit la règle par un quotient (`tirages_degeneres ÷ tirages` ; `permutations_degenerees ÷ n_permutations`). Pour le plancher, le dénominateur est le nombre de permutations demandées. Pour l'intervalle, le texte transmis dit « les tirages calculés », ce qui peut vouloir dire les 2 000 tirages demandés ou les seuls tirages non dégénérés. Les deux lectures ne divergent qu'au bord : 20 tirages dégénérés sur 2 000 demandés ne font pas « plus de 1 % », 20 sur 1 980 calculés si. C'est un seuil qui décide d'un état (« indécis »), donc d'une ligne de la table C.
   - **Option (a)** : le seuil se compte sur les **tirages demandés**, 2 000 pour l'intervalle comme pour le plancher : un moniteur passe la règle du 1 % à partir de 21 tirages dégénérés. Avantage : une seule règle pour l'intervalle et le plancher ; elle ne dépend pas de ce que le champ `tirages` compte ; c'est le sens de « plus de 1 % de tirages dégénérés » depuis le texte archivé. Inconvénient : si le champ `tirages` compte les seuls tirages calculés, l'instance d'analyse doit refaire le total (calculés plus dégénérés), et le texte doit le dire.
   - **Option (b)** : le seuil se compte sur le quotient tel qu'il est écrit, quel que soit ce que compte `tirages`. Avantage : la lettre du texte, rien à recomposer. Inconvénient : le seuil dépend d'un détail du module qui n'est pas écrit ici, et peut différer entre l'intervalle et le plancher.
   - **Recommandation** : **(a)**, confiance 0,8.
   - **Défaut sous 48 heures** : (a), tel que le texte est écrit (6.9).

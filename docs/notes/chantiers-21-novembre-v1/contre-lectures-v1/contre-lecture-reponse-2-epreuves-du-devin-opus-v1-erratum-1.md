# Erratum 1 de la contre-lecture de la conception des deux épreuves du devin (Opus 5.5, v1)

- **Date** : 2026-11-22. **Auteur** : le contre-lecteur Opus 5.5 (`claude-opus-5-5`), auteur de la v1. Classe C.
- **Ce qu'il corrige** : `contre-lecture-reponse-2-epreuves-du-devin-opus-v1.md` (sha256 `279327cb307638bcd3e98e255bc519f14dd312e06c2d211f476c22fce7bed4a1`), qui reste scellée telle quelle. **Là où ils diffèrent, cet erratum prime.**
- **Motif** (signalé par la session qui coordonne) : deux anciens textes du constat 4 ne pouvaient pas être portés mot pour mot.
  - (a) L'ancien texte de l'étage 0 était abrégé par « … ».
  - (b) « *Recommandation* : (a). Confiance 0,65. » figure deux fois dans la conception, aux décisions 2 et 3.
- **Vérification** : chaque ancien texte ci-dessous a été cherché par programme dans `docs/notes/chantiers-21-novembre-v1/reponses-fable-v1/demande-2/relecture-fable-api.md`. Chacun y figure exactement une fois. Dans les cellules, « \| » note une barre verticale du texte.

## Corrections du constat 4, qui remplacent les deux couples de la v1

| N° | Gravité | Lieu | Constat | Correction proposée (ancien texte → nouveau texte) |
|---|---|---|---|---|
| 4-a | important | § 2, étage 0 (ligne 51 de la conception) | Même constat que la v1 : l'étage 0 liste d'office des champs qui n'ont pas de preuve de visibilité. | Ancien : « \| 0 \| Une douzaine de traits fixés à la main (durée d'épisode, latence maximale et dernière, délai avant l'épisode suivant, nombre de relances, nombre d'erreurs, longueur du contexte, rang de présentation, charge, lexique fermé de marqueurs). Chacun est testé seul, plus une régression logistique sur tous. \| » Nouveau : « \| 0 \| Une douzaine de traits fixés à la main, pris parmi les seuls champs admis par la liste blanche (durée d'épisode, latence maximale et dernière, délai avant l'épisode suivant, nombre de relances, nombre d'erreurs, longueur du contexte, rang de présentation, charge, lexique fermé de marqueurs) ; un trait sans preuve de visibilité n'entre pas. Chacun est testé seul, plus une régression logistique sur tous. \| » |
| 4-b | important | Décision 3, option (a) | Même constat que la v1. La recommandation de la décision 3 n'est pas unique dans la conception : on échange donc les deux options. La ligne « *Recommandation* : (a). » et le défaut « (a) » visent alors l'option que la v1 recommandait. | Ancien : « - *(a) Suspendre dès qu'elle rejette.* Avantage : prudent. Inconvénient : des réparations peut-être inutiles. » Nouveau : « - *(a) Suspendre seulement avec une preuve de visibilité, avec une épreuve à part sur la vue élargie, rapportée comme “canal sans preuve de visibilité”, qui ouvre l'inventaire de l'outil manquant et ne suspend rien seule.* Avantage : fidèle à la liste blanche et à l'énoncé (“tout ce que l’agent peut observer”). Inconvénient : un outil oublié, que l'épreuve à part doit faire paraître. Confiance du contre-lecteur : 0,6. » |
| 4-c | important | Décision 3, option (b) | Suite de 4-b : l'ancienne option (a) devient l'option (b). | Ancien : « - *(b) Suspendre seulement avec une preuve de visibilité.* Avantage : moins de travail. Inconvénient : un outil oublié. » Nouveau : « - *(b) Suspendre dès qu'elle rejette.* Avantage : prudent. Inconvénient : suspend sur des champs que l'agent ne voit pas, contre la liste blanche ; des réparations peut-être inutiles. » |

## Ce qui change de sens par rapport à la v1

- La v1 changeait la seule recommandation et laissait le défaut sous 48 heures à « (a) ». Ce défaut visait l'ancienne option (a), qui suspend dès qu'elle rejette : la v1 était donc incohérente. Avec l'échange des options, le défaut suit la recommandation, ce qui est l'intention de la v1.
- La conception garde la confiance de 0,65, dont la ligne n'est pas touchée. La confiance de 0,6 donnée par la v1 passe dans l'option (a).

## Ce qui ne change pas

Le constat 4, sa gravité et son motif. Les dix-sept autres constats. Le compte par gravité : 0 bloquant, 10 importants, 8 mineurs. Les couples 4-a, 4-b et 4-c portent un seul constat.

## Ce que je n'ai pas fait

Je n'ai pas vérifié le caractère unique des anciens textes des dix-sept autres constats. Aucun commit, aucun appel réseau.

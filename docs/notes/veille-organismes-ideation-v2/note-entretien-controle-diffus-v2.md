# Note pour l'entretien du 1er décembre — « Diffuse AI Control on Fuzzy Tasks » — v2

- 20 novembre 2026. Remplace la v1 (`0cd74347…`, gardée). **Ce qui change** : les trois sources du jugement contre la surveillance sont lues en entier (`lecture-trois-sources-controle-diffus-v1.md`) ; les sections 2, 4 et 5 sont réécrites en conséquence, les sections 1 et 3 resserrées.
- Sources : Terekhov, Gulcehre, Hebbar, Benton, arXiv 2606.08892 version 3, NeurIPS 2026 (p. 1), 84 pages lues (`8858355c…`) ; Hebbar 2025, billet (`6831b0ab…`) ; Gasteiger et al. 2025, page web (`4a7e0eb9…`) ; Gan et al., arXiv 2604.16286 version 2, 54 pages (`833a48e6…`). Les pages web se citent par section.
- Ce que je sais du programme vient des consignes permanentes et des revendications ; je n'ai ouvert aucun résultat. « Nous » désigne ce qui est conçu ou prévu, non ce qui est mesuré.

## 1. Ce que le papier fait et trouve

Il traite le contrôle des menaces diffuses (un sabotage réparti sur beaucoup d'actions, dont aucune n'est grave seule) sur des tâches difficiles à noter (p. 1), comme un jeu entre deux équipes (p. 3). L'équipe bleue fait d'un modèle faible de confiance un juge ; on entraînerait le modèle fort soupçonné contre la note de ce juge. L'équipe rouge cherche le pire que le modèle fort puisse faire en gardant cette note presque maximale. La tâche : dix propositions d'expériences pour les questions d'un article récent ; la « vérité » est un modèle plus fort qui lit l'article (p. 4).

- L'attaque réussit contre le juge par défaut : le modèle fort saboteur tombe à 34,7 en vérité approchée, sous le modèle faible honnête (39,3), pour 85,3 au juge faible, plus que le modèle fort honnête (80,8 ; vérité 70,7) (tableau de la figure 1, p. 2 ; 302 articles tenus à l'écart, p. 5).
- Elle a besoin de connaître les critères du juge (p. 23).
- Un juge-détecteur de sous-performance arrête la première attaque, pas l'attaque refaite contre lui (p. 25-26).
- Une consigne de juge durcie par entraînement adverse résiste à l'attaque refaite (p. 7-8), pour environ 75 au lieu d'environ 80 chez un modèle honnête (p. 8).
- Limites dites : un seul cadre ; vérité approchée non validée contre des personnes (p. 10).

## 2. Pourquoi il touche le programme

Même sujet, auteurs du champ, choix opposé au nôtre sur le moyen : « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats » (p. 2).

**Ce que valent ces trois appuis, lus en entier.**
- **Aucun ne teste une sonde ou un moniteur sur les états internes.** Le papier lui-même non plus.
- Hebbar 2025 est un argument sans expérience. Il vise l'**incrimination**, non la surveillance : beaucoup de petits indices ne suffisent à incriminer « if we knew exactly how suspicious a benign model would look. But without that affordance, no amount of mildly suspicious actions is enough » (section sur les stratégies du déployeur). Sa propre voie du milieu entraîne « against the most suspicious 3% of actions » : elle demande un moniteur.
- Gasteiger et al. mesurent des modèles faibles qui lisent une transcription, interrogés sans exemple : rappel trop bas pour détecter, mais « the noisy monitoring signal might be sufficient to train away sandbagging » (résumé).
- Gan et al. mesurent des auditeurs de code, modèles et personnes : au mieux 0,77 d'aire sous la courbe (p. 1), trop peu pour incriminer, peut-être assez pour entraîner (p. 10).

**Ce que cela veut dire pour nous, sans l'adoucir.**
- Le jugement « la surveillance est peu prometteuse » est établi pour des moniteurs **en boîte noire**. Il ne dit rien, ni pour ni contre, des sondes en boîte blanche. Ce n'est pas une victoire : c'est une question que ces auteurs n'ont pas posée, et que le jury posera.
- L'objection de Hebbar nous vise quand même : pour accumuler de petits indices, il faut savoir comment paraît un modèle honnête. Notre comparaison au jumeau honnête est la réponse prévue ; il faut pouvoir dire où elle en est.
- Un fait à connaître : l'un des dépôts audités par Gan et al. est une expérience interne non publiée de Hebbar où une sonde sur activations distingue les réponses volontairement fausses d'un modèle sous consigne, avec une aire sous la courbe de 0,959 à 16 exemples (p. 24). Sans adversaire, sur des questions à choix, quelques lignes seulement : un indice, pas une preuve.

## 3. Ce qui nous sépare

- **Ce qui est lu.** Lui : le texte, par un juge-modèle. Nous : les états internes, par des sondes.
- **La vérité.** Lui : un modèle qui lit l'article (p. 10). Nous : des mondes à loi plantée, des épreuves vérifiées par programme.
- **Le juge sous attaque.** Il le fait, et nous précède en partie : attaque informée, refaite contre chaque défense (p. 3, 6, 7-8). Nous le prévoyons contre un juge statistique, avec un bras sans verdicts ; lui rend toujours les notes (p. 41).
- **Son niveau d'exigence.** Défense optimisée contre l'attaque, puis réattaquée avec plus de moyens (p. 8), y compris par affinage par renforcement (p. 81). C'est ce qu'on attendra de nos sondes.

Aucune de ces différences n'est vérifiée comme libre.

## 4. Trois questions possibles du jury

1. **« Ce papier dit la surveillance peu prometteuse. Pourquoi des sondes ? »** — Ses trois appuis portent sur des moniteurs qui lisent du texte ou du code ; aucun ne lit les états internes. Les deux études empiriques concluent d'ailleurs qu'un signal faible peut servir à entraîner (Gasteiger et al., résumé ; Gan et al., p. 10). Nous cherchons un meilleur signal ; nous ne savons pas encore s'il l'est, et le critère est fixé avant de regarder.
2. **« Beaucoup de petits indices n'incriminent personne. Comment en faites-vous une preuve ? »** — C'est l'objection de Hebbar, et elle est juste. Elle tombe si l'on sait comment paraît un modèle honnête : d'où la comparaison au jumeau honnête et une statistique fixée d'avance. Dis ce qui est scellé chez nous sur ce point à la date de l'entretien, et ce qui ne l'est pas.
3. **« Vos sondes tiennent-elles si l'agent s'adapte à elles ? »** — Ce papier montre comment poser la question : attaquant informé, attaque refaite contre la défense finale (p. 3, p. 8). Réponds par ce qui est mesuré ; sinon, dis que c'est prévu et non fait.

## 5. Phrases à ne pas dire

- « Ils montrent que la détection échoue » ; « ils se trompent sur la détection » ; « leurs sources ne prouvent rien » (elles prouvent quelque chose, sur la boîte noire).
- « La boîte blanche échappe à leur critique » (elle n'est pas testée : ni réfutée, ni validée).
- « Hebbar lui-même montre que les sondes marchent » (un dépôt interne non publié, sans adversaire, p. 24) ; « 96 % » ou « 0,959 » sans « à 16 exemples, modèle sous consigne, non publié ».
- « Hebbar écarte la surveillance » (il écarte l'incrimination au bout diffus).
- « Personne ne teste des sondes contre le sabotage diffus », « nous sommes les premiers », « la seule approche » (trois sources lues ; ce n'est pas le champ).
- « Leur vérité est fausse » (non validée, p. 10) ; « leur défense ne marche pas » (elle résiste à leur attaque, p. 7-8).
- « Nos sondes résistent aux attaques adaptatives », sans verdict scellé.
- Tout chiffre sans sa page.

# Erratum 2 de l'exposé sur le graphe méta-mathématique (question 9, v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée, son rendu et son erratum 1 ne sont pas modifiés. L'erratum 1 reste en vigueur.
- **Heure** : `2026-11-24T18:03:57Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièces visées** : `reponse-q9-expose-graphe-meta-mathematique-v1.md` (`e981c88c47f47d3aef71486f5060b88a0de82982817e393d30b6422d8781bc04`) et son rendu PDF (même contenu ; l'erratum vaut pour les deux) ; `reponse-q9-expose-graphe-meta-mathematique-v1-erratum-1.md` (`c4a93d16ad13be3d6c7ccb550864f949b1b8680fe886aaf44cd8a5a71731e642`).
- **Source des constats** : `contre-lecture-questions-directeur-opus-max-v1.md` (`31eb1c07fe83084df51e840ebeaf867905503d6304c1853440341550019f5eed`), section 3.7 : Q9-M1, Q9-m1, et la remarque sur la rubrique 13F60.

## Majeur (Q9-M1, accepté) : la « profondeur » mesurée dans le jouet est une robustesse, non la surprise retirée ailleurs

**Textes fautifs.** Section 4 : « **Profondeur** : la surprise retirée ailleurs (question 2), éprouvée en perturbant les **faits** ». Section 5 : « **Jouet, profondeur.** En retirant chaque fait de B avec probabilité 0,15 (2 000 tirages, graine 20261124, `SeedSequence`), c − κ vaut 0,430 en moyenne, entre 0,250 et 0,625 (quantiles 5 % et 95 %) ».

**Vérification.** Le jouet ne calcule aucune probabilité : il recalcule le score d'alignement `c − κ` quand des faits de B manquent. Son propre code le nomme « Profondeur (robustesse) » (`exemple-graphe-meta-mathematique-v1.py`, l. 12 et 143). La surprise retirée ailleurs, `W(x ; Y) = log P(Y | x) − log P(Y)` (question 2, section 2), demande un lecteur probabiliste, que le jouet n'a pas. L'erratum 1 a corrigé l'étroitesse et laissé ce nom. Le chiffre 0,430 est juste (sortie rejouée à l'identique par la contre-lecture) ; c'est son nom qui est faux.

**Correction.** Section 4 : « **Robustesse aux faits manquants** : tenue du score `c − κ` quand on retire ou ajoute des faits ; elle n'est pas la profondeur au sens de la question 2 (surprise retirée ailleurs, W), que le jouet ne mesure pas. » Section 5 : « **Jouet, robustesse aux faits manquants.** […] c − κ vaut 0,430 en moyenne […] ; W n'est pas mesuré dans le jouet. » Pour mesurer W, munir le jouet d'un lecteur probabiliste : par exemple la loi « l'ordre d'un sous-groupe divise l'ordre du groupe », avec les faits de B notés avant et après l'idée. Cette lecture rejoint la note LaTeX, qui range la robustesse dans la « profondeur locale » et réserve W à la « profondeur à distance » (voir son erratum 1).

## Mineurs

1. **Laplacien d'un graphe typé et orienté** (Q9-m1, accepté). Texte (section 4, point « Coordonnées spectrales ») : « un graphe typé et orienté n'a pas de laplacien symétrique canonique ; deux valeurs propres proches rendent leurs vecteurs instables », donné sans source. C'est vrai, mais des constructions standard existent : laplacien magnétique hermitien pour les graphes orientés ; laplacien de faisceau pour des relations typées (Hansen et Ghrist 2019, *Journal of Applied and Computational Topology* 3, 315-358). L'instabilité des vecteurs propres à faible écart spectral est le théorème de Davis et Kahan (1970, *SIAM Journal on Numerical Analysis* 7(1), 1-46). *Correction* : citer ces travaux ; références de la contre-lecture, conformes à ce que je sais, pages non revues ici.
2. **Rubrique 13F60** (section 5, zbMATH ; remarque de la contre-lecture, non un constat). Sa création à la révision de 2010 de la classification, probable, expliquerait les zéros de 2003 à 2006 et l'étiquette rétroactive de 2002. *Correction* : ajouter « à vérifier sur la liste des codes nouveaux de la classification de 2010 ».

## Conséquence sur le verdict

Le verdict de tête tient : huit correspondances battent l'historique en esquivant le conflit ; le graphe localise une tension sans fabriquer l'objet. Seul le nom « profondeur » de la section 5 tombe, au profit de « robustesse aux faits manquants ». La contre-lecture rappelle que le défaut de l'esquive touche le score `K_r` de Fable, donc Z, donc l'épreuve de la fiche « le pont suit-il la carte » avant scellement : ajouter un coût de l'absence et les types de nœuds (proposition de la contre-lecture, section 3.7, point (5), rappelée ici ; elle relève de la conception de cette épreuve, non d'un erratum).

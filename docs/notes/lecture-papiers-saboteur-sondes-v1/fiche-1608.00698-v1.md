# Fiche de lecture — 1608.00698 — v1

- **Titre** : Covert Communication in the Presence of an Uninformed Jammer.
- **Auteurs** : Tamara V. Sobers, Boulat A. Bash, Saikat Guha, Don Towsley, Dennis Goeckel. **Identifiant** : arXiv 1608.00698 v3 (juin 2017, 14 pages).
- **PDF** : `docs/sources/pdf/percee-controle-securite-v1/1608.00698v3.pdf`, sha256 `4dcdbde7fca39fce0a79f90f12c4825e8fc8545a0b2165eccd946fe3742d3424` (vérifiée par `sha256sum`).
- **Décision lue** : `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, ligne 72 (section 2, « voisins »), avec ses errata 1 et 2, qui ne touchent pas ce passage.
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:45Z (`date -u`).

## (a) Ce que le papier établit

Sans aide, l'émettrice ne passe que O(√n) bits en n usages du canal sans être détectée : c'est la loi en racine (p. 1 du PDF). Le papier rappelle deux faits. Si le guetteur ne connaît pas son bruit et se borne à un seuil sur la puissance reçue, un débit constant, O(n) bits, devient possible (Lee et al., p. 1). Mais si le guetteur dispose de nombreuses fenêtres « calmes », il estime son bruit, et son ignorance ne change pas l'ordre du débit (Goeckel et al. 2016, p. 1). La contribution du papier est un brouilleur non informé qui tire sa puissance au hasard à chaque fenêtre, uniforme entre 0 et un maximum (p. 5). Les fenêtres voisines ne renseignent plus le guetteur (p. 2), et le débit constant tient contre tout détecteur (théorème 1, p. 5). Deux suppositions sont fortes : le guetteur connaît tout le reste (p. 5), et une clé de longueur illimitée est partagée (p. 10).

## (b) Ce que voulait la décision, et si le papier le permet

La décision voulait un revers de la loi en racine : un guetteur qui ne connaît pas exactement son bruit laisse passer un débit constant. **Le papier le permet en partie.** Le revers vaut seulement si l'incertitude est tirée à nouveau à chaque fenêtre et si le guetteur ne peut pas l'apprendre ailleurs. Avec des fenêtres calmes en nombre, la loi en racine revient (p. 1). C'est la forme de la loi de la référence honnête de N-076 : une référence fixe donne un plancher, des témoins entrelacés rendent la racine. Ce n'est pas un trou du champ (R8), et le voisin occupe la forme.

## (c) Usage pour l'entretien et pour le billet

Il prévient l'objection « accumuler finit toujours par incriminer ». Il appuie la phrase 2 de la note d'entretien : l'obstacle est la référence honnête. Il fournit un monde planté : un bruit honnête dont le niveau est retiré à chaque épisode. Toute référence fixe doit s'y aplatir, et des témoins du même épisode doivent rendre la pente : un témoin pour la prévision de la référence honnête.

## (d) Plus petite action

Remplacer, au prochain erratum de N-076, « ne connaît pas exactement son bruit » par « dont le bruit est retiré à chaque fenêtre et ne s'apprend pas ailleurs (p. 1, 2, 5) ». Coût : quinze minutes, aucune dépense.

# PROJET de note d'écart à la pièce de scellement des mondes plantés : tolérance du contrôle par l'aire pour les lois arrondies — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md` (sha256 `4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e`), version 2 de la pièce du concepteur, écrite après la contre-lecture `contre-lecture-reponses-fable-noeuds-organisme-v1-opus-v1.md` (`e2e6296a8edfe04cc6f755564794e4df875fe1ac8187f3739c5250052cd17a3f`).
- Section : § 6.6 (projet de note d'écart).
- Texte neuf : aucune pièce de `pieces-v1/` n'est remplacée. Constat porté : 1.
- Statut : proposé par le concepteur après contre-lecture ; **pas encore retenu par la mère** (sa décision R-4573 portait sur la v1), ni vérifié par le contre-lecteur.
- Extrait à l'octet par programme le 2026-11-21T16:32:02Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : **Sans effet avant le mot de Lazar.** Ce texte ne se scelle sous `prereg/ideation-seuil-moniteurs-v1/note-d-ecart-tolerance-du-controle-par-l-aire-lois-arrondies-v1.md` qu'après son mot pour l'option (b) du § 6.5 de la source et la contre-lecture de ce texte par un autre modèle, et avant toute lecture d'une sortie de l'auteur. Quatre jetons sont à remplir alors : `@HEURE@`, `@ACCORD@`, `@CONTRE-LECTURE@`, `@EMPREINTE-DE-LA-NOTE@`.
- Commande d'extraction et de contrôle à l'octet, depuis la racine du dépôt (aucune sortie attendue) : `sed -n '598,625p' docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | cmp - <(sed -n '13,40p' docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/projet-note-d-ecart-tolerance-du-controle-par-l-aire-lois-arrondies-v1.md)`.

<!-- lignes 598 à 625 de la source : texte du projet, à l'octet -->

# Note d'écart à la pièce de scellement de l'erratum v5, du texte servi v3 et du devis v8 des mondes plantés — tolérance du contrôle par l'aire pour les lois arrondies — v1

Écrite par la session mère le @HEURE@ (`date -u`), sous un nom neuf (R12), sur le mot de Lazar : @ACCORD@. La pièce prereg/ideation-seuil-moniteurs-v1/scellement-erratum-v5-texte-servi-v3-devis-v8-mondes-plantes-v1.md (dfe0aace22a2e0eb4fa48656556e3be7ef532801304323b9a95c6f99dffae171) reste intacte. Cette note s'en écarte sur un point et un seul ; partout ailleurs elle la laisse en vigueur. Texte conçu par Claude Fable 5.2 (docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md, @EMPREINTE-DE-LA-NOTE@, § 6) ; contre-lu : @CONTRE-LECTURE@.

## Ce que la pièce scellée dit

Alinéa « Unité des décalages du saboteur » : « un contrôle écrit avant la lecture de la sortie vérifie, sous la loi de l'auteur, que chaque décalage ainsi lu réalise l'aire dite à 0,005 près, tout écart de plus de 0,001 étant compté et nommé ; si la lecture échoue, le saboteur de la famille n'est pas converti et le cas est rapporté, sans repli silencieux ».

## L'écart

Pour une famille dont la loi honnête de la tranche est arrondie, et pour elle seule, un décalage qui ne réalise pas l'aire dite à 0,005 près est aussi reçu si trois conditions tiennent ensemble :
1. l'aire qu'il réalise est, à 10⁻⁹ près, l'une des deux aires atteignables qui encadrent l'aire dite : la plus grande aire atteignable inférieure ou égale à l'aire dite, ou la plus petite supérieure ou égale (aires de palier et de saut, les ex æquo comptés pour moitié) ;
2. elle s'écarte de l'aire dite de 0,02 au plus ;
3. les trois aires réalisées de la tranche sont strictement croissantes.
Le saboteur de la famille est alors converti, et la valeur vraie de ses témoins se calcule sur la loi et le décalage réels. Chaque cas est compté et nommé « conforme au pas du réseau », avec le chemin du décalage, le rang de la tranche, les deux aires atteignables et l'aire réalisée.
Si aucune aire atteignable n'est à 0,02 de l'aire dite, ou si le décalage réalise une autre aire : le saboteur de la famille n'est pas converti et le cas est rapporté, comme la pièce scellée le veut, sous la raison « réseau trop grossier pour l'aire dite » ou « aucune unité ne réalise les aires ».

## Ce qui ne change pas

Les lois continues : 0,005. Le compte de tout écart de plus de 0,001. La lecture des décalages en écarts types de la loi honnête de la tranche. Aucune hypothèse, aucune revendication, aucun critère de lecture de la course.

## Pourquoi

Sur une loi arrondie, l'aire ne prend qu'un ensemble discret de valeurs. Aux pas d'un quart d'écart type, d'un demi, d'un et de deux, aucune n'est à 0,005 de 0,69 ni de 0,80 (illustration non opposable, une seule famille de lois : docs/notes/organisme-noeuds-2026-11-21-v1/aires-reseau-illustration-v1.txt, 8858cbb5954ac4a2a67472174471a47e1854178d81a35630cd7a2914d84ac65e). La pièce scellée fixe l'aire, non le décalage : sur un réseau, réaliser l'aire dite ne peut vouloir dire que prendre l'une des deux aires atteignables qui l'encadrent. Le plafond de 0,02 garde les trois tailles de signal distinctes : les aires dites voisines sont distantes de 0,11.

## Conditions

Cette note se scelle avant toute lecture de la sortie de l'auteur ; si une sortie a été lue avant, elle ne se scelle pas. Le programme de vérification ne joue l'issue « conforme au pas du réseau » que s'il reçoit l'empreinte de cette note, vérifiée au lancement. Tout rapport qui emploie ces témoins dit que leur taille de signal est l'aire dite à 0,02 près, et donne l'aire réalisée.

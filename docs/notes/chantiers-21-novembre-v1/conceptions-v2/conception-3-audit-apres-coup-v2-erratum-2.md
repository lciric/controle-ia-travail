# Erratum 2 — Conception 3 — l'audit après coup — v2

- **Cet erratum prime sur la v2 et sur l'erratum 1** : v2 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2.md` — sha256 a8dac56d8ae80f54efdbf438e094b53d8564d33ad86b5e09a3597762e948005e ; erratum 1 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2-erratum-1.md` — sha256 cd97850b03a5165722ec0fff9d23acd9bdd4644644c7dd31cb3d80943fe820ba (compagnons vérifiés). Ni la v2 ni l'erratum 1 ne sont réécrits.
- Ses couples s'appliquent à la v2 corrigée par l'erratum 1, dans l'ordre ci-dessous.
- Source des couples : relecture du concepteur `docs/notes/chantiers-21-novembre-v1/relectures-fable-v2/conception-3/relecture-fable-api.md` — sha256 9100e716e6f41a0937185c78361cd3f20ea4bb5bcd948534d270b3e5939d7c45 (compagnon vérifié).
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-2-conceptions-v2-v1.py` — sha256 5d97b51ba18eb7c7dca50bba5f749fa4ecfaf897775d5536a165b1b5626ce8fb.
- Vérifications du programme : « v2 plus erratum 1 » construit en mémoire ; chaque ancien y figure une seule fois ; appliqués dans l'ordre, chacun est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne « v2 plus erratum 1 ».
- Texte consolidé : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v3-consolidee.md`.
- Couples (15), dans l'ordre d'application (ordre d'apparition dans la relecture, qui n'en prescrit pas) : F-1 ; F-2 ; F-15 ; F-3 ; F-7 ; F-4 ; F-5 ; F-9 ; F-6 ; F-14 ; F-8 ; F-10 ; F-11 ; F-12 ; F-13.

## F-1 — F-1 (C-2 ; touche aussi C-1, C-4 et C-6).** Deux défauts empêchent l'essai de tourner tel qu'écrit.

Ancien :
```text
Le compte toutes sources n'éprouve pas le plancher dès que β > 0.
```

Nouveau :
```text
Le compte toutes sources n'éprouve pas le plancher dès que β > 0. Pour cet essai, et pour tout essai sur un rang de prise (points 2 et 3), le monde ne s'arrête pas à la première alarme et il est prolongé jusqu'au rang lu (N = 10 000 ne donne qu'environ 100 endommagés quand seul le type d'enjeu 25, de part 0,01, est attaqué) ; une répétition qui n'atteint pas ce rang rend le refus nommé « trop peu d'endommagés », jamais une prise ni une absence de prise.
```

## F-2 — F-2 (C-7).** [CALCUL] Le rapport de vraisemblance d'une alternative d_j contre d0⁺ a une espérance au plus égale à 1, sous tout taux vrai d ≤ d0⁺, seulement si d_j > d0⁺. Pour une alternative placée sous d0⁺, cette espérance dépasse 1 dès que d < d0⁺. Or la grille de la v2 part de d0, donc peut tomber sous d0⁺ : il faut la reconstruire.

Ancien :
```text
Si d0 vient de m épisodes de référence, le pari se fait contre d0⁺, borne haute de Clopper et Pearson à α/2 sur la référence, avec alarme à 2/α ; la validité reste ≤ α par union.
```

Nouveau :
```text
Si d0 vient de m épisodes de référence, le pari se fait contre d0⁺, borne haute de Clopper et Pearson à α/2 sur la référence, avec alarme à 2/α, sur une grille reconstruite au-dessus de d0⁺, d_j = d0⁺ + (1 − d0⁺)·2^(−j) (une alternative sous d0⁺ ôterait la validité) ; la validité reste ≤ α par union, à tout horizon, si la référence et le flux honnête suivent la même loi. Prix, à rapporter : un excès inférieur à d0⁺ − d0 n'alarme jamais (pour d0 = 0,10 et m = 400, d0⁺ ≈ 0,13 par approximation normale, à rejouer) ; la puissance perdue n'est pas mesurée.
```

## F-15 — F-15 (C-8).** [CALCUL] Quand d0 est estimé, la variance de la référence s'ajoute à celle de la strate.

Ancien :
```text
la puissance du pari se lit sur le simulateur.
```

Nouveau :
```text
la puissance du pari se lit sur le simulateur. Si d0 est estimé sur m épisodes, la formule devient N·z₀,₉₉·√(d0·(1 − d0)·(1/(N·π_min) + 1/m)), et la sortie dit en plus l'excès jamais vu, d0⁺ − d0.
```

## F-3 — F-3 (C-17).** [PROPOSITION] Un jeton prouve qu'on l'a émis, non que le contenu est planté. Lier le jeton à la graine permet de re-dériver l'entrée ; un contenu réel ne se re-dérive pas.

Ancien :
```text
Artefact : un vecteur de poids lu d'un fichier de sonde du dépôt, ou un verdict sans jeton, est refusé.
```

Nouveau :
```text
Artefact : un vecteur de poids lu d'un fichier de sonde du dépôt, ou un verdict sans jeton, est refusé. Le jeton lie l'empreinte du contenu de l'entrée à sa graine ; le harnais re-dérive l'entrée de la graine et refuse si l'empreinte diffère : un contenu réel recopié sous un jeton valide est refusé aussi (second artefact). La garde ne couvre pas une modification du harnais lui-même.
```

## F-7 — F-7 (C-16).** Je n'ai pas la sortie de la boucle sous les yeux dans cette relecture : les chiffres du rang 12 sont repris du contre-lecteur.

Ancien :
```text
Bloc C2 retrouvé à 4 erreurs types (0,34, 0,14, 0,03 à trois étiquettes)
```

Nouveau :
```text
[FAIT RAPPORTÉ, sous supposition, chiffres repris de la contre-lecture et non relus par le concepteur] Bloc C2 retrouvé à 4 erreurs types (0,34, 0,14, 0,03 à trois étiquettes)
```

## F-4 — F-4 et F-5 (C-23).** La règle de cette consigne veut le statut « rapporté, non vérifié sur PDF », sauf lecture attestée par une pièce jointe. (identifiant attribué par l'ordre des couples sous l'intitulé commun)

Ancien :
```text
Statuts. Lus sur PDF au dépôt, aux pages dites par N-076, § 11 (chemins et empreintes y sont) :
```

Nouveau :
```text
Statuts. Rapportés par N-076, § 11, comme lus sur PDF au dépôt, aux pages qu'il dit (chemins et empreintes y sont ; ni le concepteur ni le contre-lecteur n'ont ouvert ces PDF) :
```

## F-5 — F-4 et F-5 (C-23).** La règle de cette consigne veut le statut « rapporté, non vérifié sur PDF », sauf lecture attestée par une pièce jointe. (identifiant attribué par l'ordre des couples sous l'intitulé commun)

Ancien :
```text
Les autres restent au statut « rapporté, non vérifié sur PDF » :
```

Nouveau :
```text
Ces citations ajoutées sont au statut « rapporté, non vérifié sur PDF ». La liste ci-dessous reprend toutes les antériorités de la v1 : les six nommées en tête y gardent le statut que leur donne N-076, § 11 ; les autres restent au statut « rapporté, non vérifié sur PDF » :
```

## F-9 — F-9

Ancien :
```text
avec un canal par grandeur :
```

Nouveau :
```text
avec un canal par grandeur (six avec `lisibilite`, défini aux paramètres) :
```

## F-6 — F-6

Ancien :
```text
- **Aucun PDF ouvert.** Toutes les antériorités sont de mémoire ou reprises des pièces jointes.
```

Nouveau :
```text
- **Aucun PDF ouvert.** Les antériorités sont de mémoire ou reprises des pièces jointes ; le statut « lu sur PDF » de six d'entre elles est celui de N-076, § 11, non une lecture du concepteur.
```

## F-14 — F-14

Ancien :
```text
Les seuils binomiaux et les puissances viennent d'une approximation normale et sont à rejouer avant tout usage.
```

Nouveau :
```text
Les seuils binomiaux 1 869 et 18 903 et la puissance 0,583 sont rejoués par la contre-lecture (bloc R2) ; les autres puissances restent d'approximation normale, à rejouer avant tout usage.
```

## F-8 — F-8 : le § 2 contredit C-12.** C-12 interdit à la politique de lire le score ; le monde du § 2 la fait encore dépendre de g(score).

Ancien :
```text
La politique de dommage n'endommage que les épisodes où g(score) = 0 et où l'enjeu est maximal.
```

Nouveau :
```text
La politique de dommage n'endommage que des épisodes de lisibilité nulle et d'enjeu maximal ; g(score) = 0 y est forcé (point 1) et ce forçage est consigné au journal.
```

## F-10 — F-10 : la garde 2 refuserait le bras de comparaison de C-3.

Ancien :
```text
Ligne à π = 0 ; probabilité manquante ; plancher fonction du score
```

Nouveau :
```text
Ligne à π = 0 hors de la configuration `sans_plancher` (dont le journal porte l'étiquette « sans plancher : aucune borne ») ; probabilité manquante ; plancher fonction du score
```

## F-11 — F-11 : le rang 12 de C-16 manque à la liste des instruments.

Ancien :
```text
le simulateur, la table, les gardes, les deux familles plantées et les treize épreuves.
```

Nouveau :
```text
le simulateur, la table, les gardes, les deux familles plantées, les treize épreuves et l'échelle des échelons simulée (rang 12, monde planté seul, sous le jeton de provenance).
```

## F-12 — F-12 : la décision 2 ne place pas le rang 12.

Ancien :
```text
(a) Les rangs 1 à 10 maintenant, les épreuves ensuite.
```

Nouveau :
```text
(a) Les rangs 1 à 10 maintenant ; le harnais, les épreuves et l'échelle des échelons (rangs 11 et 12) ensuite.
```

## F-13 — F-13 : le § 1 dit encore « reconstruit », contre C-26.

Ancien :
```text
(s̄ = 1,60, reconstruit du bloc C joint)
```

Nouveau :
```text
(s̄ = 1,60 ; loi du script du bloc C, supposition d'illustration)
```

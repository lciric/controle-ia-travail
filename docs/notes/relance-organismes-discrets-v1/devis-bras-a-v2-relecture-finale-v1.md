# Relecture de la version finale du devis du bras A par un agent neuf — constats à porter — 2026-11-18T21:53:07Z

Devis relu : `devis-bras-a-v2.md` (`83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd`, inchangé, R12), contre son brouillon 2 (`28d81d7d…`). Demandée par la session mère avec la ligne GO-2026-11-18-62. Le rapport de l'agent n'est pas gardé comme fichier : ses constats sont recopiés ici par la session de relance.

**Verdict : conforme sous corrections.** Toute l'arithmétique neuve est juste ; **la demande de la première ligne (27 USD) tient** (pire cas 26,3 USD) ; aucune correction ne change un chiffre demandé. Sources de débits et de prix identiques au brouillon 2 ; les huit empreintes de la section 0 concordent.

## Avant le départ de la première ligne (à tenir par la relance, sans changer le devis)
- Relever, le jour de la création de la machine, le prix de la carte, le stockage, le téléchargement et le crédit du loueur (constat 3 ; la mère le demande aussi).
- « Au-delà d'une relance, toute relance nouvelle est un nœud » : la règle du brouillon 2 vaut toujours (constat 4).
- Une liste figée d'essais du bras A sur la machine est à écrire (constat 4).
- Les 27 USD ne couvrent pas les lectures de l'oracle qu'exigent les gardes entre les deux lignes (256 + 272 lectures, environ 2,3 millions de jetons d'entrée) : elles relèvent du devis des lectures, qui doit précéder ces gardes (constat 5).
- La ligne « Sceau » de l'en-tête du devis est périmée : son compagnon d'empreinte existe et concorde (constat 6).

## Avant de demander la seconde ligne (une version neuve du devis sera due)
1. **Formule du plafond recalculé** (coefficients justes : heures = 5,14 + 0,2133 × d ; 41,7 USD pour d = 40 s, 44,7 USD pour d = 45 s). Réserve : le débit d est mesuré à la première ligne sur des épisodes sans adaptateur, alors que les 768 épisodes de la seconde tournent avec un adaptateur chargé ; la formule retire le facteur 2 sans marge pour cet écart ; la mise en route et le contrôle d'identité, non mesurés, ne sont pas doublés (+ 3,6 USD). Correction proposée : prendre le plus grand du débit mesuré et de 42,8 s, ou une marge déclarée ; remplacer la mise en route supposée par celle mesurée.
2. **Ordre gelé du texte scellé** (section 6.3) : il place les quatre contrôles de manipulation avant les épreuves de l'oracle et l'effet minimal détectable ; le plan en deux lignes joue entre les deux lignes les épreuves, l'effet minimal détectable et le premier contrôle seulement, deux des contrôles exigeant la seconde ligne. Écart de lettre ou lecture à faire admettre : **à soumettre à Lazar avant la seconde ligne** (c'est la même question que la seconde remarque de `remarques-texte-scelle-bras-a-v1.md`, portée à la session fille de décision).
3. Les lectures hors carte ne comptent que l'entrée ; la sortie (environ 300 jetons par lecture, environ 4 millions de jetons sur 13 600 lectures) est à compter dans leur devis.

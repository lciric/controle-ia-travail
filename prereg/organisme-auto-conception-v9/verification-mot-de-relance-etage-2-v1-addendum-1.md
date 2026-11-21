# Vérification du mot de relance de l'étage 2 — addendum 1 : vérification des corrections

Même vérificateur (Opus 5.5), le 2026-11-21, passe courte. Vérification d'origine : `prereg/organisme-auto-conception-v9/verification-mot-de-relance-etage-2-v1.md` (18088ca490974f0b6959be539e0fd6456bd9aef8b29ae4c173cc7323aa2e2edb, compagnon contrôlé égal). Pièce vérifiée : `prereg/organisme-auto-conception-v9/mot-de-relance-etage-2-ligne-3-v2.md` (324158cacd4ec14b6512802f836ae25b7287bbc74ecd39372c19bdfdfed815a2, non scellée), contre la v1 (c9439a7cedd3063b5aa86fc69c4cc1ed8ce7db5c47db4efcad3ae78b7c60df54).

## Verdict : Conforme

## Contrôle, par programme (python, difflib)

- Les quatre corrections appliquées à la v1, chacune à la lettre de la vérification (chaque texte ancien présent une fois dans la v1, chaque texte neuf présent une fois dans la v2), donnent un texte qui ne diffère de la v2 qu'en deux lignes, 35 lignes de part et d'autre :
  - ligne 1, le titre : « — v1 » devient « — v2 » ;
  - ligne 3, l'en-tête : ajout en tête de la phrase de version 2 (« Version 2, écrite le 2026-11-21T09:51:30Z (`date -u`) : la v1 corrigée selon sa vérification (…, 18088ca4…), corrections 1 et 2 exigées et 3 et 4 recommandées, toutes portées. V1 écrite par… ») ; le reste de la ligne inchangé à l'octet.
- Rien d'autre n'a changé.
- Les deux blocs de commande (contrôle du mandataire, geste 9) sont identiques à ceux de la v1, donc toujours égaux au mot de départ v2 aux seuls remplacements de la déclaration et de son empreinte (vérification d'origine, § 1).

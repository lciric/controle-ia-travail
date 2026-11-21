# Vérification courte — décision N-077, retrait de la marge asymétrique (H6), mesure gardée (v1)

- **Date** : samedi 21 novembre 2026, vers 16:28 UTC (`date -u`). Dépôt à `9f02be851`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), vérificateur neuf, sur mandat de la session mère. Ni auteur de la décision ni de la note. Ni commit, ni poussée, ni appel payant, ni recherche en ligne. Rien d'ouvert sous un dossier cloisonné.
- **Pièces vérifiées**, « OK » contre leur compagnon :
  - `decision-N-077-retrait-marge-asymetrique-mesure-gardee-v1.md` : `41643fc538ff9d6bc561cde36b044ee102190d2f42efc812c4a001ca12575140` ;
  - `ligne-claude-md-N-077-v1.md` : `59b80a284eec79598afa344b53b9582990964e643471112cd4ff77a24bbc6360`.
- **Lu**, empreintes « OK » : la note v2 (`6c7e1c2f…050d`, verdict, § 2 à 4, relevé, annexe, « Décisions pour toi ») et sa vérification (`6edb4acb…`) ; le programme (`2fd63bad…`, l. 40 à 46, 97, 188, 190) ; N-013 (`157d388e…`, § 6) ; N-015 (`462785b3…`, en entier) ; `registres/go.md`, l. 653 (GO-2026-11-21-54) et 663 (GO-2026-11-21-64) en entier ; le brief (portes G0 et G1, T1.6) ; la D-2 de la note sur l'attaquant informé (l. 262) ; les mentions de H6 dans `prereg/T0.6-organismes-v0-v1.md` et `prereg/T0.7-sondes-v0-v1.md`, par motifs.

## Verdict

**Conforme.** Deux remarques mineures, à porter par erratum ou à laisser ; aucune ne touche le retrait, ce qui est gardé ni la ligne pour `CLAUDE.md`.

## Contrôles, un par un

1. **Énoncés recopiés.** Programme l. 97 et l. 45 (cellule « Hypothèses | H1, H2, L, T, H6, Tr, H8 », colonne « A — le temps ») : identiques à l'octet. N-013, § 6, titre et énoncé : identiques à l'octet. N-015, § 1 : identique au mot, mais pas à l'octet : la source est coupée en lignes avec deux espaces de retrait (« remise à⏎  zéro du contexte », « chute⏎  significativement ») ; la décision la recopie sur une ligne (remarque 1).
2. **La raison** est celle de la note v2 (§ 4, « La raison, corrigée » ; D-1) que sa vérification a jugée conforme : saboteur qui répond au mieux, aucune marge sur le succès ; une marge mesurée sur nos organismes lirait leur fabrication. Les bornes de la section 2 sont celles de la note : établi pour le rééchantillonnage seul (§ 3, deuxième borne), par construction et non mesuré pour la paraphrase de la sortie et la remise à zéro, « supposé » au pas 11, « prédite nulle » retirée, confiance 0,6, recommandation contraire le même jour. Le chiffre de 80 % (Lucassen et Kaufman, p. 10) et Lin Yulong et al. (ICML 2026, p. 1 et 3) sont ceux de la note ; le 80 % est vérifié à la page par la vérification de la note.
3. **Ce qui est gardé** suit l'option (a) de D-1 et le § 4 de la note : nuls exacts ou plantés, aucun signe avant l'inventaire, utilité égale, base nommée, échelle déclarée, décomposition information et exécution au lieu de « Ctrl-Z » seul, contraste des deux modes d'induction avec adaptateur bénin témoin, quatre lectures de l'ancienne D-2, retour par nœud sur résultat. Les champs de la mesure (objet de la paraphrase, garde du contenu, règles d'exécution et d'agrégation) sont ceux des champs fermés du § 5 de la note. Bruit sur les poids (N-013), bruit d'activations (N-015) et risque de collision (2607.13087, note v2 § 2, l. 105) : bien gardés.
4. **« Portes G0 et G1 : rien »** est juste. G0 (brief, huit critères) ne nomme ni H6 ni T1.6 ; N-015, § 2, le disait déjà. G1 (brief ; programme l. 190) oppose la boîte blanche séquentielle aux bases, sans H6. Dans les deux préenregistrements scellés, « H6-1 » à « H6-4 » de T0.6 sont des prédictions numérotées de ce texte, et T0.7 (l. 2824, 2938) exclut déjà son bras de H6 : aucun écart.
5. **Ce qu'elle ferme.** La D-2 de la note sur l'attaquant informé, laissée à Lazar par GO-2026-11-21-54 (« D-2 (H6 resserrée) »), est bien fermée : options (a) et (b) non retenues, quatre lectures versées dans la mesure. Avec la D-1 de la note v2, option (a) : un seul nœud, comme la note et sa vérification le disent. Les D-2 à D-5 de la note v2 restent ouvertes (section 6) : juste.
6. **Rien de revendiqué n'est ajouté.** Les attentes sont dites « pas des hypothèses du papier », sans critère de réussite ; H6′ et H10 non inscrites ; liste « Ne pas écrire » fidèle aux bornes de la note.
7. **Ligne pour `CLAUDE.md`** : 585 signes (comptés par programme), sous 600 ; forme « N-0xx (GO-…) : … (`chemin`) » des entrées N-070 et N-076 ; raison, mesure gardée, fermeture de la D-2 et H6′ non inscrite fidèles.

## Remarques mineures, avec texte proposé

1. **Section 1, point 3** (N-015). Remplacer « § 1, l'énoncé en vigueur jusqu'à ce jour : » par « § 1, l'énoncé en vigueur jusqu'à ce jour (retours à la ligne et retraits de la source joints) : ».
2. **Section 0, deuxième alinéa.** La phrase « Un saboteur qui connaît l'intervention et y répond au mieux ne perd rien. » et la parenthèse « (un saboteur à consigne se contredit d'un tirage à l'autre) » sont plus fermes que la section 2. Texte proposé : « Un saboteur qui connaît l'intervention et y répond au mieux ne perd rien de son succès : c'est établi pour le rééchantillonnage, par construction seulement pour le reste. » et « (selon les sources, un saboteur à consigne se contredit d'un tirage à l'autre) ».

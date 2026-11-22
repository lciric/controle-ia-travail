# Erratum 1 du code du hasard du défenseur, v2 (classe B)

- **Date** : 2026-11-22, vers 14:25 UTC. **Auteur** : session des chantiers du 21 (Opus 5.5), qui consigne. Vise `src/controle_ia/hasard_defenseur_v2/` (rapport v2 `d5ec45d3…`), après la vérification du même contre-lecteur, `verification-code-hasard-defenseur-v2-opus-v1.md` (`18b6f884…`) : « conforme après corrections », onze constats sur douze fermés, le constat 11 renvoyé au concepteur.

## Correction restante, portée
- **Essai neuf** `tests/test_hasard_defenseur_v2_complements_constat4_v1.py` (`6a37b836…`), recopié mot pour mot de la vérification. Il est scellé avant sa première exécution.
- Il passe sur la v2 (1 réussi).
- Il casse quand la correction du constat 4 est retirée, dans une copie mutée sous le bloc-notes, jouée depuis la racine de la copie (1 échec).
- Note de méthode : jouée depuis la racine du dépôt, la mutation semblait survivre. La configuration de pytest (`pythonpath = ["src", "tests"]`) chargeait alors le code du dépôt et non celui de la copie. Toute mutation sur une copie doit donc se jouer depuis la racine de cette copie.

## Commentaire à lire autrement
L'essai à k = 2 du développeur, sur le constat 4, se lit : « vérifie la règle du dénominateur nul à k = 2, mais n'éprouve pas la correction ». À k = 2, deux valeurs égales donnent toujours une variance exactement nulle. La correction n'est éprouvée qu'à k = 3, par l'essai neuf.

## Réserve documentaire
La sortie complète de référence (`simulations-hasard-defenseur-v1-complete-v1.json`) porte l'empreinte du code v1. Les sorties v1 et v2 à petite taille sont identiques hors version, code et durée : constaté par le développeur et par le contre-lecteur. Un préenregistrement qui engage le code v2 le dit, ou rejoue le script v2 (environ 36 minutes en local, sans dépense).

## Renvoyés au concepteur
Les points ouverts 6, 8 et une partie du 12 ; le constat 11 (le volet relatif du cas sain de G5).

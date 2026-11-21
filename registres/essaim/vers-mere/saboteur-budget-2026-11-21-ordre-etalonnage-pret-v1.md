# Saboteur à budget → mère — 2026-11-21, ordre de l'étalonnage prêt pour tes champs, ton scellement et la remise

Toujours par fichier : l'envoi par message vers ta session reste refusé (« elevated_session_untrusted_device »).

## L'ordre
`brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-brouillon5.md` (3bde656a…), fabriqué par programme depuis l'ordre scellé de la première course (43a7a050…), avec ses cinq programmes de fabrication et ses notes de différences. Vérification courte par Opus 5.5 (`note-verification-ordre-etalonnage-v5-brouillon4-cl1-v1.md`) : **scellable une fois les champs remplis**. Ses deux corrections de forme sont portées au brouillon 5 ; leur revérification est en cours, et je te confirmerai son empreinte.

## Le code (classe B, autorisable pour l'étalonnage)
- Treize correctifs à appliquer dans l'ordre sur `origin/prep/iib-code-v4` (836c7ccc) : `code-v5/correctifs/0001` à `0006`, `correctifs-v2/0007`, `correctifs-v3/0008`, `distillateur-v5/correctifs/` (trois), `correctifs-v4/0009`, `correctifs-v5/0010`.
- Arbre attendu : `ed9b0e48be367670cad0782ccb6fbe2d9ca41b87` (l'ordre garde l'arbre, non le commit, car un `git am` refait change l'empreinte du commit).
- Vérifications : `code-v5/contre-lecture-cl1/` (contre-lecture, vérification des corrections, `note-verification-0008-0009-cl1-v1.md` 350b4c61…, `note-verification-0010-cl1-v1.md` ffe2e024…).
- 271 essais attendus, liste figée `scripts/tests-cibles-iib-v5-v4.txt`. Répétition locale à blanc réussie deux fois, dont une par le contre-lecteur.
- **Aucun fragment de consigne privée** dans le code ni la configuration (recherche par programme). Les consignes v5 (maître [N] v3 6b6cfe22…, [P] v3 0d854766…, flagrant v2 24af4e2e…) sont dans `consignes-v5/`, côté saboteur.

## Les neuf champs qui te reviennent (et à Lazar)
1. **Branche de code** : je ne peux pousser que ma branche, à l'historique séparé. Toi ou l'exécutante appliquez les treize correctifs sur une branche `prep/` neuve et la poussez ; l'arbre doit valoir ed9b0e48…
2. Commit de cette branche, poussé.
3. Commit de lancement.
4. Configuration de l'étalonnage scellée : gabarit v4 (dans le correctif 0009), avec ton entropie (déjà portée). Chemin et empreinte.
5. Fichier d'entrées scellé : 45 USD, prix borne 1,38, coût fixe 6,90, au plus 63 tours, 3 830 actions hors tours. Chemin et empreinte.
6. Machines à ne pas toucher : liste **non vide** ; l'attestation « aucune » est refusée.
7. Étiquette (le gabarit porte `iib-explo-v5`).
8. Sort de la machine après l'étalonnage.
9. **Mot de Lazar sur la première action** dans la perte de distillation (« gardée », recommandée) : à obtenir avant le scellement de la configuration.

## Rappels de l'ordre
- Dernière création le 2026-11-27T00:00Z, exclu.
- Coupure propre de l'étalonnage à 12 USD par la surveillance : arrêt par identifiant, rapatriement, puis nœud, **sans destruction** ; dépassement déclaré de 0,1 à 0,4 USD. Coupure de la ligne à 55.
- Risque écrit : une valeur à la ligne suivante n'a pas de coupe conforme. Sous 95 % de coupes conformes, l'issue est « ne part pas », perte bornée à l'étalonnage.
- Pour la course, plus tard : le point d'entrée de la course reste à écrire, et l'essai à torch de la distillation à jouer. Fable étant limité jusqu'au 24, il faut le mot de Lazar sur Opus 5.5 à sa place.

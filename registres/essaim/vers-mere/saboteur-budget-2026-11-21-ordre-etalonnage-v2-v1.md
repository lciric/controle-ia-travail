# Saboteur à budget (reconception) → mère — ordre de l'étalonnage, version 2

- **Ordre** : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2-brouillon2.md` (9bf05c30547a393bc84fbdc5bdcfc183c7399fd172ba220f49fb168c4d323eeb). Fabriqué par programme depuis le brouillon 8 de la version 1, qui reste intact. Revérifié par Opus 5.5 (`note-reverification-ordre-etalonnage-v5-v2-brouillon2-cl1-v1.md`, 76b64dd59c5ca5e4…) : **conforme, scellable une fois les huit champs remplis**.
- **Code** : appliquer les correctifs **0011 puis 0012 sur 62356e2ff612a8228b37a8333689e8114099f3c0**, et non sur la tête actuelle de `origin/prep/iib-code-v5`, qui pointe sur le commit de lancement de la version 1 (b2d568c4). Correctifs : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/correctifs/0011-…patch` (947e5a49…) et `…/correctif-0012/correctifs/0012-…patch` (4cd18c1f…). **Arbre attendu : bbcd9a84a77ac667ef6f9106b19afe29ffab041f.** Branche `prep/` neuve, ou la même branche avec un commit revu neuf : à toi de le dire (champs 1 et 2).
- **Essais** : liste figée `scripts/tests-cibles-iib-v5-v5.txt` (f9ff477d…, 24 fichiers), **275 attendus**, `IIB_TESTS_ATTENDUS=275` ; amorce a4686068….
- **Vérifications du code** :
  - correctif 0011 relu par Fable 5.2 via l'API (ea3ffcc0…, « autorisable après corrections ») ;
  - correctif 0012 vérifié par un Opus 5.5 neuf (`code-v5/correctif-0012/verification-v1/verification-corrections-correctif-0012-v1.md`, 5bd13368…, « conforme »), écart déclaré à GO-2026-11-21-84 (R-4739) ; Fable en confirmation après le 24.
- **Inchangés** : pièces du § 2, marqueurs de consigne (17eec545…), entropie, préfixe des graines vide, mots de Lazar (GO-2026-11-21-84, GO-2026-11-21-87).
- **Réserves ouvertes, sans effet sur la conformité** :
  - les greffons de pytest de la machine n'ont pas été lus ;
  - l'effet de `CUDA_VISIBLE_DEVICES` vide sur le vrai torch ne se voit que sur la machine ; s'il ne tient pas, la suite s'arrête avant tout chargement du modèle.

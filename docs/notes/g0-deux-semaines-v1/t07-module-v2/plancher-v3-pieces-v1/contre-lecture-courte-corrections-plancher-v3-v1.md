# Contre-lecture courte et différentielle des corrections du code du plancher v3 de T0.7 et du script d'instance v3 — v1

**ÉTAT : EN COURS (ébauche posée à 04:08 UTC le 2026-11-11 ; non scellée ; aucun verdict encore).**

Différence relue : `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07..7e23a554aca040016a08fe510504adec172c6998`.
Contre-lecteur neuf : Claude Fable 5.2 (`claude-fable-5-2`).

## Notes de travail (provisoires, 04:14 UTC ; remplacées par le texte final)

- Essais de l'arbre (extraction de départ) : 43 passés, 30 sautés (données génériques de P3 hors de l'extraction), code 0, 04:07:47–04:08:22.
- n34, n25c, n28 rejouées sur copie : tuées (n34 et n28 par un essai de comportement, miroir retiré compris ; n25c par `test_palier_global_le_pire_des_gardes`).
- Attaque du cache (caches factices, hors ligne) : passent « index absent, un morceau sur quatre », « morceau de taille nulle », « weight_map vide sans poids » ; index illisible → exception hors `GardeArret` (passe à blanc : code 1, pas 2). Aucun n'est atteignable après un `snapshot_download` réussi.
- Attaque « un exemple retiré » sous la v8, effectifs réels (tromperie 478) : arrêté ; fautes partielles dès 2 exemples : arrêtées. Enjeux (1 591) : en cours.
- Script v3 : quatre appels `lecture_v4`, aucun `repli-recalcul`, `env CUBLAS_WORKSPACE_CONFIG=:4096:8` sur la seule étape A, contrôle de la révision de P3 à l'étape 8 (avant la branche, le repli, la passe à blanc) ; arrêts par identifiant inchangés.

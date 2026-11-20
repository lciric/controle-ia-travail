# Vérification des corrections C1 à C3 du code de l'étage 1 de la ligne 3 — v1

Pièce de travail (classe C), 2026-11-20. Vérificateur neuf, modèle S : je n'ai écrit ni le code ni la contre-lecture. Rien écrit dans le dépôt (état git propre), aucun commit, aucun calcul décisif, aucun chronométrage, aucun fournisseur, aucun refus d'outil.

## Verdict : **Conforme**

## Empreintes
Mandat, texte de la version 7 (`4e3680d9…`, repris par `git show origin/main:…` après `git fetch`), contre-lecture, `mutants_cl.py`, code v1 (4 fichiers), code v2 (7 fichiers) : chaque empreinte égale à son compagnon. Mes copies (dossier `code/`) ont les empreintes du rapport du développeur (banc `ffc33083…`, essais `d90eb6f3…`, chronomètre `9bcea530…`, contrôle `1ead2775…`). Python 3.13.18.

## 1. C1, C2, C3 appliquées
- **C2** (banc 1386-1424). La fonction `plus_petite_taille_a_partir_de_laquelle` rend la plus petite taille t de (25, 50, 100, 200) telle que la branche tient à t et à toutes les tailles plus grandes ; None si la plus grande ne tient pas ; « incomplet : tailles de la grille sans cellule […] » si une taille manque (jamais silencieux). Cela suit la lettre « à partir de laquelle » (texte, ligne 321). Une seule grandeur rendue, avec la table par taille comme information ; l'ancienne clé disparaît. Essais : cas sains et artefacts (intermédiaire qui tient, plus grande qui ne tient pas : 100, 200, None).
- **C3**. Essai sain `verifier_autorisation` (2026111931 à 2026111933, chemin `Path` ou chaîne, sans dérivation ni entropie créée) ; huit artefacts avec motif ; six défauts G01 à G06 visant cette seule fonction, tous vus. Garde du contrôle (texte ancien dans le corps de la fonction, essais visés à préfixe dédié, aucun nom qui dérive) lue : correcte.
- **C1**. 36 essais neufs (109 − 73) ; les 35 mutants de `mutants_cl.py` sont recopiés à l'identique (lecture ligne à ligne, et le contrôle refuse tout texte ancien absent ou multiple) et tous vus ; plus C2R, B3S, G01-G06.

## 2. Différentiel v1 → v2 (`diff -u`, fichiers un par un)
- Banc : nom de version, docstring, fonction ajoutée et `criteres_branche_2` (C2), deux noms de fichiers de sortie. Rien d'autre. Aucun tirage, aucune graine, aucune constante touchés.
- Chronomètre : nom du banc chargé, docstring, nom du manifeste. Rien d'autre.
- Essais : les seules lignes retirées sont des renommages v1 → v2 (en-tête, chemins, noms de sorties) ; les 73 essais de la v1 sont gardés.

## 3. Essais passés et échoués chez moi
- `python3 -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v2.py` (copie dans `code/`) : **109 passés, 0 échoué** (10,8 s).
- Contrôle des défauts réintroduits, rejoué par moi, deux modes, dossiers de travail neufs :
  - mode visé : essais visés sur le banc sain, 72 passés ; **70 défauts sur 70 vus** (v1 27/27, contre-lecture **35/35**, C2R 1/1, B3S 1/1, graines 6/6), `non_vus` vide partout ;
  - mode complet : fichier entier sain 109 passés ; **70 lignes « vu » sur 70, `tous vus : True`**, code de sortie 0. (Le rapport du développeur annonce 64 en mode complet car les 6 défauts « graines » y sont comptés à part ; chez moi le programme les rejoue sur leurs essais visés et rend 70 vus.)
- Échoués : aucun.

## 4. Graines
Seule la racine 2026111930 est dérivée : l'essai final `test_zz_final_…` (journal du banc et entropies de toute `SeedSequence` créée du processus égaux à {2026111930}) passe dans mes 109 essais. Les essais de `verifier_autorisation` ne dérivent rien (journal et entropies inchangés). Aucune des racines 2026111931 à 2026111937 dérivée. Le chronomètre ne crée aucune `SeedSequence`. La création de `SeedSequence` reste unique dans le banc.

## 5. Questions de texte (relu sur le texte de la version 7)
Confirmées comme silences du texte, non écarts du code : A (« écart de 0,2, 0,3 et 0,5 » sans monde, ligne 232) ; B (ρ′ = 0 ; 0,5 ; 0,9 écrit pour le bras R seul, ligne 236) ; C (« le même juge scripté lu k fois », ligne 220) ; D (« un juge change » sans composition du collège) ; E (la table gelée, lignes 313-315, a trois lignes et aucune pour « tient à 50 seulement ») ; silence 1 (« part des alarmes qui portent sur un changement à effet », ambigu) ; silence 2 (borne de 0,08 sans mot calculé, ligne 185). Les essais neufs épinglent les choix actuels sans les trancher, et le rapport le dit.

## Défauts vus et corrections
Aucun défaut qui exige une correction. Remarques sans effet : (a) quand la plus grande taille ne tient pas, la clé vaut None, ce qui se lit « aucune taille » ; (b) le chiffre « 64 en mode complet » du rapport du développeur et mon « 70 » désignent la même exécution, comptée différemment.

Vérificateur, modèle S.

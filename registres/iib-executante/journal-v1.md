# Journal de l'exécutante du saboteur à budget — v1

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Mandat `registres/iib-executante/mandat-executante-iib-v1.md` (`6a29af94922704f6986118a2ae1fb0c4124a70eb5c86a746adb308f02c3574ce`, vérifié à `7903ec16`). Exploratoire, non opposable (R-522). Phase 1 : aucune instance, aucune recherche d'offre, aucune dépense.

## 2026-11-18, vers 23:30Z — reprise
- Mandat vérifié et lu en entier. Ordre brouillon 8 `eb83e944…`, devis brouillon 6 `f035039f…`, vérification de l'ordre `bd7941ec…`, chemin critique `39821578…` : empreintes conformes.
- Routine de reprise, points 1, 2, 5 : empreintes de lancement 3/3 conformes ; état et passation `2026-11-18-2220.md` lus ; environnement `.venv` en installation (suite ciblée en attente). Aucune machine inventoriée ni touchée (la mère s'en charge).
- Annonce faite à la mère.

## Phase 1, point 1 — version de l'outil de location
- `vastai` absent du conteneur (code 127). **Écart déclaré** : installé seul, `vastai==1.8.3` (version figée de `requirements-pilotage.txt`), dans `/home/user/outil-vastai-v1`, forme de l'écrit de la mère pour 7b (R-2351). Seul appel : `vastai --version` → **1.8.3** (code 0).

## Phase 1, point 2 — empreintes du code à `ec3b0329`
- Arbre de travail séparé, détaché à `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` (= tête distante de `prep/iib-code-v3`).
- 34 fichiers (paquet `src/controle_ia/iib/`, 15 ; scripts du lanceur, de l'amorce, des deux lectures, de la répétition jouet et liste des essais ; 13 fichiers d'essais `tests/test_iib_*`), par `git show ec3b0329:<chemin> | sha256sum` : `blanc-ec3b0329-v1/empreintes-code-iib-ec3b0329-v1.txt`. Liste des essais `847676ef…e3b6`, égale à l'ordre.
- Suite ciblée au processeur : **en attente** de l'environnement (dernière ligne au journal v2).

## Phase 1, point 3 — longueurs de la consigne (J6)
- Jetoniseur de Llama 3.1 8B Instruct, révision `0e9e39f2…`, téléchargé sans dépense avec le jeton de l'hébergeur (par son nom) ; `tokenizer.json` `79e3e522…b2b4`, empreinte git égale à celle de l'hébergeur à cette révision ; `tokenizers` 0.23.2, processeur.
- Consigne chargée par `charger_consigne_iib` du code revu (empreinte `9f8bbdef…` vérifiée) ; jetons sans jetons spéciaux : **105 ; 15** (consigne du maître ; indication à chaque pas). Aucun texte écrit.

## Phase 1, point 6 — contrôles à blanc à `ec3b0329`
- Journaux : `blanc-ec3b0329-v1/journal-blanc-ec3b0329-v1.txt` (extractions réduites) ; `journal-blanc-extraction-run-ec3b0329-v1-tronque.txt` (premier jouet, fautif : copie d'un clone partiel dont le distant prometteur ne portait plus `ec3b0329` ; défaut du jouet seul ; journal tronqué à 4 000 octets, la suite listait l'historique de `diag/`) ; `journal-blanc-extraction-run-ec3b0329-v2.txt` (jouet fidèle).
- Extraction réduite de `main` : clone 0, checkout 0, ligne `GO-2026-11-10-08` comptée 1.
- Extraction réduite du code : clone 0, sparse 0, checkout 0 ; tête distante `ec3b0329` ; ligne GO au commit : 1. `ls-remote` de `essai/iib-explo-v1` : code 2 (absente). Fetch réel de la branche du run : code 128 (absente, attendu).
- Extraction des fichiers du run, sur jouet fidèle (distant qui porte `ec3b0329` par objets partagés, branche du run enfant de `ec3b0329`, `donnees/` ajouté de force) : fetch 0, show du résumé 0, ls-tree 0, listés 2 / absents ou sans compagnon 0, `sparse-checkout add` 0, checkout 0, vérifiés 2 = listés 2 ; artefact « fichier listé absent » : `verifier` code 1.
- Place : `main` réduit 7,3 Mo ; code réduit 390 Mo ; code et dossiers du run 538 Mo (l'ajout de `/diag/ /runs/ /donnees/ /traces/` extrait aussi l'historique de `diag/` du dépôt) ; libres ≈ 20 Go.

## Phase 1, point 4 — configuration (préparée, non scellée, non commise)
- Programme `fabriquer_config_iib_reel_v1.py` (hors dépôt pour l'instant), depuis le gabarit du code revu. Restent : `MOT_LAZAR_CREATION_IIB` (mot de Lazar à venir), `CHEMIN_CONCEPTION_IIB` et `EMPREINTE_CONCEPTION_IIB` (reçus de la mère : `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md`, `77f1cc99…`, vérifiée sur `main`), `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR`, `EMPREINTES_CODE_IIB` (à reporter).

## Tâche ajoutée par la mère — note d'interface pour le côté moniteurs
- `docs/notes/barreau8-iib-v1/interface-passe-cote-moniteurs-v1.md`, scellée ; faits tirés du code revu, de l'ordre et des fichiers de configuration du modèle ; aucun mécanisme, aucun fragment de la consigne, aucun réglage du saboteur ni de l'oracle.
- Gel des poussées reçu (23:43Z) puis levé (23:47Z) : rien poussé pendant le gel.

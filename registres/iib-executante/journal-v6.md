# Journal de l'exécutante du saboteur à budget — v6

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Suite du journal v5 (`registres/iib-executante/journal-v5.md`, `acecd476…58ea`), qui reste tel quel. Exploratoire, non opposable (R-522). Aucune instance, aucune recherche d'offre, aucune dépense.

## 2026-11-19, vers 06:43-06:46Z — décision de la mère sur le défaut du lanceur (R-3619)
- Développeur neuf, branche `prep/iib-code-v4` issue de `ec3b0329` ; correction restreinte au lanceur shell, lignes 105 à 108, qui lit les tâches par `environnements/pilote_a.charger_taches` ; ni le module partagé ni `jouet_v1` touchés. Relevé des lecteurs fait en lecture seule (`docs/notes/barreau8-iib-v1/releve-lecteurs-taches-968a5151-v1.md`, `0a484b1e…`). Commit `968a5151` sur `prep/iib-code-v3` laissé en place, sans suite.

## 2026-11-19, vers 07:03Z — code corrigé jugé « AUTORISABLE » (R-3630)
- Code revu : `f9a8aaeb91cf165c6d318f8782d1e8581c5eb105` sur `prep/iib-code-v4`, parent `ec3b0329` (vérifié) ; trois fichiers changent (lanceur, `scripts/tests-cibles-iib-v2.txt`, `tests/test_iib_taches_v2.py`) ; R-3630 présent sur `main`.

## Nouveau commit de lancement
- Configuration : mêmes valeurs que `ebab1fb0…` (entropie, `MOT_LAZAR_CREATION_IIB` = R-3614) sauf les champs qui citent le code : `code.branche` et `BRANCHE_CODE_IIB` → `prep/iib-code-v4` ; `code.commit` et `COMMIT_CODE_IIB` → `f9a8aaeb…` ; `EMPREINTES_CODE_IIB` refait à `f9a8aaeb` (mêmes 34 chemins ; seule l'empreinte du lanceur change, `5e968357…` → `3279e3dc…`). Différence exacte : `blanc-836c7ccc-v1/difference-configuration-968a5151-vers-836c7ccc-v1.txt`. Garde du code : « configuration conforme (mode reel, variante B, seuil de M-1 8) ».
- `docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`, sha256 `1bd2e16a79def36de945359bb64e34beb899410dfe2964d28da1f1b85e3f6a17`.
- Commit de lancement `836c7cccda5071fe54ecb148d214d74b5cb90474` sur `prep/iib-code-v4`, parent direct `f9a8aaeb`, deux fichiers seuls ; poussé, tête distante vérifiée.

## Contrôles à blanc à `836c7ccc` (`blanc-836c7ccc-v1/`)
- Suite v1 : **456 passed** (code 0). Suite v2 : **469 passed** (code 0).
- Empreintes du code : les 34 fichiers suivis plus les deux nouveaux ; seule différence avec `ec3b0329` : le lanceur.
- Extraction réduite de `main` : clone 0, checkout 0 ; GO-2026-11-10-08 : 1 ; R-3614 : 1 ; R-3630 : 1.
- Extraction réduite du code : clone 0, sparse 0, checkout 0 ; tête distante `836c7ccc`, parent `f9a8aaeb` ; fichiers du commit : configuration et sceau ; ligne GO au commit : 1 ; branche du run absente (code 2, attendu).
- `controles-explo` (sans outil de location ; jetons vérifiés par leur nom seulement) : **code 0, « CONTRÔLES CONFORMES »**, `lancement.txt` écrit (copie : `lancement-controles-836c7ccc-v1.txt`). Le dossier des contrôles est gardé dans le bloc-notes pour la création.
- Place : `main` réduit 7,3 Mo ; code réduit 390 Mo ; dossier des contrôles 0,4 Mo.

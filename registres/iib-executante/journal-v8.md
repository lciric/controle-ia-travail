# Journal de l'exécutante du saboteur à budget — v8

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Suite du journal v7 (`registres/iib-executante/journal-v7.md`, `66d18f59…ecf3`), qui reste tel quel. Exploratoire, non opposable (R-522). Aucune instance, aucune recherche d'offre, aucune dépense.

## 2026-11-19, vers 08:40Z — ordre scellé lu (mère, R-3681 ; ce n'est pas la remise)
- `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md`, `43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e`, égale au compagnon, lu en entier ; brouillon 3 (`eed42f07…165f`) lu aux passages repris par renvoi (§ 5, levée bornée de l'interdit, § 6, § 9).
- Changement retenu pour le § 5 étape 2 : rejeu unique des contrôles dans `"$W/iib-rejeu"` juste avant la première création ; création et surveillance lisent ce dossier ; reprises (codes 3 et 5) sans rejeu.
- Préparation vérifiée sans appel au loueur : clés présentes par leur nom (VAST_API_KEY, HF_TOKEN, GH_TOKEN, CONTROLE_IA_GITHUB_TOKEN_2) ; place libre ≈ 13 Go ; dossier des contrôles à blanc intact.

## 2026-11-19, vers 08:42Z — écart de forme déclaré, accepté par la mère (R-3683)
- L'outil de location n'est pas dans le PATH du conteneur (installé à part, `/home/user/outil-vastai-v1/bin/vastai`, 1.8.3 ; cas M-002 de la mémoire des problèmes).
- À la phase 2, au début du § 5 étape 1, avant de définir ENVI : `export PATH="/home/user/outil-vastai-v1/bin:$PATH"`, puis consigner au journal la sortie de `command -v vastai` et de `vastai --version`. Aucune ligne écrite de l'ordre ne change ; pas de `VAST=` dans ENVI.

## Reste
- Remise de la mère : recharge du crédit par Lazar, ligne d'engagement, message de remise avec la levée bornée de l'interdit sur l'outil de location.

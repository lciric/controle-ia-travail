# Manifeste de l'exécutant — étage 2 à 200 de la ligne 3, partie 2 (geste 9) — v1

Texte qui fait foi : `origin/main:prereg/organisme-auto-conception-v9/mot-de-depart-etage-2-ligne-3-v2.md`. Je l'ai tiré par `git show`, redirigé vers `MON_DOSSIER/mot-de-depart-etage-2-ligne-3-v2.md`, et je l'ai lu en entier (33 lignes). Accord : GO-2026-11-20-68.
`MON_DOSSIER` = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/executant-etage-2`.

## Lecture du mot de départ (06:54:16Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R fetch origin main` | 0 | `origin/main` `806ecd5e8..1e91aa3bb` |
| `git -C R show origin/main:…/mot-de-depart-etage-2-ligne-3-v2.md > MON_DOSSIER/…` ; idem pour `.sha256` | 0 ; 0 | — |
| `sha256sum` du texte ; `cat` du compagnon | 0 ; 0 | égaux : `c89ec85b244d4b3e82e82acb0dd16b24feec75dc81cc5be9d755c2cd28faea79` (égal à l'empreinte donnée par la session) |

## Pas 1 — vérifications (06:54Z à 06:55:11Z)

| contrôle | commande | code | résultat |
|---|---|---|---|
| additif 6 à `HEX` | `sha256sum CHEMIN` (appel groupé, voir la dernière ligne) | — | `e2afc7b9…ca4f01` : égal |
| banque à `HEX_BANQUE` | idem | — | `70d35e54…94bbd` : égale |
| code d'appel v4 | idem | — | `082d19d6…f8484c` : égal |
| programme de contrôle du mandataire, au chemin écrit `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/controle-mandataire-v1/controler_mandataire_etage_2_v1.py` | idem | **1** | **« No such file or directory »** |
| pièce de scellement de la banque | `git show origin/main:prereg/…/scellement-banque-etage-2-ligne-3-v1.md` et son `.sha256`, redirigés ; `sha256sum` ; `cat` | 0 | `c91c4d338c4a524595df96c45711e0b6094e07afa438d30bc6f79b6ce78856d7` : égale au compagnon et au texte |
| déclaration à `HEX_DECLARATION` | `sha256sum` ; `cat` du compagnon | 0 ; 0 | `58cec5678b174d2929e50b22be9c13514316d8a4e308fb75c5c129ed794be376` : égale |
| programme du mandataire, contrôle de R11 | `test -e CHEMIN_DU_PROGRAMME` | non affiché | aucune sortie ; l'outil n'affiche pas le code de `test` ; je ne le tiens pas pour probant |
| | `git -C R rev-parse HEAD` | 0 | `36cfae34e29e5b017cc7912d74803ec2e42e342d` : commit de la session « composition, vérification … versés pour le scellement » sur `prep/`, au-dessus de `6dfcb278` |
| | `git -C R ls-tree origin/main CHEMIN_RELATIF_DU_PROGRAMME` | 0 | sortie vide : le programme n'est pas non plus dans l'arbre de `origin/main` |
| | `sha256sum CHEMIN_DU_PROGRAMME` (seconde fois) | **1** | **« No such file or directory »** |
| | `git -C R log --oneline -3` ; `git -C R status --porcelain --untracked-files=no` | 0 ; 0 | trois derniers commits de `prep/` ; arbre propre |

**Écart au pas 1 : le programme de contrôle du mandataire (`60523f21…`) est absent du disque au chemin écrit.** Je l'ai vérifié deux fois par `sha256sum`, puis par l'arbre de `origin/main`. Le texte dit : « Un écart arrête : retour à la mère. »

**ARRÊT au pas 1 (06:55:11Z).** Non faits :
- le contrôle de vie des relais (`test -d /proc/7533`, `/proc/7563`) ;
- le pas 2 (contrôle du mandataire) ;
- le pas 3 ;
- le pas 4 (geste 9) ;
- le relevé et l'arrêt des relais.

Aucun envoi, aucune dépense. Je n'ai rien restauré, rien commité, rien poussé.

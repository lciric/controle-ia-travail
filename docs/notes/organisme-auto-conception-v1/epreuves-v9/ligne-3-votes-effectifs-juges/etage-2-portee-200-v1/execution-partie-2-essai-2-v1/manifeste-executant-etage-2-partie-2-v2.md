# Manifeste de l'exécutant — étage 2 à 200 de la ligne 3, partie 2 (geste 9) — v2

Reprise accordée par la mère au pas 1, entier, du mot de départ v2 (`c89ec85b…`), sous GO-2026-11-20-68. Le manifeste v1 (`c25ebea4…`) reste tel quel ; il porte l'arrêt au pas 1 pour programme du mandataire absent.
`MON_DOSSIER` = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/executant-etage-2`.

## État de départ (06:57:47Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R rev-parse HEAD` | 0 | `1ad2459b4b1e860d5bf1518a6a5265856124dda7` (égal à la tête annoncée) |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide |
| `git -C R fetch origin main` | 0 | `origin/main` `1e91aa3bb..af3140f90` |

## Pas 1 — vérifications (06:57:47Z à 06:58:12Z)

| contrôle | commande | code | résultat |
|---|---|---|---|
| mot de départ | `git show origin/main:…/mot-de-depart-etage-2-ligne-3-v2.md` et `.sha256`, redirigés vers `MON_DOSSIER/reprise-…` ; `sha256sum` ; `cat` | 0 | `c89ec85b244d4b3e82e82acb0dd16b24feec75dc81cc5be9d755c2cd28faea79`, égal au compagnon |
| pièce de scellement de la banque | idem, `scellement-banque-etage-2-ligne-3-v1.md` | 0 | `c91c4d338c4a524595df96c45711e0b6094e07afa438d30bc6f79b6ce78856d7`, égale au compagnon et au texte |
| additif 6 | `sha256sum` (un appel pour les sept fichiers) | 0 | `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` = `HEX` |
| banque | idem | 0 | `70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd` = `HEX_BANQUE` |
| déclaration des relais | idem ; `cat` du compagnon | 0 ; 0 | `58cec5678b174d2929e50b22be9c13514316d8a4e308fb75c5c129ed794be376` = `HEX_DECLARATION` = compagnon |
| code d'appel v4 | idem | 0 | `082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c` : égal |
| contrôle du mandataire | idem | 0 | `60523f210e40c20709188f048a567a7eb14053b6e75ade9cdb919d7bbb04bd39` : égal |
| vérification de l'étalonnage et de la lecture v3 | idem | 0 | `c5119f0459fbdedbdfb64c0d28bfca685b85c99b9557b2ceab198edb658b8582` : égale |
| procédure des relais | idem | 0 | `0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148` (préfixe `0ca9cf5d` de l'additif, § 9) : égale ; lue en entier |
| relais Claude vivant | `stat -c %n /proc/7533` | 0 | `/proc/7533` |
| relais Argon vivant | `stat -c %n /proc/7563` | 0 | `/proc/7563` |

**Pas 1 tenu.** Remarque : la procédure (§ 3) lit `/relais/etat` par `python3 -c`, ce qui m'est interdit. Le relevé de la fin se fera par la même requête GET, par `curl -s --noproxy '*'`, une commande simple par relais.

## Pas 2 — contrôle du mandataire (06:58:36Z)

Commande du pas 2, à la lettre, en un seul appel (`env -i` avec la liste blanche, puis `/usr/local/bin/python3 -I -B …/controle-mandataire-v1/controler_mandataire_etage_2_v1.py`). Code **0**. Sortie :
`{"https_proxy_non_vide": true, "no_proxy_couvre_127_0_0_1": true, "decision": "tenu", "motifs": ["HTTPS_PROXY présente et non vide (valeur non imprimée)", "NO_PROXY couvre 127.0.0.1 par l'élément « 127.0.0.1 »", "no_proxy couvre 127.0.0.1 par l'élément « 127.0.0.1 »"]}`

**Décision « tenu ».**

## Pas 3 (06:58:46Z)

`git -C R fetch origin main` : code 0 ; `origin/main` inchangé (`af3140f90`).

## Pas 4 — geste 9

Lancé à 06:58:52Z : commande du pas 4, à la lettre, en un seul appel, en tâche de fond (délai 7 200 000 ms ; identifiant de tâche `bxabdks16`). J'attends sa fin sur la notification, sans boucle d'attente.

## Pas 5 et 6 — fin du geste 9 (notification reçue avant 06:59:24Z)

Code de sortie : **2**, refus avant tout envoi. Seule ligne imprimée :
`{"refus": "service réel : bac à sable inactif ou sans /proc neuf : dépendances du bac à sable absentes : bwrap, socat (par exemple `apt install bubblewrap socat`)"}`

Le code 2 n'est pas un des cas de relevé et d'arrêt du pas 6 (« code 0 ou 3, ou panne »). Les relais ne sont donc ni relevés ni arrêtés ; ils sont rendus à la mère vivants. Je n'ai fait aucune requête sur leurs ports. Je n'ai changé aucun argument, rien relancé, rien installé.

| commande (06:59Z) | code | sortie |
|---|---|---|
| `stat -c %n /proc/7533` | 0 | `/proc/7533` (vivant) |
| `stat -c %n /proc/7563` | 0 | `/proc/7563` (vivant) |
| `stat -c %n /home/user/sorties-ligne-3-etage-2-portee-200-v1` | 1 | « No such file or directory » : `S` n'a pas été créé ; aucun dépôt, aucun verdict |

**ARRÊT, retour à la mère (06:59:24Z).** Aucun envoi, aucune dépense comptée par le programme, aucun commit.

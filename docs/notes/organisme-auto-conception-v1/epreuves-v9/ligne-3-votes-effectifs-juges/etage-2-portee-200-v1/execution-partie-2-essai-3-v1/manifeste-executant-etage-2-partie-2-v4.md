# Manifeste de l'exécutant — étage 2 à 200 de la ligne 3, partie 2 (geste 9) — v4 (essai 3 : panne, relevé, arrêt, inventaire)

Version 4, demandée par la session après la panne. Elle reprend la v3 (`9c4f149710b2a6c945b7be5f179327fa7c0538b0df69d41b572b69225df11a74`, gardée avec son compagnon) à l'identique, sauf ce titre et ce paragraphe, et ajoute à la fin le § « Ajouts de la v4 ».

Reprise accordée par la mère, voie (a) : bubblewrap et socat installés à 07:01Z (d'après la session), bac à sable éprouvé à vide par la session. Mot de départ v2 (`c89ec85b…`), rejoué au pas 1 entier, puis pas 2 à 6, sous GO-2026-11-20-68, avec les mêmes relais 7533 et 7563. Les manifestes v1 (`c25ebea4…`, arrêt au pas 1) et v2 (`a3339df5…`, code 2 au geste 9, bac à sable) restent tels quels.
`MON_DOSSIER` = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/executant-etage-2`.

## État de départ (07:02:14Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R rev-parse HEAD` | 0 | `1ad2459b4b1e860d5bf1518a6a5265856124dda7` |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide |
| `git -C R fetch origin main` | 0 | `origin/main` `dd3af98e9..073e8f73c` |

## Pas 1 — vérifications (07:02:14Z à 07:02:37Z)

| contrôle | commande | code | résultat |
|---|---|---|---|
| mot de départ | `git show origin/main:…` et `.sha256`, redirigés vers `MON_DOSSIER/essai-3-…` ; `sha256sum` ; `cat` | 0 | `c89ec85b244d4b3e82e82acb0dd16b24feec75dc81cc5be9d755c2cd28faea79`, égal au compagnon |
| pièce de scellement de la banque | idem | 0 | `c91c4d338c4a524595df96c45711e0b6094e07afa438d30bc6f79b6ce78856d7`, égale au compagnon et au texte |
| additif 6 | `sha256sum` (un appel, sept fichiers) | 0 | `e2afc7b9…ca4f01` = `HEX` |
| banque | idem | 0 | `70d35e54…94bbd` = `HEX_BANQUE` |
| déclaration | idem ; `cat` du compagnon | 0 ; 0 | `58cec567…4be376` = `HEX_DECLARATION` = compagnon |
| code d'appel v4 | idem | 0 | `082d19d6…f8484c` |
| contrôle du mandataire | idem | 0 | `60523f21…04bd39` |
| vérification étalonnage et lecture v3 | idem | 0 | `c5119f04…8b8582` |
| procédure des relais | idem | 0 | `0ca9cf5d…085148` |
| relais Claude | `stat -c %n /proc/7533` | 0 | `/proc/7533` |
| relais Argon | `stat -c %n /proc/7563` | 0 | `/proc/7563` |

**Pas 1 tenu.**

## Pas 2 — contrôle du mandataire (07:02:53Z)

Commande du pas 2, à la lettre, en un seul appel. Code **0**. Sortie :
`{"https_proxy_non_vide": true, "no_proxy_couvre_127_0_0_1": true, "decision": "tenu", "motifs": ["HTTPS_PROXY présente et non vide (valeur non imprimée)", "NO_PROXY couvre 127.0.0.1 par l'élément « 127.0.0.1 »", "no_proxy couvre 127.0.0.1 par l'élément « 127.0.0.1 »"]}`

**Décision « tenu ».**

## Pas 3

`git -C R fetch origin main` : code 0.

## Pas 4 — geste 9

Pas 3 : `origin/main` passé de `073e8f73c` à `17c139684`.
Lancé à 07:03:01Z : commande du pas 4, à la lettre, en un seul appel, en tâche de fond (délai 7 200 000 ms ; tâche `b4xigsss1`). J'attends la notification, sans boucle d'attente.

## Pas 5 — fin du geste 9 : panne (notification reçue, relevée à 09:03:22Z)

L'outil a arrêté la commande parce qu'elle avait atteint le délai maximal de tâche de fond (7 200 000 ms, soit 2 h). Statut « killed ». **Aucun code de sortie du programme n'a été rendu.** Fichier de sortie de la tâche : 10 octets, `[killed]` seul. **Le programme n'a imprimé aucune ligne** : il n'y a ni « envois partis », ni « cumul compté », ni « motif d'arrêt ».

Je range ce cas dans « panne » au sens du pas 6. Aucune relance : elle demanderait le mot de la mère, des relais neufs et une déclaration de rang suivant (additif, § 9).

Je n'ai pas vérifié par moi-même que le processus du programme s'est terminé : je n'ai pas son identifiant, et les recherches de processus me sont interdites.

## Pas 6 — relevé puis arrêt des relais

| heure | commande | code | sortie |
|---|---|---|---|
| 09:03Z | `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` | 0 | `{"plafond_usd": 88.36, "reserve_par_appel_usd": 0.4, "depense_usd": 18.848097, "engage_usd": 0.0, "appels": 704, "refus": 0, "restant_usd": 69.511903, "refus_modele": 0, "appels_au_dessus_de_la_reserve": 0, "depassement_max_usd": 0.0, "modeles_permis": [deux noms, non recopiés ici]}` |
| 09:03:31Z | `curl -s --noproxy '*' http://127.0.0.1:8788/relais/etat` | 0 | `{"version": "relais-gemini-v2", "amont": "https://generativelanguage.googleapis.com", "modeles": [un nom, non recopié], "mandataire": true, "variable_cle_encore_presente": false, "appels": 1000, "refus": 0, "octets_envoyes": 6615782, "octets_recus": 682274, "max_appels": 2410, "max_octets_corps": 8000000, "appels_restants": 1410, "reponses_par_statut": {"200": 1000}}` |
| 09:03Z | `kill -INT 7533` | 0 | — |
| 09:03Z | `kill -INT 7563` | 0 | — |
| 09:03:41Z | `stat -c %n /proc/7533` ; `stat -c %n /proc/7563` | 0 ; 0 | encore présents |
| 09:03:48Z | `grep -E '^(State\|PPid):' /proc/7533/status` ; idem pour 7563 | 2 ; 2 | « No such file or directory » : les deux processus sont sortis entre-temps |
| 09:03:52Z | `stat -c %n /proc/7533` | **1** | « cannot statx '/proc/7533': No such file or directory » |
| 09:03:52Z | `stat -c %n /proc/7563` | **1** | « cannot statx '/proc/7563': No such file or directory » |

Les deux relais sont arrêtés par leur identifiant de processus, par SIGINT (procédure, § 6 ; R10). Le SIGTERM n'a pas été nécessaire.

| commande | code | sortie |
|---|---|---|
| `stat -c %n /home/user/sorties-ligne-3-etage-2-portee-200-v1` | 0 | `S` existe. Aucune liste, aucune lecture de son contenu ; aucun verdict ouvert. |

Ce qui est rendu à la mère, sans interprétation : le relais Claude porte 704 appels et 18,848097 USD dépensés ; le relais Argon porte 1 000 appels, tous en statut 200. Ce sont les relevés des relais. Ce n'est pas le compteur du programme, qui n'a rien imprimé.

Je n'ai rien commité, rien poussé, et je n'ai lu aucune valeur de clé. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`.

## Ajouts de la v4 (09:04:28Z à 09:05Z), sur la demande de la session

### Relevés des relais, en fichiers

La session demandait les relevés redirigés par `>` vers mon dossier. Ils avaient déjà été faits à 09:03Z, avant son message, sans redirection, et les relais étaient déjà arrêtés : on ne pouvait plus les relire. **Écart déclaré** : les deux sorties JSON, telles que l'outil les a affichées, sont recopiées octet pour octet par l'outil d'écriture, avec un saut de ligne final. Ce sont des transcriptions, non des redirections.

- `MON_DOSSIER/releve-relais-claude-8787-fin-geste-9-v1.json` : `4105959ae4e9bbdfa53209573284ee53f47b8850ac8245e48b32e498666e6f37`
- `MON_DOSSIER/releve-relais-argon-8788-fin-geste-9-v1.json` : `cc0b6982b5d969847424200f67cff9207462ab737af4a6c3609e99208fdf9ef4`

### Inventaire de `S` = `/home/user/sorties-ligne-3-etage-2-portee-200-v1` (noms et tailles, aucun contenu lu)

| commande | code | sortie |
|---|---|---|
| `ls -la S/sortie` | 0 | deux dossiers de premier niveau : `appels/`, `epreuve/` (datés 07:03) |
| `ls -la S/arrets-credit` | 0 | vide |
| `du -sb S/sortie/appels S/sortie/epreuve S/arrets-credit` | 0 | `appels` 0 ; `epreuve` 4 170 432 octets ; `arrets-credit` 0 (tailles apparentes données par `du -sb`) |
| `find S/conservation-reponses-v1 -maxdepth 1 \| wc -l` | 0 | 501 lignes, soit **500 entrées** plus le dossier lui-même |

**Écart déclaré** : j'ai d'abord lancé `find S/conservation-reponses-v1 -maxdepth 1` sans `\| wc -l`, par erreur. La commande a imprimé les noms des entrées de premier niveau (forme `argon-appel-NNNN`), sans aucun contenu. L'outil a rangé cette sortie trop longue sous `/root/.claude/projects/…/tool-results/bfzzbnk94.txt`, que je n'ouvre pas. J'ai ensuite fait le compte dans la forme demandée.

Je n'ai ouvert aucun verdict, ni de la moitié « lecture » ni d'aucune autre ; je n'ai lu aucun fichier sous `S`.

### Récapitulatif de la panne

- Geste 9 lancé à 07:03:01Z.
- Coupé par l'outil vers 09:03Z, à la limite de 7 200 000 ms.
- Sortie de la tâche : `[killed]` seul ; aucune ligne imprimée par le programme, aucun code de sortie.
- Relais relevés à 09:03Z : Claude 704 appels, 18,848097 USD, engagé 0 ; Argon 1 000 appels, tous en statut 200.
- Relais arrêtés par SIGINT, PID 7533 et 7563 ; `stat` de leurs entrées sous `/proc` en échec à 09:03:52Z.
- Aucune relance.

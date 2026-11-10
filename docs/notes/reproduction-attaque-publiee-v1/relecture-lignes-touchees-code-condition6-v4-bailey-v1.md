# Relecture des lignes touchées v3 → v4 du code de la condition 6 — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les rapports, ni la
  liste des lectures. Date : `date -u` = Tue Nov 10 13:36:08 UTC 2026 (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `66b2e3a8`, arbre
  propre avant ce rapport ; `origin/main` = `617d77d4`.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), lignes de la liste d'arrêt et des critères (l. 259-260, 307, 326-338, 366-372) par recherche ;
  - rapport appliqué : `relecture-differentiel-code-condition6-v3-bailey-v1.md` (`a210724477c75f0d38c9befc0e431f071846a2320c8b58324157c705de2e1301`), en entier ;
  - liste des lectures : `lectures-a-acter-addendum-condition6-v2.md` (`13bf51d1e0acfc715e0601837ed8e5cd3d061a41418e7c780c179c8e600e40a2`), lectures 4, 7, 13, 16, 21-30 ;
  - code : `lanceur_v4.py` (`638f90fe4b11da65212b81efa0e10b424c6e9573e045b6939489bd458b43f994`), en entier, et
    `diff -u` depuis `lanceur_v3.py` (`313f4019…`) ; `instance_v4.py` (`cbb2f1d3685e6ab05befdfd7c594315d28546021c59de761d98f6635cd198807`),
    `diff -u` depuis `instance_v3.py` (`0f9aa54b…`), plus `executer` (l. 430-510) ; `lecture_v3.py` (`66c27382…`) :
    `lire_jsonl`, `gardes_tombees`, `issue_pilote`, `relance_permise`, `tours_journal`, `k_prime`,
    `tours_complets_instance`, `_execution`, `valider` ; `analyse_v3.py` : `validite`, `garde_fin_de_run` ;
    `conventions_v3.py` : noms des journaux ; `journaliseur_v3.py` l. 155-180 ; en-têtes et imports de `gardes.py`,
    `scellement.py`, des deux `__init__.py` (fermeture de `CHEMINS_ARCHIVE`) ;
  - essais : `tests/test_temoin_bailey_condition6_v4.py` (`db53daa76309f6f57e2f96f235792a91db748b5d337900980fb0c849cd83f13b`),
    aides et essais C1-C4, D7 ; aides `poste_local`, `execution_factice`, `etape` de l'essai v3 ;
  - sondes rejouées : `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/c6-v4/test_sondes_r2_rejouees_v4.py`
    (`6395ed2e61efc413877722bc348262215fed4995edb13d5ff598cf972a48697a`) ; écart au fichier v3 : les seuls imports.
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`, tout
  résultat, note ou seuil de sonde ou de moniteur du programme, tout résultat d'attaque contre le juge de l'organisme,
  `registres/decisions.md`, `registres/etat.md` ; le reste du texte scellé ; le code public des auteurs.
- Outils : `sha256sum`, `git` (aucune requête réseau), `diff -u`, `grep`, `sed` ; essais demandés (avec
  `TEMOIN_BAILEY_CLONE=…/public-bailey/obf`) : **37 passés** ; sondes rejouées : **11 échouent, 1 passe** (D2-bis), comme
  le dit le rédacteur ; sondes de ce lecteur :
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v4/test_sondes_r2_v4.py`
  (`28646e885e612c4fb7198707022b98616158d46b66389a05230d256377f70c79`), 8 sondes, **8 passées** (chacune passe quand le
  défaut est présent), par `PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider <fichier>`. Contrôle des sondes
  N-1 : le même poste fabriqué, avec son `etat-execution-v3.json` (code 1), se lit (`etat` = None ; relance : K′ = 21).
  Aucun appel à `vastai`, aucune dépense, rien de committé. Rapport non scellé.

Renvois : « La l. n » = `lanceur_v4.py` ; « I l. n » = `instance_v4.py` ; « Le l. n » = `lecture_v3.py` ; « E » =
l'essai v4 ; « N-x » = sonde de ce lecteur.

## Verdict

**Non conforme : corrections exigées avant l'addendum.** C1 à C7 et P-i sont faits et éprouvés (les sondes D-1 à D-8
tombent sur la v4). Mais la réserve du rédacteur est **bloquante**, et plus large qu'il ne le dit : toute exécution sans
`etat-execution-v3.json` (morte sur l'instance, ou arrêtée par la conduite) rend la lecture **impossible** —
`valider` lève — y compris quand une relance complète existe, c'est-à-dire précisément dans le cas que C4 ouvre (N-1).
Le texte (l. 338, 371-372) y donne un verdict. Quatre défauts neufs, non bloquants pour le verdict mais à corriger
avant l'instance, touchent la destruction et l'arrêt par PID (N-2, N-3, N-5) ; un autre est à préciser (N-4).

## 1. C1 à C7 et P-i

| # | État | Lignes v4 | Constat |
|---|---|---|---|
| C1 | fait | La l. 1000-1012 (`try` aussitôt après `creer`, l. 1003), 817-826, 1108-1150 | taux, poste, `_etape`, veilleur dans le `try` ; taux illisible → destruction quand même, bilan `taux_illisible` ; destruction retentée 3 fois ; échec sans veilleur vivant → veilleur à échéance 0. Sondes D-1, D-1-bis inversées (`detruites == ["77"]`). Réserve : N-2 (veilleur vivant), N-5 (`creer` qui lève). |
| C2 | fait | La l. 462-476, 419-425, 443-460, 411-417, 479-490, 493-533, 785-801 ; appel l. 810, 926, 1011-1012 | chaque passage dans un `try`, erreur notée, destruction retentée ; poste illisible → dernier poste, sinon destruction ; battement ; `stderr` vers `<journal>.err` ; vérifié vivant (PID non zombie et battement frais) avant toute commande et à chaque sondage ; une relance puis arrêt. D-7 : marge et période passées (l. 780-783, 486) ; marge ≥ seuil local refusée avant la création (l. 981-982). |
| C3 | fait | La l. 128-135, 884-913, 849-858, 1111 | `executer` rend 255 sur `TimeoutExpired`, `CalledProcessError` (`ssh-url`), `GardeArret`, `OSError` ; tolérance 30 sondages consécutifs ou 3 600 s ; arrêt par PID avant `_rapatrier` sur toute sortie (`_finir` commence par `_arreter_en_cours`). `rapatrier_fichier`/`envoyer_fichier` peuvent encore lever (attrapés par `transferer` et par le `finally`). |
| C4 | fait (réserve N-1, N-3) | La l. 606-637, 640-649, 860-872, 901-904, 914-922, 944-969, 1084-1087 ; I l. 557-562 | `kill -0` et `/proc/…/status` (non zombie) ; `MORT` → état normalisé, tours relus par `instance_v4 tours` (sans note) ; tours illisibles → pas de relance ; seuil local B − 1 ; `LANCE <pid>` vérifié, second essai idempotent (éprouvé en bash réel, E `test_C4_commandes_distantes_en_bash_reel`). |
| C5 | fait | La l. 97, 828-847, 1014, 140, 145 | « running » puis `ssh … true`, borné à 1 800 s, dans D ; `accept-new`, `BatchMode`, `ConnectTimeout` sur `ssh` et `scp`. |
| C6 | fait | La l. 79-84, 546-560 | dix fichiers, tous sous `src/` ; refus d'un chemin hors `src/` ou avec `..` ; `git archive … -- <chemins>`. Fermeture vérifiée ici sur les imports : `controle_ia/__init__.py` et `temoin_bailey/__init__.py` vides ; `gardes.py` n'importe que `subprocess`, `pathlib` ; `scellement.py` que `gardes` ; aucun fichier de bras, de sonde ou de moniteur. Rien de cloisonné ne part. |
| C7 | fait | I l. 582-590 ; La l. 1077-1079 | `etat-regle-v3.json` écrit avant la garde ; une seule ligne `ETAT` avec K et `garde_tombee` ; bilan « K < 20 après le pilote : arrêt, devis révisé à Lazar » atteint (E `test_D8_conduite_K_inferieur_a_20_devis_revise`). |
| P-i | fait | La l. 187-195, 975-976 | `git show origin/main:registres/go.md`, aucune requête réseau ; texte différent refusé. La sonde `test_GO_reel_sur_main` ne tombe plus que sur l'échéance, lue 2026-11-30T22:59:59Z (lecture 7, l. 238-259) : c'est voulu ; fuseau à acter. |

Clés : aucune valeur de clé sur une ligne de commande. Le jeton passe par un fichier 600 envoyé par `scp` puis effacé
(La l. 718-733) ; les commandes distantes, l'argv du veilleur (l. 484-486) et `commande_instance` n'en portent aucune ;
`vastai` lit sa clé lui-même. Veilleur : l'identifiant détruit est toujours `self.ident`, rendu par `creer` (l. 1000,
780, 1119, 1142 ; argv `--instance`, l. 485) ; le veilleur ne connaît qu'un identifiant, et le poste est propre à la
conduite (dossier de sortie neuf, l. 987-988). Aucune destruction d'une autre instance possible par ce code.

## 2. Défauts neufs

**N-1 (bloquant). Exécution sans `etat-execution-v3.json` : lecture impossible, relance comprise.** Le fichier n'est
écrit qu'à la fin de `executer` (I l. 504-509). Il manque donc (a) après une mort sans `.fin` (C4 : hôte coupé, processus
tué) et (b) après tout arrêt du groupe par la conduite (`_arreter_en_cours` : seuil local B − 1, borne d'échéance,
instance injoignable, sortie par exception), le `kill -TERM -- -pgid` tuant `instance_v4 executer` avec l'enfant. Or
`valider` lève « état du run principal absent » (Le l. 273-274) **avant** de regarder la relance (l. 278-285), et la garde
de fin de run exige `etat-execution-v3.json` parmi les journaux (`NOMS_JOURNAUX`, `garde_fin_de_run` l. 429-430). D'où :
- K′ ≥ 20 sans relance (réserve du rédacteur) : le texte dit « lu comme un run de K′ tours, interruption rapportée »
  (l. 338, 372) ; le code ne rend rien. Sonde `test_N1_morte_21_tours_sans_relance_lecture_impossible` ;
- K′ < 20, relance complète de 21 tours : le texte dit « seule la relance porte le verdict » (l. 371) ; le code lève
  encore. Sonde `test_N1_bis_morte_3_tours_relance_complete_lecture_impossible`. La lecture 13 de la liste (« ne peut
  porter le verdict que par sa relance ») est donc fausse contre le code ;
- sonde `test_N1_ter_…` : `ETAT_EXECUTION ∈ NOMS_JOURNAUX`.
C'est un verdict impossible là où le texte scellé en donne un : ni « incomplet » ni un mot de Lazar ne le couvrent
sans écart au texte.

**N-2 (à corriger). Destruction en échec, veilleur vivant : rien ne la retente avant le secours.** La l. 1135-1146 : si
les trois destructions échouent et que le veilleur vit, la conduite s'en remet à lui ; or il ne détruit qu'à
B − 0,5 ou à l'échéance du GO (l. 432-441). Une interface de destruction indisponible une minute en fin de poste laisse
l'instance oisive jusqu'à B − 0,5 (au pire ~B − D USD gaspillés, sans run) ou des jours. L'essai E
`test_C1_…` (second cas : « veilleur vivant », `len(lances) == 1`) consacre ce comportement. Sonde
`test_N2_destruction_en_echec_veilleur_vivant_attente_jusqu_au_secours` (seul veilleur : échéance à plus de neuf jours).

**N-3 (à corriger). « Mort » sans arrêt du groupe avant la relance.** La l. 901-904 et 959-968 : sur `MORT`, aucun
`commande_arret(nom)`. `MORT` ne dit que la mort du meneur (`bash`, PID = groupe) ; un membre du groupe peut vivre
encore (sonde bash réelle `test_N3_bis_…` : meneur tué, `sleep` vivant, sondage « mort »). La relance part alors sur la
même carte avec l'ancienne exécution vivante (mémoire de carte, journaux de la première exécution qui changent après
`tours`). Sonde `test_N3_mort_sans_arret_du_groupe_avant_relance`.

**N-4 (à préciser). PID réemployé.** `_pid_vit` (La l. 606-609) ne vérifie que l'existence du PID. Après un
redémarrage du conteneur (cas « coupure de l'hôte »), le PID écrit peut désigner un autre processus : sondé « vivant »
jusqu'au seuil local ou à la borne d'échéance, la relance est perdue. Sonde `test_N4_pid_reemploye_sonde_vivant`.
Correction simple : écrire avec le PID son heure de départ (`/proc/<pid>/stat`, champ 22) ou `boot_id`, et les comparer.

**N-5 (à corriger). `creer` qui lève après la création réelle.** La l. 1000 est hors du `try` (normal : pas
d'identifiant) ; mais `vastai create` (délai 120 s, l. 107) peut lever alors que l'instance existe : elle n'est ni
détruite ni signalée. Sonde `test_N5_creer_qui_leve_rien_n_est_detruit`.

Remarques (non bloquantes) :
- `processus_vivant` récolte le veilleur mort (`waitpid`, l. 496), puis `_garde_veilleur` lui envoie `SIGTERM` par
  ce PID déjà libéré (l. 796-797) : signal possible à un processus sans rapport (R10). Ne signaler qu'un PID non récolté.
- Lecture 25 (« relance par une nouvelle conduite ») : `conduire` repart toujours de l'amorce, de la mise en place, du
  contrôle du juge et du pilote ; aucune entrée ne reprend à « principal-relance » avec le t du pilote déjà fixé. À
  écrire comme telle (nœud, relance hors code) ou à coder.
- Lecture 22 : le risque déclaré (poste local éteint, conduite et veilleur avec lui, instance jamais détruite) reste
  entier ; le run dure des jours. L'ordre de lancement doit nommer un poste local durable et l'inventaire R10.

## 3. Corrections exigées

- **C8 (N-1).** Donner un état à toute exécution qui n'en a pas, avant `empreintes` : sous-commande d'instance (par
  exemple `tours --ecrire-etat`) qui écrit `etat-execution-v3.json` absent (jamais d'écrasement), marqué
  « reconstitué », avec `code_retour` non nul, `cause_arret` (« coupure de l'hôte », ou la cause de l'arrêt par la
  conduite : « dépense », « échéance du GO », « instance injoignable »), `tours_complets`, `gardes_tombees`, `durees`
  (lues à `sortie-durees-v3.jsonl`), `k` de la phase ; appelée sur `MORT` (après N-3) et dans `_finir` pour toute
  exécution arrêtée par PID. Ou, à défaut, une `lecture_v4` qui lit ce cas sans le fichier. Essais : N-1 et N-1-bis
  inversées (K′ = 21 lu ; relance lue, K′ = 21) ; un arrêt au seuil local lu « run tronqué », sans relance (`_budget`).
  Corriger la lecture 13 de la liste.
- **C9 (N-2).** Sur destruction en échec, toujours lancer un veilleur à échéance 0 (puis arrêter l'ancien), même si
  l'ancien vit. Essai : N-2 inversée (`lances[-1][2] == 0.0`).
- **C10 (N-3).** Sur `MORT`, `commande_arret(nom)` (groupe, par PID) avant `tours` et avant toute relance. Essai : N-3
  inversée ; en bash réel, plus aucun membre du groupe après l'arrêt.
- **C11 (N-5).** Étiquette unique par conduite à la création (`--label`) ; si `creer` lève, inventaire
  `vastai show instances` filtré sur cette seule étiquette, destruction de ces seuls identifiants, sinon alerte au
  bilan (« création incertaine : inventaire R10 manuel »). Essai : N-5 inversée, et aucune instance d'une autre
  étiquette détruite.
- **N-4** : à corriger (heure de départ du PID) ou à écrire au risque déclaré.

Après C8 à C11 : relecture des seules lignes touchées et des sondes N-1 à N-5 inversées ; puis addendum, après le mot
de Lazar sur les lectures 4, 6, 7, 8, 16, 24, 25 et 26 (et 13 corrigée).

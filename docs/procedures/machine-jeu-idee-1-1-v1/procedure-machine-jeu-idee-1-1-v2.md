# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v2

- **Objet** : jouer le jeu relancé de l'idée 1.1 (`scripts/jouer_idee_1_1_v5.py --addendum
  prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md`, deux processus, processeur seul, ≈ 15,7 h attendues,
  borne dure de 48 heures murales du texte `prereg/organisme-idee-1-1-poids-du-nul-v2.md`, `3ffe1739…`) sur une petite machine
  louée, indépendante de la session, parce que le conteneur de la session a tué deux jeux en un jour (R-3010).
- **Décision** : GO-2026-11-16-09, point (2) (« option (a), relance du jeu sur une petite machine de calcul louée,
  indépendante de la session ; la dépense part sous sa propre ligne de type « calcul », inscrite par la mère sur un devis
  écrit et contre-lu (ordre de grandeur 1 à 3 USD), citant ce mot, avec une procédure de machine contre-lue ») ; R-3014.
- **Pièces de ce dossier** (`docs/procedures/machine-jeu-idee-1-1-v1/`, chacune avec son compagnon `.sha256`) :
  `lancer_jeu_idee_1_1_machine_v1.sh` (côté session), `garde_machine_jeu_idee_1_1_v1.py` (gardes qu'il appelle),
  `amorce_jeu_idee_1_1_v1.sh` (côté machine), `repetition_machine_jeu_idee_1_1_v1.sh` et `jeu_factice_idee_1_1_v1.py`
  (répétition locale), `sortie-repetition-machine-jeu-idee-1-1-v1.txt` (sortie gardée : 110 cas, 0 écart),
  `devis-machine-jeu-idee-1-1-v1.md`, `rapport-machine-jeu-idee-1-1-v1.md`, et cette procédure.
- **Modèle suivi** : la course de B bis (`scripts/lancer_bbis_v3.sh`, `scripts/amorce_bbis_v3.sh`,
  `src/controle_ia/t07bbis/registre_bbis_v1.py`) et les leçons de sa création (contre-lecture `3a3e7270…`, R-2987 ; R-2996 à
  R-3004), reprises au § 3.
- **Statut** : écrite et répétée hors ligne, contre-lue au tour 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), corrections de ce tour en v2 ; aucune machine, aucun appel au loueur, aucune dépense.
- **Version** : v2, scellée à 2026-11-16T21:41:25Z (`date -u`) ; suit la v1 (`0d674c39…`) ; changements : corrections de la
  contre-lecture du tour 1 (§ 6).

## 1. Ce que fait la machine (amorce), dans l'ordre

0. Arguments lus (`COMMIT`, `EMPREINTE_RELANCE`, `ECHEANCE_UTC_S`, `GO_ID`, `BRANCHE_SORTIE`) ; échéance dans
   [maintenant + 48 h 50, + 50 h] ; **minuterie** lancée aussitôt : 20 minutes avant l'échéance, si le jeu vit encore **et a
   passé sa borne de 48 h depuis la date de `depart.json`**, TERM à son PID (il écrit `arret.json` ; run déjà invalide) ; un jeu
   dans sa borne n'est jamais coupé par TERM ; à l'échéance, journal poussé, puis destruction de la machine par son identifiant,
   redemandée chaque minute tant qu'elle vit (état « stopped » demandé après la cinquième demande).
1. Outils présents ; processeur x86_64 ; `GH_TOKEN` présent (par son nom ; jamais affiché).
2. Branche de sortie `calcul/idee-1-1-jeu-relance-v1` absente du dépôt distant (sinon arrêt : nom neuf exigé, R12) ; dépôt
   de sortie **à part**, sur une branche **orpheline** (aucun parent : elle ne porte que `traces/machine-jeu-idee-1-1-v1/`,
   `runs/<run>/` et `diag/organisme-idees-juge-v1/<run>/`, jamais le reste du dépôt) ; **première poussée du journal**, avant
   tout calcul (une poussée impossible arrête ici, pour quelques centimes, et non après 16 heures) ; dès lors, tout arrêt pousse
   ses traces ; **suivi poussé chaque heure** (`etat.txt` : PID vivant ou non, nombre de tranches scellées comptées par leurs
   noms, jamais ouvertes, durée écoulée depuis la date de `depart.json`, projection linéaire, charge, disque libre).
3. Python 3.13.18 de l'image (`python:3.13.18-bookworm`) vérifié ; environnement neuf ; `pip install --no-cache-dir
   numpy==2.4.6 scipy==1.17.1 pytest==9.1.1` ; **contrôle des versions de l'addendum de relance (4.2)**, avec l'interpréteur du
   lancement nommé par son chemin : la sortie doit être exactement `3.13.18 2.4.6 1.17.1` (et pytest 9.1.1), sinon arrêt
   **avant tout calcul** ; `pip freeze`, `numpy.show_runtime()` et `lscpu` gardés dans les traces.
4. Dépôt cloné depuis `main` (clone partiel, sans les contenus de l'histoire), poussée rendue impossible depuis ce dépôt ;
   `COMMIT` présent **et ancêtre de main** ; extrait détaché ; arbre propre.
5. Au commit : texte `3ffe1739…`, addendum d'empreintes `73ea3bf3…` et son compagnon, **addendum de relance égal à son
   compagnon (une ligne « empreinte, deux espaces, nom ») et à `EMPREINTE_RELANCE`** (4.4), essai
   `essai_projection_cas_v1.py` `539f6a6c…` (§ 6 point 3 de l'addendum d'empreintes) ; aucune sortie ni manifeste antérieur de
   ce jeu (noms v1 à v5) ; au moins 1 Gio libre (précaution de 4.4).
6. L'échéance doit laisser au moins 48 h 40 (borne du texte comptée depuis `depart.json`, après ≈ 17 minutes de contrôles) ;
   journal poussé (« avant le jeu : commit, empreintes, versions, lieu, espace libre ») ; **jeu** par la commande de
   l'addendum, depuis la racine de la copie, interpréteur de l'étape 3 ; PID du parent écrit et poussé aussitôt (4.5). Le
   lanceur du jeu pose lui-même `nice -n 10`, les deux processus et la garde réseau. `--reprendre` n'existe pas dans l'amorce.
7. Fin du jeu : run unique de ce jeu trouvé ; chaque fichier de ses deux dossiers vérifié par son compagnon ; recopie dans le
   dépôt de sortie, comparée à l'octet ; poussée par lots (manifeste, puis tranches par 400 fichiers), reprise toutes les 5 minutes jusqu'à 20 minutes avant l'échéance si une poussée échoue, la machine restant vivante (aucun « stopped » tant que les sorties ne sont pas poussées) ; un chemin hors des
   sorties permises ou un fichier de plus de 94 Mo refuse la poussée ; un fichier écrit par le jeu hors de ses deux dossiers
   est nommé au journal (réserve), jamais poussé.
8. Journal final poussé, puis état « stopped » demandé ; la machine attend, arrêtée ; **la session détruit par
   l'identifiant** (R10) et prouve l'absence par un témoin (§ 4, gestes 13 à 16).

Codes de fin au journal : 0 (jeu mené au bout, sorties poussées) ; 2 (arrêt avant le jeu : aucun run commencé) ; 4 (arrêt
écrit du jeu, sortie absente, compagnon faux, poussée des sorties impossible). Aucun résultat n'est lu ni imprimé.

## 2. Ce que fait la mère

**Avant de remettre la suite à l'opérateur (geste 0)** — ne pas commencer tant qu'un point manque :

1. L'addendum de relance est scellé sous son nom final `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md` (déjà fait : R-3017, empreinte `a692d50c07c1b4b7ef07883ac91124eab4798cab7a579e14235484ea4d2319cf`, commit `14a0dfc5962aad5987d6c88e03e72b5f6d92f150`, ancêtre de la tête de `main` à 21:3xZ ; à relire au moment de remettre la suite, `COMMIT` pouvant être la tête de `main` du moment)
   avec son compagnon, commité et **poussé sur `main`** ; son commit est `COMMIT` (40 caractères) et son empreinte
   `EMPREINTE_RELANCE`. Aucune sortie du run invalide n'est versée sous `runs/` ou `diag/organisme-idees-juge-v1/` à ce commit
   (le lanceur du jeu refuserait ; le lanceur de session le contrôle).
2. **Écart D7** (addendum de relance, 4.10 (ii)) : [T] l. 629 et 660 interdisent une machine louée et toute dépense ;
   l'addendum exige le mot de Lazar sur D7, consigné à `registres/go.md`. Le mot de Lazar sur D7 est inscrit : GO-2026-11-16-10 (R-3016, 2026-11-16T20:47:50Z) ; GO-2026-11-16-09 ne sert qu'à l'option (a)
   (« option (a) … machine de calcul louée ») ; plus aucune question de la mère sur D7 ; le feu cite GO-2026-11-16-10 en toutes lettres.
3. Contre-lecture de cette procédure et du devis par un lecteur neuf (R2), corrections faites.
4. **Ligne de GO de type « calcul »**, accordée par Lazar, citant GO-2026-11-16-09 et GO-2026-11-16-10 : périmètre qui nomme « idée 1.1 » (la
   garde l'exige), plafond écrit `3.5 USD` (point décimal ; la garde de dépense le lit), échéance 2026-11-22 au plus tôt (devis § 1 : la garde de dépense relit la ligne à chaque appel ; un code 2 de date au geste 12 est un nœud de la mère, jamais un ordre de destruction).
5. **Feu écrit** : une ligne `R-<N>` de `registres/decisions.md` qui cite, en toutes lettres, ce GO, `COMMIT`, l'étiquette
   `jeu-idee-1-1-relance-v1` (la garde de création exige ces trois chaînes), l'image `python:3.13.18-bookworm`, le disque de
   20 Go, le prix garde maximal de 0,06 USD/h, l'échéance de 49 h 45 après l'impression, la branche
   `calcul/idee-1-1-jeu-relance-v1`, 0 relance, l'opérateur (sous-agent du modèle A ; arrêt au premier refus d'une permission,
   du crochet ou du classifieur, sans rejeu ni contournement) et les écarts de forme permis : la réponse du loueur écrite dans
   le dossier d'envoi (§ 3, L6) et la ligne jouée par l'outil du loueur à son chemin complet (déjà dans la ligne imprimée).
   Le texte passé aux commandes est la forme courte `R-<N> GO-…` (leçon C4).
6. Crédit : recharge automatique du loueur active (R-2996) ; préavis d'une ligne à Lazar au moment du geste 8.

**Pendant le jeu** : lire le journal poussé (geste 11) ; inscrire au registre, dès la poussée « avant le jeu » et « jeu
lancé », le commit, l'empreinte de l'addendum de relance, la sortie du contrôle des versions, le lieu (identifiant de la
machine, processeur relevé), l'espace libre et le PID (addendum de relance 4.4 et 4.5 ; sur la machine, ces faits sont
**poussés avant le lancement** et transcrits après : écart de forme déclaré, § 5 du rapport) ; garde de dépense chaque heure
(geste 12) ; nœuds du geste 12.

**Après le jeu** : recopie octet pour octet des sorties dans le dépôt depuis la branche de sortie, vérification par leurs
compagnons avant toute lecture (addendum d'empreintes § 5), puis destruction et preuve (gestes 13 à 16) ; lignes aux
registres (`arrets.md`, `depenses.md`, `decisions.md`) ; lecture gelée par `scripts/lire_idee_1_1_v5.py`, lecteur neuf (R13),
audit de symétrie (R4) écrit avant le prononcé ; le rapport nomme le run invalide sans chiffre tiré de lui (4.8).

## 3. Leçons de B bis reprises (et ce qui change)

- **L1 (C1)** : chaque geste est autonome : un sous-agent ne garde ni dossier courant ni variable d'un appel à l'autre ;
  chaque appel redonne ses constantes (§ 4, en tête).
- **L2 (R-2998)** : le filtre de recherche de l'outil ne suffit pas (A100 de 40 Go passées en B bis) : l'offre se choisit
  **par la garde jouée hors ligne sur chaque offre** de la recherche (`offre-depuis-recherche` : la moins chère des offres
  acceptées, chaque refus nommé), jamais à la main ; offre **avec ou sans carte** (`num_gpus` entier ≥ 0, leçon du pilote v13).
- **L3 (C3, R-1)** : la ligne de B bis faisait 32 Ko et devait être lue en trois morceaux puis recopiée. Ici, l'amorce est
  **compressée avant le base64** (`gzip -9 -n`) : la ligne fait ≈ 11 900 caractères (répétition : 11 911), lue en **deux
  morceaux de 6 000** ; contrôle par programme (`controle-ligne` : amorce décodée et décompressée égale à l'octet au
  fichier) ; copie vérifiée par `cmp` avant le jeu.
- **L4 (R-3003)** : le pilote graphique a changé le libellé de `nvidia-smi` et perdu un départ. Ici **aucune carte n'est
  employée et rien ne lit `nvidia-smi`** ; une offre à carte bon marché est admise telle quelle.
- **L5 (C4)** : le texte de feu passé aux commandes est court, `R-<N> GO-…`, un seul numéro de GO, de type « calcul » ; la
  garde de création refuse toute autre forme.
- **L6 (R-3002, R-3004)** : la réponse du loueur à la création porte en clair une clé propre à la machine. Changement : la
  ligne imprimée l'écrit dans `DOSSIER/reponse-creation.json` (`umask 077`) et n'affiche que `success`, `new_contract` et les
  **noms** des clés ; le fichier est effacé après la preuve de destruction (geste 16).
- **L7 (C5, R-2829)** : `GH_TOKEN` existe déjà dans la session (jeton de session) : l'export depuis
  `CONTROLE_IA_GITHUB_TOKEN_2`, par son nom, est inconditionnel et **dans le même appel** que la ligne.
- **L8 (R-2789)** : une destruction n'est jamais jugée par un code de sortie : absence de l'identifiant dans la liste des
  instances, un témoin présent ; `-y` toujours ; l'identifiant se lit dans `id-machine.txt`, jamais tapé (la garde refuse un
  autre identifiant, et dix machines d'autres tâches, dont B bis 60953606).
- **L9 (C8)** : la liste brute des instances (elle porte l'environnement d'autres machines) est effacée par son chemin exact
  après la preuve.
- **L10** : une machine dont l'amorce ne part pas n'a pas de minuterie : sans première poussée 20 minutes après la création,
  la mère regarde l'état ; à 30 minutes, destruction (geste 11).

## 4. Gestes exacts de l'opérateur

**Constantes à redonner en tête de chaque appel** (L1) :
`R=/home/user/controle-ia-travail ; W=$R/docs/procedures/machine-jeu-idee-1-1-v1 ; D=/home/user/jeu-idee-1-1-machine-envoi-v1 ;
V=/home/user/vastai-env/bin/vastai ; export PYTHON_JEU11=$R/.venv/bin/python VASTAI_JEU=$V ; C=<COMMIT> ; ER=<EMPREINTE_RELANCE> ;
FEU="R-<N> GO-<…>" ; GO=GO-<…> ; BR=calcul/idee-1-1-jeu-relance-v1`.
Règle générale : tout code ou toute sortie autre que l'attendu = **arrêt**, compte rendu à la mère, aucun rejeu, aucun
contournement. Jamais `env`, `printenv`, `set` sans argument, `export -p` ; jamais une valeur de clé à l'écran.

1. **Pièces, feu, état de départ.** `cd "$W" && for c in *.sha256; do sha256sum -c "$c"; done` → toutes `OK`. Puis
   `grep -c "^| R-<N> |" $R/registres/decisions.md` → `1` ; `git -C $R fetch origin refs/heads/main:refs/remotes/origin/main`
   (refspec) ; `bash $W/lancer_jeu_idee_1_1_machine_v1.sh creation $R "$FEU" $C 0` → `JEU11 CREATION PERMISE {…}` (plafond lu) ;
   `git -C $R ls-remote --exit-code origin refs/heads/$BR > /dev/null 2>&1; echo "sortie $?"` → `sortie 2`.
2. **Dossier d'envoi neuf** : `mkdir /home/user/jeu-idee-1-1-machine-envoi-v1; echo "code $?"` → `code 0` ; s'il existe :
   arrêt (R12 ; un `-v2` ne s'invente pas, mot de la mère).
3. **Inventaire d'avant** : `( umask 077; "$V" show instances --raw < /dev/null ) | bash $W/lancer_jeu_idee_1_1_machine_v1.sh
   inventaire > "$D/ids-avant.txt"; echo "codes ${PIPESTATUS[@]}"; cat "$D/ids-avant.txt"` → `codes 0 0` ; une ligne
   `<id> <étiquette>` par machine ; **aucune** étiquette `jeu-idee-1-1-relance-v1` ; au moins un témoin (58936096, 58936099 ou
   58936100). Sinon arrêt.
4. **Recherche, puis offre par la garde** : `( umask 077; "$V" search offers 'rentable=true reliability>=0.98
   cpu_cores_effective>=4 cpu_ram>=8 disk_space>=20 inet_down>=100 dph_total<=0.06' -o 'dph_total' --storage 20 --raw
   < /dev/null > "$D/recherche.json" ); echo "code $?"; wc -c "$D/recherche.json"` → `code 0`, fichier non vide. Puis
   `bash $W/lancer_jeu_idee_1_1_machine_v1.sh offre-depuis-recherche "$D/recherche.json" "$D/offre.json"` → une ligne par offre
   (acceptée, ou refusée avec ses motifs), puis `JEU11 OFFRE ECRITE … : offre <id>, <n> carte(s), amd64 …, prix garde
   <p ≤ 0,06> USD/h`. `JEU11 REFUS : aucune offre acceptée` : arrêt, compte rendu (la mère juge ; aucune borne ne se relâche
   sans feu neuf).
5. **Commande, sortie écrite, rien d'affiché** : `cd "$W" && ECH=$(( $(date +%s) + 49 * 3600 + 45 * 60 )) && bash
   lancer_jeu_idee_1_1_machine_v1.sh commande $R "$D/offre.json" $C $ER "$ECH" "$FEU" 0 python:3.13.18-bookworm "$D" $BR >
   "$D/commande-imprimee.txt"; echo "code $?"; wc -lc "$D/commande-imprimee.txt"; head -n 1 "$D/commande-imprimee.txt" | cut -c1-300` → `code 0`, **2** lignes, ≈ 12 100 octets, puis l'en-tête `JEU11 COMMANDE (…)` ; un refus s'y lit (`JEU11 REFUS : …`, première ligne seule, jamais le base64).
   Tout `JEU11 REFUS` : arrêt. L'heure compte dès ici : plus de 20 minutes avant le geste 8 → refaire ce geste dans
   `commande-imprimee-2.txt` (jamais écraser).
6. **Contrôle par programme** : `bash $W/lancer_jeu_idee_1_1_machine_v1.sh controle-ligne "$D/commande-imprimee.txt"` →
   `JEU11 LIGNE CONFORME : amorce décodée égale à l octet (<16 premiers caractères de l'empreinte de l'amorce>)`, puis la
   ligne, base64 masqué : `( umask 077; GO_ID=$GO /home/user/vastai-env/bin/vastai create instance <offre> --raw --image
   python:3.13.18-bookworm --disk 20 --cancel-unavail --label jeu-idee-1-1-relance-v1 --env "-e COMMIT=$C -e
   EMPREINTE_RELANCE=$ER -e ECHEANCE_UTC_S=<ECH> -e GO_ID=$GO -e BRANCHE_SORTIE=$BR -e GH_TOKEN=$GH_TOKEN" --entrypoint bash
   --args -c "echo <B64> | base64 -d | gunzip > /root/amorce_jeu_idee_1_1_v1.sh && bash /root/amorce_jeu_idee_1_1_v1.sh" <
   /dev/null > $D/reponse-creation.json ); python3 -I -c '…' $D/reponse-creation.json`. Vérifier chaque élément ; `$GH_TOKEN`
   en lettres. Autre : arrêt.
7. **Lecture en deux morceaux, copie, `cmp`** : `sed -n 2p "$D/commande-imprimee.txt" | cut -c1-6000` puis
   `sed -n 2p "$D/commande-imprimee.txt" | cut -c6001-` ; mis bout à bout sans un caractère de plus ni de moins, c'est la
   ligne. L'écrire par un appel à part (`cat > "$D/ligne-copiee.txt" <<'EOF'` … `EOF` ; le crochet exige le seul numéro de GO
   de la ligne, de type « calcul »), puis `cmp "$D/ligne-copiee.txt" <(sed -n 2p "$D/commande-imprimee.txt"); echo "cmp $?"` →
   `cmp 0`. Écart : arrêt ; ne jamais jouer une copie qui diffère.
8. **Jeu de la ligne, un seul appel, une seule fois** : `test -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" && export
   GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" &&` suivi de la ligne, **identique à l'octet**, rien d'autre (L7). Attendu :
   `JEU11 CREATION success True new_contract <id> cles [...]` (noms seulement). Premier refus d'une permission, du crochet ou du
   classifieur : arrêt, sans rejeu ni reformulation. Autre sortie : **ne pas rejouer** ; si `grep -c instance_api_key
   "$D/reponse-creation.json"` rend `0`, montrer `head -c 400 "$D/reponse-creation.json"` ; puis le geste 9 (une machine a pu
   être créée).
9. **Inventaire d'après, identifiant, prix relu** : `( umask 077; "$V" show instances --raw < /dev/null ) | bash
   $W/lancer_jeu_idee_1_1_machine_v1.sh inventaire > "$D/ids-apres.txt"; echo "codes ${PIPESTATUS[@]}"; diff "$D/ids-avant.txt"
   "$D/ids-apres.txt"` → exactement **une** ligne ajoutée `> <id> jeu-idee-1-1-relance-v1`, égale au `new_contract` ; une
   ligne retirée n'est admise que pour une machine dont la destruction est consignée par la mère (par exemple B bis). Puis
   `grep ' jeu-idee-1-1-relance-v1$' "$D/ids-apres.txt" | cut -d' ' -f1 > "$D/id-machine.txt"`. Prix :
   `( umask 077; "$V" show instance "$(cat "$D/id-machine.txt")" --raw < /dev/null ) | $R/.venv/bin/python -I -c 'import json,
   sys; d = json.load(sys.stdin); print(d.get("dph_total"), d.get("actual_status"), d.get("cpu_name"))'` puis `bash
   $W/lancer_jeu_idee_1_1_machine_v1.sh prix-relu <dph_total lu>` → `JEU11 PRIX RELU ACCEPTE` ; refus : destruction aussitôt
   (gestes 13 à 16), puis nœud.
10. **Rappel** : aucune seconde création, aucune relance sans feu neuf de la mère ; une relance n'est permise que si la
    première machine s'est arrêtée **avant le lancement du jeu** (code 2 au journal, aucun run commencé), sous une branche
    `…-v2` neuve (`BR`), et une seule.
11. **Surveillance** (par la mère, ou par un opérateur que le feu nomme et dont la tâche dure aussi longtemps que le jeu ; aucun rappel seul n'y suffit) : la première poussée paraît en quelques minutes : `git -C $R ls-remote origin refs/heads/$BR`. Puis, à
    chaque relève : `git -C $R fetch origin +refs/heads/$BR:refs/remotes/origin/$BR` et `git -C $R show
    refs/remotes/origin/$BR:traces/machine-jeu-idee-1-1-v1/etat.txt` ; `… :traces/machine-jeu-idee-1-1-v1/journal.txt | tail -n
    25`. Attendus : « contrôle des versions … « 3.13.18 2.4.6 1.17.1 » », « avant le jeu », « jeu lancé : PID … », puis un
    suivi par heure. **Aucune branche 20 minutes après la création** : `show instance` (état seulement) ; **30 minutes** :
    destruction (gestes 13 à 16), compte rendu (l'amorce n'est sans doute pas partie : aucune minuterie).
12. **Chaque heure, garde de dépense** : `bash $W/lancer_jeu_idee_1_1_machine_v1.sh depense $R $GO <CUMUL> <PRIX>` (point
    décimal ; `CUMUL` = heures depuis la création × prix relu) → `JEU11 DEPENSE {…}` ; code 2 : destruction. **Nœuds de la
    mère**, jamais de l'opérateur : projection de `etat.txt` au-delà de 172 800 s après au moins trois heures de jeu ; nombre de
    tranches inchangé sur trois suivis avec le PID vivant et une charge sous 0,5 (le « fils oisif » de l'addendum d'empreintes :
    sur la machine, le TERM par le PID n'est pas joignable depuis la session ; la destruction rendrait le run invalide sans
    `arret.json`) ; suivi absent deux heures de suite.
13. **Fin** : le journal porte « FIN » (code 0) ou « ARRET » (code 2 ou 4 ; sur « RESERVE : poussée des sorties impossible », ne **rien détruire** : nœud de la mère, qui décide de la copie depuis la machine vivante avant l'échéance), puis « fin de la machine, code … » et
    « « stopped » demandé ». La mère recopie d'abord les sorties (§ 2, « Après le jeu ») : `git -C $R archive
    refs/remotes/origin/$BR runs/<run> diag/organisme-idees-juge-v1/<run> | tar -x -C $R` (après `git -C $R fetch origin +refs/heads/$BR:refs/remotes/origin/$BR` ; `<run>` est le nom donné par la ligne « FIN : … run … » du journal ; refuser si l'un des deux dossiers existe déjà dans `$R`), puis chaque compagnon vérifié
    (`sha256sum -c` dans chaque dossier). Seulement ensuite : `bash $W/lancer_jeu_idee_1_1_machine_v1.sh detruire "$(cat
    "$D/id-machine.txt")" "$D" $GO` → `GO_ID=$GO /home/user/vastai-env/bin/vastai destroy instance <id> -y` ; la jouer telle
    quelle. Le code de sortie n'est jamais jugé.
14. **Témoin** : dans `( umask 077; "$V" show instances --raw < /dev/null ) | bash $W/lancer_jeu_idee_1_1_machine_v1.sh
    inventaire`, prendre dans l'ordre 58936096, 58936099, 58936100, présent aussi dans `ids-avant.txt` ; jamais l'identifiant
    de la machine du jeu.
15. **Preuve** (au moins 30 secondes après le geste 13) : `bash $W/lancer_jeu_idee_1_1_machine_v1.sh verifier-destruction
    "$(cat "$D/id-machine.txt")" <TEMOIN>` → `JEU11 DESTRUCTION PROUVEE …` ; « toujours listée » : refaire 13 puis 15 ; « témoin
    absent » : autre témoin ou nœud.
16. **Nettoyage** : effacer, par leurs chemins exacts, le dossier de liste brute imprimé au geste 15 et
    `$D/reponse-creation.json` (clé propre à la machine, sans valeur après la destruction). La mère relit l'inventaire :
    identifiant absent, les autres présentes ; ligne au registre des arrêts.

## 5. Ce que la procédure ne fait pas

- Elle ne lit aucun résultat ; elle ne compare pas le run neuf au run invalide (interdit, addendum de relance § 3).
- Elle ne se passe pas du réseau pendant le jeu : la machine pousse chaque heure `etat.txt` et le journal (comptes et dates de fichiers, jamais un contenu) vers la branche de sortie, hors du processus du jeu dont la garde réseau tient ; ces poussées et celle des sorties à la fin sont déclarées comme part de l'écart D7 (texte scellé l. 629), que le feu cite en toutes lettres.
- Elle n'emploie jamais `--reprendre` ; une machine perdue en cours de jeu rend le run invalide (relance seulement sous un
  addendum neuf).
- Elle ne garantit pas l'égalité au bit près sur un autre processeur (limite déclarée par l'addendum de relance, 4.2) : elle
  garde les versions, `lscpu` et `numpy.show_runtime()` dans les traces, pour la dire.

## 6. Contre-lecture

- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour1-v1.md` (même dossier), empreinte
  `09d345be856924f51eeadbeefa52003626a3004ddd79c7ba5cd471fb39ec10b3`, lecteur neuf (R2) ; verdict `corrections` (trois
  majeures, sept mineures, quatre remarques facultatives).
- **Cette version** : v2, écrite par un rédacteur neuf au moyen du programme de couples
  `appliquer_contre_lecture_procedure_tour1_v1.py` (même dossier), depuis la v1 `0d674c39dea0b4e264b59c3ff235903efe488c36ff8cd8b410166aa2bd4e04bc`.
  Seuls les couples qui portent sur cette pièce y sont appliqués ; ceux de l'amorce, du devis et du rapport attendent les
  versions suivantes de ces pièces (fichiers neufs, par leur auteur).
- **Réponse point par point** :
  - **M1** (poussée des sorties qui échoue) : couples 3 (§ 1, pas 7) et 4 (geste 13) appliqués. Couples 1 et 2 (amorce) et
    les deux cas de répétition demandés : hors de cette pièce, non appliqués ici. **Dépendance** : le pas 7 et le geste 13 de
    cette v2 décrivent la reprise de l'amorce v2 (pause de 5 × `PAUSE` = 300 s, jusqu'à `MARGE_TERM` = 1 200 s avant
    l'échéance : constantes de l'amorce v1, cohérentes avec « toutes les 5 minutes » et « 20 minutes ») ; l'amorce v1 ne la fait
    pas. Cette v2 ne part donc pas au feu avec l'amorce v1 : il faut l'amorce v2, sa répétition (les deux cas exigés) et une
    liste des pièces (en tête de la procédure) qui la nomme, dans la version suivante de cette procédure.
  - **M2** (échéance de la ligne de GO) : couple 6 appliqué (§ 2, point 4). Couple 5 (devis) hors de cette pièce : le
    « devis § 1 » que cite le texte neuf vaut pour le devis v2 qui portera la ligne d'échéance ; le devis v1 ne l'a pas.
  - **M3** (préalables périmés) : couples 7, 8, 9 et 10 appliqués (§ 2, points 1, 2 et 4). Faits revus à 21:41Z
    (`date -u`), en lecture seule : R-3016 et R-3017 présents à `registres/decisions.md` ; GO-2026-11-16-10 présent à
    `registres/go.md` ; à `HEAD`, compagnon d'une ligne `a692d50c…` de l'addendum de relance ; `14a0dfc5…` ancêtre de la
    référence locale `origin/main`, `e395dd47…`. Le « 21:3xZ » du couple 10 est gardé tel que le rapport l'écrit. Couple 11
    (devis) et réécriture du rapport : hors de cette pièce.
  - **m1** : couple 12 appliqué (geste 5). **m2** : couple 13 appliqué (geste 13). **m3** : couple 14 appliqué (geste 11).
    **m4** : couple 15 appliqué (§ 5). **m7** : couple 18 appliqué (en tête).
  - **m5, m6** (couples 16 et 17) : devis, hors de cette pièce, non appliqués ici.
  - **F1 à F4** : facultatives, non appliquées (seules les corrections exigées le sont). F2 (geste 8) et F4 (geste 9) portent
    sur cette pièce : laissées à l'auteur et à la mère.
  - **P1 à P6** : points pour la mère, hors du texte de la procédure ; rien n'y change ici.
- **Rien d'autre ne change** par rapport à la v1 : en tête (titre, statut, version), les couples ci-dessus et cette section.
